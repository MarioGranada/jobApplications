"""Contract rate calculator — Estonia, tax year 2027 (2026 rules carried forward).
Run: python3 calc_rates.py
All money in EUR. Edit ASSUMPTIONS to re-run scenarios."""

# ---------- ASSUMPTIONS ----------
INCOME_TAX = 0.22          # flat, kept at 22% for 2026 (24% hike cancelled)
BASIC_EXEMPTION = 700 * 12 # flat €700/month from 2026 (tax hump abolished)
SOCIAL_TAX = 0.33
UI_EMPLOYEE, UI_EMPLOYER = 0.016, 0.008
PILLAR2 = 0.02             # II pillar default 2% (you may have chosen 0/4/6%)
CIT_ON_PROFIT = 0.22       # 22/78 on net dividend == 22% of the profit distributed
KUUMAAR = 946              # min social-tax monthly base ASSUMED for 2027 (2026: €886; min wage €946 from Apr 2026)
SOCIAL_CAP_BASE = 10 * 12 * 946  # FIE social-tax base cap (10x min wage)

WORKDAYS_2027 = 254        # 261 weekdays − 7 Estonian public holidays on weekdays
VACATION_DAYS = 20         # ≈ 28 calendar days statutory leave
SICK_DAYS = 5
BILLABLE_DAYS = WORKDAYS_2027 - VACATION_DAYS - SICK_DAYS  # 229
HOURS_PER_DAY = 8

FIE_COSTS = 1200           # yearly deductible costs (laptop share, software, insurance)
OU_COSTS = 2400            # accountant (~€80/mo) + annual report + bank + misc

REF_GROSS_MONTH = 5000     # last Coursy salary (gross, taxed)
REF_ALLOWANCE = 150        # monthly utilities/WFH compensation, paid untaxed

# ---------- MODELS ----------
def employee_net_annual(gross_annual):
    ui = gross_annual * UI_EMPLOYEE
    p2 = gross_annual * PILLAR2
    it = max(0, gross_annual - ui - p2 - BASIC_EXEMPTION) * INCOME_TAX
    return gross_annual - ui - p2 - it

def individual(revenue):
    """Payroll employee of agency/EOR. Agency's total cost == revenue (apples-to-apples)."""
    gross = revenue / (1 + SOCIAL_TAX + UI_EMPLOYER)
    net = employee_net_annual(gross)
    return dict(net=net, taxes=revenue - net, gross_salary=gross)

def fie(revenue, costs=FIE_COSTS):
    profit = revenue - costs
    min_social = KUUMAAR * 12 * SOCIAL_TAX
    if profit * SOCIAL_TAX < min_social:
        base = profit; social = min_social
    else:
        base = min(profit / 1.33, SOCIAL_CAP_BASE); social = base * SOCIAL_TAX
    taxable_after_social = profit - social
    p2 = max(0, taxable_after_social) * PILLAR2
    it = max(0, taxable_after_social - p2 - BASIC_EXEMPTION) * INCOME_TAX
    net = profit - social - p2 - it
    return dict(net=net, taxes=social + p2 + it, social=social, income_tax=it, pillar2=p2)

def ou(revenue, costs=OU_COSTS, monthly_fee=KUUMAAR):
    """Board-member fee at the minimum social-tax base (keeps health insurance) + rest as dividends."""
    fee = monthly_fee * 12
    fee_cost = fee * (1 + SOCIAL_TAX)          # board fee: no unemployment insurance
    p2 = fee * PILLAR2
    it_fee = max(0, fee - p2 - BASIC_EXEMPTION) * INCOME_TAX
    fee_net = fee - p2 - it_fee
    profit = revenue - costs - fee_cost
    dividends_net = max(0, profit) * (1 - CIT_ON_PROFIT)
    net = fee_net + dividends_net
    return dict(net=net, taxes=revenue - costs - net, fee_net=fee_net, dividends_net=dividends_net,
                cit=max(0, profit) * CIT_ON_PROFIT)

def breakeven(model, target_net):
    lo, hi = 0, 400_000
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if model(mid)["net"] < target_net else (lo, mid)
    return hi

# ---------- REPORT ----------
if __name__ == "__main__":
    ref_gross = REF_GROSS_MONTH * 12
    g, a = REF_GROSS_MONTH, REF_ALLOWANCE
    ui, p2 = g*UI_EMPLOYEE, g*PILLAR2
    it = (g - ui - p2 - BASIC_EXEMPTION/12) * INCOME_TAX
    net_m = g - ui - p2 - it + a
    cost_m = g*(1+SOCIAL_TAX+UI_EMPLOYER) + a
    ref_gross, ref_net, ref_cost = g*12, net_m*12, cost_m*12
    print("COURSY MONTHLY BREAKDOWN")
    print(f"  Gross salary            {g:>9,.2f}")
    print(f"  + Social tax 33%        {g*SOCIAL_TAX:>9,.2f}  (pension 20% {g*.20:,.2f} / health 13% {g*.13:,.2f})")
    print(f"  + Employer UI 0.8%      {g*UI_EMPLOYER:>9,.2f}")
    print(f"  + WFH allowance (untaxed){a:>8,.2f}")
    print(f"  = Coursy total cost     {cost_m:>9,.2f}")
    print(f"  − Employee UI 1.6%      {ui:>9,.2f}")
    print(f"  − II pillar 2%          {p2:>9,.2f}")
    print(f"  − Income tax 22%        {it:>9,.2f}")
    print(f"  = Net paid out          {net_m:>9,.2f}  (salary {net_m-a:,.2f} + allowance {a:,.2f})")
    print(f"  State + pension took    {cost_m-net_m:>9,.2f}  ({1-net_m/cost_m:.1%} of cost)")
    print(f"Billable days: {BILLABLE_DAYS}")
    print(f"Yearly: gross {ref_gross:,.0f} | net {ref_net:,.0f} | cost {ref_cost:,.0f} "
          f"→ cost per worked day {ref_cost/BILLABLE_DAYS:,.0f}, per hour {ref_cost/BILLABLE_DAYS/HOURS_PER_DAY:,.1f}\n")

    print("Break-even day rate to match Coursy NET (no risk premium):")
    for name, m in [("Individual", individual), ("FIE", fie), ("OÜ", ou)]:
        r = breakeven(m, ref_net)
        print(f"  {name:10s} €{r/BILLABLE_DAYS:6.0f}/day  €{r/BILLABLE_DAYS/HOURS_PER_DAY:5.1f}/h")
    print()

    hdr = f"{'Day':>5} {'Hour':>6} {'Revenue':>9} | {'Indiv net':>10} {'FIE net':>10} {'OÜ net':>10} | {'Indiv/mo':>8} {'FIE/mo':>8} {'OÜ/mo':>8} | {'vs Coursy (OÜ)':>14}"
    print(hdr); print("-" * len(hdr))
    for day in (400, 450, 500, 550, 600, 650, 700):
        rev = day * BILLABLE_DAYS
        i, f, o = individual(rev)["net"], fie(rev)["net"], ou(rev)["net"]
        print(f"{day:>5} {day/HOURS_PER_DAY:>6.1f} {rev:>9,.0f} | {i:>10,.0f} {f:>10,.0f} {o:>10,.0f} | "
              f"{i/12:>8,.0f} {f/12:>8,.0f} {o/12:>8,.0f} | {o/ref_net-1:>+13.0%}")


# ---------- WATERFALL BENCHMARK ----------
def waterfall(day):
    rev = day * BILLABLE_DAYS
    print(f"\nWATERFALL @ €{day}/day × {BILLABLE_DAYS} days = €{rev:,.0f}/yr (€{rev/12:,.0f}/mo)")
    # Individual
    g = rev / (1 + SOCIAL_TAX + UI_EMPLOYER)
    st, uer = g*SOCIAL_TAX, g*UI_EMPLOYER
    uee, p2 = g*UI_EMPLOYEE, g*PILLAR2
    it = (g - uee - p2 - BASIC_EXEMPTION) * INCOME_TAX
    ind = [("Social tax 33%", st), ("Employer UI 0.8%", uer), ("= Gross salary", g),
           ("Employee UI 1.6%", uee), ("II pillar 2%", p2), ("Income tax 22%", it),
           ("= NET", g-uee-p2-it), ("I-pillar pension accrual (20% SOC)", g*.20)]
    # FIE
    prof = rev - FIE_COSTS
    base = min(prof/1.33, SOCIAL_CAP_BASE); fst = base*SOCIAL_TAX
    fp2 = (prof-fst)*PILLAR2; fit = (prof-fst-fp2-BASIC_EXEMPTION)*INCOME_TAX
    fie_ = [("Business costs", FIE_COSTS), ("= Profit", prof), ("Social tax (33% of profit/1.33)", fst),
            ("II pillar 2%", fp2), ("Income tax 22%", fit), ("= NET", prof-fst-fp2-fit),
            ("I-pillar pension accrual (20% SOC)", base*.20)]
    # OÜ
    fee = KUUMAAR*12; fst2 = fee*SOCIAL_TAX
    op = rev - OU_COSTS - fee - fst2; cit = op*CIT_ON_PROFIT
    fp22 = fee*PILLAR2; fit2 = (fee-fp22-BASIC_EXEMPTION)*INCOME_TAX
    ou_ = [("Company costs", OU_COSTS), ("Board fee gross", fee), ("Social tax on fee 33%", fst2),
           ("= Distributable profit", op), ("Corporate income tax 22%", cit), ("= Net dividends", op-cit),
           ("Fee: II pillar 2%", fp22), ("Fee: income tax 22%", fit2), ("= Fee net", fee-fp22-fit2),
           ("= NET (dividends + fee net)", op-cit+fee-fp22-fit2), ("I-pillar pension accrual (20% SOC)", fee*.20)]
    for name, rows in (("INDIVIDUAL", ind), ("FIE", fie_), ("OÜ", ou_)):
        print(f"  {name}")
        for k, v in rows:
            print(f"    {k:38s} {v:>11,.2f} {v/12:>10,.2f}")

if __name__ == "__main__":
    for d in (500, 550, 600):
        waterfall(d)

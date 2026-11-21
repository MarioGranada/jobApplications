# Contract rate analysis: Senior React Engineer, European bank (Auth team), until Dec 2027

_Prepared 16.11.2026. Rerun with `python3 calc_rates.py` after changing the assumptions._

## 1. Reference point: Coursy salary

**What Coursy paid for the role:**

From Coursy's total cost down to what reached your bank account:

| # | Step | Monthly | Yearly | Who receives it |
|---|---|---|---|---|
| 1 | **Total cost of your role to Coursy** | **€6,840.00** | **€82,080** | |
| 2 | − Utilities/WFH allowance (set aside, untaxed) | −€150.00 | −€1,800 | You (step 11) |
| 3 | **= Employer budget for salary + employer taxes** | €6,690.00 | €80,280 | |
| 4 | − Social tax 33% of gross (20% / 13%) | −€1,650.00 | −€19,800 | State: €1,000 to your state pension (I pillar), €650 to your health insurance (Haigekassa) |
| 5 | − Employer unemployment insurance 0.8% of gross | −€40.00 | −€480 | Töötukassa |
| 6 | **= Gross salary (contract figure)** | **€5,000.00** | **€60,000** | |
| 7 | − Employee unemployment insurance 1.6% | −€80.00 | −€960 | Töötukassa |
| 8 | − II pillar pension 2% | −€100.00 | −€1,200 | Your own pension fund |
| 9 | − Income tax = (gross − UI − II pillar − tax-free allowance) × 22%<br>monthly: (€5,000 − €80 − €100 − €700) × 22% = €4,120 × 22%<br>yearly: (€60,000 − €960 − €1,200 − €8,400) × 22% = €49,440 × 22% | −€906.40 | −€10,877 | State |
| 10 | **= Net salary** | €3,913.60 | €46,963 | You |
| 11 | + Utilities/WFH allowance (from step 2) | +€150.00 | +€1,800 | You |
| 12 | **= Net paid to you** | **€4,063.60** | **€48,763** | You |

**Where Coursy's €6,840 went each month:**

| Destination | Monthly | Yearly | Share of cost |
|---|---|---|---|
| Your bank account (net salary + allowance) | €4,063.60 | €48,763 | 59.4% |
| Your pensions (I pillar €1,000 + II pillar €100) | €1,100.00 | €13,200 | 16.1% |
| Income tax | €906.40 | €10,877 | 13.3% |
| Health insurance | €650.00 | €7,800 | 9.5% |
| Unemployment insurance (€40 + €80) | €120.00 | €1,440 | 1.8% |
| **Total** | **€6,840.00** | **€82,080** | **100%** |

Total taxes and contributions (steps 4, 5, 7, 8 and 9): **€2,776.40/month (€33,317/year)**.

- This matches your payslip (€4,063) exactly, which confirms a **2% II pillar** and that the €150 was paid untaxed.
- **Coursy spent €1.68 for every €1 you took home.** About 41% of the cost of your role went to the state and your pension funds. Of that, €1,100/month (the 2% II pillar plus the 20% pension part of social tax) was building your own pension.
- The €150 was a cost reimbursement, not salary. If Coursy had instead treated it as a taxed fringe benefit, it would have cost them about €256/month instead of €150. As a contractor, those home-office costs become **deductible business expenses** in an FIE or OÜ.
- **Cost per day actually worked:** €82,080 ÷ 229 = **€358/day (€44.8/h)**.

That salary also covered 28 days of paid holiday, paid sick leave, public holidays, notice period and severance, unemployment insurance and a laptop. A contractor pays for all of these themselves, which is why the rate has to sit well above the "salary ÷ days" figure.

## 2. Billable days (2027)

- 261 weekdays − 7 Estonian public holidays that fall on weekdays (1 Jan, 24 Feb, 26 Mar Good Friday, 23–24 Jun, 20 Aug, 24 Dec) = **254**
- − 20 days holiday − 5 sick days = **229 billable days** (8 h/day)

## 3. Break-even: the day rate that only matches Coursy's net

| Structure | Day | Hour |
|---|---|---|
| Individual (payroll) | €365 | €45.6 |
| FIE | €362 | €45.2 |
| OÜ | €290 | €36.3 |

**This is the floor, not the ask.** It includes no premium for risk, gaps between contracts, or lost benefits.

## 4. Net income per structure at different rates (229 days, gross rate excl. VAT)

| Day | Hour | Revenue | Individual net | FIE net | OÜ net* | OÜ /month | OÜ vs Coursy |
|---|---|---|---|---|---|---|---|
| €450 | €56 | €103,050 | €59,759 | €60,385 | €77,256 | €6,438 | +58% |
| €500 | €62.5 | €114,500 | €66,194 | €66,966 | €86,187 | €7,182 | +77% |
| €550 | €69 | €125,950 | €72,629 | €73,546 | €95,118 | €7,926 | +95% |
| **€600** | **€75** | **€137,400** | **€79,063** | **€80,127** | **€104,049** | **€8,671** | **+113%** |
| €650 | €81 | €148,850 | €85,498 | €86,708 | €112,980 | €9,415 | +132% |

\* OÜ net assumes everything is paid out as dividends. Money left inside the OÜ is not taxed until it is distributed.

## 4b. Benchmark at €600/day: from invoice to net, per structure

Revenue: €600 × 229 days = **€137,400/year (€11,450/month)**, the same for all three. Each table goes from the money the agency pays down to what reaches you, in the same order as the Coursy table.

### Individual (agency or EOR payroll; the €137,400 is the agency's total employer cost)

| # | Step | Monthly | Yearly |
|---|---|---|---|
| 1 | **Agency's total cost** | **€11,450.00** | **€137,400** |
| 2 | − Social tax 33% of gross | −€2,823.99 | −€33,888 |
| 3 | − Employer unemployment insurance 0.8% | −€68.46 | −€822 |
| 4 | **= Gross salary** | **€8,557.55** | **€102,691** |
| 5 | − Employee unemployment insurance 1.6% | −€136.92 | −€1,643 |
| 6 | − II pillar 2% | −€171.15 | −€2,054 |
| 7 | − Income tax 22% (after the €700 exemption) | −€1,660.88 | −€19,931 |
| 8 | **= Net to you** | **€6,588.59** | **€79,063** |

### FIE (sole proprietor)

| # | Step | Monthly | Yearly |
|---|---|---|---|
| 1 | **Invoiced** | **€11,450.00** | **€137,400** |
| 2 | − Business costs (laptop, software, insurance) | −€100.00 | −€1,200 |
| 3 | **= Business profit** | **€11,350.00** | **€136,200** |
| 4 | − Social tax 33% of (profit ÷ 1.33) | −€2,816.17 | −€33,794 |
| 5 | − II pillar 2% | −€170.68 | −€2,048 |
| 6 | − Income tax 22% (after the €700 exemption) | −€1,685.89 | −€20,231 |
| 7 | **= Net to you** | **€6,677.26** | **€80,127** |

### OÜ (Munbuh Corp OÜ as a B2B contractor: minimum board fee plus dividends)

**How the money moves**

```
Agency ──invoice (+VAT if applicable)──▶ Munbuh Corp OÜ bank account
                                              │
              ┌───────────────┬───────────────┼───────────────────────┐
              ▼               ▼               ▼                       ▼
        VAT to EMTA    Company costs    Board fee (monthly)    Profit (kept or distributed)
        (not yours)    (accountant…)    + social tax 33%       └─▶ dividend + CIT 22/78
                                              │                       │
                                              ▼                       ▼
                                    YOUR personal account ◀───────────┘
```

**Monthly / yearly, with formulas** (€600/day × 229 days; the monthly figures are a yearly average, since real invoices vary with working days per month)

| # | Step | Formula | Monthly | Yearly | Who receives it |
|---|---|---|---|---|---|
| 0 | VAT on the invoice | Foreign EU agency: reverse charge, so €0.<br>Estonian agency: +24% on top (€2,748/mo), collected and paid to EMTA by the 20th of the next month | (pass-through) | (pass-through) | State (never yours) |
| 1 | **Revenue invoiced (excl. VAT)** | €600 × 229 days | **€11,450.00** | **€137,400** | Munbuh |
| 2 | − Company costs | accountant ~€80, bank, annual report, insurance, software | −€200.00 | −€2,400 | Suppliers |
| 3 | − Board-member fee, gross | minimum social-tax base (2027 assumption €946) | −€946.00 | −€11,352 | You (steps 8–11) |
| 4 | − Social tax on the fee | €946 × 33% (no unemployment insurance on board fees) | −€312.18 | −€3,746 | State: €189.20 to your I-pillar pension, €122.98 to health insurance |
| 5 | **= Profit before CIT** | €11,450 − €200 − €946 − €312.18 | **€9,991.82** | **€119,902** | Munbuh |
| 6 | − Corporate income tax (only when paid out) | net dividend × 22/78, which equals profit × 22%<br>€7,793.62 × 22/78 = €2,198.20 | −€2,198.20 | −€26,378 | State |
| 7 | **= Net dividends to you** | profit × 78% = €9,991.82 × 0.78 | **€7,793.62** | **€93,523** | You (no further personal tax) |
| 8 | Board fee, gross | from step 3 | €946.00 | €11,352 | |
| 9 | − II pillar 2% | €946 × 2% | −€18.92 | −€227 | Your pension fund |
| 10 | − Income tax on the fee | (€946 − €18.92 − €700) × 22% = €227.08 × 22% | −€49.96 | −€600 | State |
| 11 | **= Board fee, net** | €946 − €18.92 − €49.96 | **€877.12** | **€10,525** | You |
| 12 | **= Net to you** | dividends €7,793.62 + fee €877.12 | **€8,670.74** | **€104,049** | You |

**Where the €11,450 goes each month**

| Destination | Monthly | Yearly | Share |
|---|---|---|---|
| Your bank account (dividends + net fee) | €8,670.74 | €104,049 | 75.7% |
| Corporate income tax | €2,198.20 | €26,378 | 19.2% |
| Company costs | €200.00 | €2,400 | 1.7% |
| Your pensions (I pillar €189.20 + II pillar €18.92) | €208.12 | €2,497 | 1.8% |
| Health insurance | €122.98 | €1,476 | 1.1% |
| Income tax on the fee | €49.96 | €600 | 0.4% |
| **Total** | **€11,450.00** | **€137,400** | **100%** |

**Rules and practical points**
- **CIT is only due when money leaves the company.** Anything you leave in Munbuh pays 0% tax until it is distributed. You decide when to pay it out, for example keeping 3–6 months of income as a buffer between contracts.
- **Dividends are not paid monthly.** An OÜ normally distributes profit based on its **approved annual report**. The 2027 annual report is due by 30 June 2028, so dividends from 2027 profit would normally be paid out from mid-2028. Retained earnings Munbuh already has from previous years can be distributed sooner. During 2027 you'd live on the board fee plus any existing retained earnings, or a higher board fee (see the next point). **Agree the cash-flow plan with your accountant before the first invoice.**
- **Moving money from dividends to board fee costs about 20 cents per euro.** €1 of company money keeps €0.78 as a dividend but only about €0.57 as board fee: (1 − 2% − 22% income tax) ÷ 1.33 social tax. A higher fee does build more state pension, and is the usual way to bridge 2027 until the first dividend.
- **You can't take money out any other way.** Personal spending paid by the company, or unreturned cash, counts as a hidden profit distribution and is taxed at 22/78 like a dividend. Loans from the OÜ to you have special tax rules, so ask your accountant first.
- **Genuine business costs are deductible and their VAT is reclaimable:** laptop, monitor, software, courses, coworking, liability insurance, and a documented share of home-office costs, which is what Coursy covered with its €150.
- **Cash calendar:** each month you invoice, the agency pays (often net 30), the company pays your board fee, and by the 10th of the next month the company files TSD and pays the tax on the fee (plus the KMD VAT return by the 20th if VAT-registered). Each year: annual report by 30 June, then any dividends with CIT declared on TSD and paid by the 10th of the month after the payout.

### Side by side

| | Individual | FIE | OÜ | Coursy (ref) |
|---|---|---|---|---|
| Revenue / cost of role per year | €137,400 | €137,400 | €137,400 | €82,080 |
| **Net per month** | **€6,589** | **€6,677** | **€8,671** | €4,064 |
| **Net per year** | **€79,063** | **€80,127** | **€104,049** | €48,763 |
| Share of revenue you keep | 57.5% | 58.3% | **75.7%** | 59.4% |
| Taxes + contributions per year | €58,337 | €56,073 | €30,951 | €33,317 |
| vs Coursy net | +62% | +64% | **+113%** | — |
| State pension (I pillar) accrual per year | €20,538 | €20,481 | €2,270 | €12,000 |
| Health insurance | ✅ | ✅ | ✅ (via the board fee) | ✅ |
| Unemployment insurance cover | ✅ | ❌ | ❌ (fee has no UI) | ✅ |
| Liability | Employer's | **Unlimited, personal** | Limited to the company | Employer's |
| Can keep money aside untaxed for gaps between contracts | ❌ | ❌ | ✅ | — |
| Deductible expenses / VAT reclaim | ❌ | ✅ | ✅ | — |
| Admin effort | None | Low | Medium (accountant) | None |

**Takeaways**
- The **OÜ nets about €25k more per year** than either alternative, roughly €2,000/month.
- **The OÜ's catch is pension.** The minimum fee builds about €2.3k/year of I-pillar entitlement against about €20.5k in the other two. You can close most of that gap by investing around €2–3k/year from the dividends in a III pillar fund or index fund, or by paying yourself a higher fee. Dividends have already been taxed in the company, so the III pillar income-tax deduction gives little extra benefit here. You'd still be far ahead.
- **FIE vs Individual is nearly a wash.** FIE is €1k/year better but carries unlimited personal liability and no unemployment cover, so there's little reason to choose it over the OÜ you already have.
- The same ranking holds at €500 and €550/day. Run `python3 calc_rates.py` for those waterfalls.

## 5. The three structures compared

### A) Individual: employment or service contract on the agency's (or an EOR's) payroll
- Taxed like a normal salary: 33.8% employer taxes, then 1.6% + 2% + 22% on your side. **About 42% of the agency's cost reaches you.**
- Above, "revenue" means the agency's total cost. If they pay your rate as *gross salary*, you net more, but they will lower the rate to cover the 33.8% on top.
- If the agency has no Estonian entity, they need an Employer-of-Record (Deel, Remote, …), whose fee usually comes out of your rate.
- Pros: no admin, full social cover, may count as employment for Töötukassa. Cons: worst net, no deductible expenses, and many agencies only contract B2B anyway.
- Note: you can't simply invoice a company as a private person in Estonia. Recurring paid services count as business income, so you need FIE or OÜ.

### B) FIE (sole proprietor)
- Social tax is 33% of profit ÷ 1.33 (about 24.8% effective), then II pillar 2%, then 22% income tax after the €8,400 exemption. **About 58% of profit reaches you.**
- Social tax is paid as quarterly advances, with a final settlement on the annual Form E.
- Pros: free and quick to register (e-Business Register), simple bookkeeping, full health insurance and pension accrual on the whole income.
- Cons: **unlimited personal liability**. A bank contract usually requires professional liability insurance, which is harder to buy as an FIE. No retained-earnings buffer, and all profit is taxed every year. Some agencies or banks refuse sole traders.
- Bottom line: at this income level FIE nets **almost the same as payroll**. It mainly makes sense if you don't want a company.

### C) OÜ (private limited company): recommended
- Assumed setup: a board-member fee at the minimum social-tax base (about €946/month, which keeps your health insurance) and the rest as dividends. Dividends carry 22% CIT (22/78 of the net dividend) and **no personal tax** after that. **About 76% of revenue reaches you.**
- Pros:
  - Best net by about €20–25k/year at €500–600/day.
  - Limited liability.
  - Profits can stay in the company **untaxed** to cover gaps between contracts. This is the real advantage for a freelancer.
  - Laptop, software, insurance, coworking and courses are deductible, and VAT can be reclaimed.
  - Agencies and banks expect a company.
- Cons:
  - Accountant (about €50–100/month), annual report, registration fee of about €265, mandatory VAT registration once turnover passes €40k.
  - A minimal salary means **minimal state pension (I pillar) accrual**. Compensate with voluntary III pillar contributions, or pay a higher salary.
  - Health insurance depends on keeping that minimum fee.
- VAT: quote rates **excluding VAT**. For an agency in another EU country it's reverse charge (no VAT on the invoice). For an Estonian agency, add 24%.

## 6. Recommendation

| | Day | Hour |
|---|---|---|
| **Ask (opening)** | **€600** | **€75** |
| Target landing | €550 | €69 |
| Walk-away floor | €480–500 | €60–62.5 |

Reasoning:
1. **Premium over break-even.** Contractors normally need +30–50% over their employee-equivalent cost to cover risk, bench time between contracts, no notice period and no severance. €365 × 1.35 ≈ €490, so that's the floor.
2. **Market.** Senior React/TypeScript contractors placed through agencies with European banks typically get **€500–700/day** remote from the Baltics/EU, and more if based in DACH/Nordics/UK. Bank budgets are higher, and the agency adds a 15–25% margin on top of your rate, so the bank is probably paying €650–800 for this seat.
3. **Long contract (~13 months).** That justifies a small discount from a short-gig rate, which is why €550 is the landing point rather than €600+.
4. **At €600/day through an OÜ you'd net about €8,670/month, roughly 2.1× Coursy's net (€4,063).** Even at the €500 floor it's about €7,180/month.

**How to phrase it:** "My rate is €600 per day (€75/hour) excluding VAT, invoiced through my Estonian company, for full-time remote work." Then ask about their budget, remote/onsite expectations, payment terms (aim for net-30 or better), notice/termination clause, and whether 1 day = 8 h.

## 7. Other things to sort out

- **Töötukassa:** you are eligible for unemployment insurance benefit (60% of your average wage for the first 100 days). Registering as unemployed generally conflicts with being an active FIE or an OÜ board member, so register as unemployed now and set up the company only when the contract is close to signing. Confirm the rules with Töötukassa.
- **II pillar:** the model uses 2%. If you chose 4% or 6%, or left the II pillar, the net figures shift slightly.
- **Requirements gap:** the posting stresses **Micro-frontends / Module Federation / Single-SPA** and **Vitest/Playwright**. The CV doesn't name these explicitly. If you have any experience with them (for example, the multi-platform design system at Yolo), add them to the CV before sending it. That will also make the €600 ask easier to defend.

## Assumptions and sources (verify before signing)

- 22% income tax and a flat €700/month exemption in 2026 ([EY, Dec 2025](https://taxnews.ey.com/news/2025-2446-estonia-significant-tax-changes-in-estonia-from-2026), [Grant Thornton](https://www.grantthornton.ee/en/insights1/overview-of-2025-2026-tax-changes/)). Assumed unchanged for 2027.
- The 2026–2028 2% defence/security tax was repealed in June 2025 ([ERR](https://news.err.ee/1609687289/estonia-scraps-defense-tax-makes-vat-rise-permanent), [EY](https://www.ey.com/en_gl/technical/tax-alerts/estonia-abolishes-temporary-defense-tax-increases-several-tax-rates)).
- FIE social tax rules, the ÷1.33 deduction and the €886 monthly base for 2026 ([EMTA: FIE social tax](https://www.emta.ee/ariklient/registreerimine-ettevotlus/ettevotjale/fuusilisest-isikust-ettevotjale-fie/sotsiaalmaks), [EMTA: II pillar](https://emta.ee/ariklient/registreerimine-ettevotlus/ettevotjale/fuusilisest-isikust-ettevotjale-fie/kohustuslik-kogumispensioni-makse)). **The €946 base for 2027 is an assumption.**
- Costs: FIE €1,200/year, OÜ €2,400/year. Market day rates are an estimate. Check them against a few recruiter conversations.

# Block Labs: relocation fit and contract type

_Prepared 2026-11-23 for the recruiter intro call (Thursday 26 Nov 2026, 11:00). The full relocation plan is in `spain/spain_relocation_dnv_context.md`. Spanish and Estonian tax figures are rough estimates to verify with a gestor before signing._

**Terms:** EOR = Employer of Record; PAC = *Profesional Altamente Cualificado*. Both are defined at the top of `rate/rate-analysis.md`.

## The company

- HQ in Sofia, founded in 2022, about 107 employees, iGaming. Hires remotely in several countries (Portugal among them).
- **Bulgaria is an EU member** (since 2007), fully in Schengen and on the euro since 1 Jan 2026. Block Labs therefore counts as an EU employer.
- The posting lists **"Málaga, Spain · Remote"**, so the seat itself is in Spain.
- Process: recruiter → hiring manager (30 min) → take-home or live coding → panel → technical reference → decision. They aim to finish within about 2 weeks of the intro call, so an offer could come around 10 Dec 2026.
- Every offer needs 2 HR references, one from each of the last 2 employers. Get the Coursy HR contact before 30 Nov.

## How each way of hiring fits the Spain plan

| How they hire | Fit | What it means |
|---|---|---|
| **Employee of the Bulgarian (or another non-Spanish EU) entity, remote from Spain** | ✅ Best | Matches the DNV primary track. The company is older than 1 year. File the UGE-CE notification within 30 days. Beckham (24%) stays open. |
| **Employee of a Spanish entity or a Spanish EOR** | ❌ Avoid | Counts as a Spanish employer, which COLELETEL doesn't allow. It would mean changing the visa (a PAC modification), so don't take this route. |
| **Contractor / B2B** | ❌ Avoid at this pay | Turns you into a Spanish *autónomo*, changes the DNV to self-employed, closes Beckham and nets less than Coursy (see below). |

**A1 correction:** a Bulgarian employer is unlikely to issue an A1, because a posting A1 needs prior insurance in Bulgaria and is meant for temporary postings (see "Starting immediately"). Expect Spanish Social Security instead: Block Labs registers as a foreign employer without a Spanish establishment, and you move to the public health system (SIP card). Estonian pillar contributions stop in either case.

**Tax:** under the Spain–Bulgaria tax treaty, salary for work done in Spain is taxed only in Spain. Give Block Labs a Spanish tax residency certificate so they don't withhold Bulgarian tax. Confirm with a gestor how Beckham payments work when the employer withholds nothing (Modelo 149, then Modelo 151).

## Salary asked: €6,250–7,050/month gross, read as an employee salary

Reference point: Coursy paid **€4,064/month net** (€48,763/year), from `rate/rate-analysis.md`.

| Gross/month (×12) | Spain employee + Beckham, net/month | vs Coursy | Estonia employee, net/month | Block Labs' cost, Spain | Block Labs' cost, Estonia |
|---|---|---|---|---|---|
| €6,250 (€75,000) | ≈ €4,420 | +9% | ≈ €4,850 | ≈ €7,900 | ≈ €8,360 |
| €6,650 (€79,800) | ≈ €4,720 | +16% | ≈ €5,150 | ≈ €8,300 | ≈ €8,900 |
| €7,050 (€84,600) | ≈ €5,030 | +24% | ≈ €5,460 | ≈ €8,700 | ≈ €9,430 |

Assumptions:
- Spain: employee Social Security 6.5% on the 2026 maximum base (≈ €5,101/month), then Beckham 24% on gross. The employer adds about 32% on that capped base.
- Estonia: the rates used in `rate/calc_rates.py` (1.6% UI, 2% II pillar, 22% income tax over a €700 allowance); the employer adds 33.8%.
- **Without Beckham**, the Spanish net is lower (progressive IRPF in the Valencian Community), so file Modelo 149 on time.
- Spain usually quotes **annual** gross, often paid in 14 instalments. Say "€75,000–85,000 gross per year" so the range can't be read as 14 × €6,250.

## Social security and pensions as an employee of the Bulgarian entity

EU rule (Regulation 883/2004): you're insured in **one** country at a time, the one you work in. Working from Spain means Spain, so **nothing is paid into the Estonian system any more**.

| | What happens |
|---|---|
| **Spanish Social Security** | Block Labs pays ≈ 31% and you pay ≈ 6.5% (on a capped base). It covers the Spanish pension, public healthcare (SIP card) and unemployment. |
| **Estonian I pillar (state pension)** | Your years in Estonia are kept. At retirement, Estonia pays its share for those years and Spain pays for the Spanish years. EU aggregation counts the Estonian years towards Spain's 15-year minimum. |
| **Estonian II pillar (funded)** | Contributions stop by themselves. The fund stays invested and is yours. Leave it; withdrawing early is taxed. |
| **Estonian III pillar** | You can still buy it through LHV, but the tax deduction is only for Estonian taxpayers. A plain index fund does the same job. |
| **Haigekassa (Estonian health)** | Ends after Coursy's grace period. During the Munbuh bridge, a board fee at the minimum base keeps it. Keep private insurance in Spain until the Spanish SS registration. |

**Staying in the Estonian system** would need an Article 16 exception agreed by both Sotsiaalkindlustusamet and Spain's TGSS, with Block Labs paying Estonian social tax. It's discretionary, slow and the opposite of frictionless, so don't ask for it.

## Why B2B at the same number doesn't work

If €6,250/month were a B2B invoice instead (€75,000/year):

- **As a Spanish autónomo:** RETA quota ≈ €530/month, then progressive IRPF with no Beckham, plus a gestor and quarterly filings (303, 130, 349). That leaves **about €3,900/month net, less than Coursy.**
- **Through Munbuh Corp OÜ:** the OÜ model in `rate/` only works while you live in Estonia. Once you live in Spain, the company is managed from Spain, so it would owe Spanish corporate tax, and its dividends would be taxed in Spain. The relocation plan already rules this out.
- A B2B rate has to cover what the employer would otherwise pay on top of salary (€7,900–8,700/month), **plus** the usual 30–50% contractor premium for no holidays, notice or sick pay. That puts the floor around **€480–500/day (~€10,000+/month)**, the same as the walk-away floor in `rate/rate-analysis.md`.

## What to ask for

**An employment contract (*contrato laboral* / payroll) with a non-Spanish Block Labs entity, registered in Spanish Social Security from your arrival on 23 Jan 2027, with a written letter authorizing remote work from Spain.** A Spanish entity or Spanish EOR is not an option, because it would require changing the visa.

If they only offer B2B: quote **€500/day excl. VAT** (or about €10,500/month) and say that €6,250–7,050 was a salary figure. Before accepting, check the self-employed DNV change with an immigration lawyer.

## If Block Labs only offers a contractor agreement ("pay your own taxes")

**Vehicle: a Spanish *autónomo* registration, not the FIE and not the OÜ.** Once you live and work in Spain:
- Spain taxes all of the income, because the work happens in Spain and there is no Estonian business presence. An Estonian FIE would give no tax benefit, only extra filings in two countries.
- Spanish self-employed Social Security (RETA) is mandatory regardless.
- Close any FIE when leaving Estonia, and keep Munbuh out of it (see above).

**Setup:**
- Register with Hacienda (Modelo 036/037) and the EU VAT register (ROI/VIES) so invoices to Bulgaria use reverse charge, with no Spanish VAT on them.
- Register in RETA. New autónomos usually get the *tarifa plana* (€80/month for the first 12 months); confirm you're eligible.
- Quarterly: Modelo 303 (VAT), 349 (EU invoices) and 130 (20% income-tax advance, because a foreign client doesn't withhold). Annual: the Renta return.
- Hire a gestor (about €100/month).

**Visa:** change the DNV from employee to self-employed through UGE-CE **before invoicing**. You'll need the service contract with Block Labs (founded 2022, so older than 1 year), proof of your degree or experience, and income above €3,917/month. Ask an immigration lawyer.

**Beckham:** not available, because it doesn't cover ordinary freelancing. Income tax is progressive (state + Valencian Community).

**Net per month as an autónomo** (rough: full RETA ≈ €590/month, gestor and €1,500/year of expenses, single filer):

| Invoice/month (×12) | ≈ Day rate (225 days) | Net/month | Net/month in year 1 with tarifa plana |
|---|---|---|---|
| €6,250 | €333 | ≈ €3,870 | ≈ €4,140 |
| €7,050 | €376 | ≈ €4,290 | ≈ €4,550 |
| €8,000 | €427 | ≈ €4,780 | ≈ €5,040 |
| €9,000 | €480 | ≈ €5,290 | ≈ €5,550 |
| €10,000 | €533 | ≈ €5,790 | ≈ €6,050 |

- Matching the **employee** midpoint (€6,650 gross, ≈ €4,720 net) takes an invoice of about **€8,000/month**. That's before any premium for no paid holidays, no notice period and no severance.
- **Ask: €500/day excl. VAT, or €10,000–10,500/month if they prefer a monthly fee.** Floor: €480/day (≈ €9,000/month). Below €8,000/month, take the employee contract instead.
- Contract terms to ask for: EUR, monthly invoicing, payment within 15–30 days, a mutual notice period (30 days or more), and clarity on whether holidays are paid.
- One full-time client who manages you like an employee looks like *falso autónomo* to a Spanish labour inspection. The risk falls mostly on the client, but it's one more reason to prefer employment.

### Why not a Spanish SL unipersonal (SLU) instead of a plain autónomo

Considered on 2026-11-23 and not recommended at this income:
- **Visa:** the DNV covers remote work for companies outside Spain. Working through your own Spanish company is a grey area that UGE-CE may not accept, so it could need a different permit. Ask an immigration lawyer before doing anything.
- **Social Security:** as the owner and director you still pay RETA (*autónomo societario*), so it doesn't replace being autónomo; it adds a company on top.
- **Tax:** corporate tax is 25% (lower rates for new and small companies), then your salary at progressive IRPF and dividends at 19–28%. For a one-person service company, Hacienda's safe-harbour rule expects you to pay yourself at least 75% of the profit as salary. That cancels most of the saving at €75–85k revenue.
- **Cost and admin:** notary and registry to set up, an accountant at €100–200/month, annual accounts and corporate-tax filings.
- **Beckham:** uncertain for an owner-director. It needs a specialist's confirmation.
- **The one real advantage:** Block Labs would keep paying invoices the whole time, with no switch to employment. It only becomes worth it if they insist on B2B **and** pay ≥ €500/day, or once you have several clients.

## Starting immediately (before arriving in Spain on 23 Jan 2027)

Mario is available to start immediately. Timeline: Estonia-based until 22 Jan, Alicante from 23 Jan 2027 (the Colombia weeks count as Estonia).

**Plan: a short contractor bridge, then employment from arrival.**

| Period | Contract | Why |
|---|---|---|
| Start date → 22 Jan 2027 (Estonia) | **B2B through Munbuh Corp OÜ**, invoicing monthly | Zero setup for Block Labs: they just pay an invoice. You're still Estonian, so the OÜ works normally for these weeks. No Spanish visa rules apply yet. |
| From 23 Jan 2027 (Alicante) | **Employee of the Bulgarian entity**, on Spanish Social Security (or a Bulgarian A1, see below) | Fits the DNV as issued. Notify UGE-CE within 30 days and file Beckham (Modelo 149) within 6 months of the Social Security registration. |

Bridge details:
- Rate: invoice the monthly figure (€6,250–7,050). That nets ≈ €4,600–5,200/month through the OÜ, which is fine for a few weeks.
- Töötukassa benefit stops once you work. Deregister when the contract is signed.
- Pay the bridge income out as a board fee in Dec 2026–Jan 2027, or keep it in the OÜ. Spain taxes dividends Munbuh pays you after you become Spanish-resident (19–28%). Ask the Xolo accountant.
- Keep Munbuh's role to the bridge only. It stops invoicing Block Labs when the employment contract starts.

**Option: employee of the Bulgarian entity from day one (simplest overall: one contract).** For the Estonia weeks, you pay the Estonian taxes yourself on Block Labs' behalf (EU Regulation 987/2009, Article 21(2)):

1. **Contract clause:** "The employee fulfils the employer's social security obligations in Estonia on its behalf. The employer pays the employer contributions on top of the gross salary."
2. **Block Labs pays monthly:** gross + 33.8% (at €6,250 gross: €6,250 + €2,112 = **€8,362**). Without the extra 33.8%, the employer share would come out of your gross.
3. **Block Labs registers with e-MTA as a non-resident employer** (required before you start) and enters you in the employment register (TÖR). Then it **authorises you in e-MTA** to file and pay on its behalf. e-MTA says an employee can't do this alone: "This must be done by the employer." Confirmed 2026-11-23 on [Income from employment](https://www.emta.ee/en/private-client/taxes-and-payment/taxable-income/income-employment), [Non-resident employer](https://www.emta.ee/en/business-client/registration-business/non-residents-e-residents/non-resident-employer) and [Social tax](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax) (Article 21 authorisation).
4. **By the 10th of each following month, file TSD and pay** (at €6,250 gross):

| Item | Rate | Amount |
|---|---|---|
| Social tax (employer share) | 33% | €2,062.50 |
| Unemployment insurance, employer | 0.8% | €50.00 |
| Unemployment insurance, employee | 1.6% | €100.00 |
| II pillar | 2% | €125.00 |
| Income tax | 22% after €700 allowance | €1,166.50 |
| **You keep** | | **≈ €4,858** |

- Income tax: a non-resident employer is a withholding agent, so it goes through the same monthly TSD. If it isn't withheld, you declare it in the annual return (table 5.1, part II) and pay it yourself. Set the 22% aside either way.
- No FIE or OÜ is needed for an employment contract; that rule applies only to service contracts.
- January 2027 salary: Estonia taxes the days worked there. Spain, where you're resident for 2027, credits that tax under the Estonia–Spain treaty. Ask the gestor.
- An Estonian accountant can file the monthly TSD for you.

**Bulgarian A1, in short:** an A1 is not automatic. A posting A1 needs at least 1 month of Bulgarian insurance before the posting, and it's meant for temporary postings (up to 24 months), not a permanent move. Without it, Block Labs registers in Spanish Social Security as a foreign employer without a Spanish establishment. Ask whether their payroll provider already does this for anyone in Spain.

**Autónomo:** only an option once you live in Spain. It needs a Spanish address (with the NIE you already have), Hacienda and RETA registration before the first invoice, and the DNV change to self-employed. That's why the bridge goes through Munbuh and the Spain part goes through employment.

## Order of topics in the recruiter call

1. Open as **based in Tallinn** (true until mid-December). Don't bring up Spain early.
2. At the end, when logistics, salary or contract come up, mention Spain in one or two lines. Don't let the call end without it: the contract type depends on it, and an Estonian setup (an Estonian EOR or payroll) would have to be redone in 6 weeks. The seat is listed as Málaga anyway, so this lowers friction rather than adding it.

   > "One practical note: I can start right away, invoicing through my Estonian company. From 23 January I'll be based in Spain, in Alicante, where I already hold residence for remote work, so there's no sponsorship involved. From then I'd just need an employment contract and a letter confirming I can work remotely from Spain."

3. Then ask:
   - Do they have an office or a Spanish entity in Málaga? Is the role fully remote from Alicante, or do they expect office days? (Alicante–Málaga is about 5 h by road.)
   - Which legal entity employs people based in Spain: Bulgarian, Portuguese, Spanish, or an EOR?
   - Employee or contractor?
   - Do they register Spain-based employees in Spanish Social Security and run their payroll?
   - Can they provide the contract, the remote-work letter and company registration documents for the immigration notification?
   - Can I start immediately as a contractor through my Estonian company, and switch to employment when I arrive in Spain on 23 Jan?

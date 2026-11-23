# Minimum salary: €4,400 net per month

_Set 2026-11-23. This is Mario's **absolute minimum take-home pay**. Any offer must reach it. The tables give the gross salary (or invoice) and the company cost needed for €4,400 net/month in each setup._

Reference: Coursy paid €4,064/month net (`rate/rate-analysis.md`). The minimum is 8% above that.

## Summary: what €4,400 net/month takes

| | **Employee** (gross salary) | **Own company** (invoice excl. VAT, break-even) |
|---|---|---|
| **Estonia** | **€5,650/month · €67,800/year** (company cost ≈ €7,560/month) | **OÜ: €6,000/month · €72,000/year** (≈ €315/day) |
| **Spain** | **€6,250/month · €75,000/year with Beckham** (company cost ≈ €7,900/month). Without Beckham: €6,800 · €81,600. | **SLU: €7,100/month · €85,000/year** (≈ €380/day). Plain autónomo: €7,300 · €87,600. |

- With your own company, the invoice **is** the company's cost: there are no employer contributions on top.
- Own-company figures only break even. The ask stays **€480–500/day**.
- In Spain, both own-company routes need the DNV changed to self-employed, and an SLU may not fit the DNV at all (see `jobs/Block_Labs-Staff_Software_Engineer_Frontend/relocation_and_contract.md`). The OÜ only works while you live in Estonia.

## Employee (salary)

Compare offers on the **annual** figure. Spanish salaries are often paid in 14 instalments, so a monthly figure alone can mislead.

| Setup | Minimum gross/month (×12) | Minimum gross/year | Company cost/month | Company cost/year |
|---|---|---|---|---|
| **Spain, with Beckham (24%)**: the Block Labs plan from 23 Jan 2027 | **€6,250** | **€75,000** | ≈ €7,900 | ≈ €94,500 |
| Spain, without Beckham (progressive IRPF, Valencian Community) | **€6,800** | **€81,600** | ≈ €8,450 | ≈ €101,000 |
| Estonia (until 22 Jan 2027, or an Estonian employer) | **€5,650** | **€67,800** | ≈ €7,560 | ≈ €90,700 |

- **The bottom of the €6,250–7,050 range asked from Block Labs is the floor.** With Beckham, €6,250 gross nets ≈ €4,418/month. Don't go below €75,000/year.
- If Beckham is refused or not filed in time (Modelo 149, within 6 months of the Spanish Social Security registration), the Spanish floor rises to €81,600/year.
- Spain company cost = gross + ≈ 32% employer Social Security on the capped base (≈ €5,101/month in 2026).
- Spain employee: 6.5% Social Security on the same capped base. Without Beckham: €2,000 standard deduction, single filer.
- Estonia company cost = gross × 1.338 (33% social tax + 0.8% unemployment insurance). Employee side: 1.6% unemployment insurance, 2% II pillar, 22% income tax over the €700/month allowance.

## Own company or contractor (invoice, excl. VAT)

These amounts only **break even** at €4,400 net. They include no premium for unpaid holidays, sick days, notice or gaps between contracts. The rate to ask for stays at **€480–500/day** (`rate/rate-analysis.md`, `jobs/Block_Labs-Staff_Software_Engineer_Frontend/relocation_and_contract.md`).

| Setup | Minimum invoice/month (×12) | Minimum invoice/year | ≈ Day rate |
|---|---|---|---|
| Spain, autónomo (full RETA ≈ €590/month, progressive IRPF, gestor and expenses) | **€7,300** | **€87,600** | €390 (225 days) |
| Spain, autónomo, year 1 with tarifa plana (€80/month) | €6,750 | €81,000 | €360 |
| Spain, **SLU** (owner-director; salary = 75% of profit, RETA ≈ €590/month, 15% corporate tax for a new company, dividends at 19–23%, gestor €200/month) | **€7,100** | **€85,000** | €380 (225 days) |
| Spain, SLU at the standard 2026 small-company rate (19% / 21%) | €7,200 | €86,100 | €385 |
| Estonia, Munbuh Corp OÜ (minimum board fee + dividends; until 22 Jan 2027 only) | **€6,000** | **€72,000** | €315 (229 days) |

- SLU: the 75% salary share follows Hacienda's safe-harbour rule for one-person service companies. Setup (notary, registry, about €1,000 one-off) isn't included. Beckham is assumed unavailable.
- Use the full-RETA figure as the Spanish autónomo floor, not the year-1 figure, because the tarifa plana ends after 12 months.
- The OÜ assumes all profit is paid out as dividends, which normally comes after the annual report (see `rate/rate-analysis.md`).

## Assumptions

All figures are monthly averages based on 2026 rates. They're estimates, so confirm them with a gestor (Spain) or an accountant (Estonia) before signing. Model: `rate/calc_rates.py` (Estonia) and the Spanish assumptions in `jobs/Block_Labs-Staff_Software_Engineer_Frontend/relocation_and_contract.md`.

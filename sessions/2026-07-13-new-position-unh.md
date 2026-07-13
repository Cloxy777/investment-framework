# NEW POSITION — UNH (UnitedHealth Group Incorporated, NYSE) — 2026-07-13

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6)
**Date:** 13 Jul 2026 (Monday)
**10Y US Treasury Yield:** 4.54% (FRED `DGS10`, most recent posted observation dated 2026-07-09, page shows "Updated: Jul 10, 2026" — normal 1-day FRED reporting lag) — recorded for completeness; not used, since this session stops at the Quality Gate (§4) before reaching the Rate Environment Gate.
**Current UNH portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is UNH's first-ever `/new-position` evaluation under this framework.
**Sector:** Healthcare — Managed Care / Health Insurance (UnitedHealthcare segment) + Health Services (Optum segment)
**Filer type:** US domestic filer — UnitedHealth Group reports on a standard US-GAAP calendar-year basis, CIK **731766**, filing Form 10-K (annual) and Form 10-Q (quarterly).
**First-use jargon decode:** see closing Glossary (§9).

---

## 0. Why this session exists — trigger source

A Telegram post on the **FinnInvestChannel** channel (post #2919, ~06:46 UTC 2026-07-13) said (translated from Ukrainian): *"Reports are starting 😎 ✅ This week: ASML, which makes chip-manufacturing machines ✅ UNH — a giant in medical insurance ✅ TSMC — makes almost all the most advanced chips ✅ Netflix, which has slid on slowing growth."* Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only, verified independently below. This is a generic earnings-calendar reminder naming four unrelated companies, not a specific analytical claim about UNH.

**Independent verification of the "reports this week" claim:** UnitedHealth Group **confirmed its Q2 2026 earnings release for Thursday, July 16, 2026, before market open**, with an 8:00 a.m. ET investor call — announced by the company on 2026-06-11 ([UnitedHealth Group newsroom](https://www.unitedhealthgroup.com/newsroom/2026/2026-06-11-uhg-announces-q2-earnings-release-date.html)) and independently corroborated by [Yahoo Finance](https://finance.yahoo.com/healthcare/articles/expect-unitedhealth-groups-q2-2026-093554304.html) and [stockanalysis.com](https://stockanalysis.com/stocks/unh/). **The trigger's claim is accurate** — UNH reports three days after this session.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$424.62** | Most recent **completed** regular-session close (Friday 2026-07-10), IBKR `get_price_snapshot` `prior-close` field (contract_id **13272**, NYSE, "UNITEDHEALTH GROUP INC", exact-symbol US primary listing confirmed via `search_contracts`) |
| Live pre-market tick (informational, not used) | $425.12 (+0.12% vs. $424.62) at 07:30:06 UTC 2026-07-13 (`is_close: false`) | IBKR `get_price_snapshot` `last` field. Session run at 08:10 UTC Monday — US regular session had not yet opened (opens 13:30 UTC / 9:30am ET); this is a thin, wide-spread (bid $424.50 / ask $427.99) pre-market print, only 0.12% above Friday's close — immaterial, not treated as the live price per Rule 0's "intraday, not a portfolio snapshot" standard, but confirms no material gap risk |
| Independent cross-check | **$424.62**, timestamped "July 10, 2026, 4:00 PM EDT" | [stockanalysis.com/stocks/unh](https://stockanalysis.com/stocks/unh/) — exact match to IBKR's prior close |
| 52-week range | $229.74 (low) – $434.26 (high) | IBKR `get_price_snapshot` `misc_statistics`; stockanalysis.com shows a very close $234.60–$434.30, both sources agree the stock is near its 52-week high |
| Dividend yield (live) | 2.11% (IBKR) vs. 2.08% (stockanalysis.com) | Both sources cross-check within 3bps |
| Analyst consensus PT | **$420.46** (27 analysts, "Buy") — essentially at, not above, the live price | stockanalysis.com `/forecast` page, dated this session |
| US 10Y Treasury yield | 4.54% | FRED `DGS10`, as-of 2026-07-09 |

**No staleness/discrepancy pattern found this session** (unlike the TSM session's one-session-stale `get_price_snapshot` `last` field) — IBKR's `prior-close` and stockanalysis.com's independently-reported timestamp/price match to the cent. **$424.62 is used as the live price for reference throughout this session** — no order-setup arithmetic is performed, since the Quality Gate fails below (§4).

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

All income-statement, balance-sheet, and cash-flow figures below are **primary-sourced** from UnitedHealth Group's own SEC filings: the FY2025 Form 10-K (filed 2026-03-02, accession 0000731766-26-000062) for FY2025/FY2024/FY2023 annual figures and the FY2025 year-end balance sheet; the Q1 2026 Form 10-Q (filed 2026-05-05, accession 0000731766-26-000127) for the Q1 2026 balance sheet and cash-flow comparatives; and the company's own quarterly earnings-release Exhibit 99.1/99.2 8-K filings (Q1 2025 through Q1 2026) for quarterly income-statement detail used in the trailing-twelve-month (TTM) reconstruction. Each is cited by exact SEC EDGAR URL below. Qualitative/market-structure evidence (DOJ investigation, CMS policy, PBM market share, Medicare Advantage enrollment) is vendor/press-sourced and cited individually, clearly flagged as such.

### 2.2 Quarterly income statement — primary-sourced (SEC EDGAR 8-K earnings releases)

| Quarter | Revenue ($M) | Medical Costs ($M) | Operating Costs ($M) | Cost of Products Sold ($M) | D&A ($M) | Total Op. Costs ($M) | Earnings from Ops ($M) | Interest Exp. ($M) | Pretax Income ($M) | Tax Provision ($M) | Net Earnings ($M) | Net Earnings, Common ($M) | Diluted EPS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 2025 | 109,575 | 73,411 | 13,594 | 12,390 | 1,061 | 100,456 | 9,119 | (998) | 8,106 | (1,632) | 6,474 | 6,292 | $6.85 |
| Q2 2025 | 111,616 | 78,585 | 13,778 | 13,019 | 1,084 | 106,466 | 5,150 | (1,027) | 4,082 | (510) | 3,572 | 3,406 | $3.74 |
| Q3 2025 | 113,161 | 79,958 | 15,223 | 12,566 | 1,099 | 108,846 | 4,315 | (1,003) | 3,229 | (686) | 2,543 | 2,348 | $2.59 |
| Q4 2025 | 113,215 | 82,041 | 16,997 | 12,680 | 1,117 | 112,835 | 380 | (974) | (720) | **938** (benefit) | 218 | 10 | $0.01 |
| Q1 2026 | 111,721 | 73,489 | 15,390 | 12,823 | 1,029 | 102,731 | 8,990 | (955) | 7,963 | (1,482) | 6,481 | 6,280 | $6.90 |

Sources: [Q1 2025 8-K](https://www.sec.gov/Archives/edgar/data/731766/000073176625000123/a2025q1exhibit991.htm) (via Q1 2026 comparative column, cross-cited), [Q2 2025 8-K](https://www.sec.gov/Archives/edgar/data/731766/000073176625000228/a2025q2exhibit991.htm), [Q3 2025 8-K](https://www.sec.gov/Archives/edgar/data/731766/000073176625000301/a2025q3exhibit991.htm), [Q4 2025 8-K](https://www.sec.gov/Archives/edgar/data/731766/000073176626000025/a991unherq42025.htm), [Q1 2026 8-K](https://www.sec.gov/Archives/edgar/data/0000731766/000073176626000121/uhgearningsreleaseq12026.htm). **Q4 2025's tax "provision" of +$938M is a net tax *benefit*** (pretax loss of −$720M becomes net earnings of +$218M) — see §3 for the one-time charge that drove this quarter's collapse.

### 2.3 TTM reconstruction (Q2 2025 + Q3 2025 + Q4 2025 + Q1 2026 — most recent four reported quarters; Q2 2026 not yet filed, reports 2026-07-16)

```
Revenue TTM            = 111,616 + 113,161 + 113,215 + 111,721 = 449,713
Medical Costs TTM       = 78,585 + 79,958 + 82,041 + 73,489     = 314,073
Operating Costs TTM     = 13,778 + 15,223 + 16,997 + 15,390     = 61,388
Cost of Products Sold TTM = 13,019 + 12,566 + 12,680 + 12,823   = 51,088
D&A TTM                 = 1,084 + 1,099 + 1,117 + 1,029         = 4,329
Total Op. Costs TTM     = 106,466+108,846+112,835+102,731       = 430,878  (cross-check: 314,073+61,388+51,088+4,329 = 430,878 ✓)
EBIT (Earnings from Ops) TTM = 5,150+4,315+380+8,990            = 18,835   (cross-check: 449,713−430,878 = 18,835 ✓)
Interest Expense TTM    = 1,027+1,003+974+955                   = 3,959
Pretax Income TTM       = 4,082+3,229+(−720)+7,963              = 14,554
Tax TTM (net)            = −510−686+938−1,482                   = −1,740  (net expense)
Net Earnings TTM         = 14,554 − 1,740                        = 12,814  (cross-check: 3,572+2,543+218+6,481 = 12,814 ✓)
Net Earnings, Common TTM = 3,406+2,348+10+6,280                  = 12,044
Diluted EPS TTM (summed) = 3.74+2.59+0.01+6.90                   = $13.24
Effective tax rate TTM   = 1,740/14,554                          = 11.96%  (unusually low — driven by Q4 2025's tax benefit; flagged, see §3)
```

### 2.4 Balance sheet — primary-sourced (Q1 2026 Form 10-Q, most current filed quarter)

| Item | Value ($M) | Source |
|---|---|---|
| Cash and cash equivalents | 28,001 | [10-Q balance sheet](https://www.sec.gov/Archives/edgar/data/0000731766/000073176626000127/unh-20260331.htm), XBRL-tagged [R2.htm](https://www.sec.gov/Archives/edgar/data/0000731766/000073176626000127/R2.htm) |
| Short-term borrowings + current maturities of LT debt (incl. $3.4B commercial paper as a disclosed subset, not additive) | 6,477 | same |
| Long-term debt, less current maturities | 71,440 | same |
| **Total debt** | **77,917** | 6,477 + 71,440 |
| Total equity (incl. $6,014M nonredeemable noncontrolling interests; UNH shareholders' equity alone $97,881M) | 103,895 | same |
| Total assets | 312,644 | same |

```
Net Debt = Total Debt − Cash = 77,917 − 28,001 = 49,916
```

### 2.5 Cash flow — primary-sourced (FY2025 10-K + Q1 2025/Q1 2026 10-Q comparatives)

| Period | Operating CF ($M) | CapEx ($M) | FCF ($M) |
|---|---|---|---|
| FY2023 | 29,068 | 3,386 | 25,682 |
| FY2024 | 24,204 | 3,499 | 20,705 |
| FY2025 | 19,697 | 3,622 | 16,075 |
| Q1 2025 | 5,456 | 898 | 4,558 |
| Q1 2026 | 8,912 | 763 | 8,149 |

Sources: [10-K cash flow statement, R9.htm](https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/R9.htm); [Q1 2026 10-Q cash flow statement, R6.htm](https://www.sec.gov/Archives/edgar/data/0000731766/000073176626000127/R6.htm) (which also carries the Q1 2025 comparative column).

```
TTM OCF   = FY2025 (19,697) − Q1 2025 (5,456) + Q1 2026 (8,912) = 23,153
TTM CapEx = FY2025 (3,622)  − Q1 2025 (898)   + Q1 2026 (763)   = 3,487
TTM FCF   = 23,153 − 3,487 = 19,666
```

### 2.6 Annual income statement, FY2023–FY2025 (primary-sourced, 10-K)

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Total Revenues ($M) | 371,622 | 400,278 | 447,567 |
| Medical Costs ($M) | 241,894 | 264,185 | 313,995 |
| Cost of Products Sold ($M) | 38,770 | 46,694 | 50,655 |
| Net Earnings, Common ($M) | 22,381 | 14,405 | 12,056 |
| Diluted EPS | $23.86 | $15.51 | $13.23 |

Source: [FY2025 10-K income statement, R5.htm](https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/R5.htm).

**FY2022 Revenue** (needed for 3yr CAGR): **$324,162M** — [UnitedHealth Group Reports 2022 Results, SEC 8-K](https://www.sec.gov/Archives/edgar/data/731766/000073176623000003/a2022q4exhibit991.htm).

```
Revenue 3yr CAGR (FY2022→FY2025) = (447,567/324,162)^(1/3) − 1 = 11.35%
```

---

## 3. Rule 9 Context — Why UNH's Trailing Financials Look the Way They Do (read before §4)

This section is placed ahead of the Quality Score because the numbers below cannot be read in isolation from what happened to UnitedHealth Group in 2025–2026 — a materially disclosed, still-unfolding sequence of events squarely inside this framework's Rule 9 fundamental-trigger categories (management change, guidance revision, macro/regulatory shift):

1. **CEO change (13 May 2025):** CEO Andrew Witty stepped down; Stephen J. Hemsley (CEO 2006–2017) returned as CEO, remaining Board Chairman; Witty stayed on as senior adviser. Announced the same day as the 2025 guidance suspension below. [UnitedHealth Group newsroom](https://www.unitedhealthgroup.com/newsroom/2025/2025-05-13-uhg-announces-leadership-transition.html), [CNBC](https://www.cnbc.com/2025/05/13/unitedhealth-group-ceo-andrew-witty-steps-down.html).
2. **2025 guidance suspended (13 May 2025), then re-established (29 July 2025):** UNH pulled its full-year 2025 outlook — issued less than a month earlier — citing medical costs running higher than expected; the stock fell as much as 17% intraday on the news ([Stocktwits/press coverage](https://stocktwits.com/news-articles/markets/equity/unitedhealth-suspends-2025-guidance-ceo-andrew-witty-resigns/chi8S4qRbZQ)). Guidance was re-established with Q2 2025 results ([company release](https://www.unitedhealthgroup.com/newsroom/2025/2025-07-29-unh-reestablishes-full-year-outlook-and-reports-second-quarter-2025-results.html)) — the same release disclosing a 430bps YoY jump in the medical care ratio to 89.4% and $1.2B of unfavorable discrete items.
3. **DOJ investigation (disclosed publicly ~24 July 2025, ongoing):** UnitedHealth Group is under **both criminal and civil** DOJ investigation into Medicare Advantage billing/risk-adjustment practices, with reporting indicating the probe extends to Optum Rx and physician-reimbursement practices. The company says it proactively contacted the DOJ and has launched a third-party billing-practices review; independent CMS audits are cited by the company as supporting its practices. **No findings, settlement, or charges have been reported as of this session — an open, unresolved allegation, tracked as a risk flag, never treated as a settled fact in either direction**, consistent with this framework's treatment of the FICO CID and Doximity securities-investigation precedents. [CNBC](https://www.cnbc.com/2025/07/24/unitedhealthcare-doj-investigation-medicare-billing.html), [FierceHealthcare](https://www.fiercehealthcare.com/payers/wsj-report-doj-interviewing-former-employees-about-medicare-billing-practices-unitedhealth), [Healthcare Finance News](https://www.healthcarefinancenews.com/news/unitedhealth-acknowledges-federal-probe-medicare-advantage-practices).
4. **Q4 2025 one-time charge ($1.6B net-of-tax, $1.78/share):** the primary driver of Q4 2025's near-total earnings collapse (Earnings from Operations $380M vs. ~$4-9B in every other quarter shown; Net Earnings to common $10M). Company-disclosed components: $799M direct cyberattack-remediation costs (from the 2024 Change Healthcare cyberattack), a $442M net gain on portfolio divestitures (partial offset), and $2.521B of restructuring/other charges (real-estate rationalization and workforce reductions $746M, loss-contract reserves on unprofitable Optum contracts $623M, contract reassessments $573M, net equity-securities valuation losses $329M, United Health Foundation advance funding $250M). Management describes this as "largely non-cash" and excluded from its own non-GAAP adjusted-EPS measure (Q4 2025 adjusted EPS $2.11 vs. GAAP $0.01). [Company release / SEC 8-K](https://www.sec.gov/Archives/edgar/data/731766/000073176626000025/a991unherq42025.htm), [AlphaStreet summary](https://news.alphastreet.com/unitedhealth-group-q4-2025-earnings-hit-by-one-time-charges-as-revenue-growth-continues-shares-slide-on-cautious-outlook/amp/).
5. **2026 guidance issued (26 Jan 2026) and Q1 2026 beat/raise:** FY2026 guidance was set at revenue >$439.0B, GAAP EPS >$17.10, adjusted EPS >$17.75. Q1 2026 results (reported 21 Apr 2026) beat expectations — medical care ratio improved 90bps YoY to 83.9%, net earnings to common of $6,280M (vs. $6,292M a year earlier, essentially flat) — and the company's own guidance commentary points to a 2026 recovery narrative. [Q1 2026 8-K](https://www.sec.gov/Archives/edgar/data/0000731766/000073176626000121/uhgearningsreleaseq12026.htm).

**Framework treatment:** this session's Quality Score is built on the **TTM window Q2 2025–Q1 2026** (§2.3) per the standard methodology — a window that captures three of the worst quarters in the company's recent history (Q2–Q4 2025) and only one recovering quarter (Q1 2026). Per Rule 6 ("normalize before you value") and this framework's consistent precedent of scoring off **filed GAAP figures, not company-adjusted non-GAAP metrics** (see the PepsiCo Core EPS, Stellantis AOI, and S&P Global Adjusted EBITDA treatments in [glossary.md](../framework/glossary.md)), **no adjustment is made to the GAAP TTM figures used below** — the one-time charge's effects are disclosed and discussed qualitatively (§6), not backed out of the scored inputs. This is a disclosed, deliberate methodological choice, not an oversight.

---

## 4. Phase 01 — Quality Score (2026-06-29 methodology)

### 4.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | FY2023: 25,682/22,381 = **114.7%** · FY2024: 20,705/14,405 = **143.7%** · FY2025: 16,075/12,056 = **133.3%** · TTM: 19,666/12,044 = **163.3%** | disqualify if 2+ consecutive years <70% | ✅ PASS, by a wide margin every year shown |
| Net Debt/EBITDA over threshold (2.5× standard — UNH does not qualify for the Upgrade 5 asset-light override; it is a risk-bearing insurer, not a payment network/exchange) | TTM: Net Debt $49,916M / EBITDA $23,164M (=EBIT $18,835M + D&A $4,329M) = **2.155×** | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years | FY2023 $25,682M · FY2024 $20,705M · FY2025 $16,075M — all positive (declining trend, still positive) | disqualify if not | ✅ PASS |

**No hard disqualifier fires.** UNH's problem, as the weighted score below shows, is not a balance-sheet or cash-flow-quality failure — its cash generation remains strong and its leverage remains under threshold — but a genuine, broad-based **profitability and margin deterioration** that the continuous weighted score is specifically designed to capture (this is exactly the kind of case the 2026-06-29 move from binary pass/fail to a graded 0–100.0 score was built for).

### 4.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (TTM, common) = 12,044 / 449,713 = 2.678%
  NetMargin_Component = clamp((2.678/30)×100, 0, 100) = 8.93

  NOPAT = EBIT_TTM × (1 − eff. tax rate) = 18,835 × (1 − 0.1196) = $16,581M
  Invested Capital = Total Debt + Total Equity − Cash (Q1 2026) = 77,917 + 103,895 − 28,001 = $153,811M
  ROIC = 16,581 / 153,811 = 10.78%
  ROIC_Component = clamp((10.78/30)×100, 0, 100) = 35.93

  Profitability_Score = (8.93 + 35.93) / 2 = 22.43   (no FCF-positivity cap — 3yr positive confirmed above)

MARGINS (15% weight):
  Gross Profit TTM = Revenue − Medical Costs − Cost of Products Sold = 449,713 − 314,073 − 51,088 = $84,552M
    [Judgment call, disclosed: UnitedHealth Group's income statement has no single "Cost of Revenue" line
     the way a product/software company does. This session treats Medical Costs (claims paid) and Cost of
     Products Sold (Optum Rx/product costs) as the direct cost-of-revenue analog — the core, volume-driven
     cost of delivering the insurance/PBM product — leaving Operating Costs (SG&A-like) and D&A below the
     line, consistent with how those items function economically. No framework precedent exists for a
     managed-care company; this construction is the most defensible reading of the existing formula, not
     an invented substitute metric, and is flagged for human review.]
  Gross Margin (TTM) = 84,552 / 449,713 = 18.80%
  GrossMargin_Score = clamp((18.80/80)×100, 0, 100) = 23.50

  3yr trend check: FY2023 GM = (371,622−241,894−38,770)/371,622 = 24.48%
                   FY2024 GM = (400,278−264,185−46,694)/400,278 = 22.33%
                   FY2025 GM = (447,567−313,995−50,655)/447,567 = 18.53%
  Trend is DECLINING (24.48% → 22.33% → 18.53%), not expanding — no +10 structural-trend bonus applies.
  This is itself a documented, quantified version of the "medical cost trend outrunning pricing" story (§3).

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022→FY2025) = 11.35%
  Growth_Score = clamp((11.35/25)×100, 0, 100) = 45.4
  Structural deceleration modifier: −10 applied. Documented evidence (not cyclical, multi-year policy-driven):
    (a) UnitedHealth Group itself attributes elevated 2025 medical costs partly to "the ongoing effects of the
        Biden-era Medicare funding reductions" (UNH's own Q3 2025 earnings release language, cited above);
    (b) UnitedHealthcare's own 2026 guidance is a *deliberate* Medicare Advantage membership reduction of
        1.3–1.4 million (up from an originally guided ~1 million), described by management as "prioritizing
        margin recovery... a deliberate trade-off on membership growth" (Becker's Hospital Review,
        "UnitedHealthcare's 'deliberate trade-off' for margin recovery"); a broader estimate put the total
        2026 MA membership decline as high as 2.8 million (Becker's Payer Issues);
    (c) UnitedHealth Group's own share of total US Medicare Advantage enrollment is reported falling from
        29% (2025) to 26% (2026), ~9.3 million enrollees (KFF, "Medicare Advantage in 2026: Enrollment
        Update and Key Trends," https://www.kff.org/medicare/medicare-advantage-in-2026-enrollment-update-and-key-trends/);
    (d) a live regulatory threat to a historical MA revenue-growth mechanism: CMS has proposed excluding
        "chart reviews" (retrospective diagnosis-code audits, estimated to have driven ~$24B of MA
        industry-wide overpayments in 2023 per MedPAC) from 2027 risk-adjustment scoring — a change
        "disproportionately affecting UnitedHealthcare" per Healthcare Dive's reporting, layered on top of
        the open DOJ risk-adjustment/"upcoding" investigation (§3).
  Growth_Score = clamp(45.4 − 10, 0, 100) = 35.4

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM) = 2.155×
  BalanceSheet_Score = clamp(100×(1 − 2.155/4), 0, 100) = 46.13

MOAT SIGNAL (15% weight) — checklist, cited evidence only:
  Market share stable/growing:  FALSE — documented DECLINE, not stability/growth: Medicare Advantage share
    29%→26% YoY (KFF, above) and a company-guided 1.3–2.8M enrollee loss in 2026 (Becker's, above).
  Brand premium (pricing power):  FALSE — the company's own central 2025 narrative is that its pricing
    structurally lagged its medical cost trend (§3) — the opposite of demonstrated pricing power; no
    evidence found of price increases sustained without volume/share loss.
  Network effect:  FALSE — no documented two-sided marketplace mechanism distinct from the scale/negotiating
    leverage credited below (not double-counted across two checklist rows, consistent with prior sessions'
    convention, e.g. the TSM session's treatment of foundry scale vs. switching costs).
  Switching costs:  FALSE — the only retention-rate citation found this session (large-employer "Uniprise"
    segment client retention of 97–99%) traces to old UnitedHealth Group SEC filings (search results
    returned FY2001/2009/2010-era 10-Ks for this specific figure) with no current, dated confirmation
    found this session — too stale to credit under this framework's "cited evidence" standard, especially
    during an active margin/regulatory crisis where retention dynamics may well have changed. Excluded
    rather than assumed, per "never invent or estimate."
  Scale cost advantage:  TRUE, with a caveat — Optum Rx is one of three pharmacy-benefit managers (with CVS
    Caremark and Cigna's Express Scripts) that together process ~80% of all US prescription-drug claims;
    Optum Rx alone processed ~1.659 billion adjusted claims in 2025, up from 1.623 billion in 2024
    (Drug Channels, "The Top Pharmacy Benefit Managers of 2025," https://www.drugchannels.net/2026/03/the-top-pharmacy-benefit-managers-of.html).
    This demonstrates genuine top-3 concentrated-market scale, credited here — though it falls short of a
    precise "cost-per-claim vs. smaller competitors" figure (the strictest reading of this checklist row's
    evidence bar), and is flagged as the weaker of this session's two considered scale citations; a second,
    Q4-2022-vintage medical-care-ratio peer comparison (UNH lower than Elevance/CVS-Aetna/Cigna) was found
    but excluded as evidence here for comparing across mismatched time periods against UNH's current TTM.
  Moat_Score = (1/5) × 100 = 20.0

FCF QUALITY (10% weight):
  FCF/NI (TTM) = 19,666/12,044 = 163.28%
  FCFQuality_Score = clamp(((1.6328 − 0.40)/0.60)×100, 0, 100) = clamp(205.5, 0, 100) = 100.0
  ⚠️ Flagged, not silently accepted at face value: this ratio is inflated by the Q4 2025 charge's
     depressing effect on the Net Income denominator (much of that $1.6B net charge was explicitly
     described by the company as "largely non-cash" — §3), not purely a sign of superior underlying cash
     conversion. A "clean" TTM substituting Q4 2025's own adjusted (non-GAAP) net earnings to common of
     roughly $1.9B (implied by adjusted EPS $2.11 × ~910M diluted shares) in place of GAAP's $10M would
     still yield FCF/NI comfortably above 100% (≈19,666/(12,044+1,910−10) ≈ 19,666/13,944 ≈ 141%) — so the
     100.0 sub-score is directionally correct even on a normalized basis, just less extremely so.

QUALITY SCORE = 22.43×0.25 + 23.50×0.15 + 35.4×0.20 + 46.13×0.15 + 20.0×0.15 + 100.0×0.10
             = 5.6075 + 3.525 + 7.08 + 6.9195 + 3.00 + 10.00
             = 36.13 → rounds to 36.1
```

**Robustness check (not just a point estimate):** even under a maximally generous, evidence-unsupported alternate reading crediting Growth_Score = 100.0 and Moat_Score = 100.0 (both far beyond what this session's citations support), the ceiling would be:

```
22.43×0.25 + 23.50×0.15 + 100×0.20 + 46.13×0.15 + 100×0.15 + 100×0.10
= 5.6075 + 3.525 + 20.00 + 6.9195 + 15.00 + 10.00 = 61.05
```

**Still well below the 80.0 gate.** The Profitability, Margins, and Balance Sheet sub-scores — all directly anchored to filed GAAP figures, not judgment calls — mathematically cap the maximum possible Quality Score at ~61.1, regardless of how the two more qualitative sub-scores (Growth, Moat) are read. **The gate-FAIL conclusion in §4.3 is not sensitive to this session's Moat/Growth judgment calls.**

### 4.3 Gate result

**Quality Score = 36.1 / 100.0 — FAILS the 80.0+ gate.** No hard disqualifier independently fires (§4.1) — this is a clean score-based failure, driven primarily by thin, GAAP-reported net margin (2.68%) and a returns profile (ROIC 10.78%) that, while not poor by insurance-industry standards, falls well short of this framework's Profitability sub-score calibration (which rewards margins more typical of asset-light software/consumer-brand businesses). Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md): **stop here — do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or fair-value/order-setup work.**

---

## 5. A Structural Caveat for Human Review (not a re-scoring, a flag)

This framework's Quality Score formula — Profitability weighted on Net Margin and ROIC against a 30% "saturation" ceiling (§ [quality-scoring.md](../framework/quality-scoring.md)) — was calibrated primarily against high-gross-margin, asset-light business models (the worked example in that file uses 18% net margin / 22% ROIC as a *mid-scoring* company). A **managed-care/health-insurance business model is structurally thin-margin by design** — premium revenue is mostly a pass-through of medical claims, and a 2–6% net margin is typical even for a well-run, market-leading insurer in a normal year (UNH's own FY2023 net margin, before this crisis, was ~6.0%; even that "clean" year would only lift NetMargin_Component to ~20.0, not enough by itself to flip the gate result). **This is analogous to the framework's already-documented finding that its standard Balance Sheet sub-score (Net Debt/EBITDA) "is not meaningful for a depository institution"** (see the CET1 glossary entries, cited from the 2026-07-12 BAC and C sessions) — a health insurer may be a comparable case where the framework's standard Profitability/Margins formulas don't map cleanly onto the business model's economics, even independent of UNH's own 2025 turmoil.

**This session does not adjust the formula or the score** — per "never invent or estimate," a sector-specific scoring adjustment for managed-care companies is not something this session is authorized to improvise. It is flagged here explicitly as a candidate framework-fit question for human review (parallel to the bank caveat), separate from and in addition to UNH's own company-specific 2025–2026 turmoil, which independently justifies a low score on its own terms (§3, §4.2).

---

## 6. Qualitative Notes

1. **The DOJ investigation (criminal + civil, Medicare Advantage billing/risk-adjustment practices, extending to Optum Rx and physician reimbursement) is open and unresolved** — treated as a risk flag, not a finding, consistent with this framework's standard for open regulatory/legal allegations (see the FICO CID and Doximity securities-investigation precedents in [glossary.md](../framework/glossary.md)). Its ultimate outcome (a manageable settlement vs. material fines/operational restrictions/forced Optum divestiture, per press reporting) is unknowable from here and was not assumed in either direction in this session's scoring.
2. **The Q4 2025 one-time charge ($1.6B net-of-tax) materially distorts this session's TTM window**, both directly (Q4 2025's near-zero reported profit) and indirectly (the artificially low 11.96% blended effective tax rate feeding NOPAT/ROIC, and the inflated-looking 163% FCF/NI ratio). This session scored off the GAAP figures as filed, per framework precedent (§3), and disclosed the distortions rather than silently adjusting for them.
3. **A genuine 2026 recovery narrative exists and should not be ignored**, even though it doesn't change this session's gate outcome: Q1 2026's medical care ratio improved 90bps YoY to 83.9%, the company issued 2026 guidance for adjusted EPS >$17.75 (well above 2025's $16.35), and Q1 2026 results were reported as a beat with a raised outlook. **None of this yet shows up in the TTM window scored here**, which is still dominated by three 2025 quarters. The next two quarters (Q2 2026, reporting 2026-07-16, and Q3 2026) will progressively roll the worst 2025 quarters out of the trailing window — this is the single most important thing to watch (§8).
4. **Two segments (UnitedHealthcare and Optum) with different economics are consolidated into one score.** Q1 2026 segment revenue: UnitedHealthcare $86,265M, Optum Health $24,109M, Optum Insight $5,125M, Optum Rx $35,736M (Total Optum $63,749M) — [Q1 2026 8-K](https://www.sec.gov/Archives/edgar/data/0000731766/000073176626000121/uhgearningsreleaseq12026.htm). This session did not attempt a segment-level sum-of-the-parts score; the consolidated GAAP figures are what this framework's methodology calls for.
5. **The best documented bear case, in the framework's own "5 Qualitative Questions" terms:** medical cost trend has structurally outrun UNH's own pricing across essentially all of 2025 (§3, §4.2 Margins), a core historical Medicare Advantage growth/margin mechanism (risk-adjustment-driven revenue) is under simultaneous DOJ investigation and CMS rulemaking threat (§4.2 Growth), and the company itself chose to shrink its largest single product line's membership by up to 2.8 million in 2026 rather than compete on price for volume — a rational margin-recovery move, but one this framework's Growth sub-score is specifically built to read as deceleration, not expansion.
6. **The Telegram trigger was accurate but analytically thin** — UNH's Q2 2026 earnings genuinely fall three days after this session (§0), but the post itself supplied no analysis beyond naming the ticker alongside ASML, TSM, and NFLX as part of a generic "earnings season starts this week" reminder.

---

## 7. Recommendation

# **PASS — Quality Gate FAIL (Quality Score 36.1 < 80.0). Do not enter.**

UnitedHealth Group does not clear this framework's strict 80.0+ Quality Score gate, and — per the robustness check in §4.2 — could not clear it even under an implausibly generous re-reading of this session's more judgment-based sub-scores (Growth, Moat), because its GAAP-anchored Profitability, Margins, and Balance Sheet sub-scores alone cap the maximum achievable score at ~61.1. No hard disqualifier independently fires; this is a clean, score-based failure driven by thin net margins (structurally typical of the managed-care business model, compounded by 2025's medical-cost-trend crisis) and a real, multi-source-documented growth deceleration (Medicare Advantage membership and share both declining, alongside an active DOJ risk-adjustment investigation). **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed — this session stops at the Quality Gate per the command specification.**

---

## 8. Next Review Trigger

- **UnitedHealth Group's Q2 2026 earnings, Thursday 16 July 2026** (three days after this session) — the next scheduled Rule 9 trigger. Specifically check whether the 2026 recovery trajectory (medical care ratio, adjusted EPS, and any Medicare Advantage membership/guidance update) continues, and whether the trailing GAAP net margin/ROIC meaningfully improve as 2025's worst quarters begin rolling out of the TTM window.
- **Any DOJ investigation development** — a settlement, formal charges, or a stated resolution timeline would be a material Rule 9 trigger requiring immediate re-score, in either direction.
- **CMS's 2027 Advance Notice / final risk-adjustment rule** (the proposed exclusion of chart reviews from MA risk scoring) — a confirmed final rule would be a direct, quantifiable input to a future Growth sub-score re-assessment.
- **FY2026 fiscal year-end close** (~Jan 2027 report) — the point at which FY2023's still-elevated year rolls out of the 3yr Revenue CAGR window and a full clean post-crisis annual figure becomes available for Profitability/Margins.
- Standard Rule 9 triggers: further management change, material M&A, a macro/rate shift, or a >15% unexplained price move.

**No position opened — nothing to log in `decisions/`.**

---

## 9. Glossary

- **CEO/management change (Rule 9)** — a documented trigger for mandatory re-valuation; UNH's 13 May 2025 CEO transition (Andrew Witty → Stephen Hemsley) is discussed in §3.
- **CIK (Central Index Key)** — the SEC's unique numeric identifier for UnitedHealth Group (731766), used to construct this session's EDGAR filing URLs.
- **CMS (Centers for Medicare & Medicaid Services)** — the US federal agency that administers Medicare, Medicaid, and the Medicare Advantage program, including setting annual per-member payment rates, publishing the risk-adjustment payment methodology, and awarding the annual Star Ratings that affect a plan's payment and marketing. UnitedHealth Group's 2025–2026 margin story is directly tied to CMS policy — the company itself cited "the ongoing effects of the Biden-era Medicare funding reductions" as a driver of its elevated 2025 medical care ratio, and its 2026 Medicare Advantage membership reduction was a direct response to CMS's funding trajectory. *(New term.)*
- **Composite Score** — this framework's blended 0.0–100.0 ranking (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`); **not computed this session**, since UNH's Quality Score (36.1) fails the 80.0+ gate before reaching this step.
- **D&A** — Depreciation & Amortization.
- **DOJ (Department of Justice)** — see §3; UNH's ongoing criminal and civil investigation into Medicare Advantage billing/risk-adjustment practices.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **EPS** — Earnings Per Share.
- **FCF / FCF Yield / FCF/NI conversion ratio** — Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check) — see §4.2's flag on why UNH's 163% ratio is partly an artifact of a depressed net-income denominator.
- **Hard disqualifier** — a Quality Score condition that fails a company regardless of weighted score; none fired for UNH (§4.1) — the company failed on weighted score alone.
- **Managed care** — a health-insurance model (Medicare Advantage, Medicaid managed care, employer-sponsored HMO/PPO plans) where a private insurer administers care and payment on a government program's or employer's behalf, in exchange for a fixed or risk-adjusted payment, as distinct from traditional fee-for-service insurance. UnitedHealthcare is the largest managed-care organization in the US by this measure. *(New term.)*
- **MCR (Medical Care Ratio) / MLR (Medical Loss Ratio)** — the percentage of premium revenue a health insurer pays out in medical claims (MCR is UnitedHealth Group's own term; MLR is the more common industry/regulatory term). Lower is generally better for underwriting margin. UNH's consolidated MCR swung from 71.1% (Q2 2025) to 89.9% (Q3 2025) to 89.1% (FY2025) before improving to 83.9% in Q1 2026 — the volatility central to this session's Margins finding. *(New term.)*
- **Medicare Advantage (MA)** — a privately-administered alternative to traditional government-run Medicare, in which CMS pays a private insurer a set, risk-adjusted amount per enrolled member, often bundled with supplemental benefits. UnitedHealth Group's largest single product line and the center of both its 2025 margin crisis and its DOJ investigation. *(New term.)*
- **NOPAT** — Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the numerator this framework uses to compute ROIC.
- **Optum** — UnitedHealth Group's health-services arm, split into three reporting segments: Optum Health (care delivery/value-based care), Optum Insight (data/analytics/software for providers and payers), and Optum Rx (pharmacy benefit management) — distinct from the UnitedHealthcare insurance segment. *(New term.)*
- **PBM (Pharmacy Benefit Manager)** — a company that administers prescription-drug benefits on behalf of health plans and employers, negotiating manufacturer rebates and pharmacy reimbursement rates. Three PBMs (CVS Caremark, Cigna's Express Scripts, UnitedHealth Group's Optum Rx) together process roughly 80% of US prescription-drug claims — cited as this session's Moat Signal "scale cost advantage" evidence. *(New term.)*
- **Quality Score** — this framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to reach Phase 02/Composite Score. UNH scored 36.1.
- **Risk adjustment / "upcoding" / "chart review"** — the CMS methodology that pays Medicare Advantage insurers more for enrollees coded with more/higher-severity diagnoses. "Chart review" is a retrospective audit of a member's record to identify additional billable diagnosis codes; congressional oversight (MedPAC) estimated chart reviews drove ~$24B of MA industry-wide overpayments in 2023. "Upcoding" is the disputed/alleged practice of coding more aggressively than a patient's condition supports to increase risk-adjusted payment — the central allegation in the DOJ's investigation of UNH (§3). *(New term.)*
- **ROIC / ROE** — Return on Invested Capital / Return on Equity.
- **Rule 0 / Rule 6 / Rule 9** — this framework's standing instructions to always fetch a live price first; normalize/strip out one-time items before valuing (not applied to the *scored* GAAP inputs this session, per framework precedent — see §3); and force re-valuation on specific fundamental triggers (management change, guidance revision, macro/regulatory shift, etc.).
- **Star Rating (CMS Star Rating)** — CMS's annual 1-to-5-star quality score for each Medicare Advantage plan, published each October, which affects a plan's CMS bonus payments and competitiveness. UnitedHealthcare guided ~78% of its MA membership into 4-star-or-above plans for 2026. *(New term.)*
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results; this session's TTM window is Q2 2025–Q1 2026 (§2.3).
- **XBRL (eXtensible Business Reporting Language)** — the structured, machine-readable format the SEC requires financial-statement figures to be tagged in, used this session to pull precise balance-sheet/cash-flow figures via the `R*.htm` report pages.

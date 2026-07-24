# New Position Evaluation — QCOM (Qualcomm Incorporated)

**Task type:** NEW POSITION
**Date:** 2026-07-24
**10Y US Treasury yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (see Section 3) before the Rate Environment Gate would otherwise apply (same precedent as the 2026-07-19 SCHW session).
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — a FinnInvestChannel post (FinnInvestChannel/2988, ~17:53 UTC 2026-07-24) discussing Qualcomm's chip business across smartphones, PCs, vehicles, smart devices, and data-center accelerators, with a general observation that "sentiment drives prices more than fundamentals in the short term" and that price was more attractive nearer a recent bottom. QCOM has **no prior watchlist entry anywhere** under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). A Phase 01 screening pass on 2026-07-07 ([sessions/2026-07-07-screening-na1.md](2026-07-07-screening-na1.md)) found QCOM FAILing the old binary pre-screen on Revenue 3yr CAGR alone (0.06%, essentially flat FY22→FY25) — but that was a screening pass-through under the pre-Quality-Score binary filter set, not a formal `/new-position` evaluation under the current 80.0+ Quality Score engine, and none of its figures are reused here without being re-fetched live. Per Rule 0, **no claim from the triggering post is used as a financial input anywhere below** — the post's framing (chip-business commentary, a "sentiment vs. fundamentals" observation, a "more attractive near the bottom" price comment) is not independently verifiable as a financial figure and is only the reason QCOM was looked at today; every number in this session was fetched fresh, independent of the post.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 273544, NASDAQ — "QUALCOMM INC") | **$167.24** | Last trade at ts 1784923390 (2026-07-24, US regular session), `is_close: false`, `halted: false` — a genuine live intraday print, not a stale/prior-close figure. |
| Day change (same snapshot) | **−$3.87 (−2.26%)** on the day | not used as a financial input — directional context only |
| Bid/ask | $166.61 / $167.02 | live NBBO at fetch time |
| 52-week range (IBKR `misc_statistics`) | low **$121.99** / high **$259.92** | 13-week, 26-week, and 52-week highs are all identical ($259.92), meaning that high was set within the trailing 13 weeks — current price is **~35.7% below** that recent high and **+37.1%** above the 52-week low. A large, real drawdown, shown here as context only; not itself a scoring input, and not the basis for any conclusion below (Rule 0 / "never act on price movement alone"). |
| Dividend yield (IBKR) | 2.1% | not used as a scoring input in this session (gate fails before any valuation-stage shareholder-yield component would matter) — shown for completeness. |
| Implied market cap (live price × ~1.05B shares out, per `stockanalysis.com`) | ~$175.6B | context only, not independently re-derived from a primary share-count filing this session. |

**Live price used throughout this session: $167.24.**

---

## 2. Data Source Note

Qualcomm Incorporated is a US SEC filer (**CIK 0000804328**, "QUALCOMM INC/DE", fiscal year ending late September). Fundamentals for this session were sourced from two places, cross-validated against each other:

- **`stockanalysis.com`** (`/stocks/QCOM/financials/`, `/financials/ratios/`, `/financials/balance-sheet/`, `/financials/cash-flow-statement/`, and the ticker overview page) — same fallback source used in the 2026-07-07 NA-1 screening session (yfinance/direct Yahoo access was blocked there by a TLS connection-reset error; not separately re-attempted this session given that established precedent).
- **SEC XBRL `companyconcept` API** (`data.sec.gov/api/xbrl/companyconcept/CIK0000804328/us-gaap/...`) — pulled directly to independently reconstruct trailing-twelve-month (TTM) Net Income, Operating Income (EBIT), pretax income, and income tax expense from the four most recent disclosed fiscal quarters (Q3 FY2025 through Q2 FY2026, the most recent filed 10-Q, period ended 2026-03-29). This was necessary because `stockanalysis.com`'s own TTM cash-flow-statement fetch returned an internally inconsistent, implausible figure (a nonsensical $53.3B TTM operating cash flow, roughly 4× the correct scale) on one fetch attempt — flagged and **not used**; the SEC XBRL reconstruction below is the figure of record wherever the two sources could conflict, and every quarterly SEC figure was cross-summed against `stockanalysis.com`'s own reported TTM total as an internal consistency check (all four checks — Net Income, Operating Income, Pretax Income, Revenue — reconciled exactly; see Section 3.2).
- **`data.sec.gov/submissions/CIK0000804328.json`** — confirmed CIK/company match.
- **Independent web search** (non-Telegram, non-trigger-post sources) — used only for the qualitative Growth-modifier and Moat-signal evidence in Section 3.2, each cited individually at the point of use.

No required Phase 01 input was invented, estimated, or inferred from the triggering post.

### 2.1 A note on two large, offsetting one-time tax items in the TTM window

Qualcomm's FY2025 Q4 (quarter ended 2025-09-28) results included a **$5.7B non-cash income-tax charge** to establish a valuation allowance against federal deferred tax assets, following the tax-reform provisions of the "One Big Beautiful Bill Act" (enacted 2025-07-04) — this alone drove a **$3.12B net loss** in that quarter despite normal operating performance (revenue $11.27B, operating income $2.92B). In FY2026 Q2 (quarter ended 2026-03-29), following IRS/Treasury Notice 2026-07, Qualcomm **fully reversed that same $5.7B valuation allowance** as a tax **benefit**, producing a **$7.37–7.41B net income** quarter on operating income of only $2.31B. [Sources: [CNBC, 2025-11-05](https://www.cnbc.com/2025/11/05/qualcomm-qcom-q4-2025-earnings-report.html); [StockTitan 10-Q recap](https://www.stocktitan.net/sec-filings/QCOM/10-q-qualcomm-inc-de-quarterly-earnings-report-3c0b90ab8861.html)]

Both quarters fall inside this session's TTM window (Q3 FY2025 → Q2 FY2026), so the **~$5.7B charge and ~$5.7B reversal are both included and roughly cancel out** — the TTM Net Income figure used throughout Section 3.2 ($9,923M, TTM Net Margin 22.31%) is consistent with QCOM's normal historical net-margin range (20.5%–29.4% across FY2021–FY2024) rather than being distorted upward or downward by the anomaly. This is confirmed directly: TTM Pretax Income ($11,702M) − TTM Tax Expense ($1,779M) = **$9,923M**, exactly matching the reported TTM Net Income independently sourced from `stockanalysis.com` — full reconciliation in Section 3.2. Flagged here rather than silently netted, per "show every calculation."

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | QCOM data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF (Operating Cash Flow − CapEx, `stockanalysis.com` annual cash-flow statement): FY2022 **$6,834M**, FY2023 **$9,849M**, FY2024 **$11,161M**, FY2025 **$12,820M**, TTM (through 2026-03-29) **$12,502M** — FCF-positive every year shown (5 of 5). | **PASS — does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | As of the most recent balance sheet (2026-03-29): Total debt = ST debt $498M + LT debt $14,772M = **$15,270M**. Liquid assets = Cash $5,435M + ST investments $4,364M = **$9,799M**. **Net debt = $15,270M − $9,799M = $5,471M**. TTM EBITDA (Section 3.2) = **$12,930M**. Net Debt/EBITDA = **0.42×**. | **PASS — well under threshold.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FCF/NI by year: FY2022 **52.83%** ($6,834M/$12,936M), FY2023 **136.2%**, FY2024 **110.0%**, FY2025 **231.4%** (net income mechanically depressed by the Q4 FY2025 tax charge — see §2.1), TTM **125.99%**. Only **one** year (FY2022) falls below 70% — not 2 consecutive years. | **PASS — does not fire.** |

No hard disqualifier fires. QCOM's outcome is decided entirely by the weighted score below, exactly as it was for the 2026-07-06 AAPL session.

### 3.2 Sub-scores (all six, per the weighted formula)

**TTM reconstruction (Q3 FY2025 → Q2 FY2026, the four most recent quarters through the most recently filed 10-Q, period ended 2026-03-29), sourced from SEC XBRL `companyconcept` and cross-checked against `stockanalysis.com`'s own reported TTM totals:**

| Line item ($M) | Q3 FY2025 (end 2025-06-29) | Q4 FY2025 (derived: FY2025 annual − 9mo) | Q1 FY2026 (end 2025-12-28) | Q2 FY2026 (end 2026-03-29) | **TTM total** | Cross-check vs. `stockanalysis.com` TTM |
|---|---|---|---|---|---|---|
| Revenue | 10,365 | 11,271 | 12,252 | 10,599 | **44,487** | 44,487 ✓ exact match |
| Operating Income (EBIT) | 2,762 | 2,918 | 3,366 | 2,309 | **11,355** | 11,355 ✓ exact match |
| Pretax Income | 2,952 | 2,971 | 3,547 | 2,232 | **11,702** | not separately reported by `stockanalysis.com`; internally consistent (see below) |
| Income Tax Expense (Benefit) | 286 | 6,088 | 543 | (5,138) | **1,779** | not separately reported by `stockanalysis.com`; internally consistent (see below) |
| Net Income | 2,666 | (3,117) | 3,004 | 7,370 | **9,923** | 9,923 ✓ exact match |
| D&A (quarterly, derived from cumulative YTD cash-flow tags) | 398 | 371 | 393 | 413 | **1,575** | FY2025 annual D&A $1,602M (close, consistent scale) |

(FY2025 Q4 and annual-tax-expense figures derived as FY2025-annual-10-K total minus the disclosed 9-month-YTD figure through Q3 FY2025, per line item — standard TTM reconstruction; every input is a directly-filed SEC XBRL figure. **Internal consistency check:** TTM Pretax Income $11,702M − TTM Tax Expense $1,779M = **$9,923M**, exactly matching TTM Net Income sourced independently from `stockanalysis.com` — full cross-validation, not a coincidence.)

TTM effective tax rate = $1,779M / $11,702M = **15.20%**. TTM EBITDA = $11,355M + $1,575M = **$12,930M**. TTM Gross Profit (per `stockanalysis.com`, cross-checked against Q-by-Q gross margin disclosures) = **$24,379M** (Gross Margin 54.80%).

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = 9,923/44,487 = **22.31%** → NetMargin_Component = clamp((22.31/30)×100) = **74.36**. ROIC = NOPAT/Invested Capital. NOPAT = TTM EBIT × (1 − effective tax rate) = 11,355 × (1−0.1520) = **$9,628.7M**. Invested Capital = Total Debt ($15,270M) + Equity ($27,278M, as of 2026-03-29) − liquid assets ($9,799M, same cash+ST-investments figure netted in the Balance Sheet row above) = **$32,749M**. ROIC = 9,628.7/32,749 = **29.40%** → ROIC_Component = clamp((29.40/30)×100) = **98.00**. Profitability_Score = (74.36+98.00)/2 = **86.18** (no FCF-positivity cap — 5 years positive). | **86.18** |
| **Margins (15%)** | Gross Margin (TTM) = 24,379/44,487 = **54.80%**. GrossMargin_Score = clamp((54.80/80)×100) = **68.50**. No +10 structural-trend bonus — that bonus only applies when gross margin is expanding *while still below* the 40% static threshold; QCOM's has been well above 40% throughout the lookback window (FY2021 57.51% → FY2025 55.43%, TTM 54.80% — a mild multi-year *decline*, not the kind of below-threshold expansion the bonus is designed for). | **68.50** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $44,200M → FY2025 $44,284M, both directly filed annual figures, via a sharp FY2023 dip ($35,820M, −19.0% YoY) and FY2024–FY2025 recovery (+8.8%, +13.7%)) = (44,284/44,200)^(1/3) − 1 = **+0.063%** → base = clamp((0.063/25)×100) = **0.25**. **Documented TAM-expansion evidence** (independently sourced, not from the trigger post): (1) Qualcomm's **automotive design-win pipeline reached $65B** and automotive revenue is on track to exit FY2026 at a **~$6B annualized run-rate** (target $10B by FY2029), per its June 2026 Investor Day [Futurum Group, 2026-06-24]; Q2 FY2026 automotive revenue itself grew **+38% YoY to $1.326B** and IoT grew **+9% YoY to $1.726B**, even as handset revenue fell −13% YoY [StockTitan Q2 FY2026 earnings recap]. (2) Qualcomm **entered the data-center AI-inference-accelerator market** with its AI200/AI250 chip line, announced 2025-10-27, targeting commercial availability in 2026/2027, with a disclosed ~200MW rack-system commitment from Saudi-backed Humain [SiliconANGLE, DataCenterDynamics, HPCwire, 2025-10-27/28]. This is a genuine, company-confirmed diversification away from a declining core handset business into three new/expanding revenue lines, not a cyclical bounce — **+10 applied**. Growth_Score = 0.25 + 10 = **10.25**. *Flagged judgment call, same category as the AAPL 2026-07-06 session's Services-mix call: a reasonable reader could argue for 0 instead of +10, since none of the three growth vectors (automotive, IoT, data-center AI) yet offsets the ~19% handset-driven FY2023 revenue collapse on a trailing basis, and the AI accelerator line has **zero** disclosed revenue to date. Sensitivity check below shows this call does not change the gate outcome either way.* | **10.25** |
| **Balance Sheet (15%)** | Net Debt/EBITDA (TTM, as of 2026-03-29) = $5,471M / $12,930M = **0.42×** (see 3.1). BalanceSheet_Score = clamp(100×(1−0.4231/4)) = clamp(89.42) = **89.42**. | **89.42** |
| **Moat Signal (15%)** | See evidence table below — **1 of 5 signals** cleared the cited-evidence bar. (1/5)×100 | **20.00** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 12,502/9,923 = **125.99%** → clamp(((1.2599−0.40)/0.60)×100) = clamp(143.3) = **100.0**. | **100.00** |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | **Conflicting evidence, not clearly established.** One 2026 source cites Qualcomm holding ~60% share of the *premium* non-Apple/Android smartphone-chip segment and ~60.1% of the broader Android chipset market. But a separate, more specific unit-volume comparison shows Qualcomm's overall 5G smartphone-chip share **declining** from 31.2% (1Q23) to 26.5% (1Q24) as MediaTek gained share (to ~38% overall unit share by Q3 2025, the current #1 by volume) — and Q2 FY2026 handset *revenue* itself fell −13% YoY (Section 3.2). Two different metrics point in different directions (premium-segment dominance vs. overall unit-share erosion); per the framework's "never invent — cite the specific evidence" standard, this is graded on the more concrete, sourced trend data (declining overall share, declining handset revenue) rather than resolved in Qualcomm's favor. | **FALSE** (conflicting; graded conservatively) |
| Brand premium | The clearest available data point this session — a reported "double-digit price increase due to rising costs" — is framed as a **cost pass-through**, not evidence of volume-loss-free pricing power from brand strength (the framework's actual evidentiary bar). No specific ASP-without-volume-loss or premium-vs-competitor pricing data was found and independently verified this session. | **FALSE** (insufficient evidence this session) |
| Network effect | No two-sided marketplace or user-growth-driven-value mechanism applies to a chip design/licensing business in the way it does for a platform/marketplace company; none found. | **FALSE** |
| Switching costs | **Well-documented mechanism.** Qualcomm's Standard-Essential Patent (SEP) portfolio underpins a "no license, no chips" model: device OEMs must pay Qualcomm a per-unit patent-licensing royalty **regardless of which company's chips they actually buy** — a practice the Ninth Circuit Court of Appeals found did not violate US antitrust law (2020, reversing an FTC v. Qualcomm district-court finding). This is a real, legally-tested, structural switching-cost/lock-in mechanism independent of Qualcomm's chip-market-share trend. | **TRUE** |
| Scale cost advantage | **Evidence points the other way.** MediaTek, not Qualcomm, now holds the larger unit-volume position (~38% global smartphone-SoC share by volume in Q3 2025 vs. Qualcomm's declining share, above), with 800M+ annual shipments — the framework's evidentiary bar here (cost-per-unit data showing a gap *in the subject company's favor*) is not met; Qualcomm's higher gross margin appears to reflect its premium-tier product mix rather than a documented per-unit cost-scale edge over a *smaller* competitor. | **FALSE** |

### 3.3 Final weighted Quality Score

```
Quality Score = (86.18 × 0.25) + (68.50 × 0.15) + (10.25 × 0.20) + (89.42 × 0.15) + (20.00 × 0.15) + (100.00 × 0.10)
              = 21.545 + 10.275 + 2.050 + 13.413 + 3.000 + 10.000
              = 60.283 → 60.3 (rounded to nearest 0.1)
```

**60.3 < 80.0 — fails the gate**, by **19.7 points** — a decisive miss, not a narrow one (contrast the 2026-07-06 AAPL session's 3.8-point near-miss). Two sub-scores are strong (Profitability 86.18, FCF Quality 100.0, and Balance Sheet 89.42 is solid), but **Growth (10.25)** and **Moat (20.00)** are both weak, and together with the middling Margins score (68.50) they pull the weighted total well below the bar.

**Sensitivity check (per the flagged judgment calls in 3.2):**
- **Growth modifier removed** (0 instead of +10): Quality Score = 60.283 − 2.05 = **58.2**. Still fails decisively.
- **Moat generously re-graded** (crediting 3 of 5 signals instead of 1, e.g. giving Qualcomm the benefit of the doubt on Market share and Brand premium despite the conflicting/thin evidence): Moat_Score = 60.0, contributing 9.0 instead of 3.0 → Quality Score = **66.3**. Still fails.
- **Maximally generous Moat** (all 5 of 5 signals credited, the theoretical ceiling): Moat_Score = 100.0, contributing 15.0 → Quality Score = **72.3**. **Still fails the 80.0 gate even under the single most generous defensible reading of every discretionary call in this session.**

**The Phase 01 FAIL outcome is robust to every discretionary call made in this session** — unlike the AAPL near-miss, no combination of reasonable judgment calls on the qualitative modifiers gets QCOM to 80.0.

### Result: **Phase 01 FAIL**

Per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md): a company scoring below 80.0 does not proceed to Phase 02. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**FAIL — does not clear the Quality Score gate.** No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that misses this framework's 80.0+ quality bar by nearly 20 points. No position is opened; no limit order is recommended.

This is a more clear-cut result than several recent near-miss sessions (AAPL, ADP). QCOM's core business remains solidly profitable (Profitability 86.18, driven by a genuinely strong 29.4% ROIC and 100.0 FCF Quality), and its balance sheet is conservative (0.42× Net Debt/EBITDA). But the framework's Quality Score is explicitly built to reward durable, moaty growth, and QCOM currently offers **essentially flat trailing revenue** (a 3-year CAGR of 0.06%, masking a sharp FY2023 handset-driven collapse and a FY2024–FY2025 recovery back to roughly the same absolute level) plus a **moat picture with only one clearly-documented signal** (patent-licensing switching costs) out of five — its historically dominant smartphone-chip position shows real, sourced signs of erosion to MediaTek in unit-volume terms even as its premium-segment position and diversification story (automotive, IoT, data-center AI) remain unproven at scale (the AI200/AI250 line has zero disclosed revenue to date). The triggering post's own framing — that "sentiment drives prices more than fundamentals in the short term" — is not something this framework acts on either way: Rule 9's non-negotiables explicitly exclude "price dropped on intact thesis" or "macro fear" as exit/entry triggers, and by the same logic, a large price decline alone (QCOM is ~35.7% below its own 52-week high) is not treated as a buying opportunity without the underlying quality bar being cleared first — which it is not, on the numbers pulled fresh this session.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mandatory Rule 9 re-check:** Qualcomm's fiscal Q3 2026 earnings, scheduled **2026-07-29** (5 days after this session) — a fresh quarter of data, and specifically worth watching for (a) whether the automotive/IoT growth trajectory continues, (b) any disclosed AI200/AI250 (data-center) revenue or bookings, and (c) further handset-revenue trend confirmation.
- **Mechanical trigger:** the Growth (10.25) and Moat (20.00) sub-scores are the dominant gaps to the 80.0 gate. The most direct paths to a materially different result: (1) a sustained multi-quarter revenue re-acceleration that lifts the trailing 3yr CAGR meaningfully above the current ~0%, most plausibly from automotive/IoT/data-center diversification continuing to outpace handset erosion; or (2) independently verifiable evidence resolving the Market-share signal in Qualcomm's favor (a data point showing stabilized-or-growing overall unit share, not just premium-segment share, would flip that signal to TRUE and add ~3 points).
- **Other Rule 9 events:** a guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause (note: QCOM's ~36% decline from its 52-week high is a known, already-priced move, not an unexplained one, so it does not itself constitute a fresh Rule 9 trigger).
- Absent any of the above, future Telegram mentions of QCOM should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **10-K (Annual Report)** — The annual financial-disclosure report a US public company must file with the SEC, containing full audited financial statements, MD&A, and risk factors.
- **10-Q (Quarterly Report)** — The quarterly financial-disclosure report filed between annual 10-Ks — used here to reconstruct trailing-twelve-month (TTM) figures through the most recently filed quarter.
- **ASP (Average Selling Price)** — The average price a company sells a unit of its product for — a pricing-power signal considered (but not established with sufficient evidence this session) for QCOM's Brand Premium moat-signal check.
- **CAGR (Compound Annual Growth Rate)** — The smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx (Capital Expenditure)** — Money a business spends on physical or capitalized long-lived assets.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every EDGAR filer (Qualcomm's is 0000804328) — used to construct this session's SEC XBRL/filing data-pull paths.
- **D&A (Depreciation & Amortization)** — A non-cash expense spreading the cost of long-lived assets over time.
- **Deferred tax valuation allowance release** — A one-off GAAP accounting event where a company reverses a prior write-down on its deferred tax assets. QCOM's case this session is the mirror image within the same trailing-twelve-month window: a $5.7B valuation-allowance *charge* in FY2025 Q4, fully *reversed* as a $5.7B benefit in FY2026 Q2 — the two roughly cancel out in the TTM figures used throughout Section 3.2 (see §2.1).
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **Effective tax rate** — The actual percentage of pretax income paid as tax in a period — used here to convert TTM EBIT into NOPAT for the ROIC calculation.
- **EPS (Earnings Per Share)** — Net income divided by number of shares outstanding.
- **FCF (Free Cash Flow)** — Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score — none fired for QCOM this session.
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. QCOM scores 60.3.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies eligible for valuation scoring. (QCOM does not make this list, this session.)
- **ROIC (Return on Invested Capital)** — How efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **SEP (Standard-Essential Patent)** — A patent covering technology unavoidably used by anyone implementing an industry standard; the basis of Qualcomm's "no license, no chips" model, credited as this session's one TRUE Moat Signal (switching costs).
- **TAM (Total Addressable Market)** — The total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not fetched this session, since Phase 01 failed first).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure — the basis used throughout this session's sub-scores.
- **XBRL (eXtensible Business Reporting Language)** — The SEC's structured, machine-readable data-tagging format for filed financial statements — the source of the independently-reconstructed TTM figures in Section 3.2, pulled via the SEC's `companyconcept` API.

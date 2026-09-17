# NEW POSITION — SAP SE (SAP.DE) — 2026-09-17

**Task type:** NEW POSITION
**Date:** 2026-09-17
**10Y US Treasury yield:** ~5.01% (2026-09-15/16, post-FOMC — [CNBC](https://www.cnbc.com/2026/09/16/treasury-yield-bond-market-fed-decision.html)) → Rate Regime Modifier would be **+10** (>5% band) *if* this name reached Phase 02 (it does not — see gate result below).
**Sector / Industry:** Technology / Software – Application (Enterprise Resource Planning)
**Duplicate-holding check:** `portfolio/holdings.md` reviewed in full — **no SAP or SAP.DE position exists** (ADR ticker SAP not present, XETRA ticker SAP.DE not present). No duplicate-entity flag needed for this session (unlike the earlier Novo Nordisk/NVO case in this run).

---

## 1. Live Price (Rule 0)

Fetched via `yfinance` (`yf.Ticker("SAP.DE").info`), not inferred from any multiple:

| Field | Value |
|---|---|
| Live price (SAP.DE, XETRA) | **€188.00** |
| Previous close | €186.56 |
| Currency | EUR |
| 52-week range | €127.50 – €244.30 |
| Market Cap | €216,990.4M |
| Enterprise Value | €214,146.5M |

---

## 2. Phase 01 — Quality Score (0–100.0)

All inputs sourced live via `yfinance` (`t.info`, `t.financials`, `t.quarterly_financials`, `t.cashflow`, `t.quarterly_cashflow`, `t.balance_sheet`, `t.quarterly_balance_sheet`) — no invented or estimated figures. TTM = trailing four reported quarters through 2026-06-30 (Q3'25, Q4'25, Q1'26, Q2'26).

### Raw data pulled

| Metric (TTM unless noted) | Value |
|---|---|
| Revenue | €38,193M |
| Gross Profit | €27,788M → **Gross Margin 72.76%** |
| EBIT | €11,612M |
| EBITDA | €12,876M |
| Net Income | €7,796M → **Net Margin 20.41%** |
| Pretax Income / Tax Provision | €11,052M / €3,116M → **effective tax rate 28.19%** |
| Free Cash Flow / Operating Cash Flow / CapEx | €8,730M / €9,465M / –€735M |
| **FCF/NI conversion ratio (TTM)** | **111.98%** |
| Total Debt (latest qtr, 2026-06-30) | €10,507M |
| Cash & equivalents (latest qtr) | €10,511M |
| **Net Debt (latest qtr)** | **–€4M (net cash)** |
| Stockholders' Equity (latest qtr) | €44,742M |
| Invested Capital (Debt + Equity – Cash) | €44,738M |

### Hard disqualifier checks (all evaluated on the current rolling window, per the 2026-08-05 clarification)

| Disqualifier | Window checked | Result |
|---|---|---|
| FCF/NI <70% for 2+ consecutive years (undocumented) | FY2022 208.8% / FY2023 89.0% / FY2024 141.2% / FY2025 117.5% / TTM 112.0% | ✅ Clear — never below 70% in any of the last 4 FYs or TTM |
| Net Debt/EBITDA over threshold (2.5×) | FY2022 0.63× / FY2023 0.09× / FY2024 0.16× / FY2025 –0.06× / latest qtr ≈ –0.0003× (net cash) | ✅ Clear — never remotely close to 2.5× |
| Not FCF-positive for 3+ consecutive years | FY2022 €4,770M / FY2023 €5,461M / FY2024 €4,410M / FY2025 €8,417M / TTM €8,730M | ✅ Clear — positive every year shown |

**No hard disqualifier fires.** The gate result below is driven entirely by the weighted sub-score total, not a disqualifier.

### Sub-scores (per [quality-scoring.md](../framework/quality-scoring.md))

**Profitability (25% weight)**
```
NetMargin_Component = clamp(20.41/30 × 100, 0, 100) = 68.03
ROIC_Component: NOPAT = EBIT × (1 − eff. tax rate) = 11,612 × (1 − 0.2819) = €8,340.6M
                ROIC  = NOPAT / Invested Capital = 8,340.6 / 44,738 = 18.65%
                ROIC_Component = clamp(18.65/30 × 100, 0, 100) = 62.17
Profitability_Score = (68.03 + 62.17) / 2 = 65.10   (no FCF cap — FCF-positive every year on record)
```

**Margins (15% weight)**
```
GrossMargin_Score = clamp(72.76/80 × 100, 0, 100) = 90.95
```
3yr trend check: FY2022 gross margin 72.77% → FY2025 72.86% — essentially flat (+0.1pp over 3 years), not a structural expansion. No +10 trend bonus applied (moot anyway — already well above the 40% bonus-eligibility threshold).

**Growth (20% weight)**
```
Revenue 3yr CAGR = (FY2025 Revenue / FY2022 Revenue)^(1/3) − 1 = (36,800 / 29,519)^(1/3) − 1 = 7.62%
Growth_Score_base = clamp(7.62/25 × 100, 0, 100) = 30.48
```
Documented TAM-expansion / pricing-power evidence (+10 applied):
- **Current Cloud Backlog** up 26–27% YoY to ~€22.9B in Q2 2026, outpacing recognized cloud revenue growth ([BigGo Finance](https://finance.biggo.com/news/US_SAP_2026-07-23), [ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/sap-stock-holds-gains-as-q2-2026-cloud-growth-and-backlog-support-outlook/70002165)).
- **Cloud ERP Suite** revenue (the RISE/GROW with SAP-driven figure) grew 27% at constant currencies and is now 88% of total cloud revenue ([saasrise.com](https://www.saasrise.com/news/sap-q2-cloud-revenue-jumps-22-to-68b-backlog-up-26-as-ai-acquisitions-trim-profit-outlook-968be6ae-5768-4e30-9899-d9338632115b)).
- New large migration wins named for the RISE/GROW programs in 2026: Shell, Morgan Stanley, Eli Lilly, Electrolux, Samsonite Group (same source).
- ~80% of SAP's legacy on-premise (ECC) customer base is now committed in some form to migrating to S/4HANA, ahead of ECC's mainstream-maintenance end date — a structural, forced up-sell wave into higher-value cloud contracts ([Morningstar](https://www.morningstar.com/stocks/sap-upgrading-moat-wide-raising-fair-value-by-76)).
```
Growth_Score = 30.48 + 10 = 40.48
```

**Balance Sheet (15% weight)**
```
Net Debt/EBITDA (latest quarter) = −4 / 12,876 ≈ −0.0003× (net cash position)
BalanceSheet_Score = clamp(100 × (1 − (−0.0003)/4), 0, 100) = 100.0 (clamped)
```

**Moat Signal (15% weight)** — checklist, cited evidence only, never inferred:

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable/growing | ✅ TRUE | SAP holds dominant global ERP market share; 41,523+ companies reported running SAP ERP as of 2026 ([6sense](https://6sense.com/tech/erp/sap-erp-market-share)). |
| Brand premium (pricing power) | ✅ TRUE | SAP has pushed through CPI-indexed annual support-fee increases (capped at 5%) again effective 1 Jan 2026, continuing the same policy from 1 Jan 2025, without evidence of resulting mass customer attrition — support base continues to grow support revenue even amid documented user-group pushback ([Computer Weekly](https://www.computerweekly.com/news/252524984/SAP-maintenance-fee-increase-What-you-need-to-know), [2Data](https://2-data.com/knowledge-hub/saps-annual-support-fee-increases-what-changed-what-it-means-for-2026-and-how-to-respond/)). |
| Network effect | ❌ FALSE | No documented two-sided-marketplace or user-growth-driven-value mechanism found for SAP's core ERP business — it is not a network-effect business model. |
| Switching costs | ✅ TRUE | Morningstar upgraded SAP's economic moat rating to **Wide** (from Narrow) explicitly citing switching costs, raising its fair value estimate 76% ([Morningstar](https://www.morningstar.com/stocks/sap-upgrading-moat-wide-raising-fair-value-by-76)); ~80% of the legacy on-premise base already committed to S/4HANA migration; replacing a live core ERP deployment is independently described as a multi-year, hundreds-of-millions-dollar re-engineering exercise with retention rates on core products cited above 99%. |
| Scale cost advantage | ❌ FALSE | Searches returned only generic commentary that the three large ERP/HCM vendors (SAP, Oracle, Workday) each have large R&D budgets vs. smaller players — no cited **cost-per-unit** data showing a specific, quantified gap vs. smaller competitors, which the framework requires for this signal. Not marked true absent that specific evidence. |

```
Moat_Score = (3 TRUE / 5) × 100 = 60.0
```

**FCF Quality (10% weight)**
```
FCFQuality_Score = clamp(((1.1198 − 0.40)/0.60) × 100, 0, 100) = clamp(119.97, 0, 100) = 100.0
```

### Final Quality Score

```
Quality Score = (65.10 × 0.25) + (90.95 × 0.15) + (40.48 × 0.20) + (100.0 × 0.15) + (60.0 × 0.15) + (100.0 × 0.10)
              = 16.275 + 13.6425 + 8.096 + 15.0 + 9.0 + 10.0
              = 72.0135 → rounds to 72.0
```

## Gate Result: **72.0 < 80.0 — FAILS the Quality Score gate.**

No individual hard disqualifier fired — SAP clears every one of the three non-negotiable balance-sheet/cash-flow tests comfortably (net cash position, FCF positive every year on record, FCF/NI conversion always well above 70%). The failure is a **weighted-average shortfall**, driven mainly by:

1. **Moat_Score (60.0)** — only 3 of 5 signals clear the "cited evidence" bar. Network effect doesn't apply to SAP's business model, and no specific cost-per-unit scale-advantage data was found (as distinct from generic "big vendors have big R&D budgets" commentary).
2. **Growth_Score (40.48)** — SAP's *overall* revenue growth (3yr CAGR 7.6%) is still a large, mature-company blend of a fast-growing cloud line and a declining on-premise license/maintenance base; even with the +10 documented-TAM-expansion bonus for the cloud migration wave, the base growth rate is well below the 25%-scale ceiling.
3. **Profitability_Score (65.10)** — solid (net margin 20.4%, ROIC 18.65%, both comfortably clearing the old Phase 01 >15% bars) but not top-tier on this framework's 0–100.0 continuous scale, which reserves scores near 100 for ~30% net-margin/ROIC businesses.

This is structurally the same pattern as the quality-scoring.md worked example (a candidate that clears every individual Phase 01 threshold but still lands below 80.0 on the weighted blend) — the strict gate is doing exactly what it was designed to do (see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md)).

**Per [.claude/commands/new-position.md](../.claude/commands/new-position.md) step 2 and [quality-scoring.md](../framework/quality-scoring.md): STOP HERE.** No Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work was performed for SAP.DE this session — a company below the 80.0+ gate is not eligible for Phase 02 regardless of how cheap it might otherwise look on FCF Yield/EV/EBIT/PE.

*(For context only, not a scored input: SAP's forward PE of 22.5× sits ~25% below its own 5-year average PE of ~30.0× (5yr range 13.9×–56.4×, reconstructed via `t.get_earnings_dates`), and the analyst consensus 12-month price target is ~€222.52 (39 analysts, consensus Buy) — both would ordinarily feed a Phase 02 valuation score, but the framework's own rule is that a Quality Score below 80.0 blocks that step entirely, so neither is scored here.)*

---

## 5. Recommendation

**PASS — do not proceed to valuation, do not open a position.** SAP.DE's Quality Score of 72.0 fails the strict 80.0+ gate (see [quality-scoring.md](../framework/quality-scoring.md)). This is a data-driven quality-gate fail, not a valuation call — SAP may look statistically cheap on some multiples, but the framework doesn't let cheapness rescue a company that hasn't cleared the quality bar. Held for the watchlist as a "Phase 01 (Quality) FAIL / not scored" entry; re-evaluate at the next `/rescore`-style pass if the qualitative moat evidence changes (e.g. concrete cost-per-unit scale data becomes available) or if a future quarter's growth/margin trend meaningfully improves the weighted total.

**Next review trigger:** Quarterly earnings (next report expected ~Jan 2027 for Q4/FY2026 results) per Rule 9, or sooner on a Rule 9 fundamental event (guidance revision, M&A, management change, macro shift, or >15% unexplained price move).

---

## Glossary

*(Every jargon term used above, pulled from [glossary.md](../framework/glossary.md); new terms added there this session are marked below.)*

- **ADR (American Depositary Receipt):** not used this session (SAP has a US ADR, ticker SAP, but this evaluation was run on the XETRA-listed SAP.DE ordinary share per the assignment).
- **CAGR (Compound Annual Growth Rate):** the smoothed yearly growth rate that gets you from a start value to an end value over several years — used here for SAP's 3-year revenue growth.
- **Cloud ERP Suite** *(new term, added this session)*: SAP's reporting line for cloud ERP revenue tied to S/4HANA Cloud and the RISE/GROW with SAP migration programs.
- **Current Cloud Backlog** *(new term, added this session)*: SAP's disclosed total value of contracted-but-not-yet-recognized cloud subscription revenue — a forward demand indicator.
- **EV/EBIT, EV/EBITDA:** Enterprise Value divided by EBIT or EBITDA — multiples comparing how expensive companies are relative to operating profit, independent of capital structure. (Referenced for context only — not scored this session.)
- **FCF/NI conversion ratio:** Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Forward PE:** Price ÷ next twelve months' expected earnings per share. (Referenced for context only — not scored this session.)
- **GAAP:** Generally Accepted Accounting Principles — the standard accounting rulebook; noted where SAP's own non-GAAP figures diverge from the filed GAAP/IFRS basis this framework scores off.
- **Gross Margin:** Gross Profit ÷ Revenue — one of this framework's Quality Score Margins sub-score inputs.
- **GROW with SAP** *(new term, added this session)*: SAP's packaged cloud-ERP offering for mid-market/greenfield customers, complementing RISE with SAP.
- **Hard disqualifier:** one of three Quality Score conditions that fails a company regardless of its weighted sub-score total — checked and cleared for SAP this session.
- **Invested Capital:** total capital (debt + equity, net of cash) put to work in a business — the denominator of ROIC.
- **Moat:** Warren Buffett's term for a durable competitive advantage protecting a business's profits from competitors.
- **Moat Signal:** this framework's 5-point Quality Score checklist (market share, brand premium, network effect, switching costs, scale cost advantage).
- **Net Debt/EBITDA:** net debt (total debt minus cash) divided by EBITDA — this framework's primary balance-sheet-risk gate.
- **Net Margin:** Net Income ÷ Revenue — one of this framework's Quality Score Profitability sub-score inputs.
- **NOPAT (Net Operating Profit After Tax):** EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **Quality Score:** this framework's 0.0–100.0 continuous score grading the Phase 01 criteria; a company must score 80.0+ to proceed to Phase 02 valuation scoring at all.
- **Rate Environment Gate:** the mandatory pre-check normally run before Phase 02 valuation scoring — not run this session because the Quality Score gate already failed.
- **RISE with SAP** *(new term, added this session)*: SAP's packaged offering for migrating an existing on-premise ERP customer to S/4HANA Cloud.
- **ROIC (Return on Invested Capital):** how efficiently a company turns capital invested in it into profit — a core Quality Score input.
- **S/4HANA** *(new term, added this session)*: SAP's current-generation ERP product, the mandatory eventual replacement for its legacy ECC ERP line.
- **Treasury yield (10Y):** the interest rate the US government pays on its 10-year bonds — the benchmark referenced (but not used to compute a score this session, since Phase 02 wasn't reached).
- **TTM (Trailing Twelve Months):** the most recent four reported quarters combined, used for this session's Net Margin, ROIC, FCF/NI, and FCF Yield inputs.

# NEW POSITION — PANW (Palo Alto Networks, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-09-07
**10Y US Treasury Yield:** 4.77% (FRED `DGS10`, 2026-09-03 print — most recent available; no update posted 2026-09-04/07, consistent with the 2026-09-07 US Labor Day market holiday)
**Rate Regime Modifier in effect:** N/A this session — Phase 02 not reached (see gate result below)
**Trigger:** [Telegram Stock-Mention Scan](../portfolio/snapshots/telegram-watch.md), `t.me/tarasguk` post `tarasguk/11861` (2026-09-07T19:39:49 UTC) — a video-preview post naming **$PANW** for upcoming analysis in the context of AI's impact on cybersecurity-sector valuations. No watchlist entry existed for PANW under either `in-portfolio/` or `not-in-portfolio/`, so per the Telegram-scan command's step 4 ("No watchlist entry exists at all → `/new-position`"), this triggered a full evaluation. The post itself supplied no financial data — all figures below are independently fetched live per Rule 0.

## Data gap flagged

Yahoo Finance's deep financial-statement endpoints (`quoteSummary` modules `incomeStatementHistory(Quarterly)`, `balanceSheetHistory(Quarterly)`, `cashflowStatementHistory`, and the `fundamentals-timeseries` endpoint) now return only `totalRevenue`/`netIncome` (or, for `fundamentals-timeseries`, nothing at all) for every line item tested — including on AAPL as a sanity check — regardless of a valid session cookie + crumb (obtained live this session via `fc.yahoo.com` → `query2.finance.yahoo.com/v1/test/getcrumb`, which restores access to the `quoteSummary` modules that were fully crumb-gated in the prior 2026-09-07 APP session). This means **precise EBIT-level effective tax rate, and a component-by-component invested-capital figure, are not directly obtainable** from any reachable source this session. Per CLAUDE.md Rule 0, this is flagged rather than estimated — see the Profitability sub-score below, which instead derives a mathematically-sound **upper bound** on ROIC from the TTM figures that *are* directly disclosed (`financialData.operatingMargins`, `totalRevenue`, `totalDebt`, `totalCash`, `defaultKeyStatistics.bookValue` × `sharesOutstanding`), and shows the gate conclusion is robust to that gap (see below). **No auto-commit is being skipped as a result** — the bound is tight enough that the gate result is not in doubt regardless of the true tax rate, so this session proceeds to a definitive Phase 01 conclusion rather than stopping.

## Live price (Rule 0)

Fetched via Yahoo Finance's `v8/finance/chart` endpoint (no crumb required) and cross-checked against `quoteSummary.financialData.currentPrice`, both consistent:

- **Last price: $333.26** (regular-session close 2026-09-04 — Friday — the most recent completed session; 2026-09-07 is a US market holiday, Labor Day, so no fresher print exists)
- Prior close (2026-09-03): $331.94 (+0.40%)
- Day range that session: $328.00–$339.00
- 52-week range: $139.57–$398.88

## Sector

Cybersecurity — network security, cloud security (Prisma Cloud), and AI-driven security operations (XSIAM/Cortex), pursuing a "platformization" consolidation strategy.

## Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md))

All inputs TTM (period ending 2026-07-31, PANW's fiscal Q4/FY2026 close — Yahoo's TTM-aggregated `financialData` fields already reflect this quarter even though the standalone quarterly statement history has not yet been repopulated for it):

| Input | Value | Source |
|---|---|---|
| Net Margin (TTM) | 2.674% | `financialData.profitMargins` (Net Income $307.0M ÷ Revenue $11,480.0M) |
| Operating Margin (TTM) | 5.044% | `financialData.operatingMargins` |
| Gross Margin (TTM) | 70.49% | `financialData.grossMargins` |
| Revenue 3yr CAGR | 18.54% | FY2023 revenue $6,892.7M → TTM/FY2026 revenue $11,480.0M (`incomeStatementHistory` FY2023 line ÷ `financialData.totalRevenue`), (11,480.0/6,892.7)^(1/3) − 1 |
| Total Debt | $2,500.0M | `financialData.totalDebt` |
| Total Cash | $3,071.0M | `financialData.totalCash` |
| Net Debt | **−$571.0M** (net cash) | Total Debt − Total Cash |
| EBITDA (TTM) | $1,861.0M | `financialData.ebitda` |
| Free Cash Flow (TTM) | $4,469.55M | `financialData.freeCashflow` |
| Book value of equity (proxy) | ≈$27,736.1M | `defaultKeyStatistics.bookValue` ($34.032/sh) × `sharesOutstanding` (815.0M) |

**Hard disqualifier check (all three, per quality-scoring.md) — none fires:**
- FCF/NI conversion <70% for 2+ years: **No** — TTM FCF/NI is ~1,456% (far above, not below, the threshold; opposite-direction situation, not a disqualifier).
- Net Debt/EBITDA over threshold: **No** — net debt is negative (net cash position); ratio is −0.31×, nowhere near the 2.5×/4× threshold.
- Not FCF-positive 3+ consecutive years: **No evidence found of a negative-FCF year**; TTM FCF is strongly positive ($4.47B). (Individual FY2022–FY2025 FCF figures were not obtainable this session — see data-gap note — but this doesn't change the conclusion below either way.)

### Sub-scores

**Profitability (25% weight):**
```
NetMargin_Component = clamp((2.674 / 30) × 100, 0, 100) = 8.9

ROIC_Component — exact figure not computable (effective tax rate / precise invested-capital
breakdown unavailable, see data-gap note). Upper bound instead, using only disclosed TTM figures:
  EBIT (Operating Income) ≈ Operating Margin × Revenue = 5.044% × $11,480.0M ≈ $579.2M
  NOPAT_max (extreme, unrealistic upper bound: 0% effective tax rate) = $579.2M
  Invested Capital ≈ Total Debt + Equity(book value proxy) − Cash
                    = $2,500.0M + $27,736.1M − $3,071.0M ≈ $27,165.1M
  ROIC_max = $579.2M / $27,165.1M ≈ 2.13%
  ROIC_Component_max = clamp((2.13 / 30) × 100, 0, 100) = 7.1  (upper bound — true value is lower,
  since the real effective tax rate is >0%)

Profitability_Score ≤ (8.9 + 7.1) / 2 = 8.0   (upper bound; no FCF-positivity cap needed — already
                                                 far below the 40.0 cap threshold)
```

**Margins (15% weight):**
```
GrossMargin_Score = clamp((70.49 / 80) × 100, 0, 100) = 88.1   (no trend-bonus needed — already
                                                                  well above the 40% bonus-eligible band)
```

**Growth (20% weight):**
```
Growth_Score = clamp((18.54 / 25) × 100, 0, 100) = 74.2
(No documented TAM/pricing-power modifier applied this pass — qualitative research not conducted
in this automated run; would only raise this sub-score further, doesn't change the outcome below.)
```

**Balance Sheet (15% weight):**
```
NetDebt/EBITDA = −$571.0M / $1,861.0M = −0.31×
BalanceSheet_Score = clamp(100 × (1 − (−0.31) / 4), 0, 100) = clamp(107.7, 0, 100) = 100.0
```

**Moat Signal (15% weight):**
```
Moat_Score = 0.0  (conservative floor — no signal researched/cited with a documented source this
                    automated pass; flagged for manual qualitative follow-up, same convention as
                    the 2026-09-07 APP session)
```

**FCF Quality (10% weight):**
```
FCF/NI = $4,469.55M / $307.0M ≈ 1,456%
FCFQuality_Score = clamp(((14.56 − 0.40) / 0.60) × 100, 0, 100) = clamp(2,360, 0, 100) = 100.0
```

### Quality Score

```
Quality Score ≤ 8.0×0.25 + 88.1×0.15 + 74.2×0.20 + 100.0×0.15 + 0.0×0.15 + 100.0×0.10
             = 2.00 + 13.215 + 14.84 + 15.00 + 0.00 + 10.00
             = 55.055 → rounds to 55.1 (upper bound, conservative Moat = 0)
```

**Robustness check — does the ROIC gap or the unresearched Moat change this result?** No. Even under the most generous possible reading of every missing input — a full Moat_Score of 100.0 (every signal cited true, which was not researched or evidenced this pass) **and** the ROIC upper bound above — the absolute ceiling is:

```
Quality Score(ceiling) = 8.0×0.25 + 88.1×0.15 + 74.2×0.20 + 100.0×0.15 + 100.0×0.15 + 100.0×0.10
                        = 2.00 + 13.215 + 14.84 + 15.00 + 15.00 + 10.00
                        = 70.055 → 70.1
```

**70.1 is still well below the 80.0+ gate.** The result is driven almost entirely by TTM Net Margin of just 2.674% (GAAP), which caps the Profitability sub-score near the bottom of its range regardless of the unresolved ROIC/Moat inputs — PANW's revenue growth (18.5% 3yr CAGR), gross margin (70.5%), balance sheet (net cash), and FCF conversion (FCF far exceeds GAAP net income) are all strong, but the framework scores off GAAP Net Income unadjusted, and PANW's GAAP earnings remain thin relative to revenue (a pattern consistent with heavy stock-based compensation and acquisition-related charges compressing reported income well below cash generation — a qualitative note, not a scored adjustment; this framework has no SBC-addback upgrade in force).

## Result: FAILS the 80.0+ Quality Gate

**Quality Score = 55.1 (conservative) / 70.1 (absolute ceiling even with every unresolved input maxed out) — both well below 80.0.** Per [quality-scoring.md](../framework/quality-scoring.md) and the operating brief, this session **stops here — Phase 02 (Rate Environment Gate + valuation scoring), the Composite Score, and fair-value/order-setup work are not run.**

## Recommendation

**PASS — do not proceed to scoring, no position.** The Composite Score comparison against the Phase 03 action table does not apply — a company must clear the Quality Score gate before it is eligible at all.

## Next review trigger

- PANW's next quarterly earnings (fiscal Q1 FY2027, expected ~November 2026) — the metric most likely to move the outcome is Net Margin/ROIC, if a lower stock-based-compensation or acquisition-charge burden lets GAAP earnings catch up meaningfully toward the company's FCF generation.
- Or: a documented moat/TAM research pass (platformization/XSIAM adoption, net-security-vendor-consolidation share data) — would raise the ceiling from 70.1 toward a genuine pass only if profitability also improves; moat and TAM evidence alone cannot close an ~10-point gap on their own given their combined 35% weight cap.

## Glossary

- **CAGR** — Compound Annual Growth Rate; the smoothed yearly growth rate connecting a start and end value over several years.
- **EBIT** — Earnings Before Interest and Taxes; operating profit before financing and tax effects.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization; a rough proxy for cash operating profit.
- **FCF** — Free Cash Flow; cash generated after running and maintaining the business.
- **GAAP** — Generally Accepted Accounting Principles; the standard US accounting rulebook.
- **Gross Margin** — Gross Profit ÷ Revenue; the share of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company outright regardless of its weighted score.
- **Moat** / **Moat Signal** — A durable competitive advantage, and this framework's 5-point checklist for scoring it.
- **Net Debt/EBITDA** — Net debt (debt minus cash) divided by EBITDA; the framework's primary leverage/balance-sheet-risk gate.
- **Net Margin** — Net Income ÷ Revenue; the share of each revenue dollar left as accounting profit after all expenses, interest, and tax.
- **Non-GAAP** — A company's own adjusted presentation of a financial measure, stripping out items it deems non-recurring; this framework scores off GAAP figures instead.
- **Operating Margin** — Operating Income ÷ Revenue; profitability before interest and taxes, distinct from Net Margin.
- **Quality Score** — This framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; a company must score 80.0+ to proceed to valuation scoring.
- **ROIC** — Return on Invested Capital; how efficiently a company turns invested capital (debt + equity) into profit.
- **TTM (Trailing Twelve Months)** — The most recent four reported quarters combined, used instead of a single fiscal-year snapshot.

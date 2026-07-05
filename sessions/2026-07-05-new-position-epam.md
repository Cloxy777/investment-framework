# NEW POSITION — EPAM (EPAM Systems, Inc.)

**Date:** 2026-07-05 | **Task type:** NEW POSITION | **10Y US Treasury yield:** 4.485% (^TNX, 2026-07-02 close — most recent available) → Rate Regime bracket 3.5–5% (would be **+5** modifier, not applied — see outcome below)

**Sector / Industry:** Technology — Information Technology Services (software engineering / digital-transformation outsourcing).

---

## Step 0 — Live price (Rule 0)

Fetched via `yfinance` (`t.info`), not inferred from any multiple:

| Metric | Value |
|---|---|
| **Live price** | **$88.27** |
| 52-week range | $73.06 – $222.53 |
| Market cap | $4.61B |
| Analyst mean target | $144.06 (median $139.00, range $99.00–$235.00, 18 analysts) |

Note the price sits far below its 52-week high (−60.3%) — background only, not used as a scoring input (Rule 0 / "never act on price movement alone").

---

## Step 1 — Data gaps flagged

Moat-signal evidence (market share, brand premium, network effect, switching costs, scale-cost advantage) was **not sourced/cited this session** — none of the 5 Moat Signal checklist items in [quality-scoring.md](../framework/quality-scoring.md) are marked true, since no citation was pulled. TAM-expansion/pricing-power evidence for the Growth sub-score modifier was likewise not sourced. Flagged rather than invented. **Neither gap changes the outcome below**: crediting the maximum possible Moat_Score (100.0, all 5 signals) would only add 15.0 points to the weighted Quality Score (43.1 → 58.1) — still 21.9 points short of the 80.0 gate.

All quantitative inputs below are sourced directly from `yfinance` (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet`), fiscal years 2022–2025 (2021 unavailable — `yfinance` only carries 4 years of annual statements).

---

## Step 2 — Phase 01 Quality Score

### Hard disqualifier checks (fail regardless of weighted score)

| Disqualifier | Result |
|---|---|
| FCF/NI conversion <70% for 2+ **consecutive** years, no growth-capex explanation | **Not triggered** — FY2022–2025: 91.2%, 128.1%, 115.9%, 162.2%. All four years clear 70% comfortably. |
| Net Debt/EBITDA over threshold (2.5× standard) | **Not triggered** — company is in a **net cash** position (Net Debt/EBITDA = −1.68×, see Balance Sheet sub-score). |
| Not FCF-positive for 3+ consecutive years | **Not triggered** — FY2022–2025 all FCF-positive. |

No hard disqualifier is being relied upon to fail this company — the weighted score fails decisively on its own.

### Sub-score calculations

**Profitability (25% weight):**
```
Net Margin (TTM, yfinance profitMargins) = 6.961%
ROIC = NOPAT / Invested Capital
  EBIT (FY2025)                = $520.003M
  Tax rate (FY2025)            = Tax Provision / Pretax Income = $127.946M / $505.624M = 25.30%
  NOPAT                        = $520.003M × (1 − 0.2530) = $388.418M
  Invested Capital              = Total Debt + Total Equity − Cash = $143.704M + $3,677.808M − $1,296.077M = $2,525.435M
  ROIC                         = $388.418M / $2,525.435M = 15.38%

NetMargin_Component = clamp((6.961/30)×100, 0, 100) = 23.20
ROIC_Component       = clamp((15.38/30)×100, 0, 100)  = 51.27
Profitability_Score  = (23.20 + 51.27) / 2 = 37.24
```
FCF-positive-3-consecutive-years cap check: FY2023–2025 all positive — no 40.0 cap applies.

**Margins (15% weight):**
```
Gross Margin (TTM, yfinance) = 29.055%
GrossMargin_Score = clamp((29.055/80)×100, 0, 100) = 36.32
```
3yr trend (FY2022→FY2025, `t.financials` Gross Profit/Revenue): 31.88% → 30.57% → 30.68% → 28.83% — **mildly contracting**, not expanding. No structural-expansion bonus applies.

**Growth (20% weight):**
```
Revenue FY2022 = $4,824.698M → Revenue FY2025 = $5,457.056M  (3-year span)
Revenue 3yr CAGR = (5,457.056 / 4,824.698)^(1/3) − 1 = 4.19%
Growth_Score = clamp((4.19/25)×100, 0, 100) = 16.76
```
No TAM-expansion/pricing-power evidence cited this session (data gap, see above) — no +10 modifier applied. Note for the record: revenue actually *dipped* in FY2023 (likely reflecting EPAM's Russia/Ukraine-exposure disruption around that period) before recovering to +15.4% YoY in FY2025 — the 3yr CAGR reflects that dip-and-recover pattern, not a smooth trend either way.

**Balance Sheet (15% weight):**
```
Net Debt = Total Debt − Cash = $143.704M − $1,296.077M = −$1,152.373M  (net cash)
Net Debt/EBITDA = −$1,152.373M / $686.084M (FY2025 EBITDA) = −1.68×
BalanceSheet_Score = clamp(100 × (1 − (−1.68)/4), 0, 100) = clamp(142.0, 0, 100) = 100.0
```

**Moat Signal (15% weight):**
```
0 of 5 signals cited/documented this session (see data-gap flag above)
Moat_Score = (0/5) × 100 = 0.0
```

**FCF Quality (10% weight):**
```
FCF/NI (FY2025, most recent) = $612.691M / $377.678M = 162.24%
FCFQuality_Score = clamp(((1.6224 − 0.40)/0.60)×100, 0, 100) = clamp(203.7, 0, 100) = 100.0
```

### Final Quality Score

```
Quality Score = (37.24×0.25) + (36.32×0.15) + (16.76×0.20) + (100.0×0.15) + (0.0×0.15) + (100.0×0.10)
              = 9.31 + 5.45 + 3.35 + 15.00 + 0.00 + 10.00
              = 43.11 → rounds to 43.1
```

**43.1 < 80.0 — fails the Quality Score gate**, by 36.9 points. Even crediting the maximum possible Moat_Score (100.0 — all 5 signals documented true, which was not attempted or verified) would only raise the score to **58.1** — still 21.9 points short of the gate. The shortfall is driven by thin profitability (net margin 6.96%, well under the >15% Phase 01 threshold), a gross margin under the 40% pre-screen bar with a mildly contracting (not expanding) 3-year trend, and a weak 3-year revenue CAGR (4.19%, vs. >10%/>8% thresholds) — the balance sheet (net cash) and FCF conversion (162%) are the only strong sub-scores.

---

## Step 3 — Recommendation

**PASS. Stop before Phase 02.** Per [quality-scoring.md](../framework/quality-scoring.md) and the operating brief, a company must score 80.0+ to be eligible for valuation scoring, fair value, or order setup — EPAM misses by 36.9 points, and misses even under the most generous plausible assumption (full Moat credit) by 21.9 points. No Phase 02 valuation score, fair value, Rate Environment Gate application, or order setup is computed — doing so would violate the gate.

No hard disqualifier is involved; this is a straightforward weighted-score failure driven by margin and growth metrics that don't currently clear this framework's high quality bar, not a balance-sheet or cash-flow-quality failure.

**Watchlist status:** first evaluation of this ticker — new entry created at `watchlist/not-in-portfolio/EPAM/EPAM-2026-07-05.md`.

**Next review trigger:** Rule 9 event (quarterly earnings, guidance revision, management change, M&A, macro shift, or >15% unexplained move) — or evidence of a sustained (not one-quarter) recovery in net margin/gross margin/revenue growth toward the Phase 01 thresholds (net margin >15%, gross margin >40%, revenue CAGR >10%).

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **EBIT** — Earnings Before Interest and Taxes.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization.
- **FCF** — Free Cash Flow.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether accounting profit is turning into real cash.
- **Gross Margin** — Gross Profit ÷ Revenue.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score.
- **Net Debt/EBITDA** — leverage ratio; net debt (debt minus cash) divided by EBITDA.
- **Net Margin** — Net Income ÷ Revenue.
- **NOPAT** — Net Operating Profit After Tax; EBIT × (1 − effective tax rate).
- **Quality Score** — this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to proceed to valuation scoring.
- **Rate Regime Modifier** — additive adjustment (−10 to +10) to the valuation score based on the 10-Year Treasury yield bracket (not applied here — gate failed before Phase 02).
- **ROIC** — Return on Invested Capital; NOPAT ÷ Invested Capital.
- **Treasury yield (10Y)** — the US government's 10-year borrowing rate, this framework's risk-free-rate benchmark.
- **TTM** — Trailing Twelve Months.

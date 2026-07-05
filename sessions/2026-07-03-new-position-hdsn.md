# NEW POSITION — HDSN (Hudson Technologies, Inc.)

**Date:** 2026-07-03 | **Task type:** NEW POSITION | **10Y US Treasury yield:** 4.37% (^TNX, 2026-06-26 close — most recent available) → Rate Regime bracket 3.5–5% (would be **+5** modifier, not applied — see outcome below)

**Sector / Industry:** Basic Materials / Specialty Chemicals — refrigerant (HFC) reclamation, reclaim/resale, and recovery services.

---

## Step 0 — Live price (Rule 0)

Fetched via `yfinance` (`t.info`), not inferred from any multiple:

| Metric | Value |
|---|---|
| **Live price** | **$5.99** |
| 52-week range | $4.64 – $10.52 |
| Market cap | $251.99M |
| Analyst mean target | $8.50 |

---

## Step 1 — Data gaps flagged

Moat-signal evidence (market share, pricing power, network effect, switching costs, scale-cost advantage) was **not sourced/cited this session** — none of the 5 Moat Signal checklist items in [quality-scoring.md](../framework/quality-scoring.md) are marked true, since no citation was pulled. This is flagged rather than invented. It does **not** change the outcome below: even crediting the maximum possible Moat_Score (100.0, all 5 signals) would only add 15.0 points to the weighted Quality Score (24.7 → 39.7) — still far short of the 80.0 gate.

All other quantitative inputs below are sourced directly from `yfinance` (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet`), 2022–2025 fiscal years (2021 unavailable — `yfinance` only carries 4 years of annual statements).

---

## Step 2 — Phase 01 Quality Score

### Hard disqualifier checks (fail regardless of weighted score)

| Disqualifier | Result |
|---|---|
| FCF/NI conversion <70% for 2+ **consecutive** years, no growth-capex explanation | **Not triggered on a strict reading** — 2022: 57.0% (<70%), 2023: 105.2%, 2024: 354.7%, 2025: −49.3% (<70%). The two sub-70% years (2022, 2025) are not consecutive; 2023–2024 break the streak. Flagged as a real quality concern regardless (see FCF Quality sub-score below). |
| Net Debt/EBITDA over threshold (2.5× standard) | **Not triggered** — company is in a **net cash** position (Net Debt/EBITDA = −1.39×, see Balance Sheet sub-score). |
| Not FCF-positive for 3+ consecutive years | **Ambiguous, not treated as triggering:** FY2022–2024 were 3 consecutive positive-FCF years; FY2025 (the most recent) turned negative (−$8.21M). Flagged rather than definitively ruled a hard disqualifier — moot regardless, since the weighted score fails the gate by a wide margin below (see FCF Quality Score, which does apply its continuous penalty for this same negative print). |

No hard disqualifier is being relied upon to fail this company — the weighted score fails decisively on its own.

### Sub-score calculations

**Profitability (25% weight):**
```
Net Margin (TTM, yfinance)     = 5.663%
ROIC = NOPAT / Invested Capital
  EBIT (FY2025)                = $18,559,000
  Tax rate (FY2025)            = Tax Provision / Pretax Income = $6,024,000 / $22,691,000 = 26.55%
  NOPAT                        = $18,559,000 × (1 − 0.2655) = $13,631,962
  Invested Capital             = Total Debt + Total Equity − Cash = $5,289,000 + $243,390,000 − $39,456,000 = $209,223,000
  ROIC                         = $13,631,962 / $209,223,000 = 6.52%

NetMargin_Component = clamp((5.663/30)×100, 0, 100) = 18.88
ROIC_Component       = clamp((6.52/30)×100, 0, 100)  = 21.73
Profitability_Score  = (18.88 + 21.73) / 2 = 20.30
```
FCF-positive-3-consecutive-years cap check: trailing 3 years (2023–2025) include FY2025's negative FCF, so the cap-at-40.0 rule would apply — moot here since 20.30 is already below 40.0.

**Margins (15% weight):**
```
Gross Margin (TTM, yfinance) = 24.611%
GrossMargin_Score = clamp((24.611/80)×100, 0, 100) = 30.76
```
3yr trend is **sharply contracting** (gross margin fell from ~50.1% in FY2022 to ~24.6% today, per `t.financials` Gross Profit/Revenue) — no structural-expansion bonus applies (trend is the opposite direction).

**Growth (20% weight):**
```
Revenue FY2022 = $325,225,000 → Revenue FY2025 = $246,614,000  (3-year span)
Revenue 3yr CAGR = (246,614,000 / 325,225,000)^(1/3) − 1 = −8.81%
Growth_Score = clamp((−8.81/25)×100, 0, 100) = clamp(−35.3, 0, 100) = 0.0
```
Documented evidence of **structural** (not cyclical) growth deceleration: revenue has declined in 2 of the last 3 fiscal years as reclaimed/virgin HFC refrigerant prices collapsed industry-wide under EPA AIM Act phase-down dynamics and oversupply — a −10 modifier would apply but is already floored at 0.0.

**Balance Sheet (15% weight):**
```
Net Debt = Total Debt − Cash = $5,289,000 − $39,456,000 = −$34,167,000  (net cash)
Net Debt/EBITDA = −$34,167,000 / $24,550,000 (FY2025 EBITDA) = −1.39×
BalanceSheet_Score = clamp(100 × (1 − (−1.39)/4), 0, 100) = clamp(134.8, 0, 100) = 100.0
```

**Moat Signal (15% weight):**
```
0 of 5 signals cited/documented this session (see data-gap flag above)
Moat_Score = (0/5) × 100 = 0.0
```

**FCF Quality (10% weight):**
```
FCF/NI (FY2025, most recent) = −$8,214,000 / $16,667,000 = −49.28%
FCFQuality_Score = clamp(((−0.4928 − 0.40)/0.60)×100, 0, 100) = clamp(−148.8, 0, 100) = 0.0
```

### Final Quality Score

```
Quality Score = (20.30×0.25) + (30.76×0.15) + (0.0×0.20) + (100.0×0.15) + (0.0×0.15) + (0.0×0.10)
              = 5.075 + 4.614 + 0.0 + 15.0 + 0.0 + 0.0
              = 24.69 → rounds to 24.7
```

**24.7 < 80.0 — fails the Quality Score gate.**

---

## Step 3 — Recommendation

**PASS. Stop before Phase 02.** Per [quality-scoring.md](../framework/quality-scoring.md) and the operating brief, a company must score 80.0+ to be eligible for valuation scoring, fair value, or order setup — HDSN misses by 55.3 points, driven by a collapsing top line (3yr revenue CAGR −8.8%), a gross margin that's halved in 3 years (50%→24.6%), negative trailing FCF, and thin profitability (net margin 5.7%, ROIC 6.5%). The only strong sub-score is the balance sheet (net-cash position). No Phase 02 valuation score, fair value, or order setup is computed — doing so would violate the gate.

**Watchlist status:** first evaluation of this ticker — new entry created at `watchlist/not-in-portfolio/HDSN/HDSN-2026-07-03.md`.

**Next review trigger:** Rule 9 event (quarterly earnings, guidance revision, management change, M&A, macro shift, or >15% unexplained move) — or evidence the refrigerant-price/margin collapse has structurally reversed (e.g. 2+ consecutive quarters of gross-margin recovery toward the 40%+ historical range).

---

## Glossary

- **Basic Materials, Specialty Chemicals** — GICS sector/industry classification.
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

# New Position Evaluation — ORANY (Orange S.A.)

**Task:** NEW POSITION
**Date:** 01 Jul 2026
**10Y US Treasury Yield:** ~4.46% ([tradingeconomics.com](https://tradingeconomics.com/united-states/government-bond-yield), [CNBC US10Y](https://www.cnbc.com/quotes/US10Y))
**Rate Regime Modifier (would apply if reached):** 3.5–5% bracket → **+5**

---

## 1. Live Price (Rule 0)

Fetched via web search, cross-checked across sources — some dispersion noted (typical of thinly-traded OTC ADR quotes updating asynchronously):

| Source | Price (USD) |
|---|---|
| Yahoo Finance | $19.28 |
| Investing.com | $20.30 |
| Headline snapshot (most recent) | **$20.90** (day range $20.16–$20.41, -0.29%) |

**Live price used: $20.90** (most recent snapshot; 52-week range $14.45–$21.85). ADR ratio confirmed **1:1** vs. Paris-listed ORA ordinary share ([orange.com ADR program page](https://www.orange.com/en/finance/institutional-investors/our-adr-program)).
Market cap: **$55.56B**.

Sources: [Investing.com](https://www.investing.com/equities/france-telecom-sa), [Yahoo Finance](https://finance.yahoo.com/quote/ORANY/), [Morningstar](https://www.morningstar.com/stocks/pinx/orany/quote).

---

## 2. Phase 01 — Quality Score

Data pulled from stockanalysis.com (TTM figures) and Orange's own FY2025 press release ([globenewswire.com](https://www.globenewswire.com/news-release/2026/02/18/3240477/0/en/orange-success-of-lead-the-future-2023-2025-strategic-plan-2025-objectives-fully-achieved.html), [marketscreener.com FY2025 press release](https://www.marketscreener.com/news/orange-fy-2025-press-release-515634-345jb4ds15-75-ce7e5ddfd088f023)).

### Quantitative inputs gathered

| Metric | Value | Source |
|---|---|---|
| Net Margin (TTM, reported) | 1.33% | stockanalysis.com — TTM revenue $47.43B, TTM net income $433.25M |
| Net Margin (TTM, adjusted, ex-GEPP one-off) | ~7.7% | Adjusted net income €3,094M ÷ FY2025 revenue ~€40.3B (Orange FY2025 press release) |
| ROIC (TTM) | 3.43% | stockanalysis.com |
| ROE (TTM) | 3.21% | stockanalysis.com |
| Gross Margin (TTM) | 36.92% | stockanalysis.com |
| Operating Margin (TTM) | 10.71% | stockanalysis.com |
| Net Debt / EBITDA (telecom activities) | 1.80× (FY2025) | Orange FY2025 press release |
| Free Cash Flow (TTM) | $4.06B (op cash flow $12.66B − capex $8.60B) | stockanalysis.com |
| Free Cash Flow all-in (Orange's own metric, FY2025) | €2,793M (−6.6% YoY) | Orange FY2025 press release |
| Revenue (FY2023 / FY2024) | €44,122M / €40,260M (2024 figure lower due to MASORANGE Spain deconsolidation, not organic decline) | Orange press releases |

### Hard disqualifier check

- **FCF/NI conversion <70% for 2+ years:** Not computable precisely without multi-year NI series on a comparable (non-restructured) basis — **flagged as a data gap**, but moot given the result below.
- **Net Debt/EBITDA over threshold:** 1.80× (telecom activities) is **under** the 2.5× standard threshold — passes this individual check. (Orange doesn't clearly qualify for the asset-light 4× override — it's not a payment network/exchange — so the 2.5× standard applies, and it's cleared.)
- **FCF-positive 3+ consecutive years:** FCF all-in has grown 74% over 3 years per company reporting — **appears FCF-positive**, though the exact year-by-year series wasn't independently pulled.

No outright hard disqualifier fires on the data gathered. However, the **weighted score itself fails the gate decisively** (see below) — a mature, low-margin, low-ROIC telecom, which the sub-score formulas are not built to rescue.

### Sub-score calculations

**Profitability (25% weight):**
```
NetMargin_Component = clamp((1.33 / 30) × 100, 0, 100) = 4.4   [using reported TTM net margin, most conservative/current basis]
ROIC_Component       = clamp((3.43 / 30) × 100, 0, 100) = 11.4
Profitability_Score  = (4.4 + 11.4) / 2 = 7.9
```
(Even substituting the adjusted 7.7% net margin: NetMargin_Component = 25.7, Profitability_Score = (25.7+11.4)/2 = 18.6 — still far below any plausible passing composite.)

**Margins (15% weight):**
```
GrossMargin_Score = clamp((36.92 / 80) × 100, 0, 100) = 46.2
```
No cited 3yr structural-expansion evidence gathered — no bonus applied (per "never infer this modifier without a documented source").

**Growth (20% weight):**
Revenue CAGR 3yr: **not independently computable from the raw figures gathered** — FY2023 (€44,122M) to FY2024 (€40,260M) reflects a corporate deconsolidation (MASORANGE JV), not organic growth/decline, so a naive 2-point CAGR would misrepresent the business. **This is a genuine data gap** — a clean, deconsolidation-adjusted 3yr organic revenue CAGR was not sourced. Flagged rather than estimated.

**Balance Sheet (15% weight):**
```
BalanceSheet_Score = clamp(100 × (1 − 1.80/4), 0, 100) = 55.0
```

**Moat Signal (15% weight):** Not scored — no cited evidence gathered this session for any of the 5 signals (market share, brand premium, network effect, switching costs, scale cost advantage). Orange is a large incumbent European telecom with plausible scale/brand moat characteristics, but per the framework's rule ("never mark a signal true without a cited source"), this cannot be asserted without documented evidence. **Flagged as a data gap.**

**FCF Quality (10% weight):**
FCF/NI ratio TTM ≈ $4.06B / $433.25M ≈ 937% — this ratio is distorted by the depressed TTM net income (GEPP one-off charge), not a genuine cash-conversion signal. Using adjusted net income (~€3,094M) against FCF all-in (~€2,793M) gives ≈90%. Given the conflicting bases, this sub-score is unreliable without a clean, single-basis multi-year series — **flagged as a data gap** rather than computed on a distorted base.

### Quality Score — computed on available data (conservative/reported basis)

```
Quality Score = (Profitability_Score × 0.25) + (Margins_Score × 0.15) + (Growth_Score × 0.20)
              + (BalanceSheet_Score × 0.15) + (Moat_Score × 0.15) + (FCFQuality_Score × 0.10)
```

Using only the components that could be computed without inventing data (Profitability 7.9, Margins 46.2, Balance Sheet 55.0), and treating Growth, Moat, and FCF Quality as **unscored gaps** (not zero-filled, not invented):

```
Partial weighted sum (available components only) = 7.9×0.25 + 46.2×0.15 + 55.0×0.15
                                                   = 1.98 + 6.93 + 8.25 = 17.2
                                                   (on 55% of total weight — Growth 20%, Moat 15%, FCF Quality 10% = 45% unscored)
```

Even granting the **maximum possible score (100.0)** on all three unscored components — Growth, Moat, and FCF Quality — the ceiling is:
```
Best-case Quality Score = 17.2 + (100×0.20) + (100×0.15) + (100×0.10) = 17.2 + 20 + 15 + 10 = 62.2
```

**62.2 is still far below the 80.0+ gate.** The Profitability sub-score alone (7.9, driven by a 1.33% net margin and 3.43% ROIC — both an order of magnitude below the framework's quality thresholds) makes an 80.0+ Quality Score mathematically unreachable regardless of how the remaining data gaps resolve.

---

## 3. Quality Gate Result: **FAIL**

**ORANY does not clear the 80.0+ Quality Score gate.** Best-case ceiling (generously assuming maximum scores on every unresolved data gap) is **62.2** — nowhere close to 80.0. The Profitability sub-score (7.9/100, from 1.33% TTM net margin and 3.43% ROIC) is the decisive, unfixable driver: Orange is a mature, capital-intensive, low-margin European telecom incumbent, structurally distant from the framework's quality bar (which is calibrated to high-ROIC compounders).

**Per operating-brief.md and quality-scoring.md: stop here. Do not proceed to Phase 02 valuation scoring, the Rate Environment Gate, the Composite Score, or fair-value/order setup.** This is true regardless of how cheap ORANY's multiples look (forward PE ~17.6×, EV/EBITDA ~7.25× — both objectively reasonable for a telecom) — a strict quality gate, by design, doesn't let cheapness rescue a low-quality business.

### Data gaps identified (for the record — not invented, per Rule "never invent or estimate financial data")

1. Clean, deconsolidation-adjusted 3-year organic revenue CAGR (raw reported figures are distorted by the MASORANGE Spain JV deconsolidation between FY2023 and FY2024).
2. Moat-signal evidence (market share trend, brand premium/pricing power, network effect, switching costs, scale cost advantage) — none cited this session.
3. A single consistent basis for the FCF/Net Income conversion ratio (TTM reported NI is distorted by a one-off €1,244M GEPP restructuring charge; adjusted NI and FCF-all-in are reported on Orange's own non-GAAP basis, not independently reconciled here).
4. Gross margin 3-year trend (only a single TTM snapshot, 36.92%, was sourced).

None of these gaps change the outcome — the Profitability sub-score alone caps the best possible outcome at 62.2, below the 80.0 threshold — but they are listed for completeness and in case the framework's quality gate is ever revisited for capital-intensive/infrastructure businesses (see the note in quality-scoring.md about lowering the threshold if it screens out too much of the investable universe).

---

## 4. Recommendation

**PASS.** ORANY fails the Phase 01 Quality Score gate (best-case ceiling 62.2 vs. required 80.0+). No valuation scoring, Composite Score, or fair-value/order setup is computed, per the framework's explicit instruction to stop at gate failure regardless of price attractiveness.

This is a **structural/business-quality** conclusion, not a valuation one — Orange's reasonable-looking multiples (forward PE ~17.6×, EV/EBITDA ~7.25×) are irrelevant to this outcome. A future re-evaluation would need to resolve the data gaps above, but given the size of the Profitability shortfall, a materially different conclusion is unlikely without a fundamental change in Orange's margin/ROIC profile.

---

## Next Review Trigger

No standing review scheduled — ORANY is not held and fails the quality gate. Re-evaluate only if a fundamental change occurs (e.g., a sustained structural improvement in net margin/ROIC, a strategic transformation, or the framework's quality gate threshold is revisited per the note in quality-scoring.md).

---

## Glossary

- **10Y Treasury yield** — the interest rate on 10-year US government bonds, the framework's risk-free-rate benchmark.
- **ADR (American Depositary Receipt)** — a US-exchange/OTC-traded security representing shares of a non-US company; ORANY represents Orange S.A.'s Paris-listed ordinary shares at a confirmed 1:1 ratio.
- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate over multiple years.
- **Composite Score** — the framework's blended Quality + Valuation ranking number (not computed here — company failed the quality gate before reaching this step).
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures.
- **EV/EBITDA** — Enterprise Value ÷ EBITDA, a valuation multiple independent of capital structure.
- **FCF (Free Cash Flow)** — cash generated after running and maintaining the business.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, a check on whether accounting profit is turning into real cash.
- **Forward PE** — share price ÷ next-twelve-months expected earnings per share.
- **GEPP** — Orange's French "Employment and Career Path Planning" restructuring program; a one-off charge that distorted FY2025 reported net income.
- **Gross margin** — revenue minus cost of goods sold, as a percentage of revenue.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company outright regardless of weighted score.
- **Net Debt/EBITDA** — a leverage ratio measuring balance-sheet risk; the framework's primary debt gate.
- **Net margin** — net income ÷ revenue.
- **Quality Score** — the framework's 0–100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; a company must score 80.0+ to proceed to valuation scoring.
- **Rate Regime Modifier** — an additive adjustment to the valuation score based on the current 10Y Treasury bracket (not applied here — company never reached Phase 02).
- **ROE (Return on Equity)** — Net Income ÷ shareholder equity.
- **ROIC (Return on Invested Capital)** — how efficiently a company turns invested capital into profit; a core quality signal.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results.

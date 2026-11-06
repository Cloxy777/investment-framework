# New Position Evaluation — VRT (Vertiv Holdings Co, NYSE)

**Task type:** NEW POSITION · **Date:** 2026-11-06 · **Sector:** Industrials — data-center power & thermal management
**10Y Treasury:** 4.90% (FRED DGS10, 2026-11-04 latest print) — not used (gate stopped before Phase 02)

## 1. Data gaps flagged
- Gross buyback yield: the script printed UNKNOWN; Q3 2026 release shows **no repurchase line** (YTD 2026 or 2025) → 0 (irrelevant to Quality gate).
- `cycle_peak` / `value_trap_candidate`: UNKNOWN (yfinance lacks 8 quarters of diluted EPS) — data gap, not estimated.
- Moat evidence: only market-share signal has a citation; the other four are FALSE for lack of a cited source (not invented).

## 2. Live price (Rule 0)
IBKR snapshot (contract 402783527): last **$182.44**, bid/ask 182.39 / 183.27, +3.23% day. 52-wk range 147.76 – 379.84 (−52% from high).

## 3. fetch_fundamentals output (verbatim)
```
Market Cap = 68,051,726,336 · EV = 67,696,926,720 · Shares = 385,060,421
Forward PE = 18.140 · FCF Yield % = 4.576 · EV/EBIT = 25.526
Net Margin % = 15.995 · Gross Margin % = 38.115 · ROIC % = 31.027 [tax 0.1981, NOPAT 2,126,707,870, InvCap 6,854,300,000]
Revenue 3yr CAGR % = 21.585 · Net Debt/EBITDA = 0.372 [EBITDA 3,188,199,936]
FCF/NI TTM % (plain) = 148.437 · (FCF-SBC)/NI = 145.686 · SBC yield % = 0.085
Gross buyback yield % = UNKNOWN (set 0: no repurchases in filings)
FCF/NI annual (oldest first) = [-344.4%, 166.4%, 229.0%, 141.6%] · FCF positive 3yr+ = True
5yr PE avg/low/high = 38.455 / 16.227 / 68.136 (n=20 quarters)
SBC 57.7M · FCF 3,114.2M · SBC/FCF 1.9% · FCF yield after SBC 4.49%
cycle_peak UNKNOWN · value_trap_candidate UNKNOWN
```
flags_common (`--forward-pe 18.14 --eps-growth 38`, growth = management FY2026 organic guide): `multiple_ceiling NONE`. Handling: no flag raised; the two UNKNOWNs are data gaps and don't affect a gate stop.

Disqualifier note: FCF/NI of −344.4% is one year only (oldest); never 2+ consecutive years <70% → no disqualifier.

## 4. Quality Score (script output, verbatim)
Inputs: `scratchpad/q.json` — manual fields: TAM evidence (Vertiv Q3 2026 8-K Ex.99.1: organic orders >100% YoY, sales +61%, FY26 guide $14.65B / 37–39% organic); gross-margin structural trend = FALSE (2023 sources conflict 32.3% vs 35.0%; FY24 36.6% → FY25 36.3% flat; TTM 38.1%); moat per table.

```
NetMargin_Component = clamp((15.995/30)x100) = 53.32
ROIC_Component = clamp((31.027/30)x100) = 100.00
Profitability_Score = (53.32 + 100.00) / 2 = 76.66
GrossMargin_Score = clamp((38.115/80)x100) = 47.64
Growth_Score = clamp((21.585/25)x100) = 86.34 +10 TAM = 96.34
BalanceSheet_Score = clamp(100x(1 - 0.372/4)) = 90.70
Moat: 1/5 TRUE -> 20.00
  market_share_stable_or_growing TRUE  — #1 data-center thermal mgmt (~20%, Dell'Oro/Omdia via secondary Substack) + ~55% organic Q3 growth; FY25 annual report "gaining market share"
  brand_premium FALSE — FY25 10-K: gross margin flat 36.6%→36.3%, price offset by tariff inflation
  network_effect FALSE — n/a
  switching_costs FALSE — no primary-source citation retrieved
  scale_cost_advantage FALSE — no cited cost-per-unit data
FCFQuality_Score = clamp(((1.4569 - 0.40)/0.60)x100) = 100.00
Quality Score = (76.66x0.25)+(47.64x0.15)+(96.34x0.20)+(90.70x0.15)+(20.00x0.15)+(100.00x0.10) = 72.184 -> 72.2
# Quality Score = 72.2 — FAILS the 80.0+ gate
```

## 5. Recommendation: **PASS (watchlist as Phase 01 FAIL) — do not proceed to Phase 02**
No Rate Gate, valuation score, Composite or order setup run (gate policy). Shortfall is 7.8 points, almost entirely the Moat sub-score: each additional documented Moat Signal adds +3.0 Quality points, so ~3 signals (not 1) would be needed to clear 80.0. Switching costs (installed base/service) and scale advantage are plausible but I did not retrieve primary-source (10-K) evidence and did not assume it. Informational only: price is −52% from its 52-week high; forward PE 18.1 vs 5yr avg 38.5 — the framework doesn't act on that without clearing the gate.

## 6. Next review trigger
Re-run `/new-position VRT` after documenting primary-source moat evidence from the FY2025 10-K, or at Q4 2026 earnings (~Feb 2027), or on any Rule 9 trigger.

## Glossary
- **Quality Score** — 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat and FCF quality; 80.0+ needed to proceed to valuation.
- **Moat Signal** — 5-point checklist (market share, brand premium, network effect, switching costs, scale cost advantage), each TRUE only with a cited source; Moat score = TRUE count ÷ 5 × 100.
- **Hard disqualifier** — Quality condition that fails a company regardless of weighted score (FCF-negative 3+ yrs, leverage over threshold, FCF/NI <70% for 2+ consecutive years).
- **TAM** — Total Addressable Market: total revenue opportunity if a company captured 100% of its market.
- **ROIC** — Return on Invested Capital: profit earned on debt + equity capital invested.
- **CAGR** — Compound Annual Growth Rate: smoothed yearly growth from start to end value.
- **FCF** — Free Cash Flow: cash left after running and maintaining the business.
- **SBC** — Stock-Based Compensation: pay in shares/options; added back in FCF but a real dilution cost; this framework subtracts it.
- **Net Debt/EBITDA** — years of operating cash profit needed to repay net debt.
- **Gross Margin / Net Margin** — share of revenue left after direct costs / after all costs.
- **FCF/NI conversion ratio** — FCF ÷ net income: is accounting profit turning into cash?
- **Forward PE** — price ÷ next-twelve-month expected earnings per share.
- **Rule 0** — always fetch a live price first; never infer it.
- **Composite Score** — 50/50 blend of (100 − Quality) and Valuation; only computed after the quality gate is cleared (not computed here).

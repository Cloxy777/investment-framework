# NEW POSITION — HTO (H2O America, formerly SJW Group)

**Task type:** NEW POSITION
**Date:** 2026-06-30
**10Y US Treasury Yield:** ~4.38% (TradingEconomics/Fed H.15, 2026-06-29 print — see Sources)
**Rate Regime Modifier (would apply if Phase 02 were reached):** 3.5–5% bracket → +5 (not applied — gate fails before Phase 02)
**Current portfolio weight:** 0% (not held — absent from [holdings.md](../portfolio/holdings.md))

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$61.52** | Yahoo Finance quote API, `regularMarketPrice`, market state REGULAR, NasdaqGS, quote timestamp 2026-06-30 17:16:35 UTC |
| Day range | $60.46 – $61.52 | Same source |
| 52-week range | $43.75 – $61.87 | Same source |
| Previous close | $61.01 | Same source |
| Market cap | $2.57B | Same source |

## 2. Company Identification

**HTO = H2O America** (renamed from SJW Group in May 2025), NASDAQ-listed. **Sector: Utilities — Regulated Water.** Owns regulated water/wastewater utility subsidiaries: San Jose Water Company (California), Connecticut Water Company, Maine Water Company, and SJWTX (Texas). A capital-intensive, rate-regulated infrastructure business — not a tech/growth name, included here because it was named for evaluation.

## 3. Phase 01 — Quality Score (per quality-scoring.md)

### Data used (FY2022–FY2025 annual, 10-K-sourced figures via Yahoo Finance fundamentals timeseries)

| Metric ($M unless noted) | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Revenue | 620.70 | 670.36 | 748.44 | 800.59 |
| Gross profit | 357.17 | 388.43 | 425.12 | 456.53 |
| Gross margin | 57.54% | 57.94% | 56.80% | 57.02% |
| EBIT | 140.39 | 157.09 | 174.33 | 187.51 |
| EBITDA | 246.83 | 265.23 | 289.38 | 308.00 |
| Net income | 73.83 | 84.99 | 93.97 | 102.58 |
| Net margin | 11.90% | 12.68% | 12.55% | 12.81% |
| Operating cash flow | 166.20 | 190.83 | 195.53 | 244.80 |
| CapEx | (244.24) | (290.72) | (380.64) | (522.90) |
| **Free cash flow** | **(78.04)** | **(99.89)** | **(185.11)** | **(278.10)** |
| FCF/NI ratio | −105.7% | −117.5% | −197.0% | −271.1% |
| Total debt | 1,655.90 | 1,747.17 | 1,829.68 | 1,977.16 |
| Net debt | 1,643.56 | 1,737.45 | 1,818.56 | 1,956.47 |
| Net Debt/EBITDA | 6.66× | 6.55× | 6.28× | **6.35×** |
| Invested capital | 2,766.77 | 2,980.57 | 3,196.65 | 3,517.93 |
| Stockholders' equity | 1,110.87 | 1,233.40 | 1,366.97 | 1,540.77 |

Effective tax rate (FY2025): $12.36M tax ÷ $114.93M pretax income = 10.75%.
NOPAT (FY2025) = EBIT × (1 − 10.75%) = $187.51M × 0.8925 = $167.35M.
**ROIC (FY2025) = NOPAT ÷ Invested Capital = $167.35M ÷ $3,517.93M = 4.76%.**
ROE (FY2025, for reference) = $102.58M ÷ $1,540.77M = 6.66%.
Revenue 3yr CAGR (FY2022→FY2025) = (800.59/620.70)^(1/3) − 1 = **8.85%**.

### Hard disqualifier check (fires regardless of weighted score — quality-scoring.md)

| Hard disqualifier | Applies to HTO? | Basis |
|---|---|---|
| FCF/NI conversion ratio <70% for 2+ consecutive years, no documented growth-capex carve-out | **Plausibly yes, but not relied on as primary** | FCF/NI is negative in all four years on record (−105.7% to −271.1%). A water utility's CapEx is a mix of mandatory pipe-replacement/system-maintenance spend and discretionary capacity growth, and no filing breakdown of that split was pulled this session — per "never invent or estimate financial data," this one is flagged but not used as the deciding citation. |
| Net Debt/EBITDA over threshold (2.5× standard; 4× Upgrade 5 asset-light override) | **Yes — fires** | 6.35× (FY2025), and has run 6.28×–6.66× across all four years. The Upgrade 5 asset-light override is explicitly scoped to "payment networks, exchanges, or asset-light financials" — a physical water-pipe-and-treatment-plant utility is the opposite of asset-light (FY2025 net PP&E $3.89B against $5.15B total assets), so the standard 2.5× threshold applies, not the 4× override. 6.35× is 2.5× over the standard threshold. |
| Not FCF-positive for 3+ consecutive years | **Yes — fires, unconditionally** | FCF was negative in **all four** years on record (FY2022 −$78.0M, FY2023 −$99.9M, FY2024 −$185.1M, FY2025 −$278.1M), and the trend is **worsening**, not improving (CapEx nearly tripled, $244M→$523M, over the period as revenue grew only 29%). This disqualifier carries no growth-capex carve-out in the framework text — it applies regardless of the reason for the cash burn. |

**Two hard disqualifiers fire independently and unconditionally** (Net Debt/EBITDA, FCF positivity) — either alone is sufficient to fail the gate before any weighted score is considered.

### Weighted Quality Score (computed in full per "show every calculation" — not overridden by the disqualifiers above)

| Sub-score (weight) | Inputs | Calculation | Result |
|---|---|---|---|
| **Profitability** (25%) | Net margin 12.81%, ROIC 4.76% (FY2025) | NetMargin_Component = clamp((12.81/30)×100) = 42.7. ROIC_Component = clamp((4.76/30)×100) = 15.9. Avg = (42.7+15.9)/2 | **29.3** |
| **Margins** (15%) | Gross margin 57.02% (FY2025); 3yr trend 57.54%→57.94%→56.80%→57.02% — flat, no clear structural expansion | clamp((57.02/80)×100) = 71.3; no trend bonus (already >40%, and trend is flat/noisy, not expanding) | **71.3** |
| **Growth** (20%) | Revenue 3yr CAGR 8.85% | clamp((8.85/25)×100) = 35.4; no TAM/pricing-power bonus or deceleration penalty applied — no cited evidence either way was sourced this session (regulated-utility growth is mechanically rate-base/customer-growth driven, not a TAM-expansion or pricing-power story in the framework's intended sense) | **35.4** |
| **Balance Sheet** (15%) | Net Debt/EBITDA 6.35× (FY2025) | clamp(100×(1−6.35/4)) = clamp(−58.8) | **0.0** |
| **Moat** (15%) | 2 of 5 signals marked true (see below) | (2/5)×100 | **40.0** |
| **FCF Quality** (10%) | FCF/NI −271.1% (FY2025) | clamp(((−2.711−0.40)/0.60)×100) = clamp(−518.5) | **0.0** |

**Moat signal detail** (cited per quality-scoring.md's "do not mark a signal true without a cited source"):
- ✅ **Market share stable or growing** — H2O America's subsidiaries (SJWC, CWC, MWC, SJWTX) operate as exclusive regulated-monopoly franchises in their service territories (company business description, Yahoo Finance/SEC profile data pulled this session) — no documented share loss is possible under this franchise structure.
- ❌ Brand premium — no evidence; rates are regulator-set, not brand-driven.
- ❌ Network effect — not applicable to a water utility's business model.
- ✅ **Switching costs** — customers have no alternative water-distribution infrastructure to switch to within a franchise territory (physical pipe-network lock-in, documented by the same regulated-monopoly business description).
- ❌ Scale cost advantage — no cited cost-per-unit-vs.-competitor data was sourced this session.

```
Quality Score = (29.3 × 0.25) + (71.3 × 0.15) + (35.4 × 0.20) + (0.0 × 0.15) + (40.0 × 0.15) + (0.0 × 0.10)
              = 7.325 + 10.695 + 7.080 + 0.000 + 6.000 + 0.000
              = 31.1
```

**Quality Score: 31.1 / 100.0 — fails the 80.0+ gate by a wide margin**, independently confirmed by two unconditional hard disqualifiers (Net Debt/EBITDA 6.35× vs. 2.5× standard threshold; FCF negative all 4 of the last 4 fiscal years, worsening). Per [quality-scoring.md](../framework/quality-scoring.md) and the operating brief, **this stops the evaluation here — no Phase 02 valuation score, Composite Score, or fair-value/order setup is computed.**

## 4. Recommendation

**PASS — do not enter, do not watchlist for a near-term retry.** HTO is a financially stable, well-run regulated water utility (positive and growing net income, exclusive-franchise moat, reasonable gross margins) but its capital structure and cash-flow profile are structurally incompatible with this framework's quality bar: it has never generated positive free cash flow in the last four fiscal years (CapEx running 2–3× operating cash flow, funding an accelerating multi-year infrastructure build-out), carries 6.3×+ net debt/EBITDA versus the framework's 2.5× standard ceiling, and posts a 4.76% ROIC — all structural features of the regulated-utility business model (capital recovered through the rate base over decades, not through near-term FCF) rather than a temporary or correctable condition. This is not a "buy when it gets cheaper" situation; the valuation score is irrelevant here because the business never clears the quality gate regardless of price.

## 5. Next Review Trigger

Re-evaluate only if a **structural** change occurs — not a price move or a single good quarter:
- A multi-year (2+ year) trend of FCF turning and staying positive as the current CapEx supercycle (pipe replacement / system expansion) completes and normalizes toward maintenance-only levels, **or**
- Net Debt/EBITDA sustainably falling below 2.5× (a large equity raise or multi-year EBITDA growth outpacing debt growth), **or**
- A documented, filing-sourced breakdown showing CapEx is predominantly (>30%) growth-CapEx rather than maintenance, which would make Upgrade 1 (Owner Earnings) a legitimate substitute for FCF in a *future* re-evaluation — note this would still need to clear the unconditional "FCF-positive 3+ years" disqualifier independently, since that disqualifier has no growth-capex carve-out in the framework text.

No standing earnings-driven re-score is scheduled since this is not a held position; this entry is for-reference only unless one of the above triggers, or another Rule 9 event, occurs.

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — cash spent on physical assets (e.g. pipes, treatment plants) that are expected to provide value over multiple years. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. A negative figure means the business is consuming more cash than it generates from operations, after CapEx. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — measures how much of reported accounting profit actually shows up as real cash; a sustained low or negative ratio is a quality red flag. |
| **Hard disqualifier** | One of three quality-gate conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company outright regardless of its weighted Quality Score. HTO fails two of the three. |
| **Hybrid Upgrade** | One of seven specific rule add-ons (numbered 1–7) layered onto the base 6-phase framework; Upgrade 1 (Owner Earnings) and Upgrade 5 (Debt Gate asset-light override) are both discussed and found not to rescue HTO here. |
| **Moat** | A durable competitive advantage protecting a company's profits from competition; scored here via a 5-signal checklist. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; lower is safer. HTO's 6.35× is well over the framework's 2.5× standard ceiling. |
| **NOPAT** | Net Operating Profit After Tax — EBIT adjusted for taxes, used as the numerator in ROIC. |
| **Owner Earnings** | A Hybrid Upgrade (1) alternative to FCF — Net Income + D&A − *maintenance-only* CapEx — used when a large share of a company's CapEx is genuinely growth-related rather than upkeep. Discussed but not applied to HTO this session (no filing-sourced maintenance/growth CapEx split was available, and it would not override the unconditional FCF-positivity disqualifier in any case). |
| **Quality Score** | A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. HTO scores 31.1. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **ROE** | Return on Equity — Net Income ÷ Shareholders' Equity; shown for reference alongside ROIC. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. HTO's 4.76% is well below the framework's quality bar. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results; HTO's most recent full fiscal year (FY2025, ended 2025-12-31) is used here as the closest available TTM-equivalent. |
| **Treasury yield (10Y)** | The yield on 10-year US government bonds; a benchmark "risk-free" rate used in the Rate Environment Gate. Not applied here since the Quality Gate fails before Phase 02. |

## Sources

- [H2O America (HTO) Stock Analysis](https://stockanalysis.com/stocks/hto/)
- [H2O America (HTO) — Yahoo Finance](https://finance.yahoo.com/quote/HTO/)
- Yahoo Finance `quoteSummary` and `fundamentals-timeseries` APIs (live price, FY2022–FY2025 income statement, cash flow statement, balance sheet) — pulled directly 2026-06-30
- [US 10 Year Treasury Note Yield — TradingEconomics](https://tradingeconomics.com/united-states/government-bond-yield)
- [Federal Reserve H.15 Selected Interest Rates, 2026-06-29](https://www.federalreserve.gov/releases/h15/)

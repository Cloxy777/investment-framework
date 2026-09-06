# RESCORE — MCD (McDonald's Corporation)

**Date:** 06 Sep 2026
**Mode:** `--both` (default) — Quality Score gate re-check + valuation (moot given gate result)
**Status:** Not held (watchlist, not-in-portfolio). Rule 9 trigger: Q2 FY2026 earnings released 2026-08-04/05, not yet checked since the [2026-07-10 addendum](../watchlist/not-in-portfolio/MCD/MCD-2026-06-24.md).

## 1. Live price (Rule 0)

**$256.00** — IBKR `get_price_snapshot`, contract_id 9408 (NYSE), `ts` 1788566390, `is_close: false`. Change vs prior session (07-10, $277.22): **−7.66%** — below the >15% Rule 9 threshold on its own, but notable: price now sits essentially at the 52-week low ($255.49, per `misc_statistics`), down from 52w high $337.59.

## 2. Rule 9 checklist

| Category | Result |
|---|---|
| Earnings | **Yes — Q2 FY2026 reported 2026-08-04.** This alone triggers the re-check. Revenue $7,099M (+4% YoY), Net income $2,362M (+5%), adjusted EPS $3.38. |
| Guidance revision | Not identified as a formal guidance change in this pass; company response (new national digital flash offers, H2 marketing reallocation toward value) is operational, not a stated numeric guidance revision. |
| Management change | None found this window. |
| M&A | None found. |
| Macro shift | None specific to MCD beyond broadly-cited "consumer pressure." |
| >15% unexplained price move | No — −7.66% since 07-10, and it is explained (post-earnings comp deceleration, see below). |

**Net: Rule 9 fires on the earnings release.** Full Quality Score recompute performed below (same continuous-score approach as the 07-10 addendum, since the underlying Phase 01 binary verdict was already superseded by that addendum).

## 3. Data (sources cited; nothing invented)

**TTM through Q2 FY2026 (quarter ended 2026-06-30):**

| Metric | TTM value | Cross-check |
|---|---|---|
| Total Revenue | $27,703M (Q3'25 $7,078 + Q4'25 $7,009 + Q1'26 $6,517 + Q2'26 $7,099) | stockanalysis.com TTM $27,702M |
| Gross Profit | $15,896M | stockanalysis.com TTM (matches) |
| EBIT (Operating Income) | $12,663M (3,320+3,159+2,884+3,300) | stockanalysis.com TTM $12,664M |
| D&A | $2,266M (559+576+566+565) | stockanalysis.com cash-flow quarterly detail |
| **EBITDA (EBIT + D&A)** | **$14,929M** | derived |
| Net Income | $8,787M (2,278+2,164+1,983+2,362) | stockanalysis.com TTM (matches) |
| Operating Cash Flow | $11,344M | stockanalysis.com TTM $11,347M (rounding) |
| CapEx | $3,583M | stockanalysis.com TTM $3,586M (rounding) |
| Free Cash Flow | $7,761M | stockanalysis.com TTM (matches exactly) |
| Effective tax rate (TTM) | 21.99% | Gurufocus, "MCD Tax Rate %" (as of Mar 2026 TTM); consistent with 07-10 session's 21.89% basis |

**Balance sheet (2026-06-30, most recent quarter):**

| Metric | Value | Source |
|---|---|---|
| Total Debt | $54,604M | stockanalysis.com balance sheet |
| Cash and equivalents | $822M | stockanalysis.com balance sheet |
| Common Stockholders' Equity | −$1,023M (still negative, structural — buyback-funded) | stockanalysis.com balance sheet |
| **Net Debt (Total Debt − Cash)** | **$53,782M** | matches stockanalysis.com's own Net Debt figure (sign convention reversed there) |

**Revenue 3yr CAGR:** FY2022 $23,183M → FY2025 $26,885M → **CAGR 5.06%**, unchanged from the 06-24/07-10 sessions (FY2026 not yet a complete fiscal year, so the base window hasn't rolled forward).

## 4. Recomputed ratios (TTM through Q2 FY2026)

```
Net Margin (TTM)   = $8,787M / $27,703M = 31.72%    (07-10 TTM basis: 31.62% — essentially flat)
Gross Margin (TTM) = $15,896M / $27,703M = 57.38%   (07-10 TTM basis: 57.35% — essentially flat)

ROIC (TTM) — Invested Capital = Total Debt + Common Equity − Cash
  = $54,604M + (−$1,023M) − $822M = $52,759M
  NOPAT = EBIT $12,663M × (1 − 21.99%) = $9,879.1M
  ROIC = $9,879.1M / $52,759M = 18.72%   (07-10 basis: 18.95% — essentially flat, same methodology)

Net Debt/EBITDA (TTM) = $53,782M / $14,929M = 3.60×
  (07-10 TTM basis: 3.59× — essentially unchanged, still far above the 2.5× standard threshold)

FCF/NI conversion (TTM) = $7,761M / $8,787M = 88.32%
  (07-10 TTM basis: 81.11% — improved, comfortably above 70%, no disqualifier)
```

**Comparable sales trajectory (the material change this session):**

| Quarter | Global comps | US comps |
|---|---|---|
| Q4 FY2025 | +5.7% | — |
| Q1 FY2026 | +3.8% | +3.9% |
| **Q2 FY2026** | **+1.3%** | **+0.8%** |

Three consecutive quarters of deceleration. Management and press coverage attribute the Q2 slowdown to **execution issues, not a one-off event**: "an overload of limited-time promotions and menu confusion" that hurt US customer traffic and service times, explicitly **"persisted into July"** (i.e., continuing into Q3, not a quarter-bound blip) — [IndexBox](https://www.indexbox.io/blog/mcdonalds-q2-2026-traffic-slows-amid-promotion-overload-and-menu-confusion/). McDonald's own characterization was a **"meaningful deceleration"** — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/mcdonald-beats-estimates-comparable-sales-114550305.html). Company response (new national digital flash offers, H2 marketing reallocation toward value) is a corrective *reaction* to an already-identified ongoing problem, not evidence the deceleration has already reversed.

## 5. Quality Score Engine — recomputed

Per [framework/quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29, unchanged):

| Sub-score (weight) | Inputs | Value |
|---|---|---|
| Profitability (25%) | NetMargin_Component clamp(31.72/30×100) = **100.0** (capped); ROIC_Component clamp(18.72/30×100) = **62.4**; no FCF-positivity cap (FCF positive every period checked) | (100.0+62.4)/2 = **81.2** |
| Margins (15%) | GrossMargin_Score clamp(57.38/80×100) = 71.73; no structural-trend bonus — gross margin still flat in the 56.75–57.41% band, no multi-year expansion | **71.73** |
| Growth (20%) | Growth_Score base clamp(5.06/25×100) = 20.24; **−10 deceleration modifier** (documented: 3 consecutive quarters of comp-sales deceleration, 5.7%→3.8%→1.3% global, driven by cited execution/traffic issues explicitly said to persist into the following quarter — not a single-quarter cyclical blip). The +10 pricing-power modifier applied last session is **removed**: check growth alone no longer offsets a traffic decline management itself calls a "meaningful deceleration." | 20.24 − 10 = **10.24** |
| Balance Sheet (15%) | Net Debt/EBITDA (TTM) 3.60× → 100×(1−3.60/4). No asset-light override (restaurant franchisor) | **10.0** — **hard disqualifier fires independently** (>2.5× standard threshold) |
| Moat (15%) | Unchanged from 07-10: **Brand premium/pricing power TRUE** (comps still positive on price/mix even as traffic falls) and **Scale cost advantage TRUE** (largest US buyer of beef/pork/potatoes, ~15% procurement cost edge — unchanged structural fact, no new citation needed this session). Market share, network effect, switching costs remain FALSE (Q2 traffic decline is if anything a headwind to the market-share signal, reinforcing the prior FALSE) | **40.0** |
| FCF Quality (10%) | TTM FCF/NI = 88.32% → clamp(((0.8832−0.40)/0.60)×100) | **80.53** |

```
Quality Score = 81.2×0.25 + 71.73×0.15 + 10.24×0.20 + 10.0×0.15 + 40.0×0.15 + 80.53×0.10
              = 20.300 + 10.7595 + 2.048 + 1.500 + 6.000 + 8.053
              = 48.660 → rounds to 48.7
```

**Quality Score = 48.7 / 100.0 — fails the 80.0+ gate, down from 51.6 (2026-07-10).** Fails two independent ways at once, same structure as every prior MCD evaluation:

1. **The weighted score itself** (48.7 < 80.0) — the drop from 51.6 is driven almost entirely by the Growth sub-score flipping from a +10 pricing-power bonus to a −10 deceleration penalty (30.24 → 10.24), on top of an already-weak base CAGR.
2. **A hard disqualifier, independent of the weighted score:** Net Debt/EBITDA (3.60×) remains well above the 2.5× standard threshold. No asset-light override applies.

FCF-positivity and FCF/NI-conversion hard disqualifiers do **not** fire (FCF positive every period checked; FCF/NI conversion 88.32% TTM, comfortably above 70%).

## 6. Valuation Score / Composite Score

**Not computed.** Per [quality-scoring.md](../framework/quality-scoring.md), Phase 02 valuation scoring and the Composite Score require clearing the 80.0+ Quality gate first. MCD does not (48.7), so no Rate Environment Gate or Phase 02 work was performed — moot given the gate result, consistent with every prior MCD session.

## 7. Recommendation

**PASS — Quality Score 48.7/100.0, fails the 80.0+ gate (also independently failed by the Net Debt/EBITDA hard disqualifier). Do not enter.** No position held, nothing to log in `decisions/`. Quality has *worsened* since the last check (51.6 → 48.7), driven by a documented, management-acknowledged comp-sales deceleration — this reinforces rather than challenges the standing PASS.

## Next review trigger

MCD's Q3 FY2026 earnings (expected ~early November 2026, standard MCD calendar); confirmation of whether the Q2 execution issues (promotion overload, menu confusion, US traffic decline) resolve or worsen through Q3 — the framework's stated flip conditions remain unchanged: a sustained re-acceleration in comps/unit growth pushing 3yr revenue CAGR materially above 8–10% (currently 5.06%), or an announced, credible multi-year deleveraging plan bringing Net Debt/EBITDA toward ~2.5× (currently 3.60×, essentially flat this quarter); or a >15% unexplained price move from $256.00. Routine Telegram mentions absent new fundamental information should continue to be logged as "last checked, no change."

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file — every term used in this session (CAGR, EBIT/EBITDA, FCF/NI conversion ratio, Hard disqualifier, Moat, NOPAT, Net Debt/EBITDA, Quality Score, ROIC, Rule 0, Rule 9, Comparable sales, TTM) is already defined there from prior MCD sessions; no new terms this pass.

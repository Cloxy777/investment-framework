# NEW POSITION — COHR (Coherent Corp.)

**Task type:** NEW POSITION
**Date:** 2026-08-14
**10Y US Treasury Yield:** 4.645% (Trading Economics / market commentary, 2026-08-14 — see Sources)
**Rate Regime Modifier (would apply if Phase 02 were reached):** 3.5–5% bracket → +5 (not applied — Quality Gate fails before Phase 02, same as the prior session)
**Current portfolio weight:** 0% (not held — absent from [holdings.md](../portfolio/holdings.md); confirmed via direct grep this session)

**Trigger:** Scheduled re-check per the prior [2026-07-28 COHR session](2026-07-28-new-position-cohr.md)'s stated "Next Review Trigger" — COHR's FY2026 Q4 / full-fiscal-year earnings, released 2026-08-12 (Rule 9 mandatory re-valuation event: quarterly earnings release). This is a full `/new-position` re-run, not a `/rescore` (COHR is still not held), using entirely fresh data pulled this session — no figure is carried over from the prior session's calculations.

## Data gaps flagged upfront

- **Owner Earnings (Hybrid Upgrade 1) still cannot be precisely computed** — same gap as the 2026-07-28 session. Coherent's FY2026 capex ramp is again documented as capacity-expansion (growth) capex by management, but the company still does not disclose a maintenance-vs-growth CapEx split. The FCF-based sub-scores below use unadjusted GAAP FCF, which is very likely more punitive than a true Owner-Earnings-adjusted picture would be.
- **Net income data-provider discrepancy**: stockanalysis.com's aggregated FY2026 net income figure ($769.9M) does not reconcile with the disclosed GAAP diluted EPS ($4.12) and diluted share count (195.4M) — $769.9M ÷ 195.4M = $3.94/share, not $4.12. The SEC-8-K-sourced figure of **$805.0M** ($805.0M ÷ 195.4M = $4.12/share) is internally consistent and used as the primary, scored figure; the discrepancy is flagged, not silently resolved by picking whichever number is more favorable.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price (2026-08-14, intraday)** | **$334.82** | IBKR market-data snapshot (`get_price_snapshot`, contract 584127832, NYSE), `last` field |
| Bid / Ask | $334.75 / $334.99 | Same IBKR snapshot |
| Change on the day | +$7.59 / +2.32% | Same IBKR snapshot |
| Day volume (partial session at time of pull) | 3,326,596 shares | Same IBKR snapshot |
| 52-week range | $84.43 – $440.00 | Same IBKR snapshot (`misc_statistics`) |
| 52-week-ago open | $91.10 | Same IBKR snapshot |
| Market cap (at $334.82, 195.64M shares) | ~$65.5B | shares outstanding 195,639,321 (stockanalysis.com, cross-checked against IBKR) × $334.82 |
| Cross-check | $333.90, +2.04% (as of the same date) | stockanalysis.com — consistent with the IBKR live tick within normal intraday movement |

No fair-value/order-setup calculation depends on the exact tick this session either (evaluation again stops at the Quality Gate, before Phase 02) — shown for completeness and audit-trail purposes per Rule 0.

## 2. Company Identification

Unchanged from the 2026-07-28 session: **COHR = Coherent Corp.** (formerly II-VI Incorporated), NYSE-listed. **Sector: Technology — Scientific & Technical Instruments / Photonics.** Three segments: Networking (transceivers, optical components for datacenter/telecom), Materials (engineered materials, lasers, laser optics), Lasers (industrial/scientific laser systems). NVIDIA holds a $2B equity stake in Coherent alongside a multi-year co-packaged-optics (CPO) supply agreement (announced 2026-05-06).

**What's changed since 2026-07-28:** Coherent reported **Q4 and full-year FY2026 results on 2026-08-12** (fiscal year ended 2026-06-30) — record Q4 revenue of $2.05B (+34% Y/Y), record full-year revenue of $7.12B, GAAP profitability for the full year (net income $805.0M vs. a net loss the prior year), but a **full fiscal year of sharply negative free cash flow** (−$1.02B) driven by a large, continuing InP (indium phosphide) capacity-expansion capex program — the same capex story flagged in July, now realized across a complete fiscal year rather than a single partial quarter. Management guided Q1 FY2027 revenue of $2.2–$2.4B and reiterated a target of a >$3B quarterly revenue run-rate by the end of FY2027, with record bookings extending into calendar 2028.

## 3. Phase 01 — Quality Score (per quality-scoring.md)

### Data used

All figures below are **FY2026 (fiscal year ended 2026-06-30)** — Coherent's fiscal year exactly matches a trailing-twelve-month window as of this session's date (2026-08-14), since Q4 FY2026 was just reported. Sourced from Coherent's own 2026-08-12 earnings release (via SEC 8-K exhibit, reproduced by stocktitan.net and stockanalysis.com) and cross-checked against `yfinance` for FY2022–FY2025 history.

| Metric ($M unless noted) | FY2022 | FY2023 | FY2024 | FY2025 | **FY2026** |
|---|---|---|---|---|---|
| Revenue | 3,316.62 | 5,160.10 | 4,707.69 | 5,810.12 | **7,118.20** |
| Gross profit | 1,265.50 | 1,618.28 | 1,455.96 | 2,043.32 | **2,669.00** |
| Gross margin | 38.16% | 31.36% | 30.93% | 35.17% | **37.50%** |
| Operating income (EBIT, GAAP) | 403.06 | (68.69) | 140.83 | 337.43 | **897.90** |
| Pretax income | 281.81 | (355.56) | (147.65) | 94.18¹ | **847.70** |
| Tax provision | 47.05 | (96.10) | 11.12 | 64.12¹ | **60.80** |
| Effective tax rate | 16.70% | n/m (neg. pretax) | n/m (neg. pretax) | 68.08%¹ | **7.17%** |
| Net income (GAAP) | 234.76 | (259.46) | (156.15) | (80.56)² | **805.00**³ |
| Net margin | 7.08% | (5.03%) | (3.32%) | (1.39%) | **11.31%** |
| Operating cash flow | 413.33 | 634.03 | 545.73 | 633.60 | **79.50** |
| CapEx | (314.33) | (436.06) | (346.82) | (440.84) | **(1,102.90)** |
| **Free cash flow (OCF − CapEx)** | **99.00** | **197.97** | **198.92** | **192.76** | **(1,023.40)** |
| Total debt | 2,438.21 | 4,488.82 | 4,303.15 | 3,893.66 | **3,222.20** |
| Cash & equivalents | 2,582.37 | 821.31 | 926.03 | 909.20 | **1,162.00** |
| Total equity (incl. noncontrolling interest) | 4,383.28 | 7,228.97 | 7,946.28 | 8,481.28 | **11,238.20** |
| D&A | 286.78 | 681.69 | 559.76 | 553.60 | **~516.20**⁴ |

¹ FY2025 figures shown here are full-fiscal-year (`yfinance` annual series); the prior session's table used a TTM-through-Q3 window and slightly different net income (−$80.56M common-basis), which is retained here for the trend row.
² FY2025 net income shown on a total (pre-common-adjustment) basis for consistency with the FY2026 column; matches the July session's TTM-basis figure directionally.
³ **FY2026 net income: $805.0M, GAAP diluted EPS $4.12** — internally consistent (805.0 ÷ 195.4M diluted shares = $4.12). See the data-gap note above re: a conflicting $769.9M figure from a secondary aggregator, not used.
⁴ FY2026 D&A reconstructed as: Q1–Q3 FY2026 actual D&A (from `yfinance` quarterly cash flow, $381.33M) + implied Q4 D&A (TTM D&A of $516.15M per a third-party data aggregator minus the Q1–Q3 sum = $134.82M, consistent in magnitude with prior quarters' $122–147M range). Shown to 1 decimal as ~$516.2M.

**Effective tax rate flag:** FY2026's 7.17% GAAP effective tax rate is unusually low — pretax income included a **$124.1M gain on business sale** and a **$74.0M gain on investment sale**, partly offset by **$63.4M restructuring charges** and **$64.4M asset impairment** (all company-disclosed, non-recurring items per the earnings release). Coherent's own guided **normalized non-GAAP tax rate for FY2026 was 19%**. Per Rule 6 ("normalize before you value" — cited here for transparency even though it's formally a fair-value-methodology rule, not a quality-score rule) and "show every calculation," both the actual (7.17%) and normalized (19%) rates are shown below; **the actual rate is used as the primary scored NOPAT/ROIC input** (it is the real, filed figure — using the guided rate instead would substitute a company-provided estimate for a filed fact), with the normalized version shown as an explicit sensitivity check, not silently substituted.

**Revenue 3yr CAGR — window note.** This session uses **FY2023 → FY2026** (the current rolling 3-fiscal-year window, per the 2026-08-05 rolling-window clarification's general "the window rolls forward as each new fiscal year reports" principle, applied here to the CAGR metric for the first time): (7,118.20 / 5,160.10)^(1/3) − 1 = **11.32%**. This is materially lower than the July session's 20.55% (FY2022→FY2025) because that older window's base year (FY2022→FY2023) captured the II-VI/Coherent merger's inorganic revenue jump (+55.6% in one year) — the FY2023→FY2026 window used here reflects fully organic, post-merger growth instead, which is the more decision-relevant read of underlying trend per Rule 6's spirit.

### Hard disqualifier check (fires regardless of weighted score — quality-scoring.md)

| Hard disqualifier | Applies to COHR? | Basis |
|---|---|---|
| FCF/NI conversion ratio <70% for 2+ consecutive years, no documented growth-capex explanation | **Does NOT fire** | Current rolling window = FY2025, FY2026 (most recently completed fiscal years, per the 2026-08-05 rolling-window clarification). **FY2025:** net income was negative (−$80.56M common-basis) → ratio not meaningful, and per this same ticker's own 2026-07-28 session precedent, a negative-NI year is treated as NM rather than a counted "<70%" failure instance (the check's design intent — "how much of reported profit shows up as cash" — doesn't apply when there's no profit to convert). **FY2026:** net income positive ($805.0M), FCF/NI = −1,023.40/805.00 = **−127.1%**, clearly <70%. This is the only counted failure instance in the current 2-year window — **1 year, not "2+ consecutive"** — so the disqualifier does not fire on the count alone. It also carries a **documented growth-capex explanation** (InP capacity expansion; CEO/CFO commentary on the 2026-08-12 call about continuing capacity investment and capex "expected to increase further sequentially," record bookings extending into calendar 2028) — the same carve-out basis as July, now for a full fiscal year rather than a partial one. |
| Net Debt/EBITDA over its applicable threshold (2.5× standard) | **Does NOT fire** | Net Debt = $3,222.20M − $1,162.00M = $2,060.20M. EBITDA = EBIT $897.90M + D&A ~$516.20M = $1,414.10M. Net Debt/EBITDA = **1.457×**, comfortably under 2.5× (COHR is not an asset-light payment network/exchange, so the Upgrade 5 override is irrelevant here anyway). |
| Not FCF-positive for 3+ consecutive years | **Does NOT fire, but this is now a materially worse, confirmed trend** | Most recent 3 fiscal years: FY2024 +$198.92M, FY2025 +$192.76M, **FY2026 −$1,023.40M**. Only the most recent year is negative — not 3 consecutive negative years, so the disqualifier does not fire. But unlike July (where the negative figure was only a partial-year/TTM artifact through Q3), **this is now a complete, reported fiscal year of deeply negative free cash flow** — a real, confirmed trend, not a quarter-to-quarter timing effect. This also triggers the Profitability sub-score's FCF-positivity cap (see below), though non-bindingly. |

**No hard disqualifier fires** — same conclusion as July — but the underlying facts are, if anything, more stark: a full fiscal year of FCF burn is now on the record rather than a single elevated quarter.

### Weighted Quality Score (computed in full per "show every calculation")

| Sub-score (weight) | Inputs | Calculation | Result |
|---|---|---|---|
| **Profitability** (25%) | Net margin 11.31%, ROIC 6.73% (both FY2026) | NetMargin_Component = clamp((11.31/30)×100) = 37.70. ROIC_Component = clamp((6.73/30)×100) = 22.44. Avg = (37.70+22.44)/2. *FCF-positivity cap check: FY2026 breaks the 3-consecutive-year positive-FCF streak (see disqualifier table above), so the Profitability_Score cap of 40.0 technically applies — non-binding here since the raw score (30.07) is already below 40.0.* | **30.07** |
| **Margins** (15%) | Gross margin 37.50% (FY2026); 3yr FY trend 30.93% (FY24) → 35.17% (FY25) → 37.50% (FY26) | clamp((37.50/80)×100) = 46.87; **+10 structural-trend bonus** — a genuine, monotonic 3-consecutive-fiscal-year expansion while still below the 40% static threshold, per quality-scoring.md's explicit "below 40% but moving the right direction" carve-out | **56.87** |
| **Growth** (20%) | Revenue 3yr CAGR (FY23→FY26) 11.32% | clamp((11.32/25)×100) = 45.28; **+10 documented TAM-expansion evidence** (NVIDIA $2B equity stake + multi-year CPO supply agreement; record bookings extending into calendar 2028 per the 2026-08-12 call; management's own >$3B-quarterly-revenue-by-end-of-FY2027 target; continuing InP capacity doubling — independently corroborated, see Sources) | **55.28** |
| **Balance Sheet** (15%) | Net Debt/EBITDA 1.457× (FY2026) | clamp(100×(1−1.457/4)) | **63.58** |
| **Moat** (15%) | 3 of 5 signals marked true (unchanged from July, re-verified this session — see below) | (3/5)×100 | **60.00** |
| **FCF Quality** (10%) | FCF/NI ratio (FY2026) = −1,023.40/805.00 = −1.271 | clamp(((−1.271−0.40)/0.60)×100) = clamp(−278.6) — **floored at 0**; flagged as capex-timing-driven per the Owner Earnings data-gap note, not an earnings-quality failure in the Valeant/Wirecard sense, but now a full-fiscal-year fact rather than a partial-year one | **0.00** |

**Moat signal detail (re-verified this session, cited per quality-scoring.md's "do not mark a signal true without a cited source"):**
- ✅ **Market share stable or growing** — Coherent led the **overall** global optical transceiver market with **>22.2% share in 2025** (unchanged citation, GMI/gminsights.com). **New nuance found this session, not used to flip the signal but flagged as a genuine competitive risk**: in the fastest-growing **800G** segment specifically, InnoLight Technology (China) is reported as the 2026 leader with ~35% share of 800G module shipments, deep NVIDIA/Google/hyperscaler partnerships, and >92% yield rates — a different, narrower scope than the overall-market figure Coherent's signal is based on, so it doesn't contradict the "overall share stable/growing" claim, but it is real, cited evidence of segment-specific competitive pressure worth carrying into the qualitative bear case. [Sources: gminsights.com, mordorintelligence.com — see Sources.]
- ❌ Brand premium — no cited ASP/pricing-power-without-volume-loss evidence sourced this session either.
- ❌ Network effect — not applicable to Coherent's component/hardware-supplier business model (unchanged).
- ✅ **Switching costs** — unchanged basis: 12–24 month datacenter-optics supplier qualification cycles industry-wide, Coherent's vertical integration (materials-to-module). Reinforced this session by the 2026-08-12 call's disclosure of **record bookings extending into calendar 2028** — a multi-year forward-order visibility consistent with genuine platform-level lock-in, not just a one-quarter pop.
- ✅ **Scale cost advantage** — unchanged basis: the 3-inch→6-inch InP wafer transition disclosed on the 2026-05-06 call (>4× devices/wafer at <half the cost/device).

```
Quality Score = (30.07 × 0.25) + (56.87 × 0.15) + (55.28 × 0.20) + (63.58 × 0.15) + (60.00 × 0.15) + (0.00 × 0.10)
              = 7.5175 + 8.5305 + 11.056 + 9.537 + 9.000 + 0.000
              = 45.64
              → rounds to 45.6
```

**Quality Score: 45.6 / 100.0 — fails the 80.0+ gate.** No hard disqualifier independently fires. Per [quality-scoring.md](../framework/quality-scoring.md) and the operating brief: **this stops the evaluation here — no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order setup is computed.**

**Why the score moved (48.6 → 45.6) despite full-year GAAP profitability turning positive:** Profitability (19.34→30.07) and Margins (45.97→56.87) both **improved** — Coherent is genuinely more profitable and margin-expanding than it looked in July. But **Growth fell sharply (92.20→55.28)**, almost entirely because the rolling 3-year CAGR window now excludes the merger-inflated FY2022→FY2023 base year (see window note above) — this is a methodology artifact of time passing and the window rolling forward, not a deterioration in the business's actual growth rate. The net effect is a slightly lower overall score, but the *underlying* fundamentals are trending toward the gate, not away from it (better profitability, better margins, unchanged strong balance sheet and moat) — the still-large gap to 80.0 is driven almost entirely by two structural issues: unremarkable-for-the-gate ROIC (6.73%, vs. a 15%+ Phase 01 norm) and the FCF Quality sub-score being floored at zero by the ongoing, now-fiscal-year-confirmed capex-driven cash burn.

## 4. Recommendation

**PASS — do not enter, do not open a standard watchlist limit-order posture.** Same conclusion as 2026-07-28, now confirmed with a full fiscal year of post-merger, post-NVIDIA-investment data rather than a partial-year snapshot. Coherent remains the clear overall-market leader in a fast-growing, structurally important market (optical connectivity for AI datacenters), now with a full year of **positive GAAP net income** and **expanding gross margins** (37.50%, up from 30.93% two years ago) to show for it. But it still fails this framework's strict 80.0+ Quality Gate by a wide margin (45.6) because **ROIC remains well under the framework's quality bar** (6.73% TTM/FY2026, vs. 15%+ implied by the sub-score's scaling) and **free cash flow just posted its first full fiscal year of deep negative territory** (−$1.02B) as the company front-loads a large, real InP capacity-expansion program. As in July, this is a name whose story is forward-looking (capacity built now, for demand growth later, with record bookings into 2028) in a way this framework's *trailing*-financials-weighted Quality Score is not built to credit on the front end.

**Still a "revisit later" name, not a "never" name.**

## 5. Next Review Trigger

Re-evaluate on any of the following:
- **FY2027 Q1 earnings** — based on the prior 3 years' reporting pattern (Q1 FY2026 reported 2025-11-05, Q3 FY2026 reported 2026-05-06, Q4 FY2026 reported 2026-08-12), Q1 FY2027 is expected in early-to-mid November 2026; **exact date not yet officially announced as of this session, so not stated as a fact — flagged as a pattern-based expectation only.** This will show whether the FY2026 capex ramp (and associated FCF burn) is continuing at the same intensity, moderating, or has peaked, per management's own "capex expected to increase further sequentially" guidance from the 2026-08-12 call.
- A **maintenance-vs-growth CapEx breakdown** becoming available (10-K disclosure, investor-day materials, explicit management commentary) — still the single change most likely to materially move the Profitability and FCF Quality sub-scores via a proper Owner Earnings calculation.
- **2+ consecutive quarters of ROIC recovering toward the mid-teens** as new InP capacity comes online and is utilized — a genuine, not merely capex-timing-driven, re-trigger.
- Any Rule 9 event: guidance revision, M&A, management change, or a >15% unexplained price move.

No valuation score exists for COHR (fails at the Quality Gate again), so no stale-score flag applies and none is created in [watchlist/STALE.md](../watchlist/STALE.md) (consistent with the 2026-07-28 session and the STALE.md registry's explicit "Phase 01 FAIL / not scored" exclusion).

## Glossary

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year — a quick gauge of where the current price sits within its recent trading history. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets (factories, equipment, data centers). |
| **Co-packaged optics (CPO)** | A chip-packaging approach that mounts optical (light-based) data-transmission components directly next to/inside the same package as a switch or accelerator chip — reduces power consumption and boosts bandwidth density for AI-cluster networking. NVIDIA's 2026 supply agreement with Coherent covers CPO components. |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **Diluted EPS** | Earnings per share calculated using a fully diluted share count (including the dilutive effect of options, RSUs, and convertible securities) — a more conservative per-share profit figure than basic EPS. Used here to cross-check and select between two conflicting net-income figures from different data providers. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **Effective tax rate** | The actual percentage of a company's pretax income paid as income tax in a given period (tax provision ÷ pretax income) — distinct from the statutory tax rate. COHR's FY2026 rate (7.17%) is unusually low, flagged this session as driven by one-time gains rather than a sustainable tax position. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. A negative figure means the business is consuming more cash than it generates from operations, after CapEx. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — measures how much of reported accounting profit actually shows up as real cash; a sustained low or negative ratio is a quality red flag, though a documented growth-capex explanation (as here) is an explicit carve-out from the hard-disqualifier version of this check. |
| **Hard disqualifier** | One of three Quality Score conditions ([quality-scoring.md](../framework/quality-scoring.md)) that fails a company regardless of its weighted sub-score total. None fired for COHR this session. |
| **Indium phosphide (InP)** | A compound semiconductor material used to make the lasers and photodetectors inside optical transceivers — the material at the center of the 2026 industry-wide AI-datacenter supply shortage and the subject of Coherent's ongoing capacity-expansion capex program. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) that has been put to work in a business — the denominator in a Return on Invested Capital (ROIC) calculation. This session uses the framework's documented formula (debt + equity − cash, per glossary.md), applied to total equity including noncontrolling interest to match EBIT's fully-consolidated basis. |
| **Moat** | Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors; scored here via a 5-signal checklist. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. |
| **NCI (Noncontrolling Interest, a.k.a. Minority Interest)** | The portion of a consolidated subsidiary's equity (and, on the income statement, its earnings) that belongs to outside shareholders rather than the parent company filing the financial statements — required under GAAP when a company owns less than 100% of a subsidiary but still controls and must fully consolidate it. Coherent carries ~$335M of NCI on its balance sheet, relevant to correctly scoping Invested Capital against EBIT's fully-consolidated basis. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — operating profit after a tax adjustment but before financing costs; the numerator this framework uses to compute ROIC. |
| **Optical transceiver** | A module that converts electrical data signals into light (optical) signals for transmission over fiber-optic cable, and back again at the receiving end — the core product category connecting servers/switches inside and between AI data centers. Coherent led this market with >22.2% overall global share in 2025, though a narrower, faster-growing 800G sub-segment is reportedly led by a different competitor (InnoLight) — see Moat signal detail. |
| **Owner Earnings** | Warren Buffett's adjusted cash-flow measure: Net Income + D&A − *Maintenance* CapEx only (excludes growth CapEx). Still could not be precisely computed for COHR this session — same disclosed-data gap as July. |
| **Qualification cycle (supplier)** | The multi-month-to-multi-year process a customer must run to test, validate, and approve a supplier's component before it can be designed into production — typically 12–24 months in datacenter optics; a documented Switching Costs moat-signal mechanism. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading profitability, margins, growth, balance sheet, moat signal, and FCF quality. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. COHR scores 45.6 this session (48.6 in July). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 6** | This framework's fair-value-methodology instruction to normalize earnings/margins before valuing a business — strip out one-time items, use cycle-normalized figures. Cited here (for transparency, not as a binding quality-score rule) re: COHR's unusually low FY2026 effective tax rate. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move. This session's trigger. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. COHR's FY2026 6.73% remains well below the framework's quality bar. |
| **Rolling-window (disqualifier/metric test)** | This framework's convention (clarified 2026-08-05) that trailing-year tests (FCF-positive streaks, FCF/NI conversion, revenue CAGR) are evaluated against the most recently completed fiscal years available at the time of scoring, not a fixed historical window — the window "rolls forward" as each new fiscal year reports. Applied this session to both the hard-disqualifier check and, for the first time, the Growth sub-score's CAGR window. |
| **Treasury yield (10Y)** | The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate. Recorded here for the session header but not applied, since the Quality Gate fails before Phase 02. |

## Sources

- IBKR market-data snapshot (live price, bid/ask, change, 52-week stats) — pulled directly 2026-08-14
- `yfinance` (annual/quarterly income statement, cash flow, and balance sheet, FY2022–FY2026 partial) — pulled directly 2026-08-14
- [Coherent Corp. Reports Fourth Quarter and Full Year Fiscal 2026 Results — GlobeNewswire](https://www.globenewswire.com/news-release/2026/08/12/3344051/11543/en/coherent-corp-reports-fourth-quarter-and-full-year-fiscal-2026-results.html)
- [Coherent Corp. FY2026 Q4/Full-Year Results — company press release](https://www.coherent.com/news/press-releases/fourth-quarter-and-fiscal-year-2026-results)
- [Coherent FY26 Earnings: Q4 Revenue Hits $2.05B — StockTitan (full income statement/balance sheet detail)](https://www.stocktitan.net/news/COHR/coherent-corp-reports-fourth-quarter-and-full-year-fiscal-2026-4dp7hm0orxpy.html)
- [Coherent (COHR) Stock Price & Overview — stockanalysis.com](https://stockanalysis.com/stocks/cohr/)
- [Coherent (COHR) Financials — stockanalysis.com](https://stockanalysis.com/stocks/cohr/financials/)
- [Coherent (COHR) Statistics & Valuation — stockanalysis.com](https://stockanalysis.com/stocks/cohr/statistics/)
- [Coherent Q4 results feature 34% revenue surge and improving gross margin — Seeking Alpha](https://seekingalpha.com/news/4631806-coherent-q4-results-feature-34-revenue-surge-and-improving-gross-margin)
- [Coherent (COHR) Delivers Strong Fiscal Q4 Results on AI-Driven Demand — Tickeron](https://tickeron.com/blogs/coherent-cohr-delivers-strong-fiscal-q4-results-on-ai-driven-demand-15663/)
- [Coherent Targets First $3B Quarter by Fiscal 2027 — BigGo Finance (Q4 FY2026 earnings-call summary)](https://finance.biggo.com/news/US_COHR_2026-08-12)
- [Optical Transceiver Market Size & Share — GMI/gminsights.com](https://www.gminsights.com/industry-analysis/optical-transceiver-market)
- [Optical Transceiver Market Size, Growth Drivers — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/optical-transceiver-market)
- [US 10 Year Treasury Note Yield — TradingEconomics](https://tradingeconomics.com/united-states/government-bond-yield)
- [2026-07-28 COHR session (prior evaluation, superseded by this one)](2026-07-28-new-position-cohr.md)

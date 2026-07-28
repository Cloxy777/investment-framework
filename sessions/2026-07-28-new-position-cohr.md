# NEW POSITION — COHR (Coherent Corp.)

**Task type:** NEW POSITION
**Date:** 2026-07-28
**10Y US Treasury Yield:** ~4.62–4.64% (TradingEconomics / market commentary, 2026-07-28 — see Sources; not pinned to a single FRED print this session since the evaluation stops before Phase 02, see below)
**Rate Regime Modifier (would apply if Phase 02 were reached):** 3.5–5% bracket → +5 (not applied — Quality Gate fails before Phase 02)
**Current portfolio weight:** 0% (not held — absent from [holdings.md](../portfolio/holdings.md); no prior watchlist entry existed for COHR before this session)

**Trigger:** Routine 6 (Telegram Stock-Mention Scan) — [t.me/FinnInvestChannel](https://t.me/FinnInvestChannel), post FinnInvestChannel/2999 (~10:31 UTC 2026-07-28), reporting Lumentum CEO Michael Hurlston's comment that an indium-phosphide (InP) laser shortage for AI could exceed the memory-chip shortage, and that NVIDIA has invested in both Lumentum and Coherent (COHR) because of it. Per the telegram-scan trigger rule, no watchlist entry existed for COHR → full `/new-position` run. **The Telegram post itself was used only as the trigger — no figure from it was used as financial data; every number below was independently and freshly fetched per Rule 0 and cross-checked against primary/company-disclosed sources.**

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Last regular-session close (2026-07-27)** | **$271.31** (−3.92% / −$11.08 on the day) | Yahoo Finance `quoteSummary`/chart API, `regularMarketPrice`, timestamp 2026-07-27 20:00:03 UTC (4:00pm ET close), NYSE |
| **Live pre-market quote (2026-07-28, as of this session)** | **$257.48**, last 1-minute tick at 12:27:20 UTC (8:27am ET) | Yahoo Finance 1-minute intraday chart API, `marketState: PRE` — regular session had **not yet opened** (opens 9:30am ET / 13:30 UTC) at the time of this pull |
| Reported pre-market change (separate snapshot) | −5.44% ($256.54) vs. prior close | Yahoo Finance `quoteSummary` `price` module, pre-market snapshot ~12:21 UTC |
| Day range (2026-07-27) | $256.22 – $283.14 | Same source |
| 52-week range | $84.35 – $440.00 | Same source |
| All-time high | $440.00 | Same source |
| 200-day average | $252.39 | Same source |
| 50-day average | $357.95 | Same source (reflects the stock's steep July 2026 decline from the $350s) |
| Market cap (at $271.31 close) | $53.08B | shares outstanding 195,639,321 × $271.31 |
| Shares outstanding | 195,639,321 | Yahoo Finance `defaultKeyStatistics` |

**No fair-value/order-price calculation in this session depends on the exact live tick** (the evaluation stops at the Quality Gate below, before any Phase 02/fair-value math), so the pre-market vs. regular-session distinction doesn't introduce calculation risk here — both figures are shown for completeness and because a large, still-moving price gap (previous close $271.31 → pre-market $257.48, a further ~5% move) is itself a fact worth recording for any future re-check.

**Context on the July 2026 decline (Rule 9 / qualitative, not used as a scored input):** COHR fell from the $350s in early July to $271.31 by 2026-07-27, part of a broader photonics/optical-communications sector pullback (Lumentum, Ciena, Applied Optoelectronics all fell over the same window) attributed to profit-taking after months of AI-driven gains, not a COHR-specific fundamental miss — COHR's next earnings release (FY2026 Q4, fiscal year ended 2026-06-30) is scheduled for **2026-08-12**, after this session. [Sources: GuruFocus, 247wallst.com — see Sources section.]

## 2. Company Identification

**COHR = Coherent Corp.** (formerly II-VI Incorporated; renamed September 2022 after the II-VI/Coherent Inc. merger), NYSE-listed. **Sector: Technology — Scientific & Technical Instruments / Photonics.** Three segments: Networking (transceivers, optical components for datacenter/telecom), Materials (engineered materials, lasers, laser optics), Lasers (industrial/scientific laser systems). Headquartered in Saxonburg, PA. ~30,200 full-time employees.

Directly relevant to the trigger: Coherent is the #1 named competitor/partner alongside Lumentum in the indium-phosphide laser supply story — NVIDIA holds a **$2B equity stake** in Coherent alongside a multi-year co-packaged-optics (CPO) supply agreement, announced on Coherent's Q3 FY2026 earnings call (2026-05-06). [BigGo Finance, Motley Fool transcript — see Sources.]

## 3. Phase 01 — Quality Score (per quality-scoring.md)

### Data used

All figures pulled directly 2026-07-28 via Yahoo Finance `quoteSummary` and `fundamentals-timeseries` APIs (annual = fiscal year ended June 30; TTM = trailing four quarters through 2026-03-31, the most recent reported quarter — COHR's Q4 FY2026, ended 2026-06-30, has not yet been reported as of this session).

| Metric ($M unless noted) | FY2022 | FY2023 | FY2024 | FY2025 | **TTM (thru 2026-03-31)** |
|---|---|---|---|---|---|
| Revenue | 3,316.62 | 5,160.10 | 4,707.69 | 5,810.12 | **6,602.08** |
| Gross profit | 1,265.50 | 1,618.28 | 1,455.96 | 2,043.32 | **2,428.11** |
| Gross margin | 38.16% | 31.36% | 30.93% | 35.17% | **36.78%** |
| EBIT | 403.06 | (68.69) | 140.83 | 337.43 | **710.07** |
| EBITDA | 689.84 | 613.00 | 700.59 | 891.03 | **1,226.22** |
| Net income (attributable to common) | 166.53 | (403.67) | (279.51) | (80.56) | **400.61** |
| Net margin (common basis) | 5.02% | (7.82%) | (5.94%) | (1.39%) | **6.07%** |
| Operating cash flow | 413.33 | 634.03 | 545.73 | 633.60 | **140.34** |
| CapEx | (314.33) | (436.06) | (346.82) | (440.84) | **(678.58)** |
| **Free cash flow (OCF − CapEx)** | **99.00** | **197.97** | **198.92** | **192.76** | **(538.24)** |
| Total debt | 2,438.21 | 4,488.82 | 4,303.15 | 3,893.66 | 3,425.11 (2026-03-31) |
| Cash & equivalents | 2,582.37 | 821.31 | 926.03 | 909.20 | 1,592.73 (2026-03-31) |
| Net debt | 708.06¹ | 3,488.49¹ | 3,174.19¹ | 2,777.72¹ | **1,832.39** (2026-03-31) |
| Net Debt/EBITDA | — | — | — | — | **1.494×** (TTM) |
| Invested capital | 5,471.58 | 8,852.03 | 9,310.33 | 9,331.44 | 11,477.59² (TTM avg) |

¹ Annual net-debt figures per Yahoo's `annualNetDebt` series, shown for context only — the Balance Sheet sub-score uses the current TTM figure.
² Average of invested capital at the start (2025-03-31, $9,084.42M) and end (2026-03-31, $13,870.76M) of the TTM window — see ROIC calc below; the large jump reflects the ~$2.1B stockholders'-equity increase in the quarter ended 2026-03-31, consistent with NVIDIA's $2B equity investment closing that quarter.

**FCF/NI conversion ratio:** FY2024 = 198.92 / (279.51) = not meaningful (negative NI); FY2025 = 192.76 / (80.56) = not meaningful (negative NI); **TTM = (538.24) / 400.61 = −134.4%** (negative — FCF and NI have opposite signs in the TTM window).

**Effective tax rate (TTM):** tax provision $53.23M ÷ pretax income $505.81M = **10.52%**.
**NOPAT (TTM) = EBIT × (1 − tax rate) = $710.07M × (1 − 0.1052) = $635.34M.**
**ROIC (TTM) = NOPAT ÷ Avg. Invested Capital = $635.34M ÷ $11,477.59M = 5.54%.**
*(Sensitivity check, not used: ROIC using period-end-only invested capital of $13,870.76M — i.e., fully loaded with the post-NVIDIA-raise capital base — is 4.58%, even lower. Either way ROIC is well under the Phase 01 15% threshold; the recent capital raise makes this quarter's denominator elevated relative to capital not yet deployed, which if anything modestly *understates* true underlying ROIC, but not by enough to change the conclusion.)*

**Revenue 3yr CAGR (FY2022→FY2025):** (5,810.12 / 3,316.62)^(1/3) − 1 = **20.55%**.

### Hard disqualifier check (fires regardless of weighted score — quality-scoring.md)

| Hard disqualifier | Applies to COHR? | Basis |
|---|---|---|
| FCF/NI conversion ratio <70% for 2+ consecutive years, no documented growth-capex explanation | **Does NOT fire — documented exception applies** | TTM FCF/NI is deeply negative (see above), driven by a CapEx surge from $154M (Q2 FY26) to $290M (Q3 FY26) — per Coherent's own Q3 FY2026 earnings call (2026-05-06), this capex is **explicitly company-disclosed as internal indium-phosphide capacity expansion** ("doubling internal 6-inch InP capacity ahead of schedule," "capex expected to increase further sequentially in Q4"), directly tied to the NVIDIA $2B equity stake/CPO supply agreement. This is a documented growth-capex explanation, so the hard-disqualifier text's explicit carve-out applies — flagged, not fired. |
| Net Debt/EBITDA over its applicable threshold (2.5× standard) | **Does NOT fire** | TTM Net Debt/EBITDA = 1.832B/1.226B = **1.494×**, comfortably under 2.5×. (COHR is not an asset-light payment network/exchange, so the Upgrade 5 4× override doesn't apply — irrelevant anyway since 1.494× clears the standard 2.5× threshold too.) |
| Not FCF-positive for 3+ consecutive years | **Does NOT fire (fiscal-year basis)** | All 4 of the last 4 **full fiscal years** (FY2022–FY2025) show positive FCF: $99.0M, $198.0M, $198.9M, $192.8M. The **TTM** figure (partial-year, through Q3 FY2026) is deeply negative (−$538.2M), driven by the same documented capex ramp above, but this disqualifier is framed in terms of consecutive fiscal years, not a rolling TTM window — so it is not triggered on a literal reading. **This is flagged prominently below as a major, current, real trend** (not dismissed), and is exactly the kind of fact pattern the framework's Upgrade 1 (Owner Earnings) exists to handle — see the data-gap note below. |

**No hard disqualifier fires**, but see the FCF Quality sub-score and the Owner Earnings/data-gap discussion below — the TTM cash-flow picture is genuinely weak and materially drags the weighted score even without a disqualifier firing.

**⚠️ Data gap — Owner Earnings (Hybrid Upgrade 1) cannot be precisely computed.** The Q3 FY2026 capex ramp is documented as growth/capacity-expansion capex (well over the 30% growth-CapEx threshold that triggers Upgrade 1 — in fact nearly all of the incremental TTM capex appears to be capacity expansion per management's own commentary), which would normally call for **Owner Earnings = Net Income + D&A − Maintenance CapEx only** in place of raw FCF. **Coherent does not publicly disclose a maintenance-vs-growth CapEx split** (no such figure was found in its filings, earnings-call transcripts, or press materials pulled this session). Per "never invent or estimate financial data," **this maintenance-CapEx figure is not fabricated** — the FCF Quality and FCF Yield sub-scores below use the reported (GAAP, unadjusted) TTM FCF figure instead, which is very likely **more punitive than the true Owner-Earnings-adjusted picture** would be, since it charges 100% of the capacity-expansion capex against cash flow. **This is a genuine, flagged limitation of this session's output, not a resolved calculation.**

### Weighted Quality Score (computed in full per "show every calculation")

| Sub-score (weight) | Inputs | Calculation | Result |
|---|---|---|---|
| **Profitability** (25%) | Net margin 6.07% (TTM), ROIC 5.54% (TTM) | NetMargin_Component = clamp((6.07/30)×100) = 20.23. ROIC_Component = clamp((5.54/30)×100) = 18.45. Avg = (20.23+18.45)/2. *(No FCF-positivity cap triggered — FY22–25 all FCF-positive.)* | **19.34** |
| **Margins** (15%) | Gross margin 36.78% (TTM); 3yr FY trend 38.16%→31.36%→30.93%→35.17%→36.78% (TTM) | clamp((36.78/80)×100) = 45.97; **no +10 trend bonus applied** — the trend dipped sharply (2022 merger-integration drag) before partially recovering, not a clean monotonic 3-year expansion; flagged as a judgment call, not invented as "expanding" without a clear pattern | **45.97** |
| **Growth** (20%) | Revenue 3yr CAGR 20.55% | clamp((20.55/25)×100) = 82.20; **+10 documented TAM-expansion evidence** (NVIDIA $2B equity stake + multi-year CPO supply agreement; capacity doubling of InP output; Lumentum CEO's industry-wide shortage comments — all independently corroborated, see Sources) | **92.20** |
| **Balance Sheet** (15%) | Net Debt/EBITDA 1.494× (TTM) | clamp(100×(1−1.494/4)) | **62.64** |
| **Moat** (15%) | 3 of 5 signals marked true (see below) | (3/5)×100 | **60.00** |
| **FCF Quality** (10%) | FCF/NI ratio (TTM) = −538.24/400.61 = −1.344 | clamp(((−1.344−0.40)/0.60)×100) = clamp(−290.6) — **floored at 0**; flagged as capex-timing-driven per the Owner Earnings data-gap note above, not an earnings-quality failure in the Valeant/Wirecard sense | **0.00** |

**Moat signal detail** (cited per quality-scoring.md's "do not mark a signal true without a cited source"):
- ✅ **Market share stable or growing** — Coherent led the global optical transceiver market with **>22.2% share in 2025** (the clear #1, ahead of Cisco, Broadcom, Lumentum, Accelink), per GMI/gminsights.com industry-analysis data. [Source: gminsights.com — see Sources.]
- ❌ Brand premium — no cited ASP/pricing-power-without-volume-loss evidence was sourced this session.
- ❌ Network effect — not applicable to Coherent's component/hardware-supplier business model; no two-sided-marketplace or user-growth-driven value mechanism identified.
- ✅ **Switching costs** — datacenter-optics supplier qualification cycles run 12–24 months industry-wide; Coherent's combined breadth (silicon photonics, InP EML lasers, VCSELs) and depth (materials-to-module vertical integration) creates documented technical-requalification switching costs once a hyperscaler/platform partner has qualified it into their roadmap. [Sources: industry commentary on qualification cycles and Coherent's vertical integration — see Sources; treated as a documented industry mechanism rather than a company-specific number, flagged accordingly.]
- ✅ **Scale cost advantage** — Coherent's transition from 3-inch to 6-inch InP wafers is disclosed (Q3 FY2026 earnings call) to yield **more than 4× the devices per wafer at less than half the cost per device** versus 3-inch — a cited, quantified cost-per-unit scale advantage. [Source: Q3 FY2026 earnings call, via BigGo Finance summary — see Sources.]

```
Quality Score = (19.34 × 0.25) + (45.97 × 0.15) + (92.20 × 0.20) + (62.64 × 0.15) + (60.00 × 0.15) + (0.00 × 0.10)
              = 4.835 + 6.896 + 18.440 + 9.396 + 9.000 + 0.000
              = 48.567
              → rounds to 48.6
```

**Quality Score: 48.6 / 100.0 — fails the 80.0+ gate.** No hard disqualifier independently fires, but the weighted score falls well short of the bar, driven primarily by weak trailing profitability (Profitability sub-score 19.3) and a FCF Quality sub-score floored at 0.0 by the current capex-ramp-driven cash burn (flagged above as likely overstated in severity, given the unresolved Owner Earnings data gap). Per [quality-scoring.md](../framework/quality-scoring.md) and the operating brief: **this stops the evaluation here — no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order setup is computed.**

## 4. Recommendation

**PASS — do not enter, do not open a standard watchlist limit-order posture.** Coherent is the clear #1 player in a fast-growing, structurally important market (optical transceivers for AI datacenters), with a genuine, well-documented moat (market share, switching costs, a real scale-driven cost advantage) and a credible near-term growth catalyst (NVIDIA's $2B equity stake and CPO supply agreement, tied directly to the indium-phosphide shortage story that triggered this session). None of that is in question. But on this framework's strict Quality Score formula, COHR currently fails the 80.0+ gate by a wide margin (48.6) because its **trailing profitability is weak** (TTM ROIC 5.54%, net margin 6.07% — both well under the framework's quality bar) and its **trailing free cash flow has swung deeply negative** in the most recent quarter as the company front-loads a large, real capacity-expansion capex program. This is a name whose story is forward-looking (a capacity build now, for demand growth later) in a way this framework's *trailing*-financials-weighted Quality Score is not built to credit — that's a feature of the gate's design (never invent a rosy forward number to rescue a company on trailing numbers), not a flaw specific to COHR.

**This is a "revisit later" name, not a "never" name** — see the review triggers below, in particular the still-open Owner Earnings data gap, which could plausibly move the FCF Quality and Profitability picture meaningfully if Coherent (or a future 10-K) discloses a maintenance-vs-growth CapEx split.

## 5. Next Review Trigger

Re-evaluate on any of the following:
- **FY2026 Q4 earnings (2026-08-12)** — the next full-fiscal-year print; this will show whether the capex ramp/OCF weakness is a one-quarter spike or a longer trend, and will complete a clean FY2026 annual FCF figure.
- A **maintenance-vs-growth CapEx breakdown** becoming available (10-K disclosure, investor-day materials, or explicit management commentary) — this would let Owner Earnings (Upgrade 1) be computed precisely instead of flagged as a gap, and could materially raise the Profitability and FCF Quality sub-scores.
- **2+ consecutive quarters of TTM ROIC recovering toward the mid-teens** as the new InP capacity comes online and is utilized (per management's stated timeline: capacity doubling "next quarter" from the 2026-05-06 call, more than quadrupling by end-2027) — would be a genuine, not merely price-driven, re-trigger.
- Any Rule 9 event: the 2026-08-12 earnings release itself, a guidance revision, M&A, management change, or a >15% unexplained price move beyond the already-large July 2026 decline already noted here.

No valuation score exists yet for COHR (fails at the Quality Gate), so no stale-score flag applies and none is created in [watchlist/STALE.md](../watchlist/STALE.md).

## Glossary

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year — a quick gauge of where the current price sits within its recent trading history. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets (factories, equipment, data centers). |
| **Co-packaged optics (CPO)** | A chip-packaging approach that mounts optical (light-based) data-transmission components directly next to/inside the same package as a switch or accelerator chip, instead of via a separate pluggable transceiver module — reduces power consumption and boosts bandwidth density for AI-cluster networking. NVIDIA's 2026 supply agreement with Coherent covers CPO components. |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. A negative figure means the business is consuming more cash than it generates from operations, after CapEx. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — measures how much of reported accounting profit actually shows up as real cash; a sustained low or negative ratio is a quality red flag, though a documented growth-capex explanation (as here) is an explicit carve-out from the hard-disqualifier version of this check. |
| **Hard disqualifier** | One of three Quality Score conditions ([quality-scoring.md](../framework/quality-scoring.md)) that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation. None fired for COHR this session, but the weighted score still failed the gate independently. |
| **Hybrid Upgrade** | One of seven specific rule add-ons layered onto the base 6-phase framework; Upgrade 1 (Owner Earnings) is discussed at length here but could not be precisely applied — see the data-gap note in Section 3. |
| **Indium phosphide (InP)** | A compound semiconductor material used to make the lasers and photodetectors inside optical transceivers — the material at the center of the 2026 industry-wide AI-datacenter supply shortage that triggered this session (Lumentum CEO's comments, NVIDIA's equity stakes in both Lumentum and Coherent). |
| **Moat** | Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors; scored here via a 5-signal checklist. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — operating profit after a tax adjustment but before financing costs; the numerator this framework uses to compute ROIC. |
| **Optical transceiver** | A module that converts electrical data signals into light (optical) signals for transmission over fiber-optic cable, and back again at the receiving end — the core product category connecting servers/switches inside and between AI data centers. Coherent led this market with >22.2% global share in 2025. |
| **Owner Earnings** | Warren Buffett's adjusted cash-flow measure: Net Income + D&A − *Maintenance* CapEx only (excludes growth CapEx) — used instead of raw FCF for moat-building reinvestors. Could not be precisely computed for COHR this session because a maintenance-vs-growth CapEx split isn't disclosed — flagged as a genuine data gap, not estimated. |
| **Pre-market (trading session)** | The period before a stock exchange's regular 9:30am–4:00pm ET trading hours, during which limited trading activity occurs at generally lower liquidity and can diverge meaningfully from the eventual regular-session open. |
| **Qualification cycle (supplier)** | The multi-month-to-multi-year process a customer (especially a hyperscaler or AI-hardware platform vendor) must run to test, validate, and approve a supplier's component before it can be designed into production — typically 12–24 months in datacenter optics; a documented Switching Costs moat-signal mechanism. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading profitability, margins, growth, balance sheet, moat signal, and FCF quality. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. COHR scores 48.6. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. COHR's TTM 5.54% is well below the framework's quality bar. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure. Used throughout this session's Quality Score inputs (through the quarter ended 2026-03-31, the most recent reported). |
| **Treasury yield (10Y)** | The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate. Recorded here for the session header but not applied, since the Quality Gate fails before Phase 02. |

## Sources

- Yahoo Finance `quoteSummary` and `fundamentals-timeseries` APIs (live/pre-market price, FY2022–FY2025 and TTM income statement, cash flow statement, balance sheet) — pulled directly 2026-07-28
- [Coherent Corp (COHR) Shares Fall — GF Value / GuruFocus coverage of the July 2026 decline](https://www.gurufocus.com/news/8956302/coherent-corp-cohr-shares-fall-53-gf-value-says-still-overvalued)
- [Applied Optoelectronics Plunges 17%, Coherent and Lumentum Sink 10% as Photonics Stocks Reset — 24/7 Wall St.](https://247wallst.com/investing/2026/07/02/applied-optoelectronics-plunges-17-coherent-and-lumentum-sink-10-as-photonics-stocks-reset/)
- [Coherent Corp. Announces Timing of FY2026 Q4/Fiscal Year-End Earnings Release (2026-08-12) — GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/22/3331208/11543/en/Coherent-Corp-Announces-Timing-of-FY2026-Fourth-Quarter-and-Fiscal-Year-End-Earnings-Release.html)
- [Coherent (COHR) Q3 2026 Earnings Transcript — The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/05/06/coherent-cohr-q3-2026-earnings-transcript/)
- [COHR Q3 2026 Earnings Call — Record Revenue, NVIDIA Partnership, InP Capacity Doubling — BigGo Finance](https://finance.biggo.com/news/US_COHR_2026-05-06)
- [Coherent Optical Equipment / Optical Transceiver Market Size & Share — GMI/gminsights.com](https://www.gminsights.com/industry-analysis/optical-transceiver-market)
- [Coherent Corp. (COHR): A Leader in Optical Transceivers Amid AI Data Center Growth — Insider Monkey](https://www.insidermonkey.com/blog/coherent-corp-cohr-a-leader-in-optical-transceivers-amid-ai-data-center-growth-1774841/)
- [Coherent finds the AI bottleneck — Where Is My Moat (industry commentary on qualification cycles / switching costs)](https://whereismymoat.com/p/coherent-finds-the-ai-bottleneck)
- [US 10 Year Treasury Note Yield — TradingEconomics](https://tradingeconomics.com/united-states/government-bond-yield)

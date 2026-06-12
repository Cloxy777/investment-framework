# NEW POSITION — TTD (The Trade Desk, Inc.) — 2026-06-12

**Task type:** NEW POSITION
**Date:** 12 Jun 2026
**10Y US Treasury Yield:** 4.46% (FRED DGS10, 11 Jun 2026 close)
**Rate Regime Modifier (Step 2, would apply if scored):** +5 (10Y in the 3.5–5% bracket) — **not applied; Phase 01 gate outcome determines whether Phase 02 is reached**
**Current TTD portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Technology — AdTech (Demand-Side Platform / programmatic advertising)

---

## 1. Live Price (Rule 0)

IBKR `search_contracts` / `get_price_snapshot` access was denied this session — fell back to WebSearch per the session instructions.

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$19.29** | WebSearch aggregation, intraday quote explicitly tagged "today" (12 Jun 2026), down −3.02% intraday |
| 52-week high | $91.45 | WebSearch (multiple aggregators, consistent) |
| 52-week low | $18.31–$19.10 (sources vary by a few cents — TTD appears to be making fresh 52-week lows in real time) | WebSearch aggregation |
| 11 Jun 2026 session range (context) | $18.37 (low) – $19.49 (high) | WebSearch |
| Analyst consensus PT (12-mo) | ~$25.34 (38 analysts, S&P Global, "Hold" consensus) / alt: $25.81 avg (31 analysts, "Buy"-leaning 14B/3S/20H split) | WebSearch (Investing.com / public.com) |
| Analyst PT range | $11 – $47 (extremely wide dispersion) | WebSearch |

⚠️ **Source variance flagged (per Rule 0):** WebSearch returned a wide scatter of "current" prices across queries — $18.77 (open), $19.29 (−3.02% intraday, tagged "today"), $19.43 (9 Jun close), $21.83 (+3.19%, ambiguous date), and a clearly stale/erroneous $40.49 (stockanalysis.com cache, contradicted by its own "52-week low $18.31" and "down 68.78% over past year" figures on the same page). The cluster of figures in the **$18.30–$19.99** band across 9–12 Jun 2026 is internally consistent with the 52-week-low figures and the "down >86% from 2024 highs" / "down 68.78% YoY" framing found independently. **$19.29 (the most recently-dated explicit "today" intraday quote, −3.02%) is used as the live price.** The $21.83 and $40.49 figures are treated as stale-cache artifacts and discarded — neither is consistent with the 52-week-low or YoY-decline figures from the same search session.

**Context:** TTD has had a brutal 13 months — from an all-time high near $140 (2024) and a 52-week high of $91.45, down to ~$19 today, a >86% drawdown from 2024 highs and >79% from the 52-week high alone. The collapse accelerated sharply after **Q4 FY2025 earnings (25 Feb 2026)** — Q4 itself **beat** estimates (revenue $847M +14% YoY, net income $187M, adjusted EBITDA ~47% margin) but the stock fell ~66% on guidance/visibility concerns (per "Trade Desk Q4 2025 slides: 73% EPS beat masks 66% stock decline"). CEO Jeff Green made a ~$148M personal insider purchase (6M shares at $23.49–$25.08) in early March 2026 — the stock has since fallen **further**, through and below his purchase price, to today's ~$19.29. Q1 FY2026 (7 May 2026) showed continued deceleration: revenue +12% YoY (vs +25% in Q1 2025), gross margin an 8-quarter low of 74% (vs 76.8% in Q1 2025), and GAAP net margin compressing to 5.8% (vs 8% in Q1 2025).

---

## 2. Data Gathered (Phase 01 Inputs) & Gaps Flagged

| Metric | Value | Source / Derivation |
|---|---|---|
| FY2022 Revenue | $1,578M (+32% YoY) | Trade Desk FY2022 8-K (Q4/FY2022 results) |
| FY2023 Revenue | $1,946M (+23.3% YoY) | Trade Desk FY2023 10-K / 8-K |
| FY2024 Revenue | $2,440M (+25.6% YoY) | Trade Desk FY2024 10-K / 8-K |
| FY2025 Revenue | $2,896.284M (+18.7% YoY) | Trade Desk FY2025 8-K (Q4/FY2025 results, 25 Feb 2026) |
| Q1 FY2025 Revenue | $616M (+25% YoY) | Trade Desk Q1 FY2025 10-Q/8-K |
| Q1 FY2026 Revenue | $689M (+12% YoY) | Trade Desk Q1 FY2026 10-Q/8-K (7 May 2026) |
| **TTM Revenue** | **$2,969.284M** = 2,896.284 + 689 − 616 | Computed (roll-forward) |
| **Revenue CAGR 3yr** (FY2022→FY2025) | **22.43%** = (2,896.284/1,578)^(1/3) − 1 | Computed |
| FY2025 Net income (GAAP) | $443.304M (+13% YoY, ~15.3% margin on FY2025 revenue) | Trade Desk FY2025 8-K |
| Q1 FY2025 Net income | $51M (8% margin) | Trade Desk Q1 FY2025 10-Q/8-K |
| Q1 FY2026 Net income | $40M (5.8% margin, down from 8%) | Trade Desk Q1 FY2026 10-Q/8-K |
| **TTM Net Income** | **$432.304M** = 443.304 + 40 − 51 | Computed (roll-forward) |
| **TTM Net margin** | **14.56%** = 432.304 / 2,969.284 | Computed — see Gap #1 |
| Gross margin FY2023 | 81.2% | WebSearch (MacroTrends aggregation) |
| Gross margin FY2024 | 80.7% | WebSearch (MacroTrends aggregation) |
| Gross margin FY2025 | 78.6% (5-year low at the time) | WebSearch (MacroTrends aggregation) |
| Gross margin Q1 FY2025 | 76.8% | TIKR (Q1 FY2026 earnings recap) |
| Gross margin Q1 FY2026 | **74.0%** — an 8-quarter low, −3.2pp YoY | TIKR / Investing.com (Q1 FY2026 earnings recap) |
| FY2025 Income from operations (GAAP EBIT) | $427.167M | Trade Desk FY2025 8-K (Q4/FY2025 results) |
| Q1 FY2025 Income from operations | $54.452M | Trade Desk Q1 FY2025 10-Q |
| Q1 FY2026 Income from operations | $66.647M | Trade Desk Q1 FY2026 10-Q |
| **TTM EBIT** | **$439.362M** = 427.167 + 66.647 − 54.452 | Computed (roll-forward) |
| FY2025 OCF / FCF | OCF not separately re-confirmed this session / **FCF $795.71M** | WebSearch (MacroTrends FCF series) |
| FY2024 FCF | $678.4M (one source) / $632.4M (alt source — see Gap #2) | WebSearch (MacroTrends / alt aggregator) |
| FY2023 FCF | $632.4M (one source) / $543.3M (alt source — see Gap #2) | WebSearch (MacroTrends / alt aggregator) |
| Q1 FY2025 FCF | $230M | Trade Desk Q1 FY2025 8-K |
| Q1 FY2026 FCF | $276M | Trade Desk Q1 FY2026 8-K |
| **TTM FCF** | **$841.71M** = 795.71 + 276 − 230 | Computed (roll-forward) |
| **FCF/NI conversion (TTM)** | **194.7%** = 841.71 / 432.304 | Computed |
| FY2025 EBITDA | $705.1M (+37.0% YoY) | WebSearch (AlphaQuery) |
| Cash + ST investments (31 Mar 2026, Q1 FY2026 10-Q) | $878.377M + $527.538M = **$1,405.915M** | Trade Desk Q1 FY2026 10-Q balance sheet |
| Total debt | $0.0 (debt-free) | WebSearch (multiple aggregators) |
| **Net cash position** | **$1,405.915M** (net debt negative) | Computed |
| Shares outstanding | ~427.0M | WebSearch (Google Finance aggregation) |
| **Market Cap** (at $19.29) | 427.0M × $19.29 = **$8,236.83M** | Computed |
| **Enterprise Value** | $8,236.83M − $1,405.915M = **$6,830.92M** | Computed |
| **EV/EBIT (TTM)** | $6,830.92M / $439.362M = **15.55×** | Computed |
| **FCF Yield (TTM)** | $841.71M / $8,236.83M = **10.22%** | Computed |
| ROIC (TTM, GuruFocus) | 26.21% (TTM, Dec 2025 basis) / 43.96% (alt GuruFocus figure, methodology unclear) / 18.0% (3yr avg) / 21.6% (5yr avg) | WebSearch (GuruFocus, ValueSense) — wide range but **directionally well above 15%** on every basis |
| Forward PE (GuruFocus, ~5 Jun 2026) | 10.78–10.79× | WebSearch (GuruFocus) |
| GuruFocus PEG | 0.50 | WebSearch (GuruFocus) |
| FY2026 consensus EPS (basis ambiguous) | $1.84 | WebSearch (aggregator) — see Gap #4 |
| Non-GAAP diluted EPS: FY2022 | $0.66 | Trade Desk FY2023 8-K (prior-year comparison) |
| Non-GAAP diluted EPS: FY2023 | $0.84 (+27.3% YoY) | Trade Desk FY2023 8-K |
| Non-GAAP diluted EPS: FY2024 | $1.07 (+27.4% YoY) | Trade Desk FY2024 8-K |
| Non-GAAP diluted EPS: FY2025 | $1.66 (+55.1% YoY) | Trade Desk FY2025 8-K |
| Non-GAAP diluted EPS: Q1 FY2025 | $0.33 | Trade Desk Q1 FY2025 8-K |
| Non-GAAP diluted EPS: Q1 FY2026 | $0.28 | Trade Desk Q1 FY2026 8-K |
| **TTM Non-GAAP diluted EPS** | **$1.61** = 1.66 + 0.28 − 0.33 | Computed |
| GAAP diluted EPS: FY2022 | $(0.04) (loss) | WebSearch (GuruFocus/EPS aggregation) |
| GAAP diluted EPS: FY2023 | $0.16 | WebSearch (GuruFocus/EPS aggregation) |
| GAAP diluted EPS: FY2024 | $0.42 | Trade Desk FY2025 8-K (prior-year comparison) |
| GAAP diluted EPS: FY2025 | $0.78 | Trade Desk FY2025 8-K |
| 10yr avg/range PE | **Not retrieved this session** — gate did not require it (see below) | — |
| CEO insider buying | Jeff Green, ~$148M (6M shares, $23.49–$25.08 weighted avg), 2–4 Mar 2026 — +373% increase in his stake | WebSearch (multiple sources, StockTitan Form 4) |
| Recent buyback authorization | $500M increase announced alongside FY2025 results (Feb 2026) | WebSearch (StockTitan) |

### Data Gaps / Flags

1. **TTM Net Margin (14.56%) is the central, decision-relevant number this session — it sits just BELOW the strategy.md Phase 01 threshold (>15%) but just ABOVE the valuation-scoring.md pre-screen filter (>12%).** Unlike DUOL's borderline net-margin case (≈15.09% ex a one-off tax item, narrowly *clearing* 15%), TTD's 14.56% is a **genuine, trend-confirmed miss**: GAAP net margin compressed from 8% (Q1 FY2025) to 5.8% (Q1 FY2026), the *same direction* as the gross-margin compression (76.8%→74.0%, an 8-quarter low). This is not a one-off accounting item — it is the TTM figure directly reflecting two consecutive years of full-year margin improvement (FY2023→FY2024→FY2025: net margin trended up to ~15.3% for FY2025 alone) **followed by a fresh-quarter reversal** in Q1 FY2026. See §3 for the gate treatment.

2. **FY2023/FY2024 FCF figures have a source discrepancy** ($632.4M vs $543.3M for FY2023; $678.4M vs $632.4M for FY2024 — the two aggregators appear to be off by one year from each other, similar to the FY2024 revenue confusion that was caught and corrected in §2 above). **Both pairs of figures are positive** for both years regardless of which is correct, so the Phase 01 "FCF positive 3 consecutive years" check is unaffected either way — flagged for completeness, not decision-relevant.

3. **ROIC has a wide range across sources** (43.96% "as of Dec 2025" vs 26.21% "TTM Dec 2025 basis" vs 18.0% 3yr avg vs 21.6% 5yr avg, all from GuruFocus-family pages with unclear/differing methodology). All four readings clear the >15% Phase 01 threshold by a wide margin — **does not change the gate outcome**.

4. **Forward PE / PEG sourcing is layered and slightly stale.** GuruFocus (~5 Jun 2026, price likely ~$18–19 at that time) shows Forward PE 10.78–10.79× and PEG 0.50. An independently-found "$1.84 FY2026 consensus EPS" figure, if non-GAAP and divided into today's $19.29, gives Forward PE = 10.48× — broadly consistent with GuruFocus's 10.78× (small difference attributable to the few-cent price move between the two data-pull times). **This is recorded for completeness but is not used in this session** — Phase 01 fails before Forward PE/PEG become decision-relevant (see §3/§4).

5. **Non-GAAP diluted EPS growth (the basis for a Fast Grower / PEG determination, had Phase 01 passed) shows +27.3% (FY2023), +27.4% (FY2024), +55.1% (FY2025)** — three consecutive years >15%, which would have qualified TTD as a Fast Grower. **This is not reached** in this session because Phase 01 does not pass — flagged for the record in case TTD is re-evaluated after a margin-recovery quarter.

**No metric was invented or estimated.** The single decision-relevant figure (TTM net margin 14.56%) is built from four directly-sourced 8-K figures (FY2025 NI, Q1 FY2025 NI, Q1 FY2026 NI, plus the corresponding revenue figures) with no estimation involved.

---

## 3. Phase 01 — Quality Gate

| Check | TTD Value | Threshold | Result |
|---|---|---|---|
| **Net margin (TTM)** | **14.56%** | >15% (strategy.md) / >12% (valuation-scoring.md pre-screen) | ⚠️ **FAIL on primary threshold** (narrowly — see discussion below); passes the looser pre-screen |
| ROIC | 18–44% (range across sources, all bases) | >15% | ✅ PASS (comfortably, on every basis) |
| Revenue CAGR 3yr (FY2022→FY2025) | 22.43% | >10% | ✅ PASS (comfortably) |
| Gross margin | 78.6% FY2025 (>40% ✅), but **trend is FY2023 81.2% → FY2024 80.7% → FY2025 78.6% → Q1 FY2026 74.0%** (8-qtr low) | >40% **or** structurally expanding | ⚠️ Level passes; trend is **contracting**, not expanding — fails the alternative test |
| FCF positive 3 consecutive years | FY2023/24/25 all positive (632–796M range depending on source) | required | ✅ PASS |
| Net debt/EBITDA | Net **cash** of $1.406B, zero debt | <2x | ✅ PASS (trivially — net cash) |
| FCF/NI conversion ratio (TTM) | 194.7% | >70% | ✅ PASS |
| Share issuance pattern | Net buybacks; $500M buyback authorization increase (Feb 2026) | not dilutive | ✅ PASS |
| Moat signal | Largest independent DSP; ~95% client retention (historically cited); CEO $148M personal insider buy (Mar 2026) signals high conviction | required | ✅ Qualitatively strong |

### Gate discussion — why this is a FAIL, not a pass-with-flags

This is a genuinely close call, and it is worth being explicit about *why* it lands on FAIL rather than "pass, narrowly":

- **The threshold is binary in strategy.md**: "Net margin >15%." TTD's TTM net margin is 14.56% — **not** >15%, by a margin of 0.44 percentage points.
- **Unlike DUOL's prior borderline case** (≈15.09% ex a one-off tax item — a number *inflated upward* by a non-recurring item, with the underlying business arguably *stronger* than the headline-adjusted figure suggested), TTD's 14.56% has **no one-off adjustment to make it look better** — it is the straightforward TTM roll-up of four directly-reported figures.
- **The miss is corroborated by a second, independent criterion failing in the same direction**: gross margin, which clears the absolute >40% bar comfortably (78.6%) but fails the "structurally expanding" alternative outright — it has contracted in **four consecutive periods** (81.2% → 80.7% → 78.6% → 74.0%), with the most recent data point (Q1 FY2026, 74.0%) representing an **8-quarter low**. Two margin-related criteria pointing the same direction, both on the most recent (TTM/quarterly) data, is a *trend* signal, not noise.
- **The trend is recent and ongoing**: FY2025 alone (net income $443.304M / revenue $2,896.284M = 15.30%) would have cleared 15% comfortably. It is **Q1 FY2026 specifically** (net margin 5.8%, down from 8% a year earlier) dragging the TTM figure below the line. The gate is built on trailing financials precisely so that a single weak/transitional quarter doesn't get overridden by a narrative about why it's temporary (the same principle applied to CIEN's "exciting single quarter doesn't override TTM" reasoning, in the opposite direction).

**Gate result: FAIL on Net Margin (TTM 14.56% vs >15% required), corroborated by Gross Margin trend (contracting, not expanding, fails the alternative to the >40% level test).** All other seven criteria pass, several (ROIC, Revenue CAGR, FCF/NI conversion, net cash) by very wide margins. Per the operating brief ("if it fails, stop and write up why"), this session does **not** proceed to the Rate Environment Gate or Phase 02 valuation score.

---

## 4. Does the Turnaround Sub-Gate (Upgrade 4) Open an Alternate Path?

Given how close this call is — and how strong the *other* seven criteria are — it's worth explicitly checking Upgrade 4 (Turnaround Sub-Gate / Fallen Angel Path), which allows a **2–3% Conditional Watch position** if **all five** conditions are met:

| Condition | TTD Status | Met? |
|---|---|---|
| 1. ROIC historically >15% for ≥5 years in past decade | 3yr avg 18.0%, 5yr avg 21.6%, TTM 26.21% — all comfortably >15%; TTD has been a high-ROIC business essentially since IPO (2016) | ✅ Likely met (high confidence, though a full 10yr year-by-year series wasn't individually pulled) |
| 2. CEO/CFO insider buying >$500K in past 6 months (Form 4 verified) | CEO Jeff Green's ~$148M purchase (2–4 Mar 2026, Form 4 per StockTitan) — **far** exceeds the $500K bar | ✅ Met |
| 3. Independent FV estimate showing ≥40% MOS | **Not built this session** — Phase 01 failure means no Phase 02 score, no DCF, no blended FV was computed | ❌ Not evaluated — **cannot confirm** |
| 4. Net Debt/EBITDA <3× | Net cash position ($1.406B), zero debt | ✅ Met (trivially) |
| 5. Core moat still identifiable | Largest independent DSP, open-internet positioning vs. walled gardens — moat *narrative* intact even if margins are under near-term pressure | ✅ Met (qualitatively) |

**4 of 5 conditions appear met; condition 3 (≥40% MOS) cannot be confirmed without building an independent fair-value estimate — which itself requires the Phase 02 inputs (FCF, EV/EBIT, Forward PE) that this session deliberately did not finalize into a score, since Phase 01 failed.**

**This session does not build that independent FV** — doing so would effectively mean running most of Phase 02/Step-1-Fair-Value machinery for a name that failed the standard gate, which risks exactly the "dress up a name the quality screen says isn't there yet" failure mode flagged in the CIEN session. However, **all the raw inputs needed to build that independent FV in a follow-up session are already captured in §2 above** (TTM FCF $841.71M, TTM EBIT $439.362M, EV $6,830.92M, net cash $1.406B, shares 427M) — so a focused follow-up could resolve condition 3 quickly without re-pulling data, **if** the human investor wants to pursue the Turnaround Sub-Gate path given how unusually strong conditions 1, 2, 4, and 5 are for a "fallen angel" candidate.

---

## 5. Recommendation

# **PASS — do not open a position now. Watchlist with conditions.**

TTD fails the Phase 01 quality gate on **TTM Net Margin (14.56% vs >15% required)**, corroborated by a **contracting gross-margin trend** (81.2%→80.7%→78.6%→74.0% over the last four annual/quarterly data points, an 8-quarter low). Per the framework's non-negotiables, a quality-gate failure on trailing financials is not overridden by price action (TTD is down >86% from 2024 highs) or by a compelling narrative (CEO's $148M insider buy, net-cash balance sheet, 22.4% revenue CAGR, 26% TTM ROIC) — those are exactly the kind of "exciting but not yet proven in the trailing numbers" signals the gate exists to filter on the *other* side of (see CIEN's symmetric case).

**That said, this is the closest "near-miss" Phase 01 failure this framework has logged** (a 0.44-percentage-point net-margin gap, on a business that posted a 15.30% net margin for FY2025 as a whole, with FCF/NI conversion at 195% and a net-cash balance sheet) — and it sits on top of an unusually strong set of Turnaround Sub-Gate (Upgrade 4) signals (CEO insider buying alone is >280x the $500K bar). **The bottleneck to a Conditional Watch (2–3%) entry is condition 3 (≥40% MOS via independent FV) — not yet evaluated, but all raw inputs needed to evaluate it are captured in §2.**

**Recommended next steps:**
1. **Primary trigger — Q2 FY2026 earnings** (expected ~August 2026): re-run Phase 01 with refreshed TTM net margin and gross-margin trend. If Q2 FY2026's net margin recovers toward/above the FY2025 full-year run-rate (15.3%), TTM net margin would mechanically cross back above 15% and the standard gate would likely pass — proceed directly to Rate Gate + Phase 02 at that point.
2. **Alternative trigger — Turnaround Sub-Gate follow-up** (does not require waiting for Q2 earnings): build the independent FV (DCF + multiples, per fair-value-methodology.md) using the inputs already in §2, to resolve condition 3. If ≥40% MOS is confirmed, a 2–3% Conditional Watch position could open under Upgrade 4 with a **mandatory 2-quarter review**, even with Phase 01 still technically failing on net margin.
3. Either path should be revisited **immediately** if a >15% unexplained price move occurs from $19.29 (Rule 9) — TTD's volatility profile (>86% drawdown in 13 months, continuing to make fresh 52-week lows even after a $148M CEO purchase) makes this a realistic near-term possibility in either direction.

---

## 6. Next Review Trigger

- **Q2 FY2026 earnings** (expected ~August 2026) — mandatory Phase 01 re-check (Rule 9). Specifically: does TTM net margin cross back above 15%? Does the gross-margin contraction (74.0% in Q1 FY2026) stabilize or continue?
- **Turnaround Sub-Gate (Upgrade 4) follow-up** — optional, can be done independently of earnings timing: build the independent FV (DCF + ≥3 multiples approaches) using the §2 inputs to test condition 3 (≥40% MOS). If confirmed alongside conditions 1/2/4/5 (already met), a 2–3% Conditional Watch position could be considered with a mandatory 2-quarter review.
- **>15% unexplained price move from $19.29 in either direction** — immediate re-score per Rule 9.
- **No position opened by this session — nothing to log in `decisions/`.**

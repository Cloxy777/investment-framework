# RESCORE — NVDA (NVIDIA Corporation)

**Task type:** RESCORE (single ticker, mode `--both`) — user-invoked (`/rescore nvda`), off-cycle (no new quarterly filing; see §3)
**Date:** 2026-11-05
**10Y US Treasury Yield:** 4.95% (FRED series DGS10, latest published observation 2026-11-03; 11-04 not yet posted. Last 5 prints: 5.05% 10-28 → 4.98 → 4.94 → 4.91 → 4.95)
**Rate Regime Modifier (Step 2):** +5 (3.5–5% bracket) — **0.05pp below the 5% boundary and was above it on 10-28 (5.05%)**; at >5% the modifier would be +10 (sensitivity in §6)
**Last review on record:** NVDA **23.0** Composite (Quality 90.3 / Valuation 36.2), 2026-09-17 — [sessions/2026-09-17-rescore-nvda.md](2026-09-17-rescore-nvda.md). **That score predates the 2026-10-12 SBC-as-a-cost methodology** and was flagged STALE; this run is the first NVDA score under the current methodology, so part of the move is methodological, not market-driven (see §9).
**Current NVDA weight:** 19 sh × $186.77 = $3,548.63 ≈ **7.7–7.8%** of framework-account NLV (U19421206; NLV $46,102.05 at the 2026-11-02 sync, ≈$45.75K if only NVDA is re-marked). Under the 15% hard cap (Upgrade 7) and, after today's drop, back under the 8% allocation cap (it was 8.47% at the last sync at $205.40).

## Why this session ran
User-invoked `/rescore nvda`. Context found while collecting data: NVDA is **−$13.36 / −6.68% today** (broad Big-Tech sell-off; headlines in §3). It is also a stale-score name (clears the mark, §10).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$186.77** | IBKR `get_price_snapshot` (contract 4815747), last trade, ts 1793892036 (2026-11-05 intraday). Bid/ask $186.72 / $186.78. |
| Today's move | **−$13.36 / −6.68%** (implies prior close ≈ $200.13) | IBKR `change`. Under the 15% Rule 9 unexplained-move line. |
| Cross-check quotes (same morning) | finviz $186.79 · stockanalysis $186.27 · marketbeat $187.03 | Page headers, ~10:18–10:20 AM ET 2026-11-05 — all within 0.4% |
| 52-week range | $164.08 – $243.37 | IBKR `misc_statistics` (52w high is up from $236.27 on 09-17: the stock rallied into October, then fell) |
| YTD | +0.26% | IBKR `year_to_date_change` (was +17.41% on 09-17) |
| Price vs 09-17 | $218.70 → $186.77 = **−14.6%** over 7 weeks | Cumulative, not a single-day event; no Rule 9 trigger from price alone |

**Today's drop — cause NOT verified.** Finviz headlines at the time: "Big Tech slumps, dragging down S&P 500" (MarketWatch 10:07), "Dow drops 165 points on losses in NVIDIA, Cisco shares" (MarketWatch 09:45), "Nvidia orders data centre clients to reduce China exposure" (FT, 05:51 — **single headline, not confirmed from a primary source and not independently found by my own search**), and a 11-04 item on Democratic election wins / proposed data-center limits raising questions on AI-infrastructure demand. Per Rule 0 / "never act on price alone", none is treated as a documented fundamental trigger: no filed guidance change, no 8-K. An undated web snippet suggests NVIDIA's forecasts already exclude China data-center sales, which (if true) would limit the scored impact of a China-exposure headline — also unverified. **If NVIDIA files an 8-K or the FT report is confirmed, re-run.**

---

## 2. Data Gaps / Sourcing Notes (flagged, not silently worked around)

1. **`yfinance` unavailable again.** `python -m scripts.fetch_fundamentals NVDA` failed with `YFRateLimitError: Too Many Requests` (Yahoo crumb endpoint). So the script's yfinance-derived block and its advisory block were **not produced**; substitutes below. This is now a recurring failure across 5+ NVDA sessions — worth escalating outside the analysis session.
2. **No new financial filing since the last review.** SEC EDGAR submissions feed (CIK 1045810): newest periodic filings are 10-Q filed 2026-08-26 and 8-K 2026-09-03; since then only Forms 4/4-A/144 (insider). **All TTM statement inputs (revenue, EBIT, NI, OCF, capex, FCF, D&A, EBITDA, gross profit, debt/cash, equity, invested capital, ROIC, 3yr revenue CAGR) are therefore reused from the 09-17 / 08-27 derivation**, not re-derived.
3. **Newly derived this session from SEC XBRL (companyfacts API) — the SBC-as-cost inputs the 09-17 run didn't need:**
   - SBC TTM = FY2026 $6,386M + H1 FY2027 $3,954M − H1 FY2026 $3,099M = **$7,241M**
   - Gross cash buybacks TTM = $40,086M + $39,044M − $23,815M = **$55,315M**
   - Cross-check of the reused TTM OCF: $102,718M + $74,421M − $42,779M = $134,360M ✓ (matches the reused figure exactly)
   - GAAP diluted EPS TTM = $4.90 + $4.85 − $1.84 = **$7.91** (matches finviz EPS ttm 7.91 ✓); EPS TTM one year earlier (Jul-2025) = $2.94 + $1.84 − $1.27 = **$3.51**
4. **Forward EPS = $15.81** (finviz "EPS next Y", +70.15% growth), same vendor and convention as 09-04/09-17. stockanalysis shows "EPS Next Year 15.91" (+0.6%, consistent). Finviz's 18-analyst consensus-PT sample is thin, so PT inputs use the two broader aggregators (below). The open methodology item from earlier sessions (pick one authoritative forward-EPS source) remains unresolved.
5. **Consensus price targets:** stockanalysis $327.14 (62 analysts; high $515, low $180) and marketbeat $318.85 (54 analysts; high $515, low $210). Their mean = **$322.995** (same two-aggregator convention as 09-17). Finviz $332.73 shown for reference only.
6. **5-yr PE history reused, not re-derived:** avg **57.84×** (range 25.97×–142.78×, n=20 quarters) carried from 09-01/09-04/09-17; no alternate bulk-history source while yfinance is down. Used in `avg` mode as in prior sessions. Note: with forward PE at 11.8×, FwdPE_Score floors at 0.0 under either the avg or the range formula, so this gap cannot move the score.
7. **Earnings date discrepancy:** finviz shows **Nov 17 (after close)**; the 09-17 log carried a third-party estimate of ~25 Nov. Neither is confirmed by NVIDIA IR (last year's Q3 10-Q was filed 2025-11-19). Treat the print as imminent (≈12–20 days) and unconfirmed.
8. **Advisory-block data gap:** `cycle_peak` / `value_trap_candidate` could not come from the script's yfinance path; computed from the SEC EPS figures above via `flags_common` instead (§5b).

---

## 3. Inputs Collected

| Item | Value | Status |
|---|---|---|
| Shares outstanding | 24,100M | SEC 10-Q cover (2026-08-26 filing); finviz shows 24.15B |
| **Market cap** | 24,100M × $186.77 = **$4,501,157M** | Recomputed at live price |
| Net debt | **−$23,220M** (net cash; debt $33,366M, cash+ST securities $56,586M at 2026-07-26) | Reused |
| **Enterprise value** | $4,501,157M − $23,220M = **$4,477,937M** | Recomputed |
| TTM revenue / EBIT / net income | $302,969M / $197,579M / $192,879M | Reused |
| TTM OCF / CapEx / **FCF** | $134,360M / $7,354M / **$127,006M** | Reused (OCF re-verified, §2.3) |
| TTM D&A / EBITDA | $3,687M / $201,266M | Reused |
| **EV/EBIT** | $4,477,937M ÷ $197,579M = **22.664×** | Recomputed |
| **FCF yield** | $127,006M ÷ $4,501,157M = **2.8216%** | Recomputed |
| **SBC yield** | $7,241M ÷ $4,501,157M = **0.1609%** | New this methodology |
| **Gross buyback yield** | $55,315M ÷ $4,501,157M = **1.2289%** | New (gross cash basis) |
| (FCF − SBC) ÷ NI TTM | ($127,006M − $7,241M) ÷ $192,879M = **62.09%** | New; plain FCF/NI = 65.85% |
| SBC ÷ FCF | 5.70% | Far below the 100% disqualifier |
| Gross / net margin (TTM) | 74.68% / 63.66% | Reused (finviz profit margin 63.66% ✓) |
| ROIC (TTM) | 63.21% | Reused |
| Revenue 3yr CAGR | 100.05% | Reused |
| Net debt/EBITDA | −$23,220M ÷ $201,266M = −0.1154× | Reused |
| FCF/NI annual FY23–FY26 | 87.18% / 90.80% / 83.50% / 80.51% | Reused |
| Forward EPS / **Forward PE** | $15.81 / $186.77 ÷ $15.81 = **11.813×** | Recomputed |
| **PEG** | 11.813 ÷ 70.15 = **0.1684** (Lynch definition; finviz displays 0.18) | Recomputed |
| Dividend yield | $1.00 ÷ $186.77 = 0.5354% | Recomputed |
| 10Y Treasury | 4.95% | FRED 2026-11-03 |

**Fast Grower determination (PEG applicable):** unchanged from every prior session — EPS growth >15% for 3+ years on a clean, non-distorted base (FY23–FY26 EPS expansion; no one-off in reported NI flagged, so no `--normalised-ni`).

**Per-flag handling (advisory, no score effect) — §5b below.**

---

## 4. Quality Score (scripted — inputs in this section's JSON were assembled from §3)

Hard disqualifiers: FCF/NI annual FY2025 83.50% / FY2026 80.51% (both ≥70%) ✅ · Net debt/EBITDA −0.115× ✅ · FCF-positive every year ✅ · SBC/FCF 5.70% (<100%) ✅. TTM FCF/NI 65.85% (plain) / 62.09% (after SBC) is below 70% but the disqualifier tests completed fiscal years only — **same standing watch item as 08-27/09-17**.

`gross_margin_structural_trend` was set **false**: annual gross margin ran FY23 56.9% → FY24 72.7% → FY25 75.0% → FY26 71.1% (SEC XBRL), i.e. up over the window but not a clean 3-year expansion, and no earlier NVDA session claimed the bonus. (Moot-ish: it would add +1.0 to the Quality Score.) TAM evidence (+10 on Growth) cited from the 08-26 filing/call per the 08-27 session; Growth sits at the 100.0 cap regardless.

Script output (verbatim):

## Quality Score

**Profitability (25%)**
```
NetMargin_Component = clamp((63.66/30)x100) = 100.00
ROIC_Component = clamp((63.21/30)x100) = 100.00
Profitability_Score = (100.00 + 100.00) / 2 = 100.00
```
**Margins (15%)**
```
GrossMargin_Score = clamp((74.68/80)x100) = 93.35
```
**Growth (20%)**
```
Growth_Score = clamp((100.05/25)x100) = 100.00
+10 TAM/pricing-power evidence: Data Center revenue $89.0B in Q2 FY2027 (+117% YoY, 92% of revenue); Q3 FY2027 guide $108.0B (SEC 8-K / earnings call 2026-08-26, per sessions/2026-08-27-rescore-nvda.md). No new filing since.
Growth_Score (final, clamped) = 100.00
```
**Balance Sheet (15%)**
```
BalanceSheet_Score = clamp(100x(1 - -0.1154/4)) = 100.00
```
**Moat Signal (15%)**
```
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Data Center 92% of Q2 FY2027 revenue; ~80% AI-accelerator share (07-05 and 08-27 sessions) |
| brand_premium | True | Premium B200/GB200 ASPs vs AMD MI350X/ASICs; TCO comparisons (07-05 session), unchanged |
| network_effect | True | CUDA ecosystem 4M+ developers, 40,000+ orgs (07-05 session), unchanged |
| switching_costs | True | CUDA-embedded production code (07-05 session), unchanged |
| scale_cost_advantage | False | No cost-per-unit citation vs a named smaller competitor - same strict-reading gap as every prior session |
Moat_Score = (4/5) x 100 = 80.00
```
**FCF Quality (10%)**
```
FCFQuality_Score = clamp(((0.6209 - 0.40)/0.60)x100) = 36.82  [ratio = (FCF - SBC)/NI]
```
**Quality Score — Final**
```
Quality Score = (100.00x0.25) + (93.35x0.15) + (100.00x0.20) + (100.00x0.15) + (80.00x0.15) + (36.82x0.10)
= 89.685 -> rounds to 89.7
```

# Quality Score = 89.7 — PASSES the 80.0+ gate

---

## 5. Valuation Score (scripted)

Fair-value inputs: **Base** = consensus forward EPS $15.81 × 21× = **$332.01** (sanity check: within ~1.5% of both aggregators' mean PT $322.995 / ~1.7% of stockanalysis $327.14); **Bull** = $18.00 × 24× = **$432.00** and **Bear** = $11.00 × 16× = **$176.00** carried unchanged from 09-17 (no filed change to the multi-year bull/bear framing; today's headlines are unverified). Catalyst: Q3 FY2027 earnings (Nov 17 per finviz, unconfirmed) → documented catalyst inside 18–24 months, 2-year default window. Intrinsic growth 10%/yr (the standing conservative convention). `pe_mode: avg` (5yr avg 57.84×, reused).

Script output (verbatim):

## Valuation Score

**FCF Yield (40%)**
```
FCF yield after SBC = 2.8216% - 0.1609% (SBC yield) = 2.6607%
FCF_Score = clamp(100x(1 - 2.6607/10)) = 73.393
```
**EV/EBIT**
```
EV/EBIT_Score = clamp((22.664 - 12)/23 x 100) = 46.365
```
**Forward PE**
```
Deviation% = (11.8134 - 57.84)/57.84 x 100 = -79.576%
FwdPE_Score = clamp(50 + -79.576x2.5) = 0.000 (fallback formula; Historical PE Modifier already folded in)
```
**PEG**
```
PEG_Score = clamp((0.1684 - 0.5)/2.0 x 100) = 0.000
```
**Rate Environment Gate**
```
EY = 1/11.8134 x 100 = 8.4650%
Spread = EY - 10Y (4.95%) = 3.5150pp -> Step 1 = +0 (pass, >=1.5pp)
10Y = 4.95% -> Step 2 bracket modifier = +5
Total Rate Modifier = 0 + 5 = +5
```
**Upside/Downside Modifier**
```
PW Fair Value = 0.25x432.0 + 0.50x332.01 + 0.25x176.0 = 318.0050
Gap Upside % = (318.0050/186.77) - 1 = 70.2656%
Annualized gap = 70.2656% / 2yr = 35.1328%/yr
E = 35.1328 (annualized gap) + 10.0 (intrinsic growth) + 1.7643 (shareholder yield: 0.5354 div + 1.2289 buyback) = 46.8971%/yr
E (46.8971%) >= H (10.0%) -> M = -15 x clamp((46.8971-10.0)/15, 0, 1) = -15.0000
Upside/Downside Modifier (bounded [-15, +15]) = -15.0000
```
**Raw Weighted Score**
```
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.25 + FwdPE_Score x 0.2 + PEG_Score x 0.15
= 40.949
```
**Final Valuation Score**
```
Final Score = Raw (40.949) + Rate Modifier (+5) + Upside/Downside Modifier (-15.000)
= 30.949 -> rounds to 30.9
```

# Valuation Score = 30.9

### 5b. Advisory flags (no score effect) — verbatim, then handling

```
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             CYCLE_PEAK_CANDIDATE   EPS TTM +125% > 100%† — state why the multiple is compared with a normalised base
  multiple_ceiling       NONE                   forward PE 11.8, EPS growth 70.2%
  value_trap_candidate   NONE                   forward PE 11.8, EPS TTM growth +125.4%
```

**Handling:**
- **`CYCLE_PEAK_CANDIDATE` (raised): TTM GAAP diluted EPS $7.91 vs $3.51 a year earlier = +125.4%.** This is the real caveat on a 11.8× forward PE: the multiple sits on earnings that have more than doubled in a year, at what could be a capex-cycle peak. Why the score is nonetheless not distorted: (a) the FwdPE and PEG sub-scores both floor at 0.0 and would do so against *any* plausible normalised base (the 5yr *low* PE is 25.97×; a 50% normalised-EPS haircut still gives ≈23.6×), so the flag cannot move them; (b) the two sub-scores that carry the weight — FCF yield (73.4) and EV/EBIT (46.4) — are on realised TTM cash flow and operating profit, not forward EPS; (c) the **bear case ($11.00 EPS × 16× = $176) is explicitly the earnings-reversion scenario** and is 25%-weighted in the PW fair value. Residual risk is stated, not scored: the Upside/Downside Modifier is pinned at its −15.0 floor and the Valuation Score leans on it, so the *quality of the base-case EPS* is the thing to watch at the print.
- `MULTIPLE_CEILING`: NONE (forward PE 11.8 < 30). `VALUE_TRAP_CANDIDATE`: NONE (trailing EPS rising +125.4%, not falling).
- **Data gaps:** none of the flags returned `UNKNOWN` once the SEC EPS figures were supplied; the script-native advisory block (SBC/FCF, FCF after SBC) is reproduced by hand in §3.

---

## 6. Rate Environment Gate (also inside the script output above)

Step 1: EY = 1 ÷ 11.813 = 8.465%; spread vs 4.95% = +3.515pp ≥ +1.5 → pass, +0. Step 2: 10Y 4.95% → +5. **Total +5.**
Sensitivity: FRED printed 5.05% on 2026-10-28. If the 10Y closes above 5% the Step 2 modifier becomes +10 → Valuation 35.9, Composite 23.1 — same band, same action. The quarterly Rate Environment Gate refresh (October) should be checked for whether it already moved the standing regime.

---

## 7. Composite Score (Quality 89.7 / Valuation 30.9, 50/50)

## Composite Score

```
Composite Score = 0.50x(100 - 89.7) + 0.50x30.9 = 20.600 -> rounds to 20.6
```

# Composite Score = 20.6
(Quality Score 89.7, Valuation Score 30.9)

Band **0.0–29.9 "Very Cheap"** → nominal Action Table: BUY — full position 6–8%.

### Why the score moved (23.0 → 20.6)

| | 09-17 | 11-05 | Driver |
|---|---|---|---|
| Quality | 90.3 | **89.7** | FCF Quality sub-score now uses (FCF−SBC)/NI = 62.09% → 36.82 (was 43.08 on plain FCF/NI) = −0.6 pts; other sub-scores unchanged |
| Valuation | 36.2 | **30.9** | FCF yield 2.41%→2.82% (score 75.9→73.4 after SBC cost, +0.16% SBC yield); EV/EBIT 26.6×→22.7× (63.3→46.4); FwdPE and PEG already at 0; Upside/Downside still the −15.0 floor (E now +46.9%/yr vs +33.9%) |
| Composite | 23.0 | **20.6** | Almost entirely the **−14.6% price decline since 09-17**; the methodology change (SBC as a cost) nudged the score the *other* way (slightly less attractive) |

No quality-relevant fundamental moved: no filing since 08-26/09-03.

---

## 8. Action Recommendation & Order Setup

**Fair value (Rule 3, 40% DCF-style scenario PW / 60% multiples):**
```
PW Fair Value (scenario)          = 0.25×432.00 + 0.50×332.01 + 0.25×176.00 = $318.005
Multiples (mean of two aggregator PTs) = (327.14 + 318.85) / 2              = $322.995
Blended FV = 0.40×318.005 + 0.60×322.995                                    = $321.00
```
FV range ~$176 (bear) – $432 (bull), base ≈$332 (Rule 10 — a range, not a point). Composite 20.6 → MoS 17.5% (band-midpoint convention, unchanged), stop 22.5%, risk 1.5%, cap 8% — all inside the band's allowed ranges.

Script output (verbatim):

## Order Setup

```
Band: 0.0-29.9 (Enter now)
Buy Price = Fair Value (321.0) x (1 - 17.5%) = 264.8250
Live price 186.77 vs buy price ceiling 264.8250 -> enter now (live price at/below buy price ceiling); entry price used = 186.7700
Primary Sell Target = Fair Value = 321.0000
Bull-Case Trim Target = Bull FV (432.0) x 0.90 = 388.8000
Stop Loss = Entry Price (186.7700) x (1 - 22.5%) = 144.7468
R/R Ratio = (Sell Target 321.0000 - Entry 186.7700) / (Entry 186.7700 - Stop 144.7468) = 134.2300/42.0232 = 3.1942:1
Max $ Risk = Portfolio Value (46102.05) x 1.5% = 691.5308
Risk Per Share = Entry (186.7700) - Stop (144.7468) = 42.0232
Shares by risk-based sizing = 691.5308 / 42.0232 = 16.4559
Allocation cap = Portfolio Value (46102.05) x 8% = 3688.1640 -> 19.7471 shares
Position Size (shares) = min(risk-based, cap) = 16.4559  [binding: risk-based sizing]
Position Size ($) = 16.4559 x 186.7700 = 3073.4700
Current shares held = 19; gap vs. target = -2.5441
```

### Order Setup Checklist
```
[✓] Risk/Reward Ratio:      3.19:1  (must be >= 2:1)
[ ] BUY PRICE (ceiling):     264.82
[ ] Entry Price used:        186.77  (enter now (live price at/below buy price ceiling))
[ ] PRIMARY SELL TARGET:     321.00
[ ] BULL-CASE TRIM TARGET:   388.80
[ ] STOP LOSS:               144.75
[ ] Max $ Risk:               691.53
[ ] POSITION SIZE (shares):  16.4559  (binding: risk-based sizing)
[ ] POSITION SIZE ($):       3073.47
[ ] Current shares held:     19
```

### Interpretation

- **R/R 3.19:1 — passes the 2:1 gate comfortably** (09-17: 2.11:1). Live $186.77 is far below the $264.83 buy-price ceiling.
- **Sizing binds, not R/R.** Risk-based target is **16.46 shares**; the account holds **19**, i.e. **2.54 shares (~$475) above target**. The target is smaller than on 09-17 (18.66 sh) because the sizing base is now the framework account alone ($46,102 NLV, max $ risk $691.53) rather than the old blended ~$61K total (max $ risk $917.89); the lower price (smaller $ risk per share, $42.02 vs $49.21) only partly offsets that.
- **Practical action: HOLD the 19-share position — no add, no trim.** No add (already above target size). No trim: Composite 20.6 is nowhere near a trim band, and an over-target position is not itself a trim trigger — acting on a sizing gap created by a one-day price drop would be selling on price alone, which Rule 0 forbids.
- **Orders:** the standing NVDA BUY 1 @ $196.70 (ID 1346804726) is `REPLACED` with no live successor ([ibkr-orders.md](../portfolio/snapshots/ibkr-orders.md)). No replacement is recommended — the position is already over target size. No order was placed or modified by this session.
- **Cap note:** the position was 8.47% at the 11-02 sync ($205.40), above the 8% allocation cap row of the cap table; at $186.77 it is ≈7.7–7.8%. The drop, not an action, cured it — flag for the next `/rebalance` if NVDA re-rates upward before then.

**Thesis-invalidation triggers (unchanged from 09-17, plus new):**
- AI-capex digestion: hyperscaler capex growth decelerating/reversing without a one-off cause — **the print is the test**, against the $108.0B Q3 FY2027 revenue guide.
- FCF/NI conversion: 65.85% plain / 62.09% after SBC TTM; re-test at FY2027 year-end (~Feb 2027) for the 2-consecutive-year disqualifier.
- **New watch:** the (unverified) report that NVIDIA told data-center clients to cut China exposure, and the 11-04 report of proposed data-center limits — check the next 8-K / earnings call for any change in guidance or the China assumption.
- Gross margin falls >3pp structurally (TTM 74.68%; FY26 annual was 71.1%, so the margin is not monotonic — see §4); CUDA moat erosion; net debt/EBITDA rising (Hugging Face ~$11.9B, closing H1 2027); regulatory restriction on open-weight model distribution.
- Price through the $144.75 stop level (informational).

All final-decision authority rests with the human investor.

---

## 9. Next Review Trigger

- **NVDA Q3 FY2027 earnings — ≈17 Nov 2026 after close per finviz (09-17 log estimated ~25 Nov; neither confirmed by NVIDIA IR).** A standard post-earnings `/rescore` is due immediately after; this off-cycle run will be superseded by it. It will refresh every TTM input reused here.
- Rate Environment Gate: 10Y 4.95%, within 0.05pp of the 5% bracket line (touched 5.05% on 10-28).
- Re-run immediately on: a filed 8-K / guidance revision, confirmation of the China-exposure report, or a >15% unexplained move (Rule 9).
- Open methodology items: forward-EPS source choice (finviz vs stockanalysis); yfinance outage; 5yr PE history still reused.

---

## Glossary

| Term | Meaning |
|---|---|
| **10-Q (Quarterly Report)** | The quarterly financial-disclosure report a US public company files with the SEC between annual 10-Ks, containing unaudited (reviewed) financial statements for the most recent fiscal quarter — used in this framework to reconstruct trailing-twelve-month (TTM) figures between annual reports, as in the 2026-07-06 AAPL session. |
| **8-K** | The "current report" a US public company must file with the SEC within days of a material event — most commonly used to furnish (via an attached exhibit, typically "Exhibit 99.1") a quarterly earnings press release ahead of the fuller, audited 10-Q/10-K that follows weeks later. Apple's fiscal Q3 2026 results were sourced from its 30 July 2026 8-K (Exhibit 99.1) in this framework's 2026-07-31 AAPL session, since the corresponding 10-Q had not yet been filed. *(New term.)* |
| **Composite Score** | This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50 — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only for companies that have already cleared the 80.0+ Quality Score gate. Used against the Phase 03/05 action tables instead of the raw valuation score. See [valuation-scoring.md](valuation-scoring.md). |
| **Quality Score** | This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. See [quality-scoring.md](quality-scoring.md). |
| **Valuation score** | This framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive) combining the Phase 02 valuation sub-scores, the Rate Environment Gate, and the Upside/Downside Modifier into a single number that maps to an action band (Very Cheap/Cheap/Fair Value/Expensive) — see [valuation-scoring.md](valuation-scoring.md). |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper. |
| **SBC (Stock-Based Compensation)** | Employee pay in the form of company shares or stock options rather than cash. A non-cash expense added back in cash-flow statements (inflating FCF relative to GAAP net income), but a real economic cost to existing shareholders through ongoing dilution — worth tracking alongside FCF/NI conversion and share-count trend, not just the headline FCF figure. Since the 2026-10-12 methodology it is treated as a cost in both the FCF yield (Valuation) and FCF Quality (Quality). |
| **EV** | Enterprise Value — a company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT, EV/EBITDA** | Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **Forward PE** | Price ÷ next twelve months' *expected* earnings per share (vs. Trailing PE, which uses the last twelve months' actual earnings). |
| **PEG ratio** | PE ratio ÷ earnings growth rate — a PE adjusted for growth, used to judge whether a fast grower's multiple is justified by its growth rate. |
| **Fast Grower** | Peter Lynch's term for a company growing earnings per share (EPS) faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury). |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in. |
| **Treasury yield (10Y)** | The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | An additive ±15 adjustment to the valuation score based on expected annual return (the gap to PW Fair Value, annualized over the catalyst window, plus intrinsic growth and shareholder yield) — folds the forward-looking dimension into the score so strong expected upside pulls a name toward "buy" and a thin/negative expected return pushes it toward "trim/sell." |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value estimate — 25% bull case + 50% base case + 25% bear case (Rule 7) — used as the single fair-value input to both the order setup and the Upside/Downside Modifier. |
| **FV (Fair Value)** | The analyst's estimate of what a company is intrinsically worth, independent of its current market price. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set, as a cushion against being wrong — e.g. a 25% MoS means buying at 75% of estimated fair value. |
| **R/R (Risk/Reward ratio)** | (Expected gain) ÷ (Expected loss) on a trade — this framework requires at least 2:1 before entering. |
| **Stop loss** | A pre-set price below the entry at which a position is exited to cap the loss on a trade; this framework sets it 20–35% below entry depending on the Composite Score band (fair-value-methodology.md Step 4), and the position size is derived from it so a stop-out costs only 1–2% of the portfolio. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results (the last four quarters added together), as opposed to a single fiscal year or a forward-looking estimate. *(New term.)* |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. |
| **Hard disqualifier** | One of three Quality Score conditions ([quality-scoring.md](quality-scoring.md)) that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation. A weighted average can't average away an outright balance-sheet or cash-flow-quality failure. |
| **Cycle peak** | The top of a business cycle, when earnings are temporarily inflated (e.g. memory-chip prices at a high). A stock then looks cheap on trailing earnings exactly when it is most expensive on normal earnings. This framework flags it when trailing EPS grew more than 100% in a year. |
| **Advisory flag** | A warning printed during analysis (e.g. `CYCLE_PEAK_CANDIDATE`, `MULTIPLE_CEILING`, `VALUE_TRAP_CANDIDATE`, the SBC block) that changes **no** score or action by itself. The analyst must say in the session log how it was handled; `UNKNOWN` means missing data, not a pass. See valuation-scoring.md, "Advisory Flags". |
| **Value trap** | A stock that looks statistically cheap (low valuation score/multiples) but stays cheap or keeps falling because the underlying business quality is actually deteriorating or was never strong enough to support a re-rating — the risk this framework's 80.0+ Quality Score gate and Composite Score are specifically designed to surface, rather than acting on an attractively-cheap valuation score alone. |
| **Moat** | Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. |
| **CUDA** | NVIDIA's proprietary parallel-computing software platform and programming model for its GPUs — the dominant software layer AI/ML developers build on, and the basis for this framework's Network Effect (ecosystem value grows as more developers join) and Switching Costs (production code/pipelines built around it) moat-signal findings for NVDA. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **yfinance** | An unofficial open-source Python library that scrapes Yahoo Finance for prices and fundamentals; this repo's `fetch_fundamentals` script depends on it, so when Yahoo rate-limits it ("Too Many Requests") that script fails and figures must be sourced elsewhere (SEC EDGAR, finviz, stockanalysis.com) and flagged. |
| **Market Cap (Market Capitalization)** | Share price × total shares outstanding — the total value the market currently assigns to all of a company's equity. Combined with Net Debt, gives Enterprise Value (EV). *(New term.)* |
| **Catalyst window** | The timeframe (per Rule 10, typically 18–24 months) within which a documented, specific event is expected to close the gap between price and fair value — required before the Upside/Downside Modifier can credit large expected upside. |
| **Hugging Face** | An AI developer platform and community (18M+ developers, 3M+ shared models, 500K+ datasets, 1M+ applications as of the 2026-09-02 announcement) for building, sharing, and deploying open-source/open-weight AI models. NVIDIA entered a definitive agreement to acquire it for a combined ~$12.9B (~$11.9B payable to Hugging Face stockholders plus up to ~$1.0B in employee-retention equity, per NVIDIA's 2026-09-03 SEC 8-K), expected to close H1 2027; NVIDIA has committed to keeping the platform open to all silicon vendors, not just its own. Cited in this framework's 2026-09-04 NVDA session as a verified (via primary SEC filing) Rule 9 M&A trigger and corroborating Network Effect moat evidence — not yet closed, so it moves no TTM financial input this session. *(New term.)* |
| **Debt Gate** | This framework's balance-sheet check on Net Debt/EBITDA (Hybrid Upgrade 5) — standard threshold <2.5×, relaxed to <4× for asset-light payment networks/exchanges with strong interest coverage and investment-grade ratings. |

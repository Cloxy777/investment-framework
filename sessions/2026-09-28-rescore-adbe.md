# RESCORE — ADBE (Adobe Inc.) — 2026-09-28

## 1. Session header

- **Task type:** RESCORE (single ticker, `--both` mode — Quality + Valuation)
- **Date:** 2026-09-28
- **10Y US Treasury yield:** 5.18% (FRED `DGS10`, most recent posted value, 2026-09-24 — 09-25 through 09-28 not yet posted; contemporaneous news coverage puts the 09-28 intraday print at ~5.21%, "near a 20-year high," consistent with this framework's established practice of using FRED's most recent posted value)
- **Rate Regime Modifier in effect:** +10 (10Y crossed into the >5% bracket — up from +5 at last review, when 10Y was 4.83%)
- **Prior scores (2026-09-11):** Valuation 0.0 (floor), Quality Score 83.3, Composite Score 8.4 — BUY, top up toward target
- **Current ADBE weight:** 4.06% of portfolio per [holdings.md](../portfolio/holdings.md) (10 shares held, avg cost $202.07, per [snapshots/ibkr.md](../portfolio/snapshots/ibkr.md) 2026-09-20 sync); combined portfolio value $61,220.66 (2026-09-20 sync)
- **Sector:** Technology — Software (Business Professionals & Consumers / Creative & Marketing Professionals — Adobe's Customer-Group reporting structure)
- **Trigger for this session:** requested as part of a scheduled rescore batch. No new earnings have occurred since the 2026-09-11 rescore (Q4 FY2026 is not due until ~mid-December 2026), but two independent Rule 9 conditions are live: (1) a **macro shift** — the 10Y Treasury has moved from 4.83% to 5.18%+ (a "near 20-year high" bond-market selloff), crossing the Rate Regime Gate's >5% bracket, which [operating-calendar.md](../framework/operating-calendar.md)'s Rule 9 table requires be met with "Update Rate Environment Gate + re-score"; and (2) the **explicit follow-up review trigger** set by the 09-11 session itself — David Wadhwani's departure from Adobe (announced 2026-09-02) took effect 2026-09-27, one day before this session, so the moat/segment-risk item flagged then is checked now, not just on announcement.
- **This session's job:** (1) fetch live price (Rule 0), (2) recompute the Quality Score off the same TTM financials (no new fiscal quarter has closed since 09-11 — confirmed via `scripts.fetch_fundamentals`, not assumed), (3) recompute the Valuation Score (Rate Gate + all sub-scores + Upside/Downside Modifier) off the new live price and rate regime, reusing the fair-value work from 09-11 (no new earnings-driven refresh trigger fired), (4) recombine into the Composite Score, (5) produce the action recommendation and order setup, (6) check the Wadhwani-departure follow-up and scan for any other fundamental events since 09-11.

## 2. Data gaps flagged (before proceeding)

None that blocked this session; all required inputs were sourced (see below). Flagged for transparency:

1. **Q3 FY2026 10-Q may still not be filed** as of this session (not independently re-verified this pass — the 09-11 session's reconstruction of TTM cash-flow figures from the 8-K press release plus the already-filed Q1/Q2 FY26 10-Qs is reused unchanged, since no new fiscal quarter has closed and `scripts.fetch_fundamentals` confirms the same TTM figures within rounding — see §4).
2. **Point-in-time shares outstanding.** `scripts.fetch_fundamentals` reports 397.5M shares outstanding (yfinance's current field) — used directly this session as the designated auto-fetch tool's output, rather than re-deriving the 09-11 session's 395M weighted-average-diluted proxy. The two are within 0.6% of each other and don't move any sub-score band.
3. **"Slowing net-new ARR" claim (Morgan Stanley / market commentary) not independently corroborated with a primary-sourced figure this session.** Several September post-earnings commentary pieces (Yahoo Finance, Tickeron) assert net-new ARR deceleration, but a search for Adobe's own disclosed net-new Digital Media/Business-Segment ARR figure for Q3 FY26 (vs. the Q3 FY24 comp of $504M cited in an older 8-K) did not surface a clean, cited, primary-source number this session. Per "never invent or estimate financial data," the Growth Score's **−10 structural-deceleration modifier is NOT applied** — this is flagged as a Quality Watch item for the next session, when the 10-Q (with full historical ARR tables) should be filed and this can be checked properly, rather than either inventing the figure or applying an uncorroborated commentary-sourced penalty.
4. **Fair value (DCF/multiples) not re-run from scratch this session.** Per Rule 9, a full FV refresh is required on a **quarterly earnings release** — that was already done in the 09-11 session, and no new earnings, guidance revision, or M&A event has occurred since. Consistent with the 07-29 session's precedent (a price-only/macro re-check that carried forward FV unchanged), this session reuses the 09-11 session's Blended FV ($403.79), Bull DCF ($685.32), and Bear DCF ($274.60) unchanged, and only recomputes the inputs that actually changed (live price, 10Y yield, Upside/Downside Modifier's `E`). Flagged rather than silently re-running a full DCF with a bumped-up WACC on the new 10Y — that would be a same-session invented adjustment without a documented, sourced WACC methodology change.

## 3. Live data (Rule 0 — fetched first)

| Item | Value | Source |
|---|---|---|
| **Live price used** | **$231.03** | IBKR `get_price_snapshot` (contract_id 265768, NASDAQ) — last trade, timestamp 2026-09-28 19:43:09 UTC (confirmed same-day/current) |
| Bid / Ask | $230.93 / $231.03 | IBKR `get_price_snapshot` |
| Change vs. prior close | −$4.44 / −1.89% | IBKR `get_price_snapshot` |
| 52-week high / low | $363.70 / $190.12 | IBKR `get_price_snapshot` `misc_statistics` |
| 13-week high / low | $294.53 / $201.31 | IBKR `get_price_snapshot` `misc_statistics` |
| Shares outstanding | 397,500,000 (yfinance current field) | `python -m scripts.fetch_fundamentals ADBE` |
| Market Cap (recomputed off live price, Rule 0) | 397,500,000 × $231.03 = **$91,834,425,000** | Computed (fetch_fundamentals' own embedded price was $230.74 — a stale-by-hours yfinance quote; recomputed with the IBKR live print instead, consistent with Rule 0 and the SPGI-error lesson) |
| Net Debt (from fetch_fundamentals' EV − MktCap) | $1,070,768,128 | Computed: EV $92,789,923,840 − MktCap(fetch) $91,719,155,712 |
| Enterprise Value (recomputed off live price) | $91,834,425,000 + $1,070,768,128 = **$92,905,193,128** | Computed |

## 3.5 Fundamental-event review since 09-11

- **David Wadhwani's departure took effect 2026-09-27** (one day before this session), per Adobe's 2026-09-08 8-K (Item 5.02) and confirmed by press coverage (CNBC, Yahoo Finance). He remains as a senior advisor during the transition; per his own LinkedIn comments, he plans to explore new company ideas rather than staying at Adobe. **This is a scheduled, previously-disclosed event taking effect on schedule** — not a new surprise. No new moat-signal evidence (positive or negative) has surfaced from this specifically; the 09-11 session's moat checklist (3/5 true) is carried forward unchanged (see §4).
- **Anil Chakravarthy's CEO transition remains on track for 2026-12-01** — no change to the announced timeline found.
- **FY2026 guidance is unchanged** since the 09-10 earnings release: revenue $26.576B–$26.626B, non-GAAP EPS $24.45–$24.50 (midpoint used for Forward PE below), Q4 revenue $6.8B–$6.85B, Q4 non-GAAP EPS $6.30–$6.35. No revision found — not a Rule 9 guidance-revision trigger.
- **Morgan Stanley reiterated Underweight, PT $240**, post-earnings, citing limited near-term upside, creative-tools competitive pressure, and uncertainty about AI monetization inflection. An analyst opinion, not itself a Rule 9 trigger, but noted as context for the stock's continued post-earnings drift lower.
- **Macro: 10Y Treasury yield jumped from 4.83% (09-11) to 5.18%+ (09-24/09-28)** — a genuine "macro shift" per the Rule 9 table, driving the Rate Regime Modifier bracket change (see §5).
- **Price move since 09-11:** $244.30 → $231.03 = **−5.43%** — well under the ±15% "unexplained move" Rule 9 threshold, and in any case explained (soft-relative-to-top-of-range Q4 guide, AI-competition narrative, CEO-transition overhang, and now the rate selloff), so this is not an independent trigger on its own.

## 4. Quality Score (recomputed via `scripts.scoring.quality_score`)

TTM period is unchanged from the 09-11 session (through Q3 FY2026 — no new fiscal quarter has closed). Inputs refreshed via `python -m scripts.fetch_fundamentals ADBE`:

```
Market Cap            = 91,719,155,712 (fetch's own embedded price; live-price recompute in §3)
Enterprise Value      = 92,789,923,840
Shares Outstanding    = 397,500,000
Forward PE            = 8.338  (fetch's own price-based figure; recomputed in §6 off live price)
FCF Yield %           = 11.548  (fetch's own; recomputed in §6 off live price)
EV/EBIT               = 9.725  (fetch's own; recomputed in §6 off live price)
Net Margin %          = 28.048
Gross Margin %        = 89.253
ROIC % (NOPAT/InvCap) = 41.990  [tax_rate=0.2152, NOPAT=7,488,055,597, InvestedCapital=17,833,000,000]
Revenue 3yr CAGR %    = 10.522
Net Debt/EBITDA       = 0.079
FCF/NI TTM %          = 145.415
FCF/NI annual (oldest first) = [155.5%, 127.9%, 141.6%, 138.2%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 25.116 / 8.936 / 44.603  (n=20 quarters)
```

**Script output (`python -m scripts.scoring.quality_score --input`), pasted verbatim:**

```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((28.048/30)x100) = 93.49
ROIC_Component = clamp((41.99/30)x100) = 100.00
Profitability_Score = (93.49 + 100.00) / 2 = 96.75

**Margins (15%)**
GrossMargin_Score = clamp((89.253/80)x100) = 100.00

**Growth (20%)**
Growth_Score = clamp((10.522/25)x100) = 42.09
+10 TAM/pricing-power evidence: Adobe Q3 FY2026 press release (2026-09-10, filed via 8-K): AI-first ARR
grew >150% YoY to over $650M; Adobe surpassed 1 billion monthly active users (MAU) across creativity and
productivity solutions. Carried forward unchanged from the 2026-09-11 rescore -- no new fiscal quarter has
closed since (Q4 FY26 reports ~mid-Dec 2026), so there is no newer primary-source data point to update this on.
Growth_Score (final, clamped) = 52.09
  (No -10 structural-deceleration penalty applied -- see Data Gap #3: uncorroborated commentary claim, not a
   cited primary-source figure.)

**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - 0.079/4)) = 98.02

**Moat Signal (15%)** -- checklist unchanged from 09-11 (no new evidence either direction this session):
  market_share_stable_or_growing: TRUE
  brand_premium: TRUE
  network_effect: FALSE
  switching_costs: TRUE
  scale_cost_advantage: FALSE
Moat_Score = (3/5) x 100 = 60.00

**FCF Quality (10%)**
FCFQuality_Score = clamp(((1.4541 - 0.40)/0.60)x100) = 100.00

**Quality Score -- Final**
Quality Score = (96.75x0.25) + (100.00x0.15) + (52.09x0.20) + (98.02x0.15) + (60.00x0.15) + (100.00x0.10)
              = 24.19 + 15.00 + 10.42 + 14.70 + 9.00 + 10.00
              = 83.308 -> rounds to 83.3

# Quality Score = 83.3 -- PASSES the 80.0+ gate
```

**Hard disqualifier check** — none fire (unchanged): FCF/NI conversion 128–156% across FY2022–FY2025 and 145.4% TTM (comfortably >70%); Net Debt/EBITDA 0.08× (far under 2.5×/4× thresholds); FCF positive every year on record.

**Quality Score = 83.3 — unchanged from 09-11 and PASSES the 80.0+ gate.** No margin/tax drift this session (same TTM period) — the modest Profitability compression flagged 09-11 (96.7 vs. the 100.0 ceiling in every earlier ADBE session) persists but has not worsened.

## 5. Rate Environment Gate (recomputed off live price and current 10Y)

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $231.03 / $24.475 (FY2026 non-GAAP EPS guidance midpoint, unchanged since 09-10) = 9.4394×
EY = 1 / 9.4394 = 10.5939%
Spread = 10.5939% − 5.18% (10Y) = +5.4139%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** → no +5 additive.

**Step 2 — Rate Regime Modifier**
10Y = 5.18% → **">5%"** bracket (a regime change since 09-11, when 10Y was 4.83% in the "3.5–5%" bracket) → **+10** (up from +5)

**Total Rate Modifier for ADBE = +10**

## 6. Phase 02 — Valuation Score (script output, pasted verbatim)

Inputs recomputed off the live price ($231.03) and current 10Y (5.18%); fair-value scenario inputs reused unchanged from 09-11 (no new earnings-driven refresh trigger — see Data Gap #4):

```
fcf_yield_pct = 11.5335   (FCF $10,591,728,102 / Market Cap [live] $91,834,425,000)
ev_ebit       = 9.7371    (EV [live] $92,905,193,128 / EBIT $9,541,380,343)
forward_pe    = 9.4394    (live price / FY26 guidance midpoint EPS $24.475)
pe_5yr_avg    = 25.116    (fallback/avg formula -- same methodology choice as every prior ADBE session,
                           for cross-session consistency, despite a range being computable)
fast_grower   = false     (FY24/25 non-GAAP EPS growth 14.55%/13.74%, both <15% -- unchanged finding)
```

```
## Valuation Score

**FCF Yield (40%)**
FCF_Score = clamp(100x(1 - 11.5335/10)) = 0.000

**EV/EBIT** (PEG not applicable -- weight redistributed here, 40% total)
EV/EBIT_Score = clamp((9.7371 - 12)/23 x 100) = 0.000

**Forward PE**
Deviation% = (9.4394 - 25.116)/25.116 x 100 = -62.417%
FwdPE_Score = clamp(50 + -62.417x2.5) = 0.000 (fallback formula; Historical PE Modifier already folded in)

**Rate Environment Gate**
EY = 1/9.4394 x 100 = 10.5939%
Spread = EY - 10Y (5.18%) = 5.4139pp -> Step 1 = +0 (pass, >=1.5pp)
10Y = 5.18% -> Step 2 bracket modifier = +10
Total Rate Modifier = 0 + 10 = +10

**Upside/Downside Modifier**
PW Fair Value = 0.25x685.32 + 0.50x463.87 + 0.25x274.6 = 471.9150
Gap Upside % = (471.9150/231.03) - 1 = 104.2657%
Annualized gap = 104.2657% / 2.0yr = 52.1328%/yr
E = 52.1328 (annualized gap) + 10 (intrinsic growth) + 6.5000 (shareholder yield: 0 div + 6.5 buyback,
    unchanged from 09-11's recomputation) = 68.6328%/yr
E (68.6328%) >= H (10.0%) -> M = -15 x clamp((68.6328-10.0)/15, 0, 1) = -15.0000
Upside/Downside Modifier (bounded [-15, +15]) = -15.0000

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2 = 0.000

**Final Valuation Score**
Final Score = Raw (0.000) + Rate Modifier (+10) + Upside/Downside Modifier (-15.000)
            = -5.000 -> rounds to 0.0

# Valuation Score = 0.0
```

**Guardrails check:**
- Catalyst within 18–24mo? **Yes** — Q4 FY26 print (~Dec 2026, ~2.5 months out) and continued AI-monetization scaling through FY2027. Upside-side credit not capped.
- Scenario-weighted (not the rosy point)? **Yes** — bull/base/bear DCF blend carried forward unchanged from 09-11.
- The Rate Regime Modifier moving +5→+10 and the Upside/Downside Modifier's `E` widening (49.14%→68.63%/yr, purely because the price gap to an unchanged Blended FV widened) both pull in the same direction here — more attractive, not less — but the Final Score is already floored at 0.0 either way, so neither shift changes the outcome. Shown for calculation transparency (no black-box outputs).

## 7. Final Valuation Score + Composite Score

```
python -m scripts.scoring.composite_score --set quality_score=83.3 --set valuation_score=0.0

## Composite Score
Composite Score = 0.50x(100 - 83.3) + 0.50x0.0 = 8.350 -> rounds to 8.4

# Composite Score = 8.4
(Quality Score 83.3, Valuation Score 0.0)
```

| | Value |
|---|---|
| Quality Score | 83.3 (unchanged from 09-11) — PASSES 80.0+ gate |
| Valuation Score | 0.0 (floor, unchanged) |
| **Composite Score** | **8.4** (unchanged from 09-11) |

**Composite Score = 8.4 — unchanged from 09-11**, still deep in the **0.0–29.9 "Very Cheap"** band → **BUY — Full position 6–8%** (Phase 03 action table). Same action category as the last review; the rate-regime shift and the wider price gap to an unchanged fair value both pulled inputs in the more-attractive direction this session, but the score was already floored, so the net numeric result is identical. This is not a "nothing happened" outcome, though — it is a **confirmed re-check under a genuinely worse macro backdrop (a near-20-year-high 10Y) and a completed management transition**, and the thesis holds up unchanged, which is itself informative.

## 8. Fair Value & Order Setup (BUY action — full setup required)

Fair value inputs carried forward unchanged from 09-11 (see Data Gap #4): Blended FV $403.79, Bull DCF $685.32, Bear DCF $274.60.

**Script output (`python -m scripts.scoring.order_setup --input`), pasted verbatim:**

```
## Order Setup

Band: 0.0-29.9 (Enter now)
Buy Price = Fair Value (403.79) x (1 - 17.5%) = 333.1268
Live price 231.03 vs buy price ceiling 333.1268 -> enter now (live price at/below buy price ceiling);
  entry price used = 231.0300
Primary Sell Target = Fair Value = 403.7900
Bull-Case Trim Target = Bull FV (685.32) x 0.90 = 616.7880
Stop Loss = Entry Price (231.0300) x (1 - 22.5%) = 179.0482
R/R Ratio = (403.7900 - 231.0300) / (231.0300 - 179.0482) = 172.7600/51.9818 = 3.3235:1
Max $ Risk = Portfolio Value (61220.66) x 1.5% = 918.3099
Risk Per Share = 231.0300 - 179.0482 = 51.9818
Shares by risk-based sizing = 918.3099 / 51.9818 = 17.6660
Allocation cap = Portfolio Value (61220.66) x 8% = 4897.6528 -> 21.1992 shares
Position Size (shares) = min(risk-based, cap) = 17.6660  [binding: risk-based sizing]
Position Size ($) = 17.6660 x 231.0300 = 4081.3773
Current shares held = 10; gap vs. target = 7.6660
```

### Order Setup Checklist
```
[x] Composite Score (Quality 83.3 + Valuation 0.0):  8.4   (<= 49.9 OK)
[x] Expected annual return E / catalyst window:      +68.63% / 2 yr
[x] Upside/Downside Modifier applied:                -15.0
[x] DCF Fair Value (PW):                             $471.92  (unchanged inputs from 09-11)
[x] Multiples-Based Fair Value:                       $358.38  (unchanged, carried from 09-11)
[x] Blended Fair Value:                                $403.79
[x] Margin of Safety %:                                17.5%
[x] BUY PRICE (ceiling; live already far below):       $333.13
[x] PRIMARY SELL TARGET:                               $403.79
[x] BULL-CASE TRIM TARGET:                             $616.79
[x] STOP LOSS:                                         $179.05
[x] Risk/Reward Ratio:                                 3.32:1  (>= 2:1 OK -- improved vs. 09-11's 2.90:1,
                                                         since price fell further while stop widened proportionally)
[x] Max $ Risk:                                        $918.31
[x] POSITION SIZE (target, rounded down, conservative): 17 shares (from 17.666 risk-based)
[x] POSITION SIZE ($):                                 17 x $231.03 = $3,927.51 = 6.42% of $61,220.66
[x] Thesis invalidation triggers:                      see §9
```

### Position sizing — top-up toward the (updated) target
```
Full target (rounded down, conservative) = 17 shares (up from 09-11's 16 -- risk budget grew modestly with
  portfolio value, and risk-per-share fell as the price dropped, both pushing the risk-based share count up)
Held = 10 shares (unchanged; 2026-09-20 IBKR sync confirms no ADBE share-count change)
TOP-UP = 7 shares
Top-up cost = 7 x $231.03 = $1,617.21
Resulting position = 17 x $231.03 = $3,927.51 = 6.42% of the $61,220.66 combined portfolio
```
**Cap cross-check:** 6.42% sits inside the 6–8% Very Cheap band and far under the 15% hard cap (Upgrade 7).

## 9. Action, Thesis Status & Recommendation

**Recommendation: CONFIRMED BUY — top up 7 shares (~$1,617, to reach a 17-share / 6.42% target). Composite Score 8.4 ("Very Cheap"), unchanged from 09-11.**

Nothing in this session's data changes the thesis. Quality Score (83.3) and Valuation Score (0.0, floor) are numerically identical to the 09-11 rescore because no new fiscal quarter has closed and no new earnings-driven fair-value refresh trigger has fired — this is a genuine "nothing new happened financially" finding, not a shortcut. What *did* change is the backdrop: the 10Y Treasury spiked to a near-20-year high (4.83%→5.18%+), which by itself would normally be a headwind (higher discount rates, tighter Rate Regime Gate bracket), yet ADBE's Rate Regime Modifier actually improved (+5→+10, since ADBE's earnings yield still clears the Treasury by a wide +5.41pp spread) and the Upside/Downside Modifier's expected return widened (49.1%→68.6%/yr) simply because the stock fell further against an unchanged fair value — both effects were already floored out in the prior session's 0.0, so the net score doesn't move, but the setup is, if anything, more attractive on a forward-return basis, not less.

The one specific event flagged as a forward risk in the 09-11 session — **David Wadhwani's departure** — took effect 2026-09-27, one day before this session, on schedule and without incident. No new moat-erosion or segment-deprioritization evidence has surfaced as a result. The CEO transition to Anil Chakravarthy remains on track for 2026-12-01. A Morgan Stanley Underweight reiteration and unverified "slowing net-new ARR" commentary are both noted as watch items rather than scored inputs — the former is an opinion, not a scored input by framework design, and the latter lacks a primary-sourced figure this session (see Data Gap #3).

**Thesis invalidation triggers (Phase 06 / stop), carried forward from 09-11, unchanged:**
- Creative & Marketing Professionals subscription revenue growth decelerates toward mid-single-digits without a non-AI one-off cause (2 consecutive quarters) → thesis broken
- Gross margin falls >3pp structurally, or FCF/NI conversion <70% for 2 consecutive quarters
- Net debt/EBITDA rising materially on debt-funded buybacks while growth slows
- Evidence (post Dec-1 CEO transition) that Creative Cloud investment/priority is being deprioritized relative to the Experience/orchestration side of the business
- Price through the $179.05 stop (updated this session; was $189.33 at 09-11)
- **New this session:** Adobe's own next 10-Q discloses a net-new ARR figure confirming structural deceleration (not yet corroborated — see Data Gap #3) → apply the −10 Growth Score modifier at that point, per framework rule, not before

All final-decision authority rests with the human investor; funding is the investor's call.

## 10. Watchlist & stale-score disposition

- **Watchlist:** a new dated entry ([watchlist/in-portfolio/ADBE/ADBE-2026-09-28.md](../watchlist/in-portfolio/ADBE/ADBE-2026-09-28.md)) created via `scripts.watchlist_diff`, decision `new_file` — reason: **Rule 9 fundamental-event trigger fired** (the macro-shift 10Y Treasury regime change, plus the Wadhwani-departure follow-up check), even though the score/category are numerically unchanged (Composite 8.4, category BUY, both same as 09-11).
- **Stale-score mark:** see §11 — `scripts.stale_score --apply` run; ADBE's disposition reported there.

## 11. Next review trigger

- **Q4 FY2026 earnings (~mid-December 2026)** — mandatory re-score (Rule 9). Check whether Adobe's next 10-Q's net-new ARR disclosure corroborates or refutes the "slowing net-new ARR" commentary flagged this session (Data Gap #3), and whether Creative & Marketing Professionals subscription revenue growth holds ≥~10%.
- **CEO transition effective 2026-12-01** (Anil Chakravarthy) remains the next scheduled leadership-transition checkpoint; Wadhwani's departure (effective 2026-09-27) has now occurred without incident — no further follow-up needed on that specific item unless new moat/segment evidence surfaces.
- **>15% unexplained move from $231.03** in either direction — immediate re-score (Rule 9).
- **If the 10Y Treasury regime shifts again** (a further move would cross back below 5%, or further up) — informational only; already re-run this session, and the Rate Regime Modifier only matters at the margin here since the Valuation Score is floored.
- **If the top-up is executed**, log it in [decisions/](../decisions/) and reflect it at the next `/sync-portfolio` (holdings.md is handled by the orchestrator, not this session).

## 12. Glossary

- **8-K:** the SEC "current report" filed within days of a material event (earnings, management change, etc.).
- **After-hours trading:** trading after the regular US session closes but before the next day's open — a genuine, live traded price.
- **ARR (Annual Recurring Revenue):** the annualized run-rate value of a subscription/recurring-revenue business's contracted revenue at a point in time.
- **CAGR:** Compound Annual Growth Rate.
- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50.
- **DCF:** Discounted Cash Flow — a valuation method projecting future cash and discounting it to present value.
- **D&A:** Depreciation & Amortization.
- **EBIT / EBITDA:** operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **Effective tax rate:** actual tax paid ÷ pretax income, distinct from the statutory rate.
- **EPS:** Earnings Per Share.
- **EV / EV/EBIT, EV/EBITDA:** Enterprise Value (market cap + net debt) / EV divided by EBIT or EBITDA, valuation multiples.
- **EY (Earnings Yield):** 1 ÷ Forward PE, compared against the 10-Year Treasury yield.
- **Fast Grower:** a company growing EPS >15%/yr for 3+ years — triggers the PEG sub-score.
- **FCF / FCF Yield / FCF/NI conversion ratio:** Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality).
- **Forward PE:** price ÷ next year's expected EPS.
- **FV (Fair Value):** the analyst's estimate of intrinsic worth, independent of market price.
- **GAAP:** Generally Accepted Accounting Principles — the standard US accounting rulebook this framework scores off of.
- **Gross Margin / Net Margin / Operating Margin:** Gross Profit, Net Income, and Operating Income each divided by Revenue.
- **Hard disqualifier:** one of three Quality Score conditions that fails a company regardless of weighted score.
- **Hurdle rate:** the minimum acceptable annual return (10% in this framework).
- **Invested Capital:** the total capital (debt + equity) at work in a business — the ROIC denominator.
- **Item 5.02 (Form 8-K):** the SEC 8-K disclosure item for a director/officer departure, election, or appointment.
- **MAU (Monthly Active Users):** unique users engaging with a product at least once in a given month.
- **Market Cap (Market Capitalization):** share price × total shares outstanding.
- **Moat:** a durable competitive advantage protecting a business's profits.
- **MoS (Margin of Safety):** the discount below fair value demanded before buying.
- **Net Debt/EBITDA:** a leverage ratio; this framework's primary balance-sheet-risk gate.
- **Non-GAAP:** a company's own adjusted presentation of a financial measure, excluded from this framework's scoring (which uses GAAP).
- **NOPAT:** Net Operating Profit After Tax — EBIT × (1 − effective tax rate).
- **PE (Price-to-Earnings) ratio / PEG ratio:** price ÷ earnings; PE ÷ growth rate.
- **pp (percentage points):** a direct difference between two percentages.
- **Quality Score:** this framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02.
- **Rate Environment Gate / Rate Regime Modifier:** the pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive Treasury-yield-band adjustment.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss); this framework requires ≥2:1.
- **ROIC:** Return on Invested Capital — NOPAT ÷ Invested Capital.
- **Shareholder yield:** dividend yield plus net buyback yield.
- **TAM:** Total Addressable Market.
- **Terminal Value:** the lump-sum value assigned to all DCF cash flows beyond the explicit forecast period.
- **Treasury yield (10Y):** the US government's 10-year borrowing rate, this framework's risk-free-rate benchmark.
- **TTM:** Trailing Twelve Months.
- **Upside/Downside Modifier (Expected-Return Modifier):** an additive ±15 valuation-score adjustment based on expected annual return.
- **WACC:** Weighted Average Cost of Capital — the discount rate used in a DCF.

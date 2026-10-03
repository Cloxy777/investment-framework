# NEW POSITION — NFLX (Netflix, Inc.) — 2026-10-03

**Task type:** NEW POSITION (fresh full evaluation of an **already-held** name, position-aware).
**Date:** 3 Oct 2026 (Saturday; US markets closed — price is the Friday 2 Oct close)
**Held position (IBKR `get_account_positions`, live):** 12 sh @ avg cost $87.79, market value $804.89, unrealized P&L -$248.59 (-23.6% vs cost $1,053.49). Weight ≈ **1.31%** of the combined $61,622.32 portfolio ([holdings.md](../portfolio/holdings.md) shows 1.38% at the 09-27 sync price). Standard-position target band 3-5% (15% hard cap).
**Prior record:** [2026-07-17 rescore](2026-07-17-rescore-nflx.md): Valuation 49.3 / Quality 69.8 / Composite 39.8 (reference only) -> HOLD.
**Sector:** Communication Services — Streaming Media & Entertainment

*Jargon is decoded in the closing Glossary.*

---

## 1. Live price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Price used** | **$67.07** | IBKR `get_price_snapshot` (contract 15124833). `top_status` = FROZEN; last-trade timestamp 2026-10-02 ~23:59 UTC = Friday regular-session close (market closed). `plprice` (mark) $67.0744 agrees; yfinance `currentPrice` $67.06 agrees. |
| Prior close / change | $67.85 / -$0.78 (-1.15%) | IBKR |
| 52-week range | $65.08 – $124.86 (13w high $83.60; 13w/26w/52w low all $65.08) | IBKR `misc_statistics`. Stock is 3.1% above its 52-week low and 46.3% below its high |
| Move since 07-17 | $67.80 -> $67.07 = **-1.1%** | far below the 15% Rule 9 threshold (the path in between was volatile: ~$72 in late Sept, 52-week low $65.08) |
| Analyst consensus PT | $92.93 mean (yfinance) | context only; never used as an input |

## 2. Rule 9 trigger check since 2026-07-17

| Trigger | Fired? | Detail |
|---|---|---|
| Earnings release | **No** | **Q3 2026 results are scheduled for Tue 20 Oct 2026** (after the close, 1:01 pm PT; Netflix's announcement as relayed by press/stocktitan; yfinance calendar also shows 2026-10-20). Not yet reported. Consensus Q3: EPS ~$0.82, revenue ~$12.88B (Netflix's own guide: $12.86B / EPS $0.82). **Next mandatory re-score: 21 Oct 2026.** |
| Q2 10-Q | Filed since 07-17 (SEC accession 0001065280-26-000212) | Cross-check only: diluted shares 4,261.3M (matches the 8-K), period-end shares outstanding 4,163.9M, cash $9,099.2M, total debt $14,309M, $2.8B WBD fee recorded in Q1 "interest and other income (expense)", $27.1B buyback authorization remaining. All agree with the 07-17 inputs; no TTM number changes. The cash tax paid on the WBD fee is **still not quantified** (not separately disclosed in the text retrieved). |
| Guidance revision | No | FY2026 guide (revenue $51.0-51.4B, operating margin 31.5%, FCF ~$12.5B) unchanged since 07-17. Consensus FY2026E EPS now $3.58 (was $3.57). |
| Management change / M&A | None found | |
| >15% unexplained move | No | -1.1% vs the 07-17 price. |
| **Macro (Rate Gate input)** | **Yes** | 10Y Treasury (FRED `DGS10`): 4.54% on 07-16 -> **5.24% on 2026-10-01** (latest posted; peak 5.29% on 09-30). It crossed the 5% line, so the Rate Regime bracket modifier moves from +5 to **+10**. |
| **News (not a formal trigger)** | **Yes, flagged** | Netflix fell ~14% in September (Motley Fool, 2026-10-01): Wells Fargo downgraded to Underweight with a $57 target (09-18); HSBC cut to Hold citing viewing share lost to YouTube; worst Emmy conversion in a decade (16 wins on 111 nominations); co-CEO Sarandos said Netflix is "not growing as fast as I want". Deutsche Bank upgraded to Buy, $95 PT (09-30), arguing the market over-reacts to weak US trends. These are secondary-source opinions — **not scoring inputs**; they bear on the Moat "market share" signal (sensitivity in section 4) and on the Q3 watch items. |

**Conclusion:** no new fundamentals (no earnings, no guidance change), but the 10Y regime change (a Rate Gate input) and heavy negative sentiment justify a full re-run. Financial inputs are the Q2 2026 TTM set (8-K/10-Q, unchanged); price, forward multiples, Rate Gate and fair values are recomputed.

## 3. Data gathered (nothing invented)

`python -m scripts.fetch_fundamentals NFLX` (verbatim):
```
## Fundamentals — NFLX

Market Cap            = 279,233,789,952
Enterprise Value      = 286,760,534,016
Shares Outstanding    = 4,163,939,676
Forward PE            = 17.580
FCF Yield %           = 3.994
EV/EBIT               = 16.537
Net Margin %          = 28.219
Gross Margin %        = 49.118
ROIC % (NOPAT/InvCap) = 34.936  [tax_rate=0.1724, NOPAT=14,351,001,783, InvestedCapital=41,078,324,000]
Revenue 3yr CAGR %    = 12.640
Net Debt/EBITDA       = 0.369  [EBITDA_ttm=14,726,931,456]
FCF/NI TTM %          = 81.702
FCF/NI annual (oldest first) = [36.0%, 128.1%, 79.5%, 86.2%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 37.874 / 19.325 / 55.816  (n=20 quarters)
```

**Basis note (same as 07-17).** The script reports **as-reported** TTM figures that still include the one-off $2.8B Warner Bros. termination fee (net margin 28.2%, FCF/NI 81.7%), uses basic period-end shares (4,163.9M, after the record Q2 buyback), and takes forward PE off yfinance's `forwardEps` $3.81 (the next-fiscal-year estimate, not FY2026E). The framework's established basis is used for scoring:
- **Rule 6 normalization:** fee removed — TTM net income $11,390.3M (net margin 23.55%), TTM FCF $8,352.0M, FCF/NI 73.33% (as-reported 81.70% shown as a sensitivity). TTM revenue $48,370.8M, EBIT $14,354.5M, EBITDA $14,726.9M (the script's EBITDA reproduces).
- **Diluted shares 4,261.3M** (company-disclosed Q2 count; the 4,163.9M period-end count is a sensitivity).
- **Net debt $5,181.4M** (debt $14,309.3M − cash & short-term investments $9,127.9M; the yfinance quarterly balance sheet agrees with the 8-K).
- **Forward EPS = FY2026E consensus $3.58364** (yfinance `earnings_estimate`, "0y", 41 analysts; 07-17 used $3.57) -> forward PE = $67.07 / $3.58364 = **18.72×**.
- **5yr PE range** refreshed by the script: avg 37.874 / low 19.325 / high 55.816 (07-17 carried 39.44 / 19.32 / 55.82). Forward PE is again **below the whole 5-year range**.
- **Revenue 3yr CAGR 12.64%** (script; 07-17 carried 12.51%).
- ROIC from scratch (inputs unchanged): NOPAT $12,389.4M ÷ invested capital $35,333.4M = 35.07% (the script's 34.94% uses a different invested-capital basis; both cap the ROIC component at 100).
- Market cap = 4,261.3M × $67.07 = $285,805.4M; EV = $290,986.8M; EV/EBIT = 20.27×; FCF yield = 2.922%.

## 4. Quality Score (Phase 01 gate)

Hard disqualifiers: none fire (FCF/NI below 70% for 2+ *consecutive* years — no, only FY2022 at 36.0%, followed by 128.1%; Net Debt/EBITDA 0.352× vs the 2.5× limit; FCF-positive 3+ years — yes).

`python -m scripts.scoring.quality_score` output (verbatim):

## Quality Score

**Profitability (25%)**
```
NetMargin_Component = clamp((23.548/30)x100) = 78.49
ROIC_Component = clamp((35.07/30)x100) = 100.00
Profitability_Score = (78.49 + 100.00) / 2 = 89.25
```
**Margins (15%)**
```
GrossMargin_Score = clamp((49.12/80)x100) = 61.40
```
**Growth (20%)**
```
Growth_Score = clamp((12.64/25)x100) = 50.56
+10 TAM/pricing-power evidence: Q2 2026 shareholder letter (8-K Ex. 99.1, 2026-07-16): ad revenue guided ~$3.0B in 2026 (roughly double YoY); recent price changes 'consistent with prior changes and our expectations'; double-digit revenue growth in every region (UCAN +10%, EMEA +14%, LATAM +21%, APAC +16%).
-10 structural growth deceleration evidence: Netflix guidance table: YoY revenue growth Q4'25 17.6% -> Q1'26 16.2% -> Q2'26 13.4% -> Q3'26 guided 11.7%; H1 2026 member viewing hours +2% YoY (Q2 shareholder letter); co-CEO Sarandos 'not growing as fast as I want' (Motley Fool 2026-10-01).
Growth_Score (final, clamped) = 50.56
```
**Balance Sheet (15%)**
```
BalanceSheet_Score = clamp(100x(1 - 0.352/4)) = 91.20
```
**Moat Signal (15%)**
```
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Revenue +13.4% YoY Q2 2026, double-digit in every region (Q2 letter). Counter-evidence noted (secondary source, HSBC via Motley Fool 2026-10-01): US TV viewing share lost to YouTube (7.8%); sensitivity run with FALSE. |
| brand_premium | True | Q2 2026 letter: price changes consistent with prior changes and expectations; ARM/pricing power without disclosed churn deterioration. |
| network_effect | False | No two-sided marketplace mechanism for core streaming. |
| switching_costs | False | Month-to-month cancel-anytime subscription. |
| scale_cost_advantage | True | Largest industry content spend (~$20B 2026 budget), carried forward from prior sessions; 10-Q Q2 2026 filed. |
Moat_Score = (3/5) x 100 = 60.00
```
**FCF Quality (10%)**
```
FCFQuality_Score = clamp(((0.7333 - 0.40)/0.60)x100) = 55.55
```
**Quality Score — Final**
```
Quality Score = (89.25x0.25) + (61.40x0.15) + (50.56x0.20) + (91.20x0.15) + (60.00x0.15) + (55.55x0.10)
= 69.869 -> rounds to 69.9
```

# Quality Score = 69.9 — FAILS the 80.0+ gate

**Moat sensitivity.** Marking the market-share signal FALSE (to reflect HSBC's secondary-source claim that Netflix is losing US viewing share to YouTube; the primary filings still show revenue growth in every region, so the primary run keeps it TRUE) gives, from the same script:
```
Quality Score = (89.25x0.25) + (61.40x0.15) + (50.56x0.20) + (91.20x0.15) + (40.00x0.15) + (55.55x0.10)
= 66.869 -> rounds to 66.9
# Quality Score = 66.9 — FAILS the 80.0+ gate
```

| Basis | Quality Score | Gate |
|---|---|---|
| **Normalized, moat as cited (primary)** | **69.9** | **FAILS** (10.1 pts below 80.0) |
| Market-share moat signal = FALSE | 66.9 | FAILS |
| 07-17 session (for reference) | 69.8 | FAILS |

Change vs 07-17: +0.1 (Growth 50.04 -> 50.56 from the refreshed 12.64% CAGR; Gross margin 61.39 -> 61.40 rounding). No real change — expected, since no new financials exist.

**The gate fails, so no new capital can go into this name.** The Valuation Score and Composite below are computed as **reference figures for a held position** (same convention as 07-05 and 07-17), not as an entry signal.

## 5. Rate Environment Gate

```
Forward PE = 67.07 / 3.58364 = 18.716x -> EY = 5.343%
Spread = 5.343% - 10Y (5.24%) = +0.103pp  -> below +1.5pp -> FAILS -> +5
10Y = 5.24% (above the 5% bracket) -> Step 2 = +10
Total Rate Modifier = +15   (07-17: +10)
```
10Y source: FRED `DGS10` CSV, latest observation 2026-10-01 = 5.24% (09-28 5.24, 09-29 5.26, 09-30 5.29). The 10-02 print had not posted. (A summarised FRED text-page fetch returned an inconsistent ~3.9% series; it was discarded in favor of the raw CSV, which matches the 5.24% used in the other 10-03 sessions.)

## 6. Valuation Score (Phase 02) — reference only

### 6.1 Fair value rebuilt (Rules 2, 3, 7)

I reproduced the 07-17 DCF exactly first (Bear/Base/Bull $34.90 / $53.80 / $82.30) and then changed only what legitimately moved:
- **WACC +0.8 pts** (risk-free 4.54% -> 5.24%): same 07-17 construction (risk-free + beta 1.4 × ERP 3.6% = 10.28%, rounded) -> base **10.3%**, bull 9.3%, bear 11.3%.
- FY2026 FCF anchors ($11.5B / $12.5B / $13.0B), growth fades and terminal growth: **unchanged** (guidance unchanged, no new filing).
- Net debt $5.181B, shares 4.2613B and forward EPS $3.58364 refreshed.

| Scenario | WACC | PV Stage 1 | PV Stage 2 | PV Terminal | EV | DCF FV/share | TV % of EV |
|---|---|---|---|---|---|---|---|
| Bear | 11.3% | $46.43B | $32.95B | $60.91B | $140.29B | **$31.71** | 43.4% |
| Base | 10.3% | $55.35B | $46.11B | $107.67B | $209.13B | **$47.86** | 51.5% |
| Bull | 9.3% | $62.47B | $60.46B | $184.88B | $307.80B | **$71.02** | 60.1% |

```
PW DCF FV = 0.25×71.02 + 0.50×47.86 + 0.25×31.71 = $49.61
```
Multiples (multiples held at the 07-17 judgments, EPS refreshed): Fwd PE comp 28 × $3.58364 = **$100.34**; EV/EBIT comp 18× on FY2026E EBIT $16.13B -> EV $290.39B − net debt $5.18B -> **$66.93**; FCF-yield comp 5.0% on $12.5B -> EV $250.0B − $5.18B -> **$57.45**. Multiples average **$74.91**.

Per-scenario blend (40% DCF + 60% comp; Bear<->FCF-yield, Base<->EV/EBIT, Bull<->Fwd-PE):

| Scenario | DCF | Comp | Blended |
|---|---|---|---|
| Bear | $31.71 | $57.45 | **$47.15** |
| Base | $47.86 | $66.93 | **$59.30** |
| Bull | $71.02 | $100.34 | **$88.61** |

```
PW Fair Value = 0.25×88.61 + 0.50×59.30 + 0.25×47.15 = $63.59   (07-17: $66.17)
Headline blended FV (0.40×$49.61 + 0.60×$74.91) = $64.79
```
The comps multiples (28× / 18× / 5.0% yield) are modeling judgments held constant from 07-17; note a 5.0% FCF-yield comp sits *below* the 5.24% risk-free yield, so the Bear-case comp is arguably generous in today's rate regime (not adjusted — no basis to invent a new multiple). Historical-PE cross-check (context only, 0% weight): TTM EPS $3.20 × 37.874 = $121.2.

**Rule 0 sanity check:** the live price $67.07 is 5.5% above PW FV ($63.59) and 3.5% above the headline blended FV ($64.79); the Street mean PT is $92.93. The framework's value stays well below the Street, as in every prior NFLX session.

### 6.2 Script output (`python -m scripts.scoring.valuation_score`, verbatim)

Input notes: forward PE on FY2026E EPS; intrinsic growth 11.0%/yr carried from 07-17 (no new guidance); net buyback yield 4.1% = H1 2026 net repurchases $5,875.7M × 2 ÷ market cap (carried from 07-17; Q3 buybacks unknown until 20 Oct); scenario values are the blended Bull/Base/Bear above; catalyst = Q3 print / ad ramp, 2-year window (Rule 10 default).

## Valuation Score

**FCF Yield (40%)**
```
FCF_Score = clamp(100x(1 - 2.9223/10)) = 70.777
```
**EV/EBIT**
```
EV/EBIT_Score = clamp((20.271 - 12)/23 x 100) = 35.961
```
**Forward PE**
```
FwdPE_Score (raw) = clamp((18.716 - 19.325)/(55.816 - 19.325) x 100) = 0.000
Deviation vs 5yr avg (37.874) = (18.716 - 37.874)/37.874 x 100 = -50.584%
Historical PE Modifier: >20% below 5yr avg -> -10
FwdPE_Score = clamp(0.000 + -10) = 0.000
```
**PEG**
```
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT
```
**Rate Environment Gate**
```
EY = 1/18.716 x 100 = 5.3430%
Spread = EY - 10Y (5.24%) = 0.1030pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.24% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15
```
**Upside/Downside Modifier**
```
PW Fair Value = 0.25x88.61 + 0.50x59.3 + 0.25x47.15 = 63.5900
Gap Upside % = (63.5900/67.07) - 1 = -5.1886%
Annualized gap = -5.1886% / 2yr = -2.5943%/yr
E = -2.5943 (annualized gap) + 11.0 (intrinsic growth) + 4.1000 (shareholder yield: 0 div + 4.1 buyback) = 12.5057%/yr
E (12.5057%) >= H (10.0%) -> M = -15 x clamp((12.5057-10.0)/15, 0, 1) = -2.5057
Upside/Downside Modifier (bounded [-15, +15]) = -2.5057
```
**Raw Weighted Score**
```
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 42.695
```
**Final Valuation Score**
```
Final Score = Raw (42.695) + Rate Modifier (+15) + Upside/Downside Modifier (-2.506)
= 55.189 -> rounds to 55.2
```

# Valuation Score = 55.2

### 6.3 Sensitivities (hand-computed with the same formulas)

| Variant | Valuation Score |
|---|---|
| **Primary (normalized, diluted 4,261.3M)** | **55.2** |
| As-reported FCF (fee left in; FCF yield 3.90% -> FCF_Score 60.98) | ≈51.3 |
| Basic period-end shares 4,163.9M (mkt cap $279.3B; FCF yield 2.99%, EV/EBIT 19.82×) | ≈54.1 |
| 07-17 WACC kept (PW FV ≈ $66.27, M ≈ -4.5) | ≈53.2 |
| 10Y back under 5% (rate modifier +10 instead of +15) | ≈50.2 |

All variants stay in the 50.0-69.9 **"Hold / Fair Value"** band (the lowest, ≈50.2, is right at the edge). The Hold reading is therefore not boundary-fragile on the upside, but a modest rate retreat plus any price drop would take the score back under 50.0 — the same boundary the 07-17 score (49.3) sat on.

## 7. Composite Score (reference only)

The script **refuses** (Quality below the gate):
```
# Composite Score REFUSED — Quality Score fails the 80.0+ gate
Quality Score 69.9 < 80.0 — fails the gate, Composite Score is not computed for a company that hasn't cleared Phase 01
```
By hand, as a reference-only figure (same convention as 07-05 and 07-17): 0.50 × (100 − 69.9) + 0.50 × 55.2 = 15.05 + 27.60 = 42.65 -> ".X5" boundary, round up (conservative) -> **42.7** ("Cheap" band, 30.0-49.9). With the moat sensitivity (Quality 66.9): 44.2. **This is a false green light** — it looks attractive only because a sub-80 Quality Score is inverted in the formula; the standalone Valuation Score (55.2) reads "Hold", not "Cheap". It is not an entry signal.

## 8. Order setup (reference; tests whether an add could even be executed)

Inputs: Composite 42.7 (band 30.0-49.9), blended FV $64.79, bull FV $88.61, 27.5% MoS and stop (band midpoints), risk 1.5%, position cap 4%, portfolio $61,622.32, current 12 sh.

## Order Setup

```
Band: 30.0-49.9 (Set limit order)
Buy Price = Fair Value (64.79) x (1 - 27.5%) = 46.9728
Live price 67.07 vs buy price ceiling 46.9728 -> limit order at buy price (live price above ceiling); entry price used = 46.9728
Primary Sell Target = Fair Value = 64.7900
Bull-Case Trim Target = Bull FV (88.61) x 0.90 = 79.7490
Stop Loss = Entry Price (46.9728) x (1 - 27.5%) = 34.0552
R/R Ratio = (Sell Target 64.7900 - Entry 46.9728) / (Entry 46.9728 - Stop 34.0552) = 17.8173/12.9175 = 1.3793:1
*** FLAG: R/R 1.3793:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = Portfolio Value (61622.32) x 1.5% = 924.3348
Risk Per Share = Entry (46.9728) - Stop (34.0552) = 12.9175
Shares by risk-based sizing = 924.3348 / 12.9175 = 71.5568
Allocation cap = Portfolio Value (61622.32) x 4% = 2464.8928 -> 52.4750 shares
Position Size (shares) = min(risk-based, cap) = 52.4750  [binding: allocation cap]
Position Size ($) = 52.4750 x 46.9728 = 2464.8928
Current shares held = 12; gap vs. target = 40.4750
```

### Order Setup Checklist
```
[✗] Risk/Reward Ratio:      1.38:1  (must be >= 2:1)
[ ] BUY PRICE (ceiling):     46.97
[ ] Entry Price used:        46.97  (limit order at buy price (live price above ceiling))
[ ] PRIMARY SELL TARGET:     64.79
[ ] BULL-CASE TRIM TARGET:   79.75
[ ] STOP LOSS:               34.06
[ ] Max $ Risk:               924.33
[ ] POSITION SIZE (shares):  52.4750  (binding: allocation cap)
[ ] POSITION SIZE ($):       2464.89
[ ] Current shares held:     12
```

**Reading:** a disciplined buy price is **$46.97** — the live price ($67.07) is 42.8% above it. R/R at that entry is **1.38:1, below the 2:1 minimum** (the same 1.38:1 as 07-05 and 07-17). The script's "52.5 shares / $2,465" is the 4% allocation cap at the hypothetical entry price, **not a recommendation** — it only shows the distance to the 3-5% band (current 1.31%). No order is set.

## 9. Action recommendation (position-aware)

Checks:
1. **Quality gate:** 69.9 < 80.0 (fails under every basis tried: 66.9-69.9). No add for a name under the gate.
2. **Order-setup math:** no executable entry; R/R 1.38:1 < 2:1; price 42.8% above the most aggressive buy price.
3. **Valuation:** 55.2 = Hold band; not in the 70.0+ Trim band (14.8 pts away) and far from the 90.0+ Full Exit band.
4. **Full Exit triggers (checked, not assumed):**

| Trigger | Evidence | Met? |
|---|---|---|
| Fundamental deterioration (margins broken, ROIC below cost of capital) | Q2 operating margin 33.4% (-0.7pp YoY); FY2026 margin guide 31.5% vs FY2025 29.5%; ROIC 35% vs WACC ~10% | No |
| Growth thesis broken (TAM shrinking, pricing power lost, or guidance cut 2+ consecutive quarters) | FY2026 revenue-guide midpoint unchanged (~$51.2B); Q3 guide $12.86B (+11.7%) | No — but this is **the** watch item for 20 Oct |
| Balance-sheet crisis | Net debt/EBITDA 0.35×; no dilutive raise | No |
| Extreme overvaluation (90.0+ for 2 quarters) | 55.2 | No |

**Net action: HOLD the existing 12 shares (1.31%) — no add, no trim, no exit. Phase 04 Quality Watch continues.**

**Position-sizing note (3-5% target band, 15% cap).** The position sits *below* the 3-5% standard band, but that band is the target for a **gate-passing** entry, not a mandate to average down into a name that fails the Quality gate. Reaching 3-5% would require both Quality ≥ 80.0 and an executable setup (buy price near $47 or R/R ≥ 2:1); neither holds. The 15% cap is nowhere near binding. The unrealized loss (-23.6% vs the $87.79 cost) is **not** a framework trigger (no acting on price alone).

**What would change the call (Q3 print 20 Oct, mandatory re-score 21 Oct):**
(a) Q3 revenue growth at/above the 11.7% guide with the FY2026 guide held -> deceleration stabilizing, Quality Watch eases;
(b) growth clearly below 11.7% or a **cut to the FY2026 revenue midpoint** -> the Phase 04 "Growth thesis broken" Full Exit test becomes live;
(c) Q3 operating margin vs the 33.2% guide;
(d) buyback pace vs the $27.1B authorization (feeds shareholder yield);
(e) size of the WBD-fee-related cash tax in Q3 FCF;
(f) any engagement/share disclosure addressing the YouTube share-loss claim.

Earlier re-score triggers: >15% move from $67.07 (outside $57.01-$77.13), a guidance change, or an M&A/management event; 10Y falling back under 5% (rate modifier reverts to +10).

All final-decision authority rests with the human investor per the operating brief.

## 10. Open items / issues
- yfinance worked this session (the 07-17 TLS failure did not recur).
- Direct `data.sec.gov` calls from the local shell timed out; the Q2 10-Q was cross-checked via a fetched copy and the yfinance quarterly statements, which agree with the 8-K.
- A summarised FRED text-page fetch returned an inconsistent series; the raw CSV (5.24%) was used.
- The 07-17 composite (39.8) was hand-computed; the Composite script now **refuses** below-gate names, so the 42.7 here is likewise a labeled hand-computed reference.
- Unknown (not invented): Q3 buyback pace, WBD-fee cash-tax size, a precise viewing-share series.
- No trade executed; no `decisions/` entry required. `portfolio/holdings.md` was **not** edited (suggested cells: Score 55.2 / Quality 69.9 / Composite 42.7 / date 3 Oct 2026).

## 11. Watchlist update

[watchlist/in-portfolio/NFLX/NFLX-2026-10-03.md](../watchlist/in-portfolio/NFLX/NFLX-2026-10-03.md). `scripts.watchlist_diff --old-score 49.3 --old-category HOLD --new-score 55.2 --new-category HOLD` returned `new_file` ("score changed (49.3 -> 55.2)"). `scripts.stale_score --apply` result: `{"version": "2026-06-29", "newly_stale": [], "resolved": []}` (NFLX carried no stale mark; nothing to clear).

## 12. Glossary

- **8-K / 10-Q:** SEC filings — a "current report" for a material event (here the earnings letter) and the quarterly financial report.
- **Beta / ERP (Equity Risk Premium):** how much a stock swings vs the market, and the extra return investors demand for owning stocks; both feed the DCF discount rate (WACC).
- **Buyback yield / Shareholder yield:** the rate the share count shrinks from repurchases (net of issuance), plus dividends, as a % of market cap.
- **Composite Score:** this framework's blend `0.50 × (100 − Quality) + 0.50 × Valuation`; lower is more attractive; not computed (reference only) when Quality fails the gate.
- **DCF / WACC / Terminal value:** valuing a company by discounting projected cash flows; the discount rate; and the lump-sum value of all cash flows beyond the forecast years.
- **EV/EBIT / EBIT / EBITDA:** enterprise value divided by operating profit; operating profit before interest and taxes (EBITDA also before depreciation and amortization).
- **EY (Earnings Yield) / Earnings Yield Spread Test:** 1 ÷ forward PE, and its comparison to the 10Y Treasury yield in the Rate Environment Gate (a spread below +1.5pp adds +5).
- **False green light (Composite Score):** a Composite that looks "Cheap" only because a sub-80 Quality Score is inverted in the formula; never acted on.
- **FCF / FCF Yield / FCF-NI conversion:** free cash flow; FCF ÷ market cap; FCF ÷ net income.
- **Forward PE:** price ÷ next-period expected earnings per share.
- **FRED:** the St. Louis Fed's free economic-data database (source of the 10Y yield).
- **Hard disqualifier:** a Quality Score condition that fails a company regardless of the weighted score; none fired here.
- **Hurdle rate:** the minimum acceptable annual return (10% here) the Upside/Downside Modifier measures against.
- **Moat:** a durable competitive advantage protecting a company's profits.
- **MoS (Margin of Safety):** how far below fair value the buy price is set.
- **Net Debt/EBITDA:** a leverage ratio (debt minus cash, over operating earnings).
- **NOPAT / ROIC:** operating profit after tax; NOPAT ÷ invested capital — how efficiently capital earns profit.
- **PW (Probability-Weighted) Fair Value:** 25% bull + 50% base + 25% bear blended fair value (Rule 7).
- **Quality Score / Quality Watch / Quality gate:** this framework's 0-100 business-quality score (80.0+ required to enter); the monitoring flag for a held name below the gate; the 80.0 threshold itself.
- **Rate Environment Gate / Rate Regime Modifier:** the mandatory pre-check comparing earnings yield with the 10Y Treasury yield and the resulting additive score adjustment (+15 total here).
- **R/R (Risk/Reward):** expected gain ÷ expected loss on a trade; 2:1 minimum.
- **Rule 0 / Rule 6 / Rule 9:** always fetch a live price; normalize one-off distortions (here the $2.8B WBD fee); fundamental events force a re-valuation.
- **Treasury yield (10Y):** the US government's 10-year borrowing rate, the risk-free benchmark.
- **TTM (Trailing Twelve Months):** the latest four reported quarters combined.
- **Upside/Downside Modifier:** the ±15 score adjustment from expected annual return vs the 10% hurdle.
- **Valuation Score:** the 0-100 Phase 02 score (lower = cheaper); 50.0-69.9 = "Hold / Fair Value".
- **YoY:** year over year.

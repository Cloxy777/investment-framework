# NEW POSITION - APP (AppLovin Corporation, Class A) - 2026-10-03

**Task type:** NEW POSITION (re-evaluation; prior full session [2026-09-21](2026-09-21-new-position-app.md): Quality 96.7 / Valuation 54.9 / Composite 29.1, WATCHLIST ONLY because R/R 1.00:1 failed 2:1)
**Date:** 3 Oct 2026
**Current APP portfolio weight:** 0% (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Technology - Mobile AdTech (AXON engine)
**Scoring methodology in force:** version 2026-06-29 ([quality-scoring.md](../framework/quality-scoring.md), [valuation-scoring.md](../framework/valuation-scoring.md))

## 1. Live price (Rule 0)

IBKR `get_price_snapshot`, contract_id 481863646 (NASDAQ: APP, same contract as 09-21): **last $268.09** (ts 1790985592, `is_close: false`, `top_status` FROZEN, i.e. market closed; this is the last regular-session print of Fri 2 Oct 2026). Prior close $281.31, change -4.7% (-$13.22). 52-week range $266.84 - $738.01 (IBKR `misc_statistics`; the 52-week low was set within the last 13 weeks, price is within 0.5% of it). Cross-check: Yahoo `currentPrice` $268.22.

Versus **$328.88 on 2026-09-21: -18.5%** (268.09 / 328.88 - 1). Beta 2.488 (Yahoo).

## 2. Rule 9 trigger check since 2026-09-21

| Category | Fired? | Detail |
|---|---|---|
| Earnings | No | Q3 FY2026 not yet reported; Yahoo calendar shows **2026-11-04**. Latest reported quarter is still Q2 FY2026 (period ended 2026-06-30, reported 2026-08-05). Quarterly financials re-fetched today are identical to the 09-21 TTM inputs. |
| Guidance revision | No | None found since 09-21. Consensus has not moved: FY2026 EPS $15.66, FY2027 EPS $20.00, forward EPS $20.98 (all identical to 09-21); FY2027 revenue $10,249.8M (vs $10,263.9M, -0.1%). |
| Management change / M&A | None found | |
| **Regulatory / legal** | **Partly** | (a) The SEC data-collection probe was first reported 2025-10-06 (Bloomberg/CNBC), so it is not new; no company-specific enforcement action or short-seller report dated after 09-21 was found (this was the 09-21 follow-up item). (b) Securities class action (class period 2026-02-12 to 2026-08-05; lead-plaintiff deadline **2026-11-16**; alleges delays in the generative-AI video creative feature and overstated AI-model improvement): law-firm reminders ran 09-28 to 10-02; the filing itself is not new but is a live overhang. (c) **New:** AppLovin v. Unity Technologies (ad-quality data collection in MAX auctions): AppLovin's TRO request was **denied** by San Francisco Superior Court on Thu 2026-10-01 (sealing-motion hearing 2026-10-23). |
| Analyst actions (context only) | Yes, not an action trigger | Wells Fargo (Equal-Weight, target $325) on 2026-10-01 called the merchant Pixel install spike a "false start" (about 85% of newly added sites showed no measurable traffic; mostly low-traffic APAC Shopify storefronts). The BofA (Neutral, target $400) and Wells Fargo downgrades date to 2026-08-11 / 08-19, i.e. already in the 09-21 base. Yahoo's feed shows 09-01 / 09-14 target cuts (e.g. Morgan Stanley $650 to $450). |
| Macro / rates | **Yes** | FRED `DGS10`: 4.96% on 2026-09-21 -> **5.24% on 2026-10-01** (latest observation; peak 5.29% on 09-30). The 10Y crossed the framework's 5% line: Rate Regime bracket moves from 3.5-5% (+5) to >5% (+10). |
| >15% price move | **Yes, explained** | -18.5% since 09-21: Unity TRO denial, Wells Fargo e-commerce note, rising 10Y (multiple-compression headwind for a 2.49-beta stock), and the continuing de-rating after the Q2 revenue miss. Not "unexplained". |

Sources: [24/7 Wall St, 2026-10-01](https://247wallst.com/investing/2026/10/01/applovin-falls-3-as-wells-fargo-calls-pixel-install-spike-a-false-start-trade-desk-sits-out-the-selloff-magnite-dips/), [PPC Land - AppLovin v. Unity](https://ppc.land/applovin-sues-unity-to-halt-ad-quality-data-collection-within-5-business-days/), [The Crypto Basic - TRO denied](https://thecryptobasic.com/2026/10/02/applovin-stock-falls-below-52-week-low-tro-bid-against-unity-denied/), [Kessler Topaz via Morningstar - class action](https://www.morningstar.com/news/business-wire/20261001788046/applovin-corporation-app-investors-november-16-2026-deadline-in-securities-fraud-class-action-lawsuit-contact-kessler-topaz-meltzer-check-llp), [CNBC 2025-10-06 - SEC probe original report](https://www.cnbc.com/2025/10/06/applovin-stock-tanks-on-report-sec-is-investigating-company-over-data-collection-practices.html), [Alpha Spread - BofA downgrade](https://www.alphaspread.com/market-news/analyst-ratings/applovin-shares-fall-after-bank-of-america-downgrades-stock-to-neutral). These are secondary-source reports; the court docket and SEC filings were not read directly, and Benzinga pages returned HTTP 403.

**Conclusion:** no new fundamentals (no earnings, no filing), but a Rule 9 macro trigger (10Y regime change) and an explained >15% price move fired, so a full re-evaluation is warranted. Financial inputs come from the same Q2 FY2026 statements, freshly re-fetched; price, forward multiples, Rate Gate and fair values are recomputed.

## 3. Fundamentals (fresh Yahoo/yfinance pull) - `scripts.fetch_fundamentals APP`, verbatim

## Fundamentals — APP

```
Market Cap            = 89,759,965,184
Enterprise Value      = 90,221,854,720
Shares Outstanding    = 304,443,000
Forward PE            = 12.784
FCF Yield %           = 5.013
EV/EBIT               = 16.658
Net Margin %          = 64.576
Gross Margin %        = 88.464
ROIC % (NOPAT/InvCap) = 81.157  [tax_rate=0.1538, NOPAT=4,583,459,867, InvestedCapital=5,647,658,000]
Revenue 3yr CAGR %    = 24.838
Net Debt/EBITDA       = 0.189  [EBITDA_ttm=5,414,905,856]
FCF/NI TTM %          = 102.025
FCF/NI annual (oldest first) = [-213.8%, 279.3%, 131.2%, 118.3%]
FCF positive 3yr+     = True
5yr PE history        = NO-HISTORY FALLBACK (n=16 usable quarters) — only 16 quarters of reconstructable TTM-EPS PE history available, need 20 (5yr) — no-history fallback per valuation-scoring.md, never averaging over an undisclosed shorter window
```

**Reconciliation / script flag.** The script's ROIC (81.16%, invested capital $5,647.7M) and Net Debt/EBITDA (0.189x) read the **FY2025 annual** balance sheet (its latest column is 2025-12-31: net debt $1,025.9M, invested capital $5,647.7M), not the latest quarter, so they are stale versus 2026-06-30 (net debt $461.77M). I checked the raw yfinance quarterly balance sheet today and used the **quarter-end 2026-06-30** values, identical to the 09-21 session:

| Input | Value used | Basis |
|---|---|---|
| TTM revenue / net income / net margin | $6,829.12M / $4,409.85M / 64.57% | Q3 FY25 + Q4 FY25 + Q1 FY26 + Q2 FY26 (re-fetched, unchanged vs 09-21) |
| Gross margin | 88.46% | script and manual agree |
| TTM EBIT / D&A / EBITDA | $5,416.27M / $134.07M / $5,550.33M | quarterly sums (the yfinance EBITDA row also sums to about $5,550M) |
| Net debt (2026-06-30) | $461.77M (debt $3,515.07M - cash $3,053.31M) | quarterly balance sheet |
| Net Debt/EBITDA | 0.083x | 461.77 / 5,550.33 |
| ROIC | 126.44% | NOPAT $4,583.24M (EBIT x (1 - 15.38%)) / invested capital $3,624.78M (debt + equity $3,163.02M - cash). The script's 81.16% also exceeds the 30% score ceiling, so the score is unaffected either way. |
| TTM FCF / FCF-to-NI | $4,499.27M / 102.0% | script FCF/NI 102.025% agrees |
| Revenue 3yr CAGR | 24.84% | script 24.838% agrees |
| Shares (all classes, 2026-06-30) | 335,291,521 | quarterly balance sheet (Yahoo `sharesOutstanding` 304.4M is Class A only; implied total 334.65M) |
| Diluted shares (Q2 FY26) | 337.031M | quarterly financials |
| Market cap at the live price | 335.2915M x $268.09 = **$89,888M** | (the script's $89,760M comes from a Yahoo field, not the IBKR price of record) |
| EV | 89,888 + 3,515 - 3,053 = **$90,350M** | |

The 09-21 caveats still apply: the 3yr revenue CAGR is distorted by the 2025 mobile-apps divestiture, and no clean 5yr PE history exists (script: only 16 usable quarters, 20 needed, so the no-history fallback applies).

## 4. Quality Score (Phase 01)

Hard disqualifiers: FCF/NI <70% for 2+ years - no (TTM 102.0%; FY23 279.3%, FY24 131.3%, FY25 118.3%); Net Debt/EBITDA >2.5x - no (0.083x); not FCF-positive 3+ years - no. None fires.

Inputs are the 09-21 inputs (same financials; no new evidence overturns a Moat signal). Two judgment checks on the qualitative inputs:
- **TAM modifier (+10):** Wells Fargo's 10-01 "false start" note challenges the *pace* of e-commerce Pixel adoption, not the documented platform rollout or the Jefferies share-gain survey. Kept; sensitivity shown below.
- **Structural-deceleration modifier (-10):** consensus still has FY2026 revenue +47.8% and FY2027 +26.6%; BofA's cut of its own 2027 growth estimate to 23% is a single analyst's forecast (dated 08-11). That is not documented structural deceleration, so it is not applied; sensitivity shown below.

`scripts.scoring.quality_score` output, verbatim:

## Quality Score

**Profitability (25%)**
```
NetMargin_Component = clamp((64.57/30)x100) = 100.00
ROIC_Component = clamp((126.44/30)x100) = 100.00
Profitability_Score = (100.00 + 100.00) / 2 = 100.00
```
**Margins (15%)**
```
GrossMargin_Score = clamp((88.46/80)x100) = 100.00
+10 structural-trend bonus -> clamp(100.00+10, 0, 100) = 100.00
```
**Growth (20%)**
```
Growth_Score = clamp((24.84/25)x100) = 99.36
+10 TAM/pricing-power evidence: Self-serve AXON/AppLovin Ads platform rolling out to all advertisers in 2026 targeting e-commerce; Jefferies advertiser survey: APP share of e-commerce ad budgets +169 bps to 11% (see 2026-09-21 session sources). Wells Fargo 2026-10-01 calls the Pixel install spike a false start (traffic-weighted adoption not yet inflecting) - weakens, does not remove, the evidence; sensitivity shown.
Growth_Score (final, clamped) = 100.00
```
**Balance Sheet (15%)**
```
BalanceSheet_Score = clamp(100x(1 - 0.083/4)) = 97.92
```
**Moat Signal (15%)**
```
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Tenjin Ad Monetization Benchmark 2026: iOS ad-revenue share 39%->44% Q1->Q2 2026; MAX 80%+ mediation share |
| brand_premium | False | No price-increase-without-volume-loss evidence; advertisers are ROAS-driven |
| network_effect | True | AXON data flywheel, 2M+ auctions/sec across 1B+ devices |
| switching_costs | True | MAX SDK integration; switching cost est. 5-20% of revenue; 536 patents |
| scale_cost_advantage | True | 88.5% gross margin vs Unity ~74% |
Moat_Score = (4/5) x 100 = 80.00
```
**FCF Quality (10%)**
```
FCFQuality_Score = clamp(((1.0203 - 0.40)/0.60)x100) = 100.00
```
**Quality Score — Final**
```
Quality Score = (100.00x0.25) + (100.00x0.15) + (100.00x0.20) + (97.92x0.15) + (80.00x0.15) + (100.00x0.10)
= 96.689 -> rounds to 96.7
```

# Quality Score = 96.7 — PASSES the 80.0+ gate

**Sensitivity (by hand):** without the TAM modifier Growth = 99.36 and Quality = 96.69 - 0.20 x 0.64 = 96.56 (about 96.6). With a -10 deceleration modifier instead of +10: Growth = 89.36 and Quality = 96.69 - 0.20 x 10.64 = 94.56 (about 94.6). The 80.0+ gate holds in every case. The 09-21 Profitability sensitivity flag (thin invested-capital denominator) is unchanged.

**Quality Score: 96.7 - CLEARS the 80.0+ gate.**

## 5. Valuation Score (Phase 02)

### 5a. Fair value rebuilt at the new price and rate (Rules 1, 2, 3, 7)

Method identical to 09-21 (I reproduced the 09-21 DCF exactly at WACC 17.0%: base $167.07, bull $224.46, bear $102.35). Only inputs that legitimately moved are changed:

- Risk-free 4.94% -> **5.24%**; cost of equity = 5.24 + 2.488 x 5 = 17.68%; with debt about 3.7% of capital at about 4.3% after tax, **WACC base = 17.2%** (bull 16.2%, bear 18.2%). Same construction as 09-21 (17.38% cost of equity gave 17.0%). WACC and the multiples below are modeling judgments, not sourced facts.
- Growth fades, terminal growth (3.0 / 2.75 / 2.0%) and starting FCF $4,499.27M unchanged. Net debt $461.77M, 337.031M diluted shares.
- Multiples unchanged from 09-21 (Forward PE 28x/20x/14x on $20.98; EV/Revenue 16x/12x/8x on FY2027 consensus revenue, now $10,249.8M). I deliberately did **not** lower the multiples to match the market's de-rating; that would be circular (using the price to justify the value).

```
DCF (WACC 16.2 / 17.2 / 18.2):  Bull $220.55   Base $164.49   Bear $101.06
Fwd-PE basis (EPS $20.98):      Bull 28x $587.46   Base 20x $419.62   Bear 14x $293.73
EV/Rev basis (FY27 rev $10,249.8M):
  Bull 16x: (163,996.5 - 461.77) / 337.031 = $485.22
  Base 12x: (122,997.4 - 461.77) / 337.031 = $363.57
  Bear  8x: ( 81,998.2 - 461.77) / 337.031 = $241.91
Multiples-based (average of the two): Bull $536.34   Base $391.60   Bear $267.82
Blended (40% DCF / 60% multiples):
  Bull = 0.40 x 220.55 + 0.60 x 536.34 = $410.02
  Base = 0.40 x 164.49 + 0.60 x 391.60 = $300.76
  Bear = 0.40 x 101.06 + 0.60 x 267.82 = $201.11
PW Fair Value = 0.25 x 410.02 + 0.50 x 300.76 + 0.25 x 201.11 = $303.16   (09-21: $304.35)
```

PW Fair Value is essentially unchanged (-0.4%: the higher WACC offsets only slightly lower revenue consensus), but the price fell 18.5%, so the live price is now **11.6% below** PW Fair Value (09-21: 7.5% above). Sanity check (Rule 0 Step 4): the Street mean target is $497.05 (median $475.00, range $325-$790, 31 analysts, mean recommendation 1.58); the framework's bottom-up value remains well below the Street, as on 09-21.

### 5b. Inputs to the score

| Input | Value | Calculation / note |
|---|---|---|
| FCF yield | 5.006% | $4,499.27M / $89,888M |
| EV/EBIT | 16.68x | $90,350M / $5,416.27M |
| Forward PE | 12.78x | $268.09 / $20.981 (Yahoo NTM forward EPS, unchanged) |
| PEG | Not applicable | 15% weight redistributed to EV/EBIT (unreliable earnings base: FY2022 loss + 2025 divestiture; same ruling as 09-21) |
| FwdPE_Score | 50.0 neutral, flagged | No-history fallback. At a 12.8x forward PE this neutral value is probably conservative (likely overstates the score); not adjusted because the fallback rule is the rule. |
| 10Y | 5.24% | FRED DGS10, 2026-10-01 |
| Catalyst within 18-24 months | **No** (conservative) | The only scheduled event is Q3 earnings on 2026-11-04, a checkpoint rather than a documented re-rating catalyst; Wells Fargo puts the e-commerce turn "next year"; the Unity/class-action items are overhangs. Guardrail 1 therefore caps the upside modifier at -5 (the 09-21 session did not hit the cap because its modifier was only -3.51). |
| Intrinsic growth | 15.44% | mean of base-case yr1-5 FCF growth (unchanged) |
| Net buyback yield / dividend | 1.8% / 0% | share count 338.3M (FY25) -> 335.3M (Q2 FY26); assumption unchanged from 09-21 |

### 5c. `scripts.scoring.valuation_score` output, verbatim

## Valuation Score

**FCF Yield (40%)**
```
FCF_Score = clamp(100x(1 - 5.006/10)) = 49.940
```
**EV/EBIT**
```
EV/EBIT_Score = clamp((16.68 - 12)/23 x 100) = 20.348
```
**Forward PE**
```
No 5yr PE history available (no-history fallback) -> FwdPE_Score = 50.0 (neutral, flagged)
```
**PEG**
```
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT
```
**Rate Environment Gate**
```
EY = 1/12.778 x 100 = 7.8260%
Spread = EY - 10Y (5.24%) = 2.5860pp -> Step 1 = +0 (pass, >=1.5pp)
10Y = 5.24% -> Step 2 bracket modifier = +10
Total Rate Modifier = 0 + 10 = +10
```
**Upside/Downside Modifier**
```
PW Fair Value = 0.25x410.02 + 0.50x300.76 + 0.25x201.11 = 303.1625
Gap Upside % = (303.1625/268.09) - 1 = 13.0824%
Annualized gap = 13.0824% / 2.0yr = 6.5412%/yr
E = 6.5412 (annualized gap) + 15.44 (intrinsic growth) + 1.8000 (shareholder yield: 0.0 div + 1.8 buyback) = 23.7812%/yr
E (23.7812%) >= H (10.0%) -> M = -15 x clamp((23.7812-10.0)/15, 0, 1) = -13.7812
Guardrail 1: no catalyst identifiable within 18-24 months -> upside side capped at -5 (was -13.7812)
Upside/Downside Modifier (bounded [-15, +15]) = -5.0000
```
**Raw Weighted Score**
```
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 38.115
```
**Final Valuation Score**
```
Final Score = Raw (38.115) + Rate Modifier (+10) + Upside/Downside Modifier (-5.000)
= 43.115 -> rounds to 43.1
```

# Valuation Score = 43.1

**Sensitivity - catalyst guardrail:** if a catalyst were credited (cap not applied), the modifier is -13.78 and Valuation = 38.115 + 10 - 13.781 = **34.3**, Composite = **18.8**. Either way Valuation moves from the 50.0-69.9 band to 30.0-49.9 and Composite stays in the 0.0-29.9 band. The scored (conservative) figure is **43.1**.

### Score bridge vs 09-21 (54.9 -> 43.1)

| Component | 09-21 | 10-03 |
|---|---|---|
| FCF_Score | 59.2 | 49.9 |
| EV/EBIT_Score | 36.7 | 20.3 |
| FwdPE_Score | 50.0 | 50.0 |
| Raw weighted | 48.36 | 38.12 |
| Rate modifier | +10 (EY spread 1.44pp: +5; bracket 3.5-5%: +5) | +10 (EY spread 2.59pp: +0; 10Y >5%: +10) |
| Upside/Downside modifier | -3.51 | -5.00 (capped) |
| **Final** | **54.9** | **43.1** |

The whole improvement comes from the lower price (higher FCF yield, lower EV/EBIT). The Rate Gate total is unchanged at +10: the earnings-yield spread now passes because the price fell, but the 10Y crossing 5% offsets it.

## 6. Composite Score

`scripts.scoring.composite_score --set quality_score=96.7 --set valuation_score=43.1`, verbatim:

## Composite Score

```
Composite Score = 0.50x(100 - 96.7) + 0.50x43.1 = 23.200 -> rounds to 23.2
```

# Composite Score = 23.2
(Quality Score 96.7, Valuation Score 43.1)

**Composite 23.2** (09-21: 29.1), still in the 0.0-29.9 "BUY, Full position 6-8%" band. The 09-21 sensitivity flag stands: with Quality 96.7 the quality half contributes only 1.65 points, so the band is driven by the valuation half.

## 7. Fair value and order setup

`scripts.scoring.order_setup` (band 0.0-29.9; conservative ends of the ranges as on 09-21: MoS 20%, max loss 25%; risk 1.5% and cap 6% for sizing; portfolio $61,622.32 per [holdings.md](../portfolio/holdings.md) as of 2026-09-27), verbatim:

## Order Setup

```
Band: 0.0-29.9 (Enter now)
Buy Price = Fair Value (303.16) x (1 - 20%) = 242.5280
Live price 268.09 vs buy price ceiling 242.5280 -> limit order at buy price (live price above ceiling); entry price used = 242.5280
Primary Sell Target = Fair Value = 303.1600
Bull-Case Trim Target = Bull FV (410.02) x 0.90 = 369.0180
Stop Loss = Entry Price (242.5280) x (1 - 25%) = 181.8960
R/R Ratio = (Sell Target 303.1600 - Entry 242.5280) / (Entry 242.5280 - Stop 181.8960) = 60.6320/60.6320 = 1.0000:1
*** FLAG: R/R 1.0000:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = Portfolio Value (61622.32) x 1.5% = 924.3348
Risk Per Share = Entry (242.5280) - Stop (181.8960) = 60.6320
Shares by risk-based sizing = 924.3348 / 60.6320 = 15.2450
Allocation cap = Portfolio Value (61622.32) x 6% = 3697.3392 -> 15.2450 shares
Position Size (shares) = min(risk-based, cap) = 15.2450  [binding: risk-based sizing]
Position Size ($) = 15.2450 x 242.5280 = 3697.3392
Current shares held = 0; gap vs. target = 15.2450
```

### Order Setup Checklist
```
[✗] Risk/Reward Ratio:      1.00:1  (must be >= 2:1)
[ ] BUY PRICE (ceiling):     242.53
[ ] Entry Price used:        242.53  (limit order at buy price (live price above ceiling))
[ ] PRIMARY SELL TARGET:     303.16
[ ] BULL-CASE TRIM TARGET:   369.02
[ ] STOP LOSS:               181.90
[ ] Max $ Risk:               924.33
[ ] POSITION SIZE (shares):  15.2450  (binding: risk-based sizing)
[ ] POSITION SIZE ($):       3697.34
[ ] Current shares held:     0
```

- **R/R = 1.00:1 on the primary basis - FAILS the 2:1 minimum.** The geometry is unchanged from 09-21: for any MoS in 15-20% and max loss in 20-25% (the 0.0-29.9 band's ranges), R/R = MoS / ((1 - MoS) x MaxLoss) peaks at 1.25:1, so it cannot reach 2:1 when Buy Price and Sell Target both derive from the same fair value. Per fair-value-methodology.md Step 6: wait for a lower entry, find a tighter stop, or pass.
- On the Bull-Case Trim basis R/R = (369.02 - 242.53) / 60.63 = 2.09:1 (optimistic case only, not the framework's test).
- **Where the price sits:** live $268.09 is 10.5% above the $242.53 buy-price ceiling (a limit order there would need a further 9.5% fall to fill) and 11.6% below PW fair value. The earlier "price above fair value" objection has gone, but the R/R rule still blocks an order.
- **Funding flag:** IBKR USD cash was $103.51 at the 2026-09-27 sync ([holdings.md](../portfolio/holdings.md)); the $3,697 sizing would need cash that is not currently there. Not a framework gate, but practical.

## 8. Recommendation: **WATCHLIST ONLY - no order, no position**

The stock moved from above fair value to meaningfully below it, and the Valuation Score improved from 54.9 to 43.1 (Composite 29.1 -> 23.2). The framework's own R/R test (1.00:1 vs 2:1) still says not to place the mechanical limit order, so the Step 6 reading is unchanged from 09-21. Reasons, in order of weight:

1. **R/R fails (structural).** Not APP-specific; same precedent as MCO 2026-09-11 and APP 09-21.
2. **Live legal/regulatory overhangs are unresolved:** the SEC data-practices probe (reported 2025-10), the securities class action (lead-plaintiff deadline 2026-11-16), and the Unity dispute (TRO denied). None is a scored Quality input today, but they raise the odds of an unscored Rule 9 event.
3. **Estimates have not been cut yet.** Consensus EPS ($15.66 FY26 / $20.00 FY27) is unchanged while Street sentiment soured (BofA, Wells Fargo, Morgan Stanley target cuts). If Q3 (2026-11-04) shows the sequential-growth shortfall BofA fears, the forward EPS used here (and thus forward PE, fair value and EY spread) would fall. This is the main reason the improved score is not yet decisive.
4. **Rates:** 10Y at 5.24% (+10 modifier already applied); a further rise would pressure a 2.49-beta stock.

**What would change the call:** (a) a price near or below about $243 (the 20%-MoS buy ceiling) combined with an evidence-based tighter stop for an exceptional-quality name - an exception to the framework ranges that would have to be documented explicitly in `decisions/` per Rule 10, not applied here; (b) Q3 FY2026 results confirming that growth and consensus hold; (c) clarity on the SEC / class-action / Unity items. A price move alone is not a trigger (Rule 9).

No order placed; no position opened; nothing to log in `decisions/`.

## 9. Next review trigger

- **Q3 FY2026 earnings, 2026-11-04** - mandatory Rule 9 re-score.
- **Unity sealing-motion hearing 2026-10-23 and class-action lead-plaintiff deadline 2026-11-16** - check for company-specific developments.
- **10Y back below 5%**, or a further price move >15% from $268.09 in either direction.
- **Any company-specific SEC/FTC enforcement action or short-seller report** - immediate re-score.

## 10. Data gaps and flags

1. `scripts.fetch_fundamentals` reads the **annual** balance sheet for ROIC and Net Debt/EBITDA, stale by two quarters here (ROIC 81.16% vs 126.44%; leverage 0.189x vs 0.083x). Quality is unaffected (both clear their score ceilings), but the script should be fixed to use the latest quarter. Flagged, not changed this session.
2. `scripts.scoring.order_setup` raises `UnicodeEncodeError` on Windows consoles (cp1252) when printing its checklist; worked around with `PYTHONIOENCODING=utf-8`.
3. Market data is the frozen weekend IBKR snapshot (Fri 2 Oct close); Monday's open may differ.
4. News is from secondary sources (Benzinga blocked with HTTP 403); the court docket and SEC filings were not read directly.
5. WACC, fade rates, multiples and the catalyst call are modeling judgments, labeled as such. Nothing in the sourced financial data was invented or estimated.
6. 3yr revenue CAGR remains divestiture-distorted; no usable 5yr PE history (neutral fallback).

## 11. Watchlist

`scripts.watchlist_diff` (old 54.9 WATCHLIST -> new 43.1 WATCHLIST, `--fundamental-event`): decision `new_file` (Rule 9 trigger fired; valuation score also changed). New file [watchlist/not-in-portfolio/APP/APP-2026-10-03.md](../watchlist/not-in-portfolio/APP/APP-2026-10-03.md); the 09-21 file remains in git history. `scripts.stale_score --apply` result: `{"version": "2026-06-29", "newly_stale": [], "resolved": []}` (APP carried no stale mark; nothing to clear).

## Glossary

- **Quality Score**: This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. See [quality-scoring.md](quality-scoring.md).
- **Composite Score**: This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50 — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only for companies that have already cleared the 80.0+ Quality Score gate. Used against the Phase 03/05 action tables instead of the raw valuation score. See [valuation-scoring.md](valuation-scoring.md).
- **Rate Regime Modifier**: An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in.
- **Rate Environment Gate**: The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier.
- **PW (Probability-Weighted) Fair Value**: This framework's blended fair value estimate — 25% bull case + 50% base case + 25% bear case (Rule 7) — used as the single fair-value input to both the order setup and the Upside/Downside Modifier.
- **Upside/Downside Modifier (Expected-Return Modifier)**: An additive ±15 adjustment to the valuation score based on expected annual return (the gap to PW Fair Value, annualized over the catalyst window, plus intrinsic growth and shareholder yield) — folds the forward-looking dimension into the score so strong expected upside pulls a name toward "buy" and a thin/negative expected return pushes it toward "trim/sell."
- **TTM (Trailing Twelve Months)**: The most recent four reported quarters combined, used instead of a single fiscal-year snapshot to reflect a company's most current run-rate — the basis for the Net Margin and ROIC inputs to this framework's Quality Score (quality-scoring.md), e.g. Motorola Solutions' (MSI) TTM figures (period ending Q2 2026) in this framework's 2026-08-23 session. *(New term.)*
- **ROIC**: Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **NOPAT (Net Operating Profit After Tax)**: EBIT x (1 - effective tax rate): the operating profit a business keeps after paying tax, before any financing effects. It is the numerator of ROIC in this framework (NOPAT / Invested Capital).
- **Invested Capital**: The total capital (debt + equity, sometimes netted for cash) that has been put to work in a business — the denominator in a Return on Invested Capital (ROIC) calculation. This framework nets out cash (debt + equity − cash) when computing it, consistent with how Net Debt/EBITDA already nets cash from gross debt.
- **FCF**: Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **EV/EBIT, EV/EBITDA**: Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.
- **Forward PE**: Price ÷ next twelve months' *expected* earnings per share (vs. Trailing PE, which uses the last twelve months' actual earnings).
- **PEG ratio**: PE ratio ÷ earnings growth rate — a PE adjusted for growth, used to judge whether a fast grower's multiple is justified by its growth rate.
- **EY (Earnings Yield)**: 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury).
- **Earnings Yield Spread Test**: Step 1 of the Rate Environment Gate: Earnings Yield (1 ÷ Forward PE) minus the 10-Year Treasury yield. A spread below +1.5% fails the test and adds a +5 flag to the valuation score (raising the bar, not vetoing entry) — see [strategy.md](strategy.md).
- **Treasury yield (10Y)**: The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate.
- **Net Debt/EBITDA**: Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **CAGR**: Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **DCF**: Discounted Cash Flow — a valuation method that estimates a company's worth today by projecting its future cash and discounting it back to present-day value.
- **WACC**: Weighted Average Cost of Capital — the blended cost a company pays for its debt and equity financing; used as the discount rate in a DCF.
- **Terminal Value**: In a multi-stage DCF, the lump-sum value assigned to all cash flows beyond the explicit forecast period (e.g., after Year 10), estimated via a perpetuity-growth formula and then discounted back to today — often the single largest component of a DCF's total value, which is why Rule 4's sanity check flags a model where it exceeds 75% of total value.
- **Beta**: A stock's sensitivity to overall market moves — a beta of 1.0 means the stock tends to move in line with the market; above 1.0 means more volatile, below 1.0 means less. Used as an input (alongside the risk-free rate and Equity Risk Premium) to estimate a company's cost of equity in a DCF's WACC calculation.
- **TAM**: Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Moat Signal**: This framework's 5-point Quality Score checklist ([quality-scoring.md](quality-scoring.md)) that turns the general "Moat" concept (above) into a scored input: market share stable/growing, brand premium, network effect, switching costs, and scale cost advantage, each markable TRUE only against a cited source — `Moat_Score = (count of TRUE signals ÷ 5) × 100`.
- **Hard disqualifier**: One of three Quality Score conditions ([quality-scoring.md](quality-scoring.md)) that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation. A weighted average can't average away an outright balance-sheet or cash-flow-quality failure.
- **Catalyst window**: The timeframe (per Rule 10, typically 18–24 months) within which a documented, specific event is expected to close the gap between price and fair value — required before the Upside/Downside Modifier can credit large expected upside.
- **Shareholder yield**: Cash returned to shareholders as a percentage of share price — dividend yield plus net buyback yield combined.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set, as a cushion against being wrong — e.g. a 25% MoS means buying at 75% of estimated fair value.
- **R/R (Risk/Reward ratio)**: (Expected gain) ÷ (Expected loss) on a trade — this framework requires at least 2:1 before entering.
- **Rule 0**: This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9**: This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **Rule 1–8, Rule 10 (10-Rule Fair Value Framework)**: The numbered rules in [fair-value-methodology.md](../framework/fair-value-methodology.md) governing sector-appropriate valuation method choice (Rule 1), the 3-stage DCF standard (Rule 2), the weighted "football field" blend of valuation methods (Rule 3), sanity-check protocols including the 75% terminal-value cap (Rule 4), comparable-company standards (Rule 5), normalizing one-off items before valuing (Rule 6), mandatory bull/base/bear scenario weighting (Rule 7), margin-of-safety discipline by confidence level (Rule 8), and separating intrinsic value from market price with a documented catalyst (Rule 10). Rule 9 (model-refresh triggers) has its own standalone entry below. *(New term.)*
- **AXON / AXON 2.0**: AppLovin's proprietary AI/machine-learning advertising engine — processes real-time ad auctions (reported at 2M+/second) to predict and optimize which ad to show which user for the best expected return, continuously improving as more auction/outcome data flows through it (the mechanism behind this framework's Network Effect Moat Signal finding for APP: more auctions → better predictions → higher advertiser ROAS → more advertiser budget → more auctions). Cited in this framework's 2026-09-21 APP session. *(New term.)*
- **MAX (AppLovin)**: AppLovin's ad-mediation platform — software that mobile-app publishers embed (via SDK) to run an auction among competing ad networks for each ad impression and serve the highest-paying one, monetizing the app's ad inventory. Reported at 80%+ mediation-market share and the source of AppLovin's first-party auction/outcome data feeding the AXON engine — cited as Network Effect and Switching Costs Moat Signal evidence in this framework's 2026-09-21 APP session. *(New term.)*
- **SDK (Software Development Kit)**: A packaged set of code/tools a company provides for outside developers to embed inside their own app or website, integrating that company's service (analytics, ads, payments, etc.) directly into the host app. A mobile publisher embedding AppLovin's MAX SDK is the specific integration-depth mechanism behind this framework's Switching Costs Moat Signal finding for APP — removing an embedded SDK requires a new app build/release and risks a temporary monetization/data gap, not just a configuration change. Cited in this framework's 2026-09-21 APP session. *(New term.)*
- **ROAS (Return on Ad Spend)**: An advertiser's own performance-marketing metric — revenue attributed to an ad campaign ÷ the amount spent on it — the outcome metric AppLovin's AXON engine is built to optimize for on behalf of advertisers; cited in this framework's 2026-09-21 APP session as the mechanism advertisers reallocate budget toward rather than direct evidence of AppLovin pricing power (see Brand Premium Moat Signal finding, marked not demonstrated for that reason). *(New term.)*
- **Pixel (AppLovin Axon Ads Pixel)**: A small piece of tracking code an online merchant installs on its website so AppLovin's AXON engine can see which ad clicks lead to purchases and optimize ad delivery. Merchant Pixel installs are watched as an early indicator of AppLovin's e-commerce advertising expansion; install counts matter less than whether the sites actually carry traffic.
- **TRO (Temporary Restraining Order)**: A short-term court order issued quickly, often before a full hearing, that forces or stops a specific action (e.g. "stop collecting this data") while a lawsuit proceeds. Denial of a TRO does not decide the underlying case; it only means the judge did not find the emergency standard met at that stage. AppLovin's TRO request against Unity (Sep 2026) was denied.
- **Securities class action / shareholder-rights investigation**: A law firm's public solicitation of shareholders to join a potential lawsuit alleging a company issued false/misleading statements or omitted material information (distinct from a regulator-initiated probe like an SEC or DOJ investigation). An open, unresolved allegation — like a going-concern/accounting-integrity allegation — that should be tracked as a risk flag, never treated as a settled finding of wrongdoing until a court or regulator actually rules on it. Doximity (DOCS) faced multiple such investigations (Schall Law Firm, Pomerantz LLP, Halper Sadeh) opened in mid-2026 centered on whether management adequately disclosed AI-cost margin pressure ahead of its 13 May 2026 guidance miss.
- **Lead plaintiff (securities litigation)**: The court-appointed representative investor in a US securities class-action lawsuit, chosen (typically from among the investors with the largest financial loss who apply) to direct the litigation on behalf of the whole class. A "lead plaintiff deadline" (e.g. 2026-09-29 in Wise Group plc's open securities-fraud class action) is an early-stage procedural filing deadline for investors to seek that role — it is not a trial date, verdict, or resolution of the underlying case. *(New term.)*
- **Equal-Weight / Neutral (analyst rating)**: A Wall Street analyst rating in the middle of the scale, meaning the analyst expects the stock to perform roughly in line with its peers or the market; a move to it from Overweight/Buy is called a downgrade. It is context only for this framework, never an action trigger by itself.

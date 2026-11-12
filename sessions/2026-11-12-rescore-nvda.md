# RESCORE — NVDA (NVIDIA Corporation)

**Task type:** RESCORE (single ticker, mode `--both`) — user-invoked (`/rescore nvda`), off-cycle (no new filing)
**Date:** 2026-11-12
**10Y US Treasury Yield:** 4.88% (FRED DGS10, latest print 2026-11-09; 11-10..11-12 not yet posted. Prior: 4.84 on 11-05, 4.86 on 11-06)
**Rate Regime Modifier:** +5 (3.5–5% bracket)
**Last review on record:** Composite 20.6 (Quality 89.7 / Valuation 30.9), 2026-11-05 — [2026-11-05-rescore-nvda.md](2026-11-05-rescore-nvda.md)
**Current position (material change since last review):** **40 sh** (was 19; +21 bought, avg cost now $182.89 per the 2026-11-08 sync). 40 × $160.73 = **$6,429.20**; framework NLV re-marked ≈ $45,706 ($46,477.10 at the sync with NVDA at $180.00, less 40 × $19.27) → **≈14.1%**. Under the 15% hard cap (Upgrade 7), **~6pp over the 8% allocation cap**.

## 1. Live Price (Rule 0)

IBKR `get_price_snapshot` (contract 4815747): last **$160.73**, bid/ask $160.73 / $160.85. Today **−$13.00 / −7.48%** (prior close ≈ $173.73). **New 52-week low** (prior low $164.08; high $243.37). YTD −13.71%. vs 11-05 ($186.77): **−13.9%**; vs 09-17 ($218.70): −26.5%. Single-day and 7-day moves are each under the 15% Rule 9 line → **no price-based trigger**. Cause of today's drop is **not verified** (no news search run); per "never act on price alone", nothing is acted on.

## 2. Data gaps / sourcing notes

1. **yfinance worked this run** (first time since early Sept) — output in §3. Its market cap ($4,195B) implies a stale ≈$173.7 price, so market cap / EV / yields were **recomputed at live $160.73** on the 24,100M share count used previously (yfinance 24,147M is within 0.2%).
2. **No new financial filing.** SEC EDGAR submissions feed: newest periodic filings are the 10-Q and 8-K of 2026-08-26 and 8-K of 2026-09-03; since then only Forms 3/4/144. **All TTM statement inputs reused from 2026-11-05.** Cross-check: yfinance reproduces net margin 63.663%, gross margin 74.675%, FCF/NI 65.848%, (FCF−SBC)/NI 62.093%, EBITDA $201,266M, SBC $7,241M, annual FCF/NI 87.2/90.8/83.5/80.5% exactly.
3. **GAP — forward EPS $15.81 carried from 11-05 (finviz), not re-fetched.** Forward PE/PEG sub-scores are floored at 0.0 for any plausible forward EPS, so it cannot move them; it does feed the base fair value ($15.81 × 21 = $332.01).
4. **GAP — consensus price targets ($322.995 = mean of stockanalysis $327.14 / marketbeat $318.85) carried from 11-05, not re-fetched.** Feeds only blended FV (60% weight) → order setup.
5. **5-yr PE average:** yfinance now gives **55.205×** (range 32.486–122.129, n=20) vs 57.84× reused earlier — fresh figure used. Score unaffected (floors at 0.0).
6. **ROIC / net debt definitions:** yfinance prints ROIC 116.6% and Net Debt/EBITDA +0.002 (different invested-capital/debt definitions). Prior-session framework figures (ROIC 63.21%, ND/EBITDA −0.1154) were **kept** for continuity; both sets give 100.0 on those sub-scores.
7. **Earnings date unconfirmed** (finviz ≈ Nov 17 AMC). The print is imminent and will supersede this run.
8. **Portfolio value for sizing is an estimate** (re-marked NLV from the 11-08 sync, not a fresh account summary).

## 3. Inputs

yfinance output (verbatim, `python -m scripts.fetch_fundamentals NVDA`; market cap/EV/yield lines reflect a stale price — see §2.1):

```
Market Cap            = 4,195,058,188,288
Enterprise Value      = 4,163,283,976,192
Shares Outstanding    = 24,147,000,000
Forward PE            = 10.908
FCF Yield %           = 3.028
EV/EBIT               = 18.085
Net Margin %          = 63.663
Gross Margin %        = 74.675
ROIC % (NOPAT/InvCap) = 116.594  [tax_rate=0.1605, NOPAT=193,267,706,460, InvestedCapital=165,761,000,000]
Revenue 3yr CAGR %    = 100.045
Net Debt/EBITDA       = 0.002  [EBITDA_ttm=201,266,003,968]
FCF/NI TTM % (plain)  = 65.848
(FCF - SBC)/NI TTM %  = 62.093  [reported NI]
SBC yield %           = 0.173
Gross buyback yield % = 1.319
FCF/NI annual (oldest first) = [87.2%, 90.8%, 83.5%, 80.5%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 55.205 / 32.486 / 122.129  (n=20 quarters)

SBC block (TTM, advisory — no score effect)
  SBC 7,241,000,000.0   FCF 127,006,000,000.0   Market cap 4,195,058,188,288.0
  SBC/FCF = 5.7%
  FCF yield (reported)  = 3.03%
  FCF yield after SBC   = 2.85%
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
  (cycle_peak / value_trap need 8 consecutive quarters of Diluted EPS; if yfinance lacks them, run python -m scripts.scoring.flags_common with manually sourced EPS TTM figures.)
```

Recomputed at live price:

| Item | Value |
|---|---|
| Market cap | 24,100M × $160.73 = **$3,873,593M** |
| EV | $3,873,593M − $23,220M (net cash, reused) = **$3,850,373M** |
| EV/EBIT | $3,850,373M ÷ $197,579M = **19.488×** |
| FCF yield | $127,006M ÷ $3,873,593M = **3.2788%** |
| SBC yield | $7,241M ÷ $3,873,593M = **0.1869%** |
| Gross buyback yield | $55,315M ÷ $3,873,593M = **1.4280%** |
| Dividend yield | $1.00 ÷ $160.73 = 0.6222% |
| Forward PE | $160.73 ÷ $15.81 = **10.166×** |
| PEG | 10.166 ÷ 70.15 = **0.1449** |
| TTM revenue / EBIT / NI / FCF | $302,969M / $197,579M / $192,879M / $127,006M (reused) |
| 10Y | 4.88% |

Fast Grower: unchanged (EPS growth >15% for 3+ years on a clean base; no `--normalised-ni`).

## 4. Quality Score (scripted)

Hard disqualifiers: annual FCF/NI FY25 83.5% / FY26 80.5% ✅; net debt/EBITDA −0.115× ✅; FCF-positive ✅; SBC/FCF 5.7% ✅. TTM FCF/NI 65.8% plain (62.1% after SBC) remains the standing watch item (disqualifier tests completed fiscal years only). `gross_margin_structural_trend` = false, `scale_cost_advantage` = false (same strict readings as prior sessions).

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
= 89.684 -> rounds to 89.7
```

# Quality Score = 89.7 — PASSES the 80.0+ gate

## 5. Valuation Score (scripted)

Fair values: base $15.81 × 21 = $332.01; bull $432.00 / bear $176.00 carried; catalyst = Q3 FY2027 print, 2-year window; intrinsic growth 10%; `pe_mode: avg` (55.205×).

## Valuation Score

**FCF Yield (40%)**
```
FCF yield after SBC = 3.2788% - 0.1869% (SBC yield) = 3.0919%
FCF_Score = clamp(100x(1 - 3.0919/10)) = 69.081
```
**EV/EBIT**
```
EV/EBIT_Score = clamp((19.488 - 12)/23 x 100) = 32.557
```
**Forward PE**
```
Deviation% = (10.1664 - 55.205)/55.205 x 100 = -81.584%
FwdPE_Score = clamp(50 + -81.584x2.5) = 0.000 (fallback formula; Historical PE Modifier already folded in)
```
**PEG**
```
PEG_Score = clamp((0.1449 - 0.5)/2.0 x 100) = 0.000
```
**Rate Environment Gate**
```
EY = 1/10.1664 x 100 = 9.8363%
Spread = EY - 10Y (4.88%) = 4.9563pp -> Step 1 = +0 (pass, >=1.5pp)
10Y = 4.88% -> Step 2 bracket modifier = +5
Total Rate Modifier = 0 + 5 = +5
```
**Upside/Downside Modifier**
```
PW Fair Value = 0.25x432.0 + 0.50x332.01 + 0.25x176.0 = 318.0050
Gap Upside % = (318.0050/160.73) - 1 = 97.8504%
Annualized gap = 97.8504% / 2yr = 48.9252%/yr
E = 48.9252 (annualized gap) + 10.0 (intrinsic growth) + 2.0502 (shareholder yield: 0.6222 div + 1.428 buyback) = 60.9754%/yr
E (60.9754%) >= H (10.0%) -> M = -15 x clamp((60.9754-10.0)/15, 0, 1) = -15.0000
Upside/Downside Modifier (bounded [-15, +15]) = -15.0000
```
**Raw Weighted Score**
```
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.25 + FwdPE_Score x 0.2 + PEG_Score x 0.15
= 35.772
```
**Final Valuation Score**
```
Final Score = Raw (35.772) + Rate Modifier (+5) + Upside/Downside Modifier (-15.000)
= 25.772 -> rounds to 25.8
```

# Valuation Score = 25.8

### 5b. Advisory flags (no score effect)

```
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             CYCLE_PEAK_CANDIDATE   EPS TTM +125% > 100%† — state why the multiple is compared with a normalised base
  multiple_ceiling       NONE                   forward PE 10.2, EPS growth 70.2%
  value_trap_candidate   NONE                   forward PE 10.2, EPS TTM growth +125.4%
```
- **`CYCLE_PEAK_CANDIDATE`:** TTM GAAP diluted EPS $7.91 vs $3.51 a year earlier (+125.4%, SEC XBRL via the 11-05 derivation). Same handling as 11-05: FwdPE and PEG sub-scores floor at 0.0 against any plausible normalised base (5-yr *low* PE is 32.5×; even a 50% EPS haircut gives ≈20×, still below the 55× avg); the weight-carrying sub-scores (FCF yield, EV/EBIT) use realised cash flow/operating profit; the 25%-weighted bear case ($11 × 16 = $176) is the earnings-reversion scenario. Residual risk stated, not scored — base-case EPS quality is what the print tests.
- `MULTIPLE_CEILING`: NONE. `VALUE_TRAP_CANDIDATE`: NONE. No `UNKNOWN`s once the SEC EPS figures were supplied (yfinance's own flag lines showed UNKNOWN for lack of quarterly EPS history — a data gap handled by the manual run above).

## 6. Rate Environment Gate

EY 9.836% vs 10Y 4.88% → spread +4.96pp ≥ +1.5 → pass (+0). Step 2 bracket 3.5–5% → +5. Total +5. (If the 10Y closes above 5%: +10 → Valuation 30.8, Composite 20.5 — same band and action.)

## 7. Composite Score

## Composite Score

```
Composite Score = 0.50x(100 - 89.7) + 0.50x25.8 = 18.050 -> rounds to 18.0
```

# Composite Score = 18.0
(Quality Score 89.7, Valuation Score 25.8)

Note: the script rounds from the unrounded Valuation (25.772 → 18.044 → 18.0); using the rounded 25.8 gives 18.05, which the ".X5 rounds up" rule would make 18.1. Both sit in the same band; **18.0 (script) is recorded**, and the order setup was run with 18.1 — identical MoS/stop/risk/cap band.

| | 11-05 | 11-12 | Driver |
|---|---|---|---|
| Quality | 89.7 | **89.7** | No fundamental input changed |
| Valuation | 30.9 | **25.8** | Price −13.9%: EV/EBIT 22.7×→19.5× (46.4→32.6), FCF yield 2.82%→3.28% (FCF_Score 73.4→69.1); U/D modifier stays at −15.0 floor (E 46.9%→61.0%/yr) |
| Composite | 20.6 | **18.0** | Entirely price-driven; the scoring lands deeper in the "Very Cheap" band |

## 8. Action recommendation & order setup

Fair value (unchanged inputs): PW FV $318.005; multiples $322.995; blended **$321.00** (0.40 × 318.005 + 0.60 × 322.995). MoS 17.5%, stop 22.5%, risk 1.5%, cap 8% (band-midpoint convention).

## Order Setup

```
Band: 0.0-29.9 (Enter now)
Buy Price = Fair Value (321.0) x (1 - 17.5%) = 264.8250
Live price 160.73 vs buy price ceiling 264.8250 -> enter now (live price at/below buy price ceiling); entry price used = 160.7300
Primary Sell Target = Fair Value = 321.0000
Bull-Case Trim Target = Bull FV (432.0) x 0.90 = 388.8000
Stop Loss = Entry Price (160.7300) x (1 - 22.5%) = 124.5657
R/R Ratio = (Sell Target 321.0000 - Entry 160.7300) / (Entry 160.7300 - Stop 124.5657) = 160.2700/36.1642 = 4.4317:1
Max $ Risk = Portfolio Value (45706.3) x 1.5% = 685.5945
Risk Per Share = Entry (160.7300) - Stop (124.5657) = 36.1642
Shares by risk-based sizing = 685.5945 / 36.1642 = 18.9578
Allocation cap = Portfolio Value (45706.3) x 8% = 3656.5040 -> 22.7494 shares
Position Size (shares) = min(risk-based, cap) = 18.9578  [binding: risk-based sizing]
Position Size ($) = 18.9578 x 160.7300 = 3047.0867
Current shares held = 40; gap vs. target = -21.0422
```

### Order Setup Checklist
```
[✓] Risk/Reward Ratio:      4.43:1  (must be >= 2:1)
[ ] BUY PRICE (ceiling):     264.82
[ ] Entry Price used:        160.73  (enter now (live price at/below buy price ceiling))
[ ] PRIMARY SELL TARGET:     321.00
[ ] BULL-CASE TRIM TARGET:   388.80
[ ] STOP LOSS:               124.57
[ ] Max $ Risk:               685.59
[ ] POSITION SIZE (shares):  18.9578  (binding: risk-based sizing)
[ ] POSITION SIZE ($):       3047.09
[ ] Current shares held:     40
```

### Interpretation

- **Nominal action: BUY — Full position (6–8%).** Composite 18.0 is in the 0.0–29.9 band; R/R **4.43:1** passes the 2:1 gate; live price is far below the $264.83 buy ceiling.
- **Practical action: HOLD — no add, no trim.** The position is **40 sh vs an 18.96-sh risk-based target (21.0 sh over)** and ≈14.1% of NLV vs the 8% allocation cap, i.e. it is already **~2.1× the framework's full-position size**. No order setup can justify adding. No trim either: an over-target position is not a trim trigger and Composite 18.0 is nowhere near a trim band; selling on a sizing gap created by a price drop would be acting on price alone.
- **Hard-cap watch (Upgrade 7):** at the re-marked NLV the position (≈14.1%) breaches 15% once NVDA rises ≈8% to ≈$173 (solving 40p = 0.15 × ($39,277 + 40p), with the rest of the account held flat). **This is the one hard constraint that could force action**; recommend a human glance (and consideration of the standing SELL 10 NVDA @ $200.50 order noted at the 11-08 sync) at the next `/rebalance`. This session placed/modified no order.
- **Provenance flag:** the 21-share add (11-02 → 11-08 sync) is not covered by a session or decision log; the 11-05 rescore of this ticker explicitly recommended *no add* (19 sh already above its 16.46-sh target). Document it in `decisions/` or log it in [override-log.md](../portfolio/override-log.md) if it was a deliberate override.
- **Thesis-invalidation triggers (unchanged):** AI-capex digestion (the print vs the $108.0B Q3 FY2027 revenue guide is the test); FCF/NI conversion (65.8% plain / 62.1% after SBC TTM; re-test at FY2027 year-end); gross margin >3pp structural fall; CUDA moat erosion; China-exposure report (unverified); a filed guidance cut or 8-K.

All final decision authority rests with the human investor.

## 9. Next review trigger

- **NVDA Q3 FY2027 earnings, ≈17 Nov 2026 AMC (unconfirmed)** — standard post-earnings `/rescore` due immediately after; it refreshes every reused TTM input, forward EPS and price targets.
- Re-run immediately on a filed 8-K/guidance revision, a >15% unexplained move, or NVDA crossing ≈$173 (15% hard-cap line, all else flat, informational — a sizing check, not a score trigger).
- Rate gate: 10Y 4.88%, 0.12pp below the 5% bracket line.

---

## Glossary

**10-Q (Quarterly Report)**: The quarterly financial-disclosure report a US public company files with the SEC between annual 10-Ks, containing unaudited (reviewed) financial statements for the most recent fiscal quarter — used in this framework to reconstruct trailing-twelve-month (TTM) figures between annual reports, as in the 2026-07-06 AAPL session.
**8-K**: The "current report" a US public company must file with the SEC within days of a material event — most commonly used to furnish (via an attached exhibit, typically "Exhibit 99.1") a quarterly earnings press release ahead of the fuller, audited 10-Q/10-K that follows weeks later. Apple's fiscal Q3 2026 results were sourced from its 30 July 2026 8-K (Exhibit 99.1) in this framework's 2026-07-31 AAPL session, since the corresponding 10-Q had not yet been filed. *(New term.)*
**Composite Score**: This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50 — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only for companies that have already cleared the 80.0+ Quality Score gate. Used against the Phase 03/05 action tables instead of the raw valuation score. See [valuation-scoring.md](valuation-scoring.md).
**Quality Score**: This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. See [quality-scoring.md](quality-scoring.md).
**Valuation score**: This framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive) combining the Phase 02 valuation sub-scores, the Rate Environment Gate, and the Upside/Downside Modifier into a single number that maps to an action band (Very Cheap/Cheap/Fair Value/Expensive) — see [valuation-scoring.md](valuation-scoring.md).
**FCF**: Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
**FCF Yield**: Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
**SBC (Stock-Based Compensation)**: Employee pay in the form of company shares or stock options rather than cash. A non-cash expense added back in cash-flow statements (inflating FCF relative to GAAP net income), but a real economic cost to existing shareholders through ongoing dilution — worth tracking alongside FCF/NI conversion and share-count trend, not just the headline FCF figure. Since the 2026-10-12 methodology it is treated as a cost in both the FCF yield (Valuation) and FCF Quality (Quality).
**EV**: Enterprise Value — a company's total value to all capital providers: market cap + debt − cash.
**EV/EBIT, EV/EBITDA**: Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.
**EBIT**: Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
**Forward PE**: Price ÷ next twelve months' *expected* earnings per share (vs. Trailing PE, which uses the last twelve months' actual earnings).
**PEG ratio**: PE ratio ÷ earnings growth rate — a PE adjusted for growth, used to judge whether a fast grower's multiple is justified by its growth rate.
**Fast Grower**: Peter Lynch's term for a company growing earnings per share (EPS) faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score.
**EY (Earnings Yield)**: 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury).
**Rate Environment Gate**: The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier.
**Rate Regime Modifier**: An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in.
**Treasury yield (10Y)**: The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate.
**Upside/Downside Modifier (Expected-Return Modifier)**: An additive ±15 adjustment to the valuation score based on expected annual return (the gap to PW Fair Value, annualized over the catalyst window, plus intrinsic growth and shareholder yield) — folds the forward-looking dimension into the score so strong expected upside pulls a name toward "buy" and a thin/negative expected return pushes it toward "trim/sell."
**PW (Probability-Weighted) Fair Value**: This framework's blended fair value estimate — 25% bull case + 50% base case + 25% bear case (Rule 7) — used as the single fair-value input to both the order setup and the Upside/Downside Modifier.
**FV (Fair Value)**: The analyst's estimate of what a company is intrinsically worth, independent of its current market price.
**MoS (Margin of Safety)**: How far below fair value the buy price is set, as a cushion against being wrong — e.g. a 25% MoS means buying at 75% of estimated fair value.
**R/R (Risk/Reward ratio)**: (Expected gain) ÷ (Expected loss) on a trade — this framework requires at least 2:1 before entering.
**Stop loss**: A pre-set price below the entry at which a position is exited to cap the loss on a trade; this framework sets it 20–35% below entry depending on the Composite Score band (fair-value-methodology.md Step 4), and the position size is derived from it so a stop-out costs only 1–2% of the portfolio.
**TTM (Trailing Twelve Months)**: The most recent 12 months of reported financial results (the last four quarters added together), as opposed to a single fiscal year or a forward-looking estimate. *(New term.)*
**ROIC**: Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
**Net Debt/EBITDA**: Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
**Cycle peak**: The top of a business cycle, when earnings are temporarily inflated (e.g. memory-chip prices at a high). A stock then looks cheap on trailing earnings exactly when it is most expensive on normal earnings. This framework flags it when trailing EPS grew more than 100% in a year.
**Advisory flag**: A warning printed during analysis (e.g. `CYCLE_PEAK_CANDIDATE`, `MULTIPLE_CEILING`, `VALUE_TRAP_CANDIDATE`, the SBC block) that changes **no** score or action by itself. The analyst must say in the session log how it was handled; `UNKNOWN` means missing data, not a pass. See valuation-scoring.md, "Advisory Flags".
**Rule 9**: This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
**yfinance**: An unofficial open-source Python library that scrapes Yahoo Finance for prices and fundamentals; this repo's `fetch_fundamentals` script depends on it, so when Yahoo rate-limits it ("Too Many Requests") that script fails and figures must be sourced elsewhere (SEC EDGAR, finviz, stockanalysis.com) and flagged.
**Market Cap (Market Capitalization)**: Share price × total shares outstanding — the total value the market currently assigns to all of a company's equity. Combined with Net Debt, gives Enterprise Value (EV). *(New term.)*
**Catalyst window**: The timeframe (per Rule 10, typically 18–24 months) within which a documented, specific event is expected to close the gap between price and fair value — required before the Upside/Downside Modifier can credit large expected upside.
**Position cap (15% hard cap / 8% allocation cap)**: Two separate ceilings on how much of the framework account one stock may be. The **15% hard cap** (Hybrid Upgrade 7) is never to be exceeded under any circumstances. The **allocation cap** is the tighter, score-band-specific ceiling in the order-setup cap table (e.g. 8% for a 0.0–29.9 Composite) that sizes a *new* purchase; a position can sit above the allocation cap yet below the hard cap, which is a flag for review, not a forced sale. *(New term.)*
**NLV (Net Liquidation Value)**: A broker's headline value for an account: all positions at current market price, plus cash, minus any liabilities — the broker's own summary number, distinct from manually summing position values and cash yourself (the two can differ slightly due to settlement timing).
**Moat**: Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
**CUDA**: NVIDIA's proprietary parallel-computing software platform and programming model for its GPUs — the dominant software layer AI/ML developers build on, and the basis for this framework's Network Effect (ecosystem value grows as more developers join) and Switching Costs (production code/pipelines built around it) moat-signal findings for NVDA.

# NEW POSITION — Taiwan Semiconductor Manufacturing Co. (TSM) — 2026-11-05

**Task type:** NEW POSITION (re-evaluation, not held) — 5th evaluation of this ticker (prior: 07-12, 07-16, 08-10, 09-06)
**Date:** 05 Nov 2026 | **10Y Treasury:** 4.95% (FRED `DGS10`, latest posted observation 2026-11-03; 11-04/11-05 not yet posted) | **Rate Regime Modifier:** +5 (3.5–5% bracket)
**Portfolio weight:** 0% (not held) | **Framework NLV (U19421206):** $46,102.05 ([holdings.md](../portfolio/holdings.md))

**Outcome in one line:** Quality **84.5** (passes) · Valuation **53.7** · Composite **34.6** ("Cheap" band) — but **R/R 1.33–1.43:1 fails the 2:1 gate → WATCHLIST ONLY, no order.**

---

## 1. Why this session ran — Rule 9 triggers

1. **Q3 2026 earnings** (TSMC 6-K, 2026-10-15) — a scheduled "next review trigger" from the 09-06 entry.
2. **Live price −14.6% vs. the 09-06 session** ($427.98 → $365.51), just under the 15% Rule 9 move line, and **−7.64% today** alone (prior close $395.75).
3. **Cause of today's drop: not confirmed.** Same-day web results describe a sector-wide chip selloff (Philadelphia Semiconductor index −5.7% to −7.3%, Nvidia lower) but give conflicting, unverified causes (one source: U.S. midterm results/data-center regulation worries; another: cross-border chip trade restrictions/valuation compression), from crypto-exchange and flash-news sites. **Nothing here is treated as a verified fundamental event, and the framework does not act on price alone** — it is flagged as an open item (§9).

## 2. Live price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price used** | **$365.51** (bid 365.45 / ask 365.55, REALTIME) | IBKR snapshot, contract 6223250 (NYSE ADR). An earlier read this session was $364.54; the later one is used throughout. |
| Prior close | $395.75 (change −$30.24, −7.64%) | IBKR |
| Cross-check | analyst-target feed "current" $364.77 | yfinance (moments earlier) |
| 52-week range | $264.07 – $487.47 | IBKR `misc_statistics` |
| Dividend yield | 0.95% | IBKR |
| Analyst targets (sanity check only) | mean $586.69 / median $560 / high $1,000 / low $440; 21 analysts (6 Strong Buy, 14 Buy, 1 Hold) | yfinance |

## 3. Data-gap resolution — the stop-and-ask from earlier this session

`python -m scripts.fetch_fundamentals TSM` was run and its output is pasted verbatim below. **Its quantitative block is unusable for TSM**: it divides TSMC's New Taiwan dollar (NT$) financials by a US$ market cap/price, giving nonsense (FCF yield 77.7%, EV/EBIT 4.4×, EV 13.2 *trillion*). Its TTM net margin (51.12%) also differs from the primary-sourced 51.53%, consistent with the Q4-2025 vendor net-income error flagged in the 08-10 session. SBC and the advisory flags returned `UNKNOWN`. Per your instruction ("rebuild the inputs from TSMC's primary filings") **every input below was rebuilt from TSMC's own documents**; the script's currency-neutral outputs (ROIC, gross margin, 3-yr revenue CAGR, annual FCF/NI list, 5-yr PE range) were used only where cross-checked.

```


Market Cap            = 1,882,819,657,728
Enterprise Value      = 13,221,541,969,920
Shares Outstanding    = 5,186,474,013
Forward PE            = 15.491
FCF Yield %           = 77.695
EV/EBIT               = 4.367
Net Margin %          = 51.116
Gross Margin %        = 65.846
ROIC % (NOPAT/InvCap) = 39.241  [tax_rate=0.1721, NOPAT=2,506,749,632,785, InvestedCapital=6,388,026,400,000]
Revenue 3yr CAGR %    = 18.938
Net Debt/EBITDA       = -0.472  [EBITDA_ttm=3,611,427,078,144]
FCF/NI TTM % (plain)  = 57.876
(FCF - SBC)/NI TTM %  = UNKNOWN - supply manually; scorers will stop and ask  [reported NI]
SBC yield %           = UNKNOWN - supply manually; scorers will stop and ask
Gross buyback yield % = UNKNOWN - supply manually; scorers will stop and ask  (enter 0 only if the filings show no repurchases)
FCF/NI annual (oldest first) = [52.5%, 33.6%, 74.3%, 58.5%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 23.105 / 10.219 / 31.899  (n=20 quarters)



SBC block: UNKNOWN - 'Stock Based Compensation' not available for 4 consecutive quarters; supply sbc_ttm manually (python -m scripts.scoring.sbc) or state the gap. Never estimate.
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
  (cycle_peak / value_trap need 8 consecutive quarters of Diluted EPS; if yfinance lacks them, run python -m scripts.scoring.flags_common with manually sourced EPS TTM figures.)

```

### 3.0 ⚠️ Correction to the 2026-09-06 record

The [09-06 session](2026-09-06-new-position-tsm.md) cited an "August 2026 monthly-revenue 6-K" of NT$250.87B (+33% YoY, −2.4% MoM) as its Rule 9 trigger. **That filing cannot have existed on 09-06**: TSMC's August revenue 6-K was filed on **2026-09-10** and shows **NT$514.81B, +10.1% MoM, +53.3% YoY** (Jan–Aug +39.3%). The 09-06 figures do not match any primary filing found this session and should be treated as unsupported. (The 09-10 Telegram post that the telegram-scan log marked "unverified/likely inaccurate" — "53% YoY, 10% MoM" — was in fact **correct**.) The 09-06 scores themselves were built mostly from carried inputs and do not depend on that figure, but the "deceleration" narrative in that entry is withdrawn. Not edited retroactively beyond a pointer in the watchlist row; the telegram-watch log line is left as history.

### 3.1 Primary sources used

| Input | Source |
|---|---|
| Q3 2026 income statement, balance sheet, cash flow, FCF, capex, net cash | TSMC **Quarterly Management Report 3Q26** and 3Q26 condensed financial statements (investor.tsmc.com; furnished as Exhibits 99.1/99.2 to Form 6-K filed 2026-10-15, acc. 0001046179-26-000726) |
| Q4 2025 and Q1 2026 quarterly lines | Primary-sourced table in [08-10 session](2026-08-10-new-position-tsm.md) §2.3; **reconciled exactly** (revenue, gross profit, operating income, pretax, net income, D&A) to TSMC's own 9M-2026 totals (e.g. 9M revenue NT$3,898,727M = 1,134,103 + 1,270,381 + 1,494,243) |
| Aug/Sep 2026 monthly revenue | 6-Ks 2026-09-10 and 2026-10-08: Aug NT$514.81B (+10.1% MoM, +53.3% YoY); Sep NT$511.86B (−0.6% MoM, **+54.6% YoY**); Jan–Sep +41.1% YoY |
| **SBC (stock-based compensation)** | FY2025 Form 20-F consolidated cash-flow statement (acc. 0001628280-26-025362, R6): "Share-based compensation" **NT$1,246.1M** (FY2024 NT$1,242.7M — matches the XBRL fact in SEC `companyfacts`). The quarterly condensed statements do not itemise SBC, so **the latest disclosed full year is used as the TTM figure** — a disclosed substitution; it is 0.084% of TTM FCF, and even a 10× error would not change any score |
| Buybacks | 20-F: "Treasury stock acquired" 0.0 in FY2025; no repurchase line in 9M-2026 condensed financing → gross buyback yield 0 |
| Consensus EPS / targets | yfinance `earnings_estimate`: FY2026 $17.487 (12 analysts, $17.18–17.95), FY2027 $23.434 (14 analysts, $21.45–25.87), Q4-26 $5.164, Q1-27 $5.194 — **single vendor this session** (no second-vendor cross-check obtained; flagged) |
| 10Y yield | FRED `DGS10` 4.95% (2026-11-03) |

### 3.2 Derivations (NT$ millions unless stated)

```
Window = Q4'25 + Q1'26 + Q2'26 + Q3'26 (all four quarters primary-sourced)
TTM Revenue   = 1,046,090 + 3,898,727                  = 4,944,817
TTM Gross Pft = 651,987 + 2,603,985                    = 3,255,972  → GM 65.846%
TTM Op Income = 564,903 + 2,302,014                    = 2,866,917  → OM 57.978%
TTM Pretax    = 592,363 + 2,461,269                    = 3,053,632
TTM Net Inc   = 505,744 + 2,042,106 (parent)           = 2,547,850  → NM 51.526%   (Q4'25 uses TSMC's own 505,744, not the vendor's 485,465)
Eff. tax      = (3,053,632 − 2,547,850) / 3,053,632    = 16.56%
TTM D&A       = 162,112 + 584,192                      = 746,304 → EBITDA = 2,866,917 + 746,304 = 3,613,221
TTM FCF       = Q4'25 368,600 + Q1'26 348,213 + Q2'26 287,363 + Q3'26 476,570 = 1,480,746   (OCF − capex; Q4'25 per Mgmt Report; the earlier vendor figure 364,041 differs by 1.2% — immaterial)
FCF/NI        = 1,480,746 / 2,547,850 = 58.12%  |  (FCF − SBC)/NI = (1,480,746 − 1,246.1)/2,547,850 = 58.07%

Net cash (30-Sep-26, Mgmt Report "Net Cash Reserves") = cash & marketable securities 4,016,980 − interest-bearing debt 1,031,580 = 2,985,400  (cash-only variant: −717 → −0.717×; both saturate the score)
Net Debt/EBITDA = −2,985,400 / 3,613,221 = −0.826×
Invested capital = debt 1,031,580 + equity 7,043,228 − cash 3,621,894 = 4,452,914 ; NOPAT = 2,866,917 × (1 − 0.1656) = 2,392,061 ; ROIC = 53.72%

FX: TTM-average = NT$4,944,817M ÷ US$156,550M (33.73 + 35.90 + 40.20 + 46.72 reported US$B) = 31.586 (flows);
    balance sheet at TSMC's own 30-Sep-26 translation rate 31.880. (yfinance spot 33.02 was NOT used — one unverified source; web quotes ranged 31.4–32.4 and undated.
    Effect of any of these on EV: net cash is 4.9% of market cap, so a ±4% change in the balance-sheet FX rate moves EV/EBIT by <0.2%; flows use rates derived from TSMC's own reported NT$ and US$ revenue.)
Shares = 25,932.370M ordinary ÷ 5 = 5,186.474M ADR-equivalents ; Market cap = $365.51 × 5,186.474M = $1,895,708M
TTM FCF US$ = 1,480,746 / 31.586 = $46,880M → FCF yield 2.4729% ; SBC US$ = $39.45M → SBC yield 0.0021%
TTM EBIT US$ = $90,765M ; EV = 1,895,708 − 93,645 = $1,802,063M → EV/EBIT 19.85×
Forward PE (FY2027 anchor, "Construction B" as in 08-10/09-06) = 365.51 / 23.434 = 15.60×
   (A: FY2026 anchor 365.51/17.487 = 20.90× | C: NTM = 5.164 + 5.194 + ⅔×(23.434 − 5.194) = 22.52 → 16.23×)
5-yr PE history: script's documented quarterly reconstruction, 20 quarters: avg 23.105 / low 10.219 / high 31.899
   (differs from the annual 20.74 / 11.44 / 26.73 used in prior TSM sessions; both tested in §8)
PEG: still not applied (FY2023 cyclical EPS decline −14.2% is still inside the trailing 3-fiscal-year window) → weight to EV/EBIT.
```

### 3.3 Advisory flags (no score effect)

```
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             NONE                   EPS TTM +59% (<= 100%†)
  multiple_ceiling       UNKNOWN                forward PE or EPS growth unavailable
  value_trap_candidate   NONE                   forward PE 15.6, EPS TTM growth +59.4%
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  multiple_ceiling       NONE                   forward PE 15.6, EPS growth 34.0%
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
```
`cycle_peak`: NONE (TTM ADR EPS $15.54 vs $9.75 a year ago, +59%; both sums from IBKR/Yahoo reported-EPS history and consistent with TSMC's Q3 EPS US$4.60). `value_trap_candidate`: NONE (forward PE 15.6 > 15, EPS rising). `MULTIPLE_CEILING`: NONE (forward PE 15.6 < 30; FY2027 consensus EPS growth 34.0%). SBC/FCF: 0.084% — nowhere near the 30% "elevated" line. **No flag raised, and no `UNKNOWN` remains.**

---

## 4. Phase 01 — Quality Score (script output, verbatim)

Hard-disqualifier notes: FCF/NI annual list for the current 3-fiscal-year window FY2023–FY2025 = [33.6%, 74.3%, 58.5%] (primary cross-check from XBRL/20-F: 34.8% / 74.2% / 58.4%) — FY2024 breaks the streak, so the "2 consecutive years <70%" test does not fire; a growth-capex explanation is also on file (9M-2026 capex US$40.64B). **Forward watch item from 08-10 remains:** FY2026 is the next year to be added; TTM FCF/NI has recovered to 58.1% (Q3 FCF NT$476.6B, capex down QoQ). SBC vs FCF test: NT$1,246M vs NT$1,480,746M — passes.

## Quality Score

**Profitability (25%)**
```
NetMargin_Component = clamp((51.526/30)x100) = 100.00
ROIC_Component = clamp((53.719/30)x100) = 100.00
Profitability_Score = (100.00 + 100.00) / 2 = 100.00
```
**Margins (15%)**
```
GrossMargin_Score = clamp((65.846/80)x100) = 82.31
```
**Growth (20%)**
```
Growth_Score = clamp((18.938/25)x100) = 75.75
+10 TAM/pricing-power evidence: TSMC 3Q26 Management Report/press release (6-K 2026-10-15, acc. 0001046179-26-000726): revenue US$46.72B, +41.2% YoY; 9M-2026 revenue +41.1% YoY (NT$3,898.73B); 2nm = 8% of wafer revenue (from 3%) ramping; HPC 68% of revenue (from 57% a year earlier); Q4-26 revenue guidance US$52.3-54.3B (vs US$46.72B); monthly revenue Aug +53.3% YoY, Sep +54.6% YoY (6-Ks 2026-09-10, 2026-10-08)
Growth_Score (final, clamped) = 85.75
```
**Balance Sheet (15%)**
```
BalanceSheet_Score = clamp(100x(1 - -0.8262/4)) = 100.00
```
**Moat Signal (15%)**
```
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Dominant leading-edge foundry share (~70-72%) cited in 2026-07-12/08-10 sessions and NOT re-verified this session; supported this session by primary data: advanced nodes (7nm and below) = 79% of 3Q26 wafer revenue, 2nm already 8%, revenue +50.9% YoY in NT$ (3Q26 Management Report) |
| brand_premium | True | Pricing power: gross margin 66.4% in 3Q26 (6.9pp above 3Q25) while absorbing 2nm ramp dilution; Q4-26 GM guided 65-67% (3Q26 press release, 6-K 2026-10-15) |
| network_effect | False | Dedicated foundry has no two-sided marketplace effect distinct from switching costs (unchanged from prior sessions) |
| switching_costs | True | Customer designs are tied to TSMC process design kits/IP ecosystem (OIP) with multi-year redesign cost; carried citation from 2026-08-10 session, unchanged; North America customers 79% of 3Q26 revenue sustained through node transitions (Management Report) |
| scale_cost_advantage | True | Funds US$40.64B 9M-2026 capex (Management Report V) from internal cash flow (OCF NT$2,402B 9M) while net cash NT$2,985B at 30-Sep-26 and paying NT$7.00/qtr dividend; carried Intel-gap citation from 2026-08-10 session |
Moat_Score = (4/5) x 100 = 80.00
```
**FCF Quality (10%)**
```
FCFQuality_Score = clamp(((0.5807 - 0.40)/0.60)x100) = 30.12  [ratio = (FCF - SBC)/NI]
```
**Quality Score — Final**
```
Quality Score = (100.00x0.25) + (82.31x0.15) + (85.75x0.20) + (100.00x0.15) + (80.00x0.15) + (30.12x0.10)
= 84.508 -> rounds to 84.5
```

# Quality Score = 84.5 — PASSES the 80.0+ gate

**Change vs. 09-06 (83.0 → 84.5):** Gross margin sub-score 80.29 → 82.31 (TTM GM 65.85%) and FCF Quality 18.05 → 30.12 (after-SBC FCF/NI 50.8% → 58.1% on the strong Q3 cash flow). Everything else is unchanged or saturated.

---

## 5. Rate Environment Gate

```
EY = 1 / 15.597 = 6.41% ; Spread = 6.41% − 4.95% = +1.46pp  < +1.5pp  → Step 1 FAIL → +5
Step 2: 10Y 4.95% → 3.5–5% bracket → +5          Total +10
```
**Razor-thin:** the spread misses the pass line by 0.04pp. If the 10Y prints 4.90% or lower (or the forward PE is a touch lower) Step 1 passes and the Valuation Score falls ~5 points (§8).

## 6. Phase 02 — Valuation Score (script output, verbatim)

Scenario inputs for the Upside/Downside Modifier (Rule 7): **Bull** = analyst-high FY2026 EPS $17.95 × 28 = $502.60; **Base** = consensus FY2026 EPS $17.487 × 24 = $419.69; **Bear** = $12.00 × 15 = $180.00. The 28×/24×/15× multiples and the $12.00 bear EPS are **carried unchanged from the 07-16/08-10/09-06 sessions** for comparability — these are standing analyst judgements, not newly sourced numbers (the bear EPS sits 23% below TTM EPS of $15.54 and is deliberately conservative; the alternative of TTM EPS × 15 is tested in §8). FY2026 is now 9/12 reported, so its consensus range is tight ($17.18–17.95). Intrinsic growth 10%/yr is likewise the carried, disclosed conservative haircut. Catalysts inside 18–24 months: Q4-26 results (mid-Jan 2027, guided US$52.3–54.3B revenue, 65–67% GM), the 2nm ramp (8% of wafer revenue and rising), 2027 capex plan.

## Valuation Score

**FCF Yield (40%)**
```
FCF yield after SBC = 2.4729% - 0.00208% (SBC yield) = 2.4708%
FCF_Score = clamp(100x(1 - 2.4708/10)) = 75.292
```
**EV/EBIT**
```
EV/EBIT_Score = clamp((19.854 - 12)/23 x 100) = 34.148
```
**Forward PE**
```
FwdPE_Score (raw) = clamp((15.597 - 10.219)/(31.899 - 10.219) x 100) = 24.806
Deviation vs 5yr avg (23.105) = (15.597 - 23.105)/23.105 x 100 = -32.495%
Historical PE Modifier: >20% below 5yr avg -> -10
FwdPE_Score = clamp(24.806 + -10) = 14.806
```
**PEG**
```
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT
```
**Rate Environment Gate**
```
EY = 1/15.597 x 100 = 6.4115%
Spread = EY - 10Y (4.95%) = 1.4615pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 4.95% -> Step 2 bracket modifier = +5
Total Rate Modifier = 5 + 5 = +10
```
**Upside/Downside Modifier**
```
PW Fair Value = 0.25x502.6 + 0.50x419.69 + 0.25x180.0 = 380.4950
Gap Upside % = (380.4950/365.51) - 1 = 4.0998%
Annualized gap = 4.0998% / 2yr = 2.0499%/yr
E = 2.0499 (annualized gap) + 10.0 (intrinsic growth) + 0.9500 (shareholder yield: 0.95 div + 0.0 buyback) = 12.9999%/yr
E (12.9999%) >= H (10.0%) -> M = -15 x clamp((12.9999-10.0)/15, 0, 1) = -2.9999
Upside/Downside Modifier (bounded [-15, +15]) = -2.9999
```
**Raw Weighted Score**
```
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 46.737
```
**Final Valuation Score**
```
Final Score = Raw (46.737) + Rate Modifier (+10) + Upside/Downside Modifier (-3.000)
= 53.737 -> rounds to 53.7
```

# Valuation Score = 53.7

**Why the score fell from 78.0 (09-06) to 53.7:** price −14.6%, while FY2027 consensus EPS rose ~7.5% ($21.79 → $23.43) and TTM EBIT is ~15% higher, so forward PE fell 19.33× → 15.60× and EV/EBIT 24.26× → 19.85×. The 09-06 figure predates the 2026-10-12 SBC methodology, but SBC is ~0.002% of market cap for TSMC, so that change does not explain the move. **For the first time, the live price ($365.51) sits ~4% *below* the probability-weighted fair value ($380.50).**

---

## 7. Composite Score (script output, verbatim)

## Composite Score

```
Composite Score = 0.50x(100 - 84.5) + 0.50x53.7 = 34.600 -> rounds to 34.6
```

# Composite Score = 34.6
(Quality Score 84.5, Valuation Score 53.7)

**34.6** — in the 30.0–49.9 "Cheap" band (Standard position, 3–5%), down from 47.5 on 09-06.

## 8. Sensitivity (each row re-run through the scripts; Quality fixed at 84.5)

| Variant | Valuation | Composite |
|---|---|---|
| **Base (used)** | **53.7** | **34.6** |
| Forward PE, FY2026 anchor (20.90×) | 60.6 | 38.0 |
| Forward PE, constructed NTM (16.23×) | 54.3 | 34.9 |
| Prior annual 5-yr PE range (11.44 / 26.73 / 20.74) | 54.2 | 34.9 |
| No-history PE fallback (50.0 neutral) | 60.8 | 38.1 |
| 10Y = 5.00% | 53.7 | 34.6 |
| 10Y = 4.90% (Step 1 passes) | 48.7 | 32.1 |
| Bear EPS = TTM $15.54 × 15 ($233.10) | 51.9 | 33.7 |
| Intrinsic growth 15% | 48.7 | 32.1 |

**Every variant lands at Composite 32.1–38.1: always inside the 30.0–49.9 band, so the band is not sensitive to the judgement calls.** Entry is blocked by the R/R gate under all of them (the gate depends on fair value, not on the score).

---

## 9. Phase 03 — Order setup & R/R gate (script output, verbatim)

######## MoS=25 stop=25
## Order Setup

```
Band: 30.0-49.9 (Set limit order)
Buy Price = Fair Value (380.5) x (1 - 25%) = 285.3750
Live price 365.51 vs buy price ceiling 285.3750 -> limit order at buy price (live price above ceiling); entry price used = 285.3750
Primary Sell Target = Fair Value = 380.5000
Bull-Case Trim Target = Bull FV (502.6) x 0.90 = 452.3400
Stop Loss = Entry Price (285.3750) x (1 - 25%) = 214.0312
R/R Ratio = (Sell Target 380.5000 - Entry 285.3750) / (Entry 285.3750 - Stop 214.0312) = 95.1250/71.3438 = 1.3333:1
*** FLAG: R/R 1.3333:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = Portfolio Value (46102.05) x 1.5% = 691.5308
Risk Per Share = Entry (285.3750) - Stop (214.0312) = 71.3438
Shares by risk-based sizing = 691.5308 / 71.3438 = 9.6929
Allocation cap = Portfolio Value (46102.05) x 5% = 2305.1025 -> 8.0775 shares
Position Size (shares) = min(risk-based, cap) = 8.0775  [binding: allocation cap]
Position Size ($) = 8.0775 x 285.3750 = 2305.1025
Current shares held = 0; gap vs. target = 8.0775
```

### Order Setup Checklist
```
[✗] Risk/Reward Ratio:      1.33:1  (must be >= 2:1)
[ ] BUY PRICE (ceiling):     285.38
[ ] Entry Price used:        285.38  (limit order at buy price (live price above ceiling))
[ ] PRIMARY SELL TARGET:     380.50
[ ] BULL-CASE TRIM TARGET:   452.34
[ ] STOP LOSS:               214.03
[ ] Max $ Risk:               691.53
[ ] POSITION SIZE (shares):  8.0775  (binding: allocation cap)
[ ] POSITION SIZE ($):       2305.10
[ ] Current shares held:     0
```
######## MoS=27.5 stop=27.5
## Order Setup

```
Band: 30.0-49.9 (Set limit order)
Buy Price = Fair Value (380.5) x (1 - 27.5%) = 275.8625
Live price 365.51 vs buy price ceiling 275.8625 -> limit order at buy price (live price above ceiling); entry price used = 275.8625
Primary Sell Target = Fair Value = 380.5000
Bull-Case Trim Target = Bull FV (502.6) x 0.90 = 452.3400
Stop Loss = Entry Price (275.8625) x (1 - 27.5%) = 200.0003
R/R Ratio = (Sell Target 380.5000 - Entry 275.8625) / (Entry 275.8625 - Stop 200.0003) = 104.6375/75.8622 = 1.3793:1
*** FLAG: R/R 1.3793:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = Portfolio Value (46102.05) x 1.5% = 691.5308
Risk Per Share = Entry (275.8625) - Stop (200.0003) = 75.8622
Shares by risk-based sizing = 691.5308 / 75.8622 = 9.1156
Allocation cap = Portfolio Value (46102.05) x 5% = 2305.1025 -> 8.3560 shares
Position Size (shares) = min(risk-based, cap) = 8.3560  [binding: allocation cap]
Position Size ($) = 8.3560 x 275.8625 = 2305.1025
Current shares held = 0; gap vs. target = 8.3560
```

### Order Setup Checklist
```
[✗] Risk/Reward Ratio:      1.38:1  (must be >= 2:1)
[ ] BUY PRICE (ceiling):     275.86
[ ] Entry Price used:        275.86  (limit order at buy price (live price above ceiling))
[ ] PRIMARY SELL TARGET:     380.50
[ ] BULL-CASE TRIM TARGET:   452.34
[ ] STOP LOSS:               200.00
[ ] Max $ Risk:               691.53
[ ] POSITION SIZE (shares):  8.3560  (binding: allocation cap)
[ ] POSITION SIZE ($):       2305.10
[ ] Current shares held:     0
```
######## MoS=30 stop=30
## Order Setup

```
Band: 30.0-49.9 (Set limit order)
Buy Price = Fair Value (380.5) x (1 - 30%) = 266.3500
Live price 365.51 vs buy price ceiling 266.3500 -> limit order at buy price (live price above ceiling); entry price used = 266.3500
Primary Sell Target = Fair Value = 380.5000
Bull-Case Trim Target = Bull FV (502.6) x 0.90 = 452.3400
Stop Loss = Entry Price (266.3500) x (1 - 30%) = 186.4450
R/R Ratio = (Sell Target 380.5000 - Entry 266.3500) / (Entry 266.3500 - Stop 186.4450) = 114.1500/79.9050 = 1.4286:1
*** FLAG: R/R 1.4286:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = Portfolio Value (46102.05) x 1.5% = 691.5308
Risk Per Share = Entry (266.3500) - Stop (186.4450) = 79.9050
Shares by risk-based sizing = 691.5308 / 79.9050 = 8.6544
Allocation cap = Portfolio Value (46102.05) x 5% = 2305.1025 -> 8.6544 shares
Position Size (shares) = min(risk-based, cap) = 8.6544  [binding: risk-based sizing]
Position Size ($) = 8.6544 x 266.3500 = 2305.1025
Current shares held = 0; gap vs. target = 8.6544
```

### Order Setup Checklist
```
[✗] Risk/Reward Ratio:      1.43:1  (must be >= 2:1)
[ ] BUY PRICE (ceiling):     266.35
[ ] Entry Price used:        266.35  (limit order at buy price (live price above ceiling))
[ ] PRIMARY SELL TARGET:     380.50
[ ] BULL-CASE TRIM TARGET:   452.34
[ ] STOP LOSS:               186.44
[ ] Max $ Risk:               691.53
[ ] POSITION SIZE (shares):  8.6544  (binding: risk-based sizing)
[ ] POSITION SIZE ($):       2305.10
[ ] Current shares held:     0
```

**R/R fails the 2:1 minimum at every MoS/stop pair in the band (1.33–1.43:1),** consistent with every prior TSM session (1.11–1.71:1 historically). The live price ($365.51) is **28% to 37% above** the buy ceilings ($285.38 / $275.86 / $266.35). For transparency only: measured against the *bull-case trim target* ($452.34) the same entries would give ≈2.3:1, but the framework's R/R uses the primary sell target (= fair value), so this is **not** a pass. *Observation for a future framework review (not acted on):* with sell target = fair value and the band's own ranges (MoS 25–30%, stop 25–30%), R/R = MoS ÷ ((1 − MoS) × stop) can never exceed 1.71:1, so no name in the 30.0–49.9 band can clear 2:1 on this construction unless the stop is tighter than the band allows.

## 10. Recommendation

**WATCHLIST ONLY — do not enter; no order set.** The quality case is stronger than ever (Quality 84.5; Q3 revenue +41% in US$, +50.9% in NT$; 66.4% gross margin through the 2nm ramp; net cash NT$2.99T) and the stock is now cheaper than at any prior review (Composite 47.5 → 34.6; price below carried PW fair value). But the framework's entry test is R/R, and it fails (1.33–1.43:1) because a 25–30% margin of safety needs ~$266–285 and the stock trades at $365.51. A limit order at the ceiling would sit 28–37% below the market after a −7.6% day; it was not placed, and no decision log is written because no trade occurred. (If ever filled at the ceiling, indicative sizing would be ≈8 shares / ~$2,305 = the 5% allocation cap of $46,102 NLV.)

## 11. Known risks, open items, and honest caveats

- **Today's −7.6% move is unexplained by any verified source** (§1); a geopolitical/trade-restriction cause would be a Rule 9 event and must be re-checked when primary news is available.
- **Consensus EPS is single-vendor** this session (yfinance); prior sessions also cross-checked a second vendor. The forward PE (15.60×) drives the Rate Gate and 20% of the score.
- **Rate Gate sits 0.04pp from flipping** (§5); 10Y for 11-04/05 not yet posted.
- **Scenario multiples, $12 bear EPS and 10% intrinsic growth are carried judgement calls** (§6); sensitivity shown (§8).
- **SBC TTM uses FY2025's NT$1,246M** because quarterly SBC is not itemised in the condensed statements (§3.1).
- **Taiwan Strait / export-control risk** is not captured in any numeric score and remains the standing qualitative risk for this name.

## 12. Next review triggers

1. **TSMC October 2026 monthly revenue — due 2026-11-10**.
2. Identification of the cause of the 2026-11-05 selloff (primary-source news).
3. **Q4 2026 earnings, mid-January 2027** — rebuild the fair-value table on a FY2027 anchor.
4. Price at or below ~$285 (25% MoS) would make the R/R gate testable; a 10Y reading that flips Step 1; any Taiwan/export-control action; standard Rule 9 triggers (>15% unexplained move from $365.51).

---

## Glossary

**ADR (American Depositary Receipt)**: A US-exchange-listed security representing shares of a non-US company, letting US investors trade it in USD without using a foreign exchange directly. ADRs can represent a 1:1, multiple, or fractional ratio of home-market shares — for Nokia's NOK, this framework confirmed (rather than assumed) a 1-for-1 ratio against the Helsinki-listed ordinary share by cross-checking IBKR's live USD quote against Yahoo Finance's EUR-denominated financials converted at the prevailing spot FX rate; the two were internally consistent, no ratio adjustment needed.
**SBC (Stock-Based Compensation)**: Employee pay in the form of company shares or stock options rather than cash. A non-cash expense added back in cash-flow statements (inflating FCF relative to GAAP net income), but a real economic cost to existing shareholders through ongoing dilution — worth tracking alongside FCF/NI conversion and share-count trend, not just the headline FCF figure. Since the 2026-10-12 methodology it is treated as a cost in both the FCF yield (Valuation) and FCF Quality (Quality).
**FCF**: Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
**FCF Yield**: Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
**EV/EBIT, EV/EBITDA**: Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.
**Forward PE**: Price ÷ next twelve months' *expected* earnings per share (vs. Trailing PE, which uses the last twelve months' actual earnings).
**NTM (Next Twelve Months)**: A forward-looking estimate covering the next twelve months from today — distinct from a "current fiscal year" or "next fiscal year" analyst consensus estimate, which can diverge materially from a true NTM figure depending on how far into the current fiscal year the company already is. This framework had historically used a single "Forward EPS (NTM)" label loosely for whichever forward-year consensus figure a data vendor supplied; SPGI's 2026-08-09 rescore session found this imprecise post-spinoff (the vendor's "forward EPS" field actually reflected the *next* fiscal year, not a blended NTM) and switched to citing the specific fiscal-year basis used for each calculation instead. *(New term.)*
**TTM (Trailing Twelve Months)**: The most recent 12 months of reported financial results (the last four quarters added together), as opposed to a single fiscal year or a forward-looking estimate. *(New term.)*
**R/R (Risk/Reward Ratio)**: (Expected gain) ÷ (Expected loss) on a trade — this framework requires at least 2:1 before entering.
**MoS (Margin of Safety)**: How far below fair value the buy price is set, as a cushion against being wrong — e.g. a 25% MoS means buying at 75% of estimated fair value.
**PW (Probability-Weighted) Fair Value**: This framework's blended fair value estimate — 25% bull case + 50% base case + 25% bear case (Rule 7) — used as the single fair-value input to both the order setup and the Upside/Downside Modifier.
**Upside/Downside Modifier (Expected-Return Modifier)**: An additive ±15 adjustment to the valuation score based on expected annual return (the gap to PW Fair Value, annualized over the catalyst window, plus intrinsic growth and shareholder yield) — folds the forward-looking dimension into the score so strong expected upside pulls a name toward "buy" and a thin/negative expected return pushes it toward "trim/sell."
**Rule 0**: This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
**Rule 9**: This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
**6-K**: A report a foreign private issuer (a non-US-incorporated company that qualifies for this distinct SEC filer status) furnishes to the SEC to disclose quarterly/interim results, press releases, and other material information — filed in lieu of the domestic-filer 10-Q a US-incorporated company would use. POET Technologies (Ontario, Canada-incorporated) reported its Q2 2026 results to the SEC via Form 6-K rather than a 10-Q, cited in this framework's 2026-08-14 POET session. *(New term.)*
**Form 20-F**: The annual report US-listed foreign private issuers (non-US companies) file with the SEC — the international equivalent of a US company's Form 10-K. Contains full audited financial statements and is a primary regulatory disclosure, used in this framework as a fallback fundamentals source when `yfinance` is unavailable.
**Quality Score**: This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. See [quality-scoring.md](quality-scoring.md).
**Valuation score**: This framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive) combining the Phase 02 valuation sub-scores, the Rate Environment Gate, and the Upside/Downside Modifier into a single number that maps to an action band (Very Cheap/Cheap/Fair Value/Expensive) — see [valuation-scoring.md](valuation-scoring.md).
**Composite Score**: This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50 — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only for companies that have already cleared the 80.0+ Quality Score gate. Used against the Phase 03/05 action tables instead of the raw valuation score. See [valuation-scoring.md](valuation-scoring.md).
**Net Debt/EBITDA**: Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
**ROIC**: Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
**Capex**: Capital Expenditure — money spent buying or upgrading physical assets (factories, equipment, data centers).
**Moat**: Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
**Hard disqualifier**: One of three Quality Score conditions ([quality-scoring.md](quality-scoring.md)) that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation. A weighted average can't average away an outright balance-sheet or cash-flow-quality failure.
**Rate Environment Gate**: The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier.
**Treasury yield (10Y)**: The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate.
**Hurdle rate**: The minimum acceptable annual return for an investment to be worth making — this framework uses 10% as the hurdle the Upside/Downside Modifier measures expected return against.
**Gross cash buyback yield**: Cash actually spent repurchasing shares in the last twelve months ÷ market cap, ignoring new shares issued. Used (not the net-of-issuance figure) in the Upside/Downside shareholder yield because SBC dilution is already deducted in the FCF yield.
**Historical PE Modifier**: Hybrid Upgrade 2: an additive adjustment to the Forward PE sub-score based on where the current multiple sits versus the company's own trailing 5-year PE — >20% below average → −10 (cheap), within ±10% → 0, >20% above → +10 (expensive). When no statistically usable 5-year PE history exists (recent IPO, an unprofitable-to-profitable transition, or a one-off earnings distortion still inside the window), this framework uses a flagged neutral 50.0 "no-history fallback" instead of forcing an estimate — see [valuation-scoring.md](valuation-scoring.md).
**EY (Earnings Yield)**: 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury).
**Earnings Yield Spread Test**: Step 1 of the Rate Environment Gate: Earnings Yield (1 ÷ Forward PE) minus the 10-Year Treasury yield. A spread below +1.5% fails the test and adds a +5 flag to the valuation score (raising the bar, not vetoing entry) — see [strategy.md](strategy.md).
**Management Report (TSMC Quarterly Management Report)**: TSMC's own quarterly results summary (published with each earnings release and furnished to the SEC as an exhibit to a Form 6-K), containing the income statement, balance sheet, cash-flow and free-cash-flow tables, capex and guidance in NT$ and US$. It is the primary source this framework uses for TSM's quarterly inputs — it states free cash flow, net cash and capex directly, so no vendor reconstruction is needed. Cited in this framework's 2026-11-05 TSM session. *(New term.)*
**NT$ (New Taiwan Dollar, TWD)**: Taiwan's currency. TSMC reports its financial statements in NT$ millions/billions, while its US-listed ADR trades in US$ — any ratio mixing the two (e.g. a US$ market cap divided by NT$ cash flow) is wrong by a factor of ~32 until the NT$ figures are converted. This framework converts flows at the trailing-twelve-month average rate implied by TSMC's own reported NT$ and US$ revenue, and balance-sheet items at TSMC's own period-end translation rate. Cited in this framework's 2026-11-05 TSM session. *(New term.)*

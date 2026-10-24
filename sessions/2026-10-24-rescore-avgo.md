# RESCORE — AVGO (Broadcom Inc.) — 2026-10-24

**Task type:** RESCORE (mode `--both`)
**Trigger:** User-requested rescore, 12 days after 2026-10-12, and the first AVGO rescore under the **2026-10-12 SBC-as-a-cost methodology** (the 2026-10-12 session's 71.4 / 86.3 / 42.6 predate it — AVGO was on the [STALE list](../watchlist/STALE.md)). No new earnings: latest 8-K remains 2026-09-02 (Items 2.02/8.01/9.01); latest 10-Q 2026-09-10 is the Q3 FY2026 report already reflected (SEC EDGAR submissions API, CIK 0001730168). TTM/balance-sheet inputs carried forward unchanged; live price, 10Y, forward EPS, and the SBC treatment are new.
**Date:** 24 Oct 2026 (Saturday — prices are the Fri 23 Oct close)
**10Y US Treasury Yield:** **4.988%** (`yfinance` `^TNX` close 2026-10-23). **First reading below 5% since the 2026-09-15 crossing** (5.24% on 10-12, 5.146% on 10-21, 4.953% on 10-22).
**Rate Regime Modifier (Step 2):** **+5** (3.5–5% bracket) — down from +10.
**Current AVGO position:** 6 sh (IBKR U19421206 sync 2026-10-18, avg cost $382.44). At $321.68 = $1,930 = **4.04%** of the $47,820.23 framework Net Liquidation Value.
**Sector:** Semiconductors (fabless — AI accelerators/networking) + Infrastructure Software (VMware)
**Last review:** 12 Oct 2026 (Valuation 71.4 / Quality 86.3 / Composite 42.6) — [session](2026-10-12-rescore-avgo.md)

---

## 0. Override status (reported, not resolved)

[override-log.md](../portfolio/override-log.md): AVGO's 2026-06-16 override is still "Open — under review", no rationale supplied. Unchanged; outside `/rescore`'s scope. The user still owes a rationale for `decisions/`.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$321.68** | `yfinance` `currentPrice` = Fri 2026-10-23 close; `history()` Close 321.679993 agrees |
| `previousClose` | $323.24 | `yfinance` (Thu 10-22 close) |
| **Gap flag** | IBKR `get_price_snapshot` was **not available in this session** (no IBKR tools attached), so the 2-source IBKR cross-check used in prior sessions was not possible. Market is closed (Saturday), so the Friday close *is* the latest trade; only one source. Not an estimate — a sourced quote with a reduced cross-check. |
| 52-week range | $289.96 – $495.00 | `yfinance` |
| Analyst consensus PT | $529.10 | `yfinance` (vs. $531.31 on 10-12) |
| Price path | 10-12 $354.73 → 10-14 $346.25 → **10-16 $328.75** → 10-19 $334.59 → 10-22 $323.24 → 10-23 $321.68 |
| Move since last rescore | $355.04 → $321.68 = **−9.4%** | Below the 15% Rule 9 threshold. No company-specific filing explains it (no 8-K since 09-02; `yfinance` news feed returned nothing). Not diagnosed — treat as unexplained market move. |

---

## 2. Data Gathered — Sources & Gaps

| Metric | Value | Status |
|---|---|---|
| TTM Revenue / Net Income / GAAP EBIT | $89,104M / $38,265M / $42,814M | Carried forward (no new filing) |
| TTM FCF | $39,403M | Carried forward; matches `fetch_fundamentals` |
| **TTM SBC** | **$8,482M** (SBC/FCF 21.5%) | `fetch_fundamentals` SBC block (yfinance) — **new input this methodology** |
| TTM Gross Margin | 68.77% | Matches script |
| TTM EBITDA / Net Debt (Q3FY26) | $51,578M / $35,444M → 0.687× | Carried forward (script prints 0.937× on yfinance EBITDA $52,260M; AVGO's established basis kept for continuity) |
| Diluted shares | 4,887M | Carried forward; script's basic count is 4,773.6M (−2.3%) — same continuity flag as prior sessions |
| Forward EPS | **$19.4315** | `yfinance` (was $19.3938); consensus FY27 EPS growth **+66.7%** (49 analysts) |
| Forward PE | **16.555×** ($321.68 ÷ $19.4315) | matches script 16.555 |
| 5yr PE (reconstructed, n=20) | Avg 30.868×, Low 13.365×, High 52.758× | Unchanged vs 10-12 |
| Beta | 1.476 | `yfinance` |
| Dividend | $2.60/yr → 0.8083% | — |
| Gross cash buyback | ≈$8,446M TTM → 0.537% of mkt cap | `fetch_fundamentals` gross buyback yield 0.550% (basic-share basis) re-based to diluted market cap |
| VMware amortization add-back | $9.3B/yr, 21% normalized tax | Carried forward, flagged (2026-09-03 session) |

Nothing invented. **Basis note:** scored yields use the established diluted-share market cap ($321.68 × 4,887M = $1,572,050M); the script prints SBC yield 0.552% / FCF yield 2.566% on its basic-share market cap ($1,535,581M). Using diluted gives 0.540% / 2.506% — a 0.06pp difference in after-SBC yield (1.967% vs 2.014%), ~0.5 points of FCF_Score; kept for continuity with every prior AVGO session.

**`scripts.fetch_fundamentals AVGO` output (verbatim):**
```
Market Cap            = 1,535,581,224,960
Enterprise Value      = 1,571,025,190,912
Shares Outstanding    = 4,773,629,865
Forward PE            = 16.555
FCF Yield %           = 2.566
EV/EBIT               = 36.045
Net Margin %          = 42.944
Gross Margin %        = 68.770
ROIC % (NOPAT/InvCap) = 28.144  [tax_rate=0.0545, NOPAT=41,211,298,154, InvestedCapital=146,428,000,000]
Revenue 3yr CAGR %    = 24.378
Net Debt/EBITDA       = 0.937  [EBITDA_ttm=52,259,999,744]
FCF/NI TTM % (plain)  = 102.974
(FCF - SBC)/NI TTM %  = 80.808  [reported NI]
SBC yield %           = 0.552
Gross buyback yield % = 0.550
FCF/NI annual (oldest first) = [141.9%, 125.2%, 329.3%, 116.4%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 30.868 / 13.365 / 52.758  (n=20 quarters)

SBC block (TTM, advisory)
  SBC 8,482,000,000.0   FCF 39,403,000,000.0   Market cap 1,535,581,224,960.0
  SBC/FCF = 21.5%
  FCF yield (reported)  = 2.57%
  FCF yield after SBC   = 2.01%
Advisory flags
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
```

**Advisory flags — handling (no score effect):**
- `multiple_ceiling` (`flags_common --forward-pe 16.555 --eps-growth 30`): **NONE** (forward PE 16.6 < 30; the actual consensus growth, +66.7%, would not change that).
- `value_trap_candidate`: **UNKNOWN (data gap)** in the script, but not raised on its own terms: it requires forward PE ≤ 15 and negative TTM EPS growth; forward PE is 16.555 (> 15) and TTM diluted EPS has been rising (quarterly diluted EPS 0.85 → 1.74 → 1.50 → 1.91 → 2.68). Recorded as a data gap, not a pass.
- `cycle_peak`: **UNKNOWN (data gap)** — `yfinance` has only 5 quarters of diluted EPS (TTM now = 7.83; year-ago TTM unavailable), so the >100% growth test cannot be run and no estimate is made. Handling: `fast_grower` stays false (no 3-clean-year documentation; VMware-distorted base) so PEG is not used; the multiples are compared with AVGO's own 5yr range, not a cycle-peak-normalised base. **Caveat to carry:** the 16.6× forward PE rests on a consensus +66.7% EPS jump (FY26 $11.66 → FY27 $19.43) — the "cheapness" is a forecast-ramp, which is exactly what the flag exists to caution about. To close the gap, source year-ago TTM diluted EPS from the FY2025 10-K/10-Qs at the Q4 FY2026 rescore.

---

## 3. Quality Score (Phase 01 gate)

Hard disqualifiers: plain FCF/NI annual [141.9, 125.2, 329.3, 116.4] — none <70% (PASS); **SBC $8,482M = 21.5% of FCF $39,403M, <100% (PASS — new check)**; Net Debt/EBITDA 0.687× ≤ 2.5× (PASS); FCF-positive 3+ yrs (PASS). Inputs (`q.json`) identical to 2026-10-12 except the new SBC fields.

**`scripts.scoring.quality_score` output (verbatim):**
```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((42.944/30)x100) = 100.00
ROIC_Component = clamp((30.47/30)x100) = 100.00
Profitability_Score = (100.00 + 100.00) / 2 = 100.00

**Margins (15%)**
GrossMargin_Score = clamp((68.77/80)x100) = 85.96

**Growth (20%)**
Growth_Score = clamp((24.378/25)x100) = 97.51
+10 TAM/pricing-power evidence: Carried forward from prior AVGO sessions: custom AI accelerator demand from hyperscalers, VMware private cloud TAM; no new evidence (no 8-K since 2026-09-02).
Growth_Score (final, clamped) = 100.00

**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - 0.687/4)) = 82.82

**Moat Signal (15%)**
| market_share_stable_or_growing | True | Carried forward: AVGO custom AI ASIC share with hyperscaler partners (Google TPU, Meta) documented in prior sessions. |
| brand_premium | False | No consumer brand premium; B2B vendor. |
| network_effect | False | No direct network effect identified. |
| switching_costs | True | Carried forward: VMware enterprise virtualization switching costs, custom ASIC design-win lock-in. |
| scale_cost_advantage | False | Not established as distinct moat signal in prior sessions (kept conservative). |
Moat_Score = (2/5) x 100 = 40.00

**FCF Quality (10%)**
FCFQuality_Score = clamp(((0.8081 - 0.40)/0.60)x100) = 68.01  [ratio = (FCF - SBC)/NI]

Quality Score = (100.00x0.25) + (85.96x0.15) + (100.00x0.20) + (82.82x0.15) + (40.00x0.15) + (68.01x0.10)
= 83.119 -> rounds to 83.1

# Quality Score = 83.1 — PASSES the 80.0+ gate
```
**Quality 86.3 → 83.1 is a pure methodology effect** (FCF Quality 100.0 → 68.0 on the SBC deduction; every other component identical). Still passes the 80.0 gate with 3.1 points of headroom — thinner than before: the Moat component (40.0) is the conservative drag, and all else equal, (FCF−SBC)/NI would have to fall from 80.8% to below ~62% to breach the gate. **Not below 80.0 → no Phase 04 Quality Watch escalation.**

---

## 4. Rate Environment Gate

```
Forward PE = 321.68 / 19.4315 = 16.555×  →  EY = 6.0405%
Spread = EY − 10Y = 6.0405% − 4.988% = +1.0525pp
```
Step 1: spread < +1.5pp → **+5**. Step 2: 10Y 4.988% (3.5–5%) → **+5**. **Combined Rate Modifier: +10** (down from +15). The 10Y is only **1.2bp under the 5% line** — a close back above 5% restores +15 (see §7 sensitivity).

---

## 5. Valuation Score (Phase 02)

Inputs: FCF yield (reported) = $39,403M ÷ $1,572,050M = 2.5063%; SBC yield = $8,482M ÷ $1,572,050M = 0.5395%. EV = $1,572,050M + $35,444M = $1,607,494M → EV/EBIT (GAAP $42,814M) = **37.55×** (normalized EBIT $52,114M → 30.85×; GAAP basis scored, as in every prior AVGO session). Scenario fair values: NTM EPS $19.4315 × {1.10 × 34× bull, 1.00 × 25× base, 0.85 × 15× bear} = **$726.74 / $485.79 / $247.75** (same architecture since 2026-07-04). Catalyst window 1.11yr (1.14 on 10-12 less 12 days; management's FY2027 AI-semiconductor target >$100B). Intrinsic growth 12.0% (carried), dividend 0.8083%, gross cash buyback 0.537%.

**`scripts.scoring.valuation_score` output (verbatim):**
```
## Valuation Score

**FCF Yield (40%)**
FCF yield after SBC = 2.5063% - 0.5395% (SBC yield) = 1.9668%
FCF_Score = clamp(100x(1 - 1.9668/10)) = 80.332

**EV/EBIT**
EV/EBIT_Score = clamp((37.5481 - 12)/23 x 100) = 100.000

**Forward PE**
FwdPE_Score (raw) = clamp((16.555 - 13.365)/(52.758 - 13.365) x 100) = 8.098
Deviation vs 5yr avg (30.868) = (16.555 - 30.868)/30.868 x 100 = -46.368%
Historical PE Modifier: >20% below 5yr avg -> -10
FwdPE_Score = clamp(8.098 + -10) = 0.000

**PEG**
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT

**Rate Environment Gate**
EY = 1/16.555 x 100 = 6.0405%
Spread = EY - 10Y (4.988%) = 1.0525pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 4.988% -> Step 2 bracket modifier = +5
Total Rate Modifier = 5 + 5 = +10

**Upside/Downside Modifier**
PW Fair Value = 0.25x726.74 + 0.50x485.79 + 0.25x247.75 = 486.5175
Gap Upside % = (486.5175/321.68) - 1 = 51.2427%
Annualized gap = 51.2427% / 1.11yr = 46.1646%/yr
E = 46.1646 (annualized gap) + 12.0 (intrinsic growth) + 1.3453 (shareholder yield: 0.8083 div + 0.537 buyback) = 59.5099%/yr
E (59.5099%) >= H (10.0%) -> M = -15 x clamp((59.5099-10.0)/15, 0, 1) = -15.0000
Upside/Downside Modifier (bounded [-15, +15]) = -15.0000

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 72.133

**Final Valuation Score**
Final Score = Raw (72.133) + Rate Modifier (+10) + Upside/Downside Modifier (-15.000)
= 67.133 -> rounds to 67.1

# Valuation Score = 67.1
```
**Valuation Score 71.4 → 67.1.** Drivers: Rate Modifier +15 → +10 (−5.0); FCF_Score 77.3 → 80.3 on the SBC deduction (+1.2 weighted) offset by FwdPE_Score 2.5 → 0.0 (−0.5); EV/EBIT saturated at 100 in both. Raw 71.4 → 72.1; the net move is the rate gate. Still in the raw 60.0–69.9 band; the **Composite governs the action**.

---

## 6. Composite Score

```
## Composite Score
Composite Score = 0.50x(100 - 83.1) + 0.50x67.1 = 42.000 -> rounds to 42.0
# Composite Score = 42.0
(Quality Score 83.1, Valuation Score 67.1)
```
**Composite 42.0 — "Cheap" band (30.0–49.9)**, vs. 42.6 on 10-12 (Quality −3.2 → +1.6 to composite; Valuation −4.3 → −2.15).

**Sensitivities (shown, not scored):**
- *EV/EBIT on normalized EBIT (30.85×)*: EV/EBIT_Score 100 → 82.0, Valuation 59.9, Composite 38.4. Same band, same action. (The GAAP-vs-normalized basis note from 10-12 now moves the score by 7 points but not the action band — no `decisions/` note triggered.)
- *10Y back at ≥5.0%*: Rate Modifier +15 → Valuation 72.1, Composite 44.5. Same band.

---

## 7. Action Recommendation & Order Setup

### Fair Value (Rule 1: Tech/Growth → DCF primary, multiples secondary; Rule 3 weights 40/60)

**3-stage DCF** (reported-FCF base, as in all prior AVGO sessions — fair-value-methodology.md has no SBC step):
```
Cost of equity = 4.988% + 1.476 × 5.0% (assumed ERP) = 12.368%
Cost of debt = $3,116M / $59,419M = 5.244% pretax → 4.143% after 21% tax
Weights: E = 96.358% (mkt cap $1,572,050M), D = 3.642%
WACC = 12.068%

Stage 1 FCF (base $39,403M): y1 +25% $49,253.8M | y2 +20% $59,104.5M | y3 +15% $67,970.2M | y4 +12% $76,126.6M | y5 +10% $83,739.3M
Stage 2 (growth fading 8.5/7.0/5.5/4.0/2.5%): y6 $90,857.1M | y7 $97,217.1M | y8 $102,564.0M | y9 $106,666.6M | y10 $109,333.3M
Terminal value (g = 2.5%) = $1,171,211M; PV of TV = $374,802M (46.1% of DCF EV — under the 75% cap)
PV of FCFs yrs 1–10 = $439,049M
EV (DCF) = $813,851M; less Net Debt $35,444M = Equity $778,407M ÷ 4,887M sh = $159.28/sh
```
(DCF $154.25 → $159.28: WACC 12.339% → 12.068% on the lower 10Y.) *Sensitivity only:* on an SBC-deducted FCF base ($30,921M) the same stages give $123.43/sh — not used because the methodology defines no SBC step in the DCF, but it shows the DCF leg is roughly $36 lower than shown.

**Scenario-weighted multiples:** PW Fair Value **$486.52** (§5).
**Blended (40/60):** 0.40 × $159.28 + 0.60 × $486.52 = **$355.62**. The price ($321.68) is now **9.5% below** blended fair value (was ≈ equal on 10-12) — the move is price, not fundamentals. Same material tension as every prior AVGO session: DCF $159 vs. multiples $487; the blend leans on the multiples leg.

### Order setup (`scripts.scoring.order_setup`, MoS 27.5% / stop 27.5%, portfolio value $47,820.23 — 2026-10-18 sync)
```
Band: 30.0-49.9 (Set limit order)
Buy Price = Fair Value (355.62) x (1 - 27.5%) = 257.8245
Live price 321.68 vs buy price ceiling 257.8245 -> limit order at buy price (live price above ceiling); entry price used = 257.8245
Primary Sell Target = Fair Value = 355.6200
Bull-Case Trim Target = Bull FV (726.74) x 0.90 = 654.0660
Stop Loss = Entry Price (257.8245) x (1 - 27.5%) = 186.9228
R/R Ratio = (Sell Target 355.6200 - Entry 257.8245) / (Entry 257.8245 - Stop 186.9228) = 97.7955/70.9017 = 1.3793:1
*** FLAG: R/R 1.3793:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = Portfolio Value (47820.23) x 1.5% = 717.3034
Risk Per Share = Entry (257.8245) - Stop (186.9228) = 70.9017
Shares by risk-based sizing = 717.3034 / 70.9017 = 10.1169
Allocation cap = Portfolio Value (47820.23) x 5% = 2391.0115 -> 9.2738 shares
Position Size (shares) = min(risk-based, cap) = 9.2738  [binding: allocation cap]
Position Size ($) = 9.2738 x 257.8245 = 2391.0115
Current shares held = 6; gap vs. target = 3.2738
```
**Full MoS/stop matrix (R/R):**

| MoS \ Stop | 25% | 30% |
|---|---|---|
| 25% | 1.33:1 | 1.11:1 |
| 30% | **1.71:1** | 1.43:1 |

Best case 1.71:1 fails the 2:1 minimum across the whole authorized range — identical to every AVGO rescore since 2026-09-15 (the ratio depends only on MoS/stop, not on fair value). No order per Step 6.

### Net action: **HOLD** — keep the 6 shares; no add, no trim

- No trim: Composite 42.0 is far below the 70.0+ trim band; price move alone is not a trigger (Rule 9: −9.4% < 15%).
- No add: R/R fails 2:1 at every authorized combination; the position (4.04%) is already inside its 3–5% band. A 7th share would be ~4.7% — in band, but there is no sized order to place because the framework's entry price ($257.82) is $64 below market and the R/R gate fails.
- Position is at a **−15.9% unrealized loss** vs avg cost $382.44 (override entry of 2026-06-16); that is not a framework trigger (no stop is set for an override position by any rule; a Rule-9 fundamental event would be). Reported for awareness only.
- The open 2026-06-16 override remains unresolved (§0).

---

## 8. Next Review Trigger

**Q4 FY2026 earnings (expected ~December 2026)** — re-run Phase 01/02 with refreshed TTM figures. First checks:
1. **Close the `cycle_peak` data gap** — pull year-ago TTM diluted EPS from filings (§2).
2. **10Y at the 5% line** — 4.988% now; ≥5.0% restores the +15 modifier (Valuation ≈72.1 / Composite ≈44.5 — same action).
3. **Unexplained −9.4% drawdown** — earlier Rule 9 rescore if the price moves >15% from this session's $321.68 (below ≈$273 or above ≈$370) or any guidance/M&A/management event appears.
4. **DCF/multiples gap** and **SBC-deducted DCF ($123 vs $159)** remain the weakest-supported fair-value inputs.

Separately and unconditionally: the 2026-06-16 override still needs the user's rationale.

---

## Glossary

- **8-K / 10-Q**: Current report of a material event / quarterly financial report, both filed with the SEC.
- **Advisory flag**: A warning printed during analysis (cycle peak, multiple ceiling, value trap) that forces a written explanation but changes no score.
- **Beta**: A stock's sensitivity to overall market moves; an input to the cost of equity in WACC.
- **CAGR**: Compound Annual Growth Rate.
- **Catalyst window**: Time within which a documented event is expected to close the price/fair-value gap.
- **Composite Score**: `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` (0 = most attractive); computed only after clearing the 80.0+ quality gate.
- **Cycle peak**: Top of a business cycle, when earnings are temporarily inflated so a multiple looks cheapest exactly when it is most dangerous.
- **DCF (Discounted Cash Flow)**: Valuation by projecting future cash flows and discounting them to today.
- **EBIT / EBITDA**: Earnings before interest and taxes / before interest, taxes, depreciation and amortization.
- **EV / EV/EBIT**: Enterprise Value (market cap + debt − cash) / EV divided by EBIT.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against bond yields in the Rate Environment Gate.
- **FCF / FCF Yield / FCF/NI conversion**: Free cash flow; FCF ÷ market cap; FCF ÷ net income (cash-quality check).
- **Fair Value (FV)**: Analyst's estimate of intrinsic worth, independent of market price.
- **Forward PE**: Price ÷ next-twelve-months expected EPS.
- **Hard disqualifier**: A quality condition that fails a company regardless of its weighted score.
- **Hurdle rate**: Minimum acceptable annual return (10%) used by the Upside/Downside Modifier.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set.
- **Moat**: Durable competitive advantage protecting profits.
- **Net Debt/EBITDA**: Leverage ratio — the framework's main balance-sheet-risk gate.
- **NOPAT / ROIC**: After-tax operating profit; return on invested capital.
- **PW (Probability-Weighted) Fair Value**: 25% bull + 50% base + 25% bear.
- **Quality Score**: 0–100.0 (higher = better) grade of profitability, margins, growth, balance sheet, moat and FCF quality; 80.0+ required.
- **Rate Environment Gate / Rate Regime Modifier**: Pre-score check of earnings yield versus the 10Y Treasury and the resulting additive adjustment.
- **R/R (Risk/Reward)**: Expected gain ÷ expected loss; the framework requires at least 2:1 to enter.
- **SBC (Stock-Based Compensation)**: Pay in shares/options; treated as a real cost (dilution) in both Valuation and Quality since methodology 2026-10-12.
- **Shareholder yield**: Dividend yield plus gross cash buyback yield.
- **TAM**: Total Addressable Market.
- **Terminal Value**: Lump-sum value of all cash flows beyond the explicit forecast period.
- **TTM**: Trailing Twelve Months.
- **Upside/Downside Modifier**: Additive ±15 adjustment from expected annual return versus the 10% hurdle.
- **Valuation Score**: 0–100.0 (lower = cheaper) combining FCF yield, EV/EBIT, Forward PE, Rate Gate and the Upside/Downside Modifier.
- **Value trap**: A stock that looks cheap only because its earnings are falling.
- **WACC**: Weighted Average Cost of Capital — the DCF discount rate.

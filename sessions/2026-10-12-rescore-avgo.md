# RESCORE — AVGO (Broadcom Inc.) — 2026-10-12

**Task type:** RESCORE (mode `--both`)
**Trigger:** User-requested fresh rescore, 14 days after the 2026-09-28 session — not tied to a new earnings event. No 8-K newer than the 2026-09-02 Q3 FY2026 earnings filing (re-verified against SEC EDGAR's 8-K index for CIK 0001730168: latest remains 2026-09-02, then 2026-07-06). TTM/balance-sheet inputs are therefore carried forward unchanged; only live-price-dependent inputs, the 10Y yield, forward EPS, beta and the 5yr PE range are refreshed.
**Date:** 12 Oct 2026
**10Y US Treasury Yield:** **5.24%** (`yfinance` `^TNX` close 2026-10-12 = 5.240; consistent with the 5.24% cited in the 2026-10-11 ZS rescore). Up from 5.21% on 2026-09-28; still in the >5% bracket (third consecutive rescore).
**Rate Regime Modifier (Step 2):** **+10**
**Current AVGO position:** 6 sh, 4.47% of framework account U19421206 Net Liquidation ($48,635.06) per the 2026-10-12 sync ([holdings.md](../portfolio/holdings.md)). Weight rose from 3.43% purely because RGL/LM8/TLT left the account in-kind (smaller denominator), not because of a trade.
**Sector:** Semiconductors (fabless — AI accelerators/networking) + Infrastructure Software (VMware)
**Last review:** 28 Sep 2026 (Valuation 71.3 / Quality 86.3 / Composite 42.5) — [session](2026-09-28-rescore-avgo.md)

---

## 0. Override status (reported, not resolved)

[override-log.md](../portfolio/override-log.md): AVGO's 2026-06-16 override is still marked "Open — under review," no rationale supplied. Unchanged; outside `/rescore`'s scope. The user still owes a rationale for `decisions/`.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$355.04** | IBKR `get_price_snapshot` (contract_id 313130367), last trade ts 1791830246, bid 355.00 / ask 355.10 |
| Cross-check | $355.05 | `yfinance` `currentPrice` — within 0.01% |
| `yfinance` `previousClose` | $361.54 | Prior-session close; intraday move ≈ −1.8%, unremarkable |
| 52-week range | $289.96 – $495.00 | `yfinance` |
| Analyst consensus PT | $531.31 (47 analysts) | `yfinance` `targetMeanPrice` — vs. $531.85 on 2026-09-28 |
| Move since last rescore | $352.39 → $355.04 = **+0.75%** | Far below the 15% Rule 9 threshold |

---

## 2. Data Gathered — Sources & Gaps

| Metric | Value | Status |
|---|---|---|
| TTM Revenue / Net Income / GAAP EBIT | $89,104M / $38,265M / $42,814M | Carried forward (no new filing) |
| TTM FCF | $39,403M | Carried forward |
| TTM Gross Margin | 68.77% | Carried forward / matches script |
| TTM Interest Expense | $3,116M | Carried forward |
| TTM EBITDA | $51,578M | Carried forward |
| Net Debt (Q3FY26, 2 Aug 2026) | $35,444M → Net Debt/EBITDA 0.687× | Carried forward |
| Total Debt / Equity / Cash | $59,419M / $99,690M / $23,975M | Carried forward |
| Diluted shares (GAAP basis) | 4,887M | Carried forward; used consistently across all AVGO sessions. `yfinance` basic count is 4,773.6M (~2.3% lower) — noted, not blended in (continuity flag from 2026-09-15). |
| Forward EPS | **$19.3938** (`yfinance` `forwardEps` 19.39382) | Refreshed (vs. $19.381 on 2026-09-28) |
| Forward PE | **18.307×** ($355.04 ÷ $19.39382) | Refreshed (script's own 18.305× uses its own price timestamp) |
| 5yr PE range (reconstructed, n=20 quarters) | Avg **30.868×**, Low 13.365×, High 52.758× | Refreshed via `scripts.fetch_fundamentals` (avg 29.892× on 2026-09-28; drift from the rolling window and price) |
| Beta | 1.476 | `yfinance` (was 1.457) |
| Dividend | $2.60/yr annualized ($0.65/qtr) | Unchanged |
| VMware/intangible amortization add-back | $9.3B/yr, effective tax 21% normalized | Carried forward, flagged (see 2026-09-03 session) |

No metric was invented or estimated. Every refreshed figure traces to IBKR, `yfinance` or SEC EDGAR; every carried-forward figure is flagged with the reason it was not re-derived (no newer filing exists).

**`scripts.fetch_fundamentals AVGO` output (verbatim):**
```
Market Cap            = 1,694,686,380,032
Enterprise Value      = 1,761,302,151,168
Shares Outstanding    = 4,773,629,865
Forward PE            = 18.305
FCF Yield %           = 2.325
EV/EBIT               = 40.411
Net Margin %          = 42.944
Gross Margin %        = 68.770
ROIC % (NOPAT/InvCap) = 28.144  [tax_rate=0.0545, NOPAT=41,211,298,154, InvestedCapital=146,428,000,000]
Revenue 3yr CAGR %    = 24.378
Net Debt/EBITDA       = 0.937  [EBITDA_ttm=52,259,999,744]
FCF/NI TTM %          = 102.974
FCF/NI annual (oldest first) = [141.9%, 125.2%, 329.3%, 116.4%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 30.868 / 13.365 / 52.758  (n=20 quarters)
```
As in prior sessions, the script's own Market Cap/EV/ROIC/EV-EBIT use `yfinance`'s basic share count and its own ~5.45% tax estimate. The framework's established basis (4,887M diluted shares, 21% normalized tax, $9.3B amortization add-back) is used for the scored figures below; the script's Net Margin, Gross Margin, Revenue CAGR, FCF/NI and 5yr PE lines are used directly.

---

## 3. Quality Score (Phase 01 gate)

**Hard disqualifiers (unchanged):** FCF/NI TTM 102.97% (PASS, not <70% for 2+ yrs); Net Debt/EBITDA 0.687× (PASS, ≤2.5×); FCF-positive 3+ consecutive years (PASS).

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
| Signal | True | Evidence |
| market_share_stable_or_growing | True | Carried forward: AVGO custom AI ASIC share with hyperscaler partners (Google TPU, Meta) documented in prior sessions. |
| brand_premium | False | No consumer brand premium; B2B vendor. |
| network_effect | False | No direct network effect identified. |
| switching_costs | True | Carried forward: VMware enterprise virtualization switching costs, custom ASIC design-win lock-in. |
| scale_cost_advantage | False | Not established as distinct moat signal in prior sessions (kept conservative). |
Moat_Score = (2/5) x 100 = 40.00

**FCF Quality (10%)**
FCFQuality_Score = clamp(((1.0297 - 0.40)/0.60)x100) = 100.00

Quality Score = (100.00x0.25) + (85.96x0.15) + (100.00x0.20) + (82.82x0.15) + (40.00x0.15) + (100.00x0.10)
= 86.318 -> rounds to 86.3

# Quality Score = 86.3 — PASSES the 80.0+ gate
```
ROIC 30.47% = normalized EBIT $52,114M × (1 − 21%) = NOPAT $41,170.1M ÷ invested capital $135,134M (debt $59,419M + equity $99,690M − cash $23,975M) — carried forward. **Quality Score = 86.3, identical to 2026-09-28**, as expected with no new filing. Gate clearance is comfortable (sensitivity: even Moat_Score = 0 gives 80.3, still clears). No new TAM/pricing-power or moat evidence surfaced.

---

## 4. Rate Environment Gate

```
Forward PE = 355.04 / 19.39382 = 18.307×  →  EY = 5.4624%
Spread = EY − 10Y = 5.4624% − 5.24% = +0.2224pp
```
Step 1: spread < +1.5pp → fails → **+5**. Step 2: 10Y 5.24% (>5%) → **+10**. **Combined Rate Modifier: +15** (unchanged). Spread narrowed again (0.29pp → 0.22pp).

---

## 5. Valuation Score (Phase 02)

Inputs: FCF Yield = $39,403M ÷ market cap $1,735,080.5M ($355.04 × 4,887M) = 2.2710%. EV/EBIT = ($1,735,080.5M + $35,444M) ÷ $42,814M = 41.354× (GAAP; normalized EBIT $52,114M gives **33.97×**, now only 1.03× below the 35× ceiling — see §8). Scenario fair values: NTM EPS $19.39382 × {1.10 × 34× bull, 1.00 × 25× base, 0.85 × 15× bear} = **$725.33 / $484.85 / $247.27** (same architecture as every AVGO session since 2026-07-04). Catalyst: management's FY2027 AI-semiconductor revenue target (>$100B), window **1.14yr** (1.18yr on 09-28 less 14 days). Intrinsic growth 12.0% and zero net buyback carried forward; dividend yield $2.60 ÷ $355.04 = 0.7323%.

**`scripts.scoring.valuation_score` output (verbatim):**
```
## Valuation Score

**FCF Yield (40%)**
FCF_Score = clamp(100x(1 - 2.27096/10)) = 77.290

**EV/EBIT**
EV/EBIT_Score = clamp((41.3539 - 12)/23 x 100) = 100.000

**Forward PE**
FwdPE_Score (raw) = clamp((18.3069 - 13.365)/(52.758 - 13.365) x 100) = 12.545
Deviation vs 5yr avg (30.868) = (18.3069 - 30.868)/30.868 x 100 = -40.693%
Historical PE Modifier: >20% below 5yr avg -> -10
FwdPE_Score = clamp(12.545 + -10) = 2.545

**PEG**
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT

**Rate Environment Gate**
EY = 1/18.3069 x 100 = 5.4624%
Spread = EY - 10Y (5.24%) = 0.2224pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.24% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15

**Upside/Downside Modifier**
PW Fair Value = 0.25x725.33 + 0.50x484.85 + 0.25x247.27 = 485.5750
Gap Upside % = (485.5750/355.04) - 1 = 36.7663%
Annualized gap = 36.7663% / 1.14yr = 32.2511%/yr
E = 32.2511 (annualized gap) + 12.0 (intrinsic growth) + 0.7323 (shareholder yield: 0.7323 div + 0 buyback) = 44.9834%/yr
E (44.9834%) >= H (10.0%) -> M = -15 x clamp((44.9834-10.0)/15, 0, 1) = -15.0000
Upside/Downside Modifier (bounded [-15, +15]) = -15.0000

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 71.425

**Final Valuation Score**
Final Score = Raw (71.425) + Rate Modifier (+15) + Upside/Downside Modifier (-15.000)
= 71.425 -> rounds to 71.4

# Valuation Score = 71.4
```
**Valuation Score = 71.4** — raw "TRIM 25–30%" band (70.0–79.9), essentially flat vs. 71.3. As in the last three sessions, the **Composite Score** (not the raw Valuation Score) governs the action table. The +15 rate modifier and −15 expected-return modifier fully offset.

---

## 6. Composite Score

**`scripts.scoring.composite_score` output (verbatim):**
```
## Composite Score

Composite Score = 0.50x(100 - 86.3) + 0.50x71.4 = 42.550 -> rounds to 42.6

# Composite Score = 42.6
(Quality Score 86.3, Valuation Score 71.4)
```
**Composite 42.6 — "Cheap" band (30.0–49.9)**, vs. 42.5 on 2026-09-28. Note the exact value is 42.550 and the ".X5 rounds up" rule applies.

---

## 7. Action Recommendation & Order Setup

### Fair Value (Rule 1: Tech/Growth → DCF primary, multiples secondary; Rule 3 weights 40/60)

**3-stage DCF:**
```
Cost of equity = 5.24% + 1.476 × 5.0% (assumed ERP) = 12.620%
Cost of debt = $3,116M / $59,419M = 5.244% pretax → 4.143% after 21% tax
Weights: E = 96.689% (mkt cap $1,735,080M), D = 3.311%
WACC = 12.339%

Stage 1 FCF (base $39,403M): y1 +25% $49,253.8M | y2 +20% $59,104.5M | y3 +15% $67,970.2M | y4 +12% $76,126.6M | y5 +10% $83,739.3M
Stage 2 (growth fading 8.5/7.0/5.5/4.0/2.5%): y6 $90,857.1M | y7 $97,217.1M | y8 $102,564.0M | y9 $106,666.6M | y10 $109,333.3M
Terminal value (g = 2.5%) = $1,138,968M; PV of TV = $355,790M (45.1% of DCF EV — under the 75% cap)
PV of FCFs yrs 1–10 = $433,497M
EV (DCF) = $789,288M; less Net Debt $35,444M = Equity $753,844M ÷ 4,887M sh = $154.25/sh
```
(DCF $154.25 vs. $156.56 on 2026-09-28: WACC 12.216% → 12.339% on the higher 10Y and beta.)

**Scenario-weighted multiples:** PW Fair Value **$485.58** (§5).

**Same material tension as prior sessions:** DCF $154 vs. multiples $486 — a GDP-terminal-growth DCF versus AVGO's own 5yr PE range. Blended (40/60): 0.40 × $154.25 + 0.60 × $485.58 = **$353.05**. This is roughly equal to the live price ($355.04), i.e. at the blended level the stock is fairly valued, not cheap — the "Cheap" composite band rests on the multiples leg and the expected-return modifier.

### Order setup (`scripts.scoring.order_setup`, MoS 27.5% / stop 27.5% — midpoint of Cheap band; portfolio value $48,635.06)
```
Band: 30.0-49.9 (Set limit order)
Buy Price = Fair Value (353.05) x (1 - 27.5%) = 255.9613
Live price 355.04 vs buy price ceiling 255.9613 -> limit order at buy price (live price above ceiling); entry price used = 255.9613
Primary Sell Target = Fair Value = 353.0500
Bull-Case Trim Target = Bull FV (725.33) x 0.90 = 652.7970
Stop Loss = Entry Price (255.9613) x (1 - 27.5%) = 185.5719
R/R Ratio = (Sell Target 353.0500 - Entry 255.9613) / (Entry 255.9613 - Stop 185.5719) = 97.0888/70.3893 = 1.3793:1
*** FLAG: R/R 1.3793:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = Portfolio Value (48635.06) x 1.5% = 729.5259
Risk Per Share = Entry (255.9613) - Stop (185.5719) = 70.3893
Shares by risk-based sizing = 729.5259 / 70.3893 = 10.3642
Allocation cap = Portfolio Value (48635.06) x 5% = 2431.7530 -> 9.5005 shares
Position Size (shares) = min(risk-based, cap) = 9.5005  [binding: allocation cap]
Position Size ($) = 9.5005 x 255.9613 = 2431.7530
Current shares held = 6; gap vs. target = 3.5005
```
**Full MoS/stop matrix:**

| MoS \ Stop | 25% | 30% |
|---|---|---|
| 25% | 1.33:1 | 1.11:1 |
| 30% | **1.71:1** | 1.43:1 |

Best case 1.71:1 fails the 2:1 minimum across the whole applicable range — same as 2026-09-15 and 2026-09-28. Per fair-value-methodology.md Step 6, no order is placed. (Sizing is also moot: 6 sh ≈ $2,130 is ~4.4% at today's price on the $48,635 base, inside the 3–5% band; the 9.5-share figure would be a ~$3.5-share top-up at a $256 limit far below market.)

### Net action: **HOLD** — keep the 6 shares; no add, no trim

- No trim: Composite 42.6 is far below the 70.0+ trim band.
- No add: R/R fails 2:1 throughout, and the position is already inside its 3–5% band.
- Context only (not a rule trigger): the weight rose from 3.43% to 4.47% via account segregation; at the 5% cap the position would be ~$2,432 ≈ 6.85 sh, so AVGO has ~0.8 sh of headroom — a 7th share is not recommended given the R/R fail.
- The open 2026-06-16 override remains unresolved (§0).

---

## 8. Next Review Trigger

**Q4 FY2026 earnings (expected ~December 2026)** — re-run Phase 01/02 with refreshed TTM figures. Follow-ups to check first:
1. **EV/EBIT basis divergence** — normalized EV/EBIT is now 33.97× (33.72× on 09-28), only ~1× under the 35× ceiling; GAAP EV/EBIT already saturates the sub-score at 100.0. Once normalized also saturates, the basis choice stops mattering for the score; still worth a `decisions/` note if it ever moves the action band.
2. **10Y regime** — above 5% for three consecutive rescores (5.24% now). A fall back below 5% would cut the Rate Modifier to +5 and the raw Valuation Score to ~66–67, all else equal; not itself an early-rescore trigger.
3. **Blended FV ≈ live price** — DCF/multiples gap remains the framework's weakest-supported input for this name.

Earlier trigger on a >15% unexplained move from $355.04 (Rule 9), a guidance revision/M&A/management change, or new third-party market-share data. Separately and unconditionally: the 2026-06-16 override still needs the user's rationale.

---

## Glossary

- **8-K**: A US company's "current report" filed with the SEC to disclose a material event between regular filings.
- **Beta**: A stock's sensitivity to overall market moves; an input to the cost of equity in WACC.
- **bps / pp**: Basis points (0.01 percentage points) / percentage points.
- **CAGR**: Compound Annual Growth Rate.
- **Catalyst window**: Time within which a documented event is expected to close the price/fair-value gap.
- **Composite Score**: `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` (0 = most attractive); computed only after clearing the 80.0+ quality gate.
- **DCF (Discounted Cash Flow)**: Valuation by projecting future cash flows and discounting them to today.
- **EBIT / EBITDA**: Earnings before interest and taxes / before interest, taxes, depreciation and amortization.
- **Equity Risk Premium (ERP)**: Extra return equity investors demand over the risk-free rate; an assumed DCF input.
- **EV / EV/EBIT**: Enterprise Value (market cap + debt − cash) / EV divided by EBIT.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against bond yields in the Rate Environment Gate.
- **FCF / FCF Yield / FCF/NI conversion**: Free cash flow; FCF ÷ market cap; FCF ÷ net income (cash-quality check).
- **Forward PE**: Price ÷ next-twelve-months expected EPS.
- **Fair Value (FV)**: Analyst's estimate of intrinsic worth, independent of market price.
- **Hard disqualifier**: A quality condition that fails a company regardless of its weighted score.
- **Human Override**: A position held outside the framework's rules, tracked in `override-log.md`.
- **Hurdle rate**: Minimum acceptable annual return (10%) used by the Upside/Downside Modifier.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set.
- **Moat**: Durable competitive advantage protecting profits.
- **Net Debt/EBITDA**: Leverage ratio — the framework's main balance-sheet-risk gate.
- **NOPAT / ROIC / Invested Capital**: After-tax operating profit; return on invested capital; debt + equity − cash.
- **PW (Probability-Weighted) Fair Value**: 25% bull + 50% base + 25% bear.
- **Quality Score**: 0–100.0 (higher = better) grade of profitability, margins, growth, balance sheet, moat and FCF quality; 80.0+ required.
- **Rate Environment Gate / Rate Regime Modifier**: Pre-score check of earnings yield versus the 10Y Treasury and the resulting additive adjustment.
- **R/R (Risk/Reward)**: Expected gain ÷ expected loss; the framework requires at least 2:1 to enter.
- **TAM**: Total Addressable Market.
- **Terminal Value**: Lump-sum value of all cash flows beyond the explicit forecast period.
- **TTM**: Trailing Twelve Months.
- **Upside/Downside Modifier**: Additive ±15 adjustment from expected annual return versus the 10% hurdle.
- **Valuation Score**: 0–100.0 (lower = cheaper) combining FCF yield, EV/EBIT, Forward PE, Rate Gate and the Upside/Downside Modifier.
- **WACC**: Weighted Average Cost of Capital — the DCF discount rate.

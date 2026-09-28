# RESCORE — AVGO (Broadcom Inc.) — 2026-09-28

**Task type:** RESCORE (mode `--both`)
**Trigger:** User-requested fresh rescore, 13 days after the 2026-09-15 session — not tied to a new earnings event. TTM/fundamental inputs carried forward unchanged (no new 8-K since 2026-09-02, re-verified directly against SEC EDGAR's 8-K filing index for CIK 0001730168 — the 2026-09-02 Q3 FY2026 earnings 8-K remains the most recent filing).
**Date:** 28 Sep 2026
**10Y US Treasury Yield:** **5.21%** (WebSearch cross-check, dated 28 Sep 2026 — "rose to 5.21% on September 28, 2026, marking a 0.05pp increase from the previous session"; cross-checked against TradingEconomics' live quote of 5.23%, within 0.02pp, immaterial) — up further from 5.018% on 2026-09-15, continuing the regime shift first flagged that session.
**Rate Regime Modifier (Step 2):** **+10** (10Y still in the >5% bracket, unchanged from 2026-09-15)
**Current AVGO portfolio weight:** 3.43% per [holdings.md](../portfolio/holdings.md) (2026-09-27 sync; not re-synced this session — refreshing live weight is `/sync-portfolio`'s job, out of `/rescore`'s scope) — still held as an **open, unresolved Human Override**
**Sector:** Semiconductors (fabless — AI accelerators/networking) + Infrastructure Software (VMware)
**Last review:** 15 Sep 2026 (Valuation 70.9 / Quality 86.3 / Composite 42.3) — see [session](../sessions/2026-09-15-rescore-avgo.md)

---

## 0. Override status (reported, not resolved this session)

Per [override-log.md](../portfolio/override-log.md): AVGO's **2026-06-16 override remains open** — still "Open — under review," no rationale supplied. Unchanged since the last session. Not this command's scope to resolve. (Also still carried forward in [holdings.md](../portfolio/holdings.md) as a housekeeping item marked "Open — under review" despite the framework having re-evaluated the position multiple times since.)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$352.39** | IBKR `get_price_snapshot` (contract_id 313130367, NASDAQ), **REALTIME** status, ts 2026-09-28 13:42:47 UTC — during regular NASDAQ trading hours (opens 13:30 UTC / 9:30am ET), not a pre-market quote. Cross-validated against `yfinance`'s `currentPrice` field, reading **$352.875** — within 0.14%, immaterial. |
| `change` field (IBKR) | −$0.42 (−0.12%) vs. prior close | IBKR `get_price_snapshot` |
| `yfinance` `previousClose` | $352.81 | Confirms a small, unremarkable intraday move — no gap event. |
| 52-week range | $289.48 – $494.23 (IBKR `misc_statistics`) | Essentially unchanged from the 2026-09-15 session ($289.96–$495.00; rolling-window drift). |
| Analyst consensus PT | $531.85 (`yfinance`, 47 analysts) — unchanged from the 2026-09-15 session | No new analyst-revision news surfaced this session. |
| Move since last rescore | $345.55 (15 Sep) → $352.39 (28 Sep) = **+1.98%** | Well under the 15% Rule 9 unexplained-move threshold; this session is user-requested, not price-triggered. |

---

## 2. Data Gathered — Sources & Gaps

**No new 8-K since the 2026-09-02 Q3 FY2026 earnings release** — confirmed directly via SEC EDGAR's 8-K filing index for CIK 0001730168 (most recent filing remains 2026-09-02; next filing on record is 2026-07-06, i.e. nothing newer). Per the task instructions, the TTM window is **not** rolled forward this session — every TTM/fundamental figure below is carried forward unchanged from the 2026-09-15 session, and only live-price-dependent figures (and the 5yr PE range, see below) are refreshed.

| Metric | Value | Status |
|---|---|---|
| TTM Revenue | $89,104M | Carried forward — no new fiscal data |
| TTM Net Income (GAAP) | $38,265M | Carried forward |
| TTM GAAP Operating Income (EBIT) | $42,814M | Carried forward |
| TTM FCF | $39,403M | Carried forward |
| TTM Gross Profit / Margin | $61,277M / 68.77% | Carried forward |
| TTM Interest Expense | $3,116M | Carried forward |
| TTM D&A | $8,764M | Carried forward |
| TTM EBITDA | $51,578M | Carried forward |
| Net Debt (Q3FY26 end, 2 Aug 2026) | $35,444M | Carried forward — next balance-sheet data point is Q4 FY2026 (~Dec 2026) |
| Total Equity | $99,690M | Carried forward |
| Diluted shares (Q3FY26, GAAP basis) | 4,887M | Carried forward — used consistently for Market Cap/EV across all five AVGO rescore sessions to date, per the continuity flag first raised 2026-09-15 (`yfinance`'s `sharesOutstanding` field now reads 4,773.6M, a more current *basic* count, ~2.3% lower — noted, not blended in). |
| Forward EPS | **$19.381** (fresh, `yfinance` `forwardEps`) | Refreshed — essentially flat vs. $19.384 on 2026-09-15 (normal drift, not a new data point being rolled in) |
| Forward PE | **18.183×** ($352.39 ÷ $19.381) | Refreshed |
| 5yr PE range (reconstructed) | **Avg 29.892×, Low 13.365×, High 52.758×** (n=20 quarters) via `scripts.fetch_fundamentals` | **✅ Data gap resolved this session** — `yfinance`'s `get_earnings_dates` has now backfilled the 2026-09-02 reported-EPS row (flagged as stale for two consecutive sessions, 2026-09-03 and 2026-09-15). Figures are a modest refresh of the prior carried-forward values (29.9465/13.3897/52.8544), not a material change. |
| Beta | 1.457 | Unchanged from 2026-09-15 (`yfinance` `info.beta`) |
| Effective tax rate (normalized) | 21% carried forward, flagged | Unchanged — no new "clean" quarter since 2026-09-03 |
| VMware/intangible amortization add-back | $9.3B/yr carried forward, flagged | Unchanged — see 2026-09-03 session for full reasoning |
| Dividend | $0.65/quarter ($2.60/yr annualized) | Unchanged |

**No metric was invented or estimated.** Every fresh figure traces to IBKR's live snapshot, `yfinance`'s live fields (via `python -m scripts.fetch_fundamentals AVGO`), or WebSearch/WebFetch cross-checks against SEC EDGAR/TradingEconomics; every carried-forward figure is explicitly flagged with the reason it wasn't independently re-derived this session.

**`scripts.fetch_fundamentals AVGO` output (pasted verbatim):**
```
## Fundamentals — AVGO

Market Cap            = 1,681,439,457,280
Enterprise Value      = 1,719,628,333,056
Shares Outstanding    = 4,773,629,865
Forward PE            = 18.172
FCF Yield %           = 2.343
EV/EBIT               = 39.455
Net Margin %          = 42.944
Gross Margin %        = 68.770
ROIC % (NOPAT/InvCap) = 28.144  [tax_rate=0.0545, NOPAT=41,211,298,154, InvestedCapital=146,428,000,000]
Revenue 3yr CAGR %    = 24.378
Net Debt/EBITDA       = 0.937  [EBITDA_ttm=52,259,999,744]
FCF/NI TTM %          = 102.974
FCF/NI annual (oldest first) = [141.9%, 125.2%, 329.3%, 116.4%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 29.892 / 13.365 / 52.758  (n=20 quarters)
```
**Note:** the script's own Market Cap/EV/ROIC use `yfinance`'s *basic* shares-outstanding count (4,773.6M) and its own effective-tax-rate estimate (5.45%), not this framework's established diluted-share-count (4,887M) and normalized-21%-tax/amortization-add-back methodology. Per the continuity flag carried since 2026-09-15, the diluted/normalized basis is used below for all Quality and Valuation Score math (Market Cap, EV, FCF Yield, EV/EBIT, ROIC); the script's own Market Cap/EV/ROIC/EV-EBIT lines are informational cross-checks only, not the scored figures. The script's FCF Yield %, Net Margin %, Gross Margin %, Revenue CAGR %, Net Debt/EBITDA, and FCF/NI figures **are** used directly (basis-independent or already matching the carried-forward TTM figures).

---

## 3. Quality Score (Phase 01 gate) — recomputed, inputs unchanged

**Hard disqualifier check (re-verified, unchanged):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | TTM 102.97% | disqualify if <70% for 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | 0.687× | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2023–FY2025 all positive, FY2026 trending strongly positive | disqualify if not | ✅ PASS |

**`scripts.scoring.quality_score` output (pasted verbatim):**
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
+10 TAM/pricing-power evidence: AI semiconductor/networking TAM expansion carried forward from prior AVGO sessions (custom AI accelerator demand from hyperscalers, VMware private cloud TAM) -- no new evidence this session, no new 8-K since 2026-09-02.
Growth_Score (final, clamped) = 100.00

**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - 0.687/4)) = 82.82

**Moat Signal (15%)**
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Carried forward: AVGO custom AI ASIC share with hyperscaler partners (Google TPU, Meta) documented in prior sessions. |
| brand_premium | False | No consumer brand premium; B2B semiconductor/infrastructure software vendor. |
| network_effect | False | No direct network effect identified in prior sessions. |
| switching_costs | True | Carried forward: VMware enterprise virtualization switching costs, custom ASIC design-win lock-in with hyperscalers. |
| scale_cost_advantage | False | Not established as a distinct moat signal in prior sessions (kept conservative, 2/5 signals TRUE). |
Moat_Score = (2/5) x 100 = 40.00

**FCF Quality (10%)**
FCFQuality_Score = clamp(((1.0297 - 0.40)/0.60)x100) = 100.00

**Quality Score — Final**
Quality Score = (100.00x0.25) + (85.96x0.15) + (100.00x0.20) + (82.82x0.15) + (40.00x0.15) + (100.00x0.10)
= 86.318 -> rounds to 86.3

# Quality Score = 86.3 — PASSES the 80.0+ gate
```

ROIC input (30.47%) uses the framework's established normalized-EBIT basis (Normalized EBIT $52,114M = $42,814M + $9,300M carried-forward amortization add-back; NOPAT = $52,114M × (1 − 0.21) = $41,170.1M; Net Invested Capital = Total Debt $59,419M + Total Equity $99,690M − Cash $23,975M = $135,134M; ROIC = $41,170.1M / $135,134M = 30.47%) — unchanged from every prior AVGO session since all inputs are carried-forward TTM/balance-sheet figures.

**Quality Score = 86.3 — unchanged from 2026-09-15**, exactly as expected: no new 8-K, no input moved. Clears the 80.0+ gate comfortably (sensitivity check carried forward: even the most conservative moat reading, Moat_Score = 0, still gives 80.3 — still clears).

**No new TAM/pricing-power or moat-signal evidence surfaced this session.**

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $352.39 / $19.381 = 18.183×
EY = 1 / 18.183 = 5.4996%
Spread = EY − 10Y Treasury = 5.4996% − 5.21% = +0.2896pp
```
Spread (+0.29pp) < +1.5% → **fails** → **+5 additive** (yellow flag, not a veto). Margin narrowed further vs. 2026-09-15's +0.59pp — the 10Y rose faster than the earnings yield improved.

**Step 2 — Rate Regime Modifier**
10Y = 5.21% → **>5% bracket** → **+10** — unchanged bracket from 2026-09-15 (still above the 5% threshold crossed for the first time since Oct 2023 on that date).

**Combined Rate Modifier: +15** (unchanged from 2026-09-15)

---

## 5. Valuation Score (Phase 02)

**`scripts.scoring.valuation_score` output (pasted verbatim):**
```
## Valuation Score

**FCF Yield (40%)**
FCF_Score = clamp(100x(1 - 2.2881/10)) = 77.119

**EV/EBIT**
EV/EBIT_Score = clamp((41.049 - 12)/23 x 100) = 100.000

**Forward PE**
FwdPE_Score (raw) = clamp((18.183 - 13.365)/(52.758 - 13.365) x 100) = 12.231
Deviation vs 5yr avg (29.892) = (18.183 - 29.892)/29.892 x 100 = -39.171%
Historical PE Modifier: >20% below 5yr avg -> -10
FwdPE_Score = clamp(12.231 + -10) = 2.231

**PEG**
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT

**Rate Environment Gate**
EY = 1/18.183 x 100 = 5.4996%
Spread = EY - 10Y (5.21%) = 0.2896pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.21% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15

**Upside/Downside Modifier**
PW Fair Value = 0.25x724.87 + 0.50x484.53 + 0.25x247.11 = 485.2600
Gap Upside % = (485.2600/352.39) - 1 = 37.7054%
Annualized gap = 37.7054% / 1.18yr = 31.9537%/yr
E = 31.9537 (annualized gap) + 12.0 (intrinsic growth) + 0.7379 (shareholder yield: 0.7379 div + 0 buyback) = 44.6916%/yr
E (44.6916%) >= H (10.0%) -> M = -15 x clamp((44.6916-10.0)/15, 0, 1) = -15.0000
Upside/Downside Modifier (bounded [-15, +15]) = -15.0000

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 71.294

**Final Valuation Score**
Final Score = Raw (71.294) + Rate Modifier (+15) + Upside/Downside Modifier (-15.000)
= 71.294 -> rounds to 71.3

# Valuation Score = 71.3
```

**Inputs behind the script call:**
- `fcf_yield_pct` = 2.2881 → FCF Yield = TTM FCF $39,403M / Market Cap $1,722,129.93M (= $352.39 × 4,887M diluted shares)
- `ev_ebit` = 41.049 → EV $1,757,573.93M (Market Cap + Net Debt $35,444M) / TTM GAAP EBIT $42,814M. **Normalization check (flag carried forward):** Normalized EBIT $52,114M → normalized EV/EBIT = 33.72× — still below the 35× ceiling, converging further toward saturation as the score screen's GAAP EV/EBIT already caps at 100.0 either way (no longer moves the outcome, but tracked per the continuity flag first raised 2026-09-03).
- `forward_pe` = 18.183, `pe_5yr_low/avg/high` = 13.365/29.892/52.758 (fresh, §2)
- `treasury_10y_pct` = 5.21 (§4)
- `bull/base/bear_fair_value` = $724.87 / $484.53 / $247.11 — NTM EPS $19.381 × 34×/25×/15× scenario multiples, same architecture as every AVGO session since 2026-07-04 (no new information to justify revising the assumptions)
- `catalyst_within_18_24_months` = true, `catalyst_window_years` = 1.18 — same documented catalyst (management's FY2027 AI-semiconductor revenue target >$100B, confirmation expected ~Dec 2027 results), window shortened from 1.24yr (2026-09-15) purely by the 13 days elapsed
- `intrinsic_growth_pct` = 12.0 (carried forward), `dividend_yield_pct` = 0.7379 ($2.60 / $352.39)

Raw weighted sub-scores essentially flat vs. 2026-09-15 (71.29 vs. 70.93) — the marginally higher price offset by the marginally lower forward EPS estimate keeps FCF Yield and EV/EBIT close to unchanged.

**Valuation Score = 71.3 — "TRIM 25–30%" band (70.0–79.9)** per the raw Action Table, essentially unchanged from 2026-09-15's 70.9 (same band). As on 2026-09-15, this is governed by the **Composite Score**, not the raw Valuation Score, per §6.

---

## 6. Composite Score

**`scripts.scoring.composite_score` output (pasted verbatim):**
```
## Composite Score

Composite Score = 0.50x(100 - 86.3) + 0.50x71.3 = 42.500 -> rounds to 42.5

# Composite Score = 42.5
(Quality Score 86.3, Valuation Score 71.3)
```

**Composite Score = 42.5 — stays in the "Cheap" (30.0–49.9) band**, essentially flat vs. 42.3 on 2026-09-15 (a 0.2-point drift from the marginal valuation-score move above). Per [valuation-scoring.md](../framework/valuation-scoring.md)'s explicit instruction, the Composite Score governs the Phase 03/05 action table once a Quality Score is on file — AVGO's high Quality Score (86.3) continues to absorb the rate-driven pressure on the raw Valuation Score, keeping this still-excellent business in the "Cheap" band rather than a mechanical trim.

---

## 7. Action Recommendation & Order Setup

Composite Score 42.5 stays in the **30.0–49.9 "Cheap" → Standard position 3–5%** band — nominally BUY-eligible. Full order setup run below, per the operating brief.

### Fair Value — two methods, triangulated (Rule 1: Tech/Growth → DCF primary, Multiples secondary)

**Method A — 3-Stage DCF (Rule 2).** Same 10-year growth-fade schedule as prior sessions, rebased on the unchanged $39,403M TTM FCF and a WACC refreshed for the current risk-free rate (beta unchanged):

```
WACC build:
  Cost of equity = Rf (5.21%) + Beta (1.457) × ERP (5.0%, assumed) = 12.495%
  Cost of debt (pretax) = TTM interest expense $3,116M / Total Debt $59,419M = 5.244%; after-tax (21%) = 4.143%
  Weights: E/(D+E) = 96.665% (Market Cap $1,722,129.93M), D/(D+E) = 3.335% (Debt $59,419M)
  WACC = 96.665%×12.495% + 3.335%×4.143% = 12.216%

Stage 1 (yrs 1–5), FCF base $39,403M, same growth path as prior sessions:
  y1 +25% → $49,253.8M | y2 +20% → $59,104.5M | y3 +15% → $67,970.2M | y4 +12% → $76,126.6M | y5 +10% → $83,739.3M

Stage 2 (yrs 6–10), linear fade from 10% to the 2.5% terminal rate:
  y6 $90,857.1M | y7 $97,217.1M | y8 $102,564.0M | y9 $106,666.6M | y10 $109,333.3M

Terminal Value (at y10) = $109,333.3M × 1.025 / (0.12216 − 0.025) = $1,153,516.9M
Terminal Value as % of total DCF value ≈ 47.6% (under the 75% Rule 4 sanity cap)

Sum of discounted FCFs (yrs 1–10, @ 12.216% WACC) = $436,100.0M
PV of Terminal Value = $364,443.9M
Enterprise Value (DCF) = $800,543.9M
Equity Value = $800,543.9M − Net Debt $35,444M = $765,099.9M
DCF Fair Value / share = $765,099.9M / 4,887M = $156.56
```
(Down modestly from $160.10 on 2026-09-15 — a slightly higher WACC, purely on the higher risk-free rate, more than offsetting the unchanged beta.)

**Method B — Scenario-weighted multiples (§5 PW Fair Value):** **$485.26**

**⚠️ Same material finding as prior sessions — wide divergence between the two methods**, same underlying tension: a disciplined GDP-terminal-growth DCF vs. AVGO's own trailing 5-year PE range.

```
Triangulation (Rule 3, Tech/Growth weights): Blended FV = 40% × DCF + 60% × Multiples
                                            = 0.40 × $156.56 + 0.60 × $485.26
                                            = $62.62 + $291.16
                                            = $353.78
```

### Order Setup Checklist

**`scripts.scoring.order_setup` output (pasted verbatim, MoS 27.5% / stop 27.5% — midpoint of the 25–30% Cheap-band range):**
```
## Order Setup

Band: 30.0-49.9 (Set limit order)
Buy Price = Fair Value (353.78) x (1 - 27.5%) = 256.4905
Live price 352.39 vs buy price ceiling 256.4905 -> limit order at buy price (live price above ceiling); entry price used = 256.4905
Primary Sell Target = Fair Value = 353.7800
Bull-Case Trim Target = Bull FV (724.87) x 0.90 = 652.3830
Stop Loss = Entry Price (256.4905) x (1 - 27.5%) = 185.9556
R/R Ratio = (Sell Target 353.7800 - Entry 256.4905) / (Entry 256.4905 - Stop 185.9556) = 97.2895/70.5349 = 1.3793:1
*** FLAG: R/R 1.3793:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = Portfolio Value (61622.32) x 1.5% = 924.3348
Risk Per Share = Entry (256.4905) - Stop (185.9556) = 70.5349
Shares by risk-based sizing = 924.3348 / 70.5349 = 13.1046
Allocation cap = Portfolio Value (61622.32) x 5% = 3081.1160 -> 12.0126 shares
Position Size (shares) = min(risk-based, cap) = 12.0126  [binding: allocation cap]
Position Size ($) = 12.0126 x 256.4905 = 3081.1160
Current shares held = 6; gap vs. target = 6.0126
```

**Full MoS/stop matrix checked (per fair-value-methodology.md Step 6), not just the midpoint:**

| MoS \ Stop | 25% | 30% |
|---|---|---|
| 25% | 1.33:1 | 1.11:1 |
| 30% | **1.71:1** | 1.43:1 |

Best case in the applicable range (MoS 30% / Stop 25% = 1.71:1) still **fails the 2:1 minimum** throughout — matches the 2026-09-15 session's best-case figure exactly (same Fair Value/live-price ratio, essentially unchanged).

**Per fair-value-methodology.md Step 6: R/R fails the minimum threshold across the entire applicable MoS/stop range. No order is placed.**

**Position sizing is also moot for a different reason:** AVGO's current 3.43% weight already sits **within** the Composite Score's implied 3–5% "Standard position" target band — no sizing gap to fill even before the R/R gate is considered.

### Net Action: **HOLD** — maintain the current 6-share position as-is

- No trim: Composite Score (42.5) is far below any trim threshold (70.0+) — and per §6, the Composite (not the raw Valuation Score's 71.3) is the number the action table runs against.
- No add: R/R on the computed order setup fails the 2:1 minimum (best case 1.71:1), and the position is already within its Composite-Score-implied target size.
- **The open 2026-06-16 override remains unresolved** (§0) — unchanged by this rescore.

**Same action band as the 2026-09-03 and 2026-09-15 sessions (HOLD)** — the underlying picture remains essentially unchanged: Quality Score identical at 86.3, TTM data unchanged, and the Composite Score construct continues to keep a still-excellent business from being mechanically pushed toward a trim recommendation by the ongoing rate-driven pressure on the raw Valuation Score.

---

## 8. Next Review Trigger

**Date/event:** AVGO's Q4 FY2026 earnings release (expected ~December 2026, per the typical AVGO reporting cadence) — re-run Phase 01/02 with refreshed TTM figures. **Two specific follow-ups flagged, worth checking first at that rescore:**
1. **Watch the EV/EBIT GAAP-vs-normalized divergence** (§5) — normalized EV/EBIT (33.72×) remains below the 35× ceiling; if it keeps widening the choice of basis will eventually move the actual score, not just a footnote — worth a `decisions/` entry if it starts to matter for the action band.
2. **Monitor the Rate Environment regime.** The 10Y has now held above 5% for two consecutive rescore sessions (2026-09-15 and 2026-09-28) — if it falls back under 5% before the next scheduled rescore, the Rate Regime Modifier reverts to +5 and the raw Valuation Score would fall back toward the 66–67 range documented on 2026-09-03, all else equal. Not a reason to rescore early on its own (Rule 9 doesn't list rate moves alone as a trigger for names without a Turnaround/Debt-Gate dependency), but worth noting as context.

Earlier trigger on a >15% unexplained move from $352.39 (Rule 9), a further guidance revision/M&A/management change, or new third-party market-share data that would firm up the Moat_Score's remaining evidentiary gap. **Separately and unconditionally: the 2026-06-16 override still needs the user to supply a rationale** for `decisions/` and `override-log.md` — not tied to any valuation trigger.

---

## Glossary

- **8-K**: A US company's "current report" filed with the SEC to disclose a material event between regular filings — earnings releases are typically furnished as an exhibit to one.
- **Beta**: A stock's sensitivity to overall market moves; used here as an input to estimate AVGO's cost of equity in the DCF's WACC.
- **bps / pp**: Basis points (0.01 percentage points) / percentage points — units used throughout the rate and modifier calculations.
- **CAGR**: Compound Annual Growth Rate.
- **CapEx**: Capital Expenditure.
- **Catalyst window**: The timeframe within which a documented event is expected to close the price/fair-value gap — required before the Upside/Downside Modifier can credit large expected upside.
- **Composite Score**: This framework's blended 0.0–100.0 ranking number — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only after a company clears the 80.0+ Quality Score gate.
- **D&A**: Depreciation & Amortization.
- **DCF (Discounted Cash Flow)**: A valuation method estimating a company's worth today by projecting future cash flows and discounting them back to the present.
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **Equity Risk Premium (ERP)**: The extra return equity investors demand over the risk-free rate — an assumed DCF input, not a fetched fact.
- **EPS**: Earnings Per Share.
- **EV**: Enterprise Value — market cap + debt − cash.
- **EV/EBIT**: Enterprise Value ÷ EBIT, a valuation multiple independent of capital structure.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against bond yields in the Rate Environment Gate.
- **FCF (Free Cash Flow)**: Cash generated after running and maintaining the business.
- **FCF Yield**: FCF ÷ Market Cap (or EV) — higher is cheaper.
- **FCF/NI conversion ratio**: FCF ÷ Net Income — a cash-quality check.
- **Forward PE**: Price ÷ next-twelve-months expected EPS.
- **FV (Fair Value)**: The analyst's estimate of intrinsic worth, independent of market price.
- **GAAP**: Generally Accepted Accounting Principles.
- **Gross Margin**: Gross Profit ÷ Revenue.
- **Hard disqualifier**: A Quality Score condition that fails a company regardless of its weighted score.
- **Human Override**: A position opened or held outside the framework's own rules — tracked for life in `override-log.md`. AVGO's 2026-06-16 entry is one, and remains open.
- **Hurdle rate**: The minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against.
- **Invested Capital**: The total capital (debt + equity, net of cash here) put to work in a business — the denominator of ROIC.
- **IRR**: Internal Rate of Return.
- **Moat**: A durable competitive advantage protecting a business's profits from competitors.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set.
- **Net Debt/EBITDA**: A leverage ratio — this framework's primary balance-sheet-risk gate.
- **Net Margin**: Net Income ÷ Revenue.
- **NI**: Net Income.
- **NOPAT**: Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the numerator of ROIC here.
- **PEG ratio**: PE ÷ earnings growth rate.
- **PT (Price Target)**: An analyst's price forecast.
- **PW (Probability-Weighted) Fair Value**: This framework's blended fair value — 25% bull + 50% base + 25% bear.
- **Quality Score**: This framework's 0.0–100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score.
- **Rate Environment Gate / Rate Regime Modifier**: The mandatory pre-score check comparing Earnings Yield against the 10-Year Treasury, and the resulting additive score adjustment.
- **R/R (Risk/Reward ratio)**: Expected gain ÷ expected loss on a trade; this framework requires ≥2:1 to enter.
- **ROIC**: Return on Invested Capital.
- **Rule 0 / Rule 6 / Rule 9 / Rule 10**: This framework's standing instructions to always fetch a live price first; normalize distorted earnings before valuing; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline.
- **TAM**: Total Addressable Market.
- **Terminal Value**: The lump-sum value assigned to all DCF cash flows beyond the explicit forecast period.
- **TTM**: Trailing Twelve Months.
- **Upside/Downside Modifier (Expected-Return Modifier)**: The additive ±15 adjustment based on expected annual return vs. the 10% hurdle.
- **Valuation Score**: This framework's 0.0–100.0 score (lower = cheaper) combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.
- **WACC**: Weighted Average Cost of Capital — the DCF discount rate.

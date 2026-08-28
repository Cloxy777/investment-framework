# RESCORE — AVGO (Broadcom Inc.) — 2026-08-28

**Task type:** RESCORE (mode `--both`)
**Date:** 28 Aug 2026
**10Y US Treasury Yield:** 4.73% (WebSearch: TradingEconomics, 28 Aug 2026 print — up from 4.49% at the 2026-07-04 session)
**Rate Regime Modifier (Step 2):** +5 (10Y still in the 3.5–5% bracket)
**Current AVGO portfolio weight:** 3.68% (6 shares, IBKR, per [holdings.md](../portfolio/holdings.md)) — still held as an **open, unresolved Human Override**
**Sector:** Semiconductors (fabless — AI accelerators/networking) + Infrastructure Software (VMware)
**Last review:** 04 Jul 2026 (Valuation 68.2 / Quality 82.1 / Composite 43.1) — see [session](../sessions/2026-07-04-rescore-avgo.md)

---

## 0. Override status (reported, not resolved this session)

Per [override-log.md](../portfolio/override-log.md): AVGO's **2026-06-16 override remains open** — still no rationale supplied, status column still reads "Open — under review." Unchanged since the last session. Not this command's scope to resolve.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$368.77** | IBKR `get_price_snapshot` (contract_id 313130367, NASDAQ), real-time last trade (`is_close: false`), queried live this session. Cross-validated against `yfinance`'s `currentPrice`/`regularMarketPrice`, reading **$368.69** — within 0.02%, immaterial. |
| Prior close | $371.54 | IBKR `change` field (−$2.77 / −0.75% intraday) |
| 52-week range | $285.53 – $495.00 (IBKR `misc_statistics`) / $287.17 – $495.00 (`yfinance`) | Close agreement |
| YTD change | +6.76% ($23.37) | IBKR `year_to_date_change` |
| Analyst consensus PT | $525.97 (46 analysts), rating "Strong Buy" | `yfinance` — essentially unchanged from the 2026-07-04 session's $523.73 |
| Prior session price | $360.45 (04 Jul 2026) | For reference — AVGO is **+2.3%** since the last rescore. Well below the 15% Rule 9 threshold — this rescore is calendar/methodology-driven (routine quarterly cadence), not price-driven. |

**Context:** $368.77 sits ~25% below the 52-week high ($495) and ~29% above the 52-week low ($286) — still roughly the middle of the range, ~43% below the analyst consensus PT cluster.

---

## 2. Data Gathered — Sources & Gaps

Fundamentals re-pulled fresh via `yfinance` this session. **No new AVGO earnings have been reported since Q2 FY2026** (filed ~3 Jun 2026) — Q3 FY2026 is still expected in September 2026 (per the 2026-07-04 session's own forecast), confirmed by `yfinance`'s quarterly financials/cashflow/balance-sheet tables, whose most recent column is still **2026-04-30 (Q2 FY2026)**. The TTM window (Q3 FY2025–Q2 FY2026) is therefore **identical** to the 2026-07-04 session — every fundamental figure below is unchanged and re-verified, not re-derived from new data:

| Metric | Value | Source / note |
|---|---|---|
| TTM Revenue | $75,465M | `yfinance` quarterly rollforward — unchanged, same 4 quarters |
| TTM Net Income | $29,317M | Unchanged |
| TTM GAAP EBIT | $30,443M | Carried forward (8-K-sourced rollforward for the unchanged TTM window) |
| TTM FCF | $32,762M | `yfinance` quarterly cash flow rollforward — re-verified quarter-by-quarter ($10,262M + $8,010M + $7,466M + $7,024M), unchanged |
| TTM Gross Margin | 68.3% | Unchanged |
| Net Debt | $45,279M (Total Debt $64,907M − Cash $19,628M) | `yfinance` balance sheet, still 2026-04-30 (Q2 FY2026) — no new 10-Q filed |
| Diluted shares (Q2 FY2026) | 4,876M | Unchanged |
| TTM interest expense | $3,145M ($807M+$761M+$801M+$776M) | Re-verified this session, unchanged |
| Forward PE | 18.90× | `yfinance` (price $368.77 ÷ forward EPS $19.507 — EPS estimate ticked up slightly from $19.396) |
| 5yr PE range (reconstructed) | Avg 29.95×, Low 13.39×, High 52.85× (n=20 quarters) | `yfinance` `get_earnings_dates` + price history, re-run this session — essentially identical to the 2026-07-04 figures (the trailing window barely moved) |
| Beta | 1.473 | `yfinance` `info.beta` (up slightly from 1.462) |
| VMware amortization | ~$9.3B/yr (carried forward) | No new 10-Q since 2026-06-20/07-04 sessions — nothing fresher to pull |
| Effective tax rate (normalized) | 21% (unchanged basis) | Same clean-quarter normalization as the 2026-07-04 session |
| Dividend / shareholder yield | $2.60/sh, ~0.7% trailing yield; buyback yield ≈0% | Unchanged |

**No metric was invented or estimated.** Because no new quarter has reported, every fundamental input is a re-verification of the 2026-07-04 session's figures rather than a fresh derivation — flagged explicitly per "no black box." Only the **market-observable** inputs (live price, 10Y Treasury, beta, forward-EPS consensus) moved, and those flow through the calculations below.

---

## 3. Quality Score (Phase 01 gate) — re-verified, unchanged

Every input to the Quality Score (profitability, margins, growth, balance sheet, moat evidence, FCF quality) is drawn from the same unchanged TTM window and the same cited moat evidence as the 2026-07-04 session — there is no new fundamental data this session to move any sub-score. Re-verified below rather than blindly carried forward:

**Hard disqualifier check:**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | TTM 111.8% (unchanged) | disqualify if <70% for 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | 1.076× (unchanged) | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2023–FY2025 all positive (unchanged) | disqualify if not | ✅ PASS |

```
Profitability_Score = 89.4   (Net Margin 38.85% → 100.0, ROIC 23.61% → 78.7, avg = 89.35 → 89.4)
GrossMargin_Score   = 85.3   (68.28% gross margin, no trend bonus)
Growth_Score        = 100.0  (Revenue 3yr CAGR 24.39% → 97.6, +10 TAM/pricing-power evidence, capped at 100.0)
BalanceSheet_Score  = 73.1   (Net Debt/EBITDA 1.076×)
Moat_Score          = 40.0   (2/5 signals cited TRUE — market share, switching costs; same evidentiary basis as last session)
FCFQuality_Score    = 100.0  (FCF/NI 111.8%)

Quality Score = 89.4×0.25 + 85.3×0.15 + 100.0×0.20 + 73.1×0.15 + 40.0×0.15 + 100.0×0.10
              = 22.35 + 12.795 + 20.00 + 10.965 + 6.00 + 10.00
              = 82.11 → 82.1
```

**Quality Score = 82.1 — unchanged, clears the 80.0+ gate.** The same sensitivity flag from the 2026-07-04 session still stands: excluding the "market share" moat signal (a borderline evidentiary call) would drop Moat_Score to 20.0 and the final Quality Score to 79.1 — below the gate. No new third-party market-share citation has surfaced since; this remains an open item for a future session, not resolved here.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = 18.90×
EY = 1 ÷ 18.90 = 5.29%
Spread = EY − 10Y Treasury = 5.29% − 4.73% = +0.56%
```
Spread (+0.56%) < +1.5% → **fails** → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.73% → 3.5–5% bracket → **+5**

**Combined Rate Modifier: +10** (same bracket as the 2026-07-04 session, despite the 10Y rising 24bps — still inside 3.5–5%)

---

## 5. Valuation Score (Phase 02)

### FCF Yield (40% weight)

```
Market Cap = $368.77 × 4,876M shares = $1,798,123M
FCF Yield  = $32,762M / $1,798,123M = 1.822%
FCF_Score  = clamp(100×(1 − 1.822/10), 0, 100) = 81.8
```

### EV/EBIT (weight 25% base, redistributed to 40% — PEG still not applicable, see below)

```
EV = Market Cap $1,798,123M + Net Debt $45,279M = $1,843,402M
EV/EBIT (GAAP TTM) = $1,843,402M / $30,443M = 60.55×
EV/EBIT_Score = clamp((60.55 − 12)/23 × 100, 0, 100) = 100.0
```
Normalization check (strip $9.3B/yr VMware amortization): Normalized EBIT = $39,743M → EV/EBIT = 46.4×. Still far past the 35× ceiling — **EV/EBIT_Score = 100.0 either way**.

### Forward PE + Historical PE Modifier (20% weight)

```
Forward PE = 18.90×, 5yr Low = 13.39×, 5yr High = 52.85×
FwdPE_Score = clamp((18.90 − 13.39)/(52.85 − 13.39) × 100, 0, 100) = 14.0
```
**Historical PE Modifier (Upgrade 2):** Forward PE vs 5yr avg (29.95×): (18.90 − 29.95)/29.95 × 100 = **−36.9%** (>20% below) → **−10**.
```
FwdPE_Score = 14.0 − 10 = 4.0
```

### PEG (15% weight) — Fast-Grower eligibility ruling still carried forward

No new information since the 2026-07-04 session to revisit the ruling: AVGO's GAAP EPS remains distorted ~35–40% by non-cash VMware amortization, still disqualifying it from PEG eligibility. **PEG not scored; its 15% weight redistributed to EV/EBIT (→ 40%).**

### Raw Weighted Score

```
Raw = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
    = (81.8 × 0.40) + (100.0 × 0.40) + (4.0 × 0.20)
    = 32.72 + 40.00 + 0.80
    = 73.51
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

Reuses the same scenario architecture as the 2026-07-04 session (no new guidance/earnings event to warrant new scenario assumptions), refreshed for the current price and forward EPS.

**Step 1 — scenario fair values.** NTM EPS estimate: **$19.51** (`yfinance` forward EPS).

| Scenario | Wt | Assumption | EPS basis | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | AI ramp beats, re-rate | $19.51 × 1.10 = $21.46 | 34× | **$729.58** |
| Base | 50% | Consensus AI ramp, multiple eases below 5yr avg (29.95×) | $19.51 | 25× | **$487.69** |
| Bear | 25% | AI capex slowdown / hyperscaler in-sourcing, de-rate toward the low end | $19.51 × 0.85 = $16.58 | 15× | **$248.72** |

```
PW Fair Value (multiples) = 0.25×729.58 + 0.50×487.69 + 0.25×248.72 = $488.42
Gap Upside % = 488.42 / 368.77 − 1 = +32.4%
```

**Step 2 — catalyst & annualization (Rule 10).** Same documented catalyst: management's FY2026 AI-semiconductor revenue guide ($56B) and FY2027 target (>$100B), from the Q2 FY2026 earnings release (3 Jun 2026). From today (28 Aug 2026) to the FY2027 milestone confirmation (Broadcom's Q4 FY2027 earnings call, typically ~December) is **~15.5 months ≈ 1.29 years** (shorter than the 1.5yr used 04 Jul 2026, since the catalyst date is fixed and time has passed) — Guardrail 1 (catalyst within 18–24 months) remains satisfied, no cap needed.
```
Annualized gap = 32.4% / 1.29 = 25.1%
```
**Step 3 — expected annual return E.**
```
E = annualized gap (25.1%) + intrinsic growth (12%, unchanged) + shareholder yield (~0.7%, unchanged)
  = 25.1 + 12.0 + 0.7 = 37.8%
```
**Step 4 — map E to M** (hurdle H = 10%):
```
E (37.8%) ≥ H → M = −15 × clamp((37.8 − 10)/15, 0, 1) = −15 × clamp(1.85, 0, 1) = −15.0
```
**Upside/Downside Modifier M = −15.0 (fully saturated at the cap)** — same as the 2026-07-04 session; the shrinking catalyst window (1.29yr vs 1.5yr) more than offsets the smaller price-based gap (32.4% vs 34.7%), so the modifier remains saturated.

---

## 7. Final Valuation Score

```
Final Score = Raw Weighted (73.51) + Rate Modifier (+10) + Upside/Downside Modifier (−15.0)
            = 68.51 → 68.5
```

**Valuation Score = 68.5 — "Fair Value"** (50.0–69.9 band, unchanged band; up 0.3 from 68.2)

---

## 8. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 82.1) + 0.50 × 68.5
                = 0.50 × 17.9 + 34.25
                = 8.95 + 34.25
                = 43.20
```

**Composite Score = 43.2 — "Cheap"** (30.0–49.9 band, unchanged band; up 0.1 from 43.1)

---

## 9. Action Recommendation & Order Setup

Composite Score 43.2 stays in the **30.0–49.9 "Cheap" → Standard position 3–5%** band — nominally BUY-eligible. Order setup run in full below, per the operating brief.

### Fair Value — two methods, triangulated (Rule 1: Tech/Growth → DCF primary, Multiples secondary)

**Method A — 3-Stage DCF (Rule 2).** Same FCF base and 10-year growth-fade schedule as the 2026-07-04 session (no new guidance to revise the cash-flow path) — only the WACC inputs move (higher Rf, slightly higher beta):

```
WACC build:
  Cost of equity = Rf (4.73%) + Beta (1.473) × ERP (5.0%, assumed) = 12.10%
  Cost of debt (pretax) = TTM interest expense $3,145M / Total Debt $64,907M = 4.85%; after-tax (21%) = 3.83%
  Weights: E/(D+E) = 96.5% (Market Cap $1,798,123M), D/(D+E) = 3.5% (Debt $64,907M)
  WACC = 96.5%×12.10% + 3.5%×3.83% = 11.81%   (up from 11.52% on 2026-07-04)

Stage 1 (yrs 1–5), FCF base $32,762M, unchanged growth path:
  y1 +25% → $40,953M | y2 +20% → $49,143M | y3 +15% → $56,514M | y4 +12% → $63,296M | y5 +10% → $69,626M

Stage 2 (yrs 6–10), linear fade from 10% to the 2.5% terminal rate:
  y6 $75,544M | y7 $80,832M | y8 $85,278M | y9 $88,689M | y10 $90,906M

Terminal Value (at y10) = $90,906M × 1.025 / (0.1181 − 0.025) = $1,001,172M
Terminal Value as % of total DCF value = 47.0% (well under the 75% Rule 4 sanity cap)

Sum of discounted FCFs (yrs 1–10) = $369,590M
PV of Terminal Value = $327,959M
Enterprise Value (DCF) = $697,549M
Equity Value = $697,549M − Net Debt $45,279M = $652,270M
DCF Fair Value / share = $652,270M / 4,876M = $133.77
```
(Down from $138.83 on 2026-07-04, purely the effect of the higher WACC — same cash-flow assumptions.)

**Method B — Scenario-weighted multiples (§6 PW Fair Value):** **$488.42**

**⚠️ Same material finding as last session — wide divergence between the two methods,** now slightly wider (DCF fell, multiples-FV rose slightly). Not a calculation error — reflects the same tension between AVGO's AI-driven re-rating and what a disciplined GDP-terminal-growth DCF supports.

```
Triangulation (Rule 3, Tech/Growth weights): Blended FV = 40% × DCF + 60% × Multiples
                                            = 0.40 × $133.77 + 0.60 × $488.42
                                            = $53.51 + $293.05
                                            = $346.56
```

### Order Setup Checklist

```
[✓] Composite Score (incl. Quality blend):    43.2 — "Cheap" (30.0–49.9 band)
[✓] Expected annual return E / catalyst:      +37.8% / 1.29yr (feeds the Upside/Downside Modifier, §6)
[✓] Upside/Downside Modifier applied:         −15.0
[✓] DCF Fair Value:                           $133.77
[✓] Multiples-Based Fair Value:               $488.42
[✓] Blended Fair Value:                       $346.56
[ ] Margin of Safety %:                       25–30% (Composite 30.0–49.9 band)
    Buy Price range: $242.59 (30% MoS) – $259.92 (25% MoS); midpoint (27.5%) = $251.26
[✓] PRIMARY SELL TARGET:                      $346.56 (Blended FV, baseline)
[✓] BULL-CASE TRIM TARGET:                    $729.58 × 0.90 = $656.62
[ ] STOP LOSS: 25–30% max loss from Buy Price
    At midpoint Buy Price $251.26 → Stop $182.16
[✗] Risk/Reward Ratio: (346.56 − 251.26) / (251.26 − 182.16) = 95.30/69.10 = 1.38:1
    Checked across the full 25–30% MoS range: 1.21:1 – 1.56:1 — FAILS the 2:1 minimum throughout.
```

**Per fair-value-methodology.md Step 6: R/R fails the minimum threshold across the entire applicable MoS range. No order is placed.**

**Position sizing is also moot for a different reason:** AVGO's current 3.68% weight already sits **within** the Composite Score's implied 3–5% "Standard position" target band — there is no sizing gap to fill even before the R/R gate is considered.

### Net Action: **HOLD** — maintain the current 6-share position as-is

- No trim: Composite Score (43.2) is far below any trim threshold (70.0+).
- No add: R/R on the computed order setup fails the 2:1 minimum, and the position is already within its Composite-Score-implied target size.
- **The open 2026-06-16 override remains unresolved** (§0) — unchanged by this rescore.

Same conclusion as the 2026-07-04 session — the score moved marginally (Valuation 68.2→68.5, Composite 43.1→43.2) but not enough to change the action bucket or the R/R outcome.

---

## 10. Next Review Trigger

**Date/event:** AVGO's Q3 FY2026 earnings release (expected September 2026) — re-run Phase 01/02 with refreshed TTM figures, re-check the VMware-amortization roll-off, and re-confirm the PEG-eligibility ruling. Earlier trigger on a >15% unexplained move from $368.77 (Rule 9), a guidance revision/M&A/management change, or new third-party market-share data that would resolve the Moat_Score sensitivity flagged in §3. **Separately and unconditionally: the 2026-06-16 override still needs the user to supply a rationale** for `decisions/` and `override-log.md` — not tied to any valuation trigger.

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
- **Fast Grower**: Peter Lynch's term for EPS growth >15%/yr for 3+ years — this framework's PEG-sub-score trigger.
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
- **Owner Earnings**: Net Income + D&A − maintenance-only CapEx (not applicable to AVGO — its capex is immaterial).
- **PEG ratio**: PE ÷ earnings growth rate.
- **PT (Price Target)**: An analyst's price forecast.
- **PW (Probability-Weighted) Fair Value**: This framework's blended fair value — 25% bull + 50% base + 25% bear.
- **Quality Score**: This framework's 0.0–100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score.
- **Rate Environment Gate / Rate Regime Modifier**: The mandatory pre-score check comparing Earnings Yield against the 10-Year Treasury, and the resulting additive score adjustment.
- **R/R (Risk/Reward ratio)**: Expected gain ÷ expected loss on a trade; this framework requires ≥2:1 to enter.
- **ROIC**: Return on Invested Capital.
- **Rule 0 / Rule 6 / Rule 9 / Rule 10**: This framework's standing instructions to always fetch a live price first; normalize distorted earnings before valuing; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline.
- **Structural Quality Override**: Suspends the Historical PE Modifier's "expensive" penalty when a richer multiple reflects genuine business improvement rather than euphoria (does not block the "cheap" credit).
- **TAM**: Total Addressable Market.
- **Terminal Value**: The lump-sum value assigned to all DCF cash flows beyond the explicit forecast period.
- **TTM**: Trailing Twelve Months.
- **Upside/Downside Modifier (Expected-Return Modifier)**: The additive ±15 adjustment based on expected annual return vs. the 10% hurdle.
- **Valuation Score**: This framework's 0.0–100.0 score (lower = cheaper) combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.
- **WACC**: Weighted Average Cost of Capital — the DCF discount rate.

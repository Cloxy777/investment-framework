# RESCORE — GOOG (Alphabet Inc., Class C) — 2026-11-12

**Task type:** RESCORE (mode `--both`)
**Date:** 12 Nov 2026
**Trigger:** Manual `/rescore GOOG`. **No new filing** since Q3 FY2026 (reported 28 Oct, scored 2026-10-29) — this is a market-data refresh (price, forward EPS, 10Y), not an earnings rescore. All TTM financial inputs are carried unchanged from [2026-10-29](2026-10-29-rescore-goog.md) (Rule 6-normalised TTM NI $136,594M, EBIT $173,359M, FCF $19,747M, SBC $30,409M — vendor `fetch_fundamentals` FCF/SBC now match those figures).
**10Y US Treasury:** 5.07% (Yahoo ^TNX, 12 Nov intraday; 11 Nov close 4.998%). **Knife-edge on the 5.00% line again** — sensitivity below.
**Position:** 1 share, IBKR, 0.61% of portfolio (holdings.md), avg cost $295.70 (≈ breakeven).
**Last review:** 29 Oct 2026 (Valuation 37.1, Quality 70.7, HOLD).

*GOOG = Alphabet Class C (no votes); economics same as GOOGL.*

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price** | **$295.53** (bid 295.49 / ask 295.60), +1.69% on day | IBKR `get_price_snapshot` (contract_id 208813720) |
| Cross-check | Yahoo currentPrice 295.51, prev close 290.63 | yfinance |
| 52-wk range | $270.87 – $404.23 | IBKR |
| Move since 29 Oct | $282.74 → $295.53 = **+4.5%** | explained by nothing fundamental; no Rule 9 trigger |
| Forward EPS (NTM consensus) | $15.435 (was $15.311) | Yahoo; PT mean $393.9 / median $380 (n=14) |

## 2. fetch_fundamentals output (pasted)

```
Market Cap = 3,632,508,174,336 | Forward PE = 19.143 | FCF Yield 0.544% | Gross Margin 60.857% | Revenue 3yr CAGR 12.512%
FCF/NI annual (oldest first) = [100.1%, 94.2%, 72.7%, 55.4%] | FCF positive 3yr+ = True
5yr PE avg/low/high = 24.612 / 18.181 / 35.452 (n=20 quarters)
SBC block: SBC 30,409M vs FCF 19,747M -> SBC/FCF = 154.0% (SEVERE) | FCF yield after SBC = -0.29%
Advisory flags: cycle_peak UNKNOWN | value_trap_candidate UNKNOWN
```
Vendor EV/EBIT 11.96, net margin 50.0%, ROIC 51.6% are **gain-distorted** (equity-securities gains in 2026 TTM) — not used; scoring uses the Rule 6-normalised figures from 10-29.

**Advisory flags:** `flags_common --eps-now 19.16 --forward-pe 19.147 --eps-growth 27.7` → `cycle_peak UNKNOWN` (data gap: EPS TTM a year ago unavailable; moot — headline GAAP EPS is gain-inflated), `multiple_ceiling NONE`, `value_trap_candidate UNKNOWN` (data gap: trailing EPS growth; fwd PE 19.1 > 15 and consensus EPS growth +28% make it a poor fit). SBC block handled as a hard disqualifier in §3.

## 3. Quality Score

Inputs unchanged from 10-29 (no new filing). **Script as-is:**
```
# FAILS GATE
Reason: SBC 30,409 is >= 100% of TTM FCF 19,747 (or FCF <= 0) with no documented one-off explanation
```
Not waived — AI-capex-driven FCF compression is not a one-off. **Reference sub-scores** (waiver flag set only to display arithmetic, NOT a real waiver):
```
Profitability: NetMargin 28.99% -> 96.63 ; ROIC 26.84% -> 89.47 ; score 93.05
Margins: GM 60.86% -> 76.08
Growth: 12.51% CAGR -> 50.04 ; +10 TAM (Cloud +103%, $561B backlog) -> 60.04
Balance sheet: ND/EBITDA -0.695x -> 100.00
Moat: 3/5 TRUE -> 60.00
FCF Quality: (FCF-SBC)/NI = -7.8% -> 0.00
Quality Score = 70.682 -> 70.7
```
# Quality Score = 70.7 (reference) — FAILS 80.0 gate + SBC≥FCF hard DQ. Unchanged. Phase 04 Quality Watch stays escalated; existing holding not force-exited on quality alone.

## 4. Valuation Score (script output)

Inputs: Owner Earnings yield = 136,594 / (295.53 × 12,294M = 3,633,246) = **3.76%**; EV = 3,633,246 + 19,000 pref + 125,102 debt − 265,098 cash = 3,512,250 → EV/EBIT **20.26×**; Fwd PE 295.53/15.435 = **19.147×**; PEG not scored (gain-distorted growth base, per 07-22 ruling); scenarios: bull 15.435×1.07×28 = $462.44, base 15.435×24.612 = $379.89, bear $247.00 (held).

```
FCF_Score = clamp(100x(1 - 3.7600/10)) = 62.400   [Owner Earnings basis]
EV/EBIT_Score = clamp((20.26 - 12)/23 x 100) = 35.913
FwdPE raw = 5.593 ; deviation vs 24.612 avg = -22.205% -> Historical PE Modifier -10 -> FwdPE_Score 0.000
PEG n/a -> weights 40/40/20
Rate gate: EY 5.2228% - 10Y 5.07% = 0.1528pp (<1.5) -> Step 1 +5 ; 10Y >5% -> Step 2 +10 ; total +15
PW FV = 0.25x462.44 + 0.50x379.89 + 0.25x247.0 = 367.305 ; gap +24.29% ; annualised (2yr) 12.14%/yr
E = 12.1434 + 12.0 + 0.460 (div 0.298 + gross buyback 0.162) = 24.60%/yr -> M = -14.603
Raw = 39.325 ; Final = 39.325 + 15 - 14.603 = 39.722 -> 39.7
```
# Valuation Score = 39.7 (was 37.1: price +4.5%, partly offset by +0.8% forward EPS)

Sensitivities (script re-runs): 10Y = 4.998% (11 Nov close) → Step 2 +5 → **34.7**; base FV at today's price ($295.53) → **46.9**. All stay in the sub-50 band; action identical.

## 5. Composite Score
`composite_score --set quality_score=70.7 --set valuation_score=39.7` → `Composite Score REFUSED — Quality 70.7 < 80.0`. Hand-calc reference only: 0.50×(100−70.7)+0.50×39.7 = 14.65+19.85 = **34.5 — not actionable**.

## 6. Action
**HOLD — 1 share, no add / trim / exit.** Cheap numerically but gate-failing and SBC≥FCF-disqualified: framework doesn't buy those. No trim (valuation far below 70). No exit trigger; +4.5% move on no news is far below the 15% unexplained-move trigger. Order setup N/A (HOLD).

## 7. Stale-score mechanism
`python -m scripts.stale_score --apply` → `{"newly_stale": [], "resolved": []}` (GOOG was not stale). Script rewrote STALE.md with a duplicate header row; reverted as noise.

## 8. Next review trigger
Alphabet Q4/FY2026 earnings (~3 Feb 2027). Earlier on a Rule 9 event. Watch: Search growth ex-FX (≤12% again → −10 Growth deduction, Quality ≈68.7); FCF vs SBC; buyback resumption; ATM dilution; 10Y vs 5.00% line (±5 pts).

## Glossary
- **Composite Score**: 0.50×(100−Quality)+0.50×Valuation; only valid if Quality ≥ 80.0.
- **EV/EBIT**: Enterprise value ÷ operating profit.
- **Forward PE**: Price ÷ next-12-month expected EPS.
- **FCF / FCF Yield**: Operating cash flow minus CapEx / divided by market cap.
- **Hard disqualifier**: Rule failing a company regardless of weighted score.
- **Owner Earnings**: Net income + D&A − maintenance CapEx; used for growth-capex reinvestors (Upgrade 1).
- **PEG**: PE ÷ EPS growth rate.
- **Quality Score**: 0–100.0 grade; 80.0+ is the gate.
- **Rate Environment Gate / Rate Regime Modifier**: Compares earnings yield to the 10Y Treasury; adds points when rates are high.
- **Rule 0 / 6 / 9**: Fetch live price first / normalise one-offs / forced re-valuation on events.
- **SBC**: Stock-based compensation; treated as a real cost.
- **TTM**: Trailing twelve months.
- **Valuation Score**: 0–100.0 (lower = cheaper).

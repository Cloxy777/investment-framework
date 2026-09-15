# RESCORE — AVGO (Broadcom Inc.) — 2026-09-15

**Task type:** RESCORE (mode `--both`)
**Trigger:** User-requested fresh rescore, 12 days after the 2026-09-03 session — not tied to a new earnings event. Treated as a full re-run per instructions: live data re-fetched throughout, but genuinely unchanged fundamental inputs (TTM financials, Quality Score sub-scores) are carried forward with the same "flagged, carried forward" discipline as prior sessions, since no new 8-K has been filed since 2026-09-02 (verified directly against SEC EDGAR's 8-K filing list for CIK 0001730168 — the 2026-09-02 Q3 FY2026 earnings 8-K remains the most recent filing).
**Date:** 15 Sep 2026
**10Y US Treasury Yield:** **5.018%** (WebFetch: TradingEconomics, 15 Sep 2026 reading) — cross-checked via WebSearch (CNBC, NBC News, Seoul Economic Daily): the 10-year yield **crossed 5% for the first time since October 2023** on 14–15 Sep 2026, a fifth consecutive up-session driven by an oil price spike (Saudi pipeline shutdown, Strait of Hormuz talks postponed) feeding inflation fears, with markets pricing a ~89–90% probability of a Fed rate hike at this week's meeting — a genuine macro regime shift since the 2026-09-03 session's 4.79% reading, **not** a data artifact.
**Rate Regime Modifier (Step 2):** **+10** (10Y now in the >5% bracket — up from +5 in the 3.5–5% bracket on 2026-09-03; this is the first time this bracket has applied in this ticker's rescoring history)
**Current AVGO portfolio weight:** 3.49% per [holdings.md](../portfolio/holdings.md) (2026-09-13 sync; not re-synced this session — refreshing live weight is `/sync-portfolio`'s job, out of `/rescore`'s scope) — still held as an **open, unresolved Human Override**
**Sector:** Semiconductors (fabless — AI accelerators/networking) + Infrastructure Software (VMware)
**Last review:** 03 Sep 2026 (Valuation 66.6 / Quality 86.3 / Composite 40.2) — see [session](../sessions/2026-09-03-rescore-avgo.md)

---

## 0. Override status (reported, not resolved this session)

Per [override-log.md](../portfolio/override-log.md): AVGO's **2026-06-16 override remains open** — still "Open — under review," no rationale supplied. Unchanged since the last session. Not this command's scope to resolve.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$345.55** | IBKR `get_price_snapshot` (contract_id 313130367, NASDAQ), **REALTIME** status, ts 2026-09-15 04:21:47 UTC. Cross-validated against `yfinance`'s `currentPrice` field, reading **$344.72** — within 0.24%, immaterial. |
| ⚠️ Pre-market flag | Queried ~04:22 UTC, before regular NASDAQ trading hours (opens 13:30 UTC / 9:30am ET) — a real-time indicative pre-market quote, not a regular-session trade. Flagged per Rule 0 discipline (same practice as the 2026-09-03 session). |
| Prior close used by IBKR's own `change` field | Not returned this call (empty `prior-close` object); `change` field shows +$0.83 (+0.24%) vs. an unreturned reference — treated as informational only, not relied upon. | IBKR `get_price_snapshot` |
| `yfinance` `previousClose` | $361.99 (11 Sep 2026 regular close) | Confirms a real, disclosed **−4.5% move from Friday's close to this pre-market quote** — consistent with the broad rate-driven selloff described below, not company-specific news. |
| 52-week range | $289.96 – $495.00 (IBKR `misc_statistics`) | Unchanged from the 2026-09-03 session. |
| Analyst consensus PT | $531.85 (`yfinance`, 47 analysts) / $533.41 (WebSearch, 49-analyst count) — essentially unchanged from the 2026-09-03 session's $525.97, modestly **higher** | Consistent with Benzinga's post-earnings coverage: "these analysts increase their forecasts on Broadcom following upbeat Q3 earnings" (Cantor Fitzgerald's C.J. Muse raised his target to $600 from $525 on 3 Sep 2026). |
| Reaction context (WebSearch: CNBC, NBC News) | AVGO's decline since the last rescore is **not** an AVGO-specific event — it tracks a broad rate-driven selloff: the 10-year Treasury yield topped 5% for the first time since Oct 2023 (oil price spike on a Saudi pipeline shutdown/Strait of Hormuz talks postponement, feeding inflation fears and a ~89–90%-priced Fed hike this week). Schwab's market commentary separately flagged Monday (14 Sep) as a "grim" session for tech broadly, citing AI-spending-durability fears. AVGO is down ~14.6% over the past month per public.com's forecast page despite the strong Q3 beat — a macro/multiple-compression move, not a fundamental deterioration. | [CNBC](https://www.cnbc.com/2026/09/14/10-year-us-treasury-is-closing-in-on-5percent.html), [NBC News](https://www.nbcnews.com/business/business-news/diesel-oil-prices-jump-saudi-pipeline-shut-hormuz-talks-postponed-iran-rcna597579) |
| Move since last rescore | $359.00 (3 Sep) → $345.55 (15 Sep) = **−3.75%** | Well under the 15% Rule 9 unexplained-move threshold on its own; this session is user-requested, not price-triggered. |

---

## 2. Data Gathered — Sources & Gaps

**No new 8-K since the 2026-09-02 Q3 FY2026 earnings release** — confirmed directly via SEC EDGAR's 8-K filing index for CIK 0001730168 (most recent filing remains 2026-09-02, accession 0001730168-26-000076; no filing since). Per the task instructions, the TTM window is **not** rolled forward this session — every TTM/fundamental figure below is carried forward unchanged from the 2026-09-03 session (verified as the correct, most-recent set, not re-derived from scratch), and only live-price-dependent figures are refreshed.

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
| Diluted shares (Q3FY26, GAAP basis) | 4,887M | Carried forward — used consistently for Market Cap/EV across all four AVGO sessions to date. **Flag:** `yfinance`'s `sharesOutstanding` field now reads 4,773.6M (a *basic*, more current count, not the diluted weighted-average from the 8-K) — a ~2.3% difference. Kept the diluted 8-K figure for methodological continuity with every prior AVGO session's EV/EBIT, FCF Yield, and DCF math; noting the gap rather than silently blending bases. |
| Forward EPS | **$19.384** (fresh, `yfinance` `forwardEps`) | Refreshed — down slightly from $19.448 on 2026-09-03 (normal drift in the consensus estimate, not a new data point being rolled in) |
| Forward PE | **17.83×** ($345.55 ÷ $19.384) | Refreshed |
| 5yr PE range (reconstructed) | Avg 29.9465×, Low 13.3897×, High 52.8544× (n=20 quarters) — **⚠️ still unchanged, still flagged as a data gap, now for a 2nd consecutive session** | `yfinance`'s `get_earnings_dates` was checked fresh this session — the 2026-09-02 earnings-date row **still** shows `Reported EPS = NaN` (has not backfilled). Per Rule 0's explicit fallback instruction, kept the most recently verified prior value. Flag carried to the next rescore. |
| Beta | 1.457 | Refreshed (`yfinance` `info.beta`) — down slightly from 1.473 on 2026-09-03, normal drift in this slow-moving statistical parameter |
| Effective tax rate (normalized) | 21% carried forward, flagged | Unchanged — no new "clean" quarter since 2026-09-03 |
| VMware/intangible amortization add-back | $9.3B/yr carried forward, flagged | Unchanged — see 2026-09-03 session for full reasoning |
| Dividend | $0.65/quarter ($2.60/yr annualized) | Unchanged — record date 21 Sep 2026, payable 30 Sep 2026 (confirmed via SEC EDGAR 8-K text, no change to the rate) |

**No metric was invented or estimated.** Every fresh figure traces to IBKR's live snapshot, `yfinance`'s live fields, or WebSearch/WebFetch cross-checks against TradingEconomics/CNBC/NBC News; every carried-forward figure is explicitly flagged with the reason it wasn't independently re-derived this session.

---

## 3. Quality Score (Phase 01 gate) — recomputed, inputs unchanged

**Hard disqualifier check (re-verified, unchanged):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | TTM 102.97% | disqualify if <70% for 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | 0.687× | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2023–FY2025 all positive, FY2026 trending strongly positive | disqualify if not | ✅ PASS |

```
Net Margin (TTM) = 38,265/89,104 = 42.944%
NetMargin_Component = clamp((42.944/30)×100, 0, 100) = 100.0   (saturates)

Normalized EBIT = 42,814 + 9,300 (carried-forward amortization add-back) = 52,114M
NOPAT = 52,114 × (1 − 0.21) = 41,170.1M
Net Invested Capital = Total Debt 59,419 + Total Equity 99,690 − Cash 23,975 = 135,134M
ROIC = 41,170.1 / 135,134 = 30.47%
ROIC_Component = clamp((30.47/30)×100, 0, 100) = 100.0   (saturates)

Profitability_Score = (100.0 + 100.0) / 2 = 100.0

GrossMargin_Score = clamp((68.77/80)×100, 0, 100) = 86.0   (no trend bonus)

Revenue 3yr CAGR (FY2022→FY2025, unchanged) = 24.38%
Growth_Score = clamp((24.38/25)×100, 0, 100) = 97.5 + 10 (TAM evidence, carried forward) = 100.0   (saturates)

BalanceSheet_Score = clamp(100×(1 − 0.687/4), 0, 100) = 82.8

Moat_Score = (2/5 signals TRUE) × 100 = 40.0   (unchanged evidentiary basis)

FCFQuality_Score = clamp(((1.0297 − 0.40)/0.60)×100, 0, 100) = 100.0   (saturates)

Quality Score = 100.0×0.25 + 86.0×0.15 + 100.0×0.20 + 82.8×0.15 + 40.0×0.15 + 100.0×0.10
              = 25.00 + 12.90 + 20.00 + 12.42 + 6.00 + 10.00
              = 86.32 → 86.3
```

**Quality Score = 86.3 — unchanged from 2026-09-03**, exactly as expected: every input to this score is a fundamental/TTM figure, none of which moved (no new 8-K). Clears the 80.0+ gate comfortably (sensitivity check carried forward from 2026-09-03: even the most conservative moat reading, Moat_Score = 0, still gives 80.3 — still clears).

**No new TAM/pricing-power or moat-signal evidence surfaced this session** — this rescore's news flow was macro (rates/oil), not AVGO-specific. Both qualitative modifiers stay on their existing, cited evidentiary basis.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $345.55 / $19.384 = 17.8266×
EY = 1 / 17.8266 = 5.6096%
Spread = EY − 10Y Treasury = 5.6096% − 5.018% = +0.5916pp
```
Spread (+0.59pp) < +1.5% → **fails** → **+5 additive** (yellow flag, not a veto). Same qualitative result as 2026-09-03, though the margin narrowed slightly (0.63pp → 0.59pp) as the 10Y rose faster than the earnings yield improved on the lower price.

**Step 2 — Rate Regime Modifier**
10Y = 5.018% → **>5% bracket** → **+10** — a **genuine regime change** from the 3.5–5% bracket (+5) that applied at every AVGO session since 2026-07-04. The 10Y crossing 5% (first time since Oct 2023, confirmed via multiple independent sources in §1) is a real, dated macro event, not noise.

**Combined Rate Modifier: +15** (up from +10 on 2026-09-03 — the single largest driver of this session's valuation-score move, see §7)

---

## 5. Valuation Score (Phase 02)

### FCF Yield (40% weight)

```
Market Cap = $345.55 × 4,887M shares = $1,688,702.9M
FCF Yield  = $39,403M / $1,688,702.9M = 2.333%
FCF_Score  = clamp(100×(1 − 2.333/10), 0, 100) = 76.7
```
Slightly more attractive than 2026-09-03's 77.5 (lower price, same TTM FCF).

### EV/EBIT (weight 25% base, redistributed to 40% — PEG still not applicable)

```
EV = Market Cap $1,688,702.9M + Net Debt $35,444M = $1,724,146.9M
EV/EBIT (GAAP TTM) = $1,724,146.9M / $42,814M = 40.27×
EV/EBIT_Score = clamp((40.27 − 12)/23 × 100, 0, 100) = 100.0   (saturates, well above the 35× ceiling)
```

**Normalization check (same flag carried from 2026-09-03):** Normalized EBIT = $52,114M → normalized EV/EBIT = **33.08×** — now further **below** the 35× ceiling than on 2026-09-03 (34.35×), as the falling price pulls the normalized multiple away from saturation. Normalized EV/EBIT_Score = 91.7 (vs. 97.2 on 2026-09-03) — the GAAP-vs-normalized gap that was flagged as "no longer moot" last session continues to widen. **Kept GAAP basis as primary (EV/EBIT_Score = 100.0)** for continuity; using the normalized 91.7 instead would move the raw weighted score down modestly (final Valuation Score ~67.6 instead of 70.9) but not the Composite action band. Flagged again for future attention.

### Forward PE + Historical PE Modifier (20% weight)

```
Forward PE = 17.8266×, 5yr Low = 13.3897×, 5yr High = 52.8544× (carried forward, flagged §2)
FwdPE_Score (raw) = clamp((17.8266 − 13.3897)/(52.8544 − 13.3897) × 100, 0, 100) = 11.2
```
**Historical PE Modifier (Upgrade 2):** Forward PE vs 5yr avg (29.9465×): (17.8266 − 29.9465)/29.9465 × 100 = **−40.47%** (>20% below) → **−10**.
```
FwdPE_Score = 11.2 − 10 = 1.2
```

### PEG (15% weight) — Fast-Grower eligibility ruling carried forward

No new information this session to revisit the ruling (same GAAP-EPS-distortion basis as every prior AVGO session). **PEG not scored; its 15% weight redistributed to EV/EBIT (→ 40%).**

### Raw Weighted Score

```
Raw = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
    = (76.7 × 0.40) + (100.0 × 0.40) + (1.2 × 0.20)
    = 30.68 + 40.00 + 0.25
    = 70.93 → 70.9
```
Essentially flat vs. 2026-09-03's 71.6 (a slightly cheaper name on every sub-score, rounding to almost the same raw total).

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

Same scenario architecture and multiple assumptions as the last four sessions (34×/25×/15× bull/base/bear; no new information to justify revising them — Q3's AI-semi acceleration remains the most recent, still-current fundamental evidence), refreshed for the current price, forward EPS, and a slightly shorter catalyst window (12 fewer days to the same FY2027 confirmation point).

**Step 1 — scenario fair values.** NTM EPS estimate: **$19.384** (`yfinance` forward EPS, refreshed).

| Scenario | Wt | Assumption | EPS basis | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | AI ramp continues to beat, re-rate | $19.384 × 1.10 = $21.322 | 34× | **$724.96** |
| Base | 50% | Consensus AI ramp, multiple eases below 5yr avg (29.95×) | $19.384 | 25× | **$484.60** |
| Bear | 25% | AI capex slowdown / hyperscaler in-sourcing, de-rate | $19.384 × 0.85 = $16.476 | 15× | **$247.15** |

```
PW Fair Value (multiples) = 0.25×724.96 + 0.50×484.60 + 0.25×247.15 = $485.33
Gap Upside % = 485.33 / 345.55 − 1 = +40.45%
```

**Step 2 — catalyst & annualization (Rule 10).** Same documented catalyst: management's FY2027 AI-semiconductor revenue target (>$100B), confirmation expected ~Dec 2027 results. From today (15 Sep 2026) to that point is **~14.9 months ≈ 1.24 years** (slightly shorter than the 1.25yr used 2026-09-03, purely the passage of 12 days) — Guardrail 1 satisfied, no cap needed.
```
Annualized gap = 40.45% / 1.24 = 32.62%
```
**Step 3 — expected annual return E.**
```
E = annualized gap (32.62%) + intrinsic growth (12%, carried forward, flagged) + shareholder yield ($2.60/$345.55 = 0.75%)
  = 32.62 + 12.0 + 0.75 = 45.37%
```
**Step 4 — map E to M** (hurdle H = 10%):
```
E (45.37%) ≥ H → M = −15 × clamp((45.37 − 10)/15, 0, 1) = −15 × clamp(2.36, 0, 1) = −15.0
```
**Upside/Downside Modifier M = −15.0 (fully saturated at the cap)** — same as every AVGO session since 2026-07-04. The falling price against an unchanged fundamental picture widens the gap further; the shorter catalyst window amplifies the annualized figure further still.

---

## 7. Final Valuation Score

```
Final Score = Raw Weighted (70.93) + Rate Modifier (+15) + Upside/Downside Modifier (−15.0)
            = 70.93 → 70.9
```

**Valuation Score = 70.9 — "TRIM 25–30%" band (70.0–79.9)** per the raw Action Table — a **material band change from 2026-09-03's 66.6 ("Fair Value," 50.0–69.9)**, and the **first time in this ticker's rescoring history the raw Valuation Score alone has crossed into a trim band.**

**⚠️ Important: this move is driven almost entirely by the Rate Environment Gate, not by AVGO's own fundamentals or price action.** Decomposing the 4.3-point increase (66.6 → 70.9):
- Raw weighted sub-scores: 71.6 → 70.9 (−0.7, cheaper — the lower price pulled FCF Yield and the FwdPE raw score slightly more attractive)
- Rate Modifier: +10 → +15 (**+5**, the 10Y crossing 5% for the first time since Oct 2023)
- Upside/Downside Modifier: unchanged at the −15.0 cap (already fully saturated both sessions)

The entire net move (+4.3) is more than explained by the +5 Rate Regime Modifier step alone — AVGO's own numbers, if anything, got slightly cheaper. This is the Rate Environment Gate doing exactly what it's designed to do (raising the bar in a higher-rate regime), not a signal about AVGO specifically. See §8 for why this does **not**, by itself, flip the action recommendation.

---

## 8. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 86.3) + 0.50 × 70.9
                = 0.50 × 13.7 + 35.45
                = 6.85 + 35.45
                = 42.30 → 42.3
```

**Composite Score = 42.3 — stays in the "Cheap" (30.0–49.9) band**, up (less attractive) from 40.2 on 2026-09-03, but **not** enough to cross into the 50.0–69.9 "Hold" band, let alone the 70.0–79.9 trim band the raw Valuation Score alone would imply.

**Per [valuation-scoring.md](../framework/valuation-scoring.md)'s explicit instruction, the Composite Score — not the raw Valuation Score — governs the Phase 03/05 action table once a Quality Score is on file.** AVGO's still-strong 86.3 Quality Score (unchanged, §3) is exactly what the Composite blend is designed to do here: it absorbs a rate-driven valuation-score shock that has nothing to do with the business itself, keeping a high-quality name from being mechanically pushed toward a trim recommendation by a macro event. Worth flagging explicitly (no black-box outputs) rather than only reporting the blended number.

---

## 9. Action Recommendation & Order Setup

Composite Score 42.3 stays in the **30.0–49.9 "Cheap" → Standard position 3–5%** band — nominally BUY-eligible. Full order setup run below, per the operating brief.

### Fair Value — two methods, triangulated (Rule 1: Tech/Growth → DCF primary, Multiples secondary)

**Method A — 3-Stage DCF (Rule 2).** Same 10-year growth-fade schedule as prior sessions, rebased on the unchanged $39,403M TTM FCF and a WACC refreshed for the current beta/Treasury yield:

```
WACC build:
  Cost of equity = Rf (5.018%) + Beta (1.457) × ERP (5.0%, assumed) = 12.303%
  Cost of debt (pretax) = TTM interest expense $3,116M / Total Debt $59,419M = 5.244%; after-tax (21%) = 4.143%
  Weights: E/(D+E) = 96.60% (Market Cap $1,688,702.9M), D/(D+E) = 3.40% (Debt $59,419M)
  WACC = 96.60%×12.303% + 3.40%×4.143% = 12.026%

Stage 1 (yrs 1–5), FCF base $39,403M, same growth path as prior sessions:
  y1 +25% → $49,253.8M | y2 +20% → $59,104.5M | y3 +15% → $67,970.2M | y4 +12% → $76,126.6M | y5 +10% → $83,739.3M

Stage 2 (yrs 6–10), linear fade from 10% to the 2.5% terminal rate:
  y6 $90,857.1M | y7 $97,217.1M | y8 $102,564.0M | y9 $106,666.6M | y10 $109,333.3M

Terminal Value (at y10) = $109,333.3M × 1.025 / (0.12026 − 0.025) = $1,176,473.7M
Terminal Value as % of total DCF value = 46.2% (well under the 75% Rule 4 sanity cap)

Sum of discounted FCFs (yrs 1–10) = $439,935.9M
PV of Terminal Value = $377,927.1M
Enterprise Value (DCF) = $817,863.0M
Equity Value = $817,863.0M − Net Debt $35,444M = $782,419.0M
DCF Fair Value / share = $782,419.0M / 4,887M = $160.10
```
(Down modestly from $162.70 on 2026-09-03 — a slightly higher WACC, purely on the higher risk-free rate, more than offsetting the slightly lower beta.)

**Method B — Scenario-weighted multiples (§6 PW Fair Value):** **$485.33**

**⚠️ Same material finding as prior sessions — wide divergence between the two methods**, same underlying tension: a disciplined GDP-terminal-growth DCF vs. AVGO's own trailing 5-year PE range.

```
Triangulation (Rule 3, Tech/Growth weights): Blended FV = 40% × DCF + 60% × Multiples
                                            = 0.40 × $160.10 + 0.60 × $485.33
                                            = $64.04 + $291.20
                                            = $355.24
```

### Order Setup Checklist

```
[✓] Composite Score (incl. Quality blend):    42.3 — "Cheap" (30.0–49.9 band)
[✓] Expected annual return E / catalyst:      +45.37% / 1.24yr (feeds the Upside/Downside Modifier, §6)
[✓] Upside/Downside Modifier applied:         −15.0
[✓] DCF Fair Value:                           $160.10
[✓] Multiples-Based Fair Value:               $485.33
[✓] Blended Fair Value:                       $355.24
[ ] Margin of Safety %:                       25–30% (Composite 30.0–49.9 band)
    Buy Price range: $248.67 (30% MoS) – $266.43 (25% MoS)
[✓] PRIMARY SELL TARGET:                      $355.24 (Blended FV, baseline)
[✓] BULL-CASE TRIM TARGET:                    $724.96 × 0.90 = $652.46
[ ] STOP LOSS: 25–30% max loss from Buy Price
    Range: $174.07 – $199.82 depending on MoS/stop combination
[✗] Risk/Reward Ratio — checked across the full 25–30% MoS × 25–30% stop matrix:
      MoS 25%/Stop 25%: 1.33:1   MoS 25%/Stop 30%: 1.11:1
      MoS 30%/Stop 25%: 1.71:1   MoS 30%/Stop 30%: 1.43:1
    Best case in the applicable range (1.71:1) still — FAILS the 2:1 minimum throughout.
```

**Per fair-value-methodology.md Step 6: R/R fails the minimum threshold across the entire applicable MoS/stop range. No order is placed.**

**Position sizing is also moot for a different reason:** AVGO's current 3.49% weight already sits **within** the Composite Score's implied 3–5% "Standard position" target band — no sizing gap to fill even before the R/R gate is considered.

### Net Action: **HOLD** — maintain the current 6-share position as-is

- No trim: Composite Score (42.3) is far below any trim threshold (70.0+) — and per §8, the Composite (not the raw Valuation Score's 70.9) is the number the action table runs against.
- No add: R/R on the computed order setup fails the 2:1 minimum (best case 1.71:1), and the position is already within its Composite-Score-implied target size.
- **The open 2026-06-16 override remains unresolved** (§0) — unchanged by this rescore.

**Same action band as the 2026-09-03 session (HOLD)** — the underlying picture is essentially unchanged on the fundamentals side (Quality Score identical at 86.3, TTM data unchanged), with the raw Valuation Score moving materially (66.6→70.9) purely on the Rate Environment Gate's regime shift (10Y crossing 5% for the first time since 2023) rather than any AVGO-specific development. This is the Composite Score construct working as designed: a still-excellent business isn't mechanically pushed toward a trim recommendation by a macro rate shock alone.

---

## 10. Next Review Trigger

**Date/event:** AVGO's Q4 FY2026 earnings release (expected ~December 2026, per the typical AVGO reporting cadence) — re-run Phase 01/02 with refreshed TTM figures. **Three specific follow-ups flagged, worth checking first at that rescore:**
1. **Re-verify the 5yr PE range** once `yfinance`'s `get_earnings_dates` backfills the 2026-09-02 print — still flagged unchanged/stale for a 2nd consecutive session (§2).
2. **Watch the EV/EBIT GAAP-vs-normalized divergence** (§5) — the gap widened again this session (normalized 33.08× vs. the 35× ceiling, further below than 2026-09-03's 34.35×). If this keeps widening, the choice of basis will eventually move the actual score, not just a footnote — worth a `decisions/` entry if it starts to matter for the action band.
3. **Monitor the Rate Environment regime.** The 10Y crossing 5% is fresh (this week) and tied to an active Fed decision and an ongoing oil-price/geopolitical event (Saudi pipeline, Strait of Hormuz) — if the 10Y falls back under 5% before the next scheduled rescore, the Rate Regime Modifier reverts to +5 and the raw Valuation Score would fall back toward the 66–67 range documented on 2026-09-03, all else equal. Not a reason to rescore early on its own (Rule 9 doesn't list rate moves alone as a trigger for names without a Turnaround/Debt-Gate dependency), but worth noting as context for why this session's headline Valuation Score number moved when the fundamentals didn't.

Earlier trigger on a >15% unexplained move from $345.55 (Rule 9), a further guidance revision/M&A/management change, or new third-party market-share data that would firm up the Moat_Score's remaining evidentiary gap. **Separately and unconditionally: the 2026-06-16 override still needs the user to supply a rationale** for `decisions/` and `override-log.md` — not tied to any valuation trigger.

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

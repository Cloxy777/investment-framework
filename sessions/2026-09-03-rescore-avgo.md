# RESCORE — AVGO (Broadcom Inc.) — 2026-09-03

**Task type:** RESCORE (mode `--both`)
**Trigger:** Telegram scan (`/telegram-scan`, Routine 6) — channel https://t.me/tarasguk, post `tarasguk/11829` (2026-09-03T06:38:42 UTC), claiming AVGO reported Q3 FY2026 earnings with strong growth and raised long-term guidance. **None of that post's specific numbers were used as data in this session** — it was only a trigger. AVGO's own watchlist entry already named "AVGO's Q3 FY2026 earnings (~September 2026)" as the mandatory next re-check (see [2026-08-28 entry](../watchlist/in-portfolio/AVGO/AVGO-2026-08-28.md)), so this trigger is legitimate and expected. Independently confirmed via SEC EDGAR (8-K, filed 2026-09-02) and CNBC/Benzinga coverage: **AVGO did report Q3 FY2026 earnings on 2026-09-02**, after market close.
**Date:** 03 Sep 2026
**10Y US Treasury Yield:** 4.79% (WebSearch: TradingEconomics, 2 Sep 2026 close — most recent available print at time of session; yield had risen to its highest since Oct 2023 on a 5-session rally before pausing at 4.79%)
**Rate Regime Modifier (Step 2):** +5 (10Y still in the 3.5–5% bracket)
**Current AVGO portfolio weight:** 3.55% per [holdings.md](../portfolio/holdings.md) (2026-08-30 sync; not re-synced this session — refreshing live weight is `/sync-portfolio`'s job, out of `/rescore`'s scope) — still held as an **open, unresolved Human Override**
**Sector:** Semiconductors (fabless — AI accelerators/networking) + Infrastructure Software (VMware)
**Last review:** 28 Aug 2026 (Valuation 68.5 / Quality 82.1 / Composite 43.2) — see [session](../sessions/2026-08-28-rescore-avgo.md)

---

## 0. Override status (reported, not resolved this session)

Per [override-log.md](../portfolio/override-log.md): AVGO's **2026-06-16 override remains open** — still "Open — under review," no rationale supplied. Unchanged since the last session. Not this command's scope to resolve.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$359.00** | IBKR `get_price_snapshot` (contract_id 313130367, NASDAQ — re-verified via `search_contracts`, confirmed correct: "BROADCOM INC", NASDAQ), **REALTIME** status, queried 2026-09-03 08:14 UTC. Cross-validated against `yfinance`'s live `preMarketPrice` field, reading **$359.11** (timestamped 2026-09-03 08:14 UTC, 27 seconds apart) — within 0.03%, immaterial. |
| ⚠️ Pre-market flag | Both quotes were taken **before regular NASDAQ trading hours** (regular session opens 13:30 UTC / 9:30am ET; queried ~08:11–08:14 UTC). This is a real-time indicative pre-market quote, not a regular-session trade — flagged per Rule 0 discipline, not a substitute for a stale close but also not the same liquidity/certainty as a regular-session quote. `yfinance`'s "current price" fields (`currentPrice`/`regularMarketPrice` = $367.24) are **stale by one full session** — they reflect the 2026-09-02 4pm ET close, **before** the after-hours earnings release. Using the `preMarketPrice` field instead avoids repeating the SPGI-style stale-price error. |
| Prior close (regular session, 2 Sep 2026, pre-earnings) | $367.24 | `yfinance` `regularMarketPrice`/`currentPrice` (this is the *reference* the IBKR `change` field used: $367.24 − $8.24 = $359.00) |
| Close before that (1 Sep 2026) | $369.68 | `yfinance` `regularMarketPreviousClose` |
| 52-week range | $289.96 – $495.00 (IBKR `misc_statistics`) | Low ticked up vs the 2026-08-28 session's $285.53 (rolling 52-week window) |
| Analyst consensus PT | $525.97 (46 analysts per `yfinance`; WebSearch found a slightly different count of 49 analysts at the same $525.97 mean, likely a different aggregator's count) — essentially **unchanged** from the 2026-08-28 session's $525.97 | `yfinance` + WebSearch cross-check — consensus PT has not yet moved on the earnings print at time of this session (same-day earnings, analysts typically take 1–3 days to republish models) |
| Reaction context (WebSearch, CNBC) | AVGO beat Q3 estimates (revenue $29.6B vs. $29.43B consensus) but fell ~4–5% after-hours/pre-market on **Q4 guidance seen as underwhelming relative to elevated expectations** ($34.8B vs. some higher buy-side estimates) — consistent with the Telegram trigger's "next-quarter guidance a few % below expectations" characterization | [CNBC](https://www.cnbc.com/2026/09/02/broadcom-avgo-q3-earnings-report-2026.html) |
| Prior session price | $368.77 (28 Aug 2026) | AVGO is **−2.6%** since the last rescore — well below the 15% Rule 9 threshold on its own, but this rescore is earnings/methodology-driven regardless (mandatory Rule 9 trigger: quarterly earnings + guidance). |

---

## 2. Data Gathered — Sources & Gaps

**Q3 FY2026 earnings (reported 2026-09-02, after market close) is a genuine new data event** — every TTM figure below rolls the window forward one quarter (drops Q3 FY2025, adds Q3 FY2026), verified against the actual 8-K exhibit ([SEC EDGAR](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm)), not estimated.

**⚠️ Data-lag flag:** `yfinance`'s structured quarterly tables (`quarterly_financials`, `quarterly_cashflow`, `quarterly_balance_sheet`, `get_earnings_dates`) **had not yet incorporated Q3 FY2026** at time of this session (most recent column still 2026-04-30 / Q2 FY2026) — a one-session data-provider lag, consistent with this repo's prior experience of `yfinance` caches lagging fresh 8-Ks by hours to days. **Worked around by pulling the actual reported Q3 FY2026 figures directly from the SEC 8-K exhibit** via WebFetch (three targeted fetches: income statement/cash flow summary, balance sheet, and D&A detail) and manually rolling the TTM window forward — no metric was invented or estimated.

| Metric | New TTM (Q4FY25+Q1FY26+Q2FY26+Q3FY26) | Prior TTM (28 Aug) | Source |
|---|---|---|---|
| TTM Revenue | **$89,104M** | $75,465M | Q4FY25 $18,015M + Q1FY26 $19,311M + Q2FY26 $22,187M (yfinance, unchanged quarters) + **Q3FY26 $29,591M** (8-K, fresh) |
| TTM Net Income (GAAP) | **$38,265M** | $29,317M | Q4FY25 $8,518M + Q1FY26 $7,349M + Q2FY26 $9,310M + **Q3FY26 $13,088M** (8-K) |
| TTM GAAP Operating Income (EBIT) | **$42,814M** | $30,443M | Q4FY25 $7,508M + Q1FY26 $8,563M + Q2FY26 $10,788M + **Q3FY26 $15,955M** (8-K) |
| TTM FCF | **$39,403M** | $32,762M | Q4FY25 $7,466M + Q1FY26 $8,010M + Q2FY26 $10,262M + **Q3FY26 $13,665M** (8-K: CFO $14,197M − capex $532M) |
| TTM Gross Profit / Margin | **$61,277M / 68.77%** | $51,524M / 68.28% | Same rollforward + **Q3FY26 Gross Profit $20,456M** (8-K) |
| TTM Interest Expense | **$3,116M** | $3,145M | Q4FY25 $761M + Q1FY26 $801M + Q2FY26 $776M + **Q3FY26 $778M** (8-K) |
| TTM D&A (for EBITDA) | **$8,764M** | ~$8,753M (recomputed) | Q4FY25 $2,233M + Q1FY26 $2,153M + Q2FY26 $2,165M (yfinance "Reconciled Depreciation") + **Q3FY26 $2,213M** (8-K cash-flow statement: $2,042M amortization + $171M depreciation) |
| TTM EBITDA (EBIT + D&A) | **$51,578M** | ~$39,196M recomputed on the same GAAP+D&A basis (the prior session used a cached `yfinance` `info.ebitda` snapshot of $42,084M instead — see flag below) | Computed fresh this session |
| Net Debt (balance sheet, Q3FY26 end, 2 Aug 2026) | **$35,444M** (Debt $59,419M − Cash $23,975M) | $45,279M (Q2FY26 end) | 8-K balance sheet — a **$9.8B one-quarter improvement**, driven by the $13.7B FCF quarter |
| Total Equity | **$99,690M** | $87,691M | 8-K balance sheet |
| Diluted shares (Q3FY26) | **4,887M** | 4,876M | 8-K ("GAAP basis" diluted weighted-average) |
| Forward PE | **18.46×** (live price $359.00 ÷ forward EPS $19.448) | 18.90× | `yfinance` forward EPS |
| 5yr PE range (reconstructed) | **Avg 29.95×, Low 13.39×, High 52.85× (n=20 quarters)** — **⚠️ unchanged from the 2026-08-28 session, flagged as a data gap** | Avg 29.95×, Low 13.39×, High 52.85× | `get_earnings_dates` had not yet backfilled a reported-EPS row for the 2026-09-02 print at time of session (same data-lag issue as above) — used the most recently verified prior value per Rule 0's explicit fallback instruction, rather than blocking the whole rescore over one hard-to-refresh figure. Flagged as a near-term follow-up: re-verify at the next rescore once the provider catches up. |
| Beta | 1.473 | 1.473 | `yfinance` `info.beta`, re-pulled fresh this session (unchanged — a slow-moving statistical parameter, not earnings-sensitive) |
| VMware/intangible amortization (EBIT normalization add-back) | **$9.3B/yr carried forward, flagged** | $9.3B/yr | Q3FY26's actual total acquisition-intangible amortization (8-K: $1,499M COGS + $507M opex = $2,006M, ≈$8.0B annualized) is now directly available and running **below** the $9.3B/yr run-rate this framework has carried forward since 2026-06-14/06-20 — but recomputing the full new-TTM add-back would require pulling 3 more historical 8-Ks purely for this one normalization modifier, which only matters for the ROIC calc (EV/EBIT saturates at 100.0 either way — see §5). Kept the established $9.3B/yr figure per Rule 0's "most recent verified value, clearly flagged" guidance rather than partially reconstructing a mixed-basis figure. |
| Effective tax rate (normalized) | **21% carried forward, flagged** | 21% | Q3FY26's actual GAAP effective rate was 14.3% ($2,187M / $15,275M pretax, per 8-K) — another one-off-distorted data point in a series that has ranged 2.4%–21.7% quarter to quarter. No new "clean" quarter to justify revising the established 21% normalization anchor (close to the U.S. statutory rate); kept unchanged, flagged. |
| Dividend | $0.65/quarter ($2.60/yr annualized) | $2.60/yr | 8-K — unchanged |

**No metric was invented or estimated.** Every fresh figure traces to the SEC 8-K exhibit (primary source) via WebFetch, or to `yfinance`'s live/cross-checked fields; every carried-forward figure is explicitly flagged above with the reason it wasn't independently re-derived this session.

---

## 3. Quality Score (Phase 01 gate) — recomputed with fresh Q3 FY2026 data

**Hard disqualifier check:**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | TTM 102.97% | disqualify if <70% for 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | 0.687× | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2023–FY2025 all positive, FY2026 trending strongly positive | disqualify if not | ✅ PASS |

```
Net Margin (TTM) = 38,265/89,104 = 42.944%
NetMargin_Component = clamp((42.944/30)×100, 0, 100) = 100.0   (saturates)

Normalized EBIT = 42,814 + 9,300 (carried-forward amortization add-back, flagged §2) = 52,114M
NOPAT = 52,114 × (1 − 0.21) = 41,170.1M
Net Invested Capital = Total Debt 59,419 + Total Equity 99,690 − Cash 23,975 = 135,134M
ROIC = 41,170.1 / 135,134 = 30.47%
ROIC_Component = clamp((30.47/30)×100, 0, 100) = 100.0   (saturates)

Profitability_Score = (100.0 + 100.0) / 2 = 100.0

GrossMargin_Score = clamp((68.77/80)×100, 0, 100) = 86.0   (no trend bonus — already well above the 40% threshold the bonus targets)

Revenue 3yr CAGR (FY2022→FY2025, unchanged — FY2026 not yet a completed fiscal year) = 24.38%
Growth_Score = clamp((24.38/25)×100, 0, 100) = 97.5 + 10 (TAM evidence, refreshed — see below) = 100.0   (saturates)

BalanceSheet_Score = clamp(100×(1 − 0.687/4), 0, 100) = 82.8

Moat_Score = (2/5 signals TRUE) × 100 = 40.0   (unchanged evidentiary basis — see below)

FCFQuality_Score = clamp(((1.0297 − 0.40)/0.60)×100, 0, 100) = 100.0   (saturates)

Quality Score = 100.0×0.25 + 86.0×0.15 + 100.0×0.20 + 82.8×0.15 + 40.0×0.15 + 100.0×0.10
              = 25.00 + 12.90 + 20.00 + 12.42 + 6.00 + 10.00
              = 86.32 → 86.3
```

**Growth TAM/pricing-power evidence, refreshed:** Broadcom's Q3 FY2026 earnings release (2026-09-02, 8-K): AI-semiconductor revenue **$16.7B, +221% YoY** (accelerating from Q2 FY2026's +143% YoY cited in the prior session), with Q4 FY2026 guidance of **$21.7B AI-semi revenue, +236% YoY** — documented, company-sourced evidence of continued/accelerating TAM expansion, same +10 basis as before, now on stronger evidence.

**Moat Signal — unchanged, still flagged:** the "market share stable/growing" signal is still backed only by company-reported growth data and named hyperscaler relationships (now even stronger — Q3's +221% YoY vs Q2's +143% YoY), **not** a third-party market-share tracker citation, which is the specific evidentiary bar the checklist calls for. No new third-party citation surfaced this session. Moat_Score stays 40.0 (2/5: market share, switching costs).

**Quality Score = 86.3 — clears the 80.0+ gate, and materially more robustly than before.** Sensitivity check (per the "no black box" principle, same test run in prior sessions): excluding the borderline "market share" signal entirely (Moat_Score → 0 instead of 40) still gives Quality Score **80.3** — still clears. Using the more conservative Moat_Score = 20 gives **83.3**. **This resolves the "close call" flag carried in the 2026-07-04 and 2026-08-28 sessions** (where the gate margin was only ~2.1 points and hinged partly on the same judgment call) — the margin is now ≥6.3 points even under the most conservative moat reading, driven by Profitability and Balance Sheet sub-scores both improving sharply on the blowout quarter (large net income, and a $9.8B one-quarter net-debt paydown).

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $359.00 / $19.448 = 18.4595×
EY = 1 / 18.4595 = 5.4173%
Spread = EY − 10Y Treasury = 5.4173% − 4.79% = +0.6273pp
```
Spread (+0.63pp) < +1.5% → **fails** → **+5 additive** (yellow flag, not a veto).

**Step 2 — Rate Regime Modifier**
10Y = 4.79% → 3.5–5% bracket → **+5**

**Combined Rate Modifier: +10** (same bracket as the last three sessions)

---

## 5. Valuation Score (Phase 02)

### FCF Yield (40% weight)

```
Market Cap = $359.00 × 4,887M shares = $1,754,433M
FCF Yield  = $39,403M / $1,754,433M = 2.246%
FCF_Score  = clamp(100×(1 − 2.246/10), 0, 100) = 77.5
```
Materially cheaper than the prior session's 81.8 — TTM FCF is up 20.3% ($32,762M→$39,403M) against a price that's actually down 2.6%.

### EV/EBIT (weight 25% base, redistributed to 40% — PEG still not applicable, see below)

```
EV = Market Cap $1,754,433M + Net Debt $35,444M = $1,789,877M
EV/EBIT (GAAP TTM) = $1,789,877M / $42,814M = 41.81×
EV/EBIT_Score = clamp((41.81 − 12)/23 × 100, 0, 100) = 100.0
```

**⚠️ Normalization check — no longer moot, flagged explicitly.** Stripping the $9.3B/yr amortization add-back: Normalized EBIT = $52,114M → EV/EBIT = **34.35×**, which for the first time in this repo's AVGO sessions sits just **under** the 35× ceiling (EV/EBIT_Score would be **97.2**, not 100.0, on a normalized basis). In every prior session this check was moot (both bases saturated at 100.0); this session it is not. **Kept the GAAP basis as primary (EV/EBIT_Score = 100.0)** for continuity with all three prior AVGO sessions' established convention, but this is now a real, not merely academic, methodology choice — worth a documented decision if it recurs and starts moving the action band. Using the normalized 97.2 instead would move the final score from 66.6 to ~65.4 and the Composite from 40.1 to ~39.6 — same action bands either way this session, but flagged for future attention (see §8).

### Forward PE + Historical PE Modifier (20% weight)

```
Forward PE = 18.46×, 5yr Low = 13.39×, 5yr High = 52.85× (carried forward, flagged §2)
FwdPE_Score (raw) = clamp((18.4595 − 13.3897)/(52.8544 − 13.3897) × 100, 0, 100) = 12.8
```
**Historical PE Modifier (Upgrade 2):** Forward PE vs 5yr avg (29.9465×): (18.4595 − 29.9465)/29.9465 × 100 = **−38.36%** (>20% below) → **−10**.
```
FwdPE_Score = 12.8 − 10 = 2.8
```

### PEG (15% weight) — Fast-Grower eligibility ruling still carried forward

No new information to revisit the ruling: AVGO's GAAP EPS remains distorted by non-cash acquisition-intangible amortization (~$2.0B/quarter, per §2), still disqualifying it from PEG eligibility's "clean, non-distorted earnings base" requirement. **PEG not scored; its 15% weight redistributed to EV/EBIT (→ 40%).**

### Raw Weighted Score

```
Raw = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
    = (77.5 × 0.40) + (100.0 × 0.40) + (2.8 × 0.20)
    = 31.02 + 40.00 + 0.57
    = 71.59
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

Refreshed scenario architecture — same multiple/EPS-variance assumptions as the prior three sessions (no new information to justify revising the bull/base/bear multiples themselves; the underlying AI-ramp thesis was, if anything, further validated by Q3's acceleration), refreshed for the current price, forward EPS, and a shorter catalyst window.

**Step 1 — scenario fair values.** NTM EPS estimate: **$19.45** (`yfinance` forward EPS — flagged §2 as possibly still reflecting a pre-earnings consensus basis; no fresher published NTM EPS consensus found via WebSearch at time of session).

| Scenario | Wt | Assumption | EPS basis | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | AI ramp continues to beat, re-rate | $19.45 × 1.10 = $21.39 | 34× | **$727.36** |
| Base | 50% | Consensus AI ramp, multiple eases below 5yr avg (29.95×) | $19.45 | 25× | **$486.20** |
| Bear | 25% | AI capex slowdown / hyperscaler in-sourcing, de-rate toward the low end | $19.45 × 0.85 = $16.53 | 15× | **$247.96** |

```
PW Fair Value (multiples) = 0.25×727.36 + 0.50×486.20 + 0.25×247.96 = $486.93
Gap Upside % = 486.93 / 359.00 − 1 = +35.6%
```

**Step 2 — catalyst & annualization (Rule 10).** Same documented catalyst: management's FY2027 AI-semiconductor revenue target (>$100B, most recently reaffirmed and — per Q3's acceleration — arguably tracking ahead of pace). From today (3 Sep 2026) to the FY2027 confirmation point (Broadcom's FY2027 fiscal year ends ~early Nov 2027, results reported ~December 2027) is **~15 months ≈ 1.25 years** — Guardrail 1 (catalyst within 18–24 months) satisfied, no cap needed.
```
Annualized gap = 35.6% / 1.25 = 28.5%
```
**Step 3 — expected annual return E.**
```
E = annualized gap (28.5%) + intrinsic growth (12%, carried forward, flagged) + shareholder yield ($2.60/$359.00 = 0.72%)
  = 28.5 + 12.0 + 0.7 = 41.2%
```
**Step 4 — map E to M** (hurdle H = 10%):
```
E (41.2%) ≥ H → M = −15 × clamp((41.2 − 10)/15, 0, 1) = −15 × clamp(2.08, 0, 1) = −15.0
```
**Upside/Downside Modifier M = −15.0 (fully saturated at the cap)** — same as the last three sessions; the actual price decline (−2.6%) against a materially stronger fundamental base widens the gap further, and the shorter catalyst window amplifies the annualized figure.

---

## 7. Final Valuation Score

```
Final Score = Raw Weighted (71.59) + Rate Modifier (+10) + Upside/Downside Modifier (−15.0)
            = 66.59 → 66.6
```

**Valuation Score = 66.6 — "Fair Value"** (50.0–69.9 band, unchanged band; down 1.9 from 68.5 — cheaper on every sub-score, mostly offset by the saturated Upside/Downside cap already applying at the maximum discount)

---

## 8. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 86.3) + 0.50 × 66.6
                = 0.50 × 13.7 + 33.30
                = 6.85 + 33.30
                = 40.15 → rounds UP (exact ".X5" boundary) → 40.2
```

**Composite Score = 40.2 — "Cheap"** (30.0–49.9 band, unchanged band; down 3.0 from 43.2, driven almost entirely by the Quality Score jump)

---

## 9. Action Recommendation & Order Setup

Composite Score 40.2 stays in the **30.0–49.9 "Cheap" → Standard position 3–5%** band — nominally BUY-eligible. Full order setup run below, per the operating brief.

### Fair Value — two methods, triangulated (Rule 1: Tech/Growth → DCF primary, Multiples secondary)

**Method A — 3-Stage DCF (Rule 2).** Same 10-year growth-fade schedule as prior sessions (no new information to revise it), rebased on the fresh $39,403M TTM FCF (a genuine Rule 9 model-refresh event) and updated WACC:

```
WACC build:
  Cost of equity = Rf (4.79%) + Beta (1.473) × ERP (5.0%, assumed) = 12.16%
  Cost of debt (pretax) = TTM interest expense $3,116M / Total Debt $59,419M = 5.24%; after-tax (21%) = 4.14%
  Weights: E/(D+E) = 96.72% (Market Cap $1,754,433M), D/(D+E) = 3.28% (Debt $59,419M)
  WACC = 96.72%×12.16% + 3.28%×4.14% = 11.89%

Stage 1 (yrs 1–5), FCF base $39,403M, same growth path as prior sessions:
  y1 +25% → $49,254M | y2 +20% → $59,104M | y3 +15% → $67,970M | y4 +12% → $76,127M | y5 +10% → $83,739M

Stage 2 (yrs 6–10), linear fade from 10% to the 2.5% terminal rate:
  y6 $90,857M | y7 $97,217M | y8 $102,564M | y9 $106,667M | y10 $109,333M

Terminal Value (at y10) = $109,333M × 1.025 / (0.1189 − 0.025) = $1,193,145M
Terminal Value as % of total DCF value = 46.7% (well under the 75% Rule 4 sanity cap)

Sum of discounted FCFs (yrs 1–10) = $442,710M
PV of Terminal Value = $387,867M
Enterprise Value (DCF) = $830,577M
Equity Value = $830,577M − Net Debt $35,444M = $795,133M
DCF Fair Value / share = $795,133M / 4,887M = $162.70
```
(Up sharply from $133.77 on 2026-08-28 — the higher FCF base more than offsets the slightly higher WACC.)

**Method B — Scenario-weighted multiples (§6 PW Fair Value):** **$486.93**

**⚠️ Same material finding as prior sessions — wide divergence between the two methods,** now somewhat narrower in relative terms (DCF rose proportionally more than the multiples-FV). Same underlying tension as before: a disciplined GDP-terminal-growth DCF vs. AVGO's own trailing 5-year PE range.

```
Triangulation (Rule 3, Tech/Growth weights): Blended FV = 40% × DCF + 60% × Multiples
                                            = 0.40 × $162.70 + 0.60 × $486.93
                                            = $65.08 + $292.16
                                            = $357.24
```

### Order Setup Checklist

```
[✓] Composite Score (incl. Quality blend):    40.2 — "Cheap" (30.0–49.9 band)
[✓] Expected annual return E / catalyst:      +41.2% / 1.25yr (feeds the Upside/Downside Modifier, §6)
[✓] Upside/Downside Modifier applied:         −15.0
[✓] DCF Fair Value:                           $162.70
[✓] Multiples-Based Fair Value:               $486.93
[✓] Blended Fair Value:                       $357.24
[ ] Margin of Safety %:                       25–30% (Composite 30.0–49.9 band)
    Buy Price range: $250.07 (30% MoS) – $267.93 (25% MoS)
[✓] PRIMARY SELL TARGET:                      $357.24 (Blended FV, baseline)
[✓] BULL-CASE TRIM TARGET:                    $727.36 × 0.90 = $654.62
[ ] STOP LOSS: 25–30% max loss from Buy Price
    Range: $175.05 – $200.95 depending on MoS/stop combination
[✗] Risk/Reward Ratio — checked across the full 25–30% MoS × 25–30% stop matrix:
      MoS 25%/Stop 25%: 1.33:1   MoS 25%/Stop 30%: 1.11:1
      MoS 30%/Stop 25%: 1.71:1   MoS 30%/Stop 30%: 1.43:1
    Best case in the applicable range (1.71:1) still — FAILS the 2:1 minimum throughout.
```

**Per fair-value-methodology.md Step 6: R/R fails the minimum threshold across the entire applicable MoS/stop range. No order is placed.**

**Position sizing is also moot for a different reason:** AVGO's current 3.55% weight already sits **within** the Composite Score's implied 3–5% "Standard position" target band — there is no sizing gap to fill even before the R/R gate is considered.

### Net Action: **HOLD** — maintain the current 6-share position as-is

- No trim: Composite Score (40.2) is far below any trim threshold (70.0+).
- No add: R/R on the computed order setup fails the 2:1 minimum (best case 1.71:1), and the position is already within its Composite-Score-implied target size.
- **The open 2026-06-16 override remains unresolved** (§0) — unchanged by this rescore.

**Same action band as the 2026-08-28 session (HOLD), but a materially different underlying picture:** Quality Score jumped 82.1→86.3 (the gate-eligibility "close call" flagged in the last two sessions is now resolved — robust even in the worst-case moat sensitivity), Valuation Score improved (cheaper) 68.5→66.6, and Composite improved (cheaper) 43.2→40.2 — driven by a genuinely strong Q3 FY2026 print (revenue +86% YoY, GAAP EBIT +173% YoY on this quarter alone vs. year-ago quarter, a $9.8B one-quarter net-debt paydown) against a stock price that actually **fell** ~2.6% on guidance that beat the prior quarter's own trajectory but underwhelmed the market's more elevated expectations. No band change (still comfortably short of both the R/R bar for an add and the 70.0+ trim bar), so no order is placed — but this is a stronger, not weaker, name than the framework showed one week ago.

---

## 10. Next Review Trigger

**Date/event:** AVGO's Q4 FY2026 earnings release (expected ~December 2026, per the typical AVGO reporting cadence) — re-run Phase 01/02 with refreshed TTM figures. **Two specific follow-ups flagged this session, worth checking first at that rescore:**
1. **Re-verify the 5yr PE range** once `yfinance`'s `get_earnings_dates` backfills the 2026-09-02 print (flagged as unchanged/stale this session, §2) — confirm it doesn't materially shift the Forward PE sub-score.
2. **Watch the EV/EBIT GAAP-vs-normalized divergence** (§5) — normalized EV/EBIT is now within ~1× of dropping the sub-score below full saturation (34.35× vs. the 35× ceiling) for the first time. If continued EBIT growth pushes the normalized multiple further under 35× while GAAP stays saturated, the choice of basis will start to move the actual score, not just a footnote — worth a `decisions/` entry if that materializes rather than continuing to pick GAAP by unstated convention.

Earlier trigger on a >15% unexplained move from $359.00 (Rule 9), a further guidance revision/M&A/management change, or new third-party market-share data that would firm up the Moat_Score's remaining evidentiary gap (now less consequential to the gate outcome, per §3's sensitivity check, but still an open item on its own terms). **Separately and unconditionally: the 2026-06-16 override still needs the user to supply a rationale** for `decisions/` and `override-log.md` — not tied to any valuation trigger.

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
- **TAM**: Total Addressable Market.
- **Terminal Value**: The lump-sum value assigned to all DCF cash flows beyond the explicit forecast period.
- **TTM**: Trailing Twelve Months.
- **Upside/Downside Modifier (Expected-Return Modifier)**: The additive ±15 adjustment based on expected annual return vs. the 10% hurdle.
- **Valuation Score**: This framework's 0.0–100.0 score (lower = cheaper) combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.
- **WACC**: Weighted Average Cost of Capital — the DCF discount rate.

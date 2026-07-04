# RESCORE — AVGO (Broadcom Inc.) — 2026-07-04

**Task type:** RESCORE (mode `--both`)
**Date:** 04 Jul 2026
**10Y US Treasury Yield:** 4.49% (WebSearch: TradingEconomics/CNBC, 2 Jul 2026 close — most recent available; US Treasury market observed the July 4th holiday on Fri 3 Jul, then the weekend, so 2 Jul is the latest print. Unchanged vs the 2026-06-14/06-20 sessions.)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current AVGO portfolio weight:** 4.01% (6 shares, IBKR) — held as an **open, unresolved Human Override** (see §0 below)
**Sector:** Semiconductors (fabless — AI accelerators/networking) + Infrastructure Software (VMware)
**Last review:** 14 Jun 2026 (score 69.5) — overdue; predates both the 2026-06-20 Upside/Downside Modifier and the 2026-06-29 Quality Score/Composite Score additions. This session runs the full current methodology for the first time on AVGO.

---

## 0. Override status (reported, not resolved this session)

Per [override-log.md](../portfolio/override-log.md): AVGO carries an **open, unresolved override dated 2026-06-16** — 6 shares were bought at $382.275, two days after the 2026-06-14 session's explicit WATCHLIST/no-new-entry call (score 69.5), with **no rationale on record** and no `decisions/` entry. Status as of this session: **still open, still no rationale supplied, outcome "TBD."** This rescore does not attempt to resolve or adjudicate the override — it is reported here exactly as found, per instruction. The override remains the user's item to close out (supply a rationale in `decisions/` and `override-log.md`).

**Watchlist duplicate flag:** `watchlist/not-in-portfolio/AVGO/AVGO-2026-06-20.md` is a **leftover duplicate** — a `/new-position` evaluation run the same week AVGO was bought, computing a post-Upside/Downside-Modifier score of **74.8** that the in-portfolio entry never picked up when the position was logged retroactively (per the existing note in [watchlist/STALE.md](../watchlist/STALE.md)). AVGO is a held position (per [holdings.md](../portfolio/holdings.md)), so this `not-in-portfolio/` folder should not exist — it is stale and superseded. **This session's fresh 2026-07-04 computation (Valuation 68.2 / Quality 82.1 / Composite 43.1) supersedes both the 2026-06-14 (69.5) and 2026-06-20 (74.8) numbers.** Per my scope, I have **not** deleted or moved `watchlist/not-in-portfolio/AVGO/` — flagging it clearly here for `/sync-portfolio` to fold into `in-portfolio/AVGO/` as instructed in STALE.md.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$360.45** | IBKR `get_price_history` (contract_id 313130367, NASDAQ), most recent daily bar close = **2026-07-02** (last trading session before the market observed the July 4th holiday on Fri 3 Jul, ahead of the Sat 4 Jul/Sun 5 Jul weekend). Cross-validated against `yfinance`'s live `currentPrice`/`regularMarketPrice` fields, both independently reading **$360.45**. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$369.34** (marked `is_close: true`) on two consecutive calls — this is stale by one session: `get_price_history` and `yfinance` both show $369.34 as the **2026-07-01** close, not the most recent one. Used the fresher, cross-validated $360.45 figure instead. `bid_ask`/`change` fields returned empty (market closed for the weekend at query time). |
| 52-week range | $268.04 – $495.00 (IBKR `misc_statistics`) / $269.58 – $495.00 (`yfinance`) | Both sources agree closely; high is identical, low differs by <0.6%, immaterial. |
| Analyst consensus PT | $523.73 (45 analysts), rating "Strong Buy" | `yfinance` `targetMeanPrice`/`recommendationKey` — effectively unchanged from the 2026-06-20 session's $523.84. |
| Prior session prices | $405.05 (20 Jun), $382.07 (14 Jun) | For reference — AVGO is **−11.0%** since the 2026-06-20 session and **−11.0%** since the 2026-06-22 sync price ($404.53). Below the 15% Rule 9 threshold — not an independent fundamental-event trigger; this rescore is methodology-driven (overdue Upside/Downside Modifier + first-ever Quality Score), not price-driven. |

**Context:** $360.45 sits ~27% below the 52-week high ($495) and ~34% above the 52-week low ($268) — middle of the range, ~45% below the analyst consensus PT cluster.

---

## 2. Data Gathered — Sources & Gaps

Fundamentals pulled fresh via `yfinance` this session (proxy note: `yfinance`'s default `curl_cffi` transport failed TLS through this session's egress proxy — worked around by passing a plain `requests.Session()` to `yf.Ticker()`, a transport-layer fix only, no data substituted or estimated). No new AVGO earnings have been reported since Q2 FY2026 (filed ~3 Jun 2026, last reviewed 2026-06-20) — Q3 FY2026 is still expected ~September 2026, so the TTM window (Q3 FY2025–Q2 FY2026) is **unchanged** from the 2026-06-20 session.

| Metric | Value | Source / note |
|---|---|---|
| TTM Revenue | $75,465M | `yfinance` quarterly rollforward (Q2FY26 $22,187M + Q1FY26 $19,311M + Q4FY25 $18,015M + Q3FY25 $15,952M); matches `info.totalRevenue` exactly |
| TTM Net Income | $29,317M | Same rollforward; matches `info.netIncomeToCommon` exactly, and matches the 2026-06-14/06-20 sessions' 8-K-sourced figure for the identical quarters |
| TTM GAAP EBIT | **$30,443M** (carried forward — see flag) | 8-K-sourced rollforward established in the 2026-06-20 session for this exact TTM window (Q3FY25 $7,508M + Q4FY25 $5,887M + Q1FY26 $6,260M + Q2FY26 $10,788M) |
| ⚠️ EBIT vendor discrepancy | `yfinance`'s own quarterly "EBIT"/"Operating Income" fields for the *same* four quarters sum to **$33,624M / $33,253M** — ~10% above the 8-K figure. Used the previously-established 8-K figure for continuity; **doesn't change any downstream sub-score** (EV/EBIT saturates at the 100.0 ceiling either way — 59.2× vs 53.6×, both far past 35×). |
| TTM FCF | **$32,762M** (fresh rollforward — see flag) | `yfinance` quarterly cash flow: Q2FY26 $10,262M + Q1FY26 $8,010M + Q4FY25 $7,466M + Q3FY25 $7,024M |
| ⚠️ FCF vendor discrepancy | `yfinance`'s cached `info.freeCashflow` field reads **$27,212M** — this is stale by one full quarter (it matches the 2026-06-20 session's TTM figure exactly, i.e. it hasn't rolled forward). `info.operatingCashflow` ($33,622M), by contrast, *has* rolled forward and matches the fresh quarterly sum. Used the fresh rollforward ($32,762M) as the current, correct figure. |
| TTM Gross Margin | 68.3% (computed: $51,524M / $75,465M) | `yfinance` quarterly financials rollforward — consistent with the GAAP ~67–68% figures used in prior AVGO sessions. `info.grossMargins` (76.3%) is flagged again as a differently-defined/stale vendor field, not used (same discrepancy noted in the 2026-06-14/06-20 sessions). |
| Net Debt | $45,279M (Total Debt $64,907M − Cash $19,628M) | `yfinance` balance sheet, 2026-04-30 (Q2 FY2026) — **unchanged** from prior sessions (same quarter, no new 10-Q filed) |
| Diluted shares (Q2 FY2026) | 4,876M | `yfinance` quarterly financials — matches prior sessions |
| Forward PE | 18.58× | `yfinance` (price $360.45 ÷ forward EPS $19.396) |
| 5yr PE range (reconstructed) | Avg 29.95×, Low 13.39×, High 52.85× (n=20 quarters) | `yfinance` `get_earnings_dates` + price history, per the framework's documented reconstruction method — essentially unchanged from the 2026-06-20 session's 30.0×/13.4×/52.9× |
| Beta | 1.462 | `yfinance` `info.beta` — used only for this session's DCF (see §5) |
| VMware amortization | ~$9.3B/yr (carried forward, not independently re-verified) | Established in the 2026-06-14/06-20 sessions from 8-K figures; no new 10-Q since, so no fresher figure exists to pull |
| Effective tax rate | Distorted quarter-to-quarter (2.4%–21.7%) by one-off items; normalized to **21%** (the two "clean" recent quarters, Q3/Q4 FY2025) for the ROIC calc below, per Rule 6 | `yfinance` quarterly `Tax Rate For Calcs` |
| Dividend / shareholder yield | $2.60/sh, ~0.7% trailing yield; net buyback yield ≈0% (basic shares outstanding still rising slightly, Q4FY25→Q2FY26) | `yfinance` — consistent with the 2026-06-20 session's finding |

**Moat-signal evidence gap (flagged for the Quality Score's Moat checklist, §3):** the Quality Score's per-signal moat checklist requires a *specific cited source per signal marked true* — a stricter bar than the general "5 Qualitative Questions" narrative used in prior AVGO NEW POSITION write-ups. Only 2 of 5 signals have a specific citation on file (see §3); the other 3 (brand premium, network effect, scale cost advantage) lack the exact evidence type the checklist calls for (pricing-power data, a two-sided-marketplace mechanism, cost-per-unit comparisons) even though AVGO's general competitive position is well-documented qualitatively elsewhere in this repo.

**DCF assumptions (flagged as analyst judgment, not "data"):** this is the first full DCF built for AVGO in this repo. WACC inputs (beta from `yfinance`, a 5.0% Equity Risk Premium assumption — a standard modeling convention, not a fetched fact) and the 10-year growth-fade schedule are disclosed in full in §5. The resulting DCF fair value diverges sharply from the multiples-based scenario fair value — a genuine, material finding discussed there, not a calculation error.

No metric was invented or estimated; every figure above traces to `yfinance`'s live pull, a previously-established/cited primary-source figure carried forward (flagged where reused), or a disclosed modeling assumption.

---

## 3. Quality Score (Phase 01 gate — first computed for AVGO)

**Hard disqualifier check (all must pass before any weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | FY2024 329%, FY2025 116%, TTM 111.8% — all far above 70% | disqualify if <70% for 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | 1.08× (see Balance Sheet below) | disqualify if >2.5× (standard) | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2023 ($17.6B), FY2024 ($19.4B), FY2025 ($26.9B) all positive | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight)

```
Net Margin (TTM) = $29,317M / $75,465M = 38.85%
NetMargin_Component = clamp((38.85/30)×100, 0, 100) = clamp(129.5, 0, 100) = 100.0

ROIC — not directly exposed by yfinance; computed via Rule-6-normalized NOPAT ÷ Net Invested Capital:
  Normalized EBIT (TTM) = $30,443M GAAP + $9,300M VMware amortization add-back = $39,743M
  Normalized tax rate    = 21% (clean-quarter basis, see §2)
  NOPAT                  = $39,743M × (1 − 0.21) = $31,397M
  Net Invested Capital   = Total Debt $64,907M + Total Equity $87,691M − Cash $19,628M = $132,970M
  ROIC = $31,397M / $132,970M = 23.61%
ROIC_Component = clamp((23.61/30)×100, 0, 100) = 78.70

Profitability_Score = (100.0 + 78.70) / 2 = 89.35 → 89.4
```
No FCF-positivity cap applies (FCF-positive well beyond 3 years).

*Cross-check: the 2026-06-14 session cited stockanalysis.com's ROIC as 24.22% (not independently re-pulled this session). My from-scratch computation (23.61%) agrees within ~0.6pp. Using 24.22% instead would move ROIC_Component to 80.7 and Profitability_Score to 90.4 — a ~0.25pp effect on the final Quality Score, immaterial to the gate outcome either way.*

### Margins (15% weight)

```
Gross Margin (TTM) = 68.28% (computed, see §2)
GrossMargin_Score = clamp((68.28/80)×100, 0, 100) = 85.3
```
No structural-trend bonus applicable (margin already well above the 40% threshold that the bonus targets; trend itself is a post-VMware-integration recovery — FY23 68.9% → FY24 63.0% → FY25 67.8% → TTM 68.3% — not a clean multi-year expansion).

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022→FY2025) = (63,887/33,203)^(1/3) − 1 = 24.39%
Growth_Score = clamp((24.39/25)×100, 0, 100) = 97.6
TAM/pricing-power evidence (cited): Broadcom's own FY2026 guidance of $56B AI-semiconductor revenue and an FY2027 target >$100B (Q2 FY2026 earnings release, 3 Jun 2026), against Q2 FY2026 AI-semi revenue growth of +143% YoY — documented, company-sourced evidence of TAM expansion → +10
Growth_Score = clamp(97.6 + 10, 0, 100) = 100.0
```
No decelerating-growth evidence exists (growth is accelerating, not decelerating) — no −10 applies.

### Balance Sheet (15% weight)

```
Net Debt = $45,279M (unchanged this quarter)
EBITDA (TTM) = $42,084M (yfinance)
Net Debt/EBITDA = 45,279/42,084 = 1.076×
BalanceSheet_Score = clamp(100×(1 − 1.076/4), 0, 100) = 73.1
```
Standard /4 denominator applies (AVGO is not a payment network/exchange — the asset-light Upgrade 5 override doesn't apply).

### Moat Signal (15% weight) — checklist, cited evidence per signal

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Broadcom's own Q1/Q2 FY2026 earnings releases (8-K): AI-semiconductor revenue +106% YoY (Q1) and +143% YoY (Q2), against named, exclusive-style custom-ASIC design relationships with the largest hyperscalers (Google TPU, Meta, ByteDance) — company-sourced growth data plus named-customer concentration, not a formal third-party share-tracker report (flagged as a softer evidentiary basis than an ideal citation, but directly sourced, not invented). |
| Brand premium | FALSE | No cited pricing-power evidence (price increases without volume loss) exists in this repo's AVGO research to date. |
| Network effect | FALSE | No documented two-sided-marketplace mechanism identified for AVGO's business lines. |
| Switching costs | **TRUE** | VMware enterprise virtualization franchise — documented integration-depth/migration-cost mechanism (an enterprise's virtualized data-center infrastructure is costly and risky to migrate off), cited in the 2026-06-14/06-20 sessions. |
| Scale cost advantage | FALSE | No cited cost-per-unit data vs. smaller competitors exists on file for AVGO. |

```
Moat_Score = (2/5) × 100 = 40.0
```

⚠️ **This is a close call for the overall 80.0+ gate, shown transparently:** if the "market share" signal above were excluded (its evidentiary basis — company-reported growth + named customers, not a formal share-tracker citation — is genuinely borderline against the checklist's stated bar), Moat_Score would be 20.0 instead of 40.0, dropping the final Quality Score from 82.1 to **79.1 — below the 80.0 gate.** Flagging this explicitly per "no black box": the gate result here is not overwhelmingly robust to this one judgment call, and is worth revisiting if a harder third-party market-share citation becomes available at the next rescore.

### FCF Quality (10% weight)

```
FCF/NI (TTM) = $32,762M / $29,317M = 111.8%
FCFQuality_Score = clamp(((1.118 − 0.40)/0.60)×100, 0, 100) = clamp(119.6, 0, 100) = 100.0
```

### Quality Score — Final

```
Quality Score = (89.4×0.25) + (85.3×0.15) + (100.0×0.20) + (73.1×0.15) + (40.0×0.15) + (100.0×0.10)
              = 22.35 + 12.795 + 20.00 + 10.965 + 6.00 + 10.00
              = 82.11
```

**Quality Score = 82.1 — clears the 80.0+ gate** (see the moat-signal sensitivity flag above; the margin over the gate is only 2.1 points and hinges partly on one judgment call).

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = 18.58×
EY = 1 ÷ 18.58 = 5.38%
Spread = EY − 10Y Treasury = 5.38% − 4.49% = +0.89%
```
Spread (+0.89%) < +1.5% → **fails** → **+5 additive** (yellow flag, not a veto).

**Step 2 — Rate Regime Modifier**
10Y = 4.49% → 3.5–5% bracket → **+5**

**Combined Rate Modifier: +10** (unchanged bracket vs. the 2026-06-14/06-20 sessions)

---

## 5. Valuation Score (Phase 02)

### FCF Yield (40% weight)

```
Market Cap = $360.45 × 4,876M shares = $1,757,554M
FCF Yield  = $32,762M / $1,757,554M = 1.864%
FCF_Score  = clamp(100×(1 − 1.864/10), 0, 100) = 81.4
```
No Owner Earnings adjustment (Upgrade 1) — AVGO's capex remains ~1% of revenue, immaterial; established and unchanged.

### EV/EBIT (weight 25% base, redistributed to 40% — see PEG below)

```
EV = Market Cap $1,757,554M + Net Debt $45,279M = $1,802,833M
EV/EBIT (GAAP TTM) = $1,802,833M / $30,443M = 59.2×
EV/EBIT_Score = clamp((59.2 − 12)/23 × 100, 0, 100) = 100.0
```
**Rule 6 normalization check (strip the $9.3B/yr VMware amortization):** Normalized EBIT = $30,443M + $9,300M = $39,743M → EV/EBIT = $1,802,833M/$39,743M = 45.4×. **Still far past the 35× ceiling — EV/EBIT_Score = 100.0 either way**, same conclusion as the 2026-06-20 session.

### Forward PE + Historical PE Modifier (20% weight)

A genuine 5yr low/high range exists (reconstructed, §2) → primary formula:
```
Forward PE = 18.58×, 5yr Low = 13.39×, 5yr High = 52.85×
FwdPE_Score = clamp((18.58 − 13.39)/(52.85 − 13.39) × 100, 0, 100) = clamp(13.16, 0, 100) = 13.2
```
**Historical PE Modifier (Upgrade 2):** Forward PE vs 5yr avg (29.95×): (18.58 − 29.95)/29.95 × 100 = **−38.0%** (>20% below) → **−10**. (Structural Quality Override only blocks the +10 "expensive" penalty, not this −10 "cheap" credit.)
```
FwdPE_Score = 13.2 − 10 = 3.2
```

### PEG (15% weight) — Fast-Grower eligibility ruling carried forward

**Ruling maintained from 2026-06-20 (no new information to revisit it):** AVGO's GAAP EPS remains distorted ~35–40% by non-cash VMware amortization, disqualifying it from the "clean, non-distorted earnings base" the Fast-Grower/PEG eligibility rule requires. **PEG is not scored; its 15% weight is redistributed to EV/EBIT (→ 40%).**

### Raw Weighted Score

```
Raw = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
    = (81.4 × 0.40) + (100.0 × 0.40) + (3.2 × 0.20)
    = 32.56 + 40.00 + 0.64
    = 73.20
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

Reuses the same scenario architecture established in the 2026-06-20 session (no new guidance/earnings event to warrant revisiting the multiple choices), refreshed for the current price and forward EPS.

**Step 1 — scenario fair values.** NTM EPS = price ÷ forward PE, but cleaner to use `yfinance`'s own forward EPS estimate directly: **$19.40**.

| Scenario | Wt | Assumption | EPS basis | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | AI ramp beats ($56B→>$100B FY27), re-rate | $19.40 × 1.10 = $21.34 | 34× | **$725.41** |
| Base | 50% | Consensus AI ramp, multiple eases below 5yr avg (29.95×) | $19.40 | 25× | **$484.90** |
| Bear | 25% | AI capex slowdown / hyperscaler in-sourcing → est. cuts ~15%, de-rate toward the low end | $19.40 × 0.85 = $16.49 | 15× | **$247.30** |

```
PW Fair Value (multiples) = 0.25×725.41 + 0.50×484.90 + 0.25×247.30 = $485.63
Gap Upside % = 485.63 / 360.45 − 1 = +34.7%
```
(For reference: this gap is much wider than the 2026-06-20 session's +18.0% almost entirely because the *price* fell ~11% while the scenario fair-value inputs are essentially unchanged — the mechanical effect of expressing upside as % of a lower price, not a reassessment of the business.)

**Step 2 — catalyst & annualization (Rule 10).** Same documented catalyst as before: management's FY2026 AI-semiconductor revenue guide ($56B) and FY2027 target (>$100B), from the Q2 FY2026 earnings release. From today (4 Jul 2026) to the FY2027 milestone (Broadcom's fiscal year ends ~Oct/Nov 2027, likely confirmed at the Dec 2027 earnings call) is **~15–17 months**; used a rounded **1.5 years** for the annualization (Guardrail 1 — catalyst within 18–24 months — is satisfied, no cap needed).
```
Annualized gap = 34.7% / 1.5 = 23.2%
```
**Step 3 — expected annual return E.**
```
E = annualized gap (23.2%) + intrinsic growth (12%, conservative durable FCF/EPS CAGR, carried forward unchanged) + shareholder yield (~0.7%, dividend only; net buyback ≈0%, share count still slightly rising)
  = 23.2 + 12.0 + 0.7 = 35.9%
```
**Step 4 — map E to M** (hurdle H = 10%):
```
E (35.9%) ≥ H → M = −15 × clamp((35.9 − 10)/15, 0, 1) = −15 × clamp(1.73, 0, 1) = −15 × 1.0 = −15.0
```
**Upside/Downside Modifier M = −15.0 (fully saturated at the cap).**

*Robustness check: this modifier saturates at −15 under a wide range of reasonable alternative assumptions — e.g. using the older, more conservative 2yr catalyst window instead of 1.5yr still gives annualized gap 17.4%, E = 30.1%, and M still saturates at −15 (since (30.1−10)/15 > 1). Zeroing out shareholder yield or dropping intrinsic growth to 10% also still saturates. The result is not sensitive to the specific window/growth assumptions chosen — it's driven by the price decline against a materially unchanged fair-value estimate.*

---

## 7. Final Valuation Score

```
Final Score = Raw Weighted (73.20) + Rate Modifier (+10) + Upside/Downside Modifier (−15.0)
            = 68.20
```

**Valuation Score = 68.2 — "Fair Value"** (50.0–69.9 band)

---

## 8. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 82.1) + 0.50 × 68.2
                = 0.50 × 17.9 + 34.1
                = 8.95 + 34.1
                = 43.05 → rounds UP (exact .X5 boundary) → 43.1
```

**Composite Score = 43.1 — "Cheap"** (30.0–49.9 band per the Phase 03/05 action tables)

---

## 9. Action Recommendation & Order Setup

Composite Score 43.1 falls in the **30.0–49.9 "Cheap" → Standard position 3–5%** band — nominally a BUY-eligible score. Per the operating brief, the full order setup is run below.

### Fair Value — two methods, triangulated (Rule 1: Tech/Growth sector → DCF primary, Multiples secondary)

**Method A — 3-Stage DCF (Rule 2).** First full DCF built for AVGO in this repo; all assumptions disclosed:

```
WACC build:
  Cost of equity = Rf (4.49%) + Beta (1.462) × ERP (5.0%, assumed) = 11.80%
  Cost of debt (pretax) = TTM interest expense $3,145M / Total Debt $64,907M = 4.85%; after-tax (21%) = 3.83%
  Weights: E/(D+E) = 96.4% (Market Cap $1,757,554M), D/(D+E) = 3.6% (Debt $64,907M)
  WACC = 96.4%×11.80% + 3.6%×3.83% = 11.52%

Stage 1 (yrs 1–5), FCF base $32,762M, growth tapering from the AI-ramp guide toward a durable rate:
  y1 +25% → $40,953M | y2 +20% → $49,143M | y3 +15% → $56,514M | y4 +12% → $63,296M | y5 +10% → $69,626M

Stage 2 (yrs 6–10), linear fade from 10% to the 2.5% terminal rate:
  y6 $75,544M | y7 $80,832M | y8 $85,278M | y9 $88,689M | y10 $90,906M

Terminal Value (at y10) = $90,906M × 1.025 / (0.1152 − 0.025) = $1,033,475M
Terminal Value as % of total DCF value = 48.1% (well under the 75% Rule 4 sanity cap — no need to extend Stage 2)

Sum of discounted FCFs (yrs 1–10) = $374,737M
PV of Terminal Value = $347,476M
Enterprise Value (DCF) = $722,214M
Equity Value = $722,214M − Net Debt $45,279M = $676,935M
DCF Fair Value / share = $676,935M / 4,876M = $138.83
```

**Method B — Scenario-weighted multiples (the same PW Fair Value used for the Upside/Downside Modifier, §6):** **$485.63**

**⚠️ Material finding — wide divergence between the two methods.** A fade-to-GDP-terminal-growth DCF anchored on AVGO's *absolute* cash generation (Fair Value $138.83) values the stock dramatically below both the current price ($360.45) and the multiples-based scenario fair value ($485.63), which is itself anchored on AVGO's *own trailing 5-year PE range*. This is not a calculation error — it reflects that AVGO's current re-rating (driven by the AI-semiconductor supercycle) is priced well above what a disciplined long-run DCF would support once growth is faded to a GDP-level terminal rate, even though it still looks statistically "cheap" relative to where AVGO's own multiple has traded historically. Both are legitimate lenses; this is exactly the kind of tension Rule 3's triangulation is meant to surface, not hide.

```
Triangulation (Rule 3, Tech/Growth weights): Blended FV = 40% × DCF + 60% × Multiples
                                            = 0.40 × $138.83 + 0.60 × $485.63
                                            = $55.53 + $291.38
                                            = $346.91
```

### Order Setup Checklist

```
[✓] Composite Score (incl. Quality blend):    43.1 — "Cheap" (30.0–49.9 band)
[✓] Expected annual return E / catalyst:      +35.9% / 1.5yr (feeds the Upside/Downside Modifier, §6)
[✓] Upside/Downside Modifier applied:         −15.0
[✓] DCF Fair Value:                           $138.83
[✓] Multiples-Based Fair Value:               $485.63
[✓] Blended Fair Value:                       $346.91
[ ] Margin of Safety %:                       25–30% (Composite 30.0–49.9 band)
    Buy Price range: $242.84 (30% MoS) – $260.18 (25% MoS); midpoint (27.5%) = $251.51
[✓] PRIMARY SELL TARGET:                      $346.91 (Blended FV, baseline)
[✓] BULL-CASE TRIM TARGET:                    $725.41 × 0.90 = $652.87
[ ] STOP LOSS: 25–30% max loss from Buy Price
    At midpoint Buy Price $251.51 → Stop $182.34
[✗] Risk/Reward Ratio: (346.91 − 251.51) / (251.51 − 182.34) = 95.40/69.17 = 1.38:1
    Checked across the full 25–30% MoS range: 1.33:1 – 1.43:1 — FAILS the 2:1 minimum throughout.
```

**Per fair-value-methodology.md Step 6 ("Below 2:1 = do not enter... wait for lower entry, find tighter stop, or pass on the trade entirely"): R/R fails the minimum threshold across the entire applicable MoS range. No order is placed.**

**Position sizing is also moot for a different reason:** AVGO's current 4.01% weight already sits **within** the Composite Score's implied 3–5% "Standard position" target band — there is no sizing gap to fill even before the R/R gate is considered.

### Net Action: **HOLD** — maintain the current 6-share position as-is

- No trim: Composite Score (43.1) is far below any trim threshold (70.0+).
- No add: R/R on the computed order setup fails the 2:1 minimum, and the position is already within its Composite-Score-implied target size.
- **The open 2026-06-16 override remains unresolved** (§0) — this rescore does not change that; the position continues to be held outside the framework's own entry rule, tracked in `override-log.md`, pending the user's rationale.

This mirrors the pattern already established elsewhere in `holdings.md` for other BUY-band-scored holdings (MSFT, UBER, V, NOW, NVDA): a favorable score band does not automatically mean an executable trade — independent gates (here, R/R) can and do block it.

---

## 10. Next Review Trigger

**Date/event:** AVGO's Q3 FY2026 earnings release (expected ~September 2026) — re-run Phase 01/02 with refreshed TTM figures, re-check the VMware-amortization roll-off (which would mechanically improve EV/EBIT and the DCF's near-term growth base), and re-confirm the PEG-eligibility ruling. Earlier trigger on a >15% unexplained move from $360.45 (Rule 9), a guidance revision / M&A / management change, or new third-party market-share data that would resolve the Moat_Score sensitivity flagged in §3. **Separately and unconditionally: the 2026-06-16 override still needs the user to supply a rationale** for `decisions/` and `override-log.md` — not tied to any valuation trigger.

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

# RESCORE — UBER (Uber Technologies, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Trigger:** Routine 6 (Telegram Stock-Mention Scan, hourly) — [t.me/tarasguk](https://t.me/tarasguk) post `tarasguk/11626` (~2026-08-07 14:33 UTC), claiming Uber reported Q2 2026 earnings (revenue $14.2B vs $14.24B est, adjusted EPS $0.81 vs $0.81 est). **Per CLAUDE.md Rule 0, the post's text was never used as a scored input** — it is a trigger only. It happens to coincide with a legitimate, independent, on-schedule Rule 9 trigger: UBER's own [2026-07-05 watchlist entry](../watchlist/in-portfolio/UBER/UBER-2026-07-05.md) named "Next review trigger: Next earnings (~early Aug 2026)," and this session's independently-fetched data (§3) confirms a real ~$14.2B quarterly revenue print did occur, without relying on the post for the figure.
**Date:** 2026-08-07
**10Y US Treasury Yield:** 4.656% (Yahoo `^TNX` regularMarketPrice, 2026-08-07) — up from 4.62% (07-14) and 4.44% (06-20), still inside the same 3.5–5% bracket.
**Rate Regime Modifier (Step 2):** +5 (unchanged bracket)
**Last review on record:** UBER **39.4** (Valuation) / **61.0** (Quality) / **39.2** (Composite, reference-only) — 2026-07-14, [sessions/2026-07-14-rescore-uber.md](2026-07-14-rescore-uber.md). Action: HOLD existing, no add.
**⚠️ Methodology note:** UBER's Quality Score and Composite Score have in fact been computed every session since 2026-06-29 (07-05 and 07-14, both above) — the **current** watchlist pointer file (07-05) carries no stale banner. A `⚠️ STALE SCORE` banner does still sit on the **older, superseded** [UBER-2026-06-20.md](../watchlist/in-portfolio/UBER/UBER-2026-06-20.md) entry (a leftover from before the Quality Score engine existed, never cleaned up when 07-05 superseded it), and [watchlist/STALE.md](../watchlist/STALE.md) carries no UBER row. This session computes fresh Quality/Valuation/Composite scores under the current (2026-06-29) methodology regardless, and clears the leftover 06-20 banner as part of this run's housekeeping (§12).
**Current UBER portfolio weight:** 0.35% per [holdings.md](../portfolio/holdings.md) — nowhere near the 15% hard cap (Upgrade 7).

**Rule 0 data-fetch note:** `yfinance` failed in-sandbox this session with the same recurring `curl_cffi` TLS-impersonation/connection-reset failure documented across many prior sessions. Worked around per Rule 0's documented contingency: plain `requests` (with the sandbox's CA bundle) hitting Yahoo Finance's `chart`, `quoteSummary`, and `fundamentals-timeseries` endpoints directly (using a session-warmed cookie + crumb from `query2.finance.yahoo.com`), cross-checked against IBKR for the live price. All figures below trace to this fetch, not to the Telegram post.

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$74.62** | IBKR `get_price_snapshot` (contract_id 365207014, NYSE primary), `last`, bid $74.64 / ask $74.66, ts ~2026-08-07 15:55 UTC, no halt. |
| Cross-check | $74.71–$74.74 | Yahoo Finance `regularMarketPrice` — consistent (within the bid/ask spread). |
| 52-week range | $65.42 – $101.98 | IBKR `misc_statistics`. |
| Dividend yield | 0.0% | No dividend — IBKR + Yahoo consistent. |
| Analyst consensus PT | mean **$101.61**, range $70–$150, n=47, "Strong Buy" | Yahoo `financialData` — bull-case sanity check only (Rule 0 Step 4), not a scored input. |
| Price vs. 07-14 review ($72.10) | **+3.50%** | Well under the 15% Rule 9 unexplained-move threshold. |

**IBKR $74.62 used as the Rule-0 primary price**, per this framework's established convention.

---

## 2. Data Gaps / Flags

1. **Q2 2026 discrete quarterly financials not yet in Yahoo's structured feed (data lag).** Yahoo's quarterly `fundamentals-timeseries` series still ends at Q1 2026 (period ending 2026-03-31); Q2 2026 (period ending ~2026-06-30) has not yet appeared as its own line, even though the **TTM aggregate figures below already include it** (see §3). This means several sub-scores below had to be built from TTM aggregates (revenue × TTM margin) rather than a directly-reported discrete-quarter EBIT/net income figure — flagged explicitly at each such calculation, not silently treated as equivalent to a real reported number.
2. **Net debt does not reconcile across three sources this session — a genuine, unresolved data-integrity flag:**
   - **Current-snapshot balance sheet** (Yahoo `defaultKeyStatistics`, presumably reflecting the just-reported Q2 2026 quarter): Total debt $14.731B, Total cash $5.391B → **Net debt $9.340B**.
   - **Last discretely-reported quarter** (2026-03-31, Q1 2026): Total debt $12.419B, Cash $5.558B → **Net debt $6.861B**.
   - **Yahoo's own computed Enterprise Value** ($153.93B) implies a net debt of only ~$1.5B against this session's market cap (§4) — reconciling with **neither** of the above. Not usable; likely reflects a stale EV cache on Yahoo's side or a different share-count/price snapshot time.
   - **Choice made and why:** this session uses the **current-snapshot net debt ($9.340B)** as primary, since Rule 0 favors the freshest available balance-sheet data (most likely to reflect the just-reported Q2 2026 quarter) over a quarter-old figure, and because it is the more conservative (higher-leverage) of the two usable numbers. The Q1'26-quarter figure ($6.861B) is shown as an explicit sensitivity at each affected calculation. Yahoo's own EV figure is not used at all — flagged as unreliable, not silently trusted.
3. **`EBITDA (TTM)` given directly by Yahoo ($7.474B) implies an unrealistically low ~$118M of TTM D&A** (EBITDA − computed EBIT ≈ $7.474B − $7.356B), versus ~$700–750M of D&A in every prior session's SEC-sourced figures. Likely a stale/inconsistent field on Yahoo's side (possibly mixing a GAAP EBIT-ish figure with a different EBITDA vintage). Used anyway for the Balance Sheet sub-score's Net Debt/EBITDA denominator (§5) since it's the only EBITDA figure available this session without inventing a D&A estimate — flagged, not silently trusted.
4. **FCF TTM ($7.239B) is materially lower than FY2025 annual FCF ($9.763B)** — flagged in the source data as "likely reflects Q2'25's stronger comp quarter rolling out; not necessarily deterioration." This creates a large sensitivity in both the Quality Score's FCF Quality sub-score and the Valuation Score's FCF Yield/scenario-architecture inputs — shown as a full parallel calculation in §5/§7/§8, not picked silently.
5. **Growth sub-score TAM/pricing-power evidence is carried forward unchanged from 2026-07-05** (Gross Bookings +25% YoY, MAPC +17% YoY, Uber One 50M members, per Uber's Q1 2026 earnings release) — no fresher company-specific growth commentary exists in this session's data packet beyond the aggregate TTM revenue growth figure (12.2%, still robust, no deceleration signal). Not re-derived from a new source this session; flagged as carried-forward evidence per Rule 6.
6. **Moat Signal "Market share stable/growing" citation is still March 2024** (Bloomberg Second Measure) — over two years stale, unchanged open item from every prior UBER session.
7. **Shareholder yield (net buyback rate) is carried forward unchanged (+2.5%/yr)** from the 07-05 session's SEC share-count computation — no updated share-count-history datapoint exists in this session's verified data packet to recompute it fresh.
8. **PEG / Fast-Grower eligibility — still not qualifying.** Trailing GAAP diluted EPS remains extremely volatile even ex-outliers (Q1'25 $0.83 → Q2'25 $0.63 → Q3'25 $3.11 spike → Q4'25 $0.14 → Q1'26 $0.13) — not a clean, reliable 3-year >15%/yr EPS growth base. PEG stays **Not Applicable**, its 15% weight redistributed to EV/EBIT (→ 40%), unchanged from every prior UBER session.
9. **5yr historical PE range — no-history fallback still applies**, unchanged rationale from every prior UBER session (GAAP-loss-making through FY2022, no meaningful 5yr PE band).

No data was invented anywhere below. Every fallback/flag is the documented one from the framework, not an ad hoc substitute.

---

## 3. Independent Corroboration of the Telegram Post's Earnings Claim

Per Rule 0, the post's own numbers were never used — but its underlying claim (a Q2 2026 earnings release occurred) was checked independently before treating this as a valid trigger:

```
Yahoo financialData TTM total revenue           = $55.227B  (revenue growth 12.2%)
Sum of last 4 discretely-reported quarters       = Q3'25 $13.467B + Q4'25 $14.366B + Q1'26 $13.203B
                                                   = $41.036B  (only 3 quarters — Q2'25 not summed,
                                                     since the TTM window has already rolled past it)
Implied newest (Q2 2026) quarter                 = $55.227B − $41.036B ≈ $14.19B
```

This is **within rounding of** the Telegram post's claimed $14.2B — independently derived from Yahoo's own live TTM aggregate, not from the post. **This corroborates that a real Q2 2026 earnings release occurred**, consistent with UBER's own documented "next earnings ~early August 2026" review trigger — a valid, on-schedule Rule 9 event regardless of the Telegram post. As noted in §2 flag 1, the discrete Q2 2026 quarter has not yet appeared in Yahoo's structured quarterly feed, so quarter-specific EBIT/margin/FCF detail for Q2 2026 *alone* is not independently available this session — only the TTM aggregate that includes it.

---

## 4. Inputs Collected (this session)

| Item | Value | Basis |
|---|---|---|
| Shares outstanding | 2,042.56M | Yahoo `defaultKeyStatistics` |
| **Market Cap** | 2,042.56M × $74.62 = **$152,415.8M** | Computed |
| Total debt (current snapshot) | $14.731B | Yahoo, flagged §2.2 |
| Cash (current snapshot) | $5.391B | Yahoo, flagged §2.2 |
| **Net Debt (primary, current-snapshot)** | $14.731B − $5.391B = **$9.340B** | Computed |
| Net Debt (sensitivity, Q1'26 quarter) | $12.419B − $5.558B = **$6.861B** | 2026-03-31 quarterly balance sheet |
| **EV (primary)** | $152,415.8M + $9,340M = **$161,755.8M** | Computed |
| Revenue (TTM) | $55.227B | Yahoo `financialData` |
| Revenue growth (TTM, YoY) | 12.2% | Yahoo `financialData` |
| Gross margin (TTM) | 40.75% | Yahoo |
| Operating margin (TTM) | 13.32% | Yahoo |
| **EBIT (TTM, computed)** | $55.227B × 13.32% = **$7.356B** | Computed — §2 flag 1 (no discrete Q2'26 EBIT exists yet) |
| EBIT (FY2025, annual) | $6.240B | Given annual table |
| Net margin (TTM) | 17.35% | Yahoo |
| **GAAP Net Income (TTM, computed)** | $55.227B × 17.35% = **$9.582B** | Computed — same basis caveat |
| Net Income (FY2025, annual) | $10.053B | Given annual table |
| **Normalized Net Income (TTM)** | $9.582B − $4.9B (Q3'25 tax release) − $1.5B (Q3'25 equity gain) + $1.494B (Q1'26 equity loss) = **$4.676B** | Company-disclosed one-off dollar figures, still inside the current TTM window (Q3'25–Q2'26) — same normalization as 07-05/07-14 |
| FCF (TTM) | $7.239B | Yahoo `financialData`, flagged §2.4 |
| FCF (FY2025, annual) | $9.763B | Given annual table |
| EBITDA (TTM) | $7.474B | Yahoo, flagged §2.3 |
| Book value/share | $12.154 | Yahoo |
| **Total Equity (computed)** | $12.154 × 2,042.56M = **$24.825B** | Computed |
| Revenue FY2022 → FY2025 | $31.877B → $52.017B | Given annual table |
| **Revenue 3yr CAGR** | (52.017/31.877)^(1/3) − 1 = **17.73%** | Computed |
| ROE (TTM) | 37.16% | Yahoo, reference cross-check only |
| ROA (TTM) | 6.88% | Yahoo, reference cross-check only |
| Forward EPS (consensus) | $4.3806 | Yahoo |
| **Forward PE (recomputed on live price)** | $74.62 ÷ $4.3806 = **17.03×** | Computed — Yahoo's own displayed 17.05× is consistent within rounding |
| Diluted EPS, last 5 quarters | $0.83 / $0.63 / $3.11 / $0.14 / $0.13 | Given quarterly table — confirms PEG non-eligibility (§2 flag 8) |

---

## 5. UBER — Quality Score (2026-06-29 methodology)

### Hard disqualifier check (fiscal-year rolling window, per the [2026-08-05 rolling-window clarification](../framework/quality-scoring.md))

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years unexplained? | FY2023 178.2% / FY2024 69.96% / FY2025 97.12% — only **one** year dips (barely) below 70%, not consecutive | disqualify if 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | 1.25× (primary) / 0.92× (sensitivity) | disqualify if >2.5× | ✅ PASS, comfortably either way |
| FCF-positive 3+ consecutive years? | FY2023/2024/2025 all positive | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight) — normalized, per Rule 6

```
Normalized Net Margin (TTM) = $4.676B / $55.227B = 8.47%
NetMargin_Component         = clamp((8.47/30)×100, 0, 100)  = 28.23

Normalized effective tax rate = 23.42% (carried forward from 07-05's SEC-sourced computation —
   no fresher quarterly tax breakdown exists yet for the current TTM window, §2 flag 1)
NOPAT = EBIT(TTM, $7.356B) × (1 − 0.2342) = $5.633B
Invested Capital = Total Debt (current, $14.731B) + Total Equity ($24.825B) = $39.556B
ROIC (TTM, normalized) = $5.633B / $39.556B = 14.24%
ROIC_Component = clamp((14.24/30)×100, 0, 100) = 47.47

Profitability_Score = (28.23 + 47.47) / 2 = 37.85
```
No FCF-positive cap applies (3+ consecutive years positive, confirmed above).

### Margins (15% weight)

```
GrossMargin_Score = clamp((40.75/80)×100, 0, 100) = 50.94
```
TTM margin (40.75%) already sits above the 40% bonus threshold, so the structural-trend bonus doesn't apply regardless of trend direction (same rule as every prior UBER session). No bonus.

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $31.877B → FY2025 $52.017B) = 17.73%
Growth_Score = clamp((17.73/25)×100, 0, 100) = 70.92
```
**+10 (carried forward, §2 flag 5):** documented TAM/platform-growth evidence from Uber's Q1 2026 earnings release (Gross Bookings +25% YoY, MAPC +17% YoY, Uber One 50M members) — no fresher company-specific commentary exists this session, but the TTM aggregate revenue growth (12.2%) shows no deceleration signal that would instead warrant the −10 modifier.
```
Growth_Score (with bonus) = clamp(70.92 + 10, 0, 100) = 80.92
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA (primary, current-snapshot net debt) = $9.340B / $7.474B = 1.25×
BalanceSheet_Score (primary) = clamp(100×(1 − 1.25/4), 0, 100) = 68.76

Sensitivity (Q1'26-quarter net debt): $6.861B / $7.474B = 0.92×
BalanceSheet_Score (sensitivity) = clamp(100×(1 − 0.92/4), 0, 100) = 77.05
```
Standard /4 denominator (no asset-light override — UBER is a marketplace, not a payment network/exchange).

### Moat Signal (15% weight) — carried forward unchanged from 2026-07-05 (no new evidence this session)

| Signal | Marked | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** (dated, flagged) | Bloomberg Second Measure: ~76% of observed US rideshare spend, March 2024 — still the most recent independent figure found (§2 flag 6). |
| Brand premium | FALSE | No cited pricing-power-specific evidence. |
| Network effect | **TRUE** | Uber's own FY2025 10-K: "Our massive, efficient, and intelligent network... becomes smarter with every trip." |
| Switching costs | FALSE | Uber's own 10-K discloses driver multi-homing is unrestricted. |
| Scale cost advantage | FALSE | No cost-per-trip data found vs. smaller competitors. |

```
Moat_Score = (2/5) × 100 = 40.0
```

### FCF Quality (10% weight)

```
FCF/NI (TTM, GAAP basis, primary) = $7.239B / $9.582B = 75.56%
FCFQuality_Score (primary) = clamp(((0.7556 − 0.40)/0.60)×100, 0, 100) = 59.27

Sensitivity (FY2025 annual basis): $9.763B / $10.053B = 97.12%
FCFQuality_Score (sensitivity) = clamp(((0.9712 − 0.40)/0.60)×100, 0, 100) = 95.20
```
The primary (TTM) figure is materially lower than every prior UBER session's FCF Quality sub-score (100.0) — a direct consequence of the TTM FCF dip flagged in §2.4. Still passes the hard disqualifier (75.56% > 70%), but worth tracking closely once the discrete Q2 2026 quarter posts.

### Quality Score — Final

```
Quality Score = (37.85×0.25) + (50.94×0.15) + (80.92×0.20) + (68.76×0.15) + (40.0×0.15) + (59.27×0.10)
              = 9.4625 + 7.6410 + 16.184 + 10.314 + 6.000 + 5.927
              = 55.5285 → rounds to 55.5
```

# Quality Score = 55.5 — FAILS the 80.0+ gate, decisively.

**Sensitivity range (shown transparently, no black box):** substituting the Q1'26-basis Balance Sheet score (77.05) and/or the FY2025-annual-basis FCF Quality score (95.20) instead of the TTM-primary figures moves the total between **55.5 and 60.4** depending on which combination is used. **Every combination still lands well below the 80.0 gate** — this remains a robust FAIL, not a knife-edge case, consistent with every prior UBER session (07-05/07-14 both computed 61.0). This session's figure (55.5) is somewhat *lower* than the prior 61.0 — driven by the current-snapshot Balance Sheet inputs (higher flagged net debt) and the TTM FCF dip (§2.4), not by any improvement in the underlying disqualifier picture; Profitability actually improved slightly (37.85 vs 33.95 previously) on a normalized basis.

---

## 6. UBER — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 17.03 = 5.872%
Spread = EY − 10Y Treasury = 5.872% − 4.656% = +1.216pp
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (short by ~0.28pp) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.656% → "3.5–5%" bracket → **+5**

**Total Rate Modifier = +10**

---

## 7. UBER — Phase 02 Valuation Score

*Primary basis: FY2025-annual FCF/EBIT, for period-consistency (continuity with the 2026-06-20 UBER session's own explicit choice — see also §2 flags 1 and 4 on why a clean TTM pairing isn't fully available this session). Sensitivity shown using TTM-basis figures throughout.*

**FCF Yield — 40% weight**
```
FCF Yield (primary, FY2025 annual) = $9.763B / $152,415.8M = 6.406%
FCF_Score (primary) = clamp(100 × (1 − 6.406/10), 0, 100) = 35.94

FCF Yield (sensitivity, TTM) = $7.239B / $152,415.8M = 4.749%
FCF_Score (sensitivity) = clamp(100 × (1 − 4.749/10), 0, 100) = 52.51
```
→ Contribution (primary): 35.94 × 0.40 = **14.38**

**EV/EBIT — 25% + 15% (PEG redistributed) = 40% weight**
```
EV/EBIT (primary, FY2025 annual EBIT) = $161,755.8M / $6,240M = 25.92×
EV/EBIT_Score (primary) = clamp((25.92 − 12)/23 × 100, 0, 100) = 60.53

EV/EBIT (sensitivity, TTM EBIT) = $161,755.8M / $7,356M = 21.99×
EV/EBIT_Score (sensitivity) = clamp((21.99 − 12)/23 × 100, 0, 100) = 43.45
```
→ Contribution (primary): 60.53 × 0.40 = **24.21**

**Forward PE — no-history fallback — 20% weight**
```
FwdPE_Score = 50.0 (neutral midpoint, flagged — same no-history rationale as every prior UBER session)
```
→ Contribution: 50.0 × 0.20 = **10.0**

**PEG — 15%: still N/A** (§2 flag 8) — redistributed to EV/EBIT above.

**Raw weighted score (primary):**
```
= 14.38 + 24.21 + 10.0 = 48.59
```
**+ Rate Modifier (+10) = 58.59** (before the Upside/Downside Modifier)

**Raw weighted score (TTM sensitivity):**
```
= 21.00 + 17.38 + 10.0 = 48.38  → + Rate Modifier (+10) = 58.38
```

---

## 8. UBER — Upside/Downside Modifier (Expected-Return Modifier)

GAAP EPS is still too distorted (§2 flag 8) for an EPS×PE scenario set — continuing the P/FCF scenario architecture established 2026-07-05.

**Primary (FY2025-annual FCF anchor, $9.763B):**

| Scenario | Weight | Projected FCF | Growth assumption | FCF/share | Exit P/FCF | Fair Value |
|---|---|---|---|---|---|---|
| Bull | 25% | $11.520B | +18%/yr (historical FCF-growth pace) | $5.641 | 24× | **$135.38** |
| Base | 50% | $10.739B | +10%/yr (conservative vs. 17.7% revenue CAGR) | $5.258 | 18× | **$94.65** |
| Bear | 25% | $7.239B | 0% — the current (lower) TTM run-rate persists | $3.545 | 12× | **$42.54** |

```
PW Fair Value = 0.25×135.38 + 0.50×94.65 + 0.25×42.54 = $91.81
```
Sits below the $101.61 analyst consensus mean PT (Guardrail 2 — scenario-weighted, not the rosy point).

```
Gap Upside %     = ($91.81 ÷ $74.62) − 1 = +23.04%
Catalyst window  = 2 years (Rule 10 default — Uber One scale-up, AV-partner monetization, ongoing
   margin-expansion path; no single dated event narrower than this)
Annualized gap   = 23.04% ÷ 2 = +11.52pp
Intrinsic growth = +12.0%/yr  (carried forward, conservative vs. 17.73% revenue CAGR)
Shareholder yield = +2.5%/yr  (carried forward, §2 flag 7 — no fresher share-count-history data)

E = 11.52 + 12.0 + 2.5 = +26.02%/yr
```
```
E ≥ H(10%) → M = −15 × clamp((26.02 − 10)/15, 0, 1) = −15 × clamp(1.068, 0, 1) = −15.0 (floored)
```

**Sensitivity (TTM FCF anchor, $7.239B, same growth-rate assumptions applied for comparability):**

| Scenario | Projected FCF | FCF/share | Exit P/FCF | Fair Value |
|---|---|---|---|---|
| Bull (+18%) | $8.542B | $4.183 | 24× | $100.40 |
| Base (+10%) | $7.963B | $3.899 | 18× | $70.18 |
| Bear (0%) | $7.239B | $3.545 | 12× | $42.54 |

```
PW Fair Value (sensitivity) = 0.25×100.40 + 0.50×70.18 + 0.25×42.54 = $70.83
Gap Upside % = ($70.83 ÷ $74.62) − 1 = −5.08%   (a slight negative gap on this base)
Annualized gap = −5.08% ÷ 2 = −2.54pp
E (sensitivity) = −2.54 + 12.0 + 2.5 = +11.96%
M (sensitivity) = −15 × clamp((11.96 − 10)/15, 0, 1) = −15 × 0.131 = −1.96
```

**Guardrail checks (primary):** (1) documented catalyst within 18–24mo → upside credit allowed; (2) scenario-weighted PW FV below analyst consensus mean ✓; (3) full calc shown ✓; (4) bounded ±15, floor reached ✓.

---

## 9. UBER — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE (primary) = Raw weighted (48.59) + Rate Modifier (+10) + Upside/Downside (−15.0)
                                 = 43.59 → 43.6
```

| | Primary | TTM sensitivity |
|---|---|---|
| Raw weighted | 48.59 | 48.38 |
| Rate Gate | +10 | +10 |
| Upside/Downside Modifier | −15.0 | −1.96 |
| **FINAL VALUATION SCORE** | **43.6** | **56.4** |
| Prior valuation score (07-14) | 39.4 | 39.4 |
| **Quality Score** | **55.5** (FAILS 80.0+ gate) | — |

**Critical flag:** the primary (FY2025-annual-basis) and TTM-basis calculations land in **different action bands** — 43.6 is "Cheap" (30.0–49.9), 56.4 is "Fair Value / Hold" (50.0–69.9) — driven almost entirely by which FCF print (annual vs. TTM) is used as the fair-value anchor (§2 flag 4), not by the net-debt-figure choice (which moves the score by <1 point either way). **This does not change the action recommendation below**, because the Quality Score decisively fails the 80.0+ gate under every combination tested (§5) — but it is flagged prominently since it would matter a great deal once/if UBER ever clears the quality gate. Recommend a fast follow-up once Q2 2026's discrete quarterly FCF actually posts (§2 flag 1), rather than waiting a full quarter, specifically to resolve this ambiguity.

**Composite Score — reference only, per established practice for a Quality-Score-gate failure on an existing holding:**
```
Composite Score = 0.50×(100 − 55.5) + 0.50×43.6 = 0.50×44.5 + 0.50×21.8... 
                 = 22.25 + 21.8 = 44.05 → boundary rule (.X5 exact) rounds UP → 44.1
```
**Composite Score = 44.1** (vs. 39.2 on 07-14). **Not adopted to drive the action recommendation** — shown for the record only, per "no black box."

---

## 10. UBER — Action Recommendation

**Two independent facts, either one alone is enough to conclude HOLD/no-add — same structure as every UBER session since 2026-07-05:**

1. **Quality Score (55.5) fails the 80.0+ gate decisively** (§5), and by a wider margin than the 61.0 recorded on 07-05/07-14. Robust across every sensitivity tested (55.5–60.4). This remains the same **value-trap flag** first raised 2026-07-05: a Valuation Score that reads statistically attractive sitting on top of a business that hasn't cleared this framework's quality bar — reinforced, not resolved, by this session's fresher (if partly TTM-derived) data.
2. **Order-setup R/R check, for completeness (reference only, since action is driven by the gate failure regardless):**

```
Blended Fair Value (= primary PW FV):        $91.81
Margin of Safety (30.0–49.9 band):           28%  (same convention as every prior UBER session)
BUY PRICE (limit):                           $91.81 × (1 − 0.28) = $66.10
PRIMARY SELL TARGET:                         $91.81
BULL-CASE TRIM TARGET (bull × 0.90):         $135.38 × 0.90 = $121.84
STOP LOSS (Buy × (1 − 28%)):                 $66.10 × 0.72 = $47.59
R/R at formal entry = (91.81 − 66.10) ÷ (66.10 − 47.59) = 25.71 ÷ 18.51 = 1.389:1  ❌ below 2:1
R/R at live price   = (91.81 − 74.62) ÷ (74.62 − 47.59) = 17.19 ÷ 27.03 = 0.636:1  ❌ further below 2:1
   (worse than 07-14's 1.112:1 — the live price has moved closer to the estimated fair value,
   narrowing the reward side of the ratio while the stop distance is unchanged)
```

**Net: HOLD the existing 0.35% position. No fresh capital added — doubly blocked, unchanged from every UBER session since 07-05: an independent R/R failure and the Quality Score's decisive gate failure.**

**Position cap check:** 0.35% is nowhere near the 15% hard cap (Upgrade 7) — not binding, included for completeness. No BUY or TRIM action taken; **no order placed, modified, or submitted** — recommendation only, per this run's explicit scope.

**Open item, carried forward unchanged:** the 07-05 session recommended the user consider logging a **Human Override** entry (mirroring the ZS/NOW precedent for a held, quality-gate-failing position) — checked `override-log.md` this session, still not logged. Still flagged, not decided or written by this RESCORE (out of its scope).

---

## 11. Next Review Trigger

- **Routine:** UBER Q3 2026 earnings, expected early November 2026 (unconfirmed exact date, based on Uber's typical quarterly cadence).
- **Priority follow-up (new this session):** once Q2 2026's discrete quarterly financials post to Yahoo's structured feed (§2 flag 1), re-run the Valuation Score specifically to resolve the primary-vs-TTM-basis ambiguity flagged in §9 — a real, materially-swinging open question, not just a routine refresh.
- **Open data item, carried forward:** the March 2024 US rideshare market-share citation is still stale (§2 flag 6).
- **Open item, carried forward:** the value-trap / Quality Watch flag and the still-undecided Human Override question (§10).
- **Watch:** the FCF/NI conversion trend (§5 FCF Quality) — TTM basis has dropped materially below every prior session's figure; confirm with real Q2 2026 numbers whether this is a rolling-window base-effect artifact (as flagged) or a genuine cash-conversion softening.
- **Rule 9 triggers (standing):** guidance revision, M&A/material AV investment, management change, a >15% unexplained price move, or the Q3 2026 earnings print itself.

---

## 12. Housekeeping

- Cleared the leftover `⚠️ STALE SCORE` banner from [watchlist/in-portfolio/UBER/UBER-2026-06-20.md](../watchlist/in-portfolio/UBER/UBER-2026-06-20.md) (per the methodology note above — this run computes a fresh score under the current methodology in any case, and the banner was stale bookkeeping on an already-superseded entry).
- No UBER row existed in [watchlist/STALE.md](../watchlist/STALE.md) — confirmed nothing to delete there.
- New dated watchlist entry created: [watchlist/in-portfolio/UBER/UBER-2026-08-07.md](../watchlist/in-portfolio/UBER/UBER-2026-08-07.md).
- [holdings.md](../portfolio/holdings.md) UBER row updated: Last Score 43.6, Quality Score 55.5, Composite Score 44.1, Last Review 07 Aug 2026.

---

## Glossary

| Term | Meaning |
|---|---|
| **AV (Autonomous Vehicle)** | A self-driving vehicle; "robotaxi" is an AV run as an on-demand ride-hailing service. Uber partners with (rather than builds) AV developers to deploy AVs on its platform. |
| **CAGR** | Compound Annual Growth Rate. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate; shown as reference-only, not-adopted for UBER this session (55.5 Quality Score still fails the gate). |
| **D&A** | Depreciation & Amortization. |
| **Deferred tax valuation allowance release** | A one-off GAAP accounting event reversing a prior write-down on deferred tax assets — inflates net income/EPS without cash impact. The source of UBER's $4.9B Q3 2025 tax benefit, still normalized out of this session's TTM window. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Peter Lynch's term for EPS growth >15%/yr for 3+ years on a clean earnings base — this framework's PEG-eligibility trigger. UBER doesn't qualify (§2). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit cash quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Gross Bookings** | The total dollar value of activity transacted through Uber's platform before Uber's own take-rate/revenue is deducted. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. |
| **Human Override** | A position held outside the framework's own rules — tracked in `override-log.md`; still an open, undecided item for UBER. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **MAPC (Monthly Active Platform Consumers)** | The number of unique consumers who used at least one Uber offering in a given month. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the numerator of ROIC. |
| **P/FCF (Price-to-Free-Cash-Flow)** | Market capitalization ÷ Free Cash Flow — an earnings-multiple analog used in UBER's scenario architecture since GAAP EPS is too distorted for a reliable EPS×PE set. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. UBER: 55.5, fails the gate. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive adjustment for the current Treasury-yield band. |
| **ROA (Return on Assets)** | Net Income ÷ Total Assets — how efficiently a company generates profit from its full asset base; shown here as a cross-check reference only, not a scored framework input. |
| **ROE** | Return on Equity — Net Income ÷ shareholder equity. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; normalize before valuing / require a minimum 2:1 risk/reward; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs. the 10% hurdle. |
| **Value trap** | A stock that looks statistically cheap but stays cheap because underlying business quality is deteriorating or was never strong enough to support a re-rating — the risk UBER's Quality Score gate failure continues to flag. |

# RESCORE — UBER (Uber Technologies, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Trigger:** User-requested rescore, specifically to follow up on the open item flagged in the [2026-08-07 session](2026-08-07-rescore-uber.md) — whether UBER's Q2 2026 discrete quarterly financials have posted yet (resolving the primary-vs-TTM-basis Valuation Score ambiguity), and whether Q3 2026 earnings have been reported.
**Date:** 2026-09-15
**10Y US Treasury Yield:** 4.961% (`^TNX`, latest close 2026-09-14) — up sharply from 4.656% (08-07), now near the top of the 3.5–5% bracket (intraday high 5.012% on 09-14, per WebSearch corroboration of a multi-year-high yield environment this week).
**Rate Regime Modifier (Step 2):** +5 (still inside 3.5–5% bracket, but close to rolling into the >5% (+10) bracket — worth watching).
**Last review on record:** UBER **43.6** (Valuation, primary FY25-annual basis) / **56.4** (Valuation, TTM-aggregate sensitivity) / **55.5** (Quality) / **44.1** (Composite, reference-only) — 2026-08-07, [sessions/2026-08-07-rescore-uber.md](2026-08-07-rescore-uber.md). Action: HOLD existing, no add.
**Current UBER portfolio weight:** 0.35% per [holdings.md](../portfolio/holdings.md) — nowhere near the 15% hard cap (Upgrade 7).

**Rule 0 data-fetch note:** `yfinance` worked without the `curl_cffi` TLS failure that blocked it on 08-07 — used directly this session, cross-checked against IBKR for live price and 52-week stats. `^TNX` quoteSummary calls still hit a rate-limited/crumb-auth wall via `t.info`, so the 10Y yield was pulled from `t.history()` (which worked fine) instead, cross-checked against WebSearch reporting the 10Y "topped 5% this week, highest since 2007" — consistent.

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$72.19** | IBKR `get_price_snapshot` (contract_id 365207014, NYSE primary), `last`, bid $72.19 / ask $72.49, ts ~2026-09-15 (session open), no halt. |
| Cross-check | $72.63 | yfinance `regularMarketPrice` — consistent (within ~0.6%, inside the bid/ask-adjacent range). |
| 52-week range | $65.42 – $101.98 | IBKR `misc_statistics`. |
| Dividend yield | 0.0% | No dividend — yfinance confirms `dividendYield: None`. |
| Analyst consensus PT | mean **$101.21**, n=47, "Buy" | yfinance `targetMeanPrice` — bull-case sanity check only (Rule 0 Step 4), not a scored input. |
| Price vs. 08-07 review ($74.62) | **−3.26%** | Well under the 15% Rule 9 unexplained-move threshold — not itself a trigger. |

**IBKR $72.19 used as the Rule-0 primary price**, per this framework's established convention.

---

## 2. Data Gaps / Flags — and the Q2 2026 Ambiguity Resolution

**Headline result: the primary-vs-TTM-basis ambiguity flagged 2026-08-07 is now resolved.** UBER's Q2 2026 discrete quarter (period ended 2026-06-30) has posted to `yfinance`'s structured quarterly feed — confirmed via `t.quarterly_financials`, `t.quarterly_cashflow`, and `t.quarterly_balance_sheet`, all of which now carry a `2026-06-30` column with real reported figures (Revenue $14.191B, Operating Income $1.890B, Net Income $2.394B, Diluted EPS $1.17, FCF $2.792B). This lets the Valuation Score be built off a **real trailing-twelve-month (TTM) sum of four actually-reported quarters** (Q3'25 + Q4'25 + Q1'26 + Q2'26) for the first time, rather than the TTM-aggregate-÷-cached-margin approximation used 08-07.

1. **The 08-07 session's stale-Yahoo-field flags are now resolved, not carried forward as open items:**
   - **Net debt no longer has a reconciliation problem.** The "current-snapshot vs. last-discrete-quarter" split from 08-07 is gone — Q2 2026 (2026-06-30) *is* now the latest discretely-reported quarter: Total debt $14.731B, Cash $5.391B → **Net debt $9.340B**, a single clean figure.
   - **FCF/NI conversion was NOT actually deteriorating** — it was a Yahoo TTM-aggregate artifact. Real summed-quarter TTM FCF is **$10.116B** (Q3'25 $2.230B + Q4'25 $2.808B + Q1'26 $2.286B + Q2'26 $2.792B) — *higher* than FY2025 annual FCF ($9.763B), not lower as the 08-07 session's Yahoo aggregate figure ($7.239B) implied. This directly resolves 08-07's flag #4.
   - **EBITDA (TTM)** computed as a real quarterly sum is **$7.920B** (Q3'25 $2.927B + Q4'25 $0.599B + Q1'26 $0.795B + Q2'26 $3.599B) — versus Yahoo's still-stale cached `ebitda` info field of $7.474B (unchanged from 08-07, confirming it really was a stale/cached value, not a fresh TTM figure). Used the real quarterly-sum figure this session.
2. **Effective tax rate (23.42%) still carried forward** from the 07-05 SEC-sourced computation — no cleaner isolated blended-TTM effective-tax-rate figure was derivable this session either (Q2'26's own reported quarterly tax rate of 26.0% is broadly consistent with this carried-forward figure, lending it some support, but this is not a fresh independent derivation).
3. **Shareholder yield recomputed fresh this session** (superseding the 08-07 carried-forward +2.5%/yr): FY2025 shares outstanding (2,067.905M) vs. FY2024 (2,107.953M) → net buyback rate of **+1.90%/yr**. No dividend. Shareholder yield = **+1.90%/yr**.
4. **Growth/TAM evidence refreshed** with UBER's actual Q2 2026 earnings release (August 5, 2026 — since superseded by nothing newer, see §11 on Q3 2026 status): Gross Bookings +24% YoY to $58.0B (4th consecutive quarter above 20% growth), MAPC +16% YoY to 208M, Trips +18% YoY to 3.9B. Source: [Uber Q2 2026 press release](https://www.stocktitan.net/news/UBER/uber-announces-results-for-second-quarter-nyhc6z8uh8yu.html), corroborated by Uber's own investor-relations site. This replaces the 08-07 session's Q1-2026-release citation.
5. **Moat Signal "Market share stable/growing" citation is still March 2024** (Bloomberg Second Measure) — no fresher independent third-party US rideshare market-share data was found this session either. Still an open, over-two-year-stale item, carried forward unchanged.
6. **PEG / Fast-Grower eligibility — still not qualifying.** Trailing GAAP diluted EPS remains extremely volatile: Q2'25 $0.63 → Q3'25 $3.11 (spike) → Q4'25 $0.14 → Q1'26 $0.13 → **Q2'26 $1.17** — not a clean, reliable 3-year >15%/yr EPS growth base. PEG stays **Not Applicable**, its 15% weight redistributed to EV/EBIT (→ 40%), unchanged from every prior UBER session.
7. **5yr historical PE range — no-history fallback still applies**, unchanged rationale (GAAP-loss-making through FY2022, only 3 consecutive profitable fiscal years on record).

No data was invented anywhere below. Every fallback/flag is the documented one from the framework, not an ad hoc substitute.

---

## 3. Q3 2026 Earnings Status (explicit check, per this session's brief)

Checked via WebSearch: **UBER has NOT yet reported Q3 2026 earnings.** Its last report (August 5, 2026) covered Q2 2026. Q3 2026 earnings are expected **late October–early November 2026** (estimates range Oct 29 – Nov 3, 2026; exact date not yet confirmed by the company). This matches the framework's standing "next earnings ~early November 2026" review trigger — no update needed to that trigger date, and no fresher post-Q2 fundamental event exists to incorporate.

---

## 4. Inputs Collected (this session — real quarterly data, not approximated)

| Item | Value | Basis |
|---|---|---|
| Shares outstanding | 2,042.560M | yfinance `sharesOutstanding` |
| **Market Cap** | 2,042.560M × $72.19 = **$147,452.4M** | Computed |
| Total debt (Q2'26, discrete) | $14,731.0M | yfinance `quarterly_balance_sheet` |
| Cash (Q2'26, discrete) | $5,391.0M | yfinance `quarterly_balance_sheet` |
| **Net Debt** | $14,731.0M − $5,391.0M = **$9,340.0M** | Computed — single clean figure, ambiguity resolved (§2) |
| **EV** | $147,452.4M + $9,340.0M = **$156,792.4M** | Computed |
| Revenue (TTM, real quarterly sum) | Q3'25 $13,467M + Q4'25 $14,366M + Q1'26 $13,203M + Q2'26 $14,191M = **$55,227M** | yfinance `quarterly_financials` — matches yfinance's own cached TTM revenue field exactly |
| **Operating Income / EBIT (TTM, real sum)** | $1,113M + $1,774M + $1,923M + $1,890M = **$6,700M** | Computed — real reported quarters, not margin-approximated |
| EBIT (FY2025, annual, sensitivity basis) | $6,240M | Annual income statement (unchanged from 08-07) |
| **GAAP Net Income (TTM, real sum)** | $6,626M + $296M + $263M + $2,394M = **$9,579M** | Computed |
| **Normalized Net Income (TTM)** | $9,579M − $4,900M (Q3'25 tax release) − $1,500M (Q3'25 equity gain) + $1,494M (Q1'26 equity loss) = **$4,673M** | Same company-disclosed one-off dollar figures as every prior UBER session, still inside the current TTM window (Q3'25–Q2'26) |
| **FCF (TTM, real quarterly sum)** | $2,230M + $2,808M + $2,286M + $2,792M = **$10,116M** | Computed — resolves 08-07 flag #4 (§2) |
| FCF (FY2025, annual, sensitivity basis) | $9,763M | Annual cash flow statement (unchanged) |
| **EBITDA (TTM, real quarterly sum)** | $2,927M + $599M + $795M + $3,599M = **$7,920M** | Computed |
| **Gross Profit (TTM, real sum)** | $5,358M + $5,685M + $5,945M + $6,376M = **$23,364M** → **Gross margin 42.31%** | Computed — replaces stale-cached 40.75% |
| **Total Equity (Q2'26, discrete)** | **$27,316M** | yfinance `quarterly_balance_sheet` `Stockholders Equity` — direct figure, replaces the 08-07 book-value/share estimate ($24.825B) |
| **Invested Capital** | $14,731M + $27,316M = **$42,047M** | Computed |
| Revenue FY2022 → FY2025 | $31,877M → $52,017M | Unchanged annual figures |
| **Revenue 3yr CAGR** | (52,017/31,877)^(1/3) − 1 = **17.73%** | Computed — unaffected by Q2 2026 quarterly data (annual-basis metric) |
| Forward EPS (consensus) | $4.40568 | yfinance `forwardEps` |
| **Forward PE (recomputed on live price)** | $72.19 ÷ $4.40568 = **16.39×** | Computed |
| **Net buyback yield (FY2025 vs. FY2024 shares)** | (2,067.905M − 2,107.953M) / 2,107.953M = **+1.90%/yr** | Computed fresh this session (§2 flag 3), supersedes 08-07's carried-forward +2.5% |
| Diluted EPS, last 5 quarters | $0.63 / $3.11 / $0.14 / $0.13 / **$1.17** | Confirms PEG non-eligibility (§2 flag 6) |

---

## 5. UBER — Quality Score

### Hard disqualifier check (fiscal-year rolling window, per the [2026-08-05 rolling-window clarification](../framework/quality-scoring.md))

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years unexplained? | FY2023 178.2% / FY2024 69.96% / FY2025 97.12% — only **one** year dips (barely) below 70%, not consecutive. TTM (real-quarter) basis is 105.6% — strong, confirms no deterioration. | disqualify if 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | 1.179× (real quarterly TTM EBITDA) | disqualify if >2.5× | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FY2023/2024/2025 all positive; TTM real-quarter sum also strongly positive | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight) — normalized, per Rule 6

```
Normalized Net Margin (TTM) = $4,673M / $55,227M = 8.461%
NetMargin_Component         = clamp((8.461/30)×100, 0, 100)  = 28.20

Normalized effective tax rate = 23.42% (carried forward from 07-05's SEC-sourced computation — §2 flag 2;
   Q2'26's own reported 26.0% quarterly rate is broadly consistent, lending some support)
NOPAT = EBIT(TTM, real sum, $6,700M) × (1 − 0.2342) = $5,130.9M
Invested Capital = Total Debt (Q2'26, $14,731M) + Total Equity (Q2'26, real, $27,316M) = $42,047M
ROIC (TTM, normalized) = $5,130.9M / $42,047M = 12.20%
ROIC_Component = clamp((12.20/30)×100, 0, 100) = 40.68

Profitability_Score = (28.20 + 40.68) / 2 = 34.44
```
No FCF-positive cap applies (3+ consecutive years positive, confirmed above).

**Note:** this is lower than 08-07's 37.85, purely because real Q2'26 data resolved two approximations in opposite directions — TTM operating margin computed from actual quarters (12.13%) is lower than the stale cached margin (13.32%) used 08-07, and Invested Capital now uses the real, higher Q2'26 equity figure ($27.316B vs. the $24.825B book-value/share estimate) — both changes make this a *more accurate*, not more pessimistic, number.

### Margins (15% weight)

```
GrossMargin_Score = clamp((42.31/80)×100, 0, 100) = 52.88
```
TTM margin (42.31%, real quarterly sum — up from the stale 40.75% cached figure) sits above the 40% bonus threshold, so the structural-trend bonus doesn't apply regardless of trend direction. No bonus.

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $31,877M → FY2025 $52,017M) = 17.73%
Growth_Score = clamp((17.73/25)×100, 0, 100) = 70.92
```
**+10 (refreshed evidence, §2 flag 4):** UBER's actual Q2 2026 earnings release (Aug 5, 2026) — Gross Bookings +24% YoY to $58.0B (4th consecutive quarter >20% growth), MAPC +16% YoY to 208M, Trips +18% YoY to 3.9B. Clear, current, company-disclosed TAM-expansion evidence — no deceleration signal.
```
Growth_Score (with bonus) = clamp(70.92 + 10, 0, 100) = 80.92
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA = $9,340M / $7,920M (real quarterly-sum TTM EBITDA) = 1.179×
BalanceSheet_Score = clamp(100×(1 − 1.179/4), 0, 100) = 70.52
```
Standard /4 denominator (no asset-light override — UBER is a marketplace, not a payment network/exchange). No longer needs a net-debt sensitivity range — the reconciliation problem is resolved (§2).

### Moat Signal (15% weight) — carried forward unchanged (no fresher independent evidence this session)

| Signal | Marked | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** (dated, flagged) | Bloomberg Second Measure: ~76% of observed US rideshare spend, March 2024 — still the most recent independent figure found (§2 flag 5). |
| Brand premium | FALSE | No cited pricing-power-specific evidence. |
| Network effect | **TRUE** | Uber's own FY2025 10-K: "Our massive, efficient, and intelligent network... becomes smarter with every trip." |
| Switching costs | FALSE | Uber's own 10-K discloses driver multi-homing is unrestricted. |
| Scale cost advantage | FALSE | No cost-per-trip data found vs. smaller competitors. |

```
Moat_Score = (2/5) × 100 = 40.0
```

### FCF Quality (10% weight)

```
FCF/NI (TTM, real quarterly sum) = $10,116M / $9,579M = 105.61%
FCFQuality_Score = clamp(((1.0561 − 0.40)/0.60)×100, 0, 100) = clamp(109.35, 0, 100) = 100.0
```
**This resolves 08-07's flagged FCF-quality concern directly.** The 08-07 session's primary figure (59.27, TTM Yahoo-aggregate basis) implied a real cash-conversion softening; this session's real-quarterly-sum basis shows TTM FCF conversion is actually **stronger** than the FY2025 annual figure (97.12%), confirming the 08-07 dip was the flagged Yahoo aggregate/staleness artifact, not genuine deterioration.

### Quality Score — Final

```
Quality Score = (34.44×0.25) + (52.88×0.15) + (80.92×0.20) + (70.52×0.15) + (40.0×0.15) + (100.0×0.10)
              = 8.610 + 7.932 + 16.184 + 10.578 + 6.000 + 10.000
              = 59.304 → rounds to 59.3
```

# Quality Score = 59.3 — FAILS the 80.0+ gate, decisively.

**Vs. prior session:** 59.3 vs. 55.5 (08-07) — a **meaningful improvement**, driven almost entirely by the FCF Quality sub-score jumping from 59.27 to 100.0 (a data-quality resolution, not a business change — see above) plus a modest Balance Sheet improvement, partially offset by a slightly lower (more accurate) Profitability score. Still **20.7 points short of the 80.0 gate** — not remotely a knife-edge case. This confirms the task brief's expectation ("likely still fails") while showing the gate-failure margin has narrowed somewhat as the data quality issues have cleared.

---

## 6. UBER — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 16.39 = 6.103%
Spread = EY − 10Y Treasury = 6.103% − 4.961% = +1.142pp
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (short by ~0.36pp) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.961% → "3.5–5%" bracket (close to the top — a move above 5% would trip the +10 bracket) → **+5**

**Total Rate Modifier = +10**

---

## 7. UBER — Phase 02 Valuation Score

**Ambiguity resolved this session (§2, §3):** the primary basis is now the **real TTM sum of four actually-reported discrete quarters** (Q3'25 + Q4'25 + Q1'26 + Q2'26) — no longer an approximation. FY2025-annual basis is retained as a sensitivity check for continuity with prior sessions, not because a genuine ambiguity remains.

**FCF Yield — 40% weight**
```
FCF Yield (primary, TTM real sum) = $10,116M / $147,452.4M = 6.861%
FCF_Score (primary) = clamp(100 × (1 − 6.861/10), 0, 100) = 31.39

FCF Yield (sensitivity, FY2025 annual) = $9,763M / $147,452.4M = 6.621%
FCF_Score (sensitivity) = clamp(100 × (1 − 6.621/10), 0, 100) = 33.79
```
→ Contribution (primary): 31.39 × 0.40 = **12.56**

**EV/EBIT — 25% + 15% (PEG redistributed) = 40% weight**
```
EV/EBIT (primary, TTM real EBIT) = $156,792.4M / $6,700M = 23.40×
EV/EBIT_Score (primary) = clamp((23.40 − 12)/23 × 100, 0, 100) = 49.57

EV/EBIT (sensitivity, FY2025 annual EBIT) = $156,792.4M / $6,240M = 25.13×
EV/EBIT_Score (sensitivity) = clamp((25.13 − 12)/23 × 100, 0, 100) = 57.07
```
→ Contribution (primary): 49.57 × 0.40 = **19.83**

**Forward PE — no-history fallback — 20% weight**
```
FwdPE_Score = 50.0 (neutral midpoint, flagged — same no-history rationale as every prior UBER session, §2 flag 7)
```
→ Contribution: 50.0 × 0.20 = **10.0**

**PEG — 15%: still N/A** (§2 flag 6) — redistributed to EV/EBIT above.

**Raw weighted score (primary, TTM real):**
```
= 12.56 + 19.83 + 10.0 = 42.39
```
**+ Rate Modifier (+10) = 52.39** (before the Upside/Downside Modifier)

**Raw weighted score (FY2025-annual sensitivity):**
```
= 13.52 + 22.83 + 10.0 = 46.35  → + Rate Modifier (+10) = 56.35
```

---

## 8. UBER — Upside/Downside Modifier (Expected-Return Modifier)

GAAP EPS is still too distorted (§2 flag 6) for an EPS×PE scenario set — continuing the P/FCF scenario architecture established 2026-07-05, now built on the real TTM FCF figure.

**Primary (TTM real-sum FCF anchor, $10,116M):**

| Scenario | Weight | Projected FCF | Growth assumption | FCF/share | Exit P/FCF | Fair Value |
|---|---|---|---|---|---|---|
| Bull | 25% | $11,936.9M | +18%/yr (historical FCF-growth pace) | $5.845 | 24× | **$140.26** |
| Base | 50% | $11,127.6M | +10%/yr (conservative vs. 17.7% revenue CAGR) | $5.449 | 18× | **$98.06** |
| Bear | 25% | $10,116.0M | 0% — current TTM run-rate persists | $4.953 | 12× | **$59.43** |

```
PW Fair Value = 0.25×140.26 + 0.50×98.06 + 0.25×59.43 = $98.95
```
Sits below the $101.21 analyst consensus mean PT (Guardrail 2 — scenario-weighted, not the rosy point).

```
Gap Upside %     = ($98.95 ÷ $72.19) − 1 = +37.07%
Catalyst window  = 2 years (Rule 10 default — Uber One scale-up, AV-partner monetization, ongoing
   margin-expansion path; no single dated event narrower than this)
Annualized gap   = 37.07% ÷ 2 = +18.54pp
Intrinsic growth = +12.0%/yr  (carried forward, conservative vs. 17.73% revenue CAGR)
Shareholder yield = +1.90%/yr  (recomputed fresh this session, §2 flag 3, §4 — supersedes 08-07's carried-forward +2.5%)

E = 18.54 + 12.0 + 1.90 = +32.44%/yr
```
```
E ≥ H(10%) → M = −15 × clamp((32.44 − 10)/15, 0, 1) = −15 × clamp(1.496, 0, 1) = −15.0 (floored)
```

**Sensitivity (FY2025-annual FCF anchor, $9,763M, same growth-rate assumptions applied for comparability):**

| Scenario | Projected FCF | FCF/share | Exit P/FCF | Fair Value |
|---|---|---|---|---|
| Bull (+18%) | $11,520.3M | $5.640 | 24× | $135.36 |
| Base (+10%) | $10,739.3M | $5.258 | 18× | $94.64 |
| Bear (0%) | $9,763.0M | $4.780 | 12× | $57.36 |

```
PW Fair Value (sensitivity) = 0.25×135.36 + 0.50×94.64 + 0.25×57.36 = $95.50
Gap Upside % = ($95.50 ÷ $72.19) − 1 = +32.30%
Annualized gap = 32.30% ÷ 2 = +16.15pp
E (sensitivity) = 16.15 + 12.0 + 1.90 = +30.05%
M (sensitivity) = −15 × clamp((30.05 − 10)/15, 0, 1) = −15 × 1.34→clamp(1,0,1) = −15.0 (floored)
```

**Guardrail checks (primary):** (1) documented catalyst within 18–24mo → upside credit allowed; (2) scenario-weighted PW FV below analyst consensus mean ✓; (3) full calc shown ✓; (4) bounded ±15, floor reached ✓.

**Notable:** both bases now floor the Upside/Downside Modifier at −15.0 — the basis choice no longer changes this modifier's output, another sign the ambiguity's practical consequences have narrowed alongside its data-quality resolution.

---

## 9. UBER — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE (primary, TTM real basis) = Raw weighted (42.39) + Rate Modifier (+10) + Upside/Downside (−15.0)
                                                  = 37.39 → 37.4
```

| | Primary (TTM real) | FY2025-annual sensitivity |
|---|---|---|
| Raw weighted | 42.39 | 46.35 |
| Rate Gate | +10 | +10 |
| Upside/Downside Modifier | −15.0 | −15.0 |
| **FINAL VALUATION SCORE** | **37.4** | **41.3** |
| Prior valuation score (08-07) | 43.6 (primary) / 56.4 (TTM sensitivity) | — |
| **Quality Score** | **59.3** (FAILS 80.0+ gate) | — |

**Ambiguity resolution, front and center:** unlike 08-07 (where the primary and TTM-sensitivity bases landed in *different* action bands — 43.6 "Cheap" vs. 56.4 "Fair Value/Hold"), this session's **primary and sensitivity bases now land in the same band** — both 37.4 and 41.3 fall in **30.0–49.9 ("Cheap")**. The data-quality resolution described in §2 (real Q2 2026 quarterly financials replacing TTM-aggregate approximations) has closed the gap that was flagged as a priority follow-up item on 08-07. This does not change the action recommendation (still driven by the Quality Score gate failure, §10) but it does remove a genuine, previously load-bearing source of uncertainty.

**Composite Score — reference only, per established practice for a Quality-Score-gate failure on an existing holding:**
```
Composite Score (primary) = 0.50×(100 − 59.3) + 0.50×37.4 = 0.50×40.7 + 0.50×37.4
                           = 20.35 + 18.70 = 39.05 → boundary rule (.X5 exact) rounds UP → 39.1

Composite Score (FY2025-annual sensitivity) = 0.50×(100 − 59.3) + 0.50×41.3 = 20.35 + 20.65 = 41.0
```
**Composite Score = 39.1** (primary) **/ 41.0** (sensitivity) — vs. 44.1 on 08-07. **Not adopted to drive the action recommendation** — shown for the record only, per "no black box."

---

## 10. UBER — Action Recommendation

**Two independent facts, either one alone is enough to conclude HOLD/no-add — same structure as every UBER session since 2026-07-05:**

1. **Quality Score (59.3) fails the 80.0+ gate decisively** (§5) — 20.7 points short. Improved from 08-07's 55.5, but purely on data-quality resolution (real Q2 2026 quarters replacing stale/approximated figures), not on any underlying business change. Still robustly a FAIL, not a knife-edge case. The same **value-trap flag** first raised 2026-07-05 stands: a Valuation Score that reads attractive (37.4–41.3, "Cheap") sitting on top of a business that hasn't cleared this framework's quality bar.
2. **Order-setup R/R check, for completeness (reference only, since action is driven by the gate failure regardless):**

```
Blended Fair Value (= primary PW FV):        $98.95
Margin of Safety (30.0–49.9 band):           28%  (same convention as every prior UBER session)
BUY PRICE (limit):                           $98.95 × (1 − 0.28) = $71.24
PRIMARY SELL TARGET:                         $98.95
BULL-CASE TRIM TARGET (bull × 0.90):         $140.26 × 0.90 = $126.23
STOP LOSS (Buy × (1 − 28%)):                 $71.24 × 0.72 = $51.29
R/R at formal entry = (98.95 − 71.24) ÷ (71.24 − 51.29) = 27.71 ÷ 19.95 = 1.389:1  ❌ below 2:1
R/R at live price   = (98.95 − 72.19) ÷ (72.19 − 51.29) = 26.76 ÷ 20.90 = 1.280:1  ❌ below 2:1
   (worse than the buy-price R/R since live price sits above the theoretical entry, but somewhat
   better than 08-07's 0.636:1 — the live price has pulled back ~3.3% while fair value rose)
```

**Net: HOLD the existing 0.35% position. No fresh capital added — doubly blocked, unchanged from every UBER session since 07-05: an independent R/R failure and the Quality Score's decisive gate failure.**

**Position cap check:** 0.35% is nowhere near the 15% hard cap (Upgrade 7) — not binding, included for completeness. No BUY or TRIM action taken; **no order placed, modified, or submitted** — recommendation only, per this run's explicit scope.

**Open item, carried forward unchanged:** the 07-05 session recommended the user consider logging a **Human Override** entry (mirroring the ZS/NOW precedent for a held, quality-gate-failing position) — checked `override-log.md` this session, still not logged. Still flagged, not decided or written by this RESCORE (out of its scope).

---

## 11. Next Review Trigger

- **Routine:** UBER Q3 2026 earnings, confirmed **not yet reported** as of this session (§3) — expected late October–early November 2026 (window: Oct 29 – Nov 3, 2026; exact date unconfirmed by the company).
- **Resolved this session:** the primary-vs-TTM-basis Valuation Score ambiguity flagged 08-07 — no longer an open item (§9).
- **Open data item, carried forward:** the March 2024 US rideshare market-share citation is still stale (§2 flag 5) — check again for a fresher independent source at the next rescore.
- **Open item, carried forward:** the value-trap / Quality Watch flag and the still-undecided Human Override question (§10).
- **Watch:** the 10Y Treasury yield is close to the top of the 3.5–5% Rate Regime bracket (4.961%, intraday high 5.012% this week) — a sustained move above 5% would trip the Rate Regime Modifier to +10, adding further upward pressure to the Valuation Score.
- **Rule 9 triggers (standing):** guidance revision, M&A/material AV investment, management change, a >15% unexplained price move, or the Q3 2026 earnings print itself.

---

## 12. Housekeeping

- Quality Score under the current (2026-06-29) methodology — no stale-score banner existed for UBER's [2026-08-07 watchlist entry](../watchlist/in-portfolio/UBER/UBER-2026-08-07.md) (no version bump since then) and none exists in [watchlist/STALE.md](../watchlist/STALE.md) — confirmed nothing to clear.
- New dated watchlist entry created: [watchlist/in-portfolio/UBER/UBER-2026-09-15.md](../watchlist/in-portfolio/UBER/UBER-2026-09-15.md) — warranted per watchlist/README.md's "significant change" test (both the Valuation Score and Quality Score changed materially, and the primary-vs-TTM ambiguity — a standing open item on the prior entry — was resolved).
- [holdings.md](../portfolio/holdings.md) UBER row: **not updated by this session** — per this task's explicit instructions, a separate orchestrator process updates `holdings.md` after both the AVGO and UBER rescores complete, to avoid concurrent-edit conflicts. Values to carry forward: Last Score 37.4, Quality Score 59.3, Composite Score 39.1, Last Review 15 Sep 2026.
- **No commit, push, or PR opened by this session** — per this task's explicit instructions, a separate orchestrator process handles that.

---

## Glossary

| Term | Meaning |
|---|---|
| **AV (Autonomous Vehicle)** | A self-driving vehicle; "robotaxi" is an AV run as an on-demand ride-hailing service. Uber partners with (rather than builds) AV developers to deploy AVs on its platform. |
| **CAGR** | Compound Annual Growth Rate. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate; shown as reference-only, not-adopted for UBER this session (59.3 Quality Score still fails the gate). |
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
| **Net buyback yield** | The rate at which a company's share count is shrinking due to buybacks exceeding new issuance/dilution — a component of shareholder yield. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the numerator of ROIC. |
| **P/FCF (Price-to-Free-Cash-Flow)** | Market capitalization ÷ Free Cash Flow — an earnings-multiple analog used in UBER's scenario architecture since GAAP EPS is too distorted for a reliable EPS×PE set. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. UBER: 59.3, fails the gate. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive adjustment for the current Treasury-yield band. |
| **ROA (Return on Assets)** | Net Income ÷ Total Assets — how efficiently a company generates profit from its full asset base; a cross-check reference, not a scored framework input. |
| **ROE** | Return on Equity — Net Income ÷ shareholder equity. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; normalize before valuing / require a minimum 2:1 risk/reward; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs. the 10% hurdle. |
| **Value trap** | A stock that looks statistically cheap but stays cheap because underlying business quality is deteriorating or was never strong enough to support a re-rating — the risk UBER's Quality Score gate failure continues to flag. |

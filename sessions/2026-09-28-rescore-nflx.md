# RESCORE — NFLX (Netflix, Inc.) — 2026-09-28

**Task type:** RESCORE (single ticker — existing holding), mode `--both`
**Trigger:** Routine quarterly monitoring pass, prompted specifically by a **Rule 9 macro-shift trigger**: the Federal Reserve hiked its overnight rate 25bps on 16 Sep 2026 (first hike in three years, citing stubborn inflation), and the 10-Year Treasury yield has since surged to its highest level since 2007. This is a "macro shift (central bank policy...)" Rule 9 trigger independent of any NFLX-specific news — Netflix itself has **not** reported new earnings since the 17 Jul 2026 rescore (Q3 2026 results are not due until 20 Oct 2026), so no new company-specific fundamental data exists this session. Per operating-calendar.md's Rule 9 table: "Macro shift (central bank policy, commodity shock) → Update Rate Environment Gate + re-score."
**Date:** 28 Sep 2026
**10Y US Treasury Yield used:** 5.21% (28 Sep 2026 print, TradingEconomics-aggregated — a near-20-year high; up sharply from the 17 Jul session's 4.54%, driven by the Fed's 16 Sep hike and stubborn-inflation/fiscal-conditions commentary)
**Rate Regime Modifier (Step 2):** **+10** (10Y crossed from the 3.5–5% bracket into the **>5% bracket** — a genuine bracket shift, not just a within-bracket drift)
**Current NFLX portfolio weight:** 1.42% (per [holdings.md](../portfolio/holdings.md)) — Last Score 49.3, Quality Score 69.8 (fails 80.0+ gate), Composite Score 39.8 (⚠️ flagged in the 17 Jul session as a false-green-light artifact), Last Review 17 Jul 2026
**Sector:** Communication Services — Streaming Media & Entertainment

*First-use jargon decoded in the closing Glossary (step 9 of the operating brief).*

---

## 0. Fundamental-Trigger Check Since Last Review (Rule 9)

**No new NFLX-specific fundamental event since the 17 Jul 2026 rescore.** Q3 2026 earnings are scheduled for **20 Oct 2026** (confirmed via Netflix's own investor-relations announcement, cross-checked against TipRanks/StockTitan) — not yet reported. No guidance revision, management change, M&A, or >15% unexplained price move has occurred in the interim (the ticker's own price move since 17 Jul, −$67.80 → −$69.22 ≈ +2.1%, well under the 15% threshold and not itself a Rule 9 trigger).

**What *did* trigger this session is a genuine macro-shift Rule 9 event**, common to the whole portfolio, not NFLX-specific:
- The Fed raised its overnight lending rate 25bps (to 3.75%–4.00%) on 16 Sep 2026, its first hike in three years, in a unanimous 12–0 vote — citing persistent inflation risk.
- The 10-Year Treasury yield has climbed to **5.21%** as of 28 Sep 2026 (touching as high as ~5.25% intraday per some prints) — its highest level since 2007, driven by the hike itself plus elevated oil prices, resilient economic data, and mounting fiscal-deficit concerns.
- This crosses the Rate Environment Gate's Step 2 bracket boundary (3.5–5% → >5%), which is a mechanical, mandatory re-score trigger for every position under the Rate Environment Gate, and also (per Rule 2's DCF standard, "discount rate must reflect current risk-free rate") pushes up every scenario's WACC in the fair-value rebuild below.

Because there is no new NFLX-specific quarterly data, **all fundamentals-derived Quality Score inputs are carried forward unchanged from the 17 Jul 2026 session** (same TTM window, Q3 2025–Q2 2026 — Netflix has not yet reported a new quarter). Only price-dependent Valuation Score inputs (live price, market cap, EV, Forward PE, Rate Gate, DCF discount rate) are refreshed for today.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$69.22** | IBKR `get_price_snapshot` (contract_id 15124833) — `last` = $69.22 (ts 2026-09-28, not halted) and `plprice` (mark) = $69.23 agree to the cent. |
| Change vs prior close | −$1.92 / −2.70% | IBKR `change` field |
| 52-week range | $65.08 (low) – $124.86 (high) | IBKR `misc_statistics` |
| Analyst consensus PT | ~$92.93–$93 (mean/median, 51 analysts, "Buy") — forecast range $57–$135 | WebSearch aggregation (S&P Global / stockanalysis.com) — shown for context only, never used directly in the score (Rule 7/10 — the scenario-weighted PW FV below is the input that matters). |
| `yfinance` availability | **Reachable this session** (unlike several recent sessions' `curl_cffi` TLS failures) — `python -m scripts.fetch_fundamentals NFLX` ran successfully; see §2. |

**Cross-check:** WebSearch aggregators returned somewhat noisy/conflicting intraday snapshots ($70.20 from one aggregator, $69.24 from another, with an internally inconsistent day-range) — a known limitation of AI-summarized search results. Per Rule 0, the **IBKR live snapshot is used as the price of record** ($69.22), not the WebSearch aggregation, precisely because of this kind of cross-source noise.

**Context:** NFLX at $69.22 sits ~44.6% below its 52-week high ($124.86) and ~6.4% above its 52-week low ($65.08) — a modest recovery from the fresh 52-week low set around the 17 Jul session ($67.80), but still deep in the post-Q2-earnings-selloff range. This is a small, unremarkable price move on its own (+2.1% over ~10 weeks) — not itself a Rule 9 trigger.

---

## 2. Data Gathered — Sources & Gaps

### 2.1 — Quality Score inputs: carried forward unchanged (no new quarter)

Netflix has not filed a new 10-Q/8-K with fresher quarterly data since the 17 Jul 2026 session (Q3 2026 reports 20 Oct 2026). Per the framework's own "never invent or estimate" rule, this session does **not** re-derive TTM fundamentals from scratch — it explicitly carries forward the SEC-EDGAR-sourced, WBD-fee-normalized figures established in the 17 Jul session (same fiscal-quarter window: Q3 2025–Q2 2026):

| Metric | Value (carried forward from 17 Jul 2026) |
|---|---|
| Net Margin (TTM, normalized) | 23.548% |
| ROIC (TTM, NOPAT/Invested Capital) | 35.07% |
| Gross Margin (TTM) | 49.12% |
| Revenue 3yr CAGR (FY2022→FY2025) | 12.51% |
| Net Debt/EBITDA | 0.352× (Net Debt $5,181.396M / EBITDA $14,726.931M) |
| FCF/NI (TTM, normalized) | 73.33% |
| FCF/NI annual (oldest first, 4 FY) | 36.0% / 128.1% / 79.5% / 86.2% — all ≥70% except the oldest year, not 2 consecutive |
| FCF-positive 3+ consecutive years | True |
| TTM EBIT | $14,354.517M |
| TTM Revenue | $48,370.764M |
| FCF (TTM, normalized) | $8,352.005M |

**Cross-check against a fresh `python -m scripts.fetch_fundamentals NFLX` pull this session** (yfinance-sourced, as-reported basis, no WBD-fee normalization):

```
Market Cap            = 288,269,565,952
Enterprise Value      = 303,770,238,976
Shares Outstanding    = 4,163,939,676
Forward PE            = 18.155
FCF Yield %           = 3.869
EV/EBIT               = 17.518
Net Margin %          = 28.219
Gross Margin %        = 49.118
ROIC % (NOPAT/InvCap) = 34.936
Revenue 3yr CAGR %    = 12.640
Net Debt/EBITDA       = 0.369
FCF/NI TTM %          = 81.702
FCF/NI annual (oldest first) = [36.0%, 128.1%, 79.5%, 86.2%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 37.874 / 19.325 / 55.816  (n=20 quarters)
```

This as-reported pull (Net Margin 28.22%, FCF/NI TTM 81.70%, Net Debt/EBITDA 0.369×) **closely matches the 17 Jul session's own as-reported figures** (28.22%, 81.70%) — confirming the underlying TTM window genuinely hasn't changed; the small Net Debt/EBITDA difference (0.369 vs 0.352) and CAGR difference (12.64% vs 12.51%) are minor cross-source noise between this script's own EBITDA/CAGR derivation and the SEC-EDGAR reconstruction, not a real fundamental change. Gross margin (49.12% vs 49.118%) matches almost exactly. **The normalized (WBD-fee-adjusted) figures carried forward above remain this session's primary basis, consistent with the 05 Jul/17 Jul convention (Rule 6).**

**New, freshly-computed input this session (yfinance reachable, unlike prior sessions):** the **5yr trailing PE range — avg 37.874×, low 19.325×, high 55.816×** (n=20 quarters) is a genuine fresh pull (vs. the 17 Jul session's stale carried-forward 39.44/19.32/55.82, itself carried forward from 20 Jun 2026 because yfinance was unreachable in both the 05 Jul and 17 Jul sessions). This is used as the current, more accurate figure below.

### 2.2 — Valuation Score inputs: refreshed for today

| Field | Value | Source |
|---|---|---|
| **Shares outstanding (current)** | 4,163,939,676 (~4,163.94M) | `fetch_fundamentals` (yfinance `sharesOutstanding`) — **lower** than the 17 Jul session's SEC 10-Q-sourced 4,261.3M (as of 30 Jun 2026 quarter-end), consistent with continued Q3 buybacks (Netflix disclosed $27.1B of authorization remaining as of 30 Jun 2026, per its Q2 2026 10-Q). ⚠️ **Flagged data gap:** this yfinance figure is a live snapshot, not a fresh SEC filing — Netflix has not yet disclosed the exact Q3 share-repurchase dollar amount or its resulting exact share count (that comes with the Q3 10-Q). Used here as the best available current figure per Rule 0's spirit (fresher beats stale), not invented. |
| **FY2026 consensus EPS** | $3.59 | stockanalysis.com (46 analysts) — essentially unchanged from the 17 Jul session's post-Q2 $3.57 figure; used as the Forward PE denominator. |
| **Net debt** | $5,181.396M (carried forward, as of 30 Jun 2026 — no fresher 10-Q balance sheet exists yet) | SEC EDGAR/8-K, carried forward from 17 Jul session. ⚠️ Flagged: Q3 buyback activity since 30 Jun likely changed this, but the dollar amount isn't disclosed yet — not invented. |
| **10Y Treasury yield** | 5.21% | WebSearch (TradingEconomics/CNBC aggregation of 28 Sep 2026 prints, cross-checked against the Fed-hike/yield-surge news cycle of 15–28 Sep 2026) |
| **Dividend yield** | 0% (Netflix pays no dividend) | Carried forward — unchanged fact. |
| **Net buyback yield** | +4.1%/yr | Carried forward from 17 Jul session (Netflix's own disclosed H1 2026 net buybacks, $5,875.701M, annualized ÷ market cap). ⚠️ Flagged: no fresher (Q3) buyback-dollar disclosure exists yet to update this; carried forward as the most recent actual, not invented. |
| **Intrinsic growth rate** | +11.0%/yr | Carried forward from 17 Jul session (revised down from the stale +13.0%/yr to reflect the confirmed multi-quarter deceleration) — no new data this session to move it further. |
| **Qualitative — ad-tier growth** (Growth/TAM sub-score context) | Ad-tier reach now ~250M global monthly active viewers, up from 190M (Nov 2025) | WebSearch (Variety, "Netflix Claims Ad Tier Now Reaches 250 Million Viewers Worldwide") — used as fresh supporting evidence for the existing +10 TAM/pricing-power Growth modifier (already carried at +10 from 17 Jul; this is corroborating, not new-direction, evidence). |

**Data gaps explicitly flagged (not invented):** (1) Netflix's exact current share count and Q3 buyback dollar figure — not yet disclosed (10-Q due with Q3 earnings, 20 Oct 2026); (2) net debt as of today — carried forward from 30 Jun 2026, likely stale but no fresher figure exists; (3) Q3 2026 revenue-growth actual (11.7% guided) — not yet reported, so the "does the deceleration stabilize or continue" question from the 17 Jul session remains open until 20 Oct 2026.

---

## 3. Quality Score

**Hard disqualifier check (unchanged from 17 Jul — same TTM window):**

| Check | NFLX Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | TTM 73.3% (normalized); annual (oldest first) 36.0% / 128.1% / 79.5% / 86.2% — only the oldest year is <70%, not 2 consecutive | disqualify if <70% for 2+ consecutive yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | 0.352× | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2023/24/25 and TTM all positive | disqualify if not | ✅ PASS |

No hard disqualifier fires. Full script output below (`python -m scripts.scoring.quality_score --input <inputs.json>`), pasted verbatim:

```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((23.548/30)x100) = 78.49
ROIC_Component = clamp((35.07/30)x100) = 100.00
Profitability_Score = (78.49 + 100.00) / 2 = 89.25

**Margins (15%)**
GrossMargin_Score = clamp((49.12/80)x100) = 61.40

**Growth (20%)**
Growth_Score = clamp((12.51/25)x100) = 50.04
+10 TAM/pricing-power evidence: FY2026 ad revenue guided ~$3.0B (roughly doubling YoY,
  unchanged target, reaffirmed 16 Jul 2026 letter); ad-tier reach now ~250M global monthly
  active viewers as of a Sept 2026 company disclosure, up from 190M (Nov 2025) and 94M
  (May 2025) (Variety); ad tier expanding to 15 more countries with advanced targeting
  launching in 2026. Double-digit revenue growth continued in every region in Q2 2026
  (UCAN +10%, EMEA +14%, LATAM +21%, APAC +16%) and Netflix's own Q2 2026 letter states
  "the results of our recent price changes are consistent with prior changes and our
  expectations" (continued pricing power, no disclosed volume loss).
-10 structural growth deceleration evidence: Netflix's own guidance table shows YoY
  revenue growth decelerating for four consecutive prints: Q4 2025 17.6% -> Q1 2026 16.2%
  -> Q2 2026 13.4% (actual) -> Q3 2026 11.7% (guided). No fresher (Q3 actual) data
  available this session -- Q3 2026 earnings not yet reported (20 Oct 2026) -- carries
  forward unchanged pending that report. H1 2026 member-viewing-hours grew only +2% YoY
  (vs 1.5% in 2025) -- still structurally weak engagement growth.
Growth_Score (final, clamped) = 50.04

**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - 0.352/4)) = 91.20

**Moat Signal (15%)**
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Double-digit revenue growth in every operating region in Q2 2026; ~325M+ paid subscribers globally (carried forward). |
| brand_premium | True | Q2 2026 letter: pricing-power evidence, no disclosed volume/churn deterioration. |
| network_effect | False | No documented two-sided-marketplace mechanism for core streaming -- unchanged. |
| switching_costs | False | Month-to-month, cancel-anytime subscription -- unchanged. |
| scale_cost_advantage | True | Largest industry content-spend scale (~$20B 2026 content budget guided). |
Moat_Score = (3/5) x 100 = 60.00

**FCF Quality (10%)**
FCFQuality_Score = clamp(((0.7333 - 0.40)/0.60)x100) = 55.55

**Quality Score — Final**
Quality Score = (89.25x0.25) + (61.40x0.15) + (50.04x0.20) + (91.20x0.15) + (60.00x0.15) + (55.55x0.10)
= 69.765 -> rounds to 69.8

# Quality Score = 69.8 — FAILS the 80.0+ gate
```

**Quality Score = 69.8 — FAILS the 80.0+ gate — unchanged from the 17 Jul 2026 session.** This is expected and correct: no new NFLX-specific quarterly data exists this session (Q3 2026 not yet reported), so every Quality Score input is identical to 17 Jul, and the script reproduces the identical result. **Phase 04 Quality Watch flag stands, unchanged** — no new deterioration or improvement to report; watch for the Q3 2026 earnings release (20 Oct 2026) for the next real update to this score.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $69.22 / $3.59 = 19.28x
EY = 1 / 19.28 = 5.1867%
Spread = EY - 10Y Treasury = 5.1867% - 5.21% = -0.0233pp
```
Spread (−0.02%, effectively flat but on the fail side) < +1.5% → **FAILS** → **+5 additive** (yellow flag, not a veto).

**Step 2 — Rate Regime Modifier:** 10Y = 5.21% → **crosses into the >5% bracket** → **+10** (up from +5 at the 17 Jul session's 4.54%, which was in the 3.5–5% bracket)

**Total Rate Modifier: +15** — a genuine, mechanical +5 increase vs. 17 Jul, driven entirely by the 10Y crossing the 5% bracket boundary following the Fed's 16 Sep 2026 hike. This is the single largest driver of this session's score change.

---

## 5. Valuation Score (Phase 02)

**Market Cap** = 4,163,939,676 shares × $69.22 = **$288,227.90M**
**Net Debt** = $5,181.396M (carried forward, §2.2)
**EV** = $288,227.90M + $5,181.396M = **$293,409.30M**

**FCF Yield — 40% weight** (normalized TTM FCF, Rule 6, carried forward)
```
FCF Yield = $8,352.005M / $288,227.90M = 2.898%
FCF_Score = clamp(100x(1 - 2.898/10), 0, 100) = 71.02
```

**EV/EBIT — 40% weight (PEG redistributed — NFLX still isn't a Fast Grower)**
```
EV/EBIT = $293,409.30M / $14,354.517M = 20.443x
EV/EBIT_Score = clamp((20.443 - 12)/23 x 100, 0, 100) = 36.71
```

**Forward PE — 20% weight (5yr-range primary formula, freshly-computed range this session)**
```
Forward PE = 19.28x, 5yr Low = 19.325x, 5yr High = 55.816x (freshly pulled this session, §2.1)
FwdPE_Score (range) = clamp((19.28 - 19.325)/(55.816 - 19.325) x 100, 0, 100) = clamp(-0.12, 0, 100) = 0.0
Historical PE Modifier (Upgrade 2): Deviation vs 5yr avg (37.874x) = (19.28 - 37.874)/37.874 = -49.09%
  -> >20% below -> -10 modifier (moot -- already floored at 0.0)
FwdPE_Score = 0.0
```

**PEG — still not applicable.** NFLX fails the Fast-Grower test (established across every prior session). Weight redistributed to EV/EBIT (→ 40%).

**Full script output** (`python -m scripts.scoring.valuation_score --input <inputs.json>`), pasted verbatim:

```
## Valuation Score

**FCF Yield (40%)**
FCF_Score = clamp(100x(1 - 2.898/10)) = 71.020

**EV/EBIT**
EV/EBIT_Score = clamp((20.443 - 12)/23 x 100) = 36.709

**Forward PE**
FwdPE_Score (raw) = clamp((19.28 - 19.325)/(55.816 - 19.325) x 100) = 0.000
Deviation vs 5yr avg (37.874) = (19.28 - 37.874)/37.874 x 100 = -49.094%
Historical PE Modifier: >20% below 5yr avg -> -10
FwdPE_Score = clamp(0.000 + -10) = 0.000

**PEG**
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT

**Rate Environment Gate**
EY = 1/19.28 x 100 = 5.1867%
Spread = EY - 10Y (5.21%) = -0.0233pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.21% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15

**Upside/Downside Modifier**
PW Fair Value = 0.25x90.07 + 0.50x61.04 + 0.25x48.44 = 65.1475
Gap Upside % = (65.1475/69.22) - 1 = -5.8834%
Annualized gap = -5.8834% / 2yr = -2.9417%/yr
E = -2.9417 (annualized gap) + 11.0 (intrinsic growth) + 4.1000 (shareholder yield: 0 div + 4.1 buyback) = 12.1583%/yr
E (12.1583%) >= H (10.0%) -> M = -15 x clamp((12.1583-10.0)/15, 0, 1) = -2.1583
Upside/Downside Modifier (bounded [-15, +15]) = -2.1583

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 43.091

**Final Valuation Score**
Final Score = Raw (43.091) + Rate Modifier (+15) + Upside/Downside Modifier (-2.158)
= 55.933 -> rounds to 55.9

# Valuation Score = 55.9
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier) — Rebuilt for the higher discount rate

**Decision to rebuild:** No new NFLX-specific cash-flow data exists this session, so the DCF's cash-flow *growth* assumptions (Yr1 FCF anchors, Yrs2–5 growth, Yrs6–10 fade, terminal growth) are carried forward unchanged from the 17 Jul rebuild. But per Rule 2 ("Discount Rate (WACC): Must reflect current risk-free rate"), the ~+0.67pp jump in the 10Y Treasury (4.54% → 5.21%) mechanically raises every scenario's WACC, so the DCF **is** rebuilt for that one input, holding cash-flow assumptions fixed. Shares outstanding are updated to the current 4,163.94M (§2.2); net debt is carried forward (no fresher balance sheet).

### Step 1 — DCF (3 scenarios, Rule 2/7), rebuilt for WACC only

| Scenario | WACC (was 17 Jul) | Yr1 FCF | Yrs 2–5 growth | Yrs 6–10 fade | Terminal growth | PV Stage 1 | PV Stage 2 | PV Terminal | Total EV | Equity Value | **FV/share** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bear | 11.17% (was 10.5%) | $11.5B | 6%→4% | 4%→2% | 2.0% | $46.58B | $33.23B | $62.44B | $142.25B | $137.07B | **$32.92** |
| Base | 10.17% (was 9.5%) | $12.5B | 10%→7% | 6%→3.5% | 2.5% | $55.54B | $46.54B | $110.79B | $212.87B | $207.69B | **$49.88** |
| Bull | 9.17% (was 8.5%) | $13.0B | 13%→10% | 8%→5% | 3.0% | $62.70B | $61.07B | $191.16B | $314.93B | $309.75B | **$74.39** |

WACC adjustment: +0.67pp uniformly across all three scenarios, equal to the 10Y Treasury's rise (4.54%→5.21%), holding beta/ERP and every cash-flow growth assumption fixed — an isolated, single-variable, fully-explained update, not a re-derivation of the underlying business model. Cross-checked: re-running the identical cash-flow paths at the prior 17 Jul WACCs exactly reproduces that session's PV figures to the dollar (verified during construction of this table), confirming the only change is the discount rate. Terminal value is 43.9–60.7% of total EV across scenarios — under the 75% Rule 4 trigger for extending Stage 2.

```
PW DCF FV = 0.25x74.39 + 0.50x49.88 + 0.25x32.92 = 18.5975 + 24.94 + 8.23 = $51.77
```
(down from 17 Jul's $56.20 — the higher discount rate alone accounts for the full difference, cash flows unchanged.)

### Step 2 — Comparable Multiples, refreshed for current shares/EPS

| Approach | "Fair" multiple | Calculation | FV/share |
|---|---|---|---|
| Forward PE comp | 28x (unchanged rationale) | 28 × $3.59 | **$100.52** |
| EV/EBIT comp | 18x on FY2026E EBIT ($51.2B × 31.5% = $16.128B, guidance unchanged) | EV $290.30B − net debt $5.181B → equity $285.12B ÷ 4.16394B shares | **$68.48** |
| FCF-yield comp | 5.0% yield on FY2026E FCF ($12.5B, guidance unchanged) | EV $250.0B − net debt $5.181B → equity $244.82B ÷ 4.16394B shares | **$58.79** |
| **Multiples avg** | | | **$75.93** |

**Per-scenario blend (same 40% DCF/60% comp pairing convention as prior sessions):**

| Scenario | DCF | Multiples comp | Blended (0.4×DCF + 0.6×comp) |
|---|---|---|---|
| Bear | $32.92 | $58.79 (FCF-yield comp) | **$48.44** |
| Base | $49.88 | $68.48 (EV/EBIT comp) | **$61.04** |
| Bull | $74.39 | $100.52 (Fwd-PE comp) | **$90.07** |

```
PW Fair Value = 0.25x$90.07 + 0.50x$61.04 + 0.25x$48.44 = $22.5175 + $30.52 + $12.11 = $65.15
```

**Cross-check (headline Blended FV, 40% DCF-PW + 60% Multiples-avg, Rule 3 style):**
```
Blended FV = 0.40x$51.77 + 0.60x$75.93 = $20.71 + $45.56 = $66.27
```
Within 4.3% of the live price ($69.22) — a reasonable sanity check that the market is still pricing NFLX close to where this rate-adjusted framework would put fair value.

### Step 3 — E and the Modifier

```
PW Fair Value = $65.15
Gap Upside % = ($65.15 / $69.22) - 1 = -5.88%
Catalyst window = 2 years (Rule 10, unchanged) -- Q3 2026 earnings (20 Oct 2026) is a near-term
  checkpoint on whether the deceleration stabilizes or continues, but no narrower fully-resolving
  window exists.
Annualized gap = -5.88% / 2 = -2.94%/yr

Intrinsic growth = +11.0%/yr (carried forward, unchanged -- no new data this session)
Shareholder yield = +4.1%/yr (carried forward, unchanged -- no fresher Q3 buyback disclosure exists)

E = -2.94 + 11.0 + 4.1 = +12.16%/yr
```

**Map E to M** (hurdle H = 10%, E ≥ H branch):
```
M = -15 x clamp((12.16 - 10)/15, 0, 1) = -15 x 0.144 = -2.16
```

**Upside/Downside Modifier M = −2.16** — a smaller pull-down than the 17 Jul session's −3.90, because the higher discount rate lowered PW Fair Value roughly in step with the live price, leaving the gap slightly narrower (−5.9% vs −2.4% gap at 17 Jul — note the gap direction and magnitude both moved; the smaller magnitude of the negative-gap component combined with unchanged growth/yield inputs nets to a smaller overall E and thus a smaller modifier).

**Guardrails:** documented catalyst + timeline exists within 18–24 months (Q3 2026 earnings, ongoing ad-ramp) — the guardrail doesn't bind here (this is a modest negative-M / E≥H case, not a large speculative-upside claim). Scenario-weighted PW FV used throughout, never the bull case or the consensus PT. Full calc shown above — no black box.

---

## 7. Final Valuation Score

```
Final Score = Raw (43.09) + Rate Modifier (+15.0) - Upside/Downside Modifier (2.16)
            = 55.93 -> rounds to 55.9
```

**Valuation Score = 55.9 — "Fair Value" band (50.0–69.9).** This is **one full band higher** than the 17 Jul session's 49.3 ("nominally Cheap," 30.0–49.9) — despite the price barely moving (+2.1%) and the Upside/Downside Modifier actually improving (less negative pull, −2.16 vs −3.90). **The entire band shift is driven by the Rate Regime Modifier's mechanical +5 bracket jump** (10Y crossing above 5%) plus a modestly higher EV/EBIT and slightly lower FCF Yield sub-score (both a function of the higher current market cap relative to the still-flat TTM fundamentals). This is a textbook example of why the Rate Environment Gate exists as a standing pre-check before every Phase 02 score — a pure macro (interest-rate) shift moved NFLX's standalone valuation band without any change to the company's own business.

---

## 8. Composite Score — **NOT COMPUTED (Quality Score fails the 80.0+ gate)**

```
$ python -m scripts.scoring.composite_score --set quality_score=69.8 --set valuation_score=55.9
# Composite Score REFUSED — Quality Score fails the 80.0+ gate
Quality Score 69.8 < 80.0 -- fails the gate, Composite Score is not computed for a company
that hasn't cleared Phase 01
```

**Composite Score = N/A this session — correctly withheld**, per quality-scoring.md's strict rule ("A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all... Composite Score isn't computed for, and doesn't rescue, a company failing the quality gate"). The `composite_score.py` script itself refuses to run below the gate, and that refusal is respected here rather than worked around.

**⚠️ Flagged inconsistency in this ticker's own history, corrected here:** the two most recent prior NFLX sessions (05 Jul 2026: Composite 43.0; 17 Jul 2026: Composite 39.8) both computed and reported a Composite Score *despite* NFLX's Quality Score failing the 80.0+ gate in both cases (74.0 and 69.8 respectively) — the same category of error the orchestrator flagged in the AMZN and CSGP sessions. Those two NFLX entries are left as historical, frozen records (not retroactively edited, consistent with how this framework treats past session logs), but this session does **not** repeat that error: no Composite Score is computed or reported as a number, and the standalone Valuation Score (55.9) is what drives the action recommendation below.

---

## 9. Action Recommendation

Since no Composite Score exists, the action recommendation is driven directly by (a) the standalone Valuation Score's own band and (b) the Phase 04 Quality Watch / Full Exit trigger checks — the same two independent checks the 05 Jul/17 Jul sessions ultimately used to override their (invalid) Composite readings.

### (a) Standalone Valuation Score band

Score 55.9 falls in the **50.0–69.9 "Fair Value" band → HOLD — watch only, no new entry, no trim** (per the current Action Table in operating-brief.md/strategy.md). Unlike the 17 Jul session (nominal "Cheap" band, later overridden by a failing R/R check), this session's standalone score doesn't even nominally suggest a buy — no order-setup calculation is required or performed (order_setup.py is only run for BUY/TRIM recommendations).

### (b) Phase 04 Quality Watch escalation

NFLX's Quality Score (69.8) still fails the 80.0+ gate, **unchanged** from 17 Jul — no new deterioration or improvement this session (no new fundamentals exist to move it). The Quality Watch flag from the 17 Jul session stands as-is; nothing new to escalate or de-escalate.

### (c) Full Exit trigger check (explicitly verified, not assumed absent)

| Trigger | Checked against | Result |
|---|---|---|
| Fundamental deterioration — margins structurally broken, ROIC below cost of capital | No new data this session (same TTM figures as 17 Jul: op margin, ROIC both still strong) | ❌ Not met |
| Growth thesis broken — TAM shrinking, guidance cut 2+ consecutive quarters | FY2026 guidance unchanged (no new earnings this session to cut it further); ad-tier evidence continues to support TAM expansion | ❌ Not met |
| Balance sheet crisis — leverage spikes, dilutive raise | Net debt carried forward unchanged; leverage (0.352×) remains very low | ❌ Not met |
| Extreme overvaluation — Score 90.0–100.0 sustained 2+ quarters | Score is 55.9, nowhere near this range | ❌ Not met (inapplicable) |

**No Full Exit trigger fires.**

### Net Action: **HOLD** — maintain the current 1.42%-weight position as-is

- **No add** — standalone Valuation Score (55.9) sits in the Fair Value/Hold band, not a buy band; no order setup applicable.
- **No trim** — score is far from the 70.0+ trim threshold.
- **No Full Exit** — none of the four hard triggers fire, explicitly checked.
- **Phase 04 Quality Watch flag unchanged** — Quality Score 69.8, same reading as 17 Jul; nothing new to report on the business itself. The entire score movement this session (49.3 → 55.9) is a **macro/rate-driven relabeling**, not a change in the underlying investment case — flagged explicitly so the human investor doesn't mistake it for a fundamental signal.
- **Composite Score correctly withheld** (N/A) given the failing Quality gate — see §8.

All final-decision authority rests with the human investor per the operating brief.

---

## 10. Next Review Trigger

- **Q3 2026 earnings — confirmed 20 Oct 2026** — mandatory re-score (Rule 9). Check: (a) whether Q3 revenue growth lands at or below the 11.7% guide, confirming/extending the deceleration trend, or stabilizes; (b) Q3 operating margin vs. the 33.2% guide; (c) updated share count and Q3 buyback dollar figure (feeds the Upside/Downside Modifier's shareholder-yield input and market cap directly); (d) updated balance sheet (net debt) as of 30 Sep 2026; (e) whether FY2026 guidance midpoint is reaffirmed, narrowed, or cut.
- **>15% unexplained price move from $69.22 in either direction** — immediate re-score (Rule 9).
- **Further Rate Environment Gate movement** — if the 10Y Treasury moves materially from 5.21% (either direction) before the next scheduled review, particularly back below the 5% bracket boundary or up through a further Fed-driven move, that alone would move the Rate Regime Modifier and warrants an interim check given how much of this session's score movement traced to that one input.
- **`yfinance` access** — reachable this session (a positive datapoint for `/healthcheck` — contrast with several recent sessions' TLS failures); no action needed unless it recurs.
- No position change executed by this session — recommendation only (Hold at 1.42%). If the investor acts, log it in `decisions/` per CLAUDE.md Rule 10.

---

## 11. Glossary

- **8-K (Form 8-K):** the "current report" a US public company must file with the SEC within days of a material event — Netflix's own Q2 2026 shareholder letter (carried-forward source) was filed as Exhibit 99.1 to an 8-K.
- **bps (basis points):** 1 bps = 0.01 percentage points; the Fed's 16 Sep 2026 hike was 25 bps.
- **pp (percentage points):** a direct difference between two percentages — used throughout for the WACC and Treasury-yield changes this session (e.g. the 10Y's +0.67pp rise).
- **Buyback yield (net buyback yield):** the rate a company's share count shrinks per year from repurchasing its own stock, net of new issuance — a component of shareholder yield, carried forward unchanged this session.
- **CAGR:** Compound Annual Growth Rate.
- **CapEx:** Capital Expenditure.
- **Composite Score:** this framework's blended 0.0–100.0 ranking number (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`) — **not computed this session** because Quality Score fails the 80.0+ gate (see §8).
- **DCF:** Discounted Cash Flow — a valuation method estimating value from projected future cash flows discounted to the present; rebuilt this session for a higher discount rate only (§6).
- **D&A:** Depreciation & Amortization.
- **EBIT / EBITDA:** operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **EPS:** Earnings Per Share.
- **EV / EV/EBIT, EV/EBITDA:** Enterprise Value (market cap + debt − cash) / valuation multiples dividing EV by EBIT or EBITDA.
- **EY (Earnings Yield):** 1 ÷ Forward PE, compared against the 10-Year Treasury yield in the Rate Environment Gate; used in the Earnings Yield Spread Test.
- **Earnings Yield Spread Test:** Step 1 of the Rate Environment Gate — EY minus the 10-Year Treasury yield; a spread below +1.5% adds a +5 flag to the valuation score.
- **Fast Grower:** Peter Lynch's term for EPS growth >15%/yr for 3+ years on a clean earnings base — triggers the PEG sub-score. NFLX still doesn't qualify.
- **FCF / FCF Yield / FCF/NI conversion ratio:** Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income.
- **Forward PE:** price ÷ next-twelve-months expected EPS.
- **GAAP:** Generally Accepted Accounting Principles.
- **Gross Margin:** Gross Profit ÷ Revenue.
- **Hard disqualifier:** a Quality Score condition that fails a company regardless of weighted score — none fired for NFLX this session.
- **Hurdle rate:** the minimum acceptable annual return (10%) the Upside/Downside Modifier measures expected return against.
- **Invested Capital:** total capital (debt + equity, net of cash) put to work in a business — the denominator of ROIC.
- **Moat:** a durable competitive advantage protecting a business's profits from competitors.
- **MoS (Margin of Safety):** the discount below fair value demanded before buying — not applicable this session (no buy recommendation).
- **Net Debt/EBITDA:** a leverage ratio — this framework's primary balance-sheet-risk gate.
- **Net Margin:** Net Income ÷ Revenue.
- **NOPAT (Net Operating Profit After Tax):** EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **PEG ratio:** PE ÷ earnings growth rate — not applicable to NFLX this session.
- **PT (Price Target):** an analyst's price forecast.
- **PW (Probability-Weighted) Fair Value:** this framework's blended fair value — 25% bull + 50% base + 25% bear (Rule 7) — rebuilt this session for a higher discount rate (§6).
- **Quality Score:** this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. NFLX's value (69.8) is unchanged from 17 Jul and still fails this gate.
- **Rate Environment Gate / Rate Regime Modifier:** the mandatory pre-score check comparing Earnings Yield to the 10-Year Treasury, and the resulting additive score adjustment — the primary driver of this session's score movement.
- **Rule 0 / Rule 9:** this framework's standing instructions to always fetch a live price first, and to force re-valuation on specific fundamental/macro triggers (this session's trigger: a macro shift, i.e. the Fed rate hike and 10Y surge).
- **Rule 1–8, Rule 10 (10-Rule Fair Value Framework):** the numbered valuation-methodology rules in fair-value-methodology.md, including the 3-stage DCF standard (Rule 2, used to rebuild the DCF for the new discount rate this session), normalizing one-off items (Rule 6, applied to the WBD termination fee), and separating intrinsic value from market price with a documented catalyst (Rule 10).
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss) on a trade — not applicable this session (no buy/trim recommendation, so no order setup).
- **ROIC:** Return on Invested Capital — NOPAT ÷ Invested Capital.
- **Shareholder yield:** dividend yield plus net buyback yield — carried forward unchanged this session (+4.1%/yr).
- **TAM:** Total Addressable Market.
- **Treasury yield (10Y):** the US government's 10-year borrowing rate, this framework's risk-free-rate benchmark — the single most important input this session, up from 4.54% to 5.21%.
- **TTM (Trailing Twelve Months):** the most recent 12 months of reported results — unchanged this session (same fiscal quarters as 17 Jul, since Netflix hasn't reported a new one).
- **Upside/Downside Modifier (Expected-Return Modifier):** the additive ±15 adjustment to the valuation score based on expected annual return vs. the 10% hurdle.
- **Valuation Score:** this framework's 0.0–100.0 score combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.
- **WACC:** Weighted Average Cost of Capital — used in the rebuilt DCF (§6); raised ~0.67pp across all three scenarios this session to reflect the higher risk-free rate.

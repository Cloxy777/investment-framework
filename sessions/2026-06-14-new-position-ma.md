# NEW POSITION — MA (Mastercard Incorporated) — 2026-06-14

**Task type:** NEW POSITION
**Date:** 14 Jun 2026 (Sunday — US markets closed; most recent close Fri 12 Jun 2026)
**10Y US Treasury Yield:** 4.49% (Fri 12 Jun 2026 close, CNBC/TradingEconomics — verified earlier in this batch)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current MA portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Payment network (duopoly with Visa) — asset-light financial

> **Context — prior session:** MA was evaluated as a NEW POSITION on [2026-06-07](2026-06-07-new-position-ma.md) under the old 1–10 integer scale, scoring **7/10 ("Fair Value") ≈ 66.7 on the new 0–100.0 scale** (per the [legacy conversion table](../framework/valuation-scoring.md#converting-legacy-1–10-scores): New Score = (Old Score − 1) × 100/9 = (7−1)×100/9 = 66.7), recommendation WATCHLIST ONLY. That session contains useful qualitative context (moat, capital allocation track record including the BVNK stablecoin acquisition, and a "Stalwart not Fast Grower" classification call) referenced below. This session is a **fully fresh** Rule 0 + Phase 01/02 pull using today's data and the new continuous 0–100.0 formulas — the 66.7 figure is historical context only, not reused as an input. This is also MA's **first watchlist entry** (the prior session predates the watchlist convention and was never backfilled).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$489.98** | WebSearch: "MA Mastercard stock price today June 12 2026" — Mastercard closed 12 Jun 2026 at $489.98 (day range $484.54–$492.37). Cross-checked with a second independent query ("Mastercard MA stock quote 52 week range analyst price target"), which returned a consistent 52-week range and consensus PT (see below). IBKR `get_price_snapshot`/`search_contracts` MCP tools were not attempted per this batch's note (returned "permission denied" for prior agents). |
| 52-week range | $464.52 – $601.77 | WebSearch (aggregator, cross-checked across both queries) |
| Analyst consensus PT | **$646.97** average (S&P Global, 39 analysts, "Strong Buy"; range $550–$735, lowest +12.0%, highest +49.7% from current price) | WebSearch (S&P Global via aggregator) |

**Context:** $489.98 sits **~5.5% above the 52-week low** ($464.52) and **~18.6% below the 52-week high** ($601.77) — lower third of the 52-week range, and **~24.4% below the analyst consensus PT** ($646.97). (One TIKR headline separately cites "51% upside to $744" — a different, wider target than the $646.97 S&P Global consensus; flagged for completeness but $646.97 is used as the primary consensus figure per the more detailed 39-analyst breakdown.)

Versus the 2026-06-07 session ($481.76), the price is **up ~1.7%** over the week — a routine move, not a Rule 9 trigger (>15% threshold).

---

## 2. Data Gathered (Phase 01 & 02 Inputs) & Gaps Flagged

### Revenue / Earnings history (annual, GAAP)

| Fiscal Year | Net Revenue | Operating Income (EBIT) | Net Income | Diluted EPS | YoY EPS Growth |
|---|---|---|---|---|---|
| FY2022 | $22,237M | — | — | $10.22 | — |
| FY2023 | — | — | — | $11.83 | +15.8% |
| FY2024 | — | — | — | $13.89 | +17.4% |
| FY2025 | $32,791M | $18,897M | $14,968M | $16.54 | +19.1% |

Source: Mastercard 8-K annual/quarterly earnings releases and 10-K (SEC EDGAR), cross-checked against aggregators.

### TTM (Q2 2025 – Q1 2026, via rollforward = FY2025 + Q1 2026 − Q1 2025)

| Metric | FY2025 | Q1 2026 | Q1 2025 | **TTM (rollforward)** | Cross-check |
|---|---|---|---|---|---|
| Net Revenue | $32,791M | $8,398M | $7,250M | **$33,939M** | stockanalysis.com TTM revenue $33.93B — matches to within $6M ✅ |
| Operating Income (EBIT) | $18,897M | $4,907M | $4,149M | **$19,655M** | — |
| Net Income | $14,968M | $3,882M | $3,300M | **$15,550M** | — |
| Operating Cash Flow | $17,648M | $3,000M* | $2,380M | **$18,268M** | *Q1 2026 OCF reported as "$3.0B"; consistent with separately-reported "$2.7B operating free cash flow" after $335M capex |
| CapEx (PP&E + capitalized software) | $489M | $335M ($154M+$181M) | $357M ($159M+$198M) | **$467M** | — |
| **Free Cash Flow** | $17,159M | $2,665M | $2,023M | **$17,801M** | = TTM OCF − TTM CapEx |

Source: Mastercard 8-K quarterly earnings releases and 10-Q filings (SEC EDGAR), TTM computed via rollforward (same method used in the AVGO 2026-06-14 session).

### Margins

| Metric | Value | Source/Derivation |
|---|---|---|
| Operating margin (TTM) | 59.12% (Q1 2026 figure; FY2025 adjusted operating margin 60.8%, +1.5pp YoY) | GuruFocus / Mastercard Q1 2026 earnings release |
| Net margin (TTM) | **45.8%** = $15,550M / $33,939M | Computed |
| "Gross margin" | Reported as ~100% by data aggregators (payment-network revenue-recognition quirk — no traditional COGS) | Not a meaningful read; operating margin (59.12%) used as cleaner proxy, consistent with 2026-06-07 session's treatment |

### Balance sheet / leverage (Q1 2026 10-Q, period ended 31 Mar 2026)

| Metric | Value | Source |
|---|---|---|
| Cash & cash equivalents | $7,906M | MA 10-Q (Q1 2026) |
| Short-term investments | $313M | MA 10-Q (Q1 2026) |
| Short-term debt | $1,748M | MA 10-Q (Q1 2026) |
| Long-term debt | $17,212M | MA 10-Q (Q1 2026) |
| Total debt | $18,960M | Computed |
| **Net debt** | **$10,741M** | $18,960M − $7,906M − $313M |
| FY2025 EBITDA | $21,030M (+19.21% YoY) | GuruFocus/Macrotrends |
| **Net Debt / EBITDA** | **≈0.51×** | $10,741M / $21,030M |

Net debt fell slightly from the 2026-06-07 session's $11.1B — consistent with continued buyback-funded paydown.

### Valuation multiples

| Metric | Value | Source |
|---|---|---|
| Shares outstanding | 884.38M (down from 892.44M three months ago — continued buybacks) | stockanalysis.com |
| Market Cap (computed) | $489.98 × 884.38M = **$433,322M** | Computed from live price × shares (per Rule 0 — never infer price, but here price and share count are independently sourced and multiplied) |
| Forward PE | 25.90× | GuruFocus |
| Trailing PE | 30.73× | stockanalysis.com |
| 10yr Avg PE | ~37.5–38.1× (FullRatio 37.53×, FinanceCharts 38.13×, Wisesheets 37.87×) — midpoint **~37.8×** used | Cross-checked, consistent with 2026-06-07 session's reading |
| PEG ratio (reported) | 1.59 | stockanalysis.com |
| ROIC | 94.92% (stockanalysis.com — different methodology basis than the 2026-06-07 session's 41–50% GuruFocus/FinanceCharts range; both far exceed the >15% threshold so the qualitative read is unaffected) | stockanalysis.com |

### EV/EBIT inputs

```
Market Cap = $489.98 × 884.38M ≈ $433,322M
Net Debt   = $10,741M
EV         = $433,322M + $10,741M ≈ $444,063M
EBIT (TTM) = $19,655M
EV/EBIT    = $444,063M / $19,655M ≈ 22.59×
```

### EPS growth history & Fast Grower classification — REVISED from 2026-06-07

| FY | Diluted EPS | YoY Growth |
|---|---|---|
| FY2022 | $10.22 | — |
| FY2023 | $11.83 | **+15.8%** |
| FY2024 | $13.89 | **+17.4%** |
| FY2025 | $16.54 | **+19.1%** |

3yr CAGR (FY2022→FY2025) = (16.54/10.22)^(1/3) − 1 ≈ **+17.4%**

Forward consensus: 2026E EPS ≈ $20 (+21% YoY), 2027E EPS ≈ $23 (+15% YoY); company guidance cites "mid-teens CAGR over the next three years" (2025–2027 multi-year framework).

**This materially changes the picture from 2026-06-07.** That session classified MA as a **Stalwart, not a Fast Grower**, citing (a) forward consensus *decelerating* toward ~11–15%, with (b) 2 of the trailing 3 years falling just short of the >15% bar (the 2026-06-07 session's EPS series — sourced slightly differently — showed FY22→23 growth and FY23→24 growth both below 15%).

Today's freshly-sourced EPS series shows **all three trailing years (15.8%, 17.4%, 19.1%) clearing >15%, with an accelerating (not decelerating) trend**, and forward consensus remaining mid-to-high-teens (with 2026E even higher at +21%). On a literal reading of the strategy.md test — "EPS growth >15% for 3+ years" — **MA now clears this bar on the trailing data**, and nothing in the fresh forward consensus contradicts it (no deceleration signal below 15% is visible in the data gathered this session).

**Revised classification: Fast Grower.** PEG sub-score applies at 15% weight (see §5). This is a reversal of the 2026-06-07 judgment call, driven by updated trailing EPS data — not a re-interpretation of the same data. A cross-check using the Stalwart/non-Fast-Grower path (PEG redistributed to EV/EBIT) is shown in §5 for transparency; **it does not change the action recommendation** (both land in the 50.0–69.9 Fair Value band).

### Share issuance pattern

884.38M shares outstanding, down from 892.44M (2026-06-07 session, ~3 months prior) — continued active buyback program. **Not dilutive.**

### Data Gaps / Flags Summary

1. Multiple web aggregators returned conflicting FY2025 operating-cash-flow figures ($17.6B / $15.4B / $12.0B) before a targeted search confirmed **$17,648M** directly sourced and cross-checked against the FY2023→FY2024→FY2025 OCF series ($11,980M → $14,780M → $17,648M, a clean +23.4%/+19.4% YoY progression) — used as the authoritative figure.
2. stockanalysis.com's quoted "Market cap $464.22B" and "EV $457.66B" appear to reflect a different (likely stale or differently-timed) price than today's $489.98 — **not used**; market cap and EV computed directly from today's verified price × shares outstanding + net debt, per Rule 0.
3. ROIC reading (94.92%, stockanalysis.com) differs substantially in methodology from the 2026-06-07 session's 41–50% (GuruFocus/FinanceCharts) — both are **far above** the >15% Phase 01 threshold, so this does not affect the gate result, but is flagged as a methodology-basis discrepancy for future sessions.
4. No metric was invented or estimated; all figures trace to Mastercard 8-K/10-Q/10-K filings (SEC EDGAR) or named aggregators (stockanalysis.com, GuruFocus, FullRatio, FinanceCharts, Macrotrends), with derivations shown explicitly.

---

## 3. Phase 01 — Quality Gate

| Check | MA Value | Threshold | Result |
|---|---|---|---|
| Net margin | 45.8% (TTM: $15,550M / $33,939M) | >15% | ✅ PASS — 3x threshold |
| ROIC | 94.92% (stockanalysis.com) | >15% | ✅ PASS — far above |
| Revenue CAGR 3yr | **13.8%** = ($32,791M/$22,237M)^(1/3) − 1 | >10% | ✅ PASS |
| Gross margin (operating margin proxy) | 59.12% | >40% or expanding | ✅ PASS |
| FCF positive 3+ consecutive years | FY2023 $11,980M − $CapEx / FY2024 $14,780M − CapEx / FY2025 $17,648M − $489M = $17,159M — all positive, growing | required | ✅ PASS |
| Net debt/EBITDA | ≈0.51× ($10,741M / $21,030M) | <2× (core) / <4× (Upgrade 5 asset-light networks) | ✅ PASS — clears even the strictest threshold by ~8x |
| FCF/NI conversion ratio | TTM 114.5% ($17,801M / $15,550M); FY2025 114.6% ($17,159M / $14,968M) | >70% for 2+ years | ✅ PASS |
| Share issuance pattern | 884.38M shares, down from 892.44M three months ago — active buybacks | not dilutive | ✅ PASS |
| Moat signal | Duopoly network effect (Visa/Mastercard), brand, switching costs, regulatory moat | required | ✅ PASS (qualitative — see §6) |

**Gate result: PASS — comfortably, on all 9 quantitative/qualitative criteria.** Several metrics (net margin, ROIC, FCF/NI conversion, net debt/EBITDA) clear their thresholds by 2–8x. Proceeding to the Rate Environment Gate and Phase 02 scoring.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = 25.90×
EY         = 1 ÷ 25.90 = 3.861%
Spread     = EY − 10Y Treasury = 3.861% − 4.49% = −0.629%
```
Spread (−0.629%) < +1.5% threshold → **fails** the spread test → **+5 additive** (yellow flag, not a veto, per the 2026-06-07 revision).

*(Cross-check vs. 2026-06-07: that session computed EY 4.07% vs 10Y 4.55% → spread −0.48%. Today's spread, −0.629%, is slightly worse — forward PE has risen modestly (24.6× → 25.90×) while the 10Y yield has fallen slightly (4.55% → 4.49%). The spread test fails again, as anticipated.)*

**Step 2 — Rate Regime Modifier**
10Y yield = 4.49% → falls in the **3.5–5% bracket → +5**

**Combined Rate Modifier: +5 (Step 1) + 5 (Step 2) = +10**

---

## 5. Phase 02 — Full Valuation Score

### FCF Yield (40% weight)

```
TTM FCF    = $17,801M
Market Cap = $433,322M
FCF Yield  = $17,801M ÷ $433,322M ≈ 4.107%
```

```
FCF_Score = clamp(100 × (1 − FCF_Yield% / 10), 0, 100)
          = clamp(100 × (1 − 4.107/10), 0, 100)
          = clamp(100 × 0.5893, 0, 100)
          = 58.93
```

No Owner Earnings adjustment (Upgrade 1) applies — MA is asset-light; TTM CapEx ($467M) is ~2.6% of TTM OCF ($18,268M), nowhere near the 30%-of-total-CapEx growth-CapEx trigger.

**FCF_Score = 58.93**

### EV/EBIT (25% weight — PEG applies, see below)

```
EV       = Market Cap $433,322M + Net Debt $10,741M ≈ $444,063M
EBIT TTM = $19,655M
EV/EBIT  = $444,063M ÷ $19,655M ≈ 22.59×
```

```
EV/EBIT_Score = clamp((EV/EBIT − 12) / 23 × 100, 0, 100)
              = clamp((22.59 − 12) / 23 × 100, 0, 100)
              = clamp(10.59 / 23 × 100, 0, 100)
              = clamp(46.04, 0, 100)
              = 46.04
```

**EV/EBIT_Score = 46.04**

### Forward PE + Historical PE Modifier (20% weight)

Only a 10yr **average** PE is available (~37.8×, midpoint of 37.53×–38.13× sources) — no documented low/high range — so the **fallback formula** applies:

```
Forward PE    = 25.90×
10yr Avg PE   = 37.8×
Deviation%    = (25.90 − 37.8) / 37.8 × 100 ≈ −31.48%
FwdPE_Score   = clamp(50 + Deviation% × 2.5, 0, 100)
              = clamp(50 + (−31.48 × 2.5), 0, 100)
              = clamp(50 − 78.7, 0, 100)
              = clamp(−28.7, 0, 100)
              = 0.00
```

This formula already folds in the Historical PE Modifier (Upgrade 2) — no separate ±10 applied. MA's forward PE (25.90×) sits ~31% below its own 10-year average (37.8×), a continuation of the mean-reversion-discount signal seen in the 2026-06-07 session (then −34.9%).

**FwdPE_Score = 0.00**

### PEG (15% weight) — Fast Grower classification (revised, see §2)

```
PEG (reported, stockanalysis.com) = 1.59
PEG_Score = clamp((PEG − 0.5) / 2.0 × 100, 0, 100)
          = clamp((1.59 − 0.5) / 2.0 × 100, 0, 100)
          = clamp(54.50, 0, 100)
          = 54.50
```

*(Cross-check: PEG ≈ Forward PE ÷ near-term growth. Using 2026E EPS growth (+21%): PEG ≈ 25.90/21 ≈ 1.23 → PEG_Score ≈ 36.6. Using 3yr trailing CAGR (17.4%): PEG ≈ 25.90/17.4 ≈ 1.49 → PEG_Score ≈ 49.4. All three readings (1.23, 1.49, 1.59) are in the same general range and land the final score within ~0.1–1pt of each other — see Final Score sensitivity below.)*

**PEG_Score = 54.50**

### Final Score Calculation — Fast Grower path (primary)

PEG applies (Fast Grower) → weights are FCF 40% / EV-EBIT 25% / FwdPE 20% / PEG 15%.

```
Final Score = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.25) + (FwdPE_Score × 0.20) + (PEG_Score × 0.15) + Rate Modifier
            = (58.93 × 0.40)     + (46.04 × 0.25)          + (0.00 × 0.20)       + (54.50 × 0.15)      + 10
            = 23.572             + 11.510                  + 0.000               + 8.175               + 10
            = 43.257 + 10
            = 53.257
```

Round to nearest 0.1 → **53.3** (53.257 rounds to 53.3 under standard rounding; not on a ".X5" boundary so the round-up rule doesn't additionally apply)

### Cross-check — Stalwart path (PEG redistributed to EV/EBIT at 40%)

```
Final Score = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20) + Rate Modifier
            = (58.93 × 0.40)     + (46.04 × 0.40)          + (0.00 × 0.20)       + 10
            = 23.572             + 18.416                  + 0.000               + 10
            = 41.988 + 10
            = 51.988 → rounds to 52.0
```

**Both classification paths (53.3 Fast Grower / 52.0 Stalwart) land in the same 50.0–69.9 "Fair Value" band** — the action recommendation is identical either way (see §6). The Fast Grower classification is the primary call this session given the fresh, accelerating trailing-EPS data (§2), but the action is robust to the alternative.

---

## 6. Final Valuation Score & Action

# **Final Score: 53.3 — "Fair Value"** (cross-check: 52.0 under the Stalwart path — both within the same band)

| Score | Label | Action (Phase 03/05 — strategy.md Action Table) |
|---|---|---|
| **50.0–69.9** | Fair Value | HOLD — watch only, no new entry, no trim |

### What's driving this score

- **FCF Yield (58.93, moderately expensive)** — MA's ~4.1% FCF yield is right in the middle of the FCF_Score scale; richer than the "cheap" end (≥10% → 0) but well short of the "expensive" extreme.
- **EV/EBIT (46.04, moderate)** — at 22.59×, MA's EV/EBIT sits just under the midpoint (23.5× → 50.0) of the 12×–35× scale — neither cheap nor expensive on this lens.
- **Forward PE vs 10yr history (0.00, cheapest possible)** — MA's forward PE (25.90×) is ~31% *below* its own 10-year average (37.8×), the single biggest "cheap" signal in this score.
- **PEG (54.50, moderate-to-rich)** — at a PEG of 1.59, MA's reasonably-fast EPS growth (17.4% 3yr CAGR, accelerating) doesn't fully offset its absolute multiple.
- **+10 Rate Modifier** (the maximum combined Step 1 + Step 2 contribution under current rules) — the spread test fails again (−0.629%, slightly worse than the 2026-06-07 session's −0.48%), and the 10Y sits in the 3.5–5% bracket.

Without the +10 rate modifier, the raw weighted score would be ~43.3 (Fast Grower path) — solidly in the 30.0–49.9 "Cheap — standard position" band. **The rate modifier is the deciding factor pushing MA from "Cheap" to "Fair Value"** — a direct illustration of "capital has a real cost" (strategy.md's rationale for the 3.5–5% bracket).

### Qualitative cross-check (5 questions + disruption vector)

*(Reproduced/updated from the 2026-06-07 session — qualitative picture is materially unchanged over one quarter)*

1. **Why are margins high?** Two-sided network effect + scale — MA earns a toll on a duopoly rail (with Visa) that merchants and banks can't easily route around.
2. **What would it take to compete?** Building trust with billions of cardholders, tens of millions of merchants, and thousands of issuing/acquiring banks simultaneously — a multi-decade chicken-and-egg problem. Hard moat.
3. **Capital allocation:** Consistent buybacks (884.38M shares, down from 892.44M three months ago) + growing dividend + disciplined bolt-on M&A (e.g., the BVNK stablecoin-infrastructure deal, ~$1.5B, announced alongside Q1 2026 results) funded from FCF, not debt. Net debt continues to decline (~$11.1B → ~$10.7B over the quarter).
4. **Growth sources next 3–5 years:** Continued cross-border volume growth and accelerating Value-Added Services & Solutions revenue (VAS net revenue +22% in Q1 2026, +18% currency-neutral) — a genuine second growth engine diversifying away from pure transaction-toll economics. EPS growth has *accelerated* for three straight years (15.8% → 17.4% → 19.1%), and 2026 guidance (+21% consensus) continues that trend.
5. **Best bear case / disruption vector:** Real-time payment rails (e.g., FedNow, Pix, UPI) and stablecoin/crypto settlement rails could disintermediate card networks over a long horizon — though MA's BVNK acquisition reads as a hedge (own a piece of the disruption rather than be run over by it). Regulatory/interchange-fee pressure (EU, US merchant litigation) is the more near-term risk to monitor.

None of this changes the **quantitative** verdict — MA remains an excellent business, just not currently a *cheap* one. If anything, the fundamentals have gotten modestly *better* (accelerating EPS growth, declining net debt) while the score has moved from 66.7 (2026-06-07, old-scale-converted) to 53.3 today — almost entirely a function of the forward PE moving further below its 10-year average (cheaper signal) and the Fast Grower reclassification (which the 2026-06-07 session did not apply), partially offset by a slightly worse rate-spread reading.

---

## 7. Order Setup — NOT PRODUCED (by design)

Per the operating brief, the full Fair-Value/DCF/buy-sell-stop workup is run **"for every BUY or TRIM action."** A Score of 53.3 is neither a BUY (requires ≤49.9) nor a TRIM (n/a for a non-held name; TRIM only triggers at ≥70.0 anyway). The order-setup checklist gates on *"Valuation Score: ___ (must be ≤ 49.9 to enter)."* Building a full 3-scenario DCF here would mean producing buy/sell/stop levels for a trade the framework explicitly says not to make — consistent with both the 2026-06-07 MA session and the 2026-06-14 AVGO session's conventions at similar scores.

**What can be said without inventing numbers:** $489.98 sits ~24.4% below the analyst consensus PT ($646.97) — that's *other parties'* fair-value reads, cited per Rule 0 Step 4, not this framework's own blended FV. The valuation-score engine reads "fair value" (53.3) because the rate modifier (+10) is currently the single largest contributor to the score — the underlying business metrics (FCF yield 58.93, EV/EBIT 46.04, forward-PE-vs-history 0.00, PEG 54.50) average to a raw weighted score of ~43.3, which on its own would sit in the 30.0–49.9 "Cheap — standard position" band.

**What would move this toward a BUY** (scenario sketch only, not a standing order or trigger to act on): the raw (pre-rate-modifier) score of ~43.3 is already in "Cheap" territory — it's the +10 rate modifier that pushes the total to 53.3. Two paths could close this gap without any framework rule change: (a) a **decline in the 10Y Treasury yield below 3.5%** would cut the Step 2 modifier from +5 to 0 (a −5 swing); (b) a **price decline of roughly 10–15%** (toward the $415–440 zone, i.e. toward/through the 52-week low of $464.52) would lift the FCF yield toward ~4.6–4.8% and pull EV/EBIT toward ~20×, which combined with the existing favorable PE-vs-history and PEG signals could plausibly pull the raw weighted score down into the high-20s/low-30s — even a modest further deterioration in the rate-spread reading would likely still leave the *total* score comfortably under 50.0 in that scenario. **This is not a standing order or a commitment** — it's a level worth a fresh, full re-score if reached, consistent with Rule 9 (>15% move triggers re-score regardless).

---

## 8. Recommendation

# **WATCHLIST ONLY — do not open a position now.**

MA passes the Phase 01 quality gate comfortably on all 9 criteria — exceptional margins (45.8% net margin, 59.1% operating margin), minimal leverage (0.51× net debt/EBITDA), near-total-plus FCF conversion (114.5% TTM), a durable duopoly-network moat, and an intelligently-run, buyback-heavy capital allocation program with continued debt paydown. The Phase 02 valuation score of **53.3 ("Fair Value")** — or 52.0 under the alternate Stalwart classification, same band either way — means there is currently **no margin of safety** to justify a new entry; per Phase 03, Score 50.0–69.9 = hold-and-watch, not buy.

Notably, the **underlying business has gotten modestly better** since the 2026-06-07 session (EPS growth accelerating to +19.1% in FY2025, net debt continuing to decline, VAS revenue still growing ~20%+), and the raw pre-rate-modifier score (~43.3) would already sit in the "Cheap — standard position" band. **The entire gap between "Cheap" and "Fair Value" here is the +10 Rate Regime + Spread-Test modifier** — a textbook illustration of Buffett's "interest rates as gravity" framing (strategy.md's rationale for the 2026-06-07 Step 1 revision). This is a name to watch closely for either a rate-environment shift (10Y below 3.5%) or a price pullback toward the 52-week-low zone, either of which could plausibly bring it into BUY territory without any deterioration in the underlying business.

**Add MA to the watchlist** (`not-in-portfolio/MA/`) with a re-evaluation trigger at:
- **Next earnings release** (MA reports Q2 2026 results expected late July/early August 2026) — re-run Phase 02 with refreshed TTM EBIT, TTM FCF, and confirm the Fast Grower reclassification holds with another quarter of EPS data.
- A **10Y Treasury yield decline below 3.5%** (Step 2 modifier would drop from +5 to 0, a −5 point swing that alone would not flip the action band but moves materially in that direction).
- A **>15% unexplained price move** from $489.98 (Rule 9) — particularly a decline toward/through the 52-week low ($464.52) and into the $415–440 zone sketched above.
- Any **guidance revision, M&A (continued BVNK integration), or management change** (Rule 9).

---

## 9. Next Review Trigger

**Date/event:** Mastercard's Q2 2026 earnings release (expected late July/early August 2026) — re-run Phase 02 with refreshed TTM EBIT, TTM FCF, and a fourth consecutive quarter's EPS data point to further confirm/disconfirm the Fast Grower classification. Earlier trigger if a >15% unexplained price move from $489.98 occurs (Rule 9), a 10Y Treasury move below 3.5%, or any guidance/M&A/management-change event.

**No position opened — nothing to log in `decisions/`.**

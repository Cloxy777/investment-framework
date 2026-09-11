# RESCORE — ADBE (Adobe Inc.) — 2026-09-11

## 1. Session header

- **Task type:** RESCORE (single ticker, `--both` mode — Quality + Valuation)
- **Date:** 2026-09-11
- **10Y US Treasury yield:** 4.83% (FRED `DGS10`, most recent posted value, 2026-09-09 — 09-10/09-11 not yet posted)
- **Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% band)
- **Prior scores (2026-07-29):** Valuation 0.0 (floor), Quality Score 83.9, Composite Score 8.1 — BUY, top up toward target
- **Current ADBE weight:** 4.29% of portfolio per [holdings.md](../portfolio/holdings.md) (last synced 2026-09-06 at $266.50/share; stale relative to this session's live price given the post-earnings move — see §3); position is a partial fill (10 shares held)
- **Sector:** Technology — Software (Creative & Marketing Professionals / Business Professionals & Consumers — see §4 note on Adobe's reporting-structure change)
- **Trigger:** Telegram post (bolshegold, 2026-09-10) reporting Adobe's Q3 FY2026 earnings. Per Rule 0, the post's numbers were **not** used as data — they served only as the signal to pull real data. Everything in this session is independently sourced from Adobe's own SEC filings (8-K + Exhibit 99.1 press release, filed 2026-09-10) and SEC XBRL company-facts data, cross-checked against IBKR and Yahoo Finance. This is also ADBE's scheduled "Next review trigger" from the 2026-07-29 entry ("Q3 FY2026 earnings, ~mid-Sept 2026").
- **This session's job:** (1) fetch live price (Rule 0), (2) fully recompute the Quality Score off refreshed TTM financials through Q3 FY2026, (3) fully recompute the Valuation Score (Rate Gate + all sub-scores + Upside/Downside Modifier) off a refreshed DCF/multiples fair value, (4) recombine into the Composite Score, (5) produce the action recommendation and order setup, (6) separately flag and review a management-change event found independently via SEC EDGAR.

## 2. Data gaps flagged (before proceeding)

1. **`yfinance`'s default HTTP session (`curl_cffi`) failed** with a TLS/connection-reset error against Yahoo's endpoints (a recurring issue in this repo's session history). **Resolved** by passing `yfinance.Ticker(..., session=requests.Session())` with a standard `User-Agent` header — this restored full access (quote data, quarterly EPS history, price history) without needing to fall back to a degraded data source. Documented here since it's a cleaner fix than prior sessions' full fallback-to-WebSearch workaround, worth reusing in future sessions.
2. **Q3 FY2026 10-Q not yet filed.** Adobe furnished Q3 results via 8-K (Exhibit 99.1 press release) on 2026-09-10; the press release itself states the 10-Q "is expected to file in Sept. 2026" but hadn't as of this session. The press release discloses full 3-month and 9-month income-statement figures, and 3-month (not 9-month) cash-flow figures. **9-month TTM cash-flow inputs (OCF, CapEx, D&A) were reconstructed** by summing the already-filed Q1 FY26 and Q2 FY26 10-Q cumulative figures with the Q3 FY26 3-month figures from the press release (shown in full in §4) — a legitimate reconstruction from primary-source numbers already on the record, not an estimate.
3. **Exact point-in-time shares outstanding as of the Aug 28, 2026 quarter-end is not yet filed** (the next 10-Q cover page will have it). The last filed cover-page count is 397.5M (as of 2026-06-11, pre-dating ~9.5M shares of Q3 buybacks). This session uses Adobe's own disclosed **Q3 FY26 weighted-average diluted share count (395M)**, from the press release's EPS reconciliation table, as the best available current estimate — flagged as a weighted-average proxy, not an exact spot count, but more current than the stale 397.5M cover-page figure.
4. **5yr avg/low/high PE reconstruction rolled forward one quarter.** Per the automated method in [valuation-scoring.md](../framework/valuation-scoring.md) (rolling 20-quarter TTM-EPS-vs-price series), this window now runs 2021-12-16 → 2026-09-10 (previously 2021-03-23 → 2026-06-11). The 2026-09-10 EPS/price pair uses IBKR's confirmed $248.83 close for that date (Yahoo's own price history returned `NaN` for that date at the time of this session — a data-refresh lag right after the close, not a real gap).
5. **Shareholder yield (an Upside/Downside Modifier input) recomputed rather than carried forward.** Prior sessions used a flat +2%/yr assumption. This session instead computed net buyback yield from actual SEC-filed share-count decline (397.5M → 424.2M-ish trend, see §7) — a materially higher ~+6.5%/yr. Flagged as a correction of an apparently understated prior assumption; it does not change this session's outcome (the modifier still floors at −15 either way — see §7's robustness note), but is shown for calculation transparency (no black-box outputs).
6. **A material, primary-source-verified management-change event was found independently** via SEC EDGAR — not mentioned in the triggering Telegram post — and is folded into this rescore as its own Rule 9 trigger. See §3.5.

## 3. Live data (Rule 0 — fetched first)

| Item | Value | Source |
|---|---|---|
| **Live price used** | **$244.30** | IBKR `get_price_snapshot` (contract_id 265768, NASDAQ) — last trade, **after-hours** following Adobe's Q3 FY2026 earnings call (2:00pm PT / 5:00pm ET, 2026-09-10). Cross-checked: IBKR `get_price_history` confirms the prior regular-session close was $248.83 (2026-09-10), and the snapshot's own `change` field (−$4.53 / −1.82%) reconciles exactly against that close, confirming the after-hours print is genuine and current, not stale. See the **After-hours trading** glossary entry — this is a real, live traded price and is used as the Rule 0 price of record since it is the most current print available. |
| Bid / Ask | $243.55 / $244.99 | IBKR `get_price_snapshot` |
| 52-week high / low | $370.86 / $190.12 | IBKR `get_price_snapshot` `misc_statistics` |
| 13-week high / low | $294.53 / $190.12 | IBKR `get_price_snapshot` `misc_statistics` |
| Prior regular-session close (2026-09-10) | $248.83 (day range $247.19–$255.00) | IBKR `get_price_history` (ONE_WEEK, ONE_DAY bars) |
| Shares outstanding (used for Market Cap) | **395M** (Q3 FY26 weighted-average diluted, company-disclosed) | Adobe Q3 FY2026 press release (EPS reconciliation table) — see Data Gap #3 |
| Market Cap (computed) | 395M × $244.30 = **$96,498.5M** | Computed |

### 3.5 Rule 9 trigger #2 — CEO transition, found independently via SEC EDGAR

Alongside the earnings trigger, this session found a **separate, material Rule 9 management-change event** not mentioned in the triggering Telegram post: Adobe's **8-K filed 2026-09-08** (Item 5.02, event date 2026-09-02) discloses:
- **Anil Chakravarthy** (currently President, Customer Experience Orchestration Business) appointed **President and CEO**, effective **2026-12-01**.
- **Shantanu Narayen** (current Chair & CEO) will retire as CEO and become **Executive Chair** of the Board on the same date.
- Separately, **David Wadhwani** (President, Creativity & Productivity Business — the executive who has run Adobe's core Creative Cloud/Document Cloud franchise) notified the company on 2026-09-02 that he is **stepping down effective 2026-09-27**, remaining afterward only as a senior advisor during the transition.
- **CFO seat remains interim** — Steven Day signs this 8-K as "Interim Chief Financial Officer" (unchanged status since 2026-06-15; no permanent CFO yet named).

Per [operating-calendar.md](../framework/operating-calendar.md)'s Rule 9 table, a management change (CEO, CFO) mandates "re-score + thesis review + moat re-evaluation" — done here:

- **Not treated as a Phase 06 exit trigger.** This is an orderly, board-announced succession with a 3-month runway (announced Sept 2, effective Dec 1) and the outgoing CEO staying on as Executive Chair for continuity — not a disorderly departure, forced-out situation, or restatement-adjacent event. Phase 06 requires evidence of moat erosion, TAM shrinkage, or a balance-sheet crisis; an orderly succession is not itself that evidence.
- **A genuine thesis question worth monitoring, not dismissing.** Two things stand out: (1) the incoming CEO's background is in Customer Experience Orchestration (the Digital Experience / marketing-cloud side of the business), not Creative Cloud — Adobe's historic moat center of gravity — and (2) the departure of the executive who ran the Creativity & Productivity business happens in the same week. Together these could plausibly presage a strategic re-weighting toward the enterprise/experience side of the business. This is not yet evidenced in the numbers: Q3 FY26 **Creative & Marketing Professionals subscription revenue grew 13% YoY** ($4.65B) — Adobe's own reporting shows the core creative franchise still accelerating, not being deprioritized.
- **Moat Signal checklist unchanged this session** (§4) — no new cited evidence flips a signal from false to true or vice versa. The leadership transition is a forward-looking risk to monitor at the next review, not a backward-looking fact that changes today's moat evidence.
- **Segment reporting has also changed.** Adobe's Q3 FY26 press release no longer references the old "Digital Media" / "Digital Experience" segment split used in this repo's prior ADBE sessions' review triggers — it now reports only two "Customer Groups": **Business Professionals & Consumers** ($1.91B, +16% YoY) and **Creative & Marketing Professionals** ($4.65B, +13% YoY). The "Next review trigger" language is updated accordingly in §11.

**Set as an explicit follow-up review trigger** (§11): re-check moat/segment evidence once Wadhwani's departure (2026-09-27) and the CEO transition (2026-12-01) have actually taken effect, not just been announced.

## 4. Quality Score (full recomputation, TTM through Q3 FY2026)

All inputs recomputed from primary sources — Adobe's FY2023–FY2025 10-Ks/10-Qs (SEC XBRL company-facts API) and the Q3 FY2026 8-K/press release. TTM = FY2025 (ended 2025-11-28) − 9 months ended 2025-08-29 + 9 months ended 2026-08-28.

```
FY2025 (10-K):        Revenue 23,769 | Gross Profit 21,218 | Op. Income 8,706 | Net Income 7,130 | Tax 1,604 | D&A 818 | OCF 10,031 | CapEx 179
9mo ended 2025-08-29:  Revenue 17,575 | Gross Profit 15,673 | Op. Income 6,445 | Net Income 5,274 | Tax 1,196 | D&A 634 | OCF  6,871 | CapEx 145
9mo ended 2026-08-28:  Revenue 19,776 | Gross Profit 17,634 | Op. Income 7,010 | Net Income 5,428 | Tax 1,589 | D&A 582 | OCF  7,646 | CapEx 180
  (9mo FY26 D&A = Q1 174 + Q2 193 + Q3 215, all $M, per SEC XBRL quarterly filings + Q3 press release)
  (9mo FY26 OCF = 6mo cumulative $5,123M [10-Q] + Q3 3-month $2,523M [press release] = $7,646M; CapEx = 6mo $95M + Q3 3-month $85M = $180M)

TTM Revenue     = 23,769 − 17,575 + 19,776 = $25,970M
TTM Gross Profit= 21,218 − 15,673 + 17,634 = $23,179M   → Gross Margin = 89.25%
TTM Op. Income  =  8,706 −  6,445 +  7,010 = $9,271M    → Operating Margin = 35.70%
TTM Net Income  =  7,130 −  5,274 +  5,428 = $7,284M    → Net Margin = 28.05%
TTM Tax         =  1,604 −  1,196 +  1,589 = $1,997M
TTM Pretax Inc. = (7,130+1,604) − 6,470 + 7,017 = $9,281M   → Effective tax rate = 1,997/9,281 = 21.52%
TTM D&A         =    818 −    634 +    582 = $766M
TTM OCF         = 10,031 −  6,871 +  7,646 = $10,806M
TTM CapEx       =    179 −    145 +    180 = $214M
TTM FCF (OCF−CapEx) = $10,592M
TTM EBITDA (Op. Income + D&A) = 9,271 + 766 = $10,037M
```

**Balance sheet (as of 2026-08-28, per Q3 press release):** Total Debt = $1,597M (current) + $4,766M (long-term) = $6,363M. Cash & equivalents $4,359M + Short-term investments $1,280M = $5,639M. **Net Debt = $6,363M − $5,639M = $724M** (a flip from ~$385M *net cash* at FY2025 year-end — driven by ~$9.3B of TTM gross buybacks against a much smaller net debt raise; still a trivially small leverage figure either way).

```
Profitability (25% weight):
  NOPAT = TTM Op. Income × (1 − eff. tax rate) = 9,271 × (1 − 0.2152) = $7,276M
  Invested Capital = Total Debt ($6,363M) + Shareholders' Equity ($11,764M) = $18,127M   (framework's own method — no cash netting, consistent with prior ADBE sessions)
  ROIC = 7,276 / 18,127 = 40.14%
  NetMargin_Component = clamp((28.05/30)×100) = 93.5   ← below the 100 clamp ceiling for the first time (was 100.0 at FY2025's exact-30.00% net margin)
  ROIC_Component       = clamp((40.14/30)×100) = clamp(133.8) = 100.0
  Profitability_Score  = (93.5 + 100.0) / 2 = 96.7   (no FCF-positive cap — FCF positive every year on record)

Margins (15% weight): Gross Margin (TTM) = 89.25% (vs. FY2025's 89.27% — flat, no compression)
  GrossMargin_Score = clamp((89.25/80)×100) = clamp(111.6) = 100.0   (already at the clamp ceiling; trend bonus moot)

Growth (20% weight): Revenue 3yr CAGR — still FY2022 ($17,606M) → FY2025 ($23,769M) = 10.52%, UNCHANGED this session.
  Reasoning: this sub-score is defined over completed fiscal years, and FY2025 remains Adobe's most recently completed fiscal year (FY2026 doesn't close until ~Nov 2026) — there is no new fiscal year to roll the window forward onto yet, so this is a deliberate "nothing changed" finding, not a carried-forward guess.
  Growth_Score = clamp((10.52/25)×100) = 42.09
  TAM-expansion / pricing-power evidence (+10, reinforced this session): Q3 FY26 press release discloses "AI-first ARR grew more than 150% year over year" and Adobe "[achieved] a major milestone of 1 billion monthly active users (MAU) across creativity and productivity solutions" — both primary-source, company-disclosed figures documenting continued, genuine TAM expansion (a new usage surface at even larger scale than the 06-20/07-04 sessions' "Freemium MAU 50M→90M" and "AI-first ARR 3x YoY to >$500M" findings). FY2026 guidance was also raised this quarter (see §3.5), not cut — consistent with acceleration, not deceleration, so no −10 penalty.
  Growth_Score (with bonus) = 42.09 + 10 = 52.09

Balance Sheet (15% weight): Net Debt/EBITDA = 724 / 10,037 = 0.0721×
  BalanceSheet_Score = clamp(100×(1 − 0.0721/4)) = clamp(100×0.9820) = 98.2   (improved vs. 07-04's 96.4 — net debt fell even as EBITDA grew)

Moat Signal (15% weight) — checklist unchanged from 07-04 (see Data Gap discussion / §3.5 — the CEO transition is a forward risk to monitor, not new backward-looking moat evidence):
  ✓ Market share stable/growing — TRUE (unchanged basis; reinforced by the new 1B-MAU milestone as a reach/scale datapoint, though that is a total-MAU figure, not a market-share-specific one, so cited as reinforcing context rather than new independent evidence).
  ✓ Brand premium / pricing power — TRUE (unchanged basis: sustained 2026 list-price increases with continued subscriber growth).
  ✗ Network effect — FALSE (no new evidence found this session).
  ✓ Switching costs — TRUE (unchanged basis: integrated Creative Cloud stack, net revenue retention 130%+).
  ✗ Scale cost advantage — FALSE (no cited cost-per-unit evidence found this session; same gap as prior sessions).
  Moat_Score = (3/5) × 100 = 60.0

FCF Quality (10% weight): FCF/NI conversion (TTM) = 10,592 / 7,284 = 145.4%
  FCFQuality_Score = clamp(((1.454 − 0.40)/0.60)×100) = clamp(175.7) = 100.0

Quality Score = 96.7×0.25 + 100.0×0.15 + 52.09×0.20 + 98.2×0.15 + 60.0×0.15 + 100.0×0.10
              = 24.19 + 15.00 + 10.42 + 14.73 + 9.00 + 10.00
              = 83.334 → rounds to 83.3
```

**Hard disqualifier check** — none fire: FCF/NI conversion 128–156% across FY2022–FY2025 and 145.4% TTM (comfortably >70%); Net Debt/EBITDA 0.07× (far under 2.5×/4× thresholds); FCF positive every year on record.

**Quality Score = 83.3 — PASSES the 80.0+ gate**, down modestly from 83.9 (07-29/07-04). The move is real, not noise: **Net Margin compression from a rising effective tax rate** (TTM 21.52% vs. FY2025's 18.37%, itself driven by the GAAP tax-rate step-up embedded in the Q3/Q4 FY26 non-GAAP reconciliation tables) plus a **Q2 FY26 $70M goodwill impairment and $30M loss contingency** (both disclosed in the Q3 press release's non-GAAP reconciliation, both real GAAP charges this framework doesn't strip out per its GAAP-scoring convention) pulled the Profitability_Score off its prior 100.0 ceiling to 96.7 — the first time in ADBE's four rescores that this sub-score hasn't clamped. This is exactly the kind of genuine quality drift Phase 04 monitoring exists to catch; it's modest and doesn't threaten the 80.0 gate, but it's a real signal, not a rounding artifact, and is flagged as a Quality Watch item (not yet at the Phase 04 ">3pp margin compression" flag threshold — Operating Margin moved 36.63% → 35.70%, about 0.9pp).

## 5. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $244.30 / $24.475 (FY2026 non-GAAP EPS guidance midpoint, raised this quarter to $24.45–$24.50 — see §3.5) = 9.982×
EY = 1 / 9.982 = 10.018%
Spread = 10.018% − 4.83% (10Y) = +5.188%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** → no +5 additive.

**Step 2 — Rate Regime Modifier**
10Y = 4.83% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for ADBE = +5**

## 6. Phase 02 — Valuation Score (every sub-score shown)

**FCF Yield — 40% weight**
```
FCF (TTM) = $10,592M
FCF Yield = 10,592 / 96,498.5 = 10.976%
FCF_Score = clamp(100 × (1 − 10.976/10), 0, 100) = clamp(−9.76, 0, 100) = 0.0
```
→ Contribution: **0.0**

**EV/EBIT — 40% weight** (PEG not applicable — see below — its 15% weight redistributed here)
```
EV = Market Cap $96,498.5M + Net Debt $724M = $97,222.5M
EV/EBIT = 97,222.5 / 9,271 (TTM EBIT) = 10.487×
EV/EBIT_Score = clamp((10.487 − 12)/23 × 100, 0, 100) = clamp(−6.58, 0, 100) = 0.0
```
→ Contribution: **0.0**

**Forward PE (fallback formula, 5yr avg) — 20% weight**
```
5yr avg PE (auto-computed, rolled forward one quarter to include Q3 FY26 — see Data Gap #4): 25.1× (range 8.9×–44.6×, n=20 quarters, 2021-12-16 → 2026-09-10)
Deviation% = (9.982 − 25.108) / 25.108 × 100 = −60.25%
FwdPE_Score = clamp(50 + (−60.25 × 2.5), 0, 100) = clamp(−100.6, 0, 100) = 0.0
```
(Fallback formula already folds in the Historical PE Modifier — consistent with every prior ADBE session's choice of the fallback formula over the primary range-based one, despite a range being computable, to keep this ticker's methodology stable across sessions.)
→ Contribution: **0.0**

**PEG — not applicable.** Non-GAAP EPS growth FY2024 +14.55% ($16.08→$18.42) / FY2025 +13.74% ($18.42→$20.95) — both most-recently-completed fiscal years are below the 15% Fast-Grower threshold (unchanged finding). FY2026's raised guidance implies ~+16.8% EPS growth, but a guided, not-yet-completed year doesn't establish the "3+ years clean trailing base" the Fast-Grower test requires. **Still NOT a Fast Grower** → weight redistributed to EV/EBIT (40%, above).

```
Raw weighted score = 0.0 + 0.0 + 0.0 = 0.0
+ Rate Regime Modifier (+5) = 5.0
```

## 7. Upside/Downside Modifier (Expected-Return Modifier) — full calc, fair value refreshed

Adobe's Q3 earnings release is itself a mandatory Rule 9 model-refresh trigger (fair-value-methodology.md Rule 9: "Quarterly earnings release"), so the DCF/multiples fair-value work is **refreshed from updated TTM inputs this session**, not carried forward.

### Fair Value (Blended) — refreshed

**Method A: DCF (3-stage, 3 scenarios — Rule 2/7).** Same scenario structure (WACC/growth/fade/terminal) as every prior ADBE session — no qualitative change to the thesis this quarter — with TTM FCF ($10,592M, up from $10,280M) and shares (395M, down from 397.5M) refreshed.

| Scenario | WACC | Yrs1–5 FCF growth | Yrs6–10 fade | Terminal | TV weight | **FV/share** |
|---|---|---|---|---|---|---|
| **Bear** (AI structurally impairs moat) | 11.5% | ~2% | 1.5%→0.5% | 1.5% | 38.7% | **$274.60** |
| **Base** (consensus, moat holds) | 10.5% | ~7% | 6%→4% | 3.0% | 52.4% | **$463.87** |
| **Bull** (Firefly/AI monetization re-rates) | 9.5% | ~9% | 7.5%→5.5% | 4.0% | 62.9% | **$685.32** |

```
PW DCF FV = 0.25×685.32 + 0.50×463.87 + 0.25×274.60 = $471.91
```
TV weight 38.7–62.9% — under the 75% Rule-4 trigger to extend Stage 2. Even the hardened bear case ($274.60) sits well above the live price ($244.30).

**Method B: Comparable Multiples** (all deliberately discounted below ADBE's own rolled-forward 5yr-avg 25.1×)

| Approach | Fair multiple | FV/share |
|---|---|---|
| Forward PE comp | 15× × $24.475 | $367.13 |
| EV/EBIT comp | 14× × TTM EBIT $9,271M, less net debt $724M, ÷395M sh | $326.76 |
| FCF-yield comp | 7% yield on TTM FCF $10,592M, less net debt, ÷395M sh | $381.24 |
| **Multiples avg** | | **$358.38** |

```
Blended FV = 0.40 × DCF(PW) $471.91 + 0.60 × Multiples $358.38 = $403.79
```

**Cross-check vs. external:** WebSearch found analyst consensus PT clustered $263–$275 as of early September 2026 (pre-earnings-reaction; Benzinga/TipRanks/stockanalysis.com aggregation — sources below). Blended FV ($403.79) sits well above this, consistent with every prior ADBE session's finding — a DCF reflecting multi-year cash generation vs. 12-month PTs still pricing in near-term "priced for perfection" caution around the in-line-not-beat Q4 guide.

Sources: [Benzinga](https://www.benzinga.com/analyst-stock-ratings/price-target/26/09/61706607/top-wall-street-forecasters-revamp-adobe-expectations-ahead-of-q3-earnings), [TipRanks](https://www.tipranks.com/stocks/adbe/forecast), [stockanalysis.com](https://stockanalysis.com/stocks/adbe/forecast/)

### Upside/Downside Modifier calc

```
Gap Upside % = (403.79 / 244.30) − 1 = +65.29%
Catalyst window = 2.0 yr (unchanged — Creative & Marketing Professionals segment growth [the successor to "Digital Media"] and continued AI-monetization scaling, both within 18–24mo)
Annualized gap = 65.29% / 2.0 = 32.64%/yr
Intrinsic growth = +10%/yr (unchanged — anchored to ~10.5% revenue CAGR)
Shareholder yield = +6.5%/yr (RECOMPUTED this session — see Data Gap #5: SEC cover-page shares outstanding fell from 424.2M [2025-06-20] to 397.5M [2026-06-11], a 6.3% decline over ~356 days, ≈6.5%/yr annualized net-of-dilution buyback rate. Replaces the prior sessions' flat +2%/yr assumption, which appears to have understated Adobe's actual buyback intensity — TTM gross repurchases were ~$9.3B against a ~$96.5B market cap.)

E = 32.64% + 10% + 6.5% = +49.14%/yr
```

**Map E → M** (hurdle H = 10%, E ≥ H branch):
```
M = −15 × clamp((49.14 − 10)/15, 0, 1) = −15 × clamp(2.61, 0, 1) = −15 × 1 = −15.0
```
**Modifier M = −15.0** (hits the −15 floor).

**Guardrails check:**
- Catalyst within 18–24mo? **Yes** — Q4 FY26 print (~Dec 2026, ~3 months out) and continued AI-monetization scaling through FY2027, both inside the window. Upside-side credit not capped.
- Scenario-weighted (not the rosy point)? **Yes** — bull/base/bear DCF blend as always.
- **Robustness note:** even using the old, more conservative +2%/yr shareholder-yield assumption instead of the recomputed +6.5%, E would still be 32.64+10+2 = 44.64% — still far past the 25%/yr point where M floors at −15. **The recomputation doesn't change this session's outcome**, but is shown because "never invent or estimate financial data" cuts both ways — an unexamined round-number assumption deserves the same scrutiny as a missing one.

## 8. Final Valuation Score + Composite Score

```
FINAL VALUATION SCORE = 5.0 (raw + rate gate) + (−15.0) (Upside/Downside) = −10.0 → clamped to the 0.0 floor
```

| | Value |
|---|---|
| Raw weighted | 0.0 |
| Rate Regime Modifier | +5.0 |
| Upside/Downside Modifier | −15.0 (E = +49.14%/yr) |
| **FINAL VALUATION SCORE** | **0.0** (floor) |
| Prior valuation score (07-29) | 0.0 |
| **Quality Score (this session)** | **83.3 — PASSES 80.0+ gate** (down from 83.9) |

```
Composite Score = 0.50 × (100 − 83.3) + 0.50 × 0.0 = 0.50 × 16.7 = 8.35
  → exactly on a ".X5" boundary → round UP (conservative) → 8.4
```

**Composite Score = 8.4** (up slightly from 8.1, mechanically reflecting the lower Quality Score) — still deep in the **0.0–29.9 "Very Cheap"** band → **BUY — Full position 6–8%** (Phase 03 action table). No change in action category from 07-29; the underlying Quality Score softened modestly on margin/tax drift while the Valuation Score remains floored and the expected-return case, if anything, strengthened (higher TTM FCF, lower net debt, wider gap to a refreshed and higher blended FV).

## 9. Fair Value & Order Setup (BUY action — full setup required)

### Order setup
```
Margin of Safety = 17.5% (midpoint, 15–20% band for Score 0.0–29.9)
Buy Price (ceiling) = $403.79 × (1 − 0.175) = $333.13
Live price $244.30 is far below the ceiling → ENTER NOW (effective entry = live price)
Primary Sell Target = Blended FV = $403.79
Bull-Case Trim Target = Bull DCF $685.32 × 0.90 = $616.79
Stop Loss = Live Price × (1 − 0.225) = $244.30 × 0.775 = $189.33   (22.5%, midpoint of 20–25% band)
R/R = (403.79 − 244.30) / (244.30 − 189.33) = 159.49 / 54.97 = 2.90 : 1   (≥ 2:1 ✓ — improved vs. 07-29's 2.18:1, since price fell while blended FV rose)
```

### Position sizing — top-up toward the partial-fill target
```
Portfolio Value (combined, holdings.md last sync 2026-09-06) = $62,135.17
Max $ Risk (1.5%) = $932.03
Risk/share = $54.97
Risk-based size = 932.03 / 54.97 = 16.96 shares
Allocation cap (6–8% band): 6% → 15.26 sh | 8% → 20.35 sh — risk-based size (16.96) sits inside the cap band, so it governs
Full target (rounded down, conservative) = 16 shares
Held = 10 shares (unchanged — 2026-09-06 IBKR sync confirms no ADBE share-count change) → TOP-UP = 6 shares
Top-up cost = 6 × $244.30 = $1,465.80
Resulting position = 16 × $244.30 = $3,908.80 = 6.29% of the $62,135.17 combined portfolio
```
**Cap cross-check:** 6.29% sits inside the 6–8% Very Cheap band and far under the 15% hard cap (Upgrade 7).

### Order Setup Checklist
```
[x] Composite Score (Quality 83.3 + Valuation 0.0):  8.4   (≤ 49.9 ✓)
[x] Expected annual return E / catalyst window:      +49.14% / 2 yr
[x] Upside/Downside Modifier applied:                −15.0
[x] DCF Fair Value (PW):                             $471.91
[x] Multiples-Based Fair Value:                      $358.38
[x] Blended Fair Value:                              $403.79
[x] Margin of Safety %:                              17.5%
[x] BUY PRICE (ceiling; live already far below):     $333.13
[x] PRIMARY SELL TARGET:                             $403.79
[x] BULL-CASE TRIM TARGET:                            $616.79
[x] STOP LOSS:                                        $189.33
[x] Risk/Reward Ratio:                                2.90:1  (≥ 2:1 ✓)
[x] Max $ Risk:                                       $932.03
[x] POSITION SIZE (top-up shares):                    6 (to reach a 16-sh target)
[x] POSITION SIZE ($):                                $1,465.80 top-up → 6.29% total
[x] Thesis invalidation triggers:                     see §10
```

## 10. Action, Thesis Status & Recommendation

**Recommendation: CONFIRMED BUY — top up 6 shares (~$1,466, to reach a 16-share / 6.29% target). Composite Score 8.4 ("Very Cheap").**

Adobe's Q3 FY2026 print confirms the thesis rather than breaking it: revenue accelerated to +12.9% YoY on an already-large base, both Customer Groups grew double digits, AI-first ARR grew >150% YoY, and Adobe crossed 1 billion monthly active users. Full-year revenue and EPS guidance were **raised**, not cut. The stock's post-earnings decline (−1.82% after-hours, on top of a broader pullback since 07-29) reflects a Q4 guide that landed in-line with — rather than above — the top of consensus, not a fundamental deterioration; per strategy.md's Phase 06 exclusions, "a single guidance cut with a clearly identified one-off cause" isn't a valid exit reason, and this isn't even a guidance cut. Quality Score softened modestly (83.9→83.3) on real but non-threatening margin/tax drift (§4) — still comfortably clears the 80.0 gate. The newly-found CEO transition (§3.5) is a genuine forward-looking item to monitor, not yet evidence of thesis breakage. Combined with a still-floored Valuation Score and a refreshed, wider gap to a higher blended fair value, the Composite Score (8.4) remains deep in the Very Cheap / Full-position band.

**Thesis invalidation triggers (Phase 06 / stop), updated:**
- Creative & Marketing Professionals subscription revenue growth decelerates toward mid-single-digits without a non-AI one-off cause (2 consecutive quarters) → thesis broken
- Gross margin falls >3pp structurally, or FCF/NI conversion <70% for 2 consecutive quarters
- Net debt/EBITDA rising materially on debt-funded buybacks while growth slows
- Evidence (post Dec-1 CEO transition) that Creative Cloud investment/priority is being deprioritized relative to the Experience/orchestration side of the business
- Price through the $189.33 stop

All final-decision authority rests with the human investor; funding is the investor's call.

## 11. Watchlist & stale-score disposition

- **Watchlist:** a new dated entry ([watchlist/in-portfolio/ADBE/ADBE-2026-09-11.md](../watchlist/in-portfolio/ADBE/ADBE-2026-09-11.md)) created — both the Quality Score (83.9→83.3) and Composite Score (8.1→8.4) changed, and this session carries two independent Rule 9 triggers (earnings + a CEO-transition management change), so a new dated file is warranted on multiple, independently sufficient grounds per [watchlist/README.md](../watchlist/README.md).
- **Stale-score mark:** ADBE does not appear in [watchlist/STALE.md](../watchlist/STALE.md) (cleared 2026-07-04) — nothing to clear this session.

## 12. Next review trigger

- **Q4 FY2026 earnings (~mid-December 2026)** — mandatory re-score (Rule 9). Check **Creative & Marketing Professionals** subscription revenue growth (Adobe's new segment-reporting successor to "Digital Media") holds ≥~10%, and whether guidance is delivered vs. the freshly-raised FY2026 targets.
- **CEO transition effective 2026-12-01** (Anil Chakravarthy) and **David Wadhwani's departure effective 2026-09-27** — explicit follow-up per §3.5: re-review moat/segment evidence once these actually take effect, not just on announcement. A permanent CFO appointment remains separately open (interim since 2026-06-15).
- **>15% unexplained move from $244.30** in either direction — immediate re-score (Rule 9).
- **If the top-up is executed**, log it in [decisions/](../decisions/) and reflect it at the next `/sync-portfolio` (holdings.md is handled by the orchestrator, not this session).

## 13. Glossary

- **8-K:** the SEC "current report" filed within days of a material event (earnings, management change, etc.).
- **After-hours trading:** trading after the regular US session closes but before the next day's open — a genuine, live traded price, used here as the Rule 0 price of record since it's the most current print available.
- **ARR (Annual Recurring Revenue):** the annualized run-rate of subscription/recurring revenue.
- **CAGR:** Compound Annual Growth Rate.
- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50.
- **DCF:** Discounted Cash Flow — a valuation method projecting future cash and discounting it to present value.
- **D&A:** Depreciation & Amortization.
- **EBIT / EBITDA:** operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **Effective tax rate:** actual tax paid ÷ pretax income, distinct from the statutory rate.
- **EPS:** Earnings Per Share.
- **EV / EV/EBIT:** Enterprise Value (market cap + net debt) / EV divided by EBIT, a valuation multiple.
- **EY (Earnings Yield):** 1 ÷ Forward PE, compared against the 10-Year Treasury yield.
- **Fast Grower:** a company growing EPS >15%/yr for 3+ years — triggers the PEG sub-score.
- **FCF / FCF Yield / FCF/NI conversion ratio:** Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality).
- **Forward PE:** price ÷ next year's expected EPS.
- **FV / PW Fair Value:** Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear).
- **GAAP:** Generally Accepted Accounting Principles — the standard US accounting rulebook this framework scores off of.
- **Goodwill impairment:** a non-cash write-down of a prior acquisition's goodwill when its expected profitability no longer supports the price paid.
- **Gross Margin / Net Margin / Operating Margin:** Gross Profit, Net Income, and Operating Income each divided by Revenue.
- **Hard disqualifier:** one of three Quality Score conditions that fails a company regardless of weighted score.
- **Hurdle rate:** the minimum acceptable annual return (10% in this framework).
- **Invested Capital:** the total capital (debt + equity) at work in a business — the ROIC denominator.
- **Item 5.02 (Form 8-K):** the SEC 8-K disclosure item for a director/officer departure, election, or appointment.
- **MAU (Monthly Active Users):** unique users engaging with a product at least once in a given month.
- **Moat:** a durable competitive advantage protecting a business's profits.
- **MoS (Margin of Safety):** the discount below fair value demanded before buying.
- **Net Debt/EBITDA:** a leverage ratio; this framework's primary balance-sheet-risk gate.
- **Non-GAAP:** a company's own adjusted presentation of a financial measure, excluded from this framework's scoring (which uses GAAP).
- **NOPAT:** Net Operating Profit After Tax — EBIT × (1 − effective tax rate).
- **PE (Price-to-Earnings) ratio / PEG ratio:** price ÷ earnings; PE ÷ growth rate.
- **pp (percentage points):** a direct difference between two percentages.
- **Quality Score:** this framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02.
- **Rate Environment Gate / Rate Regime Modifier:** the pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive Treasury-yield-band adjustment.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss); this framework requires ≥2:1.
- **ROIC:** Return on Invested Capital — NOPAT ÷ Invested Capital.
- **RPO / cRPO:** Remaining Performance Obligations (total contracted-not-yet-recognized revenue) and current RPO (the 12-month portion).
- **Shareholder yield:** dividend yield plus net buyback yield.
- **TAM:** Total Addressable Market.
- **Terminal Value:** the lump-sum value assigned to all DCF cash flows beyond the explicit forecast period.
- **Treasury yield (10Y):** the US government's 10-year borrowing rate, this framework's risk-free-rate benchmark.
- **TTM:** Trailing Twelve Months.
- **Upside/Downside Modifier:** an additive ±15 valuation-score adjustment based on expected annual return.
- **WACC:** Weighted Average Cost of Capital — the discount rate used in a DCF.

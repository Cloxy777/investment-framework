# RESCORE — DUOL (Duolingo, Inc.) — 2026-08-06

**Task type:** RESCORE (mode `--both`)
**Date:** 06 Aug 2026
**10Y US Treasury Yield:** 4.63% — FRED `DGS10`, most recent published daily close (2026-08-04), cross-checked against ycharts.com ("10 Year Treasury Rate is at 4.63%... compared to 4.63% the previous market day," dated 2026-08-05) — both agree on a stable 4.63% over the last two sessions.
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current DUOL portfolio weight:** 8.05% per [holdings.md](../portfolio/holdings.md) (as of the 2026-08-02 combined IBKR+Freedom24 sync) — flagged as likely modestly stale post-earnings-drop (DUOL's own price fell ~9% intraday today, which mechanically lowers its share of the combined portfolio; a precise updated weight requires the next `/sync-portfolio` pass, out of scope for this rescore). IBKR-only position value today: 30 shares × $123.42 = $3,702.60.
**Sector:** Technology — Education Software (EdTech / Language Learning)
**Last review:** 04 Jul 2026 (Valuation Score 56.6, Quality Score 83.8, Composite Score 36.4).

**Why this session fired:** Hourly `/telegram-scan` (Routine 6) flagged a new post on the bolshegold channel (#9922, ~14:11 UTC 2026-08-06) reporting DUOL Q2 FY2026 earnings. Per the last watchlist entry's own Next Review Trigger, DUOL's Q2 FY2026 print is a **mandatory Rule 9 re-score**. Per this repo's Rule 0, the Telegram post's figures were treated as a pointer only, never as verified data — every number below was independently pulled from DUOL's actual SEC 8-K/shareholder-letter filing (primary source) and cross-checked against secondary aggregators. **Where the post's numbers are cited below, it is explicitly to show whether they matched (they did, closely) — not because they were relied upon.**

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$123.42** | IBKR `get_price_snapshot` (contract_id 505002183), real-time last trade, intraday 2026-08-06 16:16 UTC. Bid $123.29 / Ask $123.52. Cross-checked: (1) IBKR `get_account_positions` `market_price` for the 30-share position = $123.40 (agrees to $0.02); (2) Yahoo Finance quote page `currentPrice` = $122.86 (fetched same session, ~0.5% lower, consistent with normal intraday movement during a volatile post-earnings session); (3) stockanalysis.com = $123.71 (down 8.58%). All three independent sources agree within ~0.7% of each other. |
| Today's move | **−8.79%** (change −$11.90) per IBKR `change` field. Independently corroborated by multiple news sources: Invezz ("Duolingo stock sinks 15% as Q3 revenue forecast misses expectations" — headline figure, likely measured from a different intraday reference point), StockStory/FinancialContent ("stock drops 12%"), Yahoo Finance ("stock drops... weak revenue guidance overshadowing a solid earnings beat"). The exact percentage varies by source/timing, but the direction and driver (Q2 beat, Q3 guide miss) are consistent across all of them. |
| 52-week range | $87.89 – $468.00 | IBKR `misc_statistics`, matches stockanalysis.com exactly. `high_13w`/`high_26w` both $143.80 — confirms the $468 high is >26 weeks stale (pre-selloff peak), consistent with prior sessions. |
| Analyst consensus PT | mean **$121.24**, n=24, rating "Hold" | stockanalysis.com, refreshed today (2026-08-06) post-earnings. **Notably now very close to (slightly below) live price** — a big change from the 07-04 session, where the stock traded meaningfully *above* consensus ($125.76 vs $106.31 mean, +18%). Today's gap has essentially closed (live $123.42 vs mean PT $121.24, −1.8%), reflecting sell-side PTs cut in reaction to today's Q3 guide alongside the price drop itself. |

**No price-inference shortcuts taken** — live price fetched first per Rule 0, before any valuation math.

---

## 2. Data Gathered — Sources & Gaps

**Rule 9 trigger confirmed:** DUOL reported Q2 FY2026 results after the close 2026-08-05 (Form 8-K, accession 0001628280-26-053299, filed with the SEC 2026-08-05; shareholder letter Exhibit 99.2). This is a new quarter since the 07-04 review (which used TTM Q2 FY2025–Q1 FY2026) — full re-score required, not just a price check.

### Tooling note

`yfinance` was **non-functional this session** — every call (`t.info`, `t.quarterly_financials`) failed with `SSLError('Failed to perform, curl: (35) Recv failure: Connection reset by peer')` through the environment's egress proxy, even after pointing `CURL_CA_BUNDLE`/`SSL_CERT_FILE`/`REQUESTS_CA_BUNDLE` at the proxy's CA bundle — this is a connection-reset, not a cert-trust failure, so the standard proxy fixes didn't apply. **Worked around entirely via direct SEC EDGAR XBRL `companyconcept` API calls** (`data.sec.gov/api/xbrl/companyconcept/CIK0001562088/us-gaap/<tag>.json`), which is a *more* authoritative source than `yfinance` for these figures (the primary filed data itself, not a third-party vendor's re-derivation) — cross-checked against stockanalysis.com and the shareholder letter's own stated figures throughout. No metric was invented or estimated; every figure below traces to a specific SEC XBRL fact (with its exact `val`/`start`/`end`/`form` tuple) or a direct quote from the filed shareholder letter.

### ⚠️ Major data-integrity finding — likely GAAP vs. non-GAAP EPS mismatch across vendor "Forward PE" fields

This session hit a materially worse version of the Forward-PE instability flagged in the 06-20 and 07-04 sessions. Three vendors, queried within the same hour, gave three very different "Forward PE" readings:

| Source | Forward PE | Implied forward EPS (at ~$123 price) |
|---|---|---|
| Yahoo Finance (quote page) | 19.96× | ~$6.16 |
| stockanalysis.com (quote page) | 46.81× | ~$2.64 (quarterly-annualized basis, inconsistent with its own forecast page) |
| stockanalysis.com (forecast page, FY2026 consensus) | — | $6.69 |
| marketbeat.com (earnings page) | 48.16× (trailing), FY2027 estimate cited | $3.18 (FY2027), $4.18 implied FY2026 |

**Sanity check that resolves this:** DUOL's actual filed H1 FY2026 GAAP diluted EPS = $0.89 (Q1) + $0.66 (Q2) = **$1.55**. A full-year estimate of $6.69 (stockanalysis) would require H2 EPS of **$5.14** — a ~3.3× acceleration from H1's pace, which is not consistent with the company's own FY2026 guidance (16.3% revenue growth, 26.5% adjusted EBITDA margin — no such acceleration is guided). By contrast, marketbeat's FY2026 estimate (~$4.18, or the ~$2.81 "current year" figure cited in its growth-rate sentence) implies an H2 GAAP EPS in the $1.30–2.60 range — a plausible, moderate deceleration-consistent continuation of H1's pace. **This strongly suggests the higher figures (Yahoo, stockanalysis) are non-GAAP/adjusted EPS estimates (which strip out DUOL's large stock-based compensation expense, ~$150M/yr ÷ ~50M shares ≈ $3/share) being mislabeled or displayed alongside a GAAP live price** — exactly the kind of vendor-field mismatch this framework's Rule 6 and PEG "clean earnings" provisions exist to catch. **Independent corroboration:** this session's own Rule-6-normalized TTM EPS (see §3 below), built entirely from primary-source SEC data, computes to **$3.08/share** — close to marketbeat's figures and nowhere near Yahoo/stockanalysis's $6+ figures.

**Resolution applied this session:** because this ambiguity is directly outcome-determinative for the Upside/Downside Modifier (shown in §6 to swing the action band), Method B of the fair-value triangulation (§9) uses **EV/EBIT scenario multiples** instead of a P/E-based scenario ladder — TTM EBIT is an unambiguous, filed GAAP figure, sidestepping the disputed forward-EPS-consensus question entirely. The Rate Environment Gate's Step 1 test (§4) is shown to fail under *every* candidate forward-PE reading (19.96×, 38.81×, 46.81×, 48.16×) — so that conclusion is robust regardless of which one is "correct." Full sensitivity shown in §6 and §9.

### Standard inputs (TTM = Q3 FY2025–Q2 FY2026, the four most recently completed quarters; sourced directly from SEC XBRL `companyconcept` facts, each cross-checked against a second independent figure where possible)

| Metric | Value | Derivation / cross-check |
|---|---|---|
| TTM Revenue | $1,145,002,000 | Q3FY25 $271,713K + Q4FY25 $282,868K (FY2025 annual $1,037,589K − 9mo $754,721K) + Q1FY26 $291,967K + Q2FY26 $298,454K. Q2 FY26 figure matches the Telegram post's $298.45M exactly, and stockanalysis.com's $298.45M. |
| TTM Gross Profit | $832,616,000 (72.72% margin) | Q3FY25 $196,911K + Q4FY25 $205,869K (FY25 $749,457K − 9mo $543,588K) + Q1FY26 $213,096K + Q2FY26 $216,740K |
| TTM EBIT (Operating Income) | $157,085,000 | Q3FY25 $35,159K + Q4FY25 $43,454K (FY25 $135,570K − 9mo $92,116K) + Q1FY26 $44,527K + Q2FY26 $33,945K |
| TTM D&A | $15,799,000 | Q3FY25 $3,553K + Q4FY25 $3,808K + Q1FY26 $4,191K + Q2FY26 $4,247K (all derived from `DepreciationDepletionAndAmortization` cumulative-period subtraction, cross-checked: Q2FY26's $4,247K independently matches the shareholder letter's own Adjusted EBITDA reconciliation line item exactly) |
| TTM EBITDA (EBIT+D&A) | $172,884,000 | Computed |
| TTM FCF | $397,504,000 | Built quarter-by-quarter as (OCF − PP&E capex − capitalized software), all three components pulled from SEC XBRL: Q3FY25 $77,357K + Q4FY25 $93,731K + Q1FY26 $147,786K + Q2FY26 $78,630K. **Q2 FY26's $78,630K independently reconciles exactly to the shareholder letter's own stated FCF ($78.6M)** — strong validation of the derivation method for the other three quarters. |
| TTM Net Income (GAAP, actual) | $410,767,000 | Q3FY25 $292,195K + Q4FY25 $41,954K + Q1FY26 $43,460K + Q2FY26 $33,158K — all reconcile exactly against SEC `NetIncomeLoss` facts |
| ⚠️ TTM Net Income (normalized, see below) | **$153,919,689** | See Rule 6 normalization, next section |
| "Total Debt" (operating lease liability, noncurrent, 2026-06-30) | $86,136,000 | SEC XBRL `OperatingLeaseLiabilityNoncurrent`. **Confirms a hypothesis from prior sessions**: the 07-04 session's "Total Debt $91,873,000" (sourced from Yahoo's `totalDebt` field) turns out to be exactly the *same* concept at the prior quarter-end (`OperatingLeaseLiabilityNoncurrent` at 2026-03-31 = $91,873,000, confirmed via this session's own XBRL query) — i.e., DUOL carries **zero conventional interest-bearing debt** (confirmed: `LongTermDebtNoncurrent` XBRL concept returns 404 / not reported), and every prior session's "Total Debt" figure was actually the noncurrent operating-lease liability, consistent with Rule 6's instruction to include lease liabilities as debt-like. Carried forward with the same convention (noncurrent portion only, matching precedent) for comparability. |
| Cash & Cash Equivalents (2026-06-30) | $1,180,887,000 | SEC XBRL `CashAndCashEquivalentsAtCarryingValue`, exact match to shareholder letter |
| Net Debt | **−$1,094,751,000** (net cash) | $86,136,000 − $1,180,887,000 |
| Total Stockholders' Equity (2026-06-30) | $1,409,742,000 | SEC XBRL `StockholdersEquity`, exact match to shareholder letter |
| Diluted weighted-avg shares (Q2 FY2026) | 50,031,000 | SEC XBRL `WeightedAverageNumberOfDilutedSharesOutstanding`, form 10-Q. Check: $33,158K NI ÷ 50,031K shares = $0.6628 ≈ **$0.66** reported diluted EPS — reconciles. |
| Revenue 3yr CAGR (FY2022→FY2025) | 41.08% | Unchanged from 07-04 (no new completed fiscal year since) |
| Beta | 0.88 | Yahoo, unchanged |
| Dividend | None | DUOL pays no dividend |
| Q2 FY2026 share repurchases | $44.4M (~432K shares); YTD-through-8/1 $71.9M (~708K shares) | Shareholder letter — **matches the Telegram post's "$44M/quarter" figure closely (confirmed, not merely assumed)** |

### Rule 6 normalization — the recurring DUOL tax-valuation-allowance distortion (still in the TTM window)

Q3 FY2025 (Jul–Sep 2025) still carries the same **$245,746,000 non-cash tax benefit** flagged in every prior DUOL session (pretax income only $46,449,000, tax provision **−$245,746,000**, inflating that quarter's net income to $292,195,000). Because TTM now rolls Q3FY25→Q2FY26, this one-off is still inside the window. Per Rule 6, this session normalizes it out: the other three "clean" quarters' own effective tax rates (Q4FY25 23.02%, Q1FY26 21.77%, Q2FY26 26.91% — averaging **23.90%**) are applied to Q3FY25's pretax income instead of its actual (benefit-inflated) provision:

```
Normalized Q3FY25 tax = $46,449,000 × 23.90% = $11,101,311
Normalized Q3FY25 NI  = $46,449,000 − $11,101,311 = $35,347,689

TTM Normalized NI = $35,347,689 (Q3FY25, normalized) + $41,954,000 (Q4FY25) + $43,460,000 (Q1FY26) + $33,158,000 (Q2FY26)
                   = $153,919,689
Normalized Net Margin = $153,919,689 / $1,145,002,000 = 13.44%   (vs. 35.87% GAAP-actual)
```

This normalized figure ($3.08/share on 50.031M diluted shares) is also the independent cross-check that resolved the Forward-PE GAAP/non-GAAP ambiguity flagged above.

### Qualitative context — DAU / bookings / gross-margin checkpoints (per the 07-04 session's Next Review Trigger), cited to primary sources

The 07-04 watchlist entry set three specific checkpoints for this earnings print. All three are checked against the actual filed results (SEC 8-K Exhibit 99.2, shareholder letter, filed 2026-08-05):

| Checkpoint (from 07-04 session) | Guided | **Actual (Q2 FY2026)** | Result |
|---|---|---|---|
| DAU YoY growth ~20% guided floor | ~20% for rest of 2026 | **23%** (58.7M DAUs) — an *acceleration* from Q1's 21%, not a continuation of the 40%→30%→21% deceleration trend | ✅ **Beat.** Management: "product changes (The Green Machine), expanded influencer/performance marketing, and a one-time June Streak Revival campaign (15.4M streaks revived)... two of these are permanent, we expect DAU growth to remain above 20% for the rest of the year." |
| Bookings growth ~6% guided trough (Q2 2026) | ~6% | **8%** YoY reported (6% constant-currency — the guided figure was explicitly a cc figure) | ✅ **Met/beat** on the cc basis the guide was framed on. Subscription bookings specifically grew 10% YoY. |
| Gross margin trending to ~69% by year-end, flag if >3pp overshoot | ~69% (per 07-04's citation of the Q1 call) | **Guide revised UP**: "gross margin of approximately 71.0% in Q3 and approximately 71.6% for the full year... better than the trajectory we outlined on our Q1 call based on AI cost trends" | ✅ **Improved vs. the risk flagged last session** — the compression that was feared (71%→69%, ~2pp) did not materialize; the updated full-year guide (71.6%) is barely below TTM actual (72.72%), a <1.1pp step, well inside the 3pp flag threshold. |

**Net read: all three checkpoints came in at or better than guided**, and the "AI-disruption bear case" flagged as the risk to watch in 07-04 did not validate on any of these dimensions. The market's negative reaction today is driven specifically by the **Q3 FY2026 forward guide** (revenue growth guided to 11.1% YoY vs. Q2's actual 18.3%; full-year revenue growth guide 16.3% vs. FY2025's actual 38.7%) — a **real, company-guided, multi-quarter deceleration in monetization growth rates**, distinct from and in tension with the *positive* DAU/bookings/margin checkpoint results above. Both sides are shown; neither is smoothed over.

**China / AI competitive-risk claim (from the Telegram post) — checked against the primary source:** the shareholder letter's only "China" mention is in the marketing section (influencer-driven social impressions in China/Indonesia/India). The earnings-call transcript (via secondary summary, primary SEC transcript not independently accessible this session) attributes a portion of the DAU beat specifically to expanded marketing in China, and quotes CEO Luis von Ahn on regulatory compliance: **"Chinese law requires the use of local AI models, and Duolingo complies,"** while acknowledging "broader regulatory risks exist beyond the company's control." This substantiates the post's "China AI risks" framing as a real, disclosed topic (regulatory/compliance risk around AI model localization law), though the primary materials frame it as a compliance matter rather than an imminent threat — the post's framing runs somewhat ahead of what the primary source itself emphasizes. **FCF guidance:** the post's ">$375M for the year" figure is **confirmed** — the company's own FY2026 guidance explicitly states "free cash flow above $375 million" (independently corroborated by StockStory and a secondary earnings-call summary; not located verbatim in the directly-fetched shareholder letter text, which may reflect an extraction gap in that fetch rather than the guidance being absent).

**No metric was invented or estimated where hard figures existed;** every number above traces to a specific SEC XBRL fact, a directly quoted shareholder-letter figure, or a disclosed, reasoned modeling assumption (flagged as such).

---

## 3. Quality Score

**Hard disqualifier check (rolling-window basis per the 2026-08-05 clarification in [quality-scoring.md](../framework/quality-scoring.md) — tested against the current window, FY2023–FY2025, unchanged since no new fiscal year has completed since 07-04):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | FY2023 870%, FY2024 298%, FY2025 87.1% (all GAAP-actual, unchanged from 07-04) | disqualify if <70% for 2+ yrs w/o growth-capex explanation | ✅ PASS |
| Net Debt/EBITDA over threshold? | **−6.33×** (net cash) | disqualify if >2.5× (standard) | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2022 $43.5M, FY2023 $139.9M, FY2024 $264.4M, FY2025 $360.4M — all positive (FY2026 also tracking strongly positive TTM, $397.5M) | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight)

```
Net Margin (TTM, Rule-6 normalized) = $153,919,689 / $1,145,002,000 = 13.44%
NetMargin_Component = clamp((13.44/30)×100, 0, 100) = 44.8

ROIC — NOPAT ÷ Net Invested Capital:
  TTM pretax income = $46,449K + $54,501K + $55,552K + $45,366K = $201,868,000
  Blended normalized tax rate = 1 − ($153,919,689 / $201,868,000) = 1 − 0.7625 = 23.75%
  NOPAT = EBIT (TTM) $157,085,000 × (1 − 23.75%) = $119,777,313
  Net Invested Capital = Total Debt $86,136,000 + Total Equity $1,409,742,000 − Cash $1,180,887,000
                        = $314,991,000
  ROIC = $119,777,313 / $314,991,000 = 38.03%
ROIC_Component = clamp((38.03/30)×100, 0, 100) = 100.0 (capped)

Profitability_Score = (44.8 + 100.0) / 2 = 72.4
```
No FCF-positivity cap (FCF-positive 4+ consecutive years).

### Margins (15% weight)

```
GrossMargin_Score = clamp((72.72/80)×100, 0, 100) = 90.9
```
No structural-trend bonus (already far above the 40% threshold the bonus targets). The guided FY2026 full-year margin (71.6%) sits <1.1pp below TTM actual — not a compression flag (see checkpoint table, §2).

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022→FY2025) = 41.08% (unchanged, no new completed FY)
Growth_Score = clamp((41.08/25)×100, 0, 100) = 100.0 (capped)
```

**Modifier — both directions of evidence shown, per "no black box":**
- *Positive, fresh this session:* DAU YoY growth **accelerated** 21%→23% (Q1→Q2 FY2026), beating the guided ~20% floor; bookings growth beat its guided trough; two of the three drivers behind the DAU beat are described by management as "permanent."
- *Negative, reaffirmed this session:* full-year revenue growth is guided to **16.3%** (down from FY2025's actual 38.7%), and Q3 revenue growth is specifically guided to **11.1%** (down from Q2's actual 18.3%) — a real, company-quantified, multi-quarter deceleration in the *monetization* growth rate, distinct from the (accelerating) *user* growth rate. This is the same structural, management-guided fade documented in the 07-04 session, now reaffirmed with a fresh, more specific near-term (Q3) data point, and is the proximate cause of today's stock decline.

Since Growth_Score is already saturated at the 100.0 cap before any modifier (same situation as 07-04), only a *negative* modifier has real effect. The structural monetization-growth deceleration is judged the more decision-relevant, quantified, and company-guided of the two signals for this sub-score's purpose (a multi-year top-line growth trajectory), so the same **−10** applied in 07-04 is carried forward:
```
Growth_Score = clamp(100.0 − 10, 0, 100) = 90.0
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA = −$1,094,751,000 / $172,884,000 = −6.33×
BalanceSheet_Score = clamp(100×(1 − (−6.33)/4), 0, 100) = clamp(258.3, 0, 100) = 100.0
```
Standard /4 denominator (Upgrade 5 asset-light override doesn't apply). Deeply net-cash — confirmed this session that DUOL carries **zero conventional debt** (see §2's flagged finding); the "debt" in this ratio is purely the operating-lease liability.

### Moat Signal (15% weight)

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | DAU 58.7M (+23% YoY), MAU 140.6M (+10% YoY), paid subscribers 12.7M (+17% YoY) — Q2 FY2026 shareholder letter (SEC 8-K, filed 2026-08-05). Same softer-evidentiary caveat as prior sessions (company's own reported figures, not an independent third-party share tracker). |
| Brand premium | FALSE | No cited pricing-power evidence found this session (unchanged). |
| Network effect | FALSE | No documented two-sided-marketplace mechanism (unchanged). |
| Switching costs | **TRUE** | Streak/XP/League gamification lock-in (unchanged mechanism, still documented in this quarter's own coverage of the Streak Revival campaign's efficacy — 15.4M streaks revived by one campaign is itself evidence users value their accumulated streak history). |
| Scale cost advantage | **TRUE** | Company's own stated driver of this quarter's gross-margin beat: "AI cost trends" enabling lower per-unit content-generation cost as the company scales AI feature delivery — shareholder letter, 2026-08-05. |

```
Moat_Score = (3/5) × 100 = 60.0
```

### FCF Quality (10% weight)

```
FCF/NI (TTM, GAAP-actual) = $397,504,000 / $410,767,000 = 96.77%
FCFQuality_Score = clamp(((0.9677 − 0.40)/0.60)×100, 0, 100) = 94.6
```

### Quality Score — Final

```
Quality Score = (72.4×0.25) + (90.9×0.15) + (90.0×0.20) + (100.0×0.15) + (60.0×0.15) + (94.6×0.10)
              = 18.10 + 13.635 + 18.00 + 15.00 + 9.00 + 9.46
              = 83.195 → rounds to 83.2
```

**Quality Score = 83.2 — clears the 80.0+ gate** (down modestly from 83.8 in 07-04, still comfortably clear; the small drop is mainly the lower normalized net margin this TTM window vs. last, partially offset by a slightly higher FCF-quality read). **No Phase 04 Quality Watch escalation** — nowhere near the 80.0 floor.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test.** Given this session's flagged Forward-PE data-quality problem (§2), the test is shown against **every candidate reading** found this session:

| Forward PE source | EY = 1/PE | Spread vs. 4.63% 10Y | Step 1 result |
|---|---|---|---|
| Yahoo (19.96×) | 5.01% | **+0.38%, still <1.5%** | FAIL |
| stockanalysis FY26 EPS-implied (46.81×) | 2.14% | −2.49% | FAIL |
| marketbeat FY2027 (38.81×, off $3.18) | 2.58% | −2.05% | FAIL |
| marketbeat "current"/FY26 (48.16×) | 2.08% | −2.55% | FAIL |

**Every candidate fails Step 1** — the conclusion is robust to which specific number is used. Adopting the Yahoo figure (per this ticker's established sourcing convention, per fair-value-methodology.md's earlier sessions), Spread = 5.01% − 4.63% = **+0.38% < +1.5% → FAILS → +5 additive.**

**Step 2 — Rate Regime Modifier.** 10Y = 4.63% → 3.5–5% bracket → **+5**

**Combined Rate Modifier: +10** (Step 1 now fails, vs. passing in 07-04 — a direct consequence of the Forward-PE basis flip discussed in §2, not a change in the underlying rate environment, which is essentially flat: 4.63% vs 4.485% in 07-04.)

---

## 5. Valuation Score (Phase 02)

### FCF Yield (40% weight)

```
Market Cap = $123.42 × 50,031,000 diluted shares = $6,174,826,020
FCF Yield  = $397,504,000 / $6,174,826,020 = 6.4377%
FCF_Score  = clamp(100×(1 − 6.4377/10), 0, 100) = 35.62
```
No Owner Earnings adjustment (Upgrade 1) — DUOL's capex remains immaterial (~1.7% of TTM revenue: $28.8M PP&E+software capex ÷ $1,145.0M revenue) and DUOL isn't among the named moat-building-reinvestment companies.

### EV/EBIT (weight 25% base, redistributed to 40% — see PEG below)

```
EV = Market Cap $6,174,826,020 + Net Debt (−$1,094,751,000) = $5,080,075,020
EV/EBIT = $5,080,075,020 / $157,085,000 = 32.34×
EV/EBIT_Score = clamp((32.34 − 12)/23 × 100, 0, 100) = 88.43
```

### Forward PE + Historical PE Modifier (20% weight)

**No-history fallback applied — same conclusion as every prior DUOL session.** `yfinance`'s `get_earnings_dates()`-based 5yr-PE-series reconstruction (the method that worked for other tickers) could not be re-attempted this session due to the `yfinance` tooling failure (§2) — but the 07-04 session already established this is a **structural, ticker-specific data-depth limitation** (Yahoo's `quarterlyDilutedEPS` timeseries returns only 5 quarters for DUOL regardless of requested range, tied to its short public history and GAAP-loss years 2021–2022), independent of any one session's tooling — so the same fallback is applied with high confidence it would recur even with working tooling:
```
FwdPE_Score = 50.0 (neutral midpoint, flagged)
```

### PEG (15% weight) — Fast-Grower eligibility ruling re-verified, not just assumed

Re-checked against fresh data: DUOL's quarterly GAAP EPS series (Q1FY25 $0.72, Q2FY25 $0.91, **Q3FY25 $5.95 (tax-distorted)**, Q4FY25 $0.88, Q1FY26 $0.89, Q2FY26 $0.66) still contains the same one-off distortion inside any trailing-3yr window, and DUOL's public history (IPO July 2021) still doesn't reach 3 full years of clean, non-distorted EPS. **Ruling from [decisions/2026-06-20-framework-clarification-peg-clean-earnings.md](../decisions/2026-06-20-framework-clarification-peg-clean-earnings.md) still applies — not a Fast Grower for PEG purposes. PEG's 15% weight is redistributed to EV/EBIT (→ 40%).**

### Raw Weighted Score

```
Raw = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
    = (35.62 × 0.40) + (88.43 × 0.40) + (50.0 × 0.20)
    = 14.249 + 35.373 + 10.00
    = 59.62
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

**Methodology note (see §2's flagged finding):** this session builds the scenario fair-value ladder off **EV/EBIT** (an unambiguous, filed GAAP multiple) rather than a P/E ladder off the disputed forward-EPS consensus — a legitimate Method B choice explicitly sanctioned by [fair-value-methodology.md](../framework/fair-value-methodology.md)'s multiples table ("EV/EBIT | Standard quality check"), adopted specifically because the P/E-based version proved outcome-determinative and unreliable this session (shown as a disclosed sensitivity below).

**Step 1 — scenario fair values (EV/EBIT basis).** DUOL's current actual EV/EBIT is 32.34× (computed §5) — used as the anchor for the Base case:

| Scenario | Wt | EV/EBIT multiple | Assumption | EV ($M) | Equity Value ($M) | FV/share |
|---|---|---|---|---|---|---|
| Bull | 25% | 40× | Re-rating as DAU reacceleration converts to monetization, AI-disruption fear fades further | $6,283.4 | $7,378.2 | **$147.47** |
| Base | 50% | 32.34× (= today's actual) | Guided FY2026 trajectory plays out as described (Q3 deceleration materializes, DAU stays >20%, margin ~71.6%); multiple holds | $5,080.1 | $6,174.8 | **$123.42** (= live price, by construction) |
| Bear | 25% | 18× | Monetization deceleration proves deeper/more durable than guided, multiple compresses toward a more conservative growth-stock level | $2,827.5 | $3,922.3 | **$78.40** |

```
PW Fair Value = 0.25×147.47 + 0.50×123.42 + 0.25×78.40 = $118.18
Gap Upside % = 118.18 / 123.42 − 1 = −4.25%   (a negative gap — this method reads DUOL as modestly rich on current EV/EBIT)
```

**⚠️ Disclosed sensitivity — the P/E-based alternative this session set aside:** using Yahoo's forward-PE-implied EPS ($6.1554) with a parallel Bull/Base/Bear multiple ladder (30×/19.96×/10×) gives PW FV ≈ $126.34, Gap ≈ **+2.4%** — a small *positive* read, the opposite sign from the EV/EBIT method. Using stockanalysis's FY2026 EPS ($6.69, already flagged in §2 as likely implausible given verified H1 actuals) gives Gap ≈ **+6.9%**. The **sign and magnitude of the expected-return gap is genuinely unstable across methodologies this session** — flagged prominently rather than picking whichever is most flattering. The EV/EBIT method is adopted as primary because it doesn't require resolving the GAAP/non-GAAP ambiguity; see §9 for how the final action conclusion holds up across all three.

**Step 2 — catalyst & annualization (Rule 10).** Same multi-quarter guided-checkpoint framework as 07-04 (DAU >20%, Q3 revenue growth 11.1%, FY26 bookings +10.9%, gross margin ~71.6% — all now with specific, quantified, checkable near-term targets set by management just yesterday). Default **2-year (24-month)** catalyst window retained (Rule 10 upper bound) — satisfies Guardrail 1.
```
Annualized gap = −4.25% / 2 = −2.12%
```

**Step 3 — expected annual return E.**
```
E = annualized gap (−2.12%)
  + intrinsic growth (8%, judgment — set below the FY2026 revenue-growth guide (16.3%) and roughly midway
    to the FCF-growth guide (>$375M vs. FY2025's $360.4M actual = +4.1%), reflecting the guided
    margin/monetization deceleration; more conservative than 07-04's 10% given today's incrementally
    more cautious Q3 signal)
  + shareholder yield (−1%, judgment — Q2 FY2026 saw a real, documented $44.4M buyback (~432K shares,
    matching the Telegram post's cited pace) yet diluted weighted-average share count still ROSE
    48,987,000→50,031,000 quarter-over-quarter (+2.1% in one quarter) — SBC-driven issuance is outpacing
    the buyback more clearly than the "flat" read in 07-04; set mildly negative rather than 0% to reflect
    this session's stronger dilution evidence)
  = −2.12 + 8.0 − 1.0 = 4.88%
```

**Step 4 — map E to M** (hurdle H = 10%):
```
0 ≤ E (4.88%) < H → M = +5 × (10 − 4.88)/10 = +5 × 0.512 = +2.56
```
**Upside/Downside Modifier M = +2.56.**

---

## 7. Final Valuation Score

```
Final Score = Raw Weighted (59.62) + Rate Modifier (+10) + Upside/Downside Modifier (+2.56)
            = 72.18 → rounds to 72.2
```

**Valuation Score = 72.2 — "Trim 25–30%" band on a standalone basis** (70.0–79.9), a full band worse than 07-04's 56.6 ("Fair Value"). **Disclosed sensitivity:** using the alternative P/E-based Upside/Downside methodology (§6) instead gives Final ≈ 70.0 (still Trim-band, at its very boundary); using stockanalysis's likely-implausible FY26 EPS gives Final ≈ 68.2 (Hold band). **Two of three methodologies land in the Trim band; the third (discounted in §2 as internally inconsistent with verified actuals) lands just inside Hold.** This raw-score read is superseded by the Composite Score below, per the framework's own instruction to act on Composite once a Quality Score exists — shown next.

---

## 8. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 83.2) + 0.50 × 72.2
                = 0.50 × 16.8 + 36.10
                = 8.40 + 36.10
                = 44.50 → 44.5
```

**Composite Score = 44.5 — "Cheap" band** (30.0–49.9), nominally in the same action band as 07-04 (36.4), though the underlying mix shifted: the raw Valuation Score got materially worse (56.6→72.2) while the Quality Score barely moved (83.8→83.2) — the strong Quality Score is doing more of the work pulling the blend down this session. **Sensitivity check:** even using the most conservative disclosed Valuation Score alternative (68.2, Hold-band standalone), Composite = 0.50×16.8+0.50×68.2 = 8.40+34.10 = **42.5** — still comfortably inside the same 30.0–49.9 band. **The Composite-Score action band is robust across all three Valuation Score sensitivities this session**, even though the exact number moves by ~2 points.

---

## 9. Action Recommendation & Order Setup

Composite Score 44.5 falls in the **30.0–49.9 "Cheap" → Standard position 3–5%** band — nominally BUY-eligible on score alone. Per the operating brief, the full order setup is run below for transparency, as it was in 07-04, even though independent gates block any actual add (shown below).

**Sizing context:** DUOL's most-recently-recorded weight (8.05%, per holdings.md as of 2026-08-02, likely modestly overstated post-earnings-drop per §1's flag) is more than **1.6× the top of the "Cheap" band's 3–5% target range** even before adjusting downward for today's price move. There is no sizing gap to fill regardless of the exact current-day weight.

### Fair Value — two methods, triangulated (Rule 1: Tech/Growth sector → DCF primary, multiples secondary)

**Method A — 3-Stage DCF (Rule 2).**
```
WACC build:
  Cost of equity = Rf (4.63%) + Beta (0.88) × ERP (5.0%, assumed) = 9.03%
  Cost of debt (pretax, assumed — DUOL carries no conventional debt, only an operating-lease liability;
    same modeling convention as 07-04) = 5.0%; after-tax (21%) = 3.95%
  Weights: E/(D+E) = 98.62% (Market Cap $6,174.83M), D/(D+E) = 1.38% (lease liability $86.14M)
  WACC = 98.62%×9.03% + 1.38%×3.95% = 8.906% + 0.054% = 8.96%

Stage 1 (yrs 1–5), FCF Year 1 = $375M (company's own guided FY2026 FCF floor, ">$375M" — confirmed
  primary-source guidance, used conservatively as the floor rather than assuming a beat), taper
  12%→12%→10%→10%:
  y1 $375.0M | y2 +12% $420.0M | y3 +12% $470.4M | y4 +10% $517.4M | y5 +10% $569.2M

Stage 2 (yrs 6–10), fade from 8.5% to the 2.5% terminal rate:
  y6 +8.5% $617.6M | y7 +7.0% $660.8M | y8 +5.5% $697.1M | y9 +4.0% $725.0M | y10 +2.5% $743.2M

Terminal Value (at y10) = $743.2M × 1.025 / (0.0896 − 0.025) = $11,792.4M
Terminal Value as % of total DCF value = 58.6% (under the 75% Rule 4 sanity cap)

Sum of discounted FCFs (yrs 1–10, at 8.96% WACC) = $3,530.1M
PV of Terminal Value = $4,996.0M
Enterprise Value (DCF) = $8,526.1M
Equity Value = $8,526.1M + Net Cash $1,094.8M = $9,620.9M
DCF Fair Value / share = $9,620.9M / 50,031,000 = $192.30
```

**⚠️ Flagged (same finding as 07-04): DUOL's low Beta (0.88) drives a low ~8.96% WACC**, which combined with a durable double-digit FCF growth assumption over 10 years produces a DCF value well above both the current price and the Method B multiples read. This tension between a low-beta input and DUOL's actual realized volatility (an 8.79% single-day move today, on top of an 80%+ 52-week range) is disclosed again, not resolved by quietly lowering the DCF.

**Method B — Scenario-weighted EV/EBIT multiples (the same PW Fair Value used for the Upside/Downside Modifier, §6):** **$118.18**

```
Triangulation (Rule 3, Tech/Growth weights): Blended FV = 40% × DCF + 60% × Multiples
                                            = 0.40 × $192.30 + 0.60 × $118.18
                                            = $76.92 + $70.91
                                            = $147.83
```

### Order Setup Checklist

```
[✓] Composite Score (incl. Quality blend):    44.5 — "Cheap" (30.0–49.9 band)
[✓] Expected annual return E / catalyst:      +4.88% / 2yr default (feeds the Upside/Downside Modifier, §6)
[✓] Upside/Downside Modifier applied:         +2.56
[✓] DCF Fair Value:                           $192.30
[✓] Multiples-Based Fair Value (EV/EBIT):     $118.18
[✓] Blended Fair Value:                       $147.83
[ ] Margin of Safety %:                       25–30% (Composite 30.0–49.9 band)
    Buy Price range: $103.48 (30% MoS) – $110.87 (25% MoS); midpoint (27.5%) = $107.18
[✓] PRIMARY SELL TARGET:                      $147.83 (Blended FV, baseline)
[✓] BULL-CASE TRIM TARGET:                    $147.47 × 0.90 = $132.72
[ ] STOP LOSS: 25–30% max loss from Buy Price
    At midpoint Buy Price $107.18 → Stop $77.71 (27.5%)
[✗] Risk/Reward Ratio: ($147.83 − $107.18) / ($107.18 − $77.71) = $40.65 / $29.47 = 1.38:1
    Checked across the full 25–30% MoS range (1.33:1 at 25% MoS to 1.43:1 at 30% MoS) — fails the
    2:1 minimum throughout, the same conclusion as 07-04's session despite this session's very
    different intermediate numbers.
```

**Per fair-value-methodology.md Step 6: R/R fails the minimum 2:1 threshold across the entire applicable MoS range. No order is placed** — independently confirms the sizing-gate conclusion above.

### Net Action: **HOLD** — maintain the current 30-share IBKR / combined ~8% position as-is

- **No trim:** Composite Score (44.5) is far below any Phase 05 trim threshold (70.0+) — even though the *raw* Valuation Score alone (72.2) nominally sits in the Trim band, the framework is explicit that the Composite Score, not the raw Valuation Score, governs the action table once a Quality Score is on file. DUOL's strong Quality Score (83.2) pulls the blend back down.
- **No add:** two independent gates block it — (1) R/R fails 2:1 at every point in the applicable MoS range, and (2) the position already exceeds the Composite-Score-implied 3–5% target size by a wide margin.
- **This session's action-conclusion robustness check:** across all three disclosed Valuation Score sensitivities (72.2 primary / 70.0 / 68.2), the resulting Composite Score stays in the 42.5–44.5 range, entirely inside the 30.0–49.9 band — so **HOLD is the robust conclusion regardless of which Forward-PE/EPS methodology is "correct."** This robustness matters given how unusually unstable this session's underlying inputs were (§2, §6).
- **No exit trigger:** margins are not structurally broken (72.72% TTM, guided 71.6% FY — an improvement vs. the risk flagged last session, not a deterioration), ROIC (38.03%) is far above WACC (8.96%), balance sheet is pristine net cash with zero conventional debt, no dilutive raise, no covenant breach.

---

## 10. Next Review Trigger

**Date/event:** DUOL's Q3 FY2026 earnings release (expected ~early November 2026, based on the established cadence) — mandatory Rule 9 re-score. Specific checkpoints to verify against **this session's** guided figures: **Q3 revenue growth ~11.1% YoY** (the guide that drove today's selloff — a miss below this would validate the bear case; an in-line-or-better print would suggest today's reaction was overdone), **DAU growth remaining above 20%** (management's own reaffirmed floor, with two of the three Q2 drivers described as "permanent" — a slide back toward the 21% Q1 level or below would be the clearest sign of thesis erosion), **gross margin ~71.0% in Q3** (confirm the improved trajectory holds), and whether the **buyback pace ($44M/quarter demonstrated) begins to net-offset dilution** (weighted-average diluted share count has risen for multiple consecutive quarters despite real buyback dollars — watch for this to finally flatten or reverse). Also standard triggers: any further guidance revision, management change, M&A, or a >15% unexplained price move from $123.42 in either direction (today's own 8.79% move shows this remains a live possibility).

---

## Glossary

- **Adjusted EBITDA**: A non-GAAP profitability measure (EBITDA further adjusted for items like stock-based compensation) — DUOL's Q2 2026 Adjusted EBITDA was $77.3M (25.9% margin); used for context, not scored directly.
- **Beta**: A stock's sensitivity to overall market moves; used as an input to estimate DUOL's cost of equity in the DCF's WACC. Flagged again this session as being in tension with DUOL's realized volatility (an 8.79% single-day move today).
- **Bookings**: The total value of subscription/purchase commitments made by customers in a period (as distinct from "revenue," which recognizes that value over time) — a leading indicator the framework tracks alongside revenue.
- **bps / pp**: Basis points (0.01 percentage points) / percentage points.
- **CAGR**: Compound Annual Growth Rate.
- **Catalyst window**: The timeframe within which a documented event is expected to close the price/fair-value gap — required before the Upside/Downside Modifier can credit large expected upside.
- **Composite Score**: This framework's blended 0.0–100.0 ranking number — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only after a company clears the 80.0+ Quality Score gate. Governs the action table over the raw Valuation Score once both exist.
- **DAU (Daily Active Users)**: Duolingo's primary growth KPI. Accelerated to 23% YoY this quarter, beating its own guided ~20% floor — a key positive finding this session.
- **DCF (Discounted Cash Flow)**: A valuation method estimating a company's worth today by projecting future cash flows and discounting them back to the present.
- **Deferred tax valuation allowance release**: A one-off GAAP accounting event reversing a prior write-down on deferred tax assets, producing artificially low effective tax and inflated net income — the recurring DUOL distortion (Q3 FY2025) normalized out again this session per Rule 6.
- **Dual-class shares**: A capital structure with two+ classes of common stock with different voting rights — flagged in prior DUOL sessions; this session uses diluted weighted-average shares (combining all classes) sourced directly from SEC XBRL, avoiding the Class-A-only vendor-field trap documented previously.
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **Equity Risk Premium (ERP)**: The extra return equity investors demand over the risk-free rate — an assumed DCF input, not a fetched fact.
- **EPS**: Earnings Per Share. This session found a likely GAAP-vs-non-GAAP mismatch across vendor "forward EPS" figures — a major flagged finding (§2).
- **EV**: Enterprise Value — market cap + debt − cash.
- **EV/EBIT**: Enterprise Value ÷ EBIT, a valuation multiple independent of capital structure; used as this session's primary Method B basis specifically to sidestep the forward-EPS ambiguity.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against bond yields in the Rate Environment Gate.
- **Fast Grower**: Peter Lynch's term for EPS growth >15%/yr for 3+ years on a clean earnings base — DUOL re-confirmed this session as not qualifying (PEG not scored).
- **FCF (Free Cash Flow)**: Cash generated after running and maintaining the business.
- **FCF Yield**: FCF ÷ Market Cap — higher is cheaper.
- **FCF/NI conversion ratio**: FCF ÷ Net Income — a cash-quality check.
- **Forward PE**: Price ÷ next fiscal year's expected EPS. Highly unstable across data vendors for DUOL this session — see the flagged finding in §2.
- **FV (Fair Value)**: The analyst's estimate of intrinsic worth, independent of market price.
- **GAAP**: Generally Accepted Accounting Principles — the standard, audited basis for reported financials, as distinct from "non-GAAP"/"adjusted" figures companies and vendors sometimes report alongside them.
- **Gross Margin**: Gross Profit ÷ Revenue.
- **Hard disqualifier**: A Quality Score condition that fails a company regardless of its weighted score.
- **Hurdle rate**: The minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against.
- **Invested Capital**: The capital (debt + equity, net of cash here) put to work in a business — the denominator of ROIC.
- **IRR**: Internal Rate of Return.
- **MAU (Monthly Active Users)**: A broader user-engagement metric than DAU; DUOL's MAU grew 10% YoY to 140.6M this quarter.
- **Moat**: A durable competitive advantage protecting a business's profits from competitors.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set.
- **Net Debt/EBITDA**: A leverage ratio — this framework's primary balance-sheet-risk gate. DUOL's is deeply negative (net cash) and the company was confirmed this session to carry zero conventional interest-bearing debt.
- **Net Margin**: Net Income ÷ Revenue.
- **NI**: Net Income.
- **NOPAT (Net Operating Profit After Tax)**: EBIT × (1 − effective tax rate) — the numerator of ROIC here.
- **PEG ratio**: PE ÷ earnings growth rate.
- **PT (Price Target)**: An analyst's price forecast. DUOL's consensus PT ($121.24) has converged very close to the live price this session, unlike 07-04's wide gap.
- **PW (Probability-Weighted) Fair Value**: This framework's blended fair value — 25% bull + 50% base + 25% bear.
- **Quality Score**: This framework's 0.0–100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. DUOL's Quality Score (83.2) clears the gate comfortably.
- **Rate Environment Gate / Rate Regime Modifier**: The mandatory pre-score check comparing Earnings Yield against the 10-Year Treasury, and the resulting additive score adjustment.
- **R/R (Risk/Reward ratio)**: Expected gain ÷ expected loss on a trade; this framework requires ≥2:1 to enter.
- **ROIC**: Return on Invested Capital.
- **Rule 0 / Rule 6 / Rule 9 / Rule 10**: This framework's standing instructions to always fetch a live price first; normalize distorted earnings before valuing; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline.
- **SBC (Stock-Based Compensation)**: Non-cash employee compensation expensed under GAAP but added back in non-GAAP/adjusted metrics — the likely explanation for this session's flagged GAAP-vs-non-GAAP forward-EPS mismatch.
- **TAM**: Total Addressable Market.
- **Terminal Value**: The lump-sum value assigned to all DCF cash flows beyond the explicit forecast period.
- **TTM**: Trailing Twelve Months.
- **Upside/Downside Modifier (Expected-Return Modifier)**: The additive ±15 adjustment based on expected annual return vs. the 10% hurdle.
- **Valuation Score**: This framework's 0.0–100.0 score (lower = cheaper) combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.
- **WACC**: Weighted Average Cost of Capital — the DCF discount rate.
- **XBRL**: eXtensible Business Reporting Language — the structured data format the SEC requires for filed financial statements, queried directly this session via `data.sec.gov`'s API as the primary source for every hard number above.

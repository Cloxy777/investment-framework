# NEW POSITION — WMT (Walmart Inc., NYSE) — 2026-08-16

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 2026-08-16 (Sunday)
**10Y US Treasury Yield:** 4.51% (U.S. Treasury daily par-yield-curve rates page, most recent posted trading day 2026-08-14 — FRED's `DGS10` CSV endpoint was unreachable this session, see §7 Data Gaps; recorded for completeness only, since this session stops before the Rate Environment Gate would apply — see §4)
**Rate Regime Modifier (would apply, not applied):** 3.5–5% bracket → +5
**Current WMT portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/WMT/` or `watchlist/not-in-portfolio/WMT/`, confirmed before this session started)
**Sector:** Consumer Staples / Discount & Department Store Retail
**First-use jargon decode:** see closing Glossary (§8)

---

## 0. Why this session exists — trigger source

A post on **bolshegold** (Telegram, post bolshegold/9986, 2026-08-16T09:37:07 UTC) previewing the upcoming earnings-reporting week named WMT alongside HD: *"$HD, $WMT - можно посмотреть, но лето, season-adjusted будет норм, плюс минус. По другим данным, потребление приросло из года в год, так что норм"* ("$HD, $WMT — worth a look, but it's summer, season-adjusted should be fine either way. Other data shows consumption grew year-over-year, so it's fine"). Per the operating brief and this repo's standing convention (see the 2026-08-14 RDDT and 2026-07-19 DOCU precedent sessions), **a first-ever mention of a name with no watchlist entry triggers a full `/new-position` evaluation regardless of the mention's substance.** WMT has no existing watchlist entry and is not a current holding (confirmed above), so this session is that evaluation, built entirely from independently, primary-sourced data. **The Telegram post's text is not used as a financial input anywhere below** — it is only the reason this session exists. (A parallel session evaluates HD separately from the same trigger post; not referenced further here.)

Independently confirmed context (not a scored input): Walmart's Q2 FY2027 earnings (quarter ended 2026-07-31) are scheduled for **2026-08-20** per stockanalysis.com's tracked consensus date — i.e. "this week" relative to the trigger post, consistent with its framing.

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("WMT")`: contract_id **13824**, exchange **NASDAQ**, description "WALMART INC" — the correct primary US listing (DE/MX/CA cross-listings and unrelated tickers like WMTI/WMTN/WMTS were returned but not used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$115.34** | IBKR `get_price_snapshot`, `last` field, contract_id 13824 (NASDAQ) |
| Bid / Ask | Not returned in this snapshot request | — |
| Change vs. prior close | −$0.38 (−0.33%) | IBKR `get_price_snapshot` |
| Prior close | $115.72 | IBKR `get_price_snapshot` |
| 52-week high / low | $135.155 / $95.031 | IBKR `misc_statistics` |
| 26-week / 13-week high | $135.155 | IBKR `misc_statistics` |
| 13-week low | $106.79 | IBKR `misc_statistics` |
| Day volume | ~14.52M shares | IBKR `get_price_snapshot` |

**Cross-check:** stockanalysis.com's live snapshot (fetched same session, Aug 14 close) showed price $115.27, market cap $917.33B — consistent with the $115.34 IBKR figure (no material divergence; the two are 5 hours/one session apart). No unexplained >15% move — WMT is trading well within its 52-week range, near the middle.

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

`yfinance` was **not attempted** this session, per the documented environment failure in prior sessions (e.g. 2026-07-19 DOCU, 2026-08-14 RDDT) — went straight to the established fallback: **SEC EDGAR XBRL `companyfacts` API** (CIK **0000104169**, primary source, directly filed figures) for every quantitative Quality Score input, cross-checked against **stockanalysis.com**'s independently-computed TTM figures (matched to the dollar — see §2.2) and against Walmart's own SEC filings (10-K filed 2026-03-13 covering FY2026 ended 2026-01-31; 10-Q filed ~2026-06 covering Q1 FY2027 ended 2026-04-30; the FY2026 Q4 earnings release, 8-K Ex-99.1 filed 2026-02-19; and the Q1 FY2027 earnings release, 8-K Ex-99.1 filed 2026-05-21) for qualitative Growth/Moat evidence and the growth-capex explanation discussed in §3.7.

### 2.2 Fiscal year convention

**Walmart's fiscal year ends January 31**, not December 31. "FY2026" below covers Feb 1, 2025 – Jan 31, 2026 (the 10-K filed 2026-03-13). All "FY20XX" labels use Walmart's own convention.

### 2.3 Income statement — primary-sourced (SEC XBRL `companyfacts`, USD millions)

| Period | Revenue | Cost of Revenue | Gross Profit | Operating Income (EBIT) | Net Income | Pretax Income | Tax Expense |
|---|---|---|---|---|---|---|---|
| FY2023 (Feb'22–Jan'23) | 611,289 | — | — | — | — | — | — |
| FY2024 (Feb'23–Jan'24) | 648,125 | 490,142 | 157,983 | 27,012 | 15,511 | 21,848 | 5,578 |
| FY2025 (Feb'24–Jan'25) | 680,985 | 511,753 | 169,232 | 29,348 | 19,436 | 26,309 | 6,152 |
| FY2026 (Feb'25–Jan'26) | 713,163 | 535,395 | 177,768 | 29,825 | 21,893 | 29,469 | 7,199 |
| Q1 FY2026 (Feb–Apr'25) | 165,609 | 124,303 | 41,306 | 7,135 | 4,487 | 5,994 | 1,355 |
| Q1 FY2027 (Feb–Apr'26) | 177,751 | 133,058 | 44,693 | 7,493 | 5,330 | 7,148 | 1,658 |

**TTM (May 2025–Apr 2026), computed as FY2026 − Q1 FY2026 + Q1 FY2027:**
```
TTM Revenue          = 713,163 − 165,609 + 177,751 = $725,305M
TTM Cost of Revenue  = 535,395 − 124,303 + 133,058 = $544,150M
TTM Gross Profit     = 725,305 − 544,150            = $181,155M   (24.98% gross margin)
TTM Operating Income = 29,825 − 7,135 + 7,493        = $30,183M   (4.16% operating margin)
TTM Net Income       = 21,893 − 4,487 + 5,330        = $22,736M   (3.13% net margin)
TTM Pretax Income    = 29,469 − 5,994 + 7,148         = $30,623M
TTM Tax Expense      = 7,199 − 1,355 + 1,658          = $7,502M   (24.50% blended effective tax rate)
```
**Cross-check:** stockanalysis.com independently reports WMT's TTM Revenue **$725,305M**, Gross Profit **$181,155M** (24.98% margin), Operating Income **$30,183M**, Net Income **$22,736M** (3.14% margin, rounding) — an **exact match** to this session's own SEC-XBRL-derived TTM computation.

### 2.4 Cash flow — primary-sourced (SEC XBRL)

| Fiscal Year | OCF | CapEx | FCF (OCF−CapEx) | Net Income | FCF/NI |
|---|---|---|---|---|---|
| FY2024 | 35,726 | 20,606 | 15,120 | 15,511 | 97.48% |
| FY2025 | 36,443 | 23,783 | 12,660 | 19,436 | 65.15% |
| FY2026 | 41,565 | 26,642 | 14,923 | 21,893 | 68.16% |
| Q1 FY2026 | 5,411 | 4,986 | 425 | — | — |
| Q1 FY2027 | 4,738 | 6,684 | −1,946 | — | — |

**TTM:**
```
TTM OCF   = 41,565 − 5,411 + 4,738 = $40,892M
TTM CapEx = 26,642 − 4,986 + 6,684 = $28,340M
TTM FCF   = 40,892 − 28,340         = $12,552M
TTM FCF/NI = 12,552 / 22,736         = 55.21%
```
**Depreciation & Amortization (`DepreciationAmortizationAndAccretionNet`, for TTM EBITDA):**
```
TTM D&A = 14,203 − 3,369 + 3,821 = $14,655M
TTM EBITDA = TTM EBIT ($30,183M) + TTM D&A ($14,655M) = $44,838M
```

**FCF positive every year shown** (and every fiscal year on record for Walmart, a multi-decade-profitable retailer) — comfortably clears the "FCF-positive 3+ consecutive years" hard disqualifier with a far longer track record than the 3-year minimum. **However, FY2025 (65.15%) and FY2026 (68.16%) — the two most recently completed fiscal years — both fall below the 70% FCF/NI conversion threshold.** See §3.7 for why this does not fire as a hard disqualifier.

### 2.5 Balance sheet — primary-sourced (most recent 10-Q, quarter ended Apr 30, 2026)

| Item | Apr 30, 2026 |
|---|---|
| Cash and cash equivalents | $10,729M |
| Short-term borrowings | $10,673M |
| Long-term debt, current portion | $3,896M |
| Long-term debt, noncurrent | $36,887M |
| **Total debt** | **$51,456M** |
| Total stockholders' equity (attributable to Walmart) | $94,330M |
| **Total stockholders' equity, incl. noncontrolling interest** | **$100,682M** |
| Shares outstanding (per Q1 FY2027 10-Q cover, dated 2026-05-27) | 7,958,079,155 |

No available-for-sale securities/short-term-investments line material to WMT's balance sheet was found (unlike RDDT's cash-like securities pile) — Net Debt and Invested Capital below use Cash and Cash Equivalents only.

```
Net Debt (Apr 30, 2026) = Total Debt ($51,456M) − Cash ($10,729M) = $40,727M
Net Debt/EBITDA = 40,727 / 44,838 (TTM EBITDA) = 0.908×
```

**Invested Capital convention used this session:** Total Debt + Total Equity **including noncontrolling interest** − Cash (consistent with EV computation below, which also reflects the whole consolidated enterprise, not just the parent-attributable slice):
```
Invested Capital = 51,456 + 100,682 − 10,729 = $141,409M
```

### 2.6 Growth / margin / moat evidence — primary-sourced (FY2026 10-K, Q4 FY2026 & Q1 FY2027 earnings releases)

- **Gross margin structurally expanding, even though below the 40% static threshold:** FY2024 24.37% → FY2025 24.85% → FY2026 24.93% → TTM 24.98% — a consistent, multi-year uptick every period. Company's own Q1 FY2027 earnings release (SEC 8-K, 2026-05-21): *"Gross profit grew 29 bps [Walmart U.S.] with increased contributions from business mix and merchandise mix"* — attributing the trend to a real, disclosed mix shift toward higher-margin lines (advertising, membership, marketplace), not a one-off.
- **Walmart Connect (advertising) — a genuine new, faster-growing monetization line, not just guidance:** Q1 FY2027 earnings release: *"44% increase in Walmart Connect (ex-VIZIO)"*; *"Walmart U.S. advertising up 36%"*; global advertising business *"grew 37% overall"*; International advertising *"grew 32%, driven by continued momentum at Flipkart."*
- **Membership income growing double digits:** *"Membership fee revenue grew 17.4% globally"*; Walmart U.S. *"grew double-digits as net adds reflected a record first quarter high"*; Sam's Club U.S. *"5.6% increase in membership fee revenue due to steady growth in member counts, renewal rates, and Plus members."*
- **E-commerce accelerating:** *"eCommerce sales up 26% globally"* (Walmart U.S. +26%, Sam's Club U.S. +23%, International +27%).
- **Documented market-share evidence:** *"Strong sales, with broad-based share gains, reflecting accelerated customer transactions led by eCommerce growth"* (Q1 FY2027 earnings release).
- **Scale → cost advantage, explicitly disclosed:** FY2026 10-K, Item 1: *"These relationships enable us to obtain pricing that reflects the volume, certainty and cost-effectiveness these arrangements provide to such suppliers, which in turn enables us to provide low prices to our customers."*
- **No pricing-power/ASP (brand premium) evidence found** — the 10-K instead frames the business around **EDLP** (Every Day Low Price), the structural opposite of premium pricing.
- **No specific switching-cost mechanism found** — the 10-K describes Walmart+ membership benefits (free shipping, fuel discounts, Scan & Go) but not an integration-depth/contractual-lock-in/data-migration-cost mechanism this checklist requires.
- **Marketplace/network-effect evidence found but too thin to credit:** the 10-K acknowledges a marketplace model (*"advertising solutions for brands and online marketplace sellers, supply chain and fulfillment capabilities to online marketplace sellers"*) but does not describe an explicit two-sided-dynamics mechanism (more sellers → more buyer value, or vice versa) the way this framework's checklist requires — not credited, conservative reading.
- **Documented growth-capex explanation for the FY2025/FY2026 sub-70% FCF/NI years (§3.7):** FY2026 Q4 earnings release (8-K, 2026-02-19): *"The increase in free cash flow was due to the increase in net cash provided by operating activities described above, partially offset by an increase of $2.9 billion in capital expenditures to support our omnichannel growth strategy."* FY2027 capex guidance: *"approximately 3.5% of net sales."*
- **Revenue growth is not decelerating structurally:** FY24→FY25 +4.8%, FY25→FY26 +4.7%, and the most recent quarter (Q1 FY2027 vs. Q1 FY2026) grew **+7.33%** YoY — an acceleration, not a deceleration, consistent with the accelerating advertising/membership/e-commerce mix above.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF-positive 3+ consecutive years | Positive every fiscal year on record (§2.4) | disqualify if not | ✅ **PASS**, clean |
| Net Debt/EBITDA over threshold | **0.908×** (§2.5) | disqualify if >2.5× standard | ✅ **PASS**, clean |
| FCF/NI conversion <70% for 2+ consecutive years **without** a documented growth-capex explanation | FY2025 65.15% / FY2026 68.16% — both sub-70%, the two most recently completed fiscal years — **but** a documented growth-capex explanation exists (§2.6: FY2026 Q4 earnings release, "$2.9 billion in capital expenditures to support our omnichannel growth strategy") | disqualify if 2+ consecutive years sub-70% **and no such explanation exists** | ✅ **PASS** — explained, does not fire (continuous FCF Quality sub-score in §3.6 still reflects the low ratio) |

**No hard disqualifier fires.**

### 3.2 Profitability (25% weight)

```
Net Margin (TTM) = 22,736 / 725,305 = 3.13%
NetMargin_Component = clamp((3.13/30)×100, 0, 100) = 10.45
```

```
Effective tax rate (TTM) = 7,502 / 30,623 = 24.50%
NOPAT (TTM) = EBIT × (1 − tax rate) = 30,183 × (1 − 0.2450) = $22,788.8M
Invested Capital (Apr 30, 2026) = Total Debt ($51,456M) + Equity incl. NCI ($100,682M) − Cash ($10,729M) = $141,409M
ROIC (TTM) = 22,788.8 / 141,409 = 16.12%
ROIC_Component = clamp((16.12/30)×100, 0, 100) = 53.72
```

```
Profitability_Score = (10.45 + 53.72) / 2 = 32.08   (no FCF-positivity cap — clean, decades-long positive FCF, §3.1)
```

### 3.3 Margins (15% weight)

```
GrossMargin_Score = clamp((24.98/80)×100, 0, 100) = 31.22
```
**+10 structural-trend bonus applies** — gross margin below the 40% static threshold but expanding every year for 3+ years running (24.37% → 24.85% → 24.93% → 24.98%), with a documented, cited driver (§2.6: mix shift toward advertising/membership/marketplace, not a one-off):
```
Margins_Score = clamp(31.22 + 10, 0, 100) = 41.22
```

### 3.4 Growth (20% weight)

```
Revenue 3yr CAGR (FY2023 $611,289M → FY2026 $713,163M) = (713,163/611,289)^(1/3) − 1 = 5.27%
Growth_Score (raw) = clamp((5.27/25)×100, 0, 100) = 21.09
```
**+10 TAM-expansion modifier applies** — documented, *actual* (not guidance) evidence (§2.6): Walmart Connect advertising +44% (ex-VIZIO), global advertising +37%, membership fee revenue +17.4% globally, e-commerce +26% globally, and management's own "broad-based share gains" statement — a real, cited, multi-line acceleration story materially faster than core retail revenue.
```
Growth_Score = clamp(21.09 + 10, 0, 100) = 31.09
```
**No deceleration modifier** — revenue growth is not decelerating structurally; the most recent quarter (Q1 FY2027 vs. Q1 FY2026) grew +7.33% YoY, faster than the FY25→FY26 full-year rate of +4.7% (§2.6).

### 3.5 Balance Sheet (15% weight)

```
Net Debt/EBITDA = 40,727 / 44,838 = 0.908×   (§2.5)
BalanceSheet_Score = clamp(100 × (1 − 0.908/4), 0, 100) = 77.29
```

### 3.6 Moat Signal (15% weight)

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | "Strong sales, with broad-based share gains, reflecting accelerated customer transactions led by eCommerce growth" (Q1 FY2027 earnings release, SEC 8-K 2026-05-21) |
| Brand premium | **FALSE** | No pricing-power/ASP evidence found; the 10-K instead centers the business on **EDLP** (Every Day Low Price) — the structural opposite of a documented brand premium |
| Network effect | **FALSE** | Marketplace model acknowledged in the 10-K but not described with an explicit two-sided-dynamics mechanism this checklist requires — conservative, not credited |
| Switching costs | **FALSE** | Walmart+ membership benefits described (free shipping, fuel discounts, Scan & Go) but no integration-depth/contractual-lock-in/data-migration-cost mechanism found |
| Scale cost advantage | **TRUE** | FY2026 10-K, Item 1: "These relationships enable us to obtain pricing that reflects the volume, certainty and cost-effectiveness these arrangements provide to such suppliers, which in turn enables us to provide low prices to our customers" — a documented scale-to-cost-to-price mechanism |

```
Moat_Score = (2/5) × 100 = 40.0
```

### 3.7 FCF Quality (10% weight)

```
FCF/NI ratio (TTM) = 12,552 / 22,736 = 55.21%
FCFQuality_Score = clamp(((0.5521 − 0.40)/0.60)×100, 0, 100) = 25.35
```
As discussed in §3.1, this low ratio does **not** trigger the hard disqualifier (a documented growth-capex explanation exists), but the continuous score still reflects it in full — the explanation excuses the automatic fail, not the weighted number.

### 3.8 Quality Score — final calculation

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

              = (32.08 × 0.25) + (41.22 × 0.15) + (31.09 × 0.20)
              + (77.29 × 0.15) + (40.0 × 0.15) + (25.35 × 0.10)

              = 8.020 + 6.183 + 6.218 + 11.594 + 6.000 + 2.535

              = 40.55  →  rounds to 40.6
```

### 3.9 Gate result: **FAIL — 40.6 < 80.0**

This is not a knife-edge case — WMT sits **39.4 points below** the strict 80.0+ gate. Even generously crediting both withheld Moat signals (5-of-5, Moat_Score = 100.0 instead of 40.0) would only add `(100.0−40.0)×0.15 = 9.0` points, landing at 49.6 — still nowhere near the gate. No plausible reading of any single contestable input (Moat credit, Invested Capital's equity convention, the trend-bonus judgment call) closes a 39-point gap.

**This session stops here per the command specification: no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.** Walmart does not clear the 80.0+ Quality Score gate.

---

## 4. Why this reads as a genuine, structural miss — not a framework gap

Walmart is a real, profitable, growing, well-run business with a strong balance sheet (Balance Sheet 77.29) and a genuine, documented scale-cost/market-share moat (Moat 40.0, 2-of-5 credited) — but it is fundamentally a **thin-margin, high-volume retailer**, and this framework's Quality Score is built to reward the opposite profile (Buffett/Munger-style high-margin, high-ROIC compounders). Three of six sub-scores are structurally weak for this business model, not because of any one-off issue:

- **Profitability (32.08/100, 25% weight)** — a 3.13% TTM net margin (retail is a low-margin-by-design business) drags the blended Profitability sub-score down hard, even though the underlying ROIC (16.12%) comfortably clears the Phase 01 15% threshold on its own.
- **Margins (41.22/100, 15% weight)** — a ~25% gross margin is inherent to grocery/general-merchandise retail; it is expanding (credited via the +10 trend bonus) but starts from structurally far below the 40% static threshold this sub-score is built around.
- **FCF Quality (25.35/100, 10% weight)** — heavy, disclosed reinvestment into omnichannel/automation capex is currently outrunning net income growth, pulling FCF/NI conversion below 70% for two straight fiscal years (excused from the hard disqualifier, but not from the continuous score).

None of these are data gaps or judgment-call artifacts — they are the accurate, filed-financials-based read of what kind of business Walmart is. A large, well-capitalized, share-gaining retailer with a fast-growing higher-margin advertising/membership overlay is a legitimately good business; it simply is not the kind of >80.0-Quality-Score compounder this framework's strict gate is calibrated to admit. This is the gate doing exactly what it was designed to do (2026-06-29 decision: "deliberately high bar... to be loosened later only if it screens out too much of the investable universe").

---

## 5. Recommendation: **PASS (no entry) — Quality Gate FAIL at 40.6 (need 80.0+)**

**Do not enter WMT this session.** The Quality Score of 40.6 is 39.4 points below the strict 80.0+ gate — not a borderline miss. **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed**, consistent with the command specification's instruction to stop at the Quality Gate. No position opened.

The triggering Telegram post (a routine "worth a look, earnings this week" mention, offering no specific claims about WMT's own fundamentals) was used only as the reason to run this first-ever evaluation and was not relied upon for any figure or conclusion above.

---

## 6. Next Review Trigger

No routine re-check is scheduled on a numeric-score basis (no Phase 02 valuation score exists), but this framework tracks quality-gate misses for re-evaluation on:
- **WMT's Q2 FY2027 earnings** (quarter ended 2026-07-31, expected **2026-08-20** per stockanalysis.com's tracked consensus date — this week, the specific event the triggering Telegram post referenced) — a fresh TTM window could modestly move the Growth, Margins, and FCF Quality sub-scores, particularly if the advertising/membership/e-commerce mix shift continues at its recent pace.
- A **documented change** to a Moat sub-score input — e.g. a specific, citable price-increase/ASP data point (Brand Premium) or an explicit two-sided-marketplace-dynamics disclosure (Network Effect), either of which would need independent sourcing before being credited.
- The standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move (WMT is currently trading well within its 52-week range — no such move to investigate this session).

Absent any of the above, a future Telegram mention of WMT should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Data Gaps Flagged

1. **`yfinance`/Yahoo Finance was not attempted** this session, per the documented environment failure in prior sessions (2026-07-19 DOCU, 2026-08-14 RDDT) — worked around identically: SEC EDGAR XBRL `companyfacts` API as primary source, cross-checked against stockanalysis.com (exact match on every TTM figure checked, §2.3). No financial input was left unsourced as a result — a tooling note, not a data gap in any scored input.
2. **FRED's `DGS10` CSV endpoint (`fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10`) was unreachable this session** — repeated `curl` attempts (both HTTP/2 and forced HTTP/1.1, with retries) returned `HTTP/2 stream ... INTERNAL_ERROR` / "Empty reply from server," and a direct `WebFetch` on the same URL returned an HTTP 403. Worked around by fetching the **U.S. Treasury's own daily par-yield-curve-rates page** directly (home.treasury.gov) — arguably an even more primary source than FRED, which itself republishes Treasury's data — giving 10Y = 4.51% as of the most recent trading day (2026-08-14). A secondary cross-check attempt (cnbc.com/quotes/US10Y) also returned an HTTP 403 via the proxy. **This is recorded for completeness only** — the Rate Environment Gate is never reached this session since the Quality Score gate fails first, so no scored input depends on this figure.
3. **Marketplace/Network-Effect Moat Signal** — Walmart's 10-K acknowledges a marketplace model (third-party sellers, advertising, fulfillment services sold to them) but does not describe an explicit two-sided-dynamics mechanism the way this framework's checklist requires. Not credited, conservative reading (§3.6) — a future session with access to a more detailed marketplace-economics disclosure (seller count growth, GMV, take-rate trend) could revisit this signal, though it would not move the Quality Score anywhere near the 80.0 gate on its own (§3.9).

None of these gaps is silently patched around — each is the explicit reason for a flagged caveat rather than an invented number, and §3.9 shows none of them is remotely outcome-determinative for the gate result (a 39.4-point shortfall).

---

## 8. Glossary

| Term | Meaning |
|---|---|
| **8-K** | Full entry in [glossary.md](../framework/glossary.md). Walmart's Q4 FY2026 (2026-02-19) and Q1 FY2027 (2026-05-21) earnings press releases were both furnished via 8-K Exhibit 99.1 — the source of most qualitative Growth/Moat evidence and the growth-capex explanation in this session (§2.6, §3.1). |
| **10-K / 10-Q** | Full entries in [glossary.md](../framework/glossary.md). Walmart's FY2026 10-K (filed 2026-03-13) and Q1 FY2027 10-Q (most recent quarterly balance sheet, quarter ended Apr 30, 2026) were the primary structured-data sources this session. |
| **bps (basis points)** | Full entry in [glossary.md](../framework/glossary.md). Walmart's Q1 FY2027 earnings release cited a 29 bps (0.29 percentage point) gross-profit-rate improvement for Walmart U.S. (§2.6). |
| **CIK (Central Index Key)** | Full entry in [glossary.md](../framework/glossary.md). Walmart's is 0000104169, used to pull this session's SEC XBRL `companyfacts` data. |
| **EBIT / EBITDA** | Full entries in [glossary.md](../framework/glossary.md). Operating-profit measures used throughout this session's Balance Sheet, Profitability, and legacy-screen calculations. |
| **EDLP (Every Day Low Price)** | Full entry in [glossary.md](../framework/glossary.md) *(new term, added this session)*. Walmart's foundational pricing philosophy — the reason no "Brand premium" Moat Signal evidence was credited (§3.6). |
| **Effective tax rate** | Full entry in [glossary.md](../framework/glossary.md). Used to convert TTM EBIT into NOPAT for this session's ROIC calculation (24.50% TTM, §3.2). |
| **Fiscal Year (Walmart convention)** | Walmart's fiscal year runs Feb 1 – Jan 31; "FY2026" covers Feb 2025–Jan 2026, one year offset from a calendar-year label (§2.2). |
| **Gross Margin** | Full entry in [glossary.md](../framework/glossary.md). One of this session's Quality Score Margins sub-score inputs (24.98% TTM, §3.3). |
| **Hard disqualifier** | Full entry in [glossary.md](../framework/glossary.md). One of three Quality Score conditions that fails a company regardless of weighted score. None fired for WMT this session, though the FCF/NI conversion check came close before being excused by a documented growth-capex explanation (§3.1). |
| **Invested Capital** | Full entry in [glossary.md](../framework/glossary.md). This session computed Walmart's Invested Capital as $141,409M (debt $51,456M + equity incl. NCI $100,682M − cash $10,729M) — see the equity-convention note in §2.5. |
| **Moat Signal** | Full entry in [glossary.md](../framework/glossary.md). WMT credited 2 of 5 signals (market share, scale cost advantage) this session (§3.6). |
| **Net Debt/EBITDA** | Full entry in [glossary.md](../framework/glossary.md). Walmart's ratio is 0.908×, comfortably under the 2.5× standard threshold (§2.5, §3.5). |
| **Net Margin** | Full entry in [glossary.md](../framework/glossary.md). One of this session's Quality Score Profitability sub-score inputs (3.13% TTM, §3.2). |
| **NOPAT (Net Operating Profit After Tax)** | Full entry in [glossary.md](../framework/glossary.md). EBIT × (1 − effective tax rate); the numerator this framework uses to compute ROIC (§3.2). |
| **Omnichannel** | Full entry in [glossary.md](../framework/glossary.md) *(new term, added this session)*. Walmart's own disclosed explanation for its rising capital expenditures — the documented growth-capex explanation that kept the FCF/NI hard disqualifier from firing (§3.1, §2.6). |
| **Quality Score** | Full entry in [glossary.md](../framework/glossary.md). This framework's 0.0–100.0 continuous score grading the Phase 01 criteria; a company must score 80.0+ to proceed to Phase 02 valuation scoring at all. WMT scores 40.6 this session — a clean, non-borderline FAIL. |
| **Rate Environment Gate** | Full entry in [glossary.md](../framework/glossary.md). The Phase 02 pre-check (Earnings Yield Spread Test + Rate Regime Modifier) run before every valuation score; never reached this session since the Quality Score gate fails first. |
| **ROIC (Return on Invested Capital)** | Full entry in [glossary.md](../framework/glossary.md). Walmart's ROIC (16.12% TTM) comfortably clears the Phase 01 15% threshold on its own, even though the blended Profitability sub-score is dragged down by thin net margin (§3.2). |
| **Rule 0** | Full entry in [glossary.md](../framework/glossary.md). This framework's standing instruction to always fetch a live, current price before any valuation work, and never treat a Telegram post's claims as a verified financial input without independent confirmation. |
| **Rule 9** | Full entry in [glossary.md](../framework/glossary.md). This framework's list of fundamental events that force an immediate re-valuation. |
| **Treasury yield (10Y)** | Full entry in [glossary.md](../framework/glossary.md). 4.51% as of 2026-08-14, sourced from the U.S. Treasury's own daily rates page after FRED's CSV endpoint was unreachable (§7). Recorded for completeness only — never used in a scored calculation this session. |
| **TTM (Trailing Twelve Months)** | Full entry in [glossary.md](../framework/glossary.md). This session used May 2025–Apr 2026 (FY2026 minus Q1 FY2026 plus Q1 FY2027), the most recent complete window available. |
| **Walmart Connect** | Full entry in [glossary.md](../framework/glossary.md) *(new term, added this session)*. Walmart's fast-growing (+44% ex-VIZIO) advertising business — the primary evidence behind this session's Growth sub-score TAM-expansion modifier (§2.6, §3.4). |
| **XBRL (eXtensible Business Reporting Language)** | Full entry in [glossary.md](../framework/glossary.md). The structured, machine-readable SEC data format this session's `companyfacts` API pull used. |

---

## Appendix — Informational only: legacy 8-criterion Phase 01 screen

Not the binding gate (quality-scoring.md's graded score supersedes it), shown for template completeness per operating-calendar.md's New Position Evaluation data structure. Market cap/EV use today's live price ($115.34 × 7,958.079M shares outstanding, per the most recent 10-Q cover) — informational only, not a scored Quality Score input (EV/EBIT and FCF Yield are Phase 02 valuation inputs, never reached this session since the Quality Gate fails first, but computed here for completeness):

| Criterion | Threshold | WMT (TTM) | Pass? |
|---|---|---|---|
| Gross margin | >40% | 24.98% | ❌ |
| Net margin | >12% | 3.13% | ❌ |
| ROIC | >15% | 16.12% | ✅ |
| Revenue growth (3yr CAGR) | >8% | 5.27% | ❌ |
| FCF positive 3 consecutive years | required | Yes (decades) | ✅ |
| Net debt/EBITDA | <2.5× | 0.908× | ✅ |
| FCF yield | >4% | 1.37% (FCF $12,552M / Mkt Cap $917,884.8M) | ❌ |
| EV/EBIT | <20× | 31.76× (EV $958,611.8M / EBIT $30,183M) | ❌ |

5 of 8 fail — the same underlying story as the graded score: a large, well-run, share-gaining retailer whose thin-margin, high-volume, richly-valued profile sits well outside this framework's quality-and-cheapness screening criteria as currently calibrated.

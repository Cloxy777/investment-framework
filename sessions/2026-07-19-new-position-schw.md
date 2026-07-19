# New Position Evaluation: SCHW (The Charles Schwab Corporation) — 2026-07-19

**Task type:** NEW POSITION
**Ticker:** SCHW — NYSE, IBKR contract_id 11905
**Company:** The Charles Schwab Corporation — diversified brokerage, wealth management, banking, and asset-custody holding company (Investor Services + Advisor Services segments; primary banking subsidiary Charles Schwab Bank, SSB)
**Analyst:** Claude (automated session)
**10Y US Treasury yield:** Not needed this session — evaluation stops at the Phase 01 Quality Score gate (see Section 2g), before the Rate Environment Gate would otherwise run.
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — [t.me/bolshegold](https://t.me/bolshegold) post 9795, ~09:46 UTC 2026-07-19, naming SCHW among several tickers reporting earnings this week, with commentary that it "serves as a financial-sector marker/economic barometer; no particular forecast given." **The Telegram post is used only as a trigger — no financial data, score, or conclusion below is drawn from the post itself.** SCHW had no existing watchlist entry anywhere in `watchlist/in-portfolio/` or `watchlist/not-in-portfolio/` (confirmed by directory listing) and is not a current holding (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)) — per this repo's established convention (see the CAKE/RYAAY precedent rows in `portfolio/snapshots/telegram-watch.md`), a first-ever mention always triggers a full `/new-position` evaluation regardless of the mention's substance.

---

## 0. Ticker confirmation

`search_contracts("SCHW")` resolves among many Schwab-branded instruments (preferred shares, Schwab-sponsored ETFs/funds, bonds, foreign listings): contract_id **11905**, NYSE, "SCHWAB (CHARLES) CORP" (STK, primary US listing) — not the MEXI/TSE cross-listings, the SCHW-prefixed preferred shares (SCHW PRC/PRD/PRJ), or any of the dozens of Schwab-managed ETFs/funds (SCHD, SCHB, SCHX, SWTSX, etc.) that also match the "SCHW" search string. This is the contract used throughout.

### 0a. Business-model mismatch flagged up front (fourth instance of this framework gap — but with a materially different outcome)

Charles Schwab is a diversified brokerage/wealth-management/banking holding company, and — like JPMorgan (2026-07-14), Citigroup (2026-07-12), and SoFi (2026-06-21) before it — its GAAP income statement has **no genuine Cost-of-Revenue/Gross-Profit line**: total net revenues are already net interest revenue (interest revenue minus interest expense) plus fee income, with nothing to net a gross margin against. This was independently verified this session, not just assumed from precedent: a data-vendor page (stockanalysis.com) displayed a "Cost of Revenue" / "Gross Profit" split, but cross-checking against Schwab's own SEC-filed Consolidated Statements of Income (Q4 2025 and Q1 2026 earnings-release exhibits, fetched directly) showed the vendor's "Cost of Revenue" figure ($6,491M, FY2025) is actually just the "Compensation and benefits" expense line relabeled — not a real GAAP gross-margin concept. Following the established convention from the JPM/C/SOFI sessions (and per this session's task instructions to check that precedent), **Margins and Balance Sheet (Net Debt/EBITDA) are treated as N/M (not computable)** — see Sections 2b/2d.

**However, unlike JPM/C/SOFI, SCHW's actual cash-generation record does not fail the hard disqualifiers.** Free cash flow has been positive every fiscal year 2021 through 2025 (five consecutive years), in contrast to JPM's and Citigroup's deeply negative FY2024/FY2025 operating cash flow (driven by trading-book/loan-portfolio balance changes classified within operating activities). This makes SCHW's Quality Score gate outcome depend on the *weighted score*, not on an outright hard-disqualifier failure — a materially different (and more nuanced) case than the prior three bank/broker sessions. See Section 2g/2h.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Source | Value | Note |
|---|---|---|
| **IBKR live snapshot** (contract_id 11905) | **$102.80** | `is_close: true` — last trade, not a live intraday quote, because markets are closed (2026-07-19 is a Sunday; bid/ask returned empty, confirming no live two-sided quote is available). This is the most recent available price and is used throughout, consistent with Rule 0 ("record intraday price... not a prior-session close" applies when markets are open; on a weekend trigger, the last close is the correct, most-current price available). |
| IBKR `misc_statistics` | 52-week range: **$83.98 – $107.10**; 13-week high **$103.97** | |
| IBKR `dividend_yield` | 1.16% (trailing) | |
| IBKR `bid_ask` | Empty (no live quote — market closed) | |

**$102.80 is used throughout.**

---

## 2. Phase 01 Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

`yfinance` failed in this session's environment with the same `curl_cffi` TLS/connection-reset error documented in the 2026-07-12 (C) and 2026-07-14 (JPM) sessions — reproduced, not resolved. **Fallback used, per established precedent:** WebSearch/WebFetch against Charles Schwab's own SEC-filed earnings-release exhibits (Q4 2025 and Q1 2026 Exhibit 99.1, fetched as PDFs directly from `content.schwab.com`), cross-checked against stockanalysis.com. Every figure below is cited to its specific source; none is invented or estimated.

### 2a. Profitability (25% weight)

**TTM basis** (FY2025 − Q1 2025 + Q1 2026, all GAAP "Total net revenues" and "Net Income" from Schwab's own Consolidated Statements of Income):

```
TTM Net Income = $8,852M (FY2025) − $1,909M (Q1 2025) + $2,479M (Q1 2026) = $9,422M
TTM Revenue    = $23,921M (FY2025) − $5,599M (Q1 2025) + $6,482M (Q1 2026) = $24,804M

TTM Net Margin = 9,422 / 24,804 = 38.0%

NetMargin_Component = clamp((38.0 / 30) × 100, 0, 100) = 100.0   (clamped — above the 30% ceiling)
```

**ROIC proxy: ROE** (per the SOFI/Citigroup/JPM-session bank convention — ROIC's debt+equity invested-capital concept doesn't map cleanly to a brokerage/bank holding company; ROE is the standard substitute). Most recent full fiscal year (FY2025, GAAP): **21%** Return on average common stockholders' equity — officially reported (up from 15% FY2024; Q1 2026 quarterly-annualized was 23%, continuing the improving trend, but FY2025 is used per the established "most recent full fiscal year" convention).

```
ROIC_Component = clamp((21 / 30) × 100, 0, 100) = 70.0

Profitability_Score (raw) = (100.0 + 70.0) / 2 = 85.0
```

**FCF-positive-3-years check (feeds the Profitability cap):** **PASSES** — FCF was positive in every one of the last 5 fiscal years (Section 2e). No cap applied.

```
Profitability_Score = 85.0
```

### 2b. Margins (15% weight) — **N/M, not computable**

Confirmed this session (Section 0a): Schwab's GAAP income statement carries no Cost-of-Revenue/Gross-Profit line — total net revenues already net interest revenue against interest expense, with the remainder being fee/trading/bank-deposit-account income. A vendor-displayed "Cost of Revenue" figure was traced and found to be a mislabeled "Compensation and benefits" expense line, not a genuine gross-margin concept. **Not scored — no number invented.**

### 2c. Growth (20% weight)

```
Revenue 3yr CAGR = (FY2025 Total Net Revenue $23,921M / FY2022 Total Net Revenue $20,762M)^(1/3) − 1 = 4.8%
Growth_Score = clamp((4.8 / 25) × 100, 0, 100) = 19.4
```

(Both figures are GAAP "Total net revenues" from Schwab's own Q4 2025 and prior earnings-release exhibits — not a non-GAAP/adjusted basis.) The modest 3yr figure reflects a real dip in FY2023 (Total net revenues $18,837M, down from FY2022's $20,762M) driven by deposit-sweep-cash outflows and higher funding costs amid the 2023 regional-banking-sector deposit-flight episode — well documented in Schwab's own FY2023 disclosures and widely reported at the time — since fully reversed: FY2024 +4%, FY2025 +22%, Q1 2026 +16% YoY. Using the framework's standard FY-over-FY 3-year lookback (consistent with the JPM/C session convention) captures this dip inside the window; it is not adjusted out, per Rule 6's normalization principle only applying to one-off/non-recurring items, not a genuine multi-quarter revenue decline.

**TAM/pricing-power modifier (+10):** documented evidence — record $11.90 trillion total client assets (+18% YoY, Q4 2025) / $11.77 trillion (+19% YoY, Q1 2026); $519.4 billion FY2025 core net new assets (a 5.1% organic growth rate); Schwab is the **largest RIA custodian**, holding ~54% of the $9.8 trillion total US RIA-custodied asset market (Citywire/AdvizorPro, July 2026); Managed Investing Solutions net inflows +36% (FY2025) / +46% (Q1 2026 YoY); closed the **Forge Global** acquisition (private-markets/pre-IPO trading platform) in early March 2026, expanding into a new asset category; bank loan balances +28-29% YoY; record 46.5 million (Q4 2025) / 47.2 million (Q1 2026) total client accounts. Cited, not inferred.

```
Growth_Score = 19.4 + 10 = 29.4
```

No structural-deceleration evidence found — the opposite (growth reaccelerated after the 2023 dip); no −10 modifier applied.

### 2d. Balance Sheet (15% weight) — **N/M, not computable**

No GAAP EBIT/EBITDA line exists in the framework's standard sense (Section 0a), so Net Debt/EBITDA (including the Upgrade 5 asset-light variant) cannot be computed. **Not scored**, per the same convention applied to JPM, Citigroup, and SoFi.

**Bank/broker-equivalent context (cited, not substituted into the formula):** Consolidated Tier 1 Leverage Ratio 8.9% (Q1 2026, preliminary; down from 9.3% at Q4 2025) — Charles Schwab Bank, SSB subsidiary at 10.9% (Q1 2026, down from 11.1% at Q4 2025); Adjusted Tier 1 Leverage 6.8% consolidated / 7.5% CSB. S&P Global Ratings: **A-** (affirmed). All ratios remain above regulatory minimums, but the sequential quarter-over-quarter decline (9.3%→8.9%) is a real, if modest, capacity-tightening signal worth flagging as context — not a scored input.

### 2e. FCF Quality (10% weight)

```
FY2021 FCF = $1,202M   (positive)
FY2022 FCF = $1,539M   (positive)
FY2023 FCF = $18,887M  (positive — an unusually large inflow, driven by a swing in "Cash and investments segregated" per stockanalysis.com's cash-flow-statement breakdown, consistent with the large deposit/funding shifts of that year)
FY2024 FCF = $2,050M   (positive)
FY2025 FCF = $8,763M   (positive)
```
(Source: stockanalysis.com cash-flow statement, WebFetch 2026-07-19; Operating Cash Flow − CapEx. Cross-checked directionally against Schwab's own Q4 2025/Q1 2026 earnings-release "Capital expenditures" line, which reports quarterly CapEx of $136M–$258M — consistent in magnitude with the annual CapEx figures underlying the FCF figures above.)

```
FY2021 FCF/NI = 1,202 / 5,855   = 20.5%
FY2022 FCF/NI = 1,539 / 7,183   = 21.4%
FY2023 FCF/NI = 18,887 / 5,067  = 372.7%
FY2024 FCF/NI = 2,050 / 5,942   = 34.5%
FY2025 FCF/NI = 8,763 / 8,852   = 99.0%
```

**FCFQuality_Score uses the most recent fiscal year (FY2025), per the same convention as the JPM session:**

```
FCFQuality_Score = clamp(((0.990 − 0.40) / 0.60) × 100, 0, 100) = 98.3
```

**Hard-disqualifier check, shown explicitly (Section 2g) — flagging the FY2021–2022 pattern for transparency:** FY2021 and FY2022 were *both* below the 70% conversion threshold, which is on its face "2+ consecutive years below 70%." However, this is the oldest data in the 5-year window, and the pattern reversed sharply and durably starting FY2023 (372.7%, then 34.5%, then 99.0%) — there is no 2-consecutive-year run below 70% anywhere in the trailing 3 years (FY2023–FY2025), which is the window the JPM/Citigroup sessions actually evaluated (their two most recent fiscal years) when this disqualifier fired for those names. Read as intended — catching an *ongoing* earnings-quality problem (the Valeant/Wirecard pattern this check exists to guard against), not a since-resolved historical episode — **this disqualifier does not fire for SCHW.** This judgment call is flagged explicitly per Rule 0/"show every calculation" rather than silently resolved either way.

### 2f. Moat Signal (15% weight)

| Signal | Evidence | Result |
|---|---|---|
| Market share stable/growing | Largest RIA custodian, ~54% of the $9.8T US RIA-custodied-asset market (Citywire/AdvizorPro, July 2026); record $11.77–11.90T total client assets; 39.1M active brokerage accounts (+6% YoY, Q1 2026) | ✅ TRUE |
| Brand premium | No specific pricing-power citation (price increases without volume loss) sourced this session — "#1 Overall Broker, StockBrokers.com 2026" is a service-quality ranking, not documented pricing-power evidence | ❌ not established |
| Network effect | No documented two-sided-marketplace or user-growth-driven-value mechanism sourced this session | ❌ not established |
| Switching costs | Documented via the 2023 TD Ameritrade-to-Schwab RIA migration itself: $1.3 trillion / 3.6 million accounts / 7,000 RIA firms moved, with reported operational friction (platform/tooling differences, rep-code-to-master-number conversion, some advisor attrition to alternative custodians) — direct evidence that switching a custodial relationship is costly and disruptive, which cuts both ways (into Schwab, and by the same logic, away from it) | ✅ TRUE |
| Scale cost advantage | Only ~6% of pre-2019 revenue came from trading commissions before Schwab cut them to zero (Oct 2019); ~49% of TTM revenue now comes from net interest income, letting Schwab sustain zero-commission trading in a way smaller, commission-dependent competitors (TD Ameritrade, E-Trade) could not — both were absorbed/consolidated (TD Ameritrade acquired by Schwab itself, 2020) shortly after matching the price cut | ✅ TRUE |

```
Moat_Score = (3/5) × 100 = 60.0
```

### 2g. Hard Disqualifiers (checked independently of the weighted formula)

1. **FCF/NI conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation → does NOT fire.** See the explicit reasoning in Section 2e: the only 2-consecutive-year run below 70% is FY2021–2022, fully reversed since FY2023, with no such run anywhere in the trailing 3 fiscal years.
2. **Net Debt/EBITDA over threshold → N/A (no EBITDA exists in this framework's sense for a brokerage/bank holding company — cannot fire or clear; genuinely not computable, see 2d).**
3. **Not FCF-positive for 3+ consecutive years → does NOT fire.** FCF was positive in all 5 of the last 5 fiscal years (Section 2e).

**No hard disqualifiers fire.** This evaluation therefore proceeds to the full weighted Quality Score, unlike the JPM/Citigroup/SoFi sessions (which stopped at this step).

### 2h. Full Quality Score

Margins and Balance Sheet are N/M (Sections 2b, 2d) — 30% of the formula's weight has no real number to plug in. Per the same approach as the JPM session ("illustrative ceiling," shown for transparency, not to invent a false precision), three treatments are shown:

```
Computable components (70% of total weight):
  Profitability × 0.25 = 85.0 × 0.25 = 21.25
  Growth × 0.20         = 29.4 × 0.20 = 5.88
  Moat × 0.15            = 60.0 × 0.15 = 9.00
  FCFQuality × 0.10      = 98.3 × 0.10 = 9.83
  Computable subtotal    = 45.96

Ceiling (N/M components resolved at 100.0 each, most generous possible):
  45.96 + (100.0 × 0.15) + (100.0 × 0.15) = 45.96 + 15.00 + 15.00 = 75.96

Floor (N/M components resolved at 0.0 each, least generous possible):
  45.96 + 0 + 0 = 45.96

Renormalized (weight the 4 computable components to sum to 100%, i.e. divide by 0.70):
  45.96 / 0.70 = 65.66
```

**All three treatments — floor 46.0, renormalized 65.7, and even the most generous possible ceiling 76.0 — land below the 80.0 gate.** Unlike the ambiguity this would otherwise create (which resolution of the N/M components is "correct" isn't documented in quality-scoring.md), the gate outcome here doesn't actually depend on resolving that ambiguity: even assigning both N/M sub-scores their maximum possible value (100.0, implying a hypothetically perfect margin/balance-sheet profile) still caps the score at 75.96, which is below 80.0.

### Gate Result: ❌ **FAIL**

- No hard disqualifiers fire (Section 2g) — a materially different mechanism from JPM/Citigroup/SoFi, whose sessions failed via 2 independent hard disqualifiers each.
- The weighted score fails on its own terms: even the most generous possible ceiling (75.96, treating both N/M components as a perfect 100.0) sits below the 80.0 gate, driven primarily by a modest Growth sub-score (29.4, reflecting the real FY2023 revenue dip) and a Moat Signal that only clears 3 of 5 documented criteria (60.0).
- Per task instructions, **this evaluation stops here — no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.**

---

## 3. Why this reads as a mixed finding — a real (if modest) framework gap, layered on a genuinely mid-tier growth/moat profile

This is the **fourth** brokerage/bank-type name (after SoFi 2026-06-21, Citigroup 2026-07-12, JPMorgan 2026-07-14) to hit the "no Cost-of-Revenue/Gross-Margin line, no clean EBIT/EBITDA" structural gap in this framework's Quality Score — reinforcing that a documented depository-institution/broker carve-out (paralleling Upgrade 5's existing asset-light-financial debt-gate variant) is worth prioritizing as a framework improvement. **Unlike the three prior cases, though, SCHW's FAIL is not a hard-disqualifier outcome** — its underlying cash generation is genuinely strong and consistent (5/5 years FCF-positive, FY2025 FCF/NI conversion 99.0%, TTM net margin 38.0%, ROE 21% and rising). The FAIL instead comes from the combination of (a) the two N/M components capping the best-case ceiling at 75.96 regardless of resolution, and (b) a real, modest Growth sub-score (29.4) reflecting a genuine FY2023 revenue dip (now reversed) and a Moat Signal that only credits 3 of 5 documented signals for lack of citable Brand Premium/Network Effect evidence. This should **not** be read as "Schwab's business is deteriorating" — by every qualitative measure available this session (record client assets, record core net new assets, reaccelerating revenue growth, rising ROE, an "A-" S&P rating, capital ratios above regulatory minimums) the underlying business looks healthy and improving. It is a **quality-gate miss on this framework's specific formula**, not a red flag on the company.

---

## 4. Additional context (not scored — informational only, since Phase 02 was not run)

- **Q1 2026 earnings (16 April 2026, independently sourced — not the Telegram trigger, which concerns *upcoming* Q2 2026 earnings this week):** record $6,482M net revenue (+16% YoY), record $1.37 GAAP diluted EPS (+38% YoY), $2,479M GAAP net income (+30% YoY). Increased the quarterly dividend 19% to $0.32/share. Repurchased 24.3M shares for $2.4B.
- **Capital returns:** FY2025 total capital return $11.8B across dividends and buybacks; $7.3B of FY2025 common stock repurchases; Q1 2026 dividend increase (19%) on top of that.
- **Credit rating:** S&P Global Ratings **A-** (affirmed). Moody's rating not independently re-confirmed this session with a current date (a 2023 stable-outlook affirmation was found in search results, but a current 2026 rating letter was not; flagged as a data gap, not invented).
- **Valuation context (not scored, no Phase 02 run — figures below are pre-earnings-week snapshots, informational only):** market cap ~$176.6B, ~1.74B shares outstanding, book value per share ~$24.44, price/book ~4.16×, trailing PE ~20.2×, forward PE ~15.3×, PEG ~0.80 (source: stockanalysis.com statistics page, WebFetch 2026-07-19 — these would need refreshing against a live price and the upcoming Q2 2026 print before any future Phase 02 work).
- **Sector context for the Telegram trigger:** this channel's 2026-07-19 post named SCHW alongside several other tickers reporting earnings "this week" as a "financial-sector marker" with no directional forecast given — a neutral/informational trigger, not a claim about SCHW's results, consistent with (though distinct in tone from) the same channel's 2026-07-12/07-14 posts that named C/JPM/BAC ahead of their earnings.

---

## 5. Data sourcing note

`yfinance` failed in this session's environment (`curl_cffi` TLS/connection-reset error, same as documented in the 2026-07-12 C and 2026-07-14 JPM sessions). **Fallback used:** WebSearch and WebFetch, with primary figures sourced directly from Charles Schwab's own SEC-filed earnings-release exhibits (Q4 2025 Exhibit 99.1 and Q1 2026 Exhibit 99.1 PDFs, fetched from `content.schwab.com` and read via the PDF reader — not summarized secondhand), cross-checked against stockanalysis.com for statistics-page figures (market cap, PE, PEG, book value) and third-party citations (Citywire/AdvizorPro for RIA custody market share, prior reporting on the 2019 zero-commission cut and 2023 TD Ameritrade migration). IBKR's `get_price_snapshot` (Rule 0 live price) and `search_contracts` worked normally and are unaffected by this gap. Every figure above is cited to its specific source; none is invented or estimated.

---

## 6. Recommendation: **PASS**

**The Phase 01 Quality Score gate fails.** No hard disqualifier fires — a genuinely different (and more favorable) underlying picture than the three prior brokerage/bank sessions — but the weighted score falls short of 80.0 under every possible resolution of the two N/M (Margins, Balance Sheet) components, capping out at 75.96 even in the most generous case. Per [.claude/commands/new-position.md](../.claude/commands/new-position.md), the evaluation stops here — **no Phase 02 valuation score, Composite Score, or fair-value/order-setup work was performed.**

This is the fourth brokerage/bank-type name to surface the same structural Quality Score gap (no Cost-of-Revenue/Gross-Margin line, no clean EBIT/EBITDA), further strengthening the case that a documented depository-institution/broker carve-out is worth prioritizing as a framework improvement — but SCHW's specific FAIL mechanism (a real, if modest, weighted-score shortfall on genuine Growth/Moat sub-scores, not a hard-disqualifier failure) is materially different from JPM/Citigroup/SoFi and should be read on its own terms, not folded into "yet another bank hits the same wall" without qualification. Not resolved within this session (no framework file's formula was edited here) — flagged as a candidate framework-improvement item for a future `decisions/` entry, alongside the three prior bank sessions.

**Not a BUY/TRIM/EXIT outcome** — no position exists or is proposed. Added to the not-in-portfolio watchlist (Section 7), flagged for re-evaluation once (a) a documented depository-institution/broker carve-out exists in Phase 01/02, or (b) a further Rule 9 fundamental trigger fires (this week's Q2 2026 earnings, once released, would itself be the next trigger).

---

## 7. Watchlist entry

See [watchlist/not-in-portfolio/SCHW/SCHW-2026-07-19.md](../watchlist/not-in-portfolio/SCHW/SCHW-2026-07-19.md) — new entry (first time SCHW has been evaluated under this framework).

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Core net new assets (CNNA)** | A brokerage/wealth platform's net client asset inflows (new money in, minus money out) over a period, excluding one-off items like acquisitions/divestitures or a single very large client's extraordinary flow. Charles Schwab gathered $519.4 billion of core net new assets in FY2025 (5.1% organic growth rate). |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization — operating-profit measures that don't exist in standard form for a bank or broker, since interest is a core funding/revenue item rather than a financing add-back. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself; for a bank/broker with an active trading/lending balance sheet, this can swing sharply due to normal changes in client-related balances, not necessarily unprofitability. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score — see [quality-scoring.md](../framework/quality-scoring.md). |
| **Moat** | A durable competitive advantage that protects a business's profits from competitors. |
| **N/M (Not Meaningful)** | This framework's flag for a formula input that genuinely doesn't exist for a given business model, distinct from a mere data gap. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — used to judge whether a fast grower's multiple is justified by its growth rate. |
| **P/B (Price-to-Book)** | Price ÷ book value (accounting net worth) per share. |
| **Quality Score** | This framework's 0.0–100.0 continuous score grading profitability, margins, growth, balance sheet, moat signal, and FCF quality. A company must score 80.0+ to proceed to Phase 02 valuation scoring. See [quality-scoring.md](../framework/quality-scoring.md). |
| **Rate Environment Gate** | The mandatory pre-check (not run in this session, since the Quality Score gate failed first) comparing Earnings Yield against the 10-Year Treasury yield. |
| **RIA (Registered Investment Advisor)** | A fiduciary investment-advisory firm that places client assets with a third-party custodian (e.g. Charles Schwab) rather than holding them directly. Schwab custodies ~54% of the $9.8 trillion US RIA asset market. |
| **ROE** | Return on Equity — Net Income ÷ shareholder equity. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit; not directly meaningful for a bank/broker, so Return on Equity is used as the convention proxy instead. |
| **ROTCE (Return on Tangible Common Equity)** | Net income available to common shareholders divided by average tangible common equity — the primary profitability KPI banks/brokers report and target, typically higher than plain ROE. |
| **Tangible common equity** | Common stockholders' equity minus goodwill and acquired intangible assets — strips out prior-acquisition accounting artifacts. Schwab's average tangible common equity was $23.2B for FY2025, reflecting the 2020 TD Ameritrade acquisition's goodwill/intangibles. |
| **Tier 1 Leverage Ratio** | A bank-regulatory capital-adequacy measure: Tier 1 capital ÷ average total assets (not risk-weighted). Schwab's consolidated ratio was 8.9% at Q1 2026. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |

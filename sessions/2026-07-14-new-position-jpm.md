# New Position Evaluation: JPM (JPMorgan Chase & Co.) — 2026-07-14

**Task type:** NEW POSITION
**Ticker:** JPM — NYSE, IBKR contract_id 1520593
**Company:** JPMorgan Chase & Co. — money-center / universal bank (Consumer & Community Banking, Commercial & Investment Bank, Asset & Wealth Management)
**Analyst:** Claude (automated session)
**Trigger:** This session was triggered by the hourly Telegram Stock-Mention Scan (Routine 6) — [t.me/bolshegold](https://t.me/bolshegold) post bolshegold/9755, ~14:25 UTC 2026-07-14, claiming "$JPM отчитался EPS $7.7 вместо ожиданий $5.72" (JPM reported EPS $7.70 vs. expected $5.72). **The Telegram post is used only as a trigger to evaluate JPM — no financial data, score, or conclusion in this session is drawn from the post itself; every figure below is independently sourced via IBKR, SEC filings, JPMorgan's own investor-relations releases, and third-party aggregators.** As it happens, JPMorgan's own 2Q26 earnings release (also independently sourced below) confirms reported GAAP EPS of $7.70 for the quarter — the Telegram post's headline number is directionally accurate, though the consensus figure it cites ($5.72) does not exactly match any consensus figure found in independent sourcing (~$5.44–$5.59 depending on source); this discrepancy is noted but not investigated further since it doesn't change any input used below. JPM was not previously in `watchlist/` (confirmed — no `watchlist/*/JPM/` folder exists) and is not a current holding (confirmed against [portfolio/holdings.md](../portfolio/holdings.md) — no `JPM` row exists).

---

## 0. Ticker confirmation

`search_contracts("JPM")` resolves unambiguously among many JPMorgan-branded instruments (preferred shares, ETFs, bonds, foreign listings): contract_id **1520593**, NYSE, "JPMORGAN CHASE & CO" (STK, primary US listing). This is the contract used throughout — not the MEXI/TSE cross-listings, the JPM-prefixed preferred shares (JPM PRC/PRD/PRL/etc.), or any of the JPMorgan-managed ETFs (JEPI, JEPQ, JPST, etc.) that also match the "JPM" search string.

### 0a. Business-model mismatch flagged up front (third instance of this framework gap)

JPMorgan Chase is a **money-center / universal bank**, and the framework's Phase 01/02 methodology has **no documented carve-out for banks** beyond Hybrid Upgrade 5's Net Debt/EBITDA asset-light variant (which still presumes an EBITDA line exists). This is the same structural gap first identified in the 2026-06-21 SOFI session and confirmed a second time in the 2026-07-12 Citigroup (C) session — now recurring a third time, on the largest and (by market cap) most valuable bank in the world:
- **No GAAP EBIT/EBITDA line** — interest expense is JPM's core cost of funding (deposits/borrowings), not a financing add-back.
- **Free Cash Flow reads deeply negative in the two most recent fiscal years** — driven mechanically by "changes in trading assets," "securities borrowed," and loan-portfolio balance changes being classified within *operating* cash flow for a bank, not by capex or operating losses.
- **No Cost-of-Revenue / Gross Margin line** — a bank's revenue is net interest income plus noninterest (fee) income, with nothing to net a "gross margin" against.

Every quality-score input below is computed and shown exactly as the framework's documented formula requires; every place the formula doesn't cleanly map to a bank's business model is flagged explicitly rather than silently patched or invented.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Source | Value | Note |
|---|---|---|
| **IBKR live snapshot** (contract_id 1520593) | **$341.56** | Last trade, `is_close: false` — genuine live intraday quote, 2026-07-14 (Tuesday, market open), timestamp 2026-07-14T16:08:08Z |
| IBKR `change` | +$7.03 (+2.10%) vs. prior close | Consistent with a real, positive market reaction to today's 2Q26 earnings beat (Section 2, confirmed independently below) |
| IBKR `misc_statistics` | 52-week range: **$277.68 – $343.34**; 13-week high **$343.34** (== 52-week high — today's move is pushing JPM to/near a new 52-week high) | |
| IBKR `dividend_yield` | 1.79% (trailing) | |
| IBKR `bid_ask` | $341.54 / $341.68 | Tight spread, consistent with a large-cap, highly liquid name |

**$341.56 is used throughout.**

---

## 2. Phase 01 Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

All figures below are sourced from JPMorgan Chase's own SEC filings (10-K, 10-Q, 8-K earnings releases) and investor-relations press releases via WebSearch, cross-checked against stockanalysis.com (via WebFetch) where noted. `yfinance` failed in this session's environment (same `curl_cffi` TLS/connection-reset failure documented in the 2026-07-12 C session) — see Section 5.

### 2a. Profitability (25% weight)

**TTM basis** (FY2025 − 1Q25 − 2Q25 + 1Q26 + 2Q26, all reported/GAAP-basis "Total net revenue" and Net Income figures):

```
TTM Net Income = $57.048B (FY2025) − $14.6B (1Q25) − $15.0B (2Q25) + $16.5B (1Q26) + $16.9B (2Q26) = $60.848B
TTM Revenue    = $182.4B (FY2025) − $45.3B (1Q25) − $44.9B (2Q25) + $49.8B (1Q26) + $57.3B (2Q26) = $199.3B

TTM Net Margin = 60.848 / 199.3 = 30.53%

NetMargin_Component = clamp((30.53 / 30) × 100, 0, 100) = 100.0   (clamped — above the 30% ceiling)
```

**ROIC proxy: ROE** (per the SOFI/Citigroup-session bank convention — ROIC's debt+equity invested-capital concept doesn't map to a bank; ROE is the standard substitute). Most recent full fiscal year (FY2025, GAAP): **17%** ROE (ROTCE 20%) — officially reported. A clean TTM-average-equity ROE requires quarterly average-equity data not sourced this session; FY2025 GAAP used as the most recent full-year figure, consistent with the C-session convention.

```
ROIC_Component = clamp((17 / 30) × 100, 0, 100) = 56.67

Profitability_Score (raw) = (100.0 + 56.67) / 2 = 78.33
```

**FCF-positive-3-years check (feeds the Profitability cap, see 2e):** **FAILS** — FCF was negative in both FY2024 and FY2025 (Section 2e), breaking any run of 3 consecutive positive years. Per quality-scoring.md: *"If the company isn't FCF-positive for 3+ consecutive years, cap Profitability_Score at 40.0 regardless of margin/ROIC."*

```
Profitability_Score = 40.0   (capped — see Section 3 for why this is flagged as a bank-accounting artifact, not genuine cash-flow weakness)
```

### 2b. Margins (15% weight) — **N/M, not computable**

JPMorgan, like SOFI and Citigroup, reports no Cost-of-Revenue/Gross-Profit line — revenue is net interest income plus noninterest (fee) income, with nothing to net a gross margin against. **Not scored** — no number invented.

### 2c. Growth (20% weight)

```
Revenue 3yr CAGR = (FY2025 Total Net Revenue $182.4B / FY2022 Total Net Revenue $128.7B)^(1/3) − 1 = 12.33%
Growth_Score = clamp((12.33 / 25) × 100, 0, 100) = 49.30
```

(Both figures are reported/GAAP-basis "Total net revenue" from JPM's own 4Q22 and 4Q25 earnings press releases — not the "managed basis" figures, which run slightly higher.)

**TAM/pricing-power modifier (+10):** documented evidence — for full-year 2025, JPMorgan ranked **#1 globally for investment banking fees** (8.4% wallet share), and **#1 in the US** for equity and equity-related underwriting (12.6% share) and long-term debt underwriting (10.2% share); assets under custody reached a **record $38 trillion** as of Q2 2025 (+14% over the trailing 5 years to $35T at end-2024, then further to $38T); the balance sheet stood at **$4.9 trillion** with **$2.68 trillion** in deposits as of Q1 2026; and 2Q26 results showed record revenue across every reporting line of business. Cited, not inferred.

```
Growth_Score = 49.30 + 10 = 59.30
```

### 2d. Balance Sheet (15% weight) — **N/M, not computable**

No GAAP EBIT/EBITDA line exists for a bank (Section 0a), so Net Debt/EBITDA (including the Upgrade 5 asset-light variant, which still presumes an EBITDA) cannot be computed. **Not scored.**

**Bank-equivalent context (cited, not substituted into the formula):** JPMorgan's Standardized CET1 (Common Equity Tier 1) capital ratio was **14.3%** at Q1 2026 ($291B CET1 capital) and **14.1%** at Q2 2026 ($303B CET1 capital; advanced-approach ratio 14.2%) — both comfortably above regulatory minimums, per the company's own 1Q26/2Q26 earnings supplements. This is the bank-industry-standard capital-adequacy metric and shows a genuinely strong balance sheet, but is not translatable into this framework's specific Net Debt/EBITDA formula.

### 2e. FCF Quality (10% weight)

```
FY2021 FCF = Net cash from operating activities = +$78.084B   (positive)
FY2022 FCF = +$107.119B   (positive)
FY2023 FCF = +$12.974B    (positive)
FY2024 FCF = −$42.012B    (negative)
FY2025 FCF = −$147.782B   (negative)
```
(Source: stockanalysis.com cash-flow statement, WebFetch 2026-07-14; the FY2024 and FY2025 figures were independently cross-verified via WebSearch directly against JPM's own FY2024 10-K and FY2025 10-K narrative — "net cash used in operating activities of $147,782 million" for 2025, driven by "higher trading assets, higher securities borrowed, net originations and purchases of loans held-for-sale, higher other assets and higher accrued interest and accounts receivable, partially offset by net income... and higher trading liabilities"; and $42,012 million for 2024, driven by "higher trading assets and higher securities borrowed, largely offset by net income.")

```
FY2024 FCF/NI = −42.012 / 58.471 = −71.87%
FY2025 FCF/NI = −147.782 / 57.048 = −258.98%
```

FCF/NI conversion ratio is **negative** in both of the last 2 fiscal years — not a "conversion" in the framework's intended sense.

```
FCFQuality_Score = clamp(((ratio − 0.40) / 0.60) × 100, 0, 100) = 0.0   (clamped — ratio is negative)
```

### 2f. Moat Signal (15% weight)

| Signal | Evidence | Result |
|---|---|---|
| Market share stable/growing | #1 globally in investment banking fees (8.4% wallet share, FY2025); #1 in the US in equity underwriting (12.6%) and long-term debt underwriting (10.2%); largest US bank by assets ($4.9T balance sheet, Q1 2026) | ✅ TRUE |
| Brand premium | No specific pricing-power citation (price increases without volume loss) sourced this session — "world's most valuable bank" / #1 Forbes Global 2000 ranking is a market-cap/scale distinction, not documented pricing-power evidence | ❌ not established |
| Network effect | JPMorgan's Treasury Services processes **>$10 trillion in payments per day**, giving it the largest USD clearing share globally; all 20 of the world's 20 largest companies are JPM Payments clients | ✅ TRUE |
| Switching costs | **$38 trillion in assets under custody** (record, as of Q2 2025, +14% over the trailing 5 years) — deep integration into institutional custody/securities-services operations | ✅ TRUE |
| Scale cost advantage | No cost-per-unit citation vs. smaller competitors sourced this session | ❌ not established |

```
Moat_Score = (3/5) × 100 = 60.0
```

### 2g. Hard Disqualifiers (checked independently of the weighted formula)

Per quality-scoring.md, a hard disqualifier fails the gate **regardless of the weighted score**:

1. **FCF/NI conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation → FIRES.** JPM's capital expenditure has not been disclosed as a growth-capex buildout driving the FCF shortfall — the negative FCF driver is trading-book, securities-borrowed, and loan-portfolio balance changes classified within operating cash flow (Section 2e), a structural bank-accounting artifact, not a growth-capex story that would exempt it. No carve-out exists in the documented rule.
2. **Net Debt/EBITDA over threshold → N/A (no EBITDA exists for a bank — cannot fire or clear; genuinely not computable, see 2d).**
3. **Not FCF-positive for 3+ consecutive years → FIRES.** FY2024 and FY2025 are both negative (Section 2e); only 1 of the last 3 fiscal years (FY2023) was positive.

**Two independent hard disqualifiers fire.** Per [.claude/commands/new-position.md](../.claude/commands/new-position.md), this stops the evaluation before Phase 02 scoring.

### 2h. Full Quality Score — illustrative ceiling (shown for transparency, not to override the disqualifiers)

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20) + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)
```

Margins and Balance Sheet are N/M (Sections 2b, 2d) — no real number exists to plug in. To show the disqualifier-independent finding is robust, here is the **most generous possible resolution** of those two components (100.0 each — an explicit stated ceiling, not an invented "real" figure):

```
Quality Score (best-case ceiling) = 0.25×40.0 + 0.15×100.0 + 0.20×59.30 + 0.15×100.0 + 0.15×60.0 + 0.10×0.0
                                  = 10.00 + 15.00 + 11.86 + 15.00 + 9.00 + 0.00
                                  = 60.86
```

**Even under the most generous possible treatment of the two N/M components, the score (60.86) sits decisively below the 80.0 gate** — so the FAIL conclusion holds independent of exactly how a future bank carve-out would resolve those gaps.

### Gate Result: ❌ **FAIL**

- Two independent hard disqualifiers fire (Section 2g): not FCF-positive 3+ consecutive years; FCF/NI conversion <70% for 2+ years without a growth-capex explanation.
- The illustrative best-case weighted score (60.86) is also well below 80.0.
- Per task instructions, **this evaluation stops here — no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.**

---

## 3. Why this reads as a framework gap, not a genuine red flag

Both firing hard disqualifiers are mechanical consequences of applying a non-financial-company cash-flow formula to a money-center bank's GAAP cash-flow statement, where "changes in trading assets," "securities borrowed," and loan-portfolio balance changes are classified within *operating* activities rather than investing activities — the same directional distortion the 2026-06-21 SOFI and 2026-07-12 Citigroup sessions identified, on the largest and most consistently profitable of the three banks evaluated under this framework so far. It should **not** be read as "JPMorgan's cash generation is deteriorating" — JPM's GAAP net income has stayed in a $37.7B–$58.5B band every year since 2021 (with FY2025's $57.0B essentially flat vs. FY2024's $58.5B and well above FY2021–FY2023), it returned $31.591B in buybacks alone in FY2025 (plus dividends, raised again to $1.65/share effective 3Q26) under a fresh $50B buyback authorization (effective July 2025), and its share count has been *shrinking* every year since 2022 (2,876.6M → 2,696.2M shares, FY2023→FY2025) — the opposite of a dilutive pattern. The Quality Score, as currently documented, simply has no depository-institution carve-out — this is now the **third** bank/neobank (after SOFI and Citigroup) hitting the identical wall, further strengthening the case that this is a systemic framework gap rather than a one-off data quirk, and arguably the strongest evidence yet since JPMorgan is unambiguously the highest-quality, most consistently profitable of the three by every qualitative measure.

---

## 4. Additional context (not scored — informational only, since Phase 02 was not run)

- **2Q26 earnings (released today, 2026-07-14, independently confirmed via multiple sources — not the Telegram post):** reported EPS $7.70 (beat consensus, cited in independent sourcing as ~$5.44–$5.59 depending on source), net revenue $57.3B (vs. ~$48.8B consensus per one source), net income $16.9B, ROTCE 23%. Record revenue across every line of business; Markets revenue +35% YoY to $12.1B (Equity Markets +86%). Quarterly dividend raised to $1.65/share effective 3Q26.
- **Credit ratings:** Moody's affirmed/upgraded JPMorgan Chase & Co.'s senior unsecured debt rating to **A1**, citing "superior financial performance" (per Investing.com coverage of the rating action). S&P/Fitch ratings were not independently confirmed this session — a data gap, not invented.
- **Capital returns:** $50B new share buyback program effective 1 July 2025; FY2025 repurchases totaled $31.591B (114.4M shares) vs. $18.83B (91.7M shares) in FY2024 and $9.824B (69.5M shares) in FY2023; dividend raised to $1.65/share effective 3Q26.
- **Book value / valuation context (not scored, no Phase 02 run; figures below predate today's earnings print and are not used in any calculation above):** market cap ~$915B, ~2.68B shares outstanding, book value per share ~$128.86, price/book ~2.61×, trailing PE ~16.0×, forward PE ~14.7×, PEG ~1.59 (source: stockanalysis.com statistics page, WebFetch 2026-07-14 — these are pre-earnings-print snapshot figures and would need refreshing against today's live price/EPS for any future Phase 02 work).
- **Sector context for the Telegram trigger:** the same Telegram channel grouped C with BAC/JPM/WFC ahead of Q2 2026 bank earnings in a 2026-07-12 post (see the C session) — this session's trigger post is JPM-specific, previewing/reporting the same earnings season.

---

## 5. Data sourcing note

`yfinance` (the framework's documented per-candidate verification tool) failed in this session's environment — `t.info` raised the same `curl_cffi` TLS/connection-reset error documented in the 2026-07-12 C session, reproduced and not resolved. **Fallback used: WebSearch (for figures cited to JPMorgan Chase's own SEC filings and earnings press releases, and third-party sources like stockanalysis.com, Investing.com, TradingView/StockTitan) and WebFetch (for stockanalysis.com's financials, cash-flow-statement, and statistics pages).** Every figure above is cited to its specific source; none is invented or estimated. IBKR's `get_price_snapshot` (Rule 0 live price) and `search_contracts` worked normally and are unaffected by this gap.

---

## 6. Recommendation: **PASS**

**The Phase 01 Quality Score gate fails** — two independent hard disqualifiers fire (not FCF-positive 3+ consecutive years; FCF/NI conversion <70% for 2+ years without a growth-capex explanation), and the illustrative best-case weighted score (60.86) sits well below the 80.0 threshold even under the most generous possible resolution of the two N/M (Margins, Balance Sheet) components. Per [.claude/commands/new-position.md](../.claude/commands/new-position.md), the evaluation stops here — **no Phase 02 valuation score, Composite Score, or fair-value/order-setup work was performed.**

This is the same class of framework gap first identified in the 2026-06-21 SOFI session and confirmed a second time in the 2026-07-12 Citigroup session — no documented Quality Score carve-out exists for depository institutions — now confirmed a **third** time, on JPMorgan Chase, the largest US bank by assets and (by market cap) the world's most valuable bank. This strengthens rather than weakens the case that the gap is structural, not name-specific: **a future framework improvement (a documented depository-institution carve-out for the FCF-based hard disqualifiers and the Margins/Balance-Sheet N/M components, paralleling Upgrade 5's existing asset-light-financial variant) is worth prioritizing** given this is now the third bank/neobank hitting the identical wall, on names of increasing size and quality each time. Not resolved within this session (no framework file was edited here) — flagged as a candidate framework-improvement item for a future `decisions/` entry.

Added to the not-in-portfolio watchlist (Section 7), flagged for re-evaluation once (a) a documented depository-institution carve-out exists in Phase 01/02, or (b) a further Rule 9 fundamental trigger fires (today's 2Q26 earnings are themselves the most recent trigger; the next scheduled one is 3Q26 earnings, typically mid-October).

---

## 7. Watchlist entry

See [watchlist/not-in-portfolio/JPM/JPM-2026-07-14.md](../watchlist/not-in-portfolio/JPM/JPM-2026-07-14.md) — new entry (first time JPM has been evaluated under this framework).

---

## Glossary

| Term | Meaning |
|---|---|
| **AUC (Assets Under Custody)** | The total value of client securities/assets a bank or custodian holds and safekeeps on clients' behalf (settlement, record-keeping, asset servicing) but does not own — a scale/switching-cost metric for a custody/securities-services business, distinct from the bank's own balance sheet. JPMorgan reported a record $38 trillion in AUC as of Q2 2025, cited as Moat Signal "switching costs" evidence in this session. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CET1 (Common Equity Tier 1) ratio** | A bank's core regulatory capital-adequacy measure: its highest-quality capital (common equity) divided by its risk-weighted assets. Regulators set a minimum a bank must stay above; the cushion above that minimum is a direct measure of balance-sheet strength — the bank-industry equivalent of this framework's Net Debt/EBITDA balance-sheet check, though not directly substitutable into that formula. JPMorgan's Standardized CET1 ratio was 14.3% (Q1 2026) and 14.1% (Q2 2026), both comfortably above regulatory minimums. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization — operating-profit measures that don't exist in standard form for a bank, since interest is a core funding cost rather than a financing add-back. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself; for a bank with an active trading/lending balance sheet, this can swing sharply due to normal changes in trading assets and loan balances, not necessarily unprofitability. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; not a clean signal for a bank whose FCF is driven by balance-sheet trading/lending activity rather than maintenance vs. growth capex. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score — see [quality-scoring.md](../framework/quality-scoring.md). |
| **Moat** | A durable competitive advantage that protects a business's profits from competitors. |
| **Money-center bank** | A large, internationally active bank (e.g. Citigroup, JPMorgan, Bank of America) that raises most of its funding from wholesale/institutional sources and global capital markets rather than primarily local retail deposits — distinct from a smaller regional or community bank. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — used to judge whether a fast grower's multiple is justified by its growth rate; requires a clean, non-distorted multi-year earnings base. |
| **P/B (Price-to-Book)** | Price ÷ book value (accounting net worth) per share — a standard bank-valuation multiple. |
| **PT (Price Target)** | An analyst's forecast of where a stock's price will be at a future date. |
| **Quality Score** | This framework's 0.0–100.0 continuous score grading profitability, margins, growth, balance sheet, moat signal, and FCF quality. A company must score 80.0+ to proceed to Phase 02 valuation scoring. See [quality-scoring.md](../framework/quality-scoring.md). |
| **Rate Environment Gate** | The mandatory pre-check (not run in this session, since the Quality Score gate failed first) comparing Earnings Yield against the 10-Year Treasury yield. |
| **ROE** | Return on Equity — Net Income ÷ shareholder equity. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit; not directly meaningful for a bank, so Return on Equity is used as the convention proxy instead. |
| **ROTCE (Return on Tangible Common Equity)** | Net income available to common shareholders divided by average tangible common equity (common equity minus goodwill/intangibles) — the primary profitability KPI banks themselves report and target, distinct from and typically higher than plain ROE. JPMorgan's FY2025 ROTCE was 20% (17% ROE); 2Q26 ROTCE was 23%. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |
| **Wallet share** | An investment bank's share of total global fee revenue paid across an industry category (e.g. investment banking fees) in a given period — a market-share metric specific to fee-based advisory/underwriting businesses. JPMorgan ranked #1 globally in investment banking fees with an 8.4% wallet share in FY2025. |

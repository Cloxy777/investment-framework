# New Position Evaluation: C (Citigroup Inc.) — 2026-07-12

**Task type:** NEW POSITION
**Ticker:** C — NYSE, IBKR contract_id 87335484
**Company:** Citigroup Inc. — global money-center bank (Services/TTS & Securities Services, Markets, Banking, U.S. Personal Banking, Wealth)
**Analyst:** Claude (automated session)
**Trigger:** This session was triggered by the hourly Telegram Stock-Mention Scan (Routine 6) — [t.me/bolshegold](https://t.me/bolshegold) post #9735, ~13:22 UTC 2026-07-12, previewing Q2 2026 bank earnings and grouping $C with $BAC, $JPM, $WFC ("banking sector, opens earnings season, watch credit-card delinquencies and consumption growth"). **The Telegram post is used only as a trigger to evaluate C — no financial data, score, or conclusion in this session is drawn from the post itself.** C was not previously in `watchlist/` and is not a current holding (confirmed against [portfolio/holdings.md](../portfolio/holdings.md) — no `C` row exists).

---

## 0. Ticker confirmation

`search_contracts("C")` resolves unambiguously: contract_id **87335484**, NYSE, "CITIGROUP INC" (STK). Not to be confused with the ICE Cocoa futures root also using symbol "C," or Citigroup's own bond-issuer entries in the same search results — the equity contract_id above is the one used throughout.

### 0a. Business-model mismatch flagged up front (same class of issue as the 2026-06-21 SOFI session)

Citigroup is a **money-center / depository institution**, and the framework's Phase 01/02 methodology has **no documented carve-out for banks** beyond Hybrid Upgrade 5's Net Debt/EBITDA asset-light variant (which still presumes an EBITDA line exists). Confirmed via repo search — this is the same structural gap the 2026-06-21 SOFI session identified, now recurring on a second, much larger and more mature bank:
- **No GAAP EBIT/EBITDA line** — interest expense is Citi's core cost of funding (deposits/borrowings), not a financing add-back.
- **Free Cash Flow reads deeply negative** in 3 of the last 5 fiscal years — driven mechanically by "changes in trading assets" and "changes in loans held-for-investment" being classified within operating cash flow for a bank, not by capex or operating losses.
- **No Cost-of-Revenue / Gross Margin line** — a bank's revenue is net interest income plus fee income, with nothing to net a "gross margin" against.

Every quality-score input below is computed and shown as the framework's documented formula requires; every place the formula doesn't cleanly map to a bank's business model is flagged explicitly rather than silently patched or invented.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Source | Price | Note |
|---|---|---|
| **IBKR live snapshot** (contract_id 87335484) | **$139.57** | Marked `is_close: true` — 2026-07-12 is a Sunday, markets closed; this is the most recent broker print (Friday 2026-07-10 close) |
| IBKR `misc_statistics` | 52-week range: **$84.71 – $147.90**; 13-week high $147.90; 26-week low $102.02 | |
| IBKR `dividend_yield` | 1.7% (trailing) | Cross-checked against WebSearch (~1.9%) — minor source variance; IBKR live figure used per Rule 0 primacy |

**$139.57 is used throughout.**

---

## 2. Phase 01 Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

All figures below are sourced from Citigroup's own SEC filings/earnings releases (via WebSearch) and cross-checked stockanalysis.com data (via WebFetch) — no `yfinance` data was available this session (see Data Sourcing Note, Section 5).

### 2a. Profitability (25% weight)

```
TTM Net Income = FY2025 NI ($14.3B) − Q1 2025 NI ($4.1B) + Q1 2026 NI ($5.8B) = $16.0B
TTM Revenue    = FY2025 Rev ($85.2B) − Q1 2025 Rev ($21.6B) + Q1 2026 Rev ($24.6B) = $88.2B
TTM Net Margin = 16.0 / 88.2 = 18.14%

NetMargin_Component = clamp((18.14 / 30) × 100, 0, 100) = 60.47
```

**ROIC proxy: ROE** (per the 2026-06-21 SOFI-session bank convention — ROIC's debt+equity capital-base concept doesn't map to a bank; ROE is the standard substitute). Most recent full fiscal year (FY2025, GAAP): **6.8%** (7.7% adjusted, excluding two Citi-disclosed one-off items: the ~$1.1B after-tax AO Citibank/Russia held-for-sale loss and the ~$714M after-tax Banamex-stake goodwill impairment — cited qualitatively per Rule 6, not substituted for the GAAP figure per this framework's "score off GAAP, cite adjusted separately" convention, e.g. PEP/AOI/Adjusted-EBITDA precedent in [glossary.md](../framework/glossary.md)). A clean TTM ROE figure requires quarterly average-equity data not sourced this session — flagged; FY2025 GAAP used as the most recent full-year figure.

```
ROIC_Component = clamp((6.8 / 30) × 100, 0, 100) = 22.67

Profitability_Score (raw) = (60.47 + 22.67) / 2 = 41.57
```

**FCF-positive-3-years check (feeds the Profitability cap, see 2f):** **FAILS** — FCF was negative in FY2023, FY2024, *and* FY2025 (Section 2e). Per quality-scoring.md: *"If the company isn't FCF-positive for 3+ consecutive years, cap Profitability_Score at 40.0 regardless of margin/ROIC."*

```
Profitability_Score = 40.0   (capped — see Section 3 for why this is flagged as a bank-accounting artifact, not genuine cash-flow weakness)
```

### 2b. Margins (15% weight) — **N/M, not computable**

Citigroup, like SOFI, reports no Cost-of-Revenue/Gross-Profit line — revenue is net interest income plus non-interest (fee) income, with nothing to net a gross margin against. **Not scored** — no number invented. Flagged as the same unresolved framework gap the SOFI session first surfaced.

### 2c. Growth (20% weight)

```
Revenue 3yr CAGR = (FY2025 Rev $85.2B / FY2022 Rev $75.338B)^(1/3) − 1 = 4.19%
Growth_Score = clamp((4.19 / 25) × 100, 0, 100) = 16.74
```

**TAM/pricing-power modifier (+10):** documented evidence — Services segment (Treasury & Trade Solutions + Securities Services) revenue +17% YoY in Q1 2026, "best first quarter in a decade" per Citi's own release; TTS confirmed gaining market share in FY2024/2025; Citi's stated strategic repositioning of TTS around tokenization, instant payments, and programmable money as next-generation growth vectors. Cited, not inferred.

```
Growth_Score = 16.74 + 10 = 26.74
```

### 2d. Balance Sheet (15% weight) — **N/M, not computable**

No GAAP EBIT/EBITDA line exists for a bank (Section 0a), so Net Debt/EBITDA (including the Upgrade 5 asset-light variant, which still presumes an EBITDA) cannot be computed. **Not scored.**

**Bank-equivalent context (cited, not substituted into the formula):** Citi's Standardized CET1 (Common Equity Tier 1) capital ratio was **13.2%** at FY2025 year-end (down from 13.6% FY2024) and **12.7%** at Q1 2026 (110bps above its 11.6% regulatory minimum) — the bank-industry-standard capital-adequacy metric, showing real balance-sheet cushion, but not translatable into this framework's specific Net Debt/EBITDA formula.

### 2e. FCF Quality (10% weight)

```
FY2021 FCF = OCF $47.090B − CapEx $4.119B = +$42.971B   (positive)
FY2022 FCF = OCF $25.069B − CapEx $5.632B = +$19.437B   (positive)
FY2023 FCF = OCF −$73.416B − CapEx $6.583B = −$79.999B  (negative)
FY2024 FCF = OCF −$19.669B − CapEx $6.500B = −$26.169B  (negative)
FY2025 FCF = OCF −$67.632B − CapEx $6.520B = −$74.152B  (negative)
```
(Source: stockanalysis.com cash-flow statement, WebFetch 2026-07-12.)

FCF/NI conversion ratio is **negative** in each of the last 3 fiscal years (FCF negative while NI stayed positive throughout) — not a "conversion" in the framework's intended sense.

```
FCFQuality_Score = clamp(((ratio − 0.40) / 0.60) × 100, 0, 100) = 0.0   (clamped — ratio is negative)
```

### 2f. Moat Signal (15% weight)

| Signal | Evidence | Result |
|---|---|---|
| Market share stable/growing | TTS (Treasury & Trade Solutions) confirmed gaining market share FY2024–2025; Services segment record revenue growth | ✅ TRUE |
| Brand premium | No specific pricing-power citation (price increases without volume loss) sourced this session | ❌ not established |
| Network effect | Citi orchestrates ~$5T in daily transaction volume, serves 90% of the Fortune 500, direct membership in 270+ cash-clearing centers across 94 countries | ✅ TRUE |
| Switching costs | 60+ market custody platform holding $24–27T in client assets under custody — deep integration into corporate treasury/custody operations | ✅ TRUE |
| Scale cost advantage | No cost-per-unit citation vs. smaller competitors sourced this session | ❌ not established |

```
Moat_Score = (3/5) × 100 = 60.0
```

### 2g. Hard Disqualifiers (checked independently of the weighted formula)

Per quality-scoring.md, a hard disqualifier fails the gate **regardless of the weighted score**:

1. **FCF/NI conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation → FIRES.** Citi's capex has been flat/stable (~$6.5B/yr, no growth-capex buildout) — the negative FCF driver is trading-book and loan-portfolio balance changes classified within operating cash flow, a structural bank-accounting artifact, not a growth-capex story that would exempt it. No carve-out exists in the documented rule.
2. **Net Debt/EBITDA over threshold → N/A (no EBITDA exists for a bank — cannot fire or clear; genuinely not computable, see 2d).**
3. **Not FCF-positive for 3+ consecutive years → FIRES.** FY2023, FY2024, FY2025 all negative (Section 2e).

**Two independent hard disqualifiers fire.** Per [.claude/commands/new-position.md](../.claude/commands/new-position.md), this stops the evaluation before Phase 02 scoring.

### 2h. Full Quality Score — illustrative ceiling (shown for transparency, not to override the disqualifiers)

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20) + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)
```

Margins and Balance Sheet are N/M (Sections 2b, 2d) — no real number exists to plug in. To show the disqualifier-independent finding is robust, here is the **most generous possible resolution** of those two components (100.0 each — an explicit stated ceiling, not an invented "real" figure):

```
Quality Score (best-case ceiling) = 0.25×40.0 + 0.15×100.0 + 0.20×26.74 + 0.15×100.0 + 0.15×60.0 + 0.10×0.0
                                  = 10.00 + 15.00 + 5.348 + 15.00 + 9.00 + 0.00
                                  = 54.35
```

**Even under the most generous possible treatment of the two N/M components, the score (54.35) sits decisively below the 80.0 gate** — so the FAIL conclusion holds independent of exactly how a future bank carve-out would resolve those gaps.

### Gate Result: ❌ **FAIL**

- Two independent hard disqualifiers fire (Section 2g): not FCF-positive 3+ consecutive years; FCF/NI conversion <70% for 2+ years without a growth-capex explanation.
- The illustrative best-case weighted score (54.35) is also well below 80.0.
- Per task instructions, **this evaluation stops here — no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.**

---

## 3. Why this reads as a framework gap, not a genuine red flag

Both firing hard disqualifiers are mechanical consequences of applying a non-financial-company cash-flow formula to a money-center bank's GAAP cash-flow statement, where "changes in trading assets" and "changes in loans held-for-investment" — completely normal, expected swings for an active trading/lending balance sheet — are classified within *operating* activities rather than investing activities (unlike SOFI, where growing loan originations sat in *investing* activities). This produces the same directional distortion the 2026-06-21 SOFI session identified, via a different mechanical path. It should **not** be read as "Citigroup's cash generation is deteriorating" — Citi's GAAP net income has grown every year since FY2023 ($9.2B → $12.7B → $14.3B), it returned $7.4B to shareholders in Q1 2026 alone, and its board just authorized a new $30B multiyear buyback program (Section 4). The Quality Score, as currently documented, simply has no depository-institution carve-out — the same structural finding as SOFI, now confirmed on a second, much larger and more mature bank, strengthening the case that this is a systemic framework gap rather than a one-off data quirk.

---

## 4. Additional context (not scored — informational only, since Phase 02 was not run)

- **Credit ratings:** Moody's A3 (stable, as of 31 Mar 2026); S&P BBB+/A-2 (stable); Fitch outlook revised stable→positive (1 May 2026).
- **Capital returns:** $30B new multiyear buyback program authorized 28 Apr 2026 (begins Q2 2026), following a prior $20B program; Q1 2026 alone returned $7.4B to common shareholders ($6.3B buybacks + $1.1B dividends); 12% quarterly dividend increase announced following the 2026 Fed stress test.
- **Book value:** $110.01/share (FY2025, +8% YoY); tangible book value $97.06/share (FY2025, +9% YoY).
- **Valuation context (not scored, no Phase 02 run):** Forward PE sources ranged 10.58×–12.53×, trailing PE 15.08×–17.51× (source variance across fullratio, stockanalysis.com — not reconciled since not needed for the gate decision). PEG (stockanalysis-reported, 0.52) would not qualify for the framework's Fast-Grower PEG sub-score regardless, since EPS fell sharply from $7.00 (FY2022) to $4.04 (FY2023) before recovering to $6.99 (FY2025) — a volatile, restructuring/one-off-item-driven path, not a clean 3-year growth base.
- **Analyst consensus price targets** (informational only): mean ~$146–150, range $125–180 across sources.
- **Sector context for the Telegram trigger:** the post grouped C with BAC/JPM/WFC ahead of Q2 2026 bank earnings, flagging credit-card delinquencies and consumption growth as watch items — genuinely relevant *qualitative* context for a future re-evaluation, but not itself a scored input (per CLAUDE.md, never act on an unsourced social-media post as data).

---

## 5. Data sourcing note

`yfinance` (the framework's documented per-candidate verification tool) failed in this session's environment — `t.info` raised a `curl_cffi` TLS/connection-reset error before reaching Yahoo's endpoint, reproduced with explicit CA-bundle environment variables set and not resolved. **Fallback used: WebSearch (for figures cited to Citigroup's own SEC filings/earnings releases and third-party sources like stockanalysis.com, fullratio, macrotrends) and WebFetch (for stockanalysis.com's cash-flow-statement and statistics pages).** Every figure above is cited to its specific source; none is invented or estimated. IBKR's `get_price_snapshot` (Rule 0 live price) and `search_contracts` worked normally and are unaffected by this gap.

---

## 6. Recommendation: **PASS**

**The Phase 01 Quality Score gate fails** — two independent hard disqualifiers fire (not FCF-positive 3+ consecutive years; FCF/NI conversion <70% for 2+ years without a growth-capex explanation), and the illustrative best-case weighted score (54.35) sits well below the 80.0 threshold even under the most generous possible resolution of the two N/M (Margins, Balance Sheet) components. Per [.claude/commands/new-position.md](../.claude/commands/new-position.md), the evaluation stops here — **no Phase 02 valuation score, Composite Score, or fair-value/order-setup work was performed.**

This is the same class of framework gap first identified in the 2026-06-21 SOFI session — no documented Quality Score carve-out exists for depository institutions — now confirmed on a second bank, this time a much larger, more mature, and (by every qualitative measure available) fundamentally sounder one. This strengthens rather than weakens the case that the gap is structural, not name-specific: **a future framework improvement (a documented depository-institution carve-out for the FCF-based hard disqualifiers and the Margins/Balance-Sheet N/M components, paralleling Upgrade 5's existing asset-light-financial variant) is worth prioritizing** given this is now the second bank/neobank hitting the identical wall. Not resolved within this session (no framework file was edited here) — flagged as a candidate framework-improvement item for a future `decisions/` entry.

Added to the not-in-portfolio watchlist (Section 7), flagged for re-evaluation once (a) a documented depository-institution carve-out exists in Phase 01/02, or (b) a Rule 9 fundamental trigger fires (Q2 2026 earnings, the event the triggering Telegram post itself was previewing).

---

## 7. Watchlist entry

See [watchlist/not-in-portfolio/C/C-2026-07-12.md](../watchlist/not-in-portfolio/C/C-2026-07-12.md) — new entry (first time C has been evaluated under this framework).

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets. |
| **CET1 (Common Equity Tier 1) ratio** | A bank's core regulatory capital-adequacy measure: its highest-quality capital (common equity) divided by its risk-weighted assets. Regulators set a minimum a bank must stay above; the cushion above that minimum is a direct measure of balance-sheet strength — the bank-industry equivalent of this framework's Net Debt/EBITDA balance-sheet check, though not directly substitutable into that formula. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization — operating-profit measures that don't exist in standard form for a bank, since interest is a core funding cost rather than a financing add-back. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **Efficiency ratio (bank)** | A bank's non-interest expense divided by its revenue — the inverse of an operating margin; lower is better. Citigroup's Q1 2026 efficiency ratio was 58%, with full-year 2026 guidance around 60%. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself; for a bank with an active trading/lending balance sheet, this can swing sharply due to normal changes in trading assets and loan balances, not necessarily unprofitability. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; not a clean signal for a bank whose FCF is driven by balance-sheet trading/lending activity rather than maintenance vs. growth capex. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score — see [quality-scoring.md](../framework/quality-scoring.md). |
| **Moat** | A durable competitive advantage that protects a business's profits from competitors. |
| **Money-center bank** | A large, internationally active bank (e.g. Citigroup, JPMorgan, Bank of America) that raises most of its funding from wholesale/institutional sources and global capital markets rather than primarily local retail deposits — distinct from a smaller regional or community bank. |
| **NIM (Net Interest Margin)** | The spread a bank earns between interest received on loans/assets and interest paid on deposits/borrowings — the core profitability driver for a depository institution. |
| **P/TBV (Price-to-Tangible-Book-Value)** | Price ÷ tangible book value (book value minus intangible assets like goodwill) per share — a standard bank-valuation multiple. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — used to judge whether a fast grower's multiple is justified by its growth rate; requires a clean, non-distorted multi-year earnings base. |
| **PT (Price Target)** | An analyst's forecast of where a stock's price will be at a future date. |
| **Quality Score** | This framework's 0.0–100.0 continuous score grading profitability, margins, growth, balance sheet, moat signal, and FCF quality. A company must score 80.0+ to proceed to Phase 02 valuation scoring. See [quality-scoring.md](../framework/quality-scoring.md). |
| **Rate Environment Gate** | The mandatory pre-check (not run in this session, since the Quality Score gate failed first) comparing Earnings Yield against the 10-Year Treasury yield. |
| **ROE** | Return on Equity — Net Income ÷ shareholder equity. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit; not directly meaningful for a bank, so Return on Equity is used as the convention proxy instead. |
| **ROTCE (Return on Tangible Common Equity)** | Net income available to common shareholders divided by average tangible common equity (common equity minus goodwill/intangibles) — the primary profitability KPI banks themselves report and target, distinct from and typically higher than plain ROE. |
| **TBVPS (Tangible Book Value Per Share)** | Tangible book value divided by shares outstanding — the per-share input to a P/TBV multiple. |
| **Treasury yield (10Y)** | The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used in this framework's Rate Environment Gate. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |
| **TTS (Treasury and Trade Solutions)** | Citigroup's cash-management and trade-finance business line for corporate/institutional clients (part of its Services segment) — one of the businesses cited as Moat Signal evidence (market share gains, switching-cost/network-effect infrastructure) in this session. |

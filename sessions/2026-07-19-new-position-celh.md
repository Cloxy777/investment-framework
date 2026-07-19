# New Position Evaluation — CELH (Celsius Holdings, Inc., Nasdaq)

**Task type:** NEW POSITION (Telegram-scan trigger, manual run)
**Date:** 2026-07-19
**10Y US Treasury Yield:** 4.57% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-07-16 — normal FRED reporting lag)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §3.4). For reference only, the bracket in force would be **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current CELH portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); no CELH row in the holdings table).
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/CELH/` and `watchlist/not-in-portfolio/CELH/` before this session — this is CELH's first-ever evaluation under this framework.
**Sector:** Consumer Staples / Beverages — functional/better-for-you energy drinks, sold in the US and internationally (Nordics, and other expansion markets).
**Filer type:** US domestic filer, SEC CIK 0001341766. Listed on Nasdaq (CELH). Fiscal year ends 31 December. Most recent quarterly filing: Q1 2026 (quarter ended 2026-03-31, reported 2026-05-07); most recent annual filing: FY2025 Form 10-K.
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

Telegram channel **FinnInvestChannel**, post **#2957** (~13:16 UTC, 2026-07-19), was a store-visit observation noting a small in-store merchandising upgrade for Celsius, plus commentary that Celsius's US brand growth has slowed in recent reports while the current growth story is international expansion plus the Alani Nu brand. No confirmed earnings/guidance/M&A event was claimed in the post. Per [telegram-scan.md](../.claude/commands/telegram-scan.md)'s convention ("no watchlist entry exists at all → `/new-position <TICKER>`"), this session was triggered regardless of the mention's substance — CELH had zero prior coverage in this repo (checked both `watchlist/in-portfolio/CELH/` and `watchlist/not-in-portfolio/CELH/`, neither exists). **Per Rule 0, no claim from the triggering post is used as financial data anywhere below** — the post is only the reason this ticker was looked at; every figure in this session is independently fetched/sourced and cited. (As it happens, the post's directional color — decelerating US/core-brand growth, international + Alani Nu as the current growth story — turns out to be independently, primarily corroborated below; see §3.3 Growth.)

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

**Contract disambiguation:** `search_contracts("CELH")` returned 3 matches: **NASDAQ:CELH, contract_id 71364351, "CELSIUS HOLDINGS INC", country_code US** (the correct primary US listing), a Mexican-exchange (MEXI) cross-listing of the same company, and `CELT` ("TRADR 2X LONG CELH DAILY ETF" — an unrelated leveraged-ETF decoy sharing a similar ticker root, not used).

**Data-quality catch:** `get_price_snapshot` returned `last: $29.98` (flagged `is_close: true`). Today (2026-07-19) is a Saturday, markets closed — cross-checked against `get_price_history` (daily bars) before using this figure, and the two didn't agree:

| Date | Close |
|---|---|
| 2026-07-13 | $29.83 |
| 2026-07-14 | $30.14 |
| 2026-07-15 | $30.21 |
| **2026-07-16** | **$29.98** |
| **2026-07-17** | **$28.99** |

`get_price_snapshot`'s "last" value ($29.98) was actually **Thursday 2026-07-16's close**, one session stale — not the true most recent trade. The correct, most recent live price is **Friday 2026-07-17's close: $28.99** — independently confirmed via a direct Yahoo Finance `quoteSummary` pull (`regularMarketPrice` $28.99, `regularMarketTime` timestamp 2026-07-17 20:00:01 UTC, i.e. the 4:00pm ET NYSE/Nasdaq close). This is the same class of stale-snapshot issue flagged in this framework's 2026-07-19 STM session — flagging it again here since it recurred on a different ticker, worth noting as a standing tool-reliability caveat for any session run near a weekend.

| Field | Value | Detail |
|---|---|---|
| **Live price used** | **$28.99** | Friday 2026-07-17 close (most recent trade; market closed for the weekend on 2026-07-19, the session date) |
| 52-week high | $66.74 (IBKR `misc_statistics` and Yahoo `fiftyTwoWeekHigh`, consistent) |
| 52-week low | $27.47 (IBKR and Yahoo, consistent) — CELH is trading within ~5% of its 52-week low |
| Price 52 weeks ago (`open_52w`) | $44.45 |
| YTD change | −34.46% (−$15.76), per IBKR `year-to-date-change` |
| 13-week high/low | $35.75 / $27.47 — the stock has been in a sustained downtrend all year |

**Live price used throughout this session: $28.99.**

---

## 2. Data Source Note

`yfinance`'s `curl_cffi` HTTP backend failed with a TLS-level `Recv failure: Connection reset by peer` error, the same documented issue noted in prior sessions (e.g. STM, TSLA, both 2026-07-19). Worked around via direct `requests`-based calls to Yahoo Finance's `quoteSummary` (assetProfile, summaryDetail, financialData, defaultKeyStatistics, incomeStatementHistory, cashflowStatementHistory, balanceSheetHistory, earnings, earningsTrend, price, calendarEvents) and `fundamentals-timeseries` (annual and quarterly Revenue, Gross Profit, EBIT, EBITDA, Net Income, Net Income Attributable to Common Stockholders, Operating Cash Flow, CapEx, Free Cash Flow, Total Debt, Cash, Invested Capital, Pretax Income, Tax Provision) endpoints, obtaining a crumb token from `query2.finance.yahoo.com/v1/test/getcrumb` first. This is a primary-aggregator data source (Yahoo Finance, sourced from Celsius's own SEC filings), not an invented or estimated figure anywhere below. Internal-consistency checks were run throughout (e.g. summed quarterly figures tie to reported TTM/annual figures exactly — see §3.1 footnotes).

The 10-Year Treasury yield was sourced directly from FRED's public CSV endpoint (`fredgraph.csv?id=DGS10`). Several `WebSearch`/`WebFetch` queries were run for Growth and Moat Signal evidence (all cited individually in §3.3), drawing on Celsius's own Q1 2026 earnings release (`ir.celsiusholdingsinc.com`) as the primary source, plus secondary financial-press/analytics citations flagged as such where used.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Raw financial inputs (all sourced, cited)

**Annual figures (Yahoo Finance `fundamentals-timeseries`, sourced from CELH's own 10-K filings):**

| Fiscal Year | Revenue | Gross Profit | Gross Margin | EBIT | EBITDA | Net Income | Net Margin | Op. Cash Flow | CapEx | FCF | FCF/NI |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2022 | $653.604M | $270.869M | 41.44% | −$157.801M | −$155.884M | −$187.282M | −28.65% | $108.182M | −$8.264M | $99.918M | n/m (loss year) |
| FY2023 | $1,318.014M | $633.139M | 48.04% | $291.749M | $294.975M | $226.801M | 17.21% | $141.218M | −$17.433M | $123.785M | 54.60% |
| FY2024 | $1,355.630M | $680.207M | 50.18% | $195.050M | $202.324M | $145.074M | 10.70% | $262.898M | −$23.390M | $239.508M | 165.10% |
| FY2025 | $2,515.269M | $1,267.333M | 50.39% | $174.010M | $203.461M | $107.999M | 4.29% | $359.442M | −$36.067M | $323.375M | 299.42% |

**TTM snapshot (Q2 2025–Q1 2026, reconstructed from quarterly `fundamentals-timeseries` and cross-checked against Yahoo's own `trailing*` fields, which match exactly):**

| Metric | TTM value | Cross-check |
|---|---|---|
| Revenue | $2,968.608M | Matches Yahoo `trailingTotalRevenue` exactly |
| Gross Profit | $1,473.027M → **Gross Margin 49.62%** | Matches `trailingGrossProfit` exactly |
| EBIT | $262.396M | Matches `trailingEBIT` exactly |
| EBITDA | $298.370M | Matches `trailingEBITDA` exactly |
| Net Income | $173.679M → **Net Margin 5.851%** | Matches `trailingNetIncome`; ties to Yahoo's own `profitMargins` field (0.058510) to 4 decimal places |
| Operating Cash Flow | $329.798M | Matches `trailingOperatingCashFlow` exactly |
| CapEx | −$37.039M | Matches `trailingCapitalExpenditure` exactly |
| Free Cash Flow | $292.759M → **FCF/NI ratio 168.55%** | Matches `trailingFreeCashFlow` exactly (OCF + CapEx) |
| Tax Provision / Pretax Income | $27.897M / $201.576M → **effective tax rate 13.84%** | From `trailingTaxProvision` / `trailingPretaxIncome` |

**Flagged (earnings-quality note, not a data gap):** CELH's reported **"Net Income Attributable to Common Stockholders"** runs consistently below its plain "Net Income" line (TTM sum of quarterly figures ≈ $109.2M vs. plain Net Income TTM $173.679M) — a ~$64M gap driven by dividends/accretion on the convertible preferred stock PepsiCo holds in Celsius (see §3.3 Moat). This session uses the larger, plain **Net Income** figure for Net Margin/Profitability scoring, consistent with Yahoo's own `profitMargins` field (which also ties to plain Net Income, confirmed above) — flagged explicitly rather than silently picking a basis, per "show every calculation."

**Balance sheet (most recent quarter, per Yahoo `financialData`, reflecting Q1 2026 quarter-end 2026-03-31):** Total Debt $675.881M, Total Cash $549.201M → **Net Debt = $126.680M**. (Cross-check: the `fundamentals-timeseries` quarterly series shows Total Debt $668.881M and Cash $549.201M as of the same date — a ~$7M discrepancy in the debt figure between the two Yahoo endpoints, likely a lease-liability inclusion difference; the larger, `financialData` figure is used below, which is conservative — i.e. produces a *higher* Net Debt/EBITDA than the alternative.)

**Invested Capital (Yahoo `fundamentals-timeseries`, quarterly, Q1 2026):** $1,919.643M — up sharply from $399.929M (FY2024) and $264.040M (FY2023), reflecting the balance-sheet impact of the Alani Nu (closed 1 April 2025) and Rockstar (closed August 2025) acquisitions (largely funded via new debt and consideration, per §3.3).

**ROIC (TTM basis):**
```
NOPAT (TTM) = EBIT × (1 − effective tax rate) = $262.396M × (1 − 0.1384) = $226.08M
Invested Capital (Q1 2026 quarter-end) = $1,919.643M
ROIC = 226.08 / 1,919.643 = 11.78%
```

### 3.2 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | CELH data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF positive in **all four** of the last four fiscal years: FY2022 +$99.918M, FY2023 +$123.785M, FY2024 +$239.508M, FY2025 +$323.375M. | **Does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | Net Debt $126.680M ÷ TTM EBITDA $298.370M = **0.4246×** — comfortably under 2.5×. | **Does not fire.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | Ratio history: FY2022 n/m (net-loss year, ratio not meaningful), FY2023 **54.60%** (the one sub-70% year), FY2024 165.10%, FY2025 299.42%, TTM 168.55%. Only **one** clearly sub-70% year (FY2023), not two consecutive — and the two most recent fiscal years (and TTM) are all far above 100%. | **Does not fire.** |

**No hard disqualifiers fire.**

### 3.3 Sub-score calculation

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((5.851/30)×100, 0, 100) = **19.50**. ROIC_Component = clamp((11.78/30)×100, 0, 100) = **39.27**. Profitability_Score = (19.50+39.27)/2 = **29.39**. (No FCF-positivity cap applied — company is FCF-positive all 4 years on file.) | **29.39** |
| **Margins (15%)** | GrossMargin_Score = clamp((49.62/80)×100, 0, 100) = **62.03** (TTM gross margin). **4-year trend:** 41.44% (FY2022) → 48.04% (FY2023) → 50.18% (FY2024) → 50.39% (FY2025) → 49.62% (TTM) — genuine multi-year expansion (documented driver: PepsiCo direct-store-delivery integration cut outbound freight from ~4.5% to ~3.7% of revenue per a secondary analytics source, [eightx.co](https://eightx.co/blog/celsius-distribution-deal-gross-margin-swing), flagged as non-primary), but plateauing/ticking down slightly in the TTM window (acquired Rockstar and Alani Nu carry somewhat different margin profiles, and Q1 2026 gross margin of 48.3% — per the company's own Q1 2026 release — is down from 52.3% a year earlier). **No +10 trend bonus** — the bonus is explicitly conditioned on expansion *while below the 40% static threshold*; CELH's gross margin has been above 40% throughout this window, so it doesn't apply regardless of the trend direction. | **62.03** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $653.604M → FY2025 $2,515.269M) = (2,515.269/653.604)^(1/3) − 1 = **+56.72%/yr**. Growth_Score(raw) = clamp((56.72/25)×100, 0, 100) = clamp(226.9, 0, 100) = **100.0** (clamped, ceiling). **Material flag (judgment call, does not change the ultimate conclusion — see §3.4 robustness check):** this reported-revenue CAGR is overwhelmingly **inorganic** — Celsius acquired **Alani Nu** (closed 1 April 2025, contributing $368.1M of CELH's $782.6M Q1 2026 revenue) and **Rockstar Energy** (closed August 2025, contributing $66.6M of Q1 2026 revenue) — together roughly 56% of Q1 2026's total revenue. The **organic**, standalone CELSIUS-brand story is materially weaker: the company's own Q1 2026 earnings release states CELSIUS-brand US tracked-channel retail sales grew only **+6% YoY** for the 13-week period ended 2026-03-29 (down sharply from the brand's historical 30–80%+ YoY growth rates), while Rockstar's own retail sales *declined* 13% YoY over the same window — both company-disclosed figures ([Celsius Holdings Q1 2026 Financial Results](https://ir.celsiusholdingsinc.com/news/news-details/2026/Celsius-Holdings-Reports-First-Quarter-2026-Financial-Results/default.aspx)). International revenue (the other growth vector the triggering Telegram post named) was $35.3M in Q1 2026, +55% YoY off a small base — real, but only ~4.5% of total revenue. **No −10 structural-deceleration modifier applied**, because the literal *scored* input (total reported revenue CAGR) is not itself decelerating — it is accelerating, due to the acquisitions; a third-party source on the core-brand slowdown ([Quiver Quantitative](https://www.quiverquant.com/news/Celsius+Holdings+slides+as+investors+refocus+on+slowing+core+brand+growth+and+tougher+competitive+backdrop)) itself concludes "structural evidence is sparse," framing the weakness as competitive/near-term rather than clearly structural — so applying a penalty on an already-ambiguous basis to a metric it doesn't even map onto directly would not meet this framework's "documented, not invented" bar. **No +10 TAM modifier applied either** for the same reason (already clamped at the ceiling; moot). This is flagged prominently as the single biggest judgment call in this session — see the §3.4 robustness check demonstrating the Quality Score's FAIL conclusion does not depend on how this is resolved. | **100.0** |
| **Balance Sheet (15%)** | Net Debt $126.680M ÷ TTM EBITDA $298.370M = 0.4246× → clamp(100×(1−0.4246/4), 0, 100) = **89.39** | **89.39** |
| **Moat Signal (15%)** | See evidence table below — **1 of 5** signals cleared the cited-evidence bar. Moat_Score = (1/5)×100 = **20.0** | **20.0** |
| **FCF Quality (10%)** | TTM FCF/NI = $292.759M / $173.679M = 168.55% → clamp(((1.6855−0.40)/0.60)×100, 0, 100) = clamp(214.25, 0, 100) = **100.0** (clamped) | **100.0** |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable or growing | **TRUE.** Celsius's combined brand portfolio (CELSIUS + Alani Nu + Rockstar) held an approximate **20.9% dollar share** of the US energy-drink category in tracked retail channels as of Q1 2026, per the company's own [Q1 2026 earnings release](https://ir.celsiusholdingsinc.com/news/news-details/2026/Celsius-Holdings-Reports-First-Quarter-2026-Financial-Results/default.aspx). **Flagged:** this is a portfolio-wide figure inflated by consolidating two 2025 acquisitions under one ownership umbrella, not a clean like-for-like organic share gain of a single continuously-operated brand — credited as TRUE per the framework's literal "cited share data" bar, but flagged for the same reason the Growth sub-score's CAGR is flagged above. | **TRUE** |
| Brand premium | No cited evidence of price increases sustained without volume loss was found this session for the CELSIUS brand specifically (searches for pricing-power citations returned only stock-quote/analytics pages, not a specific pricing study). Not credited without a citable mechanism. | **FALSE** |
| Network effect | Not applicable — a packaged/branded consumer beverage has no two-sided network-effect dynamic. | **FALSE** |
| Switching costs | No documented consumer- or retailer-side lock-in mechanism found with a citable source. The PepsiCo direct-store-delivery (DSD) distribution relationship is a real, material commercial arrangement, but it is a **distribution-scale** factor (considered under Scale below), not a switching-cost mechanism in the sense this checklist row requires (contractual/integration lock-in on the customer side). Not credited here to avoid double-counting the same underlying fact under two different signals. | **FALSE** |
| Scale cost advantage | **Considered but not credited.** A secondary analytics source ([eightx.co](https://eightx.co/blog/celsius-distribution-deal-gross-margin-swing)) documents that consolidating distribution into PepsiCo's DSD network cut Celsius's outbound freight cost from ~4.5% to ~3.7% of revenue (FY2023→FY2024) — a real logistics-efficiency mechanism. However, the same source shows Celsius's gross margin (48.3–50.4% across recent periods) still trails category leader **Monster Beverage's** (53.1–54.0% FY2023–FY2024) — i.e. the cited evidence shows Celsius *closing* a margin gap against a larger incumbent, not holding a cost advantage over smaller competitors, which is what this checklist row specifically requires ("cost-per-unit data showing a gap vs. smaller competitors"). No such comparison was found. Not credited. | **FALSE** |

### 3.4 Final weighted Quality Score

```
Quality Score = (29.39 × 0.25) + (62.03 × 0.15) + (100.0 × 0.20) + (89.39 × 0.15) + (20.0 × 0.15) + (100.0 × 0.10)
              = 7.3475 + 9.3045 + 20.0 + 13.4085 + 3.0 + 10.0
              = 63.0605 → 63.1 (rounded to nearest 0.1)
```

**63.1 < 80.0 — fails the gate by 16.9 points.** No hard disqualifiers fire (§3.2); this is a weighted-score failure.

**Robustness check (per "no black-box outputs" — showing the conclusion doesn't hinge on the session's most discretionary judgment calls):**
- If the flagged, M&A-inflated **Growth_Score** were instead treated at its absolute floor (0.0, the most conservative possible reading — not a claim that this is the "correct" organic figure, just a bound): Quality Score = 63.0605 − 20.0 + 0 = **43.1**. Still fails by 36.9 points.
- If **Moat_Score** were instead credited at its ceiling (100.0 — all 5 signals, an unreasonably generous reading not supported by the evidence in §3.3): Quality Score = 63.0605 − 3.0 + 15.0 = **75.1**. Still fails by 4.9 points.
- Even **combining both** maximally-generous-to-CELH adjustments in the same direction (Growth at its scored ceiling of 100.0 *and* Moat credited at 100.0): Quality Score = 63.0605 − 3.0 + 15.0 = **75.1** (Growth is already at its ceiling, so there's no further room to add there). **The gate still fails under every combination of judgment calls tested.**

### Result: **Phase 01 FAIL — weighted Quality Score 63.1, misses the 80.0+ gate by 16.9 points.**

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... stop there and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position, and do not place a limit order. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring, per the Phase 03 table in [strategy.md](../framework/strategy.md) (Composite Score is a precondition for that table applying at all).

This is not a verdict that Celsius Holdings is a bad business — it carries genuinely strong balance-sheet metrics (Net Debt/EBITDA 0.42×, comfortably investment-grade-like), very high cash conversion (FCF/NI 168.55% TTM), and a real, growing ~21% combined dollar share of the US energy-drink category. But on the framework's specific, cited, quantitative criteria: **thin GAAP profitability** (TTM Net Margin 5.85%, ROIC 11.78% — both well below this framework's scoring ceiling, reflecting heavy acquisition-related costs/amortization layered on top of the underlying beverage business), and a **weak Moat Signal read** (1 of 5 cited-evidence signals; no credited brand-premium/pricing-power or switching-cost mechanism specific to Celsius), pull the weighted score well short of 80.0 even when the Growth sub-score is credited at its maximum for a metric this session flags as substantially inflated by two 2025 acquisitions rather than organic demand. The triggering Telegram post's own framing — that the *organic* US/core-brand growth story has slowed and the current growth narrative rests on Alani Nu and international expansion — turns out to be independently corroborated by the company's own Q1 2026 disclosures (§3.3), even though that framing wasn't used as an input to any number above.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) CELH's next earnings report (Q2 2026, not yet dated as of this session — Q1 2026 was reported 2026-05-07) — particularly whether the CELSIUS-brand standalone growth rate (6% YoY in Q1 2026) stabilizes, recovers, or decelerates further, and whether Rockstar's retail-sales decline (−13% YoY in Q1 2026) continues; (b) 2+ consecutive quarters of GAAP Net Margin/ROIC improvement toward this framework's scoring thresholds, which would meaningfully move the Profitability sub-score; (c) any specific, citable pricing-power or switching-cost evidence for the CELSIUS or Alani Nu brands, which could move the Moat sub-score; (d) a guidance revision (up or down); (e) a management change or material further M&A; (f) a >15% stock-price move with no identified cause (CELH is down ~34% YTD, but that decline has an identified, gradual cause — a sustained downtrend, not a single unexplained jump — so it does not itself constitute this trigger).
- Absent any of the above, future Telegram mentions of CELH should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Data gaps flagged (Rule 0 / "never invent")

- **`yfinance`'s `curl_cffi` backend unusable this session** (documented TLS `Recv failure: Connection reset by peer`, consistent with prior 2026-07-19 sessions) — worked around via direct `requests`-based calls to Yahoo Finance's `quoteSummary` and `fundamentals-timeseries` endpoints (crumb-authenticated), which succeeded reliably. No financial figure below was estimated or invented to compensate.
- **`get_price_snapshot` returned a one-session-stale price** ($29.98, actually Thursday 2026-07-16's close) rather than the true most recent trade ($28.99, Friday 2026-07-17's close) — caught and corrected via `get_price_history` and an independent Yahoo Finance cross-check, flagged here as a recurring tool-reliability note for future sessions run near a weekend/holiday.
- **Total Debt discrepancy between two Yahoo data modules** (`financialData`: $675.881M vs. `fundamentals-timeseries` quarterly: $668.881M, both as of 2026-03-31) — likely an operating-lease-liability inclusion difference between the two vendor constructs. Used the larger (more conservative, i.e. produces a higher Net Debt/EBITDA) figure; does not change any sub-score's bucket.
- **No primary-source (SEC filing or company press release) citation was found for a specific ACV (All Commodity Volume) / retail-outlet-count figure for the PepsiCo distribution partnership** — only found in secondary analytics articles that could not be independently verified against a primary source this session; accordingly this was **not** credited as Moat Signal evidence (Switching Costs or Scale) despite being referenced in secondary sources, consistent with this framework's cited-evidence bar.
- **No quantified organic (ex-acquisition) 3-year revenue CAGR was computed** — the company does not disclose a clean pro-forma organic growth series, and this session did not construct one, consistent with "never invent or estimate financial data." The Growth sub-score uses the literal reported-revenue CAGR (flagged in §3.3 as M&A-inflated); the robustness check in §3.4 shows the ultimate FAIL conclusion does not depend on resolving this gap.
- Forward PE (14.65×), Trailing PE (67.4×, distorted by the thin TTM earnings base), and PEG (0.30×) were pulled for context/citation only — not scored, since Phase 02 was never reached.

---

## 8. Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every company that files with EDGAR.
- **Composite Score** — This framework's single ranking number (0.0–100.0) blending the Quality Score and Valuation Score 50/50 — not computed for CELH since it never clears the 80.0+ Quality Score gate.
- **Dollar share (tracked channels)** — A CPG market-share metric: retail sales in dollars as a percentage of category retail sales, measured across the subset of stores covered by retail-scanner-data panels. CELH's combined portfolio held ~20.9% dollar share of the US energy-drink category in Q1 2026 — the sole credited Moat Signal this session.
- **DSD (Direct-Store-Delivery)** — A distribution model delivering product directly to individual retail stores rather than through a retailer's central warehouse. PepsiCo distributes Celsius's brands this way — a real commercial arrangement, but not credited as a Moat Signal this session for lack of a specific, citable cost-per-unit-vs-smaller-competitors comparison.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. CELH's TTM ratio is a strong 168.55%.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. CELH's TTM gross margin is 49.62%, up from 41.44% in FY2022.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of weighted score; none fired for CELH this session (see §3.2).
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. CELH cleared only 1 of the framework's 5 cited-evidence moat signals this session.
- **Net Debt/EBITDA** — Net debt divided by EBITDA — a leverage ratio; this framework's primary balance-sheet-risk gate. CELH's is a comfortable 0.42×.
- **Net income attributable to common stockholders** — Net income after subtracting amounts owed to preferred stockholders. CELH's figure runs below its plain Net Income because of dividends/accretion on PepsiCo's convertible preferred stock — this session used the larger, plain Net Income figure for scoring, flagged explicitly.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit. CELH's TTM Net Margin is 5.85%, thin relative to the framework's 30%-cap scoring scale.
- **Quality Score** — This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. CELH scored **63.1**.
- **ROIC** — Return on Invested Capital — how efficiently a company turns invested capital into profit. CELH's TTM ROIC is ~11.78%.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. Caught a one-session-stale price this session (§1, §7).
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked this session, since Phase 01 failed first, but cited in the header per the standard session template).

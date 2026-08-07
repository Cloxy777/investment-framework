# New Position Evaluation — CELH (Celsius Holdings, Inc., Nasdaq)

**Task type:** NEW POSITION (Telegram-scan trigger, unattended/scheduled run — Routine 6)
**Date:** 2026-08-07
**10Y US Treasury Yield:** 4.69% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-08-06 — normal FRED reporting lag)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §4). For reference only, the bracket in force would be **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current CELH portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); no CELH row in the holdings table).
**Prior coverage:** [watchlist/not-in-portfolio/CELH/CELH-2026-07-19.md](../watchlist/not-in-portfolio/CELH/CELH-2026-07-19.md) — Phase 01 FAIL, Quality Score 63.1 (fails the 80.0+ gate), robustness-checked ceiling of 75.1 under the most generous plausible assumptions. See [sessions/2026-07-19-new-position-celh.md](2026-07-19-new-position-celh.md) for the full prior derivation.
**Sector:** Consumer Staples / Beverages — functional/better-for-you energy drinks (CELSIUS, Alani Nu, Rockstar Energy brand portfolio).
**Filer type:** US domestic filer, SEC CIK 0001341766. Listed on Nasdaq (CELH). Fiscal year ends 31 December. Most recent quarterly filing: **Q2 2026 10-Q** (quarter ended 2026-06-30, filed 2026-08-06 — two days before this session). Most recent annual filing: FY2025 Form 10-K.
**First-use jargon decode:** see closing Glossary (§9).

---

## 0. Why this session exists — trigger source

Telegram channel **FinnInvestChannel**, post **#3066** (2026-08-07T18:16:14Z), claims Rockstar Energy founder Russ Savage disclosed owning roughly 4.7% of Celsius Holdings, said following a weak earnings report that management needs to change, offered to become CEO himself, and says he bought shares at $30. **Per Rule 0, this post is a trigger only — not a data source.** CELH already has a prior watchlist entry ([2026-07-19](../watchlist/not-in-portfolio/CELH/CELH-2026-07-19.md), Phase 01 FAIL), so per [watchlist/README.md](../watchlist/README.md)'s "significant change" rule, this session runs because a Rule 9 fundamental-event trigger fired (CELH reported Q2 2026 earnings on 2026-08-06, two days before this post) — not merely because of the post's substance.

**Independent verification (context only, not used as a scored input):** a `WebSearch` this session found the trigger's substance is independently corroborated by multiple mainstream outlets (CNBC, Yahoo Finance, ZeroHedge, and others) reporting the same day: Russ Savage, who sold Rockstar Energy to PepsiCo for over $4B in 2020, has built a stake of roughly 4.7% of Celsius Holdings (started accumulating in March 2026 in the low-$30s), is publicly calling for CEO John Fieldly's removal, and has offered to step in as CEO himself, citing "too many management layers and insufficient accountability." **No SEC Schedule 13D/13G filing from Savage was found on CELH's EDGAR filing history as of this session** (most recent SC 13G/A on file is dated 2024-09-10) — but a stake below the 5% ownership threshold does not itself require a 13D/13G filing, so the absence of a filing neither confirms nor disconfirms the reported 4.7% figure; it is simply unverified by primary filing as of this session. **No management change has been announced by the company** — the 8-K furnishing Q2 2026 earnings (filed 2026-08-06, the same day as the activist reporting) is signed by "John Fieldly, Chief Executive Officer," and the earnings release quotes him as "Chairman and CEO." This activist/governance situation is real and current, but (a) it is not itself a scored financial input under this framework, and (b) as shown below, it is moot to this session's outcome — CELH fails the Quality Score gate on its underlying fundamentals well before any qualitative governance question would matter.

Sources: [CNBC](https://www.cnbc.com/2026/08/07/rockstar-energy-founder-celsius-stake-ceo.html), [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/russ-savage-calls-celsius-holdings-173400926.html), [ZeroHedge](https://www.zerohedge.com/markets/celsius-shares-crash-revenue-misses-estimates)

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

**Contract disambiguation:** `search_contracts("CELH")` returned the same 3 matches as the 2026-07-19 session: **NASDAQ:CELH, contract_id 71364351, "CELSIUS HOLDINGS INC", country_code US** (the correct primary listing, used throughout), a Mexican-exchange (MEXI) cross-listing, and `CELT` (an unrelated leveraged-ETF decoy).

**Price action context:** CELH reported Q2 2026 earnings before market open on 2026-08-06 (EPS $0.36 vs. $0.42 consensus, a −13.9% miss) and closed that session at **$23.77**, down from $29.15 the day before — a roughly −18.5% one-day drop on 32.4M shares volume (vs. a ~9.2M 3-month average), consistent with a genuine earnings-reaction move, not an unexplained gap. The next session (2026-08-07, today) opened at $23.96 and rallied sharply intraday — this is the CNBC-reported bounce coinciding with the Savage stake story becoming public.

**Live price fetched via `get_price_snapshot`:** last trade **$27.56** at timestamp 1786133542 → **2026-08-07 20:12:22 UTC (4:12:22pm ET)**, i.e. a post-market print roughly 12 minutes after the 4:00pm ET regular-session close (`is_close: false` — genuinely the most current available trade, not a stale snapshot; the 07-19 session's stale-snapshot issue does not recur here).

**Cross-check via `get_price_history` (1-day, 5-min bars, extended hours):** regular-session close bar (16:00:00 ET / 20:00:00 UTC) = **$27.79**; the next several 5-min bars drift down to $27.56–27.58 by 20:10–20:12 UTC, matching the IBKR snapshot.

**Independent cross-check via a direct Yahoo Finance `quoteSummary` pull** (crumb-authenticated `requests` session, since `yfinance`'s `curl_cffi` backend again failed with the same TLS `Recv failure: Connection reset by peer` documented in prior sessions — see §2): `regularMarketPrice` **$27.77** at `regularMarketTime` 1786132801 UTC (20:00:01 UTC, the official close print) and `postMarketPrice` **$27.50** at `postMarketTime` 1786133658 UTC (20:14:18 UTC). All three independent prints ($27.56 IBKR, $27.77 Yahoo regular close, $27.50 Yahoo post-market) agree within about a quarter, over a ~14-minute window spanning the close — no stale-snapshot or cross-source discrepancy this session.

| Field | Value | Detail |
|---|---|---|
| **Live price used** | **$27.56** | IBKR last trade, 2026-08-07 20:12:22 UTC — the most current available print (post-market, ~12 min after the regular close), per this framework's standing convention (see "After-hours trading" in the Glossary) of using the most current print as the Rule 0 price of record when the market has already closed for the day |
| Regular-session close (2026-08-07) | $27.79 | For reference — the official 4:00pm ET close, used interchangeably with the live price below since the two differ by only $0.23 |
| Prior close (2026-08-06, post-earnings) | $23.77 | Day of the Q2 2026 earnings miss |
| 52-week high | $66.74 (IBKR `misc_statistics`, consistent with Yahoo `fiftyTwoWeekHigh` $66.74) |
| 52-week low | $23.555–$23.84 (IBKR $23.555, Yahoo $23.84 — both reflect this week's post-earnings low, a new 52-week low, undercutting the 07-19 session's $27.47 low) |
| Price 52 weeks ago (`open_52w`) | $51.01 |
| YTD change | −39.75% (IBKR `year_to_date_change`) |
| Today's regular-session change | +16.83% (Yahoo `regularMarketChangePercent`), +15.94% (IBKR `change_pct`) — small definitional difference in reference price, both confirm a large one-day rebound |
| Market cap (at live price) | ~$7.10B (Yahoo `marketCap`, $7,099,132,928 at the $27.77 reference print) |

**Live price used throughout this session: $27.56.**

---

## 2. Data Source Note

`yfinance`'s `curl_cffi` HTTP backend again failed with a TLS-level `Recv failure: Connection reset by peer` error, the same documented, recurring issue noted in the 2026-07-19 session and others. Worked around via direct `requests`-based calls to Yahoo Finance's `quoteSummary` (price, summaryDetail, financialData, defaultKeyStatistics, earnings, earningsTrend, calendarEvents, incomeStatementHistoryQuarterly, cashflowStatementHistoryQuarterly, balanceSheetHistoryQuarterly) and `fundamentals-timeseries` (annual and quarterly revenue, gross profit, EBIT, EBITDA, net income, operating cash flow, capex, free cash flow, total debt, cash, invested capital, pretax income, tax provision) endpoints, crumb-authenticated via `query2.finance.yahoo.com/v1/test/getcrumb`.

**Material data-quality finding this session, flagged and corrected:** Yahoo's `fundamentals-timeseries` TTM ("trailing") fields for the window ending 2026-06-30 showed **`trailingEBIT` and `trailingEBITDA` as identical** ($195.947M each) — structurally implausible, since EBITDA should exceed EBIT by the D&A add-back, and a real discrepancy also showed up against Yahoo's own quarterly EBIT breakout for Q1 2026 ($149.379M) vs. the SEC-filed GAAP `OperatingIncomeLoss` for the same quarter ($138.993M). This looks like a vendor data-population lag on the most recent quarter's EBIT/EBITDA fields, not a real fact about the business. **Rather than use these unreliable vendor fields, this session reconstructed EBIT, EBITDA, and Invested Capital directly from primary-source SEC EDGAR data** — the company's own XBRL-tagged financial facts (`data.sec.gov/api/xbrl/companyfacts/CIK0001341766.json`) and the actual filed Q2 2026 10-Q (`celh-20260630.htm`, filed 2026-08-06) and its cash-flow statement, cross-checked line-by-line against the quarter-by-quarter arithmetic (each quarter's figure ties to the cumulative 6-month/9-month/annual figures reported in the same or adjacent filings — shown in §3.1). Where Yahoo's TTM Revenue, Gross Profit, Net Income, Pretax Income, and Tax Provision fields were cross-checked against this same SEC-derived arithmetic, they matched exactly (see §3.1 footnotes) — only the EBIT/EBITDA/Invested Capital fields were unreliable this session, and only those were replaced.

The 10-Year Treasury yield was sourced directly from FRED's public CSV endpoint (`fredgraph.csv?id=DGS10`). A `WebSearch` was run for the Savage/activist context (§0) and cross-referenced against SEC EDGAR's own filing history for CELH.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Raw financial inputs (all sourced, cited; primary SEC data used for EBIT/EBITDA/Invested Capital per §2)

**Annual figures (unchanged from the 2026-07-19 session — no new fiscal year has closed since then; re-confirmed against SEC XBRL `companyfacts` this session):**

| Fiscal Year | Revenue | Gross Profit | Gross Margin | Net Income | FCF | FCF/NI |
|---|---|---|---|---|---|---|
| FY2022 | $653.604M | $270.869M | 41.44% | −$187.282M | $99.918M | n/m (loss year) |
| FY2023 | $1,318.014M | $633.139M | 48.04% | $226.801M | $123.785M | 54.60% |
| FY2024 | $1,355.630M | $680.207M | 50.18% | $145.074M | $239.508M | 165.10% |
| FY2025 | $2,515.269M | $1,267.333M | 50.39% | $107.999M | $323.375M | 299.42% |

**Quarterly figures used to reconstruct the current TTM window (2026-07-01…2026-06-30), all SEC XBRL `companyfacts` tags, each individual quarter derived by subtracting the prior cumulative period from the next (e.g. Q4 2025 = FY2025 10-K minus the 9-month 2025 10-Q) and cross-checked internally where two filings both report the same quarter:**

| Quarter | Revenue | Gross Profit | Op. Income (EBIT, GAAP) | D&A | Net Income | Pretax Income | Tax | OCF | CapEx |
|---|---|---|---|---|---|---|---|---|---|
| Q3 2025 (Jul–Sep) | $725.106M | $372.279M | −$79.999M | $8.786M | −$61.014M | −$88.031M | −$27.017M | $331.801M | $10.345M |
| Q4 2025 (Oct–Dec) | $721.628M | $341.830M | $26.065M | $8.935M | $24.739M | $22.606M | −$2.133M | −$119.438M | $10.528M |
| Q1 2026 (Jan–Mar) | $782.615M | $378.067M | $138.993M | $9.134M | $110.099M | $137.536M | $27.437M | $73.723M | $7.916M |
| Q2 2026 (Apr–Jun) | $817.925M | $393.688M | $75.255M | $10.104M | $55.293M | $69.530M | $14.237M | $222.543M¹ | $17.066M¹ |
| **TTM sum** | **$3,047.274M** | **$1,485.864M** | **$160.314M** | **$36.959M** | **$129.117M** | **$141.641M** | **$12.524M** | **$508.629M** | **$45.855M** |

¹ Q2 2026 standalone OCF/CapEx derived by subtracting the directly-reported Q1 2026 figure from the directly-reported six-month-2026 figure in the Q2 2026 10-Q's cash flow statement ($296.266M 6mo OCF − $73.723M Q1 OCF = $222.543M; $24.982M 6mo CapEx − $7.916M Q1 CapEx = $17.066M). The six-month figures themselves are read directly off the filed cash flow statement (`Net cash provided by operating activities $296,266` thousand; `Purchase of property, plant and equipment $(24,982)` thousand, six months ended June 30, 2026) — not derived or estimated.

**Cross-checks (TTM sums above vs. independently-reported Yahoo `trailing*` fields, all matching exactly):** Revenue $3,047.274M ✓, Gross Profit $1,485.864M ✓, Net Income $129.117M ✓, Pretax Income $141.641M ✓, Tax Provision $12.524M ✓. (EBIT/EBITDA intentionally **not** cross-checked against Yahoo's unreliable fields — see §2.)

**TTM derived metrics:**

| Metric | TTM value | Calculation |
|---|---|---|
| Gross Margin | **48.76%** | $1,485.864M / $3,047.274M |
| EBITDA | **$197.273M** | EBIT $160.314M + D&A $36.959M |
| Net Margin | **4.237%** | $129.117M / $3,047.274M |
| Effective tax rate | **8.842%** | $12.524M / $141.641M |
| NOPAT | **$146.139M** | EBIT $160.314M × (1 − 0.08842) |
| Free Cash Flow | **$462.774M** | OCF $508.629M − CapEx $45.855M |
| FCF/NI conversion | **358.41%** | $462.774M / $129.117M |

**Flagged (earnings-quality note, not a data gap):** Q2 2026's standalone OCF ($222.543M) is unusually large relative to net income ($55.293M) for a single quarter, driven substantially by working-capital swings disclosed in the 10-Q's cash flow statement — most notably a **−$255.328M** "Accrued distributor termination fees" outflow *and* offsetting inflows including "+$145.121M Accrued promotional allowance," "+$67.172M Deferred revenue," "+$63.230M Accounts payable," and "+$61.384M Prepaid expenses and other current assets." These are real, GAAP-filed cash flow line items (not invented), but they are lumpy, M&A-integration-related working-capital timing effects rather than a repeatable run-rate of operating cash generation — flagged here per this framework's "show every calculation, flag earnings quality" discipline, though the FCF Quality sub-score (§3.3) is computed off the literal reported ratio, consistent with quality-scoring.md's formula (which doesn't provide for a working-capital normalization adjustment).

**Balance sheet (as of 2026-06-30, per the Q2 2026 10-Q, SEC XBRL):** Total Debt (`LongTermDebtCurrent` $7.000M + `LongTermDebtNoncurrent` $667.850M) = **$674.850M**; Cash (`CashAndCashEquivalentsAtCarryingValue`) = **$631.234M** → **Net Debt = $43.616M**. Stockholders' Equity = **$1,199.584M**.

**Invested Capital (2026-06-30):**
```
Invested Capital = Total Debt + Stockholders' Equity − Cash
                  = $674.850M + $1,199.584M − $631.234M
                  = $1,243.200M
```
**Methodology note:** this formula (standard debt + equity − cash) differs from the un-transparent "Invested Capital" field Yahoo's `fundamentals-timeseries` returned and that the 2026-07-19 session cited ($1,919.643M as of 2026-03-31, which reverse-engineers to `LongTermDebtNoncurrent + StockholdersEquity` with **no cash subtraction** — i.e. it doesn't net out the company's substantial cash balance). This session uses the standard, cash-adjusted formula since it is directly reconstructable from SEC-filed data with a fully shown formula, consistent with "show every calculation" — cited explicitly here rather than silently switching methodology. Applying the same cash-adjusted formula to the 2026-03-31 balance sheet for comparison would give Invested Capital of $1,377.442M (Total Debt $675.881M + Equity $1,250.762M − Cash $549.201M) vs. Yahoo's $1,919.643M — a real definitional gap between the two approaches, not a fundamentals change.

**ROIC (TTM basis):**
```
ROIC = NOPAT / Invested Capital = $146.139M / $1,243.200M = 11.76%
```

### 3.2 Hard disqualifier check (fails regardless of weighted score)

Per quality-scoring.md's 2026-08-05 rolling-window clarification, both "consecutive years" tests below are evaluated against the **current** trailing window, not any past session's window.

| Hard disqualifier | CELH data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF positive in all four of the last four fiscal years: FY2022 +$99.918M, FY2023 +$123.785M, FY2024 +$239.508M, FY2025 +$323.375M, and TTM +$462.774M. | **Does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | Net Debt $43.616M ÷ TTM EBITDA $197.273M = **0.2211×** — comfortably under 2.5×, and materially improved from the 2026-07-19 session's 0.42× (lower net debt, a large cash balance despite $124.5M of 1H 2026 share buybacks). | **Does not fire.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years** | Current 2-year window: FY2024 165.10%, FY2025 299.42% — both well above 70%; TTM 358.41%. The single sub-70% year on record (FY2023, 54.60%) is now 3 fiscal years back, outside the current rolling window. | **Does not fire.** |

**No hard disqualifiers fire.** As in the 2026-07-19 session, CELH's balance sheet and cash-conversion metrics are genuinely strong — the gate failure below (§3.4) is a weighted-score failure, not a disqualifier failure.

### 3.3 Sub-score calculation

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((4.237/30)×100, 0, 100) = **14.12**. ROIC_Component = clamp((11.76/30)×100, 0, 100) = **39.18**. Profitability_Score = (14.12+39.18)/2 = **26.65**. (No FCF-positivity cap — FCF-positive all 4 years on file.) **Down from 29.39 in the 2026-07-19 session** — TTM Net Margin fell from 5.85% to 4.24% (Q3 2025's loss quarter is now fully in the trailing window, and Q2 2026's net income nearly halved YoY, $55.3M vs. $99.9M, on margin compression + step-up SG&A from the now-fully-consolidated Rockstar integration). | **26.65** |
| **Margins (15%)** | GrossMargin_Score = clamp((48.76/80)×100, 0, 100) = **60.95** (TTM gross margin). **5-point trend:** 41.44% (FY2022) → 48.04% (FY2023) → 50.18% (FY2024) → 50.39% (FY2025) → **48.76% (TTM, i.e. now trailing the completed FY2025 figure)** — the plateau flagged as "ticking down slightly" in the 07-19 session has continued into a clearer contraction: the company's own Q2 2026 release states gross margin fell **340bps YoY** (51.5%→48.1%) in the quarter and **356bps YoY** (51.8%→48.2%) for 1H 2026, attributed to "higher promotional and incentive activity as a percentage of revenue and channel mix" plus rising aluminum/commodity costs, partially offset by freight/integration efficiencies (Celsius Holdings Q2 2026 earnings release, `ex9912q2026.htm`). **No +10 trend bonus** — as before, the bonus is conditioned on expansion *while below* the 40% static threshold; CELH remains above 40% throughout, and the trend is now contracting, not expanding, regardless. | **60.95** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $653.604M → FY2025 $2,515.269M) = (2,515.269/653.604)^(1/3) − 1 = **+56.71%/yr** (fixed annual base, unchanged from the 07-19 session since no new fiscal year has closed). Growth_Score(raw) = clamp((56.71/25)×100, 0, 100) = **100.0** (clamped, ceiling — again overwhelmingly inorganic; Alani Nu and Rockstar together were ~53% of Q2 2026 revenue, per §3.3 detail below). **−10 structural-deceleration modifier applied this session** (not applied in 07-19): the company's own Q2 2026 earnings release states **CELSIUS-brand revenue *declined* approximately 11.7% YoY** in the quarter (vs. +6% organic *growth* reported for Q1 2026 in the prior session) and **approximately 4% YoY for 1H 2026** — a swing from growth to outright decline over two consecutive quarters, explicitly attributed by the company to a cluster of structural/deliberate actions taken together: "increased trade and promotional investment, shipment timing related to inventory rebalancing, softness in the club channel, a planned moderation in innovation activity..., and SKU optimization initiatives" (Celsius Holdings Q2 2026 earnings release). Rockstar-brand retail sales also declined a further **13% YoY** (matching the 07-19 session's Q1 2026 figure — now a second consecutive quarter of the same-magnitude decline, reinforcing rather than contradicting a structural read). Unlike the 07-19 session — where the only evidence was a single quarter's deceleration and a third-party source explicitly hedging ("structural evidence is sparse") — this session has two consecutive quarters of company-disclosed, explicitly-attributed core-brand deterioration, which meets the "documented... structural (not cyclical)" bar the modifier requires. Growth_Score = clamp(100.0 − 10, 0, 100) = **90.0**. No +10 TAM modifier applied (international revenue is real but only ~4% of total revenue, and the dominant, better-documented finding this session is negative). | **90.0** |
| **Balance Sheet (15%)** | Net Debt $43.616M ÷ TTM EBITDA $197.273M = 0.2211× → clamp(100×(1−0.2211/4), 0, 100) = **94.47** (improved from 89.39 in 07-19 — lower net debt, larger cash cushion). | **94.47** |
| **Moat Signal (15%)** | See evidence table below — **0 of 5** signals cleared the cited-evidence bar this session (down from 1/5 in 07-19 — see reasoning below). Moat_Score = (0/5)×100 = **0.0** | **0.0** |
| **FCF Quality (10%)** | TTM FCF/NI = $462.774M / $129.117M = 358.41% → clamp(((3.5841−0.40)/0.60)×100, 0, 100) = clamp(530.7, 0, 100) = **100.0** (clamped) | **100.0** |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable or growing | **Reconsidered from TRUE (07-19) to FALSE this session.** Celsius's combined-portfolio dollar share of the US RTD energy category was **20.1%** for the 13-week period ended 2026-06-28 (per the company's own Q2 2026 earnings release) — **down from the ~20.9% figure reported for the Q1 2026 period** in the 07-19 session, a real sequential decline, not just noise given it's corroborated by declines in 2 of the portfolio's 3 brands this quarter: CELSIUS-brand-alone dollar share ~9.5% (retail sales −2% YoY) and Rockstar dollar share ~1.9% (retail sales −13% YoY); only Alani Nu grew share (~8.7%, retail sales +55.7% YoY). Per this framework's "never invent... cited, not invented" bar, a *combined* figure that itself moved down quarter-over-quarter, alongside two of three constituent brands independently losing share, is not credibly described as "stable or growing" this quarter — marked **FALSE**, a genuine, evidence-driven change from the prior session's read, not a re-interpretation of the same facts. (Robustness check below shows this call does not change the ultimate gate outcome.) | **FALSE** |
| Brand premium | No new cited evidence of price increases sustained without volume loss was found this session for the CELSIUS brand; if anything, the company's own release cites *increased* promotional/trade investment (a margin-compressing, not premium-supporting, signal) as a driver of the quarter's results. Not credited. | **FALSE** |
| Network effect | Not applicable — a packaged/branded consumer beverage has no two-sided network-effect dynamic. | **FALSE** |
| Switching costs | No documented consumer- or retailer-side lock-in mechanism found with a citable source this session, same as 07-19. | **FALSE** |
| Scale cost advantage | Not re-examined in more depth this session given the more decisive Profitability-driven shortfall below; no new citable cost-per-unit-vs-smaller-competitors comparison surfaced. Not credited, consistent with 07-19's finding. | **FALSE** |

**Robustness check on the Moat call (per "no black-box outputs"):** crediting "Market share stable or growing" back to TRUE (i.e. Moat_Score = 20.0, matching the 07-19 session's read) moves the final Quality Score from 58.0 to 61.0 (see §3.4) — still 19.0 points short of the 80.0 gate. The gate outcome does not turn on this judgment call.

### 3.4 Final weighted Quality Score

```
Quality Score = (26.65 × 0.25) + (60.95 × 0.15) + (90.0 × 0.20) + (94.47 × 0.15) + (0.0 × 0.15) + (100.0 × 0.10)
              = 6.6634 + 9.1426 + 18.0 + 14.1709 + 0.0 + 10.0
              = 57.9769 → 58.0 (rounded to nearest 0.1)
```

**58.0 < 80.0 — fails the gate by 22.0 points**, a *wider* miss than the 2026-07-19 session's 16.9-point shortfall (63.1). No hard disqualifiers fire (§3.2); this is a weighted-score failure, driven primarily by a further-thinned Profitability sub-score (26.65, down from 29.39) and the Moat sub-score dropping to 0.0 (down from 20.0), partially offset by a stronger Balance Sheet sub-score (94.47, up from 89.39).

**Robustness check (showing the conclusion doesn't hinge on this session's most discretionary judgment calls):**
- **Moat Signal credited at TRUE for "market share stable/growing" (20.0, matching 07-19's read)** instead of 0.0: Quality Score = 57.9769 + 3.0 = **61.0**. Still fails by 19.0 points.
- **Growth Signal with no −10 structural-deceleration modifier applied** (i.e. Growth_Score = 100.0, matching how 07-19 treated the metric): Quality Score = 57.9769 + 2.0 = **60.0**. Still fails by 20.0 points.
- **Most generous combination tested** (Moat credited at its absolute ceiling of 100.0 — all 5 signals, an evidence-free, maximally generous reading — *and* Growth with no deceleration modifier, i.e. 100.0): Quality Score = 26.65×0.25 + 60.95×0.15 + 100.0×0.20 + 94.47×0.15 + 100.0×0.15 + 100.0×0.10 = **74.98**. Still fails by 5.0 points, even under assumptions this session's own evidence does not support.
- The gate fails under every combination tested — this session's headline conclusion rests on the Profitability, Margins, and Balance Sheet sub-scores, none of which are discretionary judgment calls (all are formula-driven off cited financial figures).

### Result: **Phase 01 FAIL — weighted Quality Score 58.0, misses the 80.0+ gate by 22.0 points.**

Per [new-position.md](../.claude/commands/new-position.md) step 2 and the identical instruction in this session's task brief: *"If it's below 80.0... stop there and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position, and do not place a limit order — unchanged from the 2026-07-19 session's conclusion, and the underlying case has **weakened, not strengthened**, since then. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring.

The triggering Telegram post's framing (an activist shareholder calling for a CEO change following a weak earnings report) is independently corroborated (§0) and is a real, live governance situation worth tracking qualitatively — but it doesn't change this session's outcome. Even if Russ Savage's characterization of the business ("too many management layers and insufficient accountability") turns out to be right, and even if a change in management materialized, this framework's Quality Score gate is a **fundamentals-first** test: the company's TTM Net Margin (4.24%) and ROIC (11.76%) remain thin, its combined-portfolio market share moved down (not up) this quarter with two of its three constituent brands independently losing share, and its core CELSIUS brand — the original moat/growth thesis — is now **shrinking** (−11.7% YoY in Q2 2026, −4% YoY for 1H 2026), not merely decelerating as the 07-19 session found. A management change alone does not repair any of these, and this framework does not speculate on hypothetical future turnarounds without documented evidence (a genuine Turnaround Sub-Gate evaluation, per [strategy.md](../framework/strategy.md) Upgrade 4, would require a demonstrated track record, insider buying, and other conditions not present here).

On the positive side, genuinely credited: the balance sheet strengthened further (Net Debt/EBITDA 0.22×, down from 0.42×), cash conversion remains very strong on a literal GAAP basis (FCF/NI 358.4% TTM, though flagged for working-capital lumpiness in §3.1), and Alani Nu continues to perform very well (+55.7% YoY retail sales). None of this is enough to offset the profitability, margin, and moat findings.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) CELH's Q3 2026 earnings report (not yet dated as of this session) — particularly whether the CELSIUS-brand decline (−11.7% YoY in Q2 2026) stabilizes, deepens, or reverses, and whether Rockstar's retail-sales decline (−13% YoY, now two consecutive quarters at that magnitude) persists; (b) a confirmed CEO/management change at Celsius Holdings (the Savage activist situation is unresolved as of this session — a real change of leadership, or a definitive company rejection/settlement, would each independently qualify as a Rule 9 "management change" trigger); (c) 2+ consecutive quarters of GAAP Net Margin/ROIC improvement toward this framework's scoring thresholds; (d) any specific, citable pricing-power or switching-cost evidence for the CELSIUS or Alani Nu brands; (e) a guidance revision (up or down); (f) material further M&A; (g) a >15% unexplained single-move price shock (this week's moves both have clearly identified causes — the earnings miss on 2026-08-06, the activist-news bounce on 2026-08-07 — so neither constitutes this trigger on its own).
- Absent any of the above, future Telegram mentions of CELH should be logged as "last checked, no change" per the watchlist's convention.

---

## 7. Data gaps flagged (Rule 0 / "never invent")

- **`yfinance`'s `curl_cffi` backend again unusable this session** (documented, recurring TLS `Recv failure: Connection reset by peer`) — worked around via direct `requests`-based calls to Yahoo Finance's `quoteSummary` and `fundamentals-timeseries` endpoints, which succeeded. No financial figure below was estimated or invented to compensate.
- **Yahoo's `fundamentals-timeseries` TTM EBIT/EBITDA fields for the window ending 2026-06-30 were internally inconsistent** (identical values, a data-population-lag artifact) — identified and **not used**; EBIT, EBITDA, and Invested Capital were instead reconstructed directly from SEC XBRL `companyfacts` and the filed Q2 2026 10-Q, with the full quarter-by-quarter arithmetic shown in §3.1, and cross-checked against every field Yahoo *did* report correctly (Revenue, Gross Profit, Net Income, Pretax Income, Tax Provision — all matched exactly). This is a genuine data-quality finding for the session, not a gap that stopped any calculation.
- **No SEC Schedule 13D/13G filing from Russ Savage was found on CELH's EDGAR history** as of this session (most recent filing of that type: 2024-09-10) — the reported ~4.7% stake is below the 5% ownership threshold that would mandate such a filing, so this is not evidence against the reported figure, just an unverified-by-primary-filing status, noted for completeness (§0). Not used as a scored input either way.
- **No quantified organic (ex-acquisition) 3-year revenue CAGR was computed**, same gap as 07-19 — the company does not disclose a clean pro-forma organic growth series. The Growth sub-score uses the literal reported-revenue CAGR (flagged in §3.3 as M&A-inflated, with a −10 structural-deceleration modifier applied this session on separately-documented evidence); the §3.4 robustness check shows the FAIL conclusion does not depend on resolving this gap.
- Forward PE (14.91×, per Yahoo `summaryDetail`) and trailing PE (120.74×, heavily distorted by the thin TTM earnings base) were pulled for context/citation only — not scored, since Phase 02 was never reached.

---

## 8. Comparison to the 2026-07-19 session

| | 2026-07-19 | 2026-08-07 (this session) | Direction |
|---|---|---|---|
| Live price | $28.99 | $27.56 | −4.9% |
| TTM Net Margin | 5.85% | 4.24% | Weaker |
| TTM ROIC | 11.78% | 11.76% | ~Flat |
| TTM Gross Margin | 49.62% | 48.76% | Weaker |
| Net Debt/EBITDA | 0.42× | 0.22× | Stronger |
| TTM FCF/NI | 168.55% | 358.41%¹ | Stronger (flagged, §3.1) |
| Combined dollar share | 20.9% (Q1 2026) | 20.1% (Q2 2026) | Weaker |
| CELSIUS-brand organic revenue | +6% YoY (Q1 2026) | −11.7% YoY (Q2 2026) | Materially weaker |
| Moat Signal | 20.0 (1/5) | 0.0 (0/5) | Weaker |
| **Quality Score** | **63.1** | **58.0** | **Weaker, still FAIL** |
| Gate shortfall | −16.9 pts | −22.0 pts | Wider miss |

¹ See §3.1's earnings-quality flag — driven substantially by lumpy working-capital timing, not a repeatable improvement in underlying cash generation.

**Conclusion unchanged (PASS), and the case has gotten weaker, not stronger, since the last evaluation** — despite a further-strengthened balance sheet, the core profitability and brand-growth deterioration this quarter more than offset it.

---

## 9. Glossary

- **8-K** — The "current report" a US public company must file with the SEC within days of a material event — used here to furnish (via Exhibit 99.1) CELH's Q2 2026 earnings press release ahead of the fuller 10-Q.
- **10-Q (Quarterly Report)** — The quarterly financial-disclosure report a US public company files with the SEC — CELH's Q2 2026 10-Q (filed 2026-08-06) is the primary source for this session's balance-sheet and cash-flow figures.
- **Activist (shareholder)** — An investor who takes a meaningful stake in a public company specifically to push for a change in strategy, capital allocation, or management, rather than as a passive holding. The trigger for this session (Russ Savage's ~4.7% CELH stake and public call for CEO change) is a real, independently-corroborated activist situation, though not itself a scored input under this framework.
- **After-hours / post-market trading** — Trading that happens after a US exchange's regular session closes (4:00pm ET) but before the next day's regular session opens — thinner volume/wider spreads, but still a genuine, live traded price. Used as this session's Rule 0 price of record ($27.56, ~12 minutes after the 2026-08-07 close) since it was the most current print available.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every company that files with EDGAR.
- **Composite Score** — This framework's single ranking number (0.0–100.0) blending the Quality Score and Valuation Score 50/50 — not computed for CELH since it never clears the 80.0+ Quality Score gate.
- **Dollar share (tracked channels)** — A CPG market-share metric: retail sales in dollars as a percentage of category retail sales in scanner-tracked stores. CELH's combined portfolio held 20.1% dollar share of the US RTD energy category in Q2 2026, down from 20.9% in Q1 2026 — a factor in this session marking the "market share stable or growing" Moat Signal FALSE.
- **D&A** — Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit.
- **EPS surprise** — The percentage by which actual reported earnings-per-share differs from the analyst consensus estimate. CELH's Q2 2026 EPS ($0.36) missed the $0.42 consensus by −13.9%, the "weak earnings report" referenced in this session's trigger.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. CELH's TTM ratio is 358.41%, flagged this session as inflated by lumpy working-capital timing rather than a clean improvement in cash quality.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of weighted score; none fired for CELH this session (§3.2).
- **Invested Capital** — The capital (debt + equity, minus non-operating cash) a company has deployed into its operations — the denominator of ROIC. This session recomputed it directly from SEC-filed balance sheet data using a cash-adjusted formula, flagged as differing from the un-transparent Yahoo vendor field used in the 07-19 session (§3.1).
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. CELH cleared 0 of the framework's 5 cited-evidence moat signals this session, down from 1 of 5 previously.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator of ROIC, representing operating profit adjusted for the tax a company actually pays.
- **Net Debt/EBITDA** — Net debt divided by EBITDA — a leverage ratio; this framework's primary balance-sheet-risk gate. CELH's is 0.22×, comfortably under the 2.5× threshold and improved from 0.42× last session.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit. CELH's TTM Net Margin is 4.24%, thinner than the 5.85% found in the 2026-07-19 session.
- **Quality Score** — This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. CELH scored **58.0** this session (was 63.1 on 2026-07-19).
- **RTD (Ready-to-Drink)** — A beverage sold pre-mixed and ready for immediate consumption, as opposed to a powder/concentrate — the category classification (RTD energy) used in the retail-tracking market-share data cited in this session.
- **ROIC** — Return on Invested Capital — how efficiently a company turns invested capital into profit. CELH's TTM ROIC is 11.76%, essentially flat vs. 11.78% last session.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **SC 13D / SC 13G** — SEC forms an investor must file upon acquiring beneficial ownership above 5% of a public company's stock (13D for an activist stake with intent to influence control, 13G for a passive stake). No such filing exists yet for Savage's reported ~4.7% CELH stake — below the 5% threshold that would require one.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **TTM (Trailing Twelve Months)** — The most recent four reported quarters summed together — this session's TTM window covers Q3 2025 through Q2 2026 (2025-07-01 through 2026-06-30).
- **XBRL** — eXtensible Business Reporting Language — the structured, machine-readable data format the SEC requires public companies to tag their financial statements in, allowing figures to be pulled programmatically and precisely rather than parsed from prose/HTML.

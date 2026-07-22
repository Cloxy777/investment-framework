# New Position Evaluation — STM (STMicroelectronics N.V., NYSE)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 2026-07-19
**10Y US Treasury Yield:** 4.57% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-07-16 — normal FRED reporting lag; fetched directly via `fredgraph.csv?id=DGS10`)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §3.4). For reference only, the bracket in force would be **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current STM portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); no STM row in the holdings table).
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is STM's first-ever evaluation under this framework.
**Sector:** Technology / Semiconductors — analog, MEMS & sensors, power & discrete (including silicon carbide), embedded processing (microcontrollers), and RF products, serving automotive, industrial, personal-electronics, and communications end markets.
**Filer type:** Netherlands-incorporated (Schiphol), SEC foreign private issuer, CIK 0000932787. Directly listed (not via ADR) on NYSE (STM) and Euronext Paris (STMPA). Fiscal year ends 31 December. Most recent annual filing: FY2025 Form 20-F.
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

Telegram channel **bolshegold**, post **bolshegold/9795** (~09:46 UTC, 2026-07-19), listed STM among "companies reporting earnings this week / under observation." STM's next earnings report is confirmed (Yahoo Finance `earningsDate`) for **2026-07-23** — consistent with the post's framing. Per [telegram-scan.md](../.claude/commands/telegram-scan.md)'s convention ("no watchlist entry exists at all → `/new-position <TICKER>`"), this session was triggered regardless of the mention's substance — STM had zero prior coverage in this repo. **Per Rule 0, no claim from the triggering post is used as financial data anywhere below** — the post is only the reason this ticker was looked at; every figure in this session is independently fetched/sourced and cited.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

**Contract disambiguation:** `search_contracts("STM")` returned 50+ matches, including several decoys sharing the same ticker root: Stabilus SE (Germany, `STM` on IBIS), Sunstone Metals Ltd (Australia, ASX:STM), Stadlauer Malzfabrik AG (Austria, `STM1`), Straumann Holding AG (Switzerland, `STMN`), Stamps.com (`STMP`, delisted/inactive), an unrelated ARCA-listed instrument (`STHH`), the same company's own Euronext Paris listing (`STMPA`) and Frankfurt listing (`SGMR`), and several unrelated mutual funds/ETFs (`STMGX`, `STMCX`, `KSTR`, etc.). The correct instrument is **NYSE:STM, contract_id 12460, "STMICROELECTRONICS NV-NY SHS", country_code US** — confirmed as the primary US listing of STMicroelectronics N.V.

**Data-quality catch:** `get_price_snapshot` initially returned `last: $62.77` (flagged `is_close: true`). Cross-checked against `get_price_history` (daily bars, last 5 sessions) before using this figure, since today (2026-07-19) is a Saturday and markets are closed — and the two didn't agree:

| Date | Close |
|---|---|
| 2026-07-13 | $68.47 |
| 2026-07-14 | $70.13 |
| 2026-07-15 | $67.75 |
| **2026-07-16** | **$62.77** |
| **2026-07-17** | **$62.06** |

`get_price_snapshot`'s "last" value ($62.77) was actually **Thursday 2026-07-16's close**, one session stale — not the true most recent trade. The correct, most recent live price is **Friday 2026-07-17's close: $62.06** (confirmed independently against Yahoo Finance's `regularMarketPrice`, timestamped 2026-07-17 20:00:03 UTC, i.e. the 4:00pm ET NYSE close). Flagging this explicitly per Rule 0's spirit ("never use a stale price") — this is exactly the class of error Rule 0 exists to catch, so the extra cross-check was run rather than taking the snapshot tool's first answer at face value.

| Field | Value | Detail |
|---|---|---|
| **Live price used** | **$62.06** | Friday 2026-07-17 close (most recent trade; market closed for the weekend on 2026-07-19, the session date) |
| 52-week high | $81.41–$81.42 | IBKR `misc_statistics` / Yahoo `fiftyTwoWeekHigh`, consistent |
| 52-week low | $20.98 (IBKR) / $21.11 (Yahoo) | Minor cross-source discrepancy, both cited |
| Price 52 weeks ago (`open_52w`) | $32.37 | Stock is up sharply (+89.1% per Yahoo's `52WeekChange`) over the trailing year despite a sharp pullback from its 52-week high in the last 13 weeks |
| 13-week low | $43.77 | Stock has fallen from the ~$70 area to the low-$60s in the last week alone — high pre-earnings volatility (report due 2026-07-23) |

**Live price used throughout this session: $62.06.**

---

## 2. Data Source Note

`yfinance`'s `curl_cffi` HTTP backend failed with the same TLS-level `Recv failure: Connection reset by peer` documented in prior sessions (e.g. TSLA, 2026-07-19) — confirmed via direct `curl_cffi` test calls to Yahoo's `quoteSummary` endpoint, reproducible even with the proxy's CA bundle explicitly set (`CURL_CA_BUNDLE`/`REQUESTS_CA_BUNDLE`). A plain `curl`/Python-`requests` session to the same Yahoo hosts succeeded cleanly (confirmed via the proxy's own `/__agentproxy/status`, which shows no relay failures) — so this session fetched Yahoo Finance's `quoteSummary` (assetProfile, summaryDetail, financialData, defaultKeyStatistics, incomeStatementHistory/Quarterly, cashflowStatementHistory, earnings, earningsTrend) and `fundamentals-timeseries` (multi-year annual FCF, OCF, CapEx, EBIT, EBITDA, revenue, net income, invested capital, total debt) endpoints directly via `requests`, obtaining a crumb token from `query2.finance.yahoo.com/v1/test/getcrumb` first. This is a primary-aggregator data source (Yahoo Finance, sourced from the company's own SEC/20-F filings), not an invented or estimated figure anywhere below. Cross-internal-consistency was checked (e.g. summed quarterly net income ties to the reported TTM net-income-to-common figure exactly: $147M) as an integrity check on the pulled data.

The 10-Year Treasury yield was sourced directly from FRED's public CSV endpoint (`fredgraph.csv?id=DGS10`). Two supplementary `WebSearch` queries were run for Moat Signal evidence (market share, switching-cost mechanism) — both cited individually in §3.3.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Raw financial inputs (all sourced, cited)

**Annual figures (Yahoo Finance `fundamentals-timeseries`, sourced from STM's own 20-F filings):**

| Fiscal Year | Revenue | Gross Profit | Gross Margin | EBIT | Net Income | Net Margin | Op. Cash Flow | CapEx | FCF | FCF/NI |
|---|---|---|---|---|---|---|---|---|---|---|
| FY2022 | $16,128M | $7,635M | 47.34% | $4,499M | $3,960M | 24.55% | $5,202M | −$3,636M | $1,566M | 39.55% |
| FY2023 | $17,286M | $8,287M | 47.94% | $4,818M | $4,211M | 24.36% | $5,992M | −$4,536M | $1,456M | 34.57% |
| FY2024 | $13,269M | $5,220M | 39.34% | $1,963M | $1,557M | 11.73% | $2,965M | −$3,181M | **−$216M** | **−13.87%** |
| FY2025 | $11,800M | $3,999M | 33.89% | $455M | $166M | 1.41% | $2,152M | −$2,204M | **−$52M** | **−31.33%** |

**TTM snapshot (Q2 2025–Q1 2026, Yahoo `financialData`/`defaultKeyStatistics`):** Revenue $12,378M, Net Income to Common $147M (Net Margin 1.19% — verified by independently summing the four reported quarters: −$97M + $237M − $30M + $37M = $147M, ties exactly), Gross Margin 33.955%, EBITDA $2,490M, Operating Cash Flow $2,112M, **Free Cash Flow −$360.5M**, ROA 1.52%, ROE 0.91%, Debt/Equity 15.3%.

**Balance sheet (most recent quarter, 2026-03-31, per `financialData`):** Total Debt $2,783M, Total Cash $4,571M → **Net Debt = 2,783 − 4,571 = −$1,788M (net cash position)**.

**ROIC (computed, FY2025 annual basis — most recent complete fiscal year; quarterly EBIT/invested-capital breakdowns aren't available from this data source):**
```
NOPAT (FY2025) = EBIT × (1 − tax rate) = $455M × (1 − 0.17) = $377.65M
Invested Capital (FY2025) = $19,961M
ROIC = 377.65 / 19,961 = 1.892%
```
**Flagged:** Net Margin above uses TTM (1.19%); ROIC uses FY2025 annual (1.89%) due to data-availability constraints (no reliable quarterly EBIT/invested-capital series from this source). Both bases are low enough that this mismatch doesn't affect the sub-score's conclusion.

### 3.2 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | STM data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF was positive in FY2022 (+$1,566M) and FY2023 (+$1,456M), then turned **negative in both FY2024 (−$216M) and FY2025 (−$52M)** — two consecutive negative years immediately preceding this session. Only 1 of the most recent 3 fiscal years (FY2023) was positive, failing the "3 consecutive years positive" requirement this disqualifier mirrors from the Phase 01 pre-screen filter ("FCF positive 3 consecutive years"). | **FIRES.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | Net Debt is **negative** (−$1,788M, net cash as of 2026-03-31) — comfortably inside the threshold regardless of EBITDA's magnitude. | **Does not fire.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | Ratio was **negative** in both FY2024 (−13.87%) and FY2025 (−31.33%) — the two most recent fiscal years. **CapEx was declining, not growing, across this exact window** (FY2023 $4,536M peak → FY2024 $3,181M → FY2025 $2,204M), so there is no "documented growth-capex" explanation available for these two years specifically — the negative FCF instead reflects operating cash flow collapsing (FY2023 $5,992M → FY2025 $2,152M) faster than capex could be cut, consistent with a severe cyclical semiconductor downturn (see §3.3 Growth discussion), not an escalating investment program. (FY2022–FY2023's own sub-70% ratios, by contrast, *do* plausibly reflect documented growth capex — STM was mid-cycle on new 300mm-wafer and SiC fab capacity during that boom period, per company disclosures — but that carve-out doesn't rescue the two most recent years, which is what this check tests.) | **FIRES.** |

**Two hard disqualifiers fire independently.** Per [quality-scoring.md](../framework/quality-scoring.md): *"These mirror the existing Phase 01 non-negotiables — a weighted average can't average away an outright balance-sheet or cash-flow-quality failure."* The full weighted score is still computed below for transparency (per operating-brief.md's "no black-box outputs" rule), but the gate fails regardless of what that arithmetic produces.

### 3.3 Sub-score calculation (shown in full despite the hard-disqualifier fail, per "no black-box outputs")

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((1.19/30)×100, 0, 100) = **3.97** (TTM Net Margin). ROIC_Component = clamp((1.892/30)×100, 0, 100) = **6.31** (FY2025 ROIC, see §3.1). Profitability_Score = (3.97+6.31)/2 = **5.14**. (The "cap at 40.0 if not FCF-positive 3yr" rule would apply given §3.2's finding, but is non-binding here since the raw score is already far below 40.) | **5.14** |
| **Margins (15%)** | GrossMargin_Score = clamp((33.955/80)×100, 0, 100) = **42.44** (TTM gross margin). **4-year trend:** 47.34% (FY2022) → 47.94% (FY2023) → 39.34% (FY2024) → 33.89% (FY2025) — a clear **structural contraction**, consistent with STM's IDM (Integrated Device Manufacturer) capital structure: fixed costs at its own owned fabs aren't absorbed as well when factory utilization falls in a downturn. **No +10 trend bonus** (bonus only applies to an *expanding* trend; this one is sharply contracting). | **42.44** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $16,128M → FY2025 $11,800M) = (11,800/16,128)^(1/3) − 1 = **−9.89%/yr**. Growth_Score = clamp((−9.89/25)×100, 0, 100) = clamp(−39.6, 0, 100) = **0.0** (floored). **No structural-deceleration −10 modifier applied** (judgment call, flagged, doesn't change the already-floored result): the decline appears **cyclical** — a broad semiconductor automotive/industrial **inventory correction (destocking)** cycle — rather than structural/competitive, based on analyst consensus (Yahoo `earningsTrend`) projecting a sharp snap-back: FY2026 revenue growth guided/consensus ~+21.8%, FY2027 ~+17.67%. **No +10 TAM-expansion modifier applied** either (no cited documented evidence found this session). Either way the modifier is moot: it's clamped to the 0.0 floor regardless. | **0.0** |
| **Balance Sheet (15%)** | Net Debt = −$1,788M (net cash, most recent quarter) ÷ TTM EBITDA $2,490M → ratio = −0.718× → clamp(100×(1−(−0.718)/4), 0, 100) = clamp(117.96, 0, 100) = **100.0** (clamped) | **100.0** |
| **Moat Signal (15%)** | See evidence table below — **2 of 5** signals cleared the cited-evidence bar. Moat_Score = (2/5)×100 = **40.0** | **40.0** |
| **FCF Quality (10%)** | TTM FCF/NI = −$360.5M / $147M = **−245.24%** → clamp(((−2.4524−0.40)/0.60)×100, 0, 100) = clamp(−475.4, 0, 100) = **0.0** (clamped) | **0.0** |

**Moat signal evidence (cited, per signal — all five checked against the framework's required cited-evidence bar):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable or growing | **TRUE (for one specific sub-segment).** STMicroelectronics is the **market-leading silicon carbide (SiC) power-device supplier by revenue share, at 32.6%** (TrendForce data via [semiconductor-today.com](https://www.semiconductor-today.com/news_items/2024/jun/trendforce-200624.shtml), reported June 2024, most recent figure found this session; flagged as somewhat dated — a fresher 2025/2026 figure wasn't located). This is a specific-segment (not company-wide) share claim — STM's overall revenue has declined sharply (see Growth above), so this signal is scoped narrowly to the SiC power business rather than the whole company. | **TRUE** |
| Brand premium | No cited evidence of price increases sustained without volume loss found this session — semiconductor components in STM's core analog/MCU/power lines are generally price-competitive commodity-adjacent products, not premium-branded. | **FALSE** |
| Network effect | Not applicable — an IDM chip manufacturer selling discrete/analog/MCU components has no classic two-sided network-effect dynamic. | **FALSE** |
| Switching costs | **TRUE.** Automotive/industrial semiconductor design-ins require **AEC-Q100** qualification, a process that "often stretches to 2+ years" for safety-critical components — once a part is designed into a vehicle platform, re-qualifying a competing part is costly and slow, a documented mechanism cited via competitive-analysis sources ([PortersFiveForce.com](https://portersfiveforce.com/blogs/competitors/st), [dcf-analysis.com](https://dcf-analysis.com/products/stm-porters-five-forces-analysis)). STM is also cited as serving over 200,000 customers worldwide, consistent with a broad, sticky automotive/industrial installed base. Flagged: these are competitive-analysis aggregator sources, not a primary regulatory/company filing — cited as the best evidence found this session, not a first-tier source. | **TRUE** |
| Scale cost advantage | No cost-per-unit data found this session showing STM retains a manufacturing cost edge over smaller/newer competitors (Infineon, onsemi, Wolfspeed compete directly in SiC/power). Not credited without that specific citation. | **FALSE** |

### 3.4 Final weighted Quality Score

```
Quality Score = (5.14 × 0.25) + (42.44 × 0.15) + (0.0 × 0.20) + (100.0 × 0.15) + (40.0 × 0.15) + (0.0 × 0.10)
              = 1.285 + 6.366 + 0.0 + 15.0 + 6.0 + 0.0
              = 28.65 → 28.7 (rounded to nearest 0.1)
```

**28.7 < 80.0 — fails the gate by 51.3 points, and two independent hard disqualifiers fire regardless (§3.2).** This is not a close call and is not sensitive to any single judgment call in this session: even crediting the two most favorable sub-scores at their maximum (Balance Sheet 100.0, reflecting a genuinely strong net-cash position, and Moat 40.0), the other four sub-scores (Profitability 5.14, Margins 42.44, Growth 0.0, FCF Quality 0.0) reflect a company mid-way through a severe cyclical semiconductor downturn: revenue down ~27% from its FY2023 peak, gross margin compressed ~14 points, and free cash flow negative for two straight years.

### Result: **Phase 01 FAIL — weighted Quality Score 28.7, misses the 80.0+ gate by 51.3 points. Two hard disqualifiers also fire independently** (not FCF-positive for 3+ consecutive years; FCF/Net Income conversion <70% for 2+ consecutive years without a documented growth-capex explanation for those specific years).

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... or a hard disqualifier fires, stop there and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position, and do not place a limit order. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring, per the Phase 03 table in [strategy.md](../framework/strategy.md) (Composite Score is a precondition for that table applying at all).

This is not a verdict that STMicroelectronics' underlying franchise (SiC power-device leadership, a broad automotive/industrial MCU and analog portfolio, a genuine net-cash balance sheet) is worthless, or that the current cyclical trough is permanent — analyst consensus itself projects a sharp FY2026–FY2027 revenue recovery (+21.8%/+17.67%). It is a verdict that, on the specific, cited, filed financial facts available today (a two-year run of negative free cash flow, a >250% year-over-year net-income collapse, gross margin down ~14 points from its FY2023 peak, and thin single-digit profitability), STM does not currently clear this framework's strict, quantitative definition of "high quality" — a bar set deliberately high per the 2026-06-29 gate decision, precisely so that a cyclically-depressed name doesn't get waved through on the promise of a future recovery that hasn't shown up in filed numbers yet. STM's upcoming 2026-07-23 earnings report (the same event the triggering Telegram post referenced) is the natural next checkpoint (see §6).

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) STM's 2026-07-23 earnings report (the specific event the triggering Telegram post referenced) — particularly whether FCF turns positive again and whether gross margin stabilizes or continues contracting; (b) 2+ consecutive quarters of resumed revenue growth consistent with the cyclical-recovery thesis in §3.3/§4; (c) a sustained reversal of the gross-margin compression trend; (d) a guidance revision (up or down); (e) a management change or material M&A/strategic-investment event; (f) a >15% stock-price move with no identified cause (note: STM has already moved >15% intra-week heading into this session — from ~$70 to ~$62 — but that move has an identified cause, pre-earnings positioning/de-risking, not an unexplained trigger).
- Absent any of the above, future Telegram mentions of STM should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Data gaps flagged (Rule 0 / "never invent")

- **`yfinance`'s `curl_cffi` backend unusable this session** (documented TLS `Recv failure: Connection reset by peer`, consistent with prior sessions) — worked around via direct `requests`-based calls to Yahoo Finance's `quoteSummary` and `fundamentals-timeseries` endpoints (crumb-authenticated), which succeeded reliably. No financial figure below was estimated or invented to compensate.
- **`get_price_snapshot` returned a one-session-stale price** ($62.77, actually Thursday 2026-07-16's close) rather than the true most recent trade ($62.06, Friday 2026-07-17's close) — caught and corrected via `get_price_history`, flagged here as a tool-reliability note for future sessions using this same MCP tool near a weekend/holiday.
- **No quantified growth-vs-maintenance CapEx split** is disclosed by STM for FY2022–FY2023 (the years where a growth-capex explanation is plausibly available) — the §3.2 disqualifier judgment call for those two years rests on a qualitative, industry-knowledge-based inference (STM's known 300mm-wafer/SiC fab capacity buildout during that period), not a precise Upgrade 1 (Owner Earnings) calculation. Doesn't change the ultimate FAIL conclusion, since the two most recent years (FY2024–FY2025, where CapEx was falling) are what actually fires the disqualifier.
- **SiC market-share figure (32.6%) is TrendForce data reported June 2024** (i.e., based on full-year-2023 shipments) — a fresher 2025/2026 figure wasn't located this session. Cited as the best available evidence, flagged as dated.
- **ROIC computed on a FY2025 annual basis, not a true TTM basis** — quarterly EBIT and invested-capital breakdowns weren't available from this session's data source (Yahoo's quarterly income-statement module returned mostly-blank EBIT/operating-income fields for this non-US filer). Flagged in §3.1; doesn't change the sub-score's conclusion given how low the figure is on either basis.
- Forward PE (24.87×), Trailing PE (387.9×, distorted by the depressed TTM earnings base), and PEG (0.45×) were pulled for context/citation only — not scored, since Phase 02 was never reached.

---

## 8. Glossary

- **AEC-Q100** — An automotive-electronics reliability qualification standard components must pass before an automaker will design them into a vehicle; re-qualifying a competing part typically takes 2+ years — the documented mechanism behind STM's "switching costs" Moat Signal finding above.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every company that files with EDGAR.
- **Composite Score** — This framework's single ranking number (0.0–100.0) blending the Quality Score and Valuation Score 50/50 — not computed for STM since it never clears the 80.0+ Quality Score gate.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit.
- **Fabless** — A chip company that designs semiconductors but outsources manufacturing to a foundry — the business model STM's competitive landscape includes, but STM itself is primarily an IDM (see below).
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. Negative for STM in both FY2024 and FY2025.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. Negative in both of STM's last two fiscal years.
- **Form 20-F** — The annual report US-listed foreign private issuers file with the SEC — STM's equivalent of a US company's Form 10-K.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. STM's has compressed from ~47.9% (FY2023) to ~33.9% (FY2025).
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score. Two fire for STM this session — see §3.2.
- **IDM (Integrated Device Manufacturer)** — A semiconductor company that both designs and manufactures its own chips in its own fabs, distinct from a fabless company. STM operates this way, which is capital-intensive and a source of operating leverage (margin compresses sharply when factory utilization falls).
- **Invested Capital** — The total capital (debt + equity, netted for cash) put to work in a business — the denominator in this framework's ROIC calculation.
- **Inventory correction (destocking)** — A cyclical phase where customers work down excess inventory built up during a prior shortage/boom, temporarily depressing a supplier's reported revenue below underlying end-demand. Cited as the basis for treating STM's FY2024–FY2025 revenue decline as cyclical, not structural.
- **MCU (Microcontroller)** — A small, self-contained processor chip used to run embedded control logic in a device — a core STM product line.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. STM cleared 2 of the framework's 5 cited-evidence moat signals this session.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; negative means net cash. STM carries a net cash position of ~$1.79B.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit. STM's TTM net margin is 1.19%.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. STM scores **28.7**.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it into profit. STM's FY2025 ROIC is ~1.89%.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. Caught a one-session-stale price this session (§1, §7).
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **SiC (Silicon Carbide)** — A semiconductor material used for high-efficiency power electronics (EV drivetrains, industrial power). STM is the market-leading SiC power-device supplier by revenue share (32.6%, TrendForce 2023 data) — its one clearly-credited Moat Signal.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).

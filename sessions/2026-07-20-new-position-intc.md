# New Position Evaluation — INTC (Intel Corporation, NASDAQ)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 2026-07-20
**10Y US Treasury Yield:** 4.57% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-07-16 — normal FRED reporting lag; fetched directly via `fredgraph.csv?id=DGS10`)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §3.4). For reference only, the bracket in force would be **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current INTC portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); no INTC row in the holdings table).
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is INTC's first-ever evaluation under this framework.
**Sector:** Technology / Semiconductors — x86 CPUs (client computing and data-center), plus an internal+external contract-manufacturing division (Intel Foundry / IFS). Filed segments: CCG (Client Computing Group), DCAI (Data Center & AI), Intel Foundry.
**Filer type:** US-domiciled (Santa Clara, CA), SEC domestic filer, CIK 0000050863. Directly listed on NASDAQ (INTC). Fiscal year ends late December (FY2025 ended 2025-12-27). Most recent annual filing: FY2025 Form 10-K.
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

Telegram channel **FinnInvestChannel**, post **#2958** (~08:02 UTC, 2026-07-20): *"На цьому тижні звіти в повному розпалі. Nokia, Google, IBM, NOW, Intel, Tesla та інші. Готуйтесь до нових netflix-ів"* ("Earnings reports are in full swing this week. Nokia, Google, IBM, NOW, Intel, Tesla and others. Get ready for new Netflix-style moves.") — a generic, forward-looking earnings-calendar reminder, not a claimed Rule 9 event (no actual results, guidance revision, etc. have happened yet). Per Rule 0, **no claim from the triggering post is used as financial data anywhere below** — the post is only the reason this ticker was looked at.

Of the six companies named (NOK, GOOG, IBM, NOW, INTC, TSLA), **INTC is the only one with no prior watchlist entry at all** (confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/`). Per this framework's established convention (see e.g. the 2026-07-19 STM, TSLA, RYAAY, CELH sessions), a ticker with zero prior coverage triggers a full `/new-position` evaluation regardless of the mention's substance — a lower bar than the "documented fundamental trigger" required to re-review an already-covered ticker. That is the sole reason this session exists; the other five names already have watchlist entries and are handled separately by the orchestrating scan.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

**Contract disambiguation:** `search_contracts("INTC")` returned several decoys sharing the same ticker root: Intel's own Mexico (MEXI), Switzerland (EBS, two listings — `INTC` and `INTCUSD`), and Canada CDR (TSE) cross-listings; two unrelated leveraged single-stock ETF products (`INTW` "Granite 2x Long INTC ETF", `LINT` "Direxion Daily INTC Bull 2x ETF", `INT`/"Corgi INTC 2x Daily ETF"); two Nasdaq/NYSE-listed *indices* referencing INTC (`INTSY`, `NY2LINTC`), not tradable equities; and two entirely unrelated Chinese/Hong Kong-listed companies that happen to share the "Intco" name root (Intco Medical Technology, Intco Recycling Resources) plus an unrelated ADR (Intchains Group, `ICG`). The correct instrument is **NASDAQ:INTC, contract_id 270639, "INTEL CORP", country_code US** — confirmed as the primary US listing.

**Live price fetched:** `get_price_snapshot` returned `last: $96.17` (`is_close: false` — genuine live intraday trade, market open Monday 2026-07-20). Cross-checked against `get_price_history` (daily bars, trailing month): Friday 2026-07-17 close was $95.04, and today's price action (open $92.075, day range $89.59–$98.05 per `misc_statistics`/Yahoo) is consistent with a live, actively-trading session — no stale-price flag this session (contrast with the STM/2026-07-19 session, where a weekend snapshot needed correction).

| Field | Value | Detail |
|---|---|---|
| **Live price used** | **$96.17** | Live intraday trade, Monday 2026-07-20 (IBKR `get_price_snapshot`, `is_close: false`) |
| Prior close (2026-07-17) | $95.04 / $96.98 | Two sources disagree by ~$1.94 (IBKR daily-bar close $95.04 vs. Yahoo `regularMarketPreviousClose` $96.98) — both cited; live intraday price used regardless, not either close |
| 52-week high | $142.35 | IBKR `misc_statistics`, matches Yahoo `fiftyTwoWeekHigh` exactly |
| 52-week low | $18.965 (IBKR) / $18.97 (Yahoo) | Consistent |
| Price 52 weeks ago (`open_52w`) | $23.22 | Stock is up **+308.6%** over the trailing year (Yahoo `52WeekChange`) — an extraordinary run driven by 2025's CEO change, US government equity stake, and Nvidia investment (see §3.3, §7) |
| 1-month range | $89.59–$142.35 | Sharp pullback from the June 2026 high (~$140) to the mid-$90s over the past month — high volatility, no single identified cause pinned down this session (pre-earnings positioning is plausible; INTC's next earnings date was not independently confirmed this session — flagged in §7 data gaps) |

**Live price used throughout this session: $96.17.**

---

## 2. Data Source Note

`yfinance`'s `curl_cffi` HTTP backend failed with the same TLS-level `Recv failure: Connection reset by peer` documented in prior sessions (e.g. STM, TSLA, 2026-07-19). Worked around via direct `requests`-based calls to Yahoo Finance's `quoteSummary` (assetProfile, summaryDetail, financialData, defaultKeyStatistics, incomeStatementHistory, cashflowStatementHistory, balanceSheetHistory, earningsTrend) and `fundamentals-timeseries` (multi-year annual + quarterly Revenue, Gross Profit, EBIT, EBITDA, Net Income, FCF, OCF, CapEx, Total Debt, Cash, Invested Capital, Stockholders' Equity, pretax income, tax provision) endpoints, obtaining a crumb token from `query2.finance.yahoo.com/v1/test/getcrumb` after a cookie warm-up (`fc.yahoo.com` + `finance.yahoo.com/quote/INTC`). This is a primary-aggregator data source (Yahoo Finance, sourced from Intel's own SEC 10-K/10-Q filings), not an invented or estimated figure anywhere below.

**Internal-consistency checks run:** TTM Net Margin computed by summing the four most recent reported quarterly net-income figures (−$2,918M − $2,918M... — see §3.1) ties to `financialData.profitMargins` (−5.90%) exactly. TTM Operating Cash Flow computed the same way ($9,980M) ties to `financialData.operatingCashflow` exactly. **Two discrepancies were found and are flagged rather than silently resolved:** (a) Yahoo's summary-level `financialData.freeCashflow` (−$8.30B TTM) does not match the figure obtained by summing the four most recent quarterly `quarterlyFreeCashFlow` values (−$3.12B) or by independently subtracting summed quarterly CapEx from summed quarterly OCF (also −$3.12B, internally consistent with the OCF match above) — this session uses the internally-consistent **−$3.12B** computed figure, not the unreconciled summary field; (b) `financialData.ebitda` (TTM $14.17B) does not match the sum of the four most recent quarterly `quarterlyEBITDA` values ($11.42B) — both bases are shown in §3.1/§3.3, and the Balance Sheet sub-score below uses the FY2025 full-audited-year EBITDA ($14.354B, directly reported, not derived) as the primary basis, consistent with this session's general preference for full-fiscal-year audited figures over reconstructed TTM sums where the two disagree. Neither discrepancy changes this session's ultimate conclusion (see §3.4).

The 10-Year Treasury yield was sourced directly from FRED's public CSV endpoint (`fredgraph.csv?id=DGS10`). A `general-purpose` research subagent ran multiple `WebSearch` queries for Moat Signal and Growth/TAM evidence — every claim below is cited individually with source and date in §3.3/§3.4/§7; the subagent's full findings (with all citations) are preserved as the evidentiary basis for this session's Moat Signal and Growth calls.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Raw financial inputs (all sourced, cited)

**Annual figures (Yahoo Finance `fundamentals-timeseries`, sourced from Intel's own 10-K filings):**

| Fiscal Year | Revenue | Gross Profit | Gross Margin | EBIT | EBITDA | Net Income | Op. Cash Flow | CapEx | FCF |
|---|---|---|---|---|---|---|---|---|---|
| FY2022 | $63,054M | $26,866M | 42.61% | $8,264M | $21,299M | $8,014M | $15,433M | −$24,844M | **−$9,411M** |
| FY2023 | $54,228M | $21,711M | 40.04% | $1,640M | $11,242M | $1,689M | $11,471M | −$25,750M | **−$14,279M** |
| FY2024 | $53,101M | $17,345M | 32.66% | −$10,176M | $1,203M | −$18,756M | $8,288M | −$23,944M | **−$15,656M** |
| FY2025 | $52,853M | $18,375M | 34.77% | $2,648M | $14,354M | −$267M | $9,697M | −$14,646M | **−$4,949M** |

**Free cash flow was negative in every one of the last four fiscal years** — see §3.2, hard disqualifier #3.

**TTM snapshot (Q2 2025–Q1 2026, computed from quarterly `fundamentals-timeseries`, cross-checked against `financialData` where available):** Revenue $53,763M (Q2'25 $12,859M + Q3'25 $13,653M + Q4'25 $13,674M + Q1'26 $13,577M — ties to `financialData.totalRevenue` $53.76B), Net Income to Common −$3,174M (−$2,918M − $591M... summed; ties to `defaultKeyStatistics.netIncomeToCommon` −$3.17B exactly), **Net Margin −5.90%** (ties to `financialData.profitMargins` exactly), Gross Margin 37.20% (`financialData.grossMargins`; own computed sum-of-quarters cross-check: $19,050M / $53,763M = 35.43% — a ~1.8pp discrepancy flagged, not material to the sub-score conclusion), Operating Cash Flow $9,980M (ties to `financialData.operatingCashflow` exactly), **Free Cash Flow −$3,119M** (own computed figure, used per §2's discrepancy note — NOT the unreconciled `financialData.freeCashflow` −$8.30B figure).

**Balance sheet (most recent quarter, 2026-03-31):** Total Debt $45,031M, Total Cash $17,247M → **Net Debt = 45,031 − 17,247 = $27,784M** (net debt, not net cash).
**Balance sheet (FY2025 year-end, 2025-12-31, full audited year):** Total Debt $46,585M, Total Cash $14,265M → **Net Debt = $32,320M.**

**ROIC (FY2025 annual basis — most recent complete, audited fiscal year; used per the same data-reliability rationale as the 2026-07-19 STM session, since a clean TTM EBIT/invested-capital pairing isn't reliably reconstructable from quarterly data given the discrepancies noted in §2):**
```
Effective tax rate (FY2025, Yahoo annualTaxRateForCalcs) = 21%
NOPAT (FY2025) = EBIT × (1 − tax rate) = $2,648M × (1 − 0.21) = $2,091.9M
Invested Capital (FY2025) = $160,866M
ROIC = 2,091.9 / 160,866 = 1.30%
```
**Flagged:** TTM EBIT (sum of Q2'25–Q1'26 quarterly EBIT: −$2,542M + $4,856M + $621M − $3,682M = **−$747M**, i.e. negative) is far more volatile and materially worse than the FY2025 full-year figure (+$2,648M) — the Q1 2026 quarter alone carried a −$3,682M EBIT swing. Both bases are shown; the FY2025 annual basis is used for the formula below as the more stable, fully-audited figure, but the quarterly volatility itself is additional (unfavorable) qualitative evidence of earnings instability, noted here for completeness.

### 3.2 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | INTC data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF was **negative in all four of the last four fiscal years**: FY2022 (−$9,411M), FY2023 (−$14,279M), FY2024 (−$15,656M), FY2025 (−$4,949M). Not merely "fewer than 3 consecutive positive years" — Intel has not posted a single year of positive FCF in this entire lookback window. | **FIRES — unambiguously.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | Using FY2025 full-year audited figures: Net Debt $32,320M ÷ EBITDA $14,354M = **2.252×** — under the 2.5× threshold. Cross-checked against the most-recent-quarter net debt ($27,784M) paired with either EBITDA basis from §2 (TTM summary $14.174B → 1.960×; own computed TTM sum-of-quarters $11.421B → 2.433×) — **every basis checked lands under 2.5×.** | **Does not fire** (on any basis tested). |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | **Formula edge case, flagged explicitly rather than mechanically applied:** in FY2022 and FY2023 (positive Net Income), the ratio is cleanly and decisively bad (FY2022: −9,411/8,014 = −117.5%; FY2023: −14,279/1,689 = −845.4% — both far below 70%). In FY2024 and FY2025 (**negative** Net Income), the mechanical ratio produces a mathematically positive but economically meaningless artifact (FY2024: −15,656/−18,756 = +83.5%; FY2025: −4,949/−267 = +1,853.6%) — a negative divided by a negative, which nominally "clears" 70% despite both cash flow and earnings being deeply negative in both years. This session does **not** rely on this disqualifier's mechanical output for FY2024–FY2025 (it would be misleading to credit a "pass" here), and does not need to: the FCF-positivity disqualifier above already fires cleanly and independently across the same years. Judgment call flagged per "no black-box outputs." | **Fires cleanly in FY2022–FY2023; mechanically ambiguous in FY2024–FY2025 (not relied upon — moot given the disqualifier above).** |

**At least one hard disqualifier fires unambiguously** (FCF-positivity, all four years). Per [quality-scoring.md](../framework/quality-scoring.md): *"These mirror the existing Phase 01 non-negotiables — a weighted average can't average away an outright balance-sheet or cash-flow-quality failure."* The full weighted score is still computed below for transparency (per operating-brief.md's "no black-box outputs" rule), but the gate fails regardless of what that arithmetic produces.

### 3.3 Sub-score calculation (shown in full despite the hard-disqualifier fail, per "no black-box outputs")

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((−5.90/30)×100, 0, 100) = **0.0** (floored — TTM Net Margin, negative). ROIC_Component = clamp((1.30/30)×100, 0, 100) = **4.33** (FY2025 annual ROIC, §3.1). Profitability_Score = (0.0+4.33)/2 = **2.17**. (The "cap at 40.0 if not FCF-positive 3yr" rule would apply given §3.2's finding, but is non-binding — the raw score is already far below 40.) | **2.17** |
| **Margins (15%)** | GrossMargin_Score = clamp((37.20/80)×100, 0, 100) = **46.50** (TTM gross margin, `financialData.grossMargins`). **4-year trend:** 42.61% (FY2022) → 40.04% (FY2023) → 32.66% (FY2024) → 34.77% (FY2025) — a net **structural contraction** of ~7.8pp over the window, despite a partial single-year rebound from the FY2024 trough. **No +10 trend bonus** (the bonus requires an *expanding* multi-year trend; the net 3-year direction here is a decline, and TTM 37.20% is not below 40% in a way that would even trigger the "below-40%-but-expanding" carve-out cleanly regardless). | **46.50** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $63,054M → FY2025 $52,853M) = (52,853/63,054)^(1/3) − 1 = **−5.72%/yr**. Growth_Score = clamp((−5.72/25)×100, 0, 100) = clamp(−22.9, 0, 100) = **0.0** (floored). **Structural-deceleration evidence found and cited** (documented, not inferred): Mercury Research Q1 2026 data shows AMD's overall x86 CPU market share reaching a record 32.6% (Intel down to 67.4%, from 72.9% a year earlier); AMD server-CPU revenue share reached 46.2% of the segment (Mercury Research, via [Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/amd-reaches-46-percent-of-server-x86-cpu-revenue-intel-still-controls-70-percent-of-the-consumer-pc-market-share)); Intel's Gaudi AI-accelerator line has materially missed its own sales targets against NVIDIA/AMD (see Moat Signal table and §7). **No +10 TAM-expansion modifier applied** — the AI PC and Intel Foundry TAM narratives exist (§7) but external Foundry revenue remains under $350M against a >$10B annual segment operating loss, i.e. not yet evidenced in the filed financials. **Neither modifier changes the result** — already clamped to the 0.0 floor regardless of which (or no) modifier applies, exactly as in the 2026-07-19 STM session's Growth sub-score. | **0.0** |
| **Balance Sheet (15%)** | FY2025 annual basis (primary, per §3.1/§2): Net Debt $32,320M ÷ EBITDA $14,354M = 2.252× → clamp(100×(1−2.252/4), 0, 100) = clamp(43.7, 0, 100) = **43.7**. Cross-checked against two alternate bases (both also under the 2.5× disqualifier threshold, see §3.2): most-recent-quarter net debt ÷ `financialData` TTM EBITDA → 1.960× → Score 51.0; most-recent-quarter net debt ÷ own computed sum-of-quarters TTM EBITDA → 2.433× → Score 39.2. All three bases land within a ~12-point band (39.2–51.0); the FY2025 full-audited-year figure is used as the "headline" number below. | **43.7** |
| **Moat Signal (15%)** | See evidence table below — **1 of 5** signals cleared the cited-evidence bar. Moat_Score = (1/5)×100 = **20.0** | **20.0** |
| **FCF Quality (10%)** | **Formula edge case, judgment call applied (documented, per "no black-box outputs"):** TTM FCF/NI = −$3,119M / −$3,174M = **+98.27%** — a *positive* ratio produced only because both cash flow and net income are negative (a negative divided by a negative). Mechanically plugging this into the formula would produce clamp(((0.9827−0.40)/0.60)×100, 0, 100) = **97.1**, which would flatteringly reward a company that is burning cash and losing money on both counts — the opposite of what this sub-score is meant to measure. This session overrides that mechanical output to **0.0**, consistent with the sub-score's actual intent (cash-generation quality) rather than the letter of the formula in this specific negative/negative edge case; flagged explicitly in §7 as a data-gap/judgment-call rather than an invented number. (For reference: the two years with positive Net Income, FY2022 and FY2023, both mechanically floor to 0.0 cleanly with no ambiguity — −117.5% and −845.4% respectively — so this override only affects the FY2024/FY2025-driven TTM figure, not the two clean years.) | **0.0** |

**Moat signal evidence (cited, per signal — all five checked against the framework's required cited-evidence bar; full sourced findings from this session's research pass):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable or growing | **FALSE.** Mercury Research Q1 2026 data: Intel's overall x86 CPU market share fell to 67.4% (down from 68.6% the prior quarter, down from 72.9% a year earlier), while AMD reached a record 32.6% ([Mercury Research data via Substack](https://substack.com/@hypertechinvest/note/c-271783284); corroborated by [The Register, 4 Jun 2026](https://www.theregister.com/systems/2026/06/04/amd-takes-a-third-of-server-cpu-market-as-shipments-grow/5251283)). In the higher-margin server/data-center segment specifically, AMD's server CPU *revenue* share reached 46.2% ([Tom's Hardware, 2026](https://www.tomshardware.com/pc-components/cpus/amd-reaches-46-percent-of-server-x86-cpu-revenue-intel-still-controls-70-percent-of-the-consumer-pc-market-share)) — a documented, multi-quarter, negative share trend, most severe in the segment that matters most for margin. | **FALSE** |
| Brand premium | **FALSE.** Intel raised list prices on select Xeon/consumer CPUs in 2025–2026 (e.g. Xeon 6980P list price +12%, per [Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/intel-confirms-price-hikes-on-select-consumer-and-server-cpus-citing-supply-costs-and-demand-select-xeon-processors-now-over-usd1-000-more-expensive)) and TrendForce reported Q1 2026 server CPU ASPs +27% YoY ([TrendForce, 27 Apr 2026](https://www.trendforce.com/news/2026/04/27/news-intel-reportedly-sells-chips-typically-scrapped-as-cpu-demand-surges-1q26-server-cpu-asps-up-27/)) — but both are explicitly attributed to an industry-wide supply shortage and richer product mix, not demonstrated brand-driven pricing power independent of competition. Against that: consolidated gross margin fell sharply (Q2 2025 27.5% vs. Q2 2024 35.4%, per [Futurum Group](https://futurumgroup.com/insights/intel-delivers-flat-q1-fy-2025-revenue-amid-ongoing-turnaround-efforts/)), and Intel's own FY2024 10-K cites "competitive pricing pressure" from AMD as a driver of gross-margin-dollar decline. No evidence found of sustained price increases *without* volume loss in a head-to-head competitive segment. | **FALSE** |
| Network effect | **FALSE (qualified).** No classic two-sided-marketplace network effect exists in a chip-manufacturing business. A software-ecosystem lock-in effect does exist (x86 runs the full Windows/enterprise-Linux stack natively) but it is explicitly **shared with AMD, not Intel-specific** — Intel and AMD jointly formed an "x86 Ecosystem Advisory Group" in Dec 2024 specifically to defend the *combined* x86 platform against ARM ([Hackaday, 21 Dec 2024](https://hackaday.com/2024/12/21/intel-terminates-x86s-initiative-after-formation-of-new-industry-group/); [Runtime.news](https://www.runtime.news/why-intel-and-amd-buried-their-differences-to-make-life-easier-for-software-developers-and-hold-off-a-common-enemy/)). Not credited as an Intel-specific competitive advantage over its direct competitor. | **FALSE** |
| Switching costs | **TRUE.** Two documented mechanisms: (1) x86 ISA/software-stack compatibility (shared with AMD, per above, but still a real cost to leaving x86 for ARM entirely); (2) semiconductor foundry qualification cycles — industry-wide, requalifying a device for an alternate foundry "takes 18–24 months minimum," plus mask-set NRE costs of $10–20M at advanced nodes ([Silicon Analysts, Foundry Engagement Guide, 2026](https://siliconanalysts.com/guide/foundry-engagement)). Flagged: switching costs are real but evidently not prohibitive for large buyers — AMD has still taken meaningful hyperscaler server share (see Market Share row above), indicating the moat is eroding, not impenetrable. Credited as documented per the framework's evidence bar, with this caveat noted. | **TRUE** |
| Scale cost advantage | **FALSE.** Intel's 2025 capex (~$14.6–18B) is roughly 3–4× smaller than TSMC's ($40.9B in 2025, guided to $60–64B for 2026 — [Industrial Info](https://www.industrialinfo.com/iirenergy/industry-news/article/chipmaker-tsmc-projects-2026-capex-will-reach-52-billion-56-billion--352061); [BigGo Finance](https://finance.biggo.com/news/5784aaf1-fcbc-4f76-8856-491b9e7175f6)). Intel Foundry's external revenue was only $307M for full-year 2025 against a $10.318B operating loss on $17.826B of total segment revenue ([Kavout](https://www.kavout.com/market-lens/intel-s-foundry-gamble-high-stakes-high-reward-and-a-divided-wall-street)) — i.e. no external-customer-validated evidence of a manufacturing cost edge. 18A yields have reportedly improved through 2025–2026 and Panther Lake reached mass production (positive technical datapoint), but no cost-per-unit citation exists showing Intel has *regained* a scale advantage over TSMC. | **FALSE** |

### 3.4 Final weighted Quality Score

```
Quality Score = (2.17 × 0.25) + (46.50 × 0.15) + (0.0 × 0.20) + (43.7 × 0.15) + (20.0 × 0.15) + (0.0 × 0.10)
              = 0.5425 + 6.975 + 0.0 + 6.555 + 3.0 + 0.0
              = 17.0725 → 17.1 (rounded to nearest 0.1)
```

**17.1 << 80.0 — fails the gate by 62.9 points, and a hard disqualifier also fires independently and unambiguously** (FCF negative in all four of the last four fiscal years — §3.2). This is not a close call and is not sensitive to any single judgment call in this session: even crediting every disputed edge-case interpretation in Intel's favor (e.g. using the higher of the two Balance Sheet bases, 51.0, or crediting the FCF Quality override at its raw mechanical 97.1 rather than the overridden 0.0) would add at most a few points to a total that is still more than 55 points short of the 80.0 gate.

### Result: **Phase 01 FAIL — weighted Quality Score 17.1, misses the 80.0+ gate by 62.9 points. A hard disqualifier also fires independently** (not FCF-positive for any of the last 4 consecutive fiscal years).

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... or a hard disqualifier fires, stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position, and do not place a limit order. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring, per the Phase 03 table in [strategy.md](../framework/strategy.md) (Composite Score is a precondition for that table applying at all).

This is not a verdict that Intel's turnaround under CEO Lip-Bu Tan is doomed, or that the current cyclical/structural trough is permanent — the company has real, cited positive datapoints this session (18A yield improvement and Panther Lake's mass-production ramp; a $8.9B US government equity investment and a $5B Nvidia co-design investment in 2025; a sharply reduced cost base following >25,000 headcount cuts; analyst consensus projecting a return to double-digit revenue growth in FY2026–FY2027 per `earningsTrend`). It is a verdict that, on the specific, cited, filed financial facts available today (free cash flow negative in every one of the last four fiscal years, net income negative in two of the last two, market share losing ground to AMD in both client and — especially — server segments, and a scale-cost disadvantage against TSMC roughly 3–4× in capex terms), Intel does not currently clear this framework's strict, quantitative definition of "high quality" — a bar set deliberately high per the 2026-06-29 gate decision, precisely so a company mid-turnaround doesn't get waved through on the promise of a recovery that hasn't shown up in filed numbers yet. Intel's next earnings report (date not independently confirmed this session — see §7) is the natural next checkpoint.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) Intel's next quarterly earnings report — particularly whether free cash flow turns positive, whether Net Debt/EBITDA and margin trends stabilize, and whether Intel Foundry's external revenue shows real traction beyond the current ~$300M/year run-rate; (b) 2+ consecutive quarters of stabilized or growing x86 market share (client and/or server) per Mercury Research; (c) a confirmed (not "reportedly") major external foundry customer win (e.g. Microsoft Maia 2 on 18A, or a Google/Nvidia commitment) actually converting to booked, disclosed revenue; (d) a guidance revision (up or down); (e) a further management change or material M&A/strategic-investment event; (f) a >15% stock-price move with no identified cause (note: INTC has already moved well over 15% in the trailing month — from ~$140 to the mid-$90s — but a specific single cause for that move was not independently confirmed this session, flagged in §7, so it is not treated here as a "no identified cause" trigger without further confirmation).
- Absent any of the above, future Telegram mentions of INTC should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Data gaps flagged (Rule 0 / "never invent")

- **`yfinance`'s `curl_cffi` backend unusable this session** (documented TLS `Recv failure: Connection reset by peer`, consistent with prior sessions) — worked around via direct `requests`-based calls to Yahoo Finance's `quoteSummary` and `fundamentals-timeseries` endpoints (crumb-authenticated), which succeeded reliably. No financial figure below was estimated or invented to compensate.
- **Two internal discrepancies in Yahoo's own summary-level fields vs. directly-summed quarterly timeseries data** (TTM Free Cash Flow: −$8.30B summary field vs. −$3.12B computed/reconciled figure used; TTM EBITDA: $14.17B summary field vs. $11.42B computed sum-of-quarters) — both flagged explicitly in §2 and §3.1/§3.3, with the computed/reconciled or full-fiscal-year-audited figure used as primary in each case. Neither discrepancy is large enough to change the Phase 01 FAIL conclusion under any combination of bases tested (§3.4).
- **FCF/Net Income conversion ratio formula edge case** (§3.2, §3.3): the ratio produces a mathematically positive but economically meaningless result when both FCF and Net Income are negative (FY2024, FY2025, and the TTM figure) — this session applied a documented judgment-call override (treating this case as 0.0 / disqualifier-relevant rather than mechanically crediting the artifact-positive ratio) rather than either inventing a number or blindly applying a formula that would misleadingly reward cash-and-earnings destruction. Flagged for framework maintainers as a possible candidate for an explicit formula clarification (similar to the 2026-06-20 PEG clean-earnings clarification), since this is not a one-off — any company with simultaneously negative FCF and negative NI will hit the same artifact.
- **Next earnings date not independently confirmed this session** — the triggering Telegram post referenced "this week" but Intel's specific confirmed earnings date was not pulled from a primary source (e.g. Intel investor-relations calendar or a confirmed Yahoo `earningsDate` field) in this session's data pulls. Flagged rather than assumed; the next review trigger in §6 does not depend on a specific date.
- **Cause of INTC's sharp one-month decline (~$140 → mid-$90s) not independently confirmed** — plausible explanations (pre-earnings de-risking, broader semiconductor-sector rotation, profit-taking after the extraordinary 2025 run-up) were not verified against a specific cited news event this session; noted in §1 and §6 rather than asserted as fact.
- Forward PE (58.90×), trailing PE (undefined/negative given trailing EPS of −$0.60), and PEG (1.36, per `defaultKeyStatistics`) were pulled for context/citation only — not scored, since Phase 02 was never reached.
- Analyst target price range ($45.00–$200.00, mean $106.70, 41 analysts per `financialData`) pulled for context only — not used in any calculation, since no fair-value work was performed.

---

## 8. Glossary

- **18A** — Intel's most advanced semiconductor manufacturing process node; its first product (Panther Lake) reached mass production in early 2026 — a positive technical datapoint that did not change this session's Scale Cost Advantage moat-signal finding (no external-customer-validated cost-competitiveness evidence yet).
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **CHIPS Act** — US legislation authorizing federal grants/incentives for domestic semiconductor manufacturing; the basis for the US government's 9.9% equity stake in Intel (Aug 2025) and Intel's related two-year dividend-payment restriction.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every company that files with EDGAR.
- **Composite Score** — This framework's single ranking number (0.0–100.0) blending the Quality Score and Valuation Score 50/50 — not computed for INTC since it never clears the 80.0+ Quality Score gate.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. Negative for Intel in FY2024 and (on a trailing-twelve-month basis) again in the most recent four quarters.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. Negative for Intel in every one of the last four fiscal years.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; produces a misleading result for Intel's two most recent years because both figures are negative (see §3.2/§3.3/§7).
- **Foundry (pure-play foundry)** — A contract chip manufacturer that fabricates chips designed by other companies rather than selling its own branded products; TSMC is the dominant example. Distinct from IFS (below), which is majority-captive.
- **Gaudi** — Intel's AI-accelerator product line, which has materially missed its own sales targets against NVIDIA and AMD.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. Intel's has contracted from ~42.6% (FY2022) to ~34.8% (FY2025).
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score. One fires unambiguously for Intel this session — see §3.2.
- **IFS (Intel Foundry / Intel Foundry Services)** — Intel's contract chip-manufacturing division; still overwhelmingly captive/internal revenue rather than external, per this session's Scale Cost Advantage finding.
- **Invested Capital** — The total capital (debt + equity, netted for cash) put to work in a business — the denominator in this framework's ROIC calculation.
- **ISA (Instruction Set Architecture)** — The instruction set a processor executes (e.g. x86, ARM); the basis for this session's Network Effect and Switching Costs moat-signal findings.
- **Mercury Research** — An independent semiconductor market-share research firm; the citation basis for this session's Market Share moat-signal finding.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. Intel cleared only 1 of 5 cited-evidence moat signals this session.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; Intel's FY2025 ratio (~2.25×) is under the framework's 2.5× threshold, so this specific disqualifier does not fire.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit. Intel's TTM net margin is −5.90%.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. Intel scores **17.1**.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it into profit. Intel's FY2025 ROIC is ~1.30%.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **x86** — The dominant CPU instruction set architecture, originally developed by Intel and also used by AMD; the ecosystem underlying this session's Network Effect and Switching Costs moat-signal findings.

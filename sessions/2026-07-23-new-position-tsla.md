# New Position Evaluation — TSLA (Tesla, Inc., NASDAQ)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 2026-07-23
**10Y US Treasury Yield:** 4.63% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-07-21 — normal FRED reporting lag; fetched directly via `fredgraph.csv?id=DGS10`)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §3.3). For reference only, the bracket in force would be **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current TSLA portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md)).
**Prior coverage:** [TSLA-2026-07-19.md](../watchlist/not-in-portfolio/TSLA/TSLA-2026-07-19.md) — Phase 01 FAIL, Quality Score **37.8** ([session](2026-07-19-new-position-tsla.md)), triggered by an earlier Telegram mention (bolshegold/9795, pre-earnings "reporting this week" framing).
**Sector:** Automotive (battery-electric vehicles) / energy storage & solar / AI-robotics (Optimus, Dojo, FSD) — evaluated here on its core, revenue-generating automotive and energy business; forward-looking robotaxi/Optimus narratives are noted qualitatively only, never scored.
**Filer type:** SEC domestic filer, CIK 0001318605. Fiscal year ends 31 December.
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

Telegram channel **tarasguk**, post **tarasguk/11464** (~06:32 UTC, 2026-07-23), covered Tesla's just-reported quarterly earnings: revenue $28.24B (+26% YoY per the post), adjusted EPS $0.33 vs. a $0.51 forecast (−18% YoY), gross margin contracting to 16.8% (from an anticipated 19.4%), operating margin falling to 1.4% (vs. 5.4% expected), and free cash flow turning negative at −$1.09B for the quarter.

**Per Rule 0, none of those post-cited figures is used as financial data below** — the post is only the reason this ticker was looked at again; every figure in this session is independently fetched/sourced and cited from stockanalysis.com's financial statements (cross-checked internally via quarterly revenue reconciliation, §1 note) plus IBKR live pricing. This session exists because TSLA's own prior watchlist entry ([TSLA-2026-07-19.md](../watchlist/not-in-portfolio/TSLA/TSLA-2026-07-19.md)) explicitly lists "a quarterly earnings release or guidance revision" as Rule 9 re-trigger (d) — that trigger fired today, independent of whatever the post itself claimed.

**Note on channel gap:** the tarasguk marker advanced from post 11462 to 11464 (a 2-post gap — 11463 was superseded and never individually evaluated), and the time gap from the prior check (~20:23 UTC 2026-07-22 to ~06:32 UTC 2026-07-23, ~10 hours) exceeds the routine's ~1hr flag threshold. Flagged per [telegram-scan.md](../.claude/commands/telegram-scan.md) step 2 — this is expected given the routine's hourly cadence and does not affect this session's conclusions (only the latest post is ever acted on).

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work. Same contract as the prior session: **NASDAQ:TSLA, contract_id 76792991**.

| Field | Value | Detail |
|---|---|---|
| **Last trade** | **$354.77** | Live intraday print (not a stale/inferred price). |
| Change (post-earnings) | −$19.24 / **−5.14%** | Consistent with a earnings-miss reaction, not scored as evidence — price action alone is never a Rule 9 trigger per CLAUDE.md. |
| YTD change | −$94.95 / **−21.11%** | |
| 52-week high | $498.83 | |
| 52-week low | $297.82 | |

**Live price used throughout this session: $354.77.**

---

## 2. Data Source Note

Same environment constraint as the 2026-07-19 session: `yfinance`'s `curl_cffi` backend is unreliable through this session's proxy. Fundamentals were sourced via `WebFetch` against **stockanalysis.com**'s financials/cash-flow/balance-sheet/statistics pages (an aggregator, flagged as such), including its quarterly-revenue breakout used to independently reconstruct a clean trailing-twelve-month revenue comparison (§3.3, Growth) rather than relying on annual fiscal-year buckets alone. The 10-Year Treasury yield was sourced directly from FRED's public CSV endpoint. No required input was invented or estimated; every figure below is cited to its source.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Raw financial inputs (all sourced, cited)

**TTM (trailing twelve months, period ended 2026-06-30 — includes the just-reported Q2 2026 quarter):**

| Metric | Value | Source |
|---|---|---|
| Revenue | $103,619M | [stockanalysis.com/stocks/TSLA/financials](https://stockanalysis.com/stocks/TSLA/financials/) |
| Gross Profit | $19,534M | same |
| Gross Margin | 18.85% | same |
| Operating Income | $4,372M | same |
| Net Income | $3,864M | same |
| Net Margin (statistics page) | 3.67% | [stockanalysis.com/stocks/TSLA/statistics](https://stockanalysis.com/stocks/TSLA/statistics/) — minor discrepancy vs. the 3.73% implied by financials-page NI/Revenue, both cited; statistics-page figure used for consistency with the prior session's convention |
| ROIC (TTM) | 5.80% | statistics page |
| Operating Cash Flow (TTM) | $18,685M | [.../cash-flow-statement](https://stockanalysis.com/stocks/TSLA/financials/cash-flow-statement/) |
| CapEx (TTM) | −$12,923M | same |
| Free Cash Flow (TTM) | $5,762M | same |

**Most recently reported quarter alone (Q2 2026, ended 2026-06-30)**, cited for context/trend-reading only, not substituted for any TTM/annual input: Revenue $28,236M, Gross Margin 16.83%, Operating Margin 1.41% — confirms (independently, via stockanalysis.com's own quarterly breakout, not the Telegram post) that this was a weak margin quarter even though it is the single largest revenue quarter shown in the last 16.

**Balance sheet (most recent quarter):** Total Debt $9,342M, Cash & Short-Term Investments $43,524M, Total Shareholders' Equity $87,519M → **Net Debt = 9,342 − 43,524 = −$34,182M (net cash position)**. Source: [.../balance-sheet](https://stockanalysis.com/stocks/TSLA/financials/balance-sheet/).

**Prior-year annual figures (unchanged from 2026-07-19 session, retained for the 5yr margin trend read):** FY2021 Gross Margin 25.28%, FY2022 25.60%, FY2023 18.25%, FY2024 17.86%, FY2025 18.03%.

### 3.2 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | TSLA data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF positive in every one of the last 5 fiscal years, and TTM (through Q2 2026) remains positive at $5,762M. | **Does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | Net Debt is negative (−$34,182M, net cash) — ratio is negative regardless of EBITDA. | **Does not fire** (best-case scenario). |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FY2022 60.2%, FY2023 29.1%, FY2024 50.5% were each below 70% (documented in the 2026-07-19 session, judged not to fire there on a cited growth-capex basis). The two most recent readings — FY2025 (163.9%) and now TTM through Q2 2026 (**149.1%** = $5,762M/$3,864M) — are both well above 70%, so the disqualifier condition (2+ *consecutive* sub-70% years) is not met looking backward from today either. | **Does not fire.** |

**No hard disqualifier fires.** Proceeding to the full weighted score.

### 3.3 Sub-score calculation

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((3.67/30)×100, 0, 100) = **12.23**. ROIC_Component = clamp((5.80/30)×100, 0, 100) = **19.33** (TTM figures). Profitability_Score = (12.23+19.33)/2 = **15.78**. FCF-positive, no cap. | **15.78** |
| **Margins (15%)** | GrossMargin_Score = clamp((18.85/80)×100, 0, 100) = **23.56** (TTM gross margin). **5-year+ trend:** 25.28% (FY2021) → 25.60% (FY2022) → 18.25% (FY2023) → 17.86% (FY2024) → 18.03% (FY2025) → 18.85% (TTM through Q2 2026). Structural compression from the 2021–22 peak remains intact; the modest TTM uptick over FY2025 is not evidence of a reversing 3yr trend — the just-reported quarter itself printed 16.83%, *below* both FY2025 and the TTM average, meaning the newest data point pulls the margin picture down, not up. **No +10 trend bonus.** | **23.56** |
| **Growth (20%)** | Independently reconstructed via stockanalysis.com's quarterly revenue breakout (not annual FY buckets, to get a clean like-for-like 3yr TTM comparison): TTM revenue through Q2 2023 = Q3'22+Q4'22+Q1'23+Q2'23 = 21,454+24,318+23,329+24,927 = **$94,028M**. TTM revenue through Q2 2026 = Q3'25+Q4'25+Q1'26+Q2'26 = 28,095+24,901+22,387+28,236 = **$103,619M** (reconciles exactly with the financials-page TTM figure, §3.1 — cross-check passed). 3yr CAGR = (103,619/94,028)^(1/3) − 1 = **+3.29%/yr** — decelerated from the 2026-07-19 session's +5.19%/yr (which used FY2022→FY2025 annual buckets). Base Growth_Score = clamp((3.29/25)×100, 0, 100) = **13.16**. **Modifier — same documented structural deceleration applied (−10):** global EV market share continuing to erode to BYD (unchanged citation basis from the 2026-07-19 session — [TechCrunch](https://techcrunch.com/2026/01/02/tesla-annual-sales-decline-9-as-its-overtaken-by-byd-as-global-ev-leader/), [CNN](https://www.cnn.com/2026/01/02/business/tesla-byd-ev)); no new offsetting TAM-expansion evidence found this session (robotaxi/Optimus still not in revenue-generating volume production). Growth_Score = clamp(13.16 − 10, 0, 100) = **3.16**. | **3.16** |
| **Balance Sheet (15%)** | Net Debt = −$34,182M (net cash) → clamps to **100.0** at the formula's best-defined point. | **100.0** |
| **Moat Signal (15%)** | No new cited evidence found this session to change any of the 5 signals from the 2026-07-19 evaluation. Re-affirmed: **1 of 5** signals clear (Network effect — FSD's cumulative supervised-mile dataset, unchanged citation). The other 4 remain unsupported, and this quarter's own operating-margin collapse to 1.41% (independently confirmed, §3.1) is consistent with, not contrary to, the "no scale cost advantage / no brand premium" findings already on record. Moat_Score = (1/5)×100 = **20.0** | **20.0** |
| **FCF Quality (10%)** | FCF/NI (TTM through Q2 2026) = $5,762M / $3,864M = **149.14%** → clamp(((1.4914−0.40)/0.60)×100, 0, 100) = 181.9, clamped to **100.0**. Same flag as the 2026-07-19 session: favorable only because net income remains structurally depressed (not because underlying cash conversion improved) — see §3.2's 3-year sub-70% run immediately preceding FY2025/TTM. | **100.0** (flagged) |

### 3.4 Final weighted Quality Score

```
Quality Score = (15.78 × 0.25) + (23.56 × 0.15) + (3.16 × 0.20) + (100.0 × 0.15) + (20.0 × 0.15) + (100.0 × 0.10)
              = 3.945 + 3.534 + 0.632 + 15.0 + 3.0 + 10.0
              = 36.111 → 36.1 (rounded to nearest 0.1)
```

**36.1 < 80.0 — fails the gate by 43.9 points**, a wider miss than the 2026-07-19 session's 37.8 (42.2-point miss). The newly reported quarter did not improve the picture: it decelerated the measured 3yr revenue-growth rate (5.19%→3.29% CAGR, driving Growth_Score down from 10.77 to 3.16) and modestly softened Profitability (17.15→15.78, on lower TTM net margin and ROIC), only partially offset by Margins ticking up fractionally (22.54→23.56). Balance Sheet, Moat, and FCF Quality sub-scores are unchanged in substance.

### Result: **Phase 01 FAIL — weighted Quality Score 36.1, misses the 80.0+ gate by 43.9 points.** No hard disqualifier fires, but none was needed.

Per [new-position.md](../.claude/commands/new-position.md) step 2: stop here rather than proceeding to scoring. **No Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position, and do not place a limit order. The Rule 9 earnings trigger materialized exactly as documented in TSLA's prior watchlist entry, and re-scoring on fresh TTM data (including the newly reported quarter) confirms the conclusion is not just intact but slightly reinforced: Quality Score moved from 37.8 to **36.1**, still a decisive fail against the 80.0+ gate, driven by continuing gross-margin weakness (this quarter printed 16.83%, the softest reading in the recent window), a near-zero operating margin (1.41%, independently confirmed), and a revenue growth rate that is *decelerating* on a clean like-for-like 3-year comparison (5.19%→3.29% CAGR) even as absolute quarterly revenue hits a new high.

This remains a verdict about the framework's strict quantitative quality bar, not a broader judgment on Tesla's long-term prospects (robotaxi, Optimus, FSD monetization) — those remain pre-revenue narratives this framework does not credit until they show up in filed financials, per its guidance-exclusion discipline.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

Unchanged from the 2026-07-19 entry, restated: no routine re-screen scheduled (Phase 01 FAIL, no numeric Phase 02 score to go stale). Re-evaluate on any of: (a) a sustained reversal of the gross-margin compression trend (2+ consecutive quarters back above ~22–23% — this quarter moved the wrong way, to 16.83%); (b) Cybercab/robotaxi or Optimus reaching actual revenue-generating volume production; (c) a stabilization or reversal of the global EV market-share decline over 2+ consecutive quarters; (d) the next quarterly earnings release or a guidance revision (this session's own trigger — already consumed); (e) a management change or material M&A/strategic-investment event; (f) a >15% stock-price move with no identified cause (today's −5.14% earnings reaction does not qualify). Absent any of the above, future Telegram mentions of TSLA should be logged as "last checked, no change."

---

## 7. Data gaps flagged (Rule 0)

- **`yfinance` unusable this session** (same documented `curl_cffi`/proxy issue as 2026-07-19) — worked around via `WebFetch` against stockanalysis.com, with an internal cross-check (quarterly-revenue reconstruction reconciling exactly to the financials-page TTM figure, §3.3) used in place of a second independent source. No financial figure below was estimated or invented.
- **Net margin discrepancy** between stockanalysis.com's statistics page (3.67%) and the figure implied by its own financials page (NI $3,864M / Revenue $103,619M = 3.73%) — both cited; the statistics-page figure was used for scoring, consistent with the prior session's sourcing convention. Immaterial to the outcome either way.
- **EBITDA** not independently derived from a primary filing this session — not needed, since Net Debt is unambiguously negative regardless of EBITDA's exact magnitude.

---

## 8. Glossary

- **BYD** — A Chinese electric-vehicle manufacturer that overtook Tesla as the world's top-selling EV maker by full-year 2025 deliveries — cited in this framework's Growth and Moat Signal findings as the primary source of Tesla's documented global market-share decline.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **Composite Score** — This framework's single ranking number (0.0–100.0) blending the Quality Score and Valuation Score 50/50 — not computed for TSLA since it never clears the 80.0+ Quality Score gate.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. Positive for TSLA in every one of the last 5 fiscal years and the current TTM.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. Currently 149.1% on a TTM basis, flagged as favorable mainly because net income remains structurally depressed rather than because cash conversion genuinely improved.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. TSLA's TTM figure is 18.85%, though the most recently reported quarter alone printed a softer 16.83%.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score. None fires for TSLA this session.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. TSLA clears only 1 of the framework's 5 cited-evidence moat signals.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; negative means net cash. TSLA carries a net cash position of ~$34.2B.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **Operating Margin** — Operating Income ÷ Revenue — the percentage of each revenue dollar left after operating expenses, before interest and taxes. TSLA's most recently reported quarter printed 1.41%, near breakeven.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. TSLA scores **36.1** this session (was 37.8 on 2026-07-19).
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. TSLA's TTM ROIC is 5.80%.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. This session's earnings-release trigger is (d) on that list.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of financial data, rolling forward each quarter, as distinct from a fixed fiscal year — used throughout this session so the newly reported Q2 2026 quarter is reflected.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).

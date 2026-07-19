# New Position Evaluation — TSLA (Tesla, Inc., NASDAQ)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 2026-07-19
**10Y US Treasury Yield:** 4.57% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-07-16 — normal FRED reporting lag; fetched directly via `fredgraph.csv?id=DGS10`)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §3.3). For reference only, the bracket in force would be **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current TSLA portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); `grep -i "tesla\|tsla"` returns no match).
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is TSLA's first-ever evaluation under this framework.
**Sector:** Automotive (battery-electric vehicles) / energy storage & solar / AI-robotics (Optimus, Dojo, FSD) — evaluated here on its core, revenue-generating automotive and energy business; forward-looking robotaxi/Optimus narratives are noted qualitatively only, never scored (guidance is not a scored input per [valuation-scoring.md](../framework/valuation-scoring.md)).
**Filer type:** SEC domestic filer, CIK 0001318605. Fiscal year ends 31 December. Most recent 10-K: FY2025, filed 2026 (`tsla-20251231.htm`).
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

Telegram channel **bolshegold**, post **bolshegold/9795** (~09:46 UTC, 2026-07-19), listed TSLA among "companies reporting earnings this week," adding "Focus on whether electric vehicle 'hypercycle 2.0' will begin." Per [telegram-scan.md](../.claude/commands/telegram-scan.md)'s convention ("no watchlist entry exists at all → `/new-position <TICKER>`"), this session was triggered regardless of the mention's substance — TSLA had zero prior coverage in this repo. **Per Rule 0, no claim from the triggering post is used as financial data anywhere below** — the post is only the reason this ticker was looked at; every figure in this session is independently fetched/sourced and cited. The "hypercycle 2.0" framing is itself an unverified forward-looking narrative, not treated as evidence of anything in this session.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

**Contract disambiguation:** `search_contracts("TSLA")` returned 25+ matches, including decoys that are *not* the underlying stock — leveraged/inverse/income ETFs tracking TSLA (`TSLL` 2x bull, `TSLQ`/`TSLS`/`TSDD` inverse, `TSLY`/`TSYY`/`TSLW`/`TSLP`/`CRSH` options-income funds, `TSLR`/`TSLG`/`3LTS` leveraged), a Canadian CDR (TSE), a Mexican listing, European CHF/GBP listings, and an unrelated mutual fund (`TSLAX`, Transamerica Small Cap Value). The correct instrument is **NASDAQ:TSLA, contract_id 76792991, "TESLA INC", country_code US** — confirmed as the primary US equity listing.

| Field | Value | Detail |
|---|---|---|
| **Last trade** | **$391.06** | `is_close: true` — this is Friday 2026-07-17's closing print; markets are closed on Saturday 2026-07-19 (today), so no fresher intraday trade exists. This is the most recent real trade, not an inferred or stale-note price. |
| 52-week high | $498.83 | |
| 52-week low | $297.82 | |
| Price 52 weeks ago (`open_52w`) | $321.66 | |
| YTD change | −$58.66 / **−13.04%** | |

**Live price used throughout this session: $391.06.**

---

## 2. Data Source Note

`yfinance`'s `curl_cffi` backend failed with a TLS-level `Recv failure: Connection reset by peer` through this session's proxy — a recurring, previously-documented environment issue in this repo (same failure class noted in prior sessions, e.g. SMR 2026-07-16). Explicit `proxies=` parameters to `curl_cffi.requests.Session` succeeded once, then failed again on repeated calls — inconsistent enough (and consistent with the proxy README's guidance not to fight tools that evade its trust/fingerprint layer) that it was abandoned rather than retried further. A plain `curl`/`requests`-style fetch to the same Yahoo host succeeded (HTTP 429 rate-limit, not a connection reset), confirming the proxy itself is not the blocker.

Fundamentals were instead sourced via `WebFetch` against **stockanalysis.com**'s TSLA financials/cash-flow/balance-sheet/statistics pages (a data aggregator, not a primary filing — flagged), cross-referenced qualitatively against Tesla's own FY2025 Form 10-K and its Q4 2025 shareholder deck (both SEC/company primary sources) via `WebSearch`. The 10-Year Treasury yield was sourced directly from FRED's public CSV endpoint (`fredgraph.csv?id=DGS10`), which also doesn't require the blocked backend. No required input was invented or estimated; every figure below is cited to its source, with the aggregator-vs-primary-filing distinction flagged wherever it matters.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Raw financial inputs (all sourced, cited)

| Fiscal Year | Revenue | Gross Profit | Gross Margin | Operating Income (EBIT) | Net Income | Net Margin | Op. Cash Flow | CapEx | FCF | FCF/NI |
|---|---|---|---|---|---|---|---|---|---|---|
| FY2021 | $53,823M | $13,606M | 25.28% | $6,523M | $5,519M | 10.49% | $11,497M | −$6,514M | $4,983M | 90.29% |
| FY2022 | $81,462M | $20,853M | 25.60% | $13,656M | $12,556M | 15.45% | $14,724M | −$7,163M | $7,561M | 60.21% |
| FY2023 | $96,773M | $17,660M | 18.25% | $8,891M | $14,997M | 15.47% | $13,256M | −$8,899M | $4,357M | 29.05% |
| FY2024 | $97,690M | $17,450M | 17.86% | $7,076M | $7,091M | 7.32% | $14,923M | −$11,342M | $3,581M | 50.50% |
| FY2025 | $94,827M | $17,094M | 18.03% | $4,355M | $3,794M | 4.07% | $14,747M | −$8,527M | $6,220M | 163.94% |

Source: [stockanalysis.com/stocks/TSLA/financials](https://stockanalysis.com/stocks/TSLA/financials/), [.../cash-flow-statement](https://stockanalysis.com/stocks/TSLA/financials/cash-flow-statement/).

**TTM snapshot (stockanalysis.com statistics page, most recent quarter basis, differs slightly from FY2025 annual above due to trailing-quarter mix):** Net Margin 3.95%, ROIC 6.34%, ROE 4.90%, ROCE 4.38%, Debt/Equity 0.19, Debt/EBITDA 1.23. Source: [stockanalysis.com/stocks/TSLA/statistics](https://stockanalysis.com/stocks/TSLA/statistics/).

**Balance sheet (FY2025 year-end):** Total Debt $8,376M, Cash & Short-Term Investments $44,059M, Total Shareholders' Equity $82,865M → **Net Debt = 8,376 − 44,059 = −$35,683M (net cash position)**. Source: [stockanalysis.com/stocks/TSLA/financials/balance-sheet](https://stockanalysis.com/stocks/TSLA/financials/balance-sheet/).

### 3.2 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | TSLA data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF positive in **every one of the last 5 fiscal years** (FY2021–FY2025, table above) — never negative. | **Does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | Net Debt is **negative** (−$35,683M, net cash) — the ratio is negative regardless of EBITDA's magnitude, i.e. comfortably inside the threshold. | **Does not fire** (best-case scenario). |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | Ratio was below 70% in **three consecutive years**: FY2022 (60.2%), FY2023 (29.1%), FY2024 (50.5%). **Judgment call, flagged explicitly:** (a) Tesla's capex in this window is documented (Tesla's own IR materials, WardsAuto, and other trade press — see §7 sources) as directed overwhelmingly at *growth* capacity — Gigafactory Texas and Berlin expansion, 4680 battery-cell capacity, Cybertruck/Cybercab tooling, and AI/Dojo compute buildout — not maintenance of existing lines; (b) FY2023's net income specifically included a one-off, non-cash **$5.9B deferred tax valuation allowance release** ([Scale CPA](https://scalecpa.com/tesla-income-tax-benefit-2023/), Tesla's own FY2023 10-K), which inflates that year's net-income denominator and mechanically depresses the ratio independent of any real cash-conversion problem. Both are documented, cited explanations (growth capex *and* a one-off accounting inflation of the denominator) — **this disqualifier is judged not to fire**, but is flagged here for human review rather than silently resolved. **This judgment call does not change the outcome below** — see §3.4. | **Judged not to fire** (flagged, see note) |

**No hard disqualifier fires.** Proceeding to the full weighted score for transparency (per operating-brief.md's "no black-box outputs").

### 3.3 Sub-score calculation

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((3.95/30)×100, 0, 100) = **13.17**. ROIC_Component = clamp((6.34/30)×100, 0, 100) = **21.13** (TTM figures, stockanalysis.com statistics page). Profitability_Score = (13.17+21.13)/2 = **17.15**. FCF-positive 5 consecutive years, so no cap applies. | **17.15** |
| **Margins (15%)** | GrossMargin_Score = clamp((18.03/80)×100, 0, 100) = **22.54** (FY2025 gross margin). **5-year trend:** 25.28% (FY2021) → 25.60% (FY2022) → 18.25% (FY2023) → 17.86% (FY2024) → 18.03% (FY2025). This is **structural compression**, not expansion — margin fell ~7.6 points from the 2021–2022 peak and has stayed near 18% for three years running (price cuts to defend volume against intensifying EV competition, per §3.4 Moat evidence). **No +10 trend bonus** (bonus only applies to an *expanding* trend). | **22.54** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $81,462M → FY2025 $94,827M) = (94,827/81,462)^(1/3) − 1 = **+5.19%/yr**. Base Growth_Score = clamp((5.19/25)×100, 0, 100) = **20.77**. **Modifier — documented structural deceleration applied (−10):** Tesla's global EV market share fell to ~8.9% (March 2026) as BYD's rose to 17.1%, with BYD overtaking Tesla as the world's #1 EV seller by full-year 2025 deliveries (1.63M vs. BYD's 2.26M) — a multi-year, competitively-driven (not cyclical) deceleration, cited to [TechCrunch](https://techcrunch.com/2026/01/02/tesla-annual-sales-decline-9-as-its-overtaken-by-byd-as-global-ev-leader/) and [CNN](https://www.cnn.com/2026/01/02/business/tesla-byd-ev). No offsetting +10 TAM-expansion modifier applied: robotaxi (Cybercab) and Optimus are still pre-volume-production as of this session ("expects to start volume production this year" per Tesla's own Q4 2025 materials) — forward guidance on an unrealized product line is exactly the kind of self-reported, not-yet-financial evidence this framework excludes from scored inputs. Growth_Score = clamp(20.77 − 10, 0, 100) = **10.77**. | **10.77** |
| **Balance Sheet (15%)** | Net Debt = −$35,683M (net cash) ÷ any positive EBITDA still yields a negative ratio → clamp(100×(1−NetDebt/EBITDA/4), 0, 100) clamps to **100.0** at the formula's best-defined point (net cash, zero-or-negative implied ratio). | **100.0** |
| **Moat Signal (15%)** | See evidence table below — **1 of 5** signals cleared the cited-evidence bar. Moat_Score = (1/5)×100 = **20.0** | **20.0** |
| **FCF Quality (10%)** | FCF/NI (FY2025, most recent complete fiscal year) = $6,220M / $3,794M = **163.94%** → clamp(((1.6394−0.40)/0.60)×100, 0, 100) = **100.0** (clamped). **Flagged as not fully representative**: this reading is favorable only because FY2025 net income was unusually depressed (4.07% margin, the lowest of the 5-year window) — not because underlying cash conversion improved. The 4-year run immediately preceding it (FY2021–FY2024: 90.3%, 60.2%, 29.1%, 50.5%) shows conversion below 70% in 3 of those 4 years. Shown per the formula (most recent complete FY, consistent with this framework's convention), with this caveat made explicit rather than silently smoothed over. | **100.0** (flagged) |

**Moat signal evidence (cited, per signal — all five checked against the framework's required cited-evidence bar):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable or growing | **Declining, not stable.** Global EV market share fell to ~8.9% (March 2026) vs. BYD's 17.1%; BYD outsold Tesla globally in full-year 2025 (2.26M vs. 1.63M deliveries, a 9% YoY Tesla decline). Tesla remains dominant in the US specifically (59% of the US EV market, Q4 2025), but that domestic figure doesn't establish a *global* stable-or-growing share claim. Cited: [TechCrunch](https://techcrunch.com/2026/01/02/tesla-annual-sales-decline-9-as-its-overtaken-by-byd-as-global-ev-leader/), [InsideEVs](https://insideevs.com/news/792143/tesla-no1-ev-maker-q1-2026/) (noting a partial Q1 2026 rebound as BYD's own sales fell 25% that quarter — a genuinely mixed, contested picture, but not one supporting an unambiguous "stable or growing" claim). | **FALSE** |
| Brand premium | No cited evidence of price increases sustained without volume loss — the opposite is well documented: Tesla has repeatedly cut prices across 2023–2025 specifically to defend unit volume against BYD/legacy-OEM competition (context in the market-share sources above). Pricing power evidence requires the reverse pattern. | **FALSE** |
| Network effect | **TRUE.** Tesla's Full Self-Driving (FSD Supervised) fleet has logged a cumulative 8+ billion supervised miles as of February 2026 (up from ~6 million in 2021), a scale of real-world edge-case training data no competitor's smaller fleet can currently match — a documented data-flywheel mechanism (more miles driven → more training data → a better-trained model deployed back to the whole fleet). Cited: [Teslarati](https://www.teslarati.com/tesla-fsd-supervised-fleet-passes-8-4-billion-cumulative-miles/), [Road to Autonomy](https://www.roadtoautonomy.com/tesla-data-advantage/). Caveat noted: these are *supervised* miles (human can intervene), distinct from Waymo's smaller but fully driverless mileage total. | **TRUE** |
| Switching costs | No documented lock-in mechanism cited this session (FSD is tied to the vehicle, not a subscription with demonstrated high renewal-cost friction; no filed data on attach/retention rates found). | **FALSE** |
| Scale cost advantage | No cost-per-unit data found showing Tesla retains a manufacturing cost edge over smaller/newer competitors — the opposite signal (sharp, sustained gross-margin compression from 25.6% to 18.0% over the FY2022–FY2025 window, same table as §3.1) is better documented than any surviving cost advantage. | **FALSE** |

### 3.4 Final weighted Quality Score

```
Quality Score = (17.15 × 0.25) + (22.54 × 0.15) + (10.77 × 0.20) + (100.0 × 0.15) + (20.0 × 0.15) + (100.0 × 0.10)
              = 4.2875 + 3.381 + 2.154 + 15.0 + 3.0 + 10.0
              = 37.8225 → 37.8 (rounded to nearest 0.1)
```

**37.8 < 80.0 — fails the gate by 42.2 points.** This is not a close call, and is not sensitive to any of this session's judgment calls: even treating the two most favorable (arguably formula-flattered) sub-scores at their maximum — Balance Sheet 100.0 and FCF Quality 100.0 — the other four sub-scores (Profitability 17.15, Margins 22.54, Growth 10.77, Moat 20.0) are decisively weak, driven by genuinely documented facts (compressed margins, decelerating growth amid intensifying competition, thin profitability, a mostly-unsupported moat case) rather than by any single disputable input. Resolving the §3.2 FCF/NI hard-disqualifier judgment call the *other* way (i.e. deciding it should fire) would not change the conclusion — it would simply make an already-failing name fail via a second, independent route.

### Result: **Phase 01 FAIL — weighted Quality Score 37.8, misses the 80.0+ gate by 42.2 points.** No hard disqualifier fires, but none was needed to reach this outcome.

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... or a hard disqualifier fires, stop there and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position, and do not place a limit order. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring, per the Phase 03 table in [strategy.md](../framework/strategy.md) (Composite Score is a precondition for that table applying at all).

This is not a verdict that Tesla's EV/energy/AI-robotics business is worthless or that "hypercycle 2.0" (the Telegram post's framing) is impossible — it is a verdict that, on the specific, cited, filed financial facts available today (compressed gross margins, decelerating core-auto revenue growth amid a well-documented global share loss to BYD, thin profitability, and a moat case resting on essentially one cited signal out of five), Tesla does not currently clear this framework's strict, quantitative definition of "high quality" at its current live price of $391.06. A market pricing this stock at a Forward PE near 168× (per stockanalysis.com's statistics page, cited for context, not scored) is pricing in exactly the kind of unrealized, forward-looking transformation (robotaxi, Optimus, FSD monetization) that this framework's Rule 0/guidance-exclusion discipline deliberately does not credit until it shows up in filed financials.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) a sustained reversal of the gross-margin compression trend (e.g. 2+ consecutive quarters back above ~22-23%); (b) Cybercab/robotaxi or Optimus reaching actual, revenue-generating volume production (not just guidance); (c) a stabilization or reversal of the global EV market-share decline over 2+ consecutive quarters; (d) a quarterly earnings release or guidance revision (the Telegram post's trigger — TSLA reports "this week" per the post, so the next print is a natural re-check point); (e) a management change or material M&A/strategic-investment event; (f) a >15% stock-price move with no identified cause.
- Absent any of the above, future Telegram mentions of TSLA should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Data gaps flagged (Rule 0)

- **`yfinance` unusable this session** (documented `curl_cffi` TLS-reset failure through the proxy, intermittent even with explicit `proxies=` overrides) — worked around via `WebFetch` against stockanalysis.com (an aggregator, flagged as such throughout) cross-checked qualitatively against Tesla's own SEC filings and IR materials via `WebSearch`. No financial figure below was estimated or invented to compensate.
- **No exact quantified growth-vs-maintenance CapEx split** is disclosed by Tesla — the §3.2 FCF/NI hard-disqualifier judgment call rests on a *qualitative*, cited growth-capex narrative (new Gigafactory/Cybercab/AI-compute buildout) rather than a precise Upgrade 1 (Owner Earnings) calculation, since Tesla does not break out maintenance capex separately. Flagged for human review; does not change the ultimate PASS conclusion (§3.4).
- **EBITDA** was not independently derived from a primary filing this session (not needed — Net Debt is unambiguously negative regardless of EBITDA's exact magnitude); the TTM Debt/EBITDA (1.23×) and EV/EBITDA (126.33×) figures are cited from stockanalysis.com's statistics page for context only, not used in the Balance Sheet sub-score calculation.
- Forward PE (168.32×), Trailing PE (370.36×), and PEG (3.95) were pulled for context/citation only — not scored, since Phase 02 was never reached.

---

## 8. Glossary

- **BYD** — A Chinese electric-vehicle manufacturer that overtook Tesla as the world's top-selling EV maker by full-year 2025 deliveries — cited in this framework's Growth and Moat Signal findings above as the primary source of Tesla's documented global market-share decline.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every company that files with EDGAR.
- **Composite Score** — This framework's single ranking number (0.0–100.0) blending the Quality Score and Valuation Score 50/50 — not computed for TSLA since it never clears the 80.0+ Quality Score gate.
- **Cybercab / Cybertruck** — Tesla's planned dedicated robotaxi vehicle (Cybercab, not yet in volume production as of this session) and its angular pickup-truck model (Cybertruck, in production) — cited in the Growth/Moat discussion as context for recent capex, not as scored revenue.
- **Deferred tax valuation allowance release** — A one-off GAAP accounting event where a company reverses a prior write-down on its deferred tax assets once it judges those assets are now likely usable, producing an artificially low effective tax rate and inflated net income/EPS in the recognition period. Tesla recognized a one-time, non-cash **$5.9B** release of this kind in Q4 FY2023, materially inflating that year's net income and, in turn, mechanically depressing its FCF/Net Income conversion ratio for that year (see §3.2).
- **Dojo** — Tesla's custom AI-training supercomputer hardware program, built to process FSD/Autopilot camera-video training data at scale — cited only as context for recent AI-related capex, not as a scored input.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit.
- **EV/EBIT, EV/EBITDA** — Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure. Cited for TSLA context only (291.79× and 126.33× respectively) — not scored, since Phase 02 was never reached.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. Positive for TSLA in every one of the last 5 fiscal years.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. Below 70% in 3 of TSLA's last 4 fiscal years (see §3.2).
- **FSD (Full Self-Driving)** — Tesla's driver-assistance/autonomy software package, sold as "FSD Supervised." Cited in this framework's Moat Signal "network effect" finding — see full glossary.md entry for detail.
- **Forward PE** — Price ÷ next twelve months' *expected* earnings per share.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. One of this framework's Quality Score Margins sub-score inputs; TSLA's has compressed from ~25% (FY2021–22) to ~18% (FY2023–25).
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score — see [quality-scoring.md](../framework/quality-scoring.md). None fires for TSLA this session, though the FCF/NI conversion check required an explicit judgment call (§3.2).
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. TSLA cleared only 1 of the framework's 5 cited-evidence moat signals this session.
- **NACS (North American Charging Standard)** — Tesla's EV-charging connector standard, now adopted industry-wide. See full glossary.md entry — cited here as a moat-dilution caveat (opening the Supercharger network to competitors' vehicles), not a strengthening signal.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; negative means net cash. TSLA carries a net cash position of ~$35.7B.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **Optimus** — Tesla's humanoid-robot program, not yet a revenue-generating product as of this session — cited only as forward-looking context, never scored.
- **PEG** — Price/Earnings-to-Growth ratio — used only for "Fast Grower" companies (EPS growth >15%/yr for 3+ years); not applicable to TSLA this session (never reached, since Phase 01 failed first), though its 3.95× reading (cited for context) would itself be a rich/expensive figure if it were scored.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. TSLA does not make this list.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. TSLA scores **37.8**.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. TSLA's TTM ROIC is 6.34%.
- **Robotaxi** — An autonomous vehicle operated as an on-demand ride-hailing service without a human safety driver — Tesla's planned Cybercab-based service is not yet in volume production/revenue-generating operation as of this session.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Trailing PE** — Price ÷ the last twelve months' *actual* earnings per share, distinct from Forward PE. Cited for TSLA context only (370.36×).
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).

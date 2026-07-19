# New Position Evaluation — CMCSA (Comcast Corporation, NASDAQ)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 2026-07-19
**10Y US Treasury Yield:** 4.57% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-07-16 — normal FRED reporting lag; fetched directly via `fredgraph.csv?id=DGS10`)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §3.4). For reference only, the bracket in force would be **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current CMCSA portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); no CMCSA/Comcast row exists).
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is CMCSA's first-ever evaluation under this framework.
**Sector:** Communication Services — Cable/Broadband Connectivity & Diversified Media (Residential/Business Connectivity, Xfinity Mobile) plus Content & Studios (NBC, Bravo, Telemundo, Universal Pictures, Peacock) and Theme Parks (Universal Destinations & Experiences), following the 2 January 2026 spin-off of the cable-networks portfolio into Versant Media Group (Nasdaq: VSNT — see Glossary).
**Filer type:** SEC domestic filer, CIK 0001166691. Fiscal year ends 31 December. Most recent 10-Q: Q1 2026 (period ended 31 March 2026, filed as `cmcsa-20260331.htm`).
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

Telegram channel **bolshegold**, post **bolshegold/9795** (~09:46 UTC, 2026-07-19), listed CMCSA among "companies reporting earnings this week / under observation." Per [telegram-scan.md](../.claude/commands/telegram-scan.md)'s convention ("no watchlist entry exists at all → `/new-position <TICKER>`"), this session was triggered regardless of the mention's substance — CMCSA had zero prior coverage in this repo. **Per Rule 0, no claim from the triggering post is used as financial data anywhere below** — the post is only the reason this ticker was looked at; every figure in this session is independently fetched/sourced and cited.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

**Contract disambiguation:** `search_contracts("CMCSA")` returned the correct instrument plus decoys: a Mexican-listed cross-listing (MEXI, contract_id 38708747) and a Swiss EBS CHF/USD-quoted line (`CMCSAUSD`, contract_id 835397100), neither the primary US listing. The correct instrument is **NASDAQ:CMCSA, contract_id 267748, "COMCAST CORP-CLASS A", country_code US** — confirmed as the primary US equity listing (Class A common stock).

| Field | Value | Detail |
|---|---|---|
| **Last trade** | **$24.10** | `is_close: true` — Friday 2026-07-17's closing print; markets are closed on Saturday 2026-07-19 (today), so no fresher intraday trade exists. This is the most recent real trade, not an inferred or stale-note price. |
| 52-week high | $32.63 | |
| 52-week low | $22.13 | |
| Price 52 weeks ago (`open_52w`) | $31.57 | |
| YTD change | −$3.26 / **−11.91%** | |

**Live price used throughout this session: $24.10.**

---

## 2. Data Source Note

`yfinance`'s `curl_cffi` backend failed with the same TLS-level `Recv failure: Connection reset by peer` documented in prior sessions (e.g. SMR 2026-07-16, TSLA 2026-07-19) — a recurring, previously-flagged environment/proxy issue in this repo, not specific to CMCSA. Fundamentals were instead sourced via `WebFetch` against **stockanalysis.com**'s financials/cash-flow/balance-sheet/statistics pages (a data aggregator, flagged as such), **spot-checked against Comcast's own Q1 2026 Form 10-Q** (primary SEC source, `cmcsa-20260331.htm`) for the balance sheet and income statement — the two independently agreed to the dollar on Total Debt ($94,612M / "$94.6B") and Cash & Cash Equivalents ($9,468M / "$9.468B"); Total Shareholders' Equity showed a small ~$266M discrepancy ($88,540M aggregator vs. $88,274M per the 10-Q) — **the 10-Q (primary source) figure is used wherever the two differ.** The 10-Year Treasury yield was sourced directly from FRED's public CSV endpoint, which doesn't require the blocked backend. No required input was invented or estimated; every figure below is cited to its source.

**Reporting-basis caveat (flagged, Rule 6 "normalize before you value"):** Comcast completed the spin-off of its cable-networks portfolio into **Versant Media Group** (Nasdaq: VSNT — see Glossary) effective 2 January 2026. The FY2021–FY2025 **annual** income-statement/cash-flow figures below still **consolidate Versant** (pre-separation), while the Q1 2026 balance sheet used for the Balance Sheet sub-score is **post-separation**. This is the same class of data-consistency gap flagged for FedEx's fiscal-year change and SanDisk's carve-out financials elsewhere in this framework (see glossary). It is disclosed here rather than silently smoothed over; it does not change the ultimate conclusion (see §3.5 — the gate is missed by ~38 points, not a close call sensitive to this basis question).

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Raw financial inputs (all sourced, cited)

| Fiscal Year | Revenue | Gross Profit | Gross Margin | Operating Income (EBIT) | Net Income | Net Margin | Op. Cash Flow | CapEx | FCF | FCF/NI |
|---|---|---|---|---|---|---|---|---|---|---|
| FY2021 | $116,385M | $77,935M | 66.96% | $20,817M | $13,833M | 11.89% | $29,146M | −$10,150M | $18,996M | 137.3% |
| FY2022 | $121,427M | $83,214M | 68.53% | $14,041M | $4,925M | 4.06% | $26,413M | −$10,956M | $15,457M | 313.8% |
| FY2023 | $121,572M | $84,810M | 69.76% | $23,314M | $15,107M | 12.43% | $28,501M | −$12,379M | $16,122M | 106.7% |
| FY2024 | $123,731M | $86,705M | 70.08% | $23,297M | $15,877M | 12.83% | $27,673M | −$12,297M | $15,376M | 96.9% |
| FY2025 | $123,707M | $88,756M | 71.75% | $20,672M | $19,660M | 15.89% | $33,643M | −$11,761M | $21,882M | 111.3% |

Source: [stockanalysis.com/stocks/CMCSA/financials](https://stockanalysis.com/stocks/CMCSA/financials/), [.../cash-flow-statement](https://stockanalysis.com/stocks/CMCSA/financials/cash-flow-statement/). (FY2022's uncharacteristically low net income/high FCF-NI ratio reflects a large impairment that year — noted here for context, not adjusted out, since no specific normalization guidance for it was found this session.)

**TTM snapshot (stockanalysis.com statistics page):** Net Margin 15.00%, ROIC 8.00%, ROE 20.92%, Debt/Equity 1.07, TTM EBITDA $35,375M. Source: [stockanalysis.com/stocks/CMCSA/statistics](https://stockanalysis.com/stocks/CMCSA/statistics/).

**Balance sheet (Q1 2026, 31 March 2026 — primary source, SEC Form 10-Q):** Total Debt $94,612M (current portion $5,394M + noncurrent $89,218M), Cash & Cash Equivalents $9,468M, Total Shareholders' Equity $88,274M → **Net Debt = 94,612 − 9,468 = $85,144M**. Source: Comcast Q1 2026 Form 10-Q, condensed consolidated balance sheet, [sec.gov/.../cmcsa-20260331.htm](https://www.sec.gov/Archives/edgar/data/0001166691/000162828026026805/cmcsa-20260331.htm).

**Q1 2026 income statement (same 10-Q, for context):** Revenue $31,457M (+5.3% YoY per the filing's own commentary), Operating Income $4,135M, Net Income attributable to Comcast $2,174M (net margin 6.91% for the quarter — well below the TTM 15.00% figure above, driven per the filing's own disclosure by higher programming expense and investment losses from the **Atairos** vehicle — see Glossary). Not used directly in the Quality Score sub-scores below (which use the TTM/FY2025 annual bases per this framework's standard convention), but flagged as a data point showing recent-quarter profitability pressure.

### 3.2 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | CMCSA data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF positive in **every one of the last 5 fiscal years** (FY2021–FY2025, table above) — never negative. | **Does not fire.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | Ratio was **above 70% in all 5 of the last 5 fiscal years** (96.9%–313.8%, table above). | **Does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard — Comcast is not a payment network/exchange, so the Upgrade 5 asset-light 4×/6× override does not apply)** | Net Debt $85,144M ÷ TTM EBITDA $35,375M = **2.41×**. Below the 2.5× threshold, but **close enough to flag explicitly for human review** — a modest further debt increase, EBITDA decline, or a stricter same-basis (fully-post-Versant TTM EBITDA) recalculation could push this over 2.5×. | **Does not fire** (flagged — close to threshold). |

**No hard disqualifier fires**, though the Balance Sheet ratio is flagged as close to its threshold. Proceeding to the full weighted score for transparency (per operating-brief.md's "no black-box outputs").

### 3.3 Sub-score calculation

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((15.00/30)×100, 0, 100) = **50.00**. ROIC_Component = clamp((8.00/30)×100, 0, 100) = **26.67** (TTM figures, stockanalysis.com statistics page). Profitability_Score = (50.00+26.67)/2 = **38.33**. FCF-positive 5 consecutive years, so no cap applies. | **38.33** |
| **Margins (15%)** | GrossMargin_Score = clamp((71.75/80)×100, 0, 100) = **89.69** (FY2025 gross margin). **5-year trend:** 66.96% (FY2021) → 68.53% (FY2022) → 69.76% (FY2023) → 70.08% (FY2024) → 71.75% (FY2025) — genuinely, steadily expanding. **No +10 trend bonus applies**, per [quality-scoring.md](../framework/quality-scoring.md)'s explicit wording: the bonus is for a margin *below* the 40% base threshold that is nonetheless expanding structurally; CMCSA's margin is already well above 40%, so the base formula alone applies. | **89.69** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $121,427M → FY2025 $123,707M) = (123,707/121,427)^(1/3) − 1 = **+0.62%/yr**. Base Growth_Score = clamp((0.62/25)×100, 0, 100) = **2.49**. **Modifier — documented structural deceleration applied (−10):** see evidence below. Growth_Score = clamp(2.49 − 10, 0, 100) = **0.00**. | **0.00** |
| **Balance Sheet (15%)** | Net Debt/EBITDA = 85,144/35,375 = **2.41×**. BalanceSheet_Score = clamp(100×(1−2.41/4), 0, 100) = **39.83**. | **39.83** |
| **Moat Signal (15%)** | See evidence table below — **1 of 5** signals cleared the cited-evidence bar. Moat_Score = (1/5)×100 = **20.00** | **20.00** |
| **FCF Quality (10%)** | FCF/NI (FY2025, most recent complete fiscal year) = $21,882M / $19,660M = **111.3%** → clamp(((1.113−0.40)/0.60)×100, 0, 100) = clamp(118.83, 0, 100) = **100.00** (clamped). | **100.00** |

**Growth modifier evidence (documented structural deceleration, cited):**
- **Cord-cutting (video):** Comcast's video/linear-TV subscriber base has been in secular, industry-wide decline for years — a structural, not cyclical, trend consistently reported across the cable sector. See **Cord-cutting** in the Glossary.
- **Broadband — still shrinking, though the rate of loss is improving:** Comcast lost **65,000** net domestic broadband customers in Q1 2026 (an improvement from −183,000 in Q1 2025), with Co-CEO Mike Cavanagh stating on the earnings call that "**fixed wireless continues to market aggressively across our footprint**" and that "**fiber over-build is moving at a rapid pace**." Across Comcast, Charter, and Altice combined, the industry lost 280,000 broadband subscribers in Q1 2026 (vs. 320,000 in Q1 2025) — a multi-quarter, industry-wide pattern, not a one-off. Sources: [Fierce Network](https://www.fierce-network.com/broadband/comcasts-q1-2026-broadband-losses-were-less-bad-expected), [Light Reading](https://www.lightreading.com/cable-technology/comcast-shares-climb-amid-narrowing-broadband-losses-record-mobile-gains), [TelecomLead](https://telecomlead.com/broadband/us-cable-broadband-operators-lost-280000-internet-subscribers-in-q1-2026-despite-offering-mobile-bundles-for-customer-retention-126743).
- **No offsetting +10 TAM-expansion/pricing-power modifier applies:** the documented evidence found this session is defensive (multi-year price locks, promotional bundling to *arrest* churn), not evidence of pricing power or a growing addressable market. Xfinity Mobile's record 435,000 net adds in Q1 2026 and Peacock's subscriber growth are genuine bright spots (noted qualitatively) but are not yet large enough, on the filed consolidated figures above, to lift the company-wide revenue trend out of essentially flat.

**Moat signal evidence (cited, per signal — all five checked against the framework's required cited-evidence bar):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable or growing | Comcast remains the largest US cable broadband provider (~40%+ of US broadband subscriptions per aggregator estimates), but its **actual subscriber count is still shrinking** — net domestic broadband losses in every recent quarter (−65,000 Q1 2026, −183,000 Q1 2025). Narrowing losses is not the same as "stable or growing." | **FALSE** |
| Brand premium | No cited evidence of price increases sustained without volume loss. The opposite is documented: Comcast has rolled out a **5-Year Price Guarantee** and elevated promotional bundling specifically to *defend* subscriber volume against fiber/FWA competition — a defensive, not pricing-power, pattern. | **FALSE** |
| Network effect | No documented two-sided-marketplace or user-growth-driven-value mechanism found for cable broadband/media distribution. | **FALSE** |
| Switching costs | **TRUE.** Comcast's 5-Year Price Guarantee (roughly 50% of new Connect customers had opted in by Q2 2025) locks a rate for five years; leaving early forfeits that locked-in price, and Xfinity Mobile bundling (record 435,000 net adds in Q1 2026) adds a second bundled service to unwind. Company commentary cited "continued stabilization in voluntary churn" tied to this program. Documented mechanism (contractual rate lock + multi-service bundling), cited: [Light Reading](https://www.lightreading.com/customer-experience/your-carrier-s-price-lock-may-not-lock-your-price), [The Desk](https://thedesk.net/2026/07/parks-broadband-churn-tracker-q1-2026/). | **TRUE** |
| Scale cost advantage | Qualitative claims of national HFC-network scale and programming-purchasing-power cost advantages were found in trade commentary, but **no specific cost-per-subscriber or cost-per-unit figure benchmarked against a named smaller competitor** was located this session — the same evidentiary shortfall that kept TSMC's CoWoS packaging capacity from being credited as a moat signal for NVDA in this framework's 2026-07-05 session. Considered, not credited, for lacking the required cost-per-unit citation. | **FALSE** (flagged) |

### 3.4 Final weighted Quality Score

```
Quality Score = (38.33 × 0.25) + (89.69 × 0.15) + (0.00 × 0.20) + (39.83 × 0.15) + (20.00 × 0.15) + (100.00 × 0.10)
              = 9.5825 + 13.4535 + 0.0000 + 5.9745 + 3.0000 + 10.0000
              = 42.0105 → 42.0 (rounded to nearest 0.1)
```

**42.0 < 80.0 — fails the gate by 38.0 points.** This is not a close call, and is not sensitive to any of this session's judgment calls: even crediting the two most favorable disputable inputs at their maximum plausible reading — Moat at 40.0 (crediting the flagged-but-uncertain scale-cost-advantage signal too) and Growth at its un-modified base of 2.49 (dropping the −10 structural-deceleration modifier entirely) — the total only rises to roughly **45.6**, still 34+ points short of the gate. The dominant driver of the fail is structural: essentially flat consolidated revenue (3yr CAGR +0.62%) and thin profitability (Net Margin 15.00%/ROIC 8.00% TTM) in a company whose core connectivity/media businesses face genuine, well-documented competitive headwinds (cord-cutting, fixed wireless, fiber overbuild).

### Result: **Phase 01 FAIL — weighted Quality Score 42.0, misses the 80.0+ gate by 38.0 points.** No hard disqualifier fires, though the Net Debt/EBITDA ratio (2.41×) sits close enough to its 2.5× threshold to flag for human attention.

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... or a hard disqualifier fires, stop there and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.** (For color only, not scored: stockanalysis.com's statistics page shows CMCSA trading at a Trailing PE of 4.64× and Forward PE of 6.78× — a genuinely cheap multiple, consistent with the stock's −11.91% YTD move and its position near the low end of its 52-week range. Cheapness on current multiples does not substitute for clearing the quality gate; per this framework's design, the Composite Score step is never reached from here regardless of how statistically cheap the stock looks.)

---

## 4. Recommendation

**PASS.** Do not open a position, and do not place a limit order. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring, per the Phase 03 table in [strategy.md](../framework/strategy.md) (Composite Score is a precondition for that table applying at all).

This is not a verdict that Comcast's underlying assets (the largest US cable/broadband franchise, NBCUniversal's studio and Peacock streaming business, Universal's theme parks) are worthless, nor that the stock's statistically cheap multiple (Trailing PE 4.64×) is wrong on some other framework — it is a verdict that, on the specific, cited, filed financial facts available today (essentially flat consolidated revenue, thin single-digit-to-mid-teens profitability, and a mostly-unsupported moat case resting on one cited signal out of five), Comcast does not currently clear this framework's strict, quantitative definition of "high quality." The cheap multiple is more consistent with a **value trap** setup than a mispriced compounder until the documented structural headwinds (cord-cutting, fixed-wireless/fiber competitive share loss) show a real reversal — see the Value trap entry in the Glossary.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) broadband net additions turning positive (not just narrower losses) for 2+ consecutive quarters; (b) a sustained increase in revenue growth (3yr CAGR moving materially above the current ~0.6%) driven by Xfinity Mobile, Peacock, or theme parks scaling enough to move the consolidated number; (c) a quarterly earnings release or guidance revision (the Telegram post's trigger — CMCSA reports "this week" per the post, so the next print is a natural re-check point); (d) a management change or material M&A/strategic-investment event (including any further Atairos-related swings); (e) a >15% stock-price move with no identified cause; (f) enough post-Versant quarters accumulating to recompute the Growth/Margin trend on a clean, fully comparable post-spin-off basis (see §2 reporting-basis caveat).
- Absent any of the above, future Telegram mentions of CMCSA should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Data gaps flagged (Rule 0)

- **`yfinance` unusable this session** (documented `curl_cffi` TLS-reset failure through the proxy, same recurring environment issue as prior sessions) — worked around via `WebFetch` against stockanalysis.com (an aggregator, flagged as such throughout), cross-checked against Comcast's own Q1 2026 SEC Form 10-Q for the balance sheet/income-statement figures that matter most to the Balance Sheet sub-score. No financial figure below was estimated or invented to compensate.
- **ROIC (8.00% TTM) and Net Margin (15.00% TTM)** are taken directly from stockanalysis.com's statistics page, not independently re-derived from primary-filing NOPAT/invested-capital components this session — flagged as an aggregator-sourced figure, consistent with this framework's standard practice elsewhere when a primary-source recomputation isn't performed.
- **Reporting-basis discontinuity from the Versant Media Group spin-off (2 January 2026):** the FY2021–FY2025 annual figures used for the Growth/Margins sub-scores still consolidate Versant; the Q1 2026 balance sheet used for the Balance Sheet sub-score does not. See §2. Flagged for human review; does not change the ultimate PASS conclusion (§3.4's sensitivity check).
- **Total Shareholders' Equity** showed a small ~$266M discrepancy between stockanalysis.com ($88,540M) and the primary-source 10-Q ($88,274M) — the 10-Q figure is used; not material to any sub-score (Balance Sheet uses Net Debt/EBITDA, not equity, as its input).
- Forward PE (6.78×), Trailing PE (4.64×), EV/EBITDA (4.81×), EV/EBIT (8.89×), and Dividend Yield (5.55%) were pulled for context/citation only — not scored, since Phase 02 was never reached.

---

## 8. Glossary

- **Atairos** — A private investment vehicle originally capitalized by Comcast to hold investments outside its core cable/media businesses; gains/losses on Comcast's remaining economic interest flow through Comcast's GAAP net income each period. Cited as a driver of Comcast's weaker Q1 2026 net income (§3.1).
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every company that files with EDGAR.
- **Composite Score** — This framework's single ranking number (0.0–100.0) blending the Quality Score and Valuation Score 50/50 — not computed for CMCSA since it never clears the 80.0+ Quality Score gate.
- **Cord-cutting** — The secular, industry-wide trend of consumers cancelling traditional pay-TV subscriptions in favor of streaming — a structural, not cyclical, headwind cited in the Growth sub-score's deceleration modifier (§3.3).
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit.
- **EV/EBIT, EV/EBITDA** — Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure. Cited for CMCSA context only (8.89× and 4.81× respectively) — not scored, since Phase 02 was never reached.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. Positive for CMCSA in every one of the last 5 fiscal years.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. Above 70% in every one of CMCSA's last 5 fiscal years (§3.2) — no disqualifier fires here.
- **Fixed Wireless Access (FWA)** — Home internet delivered over a cellular network instead of a wired connection — a documented, structural competitive threat to Comcast's broadband subscriber growth (§3.3).
- **Forward PE** — Price ÷ next twelve months' *expected* earnings per share, distinct from Trailing PE (last twelve months' *actual* earnings). Cited for CMCSA context only (6.78×) — not scored, since Phase 02 was never reached.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. One of this framework's Quality Score Margins sub-score inputs; CMCSA's has genuinely expanded from ~67% (FY2021) to ~71.8% (FY2025).
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score — see [quality-scoring.md](../framework/quality-scoring.md). None fires for CMCSA, though the Net Debt/EBITDA ratio (2.41×) is flagged as close to its 2.5× threshold (§3.2).
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. CMCSA cleared only 1 of the framework's 5 cited-evidence moat signals this session.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio. CMCSA's is 2.41× as of Q1 2026.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. CMCSA scores **42.0**.
- **ROE** — Return on Equity — Net Income ÷ shareholder equity. CMCSA's TTM ROE is 20.92%.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. CMCSA's TTM ROIC is 8.00%.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 6** — This framework's instruction to normalize earnings/margins/revenue/debt before valuing a business, rather than valuing the raw accounting statements as-is — invoked here for the Versant spin-off reporting-basis caveat (§2).
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **Trailing PE** — Price ÷ the last twelve months' *actual* earnings per share. Cited for CMCSA context only (4.64×).
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **Value trap** — A stock that looks statistically cheap but stays cheap or keeps falling because the underlying business quality is genuinely deteriorating — the risk this framework's 80.0+ Quality Score gate is specifically designed to surface rather than acting on CMCSA's cheap multiple alone (§4).
- **Versant Media Group (VSNT)** — Comcast's former cable-networks portfolio (MS NOW, CNBC, USA Network, Golf Channel, E!, SYFY, Oxygen), spun off into a separate public company effective 2 January 2026 — the source of this session's reporting-basis caveat (§2).

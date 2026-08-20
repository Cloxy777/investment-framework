# New Position Evaluation: BULL (Webull Corporation) — 2026-08-20

**Task type:** NEW POSITION (Rule 9 fundamental-event re-evaluation — earnings)
**Ticker:** BULL — NASDAQ, contract_id 776352706 (IBKR), "WEBULL CORP," country_code US
**Company:** Webull Corporation — digital retail brokerage / trading platform, Saint Petersburg, FL. Public via SPAC merger, first trade ~2025-04-11.
**Analyst:** Claude (automated session, Telegram-triggered)
**Account:** U19421206 (IBKR)
**Current portfolio weight:** 0% (not held — absent from [holdings.md](../portfolio/holdings.md))
**Prior sessions:** [2026-06-21-new-position-bull.md](2026-06-21-new-position-bull.md) (Phase 01 FAIL, 6/9 criteria fail; Phase 02 = 100.0 "Extreme," computed for the record only) → [2026-07-06-new-position-bull.md](2026-07-06-new-position-bull.md) (15-day recheck; no Rule 9 trigger; first Quality Score computed = 54.0/100.0, fails the 80.0+ gate)

---

## 0. Trigger

A Telegram post in the **bolshegold** channel reported Webull's Q2 2026 earnings (2026-08-19). This is a **Rule 9 fundamental event (quarterly earnings)** for a name already on the not-in-portfolio watchlist — per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 9 and [watchlist/README.md](../watchlist/README.md), this independently warrants a fresh `/new-position` pass. The Telegram post's headline numbers were **independently verified via WebSearch against the company's own SEC Form 6-K exhibit** (primary source) before being used for anything beyond triggering this session — see §1 for the one material discrepancy found.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$9.78** (last trade) | IBKR `get_price_snapshot`, contract_id 776352706 (NASDAQ: BULL, same contract resolved in prior sessions), ts 1787184492 → **2026-08-20 00:08:12 UTC** |
| Bid / Ask | $9.79 / $9.81 | IBKR `bid_ask` |
| Change | **+$1.14 / +13.19%** (vs. prior close) | IBKR `change` — reflects the market's reaction to the Q2 2026 beat reported the prior day |
| 52-week high / low | $16.04 / $4.50 | IBKR `misc_statistics` |
| 13-week high / low | $8.35 / $5.37 | IBKR `misc_statistics` — **stale relative to the live quote**: today's $9.78 already exceeds the cached 13-week high ($8.35), confirming the field hasn't rolled forward intraday; noted for transparency, not corrected (not an input to any calculation below) |

**Confirmed correct instrument**: NASDAQ:BULL, "WEBULL CORP" — the sole STK match with that description among the many unrelated "BULL"-named instruments IBKR's search returns (gold ETFs, leveraged-ETF IOPVs, a Canadian mining company, municipal bonds, etc.), consistent with the contract_id used in both prior BULL sessions.

### Independent verification of the Telegram post's numbers

| Metric | Telegram claim | Verified (SEC Form 6-K, primary source) | Match? |
|---|---|---|---|
| Revenue | $198.83M (+51% YoY) | **$198,831,080** (+51% YoY, per company release) | ✅ Exact match |
| Adjusted operating profit | $62.6M (+169% YoY, 31.3% margin) | **$62,590,100** adjusted operating profit; margin computed two ways in company materials (31.3%–31.5% depending on denominator/rounding) | ✅ Match (margin rounding variance only) |
| Customer assets | $28.5B (+79% YoY) | **$28.5 billion** (+79% YoY) | ✅ Exact match |
| **GAAP EPS** | **$0.07, beating $0.03 estimate** | **Basic $0.05 / Diluted $0.04** — GAAP net income attributable to Company **$24,364,324** for the quarter | ❌ **Does not match.** The $0.07 figure does not correspond to Q2 2026 on any basis found (GAAP or adjusted-operating-profit-per-share, which was $0.12). It does exactly match Webull's own **Q3 2025** diluted EPS ($0.07, per that quarter's press release) — most likely the Telegram post conflated a different quarter's figure. **The verified $0.05/$0.04 GAAP EPS is what's used below; the Telegram $0.07 figure is not used anywhere in this evaluation**, consistent with the standing rule to never use a Telegram post's numbers as financial inputs. |

**10Y US Treasury yield (context only, not gating — see §3):** ~4.75% (2026-08-19 print, WebSearch/TradingEconomics) — in the 3.5–5% Rate Regime Modifier band, would be +5 if Phase 02 were reached.

---

## 2. Phase 01 Quality Gate — recomputed fresh (not carried over)

Per task instruction and [quality-scoring.md](../framework/quality-scoring.md), the full Quality Score is recomputed from current data rather than reusing the 54.0 figure from 2026-07-06. All financial data sourced from Webull's own SEC filings (Form 6-K exhibits, the authoritative primary source) via WebSearch/WebFetch — cross-checked against stockanalysis.com as a secondary source — never estimated. TTM = trailing twelve months, **Q3 2025 – Q2 2026** (the four most recently completed quarters as of this session).

### 2a. Quarterly source data assembled (all from Webull's own SEC Form 6-K press-release exhibits)

| Quarter | Revenue | Total OpEx | Op. Income (Rev − OpEx) | Income before tax | Tax provision | Net income attrib. to Company | Source |
|---|---|---|---|---|---|---|---|
| Q3 2025 | $156.9M | $132.5M | $24.4M | $38.95M | $2.16M | $36.92M | [PR Newswire, Q3 2025 results](https://www.prnewswire.com/news-releases/webull-reports-third-quarter-2025-financial-results-302622073.html) |
| Q4 2025 | $165.2M | $147,999,822 | $17.20M | $8.1M | $5.1M | $3.0M | [SEC 6-K, Q4/FY2025](https://www.sec.gov/Archives/edgar/data/1866364/000121390026023688/ea027951201ex99-1.htm) |
| Q1 2026 | $159,928,016 | $162,306,571 | −$2,378,555 | −$12,810,716 | $8,927,156 | −$21,722,730 | [SEC 6-K, Q1 2026](https://www.sec.gov/Archives/edgar/data/0001866364/000121390026060085/ea029183001ex99-1.htm) |
| Q2 2026 | $198,831,080 | $153,376,176 | $45,454,904 | $34,686,474 | $10,343,085 | $24,364,324 | [SEC 6-K, Q2 2026](https://www.stocktitan.net/sec-filings/BULL/6-k-webull-corp-current-report-foreign-issuer-493c0f9e55d6.html) |
| **TTM** | **$680.86M** | **$596.18M** | **$84.68M** | **$68.93M** | **$26.53M** | **$42.56M** | Sum of the four rows |

**Methodology note (disclosed choice):** "Operating Income" here = Revenue − Total Operating Expenses, as directly reported per quarter — a transparent, reproducible EBIT proxy. This differs somewhat from third-party aggregator "operating income"/EBIT fields (e.g. stockanalysis.com shows different per-quarter splits), which appear to classify some line items differently; the primary-source, self-computed figure is used here per "show every calculation." **Effective tax rate (TTM) = $26.53M ÷ $68.93M = 38.5%**, applied to TTM EBIT for NOPAT below.

### 2b. Hard disqualifier check (fails regardless of weighted score — evaluated on the rolling window, per the 2026-08-05 clarification)

| Hard disqualifier | Applies to BULL? | Basis |
|---|---|---|
| FCF/NI conversion ratio <70% for 2+ **consecutive** years | **No** | Most recently completed fiscal years (FY2026 not yet complete, so the window is still FY2022–FY2025, unchanged from the 07-06 session): FY2022 −125.3%, FY2023 +7,678.9%, FY2024 −805.5%, FY2025 +2,266.9%. FY2022 and FY2024 fall below 70% but are not consecutive (FY2023 sits between at a mechanically high ratio) — same conclusion as before. As previously documented, these literal ratios are themselves not meaningful for a broker-dealer (customer-cash/margin working-capital swings dominate reported operating cash flow — "Change in Other Working Capital" was +$806.3M in FY2025 alone) — the disqualifier test, applied as written, does not fire. |
| Net Debt/EBITDA over threshold (2.5× standard / 4× asset-light) | **No** | Deeply net-cash as of 2026-06-30: Total debt $67,611,040 (Revolving credit facility $17,611,040 + Unsecured promissory notes $50,000,000) vs. cash $701,621,304 → **Net debt = −$634.0M**. TTM EBIT is unambiguously positive ($84.68M, and TTM EBITDA is at least that large since D&A ≥ 0), so Net Debt/EBITDA is unambiguously deeply negative regardless of the exact EBITDA figure — no fire, by a wide margin. Even more net-cash than the −$575.7M figure at the 06-21/07-06 sessions. |
| Not FCF-positive for 3+ consecutive years | **No** | FY2023 +$466.1M, FY2024 +$182.8M, FY2025 +$561.5M — three consecutive years, mechanically positive (same basis as before; quality of this figure is separately addressed in the FCF Quality sub-score, not this binary test). |

**No hard disqualifier fires** — same conclusion as 2026-07-06.

### 2c. Weighted Quality Score

| Sub-score (weight) | Inputs (fresh, TTM basis unless noted) | Calculation | Result |
|---|---|---|---|
| **Profitability** (25%) | **Net Margin (TTM) = $42.56M ÷ $680.86M = 6.25%.** **ROIC (TTM):** NOPAT = TTM EBIT $84.68M × (1 − 38.5% eff. tax rate) = **$52.08M**. Invested Capital (as of 2026-06-30) = Total Debt $67.61M + Equity $1,043.53M − Cash $701.62M = **$409.52M**. ROIC = 52.08 ÷ 409.52 = **12.71%**. *(First genuine TTM-basis ROIC computed for BULL — the 07-06 session used a FY2025-basis figure "as-is" for lack of a constructible TTM number at the time; four full quarters of primary-source data now exist to build one properly.)* | NetMargin_Component = clamp((6.25/30)×100) = 20.8. ROIC_Component = clamp((12.71/30)×100) = 42.4. Avg = (20.8+42.4)/2 | **31.6** (no FCF cap — FCF mechanically positive 3 consecutive years) |
| **Margins** (15%) | Gross margin proxy = (Revenue − Brokerage & transaction cost) ÷ Revenue, same convention as prior sessions (this is a broker-dealer's closest analog to cost-of-revenue; no distinct COGS line is disclosed). TTM: ($680.86M − $153.44M brokerage/transaction) ÷ $680.86M = **77.46%**. 4-point trend: 84.6% (FY2022) → 79.7% (FY2024) → 77.45% (FY2025) → **77.46% (TTM)** — the multi-year contraction has **stabilized**, not reversed | clamp((77.46/80)×100) = 96.8. No structural-expansion bonus — trend is flat-to-historically-contracting, not expanding | **96.8** |
| **Growth** (20%) | Revenue 3yr CAGR (FY2022 $388.21M → FY2025 $571.0M, most recent completed FYs, unchanged basis from prior sessions since FY2026 isn't complete) = **13.72%**. Documented TAM/engagement evidence (Q2 2026 release, cited): customer assets $28.5B (+79% YoY), DARTs 1.6M (+62% YoY), funded accounts 5.13M (+8% YoY), registered users 28.2M (+13% YoY), 35 licensed markets (18 active) with a new Pi Securities (Thailand) acquisition for APAC expansion, Vega AI analyst tool at 480K active users, Pattern Day Trader rule elimination (2026-06-04) cited by management as a direct driver of this quarter's results. **Revenue growth is accelerating, not decelerating** — Q1 2026 +36% YoY → Q2 2026 +51% YoY | clamp((13.72/25)×100) = 54.9; **+10** TAM-expansion bonus (cited, accelerating growth, multiple independent confirming metrics, no evidence of deceleration) | **64.9** |
| **Balance Sheet** (15%) | Net Debt/EBITDA deeply negative (net cash −$634.0M vs. positive TTM EBIT $84.68M/EBITDA ≥ $84.68M) — see §2b | clamp(100×(1 − negative/4)) clamps at the ceiling regardless of exact EBITDA magnitude | **100.0** |
| **Moat** (15%) | Re-checked fresh, not carried over: (1) *Market share* — Webull discloses only its own absolute growth (assets, DARTs, accounts), not share vs. Robinhood/Schwab/IBKR/Fidelity; a targeted search for comparative market-share/ranking data found none. **FALSE**. (2) *Brand premium* — no pricing-power evidence; commission-free trading remains commoditized industry-wide. **FALSE**. (3) *Network effect* — community/social-trading layer and the new Vega AI tool (480K users) are real product features, but no documented mechanism shows value compounding with user growth (not proven, just asserted). **FALSE**. (4) *Switching costs* — real but not high (unchanged assessment). **FALSE**. (5) *Scale cost advantage* — no cost-per-unit data vs. smaller competitors. **FALSE** | (0 of 5 signals meet the cited-evidence bar) / 5 × 100 | **0.0** |
| **FCF Quality** (10%) | Literal FCF/NI ratios remain not meaningful (brokerage customer-cash float). Owner-earnings-style proxy (same convention as prior sessions — full CapEx conservatively treated as maintenance, no growth/maintenance split disclosed): TTM D&A ≈ **$3.20M** and TTM CapEx ≈ **$4.89M** — both **approximated from FY2025 annual figures** (Webull's press releases do not disclose a full cash-flow statement with quarterly D&A/CapEx detail; FY2025 D&A/CapEx were independently sourced from FY2025 cash-flow data, cross-checked across two sources). This is a disclosed approximation, not an invented number, and is immaterial to the result (a ±$2M swing in either line moves the ratio by ~5pp, not enough to change the score band). Proxy = NI $42.56M + D&A $3.20M − CapEx $4.89M = **$40.87M**. Ratio = 40.87 ÷ 42.56 = **96.0%** | clamp(((96.0−40)/60)×100) | **93.3** |

```
Quality Score = 31.6×0.25 + 96.8×0.15 + 64.9×0.20 + 100.0×0.15 + 0.0×0.15 + 93.3×0.10
              = 7.900 + 14.520 + 12.980 + 15.000 + 0.000 + 9.330
              = 59.730 ≈ 59.7
```

### **Quality Score: 59.7 / 100.0 — fails the 80.0+ gate** (by 20.3 points)

A meaningful improvement from **54.0 (2026-07-06)**, driven almost entirely by the Q2 2026 beat: Profitability rose from 10.4 → **31.6** (TTM net margin flipped from negative to +6.25%, ROIC from 6.20% FY2025-basis to a genuinely-computed 12.71% TTM) and FCF Quality rose from 88.8 → **93.3**. Margins, Growth, and Balance Sheet are essentially unchanged. **Moat remains the decisive, unmoved weakness (0.0/100.0)** — no durable-competitive-advantage signal clears the cited-evidence bar, and this single sub-score alone (15% weight, contributing 0 of a possible 15.0 points) accounts for most of the remaining gap to the 80.0 threshold. Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md): **this session stops here.** No Rate Environment Gate, Phase 02 valuation score, Composite Score, or order setup is computed.

---

## 3. Rate Environment Gate — not run

Per the command spec, Phase 02 (which the Rate Environment Gate precedes) is only run once the Quality Score clears 80.0. It does not (59.7). US 10Y Treasury (~4.75%, 2026-08-19) is noted in §1 for context/audit-trail completeness only — it plays no role in this session's outcome.

---

## 4. Five Qualitative Questions (per the operating-calendar template — for the record)

**1. Why are margins high?** Gross margin (77.46% TTM) reflects genuine software/platform economics — incremental trades cost little to serve once the platform exists. It is not a one-off, but it has **contracted** over the company's public history (84.6% FY2022 → 77.46% TTM) before stabilizing this year, and net profitability at the bottom line remains thin (6.25% TTM net margin) even after a strong quarter.

**2. What would it take to compete with them?** Retail brokerage competition remains intense and well-capitalized (Robinhood, Schwab, IBKR, Fidelity). No cited relative market-share data was found this session either (checked explicitly — see Moat table). Webull's differentiators (options/derivatives tooling, international/APAC access via the new Thailand acquisition, the Vega AI tool, community/social features) are real product investments but not yet documented as a durable moat.

**3. How has management allocated capital over 5–10 years?** Still only ~16 months of public-company history. This quarter: continued platform/product investment (Vega AI, Pi Securities acquisition), no dividend, share count grew modestly (524.6M total, 2025-12-31 → 530.6M basic, 2026-06-30, +1.1% over two quarters) — a much milder pace than the +13.9% FY2025 SPAC-related jump, and plausibly ordinary equity-comp vesting rather than a fresh dilutive raise.

**4. Where is growth coming from next 3–5 years?** Same drivers as before, now with a full quarter of confirming data: customer-asset growth (+79% YoY to $28.5B), trading-volume growth (options contracts +68% YoY, equity notional +73% YoY), the Pattern Day Trader rule removal (a regulatory tailwind, 2026-06-04), and international expansion (35 licensed markets, Thailand acquisition, ~810K international funded accounts, >$5B international customer assets).

**5. Best bear case against owning it?** (a) Earnings quality — the reported FCF figure remains structurally unreliable for this business model; the owner-earnings proxy used here is materially better but still built on approximated D&A/CapEx. (b) Profitability, while now clearly positive on a TTM basis, is a two-quarter trend (Q1 2026 was a $21.7M loss) inside a longer history of volatility — not yet the multi-year durable record the framework's Profitability threshold (30% reference point) implies. (c) No moat signal clears the evidence bar — competitive intensity in commission-free brokerage is high and largely commoditized. (d) Revenue and earnings remain structurally tied to retail trading-volume cyclicality, which is sentiment-driven (visible in the Q1→Q2 2026 swing itself). (e) This quarter's strength is partly attributable to a one-time regulatory tailwind (PDT rule elimination) rather than a purely organic, repeatable driver — worth re-testing next quarter for durability.

**Disruption vector check:** Unchanged — no single technology threatens online brokerage itself within 5 years, but commoditization pressure (fee-free trading, fractional shares, AI-assisted tools) is industry-wide and ongoing.

---

## 5. Order Setup — NOT applicable

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) and [operating-brief.md](../framework/operating-brief.md), order setup (buy price, sell target, stop loss, R/R, position size) is only constructed once a Quality Score clears the 80.0+ gate and a Composite Score is computed. Neither happened here (59.7 < 80.0). **No order setup is applicable.** (For reference, current combined portfolio value per [holdings.md](../portfolio/holdings.md) is ≈$65,888.42 as of the 2026-08-16 sync — not used in this session, noted only because it would gate any hypothetical position size against the 15% cap if this had reached that stage.)

---

## 6. Data quality flags carried forward (summary)

- **Telegram EPS figure ($0.07) does not match Q2 2026** — verified GAAP EPS is $0.05 basic / $0.04 diluted; the $0.07 figure matches Q3 2025's diluted EPS instead, suggesting the original post (or an intermediate source) conflated quarters. Not used anywhere in this evaluation.
- **TTM D&A ($3.20M) and CapEx ($4.89M) approximated from FY2025 annual figures** — no quarterly cash-flow-statement breakdown is disclosed in Webull's press releases (only the income statement and balance sheet are included in the Form 6-K exhibits; the full cash-flow statement appears only in the annual Form 20-F). This affects only the FCF Quality sub-score (10% weight) and is immaterial to the pass/fail outcome — even a ±$2M swing would not move the Quality Score meaningfully, let alone across the 80.0 gate (which BULL misses by 20.3 points).
- **"Operating Income" (EBIT proxy) computed directly (Revenue − Total OpEx) rather than taken from a third-party aggregator field** — disclosed in §2a; third-party sources (e.g. stockanalysis.com) show different per-quarter operating-income splits, likely reflecting different line-item classification. The self-computed, fully reproducible figure is used throughout.
- **Reported FCF / FCF-NI conversion ratio still not usable at face value** for this business model — same brokerage customer-cash-float distortion documented in the 06-21 session. The owner-earnings-style proxy is used for the FCF Quality sub-score instead.
- **No relative/competitive market-share data found** for the Moat sub-score's first signal, despite an explicit targeted search this session (options-volume ranking vs. peers) — Webull discloses only its own absolute growth metrics.

None of these gaps prevented scoring — the Quality Score computation is complete, and the 20.3-point gap to the gate is driven by two clear, well-evidenced sub-scores (Moat 0.0, and to a lesser extent still-modest Profitability 31.6), not by any missing input.

---

## 7. Recommendation: **PASS — watchlist only**

**Quality Score 59.7/100.0 fails the 80.0+ gate.** Per [.claude/commands/new-position.md](../.claude/commands/new-position.md), the session stops at the quality gate — no Rate Environment Gate, Phase 02 valuation score, Composite Score, or order setup is computed. This is an improvement from 54.0 (2026-07-06), driven by a genuinely strong Q2 2026 quarter (record revenue, record adjusted operating profit, GAAP profitability), but the gap to the gate (20.3 points) remains substantial and is anchored by the still-zero Moat sub-score — a structural, not cyclical, gap that a single strong quarter cannot close. **No position is opened; no order setup applies.**

**Next review trigger:** Next earnings release (Q3 2026, expected ~November 2026, per the prior quarterly cadence) — re-test Profitability and FCF Quality with another quarter of data, and specifically re-check whether Q1 2026's loss quarter proves to be the outlier (supporting a genuine profitability trend) or Q2 2026 proves to be the outlier (a PDT-rule-driven one-off). Sooner, if a Rule 9 event fires (guidance revision, M&A, management change, macro shift, >15% unexplained move) or if credible third-party market-share/competitive-ranking data emerges (would directly test the Moat sub-score's first signal).

---

## 8. Token usage note

This session involved one IBKR contract search + live price snapshot, roughly 14 WebSearch/WebFetch calls (Telegram-claim verification, Q1–Q4 2025 and Q1–Q2 2026 quarterly press releases/6-K exhibits, balance sheet, D&A/CapEx sourcing, market-share check, 10Y Treasury), and a full ground-up TTM reconstruction (revenue, operating income, tax rate, NOPAT, invested capital, gross margin, owner-earnings proxy) from four quarters of primary-source SEC data — a meaningfully heavier data-assembly load than the 07-06 recheck (which reused the 06-21 session's data untouched), closer to the 06-21 session's own level, consistent with the ~120–160K token/ticker range cited in the batch-processing guidance.

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets. |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **DART (Daily Average Revenue Trades)** | A brokerage-industry activity metric counting trades that generate revenue, averaged per trading day. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **EPS** | Earnings Per Share — net income divided by shares outstanding. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; flagged here as structurally distorted by brokerage customer-cash float. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook. |
| **Hard disqualifier** | One of three Quality Score gate conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company outright regardless of weighted score. None fires for BULL. |
| **Moat** | Warren Buffett's term for a durable competitive advantage protecting a business's profits from competitors. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; deeply negative (favorable) for BULL, reflecting a net-cash balance sheet. |
| **NOPAT** | Net Operating Profit After Tax — EBIT adjusted for taxes, used as the numerator in ROIC. |
| **Owner Earnings** | Buffett's adjusted cash-flow measure: Net Income + D&A − Maintenance CapEx; used here as a data-integrity correction to a distorted reported FCF figure. |
| **PDT (Pattern Day Trader) Rule** | A US regulation restricting frequent same-day trading in accounts under $25,000; its elimination (2026-06-04) removed a barrier to active trading, cited by Webull management as a driver of Q2 2026 results. |
| **Quality Score** | A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. BULL scores 59.7. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital (debt + equity) into profit. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **SPAC** | Special Purpose Acquisition Company — a shell company that raises money via IPO to merge with a private company and take it public; the mechanism by which Webull became a public company. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |

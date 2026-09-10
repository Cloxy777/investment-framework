# NEW POSITION — CAT (Caterpillar Inc., NYSE) — 2026-09-10

**Task type:** NEW POSITION (manual run)
**Date:** 10 Sep 2026
**10Y US Treasury Yield:** 4.84% ([tradingeconomics.com](https://tradingeconomics.com/united-states/government-bond-yield), quoted 2026-09-10)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §3). For reference, the bracket in force is +5 (10Y in the 3.5–5% range) per [strategy.md](../framework/strategy.md).
**Current CAT portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** none — first `/new-position` evaluation of CAT under this framework.
**Sector:** Industrials — heavy construction/mining equipment, engines, and power generation.
**First-use jargon decode:** see closing Glossary (§7).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$802.78** | IBKR `get_price_snapshot` (contract_id **5437**, NYSE, "CATERPILLAR INC" — confirmed correct entity via `search_contracts`, which returned dozens of unrelated "CAT*"-prefixed tickers/bonds/ETFs; contract_id 5437 is the only NYSE `CAT` common-stock listing among them), `last` field, timestamp epoch 1789067158 (2026-09-10) |
| Change vs. prior close | **−$12.78 / −1.57%** | IBKR `get_price_snapshot` `change` field |
| Bid / Ask | $802.32 / $802.60 | IBKR `get_price_snapshot` |
| 52-week range | Low **$420.75** · High **$1,073.46** | IBKR `get_price_snapshot` `misc_statistics` |
| US 10Y Treasury yield | 4.84% | tradingeconomics.com, 2026-09-10 |

**$802.78 is used as the live price for this session.** Today's −1.57% move is small and unremarkable — well short of the >15% "unexplained move" Rule 9 trigger.

---

## 2. Data Gathered — Sources & Method

No dedicated CAT financial-data pipeline exists in this repo yet (unlike the SEC-XBRL / IBKR-snapshot combination used for some other names) — every figure below comes from a live web search against a named source, with the underlying value cross-checked against a second source where one was found. This is disclosed per-figure below; anything not independently corroborated is flagged.

### 2.1 Income statement / margins (TTM unless noted)

| Metric | Value | Source |
|---|---|---|
| Net margin (TTM) | 14.29% | [stockanalysis.com/stocks/cat/statistics](https://stockanalysis.com/stocks/cat/statistics/) |
| ROIC (TTM) | 18.30% | stockanalysis.com (per above) |
| Gross margin (TTM) | 29.71% | stockanalysis.com (per above) |
| Operating margin, FY2025 | 16.5% (adjusted 17.2%), down from 20.2%/20.7% in FY2024 | [Caterpillar 4Q/FY2025 earnings release, prnewswire.com](https://www.prnewswire.com/news-releases/caterpillar-reports-fourth-quarter-and-full-year-2025-results-302673883.html) |
| Trailing PE | 35.08 | stockanalysis.com |
| Forward PE | 28.32 | stockanalysis.com |
| EV/EBITDA | 25.44 (24.51 per a second source, [gurufocus.com](https://www.gurufocus.com/term/ev2ebitda/NYSE:CAT)) | stockanalysis.com |
| EV/EBIT | 37.34x | Alpha Spread ([alphaspread.com](https://www.alphaspread.com/security/nyse/cat/relative-valuation/ratio/enterprise-value-to-ebit)) |
| Enterprise value | $413.35B | stockanalysis.com |
| Market cap | $374–375B (varies slightly by source/date) | stockanalysis.com, investing.com |
| Shares outstanding | 459.67M | stockanalysis.com |

### 2.2 Revenue history (annual, $ billions, fiscal year = calendar year)

| FY2022 | FY2023 | FY2024 | FY2025 | TTM (thru Q2 2026) |
|---|---|---|---|---|
| $59.427B | $67.06B | $64.809B | $67.589B | $74.7B |

Sources: FY2022 10-K ($59.427B, per [SEC EDGAR 10-K FY2022](https://www.sec.gov/Archives/edgar/data/18230/000001823023000011/cat-20221231.htm)); FY2023/FY2024/FY2025 per Caterpillar's own 4Q earnings releases; TTM thru Jun-2026 per [stockanalysis.com/stocks/cat/revenue](https://stockanalysis.com/stocks/cat/revenue/) ("$74.7B, up 18.36% YoY").

**Revenue 3yr CAGR used for the Growth sub-score** is computed from the three most recently *completed fiscal years* (FY2022 → FY2025), not the partial-year TTM figure, consistent with how the framework's other sessions treat this metric:
```
Revenue 3yr CAGR = (67.589 / 59.427)^(1/3) − 1 = 4.38%
```
The TTM figure is materially higher (accelerating growth — see §2.4) but is not itself the scored "3yr CAGR" input; it is used qualitatively as the basis for the documented-TAM-expansion modifier instead.

### 2.3 Balance sheet / leverage

| Metric | Value | Source |
|---|---|---|
| Net Debt/EBITDA, FY2025 | 2.4x (+18.7% YoY) | [macrotrends.net financial ratios](https://www.macrotrends.net/stocks/charts/CAT/caterpillar/financial-ratios) |
| Debt/EBITDA, TTM (Jun-2026) | 2.13x ("37% below 10-yr median of 3.37") | [gurufocus.com](https://www.gurufocus.com/term/debt-to-ebitda/CAT) |
| Total debt, FY2025 | $44.058B (short-term Financial Products $5.514B + long-term MP&E $10.678B + long-term Financial Products $20.018B, plus current portions not separately broken out here) | [Caterpillar 4Q/FY2025 earnings release](https://www.prnewswire.com/news-releases/caterpillar-reports-fourth-quarter-and-full-year-2025-results-302673883.html) |

The 2.4x / 2.13x figures are the company's consolidated Net Debt/EBITDA (i.e. they already fold in Cat Financial's captive-finance debt) — consistent with this framework's **conglomerate rule** (Phase 01/quality-scoring.md), which requires that consolidation rather than excluding financial-subsidiary debt. **This is below the 2.5x standard hard-disqualifier threshold** — CAT is not asset-light/investment-grade-override eligible in the sense Upgrade 5 defines (it is an industrial equipment maker, not a payment network/exchange), so the standard 2.5x threshold applies, and it passes.

### 2.4 Free cash flow / net income

| Metric | Value | Source |
|---|---|---|
| FCF, TTM (thru Jun-2026) | $8.994B | [gurufocus.com price-to-FCF page](https://www.gurufocus.com/term/price-to-free-cash-flow/CAT) |
| Net income, TTM (thru Mar-2026) | $9.430B (−5.12% YoY) | [tradingeconomics.com/cat:us:net-income](https://tradingeconomics.com/cat:us:net-income) |
| MP&E (Machinery, Power & Energy) segment FCF, FY2025 | $9.5B | Caterpillar FY2025 earnings release |
| Enterprise operating cash flow, FY2025 | $11.7B | Caterpillar FY2025 earnings release |

**Data-quality flag:** the FCF figure (TTM thru Jun-2026) and the net income figure (TTM thru Mar-2026) are drawn from two different sources covering slightly different trailing windows (a 3-month offset) — an exact same-window FCF/NI pairing wasn't locatable via web search this session. Used as the best available approximation: **FCF/NI ≈ 8.994 / 9.430 = 95.4%.** This is far enough above the 70% hard-disqualifier threshold that the 3-month window mismatch is very unlikely to change the pass/fail outcome, but it is flagged rather than presented as exact.

**FCF-positive 3+ consecutive years:** not independently re-verified year-by-year this session (only the FY2025 segment figure and the TTM figure were sourced). CAT is broadly known to have been FCF-positive for a long, uninterrupted stretch of years; this is treated as passing the hard-disqualifier check on that basis, but is flagged as an assumption rather than a session-verified 3-year table — **worth tightening in a future session** if a dedicated data pipeline (e.g. `yfinance`, per valuation-scoring.md's documented method) is wired up for CAT specifically.

### 2.5 Growth narrative / TAM evidence (documented, cited — feeds the Growth sub-score modifier)

- **Backlog:** grew 92% YoY to **$72.1B** as of Q2 2026 (booked $9.4B of new orders in the quarter) — [CNBC, 2026-08-04](https://www.cnbc.com/2026/08/04/caterpillar-cat-q2-2026-earnings.html); engine backlog specifically "increased more than 3.5x since early 2024, with customer orders extending into 2028" — [Motley Fool, 2026-09-07](https://www.fool.com/investing/2026/09/07/caterpillars-power-generation-backlog-just-hit-72/).
- **AI data-center demand:** "sales of large generator sets and turbines used by data centers grew 72%" in Q2 2026; Power Generation segment demand explicitly tied to "increasing energy demand to support data center build-out related to cloud computing and generative AI" — [Manufacturing Dive](https://www.manufacturingdive.com/news/caterpillar-sales-surpass-20b-growing-data-center-demand-q2-2026/827068/), [CNBC](https://www.cnbc.com/2026/08/04/caterpillar-cat-q2-2026-earnings.html).
- **Forward guidance (not scored, per "Why Forward Guidance Is Not a Sub-score" in valuation-scoring.md, but relevant context):** management raised FY2026 revenue growth guidance to "mid- to high-teens," citing growth across Construction Industries, Power & Energy, and Resource Industries — CNBC (per above).

This is genuine, multi-source-corroborated, non-guidance evidence (backlog dollars and order-book composition are filed/reported facts, not a forecast) of TAM expansion in the Power Generation segment specifically — credited as the **+10 documented-TAM-expansion modifier** to the Growth sub-score (§3.2).

### 2.6 Moat signal evidence (cited, per signal — quality-scoring.md requires a citation for every signal marked TRUE)

- **Market share stable/growing — TRUE.** "Caterpillar holds nearly 17% global market share, while Komatsu holds approximately 11.2 percent of the global construction and mining equipment market, second only to Caterpillar" — cited via [marketsandmarkets.com](https://www.marketsandmarkets.com/ResearchInsight/construction-mining-equipment-market.asp) and corroborating secondary sources found via web search. CAT is the clear #1 by unit share.
- **Switching costs — TRUE.** "Caterpillar operates through 500+ independent dealers in 190+ countries," with a "160+ dealer network — independently owned, deeply capitalized, multi-generational businesses that maintain parts inventories, service bays, and customer relationships spanning up to a century in their territories" — [rijnberkinvestinsights.substack.com deep dive](https://rijnberkinvestinsights.substack.com/p/caterpillar-a-global-industrial-with), corroborated by general industry coverage. Fleet commonality, parts/service lock-in, and multi-generational dealer relationships are a genuine, documented switching-cost mechanism.
- **Brand premium — not credited.** Caterpillar is a well-known global industrial brand, but no explicit pricing-power evidence (price increases sustained without volume loss, or a documented price premium vs. named competitors) was located this session — the qualitative "iconic brand" framing found in search results doesn't meet the framework's evidentiary bar (quality-scoring.md requires "pricing power evidence," not brand recognition alone).
- **Network effect — not credited.** No two-sided marketplace or user-growth-driven value-creation mechanism applies to a heavy-equipment manufacturer/dealer model — correctly false, not a data gap.
- **Scale cost advantage — not credited.** CAT is unambiguously the largest-scale player in its industry, but no cost-per-unit data quantifying a gap vs. smaller competitors (the framework's specific evidentiary requirement for this signal) was located this session.

**Moat_Score = 2 of 5 signals credited = 40.0.** Two additional signals (brand premium, scale cost advantage) are plausible on general industry knowledge but are deliberately **not** credited without the specific citation the framework requires — consistent with "never mark a signal true without a cited source."

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF positive 3+ consecutive years | TTM FCF $8.994B positive; FY2025 MP&E FCF $9.5B positive; longer multi-year record not independently re-verified this session (§2.4 flag) | disqualify if not 3 consecutive positive years | **✅ PASSES** (on best-available evidence — flagged as an assumption, not exhaustively re-verified) |
| Net Debt/EBITDA over threshold (2.5× standard — CAT is not Upgrade 5 asset-light-eligible) | 2.4x (FY2025) / 2.13x (TTM) | disqualify if exceeds 2.5× | **✅ PASSES** — under threshold on both cited figures |
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | TTM ≈ 95.4% (§2.4 — approximate, mismatched windows) | disqualify if 2+ consecutive years <70% w/o carve-out | **✅ PASSES** — well clear of the 70% line even allowing for the window-mismatch imprecision |

**No hard disqualifier fires.** Proceed to the weighted Quality Score.

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  NetMargin_Component = clamp((14.29/30)×100, 0, 100) = 47.63
  ROIC_Component       = clamp((18.30/30)×100, 0, 100) = 61.00
  Profitability_Score  = (47.63 + 61.00) / 2 = 54.32
  FCF-positivity cap check: passes (§3.1) — no cap applied.
  Profitability_Score = 54.3

MARGINS (15% weight):
  GrossMargin_Score = clamp((29.71/80)×100, 0, 100) = 37.14
  Structural trend bonus: NOT applied — no evidence of structurally expanding gross margin;
    if anything, operating margin *compressed* 3.7pp (20.2% → 16.5%) in FY2025 (§2.1).
  Margins_Score = 37.1

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022 $59.427B → FY2025 $67.589B) = (67.589/59.427)^(1/3) − 1 = 4.38%
  Growth_Score (raw) = clamp((4.38/25)×100, 0, 100) = 17.52
  TAM/pricing-power modifier: +10 (documented AI-data-center-driven Power Generation demand;
    backlog +92% YoY to $72.1B; FY2026 guidance raised to mid-/high-teens revenue growth — §2.5,
    all cited, non-guidance evidence where noted)
  Growth_Score = 17.5 + 10 = 27.5

BALANCE SHEET (15% weight):
  Net Debt/EBITDA = 2.4x (FY2025, consolidated per conglomerate rule — §2.3)
  BalanceSheet_Score = clamp(100 × (1 − 2.4/4), 0, 100) = 40.0

MOAT SIGNAL (15% weight):
  2 of 5 signals credited with citation (market share, switching costs — §2.6)
  Moat_Score = (2/5) × 100 = 40.0

FCF QUALITY (10% weight):
  FCF/NI ≈ 95.4% (§2.4, window-mismatch caveat)
  FCFQuality_Score = clamp(((0.954 − 0.40)/0.60) × 100, 0, 100) = clamp(92.33, 0, 100) = 92.3

QUALITY SCORE = 54.3×0.25 + 37.1×0.15 + 27.5×0.20 + 40.0×0.15 + 40.0×0.15 + 92.3×0.10
             = 13.575 + 5.565 + 5.500 + 6.000 + 6.000 + 9.230
             = 45.870 → rounds to 45.9
```

**Quality Score = 45.9 / 100.0 — fails the 80.0+ gate by a wide margin (34.1 points).** No hard disqualifier independently fires; this is purely a weighted-score failure, driven mainly by **Growth** (a cyclical industrial with a historically low 3yr revenue CAGR, even after crediting the AI-power-demand TAM modifier) and **Margins** (29.7% gross margin is well below this framework's high-margin-compounder baseline of 40%+, which the sub-score formula is calibrated around). Profitability, Balance Sheet, Moat, and FCF Quality are all middling-to-decent for an industrial, but none is strong enough to offset the growth/margin shortfall — and the framework's 80.0+ bar is deliberately strict by design (quality-scoring.md).

**Gate result: FAIL.** Per quality-scoring.md, operating-brief.md, and this session's explicit instructions: **do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or any order setup.**

---

## 4. Phase 02 / Order Setup — NOT PRODUCED

No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup is computed this session. The Quality Score gate is a strict, non-negotiable prerequisite (quality-scoring.md), and CAT does not clear it (45.9 vs. 80.0 required).

---

## 5. Data Gaps Flagged

1. **FCF/NI ratio uses mismatched trailing windows** (FCF thru Jun-2026, net income thru Mar-2026) — best available via web search this session; doesn't affect the pass/fail outcome given the wide margin above the 70% threshold, but should be tightened with a same-window pull if CAT is re-evaluated.
2. **"FCF positive 3+ consecutive years" not exhaustively re-verified year-by-year** — only FY2025 segment FCF and TTM company-wide FCF were directly sourced; treated as passing on the strength of CAT's well-documented long FCF-positive history, but flagged as an assumption rather than a session-verified table.
3. **No dedicated `yfinance`/SEC-XBRL pipeline was run for CAT this session** (unlike some other tickers in this repo's session history) — every fundamental figure above comes from a web search against a named source (stockanalysis.com, macrotrends.net, gurufocus.com, company earnings releases, SEC 10-K filings), cross-checked against a second source where one was found, but not pulled from a single authoritative dataset. Given the Quality Score fails by a 34-point margin, this doesn't change the outcome, but a tighter pipeline would sharpen the exact score if CAT is ever re-evaluated near the 80.0 line (it currently is not close).
4. **Brand premium and scale cost advantage moat signals** are plausible on general industry knowledge (CAT is a well-known premium industrial brand and the largest-scale player in its industry) but were not credited without the framework's specific required evidence (pricing-power data, cost-per-unit data) — see §2.6.

---

## 6. Qualitative Notes

1. **CAT is currently in an unusual growth inflection, but the framework's backward-looking 3yr-CAGR metric doesn't fully capture it yet.** Revenue was essentially flat FY2023→FY2024 (in fact declined) before recovering in FY2025, and only in the most recent 1-2 quarters has the AI-data-center-driven Power Generation demand surge shown up in the numbers (TTM revenue $74.7B vs. FY2025's $67.6B, backlog +92% YoY). The framework's trailing 3yr CAGR (4.4%) is a fair, honest reading of the historical record — the TAM-expansion modifier credits the forward-looking story without letting a single hot quarter override the trailing metric, exactly as the framework's growth sub-score is designed to do.
2. **This is a structurally different business from the high-margin compounders this framework's Quality Score formula is implicitly calibrated around** (its worked example and most prior /new-position sessions skew toward software/platform names). A 29.7% gross margin and mid-single-digit trailing revenue growth are unremarkable-to-good for a capital-intensive industrial equipment maker, but they read as weak against this framework's 40%/quality-gate lens — that's the gate doing its job (a deliberately strict, sector-agnostic bar, per quality-scoring.md), not a data error.
3. **Nothing here is a fundamental red flag.** CAT is profitable, moderately leveraged (under the 2.5x threshold), moat-protected (dealer network, market-share leadership), and has a genuinely exciting new demand driver (AI power generation). It simply doesn't clear this framework's strict quality bar today, primarily on growth-history and margin-level grounds — a name to revisit if the current growth acceleration persists long enough to move the trailing 3yr CAGR meaningfully, or if margins expand.

---

## Recommendation

# **PASS — Quality Score gate FAILS (45.9, well below the 80.0+ threshold). Do not proceed to valuation scoring. No position. Watchlist-only pointer created for future re-evaluation, not a scored entry.**

CAT is a profitable, reasonably-levered, moat-protected industrial with a real and well-documented new growth driver (AI-data-center power generation demand, backlog +92% YoY). But it fails this framework's strict Phase 01 Quality Score gate by a wide margin — 45.9 vs. the required 80.0 — mainly on trailing revenue growth (4.4% 3yr CAGR, even after the TAM-expansion credit) and gross margin (29.7%, well under this framework's 40% high-margin baseline). **This does not count as a BUY, TRIM, or EXIT trigger**, and no fair-value/order-setup work is produced.

---

## 7. Next Review Trigger

- **CAT's Q3 2026 earnings release** (expected ~October 2026) — the next data point on whether the AI-power-generation growth acceleration is sustaining, which would move the trailing 3yr revenue CAGR meaningfully by the time of a FY2026 annual re-score.
- **Standard Rule 9 triggers:** guidance revision, a material new Power Generation/data-center contract or backlog disclosure, management change, macro/rate shift, or a >15% *unexplained* price move.
- **If growth CAGR and/or gross margin move enough to plausibly approach the 80.0 gate**, a fresh `/new-position` run with a tighter same-window data pull (§5) is warranted before any entry decision.

---

## 8. Watchlist & Stale-Score Housekeeping

- **New watchlist entry created:** [watchlist/not-in-portfolio/CAT/CAT-2026-09-10.md](../watchlist/not-in-portfolio/CAT/CAT-2026-09-10.md) — first entry for this ticker.
- **Stale-score mechanism:** not applicable — CAT is Phase 01 FAIL / not scored under Phase 02, and per watchlist/README.md, "Entries that are 'Phase 01 FAIL / not scored' are not marked" for staleness.

---

## 9. Glossary

- **10-K**: a US company's annual audited financial-disclosure report filed with the SEC.
- **Backlog**: the dollar value of signed customer orders not yet recognized as revenue — a forward demand-visibility signal for equipment makers with long order-to-delivery cycles; CAT's backlog grew 92% YoY to $72.1B (§2.5).
- **Composite Score**: this framework's blended 0.0–100.0 ranking (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`) — not computed this session, since CAT never clears the Quality Score gate required to reach it.
- **EV/EBIT, EV/EBITDA**: Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.
- **FCF (Free Cash Flow) / FCF Yield / FCF/NI conversion ratio**: cash generated after capital expenditure; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check) — central to §2.4 and §3.1.
- **Hard disqualifier**: one of three Quality Score conditions that fails a company regardless of its weighted sub-score total — none fired for CAT this session (§3.1).
- **Moat**: a durable competitive advantage protecting a business's profits from competitors — scored 40.0 (2 of 5 signals: market share, switching costs) for CAT (§2.6, §3.2).
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate — CAT's is 2.4x (FY2025), under the 2.5x standard threshold (§2.3).
- **Net Margin**: Net Income ÷ Revenue — CAT's TTM figure is 14.3% (§2.1).
- **Quality Score**: this framework's 0–100.0 graded Phase 01 score; a company must score 80.0+ to proceed to valuation scoring — CAT scored 45.9 and fails the gate (§3.2).
- **Qualified Quality List**: the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. CAT is not on it.
- **Revenue 3yr CAGR**: Compound Annual Growth Rate of revenue over the most recently completed 3 fiscal years — CAT's is 4.38% (§2.2, §3.2).
- **ROIC**: Return on Invested Capital — CAT's TTM figure is 18.3% (§2.1).
- **TTM (Trailing Twelve Months)**: the most recent 12 months of reported financial results.

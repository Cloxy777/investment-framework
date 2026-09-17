# NEW POSITION — AI.PA (L'Air Liquide S.A.)

**Date:** 2026-09-17
**Task type:** NEW POSITION
**Sector:** Basic Materials — Specialty Chemicals (industrial gas), Euronext Paris, EUR-denominated
**10Y US Treasury yield (context only — Rate Environment Gate not run, see below):** ~5.02% (US10Y closed 5.016% 2026-09-16, per [CNBC](https://www.cnbc.com/2026/09/16/treasury-yield-bond-market-fed-decision.html) and [TradingEconomics](https://tradingeconomics.com/united-states/government-bond-yield)) — would map to the >5% → **+10** Rate Regime Modifier bucket, but this is not applied because the session stops at the Quality Gate (see below).
**Sourced from:** ad-hoc candidate evaluation (not an existing holding)

**Duplicate-entity check:** [portfolio/holdings.md](../portfolio/holdings.md) was checked in full before starting. **No match found** for Air Liquide under AI.PA, AIQUY (its US OTC ADR), or any other listing. Genuinely new candidate.

---

## 1. Live Price (Rule 0)

Fetched via `yfinance` (`yf.Ticker("AI.PA").fast_info` / `.history()`), not inferred from multiples:

| Field | Value |
|---|---|
| **Live price (2026-09-17 close, Euronext Paris)** | **€165.24** |
| Previous close (2026-09-16) | €166.42 (`.info`) / fast_info previous_close €166.62 |
| 52-week range | €140.78 – €182.26 (price sits roughly in the lower half of its 52-week range, ~10% above the 52-week low) |
| Market cap | €105.45B |
| Enterprise value | €121.86B |

**Recent price context (not a scored input, informational only):** the stock has drifted down from €173.16 (2026-09-08) to €165.24 (2026-09-17), roughly a −4.6% move over 7 trading sessions — well under the 15% Rule 9 unexplained-move threshold, so this alone triggers nothing. Web search turned up no company-specific news explaining the drift; likely broad market/rate-driven (10Y Treasury pushed through 5% this week — see header).

**Analyst consensus (bull-case sanity check, per Rule 0 Step 4, not a scored input):** average analyst price target ≈ €197.72 (20-analyst consensus, "Strong Buy" — 18 buy / 2 hold / 0 sell), implying ~17.5% upside from a recent ~€168 close ([ad-hoc-news.de](https://www.ad-hoc-news.de/boerse/news/corporate-news/air-liquide-stock-holds-firm-as-latest-consensus-supports-upside/69959155)). Noted for context only — the framework never scores off guidance or sell-side targets directly.

---

## 2. Phase 01 — Quality Score (full sub-score arithmetic)

All figures from `yfinance` (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet`). Fiscal year ends 31 December; most recently completed FY = **FY2025**. No metric was estimated or invented; every figure below traces to a specific `yfinance` field, cross-checked against Air Liquide's own FY2025 results release where noted.

### Hard disqualifier checks (run first)

| Disqualifier | Result | Fires? |
|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years w/o documented growth-capex explanation | FY2022 92.0%, FY2023 93.2%, FY2024 84.6%, FY2025 76.0% — all comfortably above 70% | **No** |
| Net Debt/EBITDA over its applicable threshold (2.5× standard — Air Liquide is an industrial-gas manufacturer, not a payment network/exchange/asset-light financial, so no Upgrade 5 override) | FY2025 year-end: Net Debt €8,704.5M / EBITDA €7,528.7M = **1.16×** — well under 2.5× | **No** |
| Not FCF-positive for 3+ consecutive years | FCF positive every year FY2022–FY2025 (€2,537.1M, €2,869.6M, €2,797.1M, €2,675.0M) | **No** |

**No hard disqualifier fires.** (Note: `t.info["freeCashflow"]` returned a clearly stale/mismatched single-quarter figure of ~€243M — not used; the annual `t.cashflow.loc["Free Cash Flow"]` series above is the Rule-0-compliant filed-financials figure and is what's used throughout this session.)

### Sub-score 1 — Profitability (25% weight)

```
Net Margin (FY2025) = Net Income 3,517.9 / Revenue 26,940.2 = 13.06%
ROIC = NOPAT ÷ Invested Capital
     EBIT (FY2025) = €4,965.2M
     Effective tax rate (FY2025, t.financials "Tax Rate For Calcs") = 25.2%
     NOPAT = 4,965.2 × (1 − 0.252) = €3,714.6M
     Invested Capital (FY2025, t.balance_sheet) = €38,550.4M
     ROIC = 3,714.6 / 38,550.4 = 9.64%

NetMargin_Component = clamp((13.06/30)×100, 0, 100) = 43.53
ROIC_Component       = clamp((9.64/30)×100, 0, 100)  = 32.13
Profitability_Score  = (43.53 + 32.13) / 2 = 37.83
```
No FCF-positive-3yr cap applies (FCF positive every year FY2022–FY2025).

*Reference (average-invested-capital basis, FY2024–FY2025 average €38,215.2M): ROIC = 9.72% → ROIC_Component 32.40 → Profitability_Score 37.97. Either basis moves the final score by <0.1 — immaterial to the gate outcome.*

### Sub-score 2 — Margins (15% weight)

```
Gross Margin (FY2025) = Gross Profit 17,289.0 / Revenue 26,940.2 = 64.16%
GrossMargin_Score = clamp((64.16/80)×100, 0, 100) = 80.20
```
4-year annual trend (`t.financials`, FY2022→FY2025): 53.9% → 59.6% → 63.0% → 64.2% — genuinely expanding. But the +10 structural-trend bonus in [quality-scoring.md](../framework/quality-scoring.md) only applies to a margin still **below the 40% static threshold** while trending up; Air Liquide is already well above 40%, so **no bonus applies** (per the rule as written).

### Sub-score 3 — Growth (20% weight)

```
Revenue 3yr CAGR = (Revenue FY2025 / Revenue FY2022)^(1/3) − 1
                 = (€26,940.2M / €29,934.0M)^(1/3) − 1 = −3.45%
Growth_Score (raw) = clamp((−3.45/25)×100, 0, 100) = 0.00
```

**Data-quality flag:** Air Liquide's *reported* IFRS revenue fell from FY2022 to FY2025 almost entirely because of energy-cost **pass-through** effects — FY2022 revenue was inflated by an extraordinary surge in natural-gas/electricity costs that Air Liquide passes straight through to Industrial Merchant customers (contractually, at no margin impact), and that pass-through component has since receded as energy prices normalized. This mechanically depresses the reported top-line CAGR relative to the business's actual (comparable) growth — flagged explicitly rather than silently accepted, per "never invent or estimate financial data": the raw yfinance-sourced CAGR above is what's used for the base sub-score, since substituting a different revenue base would require inventing a number not directly in the filed financials pulled this session.

**TAM-expansion / pricing-power evidence (documented, cited via web search this session):**
- Air Liquide's own FY2025 results confirm **comparable (like-for-like, ex-FX/ex-energy) revenue growth of +2%** for the full year, with +1.7% in Q1 2025 and +1.9% in Q3 2025 ([Air Liquide FY2025 press release](https://www.airliquide.com/group/press-releases-news/2026-02-20/2025-record-performance-and-confident-its-transformation-dynamic-air-liquide-confirms-its-growth)).
- Industrial Merchant revenue benefited from a **+4.5% price effect** in 2025, described by the company as reflecting "its ability to create value for customers" — direct, company-disclosed pricing-power evidence ([Air Liquide FY2025 results](https://www.airliquide.com/group/press-releases-news/2026-02-20/2025-record-performance-and-confident-its-transformation-dynamic-air-liquide-confirms-its-growth)).
- Electronics is cited as the group's fastest-rising growth engine, alongside continued expansion in Healthcare/Home Healthcare (16% of Gas & Services revenue) — documented TAM-expansion context ([thierryvonarvy.substack.com](https://thierryvonarvy.substack.com/p/linde-and-air-liquide-the-tandem)).

**+10 applied** for this documented comparable-growth and pricing-power evidence (real revenue growth exists once the energy-pass-through distortion is accounted for, even though the raw reported-revenue CAGR used for the base sub-score is negative).

```
Growth_Score = 0.00 + 10 = 10.00
```

### Sub-score 4 — Balance Sheet (15% weight)

```
Net Debt (FY2025, t.balance_sheet)  = €8,704.5M
EBITDA (FY2025, t.financials)        = €7,528.7M
Net Debt/EBITDA = 8,704.5 / 7,528.7 = 1.156×
```
Air Liquide is not a payment network/exchange/asset-light financial — standard /4 denominator applies (no Upgrade 5 override).
```
BalanceSheet_Score = clamp(100×(1 − 1.156/4), 0, 100) = 71.10
```

### Sub-score 5 — Moat Signal (15% weight)

Checklist scored only against cited evidence (task brief's own reminder — industrial gas has real, structural moats — taken seriously and evidenced below rather than dismissed as a plain regulated utility):

| Signal | True/False | Evidence |
|---|---|---|
| Market share stable or growing | **True** | Air Liquide is the clear #1 global industrial-gas player by revenue, roughly ~$28B vs. #2 Air Products' ~$12B — "larger, more diversified across geographies and end markets... a steadier performer" ([thierryvonarvy.substack.com](https://thierryvonarvy.substack.com/p/linde-and-air-liquide-the-tandem)). |
| Brand premium / pricing power | **True** | Company-disclosed +4.5% price effect in Industrial Merchant FY2025, explicitly attributed to "its ability to create value for customers" — direct price-increase-without-disclosed-volume-loss evidence ([Air Liquide FY2025 results](https://www.airliquide.com/group/press-releases-news/2026-02-20/2025-record-performance-and-confident-its-transformation-dynamic-air-liquide-confirms-its-growth)). |
| Network effect | **False** | Industrial gas is not a two-sided marketplace / user-growth-driven-value business — no documented network-effect mechanism found. Pipeline density is a scale/switching-cost dynamic (credited below), not a network effect as this checklist defines the term. |
| Switching costs | **True** | On-site plants built and dedicated to a single customer, combined with long-term (typically 15–20yr) take-or-pay supply contracts, plus dense regional pipeline-network integration — documented, structural switching-cost mechanism cited generically for the industrial-gas business model ([thierryvonarvy.substack.com](https://thierryvonarvy.substack.com/p/linde-and-air-liquide-the-tandem); consistent with the task brief's own framing of on-site plants and take-or-pay contracts as real moat mechanisms). |
| Scale cost advantage | **True** | "High capital costs, safety expertise, and dense pipeline networks make it very hard for new entrants to compete, giving Air Liquide a durable moat" ([thierryvonarvy.substack.com](https://thierryvonarvy.substack.com/p/linde-and-air-liquide-the-tandem)) — Air Liquide's ~2.3× revenue scale over its nearest global peer (Air Products) is documented entry-barrier/cost-per-unit-advantage evidence, though no specific third-party cost-per-unit figure vs. a named competitor was found this session. |

```
Moat_Score = (4/5) × 100 = 80.0
```

### Sub-score 6 — FCF Quality (10% weight)

```
FCF/NI ratio (FY2025) = FCF 2,675.0 / NI 3,517.9 = 76.0%
FCFQuality_Score = clamp(((0.760 − 0.40)/0.60)×100, 0, 100) = clamp(60.0, 0, 100) = 60.00
```

### Final Quality Score

```
Quality Score = (37.83×0.25) + (80.20×0.15) + (10.00×0.20) + (71.10×0.15) + (80.0×0.15) + (60.00×0.10)
             = 9.4575 + 12.030 + 2.000 + 10.665 + 12.000 + 6.000
             = 52.1525 → rounds to 52.2
```

**Quality Score: 52.2 / 100.0 — fails the 80.0+ gate.**

*(Reference: using the average-invested-capital ROIC basis instead of year-end (Profitability_Score 37.97 vs. 37.83), the score would be 52.2 as well after rounding — the choice of basis does not change the outcome.)*

---

## STOP — Gate Failure, No Phase 02 Scoring Performed

Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md), a Quality Score below 80.0 halts the process here — **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, no fair-value/order-setup work was performed**, regardless of how the stock's headline multiples look (forward PE 23.1×, PEG 2.08, dividend yield ~2.0% — irrelevant, since the gate is checked first).

**No hard disqualifier fired** — the gate failure is driven entirely by the weighted score, primarily:
- **Growth (10.0)** — the largest drag. Reported revenue actually *declined* (−3.45% 3yr CAGR) due to energy-cost pass-through normalization, and even after crediting +10 for documented comparable-basis growth (+2% FY2025) and pricing power (+4.5% price effect), the sub-score is still capped near the floor. A structurally capital-intensive, low-single-digit organic grower does not clear this sub-score's bar the way a Fast Grower would.
- **Profitability (37.83)** — Air Liquide's ROIC (~9.6%) is modest by this framework's scale (30% = max score), a direct consequence of the industrial-gas business model's heavy fixed-asset base (on-site plants, pipeline networks) — the same assets that generate the Moat_Score credit are also what caps Profitability here.
- **Balance Sheet (71.10)** is solid (1.16× Net Debt/EBITDA, comfortably investment-grade territory), and **Moat (80.0)** and **Margins (80.20)** are both genuinely strong — the task brief's framing of industrial gas as a real-moat business is borne out by the evidence gathered, but it isn't enough to offset the low Growth and Profitability sub-scores under this framework's specific weights.
- **FCF Quality (60.00)** is mid-range — FY2025's 76.0% conversion ratio is comfortably above the 70% hard-disqualifier line but below the framework's 85%+ "strong" range, consistent with a capital-intensive business reinvesting heavily (CapEx ran €3.84B in FY2025 against €6.52B of operating cash flow).

**Recommendation: PASS.** Do not open a position. Add to watchlist (not-in-portfolio) for future re-evaluation.

## Next review trigger

No routine re-check scheduled (Phase 01 FAIL, no numeric Phase 02 score to go stale). Re-evaluate on any of:
- **FY2026 full-year results** (next full-year report, expected ~February 2027) — refreshes the Growth sub-score with a new 3yr CAGR window as the FY2022 energy-price-spike year rolls out of the trailing window, which should materially help the reported-revenue-CAGR distortion identified this session.
- Third-party cost-per-unit or market-share data becoming available that could move the Scale/Market-share Moat signals from "documented but generic" to a harder-cited figure.
- Any Rule 9 fundamental trigger (earnings, guidance revision, M&A, management change, macro shift, >15% unexplained price move).

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx (Capital Expenditure)** | Cash spent on long-lived physical assets (plants, equipment, pipelines) — subtracted from operating cash flow to arrive at Free Cash Flow. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. A low ratio without a CapEx explanation is a red flag for earnings-quality games. |
| **Forward PE** | Price ÷ next-twelve-months expected earnings per share — a valuation multiple based on projected, not trailing, earnings. |
| **Gross Margin** | Gross Profit (Revenue − Cost of Revenue) ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation. |
| **IFRS** | International Financial Reporting Standards — the accounting framework used by Air Liquide (a French/EU-listed company) to prepare its financial statements, distinct from US GAAP. |
| **Industrial Merchant** | Air Liquide's business line supplying packaged/bulk industrial gases to a broad range of customers, distinct from the "Large Industries" (on-site plants for major customers) and "Healthcare" business lines. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) put to work in a business — the denominator in a Return on Invested Capital (ROIC) calculation. |
| **Moat** | Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. |
| **Moat Signal** | This framework's 5-point Quality Score checklist that turns the general "Moat" concept into a scored input, each markable TRUE only against a cited source. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt. |
| **Net Margin** | Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Pass-through (cost pass-through)** | A contractual arrangement where a supplier's rising input cost (e.g. the natural gas/electricity Air Liquide consumes to produce industrial gases) is billed straight through to the customer at no margin impact — inflates and deflates reported revenue with input-cost swings without reflecting the underlying business's real growth or profitability. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — a PE adjusted for growth, used to judge whether a fast grower's multiple is justified by its growth rate; not applicable to Air Liquide (session stopped at the Quality Gate before Phase 02 in any case). |
| **Quality Score** | This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. AI.PA scores 52.2. |
| **Rate Environment Gate / Rate Regime Modifier** | A mandatory pre-check run before every Phase 02 valuation score, adjusting the score for the level of the 10Y US Treasury yield. Not run this session because the Quality Gate failed first. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **Take-or-pay** | A supply-contract structure where the buyer must pay for a committed volume of product whether or not it actually takes delivery — shifts demand risk from the seller to the buyer and gives the seller unusually high revenue/margin visibility; a structural switching-cost mechanism common in on-site industrial-gas supply agreements. |
| **TAM** | Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market. |

**Sources (web search, this session):**
- [Air Liquide 2025 results: record performance, confirmed growth outlook — Air Liquide media release](https://www.airliquide.com/group/press-releases-news/2026-02-20/2025-record-performance-and-confident-its-transformation-dynamic-air-liquide-confirms-its-growth)
- [Linde & Air Liquide: The Tandem That Owns the Air — Thierry von Arvy (Substack)](https://thierryvonarvy.substack.com/p/linde-and-air-liquide-the-tandem)
- [Air Liquide stock holds firm as latest consensus supports upside — ad-hoc-news.de](https://www.ad-hoc-news.de/boerse/news/corporate-news/air-liquide-stock-holds-firm-as-latest-consensus-supports-upside/69959155)
- [US 10 Year Treasury Note Yield — TradingEconomics](https://tradingeconomics.com/united-states/government-bond-yield)
- [10-year Treasury yield climbs back to 5% after Fed hikes rates — CNBC](https://www.cnbc.com/2026/09/16/treasury-yield-bond-market-fed-decision.html)

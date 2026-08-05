# New Position Evaluation — SHOP (Shopify Inc.)

**Task type:** NEW POSITION
**Date:** 2026-08-05
**10Y US Treasury Yield:** 4.61% (reused from same-day [sessions/2026-08-05-new-position-bkng.md](2026-08-05-new-position-bkng.md) per CLAUDE.md — "check the most recent RESCORE/rebalance session in `sessions/` for the currently active Rate Regime Modifier... do not refetch FRED yourself unless you can't find a recent one." No newer session exists.)
**Rate Regime Modifier (active):** +5 (3.5–5% bracket)

---

## 0. Trigger

Automated Telegram-scan (Routine 6): two independent channels posted about Shopify's Q2 2026 earnings on 2026-08-05 —
- [t.me/tarasguk](https://t.me/tarasguk), post `tarasguk/11605` (~12:14 UTC): revenue $3.58B (vs $3.45B est), GMV $115.6B, operating profit +68% YoY, Q3 guidance "low 30% range" revenue growth.
- [t.me/FinnInvestChannel](https://t.me/FinnInvestChannel), post `FinnInvestChannel/3047` (~12:01 UTC): revenue $3.58B (vs $3.45B est) +34% YoY, operating income $488M +68% YoY, broad-based seller growth across channels/regions.

No prior watchlist entry exists for SHOP (`watchlist/not-in-portfolio/SHOP/` and `watchlist/in-portfolio/SHOP/` both empty) and it is not a current holding. Per CLAUDE.md, none of the Telegram figures were treated as verified data — they were only a trigger to look at the ticker. Every figure below is independently sourced from SEC filings. As it happens, all claimed figures check out against the primary source (Shopify's own SEC-filed Q2 2026 earnings press release, 8-K Exhibit 99.1, filed 2026-08-05):

- Revenue **$3.58B** ✓ matches ($3,583M reported)
- Revenue growth **+34% YoY** ✓ exact match (press release: "Shopify achieved 34% revenue growth (33% in constant currency)"; independently recomputed: (3,583−2,680)/2,680 = +33.7% ≈ 34%)
- GMV **$115.6B** ✓ matches ($115,567M reported)
- Operating income **$488M, +68% YoY** ✓ matches (488 vs 291 prior year; independently recomputed: (488−291)/291 = +67.7% ≈ +68%)
- Q3 2026 guidance "low 30% range" ✓ exact match (press release: "Revenue to grow at a low-thirties percentage rate on a year-over-year basis")
- "Broad-based... growth across channels/regions" ✓ reasonably matches CFO Jeff Hoffmeister's quote: "solid results across all merchant sizes, channels, and geographies"

This is disclosed for completeness, not as a substitute for independent verification — every number used in scoring below is separately sourced and cited.

---

## 1. Live price (Rule 0)

**$150.72** — IBKR `get_price_snapshot`, contract_id 195014116 (NASDAQ, "SHOPIFY INC - CLASS A"), `ts` 1785932707 → **2026-08-05 12:25:07 UTC** (08:25 ET — **pre-market**, `is_close: false`, intraday/live). Bid/ask $150.51 / $150.90. Prior close $123.30 (**+22.24%** pre-market, the post-earnings pop). 52-week range (IBKR `misc_statistics`): low $94.00 / high $182.19; 13-week high $133.99, 26-week high $139.10 — today's pre-market print already sits above both the 13- and 26-week highs, well below the 52-week high.

This is a legitimate live Rule-0 price — pre-market prints are thinner than regular-session volume but are genuine live trades, not stale/inferred figures (same treatment as the after-hours COIN precedent, 2026-07-31 session). No cross-check source was fetched separately since IBKR's own `prior-close` field ($123.30) is internally consistent with the reported +22.24%/+27.42 point change, and the SEC 8-K/press release (filed same morning) corroborates the scale of the earnings beat driving the move.

---

## 2. Data sourcing

No `yfinance` Python module was installed in this environment; installed it (`pip install yfinance lxml`) and confirmed its own HTTP client is blocked by this session's egress proxy (`curl_cffi.requests.exceptions.SSLError: ... Connection reset by peer` on the Yahoo cookie/crumb handshake) — consistent with the documented BKNG/MCD/CVX/IBM/CCL precedent. Data was sourced as follows, every figure cited:

1. **SEC EDGAR XBRL `companyfacts` API** (`https://data.sec.gov/api/xbrl/companyfacts/CIK0001594805.json`) — primary source for all income statement, balance sheet, and cash flow figures, cross-referenced against the raw 10-Q financial statements (`R2.htm`/`R4.htm`/`R6.htm` of accession 0001594805-26-000047, the 10-Q for the quarter ended 2026-06-30, filed 2026-08-05) and the Q2 2026 earnings press release (8-K Exhibit 99.1, `exhibit991pressreleaseq220.htm`, same filing date). Shopify Inc. (CIK 0001594805) files as a US domestic filer (10-K/10-Q, not a foreign-private-issuer 40-F), so full XBRL company-facts coverage is available.
2. **stockanalysis.com** (via WebFetch) — used for consensus forward EPS, ROIC cross-check, and general context; flagged wherever it used a stale (pre-earnings) price.
3. **WebSearch** — used for ROIC cross-checks (multiple independent providers), 5yr PE range cross-checks, beta, peer valuation multiples, and qualitative moat/growth/pricing-power evidence, each cited inline where used.

No required metric was unavailable from all sources; no figure below is invented or estimated. All dollar figures below are in USD millions unless stated otherwise.

---

## 3. Phase 01 — Quality Score (methodology version 2026-06-29)

### TTM reconstruction (Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026)

Shopify's GAAP results are **highly volatile quarter-to-quarter** because "Other income (expense), net" includes large **unrealized mark-to-market gains/losses on equity and other investments** (a strategic-investment portfolio, not the core commerce/payments business). This swung from a **$1,064M unrealized loss in Q1 2026** to a **$1,249M unrealized gain in Q2 2026** — the company itself flags this in its own press release with a non-GAAP reconciliation ("Net income excluding the impact of equity investments": $439M for Q2 2026 vs. GAAP net income of $1,502M for the same quarter). This framework scores off filed **GAAP** figures throughout (never a company's own non-GAAP adjustment), consistent with the "guidance/self-reported adjusted metrics are not scored" principle — but the resulting Net Income-based figures below (Net Margin, ROIC-via-NOPAT, FCF/NI) should be read with this volatility in mind. Quarterly figures (SEC XBRL, derived where needed as `FY − 9mo` or `9mo − 6mo`):

| | Revenue | Gross Profit | EBIT (Op. Income) | D&A | Net Income | OCF | CapEx |
|---|---|---|---|---|---|---|---|
| Q3 2025 | 2,844 | 1,391 | 343 | 8 | 264 | 513 | 6 |
| Q4 2025 (FY25 − 9mo25) | 3,672 | 1,693 | 631 | 7 | 743 | 725 | 10 |
| Q1 2026 | 3,170 | 1,546 | 382 | 7 | −581 | 481 | 5 |
| Q2 2026 | 3,583 | 1,708 | 488 | 7 | 1,502 | 658 | 4 |
| **TTM** | **13,269** | **6,338** | **1,844** | **29** | **1,928** | **2,377** | **25** |

- TTM EBITDA = EBIT (1,844) + D&A (29) = **1,873**
- TTM FCF = OCF (2,377) − CapEx (25) = **2,352** (cross-checked: matches Shopify's own disclosed Q2-2026-quarter FCF of $654M exactly — $658M OCF − $4M CapEx = $654M ✓, per the 8-K press release's "Free cash flow" line)

**Upgrade 1 (Owner Earnings) — not applicable.** TTM CapEx ($25M) is trivial (0.19% of revenue) — Shopify is an asset-light SaaS/commerce platform, not a hyperscaler; not on the MSFT/GOOGL/META/AMZN required list and no growth-capex/total-capex threshold issue.

### Profitability (25% weight)

- **Net Margin (TTM)** = 1,928 / 13,269 = **14.53%**
- **ROIC (TTM)** — **flagged judgment call** (same class of issue as BKNG's 2026-08-05 and FICO's 2026-07-07 precedent — a cash/investment-rich, debt-free balance sheet makes "Invested Capital" highly sensitive to what counts as cash):
  - **My own formula** (Invested Capital = Total Debt + Equity − Cash-and-equivalents-only): NOPAT = TTM EBIT (1,844) × (1 − effective tax rate). TTM tax expense = Q3'25 44 + Q4'25 (278−129=149) + Q1'26 (−53) + Q2'26 273 = 413; TTM pretax income = NI(1,928) + tax(413) = 2,341; effective rate = 413/2,341 = **17.64%**. NOPAT = 1,844 × (1−0.1764) = **1,518.7**. Invested Capital = $0 debt + $12,684M equity (2026-06-30) − $1,656M cash = **$11,028M**. ROIC = 1,518.7/11,028 = **13.77%**.
  - **Third-party cross-checks:** stockanalysis.com **20.45%** (TTM, as of 2026-08-04); GuruFocus **23.02%** (as of Mar 2026). Both third-party figures are materially higher than my own-formula result — consistent with those providers netting Shopify's much larger pool of liquid assets (cash $1,656M **+** current marketable securities $3,291M **+** long-term investments $525M = $5,472M total) against equity rather than cash-and-equivalents alone. Re-deriving my own formula with that broader netting (Invested Capital = $0 − $12,684M − $5,472M... i.e. $12,684M − $5,472M = $7,212M) gives ROIC = 1,518.7/7,212 = **21.06%**, closely corroborating the third-party figures.
  - **Used: 20.45%** — the median of the three independently-derived figures (13.77%, 20.45%, 23.02%), the same conservative-median approach used in the BKNG precedent rather than picking the highest.
- NetMargin_Component = clamp((14.53/30)×100) = **48.43**
- ROIC_Component = clamp((20.45/30)×100) = **68.17**
- No FCF-positivity cap (FCF positive every fiscal year FY2023–FY2025 and TTM — see FCF Quality below).
- **Profitability_Score = (48.43 + 68.17) / 2 = 58.30**

### Margins (15% weight)

- **Gross Margin (TTM)** = 6,338 / 13,269 = **47.77%**
- GrossMargin_Score = clamp((47.77/80)×100) = **59.71**
- No structural-trend bonus applicable — the +10 modifier only applies when gross margin sits *below* the 40% threshold; SHOP's is already above it.
- **Margins_Score = 59.71**

### Growth (20% weight)

- **Revenue 3yr CAGR** = (FY2025 Revenue ÷ FY2022 Revenue)^(1/3) − 1 = ($11,556M ÷ $5,600M)^(1/3) − 1 = **27.31%**
- Growth_Score base = clamp((27.31/25)×100) = **100.0 (capped)** — raw pre-clamp value 109.3, over the 25% ceiling.
- **+10 documented TAM-expansion modifier** (does not change the result — already at the 100.0 ceiling, cited for completeness/qualitative record): Shopify's own disclosed TAM is **$849B** (offline payments 54% / $459B, online payments 18% / $157B, merchant services 18% / $152B, subscription solutions 10% / $81B), projected by third-party analysis to reach **$1.96–2.80T by 2030**. Enterprise adoption (Shopify Plus) grew **+34% YoY to 47,000+ stores**; B2B commerce GMV grew **+96–101% YoY** (still a small share of total GMV but the fastest-growing segment) — [digitalapplied.com](https://www.digitalapplied.com/blog/shopify-statistics-2026-platform-growth-data), [stormy.ai](https://stormy.ai/blog/shopify-tam-expansion-strategy-2026).
- **No structural-deceleration modifier applies** — growth has been *accelerating*, not decelerating: FY2023 +26.1%, FY2024 +25.8%, FY2025 +30.1%, Q2 2026 +33.7% YoY, Q3 2026 guided "low-thirties%." The opposite of the deceleration condition the −10 modifier requires.
- **Growth_Score = 100.0**

### Balance Sheet (15% weight)

- **Total Debt = $0.** Shopify's only debt instrument, $918–920M of convertible notes (SEC XBRL `ConvertibleDebtCurrent`), sat on the balance sheet through Q3 2025 but reads **$0** at FY2025 year-end (2025-12-31) and has **no entries at all** in the 2026 XBRL data — fully retired. Confirmed independently: the 2026-06-30 balance sheet (`R2.htm`) carries no debt/borrowings line of any kind among its liabilities (only accounts payable/accrued liabilities, deferred revenue, and lease liabilities).
- **Cash and cash equivalents = $1,656M** (2026-06-30, SEC XBRL `CashAndCashEquivalentsAtCarryingValue`). (Shopify also holds $3,291M of current marketable securities and $525M of long-term investments not counted here — using only cash-and-equivalents is the more conservative, less-EV-reducing choice, consistent with the framework's convention in the BKNG session.)
- **Net Debt = $0 − $1,656M = −$1,656M (net cash)**
- **Net Debt/EBITDA = −1,656 / 1,873 = −0.884×** (net cash position, far below any threshold; asset-light override not needed)
- BalanceSheet_Score = clamp(100×(1 − (−0.884)/4)) = clamp(122.1) = **100.0 (capped)**

### Moat Signal (15% weight)

| Signal | Verdict | Evidence (cited) |
|---|---|---|
| Market share stable/growing | **TRUE** | Shopify holds **45.99%** of the ecommerce-platform market in a February 2026 crawl (2.6× the #2 platform), **28.8%** share among the top 1M highest-traffic ecommerce sites, and its detected-store count grew **+11.7% YoY** (May 2025→May 2026) vs. #2 WooCommerce's **−3.2%** decline over the same window — [gravitykit.com](https://www.gravitykit.com/ecommerce-platform-market-share-2026/). |
| Brand premium / pricing power | **TRUE** | In 2023 Shopify raised subscription prices **33–34%** across its Basic/Shopify/Advanced plans (its first increase in 12 years) — Basic $29→$39, Shopify $79→$105, Advanced $299→$399 — with contemporaneous analyst commentary of "very little churn" ([Subscription Insider](https://www.subscriptioninsider.com/topics/pricing/shopify-raises-2023-merchant-subscription-prices), [TipRanks](https://www.tipranks.com/news/the-fly/shopify-price-increases-positive-for-2023-outlook-says-citi)). Revenue growth did not merely hold up but **accelerated** in the following years (+25.8% FY2024, +30.1% FY2025, +33.7% Q2 2026 YoY) — a price increase absorbed without volume loss. |
| Network effect | **TRUE** | Shop Pay has **200M+ registered buyers** forming a cross-merchant buyer-recognition network — "Shopify recognizes them with one click" wherever Shop Pay is enabled — with ~48% of active Shopify stores having it enabled and 32% of all Shopify orders processed through it during BFCM 2025 ([shopify.com/enterprise/blog/shop-buyer-network](https://www.shopify.com/enterprise/blog/shop-buyer-network)). Separately, the Shopify App Store's two-sided developer/merchant marketplace has grown to **21,000+ apps** built by **12,000+ developers**, who were paid **$1.3B** by Shopify in the most recent year — a documented two-sided-marketplace mechanism, not just a scale claim ([shopify.com/news/billion-dollar-ecosystem](https://www.shopify.com/news/billion-dollar-ecosystem)). |
| Switching costs | **TRUE** | Documented migration friction and cost: DIY re-platforming runs $0–$500, agency-led migrations $5,000–$25,000+, and Shopify Plus enterprise migrations **$50,000+** (mid-market custom replatforms $150,000–$300,000); theme rebuild — not data migration — dominates the cost, and cart/upsell/cross-sell apps typically need full reinstall/reconfiguration on migration, plus recurring monthly platform-and-app-stack costs that compound the longer a merchant stays ([Optimum7](https://www.optimum7.com/blog/shopify-migration-and-re-platforming-guide.html), [Yotpo](https://www.yotpo.com/blog/shopify-migration-cost-data-seo/)). |
| Scale cost advantage | **TRUE** | Shopify's own commentary frames transaction-volume scale (**$292B+** annualized GMV) as funding infrastructure investment smaller competitors can't match — **$1.4B R&D spend in 2024** — translating into a published **33–45% better Total Cost of Ownership** vs. BigCommerce (whose own platform/stack costs run ~32% higher than Shopify's) ([Elogic Commerce](https://elogic.co/blog/shopify-plus-pricing-2026/), [commerce-ui.com](https://commerce-ui.com/insights/shopify-pricing)). |

**Moat_Score = (5/5) × 100 = 100.0**

### FCF Quality (10% weight)

- **TTM FCF/NI ratio** = 2,352 / 1,928 = **122.0%**
- FCFQuality_Score = clamp(((1.220 − 0.40)/0.60)×100) = **100.0 (capped)**
- Historical context (per-fiscal-year, for the hard-disqualifier check below): FY2023 FCF $905M / NI $132M = 685.6% (ratio distorted by a near-zero NI denominator, a low-earnings-base artifact rather than a quality problem); FY2024 FCF $1,597M / NI $2,019M = 79.1%; FY2025 FCF $2,007M / NI $1,231M = 163.0%. All comfortably above 70% in every measurable year.

### Hard disqualifiers — none fire

- FCF/NI conversion: 122.0% TTM, 79–163%+ in every individual fiscal year shown — no issue.
- Net Debt/EBITDA: −0.884× (net cash) — no issue.
- FCF-positive 3+ consecutive years: yes — FY2023 $905M, FY2024 $1,597M, FY2025 $2,007M, TTM $2,352M, all positive and growing (FY2022 was negative at −$186M, but that's outside the "most recent 3 years" window the disqualifier checks).

### Quality Score

```
Quality Score = 58.30×0.25 + 59.71×0.15 + 100.0×0.20 + 100.0×0.15 + 100.0×0.15 + 100.0×0.10
              = 14.575 + 8.9565 + 20.000 + 15.000 + 15.000 + 10.000
              = 83.53
```

**Quality Score = 83.5 / 100.0 — clears the 80.0+ gate.** Sensitivity check: even using the more conservative *own-formula* ROIC (13.77% instead of the 20.45% median used) would drop Profitability_Score to 47.17 and the final Quality Score to **80.75** — still above the gate. Proceed to Phase 02.

---

## 4. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** EY = 1 ÷ Forward PE = 1 ÷ 81.47 = **1.23%**. Spread = 1.23% − 4.61% (10Y) = **−3.38pp** — well below the +1.5pp threshold → **+5 additive modifier** (yellow flag, not a veto, per the 2026-06-07 rule change).
- **Step 2 — Rate Regime Modifier:** 10Y yield 4.61% sits in the 3.5–5% bracket → **+5**.
- **10Y Treasury yield source:** reused from the same-day BKNG session (WebSearch cross-check, converging on 4.61% as of 2026-08-04) per CLAUDE.md's "check the most recent session, don't refetch FRED unless none exists" instruction.

**Total Rate Environment Gate modifier: +10**

---

## 5. Phase 02 — Valuation Score

### Market cap / EV basis

- **Shares outstanding** = 1,208,570,347 (Class A) + 78,073,584 (Class B) + 1 (Founder Share) = **1,286,643,932** (SEC 10-Q cover page, `dei:EntityCommonStockSharesOutstanding` as of 2026-07-31, the most current count available)
- **Market Cap** = 1,286,643,932 × $150.72 = **$193,922.97M**
- **EV** = Market Cap ($193,922.97M) + Debt ($0) − Cash ($1,656M) = **$192,266.97M**

### PEG / Fast Grower eligibility — not applicable

SHOP's GAAP diluted EPS history: FY2022 **−$2.73** → FY2023 **$0.10** → FY2024 **$1.55** (+1,450% YoY, a low-base artifact off FY2023's near-zero earnings) → FY2025 **$0.94** (**−39.4% YoY** — an outright decline, driven by a $973M Q1-2025 unrealized loss on equity investments). This is neither ">15% for 3+ consecutive years" nor a "clean, non-distorted earnings base" — SHOP only turned durably GAAP-profitable in FY2023, and its GAAP EPS since then has been dominated by large, volatile, non-operating equity-investment mark-to-market swings (the same clean-earnings-base problem the 2026-06-20 PEG clarification was written for). **PEG's 15% weight is redistributed to EV/EBIT (→ 40% weight)**, per valuation-scoring.md.

### FCF Yield (40% weight)

- FCF Yield = TTM FCF ($2,352M) ÷ Market Cap ($193,922.97M) = **1.213%**
- FCF_Score = clamp(100×(1 − 1.213/10)) = **87.87**

### EV/EBIT (40% weight, PEG-redistributed)

- EV/EBIT = $192,266.97M / $1,844M = **104.27×**
- EV/EBIT_Score = clamp((104.27 − 12)/23 × 100) = clamp(401.2) = **100.0 (capped)**
- Cross-check: GuruFocus reports EV/EBITDA 65.52× as of **June 8, 2026** — a stale figure computed off a pre-earnings price roughly 40% below today's live print and an older TTM-EBITDA base that didn't yet include Q2 2026's blowout quarter; not treated as a meaningful cross-check given how far the underlying inputs have since moved (Rule 0 discipline — use current, not cached, data). My own EV/EBITDA (EV $192,267M / EBITDA $1,873M = **102.7×**) is internally consistent with the EV/EBIT figure above.

### Forward PE (20% weight)

- **FY2026 consensus EPS = $1.85** (stockanalysis.com, 48 analysts, as of 2026-08-04/05; cross-checked against macroaxis's independently-sourced $1.86 average — consistent).
- Forward PE = Live Price ($150.72) ÷ Consensus EPS ($1.85) = **81.47×**
- **5-year avg/range PE: no-history fallback invoked, flagged.** Same distortion pattern as the BKNG precedent, more extreme here: reported 5-year average PE ranges from **98.07× (one source) to 171.0× (another)** — a >70% spread — and the trailing 6-year quarterly PE range runs from **49.3× (Sep 2021) to 779× (Dec 2023)**, reflecting quarters where trailing EPS was near-zero (FY2023's $0.10 EPS, in particular, makes any PE computed off it essentially meaningless) — [fullratio.com](https://fullratio.com/stocks/nasdaq-shop/pe-ratio), [macrotrends](https://m.macrotrends.net/stocks/charts/SHOP/shopify/pe-ratio). This is exactly the "GAAP earnings base too distorted to be meaningful" scenario valuation-scoring.md's fallback clause anticipates. No `yfinance` reconstruction was possible in this environment (blocked, see §2). **FwdPE_Score = 50.0 (neutral, flagged)** — no separate Historical PE Modifier applied, consistent with the fallback rule.

### Raw weighted score

```
Raw Score = FCF_Score×0.40 + EV/EBIT_Score×0.40 + FwdPE_Score×0.20
          = 87.87×0.40 + 100.0×0.40 + 50.0×0.20
          = 35.148 + 40.000 + 10.000
          = 85.15
```

### Upside/Downside Modifier

**Fair Value work (Step 1, fair-value-methodology.md) — DCF + comparable multiples, 3 scenarios, 40%/60% blend:**

*DCF assumptions (flagged as analyst judgment, not fetched data, per the BKNG/AVGO precedent):* Cost of equity via CAPM = risk-free 4.61% + beta × ERP (5.0% standard assumption). **Beta**: WebSearch converged on two independently-sourced values, **2.31** and **2.644** — used the average, **2.48**. Cost of equity = 4.61 + 2.48×5.0 = **17.01%**; since SHOP carries **zero debt**, WACC = cost of equity (no debt-weighting needed) → **WACC ≈ 16.61%** base case (±1pp for bull/bear, per Rule 2). Full 10-year, 3-stage model (Stage 1 yrs 1–5 explicit, Stage 2 yrs 6–10 fade, Stage 3 terminal). Terminal growth capped at 2.75% (≤ long-run GDP, per Rule 2). Base-case Y1 revenue growth (30%) set at the middle of management's own Q3 2026 "low-thirties%" guidance range — guidance is never scored directly, but is an explicitly permitted DCF sanity anchor (fair-value-methodology.md, "Why Forward Guidance Is Not a Sub-score"). FCF margin path starts near the TTM actual (17.7%, matching the company's own disclosed 18% Q2 2026 FCF margin) and expands with disclosed operating leverage.

| Scenario | WACC | Growth path (Y1→Y10) | FCF margin path (Y1→Y10) | DCF FV/share |
|---|---|---|---|---|
| Bull | 15.61% | 32% → 2.75% | 19% → 32% | **$63.52** |
| Base | 16.61% | 30% → 2.75% | 18% → 28% | **$43.26** |
| Bear | 17.61% | 27% → 2.75% | 17% → 22% | **$27.25** |

All three scenarios put Terminal Value at 33–43% of total EV, comfortably under Rule 4's 75% sanity cap.

*Comparable multiples:* Given Shopify's TTM revenue ($13.3B), Rule 5's ±50% revenue-scale peer band ($6.6B–$19.9B) is genuinely hard to fill from commerce/payments names — **flagged as a peer-set limitation**, same caveat class as prior sessions' imperfect comp sets. Used the closest available commerce/payments peers by business model, with the scale mismatch disclosed: Wix (WIX, ~$1.9B revenue) forward PE 9.3×, PayPal (PYPL, ~$31B revenue) forward PE ~10.0×, Block (SQ/XYZ, ~$26.8B revenue est. FY2026) forward PE ~19.0×, Adyen (ADYEN, ~€2B revenue) forward PE ~21.0×, Global-e (GLBE, ~$1.1B revenue) forward PE ~40.0× (multiple sources, several conflicting on exact price-date; used representative midpoints). Peer median 19.0×, average 19.86×.

| Scenario | Multiple basis | Applied to | Multiples FV/share |
|---|---|---|---|
| Bull | Near top of peer range (36×, below Global-e's high end) | FY2026 consensus EPS $1.85 | **$66.60** |
| Base | Peer average (19.86×) | FY2026 consensus EPS $1.85 | **$36.74** |
| Bear | Peer low end (Wix 9.3×) | FY2026 consensus EPS $1.85 | **$17.21** |

**Triangulation (40% DCF + 60% Multiples, per fair-value-methodology.md Step 1):**

```
Bull FV = 0.40×63.52 + 0.60×66.60 = $65.37
Base FV = 0.40×43.26 + 0.60×36.74 = $39.35
Bear FV = 0.40×27.25 + 0.60×17.21 = $21.22

PW Fair Value = 0.25×65.37 + 0.50×39.35 + 0.25×21.22 = $41.32
```

**Step 1 — Expected annual return E:**

```
Gap Upside % = (PW FV ÷ Live Price) − 1 = (41.32 / 150.72) − 1 = −72.58%
Catalyst window = 2 years (no specific 18–24mo re-rating catalyst identified — see note below; default per Rule 10)
Annualized gap = −72.58% / 2 = −36.29%
Intrinsic growth = 27.10% (base-case FCF CAGR, Y0→Y5: ($7,801M/$2,352M)^(1/5)−1 = 27.10%)
Shareholder yield = dividend yield (0% — SHOP pays no dividend) + net buyback yield (2.25%: annualized
  net share-count decline, SEC balance sheet share counts, 1,303,904,301 shares (2025-12-31) →
  1,289,206,588 shares (2026-06-30), annualized over the 182-day window — Shopify began a new buyback
  program in 2026, repurchasing $1,911M of stock in H1 2026 vs. $0 in H1 2025)
E = −36.29% + 27.10% + 2.25% = −6.94%
```

**Note on catalyst/guardrail:** this is an *expected-loss* case (E < 0), where per the framework's guardrail rules the "no catalyst → cap upside at −5" restriction does **not** apply ("Downside side unaffected — a thesis with no catalyst and an expected loss should still be penalised"). No specific re-rating catalyst was identified or required for this calculation.

**Step 2 — Map E to modifier** (H = 10%):

```
E (−6.94%) < 0 → M = +5 + 10×clamp((−E)/10pp, 0, 1) = +5 + 10×clamp(0.694, 0, 1) = +5 + 6.94 = +11.94
```

**Note on this result:** despite a substantial assumed 27.1%/yr intrinsic FCF growth rate and a modest incremental buyback yield, the sheer size of the valuation gap (live price 3.6× the probability-weighted fair value) overwhelms both — E still lands meaningfully negative. This is the clearest possible case of "richly priced, thin/negative expected forward return," exactly what this modifier is designed to penalize.

### Final Valuation Score

```
Final Score = Raw Score + Rate Environment Gate + Upside/Downside Modifier
            = 85.15 + 10.00 + 11.94
            = 107.09 → clamped to Maximum 100.0
```

**Valuation Score = 100.0 / 100.0** (the maximum — most expensive end of the scale)

---

## 6. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 83.5) + 0.50 × 100.0
                = 0.50 × 16.5 + 0.50 × 100.0
                = 8.25 + 50.0
                = 58.25 → rounds to 58.3 (exact ".X5" tie, rounds UP per the conservative boundary rule)
```

**Composite Score = 58.3 / 100.0 — "Fair Value / Hold" band (50.0–69.9).** SHOP's very high Quality Score (83.5) meaningfully pulls the blend down from the raw Valuation Score's ceiling of 100.0 — but even a Quality Score this strong cannot pull a maxed-out valuation score all the way into a buyable band. The Composite Score correctly reflects "excellent business, currently priced for perfection and then some," not "excellent business, attractively priced."

---

## 7. Fair value & recommendation

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Step 2's Composite-Score-to-action integration table:

```
Score 0.0–29.9  → Enter now
Score 30.0–49.9 → Set limit order
Score 50.0–69.9 → No MoS → Watchlist only        ← SHOP (58.3) lands here
Score 70.0–100.0 → Do not buy → Trim or exit protocol
```

**No Margin-of-Safety / Buy-Price / Stop-Loss table exists for the 50.0–69.9 band** — the framework's MoS table (fair-value-methodology.md Step 2) only defines ranges for the 0.0–29.9, 30.0–49.9, Turnaround, and Speculative bands. There is accordingly no formal order setup to compute here; this is a straightforward "not attractive enough to enter, but not a quality/thesis problem either" read, not a price/R-R-gate case like BKNG's.

```
[x] Composite Score (incl. Quality blend):        58.3  (Fair Value / Hold band, 50.0–69.9)
[x] Valuation Score (incl. Rate Gate + Upside/Downside Mod): 100.0  (maximum — clamped from 107.1 raw)
[x] Expected annual return E / catalyst window:    −6.94% / 2yr (default window; no catalyst required for a downside case)
[x] Upside/Downside Modifier applied:              +11.94
[x] DCF Fair Value (base case):                    $43.26
[x] Multiples-Based Fair Value (base case):         $36.74
[x] Blended Fair Value (PW, bull/base/bear):        $41.32
[x] Live price vs. Blended FV:                      $150.72 is 3.65× the $41.32 PW Fair Value
```

**Reference-only monitoring level:** numerically solving (holding the Blended FV inputs fixed) for the price at which the Composite Score would cross into the 30.0–49.9 "Cheap / Set limit order" band gives **≈$59.08** — a ~61% decline from today's live price. This is a rough monitoring trigger, **not** a formal Buy Price (no MoS/order-setup mechanics apply to the Hold band, and a fresh full re-score — with then-current price, EPS estimates, and E — would still be required before any order).

---

## 8. Recommendation

**WATCHLIST ONLY — do not enter.**

SHOP clears the Quality Score gate comfortably (83.5/100.0, Moat 5/5, no hard disqualifiers, debt-free with a genuine net-cash balance sheet) — this is unambiguously a high-quality business. But it is trading at extreme multiples following today's post-earnings pop: **EV/EBIT 104.3×** (vs. a 12–35× scored range), **Forward PE 81.5×** (vs. a peer group clustering 9–21×), **FCF yield just 1.2%**, and a probability-weighted blended fair value ($41.32) sitting at roughly **28% of the live price** ($150.72). The Valuation Score hits its maximum possible value (100.0, clamped from a raw 107.1) even after crediting the business's genuinely strong ~27%/yr intrinsic FCF growth trajectory in the Upside/Downside Modifier. The blended Composite Score of 58.3 reflects the Quality Score doing real work to pull the number down from the valuation ceiling — but "excellent quality partially offsetting an extreme valuation" still nets out to "Hold/watchlist," not "buy."

**No position opened. Nothing logged in `decisions/` or `portfolio/holdings.md`.**

---

## 9. Qualitative notes (5 questions + disruption vector check)

1. **Why are margins high (where they are high)?** Gross margin (47.8% TTM) reflects an asset-light SaaS-plus-payments model — Shopify's own infrastructure/hosting scale amortized over millions of merchant stores, and Shopify Payments/Shop Pay processing fees that scale with GMV without proportional headcount growth. Operating margin (13.9% TTM EBIT/Revenue) is thinner than pure-SaaS peers because "Merchant Solutions" (payments, capital, Shop Pay, fulfillment) carries materially lower gross margin than "Subscription Solutions" (79.6% vs. 89.6% TTM cost-of-revenue-implied, per Q2 2026's segment breakout) and is the faster-growing, larger segment ($2,781M vs. $802M revenue in Q2 2026 alone).

2. **Moat assessment:** Moat_Score 100.0 (5/5, all independently cited — see §3). Dominant and *growing* ecommerce-platform share (46.0% vs. #2's much smaller and shrinking share), demonstrated pricing power (33-34% price hike absorbed with "very little churn" and accelerating subsequent growth), genuine two-sided network effects (Shop Pay's 200M+ buyer network, the App Store's 21,000+ apps/12,000+ developers), real switching costs (documented $5K–$300K+ migration costs dominated by theme/app rework, not just data), and a scale cost advantage translating into a published 33–45% better TCO than its closest direct competitor.

3. **Capital allocation track record:** Historically reinvestment-heavy (near-breakeven-to-loss-making through FY2022), turned durably FCF-positive from FY2023 onward, and **initiated its first-ever meaningful share buyback program in 2026** ($1,911M repurchased in H1 2026 vs. $0 in H1 2025) — a capital-allocation inflection worth monitoring for consistency. No debt, no dividend, no major M&A in the recent period (the balance sheet shows $0 in acquisitions of businesses in H1 2026 vs. $56M in H1 2025).

4. **Growth sources next 3–5 years:** Continued core GMV/take-rate growth (GMV +32% YoY to $115.6B in Q2 2026), enterprise/Shopify Plus penetration (+34% YoY to 47,000+ stores), B2B commerce (+96–101% YoY GMV, still a small base), international expansion, and AI-driven merchant tooling ("with AI, we're expanding what's possible for all of them," per President Harley Finkelstein's Q2 2026 earnings quote) — though the AI angle here is qualitative company messaging, not independently verified evidence, and is flagged as such.

5. **Best bear case:** The valuation itself is the bear case — a 3.6× gap between live price and this framework's probability-weighted fair value leaves essentially no margin for a growth deceleration, a merchant-spending slowdown, or any disappointment relative to today's "monster quarter" narrative. More structurally: Shopify's own equity-investment portfolio (the source of the huge GAAP net-income swings this session flagged) introduces earnings volatility and optical noise unrelated to the core commerce business, which could confuse less careful readers of the headline numbers going forward. Competitive pressure from vertically-integrated retail-media/marketplace giants (Amazon, TikTok Shop) on the demand-generation side of commerce (as distinct from the platform-infrastructure side Shopify occupies) is a longer-horizon watch item, though not yet evident in Shopify's own share/growth data.

6. **Disruption vector check:** AI-agent-mediated commerce (an LLM assistant transacting directly with a merchant's backend, bypassing the traditional storefront/checkout UI Shopify's platform is built around) is the most credible medium-term structural question — similar in kind to the AI-agent-mediated *travel-booking* risk flagged for BKNG this same session cycle. Shopify's own AI tooling investments (cited above) are a direct hedge/response, and no evidence yet exists of share loss to an AI-native commerce competitor. Flagged as an ongoing Phase 04 watch item, not a present disqualifier.

---

## 10. Next review trigger

- SHOP's Q3 2026 earnings release (Rule 9 standard trigger — date not yet company-confirmed; Shopify has historically reported early-to-mid November)
- Any guidance revision (up or down) — mandatory re-valuation trigger regardless of schedule
- Price reaching the ≈$59.08 reference-monitoring level identified in §7 — worth an ad hoc re-check (not an automatic buy signal — a fresh full re-score would still be required)
- Any confirmed AI-native commerce competitor gaining measurable share — the disruption-vector watch item from §9

---

## Files touched this session

- `sessions/2026-08-05-new-position-shop.md` — this file
- `watchlist/not-in-portfolio/SHOP/SHOP-2026-08-05.md` — new (first-ever) watchlist entry
- `framework/glossary.md` — added **GMV (Gross Merchandise Volume)**, **Merchant Solutions / Subscription Solutions**, **MRR (Monthly Recurring Revenue, Shopify usage)**, **Shop Pay**, each placed in correct alphabetical position. **TCO (Total Cost of Ownership)** and **Buyback yield (net buyback yield)** already existed (from prior AI-chip and BKNG sessions respectively, generic enough to cover this session's usage) — cited rather than duplicated.

`portfolio/holdings.md`, `decisions/`, and `watchlist/STALE.md` **not touched** — no position was opened, and this is SHOP's first-ever score (nothing to mark stale).

---

## Glossary

- **8-K** — SEC "current report" filed within days of a material event; Shopify's Q2 2026 earnings press release was furnished via an 8-K Exhibit 99.1 on 2026-08-05.
- **Beta** — a stock's sensitivity to overall market moves, used with the risk-free rate and Equity Risk Premium to estimate cost of equity in WACC; SHOP's elevated beta (~2.3–2.6) drives an unusually high WACC in this session's DCF.
- **CAGR** — Compound Annual Growth Rate.
- **CAPM (Capital Asset Pricing Model)** — a standard formula for cost of equity: risk-free rate + beta × equity risk premium.
- **Composite Score** — this framework's blended Quality + Valuation ranking number (50/50), computed only for companies clearing the 80.0+ Quality Score gate.
- **DCF (Discounted Cash Flow)** — a valuation method projecting future cash flows and discounting them to present value.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **Enterprise Value (EV)** — Market Cap + Total Debt − Cash; the total cost to acquire a company including its debt.
- **EPS** — Earnings Per Share.
- **Equity Risk Premium (ERP)** — the extra return equity investors demand over the risk-free rate; a standard DCF modeling assumption (5.0% here), not a fetched fact.
- **Fast Grower** — Peter Lynch's term for a company growing EPS >15%/year for 3+ years; this framework's PEG-sub-score trigger. SHOP does not currently qualify (volatile, recently-turned-profitable GAAP earnings base).
- **FCF (Free Cash Flow)** — cash generated by operations after capital expenditure.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; an earnings-quality check.
- **FCF Yield** — Free Cash Flow ÷ Market Cap; how much cash a company throws off relative to its price.
- **Forward PE** — Price ÷ next-twelve-months expected EPS.
- **GMV (Gross Merchandise Volume)** — the total dollar value of all orders processed through Shopify's platform, before Shopify's own take-rate (fees) is deducted — Shopify's primary top-of-funnel volume metric, analogous to BKNG's "Gross Bookings." *(New term.)*
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of weighted score; none fired for SHOP.
- **Invested Capital** — the capital (debt + equity, net of cash in this framework's convention) put to work in a business; the choice of what counts as "cash" is a flagged judgment call for SHOP given its large liquid-investment balance.
- **Merchant Solutions / Subscription Solutions** — Shopify's two reported revenue segments: Merchant Solutions (payments, Shop Pay, capital/lending, fulfillment — the larger, faster-growing, lower-margin segment) and Subscription Solutions (platform access fees — the smaller, higher-margin segment). *(New term.)*
- **Moat** — a durable competitive advantage protecting a business's profits from competitors.
- **MRR (Monthly Recurring Revenue, Shopify usage)** — Shopify's own disclosed metric for recurring subscription-platform revenue run-rate ($221M in Q2 2026), distinct from GMV (transaction volume) or total reported Revenue (which also includes Merchant Solutions revenue). *(New term.)*
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate. Negative for SHOP (net cash).
- **NOPAT** — Net Operating Profit After Tax; the numerator this framework uses for ROIC.
- **PEG ratio** — PE ratio ÷ earnings growth rate; not applicable to SHOP this session (Fast Grower test not met).
- **PW (Probability-Weighted) Fair Value** — this framework's blended bull/base/bear fair value estimate (25%/50%/25%).
- **Quality Score** — this framework's 0.0–100.0 continuous quality grade; SHOP scores 83.5, clearing the 80.0+ gate.
- **Rate Environment Gate** — the mandatory pre-check comparing Earnings Yield against the 10-Year Treasury yield.
- **Rate Regime Modifier** — an additive valuation-score adjustment based on the current Treasury-yield bracket.
- **ROIC** — Return on Invested Capital; a flagged judgment call for SHOP due to its cash/investment-heavy balance sheet (see §3).
- **Rule 0** — this framework's standing instruction to always fetch a live price before any valuation work.
- **Rule 5** — this framework's comparable-company-analysis standard (minimum 5 peers, similar business model/scale/geography); flagged as imperfectly met for SHOP given the thin set of true revenue-scale peers.
- **Rule 9** — this framework's list of fundamental events forcing an immediate re-valuation.
- **Rule 10** — this framework's instruction to separate intrinsic value from market price, assign a catalyst/timeline, and track valuation accuracy over time.
- **Shareholder yield** — dividend yield plus net buyback yield combined; SHOP pays no dividend but began a meaningful buyback program in 2026.
- **Shop Pay** — Shopify's accelerated/one-click checkout product and associated 200M+-user cross-merchant buyer-recognition network, cited as Network Effect moat evidence. *(New term.)*
- **TCO (Total Cost of Ownership)** — the all-in cost of running a platform over time (subscription/licensing fees, required third-party apps, development/maintenance labor), used here as third-party evidence of Shopify's scale cost advantage vs. a named competitor. *(New term.)*
- **Terminal Value** — the lump-sum DCF value assigned to all cash flows beyond the explicit forecast period.
- **Treasury yield (10Y)** — the standard risk-free-rate benchmark used throughout the Rate Environment Gate.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.
- **Upside/Downside Modifier** — an additive ±15 valuation-score adjustment based on expected annual return; landed strongly positive (+11.94, toward the trim/sell end) for SHOP despite genuinely strong intrinsic growth, because the valuation gap is too large to overcome.
- **WACC** — Weighted Average Cost of Capital; the DCF discount rate. Equal to cost of equity for SHOP since it carries no debt.

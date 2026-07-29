# New Position Evaluation — COIN (Coinbase Global, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-07-25
**10Y US Treasury yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (see Section 3) before the Rate Environment Gate would otherwise apply (same precedent as the 2026-07-24 QCOM session and the 2026-07-19 SCHW session before it).
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — a `t.me/bolshegold` post (post #9832, ~16:02 UTC 2026-07-25) was a casual "earnings to watch next week" round-up mentioning the cashtag `$COIN` alongside other names. COIN has **no prior watchlist entry anywhere** under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). Per Rule 0, **no claim from the triggering post is used as a financial input anywhere below** — the post's text is not treated as verified data and is only the reason COIN was looked at today; every number in this session was fetched fresh, independent of the post, from IBKR (live price), `stockanalysis.com`, and SEC XBRL.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 481691285, NASDAQ — "COINBASE GLOBAL INC -CLASS A") | **$161.16** | `last.price`, `is_close: true` — today (2026-07-25) is a **Saturday**, so this is the most recent genuine trade print available: the regular-session close from **Friday 2026-07-24**, not a stale prior-week figure. `change`/`prior_close`/`bid_ask`/`open`/`high`/`low` all returned empty on two separate field requests — expected while markets are closed over the weekend. |
| 52-week range (IBKR `misc_statistics`) | low **$139.18** / high **$402.16** | 13-week and 26-week highs are both identical to the 52-week high ($402.16), meaning that high was set within the trailing 13 weeks. Current price is **~59.9% below** that recent high and **~15.8% above** the 52-week low — a very large drawdown, shown here as context only, not itself a scoring input or basis for any conclusion below (Rule 0 / "never act on price movement alone"). |
| Dividend yield (IBKR) | 0.0% | No dividend. |
| **Cross-check discrepancy, flagged:** `stockanalysis.com`'s overview page (fetched same session) reported COIN "closed at $158.29, down 1.78% for the day" for 2026-07-24 — a **~1.8% discrepancy** against IBKR's $161.16 for what should be the same closing print. Per this session's mandate (IBKR is the designated live-price connector, account U19421206), **$161.16 is treated as the price of record**; the stockanalysis.com figure is noted but not used. This discrepancy does not affect the Quality Score (Section 3), which uses no price input — it would only matter if Phase 02 valuation scoring were reached, which it is not (see Section 3.3). | | |
| Implied market cap (live price × ~263.46M shares out, per `stockanalysis.com`) | ~$42.46B | Context only — shares-out figure not independently re-derived from a primary filing this session (the SEC `dei:EntityCommonStockSharesOutstanding` XBRL concept query returned no data for this CIK). |

**Live price used throughout this session: $161.16.**

---

## 2. Data Source Note

Coinbase Global, Inc. is a US SEC filer (**CIK 0001679788**, fiscal year = calendar year). Fundamentals for this session were sourced from two places, cross-validated against each other line-by-line wherever both were available:

- **`stockanalysis.com`** (`/stocks/COIN/financials/`, `/financials/balance-sheet/`, `/financials/cash-flow-statement/`, `/financials/ratios/`, and the ticker overview page) — used for annual income-statement history (FY2021–FY2025), the FY2025/Q1-2026 balance sheet, and headline ratios.
- **SEC XBRL `companyconcept` API** (`data.sec.gov/api/xbrl/companyconcept/CIK0001679788/us-gaap/...`) — pulled directly to independently reconstruct trailing-twelve-month (TTM) Revenue, Operating Income (EBIT), Net Income, and Income Tax Expense from the four most recently disclosed quarters (Q2 2025 → Q1 2026, the most recent filed 10-Q, period ended 2026-03-31). `yfinance` was attempted first and failed with a TLS connection-reset error (`curl_cffi... Recv failure: Connection reset by peer`), consistent with the same block seen in the 2026-07-24 QCOM/EVO sessions — SEC XBRL + `stockanalysis.com` used as the established fallback.
- **`data.sec.gov/submissions/CIK0001679788.json`** — CIK confirmed, though the WebFetch summarization of this endpoint returned an incompletely-sorted filing list; not relied on for figures, only used to confirm the CIK.
- **Independent web search** (non-Telegram, non-trigger-post sources) — used for the Growth-modifier and Moat-signal qualitative evidence in Section 3.2, each cited individually at the point of use, and to confirm Coinbase's Q2 2026 earnings date (2026-07-30, after this session — see Section 6).

**Every TTM figure reconstructed from SEC XBRL below was cross-checked against `stockanalysis.com`'s own independently-reported TTM total, and all four checks reconciled to within rounding** (Revenue: $6,560,012K reconstructed vs. $6,560M reported; Net Income used to derive ROIC 5.376% vs. `stockanalysis.com`'s independently-computed ROIC 5.37%; Operating Cash Flow $2,791,854K reconstructed vs. $2,792M reported; Stockholders' Equity $13,480,573K (SEC) vs. $13,481M (`stockanalysis.com`)) — high confidence in the figures below.

No required Phase 01 input was invented, estimated, or inferred from the triggering post.

### 2.1 A note on CapEx (not separately itemized by the data vendor)

`stockanalysis.com`'s cash-flow-statement page presents Coinbase's "Free Cash Flow" as numerically identical to its "Operating Cash Flow" for every period shown, without a broken-out CapEx line. Rather than invent a CapEx figure, this was checked directly against a primary filing: Coinbase's Q3 2025 10-Q (nine months ended 2025-09-30) discloses **"Purchases of property and equipment: $(1,130)" thousand** — i.e. **~$1.13M over nine months** (~$1.5M annualized) against **>$2.4B of annual operating cash flow**. CapEx is genuinely immaterial for this asset-light exchange business (consistent with Coinbase's own minimal owned physical-infrastructure footprint), which is why the vendor's OCF and FCF figures are identical at reported precision — not a data gap, and not an invented estimate. **FCF is therefore treated as ≈ OCF throughout this session.**

### 2.2 A note on Coinbase's extreme year-to-year earnings volatility

Coinbase's revenue and net income are directly tied to crypto asset prices and trading volumes, producing a business with far more year-to-year (and quarter-to-quarter) swing than a typical Quality Score candidate: annual Net Income ranged from **+$3,097M (FY2021)** to **−$2,625M (FY2022, the "crypto winter")** to **+$94.75M (FY2023)** to **+$2,578M (FY2024)** to **+$1,260M (FY2025)**, and the trailing-twelve-month window used throughout Section 3.2 (Q2 2025 → Q1 2026) itself spans a **+$1,428.9M** quarter (Q2 2025) and a **−$394.1M** quarter (Q1 2026, revenue down 31% YoY on falling crypto prices). This volatility is a legitimate, current reflection of Coinbase's business model — not smoothed, adjusted, or normalized away anywhere below, consistent with "never invent or estimate financial data" — but is flagged explicitly here because it is the direct cause of the low Profitability sub-score in Section 3.2 (a TTM window ending in a crypto-downturn quarter, rather than a cherry-picked favorable window).

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | COIN data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF (≈ OCF, per §2.1) by year: FY2022 **−$1,585M**, FY2023 **+$673.38M**, FY2024 **+$3,104M**, FY2025 **+$2,426.383M**, TTM (Q2 2025→Q1 2026) **+$2,791.854M**. Positive every year since the FY2022 crypto-winter trough — 3 full fiscal years (FY2023–FY2025) plus the current TTM, all positive. | **PASS — does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard, or 4×/6× under the Upgrade 5 asset-light override)** | As of the most recent balance sheet (2026-03-31): Total debt **$7,776M**; Cash **$10,205M** + ST investments **$232.98M** = **$10,437.98M**. **Net debt = 7,776 − 10,437.98 = −$2,661.98M** (a **net cash** position, consistent with FY2025 year-end's **−$3,936M** net cash). Net debt is negative, so Net Debt/EBITDA is negative under any denominator — the debt-gate ratio is not a constraint regardless of which override (2.5×/4×/6×) would otherwise apply. | **PASS — well under threshold (net cash).** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FCF/NI by year: FY2023 **710.6%** ($673.38M/$94.75M), FY2024 **120.4%** ($3,104M/$2,579.066M), FY2025 **192.5%** ($2,426.383M/$1,260.327M), TTM **348.75%** ($2,791.854M/$800.602M). Every year and the TTM are far above 70% (elevated ratios are typical of a business with large non-cash stock-based-compensation add-backs relative to a volatile, currently-depressed net-income base). | **PASS — does not fire.** |

No hard disqualifier fires. COIN's outcome is decided entirely by the weighted score below, exactly as it was for the 2026-07-24 QCOM session and the 2026-06-30 CRCL session (a closely comparable digital-asset-infrastructure business).

### 3.2 Sub-scores (all six, per the weighted formula)

**TTM reconstruction (Q2 2025 → Q1 2026, the four most recent quarters through the most recently filed 10-Q, period ended 2026-03-31), sourced from SEC XBRL `companyconcept` and cross-checked against `stockanalysis.com`'s own reported TTM totals:**

| Line item ($K) | Q2 2025 (end 2025-06-30) | Q3 2025 (end 2025-09-30) | Q4 2025 (derived: FY2025 annual − 9mo) | Q1 2026 (end 2026-03-31) | **TTM total** | Cross-check vs. `stockanalysis.com` TTM |
|---|---|---|---|---|---|---|
| Revenue | 1,497,208 | 1,868,693 | 1,781,129 | 1,412,982 | **6,560,012** | 6,560,000 ✓ match |
| Operating Income (EBIT) | (24,650) | 480,532 | 273,753 | (21,421) | **708,214** | not separately reported by `stockanalysis.com` this session; internally consistent (below) |
| Net Income | 1,428,900 | 432,552 | (666,733) | (394,117) | **800,602** | ROIC cross-check below reconciles (5.376% vs. 5.37% independently reported) |
| Income Tax Expense (Benefit) | 394,873 | 69,591 | (219,574) | (70,588) | **174,302** | not separately reported; internally consistent (below) |

(FY2025 Q4 figures derived as FY2025-annual-10-K total minus the disclosed 9-month-YTD figure through Q3 2025, per line item — standard TTM reconstruction; every input is a directly-filed SEC XBRL figure. **Internal consistency check:** TTM Net Income ($800,602K) + TTM Income Tax Expense ($174,302K) = TTM Pretax Income **$974,904K**; effective tax rate = 174,302/974,904 = **17.877%**.)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = 800,602/6,560,012 = **12.20%** → NetMargin_Component = clamp((12.20/30)×100) = **40.68**. NOPAT = TTM EBIT × (1 − effective tax rate) = 708,214 × (1−0.17877) = **$581,630K**. Invested Capital (2026-03-31) = Total Debt ($7,776,000K) + Equity ($13,480,573K, SEC-confirmed) − liquid assets ($10,437,980K, same cash+ST-investments figure netted above) = **$10,818,593K**. ROIC = 581,630/10,818,593 = **5.376%** (cross-checked almost exactly against `stockanalysis.com`'s independently-computed 5.37%) → ROIC_Component = clamp((5.376/30)×100) = **17.92**. Profitability_Score = (40.68+17.92)/2 = **29.30** (no FCF-positivity cap — FCF-positive 3+ years, see 3.1). *This low sub-score is a direct, undistorted reflection of Coinbase's TTM window ending in a crypto-downturn quarter — see §2.2.* | **29.30** |
| **Margins (15%)** | Gross Margin (TTM) = **86.08%** (per `stockanalysis.com`, cross-validated: the TTM revenue figure underlying this margin, $6,560M, matches the independently SEC-reconstructed TTM revenue above almost exactly). GrossMargin_Score = clamp((86.08/80)×100) = clamp(107.6) = **100.0**. No separate +10 trend bonus needed or applicable (bonus only applies below the 40% static threshold; COIN has been at 80–87% every year FY2021–FY2025). | **100.00** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $3,194M → FY2025 $7,181.325M, both directly filed annual figures) = (7,181.325/3,194)^(1/3) − 1 = **+31.0%** → base = clamp((31.0/25)×100) = clamp(124.0) = **100.0** (already capped before any modifier). **Modifier considered but immaterial to the outcome given the cap:** documented TAM-expansion evidence this session — institutional custody scale ($376B assets on platform, >12% of global crypto market cap, OCC national trust charter granted 2026-04-02 [Forbes, 2026-04-08]), stablecoin revenue $305M in Q1 2026 (up from $274M a year earlier), a new prediction-markets product already at a $100M annualized revenue run-rate by March 2026, and derivatives volume +169% YoY in Q1 2026 [Coinbase Q1 2026 investor-relations press release, 2026-05] — would earn +10 were the base score below the ceiling. **Countervailing evidence also considered:** Q1 2026 revenue fell 31% YoY to $1.41B on falling crypto prices [Yahoo Finance, 2026-05], a real deceleration — but judged **cyclical** (crypto-price/trading-volume driven), not **structural**: Coinbase's own trading-volume *market share* hit an all-time high (8.6%) in the same quarter, and subscription/services revenue and the new product lines above continued growing through the downturn — so **no −10 structural-deceleration modifier applied**. Growth_Score = **100.0** either way, since the raw CAGR already saturates the formula. *3yr-CAGR base-effect caveat flagged explicitly: FY2022 was a crypto-winter trough, so this 31% figure partly reflects rebound-from-trough rather than a steady compounding rate — shown for transparency, per "show every calculation," even though it does not change the capped result.* | **100.00** |
| **Balance Sheet (15%)** | Net Debt (TTM, as of 2026-03-31) = **−$2,661,980K** (net cash — see 3.1). BalanceSheet_Score = clamp(100×(1 − NetDebt/EBITDA/4)) — with Net Debt negative, this evaluates to >100 and clamps to **100.0** regardless of which override denominator (4× standard or 6× Upgrade-5 asset-light) would otherwise apply. | **100.00** |
| **Moat Signal (15%)** | See evidence table below — **3 of 5 signals** cleared the cited-evidence bar. (3/5)×100 | **60.00** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 2,791,854/800,602 = **348.75%** → clamp(((3.4875−0.40)/0.60)×100) = clamp(514.6) = **100.0**. | **100.00** |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | Coinbase disclosed an **all-time-high 8.6% global crypto trading-volume market share** (spot + derivatives) in Q1 2026 [Coinbase Q1 2026 investor-relations press release, "New All-Time High Crypto Trading Volume Market Share," 2026-05], and holds an estimated **62–76% share of US-based centralized-exchange volume** [coinlaw.io, "Crypto Exchange Market Share Statistics 2026"]. Caveat noted: globally Coinbase's ~6% share is dwarfed by Binance's ~39% [same source] — the credit here is for Coinbase's own trend (growing, record share) and US-market position, not global dominance. | **TRUE** |
| Brand premium | No documented pricing-power evidence (price increases without volume loss) found this session. The clearer, more specific evidence found points the other way: Robinhood's zero-fee crypto trading and SoFi's crypto-linked bank-account entry are described as "putting pressure on Coinbase's retail transaction margins" [businessmodelanalyst.com, "Coinbase SWOT Analysis (2026)"] — fee/margin **compression** from competition, the opposite of the framework's evidentiary bar for this signal. | **FALSE** |
| Network effect | **Documented two-sided ecosystem mechanism.** Coinbase's Base (Ethereum Layer-2) blockchain reportedly reached self-sustaining network effect roughly 1.5 months after launch, with developer counts running 2–3× Ethereum mainnet's own (as of April 2024) and its onchain app ecosystem generating **$193.4M in fees in Q1 2025 alone** on **$5B+ Total Value Locked** [BitcoinWorld, "Booming Base Apps," 2026] — a genuine, structurally-documented users-plus-developers network-effect mechanism, layered on top of the exchange's own inherent liquidity-begets-liquidity dynamic. | **TRUE** |
| Switching costs | **Documented, but concentrated in one segment.** Coinbase's institutional custody business held **$376B of assets on platform** at 2025 year-end (>12% of global crypto market cap) and serves as custodian for the **majority of US spot Bitcoin/Ethereum ETFs**, operating under an OCC-granted national trust charter (preliminary conditional approval, 2026-04-02) and SOC 1 Type II / SOC 2 Type II audited controls [Forbes, 2026-04-08; coinbase.com/blog]. Migrating an ETF's custodian is a high-friction, regulator-scrutinized undertaking — a real documented switching-cost mechanism — but this evidence is specific to the institutional/custody segment, not Coinbase's broader retail trading base (where moving to a competing exchange carries comparatively low friction). Credited TRUE on the strength of the institutional-custody evidence, with this segment caveat flagged. | **TRUE** |
| Scale cost advantage | Coinbase's regulatory-licensing breadth (state money-transmitter licenses, the new OCC trust charter) plausibly raises the compliance-cost bar for smaller rivals, but no **cost-per-unit** data (the framework's specific evidentiary bar: "cost-per-unit data showing a gap vs. smaller competitors") was found this session quantifying an actual per-trade or per-account cost advantage over a smaller exchange. A general "barrier to entry" argument does not, on its own, meet this signal's bar. | **FALSE** |

### 3.3 Final weighted Quality Score

```
Quality Score = (29.30 × 0.25) + (100.00 × 0.15) + (100.00 × 0.20) + (100.00 × 0.15) + (60.00 × 0.15) + (100.00 × 0.10)
              = 7.325 + 15.000 + 20.000 + 15.000 + 9.000 + 10.000
              = 76.325 → 76.3 (rounded to nearest 0.1)
```

**76.3 < 80.0 — fails the gate**, by **3.7 points** — a much closer call than the 2026-07-24 QCOM session's 19.7-point decisive miss, and comparable in magnitude to the 2026-07-06 AAPL session's 3.8-point near-miss. Four sub-scores are at the 100.0 ceiling (Margins, Growth, Balance Sheet, FCF Quality); the entire gap to 80.0 comes from **Profitability (29.30)** — a direct, undistorted reflection of a TTM window ending in a crypto-downturn quarter (§2.2) — only partially offset by **Moat (60.00)**.

**Sensitivity check (per the flagged judgment calls in 3.2), holding Profitability fixed at 29.30:**

| Moat reading | Signals credited TRUE | Moat_Score | Quality Score | Gate result |
|---|---|---|---|---|
| Most conservative | 1 of 5 (Market share only; Network effect and Switching costs both graded FALSE) | 20.0 | 70.3 | FAIL |
| Conservative | 2 of 5 (drop Switching costs — institutional-only evidence judged insufficient) | 40.0 | 73.3 | FAIL |
| **Primary reading (this session)** | **3 of 5 (Market share, Network effect, Switching costs)** | **60.0** | **76.3** | **FAIL** |
| Generous | 4 of 5 (also credit Brand premium despite the documented fee-compression evidence against it) | 80.0 | 79.3 | **FAIL — still 0.7pt short** |
| Maximally generous | 5 of 5 (also credit Scale cost advantage on the barrier-to-entry argument alone) | 100.0 | 82.3 | PASS |

**The gate outcome is robust to every reading except the single most generous one** — crediting Brand premium despite documented evidence of fee compression from Robinhood/SoFi, *and* crediting Scale cost advantage without the cost-per-unit data the framework's own evidentiary bar requires. Both of those readings would depart from "never invent — cite the specific evidence"; this session's primary, evidence-disciplined reading (3 of 5) fails the gate by 3.7 points.

### Result: **Phase 01 FAIL**

Per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md): a company scoring below 80.0 does not proceed to Phase 02. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**FAIL — does not clear the Quality Score gate**, at **76.3 vs. the strict 80.0+ bar**, missing by 3.7 points. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup were computed — that work is reserved for names that clear this framework's quality bar first.

This is a genuinely close miss, not a decisive one (contrast the 2026-07-24 QCOM session's 19.7-point gap). Four of six sub-scores sit at the 100.0 ceiling — Coinbase's gross margin (86.08%), trailing 3-year revenue growth (+31.0%, though flagged as partly a rebound-from-crypto-winter base effect), balance sheet (a genuine net-cash position, no leverage), and cash conversion (FCF/NI 348.75%) are all excellent by this framework's measure. The entire shortfall comes from **Profitability (29.30 of 100)** — TTM Net Margin of just 12.20% and ROIC of 5.376%, both depressed by a TTM window (Q2 2025–Q1 2026) that ends in a sharp crypto-downturn quarter (Q1 2026 revenue −31% YoY, a $394M net loss) — only partly offset by a **Moat score of 60.0** (3 of 5 signals credited: growing market share, a documented Base-blockchain network effect, and institutional-custody switching costs; brand premium and scale-cost-advantage both lacked the specific documented evidence the framework requires). This underlying pattern — strong balance sheet and cash conversion, excellent trailing growth optics, but earnings quality whipsawed by the underlying asset class's price cycle — is arguably a fair characterization of Coinbase's business model risk from a "durable, non-cyclical profitability" lens, independent of where the stock happens to be trading. The triggering post was a passing cashtag mention in a generic "earnings to watch" round-up, not a claimed fundamental event, and per Rule 9's non-negotiables, a large price decline alone (COIN is ~59.9% below its own 52-week high) is not itself treated as a buying opportunity without the underlying quality bar being cleared first — which it is not, on the numbers pulled fresh this session.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mandatory Rule 9 re-check:** Coinbase's Q2 2026 earnings, scheduled **Thursday 2026-07-30** (5 days after this session, after market close) — the next quarter of data will roll the TTM window forward by one quarter (dropping the strong Q2 2025 quarter, adding Q2 2026), which could move the Profitability sub-score meaningfully in either direction depending on whether crypto prices/volumes recovered or continued falling through Q2 2026.
- **Mechanical trigger:** Profitability (29.30) is the dominant gap to the 80.0 gate; Moat (60.0) is the secondary lever. The most direct paths to a materially different result: (1) a TTM window that rolls off the Q1 2026 loss quarter and replaces it with a profitable one, lifting Net Margin/ROIC; or (2) independently verifiable, specific evidence resolving either the Brand-premium signal (documented price increases without volume loss — currently contradicted by fee-compression evidence) or the Scale-cost-advantage signal (actual cost-per-trade/cost-per-account data vs. a smaller competitor) in Coinbase's favor — per the sensitivity table in 3.3, either one alone is not enough (needs both, or a genuine 5th-signal case), but either would narrow the gap.
- **Other Rule 9 events:** a guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause (note: COIN's ~59.9% decline from its 52-week high tracks the broader 2026 crypto-price downturn and is not, on the evidence gathered this session, an unexplained move).
- Absent any of the above, future Telegram mentions of COIN should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **10-K (Annual Report)** — The annual financial-disclosure report a US public company must file with the SEC, containing full audited financial statements, MD&A, and risk factors.
- **10-Q (Quarterly Report)** — The quarterly financial-disclosure report filed between annual 10-Ks — used here to reconstruct trailing-twelve-month (TTM) figures through the most recently filed quarter.
- **CAGR (Compound Annual Growth Rate)** — The smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every EDGAR filer (Coinbase's is 0001679788) — used to construct this session's SEC XBRL/filing data-pull paths.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **Effective tax rate** — The actual percentage of pretax income paid as tax in a period — used here to convert TTM EBIT into NOPAT for the ROIC calculation.
- **FCF (Free Cash Flow)** — Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score — none fired for COIN this session.
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation.
- **Layer 2 (L2)** — A blockchain built on top of a larger base blockchain (e.g. Ethereum) to process transactions faster and more cheaply, while still settling back to the base chain for security. Coinbase's Base network is an L2 built on Ethereum — cited as this session's Network Effect Moat Signal evidence. *(New term.)*
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **OCC (Office of the Comptroller of the Currency)** — The US federal regulator that charters and supervises national banks and national trust companies. Granted Coinbase preliminary conditional approval (2026-04-02) to move its institutional custody operations into a federally regulated national trust charter — cited as this session's Switching Costs Moat Signal evidence. *(New term.)*
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. COIN scores 76.3.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies eligible for valuation scoring. (COIN does not make this list, this session.)
- **ROIC (Return on Invested Capital)** — How efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **SOC 1 Type II / SOC 2 Type II** — Independent third-party audit reports (System and Organization Controls) verifying that a service organization's internal controls over financial reporting (SOC 1) and security/availability/confidentiality (SOC 2) are properly designed and operating effectively over a review period. Coinbase's custody business maintains both, supporting its institutional-client trust — cited as this session's Switching Costs Moat Signal evidence. *(New term.)*
- **Stablecoin** — A cryptocurrency token designed to hold a stable value, typically pegged 1:1 to a fiat currency like the US dollar. Coinbase's stablecoin-related revenue (largely tied to USDC) was $305M in Q1 2026, cited as Growth sub-score TAM-expansion evidence this session.
- **TAM (Total Addressable Market)** — The total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not fetched this session, since Phase 01 failed first).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure — the basis used throughout this session's sub-scores.
- **TVL (Total Value Locked)** — The total dollar value of crypto assets deposited/committed into a blockchain network's applications (e.g. lending protocols, decentralized exchanges) — a scale/adoption metric for a blockchain ecosystem. Coinbase's Base network has $5B+ TVL, cited as this session's Network Effect Moat Signal evidence. *(New term.)*
- **XBRL (eXtensible Business Reporting Language)** — The SEC's structured, machine-readable data-tagging format for filed financial statements — the source of the independently-reconstructed TTM figures in Section 3.2, pulled via the SEC's `companyconcept` API.

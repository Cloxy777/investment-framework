# NEW POSITION — RACE (Ferrari N.V., NYSE)

**Task type:** NEW POSITION (unattended Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 2026-08-17
**10Y US Treasury yield:** ~4.69% (TradingEconomics, 2026-08-17 snapshot — recorded for the record only; the Rate Environment Gate is never reached this session, see §4)
**Current RACE portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/RACE/` or `watchlist/not-in-portfolio/RACE/`, confirmed before this session started)
**Sector:** Consumer Discretionary (Consumer Cyclical) — Ultra-Luxury Performance Automobiles

---

## 0. Why this session exists — trigger source

New top post on **tarasguk** (Telegram, post tarasguk/11694, ~06:06 UTC 2026-08-17): *"🇮🇹 Ferrari продали свій перший електромобіль на аукціоні за $40 млн. Це робить його найдорожчим новим автомобілем проданим будь-коли. Після оголошення про запуск виробництва цих автомобілів в травні цього року акції італійської компанії впали на 10%."* ("Ferrari sold its first electric vehicle at auction for $40M — the most expensive new car ever sold. After announcing production of these vehicles in May, the Italian company's shares fell 10%.") RACE has no existing watchlist entry and is not a current holding, so per `telegram-scan.md` step 4 ("no watchlist entry exists at all") this triggers a full `/new-position` evaluation regardless of the mention's substance — established precedent (2026-08-16 HD/WMT, 2026-08-14 RDDT, 2026-07-19 DOCU first-ever evaluations). **Neither the $40M auction-price claim nor the "shares fell 10%" claim is used as a financial input anywhere below** — the post is the reason this session exists, nothing more. Per Rule 0, all financial data below is independently sourced from Yahoo Finance's fundamentals API (income statement, cash flow, balance sheet timeseries) and cross-checked live price via Interactive Brokers.

Note: the post's "shares fell 10%" claim was **not** independently corroborated — RACE's 52-week change is −10.4% (Yahoo `defaultKeyStatistics.52WeekChange`), a genuine multi-month figure, not a reaction to a single announcement; no single-day 10% drop appears in the price history pulled this session. Treated as unverified color, not a Rule 9 trigger, consistent with never treating post text as financial data.

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("RACE")`: contract_id **217234340**, exchange **NYSE**, description "FERRARI NV" — correct primary US listing (BVME/Italy, EBS/Switzerland, and MEXI cross-listings returned but not used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$421.01** | IBKR `get_price_snapshot`, `last` field, contract_id 217234340 (pre-market, ts 2026-08-17 08:10:41 UTC — NYSE regular session had not yet opened at fetch time) |
| Prior close | $414.85 | Yahoo Finance chart API (2026-08-14 regular close — last completed regular session; Friday) |
| Change | +$6.16 (+1.48%) pre-market | IBKR `get_price_snapshot` |
| 52-week high / low | $504.49 / $312.57 | IBKR `misc_statistics` |
| 26-week high / low | $417.67 / $312.57 | IBKR `misc_statistics` |
| 13-week high / low | $417.67 / $320.00 | IBKR `misc_statistics` |
| Open 52 weeks ago | $464.43 | IBKR `misc_statistics` |
| Dividend yield | 2.03% | IBKR `get_price_snapshot` |

**Cross-check:** Yahoo Finance's same-window pre-market quote showed $421.22 (+1.53%, ts 08:10:41 UTC) — a $0.21 difference, immaterial (both real-time pre-market ticks, tiny timing/venue gap). $421.01 sits **~34.8% above** its 52-week low and **~16.6% below** its 52-week high — upper-middle of its range, well off the low. Analyst consensus 12-month price target (Yahoo `financialData`, 14 analysts): mean $460.61, "strong_buy" consensus (+9.4% implied from $421.01) — noted for context only, not used in any calculation below.

---

## 2. Data Sourcing & Method

**`yfinance`'s Python client failed this session** with a `curl_cffi` TLS/connection-reset error when fetching the cookie/crumb needed for its `quoteSummary` calls — a proxy-layer incompatibility with `curl_cffi`'s browser-TLS-impersonation, not a data-availability issue (plain `curl` to the same Yahoo endpoints succeeded immediately). Worked around by calling Yahoo Finance's **same underlying REST APIs directly via `curl`** (chart API for price/52-week range; `quoteSummary` for `financialData`/`defaultKeyStatistics`/`summaryDetail`/`assetProfile`; the `fundamentals-timeseries` API for multi-year annual income-statement, cash-flow, and balance-sheet line items) — same data source the framework's documented `yfinance` methodology already relies on, just accessed at the HTTP layer instead of through the Python wrapper. Live price cross-checked against Interactive Brokers per §1.

**Currency note:** Ferrari reports natively in EUR (`financialCurrency: EUR`). The `fundamentals-timeseries` annual statement figures (revenue, EBIT, EBITDA, net income, FCF, debt, cash, equity, invested capital) are pulled as a single self-consistent EUR-denominated series — used for every **ratio** below (margins, ROIC, Net Debt/EBITDA, FCF/NI, growth rates), where currency cancels out. The `financialData`/`defaultKeyStatistics` module's own ratio fields (`grossMargins`, `profitMargins`, `returnOnEquity`, `enterpriseToEbitda`, etc.) are used directly rather than re-derived from raw dollar figures, consistent with this framework's already-documented practice (verified against stockanalysis.com in the original `yfinance` methodology writeup) — this avoids the cross-currency mixing risk that raw USD-market-cap-vs-EUR-statement division would introduce.

---

## 3. Data Gathered

### 3.1 Income statement — Yahoo Finance `fundamentals-timeseries` (EUR, annual)

| Fiscal Year (ended Dec 31) | Revenue | Gross Profit | EBIT | Net Income | Pretax Income | Tax Provision |
|---|---|---|---|---|---|---|
| FY2022 | €5,095.3M | €2,446.3M | €1,203.3M | €932.6M | €1,177.8M | €238.5M |
| FY2023 | €5,970.1M | €2,974.3M | €1,631.6M | €1,252.0M | €1,602.4M | €344.9M |
| FY2024 | €6,676.7M | €3,347.2M | €1,929.0M | €1,521.9M | €1,889.0M | €363.0M |
| FY2025 | €7,145.8M | €3,692.8M | €2,104.8M | €1,596.9M | €2,063.6M | €464.1M |

**TTM (Yahoo `financialData`/`defaultKeyStatistics`, currency basis internally self-consistent with `enterpriseValue`/`marketCap`):** Revenue $7,353.3M, Net Margin 22.25%, Gross Margin 51.62%, Operating Margin 31.065%, EBITDA Margin 33.60%, ROE 45.44%, ROA 13.61%.

**Cross-check:** FY2025 revenue (€7,145.8M) and TTM revenue ($7,353.3M) track consistently (TTM > FY2025 annual, consistent with continued growth into H1 2026); FY2025 net margin (1,596.9/7,145.8 = 22.35%) matches the TTM net-margin ratio field (22.25%) to within 0.1pp — confirms internal consistency, no distortion found.

### 3.2 Cash flow — Yahoo Finance `fundamentals-timeseries` (EUR, annual)

| Fiscal Year | Operating Cash Flow | Free Cash Flow | Net Income | FCF/NI |
|---|---|---|---|---|
| FY2022 | €1,403.3M | €598.7M | €932.6M | 64.19% |
| FY2023 | €1,716.6M | €847.7M | €1,252.0M | 67.71% |
| FY2024 | €1,926.7M | €937.5M | €1,521.9M | 61.60% |
| FY2025 | €2,349.3M | €1,406.1M | €1,596.9M | 88.06% |

**TTM (Yahoo `financialData`, self-consistent basis):** FCF $1,001.98M, Net Income (`netIncomeToCommon`) $1,636.12M → **TTM FCF/NI = 61.27%.**

**FCF positive every year shown** (FY2022–FY2025, 4 consecutive years) — clears the "FCF-positive 3+ consecutive years" hard disqualifier comfortably.

**FCF/NI rolling-window check (most recently completed 2 fiscal years, per quality-scoring.md's rolling-window clarification):** FY2024 61.60%, FY2025 88.06% — only **one** of the two most recent years is below 70%, so the "<70% for 2+ consecutive years" hard disqualifier does **not** fire. Flagged: the TTM figure (61.27%) sits closer to FY2024's weaker reading than FY2025's — worth watching at the next earnings re-score (§9).

### 3.3 Balance sheet — Yahoo Finance `fundamentals-timeseries` (EUR, annual)

| Item | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Total Debt | €2,811.8M | €2,477.2M | €3,351.9M | €2,884.2M |
| Cash & Equivalents | €1,388.9M | €1,122.0M | €1,742.2M | €1,467.7M |
| Total Equity (incl. minority) | €2,602.5M | €3,070.6M | €3,543.2M | €3,914.7M |
| Invested Capital (Yahoo-computed) | €5,347.2M | €5,465.0M | €6,759.6M | €6,629.0M |
| EBITDA | €1,749.5M | €2,293.9M | €2,595.8M | €2,766.7M |
| Interest Expense | €25.5M | €29.3M | €40.1M | €41.2M |

**Net Debt/EBITDA (FY2025):**
```
Net Debt = €2,884.2M − €1,467.7M = €1,416.5M
Net Debt/EBITDA = €1,416.5M / €2,766.7M = 0.512×
```
Well clear of the 2.5× standard threshold — no hard disqualifier. Note: Ferrari's balance sheet includes Ferrari Financial Services' captive dealer/customer-financing debt on a consolidated basis (Yahoo's `totalDebt` timeseries is the consolidated GAAP/IFRS figure) — consistent with the Conglomerate rule's intent, no separate carve-out needed. Ferrari is **not** treated under the Upgrade 5 asset-light override (6× denominator) — its debt is not 100% financial-only in the payment-network/exchange sense; the standard 4× denominator is used.

**Interest coverage** = EBIT / Interest Expense = €2,104.8M / €41.2M = **51.1×** — far above the 15× asset-light-override threshold, noted for completeness even though the override doesn't apply here.

### 3.4 Growth & moat evidence — cited sources

- **Unit deliveries vs. revenue (pricing-power evidence):** Ferrari's FY2025 shipments totaled **13,640 units, down ~1% YoY**, while FY2025 revenue grew **+7% reported / +8% constant-currency** to €7.1B and EBIT grew **+12%** to €2,110M (29.5% margin, +120bps YoY) — revenue and profit growing while unit volume *declined*, driven by mix/personalization, not volume. ([Ferrari FY2025 results](https://www.ferrari.com/en-EN/corporate/articles/2025-full-year-and-fourth-quarter-financial-results), [Investing.com FY2025 slides recap](https://www.investing.com/news/company-news/ferrari-fy-2025-slides-revenue-hits-71b-as-new-models-drive-growth-93CH-4497359))
- **Order book / backlog:** as of Q2 2026, Ferrari's order book covers all of **2027** (extended from covering "through 2026" a year prior) — a lengthening, not shrinking, backlog; Q2 2026 EBIT grew 9.5% YoY "on favorable product mix and stronger-than-expected demand for personalization" despite shipment softness. ([Motor1](https://www.motor1.com/news/749639/ferrari-sold-out-through-2026/), [Seeking Alpha](https://seekingalpha.com/news/3956517-ferrari-stock-rises-on-signal-of-strong-sales-backlog))
- **Category share:** Ferrari states it held **24% of the global Luxury Performance Car segment** (2-door, >500hp, >€200k luxury sports cars) in 2025 — a category it, Lamborghini, Aston Martin, McLaren, Porsche, and others compete in; Ferrari's brand value rose **43% to $10.6B in 2024**, rated AAA+ as the world's strongest automotive brand. ([Ferrari FY2025 results](https://www.ferrari.com/en-EN/corporate/articles/2025-full-year-and-fourth-quarter-financial-results))
- **Client-loyalty allocation system (switching-cost mechanism):** Ferrari's allocation of its most sought-after/limited-edition models is explicitly relationship-based — **84% of 2025 new-car sales went to existing Ferrari owners, and 56% to buyers who already owned more than one Ferrari.** Priority is built over years of ownership, factory-event participation, and dealer relationship history, not first-come-first-served — a documented mechanism that raises the cost of "switching away" for a collector who wants future access to limited runs. ([The Fashion Law](https://www.thefashionlaw.com/what-ferraris-luce-denial-reveals-about-luxurys-allocation-economy/), [Exotics Hunter](https://www.exoticshunter.com/exotic-car-blog/how-ferrari-allocation-actually-works-and-how-to-position/))

### 3.5 Moat signal evidence

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | 24% of the global Luxury Performance Car segment (2025, self-reported, §3.4) — a commanding, multi-year #1-or-#2 position in its category; no evidence of share erosion found. |
| Brand premium | **TRUE** | FY2025 revenue +7% and EBIT +12% on unit shipments *down* ~1% (§3.4) — the textbook "price/mix increase without volume gain" signal; brand value +43% to $10.6B (2024), AAA+ rated. |
| Network effect | **FALSE** | No two-sided-marketplace or user-growth-driven-value mechanism — Ferrari is a manufacturer, not a platform business. Not applicable. |
| Switching costs | **TRUE** | Documented, relationship-based allocation system: 84% of 2025 sales to existing owners, 56% to repeat multi-Ferrari owners (§3.4) — a genuine lock-in mechanism specific to how Ferrari rations its most desirable models. |
| Scale cost advantage | **FALSE** | No cited cost-per-unit data vs. a named competitor found. Ferrari's model is the opposite of scale economics — it deliberately caps production to preserve scarcity/pricing power (already credited above), not to achieve a cost advantage. |

```
Moat_Score = (3/5) × 100 = 60.0
```

---

## 4. Phase 01 — Quality Score (2026-06-29 methodology)

### 4.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years without a documented growth-capex explanation | FY2024 61.60% / FY2025 88.06% (the two most recently completed fiscal years) — only 1 of 2 below 70% | disqualify if 2+ consecutive years sub-70% | ✅ **PASS** |
| Net Debt/EBITDA over its applicable threshold (2.5× standard) | **0.512×** | disqualify if >2.5× | ✅ **PASS**, clean |
| FCF-positive 3+ consecutive years | Positive every year FY2022–FY2025 (4 consecutive years) | disqualify if not | ✅ **PASS**, clean |

**No hard disqualifier fires.**

### 4.2 Profitability (25% weight)

```
Net Margin (TTM) = 22.25%  (Yahoo financialData.profitMargins)
NetMargin_Component = clamp((22.25/30)×100, 0, 100) = 74.17
```

**ROIC:**
```
Effective tax rate (FY2025) = €464.1M / €2,063.6M = 22.49%
NOPAT (FY2025) = EBIT × (1 − 0.2249) = €2,104.8M × 0.7751 = €1,631.4M
Average Invested Capital (FY2024–FY2025) = (€6,759.6M + €6,629.0M) / 2 = €6,694.3M
ROIC = €1,631.4M / €6,694.3M = 24.37%
ROIC_Component = clamp((24.37/30)×100, 0, 100) = 81.23
```

```
Profitability_Score = (74.17 + 81.23) / 2 = 77.70   (no FCF-positivity cap — clean 4yr positive FCF, §3.2)
```

### 4.3 Margins (15% weight)

```
Gross Margin (TTM) = 51.62%  (Yahoo financialData.grossMargins)
GrossMargin_Score = clamp((51.62/80)×100, 0, 100) = 64.53
```
**No +10 structural-trend bonus:** gross margin is already well above the 40% threshold (48.0% FY2022 → 49.8% FY2023 → 50.1% FY2024 → 51.7% FY2025, trending up) — the bonus is explicitly reserved for a margin *below* 40% that's structurally improving, which doesn't apply here.

`Margins_Score = 64.53`

### 4.4 Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 €5,095.3M → FY2025 €7,145.8M) = (7,145.8/5,095.3)^(1/3) − 1 = 11.94%
Growth_Score (raw) = clamp((11.94/25)×100, 0, 100) = 47.75
```
**TAM/pricing-power modifier (+10):** documented, cited evidence (§3.4) — FY2025 revenue grew +7% and EBIT +12% while unit shipments *fell* ~1%, and the order book lengthened to cover all of 2027 (from 2026 a year earlier). This is squarely the "documented evidence of TAM expansion and/or pricing power" this modifier is meant to capture — growth driven by price/mix/personalization, not volume, with a growing (not shrinking) demand backlog.

**No −10 deceleration modifier, despite a visibly decelerating YoY revenue-growth trend (17.2% FY2023 → 11.8% FY2024 → 7.0% FY2025):** the deceleration is explained by Ferrari's own deliberate, self-imposed unit-shipment cap (a supply-side scarcity strategy, not demand weakness) — corroborated by the lengthening (not shrinking) order book. Not treated as "structural" growth-thesis erosion.

```
Growth_Score = 47.75 + 10 = 57.75
```

### 4.5 Balance Sheet (15% weight)

```
Net Debt/EBITDA = 0.512×   (§3.3)
BalanceSheet_Score = clamp(100 × (1 − 0.512/4), 0, 100) = 87.20
```
`BalanceSheet_Score = 87.20`

### 4.6 Moat Signal (15% weight)

Per §3.5: 3 of 5 signals TRUE (Market share, Brand premium, Switching costs).
```
Moat_Score = (3/5) × 100 = 60.0
```

### 4.7 FCF Quality (10% weight)

```
TTM FCF/NI = $1,001.98M / $1,636.12M = 61.27%
FCFQuality_Score = clamp(((0.6127 − 0.40)/0.60)×100, 0, 100) = 35.45
```
`FCFQuality_Score = 35.45` — flagged: this TTM figure is weaker than FY2025's own audited annual ratio (88.06%, §3.2); the discrepancy is carried into the sensitivity check below rather than silently resolved.

### 4.8 Quality Score — final calculation

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

              = (77.70 × 0.25) + (64.53 × 0.15) + (57.75 × 0.20)
              + (87.20 × 0.15) + (60.0 × 0.15) + (35.45 × 0.10)

              = 19.425 + 9.6795 + 11.55 + 13.08 + 9.00 + 3.545

              = 66.28
```

### 4.9 Gate result: **FAIL — 66.3 < 80.0** (13.7 points short)

**Sensitivity check — is this close under any plausible generous reading?** Closer than most recent misses, but still a fail. Stacking every individually-defensible generous assumption simultaneously:
- Moat_Score generously credited 5-of-5 (100.0 instead of 60.0): +6.0
- FCFQuality_Score using FY2025's own audited annual ratio (88.06%) instead of the weaker TTM figure (61.27%): +4.47

Even summing both: 66.28 + 6.0 + 4.47 = **76.75 — still 3.25 points below the 80.0 gate.** No combination of defensible generous readings closes the remaining gap. **This session stops here per the command specification: no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.** Ferrari does not clear the 80.0+ Quality Score gate.

---

## 5. Why this reads as a genuine (structural) miss, not a framework gap

RACE is a genuinely high-quality business by conventional standards — strong ROIC (24.4%), a healthy, low-leverage balance sheet (0.51× Net Debt/EBITDA), real documented pricing power, and a moat resting on genuine scarcity/relationship dynamics (3 of 5 signals). What keeps it under this framework's strict 80.0+ bar:

1. **FCF Quality (35.45/100, 10% weight)** — the single biggest drag. TTM FCF/NI conversion (61.27%) is meaningfully weaker than FY2025's own audited 88.06%, likely reflecting capex/working-capital timing tied to the F80/Elettrica model changeover described in Ferrari's own results commentary — not disqualifying on its own (§4.1), but a real drag on the continuous score.
2. **Margins (64.53/100, 15% weight)** — a genuinely strong 51.6% gross margin by normal standards, but this framework's Margins sub-score is calibrated with 80% as its ceiling (software/platform economics); a manufacturer of physical luxury goods, however well-run, structurally cannot approach that ceiling.
3. **Growth (57.75/100, 20% weight)** — even after the +10 pricing-power credit, an 11.9% 3yr revenue CAGR sits well short of this sub-score's 25% ceiling; Ferrari's own deliberate volume discipline caps how fast reported revenue can grow, regardless of demand strength.

This is the same pattern this framework has now documented for several genuinely strong, real-economy businesses whose structural profile (physical goods, capital-intensive, deliberately volume-capped) doesn't fit a scoring scale calibrated primarily around software/platform/asset-light compounders — not a framework limitation requiring a fix, flagged per the quality-scoring.md instruction to note (not silently patch) cases like this.

---

## 6. Recommendation: **PASS (no entry) — Quality Gate FAIL at 66.3 (need 80.0+)**

**Do not enter RACE this session.** The Quality Score of 66.3 is 13.7 points below the strict 80.0+ gate — even the most generous defensible sensitivity reading (§4.9) only reaches 76.75, still short. **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed**, consistent with the command specification's instruction to stop at the Quality Gate.

The triggering Telegram post (a one-off EV-auction news item, with an uncorroborated "shares fell 10%" claim) was used only as the reason to run this first-ever evaluation and was not relied upon for any figure or conclusion above.

---

## 7. Informational only — legacy 8-criterion Phase 01 screen

Not the binding gate (the graded Quality Score above supersedes it) — shown for template completeness per operating-calendar.md's New Position Evaluation data structure. Market cap and EV use today's live price ($421.01 × 175,764,832 shares) — informational only, not scored inputs.

| Criterion | Threshold | RACE (TTM) | Pass? |
|---|---|---|---|
| Gross margin | >40% | 51.62% | ✅ |
| Net margin | >12% | 22.25% | ✅ |
| ROIC | >15% | 24.37% | ✅ |
| Revenue growth (3yr CAGR) | >8% | 11.94% | ✅ |
| FCF positive 3 consecutive years | required | Yes (4 consecutive) | ✅ |
| Net debt/EBITDA | <2.5× | 0.512× | ✅ |
| FCF yield | >4% | 1.35% (FCF $1,002.0M / Mkt Cap $74,013.6M) | ❌ |
| EV/EBIT | <20× | ~32.9× (EV $75,747.5M / EBIT ~$2,283.9M, TTM-margin-implied) | ❌ |

```
Market Cap = 175,764,832 × $421.01 = $74,013.6M
EV = Market Cap + Total Debt (TTM, $3,165.6M) − Cash (TTM, $1,431.5M) = $75,747.5M
EBIT (TTM, margin-implied) = Revenue TTM ($7,353.3M) × operatingMargins (31.065%) = $2,283.9M
```

6 of 8 pass — the legacy screen alone would have passed RACE; it's the graded Quality Score's FCF-quality and margin-ceiling calibration (§5) that catches what the binary screen would have missed. This is exactly the kind of case the 2026-06-29 move from binary screen to graded score was intended to catch.

---

## 8. Next Review Trigger

No routine numeric re-check is scheduled (Phase 01 FAILs don't carry a numeric score to go stale — per watchlist/README.md). A future re-look is warranted on:
- **RACE's next earnings release** (Ferrari typically reports late Jan/early Feb for FY and quarterly thereafter) — the freshest data would clarify whether the TTM FCF/NI weakness (§4.7) persists or was a one-off capex/working-capital timing item tied to the F80/Elettrica changeover.
- A **sustained improvement in FCF/NI conversion** back toward FY2025's own 88% level, which alone would move the Quality Score meaningfully closer to (though still short of, per §4.9) the 80.0 gate.
- Standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move.

Absent any of the above, a future Telegram mention of RACE should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 9. Data Gaps Flagged

1. **`yfinance` Python client failed this session** with a `curl_cffi` TLS/connection-reset error against the outbound proxy — worked around by calling the same underlying Yahoo Finance REST endpoints directly via `curl` (§2). This is a tooling note, not a data gap in any scored input; every figure used was pulled from the same source the framework's documented methodology already relies on.
2. **FCF/NI conversion — TTM vs. FY2025 discrepancy (§4.7, §4.9):** TTM (61.27%) is notably weaker than FY2025's own audited annual figure (88.06%). This session used the TTM figure as the primary continuous-score input (consistent with using TTM elsewhere for margins/ROIC) and flagged the FY2025 figure as a sensitivity check rather than silently picking whichever reading was more favorable — not outcome-determinative either way (§4.9), but worth confirming at the next earnings re-score whether this is capex-timing noise or a genuine deterioration.
3. **Moat signal citations** (§3.4, §3.5) are sourced from this session's web search of recent (2025–2026) company results releases and secondary reporting, not from a primary SEC/AFM filing pull (Ferrari files a 20-F-equivalent Annual Report with the Dutch AFM, not a 10-K) — flagged as a slightly lower-tier source than the SEC-XBRL-first standard used for US domestic filers in prior sessions, though every citation used is a specific, dated, named-source claim rather than an invented one.

None of these gaps is silently patched around — each is the explicit reason for a flagged caveat rather than an invented number, and §4.9's sensitivity check shows none of them are outcome-determinative for the gate result.

---

## 10. Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used throughout this session's Balance Sheet and Profitability sub-scores. |
| **Effective tax rate** | The actual share of pretax income paid as tax in a period — 22.49% for RACE's FY2025 (§4.2), used to convert EBIT into NOPAT for the ROIC calculation. |
| **FCF (Free Cash Flow) / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check). RACE's FCF/NI ratio ran 61–88% across FY2022–FY2025 (§3.2, §4.7) — the framework's single biggest drag on this session's Quality Score. |
| **Hard disqualifier** | One of three Quality Score conditions ([quality-scoring.md](../framework/quality-scoring.md)) that fails a company regardless of its weighted sub-score total. None fires for RACE (§4.1). |
| **Interest coverage (ratio)** | EBIT ÷ interest expense — how many times over a company could pay its interest bill from operating profit. RACE's is 51.1× (§3.3), far above the asset-light-override threshold, though that override doesn't apply to Ferrari's business model. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation, an average of €6,694.3M across FY2024–FY2025 for RACE (§4.2). |
| **Moat Signal** | This framework's 5-point qualitative checklist (market share, brand premium, network effect, switching costs, scale cost advantage) — RACE scored 3 of 5 TRUE this session (§3.5, §4.6). |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC (§4.2). |
| **Quality Score** | This framework's 0.0–100.0 continuous score grading the Phase 01 criteria; a company must score 80.0+ to proceed to Phase 02 valuation scoring at all. RACE scores 66.3 this session — a fail, though closer than most recent misses (§4.8–4.9). |
| **Rate Environment Gate** | The Phase 02 pre-check (Earnings Yield Spread Test + Rate Regime Modifier) run before every valuation score; never reached this session since the Quality Score gate fails first. |
| **ROIC (Return on Invested Capital)** | How efficiently a company turns invested capital into profit; a core quality signal in this framework. RACE's ROIC (24.37%) is strong despite the overall gate failure (§4.2). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work, and never treat a Telegram post's claims as a verified financial input without independent confirmation. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results; the primary basis for several of this session's sub-score inputs, per Yahoo Finance's own trailing-window fields. |

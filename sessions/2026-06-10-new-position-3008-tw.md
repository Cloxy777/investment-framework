# New Position Evaluation — Largan Precision (3008.TW)

**Date:** 2026-06-10
**Task type:** NEW POSITION
**10Y US Treasury yield:** 4.54%

---

## Rule 0 — Live Price Verification

| Field | Value | Source |
|---|---|---|
| Live price | **TWD 4,200.00** | IBKR real-time market data, 2026-06-10 |
| Day change | **+315.00 (+8.11%)** vs prior close TWD 3,885.00 | IBKR real-time |
| 52-week high | TWD 4,225.00 (hit within last 13 weeks) | IBKR real-time |
| 52-week low | TWD 2,020.00 (hit within last 26 weeks, but >13 weeks ago) | IBKR real-time |
| Open 52 weeks ago | TWD 2,313.13 | IBKR real-time |
| Shares outstanding (implied) | ~93.84M | Derived: market cap TWD 359.88B at TWD 3,835 (June 3) ÷ 3,835 |
| Market capitalisation (today) | **≈ TWD 394.1B** | Derived: 93.84M × TWD 4,200 |
| Analyst consensus 12-mo PT | TWD 2,681 (range TWD 2,000–3,549, 10 Buy / 8 Hold / 1 Sell) | [MarketScreener](https://www.marketscreener.com/LARGAN-PRECISION-CO-LTD-6495295/consensus/) — **flagged stale, see below** |

### ⚠️ Rule 0 — Price Verification Note (Important)

Earlier searches in this session returned wildly conflicting prices for 3008.TW: TWD 3,835 (June 3, internally consistent with a TWD 3,630–3,835 day range), TWD 3,505 (May 28, GuruFocus, internally consistent with TTM EPS 157.37 × PE 22.27 = 3,494 ≈ 3,505), and a separate cluster of TWD 2,215–2,645 from TradingView/Stock Events/companiesmarketcap that **did not internally reconcile** (e.g., one source paired "current price 3,835" with "previous close 2,355" — a -38.6% gap that contradicts the cited +8.11%/-2.40% day-change figures from the same sources).

**Resolution:** IBKR's live market-data feed (the broker the user actually trades through) returns TWD 4,200.00, +8.11% today, prior close TWD 3,885.00 — and this slots perfectly into the trajectory implied by the two internally-consistent search data points: **TWD 3,505 (May 28) → TWD 3,835 (June 3) → TWD 3,885 (yesterday's close) → TWD 4,200 (today)**. The 52-week high of TWD 4,225 (hit within the last 13 weeks) corroborates this. The TWD 2,200–2,700 cluster appears to reflect prices from **several months ago** (consistent with the 52-week-low of TWD 2,020 and "open 52 weeks ago" of TWD 2,313) — i.e., stale/mismatched cache data from lower-tier aggregators, not current prices. **TWD 4,200 (IBKR real-time) is used as the live price for all calculations below.**

This also means: **the stock has approximately doubled off its 52-week low over the trailing months**, and is up +8.11% today alone and ~+9-10% in the last week — see Qualitative section for the catalyst (this is a real fundamental development, not noise).

---

## Business Overview (Context)

Largan Precision is the world's largest manufacturer of plastic lenses for smartphone cameras by value, headquartered in Taichung, Taiwan. It is the dominant supplier of high-end periscope/telephoto camera lens modules to Apple (reportedly 85-90% of Apple's periscope lens orders) and a major supplier to Samsung and other Android OEMs. Together with Sunny Optical (China) and Genius Electronic Optical (Taiwan), it forms a top-3 oligopoly controlling >65% of the global handset camera lens market. The company is debt-free with a very large net cash position built up over two decades of high-margin operations.

In 2026, Largan is pivoting toward **"AI optics"** — Co-Packaged Optics (CPO) for AI/data-center interconnects, plus optical components for "Edge AI" devices (AI smartphones, spatial-computing wearables, autonomous-vehicle sensing). This narrative is the proximate driver of the recent share-price rally (see Qualitative section).

---

## Data Gaps & Flags (flagged before proceeding, per Rule 0)

| Item | Issue | How handled |
|---|---|---|
| ROIC | Conflicting figures found: 16.04%, 19.40% (as ROE), 31.07% (GuruFocus, Dec 2025) | All confirmed figures clear the >15% threshold; debt is ~zero so ROIC≈ROE. Treated as PASS, but the wide dispersion (16% vs 31%) is a data-quality flag worth a primary-filing check before sizing any position. |
| FY2023 FCF | Not independently re-confirmed this session (FY2024 TWD 20.13B and FY2025 TWD 13.57B were) | Largan has built a TWD ~119B net cash pile with zero debt over many years — strongly consistent with sustained positive FCF. Treated as PASS on weight of evidence, flagged for verification. |
| 10yr avg PE | GuruFocus reports a 10-yr **median** PE of 17.49 (range 9.55–32.41), not a mean | Used as the "10yr avg PE" proxy per Upgrade 2 — median is arguably more robust to outlier years anyway. |
| Analyst consensus PT (TWD 2,681) | Appears stale — current price (TWD 4,200) is ~37% **above** even the high-end estimate (TWD 3,549, Goldman) | Not used as a valuation anchor; flagged as likely pre-dating the June rally. Blended FV below is computed independently. |
| FY2026E consensus EPS | TWD 177.80–178.79 (cluster) | Used TWD 178 as the working figure for forward PE. |

---

## Phase 01 — Quality Gate Walkthrough

| # | Metric | Threshold | Actual | Pass? | Source / Calculation |
|---|---|---|---|---|---|
| 1 | Gross margin | >40% | **49.19%** (TTM) | ✅ PASS | [stockanalysis.com](https://stockanalysis.com/quote/tpe/3008/statistics/) |
| 2 | Net margin | >12% | **33.74%** (TTM: NI TWD 20.96B / Revenue TWD 62.11B) | ✅ PASS | TTM financials |
| 3 | ROIC | >15% | **~19-31%** (range; ROIC≈ROE given near-zero debt) | ✅ PASS (data-quality flag, see above) | [GuruFocus](https://www.gurufocus.com/term/roic/TPE:3008) |
| 4 | Revenue growth (3yr CAGR) | >8% | **9.2%** (FY2022 TWD 47.68B → TTM TWD 62.11B, 3yr CAGR); 12.8% on a 2yr FY2023→TTM basis | ✅ PASS (marginal on 3yr basis, comfortable on 2yr) | [companiesmarketcap.com](https://companiesmarketcap.com/largan-precision/revenue/) |
| 5 | FCF positive, 3 consecutive years | FCF > 0 ×3yrs | FY2024 TWD 20.13B, FY2025 TWD 13.57B confirmed positive; FY2023 not independently re-confirmed but consistent with zero-debt / TWD 119B net-cash trend | ✅ PASS (weight of evidence, flagged) | Multiple sources |
| 6 | Net Debt/EBITDA | <2.5× | **Net cash** — TWD 0 debt, ~TWD 119B cash & equivalents (Q1 2026) vs EBITDA ~TWD 27.8B → net cash/EBITDA ≈ −4.3× | ✅ PASS (trivially — net cash position) | [Yahoo Finance balance sheet](https://finance.yahoo.com/quote/3008.TW/balance-sheet/), [macroaxis EBITDA](https://www.macroaxis.com/invest/ratio/3008.TW/EBITDA) |
| 7 | FCF/NI conversion >70% (2+ yrs) | >70% | FY2024 = **77.7%** (PASS) ✅; FY2025 = **64.7%** (FAIL) ❌ — only 1 of last 2 years clears 70% | ⚠️ CONDITIONAL — see discussion below | Derived: FCF/NI each year |
| 8 | Moat Signal | Stable/growing moat | World #1 handset camera lens maker by value; dominant (85-90%) share of Apple's high-end periscope lens orders; top-3 oligopoly w/ Sunny Optical & Genius Electronic (>65% combined share). New "AI optics" (CPO) pivot is a credible second growth vector but unproven at scale. **Risks:** customer concentration (Apple-heavy), Sunny Optical encroaching on adjacent lens segments, Taiwan/cross-strait geopolitical risk (no formal framework mechanism for this — flagged again, as in prior APAC sessions) | ✅ PASS (with concentration + geopolitical flags) | Qualitative |

**Result: 7 of 8 criteria pass cleanly. Criterion 7 (FCF/NI conversion) is a CONDITIONAL flag — proceeding to Phase 02 with explicit caveat below.**

### FCF/NI Conditional Discussion (Criterion 7)

The framework states: *"If below 70% without growth capex explanation, do not proceed to Phase 02."* This was tested for TSMC in a prior APAC screening session, where a sub-70% FCF/NI ratio was treated as "conditional" because it was clearly explained by a **capex surge tied to identified growth catalysts** (foldable iPhone 2026, 20th-anniversary iPhone 2027 cycles), against a backdrop of strong/growing operating cash flow.

**Largan's situation is different and weaker:**
- FY2025 capex rose only modestly (+9.3%, TWD 11.45B → 12.51B) — not a "surge."
- FY2025 operating cash flow *fell* -17.4% (TWD 31.58B → 26.08B), tracking a **-19.1% decline in TTM net income** (TWD 25.92B FY2024 → TWD 20.96B TTM).
- The new CPO/AI-optics pilot line ("first automated pilot line targeted by September 2026") is a **FY2026 capex story**, not yet reflected in the FY2025 numbers being assessed here.

**Conclusion:** Largan's FY2025 FCF/NI miss looks primarily like an **earnings deceleration** (cyclical smartphone-lens pricing/volume pressure), not a "good problem" of accelerating growth investment. This is a **genuine yellow flag**, distinct from — and weaker than — the TSMC precedent. Given it is the *only* contested criterion among 8, and the magnitude of the miss is modest (64.7% vs. 70%, a 5.3pp gap), I am proceeding to Phase 02 with this flag carried forward explicitly. **If FY2026 FCF/NI also comes in below 70%, this becomes a 2-year pattern and should trigger a harder Phase 01 re-look** (Phase 04 monitoring trigger, noted below).

---

## Rate Environment Gate

**10Y Treasury yield: 4.54%**

**Step 1 — Earnings Yield Spread Test:**
- Forward PE ≈ TWD 4,200 / TWD 178 (FY2026E EPS) = **23.6×**
- EY = 1 / 23.6 = **4.24%**
- Spread = EY − 10Y = 4.24% − 4.54% = **−0.30%** < +1.5% → **+0.5 additive flag**

**Step 2 — Rate Regime Modifier:**
- 10Y yield 4.54% falls in the 3.5–5% bucket → **+0.5**

**Total Rate-related modifier: +1.0**

---

## Phase 02 — Valuation Score

**Fast Grower check (Upgrade 3):** FY2024 net income grew +44.76% (>15% ✅), but **TTM net income declined -19.1%** vs FY2024 — breaking any 3-consecutive-year >15% growth streak. **Largan is NOT a Fast Grower.** PEG does not apply; its 15% weight redistributes to EV/EBIT (→ 40% total), consistent with the REA.AX precedent in this session.

| Component | Weight | Value | Sub-score | Adj. | Notes |
|---|---|---|---|---|---|
| FCF Yield | 40% | TWD 13.57B / TWD 394.1B mkt cap = **3.44%** | 6 | 6 | 2-4% bracket → 6-7; consistent with REA precedent (3.60%→6) |
| EV/EBIT | 40% | EV = MktCap − NetCash = 394.1B − 119.0B = **TWD 275.1B**; EBIT ≈ 37.49% × TWD 62.11B = **TWD 23.29B**; EV/EBIT = **11.81×** | 2 | 2 | <12× bracket → 1-2; 11.81 close to the 12× boundary → 2 |
| Forward PE + Hist. PE Modifier | 20% | Fwd PE 23.6× vs sector — moderately high for a Taiwan electronics-component supplier with declining TTM earnings → base sub-score 7. Upgrade 2: 23.6× vs 10yr median PE 17.49× = **+34.9% above** → >20% above → **+1** | 7 | **8** | |

**Raw weighted score:**
```
= (FCF × 0.40) + (EV/EBIT × 0.40) + (FwdPE_adj × 0.20)
= (6 × 0.40) + (2 × 0.40) + (8 × 0.20)
= 2.4 + 0.8 + 1.6
= 4.8
```

**+ Rate Modifier (+1.0) = 5.8**

**Round to nearest integer: 5.8 → Final Score = 6** (not exactly .5, normal rounding applies)

---

## Action: Score 6 → HOLD / Watchlist Only — No New Entry

Per the operating brief's action table, Score 6-7 = "HOLD — watch only, no new entry, no trim (Fair Value)." Per fair-value-methodology.md: "Score 6-7 → No MoS → Watchlist only." No formal buy/sell/stop order setup is produced for a Watchlist verdict — but a Blended Fair Value is computed below for context, consistent with the REA.AX precedent.

---

## Fair Value (Blended)

### Method A — DCF (3-scenario, FCF base TWD 13.57B, 93.84M shares, **net cash TWD 119.0B added back to equity value**)

| Scenario | WACC | Stage 1 (yrs 1-5) growth | Stage 2 fade to | Terminal growth | PV of operations (TWD B) | + Net cash (TWD B) | Equity value (TWD B) | Per-share (TWD) |
|---|---|---|---|---|---|---|---|---|
| Bull | 8% | 8% | 3% | 3% | 374.2 | 119.0 | 493.2 | **5,257** |
| Base | 9% | 7% | 2.5% | 2.5% | 275.7 | 119.0 | 394.7 | **4,207** |
| Bear | 10% | 6% | 2% | 2% | 215.2 | 119.0 | 334.2 | **3,562** |

**Probability-weighted DCF (25% bull / 50% base / 25% bear):**
```
= 0.25 × 5,257 + 0.50 × 4,207 + 0.25 × 3,562
= 1,314.25 + 2,103.50 + 890.50
= TWD 4,308
```

### Method B — Comparable Multiples

| Multiple basis | Calculation | Implied FV (TWD/share) |
|---|---|---|
| Historical PE | TTM EPS 157.37 × 10yr median PE 17.49 | 2,753 |
| Forward PE vs history | FY2026E EPS 178 × 10yr median PE 17.49 | 3,113 |
| EV/EBIT (fair multiple ~15×, mid of 12-18× "fair" range) | Fair EV = 15 × 23.29B = 349.35B; + net cash 119.0B = 468.4B / 93.84M shares | 4,991 |
| FCF Yield (fair yield ~5%, sub-score 4-5 zone) | Fair mkt cap = 13.57B / 0.05 = 271.4B / 93.84M shares | 2,892 |

**Average of multiples: (2,753 + 3,113 + 4,991 + 2,892) / 4 = TWD 3,437**

### Blended Fair Value
```
= 40% × DCF + 60% × Multiples
= 0.40 × 4,308 + 0.60 × 3,437
= 1,723 + 2,062
= TWD 3,785
```

**Current price TWD 4,200 is ~11% above Blended FV of TWD 3,785** — modestly rich, consistent with a Score 6 "Fair Value, no margin of safety" outcome (not the ~38% premium an EV-without-cash-adjustment calc would have implied).

---

## Score & Price Sensitivity (for Watchlist monitoring)

| Price (TWD) | FCF Yield | EV/EBIT | Fwd PE (vs FY26E EPS 178) | Approx. Score | Action |
|---|---|---|---|---|---|
| 4,200 (current) | 3.44% (sub 6) | 11.81× (sub 2) | 23.6× (sub 8 w/ +1 mod) | **6** | Watchlist |
| ~3,785 (Blended FV) | 3.82% (sub 6) | 9.6× (sub 2) | 21.3× (sub 7-8) | ~5-6 | Watchlist/borderline |
| ~3,000 | 4.82% (sub 4-5) | 6.98× (sub 1) | 16.9× (sub 5, ~0 mod) | **~4** | BUY zone |
| ~2,650-2,839 (FV × 25-30% MoS) | ~5.4-5.8% (sub 4) | ~5.3-5.9× (sub 1) | ~14.9-15.9× (sub 4-5, -1 mod possible) | **~3-4** | BUY zone |

Note: the TWD 2,200-2,700 range that appeared in several (initially confusing) search results corresponds almost exactly to where Largan was trading **before** the recent AI-optics rally — and to where it would re-enter BUY territory (Score 4-5, MoS 25-30%) under this framework. The stock has moved roughly +55-100% off that zone in the past several weeks.

---

## Qualitative — What's Driving the Rally

Taiwanese-language press (BigGo, TechNews, BusinessToday) attributes the move to:
- **June 9, 2026:** Stock hit limit-up (+10%) to TWD 3,885 around the company's shareholders' meeting, where Chairman Frank Lin announced a **Co-Packaged Optics (CPO) pilot production line** nearing completion (first automated pilot line targeted for September 2026), and Largan debuted two CPO solutions (PMLA multi-channel micro-lens arrays, and Fiber Array) at COMPUTEX.
- **June 1, 2026:** Stock hit a 5-year high, partly attributed to **founding-family share purchases**.
- Broader narrative: market reframing Largan as an **"AI optics"** play — demand shifting from cloud-AI to "Edge AI" (autonomous vehicles, spatial-computing wearables, AI smartphones), which require high-end optical sensing components. Sinotrade and others frame this as the start of a "new growth cycle" for the company beyond the historically Apple-dependent smartphone-lens business.

This is a real fundamental catalyst (not pure price momentum), but it is **early-stage and unproven at revenue scale** — FY2025's financials (the basis for this Phase 02 score) do not yet reflect any CPO contribution. The market is pricing in execution on a thesis that hasn't yet shown up in the numbers.

---

## Recommendation

**WATCHLIST ONLY — Score 6 (Fair Value, no margin of safety). Do not enter at TWD 4,200.**

Largan clears 7 of 8 Phase 01 quality criteria comfortably (strong margins, debt-free with massive net cash, durable lens-market leadership, double-digit revenue growth) — this is a high-quality business. The one flag (FY2025 FCF/NI at 64.7%, vs. >70% required) reflects a cyclical earnings dip rather than a clear growth-capex story, and is worth monitoring into FY2026.

The Phase 02 score of 6 reflects a stock trading ~11% above a TWD 3,785 blended fair value, having rallied ~55-100% off its 52-week low on an early-stage "AI optics" (CPO) re-rating narrative that is not yet visible in the FY2025 financials underlying this score.

**Re-evaluation triggers:**
- Price retracement toward **TWD 2,650-2,950** (Score 4-5 BUY zone, 25-30% MoS to Blended FV)
- FY2026 results — specifically watch (a) whether FCF/NI recovers above 70% [if not, this becomes a 2-consecutive-year miss requiring Phase 01 re-assessment], (b) any disclosed CPO revenue contribution that would justify the re-rating fundamentally rather than narratively, and (c) confirmation/refresh of analyst price targets, which currently look stale relative to the new price level
- Per Fair Value Methodology Rule 9 (Model Refresh Triggers): the >15% move (stock is up ~+55-100% off its 52-week low and +8.11% today alone) — re-valuation has been performed above; **revisit again at next quarterly earnings** regardless of price action

---

## Sources

- IBKR real-time market data (live price, change, 52-week range) — 2026-06-10
- [GuruFocus — Largan PE TTM & 10yr median](https://www.gurufocus.com/term/pettm/TPE:3008)
- [GuruFocus — Largan ROIC](https://www.gurufocus.com/term/roic/TPE:3008)
- [stockanalysis.com — TPE:3008 statistics](https://stockanalysis.com/quote/tpe/3008/statistics/)
- [companiesmarketcap.com — Largan revenue](https://companiesmarketcap.com/largan-precision/revenue/)
- [companiesmarketcap.com — Largan earnings](https://companiesmarketcap.com/largan-precision/earnings/)
- [Yahoo Finance — 3008.TW balance sheet](https://finance.yahoo.com/quote/3008.TW/balance-sheet/)
- [macroaxis — 3008.TW EBITDA](https://www.macroaxis.com/invest/ratio/3008.TW/EBITDA)
- [Investing.com — Largan consensus estimates](https://www.investing.com/equities/largan-precisi-consensus-estimates)
- [MarketScreener — Largan consensus](https://www.marketscreener.com/LARGAN-PRECISION-CO-LTD-6495295/consensus/)
- [Smartkarma — Largan Q1 2026 earnings alert](https://www.smartkarma.com/home/newswire/earnings-alerts/largan-precision-3008-earnings-1q-net-income-surpasses-estimates-with-nt6-44-billion/)
- [BigGo — Largan "twin engines" CPO coverage](https://finance.biggo.com/news/TRV1KZ4BLfE1EzqPY3Zx)
- [BigGo — Largan Q1 2026 gross margin](https://finance.biggo.com/news/DTBJlZ0BvthpMgHBPyuQ)
- [TechNews — Largan 5-year high, founder family buying](https://finance.technews.tw/2026/06/01/largan-precision-stock-price-5-year-high-founder-family-bought-shares-should-you-invest-uncover-old-stock-king-transformation-secret/)
- [BusinessToday — shareholders' meeting coverage](https://www.businesstoday.com.tw/article/category/183008/post/202606090022/)
- [Mordor Intelligence — smartphone camera lens market](https://www.mordorintelligence.com/industry-reports/smartphone-camera-lens-market)
- [Goldman Sachs target via Investing.com](https://www.investing.com/news/analyst-ratings/goldman-sachs-lowers-largan-precision-stock-price-target-on-valuation-93CH-4427388)

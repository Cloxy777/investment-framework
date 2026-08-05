# New Position Evaluation — BKNG (Booking Holdings Inc.)

**Task type:** NEW POSITION
**Date:** 2026-08-05
**10Y US Treasury Yield:** 4.61%
**Rate Regime Modifier (active):** +5 (3.5–5% bracket)

## 0. Trigger

Automated Telegram-scan (Routine 6): a post on [t.me/bolshegold](https://t.me/bolshegold) (post #9906, ~2026-08-04 20:27 UTC) claimed BKNG's Q2 2026 earnings beat — Non-GAAP EPS $2.54, revenue $7.35B (+8.1% YoY), a $3.7B buyback with $14.5B remaining authorization. No prior watchlist entry exists for BKNG (`watchlist/not-in-portfolio/BKNG/` was empty) and it is not a current holding.

Per CLAUDE.md, none of the Telegram figures were treated as verified data — they were only a trigger to look at the ticker. Every figure below is independently sourced. As it happens, all four claimed figures check out exactly against the primary source (Booking Holdings' own SEC-filed Q2 2026 earnings press release, 8-K Exhibit 99.1, filed 2026-08-04):
- Adjusted (non-GAAP) EPS **$2.54** ✓ exact match ("Adjusted EPS $2.54... +15%")
- Revenue **$7.35B, +8.1% YoY** ✓ matches ($7,352M reported; (7,352−6,798)/6,798 = +8.15% independently recomputed from the filed figures)
- Buyback **$3.7B** ✓ exact match ("We repurchased $3.7 billion (excluding excise taxes) of stock in the quarter ended June 30, 2026")
- Remaining authorization **$14.5B** ✓ exact match ("total remaining authorization of $14.5 billion as of June 30, 2026")

This is disclosed for completeness, not as a substitute for independent verification — every number used in scoring below is separately sourced and cited.

---

## 1. Live price (Rule 0)

**$204.35** — IBKR `get_price_snapshot`, contract_id 308728373 (NASDAQ, "BOOKING HOLDINGS INC"), `ts` 1785888441 → 2026-08-05 00:07:21 UTC, `is_close: false` (intraday). Bid/ask $204.31 / $205.78. Prior close $194.27 (+5.19% intraday, i.e. continued post-earnings momentum the day after the 2026-08-04 report). 52-week range (IBKR `misc_statistics`): low $150.14 / high $230.45 (13-week and 26-week highs both $204.61 — today's price sits essentially at a 13/26-week high).

Cross-checked against Yahoo Finance's public chart endpoint (`regularMarketPrice` $194.27, `regularMarketTime` 2026-08-04 close) and stockanalysis.com ($194.27, "close Aug 4, 2026") — both agree with IBKR's *prior*-close field, confirming today's $204.35 print is a fresh intraday move, not a stale/duplicated close. 52-week range cross-check: stockanalysis.com shows $150.14–$231.80 (high differs from IBKR's $230.45 by $1.35, immaterial — IBKR used as the Rule 0 price of record throughout).

**Stock-split note:** Booking Holdings effected a 25-for-1 stock split effective 2026-04-02 (post-split trading began 2026-04-06). All prices, share counts, and per-share figures below (including SEC-filed historical comparatives) are already on a post-split basis — confirmed by cross-checking the 10-Q's own restated prior-year comparatives (e.g. Q2 2025 diluted shares restated to 815M, consistent with the pre-split 32.6M × 25).

---

## 2. Data sourcing

No `yfinance` Python module is installed in this environment and the module's own HTTP client is expected to be blocked by this session's egress proxy (repo precedent: MCD/CVX/IBM/CCL sessions). Per CLAUDE.md's documented fallback, data was sourced as follows — every figure below cites its source:

1. **SEC EDGAR XBRL `companyfacts` API** (`https://data.sec.gov/api/xbrl/companyfacts/CIK0001075531.json`) — primary source for income statement, balance sheet, and cash flow figures, cross-referenced against the raw 10-Q financial statement (`R4.htm` of accession 0001075531-26-000037, the 10-Q for the quarter ended 2026-06-30, filed 2026-08-04) and the Q2 2026 earnings press release (8-K Exhibit 99.1, `q2-26bkngearningsrelease.htm`, same filing date).
2. **Yahoo Finance's public `fundamentals-timeseries` endpoint**, called directly via `curl`/`requests` (not the blocked `yfinance` package) — used for multi-year annual/quarterly time series, cross-checked against SEC XBRL wherever the two overlap (they reconcile exactly on Revenue, Operating Income, Net Income, and Free Cash Flow).
3. **stockanalysis.com** (via WebFetch) — used for gross profit/margin (BKNG's GAAP income statement does **not** present a Gross Profit or Cost-of-Revenue line — confirmed by reading the raw 10-Q statement of operations directly; see §3 Margins note), forward PE / consensus EPS, peer comparables, and cross-checks.
4. **WebSearch** — used for ROIC cross-checks (multiple independent providers), 10Y Treasury yield, peer valuation multiples, and qualitative moat/growth evidence, each cited inline where used.

No required metric was unavailable from all sources; no figure below is invented or estimated.

---

## 3. Phase 01 — Quality Score (methodology version 2026-06-29)

### Profitability (25% weight)

- **Net Margin (TTM)** = TTM Net Income ÷ TTM Revenue = $7,209M ÷ $28,241M = **25.53%**
  - TTM = Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026 (all SEC XBRL, `NetIncomeLossAvailableToCommonStockholdersBasic`): $2,748M + $1,428M + $1,083M + $1,950M = $7,209M. Cross-checked via TTM Pretax Income ($9,291M) − TTM Tax ($2,082M) = $7,209M exactly.
  - TTM Revenue = $9,008M + $6,349M + $5,532M + $7,352M = $28,241M (SEC XBRL `RevenueFromContractWithCustomerExcludingAssessedTax`/`Revenues`).
- **ROIC (TTM)** — **flagged judgment call**, see box below. Used **24.49%**.
- NetMargin_Component = clamp((25.53/30)×100) = **85.09**
- ROIC_Component = clamp((24.49/30)×100) = **81.63**
- No FCF-positivity cap (FCF positive every year FY2022–FY2025 and TTM — see FCF Quality below).
- **Profitability_Score = (85.09 + 81.63) / 2 = 83.36**

> **ROIC negative-invested-capital note (same issue as the FICO 2026-07-07 precedent):** BKNG's GAAP stockholders' equity is a deficit of −$10,783M as of 2026-06-30 (SEC XBRL `StockholdersEquity`, deepening every quarter — structural, buyback-funded, same pattern as FICO/MCD, not a distress signal on its own). This framework's own Invested Capital formula (Total Debt + Equity − Cash) computes to **−$7,303M** ($20,694M + (−$10,783M) − $17,214M) — negative, because BKNG's large cash hoard *plus* deeply negative equity overwhelms its modest net debt. NOPAT ÷ a negative denominator is not a meaningful number, so rather than force a distorted own computation, I cross-checked three independently-sourced third-party figures with disclosed methodology: **GuruFocus 24.49%** (quarterly, as of Mar 2026), **stockanalysis.com 23.05%** (Q2 2026 quarter), and **stock-analysis-on.net 42.20%** (FY2025, using NOPAT $5,449M ÷ Invested Capital $12,912M — a materially different, less-cash-netted invested-capital definition that doesn't reconcile with ours). Given the genuine methodology-driven spread (23–42%), I used the **median of the three (24.49%, GuruFocus)** rather than the higher outlier — the more conservative choice, consistent with not overstating quality on an ambiguous input.

### Margins (15% weight)

BKNG's GAAP income statement (confirmed by reading the raw 10-Q statement of operations directly, SEC XBRL viewer `R4.htm`) goes straight from Total Revenues to itemized operating expenses (Marketing, Sales and other expenses, Personnel, G&A, IT, D&A, Transformation costs) — **there is no Gross Profit or Cost-of-Revenue line in BKNG's primary financial statements.** Gross margin below is therefore a **third-party-computed approximation** (stockanalysis.com), not a primary GAAP figure — flagged per "never invent or estimate financial data." The closest GAAP-derived proxy (Revenue − "Sales and other expenses," the line stockanalysis.com's figure appears to approximate) gives Q2 2026: ($7,352M − $942M) / $7,352M = 87.19%, within 0.6pp of stockanalysis.com's reported 87.76% — immaterial either way since both clear the clamp ceiling.

- **Gross Margin (TTM)** = TTM Gross Profit ÷ TTM Revenue = $24,634M ÷ $28,241M = **87.23%** (stockanalysis.com quarterly figures: Q3 2025 $8,063M + Q4 2025 $5,480M + Q1 2026 $4,639M + Q2 2026 $6,452M; FY2025 sum $23,514M reconciles exactly to stockanalysis.com's reported FY2025 gross profit, confirming internal consistency of the quarterly series)
- GrossMargin_Score = clamp((87.23/80)×100) = **100.0 (capped)**
- No structural-trend bonus applicable (already at max; trend bonus only applies below the 40% threshold)
- **Margins_Score = 100.0**

### Growth (20% weight)

- **Revenue 3yr CAGR** = (FY2025 Revenue ÷ FY2022 Revenue)^(1/3) − 1 = ($26,917M ÷ $17,090M)^(1/3) − 1 = **16.36%**
- Growth_Score base = clamp((16.36/25)×100) = **65.43**
- **+10 documented TAM-expansion modifier**: Booking's "Connected Trip" strategy — integrating flights, ground transport, attractions, and payments alongside core accommodation bookings into a single cross-vertical itinerary, explicitly targeting a larger share of a ~$1.5T total travel market rather than just the hotel-booking transaction. Cited: [ainvest.com](https://www.ainvest.com/news/booking-holdings-connected-trip-vision-scale-1-5t-travel-market-2602/) ("Can Its Connected Trip Vision Scale in a $1.5T Travel Market?"), corroborated by management's own FY2026 gross-bookings guidance of $192B and cited "rapid expansion in ancillary travel verticals such as flights and attractions." Global accommodation supply also expanded +8% YoY to 8.4M alternative-stay listings (electroiq.com), independent evidence of continued top-of-funnel TAM growth.
- **No structural-deceleration modifier applied**, despite real, guided deceleration (FY2025 revenue growth 13.4%, Q2 2026 revenue growth +8.15% YoY, Q3 2026 guided at +4–6%, FY2026 guided "high single digits" — down from FY2023's 25.0% and FY2024's 11.1%): management explicitly and repeatedly attributes the deceleration to a specific, named, cyclical/geopolitical cause — the Middle East conflict's direct and indirect impact on international travel corridors (per the Q2 2026 earnings release's own Outlook section: "we remain mindful of the Middle East conflict... assumes some pressure on inbound travel to the Middle East, while travel demand from Middle East bookers remains largely normalized") — not a structural TAM-shrinkage, moat-erosion, or competitive-share-loss cause, which is what the framework's −10 modifier specifically requires ("documented evidence growth is decelerating **structurally**, not cyclically"). Flagged for ongoing Phase 04 monitoring regardless (see Qualitative Notes, bear case).
- **Growth_Score = 65.43 + 10 = 75.43**

### Balance Sheet (15% weight)

- **Total Debt** = $20,694M as of 2026-06-30 (stockanalysis.com; reconciles exactly against SEC XBRL: `LongTermDebtNoncurrent` $18,180M + `LongTermDebtCurrent` $2,000M = $20,180M funded debt, plus `OperatingLeaseLiabilityNoncurrent` $514M = $20,694M — the same "vendor Total Debt folds in operating-lease liabilities the company's own debt line excludes" pattern flagged in the MCD/CCL sessions, fully reconciled here rather than left as an unexplained gap)
- **Cash** = $17,214M (SEC XBRL `CashAndCashEquivalentsAtCarryingValue`, 2026-06-30)
- **Net Debt** = $20,694M − $17,214M = **$3,480M**
- **TTM EBITDA** = TTM EBIT ($9,284M — see EV/EBIT below) + TTM D&A ($571M: Q3'25 $160M + Q4'25 $151M + Q1'26 $131M + Q2'26 $129M, SEC XBRL `DepreciationDepletionAndAmortization`) = **$9,855M**
- **Net Debt/EBITDA = $3,480M / $9,855M = 0.353×** — far below the 2.5× standard threshold (asset-light override not even needed)
- BalanceSheet_Score = 100×(1 − 0.353/4) = **91.17**

### Moat Signal (15% weight)

| Signal | Verdict | Evidence (cited) |
|---|---|---|
| Market share stable/growing | **TRUE** | Booking.com holds 69.3% share within the OTA-competitor set vs. Expedia's 11.5% ([globalgrowthinsights.com](https://www.globalgrowthinsights.com/blog/10-biggest-online-travel-agency-ota-companies-in-the-world-global-growth-insights-520)); Booking.com led global travel-site traffic in 2024 with 562.6M monthly visits, >5× Airbnb/Tripadvisor ([electroiq.com](https://electroiq.com/stats/booking-com-statistics/)); alternative-accommodation listings grew +8% YoY to 8.4M. *(Nuance: one hotel-brand survey found the broader OTA *channel* losing share to direct bookings industry-wide — 22% vs. 30% the prior year — but that's a statement about OTAs collectively vs. direct, not about Booking's position within the OTA set, where its lead over Expedia/peers is not shown to be eroding.)* |
| Brand premium / pricing power | **TRUE** | Booking.com's average host commission has climbed into the 15–30%+ range, and its early-2026 Genius program overhaul replaced guaranteed-visibility-for-discount with a relevance-based algorithm — effectively raising hosts' real cost per booking beyond the stated commission rate — while OTA dependence "deepened globally" in 2025 and direct-booking share for independent hotels did *not* improve despite EU rate-parity deregulation aimed at enabling it ([cloudbeds.com](https://www.cloudbeds.com/online-travel-agencies/commissions/)) — price increases without a corresponding volume/share loss. |
| Network effect | **TRUE** | Genius operates across ~2.5 million total properties with ~850,000 actively participating, a two-sided marketplace where more properties attract more members and more members incentivize more property participation — a documented mechanism, not just a scale claim ([hospitality.today](https://www.hospitality.today/article/genius-members-drive-over-half-of-booking-com-bookings)). |
| Switching costs | **TRUE** | Genius's tiered loyalty structure: members book ~50% more nights annually than non-members, and Genius Level 2/3 members (>30% of the active user base) generate more than half of total room nights — an escalating-benefit lock-in mechanism, not a one-off discount. |
| Scale cost advantage | **TRUE** | Annual digital ad spend exceeding $7 billion funds proprietary conversion/bidding algorithms smaller OTAs can't replicate at the same scale; over 50% of room nights now book through owned/direct channels (mid-fifties % over the trailing four quarters, similar to the prior year), reducing paid-marketing dependence — a documented cost-per-unit structural advantage vs. smaller competitors, who rely far more heavily on the ~15–30% OTA-commission-funded acquisition model. |

**Moat_Score = (5/5) × 100 = 100.0**

### FCF Quality (10% weight)

- **TTM FCF** = TTM OCF ($9,859M: Q3'25 $1,435M + Q4'25 $1,490M + Q1'26 $3,215M + Q2'26 $3,719M) − TTM CapEx ($320M: $64M + $73M + $107M + $76M) = **$9,539M** (all SEC XBRL, `NetCashProvidedByUsedInOperatingActivities` / `PaymentsToAcquirePropertyPlantAndEquipment`, each quarter derived by subtracting cumulative YTD figures)
- **TTM FCF/NI ratio** = $9,539M / $7,209M = **132.3%** — FCF *exceeds* net income, a structural feature of Booking's merchant model (customers prepay, Booking remits to the property later — see Deferred merchant bookings in the Glossary — a large, growing negative-working-capital float that pulls operating cash flow above accounting profit). No hard-disqualifier risk in either direction.
- FCFQuality_Score = clamp(((1.323 − 0.40)/0.60)×100) = **100.0 (capped)**

### Hard disqualifiers — none fire

- FCF/NI conversion: 132.3% TTM (well above 70%) — no issue.
- Net Debt/EBITDA: 0.353× (well under 2.5×) — no issue.
- FCF-positive 3+ consecutive years: yes — FY2022 $6,186M, FY2023 $6,999M, FY2024 $7,894M, FY2025 $9,087M, TTM $9,539M — all positive, growing every year.

### Quality Score

```
Quality Score = 83.36×0.25 + 100.0×0.15 + 75.43×0.20 + 91.17×0.15 + 100.0×0.15 + 100.0×0.10
              = 20.840 + 15.000 + 15.086 + 13.6755 + 15.000 + 10.000
              = 89.60
```

**Quality Score = 89.6 / 100.0 — clears the 80.0+ gate comfortably.** Proceed to Phase 02.

---

## 4. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** EY = 1 ÷ Forward PE = 1 ÷ 19.556 = **5.11%**. Spread = 5.11% − 4.61% (10Y) = **+0.50pp** — below the +1.5pp threshold → **+5 additive modifier** (yellow flag, not a veto, per the 2026-06-07 rule change).
- **Step 2 — Rate Regime Modifier:** 10Y yield 4.61% sits in the 3.5–5% bracket → **+5**.
- **10Y Treasury yield source:** WebSearch cross-check of multiple sources (CNBC/TradingEconomics-style reporting), converging on **4.61%** as of 2026-08-04 (range cited across sources: 4.61–4.69% over 2026-08-03/04). Direct FRED `DGS10` CSV pull failed at the network layer (proxy connection reset) — used the WebSearch cross-check per CLAUDE.md's "never invent" discipline applied to a genuinely-unreachable primary source; multiple independent secondary sources converged tightly (within 8bp), so this is not treated as a data gap.

**Total Rate Environment Gate modifier: +10**

---

## 5. Phase 02 — Valuation Score

### PEG / Fast Grower eligibility — not applicable

BKNG's diluted EPS: FY2022 $3.054 → FY2023 $4.696 (+53.8%) → FY2024 $6.9076 (+47.1%) → **FY2025 $6.6228 (−4.1%)**. EPS growth did **not** exceed 15% for 3+ consecutive years (the most recent year was negative) — fails the Fast Grower test regardless of cause. For transparency: the FY2025 EPS decline was driven by a **$1,428M non-cash foreign-currency remeasurement loss on Euro-denominated debt** recorded in "Other income (expense), net" (below the operating line) — a one-off, non-operating item, not an operating-performance problem (FY2025 operating income actually grew +16.8% YoY to $8,825M). This framework scores off filed GAAP figures rather than adjusting for one-offs when determining Fast-Grower eligibility (per the PEG clean-earnings clarification precedent), so the disqualification stands regardless of the explainable cause. **PEG's 15% weight is redistributed to EV/EBIT (→ 40% weight)**, per valuation-scoring.md.

### FCF Yield (40% weight)

- Market Cap = 751,380,500 shares (SEC 10-Q cover page, `EntityCommonStockSharesOutstanding` as of 2026-07-27, the most current count available) × $204.35 live price = **$153,544.6M**
- FCF Yield = TTM FCF ($9,539M) ÷ Market Cap ($153,544.6M) = **6.21%**
- FCF_Score = clamp(100×(1 − 6.21/10)) = **37.88**

### EV/EBIT (40% weight, PEG-redistributed)

- Enterprise Value = Market Cap ($153,544.6M) + Total Debt ($20,694M) − Cash ($17,214M) = **$157,024.6M**
- TTM EBIT (= GAAP Operating Income, since it already excludes interest and tax) = Q3'25 $3,483M + Q4'25 $2,030M + Q1'26 $1,271M + Q2'26 $2,500M = **$9,284M**
- EV/EBIT = $157,024.6M / $9,284M = **16.91×**
- Cross-check: stockanalysis.com reports EV/EBIT 16.52× (immaterial ~2% difference, likely timing/share-count basis) — both land in the same score range.
- EV/EBIT_Score = clamp((16.91 − 12)/23 × 100) = **21.37**

### Forward PE (20% weight)

- Forward PE = Live Price ($204.35) ÷ FY2026 consensus EPS ($10.45, 35 analysts, stockanalysis.com forecast page) = **19.56×**
- **5-year avg/range PE: no-history fallback invoked, flagged.** Third-party sources diverge enormously and are visibly distorted by BKNG's 2020–2021 COVID-travel-collapse earnings trough still partially inside various providers' lookback windows: reported 5-year average PE ranges from **60.33× (FullRatio) to 104.64× (FinanceCharts)** — a >70% spread between two reputable providers — and the reported 10-year PE *range* runs from 10.46× to **1,655.89×** (macrotrends), the latter reflecting quarters where trailing EPS was near-zero. A "5-year average PE" computed over a window this distorted is not a meaningful anchor — exactly the "GAAP earnings base too distorted to be meaningful" scenario valuation-scoring.md's fallback clause anticipates (even though *current* EPS is clean, the *historical* denominator isn't). No `yfinance` reconstruction was possible in this environment to build an independent, controllable series (no module installed). **FwdPE_Score = 50.0 (neutral, flagged)** — no separate Historical PE Modifier applied, consistent with the fallback rule.

### Raw weighted score

```
Raw Score = FCF_Score×0.40 + EV/EBIT_Score×0.40 + FwdPE_Score×0.20
          = 37.88×0.40 + 21.37×0.40 + 50.0×0.20
          = 15.152 + 8.548 + 10.000
          = 33.70
```

### Upside/Downside Modifier

**Fair Value work (Step 1, fair-value-methodology.md) — DCF + comparable multiples, 3 scenarios, 40%/60% blend:**

*DCF assumptions (flagged as analyst judgment, not fetched data, per the AVGO precedent):* WACC built from CAPM cost of equity (risk-free 4.61% + beta 1.10 [WebSearch, multiple sources] × 5.0% standard ERP assumption = 10.11%) blended with an estimated after-tax cost of debt (~4.46%) at market-value weights (88.1% equity / 11.9% debt) → **WACC ≈ 9.4%** (base case; ±1pp for bull/bear per Rule 2). Full 10-year, 3-stage model (Stage 1 yrs 1–5 explicit, Stage 2 yrs 6–10 fade, Stage 3 terminal, per Rule 2) — extended to 10 years because a 5-year-only model put terminal value at 75.1% of total EV, breaching Rule 4's 75% sanity check; the 10-year version brings terminal-value weight down to 56%. Terminal growth capped at 2.75% (≤ long-run GDP, per Rule 2). Base-case revenue growth path (8.0% Y1, fading to 2.75% by Y10) is set modestly below my initial 9% assumption specifically to align with management's own FY2026 "high single digit" revenue-growth guidance (Q3 2026 guided +4–6%) — guidance is never scored directly (per "Why Forward Guidance Is Not a Sub-score"), but is used here as a sanity-check anchor for a DCF input, which is an explicitly permitted use.

| Scenario | WACC | Growth path (Y1→Y10) | FCF margin path | DCF FV/share |
|---|---|---|---|---|
| Bull | 8.4% | 9.0% → 3.75% | 35.0% → 38.0% | **$335.44** |
| Base | 9.4% | 8.0% → 2.75% | 34.0% → 37.0% | **$254.16** |
| Bear | 10.4% | 7.0% → 2.75% | 34.0% flat | **$192.75** |

(Bear-case DCF of $192.75 landing close to the live price of $204.35 is a useful sanity check — a "no re-rating, modest growth" scenario should land near where the market already prices the stock, and it does.)

*Comparable multiples:* Peer forward PEs — Expedia (EXPE) 13.19×, Trip.com (TCOM) 17.01×, Airbnb (ABNB) 32.36× (WebSearch, cross-provider). Peer median 17.01×, peer average 23.26×.

| Scenario | Multiple basis | Applied to | Multiples FV/share |
|---|---|---|---|
| Bull | Peer average + quality premium (~25×) | FY2026 consensus EPS $10.45 | **$243.06** (peer avg 23.26×) |
| Base | Blend of peer median/average (20.14×) | FY2026 consensus EPS $10.45 | **$210.41** |
| Bear | Peer low end (Expedia 13.19×) | FY2026 consensus EPS $10.45 | **$137.83** |

**Triangulation (40% DCF + 60% Multiples, per fair-value-methodology.md Step 1):**

```
Bull FV = 0.40×335.44 + 0.60×243.06 = $280.02
Base FV = 0.40×254.16 + 0.60×210.41 = $227.91
Bear FV = 0.40×192.75 + 0.60×137.83 = $159.80

PW Fair Value = 0.25×280.02 + 0.50×227.91 + 0.25×159.80 = $223.91
```

**Step 1 — Expected annual return E:**

```
Gap Upside % = (PW FV ÷ Live Price) − 1 = (223.91 / 204.35) − 1 = +9.58%
Catalyst window = 2 years (see catalyst note below)
Annualized gap = 9.58% / 2 = +4.79%
Intrinsic growth = ~8.0% (base-case FCF CAGR, Y0→Y5: ($14,026M/$9,539M)^(1/5)−1 = 8.01%)
Shareholder yield = dividend yield (0.82%: $1.68 annualized ÷ $204.35) + net buyback yield (7.26%:
  actual outstanding-share-count decline, SEC 10-Q cover pages, 810.2M equivalent shares 2025-07-21 →
  751.4M shares 2026-07-27, over ~370 days)
E = 4.79% + 8.01% + 7.26% + 0.82% = 20.88%
```

**Catalyst:** the Transformation Program's cost-savings ramp is a dated, company-disclosed catalyst — management raised its expected annual run-rate savings target to ~$650M as of the Q2 2026 release, "by the end of 2027" (~17 months out, within the 18–24mo window). A second, less certain catalyst is any normalization of the Middle East conflict's direct/indirect drag on international travel corridors, which management itself frames as the primary swing factor for reacceleration. Both fall within the 18–24 month window, so the upside-side −5 guardrail cap does not apply.

**Step 2 — Map E to modifier** (H = 10%):

```
E (20.88%) ≥ H (10%) → M = −15 × clamp((20.88 − 10)/15, 0, 1) = −15 × 0.725 = −10.88
```

**Note on this result:** E is dominated by shareholder yield (7.26% net buyback + 0.82% dividend = 8.08pp of the 20.88% total) and intrinsic FCF growth (8.01pp) — the pure valuation-gap component (annualized 4.79%) is comparatively modest, i.e. this isn't a "deeply mispriced" case, it's a "high-quality compounder returning almost all its FCF to shareholders at an unusually aggressive rate" case. Flagged per Phase 04's Guidance/Earnings-quality-check spirit for ongoing monitoring: FY2024 EPS growth (+47.1%) ran well ahead of that year's revenue growth (+11.1%, a 36pp gap) — a legitimate watch item for whether buybacks are doing more of the EPS-growth work than the operating business, even though nothing here suggests earnings-quality manipulation (buybacks are fully disclosed, cash-funded, and paired with genuine double-digit operating-income growth).

### Final Valuation Score

```
Final Score = Raw Score + Rate Environment Gate + Upside/Downside Modifier
            = 33.70 + 10.00 + (−10.88)
            = 32.82 → rounds to 32.8
```

**Valuation Score = 32.8 / 100.0** (30.0–49.9 band = "Cheap" per the raw-score Action Table)

---

## 6. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 89.6) + 0.50 × 32.8
                = 0.50 × 10.4 + 0.50 × 32.8
                = 5.2 + 16.4
                = 21.6
```

**Composite Score = 21.6 / 100.0 — "Very Cheap" (0.0–29.9 band).** Per valuation-scoring.md, the Composite Score (not the raw Valuation Score) governs the Phase 03 action-table read: 21.6 nominally maps to **Full position (6–8% of portfolio)**. BKNG's very high Quality Score (89.6) pulls the blend meaningfully below the raw Valuation Score (32.8) alone — exactly the case the Composite Score was designed to catch (a much-higher-quality business shouldn't lose out to a marginally cheaper, lower-quality one).

---

## 7. Fair value & order setup

> **Result up front: the R/R gate blocks entry at this price, despite the attractive Composite Score.** Full mechanics below.

Per fair-value-methodology.md's Composite-Score-banded MoS/Stop tables (0.0–29.9 band): MoS range 15–20%, Max Acceptable Loss range 20–25%. Used **MoS = 20%** (top of range) and **Max Loss = 22%** (mid-range) as the primary case — chosen conservatively because Composite 21.6 sits in the upper-middle, not the deepest, part of the Very Cheap band.

```
[x] Composite Score (incl. Quality blend):        21.6  (Very Cheap band, 0.0–29.9)
[x] Valuation Score (incl. Upside/Downside Mod):   32.8
[x] Expected annual return E / catalyst window:    20.88% / 2yr
[x] Upside/Downside Modifier applied:              −10.88
[x] DCF Fair Value (base case):                    $254.16
[x] Multiples-Based Fair Value (base case):         $210.41
[x] Blended Fair Value (PW, bull/base/bear):        $223.91
[x] Margin of Safety %:                             20% (top of 15–20% range)
[x] BUY PRICE (limit order):                        $179.13   (= $223.91 × 0.80)
[x] PRIMARY SELL TARGET:                             $223.91   (= Blended/PW Fair Value)
[x] BULL-CASE TRIM TARGET:                           $252.02   (= $280.02 × 0.90)
[x] STOP LOSS:                                       $139.72   (= $179.13 × 0.78, 22% max loss)
[x] Risk/Reward Ratio:                               1.14:1   ← FAILS the 2:1 minimum
[x] Max $ Risk (1.5% of $60,829.03 combined portfolio): $912.44
[x] POSITION SIZE (shares, if it cleared R/R):        23.15 shares
[x] POSITION SIZE ($, if it cleared R/R):              $4,147 (≈6.82% of portfolio — within the 6–8% cap)
[x] Thesis invalidation triggers:                     see §8
```

**R/R math:**
```
R/R = (Sell Target − Entry) ÷ (Entry − Stop Loss)
    = (223.91 − 179.13) ÷ (179.13 − 139.72)
    = 44.78 ÷ 39.41
    = 1.14:1
```

**This structurally cannot reach 2:1 within this score band's authorized parameters.** R/R as a function of MoS and Max-Loss% simplifies to `MoS / [(1 − MoS) × MaxLoss%]`. Even at the most R/R-favorable *authorized* combination for a 0.0–29.9-Composite-Score position — MoS at its maximum (20%) and Max Loss at its tightest/minimum (20%) — R/R = 0.20 / (0.80 × 0.20) = **1.25:1**, still short of 2:1. Solving for the entry price that would exactly hit 2:1 (at the tightest 20% stop): Entry = Sell Target / 1.40 = $223.91 / 1.40 = **$159.94** — which implies a Margin of Safety of 28.6%, outside the 15–20% range this framework authorizes for a Very-Cheap-but-not-Turnaround score (28–40% MoS is reserved for the Turnaround Sub-Gate / cyclical-trough case, which doesn't apply here — BKNG isn't a turnaround, it's a high-quality compounder at a modest discount).

**Cross-check against the 15% position cap:** the reference position size above (6.82% of the combined $60,829.03 portfolio) is well under the 15% hard cap — not the binding constraint here.

---

## 8. Recommendation

**WATCHLIST ONLY — do not enter, despite a Composite Score (21.6) that nominally qualifies for a Full Position (6–8%).**

The mandatory 2:1 minimum Risk/Reward gate (fair-value-methodology.md Step 6: *"If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely"*) fails at every Margin-of-Safety/stop-loss combination this score band authorizes — the best achievable case (max 20% MoS, tightest 20% stop) is 1.25:1. This is a **"wait for a lower entry," not a "pass forever"** case: the underlying business clears the quality gate by a wide margin (89.6/100.0) and screens attractively cheap on a blended basis, but the current live price ($204.35) sits too close to a fair value estimate ($223.91) that itself isn't dramatically above the price — the ~9.6% total valuation gap simply isn't large enough to support both a defensible margin of safety *and* a 2:1 payoff against a realistic stop, without reaching for a Margin of Safety this framework doesn't authorize outside a genuine turnaround situation.

**Action:** set a price alert at **≤$159.94** (the level at which 2:1 R/R clears using the tightest authorized stop) or revisit on the next Rule 9 trigger — most likely BKNG's Q3 2026 earnings release (Booking has historically reported early-to-mid November; no company-confirmed date yet) or a guidance revision. No fundamental deterioration is evident (Quality Score 89.6, Moat 5/5, FCF growing every year) — this is purely a price/R-R gate, not a quality or thesis concern.

**No position opened. Nothing logged in `decisions/` or `portfolio/holdings.md`.**

---

## 9. Qualitative notes (5 questions + disruption vector check)

1. **Why are margins high?** Asset-light online marketplace model — Booking doesn't own hotels, planes, or rental-car fleets; it collects a commission/margin on transactions it facilitates. Its largest single operating-expense line (marketing, ~32% of revenue) is a *variable*, scale-leverageable cost, not fixed infrastructure — the structural reason a mature OTA at Booking's scale can sustain >85% gross-margin-proxy economics.

2. **Moat assessment:** Moat_Score 100.0 (5/5, all independently cited — see §3). Dominant share within the OTA competitor set (69.3% vs. Expedia's 11.5%), genuine two-sided network effects (Genius's 2.5M-property/850K-active network), a documented switching-cost mechanism (tiered loyalty, 50% higher booking frequency among members), demonstrated pricing power (rising effective host commission despite regulatory pressure toward direct booking), and a real scale cost advantage in paid-marketing efficiency ($7B+ annual ad spend, mid-50s% direct-traffic mix).

3. **Capital allocation track record:** Extremely aggressive and consistent — TTM buybacks of ~$10.5B against a $153.5B market cap (share count down ~7.3% YoY), a modest and growing quarterly dividend ($0.42/share, initiated 2024), no major M&A. Partly debt-funded (Euro-denominated senior notes), which introduces a real, disclosed FX risk: a $1,428M non-cash FX remeasurement loss on that Euro debt dragged FY2025 GAAP net income down significantly (net margin swung from 24.78% in FY2024 to 20.08% in FY2025) even as operating income grew +16.8%. This framework scored off the GAAP-reported (not FX-adjusted) figures throughout, consistent with not scoring self-reported/adjusted metrics.

4. **Growth sources next 3–5 years:** Connected Trip cross-vertical monetization (flights, attractions, ground transport, payments — still only "low double-digit percentage of transactions despite years of investment," i.e. most of the opportunity is still ahead of it, not behind it); Transformation Program cost savings (~$650M run-rate by end-2027) supporting margin expansion independent of top-line growth; continued alternative-accommodation supply growth (+8% YoY); potential Middle East normalization reaccelerating the international travel corridors currently under guided pressure.

5. **Best bear case:** The Middle East conflict (or a similar future geopolitical shock) persists or worsens, further denting high-value international corridors beyond current guidance. More structurally: the broader OTA distribution channel is showing early signs of share erosion to direct hotel booking (one hotel-brand survey found OTA-sourced bookings fell from 30% to 22% of the total year-over-year) — a trend worth monitoring even though it hasn't yet visibly cost Booking share *within* the OTA competitor set. Connected Trip execution risk — the strategy is real and well-resourced but has moved slowly ("low double-digit percentage of transactions" after years of investment). Continued Euro-debt FX volatility will keep distorting GAAP earnings comparability period to period.

6. **Disruption vector check:** The most credible medium-term threat is AI-agent-mediated travel booking (an LLM-based assistant booking a trip directly with a hotel/airline, bypassing OTA search/discovery entirely) — an actively-discussed structural risk across travel tech, though there is no evidence yet of Booking losing share to an AI-native competitor. Booking's own "AI Trip Planner" and the broader Connected Trip strategy are direct hedges/responses to this vector rather than reactions to an already-materialized threat. Flagged as a genuine moat-durability watch item for future Rule 9 checks, not a present-day disqualifier.

---

## 10. Next review trigger

- BKNG's Q3 2026 earnings release (Rule 9 standard trigger — date not yet company-confirmed; historically early-to-mid November)
- Any guidance revision (up or down) — mandatory re-valuation trigger regardless of schedule
- Price reaching ≤$159.94 (the R/R-gate-clearing level identified above) — worth an ad hoc re-check even absent a Rule 9 event, since it would flip the recommendation from "watchlist" to "set limit order"
- Any Middle East conflict resolution/de-escalation materially changing the international-travel-demand outlook Booking itself has flagged as the key swing factor

---

## Files touched this session

- `sessions/2026-08-05-new-position-bkng.md` — this file
- `watchlist/not-in-portfolio/BKNG/BKNG-2026-08-05.md` — new (first-ever) watchlist entry
- `framework/glossary.md` — added **CC (Constant Currency)**, **Connected Trip**, **Deferred merchant bookings**, **Excise tax (stock buyback)**, **Genius (Booking.com loyalty program)**, **Merchant revenues / Agency revenues**, **OTA (Online Travel Agency)**, **Room Nights**, **Stock split**, **Transformation Program**; extended the existing **Gross Bookings** entry to note BKNG's use of the same term.

`portfolio/holdings.md`, `decisions/`, and `watchlist/STALE.md` **not touched** — no position was opened, and this is BKNG's first-ever score (nothing to mark stale).

---

## Glossary

- **8-K** — SEC "current report" filed within days of a material event; Booking's Q2 2026 earnings press release was furnished via an 8-K Exhibit 99.1 on 2026-08-04.
- **Beta** — a stock's sensitivity to overall market moves, used with the risk-free rate and Equity Risk Premium to estimate cost of equity in WACC.
- **CAGR** — Compound Annual Growth Rate.
- **CC (Constant Currency)** — a growth-rate presentation stripping out currency-movement effects.
- **Composite Score** — this framework's blended Quality + Valuation ranking number (50/50), computed only for companies clearing the 80.0+ Quality Score gate.
- **Connected Trip** — Booking Holdings' strategy of cross-selling flights, attractions, ground transport, and payments alongside core accommodation bookings.
- **DCF (Discounted Cash Flow)** — a valuation method projecting future cash flows and discounting them to present value.
- **Deferred merchant bookings** — a balance-sheet liability for cash already collected from travelers for stays that haven't yet occurred.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **Enterprise Value (EV)** — Market Cap + Total Debt − Cash; the total cost to acquire a company including its debt.
- **EPS** — Earnings Per Share.
- **Equity Risk Premium (ERP)** — the extra return equity investors demand over the risk-free rate; a standard DCF modeling assumption (5.0% here), not a fetched fact.
- **Excise tax (stock buyback)** — a 1% US federal tax on net stock repurchases.
- **Fast Grower** — Peter Lynch's term for a company growing EPS >15%/year for 3+ years; this framework's PEG-sub-score trigger. BKNG does not currently qualify.
- **FCF (Free Cash Flow)** — cash generated by operations after capital expenditure.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; an earnings-quality check.
- **FCF Yield** — Free Cash Flow ÷ Market Cap; how much cash a company throws off relative to its price.
- **Forward PE** — Price ÷ next-twelve-months expected EPS.
- **Genius (Booking.com loyalty program)** — Booking's tiered traveler loyalty program, cited as Network Effect and Switching Cost moat evidence.
- **Gross Bookings** — total dollar value of travel services booked through Booking's platforms before Booking's own take-rate is deducted.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of weighted score; none fired for BKNG.
- **Invested Capital** — the capital (debt + equity, net of cash in this framework's convention) put to work in a business; negative for BKNG due to its large cash balance and deeply negative equity.
- **Merchant revenues / Agency revenues** — Booking's two revenue-recognition models (Booking collects payment directly vs. the property collects and pays a commission).
- **Moat** — a durable competitive advantage protecting a business's profits from competitors.
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate.
- **NOPAT** — Net Operating Profit After Tax; the numerator this framework uses for ROIC.
- **OTA (Online Travel Agency)** — an online marketplace/broker for travel bookings between travelers and travel suppliers.
- **PEG ratio** — PE ratio ÷ earnings growth rate; not applicable to BKNG this session (Fast Grower test not met).
- **PW (Probability-Weighted) Fair Value** — this framework's blended bull/base/bear fair value estimate (25%/50%/25%).
- **Quality Score** — this framework's 0.0–100.0 continuous quality grade; BKNG scores 89.6, clearing the 80.0+ gate.
- **Rate Environment Gate** — the mandatory pre-check comparing Earnings Yield against the 10-Year Treasury yield.
- **Rate Regime Modifier** — an additive valuation-score adjustment based on the current Treasury-yield bracket.
- **ROIC** — Return on Invested Capital; a flagged judgment call for BKNG due to negative invested capital (see §3).
- **Room Nights** — Booking's core accommodation-volume metric.
- **Rule 0** — this framework's standing instruction to always fetch a live price before any valuation work.
- **Rule 9** — this framework's list of fundamental events forcing an immediate re-valuation.
- **Shareholder yield** — dividend yield plus net buyback yield combined.
- **Stock split** — a corporate action increasing share count by a fixed ratio while proportionally reducing price per share; BKNG split 25-for-1 on 2026-04-02.
- **Terminal Value** — the lump-sum DCF value assigned to all cash flows beyond the explicit forecast period.
- **Transformation Program** — Booking Holdings' cost-reduction initiative, targeting ~$650M annual run-rate savings by end-2027.
- **Treasury yield (10Y)** — the standard risk-free-rate benchmark used throughout the Rate Environment Gate.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.
- **Upside/Downside Modifier** — an additive ±15 valuation-score adjustment based on expected annual return.
- **WACC** — Weighted Average Cost of Capital; the DCF discount rate.

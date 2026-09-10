# NEW POSITION — CCJ (Cameco Corporation, NYSE/TSX) — 2026-09-10

**Task type:** NEW POSITION (manual `/new-position CCJ` run)
**Date:** 10 Sep 2026
**10Y US Treasury Yield:** 4.80% (FRED `DGS10`, most recent posted observation, dated 2026-09-08)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §4). For reference, the bracket in force is +5 (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current CCJ portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None — first evaluation of this ticker.
**Sector:** Energy / Uranium mining (nuclear fuel supply).
**Filer type:** Canadian company (Saskatoon, SK), dual-listed NYSE (CCJ) / TSX (CCO); SEC filer via Form 40-F/6-K (foreign private issuer). All figures below sourced from Yahoo Finance/`yfinance`-mirrored primary financial statements (income statement, balance sheet, cash flow), cross-checked quarter-by-quarter for TTM reconstruction, plus Cameco's own Q2 2026 earnings release/call materials for qualitative evidence.
**First-use jargon decode:** see closing Glossary (§9).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$97.59** | IBKR `get_price_snapshot` (contract_id **1447060**, NYSE, "CAMECO CORP" — disambiguated via `search_contracts` against 7 results: Cincinnati Financial Corp [also ticker "CCJ" on IBIS/Frankfurt], CC Japan Income & Growth Trust ["CCJI", LSE], County International Ltd [delisted "CCJ.OLD"], Cameco's own CHF-quoted line [CCJUSD, EBS], an American Funds target-date fund ["CCJTX"], and an unrelated church bond issuer — only the NYSE "CCJ" / "CAMECO CORP" row is the target), `last` field, timestamp **2026-09-10 19:02:18 UTC** |
| Change vs. prior close | **−$2.82 / −2.81%** | IBKR `get_price_snapshot` `change` field |
| Bid / Ask | $97.41 / $97.51 | IBKR `get_price_snapshot` |
| 52-week range | Low **$77.54** · High **$135.18** | IBKR `get_price_snapshot` `misc_statistics` (13w high $111.50, 13w low $83.19, 26w high $131.10) |
| US 10Y Treasury yield | 4.80% | FRED `DGS10`, as-of 2026-09-08 |

**$97.59 is used as the live price for this session.** Today's −2.81% move is well short of the >15% "unexplained move" Rule 9 trigger and is noted as context only, per "never act on price movement alone." The stock is currently ~28% off its 52-week high and ~26% above its 52-week low — mid-range.

---

## 2. Data Gathered — Sources & Method

### 2.1 TTM reconstruction (Q3 2025 – Q2 2026)

No 10-K/annual report has been filed since FY2025 (period ended 2025-12-31); the most current audited/reviewed data available is Cameco's Q2 2026 quarterly filing (period ended 2026-06-30). TTM figures below are reconstructed by summing the four most recent reported quarters (Q3'25, Q4'25 [as the 2025-12-31 quarterly column], Q1'26, Q2'26), each pulled directly from quarterly income statement/cash-flow data — same reconstruction method used in prior sessions (e.g. IREN 2026-07 sessions) when a fresh annual filing isn't yet available.

**Income statement, TTM ($ millions):**

| | Q3'25 | Q4'25 | Q1'26 | Q2'26 | **TTM** |
|---|---|---|---|---|---|
| Revenue | 614.555 | 1,200.930 | 845.365 | 813.772 | **3,474.622** |
| Gross Profit | 170.250 | 272.797 | 301.584 | 190.136 | **934.767** |
| EBIT | 28.694 | 300.863 | 185.656 | 58.330 | **573.543** |
| EBITDA | 87.802 | 387.775 | 252.753 | 130.491 | **858.821** |
| Operating Income | 82.511 | 204.322 | 164.148 | 74.139 | **525.120** |
| Net Income | (0.141) | 199.066 | 130.751 | 25.219 | **354.895** |

**Cash flow, TTM ($ millions):**

| | Q3'25 | Q4'25 | Q1'26 | Q2'26 | **TTM** |
|---|---|---|---|---|---|
| Operating Cash Flow | 155.716 | 677.325 | (22.276) | 131.033 | **941.798** |
| CapEx | (92.510) | (109.134) | (77.739) | (106.494) | **(385.877)** |
| **Free Cash Flow** | 63.206 | 568.191 | (100.015) | 24.539 | **555.921** |

**Balance sheet, as of 30 Jun 2026 ($ millions):**

| | Value |
|---|---|
| Total Debt (long-term, carrying value; no separate finance-lease line disclosed) | 996.750 |
| Cash and cash equivalents | 1,112.718 |
| Total Shareholders' Equity (incl. minority interest) | 7,133.809 |
| Long-Term Equity Investment (Westinghouse JV, equity-method — see Glossary) | 2,906.851 |

```
Net Debt (30 Jun 2026) = Total Debt − Cash = 996.750 − 1,112.718 = (115.968)   ($M, net CASH position)
Invested Capital        = Total Debt + Equity − Cash
                         = 996.750 + 7,133.809 − 1,112.718 = 7,017.841   ($M)
```

### 2.2 FY-level history for 3yr CAGR and FCF-positivity check ($ millions)

| | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Revenue | 1,868.003 | 2,587.758 | 3,135.772 | 3,481.933 |
| Gross Profit | 233.291 | 561.666 | 782.582 | 970.273 |
| Net Income | 89.382 | 360.847 | 171.853 | 589.577 |
| Free Cash Flow | 161.159 | 534.505 | 693.653 | 1,075.407 |

Gross margin by year: FY2023 **21.71%** → FY2024 **24.96%** → FY2025 **27.87%** — a clear, structural 3-year expansion trend (uranium price recovery flowing through to margin, not a one-quarter blip).

### 2.3 Westinghouse — equity-method investment, not consolidated (data-quality flag)

Cameco holds a **49% joint-venture stake in Westinghouse Electric Company** (with Brookfield Renewable/Brookfield Infrastructure holding the balance), accounted for under the **equity method** (see Glossary): Westinghouse's own revenue and operating costs are **not** included in Cameco's Revenue, EBIT, or EBITDA above — only Cameco's *share of Westinghouse's net income* flows into Cameco's own Net Income, as a largely non-cash "equity earnings" line below the operating-income line. Per Cameco's Q2 2026 earnings materials (Investing.com transcript, cameco.com Q2 2026 press release), Q2 2026 net earnings ($25M) and adjusted net earnings ($77M) were both **down sharply YoY specifically because of reduced Westinghouse equity earnings** versus a strong prior-year comparable quarter (Q2 2025 included ~US$170M of Westinghouse equity-earnings contribution tied to the Dukovany, Czech Republic reactor-construction project).

**This matters for the Quality Score calculation below**: the ~$2.9B carrying value of the Westinghouse investment sits inside the ROIC denominator (Invested Capital, §2.1) via the Equity line, but none of Westinghouse's earnings power shows up in the EBIT numerator — mechanically depressing the computed ROIC relative to Cameco's *total* (uranium + Westinghouse) economic earning power. Flagged transparently rather than adjusted around, consistent with "never invent or estimate financial data" — the formula is applied literally as defined in [quality-scoring.md](../framework/quality-scoring.md), with this caveat shown for the record.

### 2.4 Moat evidence — cited sources

- **Market share (TRUE):** Cameco is the world's **second-largest uranium producer**, behind only Kazakhstan's Kazatomprom, accounting for **~14% of global uranium production in 2025** (Crux Investor company profile, cross-referenced against multiple industry sources). Cited as stable/leading share in a concentrated, oligopolistic global market.
- **Brand premium (not credited):** No pricing-power evidence beyond standard commodity/contract-structure dynamics (already credited separately under Switching Costs below) — uranium is a fungible commodity, no brand premium applies.
- **Network effect (not credited):** No documented network-effect mechanism for a physical commodity miner.
- **Switching costs (TRUE):** Cameco's uranium is sold almost entirely under **multi-year, reserved-capacity-style long-term supply contracts** — per its Q2 2026 disclosures, the current contract portfolio supports average annual deliveries of **over 28 million lbs U3O8 for the next five years**, with contract terms specifying escalating price floors (high-US$70s/lb) and ceilings (~US$160/lb escalated). Nuclear utility customers face substantial re-qualification/licensing costs and safety-critical supply-chain diligence to switch fuel suppliers, and multi-year contracts lock in volumes well in advance — a genuine, cited switching-cost mechanism, not just a named-customer announcement.
- **Scale cost advantage (TRUE):** Cameco's McArthur River mine (Saskatchewan) is a **Tier-1** asset (see Glossary) — among the world's highest-grade uranium deposits, with a disclosed average cash cost of **~US$11.24/lb U3O8**, well below prevailing spot/contract prices and in the lowest-cost quartile globally (Energy Intelligence, Cameco's own technical disclosures). This is specific cost-per-unit data versus the broader industry, meeting the framework's evidentiary bar.

**Moat_Score = 3 of 5 signals TRUE = 60.0.**

### 2.5 TAM / pricing-power qualitative evidence

Documented tailwinds cited in Cameco's own Q2 2026 disclosures and independently reported news: (1) Westinghouse's AP1000 reactor pipeline stands at **91 reactors**, backed by a conditional US Department of Energy commitment of **$17.5 billion** to accelerate deployment; (2) AI-datacenter-driven electricity demand growth is broadly cited across the nuclear-power sector (consistent with the IREN session's independent NVIDIA/data-center-power theme) as a structural demand driver for new nuclear buildout and thus uranium fuel demand; (3) Cameco's own long-term contracting strategy (escalating floors/ceilings, §2.4) is explicit evidence of improving pricing power versus its historical spot-price-exposed contract book. This is credited as a **+10 TAM/pricing-power modifier** to the Growth sub-score below.

**Countervailing note (not applied as a −10 "structural deceleration" modifier):** TTM revenue (§2.1, $3,474.622M) is essentially flat/slightly below FY2025's full-year figure ($3,481.933M), and Q2 2026 revenue was down 7% YoY per the earnings-call summary — attributed by management to Westinghouse equity-earnings timing and quarter-to-quarter delivery-schedule lumpiness under the long-term contract book, not a structural TAM/demand reversal. Since the framework's −10 modifier requires *documented* evidence of *structural* (not cyclical) deceleration, and management's own commentary characterizes this as timing/cyclical, it is **not applied** — but the near-term flatness is flagged here for transparency rather than silently ignored.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF positive 3+ consecutive years | FY2022: **$161.159M** · FY2023: **$534.505M** · FY2024: **$693.653M** · FY2025: **$1,075.407M** — 4 consecutive positive years | disqualify if not 3 consecutive positive years | **✅ PASSES.** Comfortably clears, with FCF growing each year. |
| Net Debt/EBITDA over threshold (2.5× standard; not asset-light eligible) | Net Debt is **negative** (net cash position, §2.1: −$115.968M) against positive TTM EBITDA $858.821M | disqualify if exceeds 2.5× | **✅ PASSES.** Net cash — no leverage risk at all. |
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | FY2023: 534.505/360.847 = **148.1%** · FY2024: 693.653/171.853 = **403.7%** · FY2025: 1,075.407/589.577 = **182.4%** | disqualify if 2+ consecutive years <70% w/o carve-out | **✅ PASSES.** Every year well above 70% — strong, consistent cash conversion. |

**No hard disqualifiers fire.** Proceed to the weighted Quality Score.

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = 354.895 / 3,474.622 = 10.21%
  NetMargin_Component = clamp((10.21/30)×100, 0, 100) = 34.0

  EBIT (TTM) = 573.543
  Invested Capital = 7,017.841   (§2.1 — includes the ~$2.9B Westinghouse equity-method
                                   investment in the denominator; see §2.3 data-quality flag)
  ROIC = 573.543 / 7,017.841 = 8.17%
  ROIC_Component = clamp((8.17/30)×100, 0, 100) = 27.2

  Raw Profitability_Score = (34.0 + 27.2) / 2 = 30.6
  FCF-positivity cap check: FCF-positive 4 consecutive years (§3.1) → no cap applies.
  Profitability_Score = 30.6

MARGINS (15% weight):
  Gross Margin (TTM) = 934.767 / 3,474.622 = 26.90%
  GrossMargin_Score = clamp((26.90/80)×100, 0, 100) = 33.6
  Structural trend bonus: gross margin below 40% threshold BUT structurally expanding
    3 straight fiscal years (§2.2: 21.71% → 24.96% → 27.87%) → +10 (capped at 100.0)
  Margins_Score = 33.6 + 10 = 43.6

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022 $1,868.003M → FY2025 $3,481.933M, most recently completed
    3-year window per the rolling-window clarification)
    = (3,481.933 / 1,868.003)^(1/3) − 1 = 23.08%
  Growth_Score = clamp((23.08/25)×100, 0, 100) = 92.3
  TAM/pricing-power modifier (§2.5, cited DOE/Westinghouse AP1000 pipeline + AI-power demand
    + escalating contract floors/ceilings): +10
  Growth_Score = clamp(92.3 + 10, 0, 100) = 100.0   (saturated)

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM) = (115.968) / 858.821 = −0.135×   (net cash — favorable)
  BalanceSheet_Score = clamp(100 × (1 − (−0.135)/4), 0, 100) = clamp(103.4, 0, 100) = 100.0

MOAT SIGNAL (15% weight):
  1. Market share stable/growing — TRUE (§2.4: ~14% of global uranium production, 2025,
     #2 producer globally).
  2. Brand premium — not credited (commodity; no distinct pricing-power evidence beyond
     contract structure, already captured under Switching Costs).
  3. Network effect — not credited (no documented mechanism).
  4. Switching costs — TRUE (§2.4: multi-year reserved-capacity contracts, 28M+ lbs/yr
     average deliveries next 5 years, utility re-qualification costs).
  5. Scale cost advantage — TRUE (§2.4: McArthur River Tier-1 mine, ~US$11.24/lb cash cost,
     cited cost-per-unit data vs. industry).
  Moat_Score = (3/5) × 100 = 60.0

FCF QUALITY (10% weight):
  FCF/NI (TTM) = 555.921 / 354.895 = 156.7%
  Both FCF and NI are positive this period (not a sign-cancellation artifact like the IREN
    2026-09-10 session's negative/negative case) — ratio taken at face value.
  FCFQuality_Score = clamp(((1.567 − 0.40)/0.60)×100, 0, 100) = clamp(194.4, 0, 100) = 100.0

QUALITY SCORE = 30.6×0.25 + 43.6×0.15 + 100.0×0.20 + 100.0×0.15 + 60.0×0.15 + 100.0×0.10
             = 7.650 + 6.540 + 20.000 + 15.000 + 9.000 + 10.000
             = 68.190 → rounds to 68.2
```

**Quality Score = 68.2 / 100.0 — no hard disqualifier fires, but the weighted score falls short of the 80.0+ gate by 11.8 points.** The shortfall is concentrated almost entirely in **Profitability** (30.6/100, the lowest sub-score, 25% weight) — Cameco's TTM net margin (10.2%) and ROIC (8.2%, further depressed by the Westinghouse equity-method treatment per §2.3) reflect a still-early-stage recovery from a multi-year uranium-price trough, not yet the >15–22% margin/ROIC levels this framework's Profitability scale rewards. **Gate result: FAIL.**

---

## 4. Phase 02 / Order Setup — NOT PRODUCED

Per [quality-scoring.md](../framework/quality-scoring.md) and the operating brief, a company must clear the 80.0+ Quality Score gate before Phase 02 valuation scoring, the Composite Score, or any fair-value/order-setup work is produced. CCJ falls short (68.2 vs. 80.0 required) — **no Rate Environment Gate, valuation score, Composite Score, fair value, or order setup is computed this session.**

---

## 5. Data Gaps Flagged

1. **No FY2026 10-K/40-F-equivalent annual filing exists yet** (FY2025 is the latest full fiscal year; the fiscal year ends 31 December, so FY2026 won't be reported until early-to-mid 2027) — TTM reconstruction from the four most recent quarters (§2.1) is used in its place, consistent with this framework's standard TTM-reconstruction method.
2. **Westinghouse's standalone financials are not independently pulled** — Cameco discloses its equity-method share of Westinghouse's results but not a full standalone Westinghouse income statement/balance sheet; the ROIC data-quality flag (§2.3) is noted rather than resolved, since attempting to "correct" ROIC by imputing Westinghouse's standalone earnings would require data this session doesn't have and risks estimating rather than sourcing figures — consistent with "never invent or estimate financial data."
3. No other data gaps — every figure used in the Quality Score computation is a directly reported primary financial-statement figure (Yahoo Finance/`yfinance`-mirrored quarterly and annual filings) or a cited qualitative source (Cameco's own Q2 2026 earnings materials, Crux Investor, Energy Intelligence).

---

## 6. Qualitative Notes

1. **This is a genuinely improving-quality cyclical, not a structurally broken business.** Every hard disqualifier passes cleanly and comfortably (net cash balance sheet, 4 consecutive years of growing FCF, strong FCF/NI conversion), and three of five moat signals are credited with real citations (market share, contract-driven switching costs, Tier-1 cost-curve position). The gate failure is a single-cause story: Profitability (margin/ROIC) hasn't yet caught up to the rest of the business's improving fundamentals.
2. **The Westinghouse JV is a real complication for the Profitability sub-score specifically** (§2.3) — it inflates the ROIC denominator (its ~$2.9B carrying value sits in Invested Capital) without contributing to the EBIT numerator, and its equity-earnings contribution to Net Income is lumpy and quarter-to-quarter volatile (as seen in the Q2 2026 YoY earnings decline). A future re-score, if Westinghouse's earnings power stabilizes or grows (DOE-backed AP1000 pipeline, §2.5), could see Net Margin and reported Net Income benefit even without a change in the uranium business itself — worth watching, but not scored today absent standalone Westinghouse data.
3. **Uranium-price cycle context**: Cameco's steadily improving gross margin (21.7% → 27.9% over FY2023–FY2025) and FCF growth track the ongoing uranium bull market and Cameco's shift toward higher-priced long-term contracts. If this trend continues, Profitability and Margins sub-scores both have a plausible path to improve at the next re-score — this is the single most important thing to watch for CCJ specifically, more than any qualitative catalyst.
4. **No fundamental red flags found.** No going-concern language, no leverage concern (net cash), no customer-concentration disclosure comparable to IREN's, no near-term debt maturity wall identified in the reviewed data.

---

## Recommendation

# **WATCHLIST ONLY — Quality Score gate FAILS (68.2, below the 80.0+ threshold), no hard disqualifier fires. Do not proceed to valuation scoring or any order setup. Track for re-score as margins/ROIC continue recovering with the uranium price cycle.**

CCJ clears every hard disqualifier comfortably and shows real, cited moat evidence (market share, contract-based switching costs, Tier-1 low-cost production) — this is not a "pass on the business" call. It is a **"not yet, on profitability" call**: the weighted Quality Score is held back almost entirely by TTM Net Margin (10.2%) and ROIC (8.2%), both still recovering from a multi-year sector trough and (for ROIC specifically) mechanically depressed by the Westinghouse equity-method accounting treatment (§2.3). **This does not count as a BUY, TRIM, or EXIT trigger** — no position is opened, and no valuation/fair-value work is warranted until the quality gate is cleared.

---

## 7. Next Review Trigger

- **CCJ's next quarterly earnings release** (Q3 2026, expected ~November 2026) — will show whether the margin-expansion trend (§2.2, §6.3) continues and whether TTM Profitability metrics improve enough to approach the 80.0+ gate.
- **Standard Rule 9 triggers:** a material new long-term uranium supply contract, a Westinghouse-specific material event (reactor project win/loss, DOE funding development), management change, macro shift (uranium spot price shock), or a >15% *unexplained* price move.
- **Gate-proximity watch:** if a future re-score's Profitability sub-score alone rose into the mid-50s–60s (net margin/ROIC continuing to climb with the uranium cycle), the overall Quality Score would plausibly cross 80.0 even with Margins/Moat unchanged — worth a fresh full re-score at the next quarterly earnings release regardless of whether a specific trigger fires.

---

## 8. Watchlist & Stale-Score Housekeeping

- **New dated watchlist entry created:** [watchlist/not-in-portfolio/CCJ/CCJ-2026-09-10.md](../watchlist/not-in-portfolio/CCJ/CCJ-2026-09-10.md) — first-ever entry for this ticker.
- **Stale-score mechanism:** not applicable — this is CCJ's first-ever score under the current (2026-06-29) methodology; nothing to clear in [watchlist/STALE.md](../watchlist/STALE.md).

---

## 9. Glossary

- **CAGR**: Compound Annual Growth Rate — the smoothed yearly growth rate from a start to an end value.
- **Composite Score**: this framework's blended 0.0–100.0 ranking (Quality + Valuation, 50/50) — not computed this session, since CCJ never clears the Quality Score gate required to reach it.
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **Equity-method investment (JV)**: an accounting treatment for a significant-but-non-controlling stake (like Cameco's 49% Westinghouse JV) where only the investor's share of net income — not the investee's own revenue/costs — flows into the investor's financials, largely as a non-cash line below operating income (§2.3).
- **FCF / FCF Yield / FCF/NI conversion ratio**: Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check).
- **Gross Margin**: Gross Profit ÷ Revenue.
- **Hard disqualifier**: a Quality Score condition that fails a company regardless of its weighted score — none fire for CCJ this session (§3.1).
- **Invested Capital**: debt + equity − cash, the ROIC denominator.
- **Moat**: a durable competitive advantage protecting a business's profits from competitors — scored 60.0 (3 of 5 signals) for CCJ this session (§3.2).
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate — CCJ is net cash, so this ratio is negative/favorable (§3.1, §3.2).
- **Net Margin**: Net Income ÷ Revenue — CCJ's TTM figure is 10.2% (§3.2).
- **Quality Score**: this framework's 0.0–100.0 quality grading system; a company must score 80.0+ to reach Phase 02 valuation scoring. CCJ scores 68.2 this session — below the gate.
- **ROIC**: Return on Invested Capital — CCJ's TTM figure is 8.2%, depressed in part by the Westinghouse equity-method treatment (§2.3, §3.2).
- **Tier-1 mine/asset**: industry shorthand for a mine in the lowest-cost, highest-margin quartile of the global cost curve — Cameco's McArthur River mine is Tier-1 (§2.4).
- **TTM (Trailing Twelve Months)**: the most recent 12 months of reported results, reconstructed here from the four most recent quarterly filings (§2.1) since no fresh annual filing exists yet.
- **U3O8 (triuranium octoxide)**: "yellowcake," the standard commercial form of uranium before enrichment — uranium production/contracts are quoted in pounds of U3O8 (§2.4).

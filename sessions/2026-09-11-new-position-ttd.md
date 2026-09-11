# NEW POSITION — TTD (The Trade Desk, Inc.) — 2026-09-11

**Task type:** NEW POSITION (fresh full re-run per instruction — no numbers carried over from the 2026-06-12 session)
**Date:** 11 Sep 2026
**10Y US Treasury Yield:** 4.95% (TradingEconomics, 11 Sep 2026)
**Rate Regime Modifier (would apply if the gate were reached):** +5 (10Y in the 3.5–5% bracket) — **not applied; this session does not reach the Rate Environment Gate (see §3)**
**Current TTD portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Technology — AdTech (Demand-Side Platform / programmatic advertising)
**Scoring methodology in force:** Quality Score + 80.0+ gate + Composite Score, version 2026-06-29 ([quality-scoring.md](../framework/quality-scoring.md), [valuation-scoring.md](../framework/valuation-scoring.md))

---

## 0. Methodology note — why this session's gate treatment differs from 2026-06-12

The 2026-06-12 session ([sessions/2026-06-12-new-position-ttd.md](2026-06-12-new-position-ttd.md)) applied the **old binary Phase 01 screen** — a hard "Net Margin >15%" pass/fail line — because that session ran *before* the 2026-06-29 Quality Score engine existed. Per [quality-scoring.md](../framework/quality-scoring.md): *"This replaces the old binary Phase 01 screen as the eligibility gate (the individual hard disqualifiers below still apply *in addition* to the score)."* Under the current methodology, Net Margin is no longer a standalone pass/fail line — it is one input to the weighted **Profitability sub-score**, and the only things that can fail a company outright regardless of score are the three named **hard disqualifiers** (FCF/NI conversion, Net Debt/EBITDA, FCF-positivity). This session runs the full graded Quality Score per the current engine, not the retired binary test.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$13.98** | IBKR `get_price_snapshot`, contract_id 248755440 (NASDAQ:TTD), last trade, +0.07% intraday |
| Bid / Ask | $13.98 / $14.04 | IBKR live snapshot |
| 52-week high | $56.39 | IBKR `misc_statistics` |
| 52-week low | $12.83 | IBKR `misc_statistics` |
| 13-week high | $20.53 | IBKR `misc_statistics` |
| 26-week high | $28.64 | IBKR `misc_statistics` |
| Open 52 weeks ago | $46.30 | IBKR `misc_statistics` |
| Cross-check | $13.97, "lowest level since January 2019" | WebSearch (stockanalysis.com/CNN aggregation), consistent with IBKR to the cent |

TTD has fallen a further **~27.5%** since the 2026-06-12 session's $19.29 (itself already down >86% from 2024 highs). From the 2024 all-time high near $140, today's $13.98 represents a **>90% drawdown**. Per Rule 0, the IBKR live snapshot is used as the price of record — no inference from multiples, no reliance on the prior session's price.

---

## 2. What changed since 2026-06-12 (Rule 9 fundamental triggers)

Three independent Rule 9 triggers have fired since the last session, all pointing the same direction:

1. **Q2 FY2026 earnings (6 Aug 2026)** — revenue $715.1M, **+3% YoY** (a sharp deceleration from Q1 FY2026's +12% and Q2 FY2025's +19%), missing consensus ($752.1M expected) by ~5%. GAAP net income $64.4M (9.0% margin, down from $90.1M / 13.0% margin in Q2 FY2025). Non-GAAP EPS $0.34 missed consensus by ~15%. CEO Jeff Green, on the earnings call: *"We underperformed our own expectations for two main reasons: macro conditions have made it more difficult for some of the world's largest brands to grow, and we didn't execute as well as we could have."* (Sources: [Nasdaq/businesswire Q2 2026 release](https://www.nasdaq.com/press-release/trade-desk-reports-second-quarter-2026-financial-results-2026-08-06), [GuruFocus Q2 2026 call highlights](https://www.gurufocus.com/news/9015077/the-trade-desk-inc-ttd-q2-2026-earnings-call-highlights-navigating-macro-headwinds-with-strategic-innovation-and-strong-jbp-growth), [BigGo Finance Q2 2026 call summary](https://finance.biggo.com/news/US_TTD_2026-08-06))
2. **Q3 FY2026 guidance** — "revenue of at least $650 million" vs. Q3 FY2025's $739.43M actual — **an implied ~12% YoY decline**, which would be the first revenue decline in company history if it holds. (Source: Q2 FY2026 press release / BigGo Finance headline "Q3 Guidance Points to 12% Drop.")
3. **Workforce reduction announced 3 Sep 2026** — ~15% of total workforce (~575 employees across 21+ countries, out of 3,843 FTEs at FY2025-end), $39–51M cash restructuring charge, "substantially completed" in Q3 2026. Management frames it as "reallocation of resources" rather than distress, but it lands 4 weeks after a guided first-ever revenue decline. (Sources: [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/trade-desk-reduce-workforce-approximately-133357942.html), [GuruFocus](https://www.gurufocus.com/news/9068306/the-trade-desk-ttd-announces-workforce-reduction-of-approximately-15-in-organizational-realignment), [CFO Dive](https://www.cfodive.com/news/trade-desk-cuts-15-workforce/829838/))

Separately, competitive-dynamics reporting (Digiday, Wedbush) documents **Amazon DSP taking share from TTD among some large advertisers** in 2026, citing Amazon's first-party shopper-data advantage and new supply partnerships (Disney, Roku) — this is used as Moat Signal evidence in §4 below, not as an independent trigger.

None of this is "price movement alone" — every item above is a documented fundamental event (earnings miss, guidance cut, restructuring, competitive-share reporting), consistent with Rule 9 and the "never act on price alone" non-negotiable.

---

## 3. Data Gathered — TTM Roll-Forward (Phase 01 / Quality Score Inputs)

TTM computed as Q3 FY2025 + Q4 FY2025 + Q1 FY2026 + Q2 FY2026 (the four most recently completed quarters as of 11 Sep 2026). All quarterly figures cross-checked between stockanalysis.com's financials/cash-flow pages (sourced from TTD's own 10-Q/8-K filings) and the individual earnings-release WebSearches above; no figure is estimated.

| Quarter | Revenue | Gross Profit | Gross Margin | Operating Income (EBIT) | Net Income | Net Margin | OCF | CapEx | FCF |
|---|---|---|---|---|---|---|---|---|---|
| Q2 FY2025 | $694.04M | $543.06M | 78.25% | $116.78M | $90.13M | 12.99% | $165.01M | $45.24M | $119.77M |
| Q3 FY2025 | $739.43M | $577.28M | 78.07% | $161.22M | $115.55M | 15.63% | $224.69M | $66.34M | $158.35M |
| Q4 FY2025 | $846.79M | $683.70M | 80.74% | $256.87M | $186.95M | 22.08% | $311.59M | $26.32M | $285.27M |
| Q1 FY2026 | $688.86M | $506.89M | 73.58% | $66.65M | $40.00M | 5.81% | $391.81M | $112.74M | $279.06M |
| Q2 FY2026 | $715.06M | $530.72M | 74.22% | $101.58M | $64.39M | 9.01% | $153.59M | $13.23M | $140.37M |

(Source: [stockanalysis.com/stocks/ttd/financials](https://stockanalysis.com/stocks/ttd/financials/) and [.../cash-flow-statement](https://stockanalysis.com/stocks/ttd/financials/cash-flow-statement/), quarterly view — figures sourced from TTD's own 10-Q/8-K filings, cross-checked against the Q2 FY2026 businesswire/Nasdaq release for the latest quarter.)

**TTM figures (Q3 FY2025 → Q2 FY2026):**

| Metric | TTM Value | Computation |
|---|---|---|
| **TTM Revenue** | **$2,990.14M** | 739.43 + 846.79 + 688.86 + 715.06 |
| **TTM Net Income** | **$406.89M** | 115.55 + 186.95 + 40.00 + 64.39 |
| **TTM Net Margin** | **13.61%** | 406.89 / 2,990.14 |
| **TTM Gross Profit** | **$2,298.59M** | 577.28 + 683.70 + 506.89 + 530.72 |
| **TTM Gross Margin** | **76.88%** | 2,298.59 / 2,990.14 |
| **TTM EBIT (Operating Income)** | **$586.32M** | 161.22 + 256.87 + 66.65 + 101.58 |
| **TTM OCF** | **$1,081.68M** | 224.69 + 311.59 + 391.81 + 153.59 |
| **TTM FCF** | **$863.05M** | 158.35 + 285.27 + 279.06 + 140.37 |
| **TTM FCF/NI conversion** | **212.1%** | 863.05 / 406.89 |

**Other inputs:**

| Metric | Value | Source |
|---|---|---|
| FY2022 Revenue | $1,578M | Prior session (unchanged historical fact); Trade Desk FY2022 8-K |
| FY2023 Revenue | $1,946M | Trade Desk FY2023 10-K/8-K |
| FY2024 Revenue | $2,440M | Trade Desk FY2024 10-K/8-K |
| FY2025 Revenue | $2,896.28M | = 616 (Q1) + 694.04 (Q2) + 739.43 (Q3) + 846.79 (Q4); matches prior session's independently-sourced $2,896.284M |
| **Revenue CAGR 3yr (FY2022→FY2025)** | **22.43%** | (2,896.28 / 1,578)^(1/3) − 1. FY2025 is still the latest *completed* fiscal year as of 11 Sep 2026 (TTD's fiscal year = calendar year) — this is the correct trailing 3yr window, unchanged from June's figure since no new fiscal year has closed. |
| Gross margin FY2023 / FY2024 / FY2025 | 81.2% / 80.7% / 78.6% | WebSearch (MacroTrends), corroborated by prior session |
| ROIC (TTM, GuruFocus) | 24.11% | [GuruFocus TTM ROIC](https://www.gurufocus.com/term/roic/TTD) — computed off TTM income-statement data |
| ROIC (quarterly-annualized, Jun 2026, GuruFocus) | 15.01% | Same GuruFocus page — a different (single-quarter-annualized) methodology; both bases clear the informal >15% reference point, but the TTM basis (24.11%) is used below for consistency with every other TTM input in this session |
| Cash + ST investments (30 Jun 2026) | $1.12B + $362.4M = **$1.4824B** | Q2 FY2026 8-K/press release (via WebFetch of stocktitan.net) |
| Total financial debt | $0.0 (debt-free; a ~$434M figure some aggregators show is operating-lease liability, not financial debt) | Multiple aggregators, consistent with prior session's "zero debt" finding |
| **Net cash position** | **$1.4824B** (net debt negative) | Computed |
| Diluted shares outstanding | 469.9M (Q2 FY2026) | Q2 FY2026 press release (via WebFetch) |
| Buyback activity | $163.5M repurchased Q1 FY2026, $422.9M Q4 FY2025; TTM buyback/SBC ratio ≈2.03× (repurchases exceed stock-based-comp dilution); diluted share count down ~4.3% YoY / ~1.5% over 5 years | WebSearch aggregation (financecharts.com, ycharts.com) |
| Customer retention | >95% for 11 consecutive years (reaffirmed on the Q2 FY2026 call) | Q2 FY2026 earnings materials |
| Forward PE | ~12.8–14.1× (source variance) | GuruFocus, ~4 Sep 2026 |

### Data gaps / flags

1. **ROIC has a two-basis spread (24.11% TTM vs. 15.01% quarterly-annualized)** from the same GuruFocus source page — both clear a >15% reference, so this does not change which side of any threshold TTD lands on; the TTM figure (24.11%) is used for consistency with the rest of this session's TTM convention.
2. **Gross margin's "structurally expanding" alternative test does not apply here** — TTD's gross margin is comfortably above the 40% level test (76.88% TTM), so the quality-scoring.md trend-bonus clause (which only fires for sub-40% margins moving up) is not triggered either way; the contracting trend (81.2% FY2023 → 78.6% FY2025 → 76.88% TTM) is noted as context but does not generate a bonus or an automatic penalty under the current Margins sub-score formula (level-only).
3. **Moat Signal "market share stable or growing"** — no company-filed or third-party (e.g. eMarketer/IDC) 2026 DSP market-share percentage was found showing TTD's share explicitly rising or falling; the evidence available is qualitative reporting (Digiday: "advertisers starting to shop around"; a Wedbush analyst note flagging intensifying Amazon DSP competition) plus TTD's own guided revenue deceleration to an implied Q3 decline. Per "never invent or estimate," this signal is marked **not demonstrated** (not TRUE) rather than invented as either direction from a hard percentage that doesn't exist in the sources found — see §4.
4. **Moat Signal "scale cost advantage"** — no cost-per-unit data (e.g., cost per impression/bid vs. smaller independent DSPs) was found; "largest independent DSP" is a scale *fact* but not a cost-per-unit *comparison*, which is what the checklist row requires. Marked **not demonstrated** rather than assumed true from scale alone.
5. **No metric in this session was invented or estimated.** Every TTM figure is a direct roll-forward of eight individually-sourced quarterly figures (four quarters × two metrics each, for revenue/NI/EBIT/FCF), cross-checked across two independent aggregations (stockanalysis.com quarterly financials/cash-flow, plus the original earnings-release WebSearches for the newest quarter).

---

## 4. Quality Score (Phase 01) — Full Calculation

### Hard disqualifier check (fail regardless of weighted score)

| Disqualifier | TTD Status | Fires? |
|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years | TTM 212.1%; every quarter in the TTM window individually FCF-positive with FCF well above net income | ❌ No |
| Net Debt/EBITDA over threshold (2.5× standard) | Net **cash** $1.4824B, zero financial debt — ratio is negative | ❌ No |
| Not FCF-positive for 3+ consecutive years | FCF positive every quarter shown above (and every fiscal year 2023–2025) | ❌ No |

**No hard disqualifier fires.**

### Sub-scores

**Profitability (25% weight)**
```
NetMargin_Component = clamp((13.61 / 30) × 100, 0, 100) = 45.4
ROIC_Component       = clamp((24.11 / 30) × 100, 0, 100) = 80.4
Profitability_Score  = (45.4 + 80.4) / 2 = 62.9   (no FCF cap — FCF-positive well beyond 3yr)
```

**Margins (15% weight)**
```
GrossMargin_Score = clamp((76.88 / 80) × 100, 0, 100) = 96.1
```
No trend bonus (bonus clause applies only to sub-40% margins trending up — not applicable at 76.88%). Margins_Score = **96.1**.

**Growth (20% weight)**
```
Growth_Score(base) = clamp((22.43 / 25) × 100, 0, 100) = 89.7
```
**Modifier — structural deceleration, −10.** Evidence: revenue growth has decelerated for five straight quarters on a consistent YoY basis — Q1 FY2025 +25% → Q2 FY2025 +19% → Q1 FY2026 +12% → Q2 FY2026 +3% → Q3 FY2026 guided to an **implied ~12% YoY decline** (§2). This is corroborated by (a) management's own admission of "execution missteps" (not purely macro), (b) documented competitive share pressure from Amazon DSP (§2, §"Moat" below), and (c) a 15%-workforce restructuring announced the same month — three independent, cited signals pointing the same direction, not a single noisy quarter. This clears the "documented... not cyclically" bar in [quality-scoring.md](../framework/quality-scoring.md). A generic CTV/retail-media TAM-expansion narrative exists industry-wide but was not found with TTD-specific, decisive evidence strong enough to offset the specific, quantified deceleration above — so the +10 TAM/pricing-power modifier is **not** applied this session (see sensitivity note below).
```
Growth_Score = 89.7 − 10 = 79.7
```

**Balance Sheet (15% weight)**
```
Net Debt = −$1.4824B (net cash) → BalanceSheet_Score = 100.0 (clamped)
```

**Moat Signal (15% weight)**

| Signal | TTD | Cited evidence | TRUE? |
|---|---|---|---|
| Market share stable or growing | Not demonstrated | No current hard share-percentage data found either direction (see gap #3); available qualitative reporting (Digiday, Wedbush) documents advertisers "shopping around" and Amazon DSP gains against TTD in 2026 | ❌ FALSE |
| Brand premium | Not demonstrated | B2B, spend-based platform; no pricing-power/ASP-style evidence found | ❌ FALSE |
| Network effect | Documented | TTD is a demand-side platform (DSP) aggregating advertiser demand against open-internet publisher supply — a two-sided marketplace where more advertiser budget attracts more supply-side integrations and vice versa; further reinforced by UID2 (Unified ID 2.0), TTD's open-source cookie-alternative identity framework adopted across the ad-tech ecosystem, which strengthens as more publishers/advertisers adopt it | ✅ TRUE |
| Switching costs | Documented | >95% customer retention sustained for 11 consecutive years (reaffirmed Q2 FY2026), even through the current stock/business turmoil — strong evidence of real integration depth (Kokai platform, agency data workflows), not just satisfaction | ✅ TRUE |
| Scale cost advantage | Not demonstrated | "Largest independent DSP" is a scale fact, not a cited cost-per-unit comparison vs. smaller competitors (see gap #4) | ❌ FALSE |

```
Moat_Score = (2 / 5) × 100 = 40.0
```

**FCF Quality (10% weight)**
```
FCFQuality_Score = clamp(((2.121 − 0.40) / 0.60) × 100, 0, 100) = clamp(286.8) = 100.0
```

### Final Quality Score

```
Quality Score = (62.9 × 0.25) + (96.1 × 0.15) + (79.7 × 0.20) + (100.0 × 0.15) + (40.0 × 0.15) + (100.0 × 0.10)
              = 15.725 + 14.415 + 15.940 + 15.000 + 6.000 + 10.000
              = 77.08 → rounds to 77.1
```

## **Quality Score: 77.1 — FAILS the 80.0+ gate.**

### Sensitivity note (shown per "no black-box outputs")

This is a close call in a different way than June's: no hard disqualifier fires, and every sub-score is individually defensible, but the total sits **2.9 points below the gate**. Two judgment calls could move it, shown for transparency — neither is applied above because neither clears this framework's "never mark a signal true without a cited source" bar:

- If the Growth modifier were treated as a wash (TAM +10 and deceleration −10 both applied, netting to 0, instead of −10 alone): Quality Score = 79.1 — **still fails**.
- If Moat Score were credited at 3/5 (crediting "scale cost advantage" from "largest independent DSP" without a specific cost-per-unit citation): Quality Score would rise to ~80.1–82.1 depending on the Growth treatment — **would pass**. This was not applied because the checklist explicitly requires a cost-per-unit citation for that row, which was not found.

Under the most defensible, fully-cited reading of the evidence gathered this session, **TTD fails the Quality Score gate at 77.1**, and does not proceed to the Rate Environment Gate, Phase 02 valuation score, or Composite Score.

---

## 5. Recommendation

# **PASS — do not open a position now. Watchlist, no significant-change conditions changed from FAIL, but the reasoning and the underlying number are materially different from June.**

TTD fails the current Quality Score gate at **77.1** (vs. the 80.0+ bar), driven by a middling Profitability sub-score (TTM net margin has *worsened* to 13.61% from June's 14.56%) and a Moat Score of only 40.0 (2 of 5 signals cited) — the first time this framework has scored TTD's moat under the graded checklist, and it lands weaker than the qualitative "strong moat" characterization from June, because this session's evidence search turned up documented competitive share pressure (Amazon DSP) rather than share-stability proof, and no cost-per-unit citation for a scale advantage.

Unlike June's near-miss (a 0.44pp net-margin gap under the old binary test, sitting on top of an otherwise-comfortable pass), this session's picture is **not** "one number away from passing" — it fails on a weighted blend of profitability, growth (now penalized for a documented, multi-quarter, structural deceleration culminating in a guided first-ever revenue decline), and moat, even though the balance sheet (net cash) and FCF quality (212% conversion) remain excellent. The CEO's own March 2026 ~$148M insider purchase (cited in the June session) is now underwater by roughly 44–47% at today's $13.98 versus his $23.49–$25.08 buy range — a data point that argues for management conviction but does not offset the deteriorating trailing financials the gate is built to measure.

**No Turnaround Sub-Gate (Upgrade 4) follow-up is warranted this session** — that path requires the standard gate to have failed *narrowly* on an otherwise-strong quality profile; this session's Moat Score downgrade and the specific, sourced Q3 guidance for a revenue *decline* (not just deceleration) are a stronger, more current signal than a single-metric near-miss, and pursuing an independent fair-value estimate on top of a 2.9-point quality-score shortfall (with several of that shortfall's inputs freshly downgraded, not merely persisting) would risk exactly the "dress up a name the quality screen says isn't there yet" failure mode this framework has flagged before (CIEN precedent, cited in the June session).

**Recommended next steps:**
1. **Primary trigger — Q3 FY2026 earnings** (expected ~November 2026): this is the quarter TTD has explicitly guided to a revenue *decline*. Re-run the Quality Score with the new TTM window. If growth stabilizes (even at low-single-digit growth rather than an actual decline) and margins hold or recover, the Growth sub-score modifier and the Moat "market share" signal should both be revisited with fresh evidence.
2. **Workforce-restructuring completion** (expected substantially done by end of Q3 2026, per the 3 Sep 2026 announcement) — worth checking whether margin metrics (net margin, EBIT margin) show the intended improvement once the $39–51M charge rolls off and the lower cost base takes effect.
3. **Immediate re-score trigger** if a >15% unexplained price move occurs from $13.98 in either direction (Rule 9) — TTD's volatility (down ~27.5% just since June, now at its lowest level since January 2019) makes this a realistic near-term possibility.
4. **Moat Signal follow-up (optional, doesn't require earnings timing):** locate a cited third-party DSP market-share series (e.g. eMarketer, WARC, or a sell-side ad-tech note with a specific 2026 percentage) to resolve the "market share stable or growing" signal definitively rather than leaving it as "not demonstrated" — and a cost-per-impression/bid comparison vs. smaller independent DSPs to resolve "scale cost advantage." Either signal flipping to TRUE would materially change the gate outcome (see sensitivity note in §4).

---

## 6. Next Review Trigger

- **Q3 FY2026 earnings** (expected ~November 2026) — mandatory Rule 9 re-score. Specifically: does revenue actually decline YoY as guided, or beat the "at least $650M" floor meaningfully? Does net margin stabilize?
- **Workforce-restructuring completion** (expected substantially done Q3 2026) — check for margin recovery evidence.
- **>15% unexplained price move from $13.98 in either direction** — immediate re-score per Rule 9.
- **No position opened by this session — nothing to log in `decisions/`.**

---

## Glossary

- **DSP (Demand-Side Platform)** — see [glossary.md](../framework/glossary.md).
- **CTV (Connected TV)** — see [glossary.md](../framework/glossary.md).
- **Kokai** — see [glossary.md](../framework/glossary.md).
- **UID2 (Unified ID 2.0)** — see [glossary.md](../framework/glossary.md).
- **Quality Score**, **Hard disqualifier**, **Moat Signal**, **Composite Score**, **Rate Environment Gate**, **Rate Regime Modifier**, **Rule 0**, **Rule 9**, **Turnaround Sub-Gate**, **FCF/NI conversion ratio**, **Owner Earnings**, **SBC (Stock-Based Compensation)** — all defined in [glossary.md](../framework/glossary.md).
- **TTM** — Trailing Twelve Months: the sum of the four most recently completed quarters, used throughout this framework instead of stale fiscal-year figures.
- **ROIC** — Return on Invested Capital: after-tax operating profit divided by the capital (debt + equity, net of cash) used to generate it — a measure of how efficiently a company turns invested capital into profit.
- **EBIT** — Earnings Before Interest and Taxes, i.e. operating income — a profitability measure unaffected by capital structure or tax jurisdiction.
- **FCF (Free Cash Flow)** — Operating Cash Flow minus Capital Expenditures — the cash a business generates after the reinvestment needed to sustain/grow it.
- **YoY** — Year-over-Year: comparing a period to the same period one year earlier.
- **8-K / 10-Q / 10-K** — SEC filings: 8-K discloses a material event (e.g. earnings release) shortly after it happens; 10-Q is the unaudited quarterly report; 10-K is the audited annual report.

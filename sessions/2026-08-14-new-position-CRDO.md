# New Position Evaluation — CRDO (Credo Technology Group Holding Ltd, NASDAQ)

**Task:** NEW POSITION
**Date:** 14 Aug 2026
**10Y US Treasury Yield:** 4.65% (most recent posted close, 13–14 Aug 2026, per TradingEconomics/FRED — [CNBC](https://www.cnbc.com/2026/08/14/treasury-yields-us-iran-economic-sanctions.html))
**Rate Regime Modifier:** +10 total (+5 Step 1 Earnings Yield Spread fail, +5 Step 2 — 10Y in the 3.5–5% bracket) — see §4.
**Current CRDO portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md)).
**Prior coverage:** None. Confirmed absent from both [watchlist/in-portfolio/](../watchlist/in-portfolio/) and [watchlist/not-in-portfolio/](../watchlist/not-in-portfolio/) — this is a first-ever evaluation of this ticker.
**Sector:** Technology — Semiconductors (fabless; high-speed connectivity for AI/hyperscaler datacenters: Active Electrical Cables, PCIe retimers, optical DSPs, licensed SerDes IP). Cayman Islands-domiciled, NASDAQ-listed. Fiscal year ends ~30 April.
**Trigger:** Direct user request for a full end-to-end `/new-position` evaluation.
**First-use jargon:** see closing Glossary (§11).

---

## 1. Data gaps flagged

- **5-year historical PE range/average is not computable.** CRDO IPO'd on Nasdaq in January 2022 (~4.6 years of trading history, short of the 20-quarter/5-year lookback) and was loss-making (negative TTM EPS, PE undefined) for the large majority of that history — GAAP net income only turned positive in FY2025, with FY2026 the first fully "clean" profitable year. Per [valuation-scoring.md](../framework/valuation-scoring.md)'s explicit caveat ("if fewer than 5 years of TTM EPS are reconstructable, treat it as the no-history fallback"), **FwdPE_Score = 50.0 (neutral, flagged)** is used rather than inventing a historical range that doesn't exist.
- **WACC is a constructed modeling assumption, not a vendor-sourced figure** — built from the risk-free rate (10Y Treasury, 4.65%) plus a standard equity risk premium (~5%) plus a company-specific risk adjustment for customer concentration/execution risk, per DCF Rule 2's explicit instruction to construct WACC this way. Full derivation shown in §6.
- **Peer EV/EBIT comps were not fully available** — only Forward PE was cleanly sourced across a 5-peer set (ALAB, MRVL, AVGO, LITE, COHR); EV/EBITDA was found for only 2 of the 5 (ALAB, MRVL), too thin a sample for a reliable median. The Forward PE peer-median comp (Rule 5, 5 peers, median used) is used as the multiples method instead — see §6.2.
- **ROIC (73.10%, stockanalysis.com) is a vendor-computed figure** — a rough independent cross-check using NOPAT ÷ (Equity+Debt−Cash) lands materially lower (~40–60%, methodology-dependent on how much of the $1.4B+ cash pile is treated as "excess"). This does **not** change the Quality Score outcome: the Profitability sub-score's ROIC component clamps to 100.0 at any ROIC ≥30%, so the exact figure above that threshold is immaterial here — flagged for transparency, not because it changes anything.
- None of these gaps block the evaluation or change its outcome — see §9.

---

## 2. Live Price (Rule 0)

Fetched directly from IBKR real-time market data (contract ID 541265127, NASDAQ), not inferred from multiples:

| Field | Value |
|---|---|
| **Live price (intraday, real-time)** | **$260.19** |
| Change vs. prior close | −$5.80 (**−2.18%**) |
| Today's range | $255.50 – $266.62 (open $264.25) |
| 52-week range | $86.49 – $308.67 |
| Today's volume | ~1.17M shares |
| Bid / Ask | $259.50 / $260.52 |
| Analyst consensus PT | ~$208–$279 across sources (wide dispersion); most-recent individual targets: Susquehanna $250 (21 Jul 2026), Barclays $300 (20 Jul 2026) — [Benzinga](https://www.benzinga.com/quote/CRDO/analyst-ratings), [MarketScreener](https://www.marketscreener.com/quote/stock/CREDO-TECHNOLOGY-GROUP-HO-132401547/consensus/) |

**Market cap (derived from live price, not vendor-cached):** $260.19 × 186.48M shares outstanding = **$48,520.23M**.

---

## 3. Phase 01 — Quality Score (0–100.0)

Per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29. All figures are real, filed GAAP figures sourced from [stockanalysis.com's CRDO financials](https://stockanalysis.com/stocks/crdo/financials/), [balance sheet](https://stockanalysis.com/stocks/crdo/financials/balance-sheet/), [cash flow statement](https://stockanalysis.com/stocks/crdo/financials/cash-flow-statement/), and [statistics page](https://stockanalysis.com/stocks/crdo/statistics/). FY2026 (ended ~30 April 2026) is CRDO's most recently completed fiscal year and the closest available TTM proxy — Q1 FY2027 has not yet been reported as of this session.

### Hard disqualifiers — checked first (rolling-window basis, per the 2026-08-05 clarification)

| Disqualifier | Result | Evidence |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | Does **not** fire | Annual FCF: FY2022 −$48.41M, FY2023 −$46.33M, **FY2024 +$17.09M, FY2025 +$29.02M, FY2026 +$407.00M** — the current rolling 3-year window (FY2024–FY2026) is uniformly positive. |
| **Net debt/EBITDA over threshold (2.5×)** | Does **not** fire | Net position is **net cash**, not net debt: $20.62M total debt vs. $1,165M cash + $278.33M short-term investments = **net cash $1,423M**. |
| **FCF/NI conversion ratio <70% for 2+ consecutive years, no growth-capex explanation** | Does **not** fire | Current rolling window: FY2025 ratio = 29.02/52.18 = 55.6% (<70%), **FY2026 ratio = 407.00/472.28 = 86.18% (≥70%)**. Only one of the two most recent years is below 70% — the "2+ consecutive years" condition requires both. |

**Result: no hard disqualifier fires.** Full weighted calculation shown below regardless, per "no black-box outputs."

### Sub-score calculations

**Profitability (25% weight)**
```
TTM (FY2026) Net Margin = 472.28 / 1,335.00 = 35.38%
TTM ROIC (stockanalysis.com) = 73.10%

NetMargin_Component = clamp((35.38/30)×100, 0, 100) = 100.0   (>30%, capped)
ROIC_Component       = clamp((73.10/30)×100, 0, 100) = 100.0   (>30%, capped — see §1 sourcing note)
Profitability_Score  = (100.0 + 100.0) / 2 = 100.0
```
No FCF-positive-3yr cap applies (already satisfied above).

**Margins (15% weight)**
```
FY2026 Gross Margin = 908.35 / 1,335.00 = 68.04%
GrossMargin_Score = clamp((68.04/80)×100, 0, 100) = 85.05
```
No structural-trend-below-40% bonus applies (gross margin is already well above 40% — the +10 bonus is specifically for margins expanding *while below* the 40% threshold). Trend for reference: FY2022 60.12% → FY2023 57.65% → FY2024 61.89% → FY2025 64.77% → FY2026 68.04% — genuinely expanding, just not eligible for the below-40% bonus.

**Growth (20% weight)**
```
Revenue 3yr CAGR (FY2023 $184.19M → FY2026 $1,335.00M) = (1,335.00/184.19)^(1/3) − 1 = 93.5%/yr
Growth_Score (raw) = clamp((93.5/25)×100, 0, 100) = 100.0 (already capped)
```
Documented TAM-expansion evidence (would add +10, already capped): AI-datacenter demand for AECs, PCIe retimers, and optical DSPs is scaling faster than most incumbents' capacity — Credo held an estimated **73% share of the AEC market** as of Q2 2025 per research firm 650 Group ([mlq.ai](https://mlq.ai/earnings/highlight/CRDO-credo-plans-to-double-aec-market-with-ne-9535fb/)), guides **>80% FY2027 revenue growth** with $600M+ from its newly-acquired optical (Dust Photonics) portfolio, and is pioneering a new "Active LED Cable" (ALC) category projected to more than double the addressable AEC market ([Seeking Alpha](https://seekingalpha.com/news/4599516-credo-signals-80-percent-fiscal-2027-revenue-growth-with-600m-expected-from-optical-portfolio)).

**Balance Sheet (15% weight)**
```
Net Debt = Total Debt ($20.62M) − Cash ($1,165M) − ST Investments ($278.33M) = −$1,422.71M (net cash)
FY2026 EBITDA = EBIT ($445.01M) + D&A (positive) > 0
Net Debt/EBITDA = negative / positive = negative ratio (net cash against positive operating earnings)
BalanceSheet_Score = clamp(100×(1 − ND/EBITDA/4), 0, 100) = 100.0   (net cash vs. positive EBITDA is unambiguously the best-case reading — unlike the AAOI/LCID negative-EBITDA ambiguity, no judgment call needed here)
```

**Moat Signal (15% weight)** — checklist, cited evidence only:

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | 73% AEC market share as of Q2 2025 per 650 Group (third-party market research), [mlq.ai](https://mlq.ai/earnings/highlight/CRDO-credo-plans-to-double-aec-market-with-ne-9535fb/). |
| Brand premium | FALSE | No citable price-increase-without-volume-loss evidence found; CRDO sells into price-sensitive hyperscaler procurement processes. |
| Network effect | FALSE | Not applicable — a component/IP supplier, not a multi-sided platform. |
| Switching costs | **TRUE** | Hyperscaler qualification testing (reliability-at-scale, power/cost validation) is a documented multi-quarter-to-multi-year process before a competing part can be designed in — the same mechanism this framework has credited for AAOI/LITE/COHR peers. Design wins convert to *years* of locked-in production revenue once qualified. [spheniscidae007.substack.com](https://spheniscidae007.substack.com/p/credo-technology-group-holding-ltd) |
| Scale cost advantage | FALSE | No citable cost-per-unit-vs-smaller-competitors figure found in this session. |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10% weight)**
```
FY2026 FCF/NI ratio = 407.00 / 472.28 = 86.18%
FCFQuality_Score = clamp(((0.8618 − 0.40)/0.60)×100, 0, 100) = 76.97
```

### Final Quality Score

```
Quality Score = 100.0×0.25 + 85.05×0.15 + 100.0×0.20 + 100.0×0.15 + 40.0×0.15 + 76.97×0.10
              = 25.000 + 12.7575 + 20.000 + 15.000 + 6.000 + 7.697
              = 86.4545 → rounds to 86.5
```

**Quality Score = 86.5 — clears the 80.0+ gate.** Proceeding to Phase 02.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test:**
```
Forward PE (live price / consensus FY2027 EPS $6.22) = 260.19 / 6.22 = 41.83×
EY = 1 / 41.83 = 2.39%
Spread = EY − 10Y Treasury = 2.39% − 4.65% = −2.26pp   (< +1.5% threshold → fails)
```
Fails → **+5 additive** (yellow flag, not a veto, per the 2026-06-07 softening).

**Step 2 — Rate Regime Modifier:** 10Y yield 4.65% falls in the 3.5–5% bracket → **+5**.

**Total Rate Regime Modifier = +10.**

**Step 3 (Rate-Normalised PE)** — N/A this session (annual January task, top-5-holdings only).

---

## 5. Phase 02 — Valuation Score (raw sub-scores)

**Fast Grower / PEG eligibility check:** CRDO's EPS growth is explosive in dollar terms, but the earnings base is **not** a "reliable, non-distorted 3+ year" base per the 2026-06-20 clarification — GAAP net income was negative in FY2022–FY2024 and only turned positive in FY2025 (first year) and FY2026 (second year). This is the same "recently turned profitable" carve-out already applied to DUOL — **PEG is not scored; its 15% weight redistributes to EV/EBIT (→ 40% weight).**

**FCF Yield (40% weight):**
```
FCF Yield = TTM FCF / Market Cap = 407.00 / 48,520.23 = 0.839%
FCF_Score = clamp(100×(1 − 0.839/10), 0, 100) = 91.61
```

**EV/EBIT (40% weight, redistributed from PEG):**
```
EV = Market Cap + Total Debt − Cash − ST Investments = 48,520.23 + 20.62 − 1,165.00 − 278.33 = 47,097.52M
EV/EBIT = 47,097.52 / 445.01 = 105.84×
EV/EBIT_Score = clamp((105.84 − 12)/23 × 100, 0, 100) = 100.0   (capped — far above the 35× ceiling)
```

**Forward PE (20% weight):**
```
No-history fallback (see §1): FwdPE_Score = 50.0 (neutral, flagged)
```

**Raw weighted score:**
```
Raw = 91.61×0.40 + 100.0×0.40 + 50.0×0.20
    = 36.644 + 40.000 + 10.000
    = 86.644
```

---

## 6. Fair Value Work (feeds the Upside/Downside Modifier, §7)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rules 1–8: two methods (DCF + comparable multiples), 3 scenarios each, triangulated 40% DCF / 60% Multiples.

### 6.1 DCF (3-stage, per Rule 2)

**Base case** — Stage 1 (yrs 1–5, FY27–31) revenue growth decelerating from the company's own >80% FY2027 guidance toward a more moderate pace; Stage 2 (yrs 6–10, FY32–36) fades to a 3% terminal rate; FCF margin assumed to hold near CRDO's current 30.5% (FY2026 actual), rising modestly to 33% as scale/SerDes-licensing mix improves. WACC = 4.65% risk-free + ~5% ERP + ~1.35% company-specific (customer-concentration/execution) premium ≈ **11%**.

| FY | Revenue ($M) | Growth | FCF margin | FCF ($M) | Discount factor (11%) | PV ($M) |
|---|---|---|---|---|---|---|
| 2027 | 2,400 | 80% | 31.0% | 744.0 | 0.9009 | 670.3 |
| 2028 | 3,480 | 45% | 31.5% | 1,096.2 | 0.8116 | 889.7 |
| 2029 | 4,524 | 30% | 32.0% | 1,447.7 | 0.7312 | 1,058.5 |
| 2030 | 5,519 | 22% | 32.5% | 1,793.7 | 0.6587 | 1,181.5 |
| 2031 | 6,513 | 18% | 33.0% | 2,149.3 | 0.5935 | 1,275.6 |
| 2032 | 7,490 | 15% | 33.0% | 2,471.7 | 0.5346 | 1,321.5 |
| 2033 | 8,389 | 12% | 33.0% | 2,768.4 | 0.4817 | 1,333.5 |
| 2034 | 9,144 | 9% | 33.0% | 3,017.5 | 0.4339 | 1,309.3 |
| 2035 | 9,693 | 6% | 33.0% | 3,198.7 | 0.3909 | 1,250.4 |
| 2036 | 9,984 | 3% | 33.0% | 3,294.7 | 0.3522 | 1,160.6 |

```
Sum PV (explicit 10yr)         = $11,450.9M
Terminal Value (g=3%) = 3,294.7×1.03/(0.11−0.03) = $42,418.9M
PV(Terminal Value)             = $14,940.1M
Terminal Value weight of total = 14,940.1/26,391.0 = 56.6%  (< 75% — Rule 4 OK)
Total EV (DCF)                 = $26,391.0M
+ Net cash                     = $1,423.0M
Equity Value                   = $27,814.0M
÷ Shares outstanding (186.48M) = $149.15/share  ← DCF Base
```

**Bull case** (25% weight): FY2027 rev $2,600M (+95%, above guidance high end), slower deceleration (55/38/28/22%), FCF margin ramping 32%→36%, WACC 10%, terminal g=3.5%.
```
Sum PV FCF (10yr) = $17,345.5M; PV(TV) = $31,004.9M; Total EV = $48,350.4M
+ Net cash $1,423M = $49,773.4M ÷ 186.48M = $266.85/share  ← DCF Bull
```

**Bear case** (25% weight): FY2027 rev $2,069M (+55%, below guidance — reflecting a growth miss driven by customer-concentration risk), faster deceleration (25/15/10/8%), FCF margin held flat at 25–28% (competitive/margin pressure), WACC 12%, terminal g=2.5%.
```
Sum PV FCF (10yr) = $5,022.3M; PV(TV) = $4,221.6M; Total EV = $9,243.9M
+ Net cash $1,423M = $10,666.9M ÷ 186.48M = $57.20/share  ← DCF Bear
```

### 6.2 Comparable Multiples (Rule 5 — 5 peers, median used)

**Peer set** (semiconductor/optics suppliers to AI-datacenter interconnect, forward PE, sourced 14 Aug 2026):

| Peer | Forward PE |
|---|---|
| Astera Labs (ALAB) | 125.29× |
| Lumentum (LITE) | 55.74× |
| Coherent (COHR) | 49.00× |
| Marvell (MRVL) | 38.54× |
| Broadcom (AVGO) | 21.97× |
| **Median** | **49.00×** |

*(Source: [GuruFocus AVGO](https://www.gurufocus.com/term/forward-pe-ratio/AVGO), search-aggregated stockanalysis.com/GuruFocus data for ALAB/MRVL/LITE/COHR.)*

```
Base:  Consensus FY2027 EPS $6.22 × peer median 49.0×          = $304.78
Bull:  High-end FY2027 EPS estimate $7.04 × 75× (re-rating toward upper peer band, below ALAB's outlier)  = $528.00
Bear:  Low-end FY2027 EPS estimate $5.54 × 21.97× (AVGO-level, mature/derated)                            = $121.71
```
*(FY2027 EPS range $5.54–$7.04, consensus $6.22, per [stockanalysis.com forecast data](https://stockanalysis.com/stocks/crdo/forecast/).)*

### 6.3 Triangulated Blended Fair Value (40% DCF / 60% Multiples)

| Scenario | DCF | Multiples | Blended (40/60) |
|---|---|---|---|
| Bull | $266.85 | $528.00 | **$423.54** |
| Base | $149.15 | $304.78 | **$242.53** |
| Bear | $57.20 | $121.71 | **$95.91** |

**Divergence flagged:** DCF and Multiples methods disagree meaningfully in every scenario (DCF consistently well below Multiples) — a known DCF limitation for hyper-torque compounders, where a 10-year explicit+fade horizon and a conservative terminal growth rate structurally understate value relative to what the market (and comparable peers) are willing to pay for continued execution. The 40/60 blend is used as specified by the framework rather than picking one method; shown transparently per Rule 3 ("output a range, not a single point").

```
PW Fair Value = 0.25×423.54 + 0.50×242.53 + 0.25×95.91 = 105.885 + 121.265 + 23.9775 = $251.13
```

---

## 7. Upside/Downside Modifier (Expected-Return Modifier)

```
Gap Upside % = (PW FV / Live Price) − 1 = (251.13 / 260.19) − 1 = −3.48%
```
**Catalyst/timeline (Rule 10):** no specific dated catalyst identifiable within 18–24 months for this modest gap to close in either direction — the stock sits close to (just above) this session's own scenario-weighted fair value, not at a large, catalyst-dependent mispricing. Default 2-year window used per the framework's explicit fallback.
```
Annualized gap = −3.48% / 2yr = −1.74%/yr
```

**Intrinsic growth rate:** +9.0%/yr — the average of this session's own DCF Stage 2 (yrs 6–10) fade-period growth assumptions (15/12/9/6/3%), representing the normalized, post-hypergrowth structural growth rate once the current AI-buildout supercycle matures (not the near-term 45–90% explosive rate, which is already fully captured in the DCF/Multiples fair-value estimate above and would double-count if reused here).

**Shareholder yield:** −3.60%/yr. CRDO pays no dividend and has not repurchased shares — GuruFocus's 5-Year Share Buyback Ratio is **−3.60%**, and shares outstanding have grown every year since IPO (+16.81% in 2025 alone); TTM net common equity issued was $1.121B ([Trefis](https://www.trefis.com/data/companies/CRDO)). Used directly as sourced rather than approximated.

```
E = Annualized gap + Intrinsic growth + Shareholder yield
  = −1.74% + 9.00% + (−3.60%)
  = +3.66%/yr
```

**Step 2 — map E to M** (hurdle H=10%, `0 ≤ E < H` branch):
```
M = +5 × (H − E)/H = +5 × (10 − 3.66)/10 = +5 × 0.634 = +3.17
```

**Sensitivity disclosed (not official):** if the two fair-value methods were used individually rather than blended — DCF-only PW FV ≈ $155.30 (gap −40.3%, would swing E sharply negative, pushing M toward the guardrail-capped upside ceiling of −5 on the attractive side, or well into +10–15 on the trim side depending on catalyst framing) vs. Multiples-only PW FV ≈ $314.82 (gap +21.0%, would swing M toward −10 to −11, deep into "attractive"). The official 40/60 blend (M = +3.17) sits between these extremes, as intended by triangulation.

---

## 8. Final Valuation Score & Composite Score

```
Final Valuation Score = Raw (86.644) + Rate Regime Modifier (+10.00) + Upside/Downside Modifier (+3.17)
                       = 99.814 → rounds to 99.8
```

| | Value |
|---|---|
| **Quality Score** | **86.5** (PASSES 80.0+ gate) |
| **Final Valuation Score** | **99.8** |

```
Composite Score = 0.50 × (100 − 86.5) + 0.50 × 99.8
                = 0.50 × 13.5 + 0.50 × 99.8
                = 6.75 + 49.90
                = 56.65 → boundary rule (.X5 rounds UP) → 56.7
```

**Composite Score = 56.7 — falls in the 50.0–69.9 "HOLD — watch only, no new entry, no trim (Fair Value)" band.**

---

## 9. Order Setup

**Not run.** Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Step 2's integration table, a Composite Score of 50.0–69.9 maps to **"No MoS → Watchlist only"** — order setup (buy price, sell target, stop loss, R/R, position size) is only computed for Score 0.0–49.9 (Buy) or the Trim/Exit bands on an existing holding, neither of which applies here.

For reference only: Blended (PW) Fair Value = **$251.13**, vs. live price $260.19 — the stock trades modestly (3.5%) above this session's own scenario-weighted fair value, not at a deep discount that would support a margin-of-safety-based entry.

---

## 10. Recommendation

# **WATCHLIST ONLY — do not enter. Composite Score 56.7 sits in the 50.0–69.9 "Fair Value / Hold" band — CRDO is an excellent-quality business (Quality Score 86.5, comfortably above the 80.0+ gate) but is not currently priced to offer an attractive entry under this framework's discipline.**

CRDO's fundamentals are genuinely outstanding: dominant AEC market share (73%), explosive but real revenue growth (93.5% 3yr CAGR, guided >80% again for FY2027), a net-cash balance sheet, and strong FCF conversion (86.2% FCF/NI). The Quality Score of 86.5 reflects this — it is one of the higher quality scores this framework has computed for a recent-IPO growth name.

But the valuation is extreme by every absolute yardstick this framework applies: trailing PE >100×, EV/EBIT ~106× (the sub-score caps out at the maximum 100.0 well before reaching CRDO's actual multiple), and a forward PE (41.8×) that only earns a neutral 50.0 sub-score because CRDO's trading history is too short and too recently loss-making to construct a real historical range — not because the multiple itself is cheap. The Rate Environment Gate adds a full +10 on top (both the Earnings Yield Spread test and the current 3.5–5% Treasury bracket work against the score). The one factor pulling the score back down is the Upside/Downside Modifier, and even there the effect is modest (+3.17, not negative) — CRDO's own scenario-weighted fair value ($251.13) sits close to, not far below, the live price, so there isn't a large mean-reversion gap to lean on even after crediting a generous 9%/yr structural growth rate.

Net: **high quality alone is not sufficient for a new entry under this framework** — the price already reflects a great deal of the company's excellent trajectory. This is watchlist material, not a buy.

---

## 11. Next Review Trigger

- **CRDO's Q1 FY2027 earnings release**, expected ~September 2026 — the next scheduled full re-derivation, and the point at which one more quarter of TTM data becomes available for the Forward PE no-history-fallback flag (still short of the 5-year/20-quarter threshold, but incrementally closer).
- **A pullback toward or below this session's own PW Fair Value (~$251)** would meaningfully improve the entry case, though as §7 shows, even a full round-trip to fair value only produces a thin, not deeply attractive, expected-return picture given CRDO's structural dilution — a genuine double-digit discount to $251, not just a return to it, is what this framework's Composite Score math would need to see to cross into a Buy band.
- **Customer-concentration developments** — a tiny handful of hyperscalers (Amazon, Microsoft, Google) account for the large majority of CRDO's revenue (Amazon alone was 61% of Q4 FY2025 revenue); any signal of in-house-silicon substitution or share loss to Broadcom/Marvell at a major customer would be a Rule 9 fundamental trigger independent of price.
- **The Co-Packaged Optics (CPO) transition** — a longer-horizon (multi-year) disruption vector flagged in this session's qualitative notes below; CRDO's copper/AEC-centric moat is less established in a CPO-dominated future, an area the company is hedging via its Dust Photonics optical acquisition.
- Standard Rule 9 triggers: guidance revision, management change, material M&A, macro shift, or a >15% unexplained price move.

**No position opened — nothing to log in `decisions/`.**

---

## Qualitative Notes (per quality-scoring.md's 5 Qualitative Questions)

1. **Why are margins high?** A mix of premium reliability positioning (Credo's ZeroFlap AECs claim up to 1,000× greater reliability than laser-based optical alternatives at lower power) and a growing high-margin SerDes IP licensing royalty stream layered on top of hardware sales.
2. **What would it take to compete?** A comparable SerDes IP portfolio (28G–224G) plus years of hyperscaler qualification testing and trusted design-in relationships with the same 3 hyperscalers that dominate CRDO's revenue — Broadcom and Marvell are the credible competitive threats given their own scale and IP depth.
3. **Capital allocation track record:** Reinvestment-heavy — R&D and capacity expansion, no dividend, no buybacks (net share issuance instead, including a $1.121B TTM equity raise), and a large net-cash balance sheet ($1.42B) partly funding the Dust Photonics optical acquisition for the FY2027 ramp.
4. **Growth sources next 3–5 years:** Continued AEC/AI-datacenter interconnect ramp, the new optical DSP/1.6T portfolio (Dust Photonics), PCIe retimer design wins converting to production revenue in CY2026, and the new Active LED Cable (ALC) category CRDO projects could more than double the addressable AEC market.
5. **Best bear case:** Extreme customer concentration — a single hyperscaler's move to in-house silicon or a competitor could materially impact results; longer-term, the eventual industry shift toward Co-Packaged Optics (CPO) at 3.2T+ speeds is a disruption vector where CRDO's current copper/AEC moat is less established (§Disruption vector check).
6. **Disruption vector check:** Yes, real — CPO could bypass the pluggable/AEC connectivity layer CRDO currently dominates; the Dust Photonics optical acquisition is a documented hedge, but does not eliminate the risk.

---

## 12. Glossary

Per [operating-brief.md](../framework/operating-brief.md), every jargon term used above, pulled from [glossary.md](../framework/glossary.md). Three new terms were added there this session (AEC, ALC, PCIe retimer, SerDes — see below, marked *New*).

| Term | Meaning |
|---|---|
| **AEC (Active Electrical Cable)** *(New)* | A copper-based, signal-conditioned cabling product for in-rack/short multi-rack AI-datacenter connectivity — CRDO's core product, ~73% market share. |
| **ALC (Active LED Cable)** *(New)* | CRDO's new LED-based connectivity category, projected to more than double the addressable AEC market. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Co-packaged optics (CPO)** | A chip-packaging approach mounting optical components directly beside/inside a switch or accelerator package, bypassing separate pluggable transceivers/cables — the long-horizon disruption vector to CRDO's current AEC-centric moat. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking, `0.50×(100−Quality Score) + 0.50×Valuation Score` — 56.7 for CRDO this session. |
| **D&A** | Depreciation & Amortization. |
| **DCF (Discounted Cash Flow)** | A valuation method estimating value from projected future cash flows discounted to present value. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT — CRDO's is ~105.8×. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury in the Rate Environment Gate. |
| **Fabless** | A chip company that designs but outsources manufacturing to a foundry — CRDO's model. |
| **Fast Grower** | A company growing EPS >15%/yr for 3+ years on a clean, non-distorted earnings base — CRDO does not yet qualify (recently turned profitable). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income — CRDO's FY2026 FCF/NI is 86.18%. |
| **Fwd PE (Forward PE)** | Price ÷ forward-looking expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear) — $251.13 this session. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score; none fired for CRDO. |
| **Hurdle rate** | The minimum acceptable annual return (10%) the Upside/Downside Modifier measures expected return against. |
| **Moat** | A durable competitive advantage; scored 40.0 (2 of 5 signals: market share, switching costs) for CRDO. |
| **Net Debt/EBITDA** | This framework's primary balance-sheet-risk gate; CRDO's is net cash against positive EBITDA — best-case reading. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax. |
| **PCIe (Peripheral Component Interconnect Express) retimer** *(New)* | A signal-conditioning chip for high-speed PCIe links — a CRDO growth product with hyperscaler design wins converting to CY2026 production revenue. |
| **PEG ratio** | PE ÷ earnings growth rate; not scored for CRDO (recently-profitable earnings base). |
| **Quality Score** | This framework's 0.0–100.0 continuous quality score; 80.0+ required for Phase 02. CRDO scored **86.5**. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-score check comparing Earnings Yield to the 10-Year Treasury, plus the additive Treasury-bracket adjustment; +10 total this session. |
| **R/R (Risk/Reward ratio)** | (Expected gain) ÷ (Expected loss); not computed this session — no order setup run (Hold band). |
| **ROIC** | Return on Invested Capital; 73.10% per stockanalysis.com (component clamps to 100.0 regardless of exact methodology above 30%). |
| **Rule 0 / 2 / 3 / 4 / 5 / 6 / 7 / 10** | This framework's standing instructions: always fetch live price first; 3-stage DCF standard; weighted "football field" valuation; sanity-check protocol; comparable company standards (5 peers min, median); normalize before valuing; mandatory scenario analysis (25/50/25); separate intrinsic value from market price with a documented catalyst/timeline. |
| **SerDes (Serializer/Deserializer)** *(New)* | The chip circuit/IP converting parallel data to serial for transmission — CRDO's core underlying technology, also licensed as a royalty stream. |
| **Shareholder yield** | Dividend yield plus net buyback yield — **−3.60%** for CRDO (no dividend, net share issuance/dilution, per GuruFocus). |
| **TAM** | Total Addressable Market. |
| **Treasury yield (10Y)** | This framework's risk-free-rate benchmark; 4.65% this session. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results; approximated here by FY2026 (ended ~30 Apr 2026), CRDO's most recently completed fiscal year. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | The additive ±15 valuation-score adjustment; computed at **+3.17** for CRDO this session (thin, mildly unattractive expected return, E=+3.66%/yr vs. the 10% hurdle). |
| **WACC** | Weighted Average Cost of Capital — the discount rate used in the DCF; 11% base case for CRDO, constructed from the risk-free rate + equity risk premium + a company-specific risk adjustment. |

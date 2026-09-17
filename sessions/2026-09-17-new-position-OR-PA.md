# New Position Evaluation — OR.PA (L'Oréal S.A.)

**Task:** NEW POSITION
**Date:** 17 Sep 2026
**10Y US Treasury Yield:** 4.945% ([CNBC, 17 Sep 2026](https://www.cnbc.com/2026/09/17/treasury-yields-move-lower-after-fed-kicks-off-hiking-cycle.html)) — falls in the 3.5–5% Rate Regime bucket (+5 modifier), but **moot for this session**: the Quality Gate fails before Phase 02 is ever reached, so no Rate Environment Gate / valuation score is computed.
**Sector:** Consumer Defensive — Household & Personal Products (Beauty/Cosmetics)
**Ticker:** OR.PA (Euronext Paris), currency EUR
**Not an existing holding** — confirmed against [portfolio/holdings.md](../portfolio/holdings.md) (not listed). Sourced as an EU quality+value candidate.

---

## 1. Live Price (Rule 0)

Fetched via `yf.Ticker("OR.PA").info` (live snapshot, not inferred from multiples):

| Field | Value |
|---|---|
| **Current/regular market price** | **€380.10** |
| Previous close | €381.90 |
| Day range | €380.10 – €386.30 |
| 52-week range | €338.85 – €405.80 |
| Analyst mean target | €418.42 (24 analysts, consensus "Buy") |
| Market cap | €202.46B |
| Enterprise value | €216.03B |

---

## 2. Phase 01 — Quality Score (full calculation)

All figures pulled directly via `yfinance` (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet`, `t.quarterly_balance_sheet`) — none invented or estimated. Two qualitative growth/moat inputs are backed by cited web sources per quality-scoring.md's "never invent — cite a source" rule for those specific sub-scores.

### Profitability (25% weight)

```
Net Margin (TTM, info.profitMargins)          = 13.90%
  Cross-check FY2025: Net Income 6,127.2M / Revenue 44,052.0M = 13.91%  ✓ consistent

ROIC:
  EBIT (FY2025)        = 8,877.0M
  Pretax Income FY2025  = 8,502.2M
  Tax Provision FY2025  = 2,363.1M  → effective tax rate = 2,363.1 / 8,502.2 = 27.80%
  NOPAT = EBIT × (1 − tax rate) = 8,877.0 × (1 − 0.2780) = 6,409.4M
  Invested Capital (latest quarter, 2026-06-30) = 48,177.2M   ← most current balance sheet, reflects H1 2026 acquisitions
  ROIC = 6,409.4 / 48,177.2 = 13.31%

NetMargin_Component = clamp((13.90 / 30) × 100, 0, 100) = 46.3
ROIC_Component       = clamp((13.31 / 30) × 100, 0, 100) = 44.4
Profitability_Score  = (46.3 + 44.4) / 2 = 45.4

FCF-positive 3+ consecutive years? YES (see FCF Quality below) — no cap applied.
```

### Margins (15% weight)

```
Gross Margin (TTM, info.grossMargins) = 74.38%
GrossMargin_Score = clamp((74.38 / 80) × 100, 0, 100) = 93.0

3yr trend: 72.36% (FY2022) → 73.85% (FY2023) → 74.20% (FY2024) → 74.33% (FY2025)
Mildly expanding, but already well above the 40% threshold, so the "+10 below-40%-but-expanding"
bonus does not apply (that bonus is only for margins below 40%).

Margins_Score = 93.0
```

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 → FY2025, yfinance t.financials):
  Revenue FY2022 = 38,260.6M ; Revenue FY2025 = 44,052.0M
  CAGR = (44,052.0 / 38,260.6)^(1/3) − 1 = 4.81%

Growth_Score (base) = clamp((4.81 / 25) × 100, 0, 100) = 19.2
```

**Qualitative TAM/pricing-power modifier — cited evidence (not invented):**
- L'Oréal holds ~18.7% global beauty-market share, the largest single player, "2–3x larger than any peer."
- The company grew faster than the global beauty market (~+3.8%) in 2026 — Q1 2026 like-for-like growth of +6.7% to +7.6%, an acceleration vs. the 3-year historical revenue CAGR, implying continued market-share gains rather than structural deceleration.
- Sources: [Quality Stocks — L'Oréal, the Leader of Beauty](https://qualitystocks.substack.com/p/loreal-the-leader-of-beauty); [Personal Care Insights — L'Oréal Q1 2026 sales](https://www.personalcareinsights.com/news/loreal-q1-2026-sales.html); [Moodie Davitt Report — North Asia travel retail](https://moodiedavittreport.com/north-asia-travel-retail-remains-challenging-as-loreal-reveals-year-of-outperformance-in-improving-global-beauty-market/)

```
Growth_Score = 19.2 + 10 (documented TAM/market-share-gain evidence) = 29.2
```

### Balance Sheet (15% weight)

```
Latest balance sheet (2026-06-30, quarterly): Total Debt 16,712.6M, Cash 4,048.8M, Net Debt 10,288.4M
FY2025 year-end (2025-12-31): Total Debt 11,916.1M, Cash 9,865.0M, Net Debt 253.7M

Material jump in leverage between FY2025 and H1 2026 — cited and documented, not a data-quality glitch:
L'Oréal financed a wave of 2025–2026 acquisitions (Kering Beauté, Creed, an additional 10% stake in
Galderma, Dr.G, COLOR WOW, Medik8) via bond issuances (€1.75B tranche Jan 2026, ~€3B for Kering Beauté,
a $1B inaugural USD bond). Per L'Oréal's own H1 2026 results release, net debt rose to €12.66B
(gearing 37.4%, up from 5.9%), with **leverage of 1.2× EBITDA** (vs. 0.2× at 2025 year-end).
Source: [L'Oréal 2026 Half-Year Results](https://www.loreal.com/en/press-release/finance/2026-half-year-results/);
[cosmeticsbusiness.com — Kering Beauté bond financing](https://cosmeticsbusiness.com/lor%C3%A9al-funds-kering-beaut%C3%A9-deal-with-%E2%82%AC3bn-bonds).

Using the company-disclosed, most-current figure: Net Debt/EBITDA = 1.2×
(cross-checks reasonably against yfinance-derived TTM figure: 10,288.4M / 10,349.5M TTM EBITDA ≈ 0.99×;
the 1.2× company-reported figure is used as the more authoritative, contemporaneously-disclosed number.)

BalanceSheet_Score = clamp(100 × (1 − 1.2/4), 0, 100) = 70.0
```

Well under the 2.5× standard disqualifier threshold (no asset-light override applicable — this is not a payment network/exchange) — **no Balance Sheet hard disqualifier fires.**

### Moat Signal (15% weight) — checklist, cited evidence only

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | ~18.7% global beauty-market share, largest player; grew faster than the ~3.8% global market in 2026 (Q1 LFL +6.7–7.6%), implying share gains. [Quality Stocks](https://qualitystocks.substack.com/p/loreal-the-leader-of-beauty) |
| Brand premium | **TRUE** | Named among "The 2026 Most Powerful Brands in Beauty" ([WWD](https://wwd.com/beauty-industry-news/beauty-features/lists/beauty-power-brands-2026-1239143216/)); "stronger brands drive shelf space and consumer trust... creates a virtuous cycle" per the same market-analysis source cited above — premium/luxury portfolio (Lancôme, YSL Beauty, Helena Rubinstein, newly-acquired Creed) sustains pricing power. |
| Network effect | **FALSE** | No documented two-sided-marketplace or user-growth-driven-value mechanism identified for a CPG/cosmetics business — not applicable to this business model. |
| Switching costs | **FALSE** | No documented contractual lock-in, integration depth, or migration-cost mechanism found for consumer beauty products (unlike, e.g., subscription software or B2B platforms). |
| Scale cost advantage | **TRUE** | "Business 2–3x larger than any peer," with cited R&D firepower and financial scale (€43.48B revenue) funding volume/cost advantages not available to smaller rivals. [Quality Stocks](https://qualitystocks.substack.com/p/loreal-the-leader-of-beauty) |

```
Moat_Score = (3 / 5) × 100 = 60.0
```

### FCF Quality (10% weight)

```
FCF/NI ratio by year (t.cashflow, t.financials):
  FY2022: 4,935.1 / 5,706.6 = 86.5%
  FY2023: 6,115.9 / 6,184.0 = 98.9%
  FY2024: 6,644.3 / 6,408.7 = 103.7%
  FY2025: 7,161.6 / 6,127.2 = 116.9%

Most recent completed fiscal year (FY2025) used for the score:
FCFQuality_Score = clamp(((1.169 − 0.40) / 0.60) × 100, 0, 100) = clamp(128.2, 0, 100) = 100.0
```

FCF positive all 4 available years (2022–2025) — **no FCF-positivity disqualifier.**
FCF/NI ratio well above 70% every year — **no FCF/NI conversion disqualifier.**

### Hard Disqualifier Check (in addition to the weighted score)

| Disqualifier | Result |
|---|---|
| FCF/NI < 70% for 2+ consecutive years w/o documented growth-capex explanation | **PASS** — ratio ranged 86.5%–116.9% across all 4 available years, never below 70% |
| Net Debt/EBITDA over applicable threshold (2.5× standard) | **PASS** — 1.2× (company-disclosed, post-acquisition), well under 2.5× |
| Not FCF-positive for 3+ consecutive years | **PASS** — positive every year 2022–2025 |

**No hard disqualifier fires.** OR.PA fails on the weighted Quality Score itself, not on a hard disqualifier.

### Final Quality Score

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

            = (45.4 × 0.25) + (93.0 × 0.15) + (29.2 × 0.20)
              + (70.0 × 0.15) + (60.0 × 0.15) + (100.0 × 0.10)

            = 11.35 + 13.95 + 5.84 + 10.50 + 9.00 + 10.00

            = 60.64  →  rounded to nearest 0.1  →  60.6
```

## Quality Score: 60.6 / 100.0 — FAILS the 80.0+ gate

**60.6 is 19.4 points below the strict 80.0+ threshold** ([quality-scoring.md](../framework/quality-scoring.md)). This is a decisive fail, not a knife-edge case (compare to the framework's SGE precedent — a clear fail at 66.8 was still treated as clear; 60.6 is further below that).

### Why it fails — the drivers

- **Profitability (45.4)** is the single biggest drag: a 13.90% net margin and 13.31% ROIC are both well below the 30% scale ceiling this sub-score uses, and both sit below the Phase 01 legacy thresholds (Net margin >15%, ROIC >15%) that the graded score replaces. L'Oréal is a genuinely profitable business, but not profitable enough on this framework's continuous scale to score well here.
- **Growth (29.2, even after the +10 documented market-share-gain credit)** — the historical 3-year revenue CAGR of only 4.81% is well short of the 25% ceiling this sub-score uses (and short of the legacy >10% Phase 01 threshold). L'Oréal's 2026 like-for-like acceleration is a genuine positive (credited via the +10 modifier), but the multi-year reported-revenue base this formula runs on remains low-single-digit.
- **Moat (60.0)** — 3 of 5 signals cleared with cited evidence (market share, brand premium, scale), but network effect and switching costs are not applicable/documented for a consumer cosmetics business — a structural ceiling for this business model on this particular checklist, not a company-specific weakness.
- **Balance Sheet (70.0)** and **FCF Quality (100.0, capped)** are genuine strengths — no hard disqualifier anywhere close to firing.

**STOPPING HERE per the 80.0+ gate rule** ([quality-scoring.md](../framework/quality-scoring.md): "Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks") and per [.claude/commands/new-position.md](../.claude/commands/new-position.md) Step 2. **No Phase 02 valuation score, no Rate Environment Gate, no Composite Score, and no fair-value/order-setup work was performed** — none of that is meaningful for a company that hasn't cleared the quality bar, however attractively priced it might look on multiples alone.

---

## 5. Recommendation

**PASS — do not open a position in OR.PA.** Quality Score 60.6 fails the 80.0+ gate by a wide margin (19.4 points). This is a Phase 01 outcome, not a valuation call — L'Oréal may well be a perfectly good business by ordinary industry standards, but it does not clear this framework's deliberately strict quality bar (set 2026-06-29, "to be loosened later only if it screens out too much of the investable universe" — see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md)). No order setup, buy price, sell target, stop loss, or position sizing was computed — those steps are only meaningful for a name that has passed the Quality Gate.

**Next review trigger:** Quarterly earnings (next expected report per L'Oréal's usual cadence — H1 2026 results already reported 2026-07/08; watch for FY2026 full-year results, typically early/mid-February) or a Rule 9 fundamental event (guidance revision, further M&A, management change). A meaningfully faster multi-year revenue CAGR (LFL growth of +6.5–7.6% sustained long enough to move the trailing 3yr reported-revenue CAGR materially above ~10%) or margin/ROIC expansion would be the concrete path to eventually clearing 80.0 — worth re-checking at the next quarterly cadence rather than sooner.

---

## Data Gaps / Flags

- No hard data gaps that blocked scoring — all quantitative Quality Score inputs were available via `yfinance` (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet`, `t.quarterly_balance_sheet`).
- The Growth and Moat sub-scores' qualitative modifiers rely on cited third-party web sources (listed inline above) rather than `yfinance`, consistent with quality-scoring.md's requirement that TAM/pricing-power and moat-signal evidence never be inferred without a citation.
- A material discrepancy exists between yfinance's TTM-EBITDA-derived Net Debt/EBITDA (≈0.99×) and L'Oréal's own H1 2026-disclosed leverage (1.2×) — the company-disclosed figure was used as authoritative since it reflects the same post-acquisition balance sheet more precisely (their own EBITDA base/definition). Either figure lands well clear of the 2.5× disqualifier threshold, so this does not change the outcome.
- Quarterly income-statement fields (`t.quarterly_financials`) returned empty for this ticker — a `yfinance` coverage gap for this non-US filer. Annual (`t.financials`) and quarterly balance-sheet (`t.quarterly_balance_sheet`) data were both available and used instead; this did not block any required Quality Score input.

---

## Glossary

- **CAGR (Compound Annual Growth Rate)** — the smoothed yearly growth rate that gets you from a start value to an end value over several years. Used here for L'Oréal's 3-year revenue CAGR.
- **EBIT** — Earnings Before Interest and Taxes, operating profit before financing/tax effects. Used in the ROIC (NOPAT) calculation.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization, a rough proxy for cash operating profit. Used in the Net Debt/EBITDA leverage ratio.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether reported accounting profit is turning into real cash. Used for OR.PA's FCF Quality sub-score.
- **Gross Margin** — Gross Profit ÷ Revenue; the percentage of each revenue dollar left after direct production/delivery costs. One of this framework's Quality Score Margins inputs.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted sub-score total (FCF/NI conversion, Net Debt/EBITDA, FCF-positivity). None fired for OR.PA — it failed on the weighted score itself.
- **Invested Capital** — the total capital (debt + equity, netted for cash) put to work in a business; the denominator of the ROIC calculation.
- **Like-for-like (LFL) growth** — a retail/consumer-goods growth metric stripping out currency and portfolio (M&A) effects, isolating organic volume-and-price growth. L'Oréal's headline reported growth figure; cited as documented evidence of market-share gains in the Growth sub-score's +10 modifier.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) protecting a business's profits from competitors.
- **Moat Signal** — this framework's 5-point Quality Score checklist that scores the general Moat concept: market share, brand premium, network effect, switching costs, scale cost advantage. OR.PA scored 3/5.
- **Net Debt/EBITDA** — net debt (total debt minus cash) divided by EBITDA; this framework's primary balance-sheet-risk gate. OR.PA: 1.2× (company-disclosed, post-acquisition).
- **Net Margin** — Net Income ÷ Revenue; the percentage of each revenue dollar left as accounting profit. One of the Profitability sub-score inputs.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate); the numerator used to compute ROIC.
- **Quality Score** — this framework's 0.0–100.0 continuous score grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality); a company must score 80.0+ to proceed to Phase 02 valuation scoring. OR.PA scored 60.6, failing the gate.
- **ROIC (Return on Invested Capital)** — how efficiently a company turns invested capital (debt + equity) into profit; a core quality signal in this framework.
- **TAM (Total Addressable Market)** — the total revenue opportunity available if a company captured 100% of its target market. Cited (via market-share-gain evidence) as a positive Growth sub-score modifier for OR.PA.

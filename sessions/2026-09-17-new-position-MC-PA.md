# NEW POSITION — MC.PA (LVMH Moët Hennessy Louis Vuitton SE)

**Task type:** NEW POSITION
**Date:** 2026-09-17
**10Y US Treasury Yield:** ~5.01% (2026-09-15 close) — for reference only; the Rate Environment Gate is not reached this session (see Phase 01 result below)
**Rate Regime Modifier in effect (if Phase 02 were reached):** +10 (>5% bracket)
**Sector / Industry:** Consumer Cyclical / Luxury Goods (Paris exchange — Euronext Paris)
**Business:** Global luxury conglomerate — Wines & Spirits (Moët & Chandon, Hennessy), Fashion & Leather Goods (Louis Vuitton, Dior, Fendi, Celine, Loewe, Givenchy), Perfumes & Cosmetics, Watches & Jewelry (Bulgari, Tiffany & Co.), Selective Retailing (Sephora, DFS, Le Bon Marché)

---

## 1. Live Price (Rule 0)

Fetched via `yfinance` (`yf.Ticker("MC.PA").info`), 2026-09-17:

| Field | Value |
|---|---|
| Current/regular market price | **€412.30** |
| Previous close | €410.95 |
| Day range | €409.50 – €416.00 |
| 52-week range | **€403.15 – €654.70** |
| Market cap | €203.25B |
| Enterprise value | €229.18B |
| Currency | EUR (native Euronext Paris listing; no ADR used) |

Price fetched live, not inferred from multiples, per Rule 0. Note the stock trades **37% below its 52-week high** — see the market-context note below; this is a real, currently-unfolding fundamental story, not a stale reference.

**Market context (not a scored input, but directly relevant to several sub-scores below):** LVMH shares have fallen roughly 30–37% year-to-date in 2026 amid a well-documented Chinese/global luxury demand slowdown. On 2026-09-15 LVMH fell out of Europe's 10 largest listed companies by market value and lost its spot as France's largest company by market cap to L'Oréal. Louis Vuitton's own brand valuation fell from ~$112B to ~$87.5B (Interbrand/Kantar-style estimates, per press reporting), and Hermès overtook LVMH as the world's most valuable listed luxury company in April 2025. Bain & Company's 2025 Luxury Goods Worldwide Market Study estimates ~60 million "aspirational" middle-income luxury shoppers have exited the category over the past three years, and average European personal-luxury-goods prices rose ~52% from 2019–2024 — commentary attributes deteriorating consumer sentiment partly to "price fatigue" from repeated post-pandemic price hikes. These are used below as cited evidence for the Growth and Moat Signal sub-scores, not invented commentary.

*Sources: [Bain & Company — Global luxury stays resilient](https://www.bain.com/about/media-center/press-releases/20252/global-luxury-stays-resilient-despite-economic-headwinds-and-shifting-consumer-trends-that-reshape-marketbain--company-and-altagamma/), [Blockonomi — LVMH stock plunges amid weakening Chinese luxury market](https://blockonomi.com/lvmh-lvmhf-stock-plunges-to-six-year-low-amid-weakening-chinese-luxury-market), [DesignRush — Louis Vuitton brand value fall](https://news.designrush.com/louis-vuitton-lvmh-brand-value-fall), [CNN — Hermès overtakes LVMH](https://www.cnn.com/2025/04/15/style/hermes-worlds-most-valuable-luxury-company), [The Fashion Law — Inflation, Positioning & China](https://www.thefashionlaw.com/inflation-positioning-china-a-dive-into-luxury-brands-price-increases/), [PurseBop — LV price increases](https://www.pursebop.com/louis-vuitton-europe-price-increase-2025/)*

---

## 2. Phase 01 — Quality Score (full sub-score calculation)

All figures pulled live via `yfinance` (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet`), FY2022–FY2025 (LVMH fiscal year = calendar year). No metric below was invented or estimated — where a figure required a judgment call (the Growth deceleration modifier, and Moat Signal marks), the underlying evidence and the exact number used are shown.

**Conglomerate rule check:** LVMH's segments (Wines & Spirits, Fashion & Leather Goods, Perfumes & Cosmetics, Watches & Jewelry incl. Tiffany & Bulgari, Selective Retailing incl. Sephora/DFS) do not include a material captive financial-services subsidiary comparable to an auto captive-finance arm (e.g. Toyota Financial Services) — LVMH's debt as reported in its consolidated IFRS financial statements (and as pulled via `yfinance`'s `balance_sheet`/`info`) already fully consolidates all group entities, so no additional debt needs to be layered in under the Conglomerate rule. This is noted explicitly rather than silently assumed.

### 2a. Profitability (25% weight)

```
Net Margin (TTM, per yfinance profitMargins) = 13.66%
NetMargin_Component = clamp((13.66/30)×100, 0, 100) = 45.53

ROIC (FY2025):
  EBIT (FY2025)        = €17,849M
  Effective tax rate    = 32.8% (yfinance "Tax Rate For Calcs", FY2025)
  NOPAT                 = 17,849 × (1 − 0.328) = €11,994.5M
  Invested Capital (FYE2025, yfinance) = €87,816M
  ROIC                  = 11,994.5 / 87,816 = 13.66%
ROIC_Component = clamp((13.66/30)×100, 0, 100) = 45.52

Profitability_Score = (45.53 + 45.52) / 2 = 45.52
```

No FCF-positive-3yr cap applies — LVMH has been FCF-positive every year FY2022–FY2025 (see 2f).

### 2b. Margins (15% weight)

```
Gross Margin (TTM, yfinance grossMargins) = 66.37%
GrossMargin_Score = clamp((66.37/80)×100, 0, 100) = 82.96
```

3-year trend (computed from `t.financials`, Gross Profit ÷ Total Revenue per FY):

| FY | Gross Margin |
|---|---|
| 2022 | 68.44% |
| 2023 | 68.81% |
| 2024 | 67.03% |
| 2025 | 66.24% |

Margin trend is **contracting**, not expanding (68.4% → 66.2% over 3 years) — no structural-expansion bonus applies (and none would be needed anyway since gross margin is already well above the 40% threshold that bonus targets).

```
Margins_Score = 82.96
```

### 2c. Growth (20% weight)

```
Revenue (t.financials, Total Revenue):
  FY2022: €79,183M
  FY2023: €86,153M
  FY2024: €84,682M
  FY2025: €80,807M

3yr CAGR (FY2022 → FY2025) = (80,807 / 79,183)^(1/3) − 1 = 0.679%

Growth_Score (raw) = clamp((0.679/25)×100, 0, 100) = 2.72
```

TAM/pricing-power modifier: **no +10 applied** — there is no documented evidence of TAM expansion (the opposite is documented — see market context above). **−10 structural-deceleration modifier applied**, based on the cited Bain & Company finding that ~60 million aspirational luxury consumers have exited the category over the trailing **three years** (a multi-year, not single-quarter, pattern) plus the documented loss of category leadership to Hermès and Louis Vuitton's own brand-value decline — this reads as a structural share/demand shift rather than one cyclical quarter, though it is acknowledged this is the most judgment-laden line in this session and is flagged as such.

```
Growth_Score = clamp(2.72 − 10, 0, 100) = 0.0
```

**Sensitivity check:** even without this modifier (i.e., treating the slowdown as purely cyclical), Growth_Score would be 2.72 rather than 0.0 — a 0.54-point difference in the final weighted Quality Score (see 2g), which does not change the gate outcome either way.

### 2d. Balance Sheet (15% weight)

```
Net Debt (FY2025, yfinance balance_sheet "Net Debt") = €11,550M
EBITDA (FY2025, yfinance financials)                  = €25,850M
Net Debt/EBITDA = 11,550 / 25,850 = 0.4468×

BalanceSheet_Score = clamp(100 × (1 − 0.4468/4), 0, 100) = 88.83
```

Well inside the standard 2.5× Debt Gate threshold — no asset-light override needed or applicable (LVMH is not a payment network/exchange).

### 2e. Moat Signal (15% weight)

Checklist scored strictly against cited evidence — no signal marked TRUE without a source:

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable or growing | **FALSE** | Hermès overtook LVMH as the world's most valuable listed luxury company (April 2025, CNN); Louis Vuitton's own brand value fell ~$24.5B (~22%) YoY; LVMH lost its France-largest-company-by-market-cap position to L'Oréal (2026-09-15). This is evidence of *relative* share/position loss, not gain or stability. |
| Brand premium | **TRUE** | Louis Vuitton and Dior both executed real, documented price increases through 2025 (Europe handbags +3–8%; US CarryAll lines +8.6–9.4%) and were able to implement them — evidence of pricing power being actively exercised, even though (see Growth above) the current cycle shows this pricing power meeting consumer resistance ("price fatigue"). Marked TRUE on the historical/structural capability; the erosion risk is separately captured in the Growth penalty above, avoiding double-penalizing the same fact twice. |
| Network effect | **FALSE** | No documented network-effect mechanism in a single-brand-purchase luxury goods/retail model — not claimed. |
| Switching costs | **FALSE** | No documented lock-in/switching-cost mechanism for a discretionary luxury-goods purchaser — not claimed. |
| Scale cost advantage | **FALSE** | LVMH's scale (68 maisons) is well known, but no cited, specific cost-per-unit data versus smaller luxury competitors was found in this session to support marking this TRUE per the strict evidence-required rule — flagged as a possible gap for a future session with sourced data (e.g. TIKR/Koyfin comp data), not invented here. |

```
Moat_Score = (1/5) × 100 = 20.0
```

### 2f. FCF Quality (10% weight)

```
FCF/Net Income ratio (t.cashflow "Free Cash Flow" ÷ t.financials "Net Income"):
  FY2022: 12,753 / 14,084 = 90.5%
  FY2023: 10,596 / 15,174 = 69.8%
  FY2024: 13,373 / 12,550 = 106.6%
  FY2025: 14,205 / 10,878 = 130.6%
```

FCF-positive all 4 reported years (2022–2025) — no "not FCF-positive 3+ years" disqualifier. FY2023's ratio (69.8%) briefly dipped just under 70%, but it is not 2 *consecutive* years below 70% (FY2022 was 90.5%, FY2024 rebounded to 106.6%) — the FCF/NI hard disqualifier does not fire.

```
FCFQuality_Score = clamp(((1.306 − 0.40)/0.60)×100, 0, 100) = 100.0   (using FY2025's 130.6% ratio, capped at 100)
```

### 2g. Final Quality Score

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

= (45.52 × 0.25) + (82.96 × 0.15) + (0.0 × 0.20) + (88.83 × 0.15) + (20.0 × 0.15) + (100.0 × 0.10)
= 11.38 + 12.44 + 0.00 + 13.32 + 3.00 + 10.00
= 50.15
```

Rounded to nearest 0.1 → **Quality Score = 50.1**

(Sensitivity: if the Growth structural-deceleration modifier above is *not* applied, Growth_Score = 2.72 instead of 0.0, adding 0.54 points → Quality Score = 50.7. **The gate outcome is identical either way.**)

### Hard disqualifier check

| Disqualifier | Status |
|---|---|
| FCF/NI <70% for 2+ consecutive years, undocumented | **Not triggered** — only FY2023 (69.8%) dipped below 70%, not 2 consecutive years |
| Net Debt/EBITDA over threshold (2.5×/4×) | **Not triggered** — 0.4468× |
| Not FCF-positive 3+ consecutive years | **Not triggered** — positive all 4 years shown |

No hard disqualifier fires. **This is a soft (score) gate failure, not a hard-disqualifier failure.**

---

## GATE RESULT: FAIL

**Quality Score 50.1 (or 50.7 under the sensitivity case) is well below the strict 80.0+ threshold required to proceed to Phase 02 valuation scoring.** Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md), this session **stops here** — no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work is computed, regardless of how cheap LVMH's depressed price (37% off its 52-week high) might otherwise look.

**Why it fails, in plain terms:** LVMH clears the balance-sheet (0.45× Net Debt/EBITDA) and cash-conversion (FCF/NI >100% most recent year) bars comfortably, and its gross margin (66%) remains high in absolute terms. But two of the six sub-scores are weak enough to sink the composite: **Growth** is essentially flat over 3 years (0.68% CAGR, now compounded by a documented structural share/demand headwind), and **Moat Signal** clears only 1 of 5 strictly-evidenced checklist items this session — the framework's Moat Signal check requires positive, cited evidence of *current* share stability/growth, and the cited evidence found this session points the other way (share/position loss to Hermès, brand-value decline). A 25%-weighted Profitability score in the mid-40s (Net Margin/ROIC both ~13.6%, below the 15% reference points the sub-score scales against) compounds the shortfall.

**Recommendation: PASS — do not open a position.** Not a "watchlist, revisit at a lower price" case in the current framework's terms, because the blocking factor is the Quality Score (fundamentals), not the valuation multiple — a cheaper price does not fix a Growth or Moat Signal problem. Re-evaluate if: (a) revenue growth reaccelerates for 2+ consecutive quarters on a documented, non-one-off basis (e.g. China demand stabilization becomes visible in reported segment data), or (b) new, specific, cited moat evidence emerges (e.g. a published market-share dataset showing LVMH share stabilizing/regaining ground). Absent either, this is a genuine quality-driven pass, not a timing call.

---

## Next Review Trigger

- LVMH's next scheduled quarterly/interim results release (Rule 9 mandatory re-valuation trigger), or
- Any Rule 9 fundamental event (management change, major M&A, guidance revision) before then, or
- Documented evidence of a market-share/growth inflection per the re-evaluation conditions above.

No routine re-screen scheduled otherwise — this is a Phase 01 fail, not a held position, so no `/rescore` cadence applies; a future `/new-position` run will re-derive the Quality Score fresh under the methodology in force at that time.

---

## Data Gaps Flagged

- No cited cost-per-unit/scale data was found this session to support the "Scale cost advantage" Moat Signal despite LVMH's large size — marked FALSE per the "never mark true without a cited source" rule rather than assumed true. A future session with TIKR/Koyfin comp data could revisit this specific line.
- The Growth sub-score's −10 structural-vs-cyclical modifier is the most judgment-laden line in this calculation; the sensitivity check above shows the gate result is unaffected either way, so this judgment call is not load-bearing for the recommendation.

---

## Glossary

*(No new terms — all jargon used below already exists in [glossary.md](../framework/glossary.md).)*

- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate connecting a start and end value over several years.
- **Conglomerate rule** — this framework's requirement to consolidate any captive financial subsidiary's debt into the Net Debt/EBITDA ratio; checked and found not applicable to LVMH's segment structure this session.
- **EBIT** — Earnings Before Interest and Taxes (operating profit before financing and tax effects).
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization (a rough cash-operating-profit proxy).
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether reported accounting profit is actually turning into cash.
- **Gross Margin** — Gross Profit ÷ Revenue; the share of each revenue euro left after direct production/delivery costs.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company outright regardless of its weighted score; none fired here.
- **Invested Capital** — total capital (debt + equity, net of cash) put to work in the business; the ROIC denominator.
- **Moat Signal** — this framework's 5-point Quality Score checklist (market share, brand premium, network effect, switching costs, scale cost advantage), each markable TRUE only against a cited source.
- **Net Debt/EBITDA** — net debt ÷ EBITDA; a leverage ratio and this framework's primary balance-sheet-risk gate.
- **Net Margin** — Net Income ÷ Revenue; the share of each revenue euro left as accounting profit after all costs.
- **NOPAT** — Net Operating Profit After Tax (EBIT × (1 − effective tax rate)); the numerator used to compute ROIC.
- **Quality Score** — this framework's 0.0–100.0 score grading the Phase 01 criteria; a company must score 80.0+ to reach Phase 02 valuation scoring at all.
- **Rate Regime Modifier** — the additive Treasury-yield-based adjustment to the valuation score; noted for context here (+10 at current >5% US 10Y yield) but not applied, since Phase 02 is never reached.
- **ROIC** — Return on Invested Capital; how efficiently a company turns invested capital into profit.
- **TTM (Trailing Twelve Months)** — the most recent four reported quarters combined.

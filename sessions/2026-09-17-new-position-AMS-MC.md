# NEW POSITION — Amadeus IT Group (AMS.MC)

**Date:** 2026-09-17
**Task type:** NEW POSITION
**10Y US Treasury Yield:** 4.945% (2026-09-17, post-FOMC hike) — Rate Regime bracket 3.5–5% → Modifier would be **+5** if Phase 02 were reached (not reached — see below)
**Ticker:** AMS.MC (Amadeus IT Group, S.A.) — Madrid exchange, EUR-denominated
**Sector / Industry:** Technology / Information Technology Services (travel-technology: Global Distribution System + airline/hotel/rail IT solutions)

---

## 1. Live Price (Rule 0)

Fetched via `yf.Ticker("AMS.MC").info` at session time:

| Field | Value |
|---|---|
| Current price | **€55.76** |
| Previous close | €55.48 |
| 52-week range | €46.21 – €69.30 |
| Market cap | €23.42B |
| Enterprise value | €25.94B |

Not inferred from multiples — pulled directly from yfinance's live quote field, per Rule 0.

---

## 2. Data Gaps Flagged

- **Brand-premium pricing-power evidence**: no cited source found showing Amadeus itself raising prices without losing volume (as distinct from *airlines* imposing surcharges on GDS bookings, which is evidence working against Amadeus's own pricing power, not for it). Moat Signal #2 marked **FALSE** rather than guessed.
- Web-search-sourced moat/TAM evidence (market share %, network-effect scale, switching-cost mechanism, scale-advantage/margin comparison) comes from secondary sources (Morningstar, PitchBook-adjacent summaries, industry blogs), not a primary Amadeus filing — flagged as lower-confidence than a 10-K citation would be, but treated as adequate "cited source" per the Moat Signal checklist's evidentiary bar (third-party market-share/industry reports are explicitly an accepted source type in quality-scoring.md).
- No hard blocker to scoring — all quantitative inputs (margins, ROIC, growth, leverage, FCF/NI) came directly from `yfinance` (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet`), no missing critical metric.

---

## 3. Phase 01 — Quality Score (0–100.0, gate = 80.0+)

*Per [quality-scoring.md](../framework/quality-scoring.md). All quantitative inputs from `yfinance` (FY2022–FY2025 annual filings, most recently completed fiscal years — rolling window per the 2026-08-05 clarification).*

### Raw data pulled

| FY | Revenue (€M) | Gross Profit (€M) | EBIT (€M) | Net Income (€M) | Pretax Income (€M) | Tax (€M) | FCF (€M) | Net Debt (€M) | EBITDA (€M) | Invested Capital (€M) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2022 | 4,485.9 | 1,872.1 | 958.1 | 664.4 | 871.7 | 204.8 | 874.1 | 2,763.5 | 1,635.7 | 8,784.5 |
| 2023 | 5,441.2 | 2,411.4 | 1,453.8 | 1,117.6 | 1,361.6 | 242.9 | 1,194.4 | 2,072.5 | 2,134.2 | 7,593.9 |
| 2024 | 6,141.7 | 2,655.0 | 1,653.0 | 1,253.0 | 1,544.4 | 295.6 | 1,357.9 | 2,120.9 | 2,353.2 | 8,233.6 |
| 2025 | 6,517.0 | 2,867.6 | 1,799.7 | 1,335.7 | 1,718.2 | 385.0 | 1,386.3 | 2,113.1 | 2,534.7 | 7,942.4 |

Derived per-year metrics (shown for the trend, current-year FY2025 figures used as the TTM proxy in the score below):

| FY | Net Margin | ROIC (NOPAT÷IC) | FCF/NI |
|---|---|---|---|
| 2022 | 14.81% | 8.34% | 131.6% |
| 2023 | 20.54% | 15.73% | 106.9% |
| 2024 | 20.40% | 16.23% | 108.4% |
| 2025 | 20.50% | 17.58% | 103.8% |

FCF-positive all 4 years available (2022–2025) — clears the "3+ consecutive years FCF-positive" hard-disqualifier test with room to spare.

### Hard disqualifier check (must clear all 3 before weighted scoring matters)

| Disqualifier | Result |
|---|---|
| FCF/NI <70% for 2+ consecutive years | **PASS** — never below 100% in any of the 4 years shown |
| Net Debt/EBITDA over threshold (2.5× standard) | **PASS** — 2025: 2,113.1 ÷ 2,534.7 = **0.83×** |
| Not FCF-positive 3+ consecutive years | **PASS** — 4 consecutive years positive |

No hard disqualifier fires. Proceeding to the weighted score (which is where this candidate ultimately fails — see below).

### Sub-score calculations

**Profitability (25% weight)** — using FY2025/TTM Net Margin 19.858% (yfinance `profitMargins`, TTM) and FY2025 ROIC 17.58% (computed):
```
NetMargin_Component = clamp((19.858/30)×100) = 66.19
ROIC_Component       = clamp((17.58/30)×100) = 58.60
Profitability_Score  = (66.19 + 58.60)/2 = 62.40   (no FCF cap — 4/4 years positive, likely longer)
```

**Margins (15% weight)** — Gross Margin TTM 44.63% (yfinance `grossMargins`):
```
GrossMargin_Score = clamp((44.63/80)×100) = 55.79
```
3yr trend check: 41.7% (2022) → 44.3% (2023) → 43.2% (2024) → 44.0% (2025) — already above the 40% threshold, largely flat since 2023 (post-COVID step-up, not a continuing structural expansion). The framework's "+10 structurally expanding" bonus is explicitly for a business *below* 40% moving up — not applicable here (Amadeus is already above the static threshold). No bonus applied. **Margins_Score = 55.8**

**Growth (20% weight)** — Revenue 3yr CAGR, FY2022→FY2025:
```
CAGR = (6,517.0 / 4,485.9)^(1/3) − 1 = 13.27%
Growth_Score (raw) = clamp((13.27/25)×100) = 53.08
```
TAM/pricing-power modifier: cited evidence of TAM expansion — Amadeus's IT Solutions segment (airline, airport, rail, hotel technology, beyond the core GDS) now represents 52% of 2025 revenue, a genuine adjacent-market expansion ([MatrixBCG competitive-landscape summary](https://matrixbcg.com/blogs/competitors/amadeus)). **+10 applied.**
Countervailing note (not scored, flagged for the record): YoY revenue growth has been decelerating — +21.3% (2023), +12.9% (2024), +6.1% (2025) — but this reads as **cyclical** normalization off the 2022–2023 post-COVID air-travel recovery trough, not a documented *structural* deceleration (no cited source ties it to a permanent TAM/pricing-power loss), so the −10 structural-deceleration modifier is **not** applied. This is a closer call than the +10 and is flagged explicitly rather than silently netted — even removing the +10 entirely, the Quality Score would land at ~68.5, still well short of the 80.0 gate (see sensitivity note at the end of this section).
```
Growth_Score = 53.08 + 10 = 63.08
```

**Balance Sheet (15% weight)** — Net Debt/EBITDA (FY2025) = 0.834× (standard business, not asset-light/payment-network — standard /4 denominator applies):
```
BalanceSheet_Score = clamp(100 × (1 − 0.834/4)) = 79.15
```

**Moat Signal (15% weight)** — checklist, evidence cited per signal:

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Amadeus holds ~37–40% of the global GDS market (largest of the 3 GDS operators, which together control ~97–100% of the market) — [Morningstar](https://www.morningstar.com/stocks/xmad/ams/quote), [MatrixBCG](https://matrixbcg.com/blogs/competitors/amadeus) |
| Brand premium | **FALSE** | No cited evidence of Amadeus raising its own prices without losing volume; the documented pricing dynamic found (airlines' "Distribution Cost Charges" on GDS bookings) is evidence *against* Amadeus's pricing power, not for it |
| Network effect | **TRUE** | Platform connects 400,000+ travel-agency locations, hundreds of airlines, and thousands of hotels — two-sided marketplace dynamics — [heavymoatinvestments.substack.com](https://heavymoatinvestments.substack.com/p/amadeus-it-is-the-travel-infrastructure) |
| Switching costs | **TRUE** | Passenger Service System replacement touches reservations, inventory, and departure control; airlines/airports integrate deeply, migrations documented as costly and risky; typically multi-year contracts — same source above |
| Scale cost advantage | **TRUE** | Amadeus outperforms Sabre (~30% share) and Travelport (smaller third player) on profitability, attributed to higher-margin SaaS mix and distribution scale — [MatrixBCG](https://matrixbcg.com/blogs/competitors/amadeus) |

```
Moat_Score = (4/5) × 100 = 80.0
```

**FCF Quality (10% weight)** — FY2025/TTM FCF/NI = 103.8%:
```
FCFQuality_Score = clamp(((1.038 − 0.40)/0.60) × 100) = clamp(106.3, 0, 100) = 100.0
```

### Final Quality Score

```
Quality Score = 62.40×0.25 + 55.79×0.15 + 63.08×0.20 + 79.15×0.15 + 80.0×0.15 + 100.0×0.10
              = 15.60 + 8.37 + 12.62 + 11.87 + 12.00 + 10.00
              = 70.46 → rounds to 70.5
```

**Sensitivity check** (per the Growth-modifier judgment call flagged above): without the +10 TAM bonus, Growth_Score = 53.08, Quality Score = 68.46 → 68.5. Either way, the result is a clear gate failure — the +10/−0 judgment call does not change the outcome.

### Gate result

**Quality Score = 70.5 — FAILS the strict 80.0+ gate.** No hard disqualifier fired independently (leverage, FCF-positivity, and FCF/NI conversion are all comfortably healthy), but the weighted score itself falls 9.5 points short of the bar.

**Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md): STOP HERE. Do not proceed to the Rate Environment Gate, Phase 02 Valuation Score, Composite Score, or fair-value/order-setup work.** Amadeus does not reach Phase 02 in this session, regardless of how cheap or expensive its multiples currently look.

### Why it fails — the driver, in plain terms

The gate failure isn't from any one glaring weakness — Amadeus clears the *individual* Phase 01 disqualifier thresholds comfortably (very low leverage, strong FCF conversion, FCF-positive throughout). It fails because it is a solid-but-not-exceptional business across the board rather than an outstanding one on any axis:
- Profitability (62.4) and Margins (55.8) are mid-pack — a ~20% net margin and ~45% gross margin are respectable for an IT-services business but well short of the ≥30%/≥80% levels that max out those sub-scores (a software business with true platform economics, e.g. a payments network or SaaS moat name, typically clears 80–100 on these).
- Growth (63.1, after the TAM bonus) reflects real but decelerating-off-a-cyclical-peak revenue growth (13.3% 3yr CAGR, but YoY growth down to 6.1% most recently) — good, not exceptional.
- The Moat score (80.0) and Balance Sheet score (79.2) are genuinely strong and pull the average up, but can't offset the two largest-weighted sub-scores (Profitability 25%, Growth 20%) landing in the low-to-mid 60s.

**Qualitative risk not captured in the quantitative score, but material to the standing "would this pass on a rescore later" question:** the travel industry's shift toward **NDC (New Distribution Capability)** — an IATA standard letting airlines sell direct or via agents without routing through a GDS — is a documented, live disintermediation threat to Amadeus's core Distribution/GDS segment. Multiple airlines (Lufthansa Group, Air Europa, Turkish Airlines) are actively surcharging GDS bookings or pulling content to push traffic to NDC/direct channels ([PhocusWire](https://www.phocuswire.com/news/distribution/ndc-ai-orders-airline-distribution-2026-uatp), [Travel Distribution News](https://traveldistributionnews.com/the-gds-doesnt-want-to-be-a-gds-anymore/)). Amadeus is actively responding (e.g. its "Advanced Airline Profile" ML filter, deployed with Air France-KLM), and current market share is still stable-to-growing per the cited sources — so this is flagged as a **moat-durability watch item**, not a present-tense moat failure, and did not change the Moat sub-score. It should be re-examined at any future rescore of this name.

Also flagged for context (Rule 9-style fundamental event, not scored): Amadeus cut its FY2026 guidance on 2026-07-31, citing increased geopolitical tensions in the Middle East affecting air-traffic assumptions — cyclical/macro in nature per the cited reporting, not a structural thesis break, and consistent with why the Growth sub-score's deceleration wasn't treated as "structural" above.

---

## 4–5. Phase 02 / Composite Score / Recommendation

**Not computed — gate failure at Step 2 above means Phase 02 (valuation scoring), the Composite Score, and the fair-value/order-setup work in [fair-value-methodology.md](../framework/fair-value-methodology.md) are all out of scope for this session**, per the explicit "stop here" instruction in [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md).

**Recommendation: PASS.** Not a candidate for a new position at this time — the Quality Score gate exists precisely to avoid grading "how cheap is it" for a company that isn't demonstrated-exceptional in the first place. Route to **watchlist only** (not-in-portfolio), for potential re-evaluation if a future rescore shows genuine margin/ROIC/growth improvement (e.g. IT Solutions segment mix shift lifting margins, or ROIC's clear 2022→2025 uptrend — 8.3% → 17.6% — continuing further).

---

## 6. Next Review Trigger

- Amadeus's next full-year (FY2026) results release (expected ~February 2027) — re-run Quality Score with a fresh trailing window.
- Any confirmed, material NDC-driven GDS volume/share loss (a Rule 9 fundamental event) — would warrant an earlier check on the Moat Signal "market share" and "network effect" marks specifically.
- Any Middle East-tensions-driven guidance cut resolving or worsening materially beyond the 2026-07-31 cut already noted.

---

## Glossary

*Per [operating-brief.md](../framework/operating-brief.md) Step 9 — terms used above, defined in [glossary.md](../framework/glossary.md).*

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper. *(Not used in a final calc this session — Phase 02 wasn't reached — but the FCF/NI conversion input is a Quality Score component.)*
- **GDS (Global Distribution System)** — A B2B travel-technology platform (Amadeus, Sabre, Travelport) that aggregates airline, hotel, and car-rental inventory into a single searchable/bookable marketplace for travel agencies — the core of Amadeus's business and its Network Effect / Switching Costs Moat Signal evidence.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or FCF/Net Income conversion under 70% for 2+ consecutive years without a documented growth-capex explanation.
- **Invested Capital** — The total capital (debt + equity, netted for cash) put to work in a business — the denominator in a Return on Invested Capital (ROIC) calculation.
- **Moat Signal** — This framework's 5-point Quality Score checklist that turns the general "Moat" concept into a scored input: market share, brand premium, network effect, switching costs, scale cost advantage — each markable TRUE only against a cited source.
- **NDC (New Distribution Capability)** — An IATA XML-based data standard letting airlines sell fares/ancillaries directly or via agents without routing through a traditional GDS — a documented long-term disintermediation risk to GDS operators like Amadeus.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC (NOPAT ÷ Invested Capital).
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria instead of treating them as pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all.
- **Rate Regime Modifier** — An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in. *(Computed for reference only this session — not applied, since Phase 02 wasn't reached.)*
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **TAM (Total Addressable Market)** — The total revenue opportunity available if a company captured 100% of its target market.

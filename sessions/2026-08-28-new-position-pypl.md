# NEW POSITION — PYPL (PayPal Holdings, Inc.) — 2026-08-28

**Task type:** NEW POSITION (Telegram-scan triggered, Routine 6, unattended)
**Date:** 28 Aug 2026
**Trigger:** Telegram scan flagged two independent posts the same morning reporting the Stripe/Advent–PayPal acquisition talks collapsing:
- [tarasguk/11789](https://t.me/tarasguk/11789) (~06:08 UTC): "Stripe відмовився купляти PayPal. Раніше пропонували $60 за акцію за повне поглинання." ("Stripe refused to buy PayPal. Previously offered $60/share for a full acquisition.")
- [bolshegold/10052](https://t.me/bolshegold/10052) (~05:03 UTC): "Stripe, Adyen отказались платить больше $50В за $PYPL и вышли из переговоров" ("Stripe, Adyen refused to pay more than $50B for $PYPL and exited talks.")

Per Rule 0 / CLAUDE.md, neither post's text is treated as financial data — both are triggers only. Independently verified via WebSearch: **Bloomberg (28 Aug 2026, same day) confirms the Advent/Stripe consortium has abandoned its pursuit of PayPal** — a real, dated M&A-collapse event. **The Adyen claim in the bolshegold post is NOT corroborated** by Bloomberg/Engadget/other outlets found — only Stripe + Advent are named in independent reporting. Flagging this discrepancy rather than repeating the unverified Adyen detail as fact.

This is materially new information beyond the existing [not-in-portfolio/PYPL/PYPL-2026-06-14.md](../watchlist/not-in-portfolio/PYPL/PYPL-2026-06-14.md) entry, whose latest note (2026-07-17) had the deal alive at $60.50/share with PayPal's board not having formally responded. The deal being abandoned entirely is a distinct, more advanced M&A outcome — a valid Rule 9 trigger independent of PYPL's Q2 2026 earnings (also new since the last watchlist entry, see below).

**10Y US Treasury Yield:** not pulled — immaterial to this session's outcome (Phase 01 gate fails before the Rate Environment Gate / Phase 02 would apply it)
**Current PYPL portfolio weight:** 0% — not currently held (confirmed against [holdings.md](../portfolio/holdings.md))
**Sector:** Financial Technology — Digital Payments (PayPal checkout, Venmo, Braintree, BNPL)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$52.49** | IBKR `get_price_snapshot` (contract_id 199169591, NASDAQ), intraday (`is_close: false`) |
| Day change | **−$8.98 / −14.61%** | IBKR `change` field |
| Bid / Ask | $52.44 / $52.60 | IBKR `bid_ask` |
| 52-week range | $38.34 – $78.80 | IBKR `misc_statistics` |
| 13-week range | $40.20 – $62.73 | IBKR `misc_statistics` |

**Context:** The −14.61% intraday drop is the market's reaction to the M&A-collapse news confirmed above — **explained**, not an "unexplained >15% move" Rule 9 trigger in its own right (and in any case a separate, already-identified M&A event is driving this session). Independent reporting (Bloomberg/Engadget) also notes the stock had rallied roughly 40% over the prior weeks on a combination of the Q2 2026 earnings beat and the takeover speculation — today's drop is a partial reversal of that run-up as the takeover speculation is removed, not a fresh, unexplained shock.

---

## 2. Rule 9 Checklist (all 6 categories)

| Category | Result |
|---|---|
| **Earnings** | **YES** — Q2 2026 results reported 28 Jul 2026 (after the 2026-07-17 watchlist entry): net revenues $8,682M (+5% YoY), GAAP net income $1,104M, GAAP diluted EPS $1.25, non-GAAP diluted EPS $1.38 (beat), full-year non-GAAP EPS guidance raised to ~$5.38. |
| **Guidance revision** | Folded into the earnings event above (raised FY guidance). |
| **Management change** | None identified since the last entry. |
| **M&A** | **YES — the trigger for this session.** Advent/Stripe consortium has abandoned its pursuit of PayPal (Bloomberg, 28 Aug 2026), after PayPal's board had earlier declined a $60.50/share, ~$53B offer as too low. Deal is now off. |
| **Macro shift** | None specific to PYPL identified. |
| **>15% unexplained price move** | No — today's −14.61% move is explained by the M&A-collapse news (see above). |

---

## 3. Data Gathered (Phase 01 / Quality Score Inputs) & Gaps Flagged

All figures sourced from PayPal's own SEC filings (8-K earnings releases, 10-Q) via WebSearch, or third-party aggregators (GuruFocus) — never invented or estimated. TTM = trailing four quarters through Q2 2026 (ended 30 Jun 2026), computed as FY2025 − Q1 2025 − Q2 2025 + Q1 2026 + Q2 2026.

| Metric | Value | Source / Derivation |
|---|---|---|
| FY2022 Net revenues | $27,518M | PayPal FY2022 10-K (carried from 2026-06-14 session, unchanged) |
| FY2025 Net revenues | $33,200M | PayPal FY2025 10-K / Q4 2025 earnings release |
| Q1 2025 Net revenues | $7,791M | PayPal Q1 2025 8-K (carried from 2026-06-14 session) |
| Q2 2025 Net revenues | $8,290M (+5% YoY) | PayPal Q2 2025 8-K earnings release |
| Q1 2026 Net revenues | $8,350M (+7% YoY) | PayPal Q1 2026 8-K (carried from 2026-06-14 session) |
| Q2 2026 Net revenues | $8,682M (+5% YoY) | PayPal Q2 2026 8-K earnings release (28 Jul 2026) |
| **TTM Revenue** | **$34,151M** = 33,200 − 7,791 − 8,290 + 8,350 + 8,682 | Computed |
| **Revenue CAGR 3yr** (FY2022→FY2025, unchanged — FY2025 still latest complete FY) | **6.46%** = (33,200/27,518)^(1/3) − 1 | Computed |
| FY2025 GAAP Net income | $5,233M | PayPal FY2025 10-K |
| Q1 2025 GAAP Net income | $1,287M | PayPal Q1 2025 8-K (carried) |
| Q2 2025 GAAP Net income | $1,261M | PayPal Q2 2025 8-K (backed out from Q2 2026 release's "-12% YoY vs $1.261B" disclosure) |
| Q1 2026 GAAP Net income | $1,110M | PayPal Q1 2026 8-K (carried) |
| Q2 2026 GAAP Net income | $1,104M | PayPal Q2 2026 8-K |
| **TTM Net income** | **$4,899M** = 5,233 − 1,287 − 1,261 + 1,110 + 1,104 | Computed |
| **TTM Net margin** | **14.34%** = 4,899 / 34,151 | Computed |
| ROIC | 21.12% (GuruFocus, "as of Jun. 2026") | GuruFocus |
| Gross margin (TTM, ~mid-2026) | 40.9% | GuruFocus / Investing.com aggregation |
| Gross margin FY2022→FY2025 | 42.3% → 39.6% → 40.5% → 41.5% | WebSearch aggregation (carried from 2026-06-14 session) |
| FY2024 FCF / FY2024 NI | $6.8B / $4,246M → **160.2%** | PayPal FY2024 earnings coverage (carried) |
| FY2025 FCF / FY2025 NI | $5.56B / $5,233M → **107.1%** | PayPal FY2025 earnings release |
| Total debt (30 Jun 2026) | $13.4B | PayPal Q2 2026 10-Q |
| Cash & investments (30 Jun 2026) | $15.3B | PayPal Q2 2026 10-Q |
| **Net debt** | **≈ −$1.9B (net cash)** | Computed |
| Credit rating (S&P) | A− (affirmed, stable outlook — most recent affirmation found dated Jun 2025) | S&P Global Ratings via cbonds |
| TAM (company-disclosed) | ~$860B combined: Checkout $390B TAM (mid-single-digit growth, <5% penetration), Payment Processing & Value-Added Services $260B TAM (low-double-digit growth, <1% penetration) | PayPal investor materials, via WebSearch aggregation |
| Market share | ~43–45% of global online payment processing (2026 estimate); branded-checkout TPV growth has slowed to +2% FXN (Q1 2026) amid Apple Pay/Google Pay competitive pressure | Third-party aggregators (chargeflow.io) + PYMNTS/TheStreet coverage |

### Data Gaps Flagged (no auto-commit skipped — gate fails regardless, see §4)

1. **TTM FCF could not be cleanly backed out.** Q1 2025 FCF was not separately disclosed in the sources found (only bundled into full-year guidance commentary), so the roll-forward method used for revenue/net income above could not be applied to FCF. The FCF Quality sub-score below uses **FY2025's FCF/NI ratio (107.1%)** as the freshest cleanly-sourced figure instead of a TTM figure — flagged explicitly rather than estimating the missing quarter.
2. **Moat signal evidence:** only "network effect" (PayPal's two-sided merchant/consumer wallet network) was independently documented this session. "Brand premium," "switching costs," and "scale cost advantage" were not verified with cited pricing-power, integration-lock-in, or cost-per-unit evidence in the sources reviewed — marked FALSE for scoring purposes per this framework's "never mark a signal true without a cited source" rule, **not** as a claim that PayPal genuinely lacks these attributes. "Market share stable or growing" was also marked FALSE: PayPal's overall share (~43–45%) is large but its core branded-checkout segment has documented growth deceleration and competitive pressure (Apple Pay/Google Pay), which cuts against a clean "stable or growing" reading.
3. **Gross margin trend bonus not applied:** the 4-year trend (42.3% → 39.6% → 40.5% → 41.5%) dipped in FY2023 before recovering, and the TTM figure (40.9%) has ticked back down from FY2025's 41.5% — not a clean, unambiguous multi-year expansion, so the Margins sub-score's +10 structural-trend bonus is withheld rather than assumed.

---

## 4. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology v2026-06-29)

**Hard disqualifier check (all evaluated on the current rolling window, most recent complete fiscal years FY2024–FY2025):**

| Disqualifier | Result |
|---|---|
| FCF/NI conversion <70% for 2+ consecutive years | FY2024 160.2%, FY2025 107.1% — both well above 70%. **Does not fire.** |
| Net Debt/EBITDA over threshold | Net cash position (~−$1.9B). **Does not fire.** |
| Not FCF-positive for 3+ consecutive years | FCF positive FY2023, FY2024, FY2025. **Does not fire.** |

No hard disqualifier fires — this is a weighted-score gate outcome, not a disqualifier-driven one.

**Sub-scores:**

```
Profitability (25%):
  NetMargin_Component = clamp((14.34/30)×100) = 47.8
  ROIC_Component       = clamp((21.12/30)×100) = 70.4
  Profitability_Score  = (47.8 + 70.4) / 2 = 59.1   (no FCF cap — FCF-positive 3+ yrs)

Margins (15%):
  GrossMargin_Score = clamp((40.9/80)×100) = 51.1   (no trend bonus — see Data Gap #3)

Growth (20%):
  Growth_Score = clamp((6.46/25)×100) = 25.8
  + 10 (documented TAM-expansion evidence: $860B combined TAM, <5%/<1% penetration — see §3)
  = 35.8

Balance Sheet (15%):
  BalanceSheet_Score = 100  (net cash position, clamped at ceiling)

Moat Signal (15%):
  1 of 5 signals TRUE (network effect only — see Data Gap #2)
  Moat_Score = (1/5) × 100 = 20.0

FCF Quality (10%):
  FCFQuality_Score = clamp(((1.071 − 0.40)/0.60)×100) = clamp(111.8) = 100.0
  (FY2025 FCF/NI ratio used — see Data Gap #1)

Quality Score = 59.1×0.25 + 51.1×0.15 + 35.8×0.20 + 100×0.15 + 20.0×0.15 + 100×0.10
              = 14.78 + 7.67 + 7.16 + 15.00 + 3.00 + 10.00
              = 57.6
```

**Quality Score = 57.6 — fails the 80.0+ gate.** Per [quality-scoring.md](../framework/quality-scoring.md): "Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks." **Stopping here — no Rate Environment Gate, Phase 02 valuation score, Composite Score, or order setup computed.**

The result is qualitatively unchanged from every prior PYPL session (2026-06-14, 07-15, 07-17): PayPal continues to fail primarily on **growth** (6.46% 3yr revenue CAGR vs. the >10%/25% band this score rewards) and now also scores weakly on **moat evidence** under this session's stricter sourcing discipline (only 1 of 5 signals independently documented) — this is the first session to compute PYPL's numeric Quality Score under the engine (live since 2026-06-29); prior sessions used the older binary Phase 01 screen, which likewise failed on revenue growth alone. Even crediting all 4 unverified moat signals as TRUE (Moat_Score 100 instead of 20) would only add ~12 points (57.6 → ~69.6), still well short of 80.0 — the gate outcome is not sensitive to that data gap.

---

## 5. Recommendation

**Pass / watchlist only.** PYPL does not clear the 80.0+ Quality Score gate (57.6). The M&A-collapse news that triggered this session doesn't change that verdict — this framework has no merger-arbitrage scoring mechanism, and the underlying business (headlined by sub-10% revenue growth) is unaffected by whether or not a takeover happens. No position opened; no order setup computed.

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **Gross Margin** | Gross Profit (Revenue − Cost of Revenue) ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted sub-score total, independent of the continuous score. |
| **Net Debt/EBITDA** | Net Debt (Total Debt − Cash) ÷ EBITDA — a leverage ratio; negative means the company holds more cash than debt ("net cash"). |
| **Quality Score** | This framework's 0–100.0 graded measure of business quality; a company must score 80.0 or above to be eligible for valuation scoring at all. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move. |
| **Rule 0** | This framework's requirement to always fetch live prices/data first, never infer or estimate them. |
| **TAM** | Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market. |
| **TPV (Total Payment Volume)** | The total dollar value of payments processed through PayPal's platform in a period — a scale/volume metric distinct from PayPal's own (smaller) take-rate revenue. |

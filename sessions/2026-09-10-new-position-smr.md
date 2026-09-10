# NEW POSITION — SMR (NuScale Power Corporation)

**Date:** 2026-09-10
**10Y Treasury yield:** 4.84% (Rate Regime Modifier would be +5 if reached — not reached, see below)
**Task type:** NEW POSITION

## Rule 0 — Live Price

Fetched via IBKR live snapshot (contract_id 559289446, SMART-routed, NYSE:SMR):

- **Last: $10.20** (−$0.61, −5.64% intraday)
- 52-week range: $7.22 – $57.33 (52w-open $36.41) — stock is down ~82% from its 52-week high
- 13-week range: $7.22 – $11.85; 26-week range: $7.22 – $14.30

Not to be confused with the leveraged-ETF tickers sharing the root, or ASX-listed Stanmore Resources (also "SMR") — same disambiguation as the 2026-07-16 entry.

## Rule 9 trigger for this re-check

Last watchlist entry ([2026-07-16](../watchlist/not-in-portfolio/SMR/SMR-2026-09-10.md)) recorded $7.60. Current $10.20 is +34.2% since then — a >15% move without an identified company-specific fundamental cause (broader SMR/nuclear-sector rally, not a disclosed catalyst) — so this re-check produces a full session per Rule 9, even though the outcome is unchanged.

## Phase 01 — Quality Score Gate

**Result: FAIL — hard disqualifier fires. Stop before Phase 02 valuation scoring, per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md).**

**Hard disqualifier: not FCF-positive for 3+ consecutive years** (no carve-out under the rolling-window clarification — the current window is uniformly negative, not "2 of 3 negative"):

| Fiscal Year | Free Cash Flow | Source |
|---|---|---|
| FY2021 | negative (operating cash flow −$99.2M) | Yahoo Finance cash flow statement |
| FY2022 | negative (operating cash flow −$148.6M) | Yahoo Finance cash flow statement |
| FY2023 | negative (operating cash flow −$183.3M) | Yahoo Finance cash flow statement |
| FY2024 | negative (operating cash flow −$108.7M) | Yahoo Finance cash flow statement |
| FY2025 | **−$460.1M FCF** | stockanalysis.com FY2025 annual figure |

Six consecutive fiscal years of negative FCF on record (FY2020–FY2025 per the 2026-07-16 session; FY2021–FY2025 re-confirmed here). The rolling window (any 3 most-recently-completed fiscal years) is uniformly negative — disqualifier fires with no ambiguity.

**Corroborating evidence the underlying picture hasn't improved since the 2026-07-16 session:**
- Q2 2026 (most recent quarter): revenue $75K, net loss $47.5M (StockTitan, sourced from the company's own 8-K)
- TTM revenue ~$31.5M, TTM EPS −$1.82 to −$2.20 depending on share-count basis (multiple sources) — still deeply unprofitable
- Liquidity: $1.9B cash/investments as of 2026-06-30 (company 8-K) — ample near-term runway, but this is a balance-sheet cushion, not evidence the FCF/profitability disqualifier has cleared

No new data point (Q2 2026 results, current $10.20 price) changes the Phase 01 outcome from the 2026-07-16 session. Full weighted quality sub-score arithmetic (Profitability, Margins, Growth, Balance Sheet, Moat, FCF Quality) is not re-run here since the hard disqualifier is dispositive on its own and the underlying financial-statement inputs haven't materially changed since the prior session's full workup — see that session for the complete sub-score-by-sub-score calculation (weighted score there: 49.8, also well below the 80.0 gate independent of the disqualifier).

**Per operating-brief.md: "If it's below 80.0, or a hard disqualifier fires, stop and report why rather than proceeding to scoring."** No Rate Environment Gate, no Phase 02 valuation score, no Composite Score, no fair-value/order-setup work performed.

## Recommendation

**PASS.** Quality gate fails on both an unconditional hard disqualifier (FCF negative every year on record, 6 consecutive fiscal years) and, independently, the weighted score (49.8, last computed 2026-07-16). Do not enter. Watchlist only, re-evaluated on the next Rule 9 trigger.

## Next review trigger

Unchanged from the 2026-07-16 entry: (a) NuScale's first closed/binding commercial power-plant sale, (b) a sustained multi-quarter positive FCF trajectory, (c) resolution of the ENTRA1 securities-fraud class action, (d) a quarterly earnings release or guidance revision, (e) a management change or material M&A/strategic-investment event, (f) a further >15% stock-price move with no identified cause.

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. Negative for SMR in every fiscal year on record. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score — see [quality-scoring.md](../framework/quality-scoring.md). The "not FCF-positive for 3+ consecutive years" disqualifier fires for SMR and has no carve-out. |
| **Quality Score** | A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. SMR fails via hard disqualifier and independently on the 49.8 weighted score. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) to the valuation score based on where the 10-Year Treasury yield sits; not reached for SMR since it never proceeds to Phase 02. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it into profit; deeply negative for SMR. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **TTM** | Trailing Twelve Months — the most recent 12 months of financial results, used instead of calendar-year figures to stay current between annual reports. |

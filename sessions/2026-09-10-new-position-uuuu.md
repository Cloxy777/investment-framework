# NEW POSITION — UUUU (Energy Fuels Inc.)

**Date:** 2026-09-10
**10Y Treasury yield:** 4.84% (Rate Regime Modifier would be +5 if reached — not reached, see below)
**Task type:** NEW POSITION

## Rule 0 — Live Price

Fetched via IBKR live snapshot (contract_id 137823153, AMEX/SMART-routed, NYSE American: UUUU):

- **Last: $13.62** (bid $13.62 / ask $13.63)
- Not to be confused with UUUUUSD (EBS Swiss-franc listing), UUUUN (Mexico listing), UUUG (2x leveraged ETF), or UUUC (2x leveraged ETF) — all share the ticker root but are separate instruments.

## Phase 01 — Quality Score Gate

**Result: FAIL — hard disqualifier fires. Stop before Phase 02 valuation scoring**, per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md).

**Hard disqualifier: not FCF-positive for 3+ consecutive years.** Energy Fuels has never posted a positive fiscal-year free cash flow on record, and the burn is worsening as the company scales up rare-earth/uranium capex:

| Fiscal Year | Operating Cash Flow | CapEx | Free Cash Flow | Source |
|---|---|---|---|---|
| FY2021 | −$29.29M | −$1.37M | **−$30.66M** | stockanalysis.com cash flow statement |
| FY2022 | −$49.70M | −$2.00M | **−$51.70M** | stockanalysis.com cash flow statement |
| FY2023 | −$15.41M | −$44.71M | **−$60.12M** | stockanalysis.com cash flow statement |
| FY2024 | −$43.97M | −$29.38M | **−$73.36M** | stockanalysis.com cash flow statement |
| FY2025 | −$89.48M | −$51.79M | **−$141.27M** | stockanalysis.com cash flow statement |

Five consecutive fiscal years of negative FCF, monotonically worsening each year — the rolling window (any 3 most-recently-completed fiscal years, per the 2026-08-05 rolling-window clarification) is uniformly negative with no ambiguity. Disqualifier fires unconditionally; there is no documented growth-capex carve-out available for this specific disqualifier (that carve-out only applies to the separate FCF/NI-conversion-ratio disqualifier, and would not help here regardless — this is an outright FCF-negative test).

**Corroborating evidence the underlying picture is not a near-term profitability story either:**
- Net income: FY2022 −$59.85M, FY2023 +$99.86M (one-off — driven by non-operating items, not the operating trend), FY2024 −$47.77M, FY2025 −$85.63M, TTM (Jun '26) −$81.75M — FY2023's single profitable year does not represent a sustained trend
- TTM revenue $105.76M (+62.5% YoY, driven by uranium sales ramp), but TTM net margin −77.3% and TTM operating margin −78.65%
- Balance sheet: $678.34M total debt taken on in FY2025 (vs. near-zero in FY2022), offset by a large cash/short-term-investment raise ($282M equity issuance + $700M debt issuance) — net cash position is a financing-driven cushion, not evidence of operational self-funding
- The FCF trajectory is consistent with a company aggressively building out rare-earth and uranium production capacity (Base rare-earth/White Mesa Mill expansion), which may be a legitimate growth story — but it does not change the Quality Score gate outcome, which is mechanical and does not weigh "why" capex is negative for this particular disqualifier

Per **operating-brief.md: "If it's below 80.0, or a hard disqualifier fires, stop and report why rather than proceeding to scoring."** Full weighted quality sub-score arithmetic (Profitability, Margins, Growth, Balance Sheet, Moat, FCF Quality) is not computed this session — the hard disqualifier is dispositive on its own, and Profitability alone would in any case be capped at 40.0 under quality-scoring.md's "not FCF-positive for 3+ consecutive years" cap rule, making an 80.0+ overall score arithmetically very hard to reach even before the gate itself is considered. No Rate Environment Gate, no Phase 02 valuation score, no Composite Score, no fair-value/order-setup work performed.

## Recommendation

**PASS.** Quality gate fails on an unconditional hard disqualifier — free cash flow negative in every fiscal year on record (5 consecutive years, FY2021–FY2025), worsening each year. Do not enter. Watchlist only.

## Next review trigger

(a) A fiscal year of positive free cash flow (the mine/mill capex program reaching a self-funding state), (b) a sustained multi-quarter trend of positive operating cash flow, (c) a quarterly earnings release or guidance revision materially changing the FCF trajectory, (d) a management change or material M&A/strategic-investment event, (e) a >15% stock-price move with no identified cause (Rule 9).

## Glossary

| Term | Meaning |
|---|---|
| **CapEx (Capital Expenditure)** | Money spent on long-lived physical assets (mines, mills, equipment) — subtracted from operating cash flow to get free cash flow. |
| **FCF (Free Cash Flow)** | Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. Negative for UUUU in every fiscal year on record. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score — see [quality-scoring.md](../framework/quality-scoring.md). The "not FCF-positive for 3+ consecutive years" disqualifier fires for UUUU and has no carve-out. |
| **Net Margin** | Net Income ÷ Revenue — the percentage of each revenue dollar that becomes bottom-line profit. Deeply negative for UUUU in 4 of the last 5 fiscal years. |
| **Operating Cash Flow** | Cash generated (or consumed) by a company's core business operations, before capital spending — the starting point for the FCF calculation. |
| **Quality Score** | A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. UUUU fails via hard disqualifier before a weighted score is even computed. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **TTM** | Trailing Twelve Months — the most recent 12 months of financial results, used instead of calendar-year figures to stay current between annual reports. |

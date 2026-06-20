# Glossary

A standing reference of financial jargon, abbreviations, and framework-specific terms used across this repo. The user is not a finance professional, so every term that could plausibly be unfamiliar gets a plain-English definition here.

**How this is used:** per [operating-brief.md](operating-brief.md), every analysis response, session log, decision log, and PR description must end with a "Glossary" section listing the terms from *this* file that actually appear in that output (not the whole file). If a response uses a term that isn't here yet, add it to this file in the same session and then cite it — this file is expected to grow over time.

Alphabetical within each group.

---

## General financial & valuation terms

| Term | Meaning |
|---|---|
| **bps (basis points)** | 1 bps = 0.01 percentage points. 50 bps = 0.5%. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets (factories, equipment, data centers). |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **DCF** | Discounted Cash Flow — a valuation method that estimates a company's worth today by projecting its future cash and discounting it back to present-day value. |
| **DDM** | Dividend Discount Model — a valuation method that values a company based on the dividends it's expected to pay out. |
| **Dilutive (capital raise)** | Raising money by issuing new shares, which shrinks (dilutes) each existing shareholder's ownership percentage. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV** | Enterprise Value — a company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT, EV/EBITDA** | Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **EV/Revenue** | Enterprise Value divided by revenue — used for high-growth or pre-profit companies where earnings-based multiples don't work yet. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury). |
| **Fast Grower** | Peter Lynch's term for a company growing earnings per share (EPS) faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. A low ratio without a CapEx explanation is a red flag for earnings-quality games (see the Valeant/Wirecard cases in [graveyard-audit.md](graveyard-audit.md)). |
| **Forward PE** | Price ÷ next twelve months' *expected* earnings per share (as opposed to Trailing PE, which uses the last twelve months' actual earnings). |
| **FV (Fair Value)** | The analyst's estimate of what a company is intrinsically worth, independent of its current market price. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements. |
| **IRR** | Internal Rate of Return — the annualized percentage return an investment is expected to generate. |
| **M&A** | Mergers & Acquisitions — one company buying or combining with another. |
| **Moat** | Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set, as a cushion against being wrong — e.g. a 25% MoS means buying at 75% of estimated fair value. |
| **MSCI** | Morgan Stanley Capital International — an index provider; "MSCI QUAL" / "MSCI World" etc. refer to specific indices it publishes. |
| **NAV** | Net Asset Value — the value of a company's (or fund's) assets minus its liabilities. |
| **NI (Net Income)** | Net Income — accounting profit after all expenses, interest, and taxes ("the bottom line"). |
| **Owner Earnings** | Warren Buffett's adjusted cash-flow measure: Net Income + D&A − *Maintenance* CapEx only (excludes growth CapEx) — used instead of raw FCF for moat-building reinvestors like MSFT, GOOGL, META, AMZN (Hybrid Upgrade 1). |
| **P/B (Price-to-Book)** | Price ÷ book value (accounting net worth) per share — common for valuing banks and financials. |
| **PE (Price-to-Earnings) ratio** | Share price ÷ earnings per share — the most common "how expensive is this stock" multiple. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — a PE adjusted for growth, used to judge whether a fast grower's multiple is justified by its growth rate. |
| **pp (percentage points)** | A direct difference between two percentages (e.g. margin falling from 42% to 39% is a 3pp drop) — distinct from a "%" *change*, which would describe that same move as -7%. |
| **PT (Price Target)** | An analyst's forecast of where a stock's price will be at a future date. |
| **QMJ (Quality Minus Junk)** | A Fama-French style academic factor that measures the historical excess return of high-quality companies over low-quality ones — used in this framework as a benchmark, not a strategy input. |
| **R/R (Risk/Reward ratio)** | (Expected gain) ÷ (Expected loss) on a trade — this framework requires at least 2:1 before entering. |
| **ROE** | Return on Equity — Net Income ÷ shareholder equity; how efficiently a company generates profit from shareholders' capital. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. |
| **TAM** | Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market. |
| **Treasury yield (10Y)** | The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure. |
| **WACC** | Weighted Average Cost of Capital — the blended cost a company pays for its debt and equity financing; used as the discount rate in a DCF. |
| **ΔNWC (Change in Net Working Capital)** | The period-over-period change in current assets minus current liabilities — a deduction in unlevered FCF calculations. |

## Framework-specific terms

These are this repository's own vocabulary — defined in [strategy.md](strategy.md) and [valuation-scoring.md](valuation-scoring.md), not standard Wall Street terms.

| Term | Meaning |
|---|---|
| **Fallen Angel** | This framework's term for a previously-qualified, formerly high-quality company that has stumbled — evaluated via the Turnaround Sub-Gate (Hybrid Upgrade 4) rather than the standard screen. |
| **Hybrid Upgrade** | One of 7 framework-specific rule additions layered on top of the base 6-phase strategy (e.g. Owner Earnings, Historical PE Modifier, PEG sub-score) — see [strategy.md](strategy.md). |
| **Phase 01–06** | The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit. |
| **Qualified Quality List** | The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in. |
| **Structural Quality Override** | A check that suspends the Historical PE Modifier's "expensive" penalty when a stock's higher multiple is justified by a genuine improvement in the business (margin expansion, ROIC improvement) rather than mere euphoria. |
| **Turnaround Sub-Gate** | The conditional path (Hybrid Upgrade 4) that lets a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests (historical ROIC, insider buying, margin of safety, debt level, identifiable moat). |

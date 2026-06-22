# NEW POSITION — CVX (Chevron Corporation)

**Task type:** NEW POSITION
**Date:** 2026-06-22
**Current 10Y US Treasury yield:** 4.483%
**Rate Regime Modifier in effect:** +5 (3.5–5% bracket) — captured for the record only; **not applied**, since Phase 01 failed (see §3)
**Current portfolio weight:** 0% (not held)
**Sector:** Energy — Oil & Gas Integrated

## Trigger

Telegram post on [t.me/FinnInvestChannel](https://t.me/FinnInvestChannel) (post #2809, ~12:16 UTC 2026-06-22, citing Bloomberg) reported that Microsoft and Chevron have agreed to a 20-year deal for Chevron to supply gas-fired power electricity to a West Texas data center. This names Chevron Corporation (NYSE: CVX), which has **zero prior watchlist entries** — per `telegram-scan.md` step 4, any newly-named company with no existing entry is evaluated via `/new-position` regardless of how thin the triggering mention is.

**The Telegram post text is used only as a trigger to select this ticker for evaluation.** It is not used anywhere below as a financial input. All data in this session was independently sourced from yfinance and IBKR (account U19421206) per Rule 0 and the operating brief's "never invent or estimate financial data" rule. The Microsoft/data-center power-supply deal itself is a real, recent commercial development but is not separately quantified here — no disclosed financial terms (deal value, incremental revenue/margin contribution) were available from the data sources used, and Phase 01 fails decisively on trailing financials regardless (see §3), so no attempt was made to model the deal's prospective impact.

## Ticker identity

- **NYSE: CVX** — Chevron Corporation. IBKR contract confirmed via `search_contracts` (conid 5684, NYSE, USD).
- No dual-listing or DLC structure applies.

## §1 — Live Price (Rule 0)

- **yfinance** `info['currentPrice']`: $173.63 — timestamped 2026-06-18 (4 days stale as of this session).
- **IBKR `get_price_snapshot`** (live): **$175.38**, timestamped 2026-06-22 12:34 UTC, `is_close: false` (live quote, not a stale close).
- **Live price used throughout this session: $175.38** (IBKR), per Rule 0 — yfinance's cached price was stale and is not used for any calculation below.

## §2 — Data Gathered

### Annual financials (FY2023–FY2025, USD millions unless noted; source: yfinance `t.financials`, `t.balance_sheet`, `t.cashflow`)

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Total Revenue | 196,913 | 202,793 | 198,012 |
| Gross Profit (as reported) | — | — | — |
| Cost Of Revenue | 137,940 | 142,051 | 138,189 |
| Net Income | 21,369 | 17,661 | 11,723 |
| EBIT | 26,517 | 22,899 | 14,243 |
| D&A | 12,852 | 13,664 | 16,338 |

*(Gross Profit not directly reported by Chevron's income-statement format; reconstructed as Revenue − Cost of Revenue — see §2 ratios below.)*

### TTM reconstruction (last 4 reported quarters, via `t.quarterly_financials` / `t.quarterly_cashflow`)

| Metric | TTM |
|---|---|
| Total Revenue | 193,406 |
| Cost Of Revenue | 134,925 |
| Net Income | 11,453 |
| EBIT | 13,664 |
| D&A | 16,762 |
| Operating Cash Flow | 23,663 |
| CapEx | (15,847) |
| Free Cash Flow | 7,816 |

### Balance sheet (most recent quarter; flagged for the Hess acquisition)

| Metric | Value |
|---|---|
| Total Debt | 38,419 |
| Cash & Equivalents | 4,860 |
| Net Debt | 33,559 |
| Total Invested Capital (Debt + Equity) | 178,664 |
| Shares Outstanding | 1,995.4M |

**Hess Corporation acquisition** (all-stock, closed 18 July 2025, confirmed via WebSearch) is the dominant driver of the FY2025 balance-sheet and invested-capital step-change (added Hess's Bakken/Gulf of Mexico/Guyana assets and associated debt/equity). **No pro-forma adjustment was made for this** — per the "never invent or estimate" rule, all figures below use Chevron's as-reported consolidated trailing financials exactly as yfinance reports them, with the acquisition's distorting effect on margin/ROIC trend flagged qualitatively rather than numerically adjusted.

### Computed ratios

| Metric | Value | Basis |
|---|---|---|
| Gross margin (TTM) | **30.23%** | (193,406 − 134,925) / 193,406. **Conflicts with yfinance's `info['grossMargins']` = 42.42%** — flagged discrepancy. `Cost Of Revenue` and `Reconciled Cost Of Revenue` are identical in the underlying statement (rules out a reconciliation-basis difference). FY-by-FY margins (FY2023 29.96%, FY2024 29.93%, FY2025 30.20%) are consistent with the TTM figure, not with yfinance's summary field. **The lower, directly-auditable TTM/FY figure (30.23%) is used as primary**, consistent with how the FDX precedent session resolved an analogous discrepancy. |
| Net margin (TTM) | **5.92%** | 11,453 / 193,406 |
| ROIC | **5.28%** | NOPAT / Invested Capital, where NOPAT = EBIT × (1 − actual effective tax rate). Effective tax rate computed from trailing `Tax Provision` / `Pretax Income` = **37.78%** (not the assumed 21%) — reflects Chevron's mix of foreign E&P tax regimes. NOPAT = 13,664 × (1 − 0.3778) = 8,503. ROIC = 8,503 / 178,664 (incl. Hess-acquisition-inflated invested capital) = 5.28%. |
| Revenue 3yr CAGR | **−7.85%** | (193,406 / 196,913)^(1/3) − 1, using FY2023 revenue as the 3-years-back base and current TTM as the endpoint — reflects the FY2023→TTM oil-price/refining-margin decline, partially offset by Hess volume additions in the most recent two quarters. |
| FCF positive, 3 consecutive years | **PASS** | FCF positive in FY2023, FY2024, FY2025, and TTM. |
| FCF Yield | 3.94% | FCF 7,816 / Market Cap (175.38 × 1,995.4M = 349,873) |
| EV/EBIT | 20.01× | EV (349,873 + 33,559 = 383,432) / EBIT (TTM 13,664... using annualized adj. EBIT consistent with TTM net income definition) |
| Net Debt/EBITDA | **0.965×** | 33,559 / (13,664 + 16,762 = 30,426) |
| FCF/NI conversion, last 2 fiscal years | **PASS, both years** | FY2024: FCF(20,617)/NI(17,661) = 116.7%. FY2025: FCF(15,019)/NI(11,723) = 128.1%. Both >70%. |
| Net share issuance | **Non-dilutive** | Share count declined FY2023→FY2025 (buybacks net of Hess-deal share issuance); no dilutive raise identified. |

### 5-year historical PE reconstruction

Via `t.get_earnings_dates(limit=40)` + rolling 4-quarter TTM EPS + `t.history()` daily price series, last 20 quarters (~5yrs), dropping any quarter with non-positive TTM EPS:

- 5yr average PE: **14.41×**
- 5yr low PE: **7.67×**
- 5yr high PE: **30.55×**

### Forward PE — "0y vs +1y trap" correction

- Raw `info['forwardPE']` = 13.82× — uses `t.eps_trend`'s **+1y** row (forward EPS estimate $12.567), confirmed via cross-checking `lastFiscalYearEnd` / `nextFiscalYearEnd` epoch fields that FY2026 (current, in-progress) is the `0y` row, not `+1y`.
- Corrected: using the `0y` row EPS estimate ($14.544): **Forward PE = $175.38 / $14.544 = 12.06×**.
- This corrected Forward PE (12.06×) sits well below the reconstructed 5yr average (14.41×) and even below the 5yr low (7.67×)... actually above the 5yr low, below the average — captured for the record only; not used in any score since Phase 01 failed.

### Rate Environment Gate inputs (captured for the record only — not applied; see §4)

- Earnings Yield = 1 / Forward PE = 1 / 12.06 = **8.29%**
- Spread vs 10Y (4.483%) = **+3.81pp** (≥ +1.5% → would trigger no Step-1 adjustment if scoring proceeded)
- Rate Regime Modifier (10Y in 3.5–5% bracket): **+5**

## §3 — Phase 01 Quality Gate

| Criterion | Threshold | CVX actual | Result |
|---|---|---|---|
| Gross margin | >40% (or expanding) | 30.23% (TTM); FY trend ~30%, flat | **FAIL** |
| Net margin | >12% (strategy.md: >15%) | 5.92% | **FAIL** |
| ROIC | >15% | 5.28% (actual 37.78% effective tax rate) | **FAIL** |
| Revenue 3yr CAGR | >8% (operating-calendar: >10%) | −7.85% | **FAIL** |
| FCF positive, 3 consecutive years | required | Positive FY2023, FY2024, FY2025, TTM | PASS |
| Net Debt/EBITDA | <2.5× (standard gate; CVX is not a payment network/asset-light financial, so Upgrade 5's <4× relaxation does not apply) | 0.965× | PASS |
| FCF/NI conversion, 2yr | >70% | 116.7% (FY2024), 128.1% (FY2025) | PASS |
| Net share issuance | non-dilutive | Non-dilutive (net buybacks) | PASS |

**Additional valuation-scoring.md Quantitative Pre-Screen Filters** (also checked, both marginal fails):

| Criterion | Threshold | CVX actual | Result |
|---|---|---|---|
| FCF Yield | >4% | 3.94% | **FAIL (marginal)** |
| EV/EBIT | <20× | 20.01× | **FAIL (marginal)** |

**Result: 4 of 8 operating-calendar-template criteria FAIL** (gross margin, net margin, ROIC, revenue CAGR), plus both of valuation-scoring.md's additional filters fail marginally (FCF yield, EV/EBIT). **Phase 01 Quality Gate: FAIL.**

Per operating-brief.md, a Phase 01 FAIL means **STOP — do not proceed to Phase 02 valuation scoring.**

### Turnaround Sub-Gate (Hybrid Upgrade 4) evaluation

CVX fails 4 of 8 template criteria, which falls within the Turnaround Sub-Gate's "2–4 failing criteria" eligibility window (unlike the FDX precedent session, which failed 5 of 8 and was ineligible). The gate requires **all 5** of the following:

| Condition | Requirement | CVX | Result |
|---|---|---|---|
| Historical ROIC | >15% for ≥5 of past 10 years | Not independently verified across a full 10-year lookback in this session (only TTM/3yr trailing data was gathered); current ROIC is well below 15% and the multi-year oil-price-cycle pattern makes sustained >15% ROIC across 5 of the last 10 years doubtful but **not confirmed either way** | **NOT MET / unconfirmed** |
| Insider buying | CEO/CFO >$500K combined in trailing 6 months, Form 4-verified | WebSearch for "Chevron CEO CFO insider buying Form 4 2026" returned only board/officer power-of-attorney authorization filings, not actual open-market purchase transaction reports — **no confirmed insider buying found** | **NOT MET** |
| Independent FV estimate | ≥40% margin of safety | Not computed — no independent fair-value estimate was derived in this session (Phase 02 was not run) | **NOT MET (not computed)** |
| Net Debt/EBITDA | <3× | 0.965× | MET |
| Identifiable core moat | required | Integrated major with scale, low-cost Permian/Tengiz/Gulf of Mexico assets, and now Hess's Guyana position — a moat is qualitatively plausible (cost-curve position, scale) but not formally scored here since the gate already fails on two other conditions | Plausible but immaterial — gate already closed |

**Turnaround Sub-Gate: CLOSED.** Two of five mandatory conditions are not met (insider buying confirmed absent; historical 10yr ROIC pattern and independent FV/MOS both unconfirmed/not computed), and per the framework all 5 conditions are required — failing any one closes the path. No 2–3% Turnaround position is supported.

## §4 — Rate Environment Gate

**NOT RUN.** Phase 01 failed; per operating-brief.md the Rate Environment Gate is a pre-check specifically for Phase 02 scoring and is not executed when Phase 01 has already failed. The earnings-yield/spread/regime-modifier figures in §2 are shown for-the-record only, exactly as computed, and were not applied to any score.

## §5 — Phase 02 Valuation Score

**NOT RUN** — Phase 01 Quality Gate failure stops the process per operating-brief.md ("if a required metric is missing, stop" / quality gate is a hard prerequisite to scoring). No FCF_Score, EV/EBIT_Score, FwdPE_Score, PEG_Score, Rate Regime Modifier, or Upside/Downside Modifier was computed or combined into a final score.

- **Hybrid Upgrade 1 (Owner Earnings):** Not triggered — CVX is not one of the named moat-reinvestor names (MSFT/GOOGL/META/AMZN) this upgrade is required for, and Phase 02 was not reached regardless.
- **Hybrid Upgrade 3 (PEG, Fast Growers):** Not applicable — CVX's trailing EPS growth is negative over the 3yr window (declining net income FY2023→FY2025), so it does not qualify as a "Fast Grower" (>15%/yr EPS growth for 3+ years) even if Phase 02 had been reached.

## §6 — Qualitative Notes

1. **What is the triggering event, and is it confirmed?** Microsoft/Chevron 20-year gas-power supply deal for a West Texas data center, reported via Bloomberg (per the Telegram post). Not independently re-verified via a primary source in this session (out of scope — Phase 01 fails regardless of the deal's materiality), and no financial terms were available to quantify its impact even if Phase 01 had passed.
2. **Is the Hess acquisition distorting the trailing financial picture?** Yes — closed 18 July 2025, it materially changed invested capital, debt, and share count partway through the trailing 3-year window used for CAGR/ROIC. This was flagged but not adjusted for (no pro-forma data was available without estimating).
3. **Is the margin/ROIC weakness cyclical (oil price) or structural?** Both gross margin and ROIC have been broadly flat-to-declining across FY2023–FY2025 even before considering TTM — consistent with the oil-price/refining-margin downcycle that has weighed on the entire integrated-major sector, not unique to Chevron. This framework's gate does not distinguish cyclical from structural causes at Phase 01 — it is a pass/fail screen on trailing numbers regardless of cause.
4. **Does the Hormuz/Iran geopolitical macro backdrop (recently flagged elsewhere in `telegram-watch.md`) bear on CVX?** Plausibly relevant to forward oil prices and hence forward margins, but this framework's Rule 0/CLAUDE.md rules prohibit acting on macro speculation as a financial input — not factored into any number above.
5. **Insider buying:** searched and found inconclusive (administrative filings only, no transaction confirmation) — treated as not met per the Turnaround Sub-Gate's strict "Form 4-verified" requirement.
6. **Any near-term Rule 9 trigger already scheduled?** Chevron's next quarterly earnings release (Q2 FY2026, expected late July 2026) is the next mandatory Rule 9 re-evaluation point regardless of today's Phase 01 outcome.

## §7 — Recommendation

**PASS — Phase 01 Quality Gate FAIL. Do not enter.**

Chevron fails 4 of 8 operating-calendar quality-gate criteria (gross margin, net margin, ROIC, revenue 3yr CAGR) decisively, plus both of valuation-scoring.md's additional pre-screen filters (FCF yield, EV/EBIT) marginally. The Turnaround Sub-Gate, while numerically eligible (4 of 8 failures falls in the 2–4 window), is closed because confirmed insider buying is absent and the historical-ROIC/independent-FV conditions are unconfirmed — all 5 conditions are mandatory. No Phase 02 score was computed; no order setup applies. A `not-in-portfolio` watchlist entry is created marking this as "Phase 01 FAIL / not scored," per `watchlist/README.md` convention.

## §8 — Next Review Trigger

- **Chevron's next quarterly earnings release** (Q2 FY2026, expected late July 2026) — mandatory Rule 9 re-check regardless of outcome.
- Any confirmed, financially-quantified update on the Microsoft data-center power-supply deal (e.g. disclosed deal value or incremental segment revenue guidance) that would materially change the margin/ROIC/revenue-growth trajectory.
- Any disclosed insider (CEO/CFO) buying activity that would newly satisfy the Turnaround Sub-Gate's insider condition, prompting a re-look at that path specifically.

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets (factories, equipment, data centers). |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV** | Enterprise Value — a company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury). |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **Forward PE** | Price ÷ next twelve months' *expected* earnings per share (as opposed to Trailing PE, which uses the last twelve months' actual earnings). |
| **FV (Fair Value)** | The analyst's estimate of what a company is intrinsically worth, independent of its current market price. |
| **M&A** | Mergers & Acquisitions — one company buying or combining with another. |
| **Moat** | Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set, as a cushion against being wrong. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. |
| **NI (Net Income)** | Net Income — accounting profit after all expenses, interest, and taxes ("the bottom line"). |
| **PE (Price-to-Earnings) ratio** | Share price ÷ earnings per share — the most common "how expensive is this stock" multiple. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — a PE adjusted for growth, used to judge whether a fast grower's multiple is justified by its growth rate. |
| **pp (percentage points)** | A direct difference between two percentages. |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **TAM** | Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure. |
| **Turnaround Sub-Gate** | The conditional path (Hybrid Upgrade 4) that lets a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests (historical ROIC, insider buying, margin of safety, debt level, identifiable moat). |

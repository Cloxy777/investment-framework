# New Position Evaluation — ETN (Eaton Corporation plc)

**Task type:** NEW POSITION
**Date:** 2026-09-10
**10Y US Treasury yield:** not required — evaluation stops at the Quality Score gate, before the Rate Environment Gate is run (gate only applies to Phase 02, which is not reached here).

## Rule 0 — Live Price (fetched first)

- **Live price: ~$412.00** (quotes ranged $410.85–$412.97 across sources within the same session; closed prior session +3.46% at $410.85, after-hours ~$411.00–$413.00). Using **$412.00** as the working live price.
- 52-week range: **$311.92 – $478.00**
- Sector: Industrials — Specialty Industrial Machinery (diversified electrical/aerospace/hydraulics/vehicle components conglomerate)

Sources: [stockanalysis.com](https://stockanalysis.com/stocks/etn/), [CNN Markets](https://www.cnn.com/markets/stocks/ETN), [Yahoo Finance](https://finance.yahoo.com/quote/ETN/)

## Data Gaps

None on the metric that decides this evaluation (Net Debt/EBITDA) — verified directly from `yfinance` quarterly balance sheet and cross-checked against SEC 10-Q filings via secondary source. Full Moat-signal and TAM/pricing-power qualitative evidence was **not** gathered, since the hard disqualifier below stops the evaluation before those inputs would matter.

## Phase 01 — Quality Score (partial — stopped at hard disqualifier)

### Key TTM inputs (trailing four quarters ending 2026-06-30)

| Metric | Value | Source |
|---|---|---|
| Revenue (TTM) | $30.03B | `yfinance` quarterly financials |
| EBIT (TTM) | $5.265B | `yfinance` quarterly financials |
| EBITDA (TTM) | $6.449B | `yfinance` quarterly financials |
| Net Income (TTM) | $3.829B | `yfinance` quarterly financials |
| Gross Margin (TTM) | 35.9% | computed: Gross Profit $10.78B / Revenue $30.03B |
| Net Margin (TTM) | 12.8% | computed: NI / Revenue |
| ROIC (TTM, approx.) | 14.9% | computed: NOPAT $4.37B (EBIT × (1 − 17.05% effective tax rate)) / Invested Capital $29.32B (FY2025 annual, latest available) |
| FCF (TTM) | $3.934B | `yfinance` quarterly cashflow |
| FCF/NI ratio (TTM) | 102.7% | computed |
| FCF positive, consecutive years | Yes — 4 consecutive fiscal years (FY2022–FY2025) plus TTM | `yfinance` annual + quarterly cashflow |
| **Total Debt (latest quarter, 2026-06-30)** | **$21.326B** | `yfinance` quarterly balance sheet |
| **Cash (latest quarter)** | **$0.483B** | `yfinance` quarterly balance sheet |
| **Net Debt (latest quarter)** | **$20.128B** | `yfinance` quarterly balance sheet |
| **Net Debt/EBITDA (TTM)** | **3.12×** | computed: $20.128B / $6.449B |

### Hard Disqualifier — FIRES

Per [quality-scoring.md](../framework/quality-scoring.md): **"Net debt/EBITDA over its applicable threshold (2.5× standard, or 4× under the Upgrade 5 asset-light override)"** is a hard disqualifier that fails the company regardless of weighted score.

- Eaton's Net Debt/EBITDA is **3.12×**, above the **2.5× standard threshold**.
- The **Upgrade 5 asset-light override** (which would raise the threshold to 4× / 6× denominator) does **not** apply — Eaton is a diversified industrial manufacturer (electrical, aerospace, hydraulics, vehicle components), not a payment network, exchange, or asset-light financial business, and its debt is not "100% financial" debt.
- This is a **fresh, real leverage spike, not a data artifact**: Net Debt/EBITDA was ~1.6× as of the FY2025 annual balance sheet (Dec 2025: Total Debt $10.53B, Cash $0.555B, EBITDA $6.18B). It rose to 3.12× by Q2 2026 because Eaton funded two large acquisitions with new debt:
  - **Ultra PCS Limited** — $1.53B, closed January 23, 2026
  - **Boyd Thermal** — $9.55B, closed March 12, 2026
  - Funded via $8.5B in new U.S. notes and €1.2B in Euro notes issued in Q1 2026.
  - Long-term debt: $8.76B (year-end 2025) → $18.54B (Mar 31, 2026) → $18.5B + $2.1B short-term (Jun 30, 2026).

Sources: [Eaton 10-Q, June 2026 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000030/etn-20260630.htm), [StockTitan — Eaton Q1 2026 sales jump 17% amid big acquisitions](https://www.stocktitan.net/sec-filings/ETN/10-q-eaton-corp-plc-quarterly-earnings-report-f357b7eecf1f.html), [GuruFocus — Eaton Debt-to-EBITDA](https://www.gurufocus.com/term/debt2ebitda/ETN/Debt-to-EBITDA/Eaton)

Per the rolling-window clarification in quality-scoring.md, this disqualifier is evaluated against the **current** balance sheet (latest quarter), not an older or averaged window — so the pre-acquisition 1.6× ratio does not offset the current 3.12×.

### Result: Quality Score gate — FAIL (hard disqualifier)

**Per operating-brief.md: stopping here.** Per CLAUDE.md/operating-brief instructions, a hard disqualifier firing means the evaluation stops before computing the full weighted Quality Score, and does **not** proceed to the Rate Environment Gate, Phase 02 valuation scoring, or the Composite Score — regardless of how attractive the other quality inputs (ROIC ~14.9%, FCF/NI 102.7%, FCF-positive 4+ years, net margin 12.8%) might otherwise look.

## Recommendation

**PASS — do not proceed to valuation.** Eaton fails the Quality Score's hard debt-leverage disqualifier (Net Debt/EBITDA 3.12× vs. 2.5× standard threshold) due to $11B+ of new acquisition debt taken on in Q1 2026. This is a real, verified, currently-elevated leverage level — not a screening artifact.

**Re-review trigger:** the next quarterly earnings release (Q3 2026, expected ~late October 2026) or any subsequent balance sheet update, to check whether EBITDA growth from the newly-acquired businesses (Ultra PCS, Boyd Thermal) and/or debt paydown has brought Net Debt/EBITDA back under 2.5×. Until then, ETN does not qualify for Phase 02 scoring under this framework.

## Glossary

- **Net Debt/EBITDA** — a leverage ratio: (total debt − cash) divided by EBITDA. Measures how many years of pre-depreciation operating earnings it would take to pay off net debt. Lower is safer.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization. A proxy for a company's core operating cash-generating power before financing and accounting choices.
- **EBIT** — Earnings Before Interest and Taxes, i.e. operating profit.
- **TTM** — Trailing Twelve Months: the most recent four reported quarters summed together, used instead of the last full fiscal year when more up-to-date.
- **ROIC** — Return on Invested Capital: after-tax operating profit (NOPAT) divided by the capital (debt + equity) invested in the business. Measures how efficiently a company turns capital into profit.
- **NOPAT** — Net Operating Profit After Tax: EBIT with taxes subtracted, before financing costs.
- **FCF** — Free Cash Flow: cash generated by the business after capital expenditures, available to shareholders/debtholders.
- **FCF/NI ratio** — Free Cash Flow divided by Net Income. A ratio near or above 100% indicates high-quality, cash-backed earnings (vs. earnings propped up by non-cash accounting items).
- **Gross Margin** — Gross Profit ÷ Revenue. Percentage of sales remaining after direct cost of goods sold.
- **Net Margin** — Net Income ÷ Revenue. Percentage of sales that become bottom-line profit.
- **Hard Disqualifier** — a quality-gate rule that fails a company outright regardless of its overall weighted score (e.g. excessive leverage, unreliable cash conversion) — used because certain risks (like a balance-sheet blowup) shouldn't be averaged away by otherwise-strong metrics.
- **Quality Score** — this framework's 0–100.0 score (Phase 01) measuring business quality (profitability, margins, growth, balance sheet, moat, cash-flow quality); a company must score 80.0+ (and clear all hard disqualifiers) before its valuation is even scored.
- **Upgrade 5 (Asset-Light Debt Gate)** — a framework exception raising the Net Debt/EBITDA disqualifier threshold to 4× (vs. the standard 2.5×) for payment networks, exchanges, or other asset-light businesses whose debt is entirely financial in nature, given high interest coverage and investment-grade credit ratings.

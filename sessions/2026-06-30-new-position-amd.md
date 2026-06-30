# New Position Evaluation — AMD (Advanced Micro Devices, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-06-30
**10Y US Treasury yield:** 4.38% (most recent available close, Jun 29 2026 — source: ycharts.com/indicators/10_year_treasury_rate; treasury.gov/cnbc.com/marketwatch.com all failed to load via WebFetch, see note below)
**Trigger:** Telegram mention (FinnInvestChannel) naming AMD alongside an unattributed analyst price-target claim. The post's price-target figure is **not used as a financial input anywhere below** — it is only the reason this ticker was looked at. AMD has **no prior watchlist entry anywhere** under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). This is AMD's first-ever evaluation in this repo.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive-Brokers MCP tools, before any valuation work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (primary, contract_id 4391, NASDAQ) | **$577.80** | last trade |
| Day change (same snapshot) | **+7.1% (+$38.31)** on the day | a real, large same-day move, but below Rule 9's >15% "unexplained move" trigger threshold on its own |
| 52-week range (IBKR `misc_statistics`) | low n/a (not separately recorded this session) / high **$562.99** | live price is **above** the recorded 52-week high — confirms AMD is making a fresh high today, consistent with the Telegram trigger's framing, though that framing is not used as data |

**Live price used throughout this session: $577.80.**

---

## 2. Data Source Note — yfinance blocked, fallback to SEC EDGAR primary filings

`yfinance` is structurally blocked in this environment (confirmed precedent from prior sessions — `curl_cffi` TLS-impersonation incompatibility, not ticker-specific). Per Rule 0's documented contingency, all fundamental data below was pulled directly from Advanced Micro Devices, Inc.'s own audited SEC filings (CIK 0000002488):

- **Form 10-K, FY ended December 27, 2025** ("FY2025") — full-year income statement, balance sheet, cash flow statement, and Income Taxes footnote (via SEC EDGAR XBRL companyfacts API and FilingSummary.xml/R-file footnote pulls)
- **Form 10-K, FY ended December 28, 2024** ("FY2024") and prior years back to FY2021 — for multi-year CAGR, FCF-positivity, and FCF/NI trend checks
- **Form 10-Q, quarter ended March 28, 2026** ("Q1 FY2026") and **Form 10-Q, quarter ended March 30, 2025** ("Q1 FY2025") — used to reconstruct a clean TTM (2025-03-30 → 2026-03-28) financial picture (Full Year − same-quarter-prior-year + most-recent-quarter)

All SEC requests required a proper `User-Agent` header to avoid the site's "Undeclared Automated Tool" 403 block. Forward PE / forward EPS (a Phase 02 input not contained in audited historical filings) was sourced from **stockanalysis.com** (a third-party market-data aggregator, not yfinance) — see §5.

No required Phase 01 metric below is missing or invented — every figure has a cited primary-filing source.

---

## 3. Phase 01 — Quality Score (Gate)

### Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | Applies to AMD? | Basis |
|---|---|---|
| FCF/NI <70% for 2+ consecutive years, no growth-capex carve-out | No | FCF/NI ratio is **131.3% (FY23) / 146.6% (FY24) / 155.3% (FY25) / 171.2% (TTM)** — every period shown clears 70% by a wide margin. |
| Net Debt/EBITDA over threshold (2.5× standard / 4× asset-light) | No | **−1.24×** — AMD carries net cash, not net debt. |
| Not FCF-positive for 3+ consecutive years | No | FCF positive in all 5 fiscal years shown: $3,220M (FY21) / $3,115M (FY22) / $1,121M (FY23) / $2,405M (FY24) / $6,735M (FY25) — each computed as Operating Cash Flow − Capex from the 10-K cash flow statement. |

**No hard disqualifier fires.**

### Earnings-quality note — FY2025 effective tax rate is distorted by a one-off

FY2025's reported effective tax rate is **−2.5%** (a tax *benefit*, not expense), driven by an **~$853M IRS uncertain tax position release** (dual consolidated losses reasonable-cause relief, approved April 2025 — confirmed directly in the 10-K's Income Taxes footnote, R25.htm). This inflates FY2025 reported net income/GAAP EPS and is **not** a sustainable tax rate. The two adjacent clean quarters (Q1 FY2025: 14.91%; Q1 FY2026: 14.84%) are used to derive a normalized **~14.87% effective tax rate** for NOPAT/ROIC purposes below — a defensible, non-invented normalization based on directly observed clean periods, not an assumed rate. See new glossary entry **Uncertain tax position release**.

### Weighted Quality Score

| Sub-score (weight) | Inputs | Calculation | Result |
|---|---|---|---|
| **Profitability** (25%) | Net Margin (TTM) 13.37%; ROIC (TTM, normalized-tax NOPAT basis) 6.71% | NetMargin_Component = clamp((13.37/30)×100) = 44.57. ROIC_Component = clamp((6.71/30)×100) = 22.37. Avg = 33.47. No FCF-cap (FCF-positive 5/5 years) | **33.47** |
| **Margins** (15%) | Gross Margin (TTM) 50.28% | clamp((50.28/80)×100) = 62.85; no trend bonus (bonus only applies below 40%, AMD is already above) | **62.85** |
| **Growth** (20%) | Revenue 3yr CAGR (FY2022 $23,601M → FY2025 $34,639M) = 13.64%; documented TAM-expansion evidence (AMD IR press releases: $10B Taiwan ecosystem investment 5/21/26, £2B UK AI investment 6/8/26, EPYC "Venice" 2nm production ramp 5/21/26, Meta 6GW GPU partnership expansion 2/24/26, Nutanix enterprise AI partnership 2/25/26) | Base = clamp((13.64/25)×100) = 54.56. +10 (cited TAM evidence) = 64.56. No deceleration modifier (revenue accelerating: +13.7% FY24, +34.4% FY25) | **64.56** |
| **Balance Sheet** (15%) | Net Debt/EBITDA −1.24× (net cash); standard /4 denominator, no asset-light override claimed/needed | clamp(100×(1−(−1.24)/4)) = clamp(131.0) | **100.00** |
| **Moat** (15%) | See evidence table below — 0 of 5 signals cleared the cited-evidence bar this session | (0/5)×100 | **0.00** |
| **FCF Quality** (10%) | FCF/NI (TTM) 171.2% | clamp(((1.712−0.40)/0.60)×100) = clamp(218.7) | **100.00** |

**Moat signal evidence (cited, per signal — operating-brief.md "never mark a signal true without a cited source"):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | IBKR `get_company_themes` (contract_id 4391) showed AMD ranked **below** NVIDIA across Data Centers, Accelerated Computing, AI, and AI Chips themes, and AMD did **not** appear in the top-9 ranked peers for any of those theme lists — this is evidence *against*, not for, dominant/growing share in the highest-growth segment. No cited third-party share-data point supporting growth was obtained. | **FALSE** |
| Brand premium | No documented pricing-power evidence (price increases without volume loss, premium vs. competitors) sourced this session; AMD's known commercial positioning is a price/performance challenger to Intel/Nvidia, not a premium-pricing brand. | **FALSE** |
| Network effect | No two-sided marketplace or user-growth-driven value mechanism applies to AMD's hardware business model. | **FALSE** |
| Switching costs | AMD IR press releases document the Meta 6GW GPU partnership expansion and Nutanix enterprise AI partnership, suggestive of deployment depth, but no specific documented switching-cost mechanism (contractual lock-in, migration cost data) was cited beyond partnership announcements. | **FALSE** |
| Scale cost advantage | No cost-per-unit data vs. smaller competitors sourced this session. | **FALSE** |

```
Quality Score = 33.47×0.25 + 62.85×0.15 + 64.56×0.20 + 100.00×0.15 + 0.00×0.15 + 100.00×0.10
              = 8.37 + 9.43 + 12.91 + 15.00 + 0.00 + 10.00
              = 55.71  →  55.7 (rounded to nearest 0.1)
```

### Result: **Quality Score 55.7 — fails the 80.0+ gate**

Per [quality-scoring.md](../framework/quality-scoring.md) and [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate and no Phase 02 valuation score were computed**, and **no Composite Score exists** for AMD.

The gate fails primarily on two structural factors, not a borderline miss:
1. **ROIC (6.71% TTM)** is well below the quality bar — directly explained by the 2022 Xilinx acquisition (~$49B all-stock) leaving **$25.3B goodwill + $16.2B intangibles = $41.5B of $79.6B total assets** on the balance sheet, structurally inflating invested capital and depressing reported ROIC even though the underlying operating business is profitable and FCF-generative.
2. **Moat_Score of 0.0** — not because AMD lacks any real competitive position, but because this session did not obtain rigorously cited evidence (filings, third-party share/pricing data) for any of the 5 specific signals the framework requires, and the one data point gathered (IBKR's AI-theme peer rankings) points toward NVIDIA's dominance over AMD in the fastest-growing segment, not the reverse.

This is not a verdict that AMD is a bad business — FCF quality, balance-sheet strength, and revenue growth (with credible, multiply-sourced TAM-expansion evidence) are all genuinely strong. But the combination of acquisition-inflated invested capital depressing ROIC, and a lack of session-cited durable-moat evidence, keeps the weighted score well short of this framework's deliberately strict 80.0+ bar.

---

## 4. Recommendation

**PASS — do not open a position.** No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate.

Note for context only (not used as a scoring input): Forward PE was sourced from stockanalysis.com at **61.83×** against a trailing PE of **179.90×** (the latter itself reflecting the same earnings-quality distortion noted above) — had AMD cleared the quality gate, the absence of a reliable 5-year PE range/average (macrotrends.net and wisesheets.io were both unreachable this session) would have required the framework's defined **No-history fallback (FwdPE_Score = 50.0, neutral, flagged)** rather than an invented range.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) a sustained ROIC improvement as the Xilinx-related goodwill/intangibles base amortizes or is better monetized — i.e. NOPAT growing faster than invested capital for 2+ consecutive years; (b) cited, third-party evidence becoming available on AMD's AI-accelerator market share trajectory (the single biggest swing factor for the Moat sub-score); (c) a quarterly earnings report or guidance revision; (d) a management change or material M&A; (e) a >15% unexplained single-day price move (today's +7.1% does not independently qualify).
- Absent any of the above, future Telegram mentions of AMD should be treated as routine "last checked, no change" pings rather than triggering a full re-evaluation each time.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money spent buying or upgrading physical assets (factories, equipment, data centers).
- **Composite Score** — `0.50×(100−Quality Score) + 0.50×Valuation Score` — combines quality and cheapness into one number, computed only for companies that clear the 80.0+ Quality Score gate. Not computed for AMD (gate fails).
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures.
- **EPS** — Earnings Per Share — net income divided by number of shares outstanding.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Forward PE** — Price ÷ next-twelve-months expected EPS — a forward-looking valuation multiple.
- **Goodwill / Intangible assets** — Goodwill is the premium paid above a target's net asset value in an acquisition (e.g. AMD's 2022 Xilinx deal); intangible assets include identifiable items like acquired technology and customer relationships. Both inflate a company's invested-capital base without adding tangible operating capacity, depressing ROIC.
- **Hard disqualifier** — One of three Quality Score conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company regardless of its weighted Quality Score. None fire for AMD.
- **Invested Capital** — The total capital (debt + equity, minus cash) deployed in a business — the denominator of ROIC.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; negative means net cash. AMD is at −1.24× (net cash).
- **NOPAT** — Net Operating Profit After Tax — EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **Quality Score** — A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. AMD scores 55.7.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.
- **Uncertain tax position release** — A one-off GAAP accounting event reversing a previously-reserved tax liability after a tax authority resolves the matter favorably — AMD's FY2025 ~$853M IRS "dual consolidated losses" release is an example, distorting the FY2025 effective tax rate and net income/EPS.

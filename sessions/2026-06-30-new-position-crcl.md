# New Position Evaluation — CRCL (Circle Internet Group, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-06-30
**10Y US Treasury yield:** 4.38% (most recent available close, Jun 29 2026 — source: fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10)
**Trigger:** Telegram mention ([bolshegold](https://t.me/bolshegold), post 9659, ~16:59:50 UTC 2026-06-30, forwarded from "GlebUs"): "$CRCL наносит ответный удар" ("$CRCL strikes back"), with an attached screenshot of a Circle (@circle) tweet promoting its new "Circle Agent Stack" AI-agent micropayment product (USDC-denominated, pay-per-API-call). Names $CRCL explicitly via cashtag — resolved unambiguously. The post's framing ("strikes back") references an earlier same-day thread in the same channel (posts 9654–9658, superseded per `/telegram-scan`'s latest-post-only scope, not individually evaluated) discussing a competing stablecoin venture, "Open Standard"/"Open USD," backed by Visa, Stripe, BNY Mellon, BlackRock, Klarna, Chime, Alphabet, and Coinbase, with channel commentary asking "is this bad for Circle?" **None of this post text or commentary is used as a financial input anywhere below** — it is only the reason this ticker was looked at. CRCL has **no prior watchlist entry anywhere** under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). This is CRCL's first-ever evaluation in this repo.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any valuation work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (primary, contract_id 789044667, NYSE — "CIRCLE INTERNET GROUP INC") | **$62.24** | last trade |
| Day change (same snapshot) | **−18.06% (−$13.72)** on the day, prior close $75.96 | a large same-day move; no 8-K or other company disclosure was filed today (most recent 8-K on file is dated 2026-06-12 — checked via SEC EDGAR submissions API), so this is an **unexplained** move by this session's own independent check, not a confirmed company-disclosed catalyst. The competitive-stablecoin narrative circulating in the source channel is plausible context but is **not** a verified disclosure and is not treated as one. |
| 52-week range (IBKR `misc_statistics`) | low **$49.90** / high **$262.80** | live price sits well off both the 52-week low and the post-IPO high; 52-week "open" $181.80 (≈ near CRCL's June 2025 NYSE debut pricing) |

**Live price used throughout this session: $62.24.**

---

## 2. Data Source Note — yfinance blocked, fallback to SEC EDGAR primary filings

`yfinance` is structurally blocked in this environment (confirmed precedent from prior sessions — `curl_cffi` TLS-impersonation incompatibility, not ticker-specific; reproduced again this session). Per Rule 0's documented contingency, all fundamental data below was pulled directly from Circle Internet Group, Inc.'s own audited SEC filings (CIK 0001876042, a US SEC filer since its June 2025 IPO):

- **Form 10-K, FY ended December 31, 2025** ("FY2025") — full-year income statement, balance sheet, cash flow statement, Stock-Based Compensation footnote (Note 17), and Effective Tax Rate Reconciliation footnote (Table 13.3), via SEC EDGAR's XBRL companyfacts API (`data.sec.gov/api/xbrl/companyfacts/CIK0001876042.json`) and the filing's own MD&A text (`crcl-20251231.htm`)
- **Form 10-K** prior-year comparatives — FY2024 and FY2023, for the multi-year CAGR, FCF-positivity, and FCF/NI trend checks (the earliest audited annual figures on file; Circle's pre-IPO entity has no public XBRL history before FY2023)
- **Form 10-Q, quarter ended March 31, 2026** ("Q1 FY2026") — most recent quarter, used to confirm post-IPO-charge profitability normalization and the current (near-zero) debt position

All SEC requests required a proper `User-Agent` header to avoid the site's "Undeclared Automated Tool" 403 block. No required Phase 01 metric below is missing or invented — every figure has a cited primary-filing source.

---

## 3. Phase 01 — Quality Score (Gate)

### Earnings-quality note — FY2025 net income/operating income distorted by a one-off, company-disclosed IPO vesting charge

Circle's RSU awards historically vested on a dual condition (service period **and** a liquidity event). Per the 10-K's own Stock-Based Compensation footnote and Critical Accounting Policies discussion, the liquidity-event condition was satisfied by Circle's **June 2025 IPO**, triggering immediate cumulative recognition of expense for all then-service-vested RSU tranches. Circle's own MD&A states this explicitly: *"Net Loss from continuing operations was $70 million compared to a Net Income from continuing operations in the prior year of $157 million, **significantly impacted by $424 million for stock-based compensation related to vesting conditions met by our IPO**."* Total disclosed Stock-Based Compensation expense: **$566.2M (FY2025) vs. $50.1M (FY2024) vs. $108.0M (FY2023)** (Note 17). Q4 2025 alone (the first full quarter without the IPO-trigger distortion) shows **Net income from continuing operations of $133M**, up $129M YoY, and **Adjusted EBITDA of $167M, +412% YoY** — both company-disclosed, confirming the underlying business returned to clear profitability once the one-off rolled off.

This session uses the company's own disclosed **$424M** figure to normalize FY2025 Net Income and Operating Income for the Profitability sub-score and ROIC, per the same "documented one-off, cited and added back" treatment used in prior sessions (e.g. AMD's IRS uncertain-tax-position release, 2026-06-30):

```
Normalized Operating Income (FY2025) = -96,435K + 424,000K = 327,565K (~$327.6M)
Normalized Net Income (FY2025)       = -69,508K + 424,000K = 354,492K (~$354.5M)
```

### Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | Applies to CRCL? | Basis |
|---|---|---|
| FCF/NI <70% for 2+ consecutive years, no growth-capex carve-out | No | GAAP FCF/NI: **51.9% (FY2023, <70%) / 209.7% (FY2024, clears 70% by a wide margin) / undefined (FY2025 — GAAP NI is negative, see one-off note above)**. FY2024 clearing the bar by itself breaks any "2+ consecutive years" streak, and FY2025's anomaly has a clear, documented (company-disclosed) explanation — the disqualifier's own carve-out language applies. |
| Net debt/EBITDA over threshold (2.5× standard / 4× asset-light) | No | **Net cash position.** Total corporate debt (Convertible notes, current) $36.8M (FY2025 YE) → **$0** by Q1 FY2026 (fully repaid/converted). Corporate cash (Circle's own cash, excluding the segregated USDC-reserve assets which are a separate, 1:1-backed balance-sheet item per the 10-K) $1,526.0M (FY2025 YE). Net debt = **−$1,489.2M** (net cash). |
| Not FCF-positive for 3+ consecutive years | No | FCF positive all 3 audited fiscal years: **$138.9M (FY2023) / $326.4M (FY2024) / $529.7M (FY2025)**, each = Operating Cash Flow − Capex from the 10-K cash flow statement (OCF $139.6M/$344.6M/$542.1M; Capex $0.7M/$18.1M/$12.4M). |

**No hard disqualifier fires.**

### Weighted Quality Score

| Sub-score (weight) | Inputs | Calculation | Result |
|---|---|---|---|
| **Profitability** (25%) | Net Margin (FY2025, normalized) 12.91%; ROIC (FY2025, normalized NOPAT basis) 12.62% | NetMargin_Component = clamp((12.91/30)×100) = 43.03. ROIC_Component = clamp((12.62/30)×100) = 42.07. Avg = 42.55. No FCF-cap (FCF-positive all 3 years shown) | **42.55** |
| **Margins** (15%) | Gross Margin proxy (Revenue − Distribution/transaction/other costs, the 10-K's own income-statement structure) FY2025 39.43%, FY2024 39.31%, FY2023 49.83% | clamp((39.43/80)×100) = 49.29; **no expansion bonus** — margin is *compressing*, not expanding (49.8%→39.3%→39.4%), per the 10-K's own MD&A: distribution/transaction costs +64.4% YoY FY2025, "driven by a $438.4 million increase in distribution costs paid to Coinbase" — a structural, contractual revenue-share dynamic, not a one-off | **49.29** |
| **Growth** (20%) | Revenue 3yr CAGR — **flagged limitation**: only 2 annual growth periods available (FY2023 $1,450.5M → FY2025 $2,746.6M); Circle's audited financials don't extend before FY2023 (pre-IPO entity), so a true 4-data-point 3yr CAGR isn't computable — using the 2-year computed rate per Rule 0 rather than inventing an earlier data point = **37.61%**; documented TAM-expansion evidence (10-K: USDC in circulation **+72% YoY to $75.3B** and onchain transaction volume **+247% YoY to $11.9T**, both Q4 2025 vs Q4 2024; the GENIUS Act, federal stablecoin-specific legislation, cited in the 10-K as a named regulatory tailwind) | Base = clamp((37.61/25)×100) = clamp(150.4) = 100.0. +10 (cited TAM evidence) — already capped | **100.00** |
| **Balance Sheet** (15%) | Net Debt −$1,489.2M (net cash); Adjusted EBITDA (FY2025, company-disclosed) $582M; standard /4 denominator | Net Debt/EBITDA = −1,489.2/582 = **−2.56×**. clamp(100×(1−(−2.56)/4)) = clamp(164.0) | **100.00** |
| **Moat** (15%) | See evidence table below — 2 of 5 signals cleared the cited-evidence bar this session | (2/5)×100 | **40.00** |
| **FCF Quality** (10%) | FCF/NI (FY2025, normalized NI basis) = 529.7/354.5 = 149.4%; GAAP-basis comparatives FY2023 51.9%, FY2024 209.7% shown above for the disqualifier check | clamp(((1.494−0.40)/0.60)×100) = clamp(182.4) | **100.00** |

**Moat signal evidence (cited, per signal — operating-brief.md "never mark a signal true without a cited source"):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | 10-K (FY2025 Highlights): USDC in circulation grew **72% YoY to $75.3 billion** (Q4 2025 vs Q4 2024) — a cited, company-disclosed circulation-growth figure | **TRUE** |
| Brand premium | 10-K uses self-descriptive language ("trusted brand," "regulation-first posture") but Circle does not charge USDC holders a fee/price, so there is no documented **pricing-power** evidence (price increases without volume loss, premium vs. competitors) to cite — self-description alone doesn't clear the bar | **FALSE** |
| Network effect | 10-K explicitly documents a multi-sided-network mechanism: "Circle Payments Network (CPN) as a multi-sided network and marketplace-style application layer... expected to benefit from network effects as additional institutions, corridors, and workflow integrations are added," backed by cited circulation ($75.3B), daily transaction volume (regularly >$10B in 2025), and banking integrations in 185+ countries | **TRUE** |
| Switching costs | 10-K's **own risk factor** undercuts this signal: "Although there are complexities and costs associated with switching to a competitor, such costs **may not be significant enough to prevent a customer from switching** service providers, especially for larger customers who commonly engage more than one financial services provider at any one time." Company's own filing argues against, not for, durable switching-cost lock-in | **FALSE** |
| Scale cost advantage | No cost-per-unit or scale-driven cost data vs. smaller stablecoin issuers found this session ("economies of scale," "cost advantage" — zero hits in the 10-K) | **FALSE** |

```
Quality Score = 42.55×0.25 + 49.29×0.15 + 100.00×0.20 + 100.00×0.15 + 40.00×0.15 + 100.00×0.10
              = 10.6375 + 7.3935 + 20.00 + 15.00 + 6.00 + 10.00
              = 69.03  →  69.0 (rounded to nearest 0.1)
```

### Result: **Quality Score 69.0 — fails the 80.0+ gate**

Per [quality-scoring.md](../framework/quality-scoring.md) and [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate and no Phase 02 valuation score were computed**, and **no Composite Score exists** for CRCL.

The gate fails on a combination of factors, not one dominant cause:
1. **Moat_Score (40.0)** — only 2 of 5 signals (market-share growth, network effect) cleared the cited-evidence bar; the **switching-costs** signal is actively contradicted by Circle's own risk-factor disclosure, and **brand premium**/**scale cost advantage** had no citable evidence this session.
2. **Profitability (42.55)** — even on a normalized (one-off-excluded) basis, ROIC (~12.6%) and Net Margin (~12.9%) both sit below this framework's quality reference points, reflecting that the bulk of Circle's gross profit is paid away in distribution costs before it reaches the bottom line.
3. **Margins (49.29)**, with **no** expansion bonus — gross margin has *compressed* from 49.8% (FY2023) to ~39.3–39.4% (FY2024–FY2025), a structural, company-disclosed trend (rising Coinbase distribution-cost share, +$438.4M YoY in FY2025 alone), the opposite of the bonus condition.

Two structural facts deserve emphasis for the record, since they were the headline of this session's trigger: (a) **Circle's revenue is ~96–99% reserve interest income**, making it structurally exposed to falling short-term rates — a real macro sensitivity not captured anywhere in the Quality Score formula and worth flagging qualitatively; (b) **today's −18.1% live-price move has no company-disclosed explanation** (no 8-K filed) — the source Telegram channel's competing-stablecoin narrative is plausible but unverified, and is explicitly **not** treated as a confirmed catalyst anywhere in this session.

This is not a verdict that Circle is a bad business — revenue growth (cited TAM expansion, GENIUS Act tailwind), balance-sheet strength (net cash, no hard disqualifier), and FCF conversion are all genuinely strong once the one-off IPO charge is excluded. But the combination of a moat profile this session could only verify 2 of 5 signals for, and profitability/margin levels that sit meaningfully below this framework's deliberately strict 80.0+ bar, keeps the weighted score well short.

---

## 4. Recommendation

**PASS — do not open a position.** No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) cited, third-party evidence of Circle's distribution-cost share to Coinbase stabilizing or declining (reversing the documented margin-compression trend); (b) cited evidence clearing the switching-costs or scale-cost-advantage moat signals (e.g. a contractual lock-in mechanism, or per-unit cost data vs. smaller issuers); (c) a quarterly earnings report or guidance revision; (d) a management change or material M&A (including any resolution of the "Open USD" competitive-stablecoin development referenced in this session's trigger); (e) confirmation — via an actual 8-K or other company disclosure, not channel speculation — of what drove today's −18.1% move, should it turn out to be a Rule-9-qualifying event.
- Absent any of the above, future Telegram mentions of CRCL should be treated as routine "last checked, no change" pings rather than triggering a full re-evaluation each time.

---

## Glossary

- **8-K** — A US SEC filing companies must make within days of a major corporate event (e.g. earnings, M&A, management change) — its absence today is evidence no company-disclosed catalyst explains the price move.
- **Adjusted EBITDA** — A non-GAAP measure (Earnings Before Interest, Taxes, Depreciation & Amortization, further adjusted for one-offs) Circle itself discloses; used here only as a cross-check for the Balance Sheet sub-score's Net Debt/EBITDA ratio.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money spent buying or upgrading physical assets (servers, office buildout, etc.).
- **Composite Score** — `0.50×(100−Quality Score) + 0.50×Valuation Score` — combines quality and cheapness into one number, computed only for companies that clear the 80.0+ Quality Score gate. Not computed for CRCL (gate fails).
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **GENIUS Act** — US federal legislation establishing a regulatory framework specifically for payment stablecoins, cited in Circle's 10-K as a named industry tailwind/uncertainty.
- **Hard disqualifier** — One of three Quality Score conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company regardless of its weighted Quality Score. None fire for CRCL.
- **Invested Capital** — The total capital (debt + equity, minus cash) deployed in a business — the denominator of ROIC.
- **Liquidity event (RSU vesting)** — A vesting condition satisfied only when a company's shares become tradable (e.g. an IPO) — Circle's pre-IPO RSUs carried this condition, causing a large one-time stock-compensation expense recognized in the IPO quarter.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; negative means net cash. CRCL is at −2.56× (net cash).
- **NOPAT** — Net Operating Profit After Tax — EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **Quality Score** — A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. CRCL scores 69.0.
- **Reserve income** — Interest income Circle earns on the short-term US Treasuries/cash backing USDC in circulation — ~96–99% of Circle's total revenue, making the business highly sensitive to short-term interest rates.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **RSU** — Restricted Stock Unit — a grant of company shares to an employee that vests (becomes owned) over time and/or upon a triggering event.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **Stablecoin** — A cryptocurrency designed to maintain a stable value, typically pegged 1:1 to a fiat currency (e.g. USDC to the US dollar) and backed by reserve assets.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results; this session primarily used FY2025 annual figures (the most recently completed fiscal year) rather than a reconstructed TTM, since Q2 2025's IPO-quarter distortion makes a literal trailing-12-month window noisier than the clean FY2025-vs-FY2024 annual comparison.
- **USDC** — Circle's flagship US-dollar-pegged stablecoin, the company's primary product and reserve-income driver.

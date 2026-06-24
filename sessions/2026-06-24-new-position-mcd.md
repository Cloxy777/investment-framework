# New Position Evaluation — MCD (McDonald's Corporation)

**Task type:** NEW POSITION
**Date:** 2026-06-24
**10Y US Treasury yield:** 4.50% (2026-06-24; via WebSearch, see Section 2 data-source note)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — `t.me/tarasguk`, post #11182, ~07:26 UTC 2026-06-24, re: McDonald's loyalty program (MyMcDonald's Rewards). This is **explicitly not a Rule 9 fundamental-event trigger** — it's a marketing-program mention, not earnings/guidance/M&A/management/macro news, and the program itself is multi-year-old, not breaking. The post text is used only as the reason to look at the ticker; no information from it is used as financial data anywhere below. MCD has no prior watchlist or session history in this repo — per established precedent (FDX, CCL, CVX, WSE: first mention of an untracked name gets a full normal evaluation regardless of how thin the trigger is), this proceeds as a standard `/new-position` run.

MCD is **not** a current holding (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)).

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first, before any valuation work.

| Source | Price | Timestamp |
|---|---|---|
| **IBKR live snapshot** (primary, contract_id 9408, NYSE) | **$271.95** | 08:50:54 UTC 2026-06-24 |
| stockanalysis.com (cross-check, prior session close) | $271.66 | close 2026-06-23 |

Bid/ask at snapshot: $271.70 / $272.22. 52-week range (from the same IBKR snapshot): low $270.10 / high $339.85 — **MCD is currently trading within ~1.7% of its 52-week low.** 52-week open: $284.67.

**Live price used throughout this session: $271.95.**

---

## 2. Data Gaps Flagged / Data-Source Note

**yfinance was unavailable for this entire session.** Yahoo Finance's data endpoints (both the crumb-gated endpoints used by `.info`/`.financials`/etc., and the no-crumb chart API) returned a sustained, broad HTTP 429 (`Too Many Requests`) throughout the session — confirmed not ticker-specific (AAPL also 429'd) and not a stale-cache artifact. This is most likely shared egress-IP rate-limit pressure from concurrent sibling automation runs (TRN, CBRS) that ran immediately prior. A background poll (10+ retries over several minutes) did not see the limit clear.

**Fallback used:** live price via the IBKR MCP tool (Rule 0 — satisfied with a primary, real-time broker source, arguably stronger than yfinance for this specific purpose). All fundamental/valuation data below was sourced via WebFetch against **stockanalysis.com** (structured financial-statement and ratio tables, cited per metric) and WebSearch (10Y Treasury yield, qualitative market-share/comps context) — both are real, cited data sources, not invented or estimated figures. This mirrors the precedent set in the 2026-06-22 TRN session, where the 10Y yield was likewise sourced via WebSearch when yfinance was blocked.

No required metric below is missing or invented — every figure has a cited source. This session **does not** stop short for a data gap; it proceeds to a full Phase 01 evaluation, which (see Section 3) returns a clear, multiply-corroborated FAIL.

---

## 3. Phase 01 — Universe Screening (Quality Gate)

The framework carries two slightly different Phase 01 threshold sets — [strategy.md](../framework/strategy.md)'s (stricter) and [valuation-scoring.md](../framework/valuation-scoring.md)'s "Quantitative Pre-Screen Filters" (looser on most lines). Both are shown below for completeness; MCD fails decisively under **either** version.

| Criterion | strategy.md threshold | valuation-scoring.md threshold | MCD actual | Result |
|---|---|---|---|---|
| Net margin | >15% | >12% | 31.85% (FY25) / 31.73% (FY24) / 33.22% (FY23) | PASS (both) |
| ROIC | >15% | >15% | 17.98% (FY25) / 17.94% (FY24) / 19.09% (FY23) / 15.70% (FY22) / 17.42% (FY21) — sustained 5yr | PASS (both) |
| FCF positive | 3+ yrs | 3 consecutive yrs | $7,186M(25) / $6,672M(24) / $7,255M(23) / $5,488M(22) | PASS (both) |
| Gross margin | >40% OR structurally expanding | >40% | 57.41%(25) / 56.75%(24) / 57.12%(23) / 56.97%(22) — flat, not clearly expanding, but comfortably clears the >40% bar either way | PASS (both, via the >40% leg) |
| **Revenue growth** | **CAGR >10%** | **CAGR >8% (3yr)** | **3yr CAGR (FY22→FY25) = 5.06%** | **FAIL (both)** |
| **Net debt/EBITDA** | **<2x** | **<2.5x** | **3.70x(25) / 3.68x(24) / 3.56x(23) / 4.10x(22) / 3.65x(21) — persistent 5yr, never close to either threshold** | **FAIL (both)** |
| FCF/NI conversion | >70% for 2+ yrs | (same check, implicit in "FCF positive 3yr") | 83.92%(25) / 81.13%(24) / 85.67%(23) | PASS (both) |
| FCF yield | (not separately gated) | **>4%** | 3.31%(25) / 3.22%(24) / 3.39%(23) / 2.85%(22) / 3.56%(21) | **FAIL (valuation-scoring.md leg)** |
| EV/EBIT | (not separately gated) | **<20x** | 21.89x (FY25 basis) / 19.55x (current/live basis) | Borderline — fails on FY25 basis, marginal pass on live basis |
| Moat signal | stable/growing share, brand, network effect | (qualitative, same) | US comps +3.8% (Q1 2026), systemwide sales +11% YoY, ~44,000 units, dominant US franchise brand. Lost the *global unit-count* crown to Mixue (China-centric, low-cost tea/ice-cream model — not a like-for-like competitive threat to MCD's Western QSR economics) | PASS (both) |
| Dilutive issuance pattern | none | none | Negative shareholders' equity from sustained debt-funded buybacks (D/E ratio −8x to −30x over 5yrs) — a long-standing, well-known structural feature of MCD's capital structure, not a distress signal or a dilution pattern. No new-share dilution observed. | PASS (both) — flagged for context |

### Result: **Phase 01 FAIL**

MCD fails on **two independent, structural criteria** under both threshold sets carried in this framework:

1. **Revenue growth.** 3-year revenue CAGR of **5.06%** (FY2022 $23,183M → FY2025 $26,885M) is roughly half the *looser* of the two thresholds (>8%) and barely half the stricter one (>10%). This is consistent with MCD's well-understood profile as a mature, low-single-to-mid-single-digit-growth franchise business — not a flaw unique to this period, but a structural mismatch with this framework's growth-gate design, which is built around quality-*and-growth* compounders rather than mature slow-growers.

2. **Balance-sheet leverage.** Net debt/EBITDA has sat in a **3.56x–4.10x band every year for the last 5 years** — not a one-off spike, but the steady-state result of MCD's long-running debt-funded buyback program (also visible in the deeply negative shareholders'-equity / debt-to-equity figures). This persistently and decisively fails both the strategy.md (<2x) and valuation-scoring.md (<2.5x) leverage gates. Note: Hybrid Upgrade 5 (Debt Gate) only relaxes this threshold to <4x for asset-light **payment networks and financials** with very high interest coverage and investment-grade ratings — MCD is a restaurant franchisor, not a payments/financial business, so it does not qualify for that exception, and even the relaxed 4x threshold is breached in 2 of the last 5 years (FY22: 4.10x) and right at the edge in FY25 (3.70x).

A third metric — **FCF yield** (2.85%–3.56% across 5 years, vs. valuation-scoring.md's >4% pre-screen line) — also fails, though only under the looser threshold set (strategy.md doesn't carry a separate FCF-yield pre-screen).

Per [new-position.md](../.claude/commands/new-position.md) step 2 and [operating-brief.md](../framework/operating-brief.md): **"if it fails, stop and report why rather than proceeding to scoring."** Accordingly, **no Rate Environment Gate and no Phase 02 valuation score were computed** — that would be black-box theater on top of a name that already doesn't clear the quality gate this framework uses to decide what's even eligible for valuation-driven entry.

This is not a comment on McDonald's as a business in any absolute sense (it is a highly profitable, durable, well-moated franchise — strong margins, strong and sustained ROIC, strong FCF/NI conversion) — it simply does not fit the specific growth-plus-balance-sheet profile this framework's Phase 01 gate is built to select for. A structurally levered, mature single-digit grower is a different investment case (closer to a bond-proxy/income compounder) than what this framework's scoring engine (FCF Yield 40%, EV/EBIT 25%, Forward PE 20%, PEG/EV-EBIT 15%) and trim/exit logic are calibrated around.

---

## 4. Recommendation

**PASS.** Do not open a position. No order setup, no fair-value derivation, no position sizing — none of that work is meaningful for a name that fails the quality gate this framework uses to define its investable universe.

This is a **structural, multi-year** Phase 01 failure (revenue growth and leverage have both sat outside threshold for at least 5 straight fiscal years), not a transient one-quarter miss — so it is unlikely to flip on the next earnings print alone. A future re-screen would be warranted only if there's a fundamental shift in either driver (e.g. a sustained re-acceleration of unit growth/comps pushing 3yr revenue CAGR materially above 8-10%, or a deliberate, multi-year deleveraging program bringing net debt/EBITDA under ~2.5x) — see Section 6.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — Phase 01 FAILs are not put on a recurring re-check cadence by default (see [watchlist/README.md](../watchlist/README.md): "Phase 01 FAIL / not scored" entries don't carry a numeric score to go stale).
- **Rule 9 fundamental trigger** that would warrant a fresh look regardless of schedule: quarterly earnings showing a *sustained* acceleration in comparable sales / unit growth (3yr revenue CAGR climbing materially above the 8-10% gate), or an announced, credible multi-year deleveraging plan bringing net debt/EBITDA toward the 2.5x area. Absent either, future Telegram mentions of MCD should be treated as routine "last checked, no change" pings rather than triggering a full re-evaluation each time, unless they themselves carry new fundamental information.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and valuation ratios.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to operating profit, independent of capital structure.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Forward PE** — Price ÷ next twelve months' expected earnings per share.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **NI (Net Income)** — accounting profit after all expenses, interest, and taxes ("the bottom line").
- **Phase 01–06** — the six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Qualified Quality List** — the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (MCD does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **Treasury yield (10Y)** — the interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.

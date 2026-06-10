# New Position Evaluation — CoreWeave (CRWV)

**Date:** 2026-06-09 (session run 2026-06-10)
**Task type:** NEW POSITION
**10Y US Treasury yield:** 4.54%

---

## Rule 0 — Live Price Verification

| Field | Value | Source |
|---|---|---|
| Live price | **$105.75** | CNBC / Yahoo Finance / search, 2026-06-10 |
| Prior session range | $98.40 – $104.30 | 2026-06-09 |
| 52-week high | $187.00 | — |
| 52-week low | $63.80 | — |
| Decline from 52-week high | −43.4% | |
| Market capitalisation | $55.85B | — |
| Analyst consensus 12-mo PT | $132.68 (+29.6%) | 25 analysts, avg "Buy" |

---

## Business Overview (Context)

CoreWeave is a "neocloud" — a GPU-specialized cloud infrastructure provider for AI training and inference workloads. It rents data-center capacity built around NVIDIA GPUs to hyperscalers, AI labs, and enterprises (Microsoft, Meta, OpenAI, Nvidia itself as both investor and supplier). IPO'd 2025. Revenue is growing extremely fast off a small base, financed by an extraordinary amount of debt secured against the GPU fleet and customer contracts.

---

## Phase 01 — Quality Gate Walkthrough

| # | Metric | Threshold | Actual | Pass? | Source / Calculation |
|---|---|---|---|---|---|
| 1 | Gross margin | >40% | **Not separately disclosed; GAAP gross margin likely materially below 40%** given D&A on the GPU fleet sits in COGS | ❌ / Data gap | Adjusted EBITDA margin 56% (Q1 2026) excludes D&A and SBC — not comparable to gross margin. GAAP operating income was just $21M (1% margin) on $2.08B revenue, implying COGS + opex consume ~99% of revenue once D&A is included |
| 2 | Net margin | >12% | **−35.6%** (Q1 2026: −$740M / $2.08B) <br> **−23.4%** (FY2025: −$1.2B / $5.131B) | ❌ FAIL | [CNBC Q1 2026 earnings](https://www.cnbc.com/2026/05/07/coreweave-crwv-q1-earnings-report-2026.html) |
| 3 | ROIC | >15% | **Negative** — operating income near breakeven ($21M Q1 2026) against ~$25B+ invested capital (debt + equity) | ❌ FAIL | Derived from Q1 2026 results + balance sheet |
| 4 | Revenue growth (3yr CAGR proxy) | >8% | **+167.9%** FY2025 YoY; **+112%** Q1 2026 YoY | ✅ PASS | [Q1 2026 results](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-First-Quarter-2026-Results/) |
| 5 | FCF positive, 3 consecutive years | FCF > 0 ×3yrs | **−$7.3B** FY2025 (capex $14.9B vs revenue $5.1B) | ❌ FAIL | Multiple sources (StockAnalysis, TS2) |
| 6 | Net Debt/EBITDA | <2.5× (or <4× under Upgrade 5 if asset-light + IG-rated + interest coverage >15×) | **~4.7×** even on generous *adjusted* EBITDA basis: Net debt ≈ $25B debt − $3.1B cash ≈ $21.9B; run-rate adj. EBITDA ≈ $1.157B × 4 = $4.6B → 21.9/4.6 = 4.7×. On GAAP EBITDA (which includes the massive D&A burden) the ratio is far worse | ❌ FAIL | Derived; debt-to-equity already 640.9% per Simply Wall St |
| 7 | FCF/NI conversion >70% (2+ yrs) | >70% | **N/A** — both FCF and NI are deeply negative | ❌ FAIL | — |
| 8 | Moat Signal (market share, brand, network effect, switching costs) | Stable/growing moat | **Unproven / contested.** $99.4B revenue backlog and 3.5GW contracted power show real demand, but CoreWeave competes against AWS/Azure/GCP (vastly larger balance sheets building their own AI capacity) and other neoclouds (Lambda, Crusoe). Historical customer concentration (Microsoft was >60% of revenue in 2023-24) is a structural risk. Switching costs exist at the contract level (backlog) but this is closer to a capital-intensive leasing/financing business than a durable consumer/network moat | ⚠️ Weak / contested | Qualitative |

**Result: 1 of 8 criteria pass (revenue growth). 6 of 8 fail outright. Gross margin is a data gap but almost certainly also fails given the economics shown.**

---

## Upgrade 4 (Turnaround / Fallen Angel Sub-Gate) — Does It Apply?

Checked because CRWV fails multiple Phase 01 criteria — Upgrade 4 allows a **Conditional Watch (2-3% max)** entry IF all 5 conditions are met:

| Condition | Met? |
|---|---|
| 1. ROIC historically >15% for ≥5 years in past decade | ❌ **No** — CoreWeave has no such history; founded as a crypto-mining operation (~2017), pivoted to GPU cloud ~2019, IPO'd 2025. There is no decade of operating history, let alone 5 years of >15% ROIC |
| 2. CEO/CFO insider buying >$500K in past 6 months | Not checked — moot, condition 1 already fails |
| 3. Independent FV estimate showing ≥40% MOS | Not checked — moot |
| 4. Net Debt/EBITDA <3× | ❌ **No** — ~4.7× even on adjusted EBITDA |
| 5. Core moat still identifiable | ⚠️ Contested (see above) |

**Upgrade 4 does not apply.** This is not a "fallen angel" with a proven quality history that has temporarily stumbled — it is a young, hyper-capital-intensive infrastructure buildout in its loss-making growth phase. The framework's Turnaround Sub-Gate is designed for companies like the GE/Nokia/IBM graveyard-audit cases that *used to* meet quality criteria; CRWV has never met them.

---

## Phase 01 Verdict: **FAIL — STOP HERE**

Per the operating brief: *"Walk the Phase 01 quality gate — if it fails, stop and report why rather than proceeding to scoring."* CRWV fails on **net margin, ROIC, FCF positivity, Net Debt/EBITDA, and FCF/NI conversion** — five of the framework's eight non-negotiable quality criteria, several by an enormous margin (net debt/EBITDA ~4.7× vs a 2.5× standard threshold; FCF −$7.3B vs required positive). No Phase 02 valuation score is calculated, per framework rules — a cheap price on a business this far from the quality bar is not a "Cheap" signal, it's irrelevant.

**This is fundamentally a different asset class than this framework screens for.** CoreWeave is a leveraged, capital-intensive bet on AI infrastructure demand outpacing both (a) hyperscaler self-build and (b) the depreciation/obsolescence curve of the underlying GPUs financing the debt. That may be a reasonable speculative thesis for some investors, but it is the opposite of "Quality Value + Dynamic Trimming" — there is no margin of safety framework that applies to a company burning $7B+ FCF/year against a $22B net debt position with no profitability track record.

---

## Recommendation

**PASS — Does not meet Phase 01 quality gate. No further action.**

Not added to watchlist under the standard framework. If revisited at all, it would require a structural change in the business (see triggers below) — this is not a "wait for a better price" situation, since price is irrelevant when the underlying economics fail this many gates simultaneously.

---

## Re-evaluation Triggers (Hypothetical — Long Horizon)

For completeness, what *would* need to change for CRWV to even be a Phase 01 candidate:

| Trigger | Why it matters |
|---|---|
| 2+ consecutive years of positive FCF | Currently −$7.3B/yr; would require capex to fall dramatically below operating cash flow — likely multi-year, post-hypergrowth phase (if ever) |
| Net Debt/EBITDA below 2.5× (or <4× if a credible asset-light/IG case can be made) | Currently ~4.7× and rising (2026 capex guidance $31-35B funded substantially by debt) |
| GAAP net margin turning positive and durable | Currently −23% to −36% |
| Demonstrated moat resilience vs hyperscaler self-build | Multi-year question — would need evidence CoreWeave retains pricing power once AWS/Azure/GCP AI capacity fully ramps |

None of these are likely inside a 2-3 year horizon given the FY2026 capex guidance of $31-35B (up from $30-35B) was *increased* at the same time revenue guidance was merely maintained — the capital intensity is going the wrong direction for this framework, not the right one.

---

## Sources

- [CoreWeave (CRWV) Stock Price — CNBC](https://www.cnbc.com/quotes/CRWV)
- [CoreWeave Reports Strong First Quarter 2026 Results — Investor Relations](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-First-Quarter-2026-Results/)
- [CoreWeave (CRWV) Q1 earnings report 2026 — CNBC](https://www.cnbc.com/2026/05/07/coreweave-crwv-q1-earnings-report-2026.html)
- [CoreWeave Stock at Risk Amid Insider Selling, Depreciation, Soaring Debt — BanklessTimes](https://www.banklesstimes.com/articles/2026/06/09/coreweave-stock-at-risk-amid-insider-selling-depreciation-soaring-debt/)
- [CoreWeave (CRWV) Balance Sheet & Financial Health — Simply Wall St](https://simplywall.st/stocks/us/software/nasdaq-crwv/coreweave/health)
- [CoreWeave (CRWV) Stock Today: Debt, AI Cloud Growth — TS2](https://ts2.tech/en/coreweave-crwv-stock-today-debt-ai-cloud-growth-and-what-the-2-25-billion-convertible-notes-mean-for-2026/)
- [CoreWeave Closes $8.5B GPU-Backed Financing Facility — Investor Relations](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-Landmark-8-5-Billion-Financing-Facility-Achieving-First-Investment-Grade-Rated-GPU-backed-Financing/default.aspx)

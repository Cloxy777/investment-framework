# New Position Evaluation — NOK (Nokia Corporation, ADR)

**Task type:** NEW POSITION
**Date:** 2026-06-24
**10Y US Treasury yield:** 4.406% (2026-06-24; via yfinance `^TNX`)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — `t.me/FinnInvestChannel`, post #2825, 2026-06-24T15:22:03+00:00, re: "Nokia робить ще один крок у AI-мережі" ("Nokia takes another step in AI networking") — Nokia expanding autonomous-network capabilities via a partnership with AWS (Autonomous Network Fabric in the cloud) and Databricks (a telecom data platform feeding AI agents). This is **explicitly not a Rule 9 fundamental-event trigger** — it's a product/partnership announcement, not earnings/guidance/M&A/management-change/macro-shift, consistent with this repo's established precedent for ruling commercial/product announcements non-Rule-9 (e.g. the MCD loyalty-program mention, and the MSFT/Chevron 20-year-deal ruling on 2026-06-22). The post text is used only as the reason to look at the ticker; no information from it is used as financial data anywhere below. NOK has no prior watchlist or session history in this repo — per established precedent (FDX, CCL, CVX, MCD: first mention of an untracked name gets a full normal evaluation regardless of how thin the trigger is), this proceeds as a standard `/new-position` run.

NOK is **not** a current holding (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)).

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first, before any valuation work.

| Source | Price | Timestamp |
|---|---|---|
| **IBKR live snapshot** (primary, contract_id 661513, NYSE, "NOKIA CORP-SPON ADR") | **$13.90** | 2026-06-24 (snapshot ts 1782319666) |
| yfinance `currentPrice`/`regularMarketPrice` (cross-check) | $13.895 | same session |

Bid/ask at snapshot: $13.90 / $13.91. Change on day: +$0.20 (+1.46%). 52-week range (from the same IBKR snapshot's `misc_statistics`): low **$3.94** / high **$17.45** — NOK is currently trading well off both extremes, roughly 253% above its 52-week low and ~20% below its 52-week high. 52-week open: $5.09 (i.e. NOK is up roughly 173% from where it started the trailing 52-week window).

**Live price used throughout this session: $13.90.**

**Currency note:** Nokia Oyj is Finland-domiciled and reports its financial statements in EUR. Its NYSE-listed ADR (NOK) is a sponsored American Depositary Receipt. Per the prompt's instruction not to assume a 1:1 ratio, this was checked rather than assumed: yfinance's `currentPrice` ($13.895) matches the IBKR live USD quote ($13.90) to within a cent, and back-solving the implied EUR/USD rate from yfinance's USD-converted `info` fields against the EUR-denominated annual financials (e.g. TTM EBITDA $2,537M USD ÷ FY2025 EBITDA €2,253M = 1.126, a plausible spot EUR/USD rate) confirms NOK is a **1-for-1** ADR with no ratio adjustment needed — see the new ADR glossary entry. All fundamentals below are sourced from yfinance's EUR-denominated annual statements (`t.financials`, `t.cashflow`, `t.balance_sheet`) since those are the audited filing-currency figures; market-cap/EV/price-derived figures use yfinance's own USD conversion, cross-checked for consistency as shown above. No figures are mixed across currencies without conversion.

---

## 2. Data Gaps Flagged / Data-Source Note

yfinance worked normally this session once `YF_DISABLE_CURL_CFFI=1` and `CURL_CA_BUNDLE=/root/.ccr/ca-bundle.crt` were set (no 429s encountered) — no fallback to WebFetch/WebSearch was needed for fundamentals. The 10Y Treasury yield was sourced via yfinance `^TNX` (4.406%, 2026-06-24 close).

**One genuine data-depth limit, noted but not a blocker:** yfinance's free-tier annual financials for NOK return only 4 fiscal years (FY2022–FY2025); FY2021 is `NaN` across the income statement, cash flow, and balance sheet. This means the 3-year revenue CAGR (FY2022→FY2025) and the 4-year (not 5-year) ROIC/margin/leverage trend below are computed on the data that does exist — not estimated to fill the FY2021 gap. This does not block Phase 01 (which only requires 3+ years of history for its growth/FCF checks) and, as shown below, the available 4 years already produce a decisive, multi-year-consistent FAIL — an FY2021 data point would not plausibly reverse a structural multi-year shrinkage/low-ROIC pattern. No required Phase 01 metric is missing; all figures below are cited to yfinance's structured statement data, not invented or estimated.

---

## 3. Phase 01 — Universe Screening (Quality Gate)

The framework carries two slightly different Phase 01 threshold sets — [strategy.md](../framework/strategy.md)'s (stricter) and [valuation-scoring.md](../framework/valuation-scoring.md)'s "Quantitative Pre-Screen Filters" (looser on most lines). Both are shown below for completeness; NOK fails decisively under **either** version.

All financial figures sourced from yfinance `t.financials` / `t.cashflow` / `t.balance_sheet` (EUR millions, Nokia's reporting currency), fiscal years ending 31 Dec.

| Criterion | strategy.md threshold | valuation-scoring.md threshold | NOK actual | Result |
|---|---|---|---|---|
| **Net margin** | **>15%** | **>12%** | **3.27%(FY25) / 6.64%(FY24) / 3.15%(FY23) / 17.89%(FY22)** — FY2022's figure is itself a one-off: Tax Provision was **−€2,033M** (a tax *benefit*, not expense) against Pretax Income of only €2,169M, i.e. a one-time tax-driven inflation, not an operating result. Excluding that distortion, net margin has run 3–7% for 3 of the last 4 years. | **FAIL (both)** |
| **ROIC** | **>15%** | **>15%** | **3.24%(FY25) / 8.06%(FY24) / 5.90%(FY23) / 7.40%(FY22)** — NOPAT = EBIT×(1−tax rate), Invested Capital from balance sheet. Never within shouting distance of 15% in any of the 4 available years. | **FAIL (both)** |
| FCF positive | 3+ yrs | 3 consecutive yrs | €1,465M(25) / €2,021M(24) / €665M(23) / €873M(22) — positive all 4 years | PASS (both) |
| Gross margin | >40% OR structurally expanding | >40% | 43.54%(25) / 46.12%(24) / 40.43%(23) / 42.51%(22) — clears >40% every year, though flat/noisy, not a clear expansion trend | PASS (both, via the >40% leg) |
| **Revenue growth** | **CAGR >10%** | **CAGR >8% (3yr)** | **3yr CAGR (FY22→FY25) = −5.76%** — revenue has *shrunk* every year: €23,761M(22) → €21,138M(23) → €19,220M(24) → €19,889M(25) | **FAIL (both, and the wrong sign)** |
| Net debt/EBITDA | <2x | <2.5x | **Net cash position all 4 years** — Net Debt/EBITDA of −0.47×(25) / −0.55×(24) / −0.36×(23) / +0.01×(22) (total debt €4,413–5,519M consistently exceeded by cash €5,462–6,623M) | PASS (both) — comfortably, balance sheet is a clear strength |
| FCF/NI conversion | >70% for 2+ yrs | (same check, implicit in "FCF positive 3yr") | 225%(25) / 158%(24) / 100%(23) / 21%(22) — passes on a conversion-ratio basis, though the >100% readings in FY24/25 reflect NOK's depressed Net Income denominator (FCF exceeding NI) rather than unusually strong cash generation; FY2022's 21% is the inverse distortion from that year's tax-driven NI spike | PASS (both), but on a denominator distorted by the same FY2022 one-off and currently-thin earnings base — not a clean read |
| FCF yield | (not separately gated) | **>4%** | TTM FCF $1,597M USD ÷ market cap $77,547M USD (yfinance) = **2.06%** | **FAIL (valuation-scoring.md leg)** |
| EV/EBIT | (not separately gated) | **<20x** | EV $74,207M USD ÷ FY2025 EBIT (€1,134M × ~1.126 FX ≈ $1,277M) = **~58×** (yfinance's own `enterpriseToEbitda` of 29.25× on the less-punishing EBITDA base is itself already 46% over the 20× line) | **FAIL decisively (valuation-scoring.md leg)** |
| Moat signal | stable/growing share, brand, network effect | (qualitative, same) | Nokia holds a real, durable position in telecom network infrastructure (RAN, optical, IP routing) and is a credited 5G/6G standard-essential-patent holder — a genuine but *narrow, commoditizing* moat in a structurally low-growth, two-to-three-player (Nokia/Ericsson/Huawei-ex-West) market, not a widening one on the revenue evidence above | Mixed/qualitative — does not offset the quantitative failures |
| Dilutive issuance pattern | none | none | Shares outstanding roughly flat (~5.58B); no recent dilutive equity raise identified in the data pulled | PASS (both) |

### Result: **Phase 01 FAIL**

NOK fails on **multiple independent, structural criteria** under both threshold sets carried in this framework:

1. **Net margin and ROIC — the core profitability gate.** Net margin has run 3.15–6.64% in 3 of the last 4 fiscal years (the lone exception, FY2022's 17.89%, is itself an artifact of a one-off €2,033M tax benefit against pretax income of only €2,169M — not a repeatable operating result). ROIC has never exceeded 8.06% in any of the 4 years with available data, against a >15% bar. Both metrics fail by a wide margin, consistently, across the whole lookback window — this is not a single bad quarter.

2. **Revenue growth — and it's not just "too slow," it's negative.** Unlike MCD's prior session (a mature *slow grower*, +5.06% 3yr CAGR), NOK's 3-year revenue CAGR is **−5.76%** — Nokia's top line has shrunk in 3 of the last 4 years (€23.76B → €21.14B → €19.22B → €19.89B). This fails the growth gate in the opposite direction from a "doesn't grow fast enough" case: this is a business whose revenue is currently contracting.

3. **Valuation multiples are stretched on a depressed earnings base.** EV/EBIT of roughly 29–58× (depending on EBIT vs EBITDA denominator) and FCF yield of ~2.1% both fail the valuation-scoring.md pre-screen by a wide margin — the market is pricing in a meaningful AI/networking-driven earnings recovery (consistent with the AWS/Databricks partnership that triggered this look) that has not yet shown up in trailing fundamentals.

The one genuine bright spot is the **balance sheet** — NOK sits in a comfortable net-cash position (Net Debt/EBITDA consistently negative), a real and structural strength, not a one-off. But Phase 01 is conjunctive (all criteria must pass), and a strong balance sheet does not offset failing profitability, ROIC, and growth simultaneously.

Per [new-position.md](../.claude/commands/new-position.md) step 2 and [operating-brief.md](../framework/operating-brief.md): **"if it fails, stop and report why rather than proceeding to scoring."** Accordingly, **no Rate Environment Gate and no Phase 02 valuation score were computed.**

This is not a verdict on Nokia's AI-networking pivot in any forward-looking sense — the AWS Autonomous Network Fabric and Databricks telecom-data-platform partnerships cited in the triggering Telegram post may well represent a genuine, even significant, strategic catalyst. But this framework scores **trailing, filed financials** at the Phase 01 gate, deliberately before any narrative or forward story is allowed to influence the assessment (Rule 0 / "never invent or estimate," and the Upside/Downside Modifier in valuation-scoring.md is explicitly a *Phase 02* tool that never even gets reached here). On the numbers that exist today, Nokia is a low-margin, low-ROIC, currently-shrinking hardware/network-equipment business — a turnaround/recovery story, not a quality compounder by this framework's Phase 01 definition.

---

## 4. Recommendation

**PASS.** Do not open a position. No order setup, no fair-value derivation, no position sizing — none of that work is meaningful for a name that fails the quality gate this framework uses to define its investable universe, and doing it anyway would be exactly the "black-box theater" the MCD precedent explicitly declined to produce.

**Worth flagging for context (not a basis for any action):** Hybrid Upgrade 4 (Turnaround Sub-Gate) exists in this framework for exactly this profile — a previously-stumbling business with an identifiable moat — but it requires **all five** of: (1) historical ROIC >15% for ≥5 of the past 10 years (data unavailable for years beyond FY2022 and the available 4 years never clear 15% regardless), (2) verified CEO/CFO insider buying >$500K in the past 6 months (not checked — moot given condition 1 already fails), (3) an independent FV estimate showing ≥40% margin of safety (not computed — Phase 01 FAIL means no FV work was done), (4) Net Debt/EBITDA <3× (NOK passes this one easily), (5) a still-identifiable core moat (arguably yes, per the qualitative note above). Condition 1 alone is enough to disqualify the Turnaround path without needing to check the rest — this is not flagged as "almost qualifying," just as the reason a deliberate sub-gate review wasn't required to reach today's PASS.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — Phase 01 FAILs are not put on a recurring re-check cadence by default (see [watchlist/README.md](../watchlist/README.md): "Phase 01 FAIL / not scored" entries don't carry a numeric score to go stale).
- **Rule 9 fundamental trigger** that would warrant a fresh look regardless of schedule: a quarterly earnings print showing a *sustained* return to revenue growth (3yr CAGR turning durably positive, ideally toward the 8–10% gate) accompanied by margin/ROIC recovery — plausible if the AI-networking/AWS-Databricks partnership and similar deals materially convert into delivered revenue and margin, rather than remaining product announcements. A material M&A move or management change would also qualify under Rule 9 independent of the financials. Absent one of these, future Telegram mentions of NOK (including further AI-network partnership news) should be treated as routine "last checked, no change" pings rather than triggering a full re-evaluation each time, consistent with the MCD precedent.

---

## Glossary

- **ADR (American Depositary Receipt)** — a US-exchange-listed security representing shares of a non-US company, letting US investors trade it in USD without a foreign exchange; confirmed 1-for-1 for NOK by cross-checking the live USD quote against EUR-denominated financials converted at the prevailing FX rate.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and valuation ratios.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to operating profit, independent of capital structure.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **NI (Net Income)** — accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — operating profit after a tax adjustment but before financing costs; the numerator this framework uses to compute ROIC.
- **Phase 01–06** — the six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Qualified Quality List** — the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (NOK does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **Treasury yield (10Y)** — the interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **Turnaround Sub-Gate** — the conditional path (Hybrid Upgrade 4) that lets a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests (historical ROIC, insider buying, margin of safety, debt level, identifiable moat).
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.

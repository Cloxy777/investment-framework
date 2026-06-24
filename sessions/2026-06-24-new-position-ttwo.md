# New Position Evaluation — TTWO (Take-Two Interactive Software, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-06-24
**10Y US Treasury yield:** 4.408% (2026-06-24 close; via yfinance `^TNX`)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — `t.me/myroslavkorol`, post #2479, ~10:51:52 UTC 2026-06-24: *"Ну і до дійсно важливого: Попередні замовлення на Grand Theft Auto VI офіційно розпочнуться ЗАВТРА (25 червня) в цифрових магазинах... Акції $TTWO +12% з моменту цього оголошення і продовжують зростати."* ("...pre-orders for Grand Theft Auto VI officially open TOMORROW (25 June) in digital stores... $TTWO stock +12% since this announcement and continuing to rise.")

**Correction note (audit trail):** This evaluation is a catch-up correction. A prior hourly run of this same routine, already committed to git as **PR #90**, processed this exact post and logged it as *"no resolvable company named"* — that characterization was incorrect. The post explicitly names the ticker **$TTWO**. This session runs the full standard evaluation that should have been triggered at the time, per this repo's established precedent (FDX, CCL, CVX, MCD, PLTR, NOK — first mention of an untracked ticker gets a full normal `/new-position` evaluation regardless of how thin or non-fundamental the triggering post's claim is). The post's "+12%" price-move claim is **not** used as financial data anywhere below — it is only the reason this ticker is being looked at; Section 1 fetches an independent, live price.

TTWO has no prior watchlist or session history in this repo (confirmed: absent from [portfolio/holdings.md](../portfolio/holdings.md) and no file under `watchlist/*/TTWO/`). TTWO is **not** a current holding.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first, before any valuation work.

| Source | Price | Timestamp |
|---|---|---|
| **IBKR live snapshot** (primary, contract_id 6478131, NASDAQ, "TAKE-TWO INTERACTIVE SOFTWRE") | **$237.04** | snapshot ts 1782320068 (2026-06-24) |
| yfinance `fast_info`/`currentPrice` (cross-check) | $236.96 | same session |

Bid/ask at snapshot: $236.90 / $237.08. Change on day: **−$5.60 (−2.31%)**. 52-week range (IBKR `misc_statistics`): low **$187.63** / high **$264.79** (13-week high $251.24, 26-week high $260.04). 52-week open: $242.37. TTWO is currently trading roughly 26% above its 52-week low and about 10% below its 52-week high — i.e. **down on the day this evaluation runs**, which sits at odds with the triggering post's "+12% and continuing to rise" framing. No attempt is made to reconcile or explain that gap — the post's price claim is not used as data; this is simply the live, independently-sourced price as of this session.

**Live price used throughout this session: $237.04.**

Contract resolution note: `search_contracts("TTWO")` returned two rows — the NASDAQ primary listing (contract_id 6478131, used throughout) and a Mexican Stock Exchange (MEXI) secondary listing (contract_id 398601615). Both rows describe the same underlying company ("TAKE-TWO INTERACTIVE SOFTWRE") — this is a single company cross-listed on two exchanges, not two different companies sharing a ticker (unlike the TRN ambiguity precedent), so no WebSearch disambiguation was needed. The NASDAQ listing was used as the primary reference per convention.

---

## 2. Data Gaps Flagged / Data-Source Note

yfinance worked normally this session with `YF_DISABLE_CURL_CFFI=1` and `CURL_CA_BUNDLE=/root/.ccr/ca-bundle.crt` set (no 429s; a benign "curl_cffi not available, falling back to requests" notice printed but did not block any call). All fundamentals below are sourced from `t.financials`, `t.cashflow`, and `t.balance_sheet` (4 fiscal years, FY2023–FY2026, fiscal year ending **March 31**) plus `t.info`/`fast_info` for live-price-derived multiples.

**One data-depth limit, noted but not a blocker:** yfinance's free-tier annual statements return only 4 fiscal years for TTWO (FY2023–FY2026); FY2022 is `NaN` across the income statement, cash flow, and balance sheet. This satisfies Phase 01's "3+ years" / "3 consecutive years" requirements but means the 3-year revenue CAGR below is computed FY2023→FY2026 (the full available window), not a different 3-year slice. No required Phase 01 metric is missing or invented — every figure below is cited to yfinance's structured statement data.

**Qualitative context (WebSearch, narrative only, not used as scored data):** TTWO's FY2025 GAAP net loss of $4.48B included a one-time, non-cash **$3.545B goodwill impairment** tied to the Zynga acquisition, itself triggered by GTA VI's well-publicized release delay. FY2026 narrowed to a $298.2M net loss (still negative) on net revenue of $6.656B (+18% YoY) and EBITDA of $760.6M (per company reporting; yfinance's own FY2026 EBITDA figure of $1,241.5M differs somewhat from the company's reported $760.6M — likely a different EBITDA construction/adjustment basis; the *scored* figures below use yfinance's structured statement data consistently across all 4 years for comparability, not the company's own adjusted-EBITDA framing). Take-Two has guided to FY2027 (the fiscal year that will include GTA VI's confirmed November 19, 2026 launch) as its first GAAP-profitable year in recent history. This is forward guidance — explicitly excluded from this framework's scored inputs (see "Why Forward Guidance Is Not a Sub-score" in [valuation-scoring.md](../framework/valuation-scoring.md)) — and is noted here only as narrative context for why the trailing financials look the way they do, not as a basis for any adjustment to the Phase 01 result below.

Sources: [Take-Two FY2026 8-K / guidance](https://www.stocktitan.net/sec-filings/TTWO/8-k-take-two-interactive-software-inc-reports-material-event-fed2dc7b6f1d.html), [Monexa — FY2025 $4.48B loss / $3.545B impairment](https://www.monexa.ai/blog/take-two-ttwo-4-48b-loss-a-3-55b-impairment-and-th-TTWO-2025-09-08), [Take-Two 10-K GTA VI risk disclosure](https://www.stocktitan.net/sec-filings/TTWO/10-k-take-two-interactive-software-inc-files-annual-report-cd41fd29443b.html).

---

## 3. Phase 01 — Universe Screening (Quality Gate)

The framework carries two slightly different Phase 01 threshold sets — [strategy.md](../framework/strategy.md)'s (stricter) and [valuation-scoring.md](../framework/valuation-scoring.md)'s "Quantitative Pre-Screen Filters" (looser on most lines). Both are shown below for completeness; TTWO fails decisively under **either** version.

All financial figures sourced from yfinance `t.financials` / `t.cashflow` / `t.balance_sheet`, fiscal years ending March 31 (FY2023 = year ended 2023-03-31, … FY2026 = year ended 2026-03-31).

| Criterion | strategy.md threshold | valuation-scoring.md threshold | TTWO actual | Result |
|---|---|---|---|---|
| **Net margin** | **>15%** | **>12%** | **−4.48%(FY26) / −79.50%(FY25) / −69.99%(FY24) / −21.02%(FY23)** — negative every single available fiscal year | **FAIL (both)** |
| **ROIC** | **>15%** | **>15%** | **−1.12%(FY26) / −89.88%(FY25) / −42.64%(FY24) / −8.58%(FY23)** — NOPAT = EBIT×(1−effective tax rate), Invested Capital = Total Debt + Equity − Cash. Negative every available year; never within any shouting distance of 15% | **FAIL (both)** |
| **FCF positive (3+ yrs)** | **3+ yrs** | **3 consecutive yrs** | **+$461.5M(FY26) / −$214.6M(FY25) / −$157.8M(FY24) / −$203.1M(FY23)** — negative FCF in 3 of the 4 available years, including the most recent 3 consecutive years before FY26 | **FAIL (both)** |
| Gross margin | >40% OR structurally expanding | >40% | 57.23%(FY26) / 54.36%(FY25) / 41.91%(FY24) / 42.72%(FY23) — clears >40% every year and has genuinely expanded (43%→57% over 4yrs, likely mix-shift toward higher-margin recurring/mobile revenue) | PASS (both) |
| **Revenue growth** | **CAGR >10%** | **CAGR >8% (3yr)** | **3yr CAGR (FY23→FY26) = 7.56%** ($5,349.9M → $6,656.4M) | **FAIL (strategy.md); marginal FAIL (valuation-scoring.md, 7.56% vs >8%)** |
| **Net debt/EBITDA** | **<2x** | **<2.5x** | **1.138×(FY26, the only year with positive EBITDA) / −0.891×(FY25) / −1.544×(FY24) / 4.566×(FY23)** — the ratio is only mechanically meaningful in years with positive EBITDA; FY26 (the one usable year) is within both thresholds, but FY24/FY25 produce a negative ratio purely because EBITDA itself was negative (not a sign of balance-sheet strength), and FY23's 4.566× breaches both thresholds outright. **Not a clean pass** — the metric is not reliably computable across the lookback because the denominator (EBITDA) is itself unreliable | **FAIL / not meaningfully computable (both)** — see narrative below |
| **FCF/NI conversion** | **>70% for 2+ yrs** | (same check, implicit) | **−154.8%(FY26) / 4.8%(FY25) / 4.2%(FY24) / 18.1%(FY23)** — never close to 70% in any year; FY26's negative ratio reflects positive FCF against a still-negative NI (denominator sign flip), not strong conversion | **FAIL (both)** |
| **FCF yield** | (not separately gated) | **>4%** | TTM (FY26) FCF $461.5M ÷ live market cap $44.01B (185.67M shares × $237.04) = **1.05%** | **FAIL (valuation-scoring.md leg)** |
| **EV/EBIT** | (not separately gated) | **<20x** | EV (live) ≈ $44.98B (market cap + total debt − cash) ÷ FY26 EBIT of **−$36.5M** = **undefined / meaningless** (negative-EBIT denominator); 3 of the last 4 years also show negative EBIT (FY23: −$1,194.2M, FY24: −$3,562.2M, FY25: −$4,315.1M, partly driven by the FY25 goodwill impairment) | **FAIL — EV/EBIT is undefined on a negative earnings base (valuation-scoring.md leg)** |
| Moat signal | stable/growing share, brand, network effect | (qualitative, same) | Genuine and real: Rockstar Games' GTA franchise is one of entertainment's most valuable IP properties, with massive pre-order demand confirmed by the very Telegram post that triggered this look, plus 2K Games and the recently-acquired Zynga mobile portfolio diversifying the revenue base. This is a business with a strong qualitative moat | PASS (both) — but does not offset the quantitative failures below |
| Dilutive issuance pattern | none | none | **Shares outstanding have risen every year**: 168.9M(FY23) → 170.8M(FY24) → 177.1M(FY25) → 185.4M(FY26) — a cumulative ~9.8% increase over 3 years, alongside meaningful annual stock-based compensation ($311–333M/yr) and rising "Issuance of Capital Stock" in the cash flow statement (most notably $1,247.5M in FY26, separate from SBC, indicating an equity raise or convertible-related issuance during the year) | **FAIL — a real, multi-year dilutive issuance pattern is present (both)** |

### Result: **Phase 01 FAIL**

TTWO fails on a wide majority of independent, structural criteria under both threshold sets carried in this framework — this is not a borderline or single-metric case:

1. **Profitability and ROIC — the core quality gate — fail outright, every available year.** Net margin has been negative in all 4 fiscal years on record (−4.48% to −79.50%), and ROIC has likewise been negative every year (−1.12% to −89.88%). The framework's quality gate requires **>15%** on both; TTWO has never once been positive on either metric in the lookback window, let alone above threshold. Even excluding the well-documented FY2025 one-off ($3.545B Zynga goodwill impairment), FY2023, FY2024, and FY2026 were all independently loss-making on an operating and net basis — this is not a single distorted year masking an otherwise-profitable trend.

2. **Cash generation is inconsistent and FCF/NI conversion never clears the bar.** FCF was negative in 3 of the last 4 years (FY23–FY25), only turning positive in the most recent fiscal year (FY26: +$461.5M). FCF/NI conversion — meant to confirm that *reported* profit is real cash — is not a meaningful check here because NI itself has been negative throughout; the ratio swings from 4–18% (when both FCF and NI are negative) to a nonsensical −154.8% in FY26 (positive FCF against negative NI). None of this resembles the ">70% for 2+ years" the gate requires.

3. **Net debt/EBITDA and EV/EBIT are not reliably computable, and where computable, fail.** Both ratios use EBIT/EBITDA as a denominator, and that denominator has been negative in 3 of the last 4 years (EBIT) and 2 of the last 4 years (EBITDA) — producing mathematically negative or wildly swinging "leverage" and "valuation" ratios that do not represent what the gate is designed to measure. The one year where EBITDA is solidly positive and the ratio is interpretable (FY26: Net Debt/EBITDA 1.14×) does clear both thresholds, and FY23's 4.566× breaches both — so even on the most charitable reading, this criterion does not show a consistent pass. EV/EBIT is undefined on the current (negative) EBIT base entirely.

4. **Revenue growth falls just short of the gate.** 3-year revenue CAGR of 7.56% (FY2023 $5,349.9M → FY2026 $6,656.4M) clears neither the stricter strategy.md bar (>10%) nor — albeit only marginally — the looser valuation-scoring.md bar (>8%). This is the one criterion close to passing, but it does not on the numbers as filed.

5. **A genuine, multi-year dilutive issuance pattern is present.** Shares outstanding rose from 168.9M to 185.4M (+9.8%) over the FY2023–FY2026 window, with rising annual stock-based compensation and a large ($1.25B) capital-stock issuance in FY2026 — directly contrary to the "no dilutive issuance pattern" requirement under both threshold sets.

The one unambiguous strength is **gross margin** (41.9–57.2%, genuinely expanding) and a real qualitative **moat** (the Rockstar/GTA IP franchise, reinforced by 2K Games and Zynga). Phase 01 is conjunctive, however — a strong gross margin and a recognizable brand do not offset failing profitability, ROIC, cash generation, leverage-ratio reliability, and a real dilution pattern simultaneously.

Per [new-position.md](../.claude/commands/new-position.md) step 2 and [operating-brief.md](../framework/operating-brief.md): **"if it fails, stop and report why rather than proceeding to scoring."** Accordingly, **no Rate Environment Gate and no Phase 02 valuation score were computed** — doing so on a name with negative trailing earnings across nearly every available metric would be exactly the "black-box theater" this framework's explicit rule declines to produce (yfinance's own `pegRatio` of 3.35 and `forwardPE` of 23.81 are visible in the raw data pull but are not scored here, consistent with that same rule — a forward PE computed against a forward-EPS estimate on a company with no clean trailing-earnings base is not a substitute for passing the quality gate first).

This is not a verdict on Take-Two's prospects once GTA VI actually ships (November 19, 2026, per the company's own confirmed date) — the franchise's commercial pull is real and visible in the very Telegram post that triggered this look, and the company has itself guided to its first GAAP-profitable fiscal year (FY2027) on the back of that launch. But this framework scores **trailing, filed financials** at the Phase 01 gate, deliberately before any pre-launch narrative or forward guidance is allowed to influence the assessment (Rule 0 / "never invent or estimate," and guidance is explicitly excluded from the scored inputs per valuation-scoring.md). On the numbers filed through fiscal year-end March 2026, Take-Two is a serially loss-making, negative-ROIC business carrying a real share-dilution pattern — a pre-catalyst, story/turnaround profile, not a quality compounder by this framework's Phase 01 definition.

---

## 4. Recommendation

**PASS.** Do not open a position. No order setup, no fair-value derivation, no position sizing — that work is not meaningful for a name that fails the quality gate this framework uses to define its investable universe on nearly every quantitative criterion, and producing it anyway would be exactly the "black-box theater" the MCD and NOK precedents both explicitly declined to produce.

**Worth flagging for context (not a basis for any action):** Hybrid Upgrade 4 (Turnaround Sub-Gate) exists in this framework for a previously-stumbling business with an identifiable moat, but it requires **all five** of: (1) historical ROIC >15% for ≥5 of the past 10 years (data unavailable beyond FY2023, and none of the 4 available years come close to 15% regardless — disqualifying on this condition alone), (2) verified CEO/CFO insider buying >$500K in the past 6 months (not checked — moot given condition 1 already fails), (3) an independent FV estimate showing ≥40% margin of safety (not computed — Phase 01 FAIL means no FV work was done), (4) Net Debt/EBITDA <3× (ambiguous given the denominator-reliability issue noted above, but likely passes on the one clean year), (5) a still-identifiable core moat (yes, per the qualitative note above — the GTA/Rockstar franchise). Condition 1 alone is enough to disqualify the Turnaround path, consistent with how this same condition disqualified NOK's prior session.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — Phase 01 FAILs are not put on a recurring re-check cadence by default (see [watchlist/README.md](../watchlist/README.md): "Phase 01 FAIL / not scored" entries don't carry a numeric score to go stale).
- **Rule 9 fundamental trigger** that would warrant a fresh look regardless of schedule: TTWO's **fiscal Q3 FY2027 earnings release** (the quarter containing GTA VI's confirmed November 19, 2026 launch) is the single most obvious future trigger — if it shows the company actually delivering the GAAP-profitable results management has guided to (turning net margin and ROIC durably positive, FCF/NI conversion toward a healthy range, and EV/EBIT computable again on a positive-earnings base), that would be a material fundamental change warranting a fresh full evaluation. A sustained reversal of the share-dilution trend, or a quarter showing 3yr revenue CAGR durably above 8–10% off a post-launch base, would also qualify. Absent one of these, future Telegram mentions of TTWO (including further GTA VI pre-order/sales hype) should be treated as routine "last checked, no change" pings rather than triggering a full re-evaluation each time, consistent with the MCD/NOK precedent — the trailing financials underlying today's FAIL will not change until a new quarterly filing lands.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and valuation ratios.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to operating profit, independent of capital structure; undefined/meaningless when EBIT is negative.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. Not meaningful when Net Income is itself negative.
- **Forward PE** — Price ÷ next twelve months' expected earnings per share.
- **GAAP** — Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements.
- **Goodwill impairment** — A non-cash accounting write-down that reduces the recorded value of a prior acquisition (here, Zynga) when its expected future profitability no longer supports the price originally paid for it.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. Unreliable when EBITDA is negative.
- **NI (Net Income)** — accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — operating profit after a tax adjustment but before financing costs; the numerator this framework uses to compute ROIC.
- **PEG ratio** — PE ratio ÷ earnings growth rate — a PE adjusted for growth; not scored in this session since Phase 01 failed first.
- **Phase 01–06** — the six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Qualified Quality List** — the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (TTWO does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **SBC (Stock-Based Compensation)** — employee pay in the form of company shares or stock options rather than cash; a real economic cost to existing shareholders through ongoing dilution.
- **Treasury yield (10Y)** — the interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **Turnaround Sub-Gate** — the conditional path (Hybrid Upgrade 4) that lets a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests (historical ROIC, insider buying, margin of safety, debt level, identifiable moat).
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.

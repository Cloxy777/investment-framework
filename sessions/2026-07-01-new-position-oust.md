# New Position Evaluation — OUST (Ouster, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-07-01
**10Y US Treasury yield:** 4.38% (most recent value on record in this repo, per the 2026-07-01 NKE rescore session — cited for header consistency with the standard session template only; **not actually invoked**, since Phase 01 fails before the Rate Environment Gate is reached — see Section 3)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — a `FinnInvestChannel` post (#2859, ~06:54 UTC 2026-07-01) reading "Ouster це компанія, яка робить lidar-сенсори" ("Ouster is a company that makes lidar sensors"), part of a short thread on renewed robotics-sector interest following the Agility Robotics IPO. OUST has **no prior watchlist entry anywhere** under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). Per [.claude/commands/telegram-scan.md](../.claude/commands/telegram-scan.md) step 4's first bullet ("No watchlist entry exists at all → `/new-position <TICKER>`"), this proceeds as a standard `/new-position` run — same "first mention of an untracked name gets a full evaluation regardless of how thin the trigger is" precedent as AMD/CDR/CHTR/CRCL. The ticker was resolved unambiguously: "Ouster" + "lidar sensors" identifies Ouster, Inc. (NASDAQ: OUST) with no plausible alternative reading. Per Rule 0, **no claim from the triggering post is used as a financial input anywhere below** — it is only the reason this ticker was looked at.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first, before any valuation work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 625287738, NASDAQ) | **$61.09** | last trade |
| Day change (same snapshot) | **−2.29% (−$1.43)** on the day (prior close $62.52) | not used as a financial input — directional context only |
| 52-week range (IBKR `misc_statistics`) | low $16.40 / high $63.79 | currently ~4.2% below the 52-week high; **+272.5%** off the 52-week low |
| Bid/ask | $60.90 / $62.00 | live NBBO at fetch time |

**Live price used throughout this session: $61.09.**

---

## 2. Data Source Note — yfinance blocked, fallback to SEC EDGAR

`yfinance` failed identically to the documented AAPL/CHTR/WSE/AMD/CDR/CRCL precedents in this environment (`curl_cffi.requests.exceptions.SSLError: ... TLS connect error: ... OPENSSL_internal: invalid library`) even after a fresh `pip install yfinance`. Confirmed environment-level `curl_cffi` TLS-impersonation incompatibility, not ticker-specific.

**Fallback used, per Rule 0's documented contingency:** Ouster, Inc. is a US SEC filer (CIK 0001816581) — fundamentals sourced from:
- **Form 10-K for FY2025** (period ended 2025-12-31, filed 2026-03-02, accession 0001628280-26-013313) — audited financials, MD&A, and Competition section.
- **SEC XBRL `companyfacts` API** — for the FY2019–FY2025 annual time series (revenue, net income, gross profit, operating cash flow, capex, D&A, cash, debt, equity) used for growth and multi-year trend checks.

Every figure in Section 3 below is cited to one of these two sources. No required Phase 01 input is missing or invented.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifiers (checked first — these override the weighted score regardless of outcome)

| Disqualifier | OUST data | Carve-out exists in the text? | Verdict |
|---|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF = Operating cash flow − capex (both from the XBRL `companyfacts` annual 10-K series): FY2019 −$40.19M, FY2020 −$42.12M, FY2021 −$71.06M, FY2022 −$110.69M, FY2023 −$140.90M, **FY2024 −$37.45M**, **FY2025 −$64.85M** (OCF −$39.956M − capex $24.893M). **Every one of the 7 fiscal years on record is FCF-negative — the company has never had a single positive-FCF year, let alone a 3-year streak.** | **No** — the FCF-positivity disqualifier carries no growth-capex carve-out in `quality-scoring.md`. | **🔴 TRIGGERED — hard FAIL, independent of every other number in this section.** |
| FCF/Net Income conversion <70% for 2+ consecutive years | FY2025 FCF/NI = −$64.85M / −$60.377M = 107.4% (literal ratio); FY2024 = −$37.45M / −$97.045M = 38.6%. **Both Net Income and FCF are negative in every year shown — this ratio has no meaningful "conversion" interpretation when there's no accounting profit to convert.** Not scored as triggering/not-triggering on its own; superseded by the FCF-positivity disqualifier above. | N/A — moot | Not independently assessed (moot, given 3.1's first row already fails outright) |
| Net Debt/EBITDA over threshold (2.5×/4×) | Financial debt: **$0** (no `LongTermDebtNoncurrent`, convertible notes, or short-term borrowings reported in FY2024 or FY2025 — only ordinary operating-lease liabilities, $12.94M noncurrent FY2025). Cash = $67.413M → **Net debt = −$67.413M (net cash)**. EBITDA FY2025 = Operating loss −$73.999M + D&A $7.781M = **−$66.218M (negative)**. | N/A — zero financial debt, so the ratio's leverage-risk purpose (years of EBITDA needed to retire debt) doesn't apply regardless of EBITDA's sign — there is no debt to retire. | PASS — does not apply (see 3.2 Balance Sheet row for the scoring treatment of this edge case) |

OUST triggers the FCF-positivity hard disqualifier outright, with **no available carve-out**. Per [new-position.md](../.claude/commands/new-position.md) step 2, this alone is sufficient to stop here — but every sub-score below is still shown in full, per that same step's explicit instruction.

### 3.2 Sub-scores (all six, per the weighted formula)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net margin = −$60.377M / $169.384M = **−35.65%** → NetMargin_Component = clamp(−35.65/30×100, 0, 100) = **0.0**. ROIC = NOPAT/Invested Capital = −$73.999M / $194.325M = **−38.08%** → ROIC_Component = clamp(−38.08/30×100, 0, 100) = **0.0**. NOPAT = Operating loss −$73.999M × (1 − 0% — no tax benefit assumed on an operating loss with no realized cash tax shield). Invested Capital = Debt $0 + Equity $261.738M − Cash $67.413M = $194.325M. Profitability_Score = (0.0+0.0)/2 = **0.0** (the FCF-positivity cap at 40.0 is moot — raw score is already below that). | **0.0** |
| **Margins (15%)** | Gross margin = Gross profit $83.436M / Revenue $169.384M = **49.27%** (FY2025), up from 36.42% (FY2024) and 9.98% (FY2023, cost-of-revenue spike year) — structurally expanding. GrossMargin_Score = clamp(49.27/80×100, 0, 100) = **61.6**. No +10 trend bonus applies (that bonus is only for margins still *below* the 40% static threshold — OUST already clears 40%). | **61.6** |
| **Growth (20%)** | Revenue: FY2022 $41.029M → FY2023 $83.279M → FY2024 $111.101M → FY2025 $169.384M. 3yr CAGR = (169.384/41.029)^(1/3) − 1 = **+60.41%** → Growth_Score = clamp(60.41/25×100, 0, 100) = **100.0** (capped). No +10 TAM modifier applied even though the underlying robotics/autonomy TAM is plausibly expanding — the score is already at the 100.0 ceiling, so the modifier is moot; not applying it also avoids relying on the (Rule-0-excluded) Telegram post's "sector came alive" framing as evidence. | **100.0** |
| **Balance Sheet (15%)** | Financial debt = $0 → Net Debt/EBITDA is degenerate (0 ÷ any EBITDA = 0×) regardless of EBITDA's sign, since there is no debt for EBITDA to service. Scored as the best-case leverage profile: BalanceSheet_Score = **100.0**. **Flagged explicitly as a judgment call**: the formula `100×(1−NetDebt/EBITDA/4)` produces a nonsensical result if evaluated literally with EBITDA negative (−$66.218M) and net debt negative (−$67.413M net cash) — a positive quotient (~1.02×) that happens to *understate* how safe the balance sheet actually is. The substantive fact driving this score is "no financial debt, $67.4M cash" — not an artifact of dividing two negative numbers. | **100.0** |
| **Moat Signal (15%)** | Checked all 5 signals against cited evidence in the FY2025 10-K; **none meet the framework's evidentiary bar**: (1) *Market share* — the 10-K's own "Strengthen our worldwide sales and marketing presence" strategy item states intent "to further grow our market share," aspirational language, not cited third-party share data showing current share is stable/growing → not documented. (2) *Brand premium* — the 10-K's own MD&A instead discloses the *opposite*: "we...experience declines in the average selling prices of our products...as our competitors continue to produce and commercialize lower cost competing technologies" → contradicted, not documented. (3) *Network effect* — a hardware sensor manufacturer with no two-sided-marketplace mechanism → not documented. (4) *Switching costs* — no documented integration-lock-in or migration-cost mechanism found → not documented. (5) *Scale cost advantage* — the 10-K explicitly states OUST "compete[s] against established market participants that have substantially greater resources," and must "continually reduce product and manufacturing costs" via "scaling our production volumes" (i.e. still chasing scale, not holding a scale advantage); the Competition section lists 11 named rivals including Hesai Technology and RoboSense, both larger-volume Chinese lidar makers → contradicted, not documented. Moat_Score = (0/5)×100. | **0.0** |
| **FCF Quality (10%)** | FY2025 FCF/NI ratio = −$64.849M / −$60.377M = 107.4% *(literal formula)* → clamp(((1.074−0.40)/0.60)×100, 0, 100) = 100.0 *(literal result)*. **Not used as-is**: with Net Income negative, "FCF/NI conversion" measures something different from its intended meaning (whether real cash backs an actual accounting profit) — there is no profit here to convert, only a larger cash loss than the accounting loss. Scoring this 100.0 would imply excellent earnings quality for a company burning $64.85M of cash a year, which is not defensible. Conservative override applied: **0.0** (no genuine profit-to-cash conversion is occurring). Flagged explicitly per Rule 0 rather than silently taking the favorable literal-formula output. | **0.0** (conservative override; 100.0 under the literal formula — shown for transparency, not used) |

### 3.3 Final weighted Quality Score

```
Quality Score = (0.0 × 0.25) + (61.6 × 0.15) + (100.0 × 0.20) + (100.0 × 0.15) + (0.0 × 0.15) + (0.0 × 0.10)
              = 0.0 + 9.24 + 20.0 + 15.0 + 0.0 + 0.0
              = 44.24 → 44.2
```

*(For transparency: taking FCF Quality at its literal, non-overridden 100.0 instead would give 0.0 + 9.24 + 20.0 + 15.0 + 0.0 + 10.0 = 54.2 — still decisively below the 80.0 gate either way.)*

**44.2 < 80.0 — fails the gate**, in addition to the hard disqualifier already firing independently in Section 3.1. Two independent mechanisms agree on the same verdict.

### Result: **Phase 01 FAIL**

OUST is a fast-growing lidar-sensor maker (revenue +60.4% 3yr CAGR, gross margin expanding from ~10% to ~49% over 3 years) riding genuine robotics/autonomy-sector demand — none of that growth story is in dispute. But it has **never once, in 7 fiscal years as a public/pre-merger company, generated positive free cash flow**, it is still deeply loss-making (net margin −35.65%, ROIC −38.08%), and its own 10-K discloses declining average selling prices and competition from larger, lower-cost rivals (Hesai, RoboSense) rather than any moat. The quality gate's job is exactly to catch "exciting growth story, no sustainable profitability or cash generation yet" — which is what this is.

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0, or a hard disqualifier fires, stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring.

This is not a verdict that Ouster's technology or growth trajectory is bad — the revenue growth and margin expansion are real and worth re-checking later. It is a verdict that **the company has not yet demonstrated it can turn that growth into positive free cash flow or a defensible competitive moat**, both of which this framework requires before valuation is even attempted.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mandatory Rule 9 re-check:** Ouster's next scheduled disclosure — Q2 FY2026 Form 10-Q (period ending 2026-06-30), expected ~early August 2026.
- **Mechanical trigger:** a first-ever positive full fiscal-year FCF print (or a credible multi-quarter trend toward one) would meaningfully change the hard-disqualifier picture and warrant a fresh full run.
- **Other Rule 9 events:** a guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause.
- Absent any of the above, future Telegram mentions of OUST should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **D&A** — Depreciation & Amortization — a non-cash expense spreading the cost of long-lived assets over time.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; not meaningful when Net Income is itself negative (see Section 3.2's FCF Quality row).
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three specific failure conditions in this framework's Quality Score engine (sustained FCF/NI conversion below 70%, excessive Net Debt/EBITDA, or no FCF-positive 3-year run) that fails a company outright regardless of its weighted score.
- **Invested Capital** — The total capital (debt + equity, minus cash) deployed in a business — the denominator of ROIC.
- **Lidar** — "Light Detection and Ranging" — a sensor technology that measures distance using laser pulses, used in autonomous vehicles, robotics, and industrial automation to build a 3D map of surroundings.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. A negative figure means net cash, not net debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT** — Net Operating Profit After Tax — EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (OUST does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price (and primary financial data) before any valuation work — never infer or invent it.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly/interim earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).

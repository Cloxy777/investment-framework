# New Position Evaluation — CDR (CD PROJEKT S.A.)

**Task type:** NEW POSITION
**Date:** 2026-06-29
**10Y US Treasury yield:** 4.40% (most recent available value, FRED series DGS10, as of 2026-06-25 — cited for header consistency with the standard session template only; **not actually invoked**, since Phase 01 fails before the Rate Environment Gate is reached — see Section 3)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — a `myroslavkorol` post (explicitly tagged `$CDR`) referencing the *Cyberpunk Edgerunners 2* anime trailer (Netflix), tied to CD PROJEKT's Cyberpunk 2077 IP. CDR has **no prior watchlist entry anywhere** under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). Per [.claude/commands/telegram-scan.md](../.claude/commands/telegram-scan.md) step 4's first bullet ("No watchlist entry exists at all → `/new-position <TICKER>`"), this proceeds as a standard `/new-position` run. The ticker (WSE: CDR) was resolved by context — CD PROJEKT S.A. is the Cyberpunk 2077 IP owner/developer — and the post's explicit `$CDR` tag, not guessed; per Rule 0, **no claim from the triggering post is used as a financial input anywhere below**, it is only the reason this ticker was looked at.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first (and re-confirmed immediately before finalizing this session), before any valuation work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 268960294, WSE) | **221.10 PLN** | last trade |
| Day change (same snapshot) | **+1.70% (+3.70 PLN)** on the day | not used as a financial input — directional context only |
| 52-week range (IBKR `misc_statistics`) | low 211.30 / high 297.00 PLN | currently **−25.6%** below the 52-week high |
| 52-week open | 278.00 PLN | for context only |
| Bid/ask | unavailable at fetch time | no live NBBO returned (outside continuous WSE trading hours at fetch time) |

**Live price used throughout this session: 221.10 PLN.**

---

## 2. Data Source Note — yfinance blocked, fallback to CD PROJEKT's own primary IR disclosures

`yfinance` failed identically to the documented AAPL/CHTR/WSE precedents in this environment: `curl_cffi.requests.exceptions.SSLError: ... TLS connect error: ... OPENSSL_internal: invalid library` even after a fresh `pip install yfinance lxml`. This is a confirmed environment-level `curl_cffi` TLS-impersonation incompatibility, not ticker-specific.

**Fallback used, per Rule 0's documented contingency:** CD PROJEKT is a Polish (WSE-listed) issuer, not an SEC filer, so the fallback is the company's own audited primary disclosures rather than SEC EDGAR:
- **Consolidated financial statements of the CD PROJEKT Group for 2025** (FY2025 actual + FY2024 comparative, *restated* to exclude the divested GOG.COM segment as discontinued operations) — `cdprojekt.com`, published March 2026.
- **Consolidated financial statements of the CD PROJEKT Group for 2024** (FY2024 actual + FY2023 comparative, *non-restated*, includes GOG.COM) — `cdprojekt.com`, published March 2025.
- **"Key financial data" workbook** (official XLSX, one sheet per fiscal year back to 2010) — `cdprojekt.com`, published March 2026 — used to source the FY2022 revenue/profit comparative not otherwise available without restatement ambiguity.

Every figure in Section 3 below is cited to one of these three documents or to a labelled WebSearch source (used only for the qualitative Moat-signal check, never for a financial number). No required Phase 01 input is missing or invented.

**Important basis caveat, disclosed up front:** CD PROJEKT sold its GOG.COM platform during FY2025 and restated FY2024 comparatives to present GOG as discontinued operations. FY2025 and the *restated* FY2024 column therefore exclude GOG; the FY2024 *actual* (non-restated) and FY2023 figures, pulled from the FY2024 report, still include it. Every figure below is labelled with which basis it's on, and Section 3.2's Growth sub-score explicitly flags where this creates a like-for-like distortion.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

**This is the first `/new-position` run in this repo to use the new 0–100.0 Quality Score engine** (replacing the old binary Phase 01 screen) — `quality-scoring.md` was added this same day and no prior session has exercised it yet.

### 3.1 Hard disqualifiers (checked first — these override the weighted score regardless of outcome)

| Disqualifier | CDR data (all figures thousand PLN) | Carve-out exists in the text? | Verdict |
|---|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF = Net cash from operating activities − true CapEx (capitalized development-project spend + PP&E/intangible/investment-property purchases, isolated from total investing cash flow, which is dominated by non-operating treasury-deposit/bond churn for this cash-rich company): **FY2023 = +279,944** (610,881 − 330,937) · **FY2024 = +173,817** (521,297 − 347,480) · **FY2025 = −47,218** (590,880 − 638,098) — **streak broken in the most recent year.** | **No** — `quality-scoring.md` states this disqualifier with no documented-growth-capex carve-out, unlike the one below. | **🔴 TRIGGERED — hard FAIL, independent of every other number in this section.** |
| FCF/Net Income conversion <70% for 2+ consecutive years | FY2023 = 58.19% (279,944/481,105) · FY2024 = 36.99% (173,817/469,874) · FY2025 = −7.94% (−47,218/594,708) — **all three years below 70%**, so the literal 2+-consecutive-years condition is also met | **Yes** — carve-out applies "without a documented growth-capex explanation." CD PROJEKT's own FY2025 cash-flow statement shows "Expenditure on development projects" (capitalized game-dev cost) rising from 272,655 (FY2023) → 249,311 (FY2024) → **513,241 (FY2025)**, and third-party reporting confirms this is funding **four simultaneous in-development titles** — The Witcher 4/"Polaris" (499 developers as of Feb 2026, up from 411 a year earlier), Cyberpunk 2 (149 developers, up from 84), plus the new-IP "Project Hadar" and Boston-studio "Project Sirius." This is a documented, cited growth-capex story, not an earnings-quality red flag. | Does **not** independently fire — carve-out applies. Reported here for transparency since the literal numeric test is met. |
| Net Debt/EBITDA over threshold (2.5×/4×) | Total debt = 29,603 (IFRS16 lease + other financial liabilities only — **no bank loans or bonds**) · Cash 114,115 + bank deposits >3mo 520,813 → **Net debt = −605,325** (net cash) · EBITDA FY2025 = Operating profit 470,648 + D&A 68,669 = 539,317 → **Net Debt/EBITDA = −1.12×** | N/A — net cash, not net debt | PASS — does not apply |

CDR triggers **one of three** hard disqualifiers outright (FCF positivity), with no carve-out available for that specific one. Per [new-position.md](../.claude/commands/new-position.md) step 2, this alone is sufficient to stop here — but every sub-score below is still shown in full, per that same step's explicit instruction.

### 3.2 Sub-scores (all six, per the weighted formula)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net margin (continuing ops) = 520,869/866,989 = **60.08%** → NetMargin_Component = clamp(60.08/30×100) = **100.0**. ROIC = NOPAT/Invested Capital = 455,392/3,205,347 = **14.21%** → ROIC_Component = clamp(14.21/30×100) = **47.4**. NOPAT = EBIT 470,648 × (1 − 3.24% effective tax rate) = 455,392; effective tax rate validated against Poland's "IP Box" 5% preferential regime on qualifying IP/game income. Invested Capital = Debt 29,603 + Equity 3,289,859 − Cash 114,115 = 3,205,347. Uncapped Profitability_Score = (100.0+47.4)/2 = **73.7** — **but capped at 40.0**, since CDR is not FCF-positive 3+ consecutive years (Section 3.1). | **40.0** (capped) |
| **Margins (15%)** | Gross margin = Gross profit 788,016 / Revenue 866,989 = **90.89%** (FY2025) vs. 85.24% (FY2024 restated) vs. 69.28% (FY2023 non-restated, GOG included) — structurally expanding either way the comparison is sliced. GrossMargin_Score = clamp(90.89/80×100) = **100.0** (already at the ceiling; the +10 trend bonus is moot — can't exceed 100.0). | **100.0** |
| **Growth (20%)** | Revenue: FY2022 = 952,576 → FY2023 = 1,230,199 → FY2024 = 985,030 (non-restated, incl. GOG) / 798,372 (restated, excl. GOG) → FY2025 = 866,989 (continuing ops only, GOG already divested). Literal 3yr CAGR on the only fully-reported start/end figures (952,576 → 866,989) = **(866,989/952,576)^(1/3) − 1 = −3.09%** → Growth_Score = clamp(−3.09/25×100) = **0.0**. **Caveat:** this figure is mechanically distorted by the GOG divestment (revenue is stripped from the 2025 endpoint that was present in the 2022 start point) — it is *not* a clean read of organic decline. The one available like-for-like comparison (FY2024 restated 798,372 → FY2025 866,989) shows **+8.59% YoY growth**, and Q1 2026 reportedly grew +6% YoY — both point to a healthier continuing-business trajectory than the literal 3yr figure implies. No +10 TAM/pricing-power modifier applied (no citable evidence of TAM expansion or price increases without volume loss found — see Moat section). No −10 structural-deceleration modifier applied either: the decline is a portfolio-composition effect (divestment), not organic deceleration, so applying that modifier would mischaracterize the cause. Formula input left at the literal, sourced figure rather than an invented "cleaner" estimate, per Rule 0. | **0.0** |
| **Balance Sheet (15%)** | Net Debt/EBITDA = −1.12× (Section 3.1) → BalanceSheet_Score = clamp(100×(1−(−1.12)/4)) = clamp(128.0) = **100.0** (capped — deep net-cash position). | **100.0** |
| **Moat Signal (15%)** | Checked all 5 signals against cited evidence; **none meet the framework's specific evidentiary bar**: (1) *Market share* — found absolute unit-sales scale (Cyberpunk 2077 35M lifetime units; Witcher trilogy 85M lifetime units) but no cited third-party *market-share %* of the AAA RPG segment → not documented. (2) *Brand premium* — Morningstar attributes CDR's moat qualitatively to "storytelling prowess and loyal fan base," but this is not the required "price increases without volume loss" pricing-power evidence → not documented. (3) *Network effect* — CD PROJEKT's only two-sided-marketplace mechanism was GOG.COM, **divested as a discontinued operation during FY2025** and no longer part of the continuing business being scored; CD PROJEKT RED's core products are single-player narrative games with no documented network-effect mechanism → not documented. (4) *Switching costs* — no documented lock-in/migration-cost mechanism found for a game publisher's consumer products → not documented. (5) *Scale cost advantage* — no cost-per-unit-vs-competitors data found → not documented. Moat_Score = (0/5)×100. | **0.0** |
| **FCF Quality (10%)** | Most recent year (FY2025) FCF/NI ratio = −47,218/594,708 = **−7.94%** (or −9.07% on a continuing-ops-NI-only basis of 520,869 — either basis floors the formula identically). FCFQuality_Score = clamp(((−0.0794−0.40)/0.60)×100) = clamp(−79.9) = **0.0**. | **0.0** |

### 3.3 Final weighted Quality Score

```
Quality Score = (40.0 × 0.25) + (100.0 × 0.15) + (0.0 × 0.20) + (100.0 × 0.15) + (0.0 × 0.15) + (0.0 × 0.10)
              = 10.0 + 15.0 + 0.0 + 15.0 + 0.0 + 0.0
              = 40.0
```

**40.0 < 80.0 — fails the gate**, in addition to the hard disqualifier already firing independently in Section 3.1. Two independent mechanisms agree on the same verdict, which is itself a useful cross-check that neither calculation is an isolated error.

### Result: **Phase 01 FAIL**

CD PROJEKT is, on several individual metrics, a genuinely excellent business — a ~91% gross margin, a 60% net margin, double-digit ROIC, an effectively debt-free balance sheet sitting on ~605M PLN of net cash, and a credible multi-title development pipeline (Witcher 4, Cyberpunk 2, two new IPs) backed by rapidly growing headcount. None of that is in dispute. But the framework's quality gate is built around **sustained cash generation**, not just accounting profitability, and FY2025 broke a clean run of positive free cash flow — driven by a roughly 84% year-over-year jump in capitalized development spend (347,480 → 638,098 thousand PLN) as four AAA titles are funded simultaneously. That is a defensible, well-documented strategic choice for a company mid-pipeline — but it is exactly the kind of "great business, badly-timed cash profile" case the hard disqualifier (Section 3.1) is designed to catch with no growth-capex exception, and the 40.0 weighted score (driven down by the FCF-positivity cap on Profitability, the zero Growth score on a GOG-divestment-distorted CAGR, and zero documented Moat signals) reaches the same conclusion independently.

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0, or a hard disqualifier fires, stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring.

This is not a verdict that CD PROJEKT is a bad company — the margin, balance-sheet, and pipeline picture is strong. It is a verdict that **FY2025's negative free cash flow, driven by simultaneous investment in four titles, currently fails this framework's strict cash-generation bar**, which carries no exception for that specific disqualifier. A reversal of that FCF trend (e.g. once Witcher 4 development capex normalizes, or on early sales of any of the in-development titles) would be the natural trigger to re-run this evaluation.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mandatory Rule 9 re-check:** CD PROJEKT's next scheduled disclosure — the **H1 2026 consolidated semiannual report, expected 2026-09-02** (the company reports semiannually for H1, not a standalone Q2).
- **Mechanical trigger:** a return to 3 consecutive FCF-positive fiscal years (i.e., FY2025 and FY2026 both positive, or earlier if a later full-year report shows FY2025 restated/revised) would clear the hard disqualifier in Section 3.1 and warrant a fresh full run.
- **Other Rule 9 events:** a guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause.
- Absent any of the above, future Telegram mentions of CDR (including further Cyberpunk-franchise content news) should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets (here, mainly capitalized game-development cost).
- **D&A** — Depreciation & Amortization — a non-cash expense spreading the cost of long-lived assets over time.
- **Discontinued operations** — An accounting presentation where a business segment that has been sold or is being wound down is reported separately from continuing operations, with prior-period comparatives restated to match — used here because CD PROJEKT sold its GOG.COM platform during FY2025.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Hard disqualifier** — One of three specific failure conditions in this framework's Quality Score engine (sustained FCF/NI conversion below 70%, excessive Net Debt/EBITDA, or no FCF-positive 3-year run) that fails a company outright regardless of its weighted score.
- **Invested Capital** — The total capital (debt + equity, minus cash) deployed in a business — the denominator of ROIC.
- **IP Box** — A Polish preferential corporate tax regime taxing qualifying intellectual-property income (e.g. game/software royalties) at 5% instead of the standard 19% rate — explains CD PROJEKT's unusually low effective tax rate.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. A negative figure means net cash, not net debt.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT** — Net Operating Profit After Tax — EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (CDR does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price (and primary financial data) before any valuation work — never infer or invent it.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly/interim earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).

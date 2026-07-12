# New Position Evaluation: BAC (Bank of America Corporation) — 2026-07-12

**Task type:** NEW POSITION
**Ticker:** BAC — NYSE, IBKR contract_id 10098
**Company:** Bank of America Corporation — money-center / universal bank (Consumer Banking, Global Wealth & Investment Management, Global Banking, Global Markets)
**Analyst:** Claude (automated session)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — cashtag `$BAC` named in a post from **[t.me/bolshegold](https://t.me/bolshegold)** (post #9735, ~13:22 UTC, 2026-07-12), grouped with `$C`, `$JPM`, `$WFC` under "banking sector, opens earnings season, watch credit-card delinquencies and consumption growth." **This post text is used only as a trigger to run this evaluation — no figure, claim, or number from it is used anywhere in the analysis below.** All financial data below comes from IBKR (live price), the SEC's own XBRL filings (`data.sec.gov`), and Yahoo Finance — never from the Telegram post.

---

## 0. Ticker confirmation & business-model flag

BAC resolves unambiguously to **Bank of America Corporation**, NYSE-listed, IBKR contract_id **10098** (via `search_contracts` — disambiguated from several unrelated same-string tickers on other exchanges and a large family of BAC preferred-share lines, bonds, and unrelated funds/tickers also named "BAC"). Confirmed **not** a current holding — BAC does not appear in [portfolio/holdings.md](../portfolio/holdings.md) — and no prior `watchlist/` entry or `sessions/` record exists for this ticker.

**Business-model mismatch flagged up front**, same finding as the [2026-06-21 SOFI session](2026-06-21-new-position-sofi.md): BAC is a **depository institution** (a bank holding company). This matters before any other step because:
- It has **no GAAP gross-margin line** (no Cost of Revenue to net against) and **no conventional EBIT/EBITDA line** — interest expense is a core funding cost (the cost of deposits/borrowings that fund the loan book), not a financing add-back.
- Its operating cash flow is dominated by trading-account and loan-funding balance-sheet swings, not "owner earnings" in the traditional sense — see Section 3 below.
- [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 1 explicitly assigns **Financials → P/B, DDM (primary) / P/E (secondary)** — not DCF/EV-EBIT — for exactly this reason. (Not reached this session — see Section 4.)

As with SOFI, **the framework's Quality Score has no documented depository-institution carve-out** (confirmed via repo-wide search of [quality-scoring.md](../framework/quality-scoring.md) — the only financial-sector-specific provision is Hybrid Upgrade 5's Net Debt/EBITDA threshold variant for "asset-light financials," which still presumes an EBITDA exists and explicitly does not extend to a balance-sheet-funded bank). Every metric below is annotated with *why* it does or doesn't transfer cleanly to a bank, per "never invent or estimate."

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Source | Price | Note |
|---|---|---|
| **IBKR `get_price_history`** (contract_id 10098, daily bars) | **$59.67** | Close of the most recent completed session, **Friday 2026-07-10** (2026-07-12 is a Sunday — markets closed; confirmed via `datetime` — no trading occurs on the evaluation date) |
| IBKR `get_price_snapshot` "last" field | $59.25 | Discrepancy investigated: this field returned **Thursday 2026-07-09's** close (marked `is_close: true`), not Friday's — superseded by the more complete 5-day price-history pull, which shows the full OHLC sequence through 2026-07-10 |
| Yahoo Finance `regularMarketPrice` | $59.67 | `regularMarketTime` timestamp decodes to 2026-07-10 20:00:03 UTC (4:00pm ET close) — matches IBKR's history bar exactly |

**$59.67 is used throughout** — the two independent sources agree once the correct (most recent, not stale) IBKR field is used. Flagging the snapshot-vs-history discrepancy explicitly per "show every calculation, no black box."

**52-week range** (IBKR `misc_statistics`): low **$44.01**, high **$60.82** (Yahoo: $44.75–$60.83, consistent). 13-week high $60.82 — BAC is trading near its 52-week/13-week high heading into Q2 2026 earnings (confirmed via WebSearch: BAC reports **Tuesday 2026-07-14**, two days after this session).

---

## 2. Phase 01 Quality Score

All figures sourced from **SEC EDGAR's own XBRL filings** (`data.sec.gov/api/xbrl/companyconcept`, CIK 0000070858 — the most authoritative source, used as primary since Yahoo's bank-specific financial-statement modules returned largely empty/non-standard fields for BAC, a known data-vendor gap for depository institutions) and Yahoo Finance's TTM snapshot fields (`quoteSummary`, cross-checked against a second vendor, stockanalysis.com, where noted). Every input is annotated with whether/how it transfers to a bank holding company.

### 2a. Raw inputs (SEC-filed, `us-gaap` XBRL tags, FY2021–FY2025)

| FY (ended 12/31) | Total Revenue (`Revenues`) | Net Income (`NetIncomeLoss`) | Operating Cash Flow (`NetCashProvidedByUsedInOperatingActivities`) | Stockholders' Equity (year-end) |
|---|---|---|---|---|
| 2021 | $89,113M | $31,978M | **−$7,193M** | $270,066M |
| 2022 | $94,950M | $27,528M | **−$6,327M** | $273,197M |
| 2023 | $98,581M | $26,515M | **+$44,982M** | $291,646M |
| 2024 | $101,887M | $27,132M | **−$8,805M** | $295,559M |
| 2025 | $113,097M | $30,509M | **+$12,613M** | $303,243M |

Cross-checked against stockanalysis.com's independently-presented figures — Net Income and OCF match SEC exactly (30,509 / 12,613 for FY2025); stockanalysis.com's *revenue* figures differ by ~5% (e.g. $107,422M vs. SEC's $113,097M for FY2025), likely a different gross-vs-net-of-interest-expense revenue convention. **SEC's own `Revenues` XBRL tag is used as the primary, filed source** per "never invent or estimate — use filed data," with the vendor discrepancy flagged rather than silently reconciled.

Yahoo's TTM snapshot fields (`financialData`/`defaultKeyStatistics`, most current, includes Q1 2026): Net Margin (TTM) **28.96%**, ROE (TTM) **10.64%** — used for the Profitability sub-score below since quality-scoring.md's input spec explicitly calls for "Net Margin (TTM)" / "ROIC (TTM)," not a fiscal-year point figure. Both are broadly consistent with the SEC FY2025 point figures (Net Margin 26.98%, ROE ≈10.19% on average equity) — no material distortion.

### 2b. Hard disqualifier check — **two fire independently**

**(i) Not FCF-positive for 3+ consecutive years** — quality-scoring.md's Hard Disqualifier #3, **no carve-out exists for this one at all** (per [glossary.md](../framework/glossary.md)'s "Hard disqualifier" entry: *"the FCF-positivity check has none"*).
```
2021: −$7,193M   2022: −$6,327M   2023: +$44,982M   2024: −$8,805M   2025: +$12,613M
```
No 3-consecutive-year positive stretch exists anywhere in this 5-year window (negative, negative, positive, negative, positive). **FIRES.**

Same root cause as SOFI's finding: a bank's operating cash flow is dominated by trading-account-security and loan-funding timing, not owner-earnings-style cash generation — this is a structural mismatch between the framework's non-financial-company FCF gate and a depository institution's accounting, not evidence of a cash-burning business. Flagged as a **framework gap**, not silently waived — the documented rule has no carve-out, so the result stands as FAIL.

**(ii) FCF/Net Income conversion ratio <70% for 2+ consecutive years, without a documented growth-capex explanation** — quality-scoring.md's Hard Disqualifier #1.
```
FY2024: −$8,805M / $27,132M = −32.45%   (well below 70%)
FY2025: +$12,613M / $30,509M = +41.34%  (below 70%)
```
Two most-recent consecutive years both fail the 70% bar. The documented waiver ("cited evidence of growth-driven, not maintenance, capex") **does not apply** — a bank has no meaningful capex line driving this; the swing is balance-sheet/trading-book timing, not reinvestment. **FIRES** — no valid carve-out.

**(iii) Net Debt/EBITDA over threshold** — **not evaluable**, no EBITDA line exists for a depository institution (same as SOFI). N/A, not a pass.

### 2c. Sub-score calculation (shown in full despite the controlling hard-disqualifier finding, per "always show full calculation")

**Profitability (25% weight):**
```
NetMargin_Component = clamp((28.96/30)×100, 0, 100) = 96.5
ROIC_Component (bank convention: ROE, per SOFI 2026-06-21 precedent) = clamp((10.64/30)×100, 0, 100) = 35.5
Profitability_Score (uncapped) = (96.5 + 35.5)/2 = 66.0
→ FCF-positivity cap applies (Section 2b(i) fired): Profitability_Score capped at 40.0
Profitability_Score = 40.0
```

**Margins (15% weight):** **N/A — not computable.** Banks report no Cost-of-Revenue/gross-margin line; there is nothing to divide. Same finding, same framework gap as SOFI. Not scored; no substitute invented.

**Growth (20% weight):**
```
Revenue 3yr CAGR (SEC `Revenues`, FY2022 $94,950M → FY2025 $113,097M) = (113,097/94,950)^(1/3) − 1 = 6.00%
Growth_Score = clamp((6.00/25)×100, 0, 100) = 24.0
```
Qualitative modifier: WebSearch of BAC's FY2025 10-K/Q4 2025 earnings materials found #1 U.S. consumer-deposits share and 28 consecutive quarters of net checking-account growth — solid *market-share* evidence (credited under Moat below) but **no citation found that specifically documents TAM expansion or pricing power** (vs. incremental share gain in an already-mature market) meeting the modifier's evidentiary bar, nor any documented structural deceleration. Per "never infer this modifier without a documented source" — **no modifier applied.**
```
Growth_Score = 24.0
```

**Balance Sheet (15% weight):** **N/A — not computable.** No EBITDA line exists for a bank; Upgrade 5's asset-light-financial variant is explicitly scoped to payment networks/exchanges, not a deposit-funded universal bank. (Context only, not scored: BAC's own regulatory capital-adequacy metric, CET1 ratio, was ~13.1% as of Q3 2025 — well above regulatory minimums — but this is not the framework's Net Debt/EBITDA metric and isn't a substitute for it.)

**Moat Signal (15% weight)** — checklist, evidence cited per signal, via WebSearch of BAC's FY2025 10-K / Q4 2025 earnings materials:

| Signal | Result | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | #1 in U.S. consumer deposits; average deposits $945B in 4Q25 (+31% vs. pre-pandemic); 28 consecutive quarters of net consumer-checking-account growth (BAC Q4 2025 earnings materials) |
| Brand premium | FALSE | No cited pricing-power evidence found — deposit/loan pricing is largely market-set; no documented premium-retention data |
| Network effect | FALSE | Retail/commercial banking has no documented two-sided-marketplace mechanism comparable to the framework's definition; no citation found |
| Switching costs | **TRUE** | 92% of BAC's 38.4M consumer checking accounts are "primary" relationship accounts (BAC Q4 2025 earnings materials) — a documented switching-cost mechanism (re-establishing direct deposit/autopay/credit history elsewhere is real friction) |
| Scale cost advantage | FALSE | Scale is evident (2nd-largest U.S. bank by assets, ~$3.5T per Q1 2026) but no cost-per-unit-vs-competitor citation was sourced, which the framework's evidentiary bar requires |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10% weight):**
```
FY2025 FCF/NI ratio = $12,613M / $30,509M = 41.34%
FCFQuality_Score = clamp(((0.4134 − 0.40)/0.60) × 100, 0, 100) = clamp(2.23, 0, 100) = 2.2
```
(This single-year figure is shown per the formula, but the hard disqualifier in Section 2b(ii) — not this continuous score — is what controls, per quality-scoring.md: *"a ratio below 70% for 2+ consecutive years... is a hard disqualifier, independent of this continuous score."*)

### 2d. Weighted score — illustrative only, does not override the hard-disqualifier fail

quality-scoring.md provides no documented mechanism to redistribute weight away from an inapplicable sub-score (unlike valuation-scoring.md's explicit PEG/EV-EBIT redistribution rule) — so no official Quality Score number can be computed without inventing a rule the framework doesn't state. Shown here purely for transparency, on two different (non-official) treatments of the two N/A components:

```
Computable components only (Profitability 25%, Growth 20%, Moat 15%, FCF Quality 10% = 70% of total weight):
  (40.0×0.25 + 24.0×0.20 + 40.0×0.15 + 2.2×0.10) / 0.70 = 21.02 / 0.70 = 30.0

Most generous possible ceiling (both N/A components hypothetically scored 100.0 — their maximum):
  21.02 + 15.0 + 15.0 = 51.02
```

**Even the most generous possible treatment of the two non-computable components (51.0) falls far short of the 80.0+ gate.** The Quality Score fails both on its own weighted terms and, independently and more decisively, on two hard disqualifiers that have no applicable carve-out.

### 2e. Gate Result: ❌ **FAIL**

- Hard disqualifier (i) — not FCF-positive 3+ consecutive years — **fires, no carve-out exists**
- Hard disqualifier (ii) — FCF/NI conversion <70% for 2+ consecutive years — **fires, no valid growth-capex waiver applies**
- Weighted score (any reasonable treatment of N/A components): **30.0–51.0**, well below the 80.0 threshold

Per [.claude/commands/new-position.md](../.claude/commands/new-position.md) Step 2 and this session's explicit instructions: **a Quality Score below 80.0, or a hard disqualifier firing, stops the evaluation here — the Rate Environment Gate, Phase 02 Valuation Score, Composite Score, and fair-value/order-setup work are not run.**

---

## 3. Framework gap flagged (not fixed this session)

Same structural finding as the [2026-06-21 SOFI session](2026-06-21-new-position-sofi.md), now with a **second, more conventionally "high quality" bank** (BAC is solidly profitable, well-capitalized, and #1 in U.S. consumer deposits — a very different risk profile from a recently-chartered neobank) hitting the *identical* hard disqualifiers for the *identical* structural reason: **quality-scoring.md has no documented depository-institution carve-out.** A bank's operating cash flow is mechanically dominated by trading-book and loan-funding timing rather than owner-earnings-style cash generation, which means the "FCF positive 3+ years" and "FCF/NI conversion >70%" hard disqualifiers may be structurally unpassable for *any* bank, regardless of underlying business quality — a candidate framework-improvement item (paralleling Upgrade 5's existing asset-light-financial variant for the Balance Sheet sub-score) worth the user's attention, not resolved here per "never invent or estimate" — no framework file edited this session.

---

## 4. Phase 02 / Composite Score / Fair Value / Order Setup — **NOT RUN**

Per Step 2 of [.claude/commands/new-position.md](../.claude/commands/new-position.md): a Quality Score gate failure stops the evaluation before valuation scoring. No Rate Environment Gate, Phase 02 sub-scores, Composite Score, fair value estimate, or buy/sell/stop order setup were computed for BAC in this session.

---

## 5. Recommendation: **PASS**

**Do not enter a position in BAC.** The Phase 01 Quality Score gate fails — on two independent hard disqualifiers (no carve-out available for either) and on the weighted score under any reasonable treatment of its two non-computable sub-scores. This is a **data-and-methodology finding, not a judgment that BAC is a bad business** — BAC is #1 in U.S. consumer deposits, solidly profitable (28.96% TTM net margin, 10.64% TTM ROE), and adequately capitalized (~13.1% CET1) by conventional bank-analysis standards. The failure reflects a **documented gap in this framework's non-financial-company-oriented Quality Score formula**, applied here exactly as written, per "never invent or estimate financial data."

Added to `watchlist/not-in-portfolio/BAC/` as **Phase 01 FAIL** (Section 6). Re-evaluate if: (a) the framework adds a documented depository-institution carve-out for the FCF-based hard disqualifiers and Balance Sheet sub-score (a candidate framework-improvement item, not yet adopted), or (b) a Rule 9 fundamental trigger fires (BAC reports Q2 2026 earnings **2026-07-14**, two days after this session — a scheduled trigger, not itself a reason to re-run early).

---

## 6. Watchlist entry

Created `watchlist/not-in-portfolio/BAC/BAC-2026-07-12.md` — first entry for this ticker, "Phase 01 FAIL."

---

## 7. Data quality flags carried forward (summary)

- **No Phase 01/02 depository-institution carve-out exists in the framework** — second occurrence of this exact gap (after SOFI, 2026-06-21), now on a much higher-conventional-quality bank, strengthening the case that this is a structural methodology gap rather than a company-specific issue. Flagged as a candidate framework-improvement item; no framework file edited this session.
- **Revenue figures diverge ~5% between SEC's filed `Revenues` XBRL tag and stockanalysis.com's presentation** (net income and operating cash flow matched exactly across both sources) — likely a gross-vs-net-of-interest-expense convention difference. SEC's own filed figure used as primary.
- **IBKR's `get_price_snapshot` "last" field returned a stale (previous-day) close** rather than the most recent session's close — resolved by cross-checking against `get_price_history`, which agreed exactly with Yahoo Finance's `regularMarketPrice`. Flagged in case this snapshot-staleness pattern recurs on other tickers evaluated over a weekend.
- **Growth qualitative modifier not applied** — found solid market-share evidence (credited under Moat) but no citation meeting the bar for documented TAM-expansion or structural-deceleration evidence specifically, so left unmodified per "never infer without a documented source."
- **Two Moat signals (Brand premium, Network effect, Scale cost advantage — 3 of 5) left FALSE for lack of a citation meeting the framework's specific evidentiary bar** (e.g. cost-per-unit data for scale), not because they're necessarily absent for a bank of BAC's size — a conservative, non-inflated reading consistent with "never mark a signal true without a cited source."

---

## 8. Token usage note

This session involved one IBKR contract search, one IBKR price snapshot (flagged stale) and one IBKR price-history pull, several SEC EDGAR XBRL `companyconcept` API calls (`NetCashProvidedByUsedInOperatingActivities`, `NetIncomeLoss`, `Revenues`, `StockholdersEquity`, `InterestAndDividendIncomeOperating`, `NoninterestIncome`, `InterestExpense`), one Yahoo Finance `quoteSummary` pull (multiple modules), two WebFetch calls (stockanalysis.com income statement and cash-flow statement, for cross-checking), and two WebSearch calls (moat/market-share evidence; earnings-date/capital-ratio confirmation) — lighter than the ~120–160K token/ticker range cited in [new-position.md](../.claude/commands/new-position.md)'s batch-processing guidance, since the evaluation stopped at the Quality Score gate rather than running the full Phase 02/fair-value/order-setup workflow.

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CET1 (Common Equity Tier 1) capital ratio** | A bank regulatory-capital adequacy measure — core equity capital divided by risk-weighted assets — the primary metric bank regulators use to judge loss-absorbing capacity, distinct from this framework's own Net Debt/EBITDA leverage gate, which doesn't apply to a bank. |
| **CIK (Central Index Key)** | The unique numeric identifier the SEC assigns to every company that files with EDGAR — used to construct the API/URL paths this framework pulls SEC filings and XBRL data from. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization — operating-profit measures that don't exist in standard form for a bank, since interest is a core funding cost rather than a financing add-back. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself; for a bank, operating cash flow is dominated by trading-account and loan-funding timing rather than owner-earnings-style generation. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; not a clean signal for a bank whose cash flow swings on balance-sheet timing rather than operating performance. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score — see [quality-scoring.md](../framework/quality-scoring.md). |
| **Moat** | A durable competitive advantage that protects a business's profits from competitors. |
| **Net Interest Margin (NIM)** | The spread a bank earns between interest received on loans/assets and interest paid on deposits/borrowings — the core profitability driver for a depository institution (referenced for context; not itself scored this session). |
| **Quality Score** | This framework's 0.0–100.0 continuous score grading profitability, margins, growth, balance sheet, moat, and FCF quality; a company must score 80.0+ to proceed to Phase 02 valuation scoring. See [quality-scoring.md](../framework/quality-scoring.md). |
| **ROE** | Return on Equity — Net Income ÷ shareholder equity. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit; approximated by ROE for a bank per framework convention. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |
| **XBRL (eXtensible Business Reporting Language)** | A structured, machine-readable data format the SEC requires public companies to tag their financial-statement figures in — lets this framework pull precise line-item figures directly from a company's own filings. |

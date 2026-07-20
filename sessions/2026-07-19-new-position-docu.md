# NEW POSITION — DOCU (DocuSign, Inc., NASDAQ) — 2026-07-19 (trigger) / run 2026-07-20

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Trigger date:** 19 Jul 2026 (Sunday) — **session run:** 20 Jul 2026 (Monday), one day after the paired VRSN evaluation triggered by the same post
**10Y US Treasury Yield:** 4.57% (FRED `DGS10`, most recent posted observation as of 2026-07-16 — recorded for completeness only, since this session stops before the Rate Environment Gate would apply — see §4)
**Current DOCU portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); grep for "DOCU" returns no match)
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/DOCU/` or `watchlist/not-in-portfolio/DOCU/`, confirmed before this session started). **Not to be confused with DOCS (Doximity)** — an unrelated company with an existing, separate watchlist entry.
**Sector:** Software — SaaS agreement/e-signature and contract-lifecycle-management platform
**First-use jargon decode:** see closing Glossary (§8)

---

## 0. Why this session exists — trigger source

A post on **bolshegold** (Telegram, post bolshegold/9795, ~09:46 UTC 2026-07-19), previewing the upcoming earnings-reporting week, named VRSN alongside a comparison to DOCU: *"$VRSN — можно посмотреть на плюс минус итоги $DOCU. Рынок и рост должен быть один и тот же"* ("VRSN — you can look at roughly the same results as DOCU; the market and growth should be similar"). Per the operating brief and this repo's standing convention (see the 2026-07-19 AXP and VRSN precedent sessions), **a first-ever mention of a name with no watchlist entry triggers a full `/new-position` evaluation regardless of the mention's substance.** DOCU has no existing watchlist entry and is not a current holding (confirmed above), so this session is that evaluation, built entirely from independently, primary-sourced data. **The Telegram post's text (including its VRSN comparison) is not used as a financial input anywhere below** — VRSN was evaluated separately, in a different session ([sessions/2026-07-19-new-position-vrsn.md](2026-07-19-new-position-vrsn.md), Quality Score 75.9, FAIL), and is not referenced again in this document except as the reason this session exists.

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("DOCU")`: contract_id **316073742**, exchange **NASDAQ**, description "DOCUSIGN INC" — the correct primary US listing (a MEXI cross-listing and an unrelated FWB (Frankfurt) listing were returned but not used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$52.74** | IBKR `get_price_snapshot`, `last` field, contract_id **316073742** (NASDAQ). `is_close: true` — a completed-session close rather than a live intraday trade at the moment of the fetch, flagged here per Rule 0 discipline rather than treated as a live tick. |
| Bid / Ask | $52.50 (size 265) / $52.68 (size 103) | IBKR `get_price_snapshot` |
| 52-week high / low | $86.65 / $40.16 | IBKR `misc_statistics` |
| 26-week high / low | $58.96 / $40.16 | IBKR `misc_statistics` |
| 13-week high / low | $57.29 / $41.37 | IBKR `misc_statistics` |
| Open 52 weeks ago | $78.24 | IBKR `misc_statistics` |
| Dividend yield | 0.0% (no dividend) | IBKR `get_price_snapshot` |
| `change` / `prior_close` fields | Not returned (empty objects) despite being requested | IBKR `get_price_snapshot` |
| US 10Y Treasury yield | 4.57% | FRED `DGS10`, as-of 2026-07-16 (most recent posted observation) |

**Cross-check:** third-party data provider stockanalysis.com's live snapshot (fetched same session) shows Market Cap $10.07B, Previous Close $53.38, Day's Range $52.16–$54.50 — consistent with (and bracketing) the $52.74 IBKR figure; no material divergence. $52.74 is **-32.6%** below its level 52 weeks ago ($78.24) and **-39.1%** below its 13/26-week high ($86.65 / $58.96) — context only, not scored.

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

Financial figures below are sourced primarily from DocuSign's own SEC filings — the XBRL company-facts API (SEC EDGAR, CIK **0001261333**) for structured financial-statement data, cross-checked against the FY2026 Form 10-K (filed 2026-03-18, covering fiscal year ended Jan 31, 2026) and the Q1 FY2027 earnings release (Exhibit 99.1 to the 8-K filed 2026-06-04, covering the quarter ended Apr 30, 2026). Valuation-context figures (market cap, PE, forward PE, analyst rating) are cross-checked against stockanalysis.com, a third-party vendor, with the exact cross-check shown at point of use. **`yfinance`/Yahoo Finance access failed this session** (`curl_cffi` TLS-fingerprint layer reset by the network proxy) — SEC EDGAR direct-fetch and a plain-`curl`-compatible third-party vendor (stockanalysis.com) were used instead; flagged in §7.

### 2.2 Fiscal year convention (important)

**DocuSign's fiscal year ends January 31, not December 31.** The company's own "FY2026" covers Feb 1, 2025 – Jan 31, 2026 (the 10-K filed 2026-03-18) — i.e., DocuSign's fiscal years run about one calendar year ahead of the number in their label relative to a normal Dec-31 fiscal year company. All "FY20XX" labels below use DocuSign's own convention.

### 2.3 Income statement — primary-sourced (SEC XBRL, cross-checked against the 10-K/8-K exhibits)

| Period | Revenue | Gross Profit | Operating Income | Net Income | Pretax Income | Tax Expense/(Benefit) |
|---|---|---|---|---|---|---|
| FY2023 (Feb'22–Jan'23) | $2,515.9M | $1,979.8M | $(88.0)M | $(97.5)M | $(89.9)M | $7.6M |
| FY2024 (Feb'23–Jan'24) | $2,761.9M | $2,189.3M | $31.6M | $74.0M | $93.7M | $19.7M |
| FY2025 (Feb'24–Jan'25) | $2,976.7M | $2,355.1M | $199.9M | **$1,067.9M** | $247.9M | **$(819.9)M** |
| FY2026 (Feb'25–Jan'26) | $3,219.5M | $2,556.4M | $298.6M | $309.1M | $347.3M | $38.2M |
| Q1 FY2026 (Feb–Apr'25) | $763.7M | $606.4M | $60.3M | $72.1M | $73.8M | $1.7M |
| Q1 FY2027 (Feb–Apr'26) | $830.2M | $659.0M | $111.3M | $78.2M | $117.8M | $39.6M |

**FY2025 GAAP net income is materially distorted by a one-off, non-cash income-tax benefit** — a **$819.9M tax benefit** (`IncomeTaxExpenseBenefit` = −$819,944,000 in the SEC XBRL data) drove net income to $1,067.9M against a pretax income of only $247.9M (an effective tax rate of roughly **−331%**). This is the same pattern this framework's glossary already documents as a "Deferred tax valuation allowance release" (first flagged for DUOL) — a company reverses a prior write-down on deferred tax assets once it judges them likely usable, producing an artificially low (or, as here, negative) effective tax rate and inflated net income in the recognition quarter, not a sign of durably higher profitability. **This session excludes FY2025's distorted quarter (Q2 FY2025, where the reversal was booked) from every TTM calculation below**, using only FY2026 and the two flanking clean quarters (Q1 FY2026, Q1 FY2027) — none of which carry this distortion (their effective tax rates are 2.3%, 11.0%, and 33.6% respectively, all unremarkable).

**TTM (May 2025–Apr 2026), the most recent complete-quarter window, computed as FY2026 − Q1 FY2026 + Q1 FY2027:**
```
TTM Revenue          = 3,219.5 − 763.7 + 830.2  = $3,286.1M
TTM Gross Profit     = 2,556.4 − 606.4 + 659.0  = $2,609.0M   (79.40% gross margin)
TTM Operating Income = 298.6 − 60.3 + 111.3     = $349.6M     (10.64% operating margin)
TTM Net Income       = 309.1 − 72.1 + 78.2      = $315.2M     (9.59% net margin)
TTM Pretax Income    = 347.3 − 73.8 + 117.8     = $391.3M
TTM Tax Expense      = 38.2 − 1.7 + 39.6        = $76.1M      (19.45% blended effective tax rate — clean, unremarkable)
```
**Cross-check:** stockanalysis.com independently reports DOCU's TTM net income as **$315.20M** — an exact match to this session's own TTM computation, corroborating that excluding the distorted quarter is the correct (and apparently standard-vendor-consistent) treatment. Their TTM revenue ($3.29B) and EPS ($1.54) likewise match.

### 2.4 Cash flow — primary-sourced (SEC XBRL)

DocuSign's cash-flow statement reports two distinct capex-like outflows: **purchases of property and equipment** (`PaymentsToAcquirePropertyPlantAndEquipment`) and **capitalized internal-use software costs** (`CapitalizedComputerSoftwareAdditions`, a separate line for a SaaS company that capitalizes software development). This session combines both into "CapEx," consistent with this framework's treatment of the same two-line capex structure for Mastercard in the 2026-06-14 MA session ("CapEx (PP&E + capitalized software)").

| Fiscal Year | OCF | PP&E CapEx | Capitalized Software | Total CapEx | FCF (OCF−CapEx) | Net Income | FCF/NI |
|---|---|---|---|---|---|---|---|
| FY2024 | $979.5M | $92.4M | $95.3M | $187.7M | $791.8M | $74.0M | 1,070.3% |
| FY2025 | $1,017.3M | $97.0M | $114.7M | $211.7M | $805.6M | $1,067.9M | 75.4%* |
| FY2026 | $1,165.0M | $106.4M | $143.4M | $249.8M | $915.2M | $309.1M | 296.1% |

*FY2025's ratio is arithmetically >70% but not a meaningful cash-quality read given the distorted (artificially inflated) net-income denominator (§2.3) — noted for completeness, not relied upon.

**TTM (same rollforward method):**
```
TTM OCF                = 1,165.0 − 251.4 + 321.7 = $1,235.3M
TTM PP&E CapEx         = 106.4 − 23.6 + 32.3      = $115.1M
TTM Capitalized SW     = 143.4 − 29.7 + 44.8       = $158.5M
TTM Total CapEx        = 115.1 + 158.5             = $273.6M
TTM FCF                = 1,235.3 − 273.6           = $961.7M
TTM FCF/NI             = 961.7 / 315.2             = 305.1%
```
**Cross-check against DocuSign's own non-GAAP "Free Cash Flow" figure:** the company's Q1 FY2027 earnings release states "Free cash flow was $289.4 million" for that quarter — this matches $321.7M (OCF) − $32.3M (**PP&E CapEx only**, i.e. **excluding** capitalized software) = $289.4M exactly. This session deliberately uses the stricter, capitalized-software-inclusive CapEx definition (per the MA precedent) rather than the company's own narrower non-GAAP figure, since capitalized software is a real cash outflow funding ongoing product development — consistent with this framework's general skepticism toward company-defined non-GAAP metrics (see glossary entries on "Adjusted EBITDA," "Core," "AOI").

**FCF positive every year shown (and in FY2022/FY2023, both GAAP-loss years — FCF was $406.1M and $363.0M respectively, still solidly positive)** — comfortably clears the "FCF-positive 3+ consecutive years" hard disqualifier check with a longer track record than the 3-year minimum.

**Depreciation & Amortization (for TTM EBITDA):**
```
TTM D&A = 116.1 − 30.4 + 32.2 = $117.9M
TTM EBITDA = TTM Operating Income ($349.6M) + TTM D&A ($117.9M) = $467.6M
```

### 2.5 Balance sheet — primary-sourced (most recent 10-Q, quarter ended Apr 30, 2026)

| Item | Jan 31, 2026 (FY2026 year-end) | Apr 30, 2026 (Q1 FY2027, most recent) |
|---|---|---|
| Cash and cash equivalents | $602.4M | $548.0M |
| Short/long-term available-for-sale debt securities (investments) | $472.5M | $476.0M |
| Total debt (convertible notes or other) | **$0** | **$0** |
| Total stockholders' equity | $1,917.8M | $1,819.7M |
| Total assets | $4,229.6M | $3,984.0M |
| Total liabilities | $2,311.7M | $2,164.3M |
| Shares outstanding | 197,765,000 | 193,057,000 |

**DocuSign carries zero total debt.** Its convertible senior notes (last carried at $722.9M current + prior noncurrent balances through FY2023) were **fully repaid by FY2024** — `ConvertibleDebtCurrent` and `ConvertibleDebtNoncurrent` both show $0 at every balance-sheet date from Jan 31, 2024 onward, with no new issuance since (`ProceedsFromConvertibleDebt` = $0 every year FY2022–FY2026). This is a genuinely debt-free balance sheet, not a data gap.

**Cash convention used in this session:** for Net Debt/EBITDA and Invested Capital, this session uses only **Cash and Cash Equivalents** ($548.0M at Apr 30, 2026) — **not** the additional $476.0M of short/long-term available-for-sale investment securities — to match this framework's own glossary definition of Invested Capital ("debt + equity − cash," without reference to investments). This is the more conservative choice (it does not net out DocuSign's additional ~$476M of liquid securities), and is flagged explicitly since it affects the Profitability sub-score — see the sensitivity check in §3.9.

**Net Debt/EBITDA (Apr 30, 2026):**
```
Net Debt = Total Debt ($0) − Cash ($548.0M) = −$548.0M   (net cash position)
Net Debt/EBITDA = −548.0 / 467.6 (TTM EBITDA) = −1.17×
```

### 2.6 Growth / moat evidence — primary-sourced (10-K, Q1 FY2027 earnings release)

- **Customer base growing:** "As of January 31, 2026, over 1.8 million customers and more than a billion users worldwide utilize Docusign" — up from "nearly 1.7 million customers" a year earlier (Jan 31, 2025), per the FY2026 10-K. Direct enterprise/commercial customers grew from ~260,000 to ~280,000 over the same period; customers with >$300,000 in annualized contract value grew from 1,131 to 1,205.
- **IAM (Intelligent Agreement Management) platform — a genuine new, adjacent TAM, not just guidance:** the 10-K states "more than 25,000 customers are on IAM today" (as of Jan 31, 2026). The Q1 FY2027 earnings release (June 2026) states IAM grew to **40,000 customers** and now represents **12.6% of total ARR**, up from **10.8% of total ARR just one quarter earlier** (Jan 31, 2026) — a documented, actual (not guided) acceleration of a new product line expanding DocuSign's addressable market beyond core e-signature into broader agreement/contract-lifecycle management, with new AI-native ("Iris" agent) capabilities announced May 2026.
- **Primary competitor named directly by the company:** the 10-K states "Our primary global competitor for eSignature is currently Adobe" (Adobe Acrobat Sign) — describing an effective two-player structure at the high end of the market, alongside smaller vendors focused on specific verticals/geographies.
- **Free/limited-tier distribution mechanism (documented, not "network effect" in name but in substance):** the 10-K states DocuSign offers "certain limited-time or feature-constrained versions of our e-signature solution for free... to drive customer reach and adoption" — consistent with the >1 billion "users" vs. 1.8 million paying "customers" gap (roughly 500-600 non-paying recipients/users per paying customer), i.e. each paying customer's outbound signature requests expose a much larger number of external counterparties to the product, some of whom convert.
- **Switching-cost mechanism:** "more than 1,100 active partner integrations" (Salesforce, SAP, Microsoft Dynamics 365, HubSpot, Coupa, Slack, per the Q1 FY2027 release) plus a "single repository" of an organization's signed agreements — replacing DocuSign means re-integrating across all of these systems and migrating a large historical document/audit-trail archive.
- **No citable pricing-power/ASP evidence found** — unlike VeriSign's contractually-set, publicly disclosed .com price increases, no specific DocuSign price-increase or per-seat ASP data was found in the 10-K or earnings release this session.
- **No citable scale-cost-advantage evidence found** — no cost-per-transaction/cost-per-envelope figure benchmarked against a named smaller competitor was found this session.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years without a growth-capex explanation | FY2025 75.4% / FY2026 296.1% (the two most recent positive-net-income years) — **both comfortably above 70%**; FY2022/FY2023 FCF was solidly positive ($406.1M/$363.0M) despite GAAP losses | disqualify if 2+ consecutive years sub-70% | ✅ **PASS**, clean |
| Net Debt/EBITDA over threshold | **−1.17×** (net cash — §2.5) | disqualify if >2.5× (standard) or >4× (asset-light override) | ✅ **PASS**, clean — DocuSign carries zero debt |
| FCF-positive 3+ consecutive years | Positive every year FY2022–FY2026 (5 consecutive years, including 2 GAAP-loss years) | disqualify if not | ✅ **PASS**, clean |

**No hard disqualifier fires.**

### 3.2 Profitability (25% weight)

```
Net Margin (TTM) = 315.2 / 3,286.1 = 9.59%
NetMargin_Component = clamp((9.59/30)×100, 0, 100) = 31.97
```

**ROIC:**
```
Invested Capital (Apr 30, 2026) = Total Debt ($0) + Equity ($1,819.7M) − Cash ($548.0M) = $1,271.7M
Effective tax rate (TTM, blended) = TTM Tax ($76.1M) / TTM Pretax ($391.3M) = 19.45%
NOPAT (TTM) = TTM Operating Income ($349.6M) × (1 − 0.1945) = $281.6M
ROIC = NOPAT / Invested Capital = 281.6 / 1,271.7 = 22.15%
ROIC_Component = clamp((22.15/30)×100, 0, 100) = 73.83
```

```
Profitability_Score = (31.97 + 73.83) / 2 = 52.90   (no FCF-positivity cap — clean multi-year positive FCF, §3.1)
```

### 3.3 Margins (15% weight)

```
TTM Gross Margin = 2,609.0 / 3,286.1 = 79.40%
GrossMargin_Score = clamp((79.40/80)×100, 0, 100) = 99.25
```
Gross margin has been essentially flat (79.27% FY2024 → 79.11% FY2025 → 79.40% FY2026) — already far above the 40% threshold the structural-trend bonus is gated on, so no bonus applies (moot — already near the 100.0 ceiling).

### 3.4 Growth (20% weight)

```
Revenue 3yr CAGR (FY2023 $2,515.9M → FY2026 $3,219.5M) = (3,219.5/2,515.9)^(1/3) − 1 = 8.57%
Growth_Score (raw) = clamp((8.57/25)×100, 0, 100) = 34.28
```
**TAM/pricing-power modifier (+10):** documented, *actual* (not guidance) evidence — the IAM platform's ARR share rose from 10.8% (Jan 31, 2026) to 12.6% (Apr 30, 2026) in a single quarter, with IAM's customer count growing from >25,000 to 40,000 over the same window (§2.6) — a genuinely new, expanding product category (contract-lifecycle/agreement-AI management, not just e-signature), evidenced by completed, reported results rather than forward guidance.
```
Growth_Score = 34.28 + 10 = 44.28
```
**No deceleration modifier:** YoY revenue growth ran 19.40% (FY22→23) → 9.78% (FY23→24) → 7.78% (FY24→25) → 8.16% (FY25→26) → 8.72% (Q1 FY27 vs Q1 FY26) — a sharp deceleration that **completed** by FY2024/FY2025, followed by three consecutive periods of stable-to-modestly-**re-accelerating** growth (7.78%→8.16%→8.72%). Consistent with this framework's treatment of the same pattern in the 2026-07-19 VRSN session, this reads as a completed, historical deceleration rather than an ongoing structural one, so the −10 modifier does not apply.

### 3.5 Balance Sheet (15% weight)

```
Net Debt/EBITDA = −1.17×   (§2.5 — net cash position, zero debt)
BalanceSheet_Score = clamp(100 × (1 − (−1.17)/4), 0, 100) = clamp(129.3, 0, 100) = 100.0
```

### 3.6 Moat Signal (15% weight)

| Signal | Evidence | Result |
|---|---|---|
| Market share stable/growing | Total customers grew 1.7M→1.8M (Jan'25→Jan'26); direct enterprise/commercial customers 260K→280K; company's own 10-K names only one "primary global competitor" (Adobe Acrobat Sign) for eSignature | ✅ TRUE |
| Brand premium (pricing power) | No specific price-increase or per-seat ASP evidence found in the 10-K or recent earnings release | ❌ not established |
| Network effect | Documented mechanism: free/feature-limited tier explicitly offered "to drive customer reach and adoption" (10-K); >1 billion users vs. 1.8 million paying customers — each paying customer's outbound signature requests expose a much larger pool of non-paying counterparties, some of whom convert | ✅ TRUE |
| Switching costs | 1,100+ active partner integrations (Salesforce, SAP, Microsoft Dynamics 365, HubSpot, Coupa, Slack) plus a "single repository" of an organization's historical signed agreements/audit trail | ✅ TRUE |
| Scale cost advantage | No cost-per-transaction/cost-per-envelope figure benchmarked against a named smaller competitor found this session | ❌ not established |

```
Moat_Score = (3/5) × 100 = 60.0
```

### 3.7 FCF Quality (10% weight)

```
TTM FCF/NI = 961.7 / 315.2 = 305.1%
FCFQuality_Score = clamp(((3.051 − 0.40)/0.60)×100, 0, 100) = clamp(441.8, 0, 100) = 100.0
```

### 3.8 Quality Score — final calculation

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

              = (52.90 × 0.25) + (99.25 × 0.15) + (44.28 × 0.20)
              + (100.0 × 0.15) + (60.0 × 0.15) + (100.0 × 0.10)

              = 13.225 + 14.8875 + 8.856 + 15.00 + 9.00 + 10.00

              = 70.97  →  rounds to 71.0
```

### 3.9 Gate result: **FAIL — 71.0 < 80.0**

**Sensitivity check #1 (Moat Signal judgment calls):** even generously crediting **both** withheld signals (5-of-5, Moat_Score = 100.0), the Quality Score would be `70.97 − 9.00 + 15.00 = 76.97` → **77.0 — still below 80.0.** Crediting only Brand Premium (4-of-5, Moat_Score = 80.0) gives 74.0. In no plausible reading of the Moat checklist does DOCU clear the gate on Moat evidence alone.

**Sensitivity check #2 (cash definition for Invested Capital):** using the broader "cash + short/long-term investments" figure ($1,024.1M instead of $548.0M cash alone — see §2.5) instead of this session's chosen narrow definition would raise Invested Capital's denominator down to $795.7M, pushing ROIC to 35.4% (clamped ROIC_Component to 100.0, Profitability_Score to 65.99) — Quality Score would rise to `70.97 + (65.99-52.90)×0.25 = 74.24` → still below 80.0 on its own. **Only stacking both generous assumptions simultaneously** (broader cash definition *and* full 5-of-5 Moat credit) reaches 80.24 — just barely over the gate. This session does not adopt either generous assumption: the broader cash definition departs from this framework's own glossary wording, and neither withheld Moat signal (Brand Premium, Scale Cost Advantage) has a citable evidentiary source found this session. **Under the evidence actually gathered, the FAIL is not a knife-edge case** — it sits 9 points below the gate under the primary (conservative, evidence-grounded) methodology, and even the single most generous defensible reading (Moat 5-of-5 alone) still falls 3 points short.

**This session stops here per the command specification: no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.** DocuSign does not clear the 80.0+ Quality Score gate.

---

## 4. Why this reads as a genuine (if narrower-margin) miss, not a framework gap

Three of six sub-scores are strong for DocuSign — Margins 99.25 (79.4% gross margin, a genuine software-economics business), Balance Sheet 100.0 (zero debt, net cash position), and FCF Quality 100.0 (FCF running 3-11× GAAP net income, since heavy non-cash stock-based compensation depresses GAAP earnings far more than it depresses cash generation) — and no hard disqualifier fires. The shortfall is concentrated in two places: **Profitability (52.90/100, 25% weight)** — a genuinely thin 9.59% TTM net margin (heavy SBC and D&A load against revenue, notwithstanding a healthy underlying 22.15% ROIC on DocuSign's now debt-free, asset-light balance sheet) — and **Growth (44.28/100, 20% weight)** — high-single-digit revenue growth (8.57% 3yr CAGR) reflecting a business whose steep post-IPO deceleration (19.4% → high-single-digits) completed several years ago and has since plateaued, with the IAM platform's rapid early adoption (10.8%→12.6% of ARR in one quarter) not yet large enough in absolute revenue terms to move the trailing 3-year blended CAGR much. This is a legitimate, evidence-grounded application of a strict, deliberately conservative gate to a real, profitable, debt-free business that simply isn't compounding fast enough (nor generating a high enough GAAP-margin base) to clear this framework's 80.0+ bar — not a structural framework limitation requiring a fix.

---

## 5. Recommendation: **PASS (no entry) — Quality Gate FAIL at 71.0 (need 80.0+)**

**Do not enter DOCU this session.** The Quality Score of 71.0 is 9 points below the strict 80.0+ gate, and — per the sensitivity checks in §3.9 — the shortfall survives every individually-defensible generous reading of the contestable inputs (Moat Signal credit, Invested Capital's cash definition); only stacking both simultaneously (neither independently supported by evidence found this session) would flip the result, and barely. **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed**, consistent with the command specification's instruction to stop at the Quality Gate.

The triggering Telegram post (a routine "similar results to DOCU" comparison relative to VRSN, offered with no specific claims about DOCU's own fundamentals) was used only as the reason to run this first-ever evaluation and was not relied upon for any figure or conclusion above.

---

## 6. Next Review Trigger

No routine re-check is scheduled on a numeric-score basis in the sense of a Phase 02 valuation score (none exists), but this framework does track quality-gate misses for re-evaluation on:
- **DOCU's next earnings release** (Q2 FY2027, covering the quarter ended Jul 31, 2026, expected per the company's usual ~5-week-after-quarter-end cadence in early September 2026 — stockanalysis.com's tracked consensus date is Sep 3, 2026) — a fresh TTM window could modestly move the Growth and Profitability sub-scores, particularly if IAM's ARR share continues compounding at its recent quarterly pace.
- A **documented change** to the Growth or Moat sub-score inputs — e.g. a specific, citable price-increase/ASP data point (Brand Premium) or a cost-per-transaction benchmark against a named competitor (Scale Cost Advantage), either of which would need independent sourcing before being credited.
- The standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move (DOCU is already down ~39% from its 13/26-week high, but per Rule 9 that alone is not a valid re-scoring trigger absent an identified fundamental cause — flagged as context only, not acted upon).

Absent any of the above, a future Telegram mention of DOCU should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Data Gaps Flagged

1. **`yfinance`/Yahoo Finance access failed this session** — the `curl_cffi` TLS-fingerprinting HTTP client `yfinance` depends on was reset by the network's egress proxy (`curl: (35) Recv failure: Connection reset by peer`), even after retries. Worked around by pulling primary-sourced XBRL data directly from SEC EDGAR's company-facts API (a more authoritative source than `yfinance` in any case) and cross-checking against stockanalysis.com (plain HTTPS, unaffected). No financial input was left unsourced as a result — this is a tooling note, not a data gap in the scored inputs.
2. **Cash definition choice for Invested Capital / Net Debt (§2.5, §3.9):** this session used "Cash and Cash Equivalents" only ($548.0M), excluding ~$476.0M of short/long-term available-for-sale investment securities, to match this framework's glossary wording literally. The Quality Score would be modestly higher (74.2 instead of 71.0) under the broader definition — still below the gate either way, but flagged as a methodology choice rather than a resolved ambiguity, in case a future session adopts the broader convention for consistency across tickers.
3. **Brand Premium and Scale Cost Advantage Moat Signals were not credited for lack of a citable, specific source** (§2.6, §3.6) — DocuSign may well have pricing power or scale cost advantages in practice, but no price-increase/ASP data or cost-per-transaction benchmark was found in the FY2026 10-K or the Q1 FY2027 earnings release this session. A future session with access to a DocuSign-specific analyst report or a per-envelope cost disclosure could revisit these two signals.
4. **Shares outstanding used (193,057,000, from the Apr 30, 2026 10-Q)** is the most recent *filed* figure — DocuSign disclosed "record share buybacks" of $317.5M in Q1 FY2027 alone and has an active, ongoing repurchase program, so the true current share count as of this session's run date is almost certainly somewhat lower (stockanalysis.com's own live figure shows 190.94M). Not used in any scored Quality Score input (share count only matters for the Phase 02 valuation score, not reached this session) — noted for completeness since it was gathered.

None of these gaps is silently patched around — each is the explicit reason for a flagged caveat rather than an invented number, and §3.9's sensitivity checks show none of them are actually outcome-determinative for the gate result.

---

## 8. Glossary

| Term | Meaning |
|---|---|
| **ACV (Annual Contract Value)** | Full entry in [glossary.md](../framework/glossary.md). DocuSign's count of customers with >$300,000 ACV grew from 1,131 to 1,205 year-over-year (§2.6) — cited as Market Share Moat Signal evidence. |
| **ARR (Annual Recurring Revenue)** | Full entry in [glossary.md](../framework/glossary.md). DocuSign's IAM platform grew from 10.8% to 12.6% of total ARR in a single quarter (§2.6, §3.4) — the primary evidence behind this session's Growth sub-score TAM-expansion modifier. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CIK (Central Index Key)** | Full entry in [glossary.md](../framework/glossary.md). DocuSign's SEC EDGAR identifier, 0001261333, used to pull this session's primary-sourced financial data (§2.1). |
| **Deferred tax valuation allowance release** | Full entry in [glossary.md](../framework/glossary.md). The reason this session excludes FY2025's Q2 quarter (an $819.9M one-off tax benefit) from every TTM figure — the same pattern first documented for DUOL (§2.3). |
| **Convertible senior notes** | Full entry in [glossary.md](../framework/glossary.md). DocuSign's convertible notes were fully repaid by FY2024 and not reissued — the reason its Balance Sheet sub-score reflects zero total debt (§2.5). |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization — operating-profit measures, both directly computable from DocuSign's clean GAAP income statement (§2.3, §2.4). |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check). DocuSign's FCF/NI ratio ran 296–1,070% across FY2024–FY2026 (excluding the distorted FY2025 figure), reflecting heavy non-cash stock-based-compensation add-backs depressing GAAP earnings far more than cash flow (§2.4, §3.7). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. None fired for DOCU this session (§3.1). |
| **IAM (Intelligent Agreement Management)** | DocuSign's newer platform expanding beyond core e-signature into broader AI-driven contract-lifecycle/agreement management — the source of this session's documented TAM-expansion evidence (§2.6, §3.4). *(New term.)* |
| **Invested Capital** | Full entry in [glossary.md](../framework/glossary.md). This session computed DocuSign's Invested Capital as $1,271.7M (debt $0 + equity $1,819.7M − cash $548.0M) — see the cash-definition sensitivity discussion in §3.9. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — DocuSign's ratio is **−1.17×** (a net cash position, zero debt), comfortably under both the 2.5× standard and 4× asset-light thresholds (§2.5, §3.5). |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. DOCU scored 71.0 this session — a FAIL that survives every individually-defensible sensitivity check (§3.8–3.9). |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit. DocuSign's ROIC (22.15% TTM) is comfortably healthy despite thin GAAP margins, reflecting its capital-light, debt-free balance sheet (§3.2). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input. |
| **Rule 6** | This framework's instruction to normalize earnings/margins/revenue before valuing a business — the basis for excluding FY2025's distorted tax-benefit quarter from this session's TTM figures (§2.3). |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro/rate shifts, or a >15% unexplained price move. |
| **SBC (Stock-Based Compensation)** | Full entry in [glossary.md](../framework/glossary.md). Non-cash compensation expense that reduces GAAP net income without reducing cash flow — the primary reason DocuSign's FCF/NI ratio runs so far above 100% (§2.4, §3.7, §4). |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — this session used May 2025–Apr 2026 (FY2026 minus Q1 FY2026 plus Q1 FY2027), the most recent complete window available, deliberately excluding the FY2025 quarter carrying the one-off tax-benefit distortion (§2.3). |
| **XBRL (eXtensible Business Reporting Language)** | Full entry in [glossary.md](../framework/glossary.md). The structured, machine-readable SEC data format this session used to pull DocuSign's exact reported figures directly from SEC EDGAR's company-facts API (§2.1). |

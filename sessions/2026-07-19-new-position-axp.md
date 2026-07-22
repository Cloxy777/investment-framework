# NEW POSITION — AXP (American Express Company, NYSE) — 2026-07-19

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 19 Jul 2026 (Sunday)
**10Y US Treasury Yield:** 4.57% (FRED `DGS10`, most recent posted observation dated 2026-07-16 — 07-17/07-18 not yet posted, normal FRED reporting lag; recorded for completeness only, since this session stops before the Rate Environment Gate would apply — see §4)
**Current AXP portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); grep for "AXP" returns no match)
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/AXP/` or `watchlist/not-in-portfolio/AXP/`, confirmed via `find`)
**Sector:** Financials — Consumer/commercial payments and lending (closed-loop card network, issuer, and merchant acquirer; also a bank holding company since 2008)
**First-use jargon decode:** see closing Glossary (§8)

---

## 0. Why this session exists — trigger source

A post on **bolshegold** (Telegram, post bolshegold/9795, ~09:46 UTC 2026-07-19) listed AXP among several tickers "reporting earnings this week," with commentary that it's a "financial/credit-card indicator for overall market health," with "no specific expectations beyond a generally positive-quarter signal." Per the operating brief and this repo's standing convention (see the CAKE and RYAAY precedent rows in `portfolio/snapshots/telegram-watch.md`), **a first-ever mention of a name with no watchlist entry triggers a full `/new-position` evaluation regardless of the mention's substance.** AXP has no existing watchlist entry and is not a current holding (confirmed above), so this session is that evaluation, built entirely from independently, primary-sourced data. **The Telegram post's text is not used as a financial input anywhere below.**

Independently confirmed via SEC EDGAR (AXP's own 8-K filing history, CIK 0000004962): AXP's most recent earnings 8-K (with Item 2.02, "Results of Operations") was filed 2026-04-23 for Q1 2026. No Q2 2026 earnings 8-K has been filed as of this session (2026-07-19) — the most recent 8-K (2026-07-15) carries only Item 7.01 (Reg FD disclosure), not results. A third-party earnings-calendar aggregator (MarketBeat) lists AXP's Q2 2026 report date as **2026-07-24** (this coming Friday) — consistent with the Telegram post's "reporting this week" framing. **Q2 2026 results are not yet available and are not used anywhere in this session.**

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("AXP")`: contract_id **4721**, exchange **NYSE**, description "AMERICAN EXPRESS CO" — the correct primary US listing (other results returned were the MEXI cross-listing, an unrelated Australian energy company also ticker "AXP," a Toronto CDR, and a leveraged single-stock ETF "AXPG" — none used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$361.57** | IBKR `get_price_snapshot`, `last` field, contract_id **4721** (NYSE). `is_close: true` — this is the last completed-session close, not a live intraday trade, because today (Sunday 2026-07-19) markets are closed; per Rule 0 this is still the most recent price obtainable via a live fetch attempt, flagged here as a close rather than an intraday quote (same situation as the 2026-07-19 RYAAY session). |
| 52-week high | $385.30 | IBKR `misc_statistics` `high_52w` |
| 52-week low | $286.19 | IBKR `misc_statistics` `low_52w` |
| 13-week high | $363.13 | IBKR `misc_statistics` `high_13w` |
| 26-week high | $368.91 | IBKR `misc_statistics` `high_26w` |
| Open 52 weeks ago | $308.11 | IBKR `misc_statistics` `open_52w` |
| Dividend yield | 0.98% | IBKR `get_price_snapshot` `dividend_yield` field |
| US 10Y Treasury yield | 4.57% | FRED `DGS10`, as-of 2026-07-16 |

$361.57 sits in the upper half of its 52-week range ($286.19–$385.30), up **+17.4%** from the level 52 weeks ago ($308.11) — context only, not scored. No order-setup arithmetic is performed this session (see §4 for why).

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

`yfinance` failed in this session's environment with the same `curl_cffi` TLS/connection-reset error documented in the 2026-07-12 Citigroup (C) and 2026-07-14 JPMorgan (JPM) sessions. **Fallback used:** SEC EDGAR full-text search and the SEC XBRL `companyconcept` API (`data.sec.gov/api/xbrl/companyconcept/CIK0000004962/...`) for primary-sourced, audited/reported figures; AXP's own 8-K earnings-release exhibits (via SEC EDGAR and AXP's investor-relations CDN); and stockanalysis.com (WebFetch) for cross-checking, with every stockanalysis.com figure independently verified against the SEC XBRL API before being relied upon (see §2.2 for the verification results). AXP's CIK is **4962**.

**Important data-quality finding:** stockanalysis.com's income-statement page reports a "Revenue $54,865M" / negative "Operating Income (EBIT) −$3,569M" for FY2025 that **do not match AXP's own reported figures** (AXP's own FY2025 8-K states "Total revenues net of interest expense" of $72.2B and net income of $10.8B — positive, not negative, operating profitability). This is the same class of vendor artifact documented in the JPM/C/SOFI sessions: forcing a financial company's income statement into a non-financial "Cost of Revenue → Gross Profit → EBIT" template that doesn't exist in AXP's own filings. **This session uses only AXP's own primary-sourced figures (10-K, 8-K earnings exhibits, SEC XBRL) for every scored input, never the stockanalysis.com "Revenue"/"EBIT" lines.** stockanalysis.com's balance-sheet and cash-flow figures, by contrast, **were** independently verified against SEC XBRL and matched exactly (§2.2) — those are used.

### 2.2 Cash flow — primary-sourced, cross-verified

| Fiscal Year | Net cash from operating activities | CapEx (PP&E purchases) | FCF | Net Income | FCF/NI |
|---|---|---|---|---|---|
| FY2021 | $14,645M | $1,550M | $13,095M | $8,060M | 162.47% |
| FY2022 | $21,079M | $1,855M | $19,224M | $7,514M | 255.89% |
| FY2023 | $18,559M | $1,563M | $16,996M | $8,374M | 202.97% |
| FY2024 | $14,050M | $1,911M | $12,139M | $10,129M | 119.85% |
| FY2025 | $18,428M | $2,425M | $16,003M | $10,833M | 147.71% |

Operating cash flow and Net Income both independently verified against SEC XBRL `companyconcept` (`us-gaap:NetCashProvidedByUsedInOperatingActivities`, `us-gaap:NetIncomeLoss`) — exact match to stockanalysis.com for all 5 years. CapEx cross-verified against XBRL `us-gaap:PaymentsToAcquirePropertyPlantAndEquipment` for FY2021–FY2024 (exact match); FY2025 capex sourced from stockanalysis.com only (not yet reflected under this XBRL tag at session time) but the resulting FY2025 FCF ($16,003M) is internally consistent with AXP's own 8-K-stated net income and OCF, so accepted.

**Company is FCF-positive in all 5 years shown, and FCF/NI exceeds 70% in every year** — clears both cash-flow-related hard disqualifiers with a wide margin. This is a materially different result from the JPM/Citigroup/SOFI bank sessions (all of which failed on negative multi-year FCF driven by trading-book/loan-portfolio balance changes classified within operating cash flow) — AXP's Card Member receivables/loans, while still a lending book, evidently don't create the same operating-cash-flow drag, likely reflecting their shorter average duration versus a money-center bank's trading and wholesale-lending book.

### 2.3 Income statement — primary-sourced (AXP's own 8-K earnings releases)

| Period | Total revenues net of interest expense | Net Income | Diluted EPS |
|---|---|---|---|
| FY2022 | $52.9B | $7,514M | $9.85 |
| FY2023 | $60.5B | $8,374M | $11.21 |
| FY2024 | $65.9B | $10,129M | $14.01 |
| FY2025 | $72.2B | $10,833M | $15.38 |
| Q1 2025 | $16,967M | $2,584M | $3.64 |
| Q1 2026 | $18,907M | $2,971M | $4.28 |

Sources: FY2022–FY2025 figures from AXP's own full-year earnings press releases (via WebSearch, cross-checked against multiple independent reports of the same AXP-issued figures); Q1 2025/Q1 2026 from the Q1 2026 earnings 8-K exhibit (SEC accession 0000004962-26-000188, `q126exhibit991.htm`). Net income figures cross-verified exactly against SEC XBRL `us-gaap:NetIncomeLoss` (§2.2). **"Total revenues net of interest expense" is AXP's own headline revenue metric** (interest income from Card Member loans plus non-interest/fee revenue, net of interest expense paid on deposits/borrowings) — there is no separate, distinguishable "interest expense" line to add back to reach a traditional EBIT, since AXP nets it directly into revenue (see §3.2/§3.4 for why this blocks a clean Margins/Balance-Sheet computation).

**No GAAP EBIT/EBITDA line and no GAAP Cost-of-Revenue/Gross-Profit line exist in AXP's own income statement** — same structural gap as JPM, Citigroup, and SOFI (all money-center/neobank sessions), now observed a **fourth time**, on a hybrid closed-loop issuer/network/lender rather than a pure bank.

**TTM (Apr 2025–Mar 2026), the most recent complete-quarter window available** (Q2 2026 not yet reported — §0):
```
TTM Revenue    = FY2025 ($72.2B) − Q1 2025 ($16,967M) + Q1 2026 ($18,907M) ≈ $74,140M
TTM Net Income = FY2025 ($10,833M) − Q1 2025 ($2,584M) + Q1 2026 ($2,971M) = $11,220M
```

### 2.4 Balance sheet — primary-sourced (SEC XBRL, cross-verified against stockanalysis.com)

| Item | Q1 2025 | FY2024 | FY2025 | Q1 2026 |
|---|---|---|---|---|
| Short-term borrowings | $1,559M | $1,374M | $1,371M | $1,692M |
| Long-term debt | $51,236M | $49,715M | $56,387M | $58,750M |
| **Total debt** | **$52,795M** | **$51,089M** | **$57,758M** | **$60,442M** |
| Deposits | — | $139,413M | $152,488M | $157,948M |
| Total shareholders' equity | $31,202M | $30,264M | $33,474M | $33,995M |
| Total assets (FY25, per 10-K excerpt) | — | — | $300.1B | — |
| Card Member loans (net of reserves) | — | — | $145,923M | — |

All figures sourced directly from SEC XBRL `companyconcept` (`us-gaap:ShortTermBorrowings`, `us-gaap:LongTermDebt`, `us-gaap:Deposits`, `us-gaap:StockholdersEquity`); total debt figures cross-verified exactly against stockanalysis.com's "Total Debt" line for FY2024 ($51.1B) and FY2025 ($57.8B) — confirming stockanalysis.com's *balance-sheet* data (unlike its income-statement construction, §2.1) is reliable for AXP.

**CET1 (Common Equity Tier 1) capital ratio** (bank-regulatory context only, not a scored input): **10.5%** at Dec 31, 2025, against an effective regulatory minimum of **7.0%** — a real but noticeably thinner cushion than JPMorgan's 14.1–14.3% (2026-07-14 JPM session) or Citigroup's 12.7–13.2% (2026-07-12 C session). Cited for completeness; not substitutable into the Net Debt/EBITDA formula (§3.4).

### 2.5 Growth / moat evidence — primary and third-party sourced

- **Billed business:** AXP's own FY2025 10-K states worldwide billed business of **$1,670 billion** for FY2025; billed business grew **+8% YoY** (7% FX-adjusted) in Q1 2026 per the Q1 2026 earnings release — an *actual, reported* result, not guidance.
- **Card Member services expense** rose **27% YoY** in FY2025 (per AXP's own Q4/FY2025 earnings release), explicitly attributed by the company to "growth in premium card accounts and higher usage of travel-related benefits" — actual, reported evidence of premium-segment growth, not a forward projection.
- **Platinum Card annual fee** raised from $695 to $895 (+29%) in September 2025 — the card's first fee increase in four years, following a prior 2021 hike from $550 to $695 — reported by multiple independent sources (Axios, CNBC, The Motley Fool, The Points Guy). AXP's own Q1 2026 results (the first full quarter after the hike) show continued YoY growth in Card Member fee income and record billed business, evidence the fee increase has not visibly cost AXP volume.
- **Market share (Nilson Report, third-party, non-company-sourced):** AXP holds **$1.7 trillion** in global purchase volume (**~9%** of global-brand card purchase volume) and **141 million** cards in circulation (**~4%** of global credit cards). AXP's own Q1 2026 billed-business growth (+8% YoY) outpaced overall US card-network purchase-volume growth (+5.9% YoY, Q1 2025, per Nilson Report's US card-network data) — directional evidence of share gain, not just market growth.
- **Closed-loop network structure:** AXP's own 10-K describes the company as the "issuer, network, and a merchant acquirer... under one roof," with direct relationships with both Card Members and merchants in ~110 countries/territories — a documented, primary-sourced structural mechanism (§8 Glossary).
- **Membership Rewards:** AXP's proprietary points/status loyalty program (§8 Glossary) — well-documented switching-cost mechanism.
- **No cost-per-unit citation vs. smaller card issuers was found this session** — Scale Cost Advantage is not credited (§3.3).

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years without a growth-capex explanation | 162.5% / 255.9% / 203.0% / 119.9% / 147.7% (FY2021–FY2025) — **every year comfortably above 70%** | disqualify if 2+ consecutive years sub-70% | ✅ **PASS**, clean |
| Net Debt/EBITDA over threshold | **Not computable — no EBITDA line exists** (§3.4) | disqualify if >2.5× (or >4× asset-light) | **N/A — cannot fire** (same treatment as JPM/C/SOFI: genuinely not computable, not defaulted to pass or fail) |
| FCF-positive 3+ consecutive years | All 5 of the last 5 fiscal years positive | disqualify if not | ✅ **PASS**, clean |

**No hard disqualifier fires.** This is a materially different starting point than the JPM (2026-07-14), Citigroup (2026-07-12), and SOFI (2026-06-21) sessions, all of which failed on the FCF-based disqualifiers before the weighted score even mattered. AXP's cash-flow profile does not have that problem — so, unlike those three sessions, **the weighted Quality Score genuinely determines the gate outcome here**, and the N/M sub-scores below cannot be waved away as moot.

### 3.2 Quality Score — computable components

**PROFITABILITY (25% weight):**
```
Net Margin (TTM) = 11,220 / 74,140 = 15.14%
NetMargin_Component = clamp((15.14/30)×100, 0, 100) = 50.47

ROE used as ROIC proxy (per the JPM/C/SOFI-session convention — ROIC's debt+equity invested-
capital concept doesn't map cleanly to a lender funded substantially by deposits/short-term
borrowings; ROE is the standard substitute):
  Average equity (TTM window) = (Q1 2025 equity $31,202M + Q1 2026 equity $33,995M) / 2 = $32,598.5M
  ROE = TTM Net Income / Average equity = 11,220 / 32,598.5 = 34.42%
  (Cross-check: independent third-party sources — CSIMarket, GuruFocus — report AXP's recent ROE
  in the 33–35% range, consistent with this session's own computation from primary XBRL inputs.)
ROIC_Component = clamp((34.42/30)×100, 0, 100) = 100.0   (clamped — above the 30% ceiling)

Profitability_Score = (50.47 + 100.0) / 2 = 75.24   (no FCF-positivity cap — 5yr positive, §3.1)
```

**GROWTH (20% weight):**
```
Revenue 3yr CAGR (FY2022 $52.9B → FY2025 $72.2B) = (72.2/52.9)^(1/3) − 1 = 10.93%
Growth_Score (raw) = clamp((10.93/25)×100, 0, 100) = 43.72
```
**TAM/pricing-power modifier (+10):** documented, *actual* (not guidance) evidence — Card Member services expense +27% YoY (FY2025) tied to premium-account growth; billed business +8% YoY (Q1 2026) outpacing broader US card-network volume growth (+5.9%, Q1 2025 Nilson data); and continued fee-income/billed-business growth in the first full quarter after a 29% Platinum-fee increase (§2.5). Guidance (AXP's own FY2026 9–10% revenue-growth guidance) is deliberately **not** used as evidence here, per this framework's standing rule that self-issued guidance is a re-valuation trigger, not a scored input.
```
Growth_Score = 43.72 + 10 = 53.72
```
No deceleration modifier: YoY revenue growth ran +14.4% (FY22→23, a post-pandemic T&E-spending snapback, not a representative base), then stabilized at +8.9% (FY23→24) and +9.6% (FY24→25) — steady, not structurally decelerating.

**MOAT SIGNAL (15% weight):**

| Signal | Evidence | Result |
|---|---|---|
| Market share stable/growing | Nilson Report (third-party): $1.7T global purchase volume (~9% share), 141M cards (~4% global share); Q1 2026 billed-business growth (+8%) outpacing broader US card-network growth (+5.9%, Q1 2025) — directional share-gain evidence | ✅ TRUE |
| Brand premium | Platinum annual fee raised $695→$895 (+29%, Sept 2025), following a 2021 hike ($550→$695) — continued billed-business and fee-income growth in the following reported quarter, evidence of sustained pricing power without visible volume loss | ✅ TRUE |
| Network effect | AXP's own 10-K: closed-loop model, "issuer, network, and a merchant acquirer... under one roof," direct two-sided relationships with Card Members and merchants — a documented mechanism | ✅ TRUE |
| Switching costs | Membership Rewards points/status-tier program — documented lock-in mechanism | ✅ TRUE |
| Scale cost advantage | No cost-per-unit citation vs. smaller card issuers found this session | ❌ not established |

```
Moat_Score = (4/5) × 100 = 80.0
```

**FCF QUALITY (10% weight):**
```
FCF/NI (FY2025, most recent complete fiscal year) = 16,003 / 10,833 = 147.71%
FCFQuality_Score = clamp(((1.4771 − 0.40)/0.60)×100, 0, 100) = clamp(179.5, 0, 100) = 100.0   (clamped)
```

### 3.3 Margins (15% weight) — constructed analog, not a company-disclosed line, shown with a robustness range

AXP's own income statement has no GAAP Cost-of-Revenue/Gross-Profit split (§2.3). Following this framework's precedent of constructing the most direct "cost of the core product" analog for a business without a conventional COGS line (the 2026-07-19 RYAAY session's flight-operating-cost construction; the 2026-07-17 CAKE session's food-and-beverage-cost construction), this session uses **Card Member rewards + Provisions for credit losses** — the two expense lines most directly and variably tied to each dollar of Card Member spending/lending (rewards paid per dollar of billed business; credit-loss provisions tied to the loan book that generates the lending revenue) — as the cost-of-revenue analog:

```
Conservative construction (rewards + provisions):
  Cost analog = $18,409M (Card Member rewards) + $5,300M (provisions for credit losses) = $23,709M
  Gross Margin analog = (72,200 − 23,709) / 72,200 = 67.16%
  GrossMargin_Score = clamp((67.16/80)×100, 0, 100) = 83.95

Generous construction (rewards only):
  Cost analog = $18,409M
  Gross Margin analog = (72,200 − 18,409) / 72,200 = 74.50%
  GrossMargin_Score = clamp((74.50/80)×100, 0, 100) = 93.13
```
No structural-trend bonus applies either way (both constructions are already well above the 40% threshold the +10 bonus is gated on). **This is a session-constructed analog, not a figure AXP itself discloses** — flagged explicitly, consistent with "never invent or estimate financial data": the *inputs* (Card Member rewards, provisions) are real, audited, primary-sourced figures; only the *classification* of them as "cost of revenue" is a judgment call. Both constructions land well above 40% either way, so this component is at least directionally robust — the real ambiguity is in Balance Sheet (§3.4) below.

### 3.4 Balance Sheet (15% weight) — genuinely not computable

No GAAP EBIT/EBITDA line exists for AXP (§2.3) — interest expense on deposits/borrowings is netted directly into "Total revenues net of interest expense," with no separately disclosed interest-expense figure to add back and reconstruct an EBIT/EBITDA analog the way §3.3's Margins construction could be attempted. Unlike Margins, there is no defensible partial construction here — **Net Debt/EBITDA (including the Upgrade 5 asset-light variant) cannot be computed for AXP, full stop.** This is the fourth instance of this exact gap after SOFI (2026-06-21), Citigroup (2026-07-12), and JPMorgan (2026-07-14) — but the first time it's the swing factor that actually changes the Quality Gate conclusion, since AXP (unlike those three) doesn't fail on the FCF-based hard disqualifiers first (§3.1).

**Context only, not substituted into the formula:** Total debt $57.8B (FY2025) against $33.5B equity and $152.5B in deposits; CET1 capital ratio 10.5% vs. a 7.0% regulatory minimum (§2.4) — a real but thinner capital cushion than JPMorgan's or Citigroup's.

### 3.5 Quality Score — the gate is genuinely too close to call

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

Fixed components: 0.25×75.24 + 0.20×53.72 + 0.15×80.0 + 0.10×100.0
                 = 18.81 + 10.744 + 12.00 + 10.00 = 51.554

Adding Margins (§3.3, two constructions):
  Conservative Margins (83.95):  51.554 + 0.15×83.95 = 51.554 + 12.5925 = 64.1465
  Generous Margins (93.13):      51.554 + 0.15×93.13 = 51.554 + 13.9695 = 65.5235

Adding Balance Sheet's full [0, 100] uncertainty range (§3.4) on top of each:

  Conservative Margins:  Floor (BS=0) = 64.1  →  Ceiling (BS=100) = 79.1
  Generous Margins:      Floor (BS=0) = 65.5  →  Ceiling (BS=100) = 80.5
```

**The ceiling lands at 79.1–80.5 depending on the Margins construction — straddling the 80.0 gate by less than a point and a half, entirely on the back of one un-computable sub-score (Balance Sheet, 15% weight) and one judgment-laden constructed sub-score (Margins, 15% weight).** Both stem from the same root cause: AXP's hybrid closed-loop issuer/network/lender business model doesn't map cleanly onto a formula built for a conventional non-financial company's income statement. Under the floor case (Balance Sheet treated as 0, the harshest possible reading), the score is 64.1–65.5 — a clear FAIL. Under the ceiling case (Balance Sheet treated as 100, the most generous possible reading, with the more generous Margins construction), the score is 80.5 — a PASS. **This is not the JPM/Citigroup/SOFI situation, where the N/M components didn't change the outcome (their ceiling stayed decisively below 80.0 either way) — for AXP, the gap genuinely determines whether this evaluation proceeds any further.**

### 3.6 Gate result: **INDETERMINATE — cannot proceed without inventing a number**

Per this session's explicit instructions and this framework's "never invent or estimate financial data" rule, this session **does not pick a point within the 79.1–80.5 band and call it AXP's Quality Score.** Doing so would mean inventing a Net Debt/EBITDA-equivalent figure for a company that structurally does not report one — exactly the kind of fabrication Rule 0 and the quality-scoring.md sourcing discipline exist to prevent. **This evaluation stops here: no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed**, consistent with the treatment of a company that hasn't cleared the 80.0+ gate (this framework doesn't proceed on an unresolved "maybe").

---

## 4. Why this reads as a framework gap, not a judgment about AXP's quality

Every hard disqualifier passes cleanly (§3.1) and three of five sub-scores compute cleanly to genuinely strong values (Profitability 75.24, Moat 80.0 on 4-of-5 well-documented signals, FCF Quality clamped at the 100.0 ceiling) — nothing here suggests AXP is a weak or troubled business. The blocking issue is entirely structural: **this framework's Quality Score formula has no documented carve-out for a closed-loop card issuer/network/lender hybrid** — a business model that is neither a conventional non-financial company (with a clean COGS/EBIT/EBITDA income-statement structure) nor a pure asset-light payment network (Visa/Mastercard, covered by the existing Upgrade 5 override) nor a conventional deposit-funded universal bank (JPM/Citigroup/SOFI, where the existing "N/M, not computable" treatment for Margins/Balance-Sheet doesn't change the outcome because the FCF-based hard disqualifiers fail those names first).

This is now the **fourth** name to hit some version of this gap (after SOFI, Citigroup, JPMorgan) and the **first where the gap is actually outcome-determinative** rather than moot — a stronger, more specific case than any of the three prior sessions for prioritizing a documented framework fix: either (a) a specific closed-loop-issuer Balance-Sheet proxy (e.g., a deposits/equity-based leverage check analogous to CET1, formally mapped onto the 0–100 scale the way Upgrade 5 already does for asset-light payment networks), or (b) an explicit ruling on whether a constructed Margins analog like §3.3's is acceptable practice going forward. **Not resolved within this session** — no framework file has been edited here, consistent with how the JPM/C/SOFI sessions handled the same class of gap (flagged for a future `decisions/` entry and framework-file edit, not silently patched around).

---

## 5. Recommendation: **PASS (no entry) — Quality Gate result INDETERMINATE, not a clean FAIL**

**Do not enter AXP this session.** This is deliberately *not* phrased as a definitive "fails the Quality Gate" the way the RYAAY (65.1/100.0) or JPM (60.86 ceiling) sessions were — those names failed decisively under every reasonable reading of their gaps. AXP's situation is different and, in a sense, more interesting: three of five sub-scores are genuinely strong, no hard disqualifier fires, and the only reason this session stops is that the two remaining sub-scores (Balance Sheet, un-computable; Margins, constructible only via a judgment call) create a plausible score band (79.1–80.5) that straddles the 80.0 gate by under a point and a half. **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed** — this session stops at the Quality Gate per the command specification, treating "genuinely indeterminate" the same as "not yet cleared" rather than guessing which side of the line is correct.

The triggering Telegram post (a routine "reporting this week, financial-sector health indicator" mention with no specific claims) was used only as the reason to run this first-ever evaluation and was not relied upon for any figure or conclusion above.

---

## 6. Next Review Trigger

No routine re-check is scheduled on a numeric-score basis (no Phase 02 score exists to go stale). Re-evaluate on any of the following:
- **AXP's Q2 2026 earnings**, confirmed (via a third-party earnings calendar; not yet SEC-filed as of this session) for **2026-07-24** — the actual trigger event the Telegram post referenced. A fresh TTM window and updated Growth/Profitability inputs would follow from it, though the Balance-Sheet/Margins structural gap (§3.4–3.6) would persist unless the framework itself is amended.
- **A framework-level fix** to the Balance-Sheet or Margins sub-score methodology for closed-loop issuer/network/lender business models (§4) — would let this evaluation actually resolve to a real, single Quality Score rather than a band.
- The standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move.

Absent any of the above, a future Telegram mention of AXP should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Data Gaps Flagged

1. **Balance Sheet sub-score (Net Debt/EBITDA) is not computable** — AXP discloses no GAAP EBIT/EBITDA line, and interest expense is netted directly into revenue with no separately disclosed figure to reconstruct one (§3.4). This is the single largest driver of the indeterminate gate result (§3.5–3.6). Not resolved this session — flagged as the primary blocking gap.
2. **Margins sub-score required a session-constructed analog** (Card Member rewards ± provisions for credit losses, §3.3) rather than a company-disclosed Gross Margin figure — the underlying inputs are real and primary-sourced, but the classification choice materially affects whether the Quality Score ceiling clears 80.0 (79.1 vs. 80.5, §3.5).
3. **FY2025 "Total revenues net of interest expense" is sourced to AXP's own press-release-rounded figure ($72.2B)**, not a precise SEC XBRL tag value — the concept isn't tagged under a standard `us-gaap:Revenues` value in AXP's recent filings (that tag stopped being used after FY2010, per XBRL query). Sensitivity check: a ±$100M swing in this figure moves the Net Margin component by roughly 0.1 points — immaterial to the §3.5 conclusion.
4. **Q2 2026 earnings (due 2026-07-24) are not yet available** — this is the actual event the triggering Telegram post referenced; not used anywhere in this session (§0).
5. **FY2025 CapEx ($2,425M) is sourced from stockanalysis.com only**, not independently cross-verified against SEC XBRL (the concept tag used for FY2021–FY2024 didn't yet carry an FY2025 value at session time) — the resulting FCF figure is internally consistent with AXP's own reported net income and operating cash flow, so accepted, but flagged as the one cash-flow figure not independently re-derived from a primary tag.

None of these gaps is silently patched around — each is the explicit reason this session stops short of a full score rather than guessing (§3.6).

---

## 8. Glossary

| Term | Meaning |
|---|---|
| **Billed business** | Full entry in [glossary.md](../framework/glossary.md). AXP's total dollar volume of spending on cards it issues directly — $1,670B for FY2025, +8% YoY in Q1 2026 (§2.5). |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Card Member** | Full entry in [glossary.md](../framework/glossary.md). AXP's own term for a cardholder — used throughout its filings ("Card Member loans," "Card Member rewards," "Card Member services"). |
| **CET1 (Common Equity Tier 1) ratio** | Full entry in [glossary.md](../framework/glossary.md). AXP's CET1 ratio was 10.5% at FY2025 year-end, against a 7.0% regulatory minimum (§2.4, §3.4) — cited for context, not substitutable into the Net Debt/EBITDA formula. |
| **Closed-loop network** | Full entry in [glossary.md](../framework/glossary.md). AXP operates as issuer, network, and merchant acquirer "under one roof" — credited as Network Effect and Switching Cost moat-signal evidence (§3.2, §2.5). |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization — operating-profit measures that don't exist in standard form for AXP, since interest expense is netted directly into its headline revenue line rather than disclosed separately (§2.3, §3.4). |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check). AXP's FCF/NI conversion ran 120–256% across FY2021–FY2025 — comfortably clean (§2.2, §3.1). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. None fired for AXP this session (§3.1). |
| **Membership Rewards** | Full entry in [glossary.md](../framework/glossary.md). AXP's proprietary points/status loyalty program — credited as Switching Costs moat-signal evidence (§3.2, §2.5). |
| **Nilson Report** | Full entry in [glossary.md](../framework/glossary.md). Third-party card-industry data provider — source for AXP's ~9% global purchase-volume share and ~4% global card-count share (§2.5, §3.2). |
| **Provisions for credit losses** | Full entry in [glossary.md](../framework/glossary.md). AXP's FY2025 credit-loss reserve-build expense ($5.3B) — used in this session's constructed Margins analog (§3.3). |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. AXP's plausible range this session is 64.1–80.5 depending on two unresolved inputs — genuinely indeterminate, not a clean pass or fail (§3.5–3.6). |
| **ROE** | Return on Equity — Net Income ÷ shareholder equity; used as this framework's ROIC proxy for financial companies. AXP's TTM ROE is 34.42% (§3.2). |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit; not directly meaningful for AXP's deposit/short-term-borrowing-funded balance sheet, so ROE is used instead (§3.2). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — this session used Apr 2025–Mar 2026 (FY2025 minus Q1 2025 plus Q1 2026), the most recent complete window available since Q2 2026 hasn't yet been reported (§0, §2.3). |

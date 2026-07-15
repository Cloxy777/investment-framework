# NEW POSITION — SNDK (Sandisk Corporation, NASDAQ) — 2026-07-15

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6)
**Date:** 15 Jul 2026
**10Y US Treasury Yield:** 4.62% (FRED `DGS10`, most recent posted observation dated 2026-07-13, updated 2026-07-14 — normal 1-day FRED reporting lag; consistent with the value used in this same day's ASML and PYPL sessions)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §4). For reference only, the bracket in force is +5 (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current SNDK portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is SNDK's first-ever evaluation under this framework.
**Sector:** Semiconductors / NAND Flash Memory & Data Storage (Cloud/enterprise SSD, Client SSD, Consumer removable flash) — spun off from Western Digital Corporation (WDC) on **21 February 2025**.
**Filer type:** US domestic filer, CIK **0002023554** (a newly-created CIK for the standalone entity — distinct from the dormant legacy CIK 0001000180, the pre-2016 "SanDisk Corp" WDC itself acquired, which has no relation to today's filings and was not used anywhere in this session). Fiscal year ends the last Friday in June.
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

A Telegram post in channel **FinnInvestChannel** (post #2936, ~14:55 UTC, 2026-07-15) discussed SanDisk facing "renewed pressure," noted activity on X (Twitter) suggesting accumulation, and asked followers' opinions. Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only. SNDK had no watchlist entry anywhere in the repo and is not a current holding, which per `.claude/commands/telegram-scan.md` step 4 unconditionally triggers a first-ever `/new-position` evaluation regardless of how vague/sentiment-driven the mention is. Independent verification below confirms the post's framing ("renewed pressure") corresponds to a real, large, and well-covered price decline (see §1) — but the post itself contributed no data to this evaluation.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$1,509.13** | IBKR `get_price_snapshot` (contract_id **760250490**, NASDAQ, "SANDISK CORP" — confirmed correct standalone entity, not one of the leveraged/inverse single-stock ETF products (SNXX, SNDU, SNDQ, SNDG, SNDC, SANS, SADP) that also matched the `search_contracts` query for "SNDK"), `last` field, timestamp fetched 2026-07-15 16:18:19 UTC (confirmed via `date -u` at fetch time — genuinely live, re-fetched after this session's research phase rather than reused from an earlier, staler snapshot) |
| Change vs. prior close | **−$248.69 / −14.15%** | IBKR `get_price_snapshot` `change` field |
| Bid / Ask | $1,507.40 / $1,508.36 | IBKR `get_price_snapshot` |
| 52-week range | Low **$40.10** · High **$2,354.39** · Open (52w ago) $42.80 | IBKR `get_price_snapshot` `misc_statistics` — an extraordinary ~58x low-to-high range, reflecting the NAND pricing supercycle discussed in §2.7 |
| IBKR `get_price_history` (weekly bars, past year) | Confirms a genuine, gradual climb from ~$42 (Jul 2025) to a peak close of **$2,354.39** (week of 2026-03-23) before a pullback to the low-$1,500s/high-$1,700s range through June–July 2026 — internally consistent trend, not a data artifact | IBKR `get_price_history`, contract 760250490, `ONE_WEEK` bars, `ONE_YEAR` period, corporate actions included (none reported — no split adjustment involved in this move) |
| Independent-source cross-check | Motley Fool (13 Jul 2026): SNDK fell ~12.6–14% intraday in a broad chip-sector selloff; FX Leaders (14 Jul 2026): stock "soars to $1,766" on a bullish KeyBanc note the next day — both consistent with the volatile, large-magnitude single-day moves this session's IBKR fetch also shows (−14.15% on 15 Jul) | WebFetch (Motley Fool, FX Leaders, via research phase) |
| US 10Y Treasury yield | 4.62% | FRED `DGS10`, as-of 2026-07-13 |

**$1,509.13 is used as the live price for this session.** The stock is genuinely, exceptionally volatile day-to-day (a ~14% single-day move is not a data error — it is independently corroborated by financial press covering the same window), consistent with a name whose entire investment case currently rests on a fast-moving NAND commodity pricing cycle (§2.7).

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note — a critical structural fact about SanDisk's short history as a standalone filer

SanDisk became an independent, standalone-traded public company on **21 February 2025**, spun off from Western Digital (WDC) via a pro-rata share distribution (1 SNDK share per 3 WDC shares held). All SEC filings under CIK 0002023554 were identified directly from SEC EDGAR's submissions API (`data.sec.gov/submissions/CIK0002023554.json`):

| Filing | Filed | Period | Note |
|---|---|---|---|
| 10-12B / 10-12B/A (×3) | 2024-11-25 → 2025-01-27 | — | Form 10 registration statement (spin-off registration); Exhibit 99.1 (Information Statement) contains 3 years of pre-separation carve-out financials |
| 10-Q | 2025-03-07 (10-Q/A 2025-03-17) | Q ended 2024-12-27 | First post-registration quarterly filing, pre-dates separation completion |
| 10-Q | 2025-05-12 | Q ended 2025-03-28 | First quarter spanning the 21 Feb 2025 separation date |
| **10-K** | **2025-08-21** | **FY2025, ended 2025-06-27** | First annual report — blends ~8 months pre-separation carve-out + ~4 months genuine post-separation standalone results |
| 10-Q | 2025-11-07 | Q ended 2025-10-03 | Q1 FY2026 — first fully clean standalone quarter |
| 10-Q | 2026-01-30 | Q ended 2026-01-02 | Q2 FY2026 |
| 10-Q | 2026-05-01 | Q ended 2026-04-03 | **Q3 FY2026 — most recent filed** |

**No FY2026 10-K has been filed yet** (FY2026 ends ~late June 2026; the annual report is not expected until ~August 2026, per the FY2025 filing cadence).

**⚠️ Data-integrity flag, disclosed rather than invented or estimated around:** Per the FY2025 10-K's own "Basis of Presentation" note (Note 1): *"Prior to the separation, the Company's historical combined financial information was derived from WDC's consolidated financial statements and accounting records and prepared as if the Company existed on a standalone basis... The Company utilized allocations and carve-out methodologies to prepare these historical Consolidated Financial Statements... The allocations may not, however, reflect the expenses the Company would have incurred as a standalone company for the periods presented."* Only the period from **22 February 2025 onward** is genuine, independently-operated standalone-company reporting — roughly **5 quarters** of true standalone history exist as of this session (Q4 FY2025 stub + Q1–Q3 FY2026). Everything before 21 Feb 2025 — including the FY2022–FY2024 figures used for the Growth sub-score below — is **carve-out/allocated data for "the Flash Business of Western Digital Corporation"** (the Form 10's own label for the pre-separation entity), not SanDisk Corporation's own independently-run history. This is a real, SEC-filed, audited-for-registration-purposes data source (comparable in kind to S&P Global's Mobility Global carve-out or SpaceX's common-control-recast financials, both previously used in this framework with the same disclosure), **not invented or estimated** — but it is flagged everywhere it feeds a sub-score below, consistent with "never invent or estimate financial data."

**This data limitation does NOT block completing the Quality Score.** Enough primary-sourced data exists (audited carve-out figures back to FY2022, plus ~5 quarters of genuine standalone reporting) to compute every sub-score with the caveats noted — it is a disclosed comparability limitation, not a genuine absence of data. No 5-year historical PE range/average exists (only ~17 months of live trading) — moot this session since Phase 02 is never reached, but noted for the record.

### 2.2 Income statement — primary-sourced

**3 fiscal years, "SanDisk Corporation" consolidated basis** (10-K, filed 2025-08-21, in $ millions):

| | FY2025 (10-K) | FY2024 (10-K) | FY2023 (10-K) |
|---|---|---|---|
| Revenue, net | 7,355 | 6,663 | 6,086 |
| Cost of revenue | 5,143 | 5,591 | 5,656 |
| Gross profit | 2,212 | 1,072 | 430 |
| Gross margin | 30.08% | 16.09% | 7.07% |
| Total operating expenses | 3,589 | 1,540 | 2,465 |
| Operating income (loss) | (1,377) | (468) | (2,035) |
| Income tax expense | 162 | 169 | 141 |
| **Net income (loss)** | **(1,641)** | **(672)** | **(2,143)** |

Source: [10-K main document](https://www.sec.gov/Archives/edgar/data/2023554/000202355425000034/sndk-20250627.htm), Consolidated Statements of Operations.

**FY2022 baseline (needed for a true 3yr CAGR, not disclosed in the 10-K itself)** — sourced from the Form 10's Exhibit 99.1 Information Statement, "**The Flash Business of Western Digital Corporation**" Combined Statements of Operations (accession 0001193125-25-013282, filed 2025-01-27):

| | FY2024 | FY2023 | **FY2022** |
|---|---|---|---|
| Revenue, net | 6,663 | 6,086 | **9,754** |
| Net income (loss) | (672) | (2,143) | not extracted (not needed for the scored calc) |

FY2023/FY2024 figures cross-check exactly against the 10-K's own figures above ($6,086M and $6,663M respectively) — an internal consistency check between the two independently-filed documents. Source: [Form 10-12B/A Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/2023554/000119312525013282/d835366dex991.htm), Combined Statements of Operations.

**Most recent quarterly data — Q3 FY2026, 10-Q filed 2026-05-01** ($ millions):

| | 3mo ended Apr 3, 2026 | 3mo ended Mar 28, 2025 | 9mo ended Apr 3, 2026 | 9mo ended Mar 28, 2025 |
|---|---|---|---|---|
| Revenue, net | 5,950 | 1,695 | 11,283 | 5,454 |
| Cost of revenue | 1,288 | 1,313 | 4,393 | 3,740 |
| Gross profit | 4,662 | 382 | 6,890 | 1,714 |
| Operating income (loss) | 4,111 | (1,881) | 5,352 | (1,395) |
| Income tax expense | 492 | 32 | 638 | 157 |
| **Net income (loss)** | **3,615** | **(1,933)** | **4,530** | **(1,618)** |

Source: [10-Q filed 2026-05-01](https://www.sec.gov/Archives/edgar/data/2023554/000162828026029401/sndk-20260403.htm), Condensed Consolidated Statements of Operations. Net revenue rose 251% (3mo) / 107% (9mo) YoY, driven per the filing's own MD&A by a **248% YoY increase in average selling price (ASP) per gigabyte** with exabytes sold roughly flat — i.e., this quarter's swing to profitability is a pricing story, not a volume story (see §2.7).

### 2.3 TTM reconstruction (ending 3 Apr 2026)

Same method as this framework's TSM/SPCX sessions: TTM = FY2025 (full year) − 9mo-ended-28-Mar-2025 (comparative column) + 9mo-ended-3-Apr-2026 (current column):

```
Revenue TTM      = 7,355 − 5,454 + 11,283  = 13,184
Cost of rev. TTM = 5,143 − 3,740 + 4,393   = 5,796
Gross profit TTM = 13,184 − 5,796          = 7,388   → Gross Margin TTM = 56.04%
Opex TTM         = 3,589 − 3,109 + 1,538   = 2,018
Op income TTM    = 7,388 − 2,018           = 5,370
Interest/other TTM = (102) − (66) + (184)  = (220)
Pretax income TTM = 5,370 − 220            = 5,150
Tax expense TTM  = 162 − 157 + 638         = 643    → Effective tax rate TTM = 643/5,150 = 12.49%
Net income TTM   = 5,150 − 643             = 4,507  → Net Margin TTM = 4,507/13,184 = 34.19%
```

### 2.4 Cash flow — primary-sourced, 3 fiscal years (10-K, $ millions)

| | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| Net cash provided by (used in) operating activities | 84 | (309) | (713) |
| Purchases of property, plant & equipment (CapEx) | (204) | (166) | (219) |
| **Free Cash Flow (OCF − CapEx)** | **(120)** | **(475)** | **(932)** |
| Depreciation & amortization | 163 | 224 | 448 |

Source: [10-K](https://www.sec.gov/Archives/edgar/data/2023554/000202355425000034/sndk-20250627.htm), Consolidated Statements of Cash Flows.

**9-month comparatives (Q3 FY2026 10-Q, $ millions):**

| | 9mo ended Apr 3, 2026 | 9mo ended Mar 28, 2025 |
|---|---|---|
| Net cash provided by (used in) operating activities | 4,545 | (10) |
| Purchases of property, plant & equipment | (134) | (159) |
| **Free Cash Flow** | **4,411** | **(169)** |
| Depreciation & amortization | 112 | 127 |

Source: [10-Q filed 2026-05-01](https://www.sec.gov/Archives/edgar/data/2023554/000162828026029401/sndk-20260403.htm), Condensed Consolidated Statements of Cash Flows.

```
TTM OCF    = 84 − (10) + 4,545   = 4,639
TTM CapEx  = 204 − 159 + 134     = 179
TTM FCF    = 4,639 − 179         = 4,460
TTM D&A    = 163 − 127 + 112     = 148
TTM EBITDA = Op income TTM + D&A TTM = 5,370 + 148 = 5,518
```

### 2.5 Balance sheet — primary-sourced (10-Q filed 2026-05-01, $ millions, as of 3 Apr 2026 vs. 27 Jun 2025)

| | **Apr 3, 2026** | Jun 27, 2025 |
|---|---|---|
| Cash and cash equivalents | **3,735** | 1,481 |
| Total assets | 17,075 | 12,985 |
| Current portion of long-term debt | **0** | 20 |
| Long-term debt | **0** | 1,829 |
| **Total debt** | **0** | 1,849 |
| Total liabilities | 3,298 | 3,769 |
| Total shareholders' equity | 13,777 | 9,216 |
| Shares issued and outstanding (millions) | 148 | 146 |

The Company's $1.9B Term Loan Facility (entered 21 Feb 2025 alongside the separation) was **settled in full on 4 March 2026, using cash on hand** — SanDisk is currently **debt-free** with a large, growing net-cash position, a direct result of the cash thrown off by the NAND pricing supercycle (§2.7). Shares outstanding rose modestly (146M → 148M, +1.4%) between fiscal year-end and the latest quarter — consistent with routine equity-compensation-plan issuance, not a dilutive capital raise.

```
Net Debt (3 Apr 2026)   = Total Debt − Cash = 0 − 3,735 = (3,735)   [net cash position]
Net Debt/EBITDA (TTM)   = (3,735) / 5,518 = (0.677)×   [net cash — deeply negative ratio]
```

### 2.6 Moat evidence — cited sources

| Signal | Result | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | TrendForce (independent market-research firm): SanDisk's global NAND flash market share moved from **12.4% (Q3 2025), ranked 4th** to **13.9%, tied for 4th with Micron (Q1 2026)** — a modest but real gain over two quarters, with SanDisk's revenue growth (+96.7% QoQ) running slightly ahead of the ~84% industry-wide average. Sources: [TrendForce, 29 Jan 2026](https://www.trendforce.com/news/2026/01/29/news-second-tier-no-more-kioxia-and-sandisk-balance-alliance-and-rivalry-in-ai-nand-race/), [TrendForce, 25 May 2026](https://www.trendforce.com/presscenter/news/20260525-13058.html) |
| Brand premium | **FALSE** | SanDisk's own 10-K describes a "premium consumer brand" and "industry leading consumer brand awareness" (Item 1, Business Strategy) — but this is the company's own self-description, not independently corroborated. No third-party citation was found showing SanDisk sustains a retail price premium over generic/private-label flash storage *without volume loss*; the large ASP increases actually observed (§2.7) are an industry-wide commodity pricing dynamic (TrendForce shows all top-5 suppliers' revenue rising ~84–105% QoQ in lockstep), not company-specific pricing power. Not credited, to avoid conflating a cyclical commodity price swing with a durable brand premium. |
| Network effect | **FALSE** | SanDisk is a hardware/component manufacturer selling into OEM, enterprise, and retail channels — no two-sided marketplace dynamic applies. |
| Switching costs | **TRUE** | SanDisk's own 10-K risk factors (Item 1A) repeatedly describe "**lengthy product qualifications**" / "**lengthy testing processes**" as a defining industry dynamic — enterprise/cloud customers must formally qualify a supplier's SSDs into their infrastructure before deployment, a multi-month-to-multi-year process. Once qualified, a customer has a real switching cost to re-qualify a competitor's drives. **Caveat:** the 10-K frames this primarily as a *risk* (a barrier SanDisk itself must clear to win new business), not explicitly as a moat protecting existing revenue — the switching-cost inference here is this framework's own reading of a documented, cited mechanism (same double-edged "qualification cycle" logic credited elsewhere in this framework for enterprise storage/semiconductor names), not an invented claim. |
| Scale cost advantage | **FALSE** | No cost-per-unit ($/GB or per-bit) comparison vs. Samsung, SK Hynix, Kioxia, or Micron was found in the 10-K or in third-party research pulled this session. Flash Ventures (§8 Glossary) is a *cost-shared* joint venture with Kioxia (wafers priced "at cost plus a small markup" between the two partners) — evidence of a cost-sharing arrangement, not a demonstrated absolute-scale cost edge over larger competitors (Samsung and SK Hynix are both larger by market share, §2.6 above). Not credited absent a specific citation. |

```
Moat_Score = (2 of 5 TRUE) / 5 × 100 = 40.0
```

### 2.7 Qualitative context — the NAND pricing supercycle (central to every number above)

An AI-datacenter-driven NAND flash shortage intensified sharply through 2025–2026: the combined revenue of the top-5 global NAND suppliers rose **83.7% QoQ in Q1 2026** to exceed $38.9B (TrendForce, 25 May 2026), driven by rising ASPs amid persistent supply-demand imbalance and surging enterprise-SSD/data-center demand. SanDisk's own Q3 FY2026 10-Q attributes its 251% YoY revenue growth almost entirely to a 248% YoY ASP increase (exabytes sold flat) — i.e., the swing from heavy losses (FY2023–FY2025) to strong current profitability is a **commodity price-cycle story**, not a demonstrated structural improvement in the underlying business's competitive position. This is directly consistent with this framework's own existing glossary characterization of the category: *"DRAM/NAND... commoditized, boom-bust cyclical businesses with little durable pricing power"* (see [glossary.md](../framework/glossary.md) DRAM/NAND entry) — a framing this session leans on explicitly when declining to credit the ASP-driven revenue surge as "pricing power" for Moat/Growth-modifier purposes (§2.6, §3.2). New industry NAND capacity (e.g. Flash Ventures' K2 fab beginning BiCS10 production July 2026; Kioxia's own planned US listing) is expected to arrive starting 2027, a disclosed forward risk to the current cycle's durability, though not itself scored.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | FY2023: FCF/NI = (932)/(2,143) = 43.5% (both negative — not economically meaningful) · FY2024: (475)/(672) = 70.7% (both negative — not economically meaningful) · FY2025: (120)/(1,641) = 7.3% (both negative — not economically meaningful) · **TTM (both positive, genuinely meaningful): 4,460/4,507 = 98.96%** | disqualify if 2+ **consecutive** years <70% w/o carve-out | **Not meaningfully assessable on the 3 most recent complete-fiscal-year figures** — both FCF and NI were negative in all three years, so the ratio (though numerically computable) does not reflect actual cash-earnings quality (dividing a negative by a negative produces a number that isn't a genuine conversion signal, the same issue flagged in this framework's 2026-07-13 SPCX session). The only economically meaningful reading — TTM, where both figures are genuinely positive — is a clean **98.96%, comfortably above 70%.** **Concluded: does not independently fire** on the best-available meaningful basis. |
| Net Debt/EBITDA over threshold (2.5× standard; not asset-light eligible — a capital-intensive hardware manufacturer, not a payment network/exchange) | **Net cash position: (0.677)×** (§2.5) | disqualify if exceeds 2.5× | **✅ PASS, comfortably** — the company is debt-free with $3.7B of cash. |
| FCF positive 3+ consecutive years | FY2023: **($932)M** · FY2024: **($475)M** · FY2025: **($120)M** — all three most recent complete fiscal years FCF-negative | disqualify if not 3 consecutive positive years | **❌ FIRES.** A clean, unconditional read: **0 of the last 3 complete fiscal years were FCF-positive.** Per [glossary.md](../framework/glossary.md)'s **Hard disqualifier** entry, this specific check carries **no carve-out** — unlike the FCF/NI conversion check, it cannot be waived even with a well-documented explanation (here, a genuine cyclical-downturn explanation: FY2023–FY2025 fell during the NAND commodity down-cycle, before the current supercycle). The strongly FCF-positive current TTM figure (+$4,460M, §2.4) reflects the ongoing supercycle, but does not change the fact that FY2023, FY2024, and FY2025 — the three most recently completed fiscal years — were each FCF-negative. |

**A hard disqualifier fires (FCF not positive for 3+ consecutive years). Per quality-scoring.md and this session's explicit instructions: STOP HERE — do not proceed to Phase 02 valuation scoring, regardless of the weighted Quality Score computed below.**

### 3.2 Quality Score — full computation (produced for the record, per the "every sub-score shown" instruction, even though the gate has already failed above)

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = 34.19%
  NetMargin_Component = clamp((34.19/30)×100, 0, 100) = clamp(113.97, 0, 100) = 100.0

  EBIT_TTM = 5,370 ; Effective tax rate TTM = 12.49%
  NOPAT = 5,370 × (1 − 0.1249) = 4,699.3
  Invested Capital (3 Apr 2026) = Total Debt + Equity − Cash = 0 + 13,777 − 3,735 = 10,042
  ROIC = 4,699.3 / 10,042 = 46.79%
  ROIC_Component = clamp((46.79/30)×100, 0, 100) = clamp(155.97, 0, 100) = 100.0

  Raw Profitability_Score = (100.0 + 100.0) / 2 = 100.0
  ⚠️ CAPPED: not FCF-positive 3+ consecutive years (§3.1) → Profitability_Score capped at 40.0 per
    quality-scoring.md ("sustained quality requires sustained cash generation, not just accounting
    profitability") — this is the single largest driver pulling the overall score down.
  Profitability_Score = 40.0

MARGINS (15% weight):
  Gross Margin (TTM) = 56.04%
  GrossMargin_Score = clamp((56.04/80)×100, 0, 100) = 70.05
  3yr trend IS expanding (FY2023 7.07% → FY2024 16.09% → FY2025 30.08% → TTM 56.04%) — genuinely
    structural (driven by the industry-wide pricing recovery), but the "+10 while below 40%" bonus
    condition requires gross margin to currently be below 40%; TTM (56.04%) is already above that
    threshold, so the bonus does not apply on the primary (TTM) basis used here.
    [Sensitivity, not used: on an FY2025-only basis (30.08%, below 40%), the bonus WOULD apply:
     GrossMargin_Score = clamp((30.08/80)×100) + 10 = 37.6 + 10 = 47.6. Doesn't change the gate outcome.]
  Margins_Score = 70.05

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022 → FY2025) = (7,355 / 9,754)^(1/3) − 1 = −8.98%
  ⚠️ FY2022 figure is pre-separation carve-out data ("The Flash Business of Western Digital
    Corporation," §2.2/§2.1) — the best available primary-sourced 3yr window, flagged not invented.
  Growth_Score = clamp((−8.98/25)×100, 0, 100) = clamp(−35.9, 0, 100) = 0.0
  TAM/pricing-power modifier: NOT applied. The current revenue surge is attributable to an
    industry-wide NAND commodity pricing cycle (§2.7) — all top-5 suppliers grew revenue in
    lockstep (83.7-104.7% QoQ) — not company-specific TAM expansion or durable pricing power.
    Crediting this as "documented pricing power" would conflate a cyclical commodity swing with
    structural quality, contrary to this framework's own DRAM/NAND characterization (glossary.md)
    and Rule 6's cyclical-normalization discipline.
  Structural-deceleration modifier: NOT applied either — growth is accelerating, not decelerating.
  Growth_Score = 0.0
  [For context only, not scored: a TTM-anchored read (13,184 vs. 9,754 over ~3.75yr) gives ≈+8.4%/yr,
   a materially different sign — illustrating how sharply this mechanical 3yr-FY window is distorted
   by using FY2022 (a prior NAND up-cycle peak) as its starting point. Not substituted for the
   specified metric, but shown for transparency per "no black-box outputs."]

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM) = (0.677)× — net cash position (§2.5)
  BalanceSheet_Score = clamp(100×(1 − (−0.677)/4), 0, 100) = clamp(116.9, 0, 100) = 100.0

MOAT SIGNAL (15% weight) — see §2.6 for full evidence:
  2 of 5 TRUE (Market share stable/growing; Switching costs) — Brand premium, Network effect,
   Scale cost advantage all not credited for lack of qualifying evidence.
  Moat_Score = (2/5) × 100 = 40.0

FCF QUALITY (10% weight):
  TTM FCF/NI = 4,460 / 4,507 = 98.96% — genuinely meaningful (both figures positive, unlike the
    FY-basis figures flagged in §3.1) — no override needed, unlike SPCX's spurious-ratio case.
  FCFQuality_Score = clamp(((0.9896 − 0.40)/0.60)×100, 0, 100) = clamp(98.27, 0, 100) = 98.3

QUALITY SCORE = 40.0×0.25 + 70.05×0.15 + 0.0×0.20 + 100.0×0.15 + 40.0×0.15 + 98.3×0.10
             = 10.00 + 10.5075 + 0.00 + 15.00 + 6.00 + 9.83
             = 51.3375 → rounds to 51.3
```

**Quality Score = 51.3 / 100.0 — fails the 80.0+ gate on the weighted score alone, AND independently fails via the FCF-positivity hard disqualifier (§3.1). A double failure, the same structure as this framework's 2026-07-13 SPCX session.**

**Gate result: FAIL.** Per quality-scoring.md, operating-brief.md, and this session's explicit instructions: **do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or any order setup.**

---

## 4. Phase 02 / Order Setup — NOT PRODUCED

No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup is computed this session. The Quality Score gate is a strict, non-negotiable prerequisite and SNDK clears neither the weighted-score threshold (51.3 vs. 80.0 required) nor the hard-disqualifier check.

---

## 5. Qualitative Notes

1. **This is fundamentally a cyclical commodity-hardware business currently mid-upswing, not a demonstrated structural compounder.** Every strong current figure (TTM net margin 34.2%, ROIC 46.8%, net-cash balance sheet, TTM FCF +$4.46B) is a direct consequence of the ongoing NAND pricing supercycle (§2.7) layered on top of a company that lost money and burned cash in every one of the three fiscal years immediately preceding it (FY2023–FY2025: cumulative net loss ~$4.46B, cumulative FCF burn ~$1.53B). The framework's hard disqualifier structure is specifically designed to catch exactly this pattern — a business whose *trailing* multi-year cash generation was poor, however good its *current* quarter looks.
2. **The FCF-positivity failure is not a rounding-error or convention artifact.** It is a clean, three-year run of negative free cash flow (−$932M → −$475M → −$120M, a narrowing but still-negative trend) that would have needed one more clean fiscal year to flip — the current TTM figure (+$4.46B) is well within the positive range, but the disqualifier is evaluated on complete fiscal years, and FY2026 (ending ~late June 2026, not yet reported) is the earliest fiscal year that could register as positive.
3. **The Growth sub-score's negative reading (3yr CAGR −8.98%) is highly sensitive to the choice of starting year** — FY2022 was itself a prior NAND up-cycle peak (revenue $9,754M), so measuring "growth" from that peak to FY2025's cyclical trough mechanically produces a negative number even though the business is now in a strong recovery. This is disclosed and shown with an alternative (TTM-anchored, ≈+8.4%/yr) read for transparency, but the specified FY-anchored 3yr metric is what's scored, consistent with treating this as a genuinely cyclical business (per Rule 6 and this framework's own DRAM/NAND characterization) rather than inventing a rule-bending exception.
4. **Moat evidence is thin (2 of 5, Moat_Score 40.0) and mostly not company-specific.** The one differentiated signal (a modest, real market-share gain, TrendForce-cited) sits inside an industry-wide rally where every major competitor grew similarly; the other credited signal (switching costs via lengthy qualification cycles) is a genuine, cited, documented mechanism but one the company's own 10-K frames primarily as a competitive risk rather than a moat. No cost-per-unit or brand-premium citation was found to support the other two candidate signals.
5. **The Telegram trigger's framing ("renewed pressure," accumulation rumors on X) is validated directionally but is not itself decisive.** SNDK genuinely fell double digits intraday in the days around this trigger (§1) — but independent verification here shows the fundamental picture (a hard Quality Score disqualifier, well below the 80.0 gate even ignoring that disqualifier) is the actual reason this name doesn't qualify for any position, unrelated to the specific price level the post was reacting to.
6. **Data gap disclosed, not invented around:** the Growth sub-score's FY2022 baseline and the FY2023/FY2024 comparatives all come from pre-separation carve-out ("Flash Business of WDC") financial statements, not genuine standalone-operated results — flagged explicitly in §2.1/§3.2, consistent with this framework's prior handling of SPCX's common-control-recast financials and Mobility Global's Form-10 carve-out data. This did not block completing the Quality Score (enough primary-sourced data existed to compute every sub-score), so per this session's instructions the evaluation proceeds to completion and the commit/PR workflow below, rather than being skipped.

---

## 6. Recommendation

# **PASS — Quality Score gate FAILS (51.3, well below the 80.0+ threshold) AND a hard disqualifier independently fires (not FCF-positive for 3+ consecutive years). Do not proceed to valuation scoring. No position, no watchlist-only tracking recommendation beyond a monitoring pointer — this ticker does not clear the framework's first screening gate.**

SanDisk is currently riding a genuine, well-documented NAND flash pricing supercycle that has turned three straight years of net losses and negative free cash flow into an extremely profitable, debt-free, cash-rich TTM picture (net margin 34.2%, ROIC 46.8%, net cash position). But the framework's Quality Score is explicitly designed to look through a single strong cycle: it fails the strict, non-negotiable 80.0+ gate on the weighted score alone (51.3, dragged down primarily by the FCF-positivity cap on Profitability and a negative 3yr revenue CAGR anchored on a prior cycle's peak), and it independently and unconditionally fails the "FCF positive 3+ consecutive years" hard disqualifier — FY2023, FY2024, and FY2025 were all FCF-negative, and that check carries no carve-out regardless of how well-explained the cause (a cyclical commodity downturn) is. Per operating-brief.md and quality-scoring.md, **this stops the evaluation before Phase 02** — no Rate Environment Gate, no valuation score, no Composite Score, and no fair-value/order-setup work is produced.

---

## 7. Next Review Trigger

- **SanDisk's FY2026 10-K (expected ~August 2026, covering the fiscal year ending ~late June 2026)** — this is the natural next checkpoint: it will be the first complete fiscal year with a real chance of registering **FCF-positive**, which (if it lands positive) would still leave the "3+ consecutive years" disqualifier unresolved for one more year (FY2024 and FY2025 remain negative in the trailing 3-year window until they roll off), but would be the first step toward eventually clearing it.
- **The disqualifier mechanically resolves no earlier than the FY2028 10-K** (the first year in which FY2026, FY2027, and FY2028 could all be positive) — a multi-year, not immediate, resolution path, assuming the current supercycle persists that long. Flagged as a long-dated trigger rather than a near-term one.
- **Standard Rule 9 triggers**: guidance revision (the company issued Q4 FY2026 revenue guidance of $7.75–8.25B and non-GAAP diluted EPS guidance of $30.00–33.00 alongside Q3 FY2026 results — any revision to that guidance at the actual Q4 print would be a trigger), management change, material M&A, or a >15% unexplained price move (today's −14.15% move is explained by the broader chip-sector selloff per press coverage, §1, so does not independently constitute an "unexplained" Rule 9 trigger on its own).
- **New industry capacity arriving from ~2027** (per §2.7) is a disclosed forward risk to the pricing cycle's durability — worth revisiting if/when competitor capacity additions begin showing up in NAND ASP data.

---

## 8. Watchlist & Stale-Score Housekeeping

- **New watchlist entry created:** [watchlist/not-in-portfolio/SNDK/SNDK-2026-07-15.md](../watchlist/not-in-portfolio/SNDK/SNDK-2026-07-15.md) — first-ever entry for this ticker (Phase 01 FAIL).
- **Stale-score mechanism:** not applicable — SNDK never previously had an entry, so there is nothing to clear from [watchlist/STALE.md](../watchlist/STALE.md).

---

## 9. Glossary

- **ASP (Average Selling Price)**: the average price a unit of product sells for — SanDisk's Q3 FY2026 revenue growth was overwhelmingly ASP-driven (+248% YoY per gigabyte), not volume-driven (§2.2, §2.7).
- **Carve-out financial statements**: historical financial statements prepared for a business unit that didn't previously report standalone, by allocating a parent's consolidated records to it "as if" independent — central to this session's data-integrity flags (§2.1, §3.2). *(New term.)*
- **CIK (Central Index Key)**: the SEC's unique numeric filer identifier — SanDisk's standalone entity is CIK 0002023554, distinct from a dormant legacy CIK for the pre-2016 SanDisk.
- **Composite Score**: this framework's blended 0.0–100.0 ranking (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`) — not computed this session, since SNDK never clears the Quality Score gate required to reach it.
- **D&A**: Depreciation & Amortization.
- **DRAM/NAND**: the two main families of memory chip; both commoditized, boom-bust cyclical businesses with little durable pricing power (existing glossary entry) — central to this session's decision not to credit SanDisk's current ASP-driven revenue surge as durable "pricing power" (§2.7, §3.2).
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **Effective tax rate**: the actual percentage of pretax income paid as tax in a period — SNDK's TTM figure is 12.49% (§3.2).
- **EPS**: Earnings Per Share.
- **FCF / FCF Yield / FCF/NI conversion ratio**: Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check) — central to this session's hard-disqualifier finding (§3.1).
- **Fiscal year (FY)**: SanDisk's fiscal year ends the last Friday in June.
- **Flash Ventures**: the joint-venture entities through which SanDisk and Kioxia jointly operate NAND wafer fabrication in Japan — cited as context for the Moat Signal "scale cost advantage" (not credited) and "switching costs" discussion (§2.6). *(New term.)*
- **Form 10 / 10-12B (registration statement)**: the SEC filing a company spinning off a subsidiary must file to register the new entity's stock — SanDisk's Form 10 (filed 25 Nov 2024, amended through 27 Jan 2025) is this session's source for pre-separation carve-out financials (§2.1, §2.2).
- **Hard disqualifier**: a Quality Score condition that fails a company regardless of its weighted score; SNDK's FCF-positivity disqualifier fired this session (§3.1).
- **Invested Capital**: debt + equity − cash, the ROIC denominator.
- **Moat**: a durable competitive advantage protecting a business's profits — scored 40.0 (2 of 5 signals) for SNDK this session, thinner than typical for names clearing this framework's gate.
- **NASDAQ**: the US stock exchange SNDK trades on.
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate — computed at a deeply negative (0.677)× (net cash) for SNDK this session, comfortably passing.
- **Net Margin**: Net Income ÷ Revenue — SNDK's TTM figure is 34.19%, driving a saturated (100.0) NetMargin_Component before the FCF-positivity cap is applied.
- **NOPAT**: Net Operating Profit After Tax — EBIT × (1 − effective tax rate).
- **Quality Score**: this framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to reach Phase 02. SNDK scored 51.3 and separately failed via a hard disqualifier.
- **ROIC**: Return on Invested Capital — SNDK's TTM figure is 46.79%, saturating its component before the FCF-positivity cap is applied.
- **Spin-off**: a corporate transaction separating part of a business into a new, independently-traded company — SanDisk's 21 Feb 2025 spin-off from Western Digital (WDC) is the reason this session must flag pre-separation carve-out data throughout (existing glossary entry).
- **TAM**: Total Addressable Market.
- **Term Loan Facility**: SanDisk's $2.0B term loan, entered at separation and fully repaid 4 March 2026 using cash on hand — the reason the company is now debt-free (§2.5).
- **Treasury yield (10Y)**: this framework's risk-free-rate benchmark; not used in any calculation this session since Phase 02 is never reached, but recorded in the session header per the standard output format.
- **TrendForce**: an independent semiconductor/memory-industry market-research firm — this session's third-party source for SanDisk's NAND market-share trend (§2.6). *(New term.)*
- **TTM (Trailing Twelve Months)**: the most recent 12 months of reported financial results — reconstructed for SNDK this session from FY2025 minus the 9-month comparative period ended 28 Mar 2025 plus the 9-month period ended 3 Apr 2026 (§2.3).

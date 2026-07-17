# NEW POSITION — CAKE (The Cheesecake Factory Incorporated, NASDAQ) — 2026-07-17

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 17 Jul 2026 (Friday)
**10Y US Treasury Yield:** 4.55% (FRED `DGS10`, most recent posted observation dated 2026-07-15 — recorded for completeness only, since this session stops at the Quality Gate (§3) before the Rate Environment Gate would apply)
**Current CAKE portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); grep for "cake" (case-insensitive) returns no match)
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/CAKE/` or `watchlist/not-in-portfolio/CAKE/`, and no row in [watchlist/STALE.md](../watchlist/STALE.md), confirmed via `find`/`grep`)
**Sector:** Consumer Discretionary — Restaurants / Casual Dining (multi-concept operator: The Cheesecake Factory, North Italia, Flower Child, Fox Restaurant Concepts ("Other FRC"))
**Filer type:** US domestic filer — CIK **887596** ("THE CHEESECAKE FACTORY INCORPORATED," Nasdaq: CAKE), Form 10-K/10-Q, 52/53-week fiscal year ending late December
**First-use jargon decode:** see closing Glossary (§9)

---

## 0. Why this session exists — trigger source

A post on **FinnInvestChannel** (Telegram, post #2949, 2026-07-17) mentioned "Cheesecake Factory ... completely sold yesterday" as the poster's own personal-trading commentary. Per the operating brief and this repo's standing convention, **Telegram post text is never used as financial data** — it is a trigger only, and its substantive claim (someone's personal trade) is not verified or relied upon anywhere in this session. CAKE has no existing watchlist entry in this repo and is not a current holding (confirmed via `grep`/`find` above), so per `/telegram-scan` step 4's first bullet, **any first-ever mention of a name with no watchlist entry triggers a full `/new-position` evaluation, regardless of the mention's substance.** This session is that evaluation, built entirely from independently, live-fetched data.

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("CAKE")`: contract_id **267227**, exchange **NASDAQ**, description "CHEESECAKE FACTORY INC/THE" — the correct, unambiguous match. Other `CAKE`-symbol results returned were unrelated instruments (Radio Fuels Energy Corp, a Calamos "CALAMS ATCLBL INCM ETF" listed on Xetra/LSE, a Mexican-exchange cross-listing of the same company, and "Yellow Cake PLC" / "Cake Box Holdings" — distinct UK-listed companies with only a coincidental ticker-adjacent name) — none of which are the primary US common stock used here.

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$82.70** | IBKR `get_price_snapshot`, `last` field, timestamp 1784268483 (≈2026-07-17 intraday), contract_id **267227** (NASDAQ), `is_close: false` (live, intraday) |
| Day change | **−$0.61 (−0.73%)** | IBKR `get_price_snapshot` `change` field |
| Prior close | $83.31 | IBKR `get_price_snapshot` `prior-close` field |
| Bid/Ask | $80.40 / $83.60 (wide spread — light quote depth at time of snapshot) | IBKR `get_price_snapshot` `bid_ask` field |
| 52-week high | $84.54 | IBKR `misc_statistics` `high_52w` (also the 13-week and 26-week high — the 52-week high was set within the last 13 weeks) |
| 52-week low | $42.86 | IBKR `misc_statistics` `low_52w` |
| Open 52 weeks ago | $61.82 | IBKR `misc_statistics` `open_52w` |
| US 10Y Treasury yield | 4.55% | FRED `DGS10`, as-of 2026-07-15 (not used this session — see header) |

$82.70 sits near the top of its 52-week range ($42.86–$84.54), close to the 52-week high set very recently, and up **+33.8%** from the level 52 weeks ago ($61.82) — context only, not itself scored. Shares outstanding (most recent SEC balance-sheet date, Q1 2026 10-Q, March 31, 2026): **49,781,827** → implied market cap ≈ **$4.12B** at the live price above (context only, not used in any scoring formula). This price is used for reference throughout this session; no order-setup arithmetic is performed, since the Quality Gate fails below (§3).

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

All financial figures below are sourced directly from The Cheesecake Factory Incorporated's own SEC EDGAR filings: the **FY2025 10-K** (filed 2026-02-23, accession 0001104659-26-018643, fiscal year ended December 30, 2025), the **FY2024 10-K** (filed 2025-02-24, accession 0001410578-25-000195) and **FY2023 10-K** (filed 2024-02-26, accession 0001104659-24-027565) for prior-year comparatives, and the **Q1 2026 10-Q** (period ended March 31, 2026, filed 2026-05-04), **Q3 2025 10-Q** (period ended September 30, 2025, filed 2025-11-03), and **Q2 2025 10-Q** (period ended July 1, 2025, filed 2025-08-04) for quarterly figures used in the TTM reconstruction below. Income-statement line items were read directly from each filing's own "CONSOLIDATED STATEMENTS OF INCOME" / "CONDENSED CONSOLIDATED STATEMENTS OF INCOME" tables (company-labeled line items, not a third-party vendor's re-mapping) — the SEC XBRL companyfacts API (`data.sec.gov/api/xbrl/companyfacts/CIK0000887596.json`) was checked first but its `CostOfGoodsAndServicesSold`/quarterly cost-line tags did not carry current-period "Food and beverage costs" data under a consistently-tagged concept, so the primary 10-K/10-Q HTML text was read directly instead for every cost-line and balance-sheet figure below — all cross-checked against each other (e.g. FY2025 10-K's FY2023 column vs. the standalone FY2023 10-K) and internally consistent to the dollar. No `yfinance` fallback was needed. Q4 2025 figures (no standalone SEC filing — 10-Qs report cumulative periods) are derived by subtraction (FY2025 10-K minus the 9-month-cumulative Q3 2025 10-Q), shown explicitly below, consistent with this framework's prior TTM-reconstruction method (e.g. the 2026-07-17 DJT session).

### 2.2 Fiscal-year income statement, FY2022–FY2025 (primary-sourced)

| Item ($000s) | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Revenues | 3,303,156 | 3,439,503 | 3,581,699 | 3,751,806 |
| Food and beverage costs | 810,926 | 803,500 | 806,021 | 813,147 |
| Labor expenses | 1,211,951 | 1,227,895 | 1,264,382 | 1,312,894 |
| Other operating costs and expenses | 881,627 | 922,428 | 959,221 | 1,014,015 |
| General and administrative expenses | 205,753 | 217,449 | 228,737 | 244,915 |
| Depreciation and amortization expenses | 92,380 | 93,136 | 101,450 | 109,031 |
| Impairment of assets and lease termination expenses | 31,387 | 29,464 | 13,647 | 22,990 |
| Acquisition-related contingent consideration/comp/amort. expenses | 13,368 | 11,686 | 2,429 | 14,449 |
| Preopening costs | 16,829 | 25,379 | 27,495 | 33,080 |
| Total costs and expenses | 3,264,221 | 3,330,937 | 3,403,382 | 3,564,521 |
| **Income from operations (EBIT)** | 38,935 | 108,566 | 178,317 | 187,285 |
| Interest and other expense/(income), net | (6,043) | (8,552) | (10,107 net int.) | (10,448 net int.) |
| Loss on extinguishment of debt | — | — | — | (15,891) |
| Income before income taxes | 32,892 | 100,014 | 171,047 | 162,895 |
| Income tax provision/(benefit) | (10,231) | (1,337) | 14,264 | 14,468 |
| **Net income** | 43,123 | 101,351 | 156,783 | 148,427 |

Source: FY2025 10-K (FY2023–FY2025 columns) and FY2023 10-K (FY2022 column, filed 2024-02-26), both accessed directly from SEC EDGAR.

**Revenue 3yr CAGR (FY2022→FY2025):**
```
CAGR = (3,751,806 / 3,303,156)^(1/3) − 1 = (1.13583)^(1/3) − 1 = 4.337%
```

### 2.3 TTM reconstruction (Q2 2025 + Q3 2025 + Q4 2025 [derived] + Q1 2026)

Most recent completed quarter is **Q1 2026** (ended March 31, 2026); Q2 2026 earnings are not yet released as of this session (confirmed via SEC EDGAR company-submissions feed — most recent filing is the Q1 2026 10-Q, filed 2026-05-04; no Q2 2026 8-K/10-Q on file yet).

**Revenue and Food & beverage costs (all $000s, primary-sourced from each quarter's own 10-Q):**

| Item | Q2 2025 | Q3 2025 | Q4 2025 (derived) | Q1 2026 | TTM |
|---|---|---|---|---|---|
| Revenue | 955,825 | 907,226 | 961,558 | 978,833 | **3,803,442** |
| Food & beverage costs | 205,843 | 197,654 | 207,389 | 212,250 | **823,136** |

```
Q4 2025 Revenue      = FY2025 (3,751,806) − 9mo Jan–Sep 2025 (2,790,248)  = 961,558
Q4 2025 F&B costs    = FY2025 (813,147)   − 9mo Jan–Sep 2025 (605,758)    = 207,389
Q2 2025 F&B costs    = 9mo (605,758) − Q1 2025 (202,261) − Q3 2025 (197,654) = 205,843

TTM Gross Margin (Revenue − Food & beverage costs, see §2.6 caveat) = (3,803,442 − 823,136) / 3,803,442 = 78.36%
```

**Operating Income (EBIT) and D&A — TTM, primary-sourced:**

| Item | Q2 2025 | Q3 2025 | Q4 2025 (derived) | Q1 2026 | TTM |
|---|---|---|---|---|---|
| Operating income (EBIT) | 64,822 | 37,269 | 33,235 | 55,045 | **190,371** |
| Depreciation & amortization | 26,860 | 27,419 | 28,670 | 27,984 | **110,933** |

```
Q4 2025 EBIT = FY2025 (187,285) − 9mo (154,050) = 33,235
Q4 2025 D&A  = FY2025 (109,031) − 9mo (80,361)  = 28,670

TTM EBITDA = EBIT_TTM (190,371) + D&A_TTM (110,933) = 301,304
```

**Net Income and Income Tax Provision — TTM, primary-sourced:**

| Item | Q2 2025 | Q3 2025 | Q4 2025 (derived) | Q1 2026 | TTM |
|---|---|---|---|---|---|
| Net income | 54,812 | 31,899 | 28,775 | 49,548 | **165,034** |
| Income tax provision | 7,417 | 3,582 | 1,927 | 3,803 | **16,729** |

```
Q4 2025 Net income = FY2025 (148,427) − 9mo (119,652) = 28,775
Q4 2025 Tax        = FY2025 (14,468)  − 9mo (12,541)  = 1,927

Net Margin (TTM) = 165,034 / 3,803,442 = 4.339%
Effective tax rate (TTM) = 16,729 / (165,034 + 16,729) = 16,729 / 181,763 = 9.203%
```

### 2.4 Balance sheet — primary-sourced (Q1 2026 10-Q condensed consolidated balance sheet, March 31, 2026)

| Item | Value ($000s) | Source |
|---|---|---|
| Cash and cash equivalents | 235,090 | 10-Q balance sheet |
| Current portion of long-term debt | 68,916 | 10-Q balance sheet |
| Long-term debt (noncurrent) | 562,077 | 10-Q balance sheet |
| **Total debt** | **630,993** | 68,916 + 562,077 |
| Total stockholders' equity | 459,226 | 10-Q balance sheet |
| Total assets | 3,297,341 | 10-Q balance sheet |
| Total liabilities | 2,838,115 | 10-Q balance sheet |

```
Net Debt        = Total Debt − Cash               = 630,993 − 235,090 = 395,903
Invested Capital = Total Debt + Equity − Cash      = 630,993 + 459,226 − 235,090 = 855,129
Net Debt/EBITDA (TTM) = 395,903 / 301,304          = 1.314×
```

FY2025 year-end cross-check (Dec 30, 2025 balance sheet): Total debt $630,074K (current LT debt $68,815K + noncurrent $561,259K), Cash $215,729K → Net Debt $414,345K; EBITDA_FY2025 = EBIT $187,285K + D&A $109,031K = $296,316K → Net Debt/EBITDA (FY-end) = 1.398× — consistent with the TTM figure above (both comfortably under the 2.5× standard threshold; CAKE does not qualify for the Upgrade 5 asset-light override, and doesn't need it).

### 2.5 Cash flow — primary-sourced (each period's own 10-K/10-Q cash flow statement)

**Annual FCF (Operating Cash Flow − Additions to property and equipment), all primary-sourced:**

| Fiscal Year | OCF ($000s) | CapEx ($000s) | FCF ($000s) | FCF/NI |
|---|---|---|---|---|
| FY2021 | 213,006 | 66,943 | **146,063** | 201.82% |
| FY2022 | 161,926 | 112,464 | **49,462** | 114.70% |
| FY2023 | 218,401 | 151,565 | **66,836** | **65.95%** |
| FY2024 | 268,325 | 160,364 | **107,961** | **68.86%** |
| FY2025 | 301,281 | 146,204 | **155,077** | 104.48% |

**Company has been FCF-positive every year shown (FY2021–FY2025) — comfortably clears the "FCF-positive 3+ consecutive years" hard-disqualifier test.**

**FY2023 and FY2024 FCF/NI conversion both sit below the 70% hard-disqualifier threshold (65.95% and 68.86%) — flagged and examined for a documented growth-capex explanation below (§2.6).**

**TTM cash flow (Q2 2025 + Q3 2025 + Q4 2025 [derived] + Q1 2026):**

```
Q1 2025 (13wk, from Q1 2026 10-Q's comparative column): OCF 78,919 / CapEx 42,816
6mo 2025 (from Q2 2025 10-Q): OCF 135,763 / CapEx 84,365  →  Q2 2025 (derived) = 6mo − Q1: OCF 56,844 / CapEx 41,549
9mo 2025 (from Q3 2025 10-Q): OCF 226,374 / CapEx 121,048  →  Q3 2025 (derived) = 9mo − 6mo: OCF 90,611 / CapEx 36,683
Q4 2025 (derived) = FY2025 − 9mo: OCF (301,281 − 226,374) = 74,907 / CapEx (146,204 − 121,048) = 25,156
Q1 2026 (13wk, from Q1 2026 10-Q): OCF 96,724 / CapEx 43,377

OCF_TTM   = 56,844 + 90,611 + 74,907 + 96,724 = 319,086
CapEx_TTM = 41,549 + 36,683 + 25,156 + 43,377 = 146,765
FCF_TTM   = 319,086 − 146,765 = 172,321

FCF/NI (TTM) = 172,321 / 165,034 = 104.42%
```

### 2.6 Growth-capex explanation for the FY2023/FY2024 FCF/NI dip — MD&A, primary-sourced

Per the FY2025 10-K's own "Property and Equipment" MD&A discussion (and the FY2024 10-K's equivalent section for the FY2023 breakdown):

| Fiscal Year | Total CapEx | New-restaurant CapEx | New-restaurant % of total | Existing-restaurant CapEx | Bakery/corporate infrastructure CapEx |
|---|---|---|---|---|---|
| FY2023 | $151.6M | **$98.4M (64.9%)** | 64.9% | $47.8M | $5.4M |
| FY2024 | $160.4M | **$99.0M (61.7%)** | 61.7% | $53.0M | $8.4M |
| FY2025 | $146.2M | $70.5M (48.2%) | 48.2% | $63.2M | $12.5M |

The company opened 16 new restaurants in FY2023, 23 in FY2024, and 25 in FY2025 across its four concepts (The Cheesecake Factory, North Italia, Flower Child, Other FRC) — a genuine, documented, cited unit-growth program, not maintenance spend. **This is a legitimate "documented growth-capex explanation" for the FY2023/FY2024 FCF/NI dip below 70%**: in both flagged years, a clear majority (61.7–64.9%) of total capital expenditure was tied directly to new-restaurant construction/development, not to sustaining the existing base. Per [quality-scoring.md](../framework/quality-scoring.md)'s hard-disqualifier text ("FCF/Net Income conversion ratio <70% for 2+ consecutive years **without a documented growth-capex explanation**"), this disqualifier **does not fire** — the exception is met, and cited directly to the company's own MD&A capex breakdown rather than inferred or assumed.

### 2.7 Comparable sales / traffic trend — MD&A, primary-sourced (two most recent 10-Ks)

**FY2025 10-K, "Fiscal 2025 Compared to Fiscal 2024":**
- **The Cheesecake Factory** (flagship, $2,688.8M of FY2025 revenue, ~71.6% of total): comparable sales **+0.1%** — average check +2.4% (menu pricing +4.3%, offset by −1.9% negative mix), **customer traffic −2.3%**.
- **North Italia** ($345.9M, ~9.2% of total): comparable sales **−2%** — average check +3% (menu pricing +4%), **customer traffic −5%**.
- **Flower Child** ($185.3M, ~4.9% of total): comparable sales +5% (smallest, fastest-growing concept).
- **Other FRC** ($355.1M, ~9.5% of total): "decrease in comparable sales" (no precise % disclosed).
- Total revenue +4.7% "primarily due to additional revenue related to new restaurant openings" — i.e., growth is now overwhelmingly unit-driven, not same-store-driven.

**FY2024 10-K, "Fiscal 2024 Compared to Fiscal 2023" (one year earlier, for trend context):**
- The Cheesecake Factory: comparable sales **+1.0%**, customer traffic **−0.7%**.
- North Italia: comparable sales **+2%**, customer traffic **−1%**.

**The trend across the two largest concepts (≈80.9% of FY2025 revenue combined) is a clear, multi-year, cited deceleration**: Cheesecake Factory comps decelerated from +1.0% (FY2024) to +0.1% (FY2025) as traffic deterioration worsened from −0.7% to −2.3%; North Italia comps went from +2% (FY2024) to **−2%** (FY2025) as traffic deterioration worsened from −1% to −5%. Price increases (menu pricing +4.3%/+4% respectively) are largely offsetting, not reversing, the traffic decline — this is a structural (multi-year, multi-concept, traffic-driven) deceleration, not a single cyclical quarter.

**Independent third-party corroboration:** per Circana's 2026 Definitive U.S. Restaurant Rankings (cited via Restaurant Dive, 2026), The Cheesecake Factory recorded a **2.2% same-store sales decline in Q4 2025** even while several peers (IHOP, Olive Garden) posted growth in the same period — an independent, non-company-sourced confirmation that the deceleration continued into the most recent quarter available. See §8 Sources.

### 2.8 Scale / market-position evidence — MD&A (primary) + third-party (Circana via Restaurant Dive)

Per the FY2025 10-K: as of February 23, 2026, the company owned/operated 368 restaurants (216 The Cheesecake Factory, 48 North Italia, 43 Flower Child, 55 Other FRC), plus 35 internationally-licensed Cheesecake Factory locations, and operates its own two-facility bakery division supplying its restaurants, international licensees, **and third-party bakery customers** (a distinct wholesale revenue stream layered on top of restaurant scale).

Per Circana's 2026 Definitive U.S. Restaurant Rankings (third-party, non-company-sourced; accessed via Restaurant Dive, 2026): **The Cheesecake Factory has the #1 average unit volume (AUV) among all major US restaurant chains, at $12.8 million per unit** — ahead of Texas Roadhouse ($7.9M) and Chick-fil-A ($7.2M), and roughly 6–8× the ~$1.5–2.0M "top-performing casual dining" benchmark the same source cites for the broader segment. This is directly consistent with the company's own MD&A-disclosed average sales per restaurant operating week for its flagship concept (~$238,146/week in FY2025 → ≈$12.4M annualized, arithmetically close to Circana's independently-sourced $12.8M figure). Attributed by the source to CAKE's large-format footprint (6,500–10,000 sq. ft.), premium menu, and full alcohol service.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years **without a documented growth-capex explanation** | FY2023: 65.95% · FY2024: 68.86% — both <70%, but **a documented growth-capex explanation exists** (§2.6: 61.7–64.9% of total capex in both years tied to new-restaurant development, cited to the company's own MD&A) | disqualify only if the sub-70% run is *undocumented* | ✅ **PASS — exception applies, cited directly** |
| Net Debt/EBITDA over threshold (2.5× standard — CAKE does not qualify for the Upgrade 5 asset-light override) | TTM: 1.314× (FY-end cross-check: 1.398×) | disqualify if >2.5× | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years | FY2021 $146.1M · FY2022 $49.5M · FY2023 $66.8M · FY2024 $108.0M · FY2025 $155.1M — all positive, every year shown | disqualify if not | ✅ PASS, by a wide margin |

**No hard disqualifier fires.** The FCF/NI conversion check is the closest call — two consecutive years genuinely sat below the 70% line — but the company's own MD&A directly and specifically attributes the majority of capex in both of those years to new-unit growth (not maintenance), which is exactly the documented exception the rule's own text carves out. This is flagged prominently here (rather than silently resolved) per this framework's "show every calculation, no black box" discipline.

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = 165,034 / 3,803,442 = 4.339%
  NetMargin_Component = clamp((4.339/30)×100, 0, 100) = 14.46

  NOPAT = EBIT_TTM × (1 − eff. tax rate) = 190,371 × (1 − 0.09203) = $172,897K
  Invested Capital = Total Debt + Equity − Cash = 630,993 + 459,226 − 235,090 = $855,129K
  ROIC = 172,897 / 855,129 = 20.22%
  ROIC_Component = clamp((20.22/30)×100, 0, 100) = 67.40

  Profitability_Score = (14.46 + 67.40) / 2 = 40.93   (no FCF-positivity cap — 5yr positive confirmed §2.5)

MARGINS (15% weight):
  Gross Margin (TTM, Revenue − Food & beverage costs — see caveat below) = 78.36%
  GrossMargin_Score = clamp((78.36/80)×100, 0, 100) = 97.95

  3yr trend check (FY2022→FY2025, annual): 75.45% → 76.64% → 77.50% → 78.33% — consistently INCREASING,
  but already well above the 40% threshold the framework's +10 "structural expansion while below 40%"
  bonus is specifically gated on — the bonus does not apply (not eligible, not merely "doesn't fire").

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022→FY2025) = (3,751,806/3,303,156)^(1/3) − 1 = 4.337%
  Growth_Score (raw) = clamp((4.337/25)×100, 0, 100) = 17.35
  Structural deceleration modifier: −10 applies. Documented, cited evidence (§2.7): comparable sales at the
  two largest concepts (≈81% of FY2025 revenue) decelerated over the two most recent fiscal years —
  Cheesecake Factory comps +1.0%→+0.1% (traffic −0.7%→−2.3%), North Italia comps +2%→−2% (traffic −1%→−5%)
  — with total revenue growth now overwhelmingly unit-driven rather than same-store-driven, independently
  corroborated by Circana's third-party-reported Q4 2025 same-store sales decline (−2.2%) even as peers grew.
  Growth_Score = clamp(17.35 − 10, 0, 100) = 7.35

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM) = 1.314×
  BalanceSheet_Score = clamp(100×(1 − 1.314/4), 0, 100) = 67.15

MOAT SIGNAL (15% weight) — 5-signal checklist, each evaluated against a specific citation:
  Market share stable/growing — FALSE. No third-party or company-disclosed market-share percentage was
    found; the 10-K's own language is aspirational ("increase our market share") or risk-factor framing
    ("could lose market share"), not evidence of an actual current share trend. The Circana-sourced Q4 2025
    same-store sales decline while named peers (IHOP, Olive Garden) grew (§2.7) is, if anything, evidence
    pointing the other way. Not credited.

  Brand premium — FALSE. The company can and does implement multi-percent menu price increases every year
    without resorting to heavy discounting (a genuine, citable practice), but the specific evidentiary bar
    this framework's checklist requires — "price increases WITHOUT volume loss" — is not met: traffic fell
    at both of the two largest concepts in the same periods prices rose (§2.7), the opposite pattern. Not
    credited, consistent with how this framework treated the same "price increase WITH volume loss" pattern
    for Match Group's Tinder brand (2026-07-16 MTCH session, RPP glossary entry).

  Network effect — FALSE. No documented two-sided-marketplace or user-growth-driven-value mechanism exists
    for a multi-concept restaurant operator.

  Switching costs — FALSE. Dining out carries no contractual lock-in, integration depth, or migration cost
    — a diner can freely choose a competing restaurant on any occasion. No mechanism found or plausible.

  Scale cost advantage — TRUE. Per Circana's 2026 Definitive U.S. Restaurant Rankings (third-party,
    non-company-sourced, via Restaurant Dive): The Cheesecake Factory has the **#1 average unit volume among
    all major US restaurant chains** ($12.8M), ahead of Texas Roadhouse ($7.9M) and Chick-fil-A ($7.2M), and
    roughly 6–8× the ~$1.5–2.0M "top-performing casual dining" segment benchmark the same source cites —
    independently consistent with the company's own MD&A-disclosed ~$238K/operating-week flagship average
    (≈$12.4M annualized). A large-format footprint (6,500–10,000 sq. ft.) plus a two-facility bakery division
    that also supplies international licensees and third-party wholesale customers (§2.8) is a genuine,
    structural scale/format cost advantage, not a one-off or self-reported claim.

  Moat_Score = (1/5) × 100 = 20.0

FCF QUALITY (10% weight):
  FCF/NI (TTM) = 172,321 / 165,034 = 104.42%
  FCFQuality_Score = clamp(((1.0442 − 0.40)/0.60)×100, 0, 100) = clamp(107.4, 0, 100) = 100.0

QUALITY SCORE = 40.93×0.25 + 97.95×0.15 + 7.35×0.20 + 67.15×0.15 + 20.0×0.15 + 100.0×0.10
             = 10.2325 + 14.6925 + 1.470 + 10.0725 + 3.000 + 10.000
             = 49.4675 → rounds to 49.5
```

**Structural caveat for human review — the Margins sub-score construction:** CAKE has no single GAAP-labeled "Cost of Revenue"/"Gross Profit" line the way a retailer or manufacturer does; its income statement instead breaks "Total costs and expenses" into Food & beverage costs, Labor expenses, Other operating costs and expenses, G&A, D&A, impairment, and preopening costs. This session used **Food & beverage costs alone** as the closest GAAP-labeled cost-of-revenue analog (the direct cost of the ingredients served), consistent with standard restaurant-industry practice and with this framework's own precedent of choosing the most direct "cost of the core product/service" line for a business without a conventional COGS line (e.g. the 2026-07-16 UNH session's "Medical Costs + Cost of Products Sold" construction). **This yields a Margins sub-score (97.95) that reads almost at the ceiling — an artifact of the construction, not evidence of software-like pricing power.** Labor (the largest single cost line, 35.0% of FY2025 revenue) and Other operating costs (27.0% of FY2025 revenue) sit *below* this "gross margin" line by construction, which is exactly why CAKE's *net* margin (4.34% TTM) is thin despite a food-cost-only "gross margin" near 78%. Flagged explicitly here, per this framework's "show every calculation, no black-box" discipline and precedent (UNH's managed-care margin-calibration caveat, MTCH's negative-equity ROIC caveat) — **this caveat does not change the gate outcome below**, since even crediting this sub-score at its full, as-computed value, the Quality Score still fails by a wide margin.

**Robustness check (not just a point estimate).** Even under the maximally generous alternate reading of the two most judgment-dependent sub-scores (Growth, with no deceleration modifier; Moat, crediting all 5 signals despite zero citable evidence for 4 of them):

```
40.93×0.25 + 97.95×0.15 + 17.35×0.20 + 67.15×0.15 + 100.0×0.15 + 100.0×0.10
= 10.2325 + 14.6925 + 3.470 + 10.0725 + 15.000 + 10.000 = 63.47
```

**Still well below the 80.0 gate.** A second, more extreme (and not defensible) hypothetical — crediting Growth at its formula-uncapped raw value *and* Moat at a full 5/5 (which would require inventing evidence for Market share, Brand premium, Network effect, and Switching costs that simply does not exist anywhere in the record, in direct violation of "never mark a signal true without a cited source") happens to arithmetically approach, but not clear, the gate:

```
40.93×0.25 + 97.95×0.15 + 100.0×0.20 + 67.15×0.15 + 100.0×0.15 + 100.0×0.10
= 10.2325 + 14.6925 + 20.000 + 10.0725 + 15.000 + 10.000 = 79.9975 → rounds to 80.0
```

This last figure is shown only to demonstrate that the gate is not being failed by an unreasonably harsh reading of any single input — reaching it requires crediting four of five Moat signals with **zero** supporting evidence, which this framework's own rules explicitly forbid ("never mark a signal true without a cited source"). The **actual, evidence-based Quality Score is 49.5** (§3.2 above), which fails the gate by more than 30 points, and even the *legitimately defensible* robustness ceiling (63.47, crediting only the judgment calls that have some real basis) fails by nearly 17 points. This is not a marginal or close call.

### 3.3 Gate result

**Quality Score = 49.5 / 100.0 — FAILS the 80.0+ gate.** No hard disqualifier independently fires (§3.1 — the FCF/NI conversion dip in FY2023/FY2024 is defused by a documented, cited growth-capex explanation). The failure is driven by thin GAAP net margin (4.34% TTM) and a low ROIC (20.22% sounds respectable in isolation, but the Profitability sub-score blends it with the much weaker net-margin component per the framework's fixed formula), a decelerating same-store-sales/traffic trend at the two largest concepts (documented and cited, §2.7, independently corroborated by a third-party Q4 2025 data point), and a weak Moat Signal read (1 of 5 — only "scale cost advantage" credited, via a genuine #1-in-industry AUV ranking). Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md): **stop here — do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or fair-value/order-setup work.**

---

## 4. Qualitative Notes

1. **CAKE clears the balance-sheet and cash-generation bars comfortably** — Net Debt/EBITDA (1.314× TTM), FCF-positivity (5 straight years), and (once the growth-capex exception is applied) FCF/NI conversion are all genuinely solid. The gate failure here is **not** a leverage or cash-quality story, unlike some names this framework has failed for balance-sheet reasons.
2. **The core problem is thin profitability relative to the framework's asset-light-calibrated thresholds, combined with a real, cited growth deceleration** — restaurant-industry net margins are structurally thinner than software/consumer-staples businesses (labor- and real-estate-intensive operating model), and this framework's Profitability sub-score (net margin ÷ 30% cap) does not adjust for that, similar to the managed-care margin-calibration caveat flagged in the 2026-07-13/07-16 UNH sessions. Even so, the deceleration in comparable sales/traffic at the two largest concepts is a real, independently-corroborated (Circana/Restaurant Dive) signal, not solely a formula-calibration artifact.
3. **The #1 industry AUV ranking is a genuine, well-documented competitive strength** — but it is a *scale* advantage (fixed-cost leverage from a large-format, high-throughput restaurant model plus a wholesale-supplying bakery division), not a *pricing-power* or *network* moat. It shows up correctly as the one credited Moat Signal (Scale cost advantage), not as Brand premium, since the same source that reports the AUV ranking also reports the Q4 2025 same-store sales decline.
4. **A quarterly $0.30/share cash dividend was declared 23 April 2026** (paid 26 May 2026, per the Q1 2026 earnings 8-K) — noted for completeness only; no fair-value/shareholder-yield work was performed this session since the Quality Gate fails first.
5. **No unusual Rule 9-style event was found in the review period** — the two most recent 8-Ks (29 April 2026 Q1 2026 earnings release + routine dividend declaration; 3 June 2026 routine annual-meeting voting results) are both ordinary-course filings, not a fundamental trigger in their own right. This session exists solely because of the Telegram first-mention rule (§0), not because of a detected fundamental event.

---

## 5. Recommendation

# **PASS — Quality Gate FAIL (Quality Score 49.5 < 80.0). Do not enter.**

The Cheesecake Factory clears every hard disqualifier (balance sheet, FCF-positivity, and — once its own documented new-unit capex spend is accounted for — FCF/NI conversion) but fails the strict 80.0+ Quality Score gate by a wide margin on the weighted score itself: thin GAAP profitability (Net Margin 4.34% TTM), a real and independently-corroborated deceleration in comparable sales/traffic at its two largest concepts, and a weak Moat Signal read (1 of 5, scale cost advantage only). **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed** — this session stops at the Quality Gate per the command specification. The triggering Telegram post (a personal "completely sold" trading comment) was used only as the reason to run this first-ever evaluation and was not relied upon for any conclusion.

---

## 6. Next Review Trigger

No routine re-check is scheduled (Phase 01 FAIL, no numeric Phase 02 score to go stale). Re-evaluate on any of the following Rule 9-style fundamental triggers:
- **CAKE's Q2 2026 earnings** (date not yet disclosed in sources reviewed; historically released in early August) — the standard quarterly trigger; will show whether the comparable-sales/traffic deceleration at The Cheesecake Factory and North Italia concepts continues, stabilizes, or reverses.
- **Any material change in unit-growth guidance** (currently ~26 new restaurants planned for FY2026, ~$210M capex) — a sharp slowdown or acceleration in new-unit openings would materially change both the Growth sub-score input and the "documented growth-capex explanation" basis used to defuse the FCF/NI hard disqualifier this session.
- A management change, material M&A, a macro/rate shift, or a >15% unexplained price move (today's −0.73% move is minor and not itself a trigger).
- **FY2026 fiscal year-end close** (~Feb 2027 report) — replaces FY2022 in the 3yr Revenue CAGR window and gives a fourth consecutive year of comparable-sales data to confirm or refute the deceleration trend flagged in §2.7.

Absent any of the above, a future Telegram mention of CAKE should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Data Gaps Flagged

1. **No third-party market-share percentage** for The Cheesecake Factory or its sister concepts vs. the broader casual-dining category — not disclosed by the company and no independent source with a precise share figure was found (only the Circana AUV ranking, which is a per-unit productivity metric, not a share-of-category metric). Non-blocking — the Moat Signal checklist treats this as a data gap (FALSE, not credited), consistent with "never invent or estimate," and the gate fails independently regardless.
2. **Q2 2026 quarterly figures** are not yet available (not yet filed as of this session) — the TTM window used (Q2 2025–Q1 2026) is the most current complete-quarter window obtainable; will roll forward at the next quarterly re-check (§6).
3. **Precise "Other operating costs and expenses" and "General and administrative expenses" sub-line breakdowns** were not decomposed further (e.g. into occupancy, marketing, utilities) — not needed for any formula in this session, since the framework's Margins sub-score only requires the food-and-beverage-cost line, and Profitability only requires net income/ROIC at the consolidated level.

None of these gaps affect the Quality Gate conclusion (§3.3), which is driven by well-sourced, primary-cited figures.

---

## 8. Sources

- SEC EDGAR: FY2025 10-K (accession 0001104659-26-018643), FY2024 10-K (accession 0001410578-25-000195), FY2023 10-K (accession 0001104659-24-027565), Q1 2026 10-Q (accession 0001104659-26-054987), Q3 2025 10-Q (accession 0001104659-25-105631), Q2 2025 10-Q (accession 0001410578-25-001564), and the Q1 2026 earnings 8-K (accession 0001104659-26-051574) — all CIK 887596.
- IBKR `search_contracts` / `get_price_snapshot` — live price, contract confirmation, 52-week statistics.
- FRED `DGS10` — 10Y Treasury yield (context only, not used this session).
- [The Cheesecake Factory, Chick-fil-A leads AUVs among major restaurant chains](https://www.restaurantdive.com/news/the-cheesecake-factory-chick-fil-a-leads-auvs-among-major-restaurant-chain/816023/) (Restaurant Dive, 2026, reporting on Circana's 2026 Definitive U.S. Restaurant Rankings) — third-party AUV ranking and Q4 2025 same-store sales figure cited in §2.7–2.8 and the Moat Signal checklist (§3.2).

---

## 9. Glossary

| Term | Meaning |
|---|---|
| **AUV (Average Unit Volume)** | The average annual sales generated by a single restaurant/store location. Full entry in [glossary.md](../framework/glossary.md) (originally added for McDonald's). CAKE's flagship concept has the #1 AUV among all major US restaurant chains per Circana (§2.8, §3.2). |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CIK (Central Index Key)** | The unique numeric identifier the SEC assigns to every company that files with EDGAR — used to construct the filing-lookup paths this framework pulls SEC data from. CAKE's CIK is 887596. |
| **Circana** | An independent market-research firm that publishes restaurant-industry data, including the annual "Definitive U.S. Restaurant Rankings" — the third-party (non-company-sourced) citation basis for CAKE's #1 average-unit-volume ranking used as Moat Signal "scale cost advantage" evidence in this session (§2.8, §3.2). *(New term.)* |
| **Comparable sales (comps / same-store sales)** | Sales growth at restaurant/store locations open at least a year (for CAKE, restaurants become eligible in their 19th month of operation), stripping out the effect of opening new units — the standard like-for-like organic-growth metric for restaurant chains. Full entry in [glossary.md](../framework/glossary.md). CAKE's comps decelerated at its two largest concepts over the two most recent fiscal years (§2.7). |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization — operating profit, and a rough proxy for cash operating profit, respectively. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check). CAKE's FCF/NI conversion dipped below 70% in FY2023/FY2024 but was defused by a documented growth-capex explanation (§2.6). |
| **Fox Restaurant Concepts (FRC)** | The Cheesecake Factory Incorporated's portfolio of additional, smaller restaurant brands (beyond its flagship Cheesecake Factory concept and North Italia) acquired in 2019 — referred to as "Other FRC" in the company's own segment/concept-level sales disclosures (e.g. "Other FRC sales increased 18.4%..." in the FY2025 10-K MD&A). Reported separately from Flower Child, which is also a Fox Restaurant Concepts brand but large enough to be broken out on its own line. *(New term.)* |
| **Hard disqualifier** | One of three Quality Score conditions that fail a company regardless of its weighted score. None fired for CAKE this session — the closest was the FCF/NI conversion check, defused by a documented growth-capex exception (§2.6, §3.1). |
| **Invested Capital** | The total capital (debt + equity, netted for cash) put to work in a business — the denominator in this framework's ROIC calculation. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; this framework's primary balance-sheet-risk gate. CAKE's is 1.314× (TTM), comfortably under the 2.5× threshold. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Net Margin** | Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit. CAKE's TTM Net Margin is 4.34% — thin, driving much of this session's Profitability sub-score. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. CAKE scored 49.5. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit; a core quality signal in this framework. CAKE's TTM ROIC is 20.22%. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. |
| **Systemwide sales** | Total sales across all restaurants operating under a chain's brand, franchised and company-operated combined. Full entry in [glossary.md](../framework/glossary.md); referenced conceptually here since CAKE's "comparable sales" and total revenue figures (§2.7) parallel this distinction (like-for-like vs. total-including-new-units). |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure. |
| **XBRL (eXtensible Business Reporting Language)** | The structured, machine-readable data format the SEC requires public companies to tag their financial-statement figures in — checked first this session (§2.1) but not used as the final source for cost-line figures, since the current-period "Food and beverage costs" concept wasn't consistently tagged; primary 10-K/10-Q text was read directly instead. |

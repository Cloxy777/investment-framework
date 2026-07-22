# NEW POSITION — RYAAY (Ryanair Holdings plc, Nasdaq ADR) — 2026-07-19

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 19 Jul 2026 (Sunday)
**10Y US Treasury Yield:** 4.57% (FRED `DGS10`, most recent posted observation dated 2026-07-16 — 07-17/07-18 not yet posted, normal FRED reporting lag; recorded for completeness only, since this session stops at the Quality Gate (§3) before the Rate Environment Gate would apply)
**Current RYAAY portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); grep for "ryaay"/"ryanair" (case-insensitive) returns no match)
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/RYAAY/` or `watchlist/not-in-portfolio/RYAAY/`, and no row in [watchlist/STALE.md](../watchlist/STALE.md), confirmed via `find`)
**Sector:** Industrials — Airlines (European ultra-low-cost carrier; parent of Ryanair DAC, Buzz, Lauda Europe, Malta Air, Ryanair UK)
**Filer type:** Foreign private issuer — CIK **1038683** ("RYANAIR HOLDINGS PLC," Nasdaq: RYAAY, ADR), reports annually on **Form 20-F** (fiscal year ends **March 31**) and furnishes unaudited full-year/interim results via **Form 6-K**; financial statements prepared under **IFRS** (EU-endorsed + IASB), reported in **EUR** — no quarterly 10-Q equivalent exists
**First-use jargon decode:** see closing Glossary (§9)

---

## 0. Why this session exists — trigger source

A post on **bolshegold** (Telegram, post bolshegold/9795, ~09:46 UTC 2026-07-19) listed RYAAY among companies "expected to report earnings this week," with a note to track "guidance and Hormuz situation" (the Middle East conflict's effect on jet fuel prices, discussed further in §4). Per the operating brief and this repo's standing convention, **Telegram post text is never used as financial data** — it is a trigger only. RYAAY has no existing watchlist entry in this repo and is not a current holding (confirmed via `grep`/`find` above), so per `/telegram-scan`'s first-ever-mention rule, **any first-ever mention of a name with no watchlist entry triggers a full `/new-position` evaluation, regardless of the mention's substance.** This session is that evaluation, built entirely from independently, primary-sourced data. (Ryanair's Q1 FY2027 trading update is separately confirmed, via web search, to be scheduled for Monday 20 July 2026 — i.e. the day *after* this session — so no Q1 FY27 figures exist yet and none are used below.)

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("RYAAY")`: contract_id **210918190**, exchange **NASDAQ**, description "RYANAIR HOLDINGS PLC-SP ADR" — the correct, unambiguous match (the other two results returned, `RYAAY.DIV` and `RYAAY.RDD`, are CORPACT record-date-position instruments tied to dividend processing, not tradable securities).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$66.36** | IBKR `get_price_snapshot`, `last` field, contract_id **210918190** (NASDAQ). `is_close: true` — this is the **last completed-session close**, not a live intraday trade, because today (Sunday 2026-07-19) markets are closed; per Rule 0 this is still the most recent price obtainable via a live fetch attempt, and is flagged here as a close rather than an intraday quote. |
| Prior close | $66.36 | IBKR `get_price_snapshot` `prior-close` field (identical to `last` — the prior trading session, Friday 2026-07-17, is both the "last" and "prior close" reference point over the weekend) |
| Bid/Ask | Empty (no live quote — market closed) | IBKR `get_price_snapshot` `bid_ask` field |
| 52-week high | $73.76 | IBKR `misc_statistics` `high_52w` |
| 52-week low | $53.14 | IBKR `misc_statistics` `low_52w` (also the 13-week and 26-week low) |
| 13-week high | $67.59 | IBKR `misc_statistics` `high_13w` |
| 26-week high | $72.56 | IBKR `misc_statistics` `high_26w` |
| Open 52 weeks ago | $56.28 | IBKR `misc_statistics` `open_52w` |
| Dividend yield | 1.49% | IBKR `get_price_snapshot` `dividend_yield` field |
| US 10Y Treasury yield | 4.57% | FRED `DGS10`, as-of 2026-07-16 (not used this session — see header) |

$66.36 sits roughly in the middle of its 52-week range ($53.14–$73.76), up **+17.9%** from the level 52 weeks ago ($56.28) — context only, not scored. This price is used for reference throughout this session; no order-setup arithmetic is performed, since the Quality Gate fails below (§3).

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

Ryanair Holdings plc is an Irish-domiciled **foreign private issuer** — it does not file US-style 10-K/10-Qs. Its primary Rule-0-compliant sources are: the **FY2026 Form 20-F** (fiscal year ended March 31, 2026; filed with the SEC 2026-06-22, accession **0001104659-26-076131**), and the **unaudited "Condensed Consolidated Preliminary" financial statements furnished as Form 6-K press releases** — specifically the **"Full Year FY26 Ryanair Holdings plc Earnings"** 6-K (accession **0001654954-26-005028**, furnished 2026-05-18, covering the year ended March 31, 2026 with March 31, 2025 comparatives) and the equivalent **FY25 full-year earnings 6-K** (accession **0001654954-25-005841**, furnished 2025-05-19, covering the year ended March 31, 2025 with March 31, 2024 comparatives). These preliminary-results 6-Ks contain the full income statement, balance sheet, cash flow statement, and MD&A in company-labeled IFRS line items — the same primary-source discipline this framework applies to a US 10-K/10-Q. The SEC's structured XBRL `companyfacts`/`companyconcept` API was checked first (`data.sec.gov/api/xbrl/companyfacts/CIK0001038683.json`) and used to cross-check FY2023–FY2025 revenue and net income figures (all matched the 6-K figures exactly), but **the FY2026 20-F's figures are not yet reflected in that API as of this session** (the bulk XBRL data lags the filing by data.sec.gov's own processing, not a Ryanair disclosure gap) — so FY2026 figures below are sourced directly from the 6-K press release text and MD&A, not the XBRL API. All figures are in **€ millions** unless stated otherwise; Ryanair reports in EUR, and no FX conversion is performed anywhere in this session since the Quality Score (Phase 01) uses no price/currency-denominated inputs at all — only the (unconverted) live USD ADR price in §1 is currency-specific, and it isn't used in any Phase 01 formula.

### 2.2 Income statement, FY2024–FY2026 (primary-sourced, € millions)

| Item | FY2024 (Mar '24) | FY2025 (Mar '25) | FY2026 (Mar '26) |
|---|---|---|---|
| Scheduled revenues | 9,145.1 | 9,229.8 | 10,556.0 |
| Ancillary revenues | 4,298.7 | 4,718.7 | 4,988.3 |
| **Total revenue** | **13,443.8** | **13,948.5** | **15,544.3** |
| Fuel and oil | 5,142.6 | 5,220.2 | 5,418.6 |
| Staff costs | 1,500.0 | 1,751.1 | 1,856.5 |
| Airport and handling charges | 1,484.5 | 1,683.5 | 1,762.3 |
| Depreciation | 1,059.5 | 1,214.4 | 1,373.4 |
| Route charges | 1,024.4 | 1,166.7 | 1,318.2 |
| Marketing, distribution and other | 757.2 | 878.4 | 803.5 |
| Maintenance, materials and repairs | 414.9 | 476.2 | 552.6 |
| Exceptional charge (Italian AGCM fine provision, see §2.7) | — | — | 85.0 |
| **Total operating expenses** | **11,383.1** | **12,390.5** | **13,170.1** |
| **Operating profit (EBIT)** | **2,060.7** | **1,558.0** | **2,374.2** |
| Net finance and other income | 61.8 | 224.0 | 80.0 |
| Foreign exchange gain/(loss) | 5.5 | 2.4 | (30.9) |
| Profit before tax | 2,128.0 | 1,784.4 | 2,423.3 |
| Tax expense | (210.9) | (172.8) | (249.6) |
| **Profit for the year (Net Income)** | **1,917.1** | **1,611.6** | **2,173.7** |
| Basic EPS (€) | 1.6828 | 1.4631 | 2.0594 |
| Weighted avg. basic shares (M) | 1,139.2 | 1,101.5 | 1,055.5 |

Source: FY26 full-year earnings 6-K (accession 0001654954-26-005028) for the FY2025/FY2026 columns, and FY25 full-year earnings 6-K (accession 0001654954-25-005841) for the FY2024 column — both companies' own "Condensed Consolidated Preliminary Income Statement" tables. **All figures used below are the GAAP/IFRS-actual, post-exceptional numbers** (e.g. Net Income €2,173.7M), not Ryanair's own non-GAAP "PAT pre-exceptional" figure of €2,258.7M quoted in its headline press release — consistent with this framework's standing rule to score off filed GAAP/IFRS figures rather than a company's self-adjusted metric (same treatment as Stellantis's AOI vs. its GAAP operating result, per [glossary.md](../framework/glossary.md)).

FY2023 revenue (€10,775.2M) and net income (€1,313.8M) cross-checked directly against the SEC XBRL `companyconcept` API (`ifrs-full:Revenue`, `ifrs-full:ProfitLoss`, tag history 2022-06-27/2024-06-27/2025-05-19 filings, all internally consistent to the decimal).

**Revenue 3yr CAGR (FY2023→FY2026):**
```
CAGR = (15,544.3 / 10,775.2)^(1/3) − 1 = (1.44262)^(0.3333) − 1 = 12.992%
```

### 2.3 Balance sheet — primary-sourced (FY26 earnings 6-K, "Condensed Consolidated Preliminary Balance Sheet as at March 31, 2026")

| Item (€M) | Mar 31, 2026 | Mar 31, 2025 |
|---|---|---|
| Cash and cash equivalents | 2,733.4 | 3,863.3 |
| Financial assets: cash > 3 months | 812.4 | 100.1 |
| Restricted cash | 31.2 | 23.1 |
| Current maturities of debt | 1,198.8 | 848.4 |
| Non-current maturities of debt | 147.8 | 1,685.2 |
| **Total debt** | **1,346.6** | **2,533.6** |
| Total shareholders' equity | 10,101.4 | 7,036.9 |
| Total assets | 19,747.7 | 17,507.0 |

```
Net Debt (Mar 2026) = Total Debt − Cash and cash equivalents = 1,346.6 − 2,733.4 = −1,386.8   (net CASH position)
Invested Capital     = Total Debt + Equity − Cash            = 1,346.6 + 10,101.4 − 2,733.4 = 8,714.6
EBITDA (FY26)         = EBIT + Depreciation = 2,374.2 + 1,373.4 = 3,747.6
Net Debt/EBITDA (FY26) = −1,386.8 / 3,747.6 = −0.370×   (net cash, not net debt)
```

Ryanair's own MD&A states: "Gross cash was €3.6BN at March 31, 2026 ... Net cash was €2.1BN at March 31, 2026" — its own gross-cash figure (~€3.6BN) additionally includes the "cash > 3 months" and "restricted cash" lines (2,733.4 + 812.4 + 31.2 = €3,577.0M ≈ €3.6BN), which this session's Net Debt/EBITDA calculation conservatively excludes (using only the "Cash and cash equivalents" line, consistent with this framework's standard convention elsewhere). Either way the company is in a **net cash position** — the company repaid its final €1.2BN bond in May 2026 and describes itself as "effectively debt free."

### 2.4 Cash flow — primary-sourced (each year's own 6-K "Condensed Consolidated Preliminary Statement of Cash Flows")

| Fiscal Year | Net cash from operating activities (€M) | CapEx — purchase of PP&E (€M) | FCF (€M) | Net Income (€M) | FCF/NI |
|---|---|---|---|---|---|
| FY2024 | 3,157.9 | 2,391.9 | **766.0** | 1,917.1 | **39.96%** |
| FY2025 | 3,415.7 | 1,552.5 | **1,863.2** | 1,611.6 | **115.61%** |
| FY2026 | 3,694.9 | 1,892.4 | **1,802.5** | 2,173.7 | **82.92%** |

Company has been **FCF-positive in all 3 of the most recent fiscal years** — clears the "FCF-positive 3+ consecutive years" hard-disqualifier test.

**FY2024's FCF/NI ratio (39.96%) sits well below the 70% hard-disqualifier line — examined below (§2.5) — but it is a single year, not part of a 2+ consecutive-year run** (FY2025 at 115.61% and FY2026 at 82.92% both clear 70% comfortably), so the hard disqualifier's literal "2+ consecutive years" condition is not met regardless of any growth-capex explanation.

### 2.5 FY2024 FCF/NI dip — context (not needed to clear the hard-disqualifier test, shown for completeness)

FY2024's elevated CapEx (€2,391.9M, the highest of the three years shown) coincides with heavy Boeing 737-8200 "Gamechanger" aircraft delivery activity disclosed in the FY26 6-K's fleet section — i.e. a genuine growth-capex year, not a maintenance-spend anomaly — but this context is not load-bearing for the gate outcome (§3.1), since the disqualifier requires two *consecutive* sub-70% years and only one exists in the three-year window examined.

### 2.6 Growth/TAM evidence — MD&A, primary-sourced (FY26 earnings 6-K)

Per the FY26 6-K's own MD&A/CEO commentary and "Fleet & Growth" section: the Group ordered "up to 300 (150 firm and 150 options) new Boeing 737-MAX-10 aircraft for delivery between 2027 to 2034" (approved at the Company's AGM, September 2023), and states explicitly: *"Industry capacity constraints, combined with our widening cost advantage, strong balance sheet, low-cost (fuel-efficient) aircraft orderbook and industry leading ops resilience will, we believe, facilitate Ryanair's profitable growth to over 300m passengers p.a. by FY34"* — up from 208.4m passengers carried in FY26, a documented, board-approved, firm-order-backed **+44% traffic/TAM expansion target** over an 8-year horizon. This is genuine, cited fleet-growth evidence (not a company aspiration without a contracted backing mechanism), separate from the pricing-power question addressed in the Moat Signal discussion below (§3.2).

Revenue growth itself is **accelerating, not decelerating**, over the three years shown: FY2024→FY2025 +3.8%, FY2025→FY2026 +11.4% — no structural-deceleration modifier applies.

### 2.7 Fare/traffic and cost context — MD&A, primary-sourced (FY26 earnings 6-K)

FY26 traffic grew 4% to 208.4m passengers (load factor flat at 94%) while average fares rose ~10% (scheduled revenue +14% on the same 4% traffic growth) — a price increase accompanied by **volume growth, not volume loss**. However, the company's own commentary frames this explicitly as "recovering last year's 7% fare decline" (FY2025 fares had *fallen* 7%) and as an industry-wide effect of "constrained EU short-haul capacity" rather than Ryanair-specific brand pricing power. The company's stated strategy is explicitly to pursue a **"load-active/yield-passive"** approach — i.e. traffic/load factor is the variable Ryanair actively manages, while fares are treated as a market-clearing residual, not a lever the company uses to extract a sustained premium. This is the opposite of a "brand premium" moat mechanism (see Moat Signal discussion, §3.2) — it is evidence of disciplined capacity management, not pricing power.

### 2.8 Market position — third-party (OAG), primary MD&A context

Per OAG's European Aviation Data (accessed via a July 2026 industry report): Ryanair is "the largest carrier in Europe" as of July 2026, operating 22.2 million seats — a **+6.3% increase vs. July 2025** — and 11.7 million more seats than easyJet, the second-largest European carrier (10.4 million seats). A separate, older third-party citation (Air Service One, June 2023, itself sourced from OAG capacity data) put Ryanair's intra-European capacity share at approximately 16% — dated, but directionally consistent context for the scale of the company's market position. The FY26 6-K's own MD&A corroborates continued share gains, attributing FY27 capacity growth to markets where "aviation taxes" have been cut, while explicitly "switching flights and routes away from uncompetitive high tax markets" — i.e. active, disclosed capacity reallocation toward growth markets, not passive share retention.

### 2.9 Exceptional item / Italian AGCM fine — MD&A, primary-sourced

In Q3 FY26, Italy's competition authority (AGCM) levied a €256M fine against Ryanair; the company's own FY26 results include an €85M (~33% of the fine) exceptional provision against it, while stating its lawyers are "confident this fine will be overturned on appeal." This session uses the **post-exceptional, GAAP-actual** Operating Profit (€2,374.2M) and Net Income (€2,173.7M) throughout (§2.2) — i.e. the €85M charge is **not** stripped out, consistent with this framework's standing rule against using a company's own non-GAAP-adjusted figures for scoring.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years without a documented growth-capex explanation | FY2024: 39.96% (single year, below 70%) · FY2025: 115.61% · FY2026: 82.92% (both above 70%) — **not a 2+ consecutive-year run** | disqualify only if 2+ *consecutive* years are sub-70% | ✅ **PASS** — condition not met (only one year sub-70%, not a consecutive run) |
| Net Debt/EBITDA over threshold (2.5× standard) | FY2026: **−0.370×** (net cash position, not net debt) | disqualify if >2.5× | ✅ **PASS**, by the widest possible margin — a negative ratio is the best possible outcome under this formula |
| FCF-positive 3+ consecutive years | FY2024 €766.0M · FY2025 €1,863.2M · FY2026 €1,802.5M — all positive, all three years shown | disqualify if not | ✅ PASS |

**No hard disqualifier fires.**

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (FY26) = 2,173.7 / 15,544.3 = 13.984%
  NetMargin_Component = clamp((13.984/30)×100, 0, 100) = 46.61

  Effective tax rate (FY26) = 249.6 / 2,423.3 = 10.30%
  NOPAT = EBIT × (1 − eff. tax rate) = 2,374.2 × (1 − 0.1030) = €2,129.7M
  Invested Capital = Total Debt + Equity − Cash = 1,346.6 + 10,101.4 − 2,733.4 = €8,714.6M
  ROIC = 2,129.7 / 8,714.6 = 24.44%
  ROIC_Component = clamp((24.44/30)×100, 0, 100) = 81.46

  Profitability_Score = (46.61 + 81.46) / 2 = 64.04   (no FCF-positivity cap — 3yr positive confirmed §2.4)

MARGINS (15% weight):
  Gross Margin construction: Ryanair (like most airlines) has no GAAP-labeled "Cost of Revenue"/"Gross
  Profit" line — its income statement instead breaks "Total operating expenses" into 7 discrete lines
  (Fuel and oil, Staff costs, Airport and handling charges, Depreciation, Route charges, Marketing/
  distribution/other, Maintenance/materials/repairs), plus an FY26 exceptional charge. This session uses
  **Fuel and oil + Airport and handling charges + Route charges** — the three cost lines most directly and
  variably tied to operating an individual flight — as the "direct flight-operating cost" analog, consistent
  with this framework's precedent of choosing the most direct "cost of the core product/service" line for a
  business without a conventional COGS line (e.g. CAKE's "Food and beverage costs only" construction,
  2026-07-17 session). Flagged as a construction choice, not an invented figure — see robustness check below.

  Gross Margin (FY26) = (15,544.3 − (5,418.6 + 1,762.3 + 1,318.2)) / 15,544.3
                       = (15,544.3 − 8,499.1) / 15,544.3 = 45.32%
  GrossMargin_Score = clamp((45.32/80)×100, 0, 100) = 56.65

  3yr trend check (same construction, FY2024→FY2026): 43.08% → 42.14% → 45.32% — non-monotonic (dipped in
  FY2025 before recovering), and already well above the 40% threshold the framework's +10 "structural
  expansion while below 40%" bonus is specifically gated on — the bonus is not eligible either way.

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2023→FY2026) = (15,544.3/10,775.2)^(1/3) − 1 = 12.99%
  Growth_Score (raw) = clamp((12.99/25)×100, 0, 100) = 51.97
  TAM-expansion modifier: +10 applies. Documented, cited evidence (§2.6): a firm 300-aircraft Boeing 737
  MAX-10 order (150 firm + 150 options, AGM-approved Sept. 2023) backing an explicit, disclosed company
  target of growing traffic from 208.4m (FY26) to over 300m passengers p.a. by FY34 (+44%) — genuine,
  contracted capacity-expansion evidence, not an aspirational statement alone. (Pricing-power evidence was
  separately considered and NOT used for this modifier — see Moat Signal discussion below; crediting the
  same fact under both Growth's TAM/pricing modifier AND Moat's Brand-premium signal would double-count it,
  and this session concluded the fare data doesn't support a genuine pricing-power reading regardless — see
  §3.2 Moat Signal and §2.7.)
  Growth_Score = clamp(51.97 + 10, 0, 100) = 61.97

  No deceleration modifier applies — revenue growth is accelerating (FY24→FY25 +3.8%, FY25→FY26 +11.4%),
  the opposite of the deceleration condition.

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (FY26) = −0.370× (net cash)
  BalanceSheet_Score = clamp(100×(1 − (−0.370)/4), 0, 100) = clamp(109.25, 0, 100) = 100.0

MOAT SIGNAL (15% weight) — 5-signal checklist, each evaluated against a specific citation:
  Market share stable/growing — TRUE. Per OAG's European Aviation Data (July 2026, third-party, non-
    company-sourced, §2.8): Ryanair is Europe's largest carrier, operating 22.2M seats in July 2026, up
    +6.3% year-on-year and 11.7M seats ahead of easyJet (the #2 European carrier, 10.4M seats) — a
    documented, independently-sourced, currently-growing lead over the field, not a self-reported or stale
    claim. Credited.

  Brand premium — FALSE. Considered carefully given FY26's ~10% average fare increase alongside +4%
    traffic growth (§2.7), which superficially resembles "price increase without volume loss." However,
    Ryanair's own MD&A frames the fare increase as *recovering* the prior year's 7% fare decline (a cyclical
    rebound tied to industry-wide capacity constraints), not a sustained brand-driven premium, and the
    company explicitly describes its own strategy as "load-active/yield-passive" — i.e. traffic volume is
    the actively-managed variable, and price is treated as a market-clearing residual, not a lever the
    company uses to capture a durable premium. This is the opposite of the evidentiary bar this checklist
    requires (a *durable* pricing-power mechanism, not a one-year cyclical fare recovery in a capacity-
    constrained market). Not credited.

  Network effect — FALSE. No two-sided-marketplace or user-growth-driven-value mechanism exists for a
    point-to-point, direct-to-consumer discount airline.

  Switching costs — FALSE. No loyalty-program lock-in, contractual retention mechanism, or integration/
    migration cost was found or is plausible for a low-cost, largely one-off-booking airline model; Ryanair
    itself does not market or rely on a proprietary loyalty-lock-in mechanism the way network-carrier loyalty
    programs do.

  Scale cost advantage — TRUE. Extensively and repeatedly documented in the company's own FY26 MD&A: a
    conservative jet-fuel hedging program (80% of FY27 requirements hedged at ~$67/bbl) explicitly described
    as widening "the cost advantage over EU competitors," an unencumbered 620-aircraft Boeing 737 fleet, a
    BBB+ (Fitch/S&P) investment-grade credit rating enabling cheaper capital than smaller/leveraged rivals,
    and explicit MD&A language: "this financial strength further widens the cost gap between Ryanair and our
    competitors, many of whom are exposed to expensive (long-term) finance, rising aircraft lease costs and
    unhedged jet-fuel." A genuine, structural, multiply-sourced (fuel hedging + fleet ownership + balance-
    sheet strength) scale/cost-structure advantage, not a one-off or self-reported claim without mechanism.
    Credited.

  Moat_Score = (2/5) × 100 = 40.0

FCF QUALITY (10% weight):
  FCF/NI (FY26) = 1,802.5 / 2,173.7 = 82.92%
  FCFQuality_Score = clamp(((0.8292 − 0.40)/0.60)×100, 0, 100) = clamp(71.54, 0, 100) = 71.54

QUALITY SCORE = 64.04×0.25 + 56.65×0.15 + 61.97×0.20 + 100.0×0.15 + 40.0×0.15 + 71.54×0.10
             = 16.010 + 8.498 + 12.394 + 15.000 + 6.000 + 7.154
             = 65.056 → rounds to 65.1 (boundary rule: exactly on ".X55"-adjacent value rounds per standard rounding here, no ".X5" tie)
```

**Robustness check (not just a point estimate).** Using the most generous alternate readings of the two most judgment-dependent inputs — Margins (using "Fuel and oil" alone as the cost-of-revenue analog, the single most generous defensible construction, giving Gross Margin 65.14% → GrossMargin_Score 81.43) and Moat (crediting a full 5/5, including Brand premium, Network effect, and Switching costs, despite this session finding **no defensible evidence** for three of those four signals):

```
64.04×0.25 + 81.43×0.15 + 61.97×0.20 + 100.0×0.15 + 100.0×0.15 + 71.54×0.10
= 16.010 + 12.215 + 12.394 + 15.000 + 15.000 + 7.154 = 77.77 → rounds to 77.8
```

**Still below the 80.0 gate even under this deliberately generous, largely non-defensible combination.** This figure is shown only to demonstrate the gate isn't failed by an unreasonably harsh reading of any single input — reaching even 77.8 requires crediting Moat signals (Brand premium, Network effect, Switching costs) this session found **no citable evidence** for, in tension with "never mark a signal true without a cited source." The **actual, evidence-based Quality Score is 65.1** (above), which fails the gate by nearly 15 points, and the robustness ceiling still falls 2.2 points short. This is not a marginal or close call.

### 3.3 Gate result

**Quality Score = 65.1 / 100.0 — FAILS the 80.0+ gate.** No hard disqualifier independently fires (§3.1 — Ryanair's balance sheet is a genuine net-cash position, and FCF-positivity is comfortably clean across all three years examined). The failure is driven by: thin-for-this-formula GAAP net margin (13.98% — a genuinely strong figure for an airline, but the framework's 30%-cap scoring scale was calibrated on asset-light business models and doesn't flatter airline-typical margins even at industry-leading levels), a Growth sub-score capped by the underlying formula's 25%-CAGR ceiling despite a real, accelerating, TAM-expansion-backed growth story, and — the single largest drag — a weak Moat Signal read (2 of 5; Market share and Scale cost advantage credited, but Brand premium specifically NOT credited despite an initially-plausible-looking fare/traffic pattern, because the company's own disclosed strategy and framing describe a cyclical fare recovery under a deliberately "yield-passive" posture, not a durable pricing-power mechanism). Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md): **stop here — do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or fair-value/order-setup work.**

---

## 4. Qualitative Notes

1. **Ryanair's balance sheet and cash-generation quality are genuinely excellent** — a net-cash position (Net Debt/EBITDA −0.37×) after repaying its final bond in May 2026, an unencumbered 620-aircraft fleet, and a BBB+ investment-grade credit rating from both Fitch and S&P. The gate failure here is **not** a leverage, solvency, or cash-quality story — Ryanair clears those bars as cleanly as almost any name this framework has evaluated.
2. **The core gap is the framework's Moat Signal checklist, calibrated more naturally to software/consumer-brand moats than to an airline's structural cost-based moat.** Ryanair's actual competitive advantage — the lowest unit cost base among European carriers, driven by fuel hedging discipline, fleet ownership/scale, and balance-sheet strength — is real, well-documented, and credited (Scale cost advantage). But three of the five checklist signals (Brand premium, Network effect, Switching costs) are structurally difficult for a point-to-point discount airline to ever satisfy, regardless of how dominant its cost position is — a low-cost carrier's business model is built on the *absence* of the brand-loyalty/lock-in mechanisms this checklist otherwise rewards. This is a genuine business-model characteristic, not a flaw in this session's evidence-gathering — flagged explicitly per this framework's "show every calculation, no black box" discipline, consistent with the CAKE and UNH sessions' margin/ROIC-formula-calibration caveats.
3. **The FY26 ~10% fare increase deserves the scrutiny this session gave it rather than an automatic "pricing power" credit.** Superficially, a fare increase alongside traffic growth looks like the textbook Moat Signal evidence bar ("price increases without volume loss"). But Ryanair's own MD&A explicitly frames the increase as a cyclical recovery from the prior year's 7% fare *decline*, driven by industry-wide capacity constraints rather than Ryanair-specific brand power, and the company's stated strategy — "load-active/yield-passive" — is explicitly the *opposite* of a brand-premium-pricing posture: Ryanair manages volume actively and treats price as a market-driven residual. Crediting this as durable pricing power would have been a stretch not supported by the company's own framing of its own results.
4. **The Q3 FY26 Italian AGCM antitrust fine (€256M, €85M provisioned) is a live legal/regulatory matter** — noted for completeness; it was included (not excluded) in this session's GAAP-actual Operating Profit and Net Income figures, and does not change the gate conclusion in either direction (the Quality Score fails by a wide enough margin that an €85M swing either way in a single year is immaterial to the outcome).
5. **The Telegram post's own framing — "guidance and Hormuz situation"** — refers to the ongoing Middle East conflict's effect on jet fuel prices; Ryanair's own FY26 release states global jet-fuel spot prices "have ... spiked to over $150bbl" and that ~80% of FY27 jet-fuel requirements are hedged at ~$67/bbl (insulating near-term earnings from the unhedged 20%), with management explicitly declining to give FY27 profit guidance "given zero H2 visibility and significant fuel price/potential supply volatility." This is genuine, current, material context for **why** this name was mentioned this week — but it is not itself scored or used in the Quality Score above, and no fair-value/order-setup work was performed this session regardless, since the Quality Gate fails first on its own terms.
6. **This session did not need to determine RYAAY's ADR-to-ordinary-share ratio** (unlike, e.g., the 2026-07-17 NOK cross-check) — no price-based valuation arithmetic is performed this session, since the Quality Score uses no price-denominated inputs, and the gate fails before any Phase 02 work that would require it.

---

## 5. Recommendation

# **PASS — Quality Gate FAIL (Quality Score 65.1 < 80.0). Do not enter.**

Ryanair Holdings clears every hard disqualifier (net-cash balance sheet, comfortably FCF-positive across all three years examined) and is a genuinely high-quality operator on several dimensions — industry-leading ROIC (24.44%), a real and structurally-documented cost-advantage moat, and an accelerating, contracted-capacity-backed growth trajectory. But it fails the strict 80.0+ Quality Score gate by a wide margin (nearly 15 points, and still ~2 points short even under a deliberately generous, largely non-defensible robustness reading): thin-relative-to-formula GAAP net margin, and — the single largest driver — a weak Moat Signal read (2 of 5) driven by the framework's checklist being structurally difficult for a low-cost, point-to-point airline business model to satisfy on the brand/network/switching-cost dimensions, regardless of how dominant its cost-based moat actually is. **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed** — this session stops at the Quality Gate per the command specification. The triggering Telegram post (a routine "reporting this week" mention, flagging the Hormuz/fuel-price backdrop) was used only as the reason to run this first-ever evaluation and was not relied upon for any conclusion.

---

## 6. Next Review Trigger

No routine re-check is scheduled (Phase 01 FAIL, no numeric Phase 02 score to go stale). Re-evaluate on any of the following Rule 9-style fundamental triggers:
- **RYAAY's Q1 FY2027 trading update**, confirmed via web search to be scheduled for **Monday 20 July 2026** (the day immediately after this session) — will show the initial read on FY27 fares/traffic and the actual (vs. hedged-forecast) impact of the Middle East conflict on unhedged jet-fuel costs.
- **Any material change in the MAX-10 delivery schedule or the 300m-passengers-by-FY34 growth target** — a material slippage or acceleration would directly change the Growth sub-score's TAM-expansion modifier basis used this session (§2.6, §3.2).
- **Resolution (either direction) of the Italian AGCM antitrust appeal** (€256M fine, €85M provisioned) — a materially different outcome than the €85M provision assumes would be a Rule 9 fundamental trigger.
- A management change (note: CEO Michael O'Leary's contract extension discussions, through April 2032, were reported as "almost concluded" in the FY26 release — a resolution either way is a Rule 9-relevant governance event), material M&A, a macro/rate shift, or a >15% unexplained price move (the current $53.14–$73.76 52-week range reflects real Middle-East-conflict-driven volatility already, not an unexplained move).
- **FY2027 fiscal year-end close** (~May 2027 report) — replaces FY2023 in the 3yr Revenue CAGR window and gives a fourth consecutive year of fare/traffic data to confirm whether the FY26 fare "recovery" (§2.7) proves durable or reverses.

Absent any of the above, a future Telegram mention of RYAAY should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Data Gaps Flagged

1. **No SEC XBRL-structured data for the FY2026 20-F** (filed 2026-06-22) was available via `data.sec.gov`'s `companyfacts`/`companyconcept` API as of this session — worked around by reading the FY26 full-year earnings 6-K's own "Condensed Consolidated Preliminary" financial statements directly (§2.1), which are primary-sourced, company-furnished figures, not a third-party estimate. Non-blocking.
2. **Q1 FY2027 figures** are not yet available (results scheduled for the day after this session — §0, §6) — FY2026 (year ended March 31, 2026) is the most current complete-fiscal-year data obtainable, and (since Ryanair's fiscal year just closed) requires no TTM/quarterly reconstruction the way a US calendar-quarter filer would.
3. **No precise, current-dated third-party intra-European market-share percentage** was found for FY2026 specifically — the most precise share figure available (≈16% intra-European, Air Service One/OAG) is from June 2023, three years stale. The July 2026 OAG seat-capacity comparison (§2.8) is current and was used as the primary Moat Signal citation instead, since it's independently sourced and dated to this session's period, even though it's a capacity (not passenger-share) metric. Non-blocking — the Moat Signal was still credited TRUE on this basis, and the gate fails independently of this signal's inclusion or exclusion.
4. **Ryanair's ADR-to-ordinary-share ratio** was not determined this session (§4, note 6) — not needed, since no price-denominated calculation was performed.

None of these gaps affect the Quality Gate conclusion (§3.3), which is driven by well-sourced, primary-cited figures and a comfortable (65.1 vs. 80.0, and 77.8 even under a generous robustness reading) margin.

---

## 8. Sources

- SEC EDGAR: FY2026 Form 20-F (CIK 1038683, accession 0001104659-26-076131, filed 2026-06-22); FY26 full-year earnings Form 6-K (accession 0001654954-26-005028, furnished 2026-05-18); FY25 full-year earnings Form 6-K (accession 0001654954-25-005841, furnished 2025-05-19).
- SEC XBRL `companyconcept`/`companyfacts` API (`data.sec.gov/api/xbrl/companyfacts/CIK0001038683.json`) — used to cross-check FY2023–FY2025 Revenue and Profit/Loss figures against the 6-K press releases (all matched exactly); FY2026 figures not yet reflected in this API as of this session (§2.1, §7).
- IBKR `search_contracts` / `get_price_snapshot` — live price, contract confirmation, 52-week statistics, dividend yield.
- FRED `DGS10` — 10Y Treasury yield (context only, not used this session).
- Web search: Ryanair Q1 FY2027 earnings-date confirmation (20 July 2026); OAG European Aviation Data (July 2026 European carrier capacity comparison, via industry reporting); Air Service One (June 2023, intra-European market share, via OAG-sourced data).

---

## 9. Glossary

| Term | Meaning |
|---|---|
| **ADR (American Depositary Receipt)** | Full entry in [glossary.md](../framework/glossary.md). RYAAY is Ryanair Holdings plc's US-exchange-listed ADR; this session did not need to determine its underlying ordinary-share ratio (§4). |
| **AGCM (Autorità Garante della Concorrenza e del Mercato)** | Italy's national competition/antitrust regulator. Levied a €256M fine against Ryanair in Q3 FY26 (under appeal); Ryanair's FY26 results include an €85M exceptional provision against it (§2.9). *(New term.)* |
| **Ancillary revenue** | An airline's non-ticket revenue — priority boarding, reserved seats, baggage fees, car hire, travel insurance, and similar add-ons — distinct from "scheduled revenue" (the base fare). Ryanair's ancillary revenue rose 6% to €4.99BN (€24/passenger) in FY26 (§2.2). *(New term.)* |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CIK (Central Index Key)** | The unique numeric identifier the SEC assigns to every company that files with EDGAR. Ryanair's CIK is 1038683. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization — operating profit, and a rough proxy for cash operating profit, respectively. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check). RYAAY's FCF/NI conversion dipped to 39.96% in FY2024 (a single year, not a disqualifying 2+ consecutive-year run — §2.4). |
| **Form 20-F** | Full entry in [glossary.md](../framework/glossary.md) — the annual report US-listed foreign private issuers file with the SEC, the international equivalent of a 10-K. |
| **Form 6-K** | Full entry in [glossary.md](../framework/glossary.md) — a furnished report foreign private issuers use to disclose material information between annual 20-Fs, roughly the international equivalent of an 8-K. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. None fired for RYAAY this session (§3.1). |
| **IFRS (International Financial Reporting Standards)** | Full entry in [glossary.md](../framework/glossary.md) — the accounting standard Ryanair (and most non-US companies) use for audited financial statements, as opposed to US GAAP. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) put to work in a business — the denominator in this framework's ROIC calculation. |
| **Load factor** | The percentage of available airline seats actually filled with paying passengers — Ryanair's load factor was flat at 94% in both FY2025 and FY2026 (§2.7), among the highest in the industry. *(New term.)* |
| **"Load-active/yield-passive" strategy** | Ryanair's own stated capacity-management strategy: actively managing traffic volume/load factor as the primary lever, while treating average fare (yield) as a market-clearing residual rather than a lever the company uses to extract a sustained price premium — cited in this session as the reason FY26's fare increase was NOT credited as Moat Signal "Brand premium" evidence (§2.7, §3.2). *(New term.)* |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; this framework's primary balance-sheet-risk gate. RYAAY's is **negative** (−0.370×, FY26) — a net-cash position, not net debt. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Net Margin** | Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit. RYAAY's FY26 Net Margin is 13.98%. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. RYAAY scored 65.1. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit. RYAAY's FY26 ROIC is 24.44%. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. |
| **TAM (Total Addressable Market)** | The total revenue opportunity available to a business if it captured its entire relevant market. Ryanair's own disclosed 300m-passengers-by-FY34 target (from 208.4m in FY26), backed by a firm 300-aircraft order, was credited as documented TAM-expansion evidence for the Growth sub-score modifier (§2.6, §3.2). |

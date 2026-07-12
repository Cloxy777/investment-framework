# NEW POSITION — TSM (Taiwan Semiconductor Manufacturing Company Limited, NYSE ADR) — 2026-07-12

**Task type:** NEW POSITION (Telegram-scan trigger)
**Date:** 12 Jul 2026 (Sunday — markets closed since Fri 10 Jul; most recent completed session's close used as the live price, per Rule 0)
**10Y US Treasury Yield:** 4.54% (FRED `DGS10`, most recent posted observation dated 2026-07-09, page shows "Updated: Jul 10, 2026" — normal 1-day FRED reporting lag)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current TSM portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is TSM's first-ever `/new-position` evaluation under this framework.
**Sector:** Technology — Semiconductors (dedicated/"pure-play" foundry — contract chip manufacturing, not a fabless chip designer)
**Filer type:** Foreign private issuer — TSMC files an annual **Form 20-F** (not a 10-K) and furnishes quarterly/interim results via **Form 6-K** (not 8-K/10-Q) with the SEC (CIK 1046179), reporting under Taiwan-IFRS in **NT$ (New Taiwan Dollar)**. All USD figures below are computed from NT$-denominated primary filings, converted at disclosed or live FX rates — never assumed. **ADR ratio: 1 ADR = 5 ordinary ("common") shares** of TSMC (Taiwan Stock Exchange: 2330.TW) — confirmed via a cited SEC Form 3 filing and cross-validated internally against this session's own share-count and EPS arithmetic (see §1, §2.6).
**First-use jargon decode:** see closing Glossary (§10).

---

## 0. Why this session exists — trigger source

A Telegram post on the **tarasguk** channel (post #11357, ~10:03 UTC 2026-07-12, edited) named **TSM alongside ASML and NFLX** as three companies "of particular interest heading into the upcoming earnings season." Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only, verified independently below.

**Independent verification:** TSMC's **Q2 2026 earnings conference is scheduled for Thursday, 16 July 2026** (14:00 Taiwan time / 02:00 US Eastern) — four days after this session — confirmed via TipRanks and Yahoo Finance/TradingView coverage. The Telegram post's "earnings season" framing is accurate and directionally useful; it carried no analytical content beyond naming the ticker.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$434.11** | IBKR `get_price_history` (contract_id **6223250**, NYSE, "TAIWAN SEMICONDUCTOR-SP ADR", exact-symbol US primary listing confirmed via `search_contracts`), daily bar close for **2026-07-10** (most recent completed trading session — today, 2026-07-12, is a Sunday) |
| ⚠️ Tooling flag | `get_price_snapshot`'s `last` field returned **$436.96** (`is_close: true`) — this matches the **2026-07-09** close in `get_price_history`, one session stale, the same recurring `get_price_snapshot`-staleness pattern flagged in prior sessions (e.g. 2026-07-05 NVO). `plprice` (mark) showed $435.80, between the two. Resolved by using `get_price_history`'s freshest daily bar. |
| Independent cross-check | **$434.11** | Multiple independent sources agree exactly: stockanalysis.com ("Last checked Jul 11, 2026," close timestamped "Jul 10, 2026, 4:00 PM EDT"), a WebSearch news snippet ("TSM...closed at $434.11, down 0.7%"), and a GuruFocus article headline explicitly citing "$434.11" |
| Today's change (2026-07-10 vs 07-09) | −0.65% to −0.7% (multiple sources agree) | stockanalysis.com / WebSearch |
| 52-week range | $221.332 (low) – $478.89 (high) | IBKR `get_price_snapshot` `misc_statistics` |
| Dividend yield (live) | 0.8% | IBKR `get_price_snapshot` `dividend_yield` — cross-checked against 0.64% (stockanalysis.com) and 0.63–0.87% (other vendors); used IBKR's live figure as the primary Rule-0-compliant source, per this framework's stated broker-data preference |
| Analyst consensus PT | **$490.34** (37 analysts, "Strong Buy") | stockanalysis.com `/forecast` page, dated this session |
| US 10Y Treasury yield | 4.54% | FRED `DGS10`, as-of 2026-07-09 |
| USD/TWD FX | **32.08** (live, 2026-07-12) | Xe.com mid-market rate — cross-checked against 32.107 (2026-07-10 close, multiple sources) |

**$434.11 is used as the live price for all arithmetic below.**

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

TSMC's Q2 2026 6-K earnings release is not yet filed (reports 16 Jul 2026). All financial data below is sourced from: (a) TSMC's own primary SEC 6-K quarterly earnings releases (Q1 2025 through Q1 2026 — the most current filed quarter) for **income-statement** figures, cited by exact SEC EDGAR URL per quarter; (b) stockanalysis.com's balance-sheet and cash-flow pages for **balance-sheet and cash-flow** line items not disclosed in TSMC's own earnings-release press documents (TSMC's quarterly earnings release contains only a summary income-statement table — confirmed by direct inspection, no balance sheet/cash flow in that document; the fuller financial statements are filed as PDF exhibits that this session's tooling could not parse — see §2.2 note); and (c) TSMC's own FY2025 Form 20-F press announcement and multiple third-party analyst/press sources for qualitative moat/growth evidence, each cited individually.

### 2.2 PDF-parsing limitation (disclosed)

TSMC's "4Q25 Management Report" (the fuller financial-statements PDF filed alongside the earnings release) could not be parsed this session — `WebFetch` returned raw, undecoded PDF binary, and the local `Read` tool's PDF-rendering path (`pdftoppm`/poppler-utils) is not installed in this environment. Balance-sheet and cash-flow figures were sourced instead from stockanalysis.com's quarterly financial-statement pages, which are **internally consistent with this session's primary-sourced income-statement/EPS figures** (see the cross-check in §2.6 — vendor "Diluted Shares Outstanding: 5,186M" ties out exactly to 25,931M primary-sourced weighted-average common shares ÷ 5). Flagged transparently rather than silently treated as equally authoritative as the SEC-filed income-statement figures.

### 2.3 Quarterly income statement — primary-sourced (SEC EDGAR 6-K filings)

| Quarter | Revenue (NT$M) | Revenue (US$B, as reported) | Gross Profit (NT$M) | GM% | Op. Income (NT$M) | OM% | Pretax Income (NT$M) | Net Income (NT$M) | NM% | EPS (NT$, common share) | EPS (US$, per ADR) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 2025 | 839,250 | 25.53 | 493,395 | 58.8% | 407,081 | 48.5% | 430,895 | 361,564 | 43.1% | 13.94 | 2.12 |
| Q2 2025 | 933,790 | 30.07 | 547,370 | 58.6% | 463,420 | 49.6% | 493,040 | 398,270 | 42.7% | 15.36 | 2.47 |
| Q3 2025 | 989,918 | 33.10 | 588,543 | 59.5% | 500,685 | 50.6% | 525,369 | 452,302 | 45.7% | 17.44 | 2.92 |
| Q4 2025 | 1,046,090 | 33.73 | 651,987 | 62.3% | 564,903 | 54.0% | 592,363 | 505,744 | 48.3% | 19.50 | 3.14 |
| Q1 2026 | 1,134,103 | 35.90 | 751,295 | 66.2% | 658,966 | 58.1% | 687,800 | 572,480 | 50.5% | 22.08 | 3.49 |

Sources (each fetched directly): [Q1 2025 6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617925000035/a1q25e_withguidancexfinal.htm), [Q2 2025 6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617925000082/a2q25e_withguidancexfinal.htm), [Q3 2025 6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617925000116/a3q25e_withguidancexfinal.htm), [Q4 2025 6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000008/a4q25e_withguidancexfinal.htm), [Q1 2026 6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000199/a1q26e_withguidancexfinal.htm). **Internal consistency check:** in each quarter, 5×(NT$ EPS)÷(implied quarterly FX) ≈ US$ EPS per ADR (e.g. Q1 2026: 5×22.08/31.7 ≈ $3.48, matches the reported $3.49) — confirms the 1-ADR:5-common-share ratio directly from the company's own dual-currency disclosure, independent of the third-party citation in the header.

### 2.4 TTM reconstruction (Q2 2025 + Q3 2025 + Q4 2025 + Q1 2026)

```
Revenue (NT$M) = 933,790 + 989,918 + 1,046,090 + 1,134,103 = 4,103,901
Revenue (US$B, as-reported each quarter) = 30.07+33.10+33.73+35.90 = 132.80   → implied TTM avg FX = 4,103,901/132,800 = 30.90
Gross Profit (NT$M) = 547,370+588,543+651,987+751,295 = 2,539,195   → Gross Margin TTM = 2,539,195/4,103,901 = 61.88%
Operating Income (NT$M) = 463,420+500,685+564,903+658,966 = 2,187,974   → Operating Margin TTM = 53.32%
Pretax Income (NT$M) = 493,040+525,369+592,363+687,800 = 2,298,572
Net Income (NT$M) = 398,270+452,302+505,744+572,480 = 1,928,796   → Net Margin TTM = 47.01%
EPS TTM (US$/ADR, summed) = 2.47+2.92+3.14+3.49 = $12.02   (cross-checks exactly against Finviz's independently-reported "EPS ttm: $12.03")
Effective tax rate TTM = (2,298,572−1,928,796)/2,298,572 = 16.09%
```

### 2.5 Balance sheet & cash flow — vendor-sourced (stockanalysis.com), cross-checked internally

| | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 (most current) |
|---|---|---|---|---|
| Cash & equivalents (NT$M) | 2,364,520 | 2,470,760 | 2,767,860 | 3,035,640 |
| Total Debt (NT$M) | 1,009,250 | 1,025,430 | 1,064,580 | 1,016,270 |
| Total Equity (NT$M) | 4,616,630 | 5,035,580 | 5,396,220 | 5,932,390 |
| Operating CF (NT$M) | 497,064 | 426,829 | 725,509 | 698,976 |
| CapEx (NT$M) | 297,226 | 287,452 | 356,906 | 350,763 |
| Free Cash Flow (NT$M) | 199,838 | 139,377 | 368,603 | 348,213 |
| D&A (NT$M) | 188,058 | 162,787 | 162,112 | 165,450 |

```
TTM OCF = 497,064+426,829+725,509+698,976 = 2,348,378
TTM CapEx = 297,226+287,452+356,906+350,763 = 1,292,347
TTM FCF = 2,348,378 − 1,292,347 = 1,056,031
TTM D&A = 188,058+162,787+162,112+165,450 = 678,407
TTM EBITDA = TTM Op. Income + TTM D&A = 2,187,974 + 678,407 = 2,866,381
FCF/NI (TTM) = 1,056,031 / 1,928,796 = 54.75%

Net Debt (Q1 2026, most current) = Total Debt − Cash = 1,016,270 − 3,035,640 = −2,019,370 (i.e. a NET CASH position of ~NT$2.02 trillion)
Net Debt/EBITDA (TTM) = −2,019,370 / 2,866,381 = −0.70×  (net cash, not net debt)
```

### 2.6 Shares outstanding / ADR ratio cross-check

```
Weighted-avg diluted COMMON shares (Q1 2026 6-K, primary) = 25,931M
÷ 5 (ADR ratio) = 5,186.2M ADR-equivalent shares
Cross-check: stockanalysis.com's annual "Diluted Shares Outstanding" column shows a constant 5,186M across FY2021–FY2025 — matches to the decimal.
```
**Market Cap (ADR basis)** = $434.11 × 5,186.2M = **$2,251,381M** ($2.251 trillion)
**Net Debt (USD, at live FX 32.08)** = −2,019,370 / 32.08 = **−$62,957M**
**EV** = Market Cap + Net Debt = 2,251,381 − 62,957 = **$2,188,424M**

### 2.7 Annual figures FY2021–FY2025 (vendor-sourced, stockanalysis.com — used for 3yr CAGR and 5yr PE range only; TTM/quarterly figures above are the primary-sourced basis for scoring)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Revenue (NT$M) | 1,587,420 | 2,263,890 | 2,161,740 | 2,894,310 | 3,809,050 |
| Gross Margin | 51.63% | 59.56% | 54.36% | 56.12% | 59.89% |
| Net Income (NT$M, vendor) | 592,359 | 992,923 | 851,740 | 1,158,380 | 1,697,600 |
| Diluted EPS (NT$, ADR-equiv.) | 114.20 | 191.45 | 164.25 | 223.35 | 327.35 |
| Annual PE (vendor) | 26.73 | 11.44 | 18.05 | 24.06 | 23.40 |

⚠️ **Vendor/primary variance flagged:** primary-sourced quarterly SEC filings sum to **FY2025 net income NT$1,717,880M** (361,564+398,270+452,302+505,744), ~1.2% above the vendor's annual figure (1,697,600M) shown in the table above. The variance is immaterial to every score computed in this session (both FCF/NI conversion and any ratio using FY2025 NI move by <1.5pp either way) and is disclosed rather than silently reconciled — the **primary quarterly sum (1,717,880M) is treated as the more authoritative figure** and used wherever FY2025 NI appears below (§3.2 hard-disqualifier table).

**Revenue 3yr CAGR (FY2022→FY2025):** `(3,809,050/2,263,890)^(1/3) − 1 = 18.94%`
**5yr PE range (2021–2025, annual):** Avg **20.74×**, Low **11.44×** (2022), High **26.73×** (2021) — a genuine annual low/high range (not just an average), so the **primary FwdPE formula** applies (§5.3).

### 2.8 Forward PE / forward EPS — wide vendor dispersion, flagged

| Source | Forward PE | Implied Forward EPS (ADR) |
|---|---|---|
| Finviz | 21.36 | $20.32 |
| stockanalysis.com (main stats page) | 22.24 | $19.52 |
| A market-commentary article (Yahoo Finance/247wallst, "$500 by year end") | ~30× (cited directly) | $14.50 |
| MarketBeat | n/a (implausibly low "FY2026: $11.07," below TTM $12.02 already achieved) | discarded — inconsistent with TSM's own Q1 2026 beat and guided ~30%+ FY2026 USD revenue growth |

**Two independently-labeled data-vendor sources (Finviz, stockanalysis.com) corroborate each other closely (21.36× and 22.24×, ~4% apart)** and both independently cross-check against this session's own primary-sourced TTM EPS ($12.03 Finviz vs. $12.02 computed here in §2.4) — strong confirmation their pipeline is sound for this ticker. **Used: Forward PE = 21.80× (average of the two corroborating sources)**, flagging the wider dispersion (MarketBeat discarded as implausible/stale; the $14.50/30× figure from news commentary noted but not used, as it carries no stated methodology or as-of date).

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ **consecutive** years w/o growth-capex explanation | FY2023: 292,150/851,740 = **34.3%** (fail) · FY2024: 870,169/1,158,380 = **75.1%** (pass) · FY2025: 1,002,565/1,717,880 = **58.4%** (fail) · TTM: **54.75%** (fail) | disqualify if 2+ **consecutive** years <70% w/o carve-out | ⚠️ **Close call, but does NOT fire on a strict reading** — FY2024 (75.1%) breaks the streak between FY2023 and FY2025, so there are not 2 *consecutive* full fiscal years below 70%. **Flagged as a monitoring item, not a clean pass** — TTM (54.75%) and FY2025 (58.4%) are both currently below 70%, so a second consecutive **sub-70% year** would exist if FY2026 comes in similarly low. **A growth-capex carve-out would apply regardless**, and is extensively documented: TSMC's own 2026 capex guidance is **US$52–56 billion**, explicitly earmarked for advanced-node capacity (2nm/N2, A16) and new fabs (Arizona, Japan, Germany) to meet AI/HPC demand — not maintenance capex. |
| Net Debt/EBITDA over threshold (2.5× standard) | TTM: **−0.70×** (net CASH position, not net debt) | disqualify if >2.5× | ✅ PASS, overwhelmingly |
| FCF-positive 3+ consecutive years | FY2023 NT$292,150M · FY2024 NT$870,169M · FY2025 NT$1,002,565M — all positive | disqualify if not | ✅ PASS |

**No hard disqualifier fires.** The FCF/NI conversion check is genuinely borderline and worth re-checking at the FY2026 close (see §9), but on the framework's literal "2+ consecutive years" test it does not currently trigger, and even a stricter reading would be carved out by TSMC's extensively documented, AI/HPC-driven capacity-expansion capex program.

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = 47.01%
  NetMargin_Component = clamp((47.01/30)×100, 0, 100) = clamp(156.7, 0, 100) = 100.0

  NOPAT = EBIT_TTM × (1 − eff. tax rate) = 2,187,974 × (1 − 0.1609) = NT$1,835,951M
  Invested Capital = Total Debt + Equity − Cash (Q1 2026) = 1,016,270 + 5,932,390 − 3,035,640 = NT$3,913,020M
  ROIC = 1,835,951 / 3,913,020 = 46.92%
  ROIC_Component = clamp((46.92/30)×100, 0, 100) = clamp(156.4, 0, 100) = 100.0
  *(Sanity cross-check: ROE = NI_TTM/Equity = 1,928,796/5,932,390 = 32.51% — the ROIC figure above reads higher than ROE
    because TSMC's cash pile exceeds its total debt, shrinking the Invested-Capital base below Equity alone; a known,
    disclosed quirk of the framework's debt+equity−cash convention for a heavily net-cash company, not an error.)*

  Profitability_Score = (100.0 + 100.0) / 2 = 100.0   (no FCF-positivity cap — 3yr positive confirmed above)

MARGINS (15% weight):
  Gross Margin (TTM) = 61.88%
  GrossMargin_Score = clamp((61.88/80)×100, 0, 100) = 77.35   (no trend bonus needed — already well above 40%)

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022→FY2025) = 18.94%
  Growth_Score = clamp((18.94/25)×100, 0, 100) = 75.8
  TAM/pricing-power modifier: +10 applied — documented evidence: (a) overall foundry market share rising
    66% (2025 pure-play, IDC forecast) → 70.4% (Q4 2025) → 72.3% (Q1 2026), a genuine multi-quarter increasing
    trend (Focus Taiwan/IDC, Dataconomy, Taipei Times); (b) reported advanced-node wafer price increases
    (3–10%, some reports up to 10% for AI-related nodes; 2nm wafers reportedly approaching ~$30,000 vs. ~$20,000
    for 3nm) across "all advanced nodes" (~74% of wafer revenue), consistent with the company's own Q1 2026
    call language citing "early pricing increases on advanced nodes" feeding Q2 2026 guidance (Tom's Hardware,
    WCCFTech, SemiWiki, Bits&Chips).
  Growth_Score = clamp(75.8 + 10, 0, 100) = 85.8

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM) = −0.70×
  BalanceSheet_Score = clamp(100×(1 − (−0.70)/4), 0, 100) = clamp(117.6, 0, 100) = 100.0

MOAT SIGNAL (15% weight) — checklist, cited evidence only:
  Market share stable/growing:  TRUE — see Growth TAM citation above (66%→70.4%→72.3%, increasing).
  Brand premium (pricing power): TRUE — advanced-node price increases (above) landing without evident
    share loss (share is *rising* over the same period); rival Samsung "routinely undercuts TSMC wafer
    pricing" yet continues to lose share — evidence the premium reflects genuine differentiation, not a
    price umbrella competitors are simply matching (tomshardware.com "TSMC vs Samsung vs Intel" coverage).
  Network effect:  FALSE — a dedicated foundry is a single-sided manufacturing service, not a two-sided
    marketplace; no user-growth-driven value mechanism is documented distinct from the switching-cost
    ecosystem credited below (not double-counted across two checklist rows).
  Switching costs:  TRUE — multiple independent citations describe redesign/requalification costs of an
    estimated $2–5B for a major customer (e.g. Apple) to move to a competing foundry, and ~$100M per
    single "re-spin," driven by tight coupling between a chip design and TSMC's specific process design
    kits (PDKs); reinforced by TSMC's Open Innovation Platform (OIP) ecosystem — 93,000+ certified IP
    titles (up from 3,000 in 2010), 30 EDA + 38 IP + 23 design-center-alliance partners (SemiWiki,
    Synopsys/TSMC OIP press materials, prnewswire.com).
  Scale cost advantage:  TRUE — Intel's own reported yields run 5–15 percentage points below TSMC's
    mature 3nm process (65–75% vs. TSMC's higher yields), with Intel not expected to reach "industry-
    standard" yields until 2027 and posting a $2.4B Q1 2026 Intel Foundry operating loss; multiple analyst
    sources describe TSMC as uniquely positioned to keep driving down 2nm costs via its yield lead and
    shipping volume (tomshardware.com, patentpc.com, semiwiki.com).
  Moat_Score = (4/5) × 100 = 80.0

FCF QUALITY (10% weight):
  FCF/NI (TTM) = 54.75%
  FCFQuality_Score = clamp(((0.5475 − 0.40)/0.60)×100, 0, 100) = clamp(24.58, 0, 100) = 24.6

QUALITY SCORE = 100.0×0.25 + 77.35×0.15 + 85.8×0.20 + 100.0×0.15 + 80.0×0.15 + 24.6×0.10
             = 25.00 + 11.60 + 17.16 + 15.00 + 12.00 + 2.46
             = 83.22 → rounds to 83.2
```

**Quality Score = 83.2 / 100.0 — clears the 80.0+ gate.** Exceptional profitability, margins, balance sheet (all saturate or near-saturate at 100.0), and one of the strongest documented Moat Signal readings scored in this repo (80.0, 4-of-5). The single meaningfully weak sub-score is FCF Quality (24.6/100) — a direct, well-explained consequence of TSMC's record capex supercycle (see §3.1), not an earnings-quality red flag in the Valeant/Wirecard sense.

**Gate result: PASS.** Per operating-brief.md/quality-scoring.md: proceed to the Rate Environment Gate and Phase 02 valuation scoring.

---

## 4. Rate Environment Gate

```
Step 1 — Earnings Yield Spread Test
Forward PE = 21.80× (blended corroborating vendor pair, §2.8)
EY = 1 / 21.80 = 4.587%
Spread = EY − 10Y Treasury = 4.587% − 4.54% = +0.047%
Threshold: Spread ≥ +1.5% → PASS (no addition). Spread < +1.5% → FAIL → additive +5.
Result: FAIL → +5
```

**Robustness check:** using either individual corroborating source instead of the blended average — Finviz's 21.36× (EY 4.682%, spread +0.142%) or stockanalysis.com's 22.24× (EY 4.496%, spread **−0.044%**) — **both independently still FAIL Step 1.** The conclusion is robust across the plausible range of sourced Forward PE, even though the exact spread magnitude is sensitive to which figure is used.

```
Step 2 — Rate Regime Modifier
10Y = 4.54% → 3.5–5% bracket → +5
```

**Combined Rate Gate additions: +5 (Step 1) + 5 (Step 2) = +10**

---

## 5. Phase 02 — Valuation Score

### 5.1 FCF Yield (40% weight)

```
FCF Yield = TTM FCF (USD) / Market Cap
TTM FCF (USD) = NT$1,056,031M / 30.90 (TTM-implied avg FX, §2.4) = $34,175.6M
FCF Yield = 34,175.6 / 2,251,381 = 1.518%
FCF_Score = clamp(100×(1 − 1.518/10), 0, 100) = 84.8
```
No Owner Earnings (Upgrade 1) substitution applied — TSM is not on the framework's named Upgrade-1 list (MSFT/GOOGL/META/AMZN), and no split between "maintenance" and "growth" capex is disclosed by TSMC that this framework could cite without inventing one; the capex effect on FCF is instead handled via the Quality Score's hard-disqualifier carve-out (§3.1), consistent with the established NVO-session precedent for non-listed, capex-heavy names.

### 5.2 EV/EBIT (40% weight — see §5.4 for the redistribution)

```
TTM EBIT (USD) = NT$2,187,974M / 30.90 = $70,809.5M
EV = Market Cap + Net Debt (USD) = 2,251,381 + (−62,957) = $2,188,424M
EV/EBIT = 2,188,424 / 70,809.5 = 30.91×
EV/EBIT_Score = clamp((30.91 − 12)/23 × 100, 0, 100) = clamp(82.2, 0, 100) = 82.2
```

### 5.3 Forward PE + Historical PE Modifier (20% weight)

A genuine 5yr annual low/high range exists (§2.7) → primary formula:
```
FwdPE_Score = clamp((21.80 − 11.44)/(26.73 − 11.44) × 100, 0, 100) = clamp(67.75, 0, 100) = 67.75
```
**Historical PE Modifier (Upgrade 2):** Forward PE vs. 5yr avg (20.74×): (21.80 − 20.74)/20.74 × 100 = **+5.11%** — within ±10% → modifier = **0**.
```
FwdPE_Score = 67.75 + 0 = 67.75
```
*Sensitivity: using the Forward PE bounds individually (21.36–22.24) moves FwdPE_Score across 64.9–70.6 — a ≤1.2-point swing on the final weighted score at 20% weight, not enough to change the action-band conclusion (§6).*

### 5.4 PEG (15% weight) — **NOT APPLIED, redistributed to EV/EBIT**

**Fast-Grower eligibility check:** Annual ADR-equivalent EPS (NT$, §2.7): FY2021 114.20 → FY2022 191.45 (+67.6%) → **FY2023 164.25 (−14.2%)** → FY2024 223.35 (+36.0%) → FY2025 327.35 (+46.6%). The trailing 3-year window (FY2023–FY2025, the window relevant to a "3+ years" test as of this scoring date) contains a **clear cyclical EPS decline in FY2023** (the 2022–2023 semiconductor inventory-correction downturn, directly visible in TSM's own reported numbers) — this is **not** a "reliable, non-distorted earnings base" showing >15%/yr growth for 3+ *consecutive* years, per the 2026-06-20 clarification. Separately, and independently disqualifying on its own: **Upgrade 3 explicitly states "Never apply [PEG] to cyclicals,"** and a foundry business with a demonstrated multi-year boom-bust EPS pattern this recent is squarely a cyclical, not a structural Fast Grower, however strong its most recent 1–2 quarters look. **PEG is not scored; its 15% weight is redistributed to EV/EBIT (→ 40%)** per the Final Score Formula note in valuation-scoring.md.

### 5.5 Raw Weighted Score

```
Raw = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
    = (84.8 × 0.40) + (82.2 × 0.40) + (67.75 × 0.20)
    = 33.92 + 32.88 + 13.55
    = 80.35
```

**+ Rate Environment Gate (§4): +10**

```
Raw + Rate Gate = 80.35 + 10 = 90.35
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

**Step 1 — scenario fair values (Rule 7).** Forward ADR EPS base ≈ $19.92 (average of the two corroborating vendor estimates, §2.8):

| Scenario | Wt | Assumption | EPS | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | AI/HPC demand stays extremely strong through the 2nm (N2)/A16 ramp; advanced-node price hikes fully realize; no material Taiwan Strait/export-control disruption; continued beat-and-raise sustains a rich multiple | $20.32 (consensus high, Finviz) | 28× (below the 5yr-range high of 26.73× would be inconsistent — used a modest premium to it, reflecting a structurally larger AI-driven TAM than any point in the 5yr lookback, while still avoiding an invented "rosy" multiple) | **$568.96** |
| Base | 50% | Consensus estimates hold; multiple settles moderately above the 5yr average (20.74×) but below the current elevated trailing multiple (~36×), reflecting durable but moderating growth premium | $19.92 | 24× | **$478.08** |
| Bear | 25% | AI-capex "digestion" cycle repeats the 2022–2023 pattern (documented analyst concern — see §7), and/or a Taiwan Strait or export-control shock; growth stalls well below consensus; multiple compresses toward the 5yr low | $14.00 | 15× | **$210.00** |

```
PW Fair Value = 0.25×568.96 + 0.50×478.08 + 0.25×210.00 = $433.78
```
**Sanity check (Rule 4):** PW FV ($433.78) sits **~11.5% below** the analyst consensus PT ($490.34) — a conservative, not rosy, scenario blend.

**Step 2 — catalyst window & annualization (Rule 10).** Documented, dated catalysts within 18–24 months: **Q2 2026 earnings, 16 July 2026** (four days out) and the 2nm(N2)/A16 node ramp through 2026–2027. Standard 2yr window used (no −5 upside cap needed — Guardrail 1 satisfied).

```
Gap Upside % = (433.78 / 434.11) − 1 = −0.076%
Annualized gap (2yr) = −0.076% / 2 = −0.038%/yr
```

**Step 3 — expected annual return E.**
```
Intrinsic growth = 10%/yr  — disclosed judgment call: TSM's own trailing 3yr EPS CAGR (FY2022→FY2025) is
   19.6% (327.35/191.45)^(1/3)−1, but this window is itself distorted by recovery from the FY2023 cyclical
   trough and an unusually strong AI-capex supercycle (the same reasoning that excluded PEG in §5.4) — using
   the full trailing figure here would double-credit the same optimism already excluded from the PEG
   sub-score. A ~50% haircut (≈10%/yr) is applied as a conservative proxy, distinct from and more cautious
   than TSMC's own stated long-term target (a company-guided "approach 25%" 2024–2029 USD revenue CAGR,
   noted for context but not adopted directly, consistent with this framework's treatment of company
   guidance as directional context rather than a scored input).
Shareholder yield = dividend yield 0.8% (IBKR live, §1) + buyback yield 0% — no material ongoing buyback
   program was found this session (TSMC's disclosed FY2026 capital appropriations are overwhelmingly
   capacity/fab construction, not repurchases); treated as 0% rather than assumed, per "never invent."
E = −0.038 + 10 + 0.8 = 10.76%/yr
```

**Step 4 — map E to M** (hurdle H = 10%, E ≥ H branch):
```
M = −15 × clamp((E − H)/15pp, 0, 1) = −15 × clamp((10.76 − 10)/15, 0, 1) = −15 × 0.0507 = −0.76
```
E sits only marginally above the 10% hurdle — a thin, not strong, embedded expected return. M = **−0.76**, within the [−15, +15] bound. Guardrail 1 (catalyst requirement) is satisfied so no cap applies; the small magnitude here is driven by the scenario math itself, not a guardrail.

---

## 7. Final Valuation Score & Composite Score

```
Raw weighted                         80.35
Rate Gate (Step 1 + Step 2)         +10.00
Upside/Downside Modifier             −0.76
FINAL VALUATION SCORE                89.59 → rounds to 89.6
```

| | Value |
|---|---|
| **Quality Score** | **83.2** (PASSES 80.0+ gate) |
| **Final Valuation Score** | **89.6** |

```
Composite Score = 0.50 × (100 − 83.2) + 0.50 × 89.6
               = 0.50 × 16.8 + 0.50 × 89.6
               = 8.4 + 44.8
               = 53.2
```

**Composite Score = 53.2** — falls in the **50.0–69.9 "Fair Value / HOLD — watch only, no new entry, no trim"** band per the current Phase 03 action table.

---

## 8. Order Setup — NOT PRODUCED

Per fair-value-methodology.md Step 2 ("Score 50.0–69.9 → No MoS → Watchlist only") and operating-brief.md ("BUY/SELL ORDER SETUP: run for every BUY or TRIM action"), **neither condition is met** — no Margin of Safety, Buy Price, Sell Target, Stop Loss, R/R, or position size is computed. **Reference only:** this session's own Probability-Weighted Fair Value ($433.78) sits essentially exactly at the live price ($434.11, −0.08%) — there is currently no embedded margin of safety by this framework's own scenario math, consistent with the HOLD conclusion independent of the mechanical score.

---

## 9. Qualitative Notes

1. **This is one of the strongest Quality Scores this framework has computed** (83.2, driven by a saturated Profitability/Margins/Balance-Sheet trio and an 80.0 Moat Signal reading — 4 of 5 checklist signals cleared with cited, multi-source evidence) — TSMC's dominant, structurally advantaged position in advanced-node semiconductor manufacturing is not in question.
2. **The Composite Score's HOLD conclusion is driven entirely by price, not quality.** TSM currently trades near an all-time-high **trailing** PE (~36×, per Finviz/wisesheets cross-check) versus its own 5-year average of 20.74× — a much larger re-rating than this framework has seen in comparably-scored names (AVGO, NVDA), and the mechanical FCF Yield/EV-EBIT/Forward-PE sub-scores correctly read this as expensive on an absolute and historically-relative basis, even after crediting the AI-driven growth premium.
3. **The Upside/Downside Modifier found only a thin, near-hurdle embedded expected return (E=10.76%, barely above the 10% hurdle)** after building a deliberately conservative bull/base/bear scenario set — the resulting PW Fair Value landed almost exactly at the live price. This is the same mechanism (per valuation-scoring.md) that is *supposed* to pull a "wonderful business at a fair (not cheap) price" toward a HOLD, not a BUY, and it did so here without needing to invoke any bearish override.
4. **PEG/Fast-Grower disqualification is a direct consequence of TSM's own numbers, not an arbitrary judgment call** — the FY2023 EPS decline (−14.2%) sits inside the trailing 3-year lookback window, and Upgrade 3 explicitly bars applying PEG to cyclicals. This is worth remembering the next time TSM is re-scored: if FY2023 rolls out of a future 3-year window without a comparable down-year replacing it, this ruling could flip.
5. **The FCF/NI conversion ratio (TTM 54.75%, FY2025 58.4%) is a genuine, close-to-the-line item worth monitoring**, not currently a hard disqualifier (§3.1) but only one fiscal year away from potentially becoming one on a strict "2+ consecutive years" reading if FY2026 comes in similarly capex-heavy. Fully explained by TSMC's own disclosed US$52–56B 2026 capex guide (2nm/A16 capacity, Arizona/Japan/Germany fabs) rather than an earnings-quality concern in the Valeant/Wirecard sense.
6. **Geopolitical and concentration risk is real and documented, not scored directly (Rule 9-style context, not a sub-score input):** Taiwan Strait tension remains a standing structural risk to a company whose entire advanced-node manufacturing base sits on the island; US export-control policy has tightened (TSMC's Nanjing, China fab moved from an indefinite waiver to an annual re-licensing requirement in early 2026); and TSMC's FY2025 20-F discloses ~75% of net revenue from North American customers — a concentrated customer base (Apple, Nvidia, AMD, and other hyperscaler/fabless names) whose own capex cycles TSMC's growth is directly levered to.
7. **A specific, near-term bear-case risk flagged by outside commentary (not yet a confirmed fact):** at least one analyst/press source (techtimes.com, ahead of the 16 Jul 2026 earnings call) frames the print as a test of whether AI-related capex (CoWoS advanced-packaging demand in particular) is approaching a "spending ceiling" — exactly the kind of demand-cycle risk this session's Bear scenario (§6) is built to price in, not a reason to treat the Bull case as base-rate.
8. **The Telegram trigger was directionally accurate but analytically thin** — TSM's Q2 2026 earnings genuinely fall four days after this session, confirming the "earnings season" framing, but the post itself supplied no analysis beyond naming the ticker alongside ASML and NFLX.

---

## 10. Recommendation

# **WATCHLIST ONLY — do not enter. Composite Score 53.2 falls in the 50.0–69.9 HOLD/Fair-Value band.**

TSM clears this framework's Quality Gate comfortably (83.2, one of the strongest computed to date — exceptional profitability, margins, balance sheet, and a well-documented 4-of-5 Moat Signal reading). But it does **not** clear the bar for a new entry: the Final Valuation Score (89.6, before the modifier) reflects a stock trading at a historically rich multiple even for a business of this quality, and the Upside/Downside Modifier's own deliberately conservative scenario math finds essentially no embedded margin of safety at the current price (PW Fair Value $433.78 vs. live price $434.11). **No order setup, no position, no capital deployed.**

---

## 11. Next Review Trigger

- **TSMC's Q2 2026 earnings, 16 July 2026** (four days after this session) — the next scheduled Rule 9 trigger, and the specific event both the Telegram post and multiple analyst previews are watching. Re-score promptly after, specifically checking: (a) whether guided ~30%+ FY2026 USD revenue growth and the 65.5–67.5% Q2 gross-margin guide were met or missed; (b) any update on 2nm(N2)/A16 ramp progress and CoWoS/advanced-packaging capacity; (c) whether the FCF/NI conversion ratio (§3.1, currently a monitored-not-firing item) improves or extends its recent sub-70% run; (d) any guidance revision.
- **A pullback toward or below this session's own PW Fair Value (~$434, i.e., essentially the current live price)** would immediately reopen the entry question, since the gate between HOLD and a BUY band here is almost entirely a price question, not a quality one.
- **Any Taiwan Strait geopolitical escalation or new US/China export-control action** affecting TSMC's Nanjing/Shanghai operations or its advanced-node export licensing (Rule 9 fundamental trigger).
- Standard Rule 9 triggers: management change, material M&A, or a >15% unexplained price move.

**No position opened — nothing to log in `decisions/`.**

---

## 12. Glossary

- **ADR (American Depositary Receipt) / ADS (American Depositary Share)**: a US-exchange-listed security representing shares of a non-US company; TSM = 1 ADR representing 5 TSMC ordinary (common) shares, confirmed via SEC filing citation and this session's own EPS-ratio cross-check.
- **BalanceSheet_Score**: this framework's Quality Score sub-score derived from Net Debt/EBITDA; TSM scored 100.0 (net cash position).
- **bps / pp (basis points / percentage points)**: bps = 0.01 percentage points; pp = a direct difference between two percentages.
- **CAGR**: Compound Annual Growth Rate.
- **CapEx**: Capital Expenditure — money spent buying or upgrading physical assets (in TSM's case, fabs and advanced-node manufacturing equipment).
- **CIK (Central Index Key)**: the SEC's unique numeric identifier for TSMC (1046179), used to construct this session's EDGAR filing URLs.
- **Composite Score**: this framework's blended 0.0–100.0 ranking — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — 53.2 for TSM this session.
- **CoWoS (Chip-on-Wafer-on-Substrate)**: TSMC's advanced chip-packaging technology combining a GPU/accelerator die with high-bandwidth memory into a single package; supply-constrained industry-wide and cited in this session's bear-case AI-capex risk discussion.
- **D&A**: Depreciation & Amortization.
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **EDA (Electronic Design Automation)**: the software tools chip designers use to design and verify semiconductors; a small number of vendors (e.g. Synopsys, Cadence) dominate this market and integrate closely with a foundry's process technology, deepening the switching-cost moat credited in §3.2. *(New term — not yet in glossary.md.)*
- **EPS**: Earnings Per Share.
- **EV / EV/EBIT**: Enterprise Value (market cap + net debt) / EV divided by EBIT, a valuation multiple.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against the 10-Year Treasury in the Rate Environment Gate.
- **Fabless**: a chip company that designs semiconductors but outsources manufacturing to a foundry rather than owning its own fabs (e.g. Apple, Nvidia, AMD, Qualcomm — all TSMC customers). *(New term.)*
- **Fast Grower**: a company growing EPS >15%/yr for 3+ years on a clean, non-distorted earnings base — this framework's PEG-sub-score trigger; TSM does not qualify (§5.4).
- **FCF / FCF Yield / FCF/NI conversion ratio**: Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check).
- **Foundry (pure-play foundry)**: a semiconductor manufacturer that makes chips designed by other ("fabless") companies rather than selling its own-branded chips; TSMC is the dominant pure-play foundry, holding ~70–72% of the global foundry market as of Q1 2026. *(New term.)*
- **Form 6-K**: a furnished report foreign private issuers file with the SEC between annual filings — this session's primary source for TSM's quarterly results.
- **Form 20-F**: the annual report foreign private issuers file with the SEC — TSMC's equivalent of a US 10-K.
- **Forward PE**: price ÷ next-twelve-months expected earnings per share.
- **FV / PW Fair Value**: Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear, Rule 7).
- **Hard disqualifier**: a Quality Score condition that fails a company regardless of weighted score; none fired for TSM, though the FCF/NI check was a close call (§3.1).
- **HPC (High-Performance Computing)**: compute-intensive workloads (AI/data-center accelerators, supercomputing) — TSMC's largest revenue category (58% of FY2025 revenue per its 20-F). *(New term.)*
- **Hurdle rate**: the minimum acceptable annual return (10%) the Upside/Downside Modifier measures expected return against.
- **IFRS**: International Financial Reporting Standards — the accounting framework TSMC reports under (vs. US GAAP).
- **Invested Capital**: debt + equity − cash, the ROIC denominator.
- **Moat**: a durable competitive advantage protecting a business's profits — scored 80.0 (4 of 5 signals) for TSM this session.
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate; TSM's is negative (net cash).
- **Net Margin**: Net Income ÷ Revenue.
- **NOPAT**: Net Operating Profit After Tax — EBIT × (1 − effective tax rate).
- **Open Innovation Platform (OIP)**: TSMC's ecosystem program (established 2008) integrating EDA, IP, and design-service partners around its process technology — grown from ~3,000 to 93,000+ certified IP titles — cited as switching-cost/ecosystem Moat Signal evidence in §3.2. *(New term.)*
- **PDK (Process Design Kit)**: the foundry-supplied set of design rules, models, and IP libraries a chip designer must build a chip around for a specific manufacturing process; switching foundries means re-designing around a different PDK, a major documented source of TSMC's switching-cost moat. *(New term.)*
- **PEG ratio**: PE ÷ earnings growth rate; not scored for TSM this session (§5.4).
- **Process node (e.g. "2nm"/"N2", "3nm", "A16")**: a generation of semiconductor manufacturing technology, historically named after a (no-longer-literal) transistor feature size; newer/smaller nodes pack more transistors per chip and cost more to manufacture. *(New term.)*
- **PT (Price Target)**: an analyst's price forecast.
- **Quality Score**: this framework's 0.0–100.0 score (higher = better); 80.0+ required to reach Phase 02/Composite Score. TSM scored 83.2.
- **Rate Environment Gate / Rate Regime Modifier**: the pre-score check comparing Earnings Yield to the 10-Year Treasury, plus the additive Treasury-bracket adjustment.
- **R/R (Risk/Reward ratio)**: expected gain ÷ expected loss; not computed this session (no order setup, §8).
- **ROIC / ROE**: Return on Invested Capital / Return on Equity.
- **Rule 0 / Rule 4 / Rule 7 / Rule 9 / Rule 10**: this framework's standing instructions to always fetch a live price first; sanity-check implied returns; use a scenario-weighted (not rosy) fair value; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst/timeline.
- **Shareholder yield**: dividend yield plus net buyback yield.
- **TAM**: Total Addressable Market.
- **Treasury yield (10Y)**: this framework's risk-free-rate benchmark.
- **TTM (Trailing Twelve Months)**: the most recent 12 months of reported financial results.
- **Upside/Downside Modifier (Expected-Return Modifier)**: the additive ±15 valuation-score adjustment based on expected annual return vs. the 10% hurdle; computed at −0.76 for TSM this session.
- **Wafer**: the thin disc of silicon (typically 300mm/12-inch at modern fabs) on which many chips are simultaneously manufactured — the basic unit a foundry prices and sells capacity by. *(New term.)*
- **XBRL (eXtensible Business Reporting Language)**: the structured, machine-readable format the SEC requires financial-statement figures to be tagged in.

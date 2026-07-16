# NEW POSITION — TSM (Taiwan Semiconductor Manufacturing Company Limited, NYSE ADR) — 2026-07-16

**Task type:** NEW POSITION (Telegram-scan trigger, Rule 9 re-evaluation)
**Date:** 16 Jul 2026
**10Y US Treasury Yield:** 4.58% (FRED `DGS10`, most recent posted observation dated 2026-07-14, page shows "Updated: Jul 15, 2026" — normal 1-day FRED reporting lag)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current TSM portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [watchlist/not-in-portfolio/TSM/TSM-2026-07-16.md](../watchlist/not-in-portfolio/TSM/TSM-2026-07-16.md) (renamed from `TSM-2026-07-12.md` this session, per the dated-filename convention — git history preserves the prior version) — Quality Score 83.2, Valuation Score 89.6, **Composite Score 53.2, WATCHLIST ONLY (50.0–69.9 Hold band)**. That entry's own documented "Next review trigger" was explicitly "TSMC's Q2 2026 earnings, 16 July 2026" — today. This session is that scheduled Rule 9 re-evaluation, triggered opportunistically by a same-day Telegram post.
**Sector:** Technology — Semiconductors (dedicated/"pure-play" foundry — contract chip manufacturing, not a fabless chip designer)
**Filer type:** Foreign private issuer — TSMC files an annual **Form 20-F** (not a 10-K) and furnishes quarterly/interim results via **Form 6-K** (not 8-K/10-Q) with the SEC (CIK 1046179), reporting under Taiwan-IFRS in **NT$ (New Taiwan Dollar)**. **ADR ratio: 1 ADR = 5 ordinary ("common") shares** of TSMC (Taiwan Stock Exchange: 2330.TW), unchanged from the 2026-07-12 session.
**First-use jargon decode:** see closing Glossary (§12) — all terms used this session were already defined in glossary.md by the 2026-07-12 TSM and 2026-07-05/07-15 NVDA/ASML sessions; no new terms introduced.

---

## 0. Why this session exists — trigger source

A Telegram post on the **FinnInvestChannel** channel (~07:26 UTC 2026-07-16, Ukrainian, machine-translated) claimed: "TSMC investing another $100B in Arizona fabs. Net profit up 77% YoY to a record $22B. Revenue up 36% to $40.2B. Company also raised its 2026 guidance, now expecting revenue growth over 40%. Demand remains strong."

**Per the operating brief, Telegram post text is never used as financial data** — it is a trigger only. Every claim was independently verified below against TSMC's own primary sources and reputable financial media:

| Telegram claim | Independent verification result |
|---|---|
| "Net profit up 77% YoY to a record $22B" | ✅ **Confirmed, primary-sourced.** TSMC's own Q2 2026 earnings release (pr.tsmc.com/english/news/3326, "TSMC Reports Second Quarter EPS of NT$27.25," 2026-07-16): Net Income NT$706.56B, +77.4% YoY — matches almost exactly. US$ equivalent ≈$22.4B (TradingKey, at the quarter's reported FX) — matches "$22B." |
| "Revenue up 36% to $40.2B" | ✅ **Confirmed, primary-sourced.** Same release: Revenue NT$1,270.38B / **US$40.20B**, +36.0% YoY, +12.0% QoQ — an exact match on both the growth rate and the dollar figure. |
| "TSMC investing another $100B in Arizona fabs" | ⚠️ **Accurate as a fact, but not new information from today.** This $100B additional Arizona investment (bringing TSMC's total US commitment to $165B) was announced **2026-03-04** at a joint press conference with President Trump — over four months before this session (Asia Matters for America, CFR). It is not mentioned in TSMC's Q2 2026 earnings press release fetched this session. The Telegram post appears to have bundled an already-public fact in with the earnings news, not reported new information. |
| "Raised its 2026 guidance, now expecting revenue growth over 40%" | ⚠️ **Directionally corroborated, not primary-source-confirmed.** TSMC's own prior guidance (from the Q1 2026 call) was full-year 2026 USD revenue growth ">30%." Multiple analyst-preview sources going into today's call expected an upward revision toward ~40% (e.g. one cited analyst, "Liu," explicitly forecasting 40% for 2026 in a pre/post-earnings note), and one vendor-aggregated post-earnings summary (stockanalysis.com) states "full-year 2026 revenue growth is projected to exceed 40%." However, **no primary TSMC transcript or major-wire (Reuters/Bloomberg/CNBC) quote giving an exact revised full-year percentage was found and independently confirmed this session** — Reuters was inaccessible to this session's tooling, and the CNBC Q2 recap did not include this specific figure in what could be fetched. Treated as **plausible and directionally consistent, but not verified to primary-source certainty.** This does not block scoring: per [valuation-scoring.md](../framework/valuation-scoring.md)'s "Why Forward Guidance Is Not a Sub-score," management guidance is never a scored input in this framework regardless — only a Rule 9 re-valuation trigger, and the trigger (the earnings release itself) is independently confirmed either way. |
| "Demand remains strong" | ✅ Corroborated — HPC/AI-related demand now 66% of revenue this quarter (up from 58% for FY2025), CoWoS packaging reported "sold out through year-end" (Phemex), 2026 capex confirmed landing "toward the high end" of the existing $52–56B guide (not a new $60–64B figure as one lower-quality aggregator blurb suggested — that specific number is flagged and **not used**, since it could not be corroborated against a second source). |

**Conclusion: the trigger is legitimate and well-corroborated on the two hard numbers that matter most (net income, revenue), a known fact was included as if new (Arizona), and one claim (the specific ">40%" guidance figure) is plausible but not independently pinned down to primary-source certainty — disclosed rather than assumed true.**

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used (per orchestrating session, fetched immediately pre-session)** | **$407.00** | IBKR, contract_id **6223250**, NYSE, "TAIWAN SEMICONDUCTOR-SP ADR" — the correct primary TSM ADR listing, disambiguated via `search_contracts` from ~20 similarly-named leveraged/inverse/options-income ETF products |
| Change vs. prior close | **−$12.48 (−2.98%)** | Prior close implied: $419.48 — matches this session's own IBKR `get_price_history` bar for 2026-07-15 exactly |
| ⚠️ Later same-session snapshot (fetched for dividend-yield/52-week-range data, not used to override the price above per explicit instruction not to re-derive) | **$400.78, −$18.70 (−4.46%)** vs. the same $419.48 prior close | IBKR `get_price_snapshot` (`last`), fetched later in this session — shows the decline **continuing intraday**, reinforcing rather than contradicting the "sell the news" dynamic discussed in §9 |
| 52-week range | $221.332 (low) – $478.89 (high) | IBKR `get_price_snapshot` `misc_statistics` |
| Dividend yield (live) | **0.83%** | IBKR `get_price_snapshot` `dividend_yield` — cross-checked against 0.97–0.66% across other vendors (Finviz, stockanalysis.com); IBKR used as the primary Rule-0-compliant source per established practice |
| Analyst consensus PT (pre-existing, likely not fully reflecting today's post-earnings target hikes) | $449.38 (MarketBeat, "Moderate Buy," 16 analysts, range $330–$590) | Multiple newer, single-name target hikes found post-earnings but not yet reflected in aggregator consensus: **Citi** raised its Taiwan-listed-share target to NT$3,800 (≈$594/ADR-equivalent at spot FX/ratio); **Barclays** raised to $625 | stockanalysis.com/forecast lists $498.24, using a stale $419.48 price base | TipRanks-sourced press coverage |
| US 10Y Treasury yield | 4.58% | FRED `DGS10`, as-of 2026-07-14 |
| USD/TWD FX (live, 2026-07-16) | **32.15** | Cross-checked across multiple sources this session, ranging 32.12–32.21 |

**$407.00 is used as the live price for all arithmetic below**, per the orchestrating session's Rule-0-compliant fetch immediately prior to this session starting.

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note and a disclosed data-vintage split

TSMC's Q2 2026 SEC 6-K had **not yet posted to EDGAR** at session time (confirmed via `data.sec.gov/submissions/CIK0001046179.json` — most recent 6-K on file was 2026-07-13, a routine monthly-revenue filing, not the earnings release). Per the same approach used in the 2026-07-15 ASML session under an identical circumstance, this session instead uses **TSMC's own investor-relations-published Q2 2026 results** (`pr.tsmc.com/english/news/3326`, "TSMC Reports Second Quarter EPS of NT$27.25," and `investor.tsmc.com/english/quarterly-results/2026/q2`) as the primary source, cross-checked against independent financial media (TradingKey, CNBC, Euronews) that all corroborate the same headline figures.

**A material, disclosed data-vintage split exists this session:**
- **Income-statement figures (revenue, gross/operating/net margin, net income, EPS)** reflect TSMC's **actual, just-reported Q2 2026 results** (fresh).
- **Balance-sheet and cash-flow figures (cash, debt, equity, OCF, CapEx, FCF, D&A)** are **carried forward unchanged from the 2026-07-12 session's Q1 2026 vintage**, per this task's explicit instruction to flag and carry forward when a metric is genuinely unavailable this run. TSMC's Q2 2026 balance sheet/cash-flow statement is filed only in a "Financial Statements" / "Management Report" PDF that (a) this session's environment cannot render (no `pdftoppm`/poppler-utils, the same disclosed PDF-parsing limitation as the 2026-07-12 session) and (b) had not yet propagated to vendor data either — `stockanalysis.com`'s quarterly balance-sheet and cash-flow pages, checked directly this session, still show Q1 2026 as their most recent column, and Finviz's own `EPS ttm` field ($12.03) still shows the **pre-Q2-2026** figure, confirming this is a genuine vendor-wide lag, not a tooling failure specific to this session.

This split is called out explicitly at every sub-score below that it affects.

### 2.2 Quarterly income statement — fresh Q2 2026 added to the primary-sourced series

| Quarter | Revenue (NT$M) | Revenue (US$B) | Gross Profit (NT$M) | GM% | Op. Income (NT$M) | OM% | Pretax Income (NT$M) | Net Income (NT$M) | NM% | EPS (NT$, common) | EPS (US$/ADR) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 2025 | 839,250 | 25.53 | 493,395 | 58.8% | 407,081 | 48.5% | 430,895 | 361,564 | 43.1% | 13.94 | 2.12 |
| Q2 2025 | 933,790 | 30.07 | 547,370 | 58.6% | 463,420 | 49.6% | 493,040 | 398,270 | 42.7% | 15.36 | 2.47 |
| Q3 2025 | 989,918 | 33.10 | 588,543 | 59.5% | 500,685 | 50.6% | 525,369 | 452,302 | 45.7% | 17.44 | 2.92 |
| Q4 2025 | 1,046,090 | 33.73 | 651,987 | 62.3% | 564,903 | 54.0% | 592,363 | 505,744 | 48.3% | 19.50 | 3.14 |
| Q1 2026 | 1,134,103 | 35.90 | 751,295 | 66.2% | 658,966 | 58.1% | 687,800 | 572,480 | 50.5% | 22.08 | 3.49 |
| **Q2 2026** | **1,270,380** | **40.20** | **860,047†** | **67.7%** | **766,039†** | **60.3%** | **883,200†‡** | **706,560** | **55.6%** | **27.25** | **4.31** |

† Gross Profit and Operating Income for Q2 2026 are **derived** (Revenue × TSMC's own disclosed margin %) — the press release gives margins and totals directly but not a separately broken-out NT$ Gross Profit / Operating Income line; simple arithmetic on two disclosed primary figures, not an estimate.
‡ Pretax Income for Q2 2026 is **imputed**, not disclosed in the primary source fetched this session — see §2.4 note on the tax-rate gap.

**Internal consistency checks (all pass):** Revenue YoY = (1,270,380−933,790)/933,790 = **+36.05%** (TSMC states +36.0%); NI YoY = (706,560−398,270)/398,270 = **+77.42%** (TSMC states +77.4%); NI QoQ = (706,560−572,480)/572,480 = **+23.42%** (TSMC states +23.4%); Revenue QoQ = (1,270,380−1,134,103)/1,134,103 = **+12.02%** (TSMC states +12.0%). Every published growth-rate headline reconciles exactly against this session's own reconstructed NT$ figures — strong confirmation the underlying numbers are sound.

Sources: [Q1 2025–Q1 2026 6-Ks](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000199/a1q26e_withguidancexfinal.htm) (primary, carried forward from 2026-07-12 session, unchanged), [Q2 2026 press release](https://pr.tsmc.com/english/news/3326) (primary, fetched fresh this session), [investor.tsmc.com Q2 2026 page](https://investor.tsmc.com/english/quarterly-results/2026/q2) (primary, confirms Q3 2026 guidance below), cross-checked against [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262033904-tsmc-q2-profit-77-percent-record-hightradingkey) and CNBC.

**TSMC's own Q3 2026 guidance (disclosed, not scored — Rule 9/guidance-as-trigger only):** Revenue US$44.6–45.8B, gross margin 65.0–67.0%, operating margin 56.0–58.0% (at an assumed 1 USD = NT$32 per the company's own stated assumption) — a further sequential step-up from Q2 2026's actual $40.20B.

**One flagged, single-sourced item not used in scoring:** TradingKey's article states Q2 2026 net income was boosted by "a NT$63.2 billion gain from Vanguard International Semiconductor (VIS) share sale." This is **not corroborated** in the primary press release text fetched this session (which discloses no one-time items), so per Rule 6 ("normalize before you value — strip out one-time items") this would matter if confirmed, but it is disclosed here as an **unconfirmed, single-source claim** — not applied as an adjustment to any score below. Worth checking against the full 6-K once it posts to EDGAR (see §11).

### 2.3 New TTM reconstruction (Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026) — income-statement items only

```
Revenue (NT$M) = 989,918 + 1,046,090 + 1,134,103 + 1,270,380 = 4,440,491
Revenue (US$B, as-reported each quarter) = 33.10+33.73+35.90+40.20 = 142.93   → implied TTM avg FX = 4,440,491/142,930 = 31.06
Gross Profit (NT$M) = 588,543+651,987+751,295+860,047 = 2,851,872   → Gross Margin TTM = 2,851,872/4,440,491 = 64.22%
Operating Income (NT$M) = 500,685+564,903+658,966+766,039 = 2,490,593   → Operating Margin TTM = 56.09%
Net Income (NT$M) = 452,302+505,744+572,480+706,560 = 2,237,086   → Net Margin TTM = 50.38%
EPS TTM (US$/ADR, summed) = 2.92+3.14+3.49+4.31 = $13.86   (up from $12.02 in the 2026-07-12 session's TTM window)
```

### 2.4 Effective tax rate — data gap, disclosed imputation for TTM ROIC purposes only

TSMC's Q2 2026 pretax income / tax expense breakdown was **not available** in the primary press release fetched this session (only revenue, margins, net income, and EPS were disclosed at the summary level; the full income statement with the tax line lives in the unparseable PDF). Rather than invent a tax rate, this session uses **TSMC's own guided figure**: its Q1 2026 earnings release guided Q2 2026's tax rate at "**around 20%**, due to accrual of tax on undistributed retained earnings" (a disclosed, primary-sourced, but guided-not-actual figure) — used only to impute a placeholder Pretax Income for the TTM tax-rate blend below, flagged throughout:

```
Imputed Q2 2026 Pretax Income = NI / (1 − guided tax rate) = 706,560 / (1 − 0.20) = 883,200 NT$M (flagged: guided, not disclosed actual)
TTM Pretax Income = 525,369 (Q3'25) + 592,363 (Q4'25) + 687,800 (Q1'26) + 883,200 (Q2'26, imputed) = 2,688,732
TTM effective tax rate = (2,688,732 − 2,237,086) / 2,688,732 = 16.80%   (in line with the 13.9–16.8% range across the last four actual quarters — not an outlier)
```

This imputed rate is **not used for any Quality/Valuation sub-score directly** in this session (the ROIC figure below is carried forward from the 2026-07-12 session unchanged, per §2.5) — it is shown here only as a transparency check that the imputation is plausible, in case a future session needs it once the actual Q2 2026 tax line is confirmed.

### 2.5 Balance sheet & cash flow — carried forward unchanged (Q1 2026 vintage, flagged)

Identical to the 2026-07-12 session's §2.5 — **not refreshed this session**, since neither TSMC's own filed statements nor vendor data (stockanalysis.com, checked directly) had a Q2 2026 balance sheet/cash-flow column available yet:

| | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 (most current available) |
|---|---|---|---|---|
| Cash & equivalents (NT$M) | 2,364,520 | 2,470,760 | 2,767,860 | 3,035,640 |
| Total Debt (NT$M) | 1,009,250 | 1,025,430 | 1,064,580 | 1,016,270 |
| Total Equity (NT$M) | 4,616,630 | 5,035,580 | 5,396,220 | 5,932,390 |
| Operating CF (NT$M) | 497,064 | 426,829 | 725,509 | 698,976 |
| CapEx (NT$M) | 297,226 | 287,452 | 356,906 | 350,763 |
| Free Cash Flow (NT$M) | 199,838 | 139,377 | 368,603 | 348,213 |
| D&A (NT$M) | 188,058 | 162,787 | 162,112 | 165,450 |

```
TTM OCF (Q2'25–Q1'26 window, unchanged) = 2,348,378 NT$M
TTM CapEx (unchanged) = 1,292,347 NT$M
TTM FCF (unchanged) = 1,056,031 NT$M
TTM D&A (unchanged) = 678,407 NT$M
TTM EBITDA (old-window OpInc 2,187,974 + old-window D&A 678,407) = 2,866,381 NT$M
FCF/NI (old-window NI 1,928,796) = 1,056,031 / 1,928,796 = 54.75%   — UNCHANGED from 2026-07-12

Net Debt (Q1 2026, most current) = 1,016,270 − 3,035,640 = −2,019,370 NT$M (net cash) — UNCHANGED
Net Debt/EBITDA (TTM, old window) = −2,019,370 / 2,866,381 = −0.70×   — UNCHANGED
Invested Capital (Q1 2026) = 1,016,270 + 5,932,390 − 3,035,640 = 3,913,020 NT$M — UNCHANGED
NOPAT (old-window EBIT 2,187,974 × (1−0.1609)) = 1,835,951 NT$M — UNCHANGED
ROIC = 1,835,951 / 3,913,020 = 46.92%   — UNCHANGED
```

### 2.6 Shares outstanding / ADR ratio — carried forward, unchanged

```
Weighted-avg diluted COMMON shares (Q1 2026, most recent primary disclosure available) = 25,931M ÷ 5 = 5,186.2M ADR-equivalent shares
```
No fresher share count was found or disclosed this session; carried forward per the same reasoning as the balance-sheet items above (share counts move slowly and TSMC has shown a constant ~5,186M ADR-equivalent across FY2021–2025 per the 2026-07-12 session's cross-check).

```
Market Cap (ADR basis) = $407.00 × 5,186.2M = $2,110,783.4M
Net Debt (USD, converted at today's live spot FX 32.15) = −2,019,370 / 32.15 = −$62,811.0M
EV = Market Cap + Net Debt = 2,110,783.4 − 62,811.0 = $2,047,972.4M
```

### 2.7 Annual figures FY2021–FY2025 — unchanged (no new fiscal year has closed since 2026-07-12)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Revenue (NT$M) | 1,587,420 | 2,263,890 | 2,161,740 | 2,894,310 | 3,809,050 |
| Diluted EPS (NT$, ADR-equiv.) | 114.20 | 191.45 | 164.25 | 223.35 | 327.35 |
| Annual PE (vendor) | 26.73 | 11.44 | 18.05 | 24.06 | 23.40 |

**Revenue 3yr CAGR (FY2022→FY2025):** unchanged, `18.94%`
**5yr PE range (2021–2025, annual):** unchanged — Avg **20.74×**, Low **11.44×**, High **26.73×**

### 2.8 Forward PE / forward EPS — significant vendor dispersion this session, resolved with disclosed reasoning

| Source | Forward PE or implied EPS | Assessment |
|---|---|---|
| stockanalysis.com `/forecast` (FY2026, "19 analysts polled by S&P Global") | FY2026 EPS 99.91 TWD/common share (+50.80% YoY) → **$15.54/ADR** at spot FX/ratio → implied PE **26.19×** | Used — clearly attributed methodology |
| A pre/post-earnings preview citing Wall Street consensus | "consensus estimate for 2026 is **$15.91 per share**, +49.3% over 2025" | Used — closely corroborates the figure above (2.4% apart); also correctly anticipated Q2's actual beat (quarterly consensus cited as $3.80–3.83 vs. actual $4.31) |
| Gurufocus | Forward PE 27.4× | Loosely corroborating (higher end) |
| Yahoo Finance (via search snippet) | Forward PE 29.43× | Loosely corroborating (higher end) |
| Finviz | Forward PE **19.64×**, "EPS next Y" $20.47 | **Excluded as an outlier** — Finviz's own `EPS ttm` field on the same page still reads $12.03, the **pre-Q2-2026** trailing figure (matches exactly what Finviz showed on 2026-07-12, before today's earnings) — clear evidence this vendor's derived fields have not refreshed post-earnings yet, so its forward-PE figure is not trusted this session |

**Used: Forward PE = 25.9×** (average of the two EPS-consensus-anchored calculations: 26.19× and 25.58× [=407/15.91]), which sits consistently below the Gurufocus/Yahoo cluster (27.4–29.4×) and far above the excluded Finviz outlier (19.64×) — i.e. a conservative pick within the credible range, not the most bearish-for-TSM (cheapest) available reading.

**⚠️ Material, explicitly flagged sensitivity:** this Forward PE input has an unusually wide, unresolved dispersion this session because it is **hours** after the earnings release — sell-side EPS-estimate revisions typically take **days**, not hours, to fully propagate through vendor consensus feeds, and this session found direct evidence (Finviz's stale EPS TTM field) that at least one vendor's data has not caught up yet. **§7 shows the full downstream sensitivity of this choice on the Composite Score and the recommendation** — it is large enough to matter and is not swept under the rug.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology, unchanged version)

### 3.1 Hard disqualifier check

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ **consecutive** years w/o growth-capex explanation | Unchanged from 2026-07-12: FY2023 34.3% (fail) · FY2024 75.1% (pass, breaks the streak) · FY2025 58.4% (fail) · TTM 54.75% (fail, carried-forward figure, §2.5) | disqualify if 2+ **consecutive** years <70% w/o carve-out | ⚠️ **Still a close call, still does NOT fire on a strict reading** — FY2024 still breaks the FY2023/FY2025 streak. The growth-capex carve-out still applies and, if anything, is now **more strongly evidenced**: TSMC confirmed this session that FY2026 capex is landing "toward the high end" of its existing $52–56B guide, on top of a Q2 2026 print showing HPC/AI revenue mix rising to 66% (from 58% for FY2025) — capacity expansion, not maintenance spend. |
| Net Debt/EBITDA over threshold (2.5× standard) | TTM (carried forward): **−0.70×** (net cash) | disqualify if >2.5× | ✅ PASS, overwhelmingly (unchanged) |
| FCF-positive 3+ consecutive years | FY2023/24/25 all positive (unchanged, annual figures not affected by Q2 2026) | disqualify if not | ✅ PASS (unchanged) |

**No hard disqualifier fires — same conclusion as 2026-07-12.** The FCF/NI conversion check remains the one monitoring item worth resolving once TSMC's Q2 2026 cash-flow statement is actually available (see §11).

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (TTM, FRESH) = 50.38%
  NetMargin_Component = clamp((50.38/30)×100, 0, 100) = clamp(167.9, 0, 100) = 100.0

  ROIC (carried forward, Q1 2026 vintage, §2.5) = 46.92%
  ROIC_Component = clamp((46.92/30)×100, 0, 100) = clamp(156.4, 0, 100) = 100.0

  Profitability_Score = (100.0 + 100.0) / 2 = 100.0   (no FCF-positivity cap — 3yr positive confirmed above)
  [Both inputs saturate the 30%-cap formula regardless of the fresh-vs-carried-forward split — no sensitivity here.]

MARGINS (15% weight):
  Gross Margin (TTM, FRESH) = 64.22%   (up from 61.88% in the 2026-07-12 session — Q2 2026's 67.7% GM, TSMC's highest in this data series, pulled the TTM blend up as it replaced Q2 2025's 58.6%)
  GrossMargin_Score = clamp((64.22/80)×100, 0, 100) = 80.28   (up from 77.35)

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022→FY2025, unchanged — no new fiscal year closed) = 18.94%
  Growth_Score = clamp((18.94/25)×100, 0, 100) = 75.8
  TAM/pricing-power modifier: +10 applied, evidence reaffirmed and refreshed this session:
    (a) foundry market share on an established rising trend (66%→70.4%→72.3% through Q1 2026, per 2026-07-12 session's citations, unchanged);
    (b) Q2 2026's own disclosed advanced-node revenue mix reinforces the same story: 2nm 3%, 3nm 30%, 5nm 33%, 7nm 11% — 77% of wafer revenue now on 7nm-or-better nodes (TSMC Q2 2026 press release), the highest advanced-node mix in this framework's TSM coverage to date, consistent with continued pricing-power-supporting demand for the most advanced (priciest) capacity;
    (c) CoWoS advanced packaging reported "sold out through year-end" (Phemex, corroborating capacity-constrained pricing power).
  Growth_Score = clamp(75.8 + 10, 0, 100) = 85.8   (unchanged score, refreshed evidence)

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM, carried forward, §2.5) = −0.70×
  BalanceSheet_Score = clamp(100×(1 − (−0.70)/4), 0, 100) = 100.0   (saturates — unchanged)

MOAT SIGNAL (15% weight) — unchanged conclusions (4/5 TRUE), evidence refreshed with Q2 2026 data where applicable:
  Market share stable/growing:  TRUE — unchanged citation (§Growth above).
  Brand premium (pricing power): TRUE — unchanged citation (2026-07-12 session: documented advanced-node price increases without share loss); Q2 2026's record 67.7% gross margin (a fresh high in this data series, beating even TSMC's own guided high end of 67.5%) is itself corroborating evidence pricing power held or improved this quarter.
  Network effect:  FALSE — unchanged (a dedicated foundry has no two-sided-marketplace mechanism distinct from the switching-cost row below).
  Switching costs:  TRUE — unchanged citation (OIP ecosystem, PDK lock-in, $2–5B re-design cost estimates).
  Scale cost advantage:  TRUE — unchanged citation (Intel's yield/cost gap); reinforced this session by the CoWoS "sold out through year-end" data point — smaller competitors cannot access comparable advanced-packaging capacity at any price this year.
  Moat_Score = (4/5) × 100 = 80.0   (unchanged)

FCF QUALITY (10% weight):
  FCF/NI (TTM, carried forward, §2.5) = 54.75%
  FCFQuality_Score = clamp(((0.5475 − 0.40)/0.60)×100, 0, 100) = 24.6   (unchanged — no fresh cash-flow data this session)

QUALITY SCORE = 100.0×0.25 + 80.28×0.15 + 85.8×0.20 + 100.0×0.15 + 80.0×0.15 + 24.6×0.10
             = 25.000 + 12.042 + 17.160 + 15.000 + 12.000 + 2.460
             = 83.662 → rounds to 83.7
```

**Quality Score = 83.7 / 100.0 — clears the 80.0+ gate**, up marginally from 83.2 on 2026-07-12. The entire delta is driven by the Margins sub-score (77.35→80.28), itself entirely a function of Q2 2026's record 67.7% quarterly gross margin pulling the TTM blend higher — every other sub-score is either unchanged (carried-forward balance-sheet/cash-flow items) or already saturated at its 100.0 ceiling (Profitability) regardless of which vintage of ROIC is used.

**Gate result: PASS.** Proceed to the Rate Environment Gate and Phase 02 valuation scoring.

---

## 4. Rate Environment Gate

```
Step 1 — Earnings Yield Spread Test
Forward PE = 25.9× (§2.8, disclosed reasoning + flagged sensitivity)
EY = 1 / 25.9 = 3.861%
Spread = EY − 10Y Treasury = 3.861% − 4.58% = −0.719%
Threshold: Spread ≥ +1.5% → PASS. Spread < +1.5% → FAIL → additive +5.
Result: FAIL → +5
```

**Robustness check:** using the excluded Finviz outlier (19.64×) instead — EY = 5.092%, spread = +0.512% — **still FAILS Step 1** (still below the +1.5% threshold either way). **Step 1's conclusion is robust regardless of which Forward PE reading is used**, unlike the FwdPE_Score sub-score itself (§5.3), where the choice matters a great deal.

```
Step 2 — Rate Regime Modifier
10Y = 4.58% → 3.5–5% bracket → +5
```

**Combined Rate Gate additions: +5 (Step 1) + 5 (Step 2) = +10** — same as 2026-07-12 (10Y moved only 4.54%→4.58%, staying within the same bracket).

---

## 5. Phase 02 — Valuation Score

### 5.1 FCF Yield (40% weight)

```
FCF Yield = TTM FCF (USD, carried forward §2.5) / Market Cap (fresh)
TTM FCF (USD) = NT$1,056,031M / 30.90 (TTM-implied avg FX, same vintage as the FCF figure) = $34,175.6M
FCF Yield = 34,175.6 / 2,110,783.4 = 1.619%
FCF_Score = clamp(100×(1 − 1.619/10), 0, 100) = 83.81
```
No Owner Earnings substitution — same reasoning as 2026-07-12 (TSM not on the named Upgrade-1 list, no disclosed maintenance/growth CapEx split to cite).

### 5.2 EV/EBIT (40% weight — see §5.4 for the redistribution)

```
TTM EBIT (USD, FRESH) = NT$2,490,593M / 31.06 (fresh TTM-implied avg FX) = $80,186.5M
EV (fresh price/shares, carried-forward net debt at today's live FX) = $2,047,972.4M (§2.6)
EV/EBIT = 2,047,972.4 / 80,186.5 = 25.54×
EV/EBIT_Score = clamp((25.54 − 12)/23 × 100, 0, 100) = 58.87
```
**Materially cheaper than 2026-07-12's 30.91× / 82.2 score** — the live price fell (−6.2% from $434.11), but TTM EBIT rose substantially more (Q2 2026's fresh, much-larger EBIT replaced Q2 2025's smaller EBIT in the TTM window), so the ratio improved despite the price move. This is exactly the mechanism a legitimate earnings-driven Rule 9 re-score is supposed to capture — an outsized earnings beat mechanically cheapens EV/EBIT unless price rises by a comparable amount, and here price actually fell.

### 5.3 Forward PE + Historical PE Modifier (20% weight)

```
FwdPE_Score = clamp((25.9 − 11.44)/(26.73 − 11.44) × 100, 0, 100) = clamp(94.57, 0, 100) = 94.57
Historical PE Modifier: (25.9 − 20.74)/20.74 × 100 = +24.9% → >20% above 5yr avg → +10
FwdPE_Score = clamp(94.57 + 10, 0, 100) = 100.0   (capped)
```

**⚠️ Sensitivity (flagged in §2.8, shown in full here):** using the excluded Finviz outlier (19.64×) instead: `clamp((19.64−11.44)/15.29×100) = 53.63`; modifier `(19.64−20.74)/20.74×100 = −5.3%` → within ±10% → 0; **FwdPE_Score(alt) = 53.63** — a **46.4-point swing** on this sub-score depending on which Forward PE source is trusted. This is the single largest source of uncertainty in this session's score and is carried through explicitly to the final Composite Score in §7.

### 5.4 PEG (15% weight) — still NOT APPLIED, redistributed to EV/EBIT

**Unchanged conclusion from 2026-07-12.** The trailing-3-fiscal-year EPS window relevant to the "3+ years" Fast-Grower test is still FY2023–FY2025 (no new fiscal year has closed), which still contains FY2023's −14.2% cyclical EPS decline. Per Upgrade 3 ("never apply PEG to cyclicals") and the 2026-06-20 clean-earnings clarification, **PEG is not scored; its 15% weight is redistributed to EV/EBIT (→ 40%)**, identical to the prior session.

### 5.5 Raw Weighted Score

```
Raw = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
    = (83.81 × 0.40) + (58.87 × 0.40) + (100.0 × 0.20)
    = 33.524 + 23.548 + 20.000
    = 77.072

+ Rate Environment Gate (§4): +10

Raw + Rate Gate = 77.072 + 10 = 87.072
```

**Sensitivity using the alternate (Finviz-outlier) FwdPE_Score of 53.63:** Raw(alt) = 33.524 + 23.548 + 10.726 = 67.798; +10 Rate Gate = **77.798** — a **9.27-point swing** carried forward to §7.

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

**Step 1 — scenario fair values (Rule 7).** Forward ADR EPS inputs anchored to the two corroborating consensus figures from §2.8 ($15.54 and $15.91), plus a bear-case haircut consistent with the 2026-07-12 session's methodology:

| Scenario | Wt | Assumption | EPS | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | AI/HPC demand stays extremely strong through the 2nm(N2)/A16 ramp; CoWoS sold-out capacity persists; advanced-node mix (now 77% of wafer revenue) keeps supporting pricing; no Taiwan Strait/export-control disruption | $15.91 (higher of the two corroborating consensus figures) | 28× (unchanged bull multiple from 2026-07-12 — a premium to, not equal to, the current elevated trailing multiple) | **$445.48** |
| Base | 50% | Consensus holds near the two corroborating figures' midpoint; multiple settles moderately above the 5yr average (20.74×) | $15.73 (average of $15.54/$15.91) | 24× (unchanged base multiple from 2026-07-12) | **$377.52** |
| Bear | 25% | AI-capex "digestion" cycle risk (the same documented analyst concern flagged in the 2026-07-12 session — techtimes.com's pre-earnings "spending ceiling" framing) and/or a Taiwan Strait/export-control shock materializes; growth stalls; multiple compresses toward the 5yr low | $14.00→ **$12.00** (lowered from 2026-07-12's $14.00 bear EPS, since TTM EPS itself has now risen to $13.86 — the bear case needs to sit meaningfully below the new, higher trailing base to still represent a genuine downside scenario, not merely "flat") | 15× (unchanged bear multiple) | **$180.00** |

```
PW Fair Value = 0.25×445.48 + 0.50×377.52 + 0.25×180.00 = $345.13
```

**Sanity check (Rule 4):** PW FV ($345.13) sits **~23–31% below** the analyst consensus PT range found this session ($449.38 MarketBeat aggregate; $594–625 in the newest single-analyst post-earnings hikes from Citi/Barclays) — a conservative, not rosy, scenario blend, consistent with Rule 7's requirement.

**Step 2 — catalyst window & annualization (Rule 10).** Documented, dated catalysts within 18–24 months: **Q3 2026 earnings** (mid-October 2026 per TSMC's consistent historical cadence, guidance already disclosed this session at $44.6–45.8B revenue) and the continuing 2nm(N2)/A16 ramp through 2026–2027. Standard 2yr window used (Guardrail 1 satisfied — real, dated catalysts exist).

```
Gap Upside % = (345.13 / 407.00) − 1 = −15.20%
Annualized gap (2yr) = −15.20% / 2 = −7.60%/yr
```

**Step 3 — expected annual return E.**
```
Intrinsic growth = 10%/yr — unchanged disclosed judgment call from 2026-07-12: TSM's trailing 3yr EPS CAGR (FY2022→FY2025, still 19.6%) remains distorted by recovery from the FY2023 cyclical trough and the ongoing AI-capex supercycle — the same reasoning that excludes PEG in §5.4 — so a ~50% conservative haircut (≈10%/yr) is applied again this session for consistency, rather than the raw trailing figure.
Shareholder yield = dividend yield 0.83% (IBKR live, §1, fresher than the 2026-07-12 session's 0.8%) + buyback yield 0% (no material ongoing repurchase program found this session, same as 2026-07-12 — capex, not buybacks, is where FY2026 capital is guided).
E = −7.60 + 10 + 0.83 = 3.23%/yr
```

**Step 4 — map E to M** (hurdle H = 10%, 0 ≤ E < H branch):
```
M = +5 × (H − E)/H = +5 × (10 − 3.23)/10 = +5 × 0.677 = +3.39 → +3.4
```
A thin, but this time clearly positive-and-nonzero, embedded expected return — a modest, not-strong, mild trim-pressure reading, bounded well within [−15, +15]. No guardrail cap applies (real catalysts exist, per Step 2).

**This modifier's inputs (the two consensus EPS figures) are decoupled from the FwdPE_Score's disputed Forward PE input** (§5.3) — the +3.4 modifier is therefore **not** subject to the same Finviz-outlier sensitivity and stays constant across both scenarios in §7.

---

## 7. Final Valuation Score & Composite Score

```
Raw weighted                         77.072
Rate Gate (Step 1 + Step 2)         +10.000
Upside/Downside Modifier             +3.390
FINAL VALUATION SCORE                90.462 → rounds to 90.5
```

| | Value |
|---|---|
| **Quality Score** | **83.7** (PASSES 80.0+ gate) |
| **Final Valuation Score** | **90.5** |

```
Composite Score = 0.50 × (100 − 83.7) + 0.50 × 90.5
               = 0.50 × 16.3 + 0.50 × 90.5
               = 8.15 + 45.25
               = 53.40
```

**Composite Score = 53.4** — falls in the **50.0–69.9 "Fair Value / HOLD — watch only, no new entry, no trim"** band. Effectively unchanged from 2026-07-12's 53.2 (Quality up 0.5pt, Valuation up 0.9pt, netting to a 0.2pt Composite move — same band, same conclusion).

### ⚠️ Full disclosed sensitivity — the Forward PE data-quality issue, carried through to its logical conclusion

Using the **excluded** Finviz-outlier Forward PE (19.64×) instead of this session's chosen 25.9× throughout §5.3/§5.5 (the Upside/Downside Modifier is unaffected, per §6):

```
Raw(alt) + Rate Gate = 77.798
Final Valuation Score(alt) = 77.798 + 3.390 = 81.188 → 81.2
Composite Score(alt) = 0.50×16.3 + 0.50×81.2 = 8.15 + 40.60 = 48.75 → 48.8
```

**48.8 sits inside the 30.0–49.9 "BUY — Standard position" band** — a different action category from this session's official 53.4/HOLD conclusion. **This is a genuinely close call, and the entire difference reduces to which vendor's Forward PE this session trusts**, not to any disagreement about TSMC's underlying results. This session's official score uses 25.9× because it is corroborated by more independent sources with clearer disclosed methodology (two consensus-EPS-anchored calculations agreeing within 2.4% of each other, plus Gurufocus/Yahoo both landing higher still) against one outlier (Finviz) that shows a direct, verifiable staleness artifact (its own unrevised EPS TTM field). **Per this framework's "never invent, act only on documented triggers" discipline, this session does not round this uncertainty away by picking whichever reading is more exciting — it reports the primary (HOLD) conclusion as official, discloses the alternate in full, and sets an explicit near-term re-check trigger (§11) rather than entering a position on a boundary case built on an admittedly unsettled input.**

---

## 8. Order Setup — NOT PRODUCED

Per fair-value-methodology.md Step 2 ("Score 50.0–69.9 → No MoS → Watchlist only") and this session's official Composite Score of 53.4, **no order setup is produced** — no Margin of Safety, Buy Price, Sell Target, Stop Loss, R/R, or position size. **Reference only:** this session's own PW Fair Value ($345.13) sits meaningfully *below* the live price ($407.00, a −15.2% gap) — there is currently a *negative*, not merely absent, margin of safety by this framework's own scenario math, a materially wider gap than the 2026-07-12 session found (−0.08%). Even under the alternate/sensitivity reading in §7 (Composite 48.8, technically inside the Buy band), this session declines to construct an order setup given the acknowledged data-quality uncertainty underlying that reading — see §11 for the explicit re-check trigger instead.

---

## 9. Qualitative Notes

1. **This was a genuinely strong quarter, independently confirmed on every headline number the Telegram post cited.** Revenue $40.20B (+36.0% YoY), net income NT$706.56B (+77.4% YoY), gross margin 67.7% (a new high in this framework's TSM coverage, beating even TSMC's own guided high end of 67.5%), operating margin 60.3% (also beating the 56.5–58.5% guide). This is not a marginal or disputed beat.
2. **The price fell anyway — resolved, not ignored.** TSM's live price fell −2.98% ($419.48→$407.00) on earnings day, and a later same-session snapshot showed the decline deepening intraday to −4.46% ($400.78). This is independently corroborated as a **sector-wide, not TSM-specific, dynamic**: Modern Diplomacy ("Asian Stocks Fall as Chip Selloff Overshadows TSMC Earnings") and FX Leaders ("TSMC Stock Slips Despite Strong AI Chip Demand and Robust Revenue Growth") both describe a broad semiconductor-sector selloff (part of a reported $1.3–1.4 trillion sector market-cap decline over the prior days) overwhelming a genuinely strong single-name print — textbook "sell the news," consistent with extremely high pre-earnings expectations (Citi/Barclays had already raised targets sharply *ahead* of the print) leaving little room for the actual beat to drive the stock higher. **This framework's own Rule 0/Rule 9 discipline treats this correctly by construction**: the valuation score is driven by the fundamentals just reported (which improved this session — EV/EBIT cheapened from 30.91× to 25.54× specifically *because* the earnings beat outpaced the price decline), not by the day's price action in isolation. The "sell the news" dynamic doesn't change the recommendation here since the Composite Score barely moved (53.2→53.4) — both a stronger quarter and a lower price roughly offset in the score, which is itself the correct mechanical outcome of the framework, not a coincidence to be explained away.
3. **The single biggest source of uncertainty this session is a vendor Forward-PE data-quality gap, not a company-specific data gap.** See §2.8/§5.3/§7 for the full disclosure — Wall Street's post-earnings EPS-estimate revisions had not yet propagated through several vendor feeds (Finviz's own stale EPS TTM field is direct proof of this) at the time of this session, hours after the print. This session made a defensible, disclosed choice (corroborated cluster over a single outlier) but flags this as the one input most likely to move the Composite Score across an action-band boundary within days, not months.
4. **Quality improved marginally (83.2→83.7), driven entirely by Q2 2026's record gross margin.** Every other Quality sub-score is either unchanged (carried-forward Balance Sheet/FCF Quality) or already saturated (Profitability).
5. **The FCF/NI conversion ratio (TTM 54.75%, carried forward) remains a genuine monitoring item**, unresolved this session because TSMC's Q2 2026 cash-flow statement isn't out yet. Worth explicit re-verification once it is (see §11) — if it comes in similarly capex-heavy for a second consecutive fiscal year, the hard-disqualifier question (currently non-firing on a strict reading) would need re-examination, though the capex-carve-out reasoning remains strongly evidenced regardless.
6. **The Arizona $100B claim in the trigger post is accurate but not new** (announced 2026-03-04, over four months before this session) — flagged in §0 as a case of the Telegram source bundling old news with new, worth remembering as a general pattern for future Telegram-triggered sessions.
7. **The ">40% 2026 guidance" claim is plausible but not pinned to primary-source certainty this session** (§0) — doesn't affect scoring either way, since guidance is never a scored input under this framework, but is disclosed rather than silently assumed true.
8. **Geopolitical and concentration risk, unchanged from 2026-07-12**, still real and still not scored directly: Taiwan Strait tension, US export-control policy on TSMC's China operations, and a customer base concentrated in North American hyperscalers/fabless names whose own AI-capex cycles TSMC's growth is levered to.

---

## 10. Recommendation

# **WATCHLIST ONLY — do not enter. Composite Score 53.4 falls in the 50.0–69.9 HOLD/Fair-Value band.**

TSM's Q2 2026 results were genuinely strong and independently verified — this session's Quality Score actually **improved** slightly (83.2→83.7) on the back of a record 67.7% gross margin, and TSMC's own fundamentals cheapened its EV/EBIT multiple even as the stock price fell. But the Composite Score's conclusion is effectively **unchanged** (53.2→53.4, same Hold band): a stronger quarter and a lower price largely offset in this framework's math, and this session's own conservative scenario-weighted Fair Value ($345.13) sits **15.2% below**, not above, the live price — a wider, more negative margin-of-safety gap than the 2026-07-12 session found. **No order setup, no position, no capital deployed.**

**One explicit caveat carried into the next review (§11):** this conclusion depends on a Forward PE input (25.9×) chosen from a wide, disclosed vendor dispersion (19.64×–29.43× across five sources) still settling in the hours after the print. Under the excluded low-end alternate reading, the Composite Score would fall to 48.8 — inside the Buy band. This session does not act on that alternate reading (see §7 for the full reasoning) but flags it prominently rather than either ignoring it or acting on it prematurely.

---

## 11. Next Review Trigger

- **Near-term data-quality re-check (days, not months):** once vendor Forward-PE/consensus-EPS data has had 3–5 trading days to fully digest the Q2 2026 beat (Finviz's stale EPS TTM field should have refreshed by then), re-verify the Forward PE input specifically — if it settles meaningfully below this session's 25.9× figure, the Composite Score could cross into the 30.0–49.9 Buy band per §7's sensitivity, which would warrant a fresh full session, not just a footnote update.
- **TSMC's Q2 2026 SEC 6-K, once filed** (not yet on EDGAR at this session's time) — cross-check this session's press-release-sourced figures against the audited filing, and specifically resolve (a) the unconfirmed NT$63.2B VIS one-time-gain claim (§2.2) and (b) the actual (not guided) Q2 2026 tax rate (§2.4), both currently flagged approximations.
- **TSMC's Q2 2026 balance sheet / cash-flow statement, once available** (vendor data still one quarter behind as of this session) — refresh Net Debt/EBITDA, ROIC, and FCF/NI conversion, all currently carried forward from the Q1 2026 vintage.
- **Q3 2026 earnings**, expected mid-October 2026 per TSMC's historical cadence (guidance already on record this session: revenue $44.6–45.8B, GM 65–67%, OM 56–58%).
- **A pullback toward or below this session's own PW Fair Value (~$345)** would meaningfully improve the entry case — a considerably lower bar than the 2026-07-12 session's ~$434 threshold.
- Any Taiwan Strait geopolitical escalation, new US/China export-control action, or standard Rule 9 triggers (management change, material M&A, a further >15% unexplained move).

**No position opened — nothing to log in `decisions/`.**

---

## 12. Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file — every term below was already defined there prior to this session (added by the 2026-07-12 TSM, 2026-07-05 NVDA, and 2026-07-15 ASML sessions); no new terms were introduced this session.

| Term | Meaning |
|---|---|
| **ADR (American Depositary Receipt)** | A US-exchange-listed security representing shares of a non-US company; TSM = 1 ADR representing 5 TSMC ordinary shares. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — 53.4 for TSM this session, up marginally from 53.2 on 2026-07-12. |
| **CoWoS (Chip-on-Wafer-on-Substrate)** | TSMC's advanced chip-packaging technology; reported "sold out through year-end" this session — cited as fresh scale/capacity-constraint Moat Signal evidence. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization. |
| **EDA (Electronic Design Automation)** | Chip-design software tools; part of this session's unchanged switching-cost Moat Signal citation. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury in the Rate Environment Gate. |
| **Fabless** | A chip company that designs but doesn't manufacture semiconductors (TSMC's customer base). |
| **Fast Grower** | A company growing EPS >15%/yr for 3+ years on a clean, non-distorted earnings base; TSM still does not qualify (§5.4). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income. |
| **Foundry (pure-play foundry)** | A contract chip manufacturer for other companies' designs; TSMC is the dominant one. |
| **Form 6-K / Form 20-F** | A furnished interim report / the annual report foreign private issuers file with the SEC. |
| **Forward PE** | Price ÷ next-twelve-months expected EPS; the single most disputed input in this session (§2.8/§5.3/§7). |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear, Rule 7); $345.13 this session, down from $433.78 on 2026-07-12. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score; none fired for TSM. |
| **HPC (High-Performance Computing)** | Compute-intensive AI/data-center workloads — 66% of TSM's Q2 2026 revenue, up from 58% for FY2025. |
| **Hurdle rate** | The minimum acceptable annual return (10%) the Upside/Downside Modifier measures expected return against. |
| **Invested Capital** | Debt + Equity − Cash, the ROIC denominator. |
| **Moat** | A durable competitive advantage; scored 80.0 (4 of 5 signals) for TSM this session, unchanged. |
| **Net Debt/EBITDA** | This framework's primary balance-sheet-risk gate; TSM's is negative (net cash), carried forward this session. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate). |
| **Open Innovation Platform (OIP)** | TSMC's design-ecosystem program — switching-cost Moat Signal evidence, unchanged citation. |
| **PDK (Process Design Kit)** | Foundry-supplied chip-design rules/IP a customer builds around — switching-cost moat evidence. |
| **PEG ratio** | PE ÷ earnings growth rate; still not scored for TSM (§5.4). |
| **Process node (e.g. "2nm"/"N2", "A16")** | A generation of semiconductor manufacturing technology. |
| **PT (Price Target)** | An analyst's price forecast. |
| **Quality Score** | This framework's 0.0–100.0 continuous score; 80.0+ required for Phase 02. TSM scored 83.7 this session, up from 83.2. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-score check comparing Earnings Yield to the 10-Year Treasury, plus the additive Treasury-bracket adjustment. |
| **R/R (Risk/Reward ratio)** | Not computed this session (no order setup, §8). |
| **ROIC / ROE** | Return on Invested Capital / Return on Equity. |
| **Rule 0 / Rule 4 / Rule 6 / Rule 7 / Rule 9 / Rule 10** | This framework's standing instructions: always fetch live price first; sanity-check implied returns; strip out one-time items before valuing; use a scenario-weighted fair value; force re-valuation on fundamental triggers; separate intrinsic value from market price with a documented catalyst/timeline. |
| **Shareholder yield** | Dividend yield plus net buyback yield. |
| **TAM** | Total Addressable Market. |
| **Treasury yield (10Y)** | This framework's risk-free-rate benchmark. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | The additive ±15 valuation-score adjustment; computed at +3.4 for TSM this session (vs. −0.76 on 2026-07-12 — now a mild trim-pressure reading rather than a near-neutral one, since the price/fair-value gap widened). |
| **Wafer** | The silicon disc a foundry manufactures chips on and prices its capacity by. |


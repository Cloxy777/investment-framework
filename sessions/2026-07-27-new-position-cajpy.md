# NEW POSITION (RE-EVALUATION) — CAJPY (Canon Inc., traded here via the sponsored ADR; primary listing Tokyo Stock Exchange 7751)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run) — a **Rule 9 fundamental-event re-trigger** of the 2026-07-25 FAIL, per that session's own "Next review trigger" note ("Canon's next earnings release... treat any earnings release as a standing Rule 9 trigger regardless")
**Date:** 2026-07-27
**10Y US Treasury Yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (see §3) before the Rate Environment Gate would otherwise apply (same precedent as the 2026-07-25 CAJPY session and others).
**Current CAJPY portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [watchlist/not-in-portfolio/CAJPY/CAJPY-2026-07-25.md](../watchlist/not-in-portfolio/CAJPY/CAJPY-2026-07-25.md) — Quality Score 37.3, **FAIL** (gate 80.0+), full session at [sessions/2026-07-25-new-position-cajpy.md](2026-07-25-new-position-cajpy.md)
**Sector:** Technology / Industrials — Diversified Imaging, Office, Medical & Industrial Equipment
**Filer type:** Japanese primary listing (Tokyo Stock Exchange 7751); as a foreign private issuer Canon files Form 20-F/6-K with the SEC. Traded here via the sponsored ADR **CAJPY**.
**First-use jargon decode:** see closing Glossary.

---

## 0. Why this session exists — trigger source

A Telegram post today (`bolshegold/9841`, ~12:08 UTC, 2026-07-27) reported Canon's actual 1H (six-month) 2026 GAAP results — EPS ¥197.36, revenue ¥2,274.54B (+3.5% Y/Y), a yen-depreciation tailwind, a tariff-related impact of +¥37B, FX gains of +¥34.1B, NIL (nanoimprint lithography) prep for 2027 mass production, a ¥160/share dividend, and a ¥200.0B buyback program. Canon's board did in fact approve and publish six-month results today, 2026-07-27 (confirmed directly from Canon's own IR site and its official results filing — see §2) — a real earnings release, so the prior session's standing Rule 9 trigger fires regardless of the specific numbers in the post.

**Per Rule 0, the Telegram post's numbers were never used as inputs.** Every figure in this session was independently pulled from Canon's own primary-source filings (see §2). Two things worth flagging about the post itself, found during independent verification:
- The EPS figure (¥197.36 diluted) **is accurate** — it matches Canon's own filed six-month results exactly.
- The ¥160/share dividend and ¥200.0B buyback are **not new information from today's release** — both were already announced at Canon's FY2025 full-year results on **2026-01-29** (buyback: up to 54,000,000 shares / ¥200,000 million, acquisition window 2026-01-30 to 2027-01-29; dividend: ¥80 interim + ¥80 year-end = ¥160 total, unchanged). Today's filing explicitly confirms "Revisions to the forecast of cash dividends most recently announced: None." The post conflated an old, already-priced-in capital-return program with today's genuinely new operating results — exactly the kind of thing Rule 0 exists to catch by forcing independent verification rather than taking a social-media summary at face value.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Contract identity** | Confirmed via IBKR, same contract as the 2026-07-25 session: "CANON INC-SPONS ADR", **PINK**, contract_id **12340038** | IBKR |
| **Live price used** | **$27.73** (`last.price`, `is_close: true`) | IBKR `get_price_snapshot`, fetched ~12:15 UTC 2026-07-27 |
| **Cross-check** | `get_price_history` (`ONE_DAY` bars) shows the most recent recorded regular-session close is still **2026-07-24 (Friday) at $27.73** — no new print had posted yet at fetch time this Monday morning (a same-day open/high/low/volume snapshot request returned all zeros, consistent with the thin-volume PINK ADR not yet having traded today). The live snapshot price and the last confirmed close are identical ($27.73), so no staleness ambiguity: this is the most recent real, confirmed trade price available, not an inferred or estimated figure. | IBKR `get_price_history` |
| 52-week range | $25.07 – $32.34 (unchanged from 2026-07-25) | IBKR `misc_statistics` |
| Dividend yield | 1.8% (IBKR) — same discrepancy vs. stockanalysis.com (3.65%) flagged in the 2026-07-25 session remains unreconciled; not load-bearing for the Quality Score gate | IBKR |
| Shares outstanding (updated) | Per Canon's own June 30, 2026 filing (§2): 1,333,763,464 issued − 484,424,702 treasury = **849,338,762 shares outstanding** (essentially unchanged from the 2026-07-25 session's 849.31M — the ongoing buyback is proceeding gradually) | Canon 1H2026 filing |
| Market Cap (USD, ADR basis) | 849,338,762 × $27.73 ≈ **$23.56B** | Derived |
| US 10Y Treasury yield | Not fetched — moot, see header | — |

**Live price used throughout this session: $27.73** (CAJPY ADR, IBKR) — unchanged from the 2026-07-25 session, consistent with no new confirmed trade since Friday's close.

---

## 2. Data Sourcing Note

**Primary source this session: Canon's own official financial-results filings**, fetched directly from `global.canon/en/ir/`:
1. **"Consolidated Financial Results for the Six Months Ended June 30, 2026"** (board-approved and published **today, 2026-07-27** — `global.canon/en/ir/results/2026/rslt2026q2e.pdf`), covering H1 2026 (Jan 1–Jun 30, 2026) with H1 2025 comparatives, full income statement, balance sheet, cash flow statement, and segment detail.
2. **"Consolidated Financial Results for the Fiscal Year Ended December 31, 2025"** (published 2026-01-29 — `global.canon/en/ir/results/2025/rslt2025e.pdf`), needed to reconstruct a trailing-twelve-month (TTM) window (see method below).

Both are Canon's own board-approved results announcements (Japanese "kessan tanshin"-style filings, translated to English for reference; semi-annual reports are explicitly noted as exempt from CPA/audit-firm review, though board-approved and the basis for the subsequent SEC Form 6-K). This is materially **better** sourcing than the previous session's `stockanalysis.com` reliance, and Rule-0-compliant primary-source data throughout.

**stockanalysis.com had not yet refreshed at the time of this session:** a fresh `WebFetch` of `stockanalysis.com/quote/tyo/7751/financials/` returned **identical** TTM/FY figures to the 2026-07-25 session (same "TTM (Mar '26)" label, same numbers to the yen) — i.e. the vendor's data pipeline has not yet ingested today's release. Flagged as a data-timing gap, not a blocker: Canon's own primary filings supersede the vendor regardless.

**TTM reconstruction method** (transparent, arithmetic, no estimation): for every income-statement and cash-flow line, **TTM (period ended June 30, 2026) = FY2025 (full year) − H1 2025 (six months ended June 30, 2025) + H1 2026 (six months ended June 30, 2026)**. All three inputs are directly disclosed, actual (not forecast) figures from Canon's own two filings above — this is subtraction/addition of real reported numbers, not an invented or estimated figure.

**`yfinance` was retried this session and is still unavailable** — the package is not installed in this environment (`ModuleNotFoundError: No module named 'yfinance'`), a different failure mode than the 2026-07-25 session's SSL/429 errors, but the same practical result: not usable this session. Not a blocker given the primary-source filings above are strictly better data anyway.

No required Phase 01 input was invented, estimated, or inferred from the triggering Telegram post.

### 2.1 Core financial data (JPY millions unless noted) — updated TTM (period ended June 30, 2026)

| Metric | **New TTM (Jun '26)** | Prior TTM (Mar '26, 2026-07-25 session) | FY2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|
| Revenue | **4,700,702** | 4,659,984 | 4,624,727 | 2,198,567 | 2,274,542 |
| Gross Profit | **2,249,187** | 2,166,321 | 2,161,955 | 1,035,713 | 1,122,945 |
| Operating Income (EBIT) | **471,677** | 440,285 | 455,390 | 214,308 | 230,595 |
| Net Income (attributable to Canon Inc.) | **347,333** | 308,125 | 332,053 | 155,904 | 171,184 |
| Net Margin | **7.39%** | 6.61% | 7.18% | 7.09% | 7.53% |
| Gross Margin | **47.85%** | 46.49% | 46.75% | 47.11% | 49.37% |
| Operating Cash Flow | **522,432** | 428,470 | 475,903 | 158,892 | 205,421 |
| CapEx (cash-flow-statement basis) | **266,068** | 272,771 | 262,165 | 119,210 | 123,113 |
| Free Cash Flow | **256,364** | 155,699 | 213,738 | 39,682 | 82,308 |
| D&A | **244,531** | n/a (not separately tracked) | 239,236 | 108,743 | 114,038 |
| EBITDA (= EBIT + D&A) | **716,208** | 756,718 (ratio-derived proxy) | — | — | — |
| Income tax | **140,102** | — | 123,906 | 53,970 | 70,166 |
| Income before tax | **511,814** | — | 482,059 | 222,319 | 252,074 |
| Effective tax rate | **27.37%** | — | 25.71% | 24.28% | 27.84% |

*(Every TTM column value = FY2025 − H1 2025 + H1 2026, per the method in §2. Cross-check: FCF TTM 256,364 = FCF FY2025 213,738 − FCF H1 2025 39,682 + FCF H1 2026 82,308 — reconciles exactly.)*

### 2.2 Balance sheet (as of June 30, 2026, vs. December 31, 2025)

| Metric | Jun 30, 2026 | Dec 31, 2025 |
|---|---|---|
| Cash & cash equivalents | 731,922 | 585,981 |
| Short-term loans + current portion of LT debt | 734,789 | 511,139 |
| Long-term debt (excl. current portion) | 404,324 | 304,970 |
| **Total debt** | **1,139,113** | **816,109** |
| **Net debt** (total debt − cash) | **407,191** | 230,128 |
| Total equity | 3,687,079 | 3,774,128 |
| Canon Inc. shareholders' equity | 3,483,846 | 3,491,808 |

Source: Canon's 1H2026 consolidated balance sheet (§2, filing 1).

### 2.3 ROIC — derived from primary-source figures (methodology shown in full, per glossary's NOPAT/Invested Capital definitions)

```
NOPAT (TTM) = EBIT (TTM) × (1 − effective tax rate, TTM)
            = 471,677 × (1 − 0.2737)
            = 471,677 × 0.7263
            = 342,560

Invested Capital (Jun 30, 2026) = Total debt + Total equity − Cash
                                 = 1,139,113 + 3,687,079 − 731,922 = 4,094,270
Invested Capital (Dec 31, 2025) = 816,109 + 3,774,128 − 585,981 = 4,004,256
Average Invested Capital         = (4,094,270 + 4,004,256) / 2 = 4,049,263

ROIC (TTM) = NOPAT / Average Invested Capital = 342,560 / 4,049,263 = 8.46%
```

Flagged as a **computed** figure (formula per [glossary.md](../framework/glossary.md)'s NOPAT/Invested Capital entries, both already established framework conventions), not a vendor-reported number — because `stockanalysis.com` has not refreshed its ratios page since today's release (§2). This is a transparent arithmetic derivation from Canon's own disclosed figures, consistent with "never invent or estimate," not a cosmetic gap; shown in full per operating-brief.md's "no black-box outputs" rule. The prior session's ROIC (7.71%) was a vendor-reported (stockanalysis.com) figure using an unknown internal methodology — the two are not perfectly apples-to-apples, but both land in the same structurally-single-digit range.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29 — unchanged since 2026-07-25)

### 3.1 Hard disqualifier check (fires regardless of weighted score)

| Hard disqualifier | CAJPY data (updated) | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF positive in every period: FY2022 ¥74,076M, FY2023 ¥220,882M, FY2024 ¥369,830M, FY2025 ¥213,738M, **new TTM ¥256,364M**. | **PASS — does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | Net Debt (TTM) ¥407,191M ÷ EBITDA (TTM) ¥716,208M = **0.57×** — well under 2.5× (improved from 0.77× in the 2026-07-25 session, driven by a large H1 2026 cash build). | **PASS — does not fire.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FCF/NI: **new TTM 256,364/347,333 = 73.82%** (now *above* 70%); FY2025 213,738/332,053 = 64.36% (below 70%). Only **one** of the two most recent periods is now below 70% — the "2+ consecutive years" condition no longer holds on the updated TTM basis. This is a material improvement from the 2026-07-25 session, where TTM (50.5%) and FY2025 (64.4%) were *both* below 70%. The growth-capex carve-out documented in the prior session (Utsunomiya semiconductor-lithography plant, still ramping toward 2027 capacity) remains available as a backstop even if a future period dips again. | **PASS — does not fire (does not even reach the raw two-year condition now).** |

No hard disqualifier fires — a stronger PASS than the 2026-07-25 session on this front. **This does not change the bottom-line outcome** — see §3.3.

### 3.2 Sub-scores (all six, updated with fresh TTM data)

| Sub-score (weight) | Formula & inputs | Result (2026-07-25) | **Result (this session)** |
|---|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = 347,333/4,700,702 = **7.39%** → NetMargin_Component = (7.39/30)×100 = 24.63. ROIC (TTM, computed §2.3) = **8.46%** → ROIC_Component = (8.46/30)×100 = 28.20. Profitability_Score = (24.63+28.20)/2 = 26.41 (no FCF-positivity cap — still FCF-positive every year). | 23.87 | **26.41** |
| **Margins (15%)** | Gross Margin (TTM) = 2,249,187/4,700,702 = **47.85%**. GrossMargin_Score = clamp((47.85/80)×100) = 59.81. Gross margin has run 45.3–49.4% across the periods shown (H1 2026 alone was 49.37%, boosted by the Imaging segment's outsized +38.8% H1 operating-profit growth) — still not a clean multi-year structural trend distinct from normal seasonal/mix noise, and moot regardless since gross margin is already above the 40% bonus-eligibility threshold. No bonus applied, unchanged reasoning from 2026-07-25. | 58.11 | **59.81** |
| **Growth (20%)** | Unchanged this session: Revenue 3yr CAGR (FY2022→FY2025, the established annual-figure basis — no new full fiscal year has closed since 2026-07-25) = **4.68%** → base 18.74, **+10 TAM-expansion modifier retained** (Canon's semiconductor-lithography/medical/network-camera growth narrative). The Telegram post's "NIL prep for 2027 mass production" claim is **corroborated** (Canon's NIL — nanoimprint lithography — technology and Utsunomiya-plant 2027 capacity target are real and already documented — see Glossary) but is the **same underlying fact already credited** in the 2026-07-25 session's +10 modifier, not new incremental evidence — no double-counting. Segment detail in today's filing shows a *mixed* short-term picture (Imaging external sales +16.9% H1 YoY; Industrial (semiconductor+FPD lithography) external sales **−9.1%** H1 YoY on soft memory/power-semiconductor demand) — a single-half swing, not the kind of multi-year structural-deceleration evidence the −10 modifier requires, so left unapplied, consistent with 2026-07-25's treatment of the camera-market data point. | 28.74 | **28.74 (unchanged)** |
| **Balance Sheet (15%)** | Net Debt/EBITDA (TTM) = 407,191/716,208 = **0.57×**. BalanceSheet_Score = clamp(100×(1−0.57/4)) = 85.79. | 80.77 | **85.79** |
| **Moat Signal (15%)** | Unchanged: still only **1 of 5 signals** (durable #1 camera-market-share) clears the cited-evidence bar — no new switching-cost, brand-premium, network-effect, or scale-cost citation surfaced this session. (1/5)×100 | 20.0 | **20.0 (unchanged)** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 256,364/347,333 = **73.82%**. FCFQuality_Score = clamp(((0.7382−0.40)/0.60)×100) = 56.37. **The single largest change this session** — up from 17.57, since the new TTM window now includes a strong H1 2026 (FCF/NI 82,308/171,184 = 48.1%... note H1-alone ratios are noisy; it's the trailing-twelve-month blend that matters and that blend improved materially) replacing a weaker year-ago H1. | 17.57 | **56.37** |

### 3.3 Final weighted Quality Score

```
Quality Score = (26.41 × 0.25) + (59.81 × 0.15) + (28.74 × 0.20) + (85.79 × 0.15) + (20.0 × 0.15) + (56.37 × 0.10)
              = 6.6025 + 8.9715 + 5.748 + 12.8685 + 3.000 + 5.637
              = 42.8275 → 42.8 (rounded to nearest 0.1)
```

**42.8 < 80.0 — still fails the gate, by 37.2 points.** An improvement of +5.5 points from the 2026-07-25 session's 37.3 (driven almost entirely by the FCF Quality sub-score's recovery, plus smaller gains in Profitability, Margins, and Balance Sheet), but still a decisive, not a close, miss. Growth (28.74) and Moat (20.0) — together 35% of total weight — are unchanged and remain the two lowest-scoring axes alongside Profitability; nothing in today's release moved either one.

**Sensitivity check** (same structure as the 2026-07-25 session, updated base):

| Growth / Moat reading | Growth_Score | Moat_Score | Quality Score | Gate result |
|---|---|---|---|---|
| Most conservative (Growth modifier nets to 0; Moat drops to 0/5) | 18.74 | 0.0 | 37.8 | FAIL |
| Conservative (Growth nets to 0; Moat stays at 1/5) | 18.74 | 20.0 | 40.8 | FAIL |
| **Primary reading (this session)** | **28.74** | **20.0** | **42.8** | **FAIL** |
| Generous (Switching Costs also credited → Moat 2/5) | 28.74 | 40.0 | 45.8 | FAIL |
| Maximally generous (Moat 3/5) | 28.74 | 60.0 | 48.8 | **FAIL — still 31.2pts short** |

The ceiling under the most generous defensible reading is **48.8** (up from 43.3 on 2026-07-25, still less than 5/8 of the way to the 80.0 bar). **The gate outcome remains robust to every plausible reading of the discretionary inputs** — today's real, materially-better earnings release narrows the gap but does not come remotely close to closing it.

### Result: **Phase 01 FAIL (unchanged verdict, improved score: 37.3 → 42.8)**

Per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md): a company scoring below 80.0 does not proceed to Phase 02. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed** — same as 2026-07-25.

---

## 4. Recommendation

**FAIL — does not clear the Quality Score gate.** Quality Score **42.8** vs. the strict 80.0+ bar, missing by 37.2 points (narrowed from 42.7 points on 2026-07-25, but still a decisive miss, robust to every sensitivity checked — ceiling 48.8 under the most generous defensible reading). No Rate Environment Gate, no Phase 02 valuation score, no fair-value/DCF work, and no order setup were computed — reserved for names that clear the quality bar first.

Canon's actual 1H 2026 results are genuinely better than a year ago — net sales +3.5% Y/Y, operating profit +7.6% Y/Y, net income +9.8% Y/Y, diluted EPS +16.7% Y/Y (partly boosted by a one-off ¥10.07/share depreciation-method accounting change, disclosed transparently in the filing's own notes) — and the balance sheet strengthened further (Net Debt/EBITDA down to 0.57× from 0.77×, FCF/NI conversion recovered above 70%). But this framework's specific bar for a "high-quality compounder" is about structural characteristics, not a single good half: **Profitability remains structurally single-digit** (net margin 7.39%, ROIC ~8.46%), **top-line growth remains modest** (3yr CAGR still 4.68% on an annual basis — no new full fiscal year has closed to update this), and **Moat evidence remains thin** (still just 1 of 5 signals). None of today's release changes any of those three structural facts. The triggering event was real (a genuine Rule 9 earnings release), and the framework worked exactly as intended: it re-evaluated with fresh, independently-sourced data rather than reacting to the Telegram post's framing, and reached a materially-informed (score moved +5.5 points) but ultimately unchanged conclusion.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mechanical trigger:** Growth (28.74) and Moat (20.0) are now the two lowest-scoring sub-scores (respectively 20% and 15% of total weight) — Profitability (26.41) and FCF Quality (56.37) both improved this session and are no longer the primary drag. A documented acceleration in consolidated (not just segment-level) revenue growth, or a newly-cited, Canon-specific switching-cost/brand-premium/scale-cost data point, would be the most direct path to a materially different result — though even the maximally generous sensitivity reading this session only reaches 48.8, so it would still take coordinated improvement across multiple sub-scores simultaneously to approach the 80.0 gate.
- **Rule 9 events:** Canon's Q3/9-month 2026 results (typically reported late October/early November), a guidance revision (today's filing reaffirmed full-year FY2026 guidance unchanged in dividend terms but the operating/net-income *projection* column shown in the filing implies only modest H2 deceleration expected — not itself a revision), management change, material M&A, or a >15% stock-price move with no identified cause.
- Absent any of the above, future Telegram mentions of CAJPY should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Watchlist & Stale-Score Actions

- Per [watchlist/README.md](../watchlist/README.md)'s "significant change" rule, a Rule 9 fundamental-event trigger firing (this session) **and** a valuation/quality-score change (37.3 → 42.8) both independently qualify as a "significant update" — so the entry file is renamed (`git mv`) from `CAJPY-2026-07-25.md` to `CAJPY-2026-07-27.md`, git history preserving the prior version, with a new dated row appended to the same table (the 2026-07-25 row is retained, not deleted).
- CAJPY carries no `⚠️ STALE SCORE` banner and has no row in [watchlist/STALE.md](../watchlist/STALE.md) — correct, since it is a Phase 01 FAIL / not-scored entry, which the stale-score mechanism explicitly excludes (no Phase 02/Composite Score exists for a methodology change to invalidate). Nothing to clear.

---

## 8. Data Gaps Flagged (summary — none blocked scoring)

1. **`yfinance` still unavailable** — this session, the failure mode was `ModuleNotFoundError` (package not installed), rather than the 2026-07-25 session's SSL/429 errors. Not a blocker: Canon's own primary-source filings (§2) are strictly better data than `yfinance` would have provided anyway.
2. **`stockanalysis.com` had not refreshed** to reflect today's release at the time of this session (confirmed via direct comparison — identical figures to the 2026-07-25 session). Not a blocker: primary-source filings used instead throughout.
3. **ROIC is a computed figure** (§2.3), not a vendor-reported one, since no vendor had refreshed post-release data available. Shown in full per "no black-box outputs" — flagged as a methodology note, not a blocker, consistent with the prior session's ROIC-sourcing caveat.
4. **Dividend yield discrepancy** between IBKR (1.8%) and `stockanalysis.com` (3.65%) remains unreconciled from the 2026-07-25 session — not load-bearing for the Quality Score gate.
5. **No new full fiscal year has closed** since 2026-07-25, so the Growth sub-score's 3yr revenue CAGR still uses the FY2022→FY2025 annual-figure basis rather than a TTM-rolled equivalent — consistent with the established methodology, not treated as a gap requiring estimation.

None of these gaps blocked scoring — every required Phase 01 input was obtained from Canon's own primary-source filings and cross-checked internally (e.g. the FCF-TTM reconciliation in §2.1).

---

## Glossary

- **ADR (American Depositary Receipt) / Sponsored ADR** — see [glossary.md](../framework/glossary.md).
- **CAGR (Compound Annual Growth Rate)** — see [glossary.md](../framework/glossary.md).
- **EBIT / EBITDA** — see [glossary.md](../framework/glossary.md).
- **Form 20-F / Form 6-K** — see [glossary.md](../framework/glossary.md).
- **Gross Margin** — see [glossary.md](../framework/glossary.md).
- **Hard disqualifier** — see [glossary.md](../framework/glossary.md).
- **Invested Capital** — see [glossary.md](../framework/glossary.md). Computed here as Total Debt + Total Equity − Cash, per this framework's standard netting convention.
- **Moat** — see [glossary.md](../framework/glossary.md).
- **Net Debt/EBITDA** — see [glossary.md](../framework/glossary.md).
- **Net Margin** — see [glossary.md](../framework/glossary.md).
- **NIL (Nanoimprint Lithography)** — see [glossary.md](../framework/glossary.md). New term this session — added because the triggering Telegram post referenced it directly.
- **NOPAT (Net Operating Profit After Tax)** — see [glossary.md](../framework/glossary.md). Used this session to compute ROIC directly from Canon's primary-source filings.
- **Phase 01–06** — see [glossary.md](../framework/glossary.md).
- **Quality Score** — see [glossary.md](../framework/glossary.md). CAJPY scores 42.8 this session (up from 37.3 on 2026-07-25).
- **ROIC (Return on Invested Capital)** — see [glossary.md](../framework/glossary.md).
- **Rule 0** — see [glossary.md](../framework/glossary.md).
- **Rule 9** — see [glossary.md](../framework/glossary.md). This session exists because a Rule 9 earnings-release trigger fired.
- **TAM (Total Addressable Market)** — see [glossary.md](../framework/glossary.md).
- **TTM (Trailing Twelve Months)** — see [glossary.md](../framework/glossary.md).

**New term added to [framework/glossary.md](../framework/glossary.md) this session:** NIL (Nanoimprint Lithography).

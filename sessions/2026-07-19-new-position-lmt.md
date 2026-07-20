# NEW POSITION — LMT (Lockheed Martin Corporation, NYSE) — 2026-07-19

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 19 Jul 2026 (Sunday trigger; session run 2026-07-20 00:17 UTC, before the US market open)
**10Y US Treasury Yield:** 4.57% (FRED `DGS10`, most recent posted observation dated 2026-07-16 — 07-17 through 07-19 not yet posted, normal FRED reporting lag; recorded for completeness only, since this session stops at the Quality Gate, before the Rate Environment Gate would apply — see §5)
**Current LMT portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); grep for "LMT" returns no match)
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/LMT/` or `watchlist/not-in-portfolio/LMT/`, confirmed via `find`/`glob`)
**Sector:** Industrials / Aerospace & Defense — prime defense contractor (aircraft, missiles/fire control, rotary/mission systems, space)
**First-use jargon decode:** see closing Glossary (§9)

---

## 0. Why this session exists — trigger source

A post on **bolshegold** (Telegram, post bolshegold/9795, ~09:46 UTC 2026-07-19) previewed the upcoming earnings-reporting week, naming **$LMT and $E** together and suggesting their energy/defense-sector ("энергетику и ВПК") forecasts were "worth checking," with an expectation of demand boosts and cost tailwinds tied to Strait-of-Hormuz/Iran tensions. Per the operating brief and this repo's standing convention (see the AXP, CELH, RYAAY precedent sessions from the same day), **a first-ever mention of a name with no watchlist entry triggers a full `/new-position` evaluation regardless of the mention's substance.** LMT has no existing watchlist entry and is not a current holding (confirmed above), so this session is that evaluation, built entirely from independently, primary-sourced data (SEC EDGAR/XBRL, IBKR live price, third-party GAO/industry reports). **The Telegram post's Iran/Strait-of-Hormuz/demand-tailwind narrative is not used as a financial input anywhere below** — it is the reason this session runs, nothing more.

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("LMT")`: contract_id **611191**, exchange **NYSE**, description "LOCKHEED MARTIN CORP" — the correct primary US listing (other results returned a Toronto CDR, a Mexican cross-listing, a Swiss EBS quote, and unrelated leveraged single-stock ETFs "LMTL"/"LMTS.OLD" — none used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$508.77** | IBKR `get_price_snapshot`, `last` field, contract_id **611191** (NYSE). `is_close: true` — session run at 2026-07-20 00:17 UTC, before the US market open (NYSE opens 13:30 UTC) — this is the last completed-session close (Friday 2026-07-17), the most recent price obtainable via a live fetch attempt at session time, flagged here as a close rather than an intraday quote (same situation as the 2026-07-19 AXP/RYAAY sessions). |
| 52-week high | $691.98 | IBKR `misc_statistics` `high_52w` |
| 52-week low | $401.84 | IBKR `misc_statistics` `low_52w` |
| 13-week high | $597.98 | IBKR `misc_statistics` `high_13w` |
| 26-week high | $691.98 | IBKR `misc_statistics` `high_26w` |
| Open 52 weeks ago | $460.00 | IBKR `misc_statistics` `open_52w` |
| Dividend yield | 2.66% | IBKR `get_price_snapshot` `dividend_yield` field |
| Year-to-date change | +$27.55 (+5.73%) | IBKR `year_to_date_change` |
| US 10Y Treasury yield | 4.57% | FRED `DGS10`, as-of 2026-07-16 |

$508.77 sits roughly in the middle-to-lower half of its 52-week range ($401.84–$691.98) — down sharply from its 52-week high, context only, not scored.

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

`yfinance` failed in this session's environment with the same `curl_cffi` TLS/connection-reset error documented in the 2026-07-12/07-14/07-19 (C, JPM, AXP) sessions. **Fallback used:** SEC EDGAR full-text search and the SEC XBRL `companyconcept`/`companyfacts` APIs (`data.sec.gov/api/xbrl/...CIK0000936468...`) for primary-sourced, audited/reported figures (LMT's CIK is **936468**); GAO (Government Accountability Office) reports and Lockheed Martin's own press releases for F-35 program cost/scale data; and third-party aggregators (stockanalysis.com, financecharts.com — via WebFetch/WebSearch) for Forward PE / 5yr-average-PE cross-checks only, since the primary `yfinance`-based reconstruction method in [valuation-scoring.md](../framework/valuation-scoring.md) could not run. **This session did not reach Phase 02, so those PE cross-checks are shown for context in §6 but not scored.**

### 2.2 Income statement, cash flow, balance sheet — primary-sourced (SEC XBRL)

**Annual (10-K), FY2021–FY2025, all in $M:**

| FY | Revenue | Net Income | Operating Income (EBIT) | Gross Profit | OCF | CapEx | FCF | FCF/NI |
|---|---|---|---|---|---|---|---|---|
| 2021 | 67,044 | 6,315 | 9,123 | 9,061 | 9,221 | 1,522 | 7,699 | 121.94% |
| 2022 | 65,984 | 5,732 | 8,348 | 8,287 | 7,802 | 1,670 | 6,132 | 106.98% |
| 2023 | 67,571 | 6,920 | 8,507 | 8,479 | 7,920 | 1,691 | 6,229 | 90.01% |
| 2024 | 71,043 | 5,336 | 7,013 | 6,930 | 6,972 | 1,685 | 5,287 | 99.08% |
| 2025 | 75,048 | 5,017 | 7,731 | 7,619 | 8,557 | 1,649 | 6,908 | 137.69% |

Sources: `us-gaap:Revenues`, `us-gaap:NetIncomeLoss`, `us-gaap:OperatingIncomeLoss`, `us-gaap:GrossProfit`, `us-gaap:NetCashProvidedByUsedInOperatingActivities`, `us-gaap:PaymentsToAcquireProductiveAssets` (LMT's CapEx tag — `PaymentsToAcquirePropertyPlantAndEquipment` stopped being used after FY2012), all pulled directly from LMT's own 10-K XBRL filings.

**Company is FCF-positive in all 5 years shown, and FCF/NI exceeds 70% in every year except FY2023 (90.0%, still comfortably above 70%)** — clears both cash-flow-related hard disqualifiers with a wide margin (§3.1).

**TTM window (Jul 2025 – Mar 2026, the most recent complete-quarter window available — Q2 2026 has not yet been reported; LMT's Q1 2026 10-Q was filed 2026-04-23, and no Q2 2026 8-K/10-Q has been filed as of this session):**

```
TTM = FY2025 total − Q1 2025 (Jan–Mar) + Q1 2026 (Jan–Mar)
```

| Metric | Q1 2025 | FY2025 | Q1 2026 | TTM |
|---|---|---|---|---|
| Revenue | 17,963 | 75,048 | 18,021 | **75,106** |
| Net Income | 1,712 | 5,017 | 1,488 | **4,793** |
| Operating Income (EBIT) | 2,372 | 7,731 | 2,063 | **7,422** |
| Gross Profit | 2,323 | 7,619 | 2,078 | **7,374** |
| Pretax income | 2,036 | 5,922 | 1,774 | **5,660** |
| Income tax expense | 324 | 905 | 286 | **867** |
| Operating cash flow | 1,409 | 8,557 | 220¹ | **7,368** |
| CapEx | 454 | 1,649 | 511 | **1,706** |
| D&A | 397 | 1,687 | 398 | **1,688** |

¹ LMT reports OCF/CapEx cumulatively (YTD) within the fiscal year in its 10-Qs, not standalone-quarterly; Q1 figures are the first-quarter YTD value directly, and Q2/Q3/Q4 2025 standalone figures were backed out by subtracting successive YTD cumulative totals (e.g. Q2 2025 standalone OCF = H1 2025 YTD $1,610M − Q1 2025 $1,409M = $201M) before summing into the TTM window shown. Same method used for all TTM figures above — no invented or estimated values, only arithmetic on directly-filed XBRL figures.

**TTM FCF = $7,368M − $1,706M = $5,662M. TTM FCF/NI = 5,662 / 4,793 = 118.13%.**

**Effective tax rate (TTM) = 867 / 5,660 = 15.32%.**

### 2.3 A documented one-off materially depresses the TTM window

Q2 2025 standalone results were sharply lower than the surrounding quarters (Operating Income $748M vs. $2,372M in Q1 2025 and $2,280M in Q3 2025; Net Income $342M vs. $1,712M in Q1 2025). This is consistent with Lockheed Martin's own publicly reported Q2 2025 results, which disclosed a roughly $1.6B pre-tax charge tied to classified-program and Canadian Maritime Helicopter Program (CH-148 Cyclone) cost growth in the Aeronautics and Missiles & Fire Control segments. **This session scores off the GAAP figures as filed (per the same precedent set in the 2026-07-13/07-16 UNH sessions, which encountered an analogous one-time-charge distortion) — the charge is not backed out or normalized anywhere in the Quality Score below.** It is the single largest driver of the TTM window's depressed Net Margin and, to a lesser extent, its Gross Margin (§3.2, §3.3).

### 2.4 Balance sheet — primary-sourced (SEC XBRL)

| Item | FY2025 (2025-12-31) | Q1 2026 (2026-03-29, latest) |
|---|---|---|
| Long-term debt (noncurrent) | $20,532M | $20,529M |
| Long-term debt (current) | $1,168M | $168M |
| **Total debt** | **$21,700M** | **$20,697M** |
| Cash & equivalents | $4,121M | $1,894M |
| **Net debt** | **$17,579M** | **$18,803M** |
| Stockholders' equity | $6,721M | $7,489M |
| Total assets | $59,840M | $59,238M |
| Total liabilities | $53,119M | $51,749M |

**Remaining Performance Obligations (RPO / backlog)** — `us-gaap:RevenueRemainingPerformanceObligation`, directly filed:

| Date | RPO |
|---|---|
| 2024-06-30 | $158.3B |
| 2024-12-31 (FY2024-end) | $176.0B |
| 2025-03-30 (Q1 2025) | $173.0B |
| 2025-12-31 (FY2025-end) | $193.6B |
| 2026-03-29 (Q1 2026, latest) | $186.4B |

FY2024-end → FY2025-end backlog growth: **+10.0% YoY** — outpacing the period's ~5.6% revenue growth (FY2024 $71.04B → FY2025 $75.05B). Q1 2025 → Q1 2026: **+7.75% YoY**. Used as documented TAM-expansion evidence in §3.2 (Growth sub-score modifier) — this is actual, filed, signed-contract backlog, not company guidance.

### 2.5 Moat evidence — third-party and primary sourced

- **Market share (Defense News / Motley Fool / industry press, third-party):** Lockheed Martin is reported as the world's largest defense contractor by revenue, a position it has reportedly held for roughly 15 consecutive years, with ~96% of its revenue from defense/aerospace programs (Motley Fool, Fed-Spend, Defense News Top 100 coverage, 2025–2026). The F-35 program specifically: nearly 1,300 aircraft delivered across 12 nations as of early 2026 — reported to outnumber all rival fifth-generation fighters combined — with a record 191 aircraft delivered in 2025 and a further 416-aircraft backlog against a ~3,000-aircraft total planned production run (Aerotime, Army Recognition, Aviation A2Z, Jan 2026 reporting on Lockheed Martin's own delivery announcement).
- **Switching costs — GAO-documented (third-party, non-company-sourced):** The F-35 program was structured by the Pentagon under **Total System Performance Responsibility (TSPR)**, giving Lockheed Martin control of the program's intellectual property, spare parts, and technical data, with the Department of Defense lacking the contractual right to use its own maintenance workforce or hire third-party vendors for sustainment work. Multiple GAO reports (GAO-20-316, GAO-23-105341, GAO-25-107632, and GAO-24-106703 on rising sustainment costs) document this as an ongoing, structural vendor-lock-in issue — a documented mechanism, not an inferred one.
- **Scale cost advantage — LMT/DoD-documented (primary + third-party):** F-35A unit flyaway cost fell below $80M for the first time with the Lot 14 pricing agreement (2019), a 12.8% reduction from the prior lot, per Lockheed Martin's own 2019 press release; the joint Lots 12–13–14, $34B multi-lot agreement achieved an average 12.7% cost reduction across all three F-35 variants — a documented cost-per-unit decline driven by production-volume scale (bulk-buy economies of scale as Low-Rate Initial Production ramped toward full-rate production).
- **Brand premium** — no citation found this session of price increases sustained without volume loss (the consumer-brand-premium evidentiary bar this framework's Moat Signal checklist requires); defense-prime pricing is negotiated contract-by-contract with the US government and allied militaries, not retail/brand-driven. **Not credited.**
- **Network effect** — no documented two-sided-market or user-growth-driven-value mechanism identified for a hardware/weapons-systems manufacturer. **Not credited.**

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years without a growth-capex explanation | 121.9% / 107.0% / 90.0% / 99.1% / 137.7% (FY2021–FY2025) — every year at or above 90%, none below 70% | disqualify if 2+ consecutive years sub-70% | ✅ **PASS**, clean |
| Net Debt/EBITDA over threshold | FY2025 (annual): Net Debt $17,579M / EBITDA $9,418M (EBIT $7,731M + D&A $1,687M) = **1.87×**. TTM (latest quarter): Net Debt $18,803M / EBITDA $9,110M (EBIT $7,422M + TTM D&A $1,688M) = **2.06×** | disqualify if >2.5× (standard; LMT is not asset-light/payment-network, so the 4× Upgrade 5 override doesn't apply) | ✅ **PASS** — both readings under 2.5× |
| FCF-positive 3+ consecutive years | All 5 of the last 5 fiscal years positive | disqualify if not | ✅ **PASS**, clean |

**No hard disqualifier fires.** Unlike the AXP/JPM/Citigroup/SOFI sessions, LMT reports conventional GAAP EBIT/EBITDA/Gross Profit lines — every sub-score below is directly computable, with no structural "N/M, not computable" gap. This is a genuine, decisive weighted-score outcome, not an indeterminate one.

### 3.2 Quality Score — component calculations

**PROFITABILITY (25% weight):**
```
Net Margin (TTM) = 4,793 / 75,106 = 6.383%
NetMargin_Component = clamp((6.383/30)×100, 0, 100) = 21.28

ROIC:
  NOPAT = EBIT_TTM × (1 − eff. tax rate) = 7,422 × (1 − 0.1532) = 7,422 × 0.8468 = $6,285.6M
  Invested Capital (latest quarter, Q1 2026) = Total Debt + Equity − Cash
                                              = 20,697 + 7,489 − 1,894 = $26,292M
  ROIC = 6,285.6 / 26,292 = 23.91%
ROIC_Component = clamp((23.91/30)×100, 0, 100) = 79.70

Profitability_Score = (21.28 + 79.70) / 2 = 50.49   (no FCF-positivity cap — 5yr positive, §3.1)
```
The Net Margin figure is materially depressed by the documented Q2 2025 one-off charge (§2.3) — flagged, not adjusted for, per framework precedent.

**MARGINS (15% weight):**
```
Gross Margin (TTM) = 7,374 / 75,106 = 9.82%
GrossMargin_Score = clamp((9.82/80)×100, 0, 100) = 12.28
```
No structural-expansion bonus: the 3-year gross-margin trend is flat-to-declining, not expanding — FY2023 12.55% (8,479/67,571) → FY2024 9.75% (6,930/71,043) → FY2025 10.15% (7,619/75,048), with the TTM figure (9.82%) at the low end of that range. This decline reflects a documented pattern of program-cost charges recurring across both FY2024 and FY2025, not a one-off confined to Q2 2025 alone (§2.3) — a genuine, structural margin-quality concern for this candidate, not an artifact of the TTM window choice.

**GROWTH (20% weight):**
```
Revenue 3yr CAGR (FY2022 $65,984M → FY2025 $75,048M) = (75,048/65,984)^(1/3) − 1 = 4.385%
Growth_Score (raw) = clamp((4.385/25)×100, 0, 100) = 17.54
```
**TAM/pricing-power modifier (+10):** documented, filed backlog (RPO) evidence (§2.4) — RPO grew +10.0% YoY (FY2024-end $176.0B → FY2025-end $193.6B) and +7.75% YoY (Q1 2025 $173.0B → Q1 2026 $186.4B), both outpacing the ~5.6% revenue growth over the same window — real, signed-contract demand growing faster than recognized revenue. Guidance (LMT's own FY2026 EPS guidance of $29.35–$30.25) is deliberately **not** used as evidence here, per this framework's standing rule that self-issued guidance is a re-valuation trigger, not a scored input.
```
Growth_Score = 17.54 + 10 = 27.54
```
No deceleration modifier — growth is slow but not documented as *structurally decelerating*; if anything, backlog growth is outpacing revenue growth.

**BALANCE SHEET (15% weight):**
```
Net Debt/EBITDA (TTM, latest quarter) = 18,803 / 9,110 = 2.064×
BalanceSheet_Score = clamp(100 × (1 − 2.064/4), 0, 100) = clamp(100 × 0.516, 0, 100) = 48.40
```

**MOAT SIGNAL (15% weight):**

| Signal | Evidence | Result |
|---|---|---|
| Market share stable/growing | Reported world's-largest-defense-contractor-by-revenue position (~15 consecutive years, third-party industry press); F-35 fleet ~1,300 delivered, outnumbering all rival 5th-gen fighters combined, record 191 delivered 2025, 416-aircraft backlog of ~3,000 planned (§2.5) | ✅ TRUE |
| Brand premium | No citation found of price increases sustained without volume loss — not a retail/brand-driven pricing model | ❌ not established |
| Network effect | No documented two-sided-market mechanism | ❌ not established |
| Switching costs | GAO-documented (GAO-20-316, GAO-23-105341, GAO-25-107632): F-35's Total System Performance Responsibility (TSPR) structure gives LMT control of IP/spare parts/technical data; DoD lacks rights to use its own workforce or third-party vendors for sustainment (§2.5) | ✅ TRUE |
| Scale cost advantage | F-35A unit cost fell below $80M with the Lot 14 agreement (2019, −12.8% vs. prior lot); Lots 12–13–14 multi-lot deal achieved a further average −12.7% across all variants — documented cost-per-unit decline from production-volume scale (§2.5) | ✅ TRUE |

```
Moat_Score = (3/5) × 100 = 60.0
```

**FCF QUALITY (10% weight):**
```
FCF/NI (TTM) = 5,662 / 4,793 = 118.13%
FCFQuality_Score = clamp(((1.1813 − 0.40)/0.60)×100, 0, 100) = clamp(130.2, 0, 100) = 100.0   (clamped)
```
(Using the most recent complete fiscal year, FY2025, instead: FCF/NI = 6,908/5,017 = 137.7% — also clamps to 100.0. Same result either basis.)

### 3.3 Quality Score — final calculation

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

              = 0.25×50.49 + 0.15×12.28 + 0.20×27.54 + 0.15×48.40 + 0.15×60.0 + 0.10×100.0
              = 12.6225 + 1.842 + 5.508 + 7.26 + 9.0 + 10.0
              = 46.23
```

**Quality Score = 46.2** (rounded to nearest 0.1, per the score boundary rule).

### 3.4 Gate result: **FAIL — 46.2 < 80.0**

**This is a clean, decisive fail, not an indeterminate one.** No hard disqualifier fires, and every sub-score is directly computable from LMT's own conventional GAAP financials (unlike the structural gaps hit in the AXP/JPM/Citigroup/SOFI sessions) — the low score is a genuine reflection of currently weak profitability (TTM Net Margin 6.38%, depressed by a documented Q2 2025 program-cost charge — §2.3), a low and non-expanding Gross Margin (9.82% TTM, below the 40% reference and trending down from ~12.5% in FY2023), and slow top-line growth (4.39% 3yr revenue CAGR, below the Phase 01 >8% screening threshold even before any weighting) that a real, backlog-driven demand signal (+10 modifier) and a still-solid Balance Sheet (48.4) and Moat (60.0) aren't enough to offset.

Per the command specification: **this session stops here.** No Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.

---

## 4. Why the Telegram post's framing doesn't change this conclusion

The triggering post's suggestion of "demand boosts and cost tailwinds" from Strait-of-Hormuz/Iran tensions is a forward-looking, catalyst-style claim — exactly the kind of unverified, non-primary-sourced input this framework's Rule 0 exists to keep out of any scored figure. Nothing in this session's independently-sourced data (SEC XBRL financials through Q1 2026, GAO reports, LMT's own press releases) reflects or requires that narrative — the Quality Score above is computed entirely from filed financials and documented third-party evidence, and would be unchanged whether or not the Telegram post's geopolitical thesis proves out. If a specific, dated fundamental event tied to that thesis materializes (a confirmed new contract award, a guidance revision, a materially different backlog print), that would be a Rule 9 trigger for re-evaluation — the post itself is not.

---

## 5. Recommendation: **PASS (no entry) — Quality Score 46.2, fails the 80.0+ gate**

**Do not enter LMT.** The Quality Gate is the framework's mandatory first checkpoint (per [quality-scoring.md](../framework/quality-scoring.md) and the `/new-position` command spec) — a company must score 80.0+ before any valuation work is even attempted, regardless of how the stock's price or multiples look. LMT's 46.2 is well short of that bar. **No Rate Environment Gate, Phase 02 valuation score, Composite Score, fair value, or order setup was computed or is appropriate here.**

This is not a judgment that Lockheed Martin is a "bad company" — it holds a genuinely dominant, well-documented competitive position (world's-largest-defense-contractor scale, GAO-documented sustainment lock-in, real backlog growth) — but this framework's Quality Score is measuring *current* profitability, margin trend, and revenue growth against a strict 80.0+ bar, and on those dimensions LMT is currently weak, weighed down by a real, filed program-cost charge and multi-year sub-8%-CAGR revenue growth. A future re-score could look different if margins normalize and growth accelerates (see §7 triggers below).

---

## 6. Context-only market multiples (not scored — session stopped at the Quality Gate)

Shown for completeness/context only, since Phase 02 was never reached:

| Metric | Value | Basis |
|---|---|---|
| Market Cap | $117.30B | Live price $508.77 × 230,563,608 shares outstanding (SEC `dei:EntityCommonStockSharesOutstanding`, as of 2026-04-20) |
| Enterprise Value | $136.11B | Market Cap + Total Debt ($20,697M) − Cash ($1,894M), Q1 2026 |
| EV/EBIT (TTM, self-computed) | 18.34× | EV $136.11B ÷ TTM EBIT $7,422M |
| FCF Yield (TTM, self-computed) | 4.83% | TTM FCF $5,662M ÷ Market Cap $117.30B |
| Forward PE (self-computed) | ~17.0× | Live price $508.77 ÷ third-party consensus FY2026 EPS estimate ~$29.92 (analyst consensus, not LMT's own guidance) |
| 5yr average PE (third-party, cross-checked) | ~19.8–20.1× | stockanalysis.com annual-PE series (FY2021–FY2025: 15.62/22.46/16.45/21.78/22.51, avg 19.76×) cross-checked against financecharts.com's independently-reported 5yr average (20.12×) — reasonably consistent |

None of the above feeds any score in this session — shown only because a reader may otherwise wonder whether the stock "looks cheap" independent of the Quality Gate result. It is not scored because the framework's Quality Gate blocks Phase 02 outright at a sub-80.0 Quality Score.

---

## 7. Next Review Trigger

No routine re-check is scheduled on a numeric valuation-score basis (no Phase 02 score exists to go stale — only the Quality Score, which itself failed the gate). Re-evaluate on any of the following:

- **LMT's Q2 2026 earnings** — not yet filed as of this session (most recent filing is the Q1 2026 10-Q, filed 2026-04-23); the Telegram post's "reporting this week" framing suggests this is imminent. A fresh TTM window would roll off the Q2 2025 one-off charge (§2.3) and could materially change the Profitability/Margins sub-scores.
- **A confirmed, dated fundamental event** tied to the triggering post's Iran/Strait-of-Hormuz thesis (e.g. a specific new contract award, a supplemental defense appropriation naming LMT programs) — not the narrative itself.
- The standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move.

Absent any of the above, a future Telegram mention of LMT should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 8. Data Gaps Flagged

1. **`yfinance` failed in this environment** (same `curl_cffi` TLS/connection-reset error as prior sessions) — all scored figures were reconstructed from SEC XBRL primary sources instead (§2.1); no gap in the scored inputs resulted, but this is noted per the framework's data-sourcing discipline.
2. **5yr PE range/average is third-party-sourced** (stockanalysis.com, financecharts.com), not independently reconstructed via the quarterly-TTM-EPS method in [valuation-scoring.md](../framework/valuation-scoring.md), since that method depends on the broken `yfinance` pull. **Immaterial to this session's conclusion** — Phase 02 was never reached, so this figure is shown only as context (§6), not scored.
3. **TTM operating cash flow and CapEx were reconstructed from YTD-cumulative 10-Q disclosures** (LMT reports OCF/CapEx as YTD figures within a fiscal year, not standalone-quarterly) by subtracting successive cumulative totals (§2.2, footnote) — arithmetic only on directly-filed figures, not an estimate, but flagged for transparency.
4. **TTM D&A was reconstructed** as FY2025 total ($1,687M) − Q1 2025 ($397M) + Q1 2026 ($398M) = $1,688M, since LMT does not separately disclose standalone Q2/Q3/Q4 D&A — same non-invented arithmetic-reconstruction method used elsewhere in this session for TTM figures.

None of these gaps affects the Quality Gate conclusion (§3.4) — all Quality Score inputs are grounded in directly-filed SEC XBRL figures or GAO/company-sourced qualitative evidence.

---

## 9. Glossary

| Term | Meaning |
|---|---|
| **10-K / 10-Q** | Annual / quarterly SEC financial-disclosure filings — LMT's CIK is 936468. |
| **Backlog / RPO (Remaining Performance Obligations)** | The dollar value of signed, contracted work not yet recognized as revenue — LMT's RPO grew to $193.6B at FY2025-end (+10.0% YoY), used as documented TAM-expansion evidence (§2.4, §3.2). Full entries in [glossary.md](../framework/glossary.md). |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization — operating-profit measures; LMT reports both in conventional GAAP form (unlike the AXP/JPM/Citigroup financial-company sessions). |
| **Effective tax rate** | Income tax expense ÷ pretax income for a period — used to convert EBIT into NOPAT for the ROIC calculation (§3.2). |
| **EV/EBIT, EV/EBITDA** | Enterprise Value divided by EBIT or EBITDA — how expensive a company is relative to operating profit. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check). LMT's FCF/NI ran 90–138% across FY2021–FY2025 — comfortably clean (§3.1). |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook. |
| **GAO (Government Accountability Office)** | The independent, nonpartisan US congressional watchdog agency that audits and reports on federal agency programs and spending, including Department of Defense weapons-system acquisition and sustainment — a third-party (non-company-sourced) citation basis for this framework's Moat Signal and risk findings on defense contractors, e.g. multiple GAO reports (GAO-20-316, GAO-23-105341, GAO-25-107632) documenting structural sustainment/vendor-lock-in issues in the F-35 program, cited in this framework's 2026-07-20 LMT session. *(New term.)* |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. None fired for LMT this session (§3.1). |
| **Invested Capital** | The total capital (debt + equity, netted for cash) put to work in a business — the denominator of ROIC. |
| **LRIP (Low-Rate Initial Production)** | The initial, small-batch manufacturing phase of a US defense acquisition program (before "full-rate production"), used to validate manufacturing processes before committing to large production volumes — unit costs in LRIP lots are typically much higher than in later full-rate-production lots, since fixed tooling/setup costs spread across far fewer units. The F-35 program's unit-cost decline from early LRIP lots to the Lot 12–14 agreement (average −12.7%, F-35A falling below $80M) reflects this scale effect — cited as Moat Signal "scale cost advantage" evidence (§2.5, §3.2). *(New term.)* |
| **Moat** | A durable competitive advantage protecting a business's profits from competitors. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the numerator of ROIC. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. LMT's score this session is 46.2 (§3.3–3.4). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. LMT's TTM ROIC is 23.91% (§3.2), a genuine strength offset by weak Net Margin (below). |
| **TSPR (Total System Performance Responsibility)** | A US Department of Defense acquisition strategy (used for the F-35 program) that gives the prime contractor near-total control over a weapon system's intellectual property, spare parts, and technical data, with the contractor performing the majority of sustainment work itself rather than the government retaining the right to use its own personnel or hire third-party vendors — a documented, GAO-cited structural switching-cost/vendor-lock-in mechanism, cited as Moat Signal "switching costs" evidence for Lockheed Martin in this framework's 2026-07-20 LMT session (§2.5, §3.2). *(New term.)* |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — this session used Apr 2025–Mar 2026 (FY2025 minus Q1 2025 plus Q1 2026), the most recent complete window available since Q2 2026 hasn't yet been reported (§2.2). |
| **XBRL** | The structured, machine-readable data format the SEC requires public companies to tag their financial-statement figures in — used throughout this session to pull LMT's own filed figures directly. |

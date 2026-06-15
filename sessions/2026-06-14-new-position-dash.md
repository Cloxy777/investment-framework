# NEW POSITION — DASH (DoorDash, Inc.) — 2026-06-14

**Task type:** NEW POSITION
**Date:** 14 Jun 2026
**10Y US Treasury Yield:** 4.49% (CNBC/TradingEconomics, market close Fri 12 Jun 2026 — most recent available; markets closed Sun 14 Jun)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket) — **not reached**, see below
**Current DASH portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md)), no existing watchlist entry (first evaluation)
**Sector:** On-demand delivery platform — food delivery (DoorDash core marketplace), Wolt (international), retail/grocery delivery (DashMart, "New Verticals")

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$150.58** | WebSearch: "DASH DoorDash stock closing price June 12 2026" — most recent trading day (Fri 12 Jun 2026 close), per macrotrends/stockanalysis-derived aggregator history |
| Cross-check 1 | $154.28 (as of search date, intraday/recent) | WebSearch: "DASH stock price today DoorDash" — same query also reported a 2026-06-11 trading range of $146.11–$154.80 |
| Cross-check 2 | $155.64 (as of 9 Jun 2026) | WebSearch: "DoorDash DASH stock quote 52 week range analyst price target" |
| 52-week range | $143.30 – $285.50 | WebSearch (both queries, consistent) |
| Analyst consensus PT | ~$245.99 average (44–45 analysts, "Buy"); range $172–$350 | WebSearch — consistent across both queries |

⚠️ **IBKR price-snapshot/contract-search MCP tools** (`get_price_snapshot` / `search_contracts`) were not attempted in this session per the batch note — returned "permission denied" for prior agents in this batch.

**Context:** All three WebSearch price readings ($150.58, $154.28, $155.64) cluster tightly within $146–$156 and sit comfortably within the 52-week range ($143.30–$285.50) — internally consistent. $150.58 (most recent close, Fri 12 Jun 2026) is used as the Rule 0 price. This is **~47% below the 52-week high** ($285.50) and only **~5% above the 52-week low** ($143.30) — DASH is trading near the bottom of its 52-week range, and **~39% below the analyst consensus PT** (~$245.99).

---

## 2. Phase 01 — Quality Gate Data (Primary Sources)

Per the task brief, **net margin >15%** is the binding threshold (per `strategy.md`/`operating-brief.md`/`operating-calendar.md`'s New Position template) — the ">12%" figure in `valuation-scoring.md`'s Quantitative Pre-Screen Filters table is an older figure used only in the EODHD-screener mapping and is not the binding number for this evaluation.

### Revenue (FY2022–FY2025, GAAP, from 8-K annual/quarterly press releases via SEC EDGAR)

| Fiscal Year | Revenue | YoY Growth |
|---|---|---|
| FY2022 | $6.583B | — |
| FY2023 | $8.635B | +31.2% |
| FY2024 | $10.722B | +24.2% |
| FY2025 | $13.717B | +27.9% |

**Revenue CAGR 3yr (FY2022 → FY2025):**
```
CAGR = (13.717 / 6.583)^(1/3) − 1
     = (2.0833)^(0.3333) − 1
     = 1.2767 − 1
     ≈ +27.7%
```

### Net Income / Net Margin (GAAP, from FY2025 10-K / 8-K and quarterly press releases)

| Metric | Value | Derivation |
|---|---|---|
| FY2025 GAAP net income (attributable to common stockholders) | $935M | DoorDash FY2025 8-K / 10-K |
| FY2025 net margin | **6.81%** | $935M ÷ $13,717M |
| TTM revenue (per stockanalysis.com) | $14.72B | stockanalysis.com TTM |
| TTM net income (per stockanalysis.com) | $926M | stockanalysis.com TTM |
| TTM net margin (per stockanalysis.com) | **6.29%** | $926M ÷ $14.72B |
| Net margin as of Q2 2025 (per macrotrends) | **6.57%** | macrotrends "net profit margin as of June 30, 2025" |
| FY2024 GAAP net income | $123M | for context — FY2025 ($935M) represents a large YoY jump but still only ~6.8% margin |

⚠️ **Cross-checked across 3 independent sources/periods (FY2025 full year: 6.81%; TTM per stockanalysis: 6.29%; mid-2025 per macrotrends: 6.57%)** — all cluster in the **6.3%–6.8%** range, all **less than half** the 15% threshold. Note: a separately-reported "0.9% net income margin of Marketplace GOV" and "13.4% Net Revenue Margin" are DoorDash's own non-standard internal metrics (margin against GOV, and a "net revenue" sub-line respectively) — **not used here**; the framework's net margin = Net Income ÷ Total Revenue, computed directly from GAAP figures above.

### ROIC

| Source | Value | Period |
|---|---|---|
| stockanalysis.com | 11.05% | TTM |
| GuruFocus | 4.54% | As of Dec 2025 |
| GuruFocus | 5.58% | As of Mar 2026 (more recent) |

All readings are **below the >15% threshold**; the most recent (5.58%) is the furthest below.

### Gross Margin (GAAP, multi-year trend)

| FY | Gross Margin | Trend |
|---|---|---|
| FY2023 | 48.2% | +2.9pp |
| FY2024 | 49.4% | +2.5pp |
| FY2025 | 51.8% | +4.9pp (accelerating) |

✅ Comfortably above 40% and structurally expanding for 3 consecutive years.

### FCF Positive 3 Consecutive Years

| Period | Operating Cash Flow | Free Cash Flow |
|---|---|---|
| TTM through Q3 2023 | $1.2B | $878M |
| FY2024 (full year) | $2.1B | $1.8B |
| FY2025 (Q1–Q3 sum) | $635M + $504M + $871M = $2.01B | $494M + $355M + $723M = $1.572B (9-month) |

✅ All periods checked show positive FCF — appears to satisfy "FCF positive 3+ years," though full FY2023 and full FY2025 figures were derived from TTM/9-month windows rather than a single clean full-year-to-full-year table (flagged for completeness, does not affect the gate outcome given the dominant failures below).

### Net Debt / EBITDA

| Metric | Value | Source |
|---|---|---|
| Cash & equivalents | $5.53B | financecharts/aggregator |
| Total debt | $3.29B | financecharts/aggregator |
| Net cash position | **+$2.25B** (net cash, not net debt) | Computed: $5.53B − $3.29B |

✅ DASH carries a **net cash** position — Net Debt/EBITDA is effectively negative/not meaningful, comfortably under the <2x threshold (and under the <2.5x pre-screen and <4x asset-light alternative).

### Share Issuance Pattern

| Period | Weighted-avg diluted shares |
|---|---|
| Q3 2024 | ~399M |
| Q4 2024 | ~405M |
| Q1 2025 | ~410M |
| Q2 2025 | ~428M |
| Q3 2025 | ~433–442M (sources vary slightly) |

A buyback program was active Jan–Apr 2025 (~$89M repurchased) but was **suspended** in April 2025. Despite the buyback, diluted share count grew from ~399M to ~433–442M (Q3 2024 → Q3 2025), an increase of roughly **8.5–10.8% in one year** — driven by stock-based compensation and equity issuances outpacing the (small, since-suspended) buyback. ⚠️ This is a **dilutive share issuance pattern** by the framework's definition, a secondary (non-binding-here) concern.

### Data Gaps / Flags Summary

1. FY2023 and FY2025 full-year FCF figures were assembled from TTM/9-month windows rather than single clean full-year tables — flagged but immaterial to the gate outcome (FCF-positive check would pass regardless).
2. ROIC has a wide range across sources (4.54%–11.05%) depending on period and methodology — all readings nonetheless fall below the 15% threshold.
3. No metric was invented or estimated. All figures trace to DoorDash 8-K/10-K filings (SEC EDGAR via WebSearch) or named aggregators (stockanalysis.com, macrotrends, GuruFocus, financecharts), with derivations shown explicitly.
4. PEG, EV/EBIT, Forward PE, 10yr avg PE, and other Phase 02 inputs were **not gathered** — Phase 01 fails decisively, so Phase 02 scoring is not run (see below).

---

## 3. Phase 01 — Quality Gate: Walk-Through

| # | Check | DASH Value | Threshold | Result |
|---|---|---|---|---|
| 1 | **Net margin** | FY2025: 6.81% ($935M / $13,717M); TTM: 6.29% (stockanalysis); 6.57% (macrotrends, mid-2025) | **>15%** | ❌ **FAIL** — less than half the required threshold across all 3 readings |
| 2 | **ROIC** | 11.05% (TTM, stockanalysis) / 4.54% (Dec 2025, GuruFocus) / 5.58% (Mar 2026, GuruFocus) | **>15%** | ❌ **FAIL** — all readings below threshold |
| 3 | Revenue CAGR 3yr | +27.7% (FY2022→FY2025) | >10% | ✅ PASS — clears by >2.5x |
| 4 | Gross margin | 51.8% (FY2025), expanding 48.2%→49.4%→51.8% over 3yrs | >40% or expanding | ✅ PASS |
| 5 | FCF positive 3+ years | Positive in every period checked (TTM 2023, FY2024, 9M-2025) | required | ✅ PASS |
| 6 | Net debt/EBITDA | Net **cash** position of +$2.25B (cash $5.53B vs debt $3.29B) | <2x | ✅ PASS |
| 7 | FCF/NI conversion ratio | Not computed — gate already failed on #1/#2 | >70% for 2yrs | — not evaluated |
| 8 | Share issuance pattern | Diluted shares +8.5–10.8% YoY (Q3'24→Q3'25) despite a since-suspended buyback | not dilutive | ❌ FAIL (secondary) |

**Gate result: FAIL.** Two criteria fail outright — **net margin** (6.3–6.8% vs. >15% required, i.e. **less than half** the threshold across three independent readings/periods) and **ROIC** (4.5–11.1% vs. >15% required, every reading below). A third (share issuance pattern) also fails on a secondary basis. Per the operating brief's non-negotiables and this session's explicit instruction, **STOP HERE — do not proceed to the Rate Environment Gate or Phase 02 scoring.**

---

## 4. Why DASH Fails (Qualitative Context)

DoorDash only became GAAP-profitable on a full-year basis in FY2024 (a modest $123M, ~1.1% margin) and FY2025 ($935M, ~6.8% margin) — a dramatic and genuinely positive inflection from years of GAAP losses, and the trajectory (margin roughly 6x'd year-over-year) is the kind of thing this framework's Phase 04 "Quality Watch" would want to track closely. But:

- **Net margin (6.3–6.8%) is still less than half the >15% bar** this framework requires for *any* business, food-delivery platform or otherwise. The framework draws no sector exception for delivery platforms — the bar is a flat >15% across the Qualified Quality List.
- **ROIC (4.5–11.1%)** likewise sits below the 15% threshold across every source checked, including the most recent (Mar 2026, 5.58%) — suggesting the gap is not closing quickly.
- Revenue growth (+27.7% 3yr CAGR), gross margin (51.8%, expanding), and balance sheet (net cash) are all genuinely strong and Quality-List-caliber on their own. This is a company with real operating leverage emerging — but the bottom-line conversion (net margin, ROIC) has not yet crossed the line this framework requires before a name enters the scored universe.

This is exactly the "popular growth stock with a real fundamental gap" case the task brief flagged — and per the framework's non-negotiables ("never invent or estimate financial data," "act only on documented triggers"), the honest call is **FAIL, not scored**, regardless of DASH's market profile or recent share-price weakness (down ~47% from its 52-week high, which on its own is *not* a valid trigger per Phase 06's "price dropped on intact thesis" exclusion — and is doubly not relevant when the thesis hasn't even cleared Phase 01).

---

## 5. Recommendation

# **PASS — Phase 01 FAIL. Not scored. Add to watchlist for future re-check.**

DASH does not enter the Qualified Quality List at this time. No Rate Environment Gate, no Phase 02 valuation score, and no order setup are produced — per the operating brief, Phase 02 only runs for names that have cleared Phase 01.

**What would change this:** DoorDash's net margin trajectory (1.1% FY2024 → 6.8% FY2025) shows real operating leverage. If margin expansion continues at a similar pace for another 1-2 fiscal years (and ROIC follows), DASH could plausibly clear the >15% net margin bar within 2-3 years — worth re-checking at each annual report, not necessarily every quarter, since this is a structural/multi-year trend rather than a single-quarter event.

---

## 6. Next Review Trigger

**Date/event:** DoorDash's **FY2026 annual results** (expected ~February 2027) — re-run Phase 01 with refreshed FY2026 net margin and ROIC. The FY2024→FY2025 net margin trajectory (1.1% → 6.8%) is the key trend to watch; if FY2026 continues compounding toward the mid-teens, DASH would be a strong candidate to clear Phase 01 within the following 1-2 years.

Earlier trigger if:
- A quarterly print shows net margin materially accelerating beyond the current trajectory (Rule 9 — guidance revision / earnings beat with a step-change in margin).
- Any M&A, management change, or macro shift per Rule 9.

**No position opened — nothing to log in `decisions/`.**

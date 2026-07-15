# NEW POSITION (Re-evaluation) — ASML (ASML Holding N.V.) — 2026-07-15

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 15 Jul 2026
**10Y US Treasury Yield:** 4.62% (FRED `DGS10`, most recent posted value as of this session, dated 2026-07-13, updated 2026-07-14 — normal FRED reporting lag; cross-checked against TradingEconomics' same-day "~4.62%, near two-month highs" commentary)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current ASML portfolio weight:** 0% — not held (unchanged; not touching `holdings.md`)
**Prior coverage:** [watchlist/not-in-portfolio/ASML/ASML-2026-07-12.md](../watchlist/not-in-portfolio/ASML/ASML-2026-07-12.md) — Quality Score 81.5, Valuation Score 100.0, Composite Score 59.3, WATCHLIST ONLY, live price then $1,797.32. That entry's documented "Next review trigger" was explicitly "Q2 2026 earnings" — this session exists because that trigger has now fired.
**Sector:** Technology / Semiconductor capital equipment — sole global manufacturer of EUV lithography systems (see the 2026-07-12 session and glossary for background; unchanged this session).

---

## 0. Why this session exists — trigger source

A Telegram post (**tarasguk channel, post #11386, 2026-07-15 05:29:54 UTC**) claimed ASML reported Q2 2026 results: EPS €7.59 vs €6.88 est, revenue €9.33B vs €8.87B est, gross margin 54.0% vs 51.9% est, Q3 2026 guidance €11–12B vs €10.34B est consensus, FY2026 guidance €43–45B vs €39.34B est consensus. Per the operating brief, **this post text is a trigger only, never treated as financial data** — independently verified below against ASML's own investor-relations materials and SEC channels before any of it was used.

**Independent verification performed:**
- ASML's own investor-relations site (`asml.com/en/news/press-releases` and `asml.com/en/investors/financial-results/q2-2026`) confirms a Q2 2026 earnings release dated 2026-07-15.
- The official press release, distributed via GlobeNewswire ("ASML reports €9.3 billion total net sales and €2.9 billion net income in Q2 2026," 2026-07-15), plus ASML's own **Excel and PDF "Financial statements US GAAP Q2 2026"** files (published same-day on ASML's investor-relations brand portal, `ourbrand.asml.com`) were pulled directly and parsed in full (see §2).
- **SEC EDGAR flag:** as of this session, ASML's Q2 2026 Form 6-K had **not yet appeared** in SEC EDGAR's submissions index or full-text search (most recent indexed 6-K remained the 2026-04-23 AGM-disclosure filing; the 2026-04-15 accession is the *Q1* 2026 quarterly filing, not Q2 — confirmed by fetching it directly and finding Q1, not Q2, figures). This is a **filing-timing/indexing lag**, not a data-availability gap: ASML's own investor-relations portal already carries the same unaudited US GAAP statements that will shortly be furnished to the SEC as the 6-K's Exhibit 99.3 (identical in content and format to the Q1 2026 and Q2 2025 6-K exhibits already on file). Used ASML's own primary-source IR-portal documents in place of the not-yet-indexed SEC copy, flagged explicitly rather than silently substituted.
- **Result: the Telegram post's figures check out.** Reported EPS €7.59 (exact match), net sales €9,326.5M ≈ €9.33B (exact match), gross margin 54.0% (exact match), Q3 2026 guidance €11.0–12.0B (exact match), FY2026 guidance €43–45B (exact match). The "est." figures in the post are broadly consistent with pre-earnings guidance/consensus levels found independently (ASML's own April guidance for Q2 was €8.4–9.0B/51–52% GM, and Yahoo Finance's Q3 2026 consensus revenue estimate — pulled fresh this session — was €10.62B, below the new €11–12B guide) but were **not used for scoring**; only the confirmed reported/guided figures below feed this session's numbers.

---

## 1. Live Price (Rule 0)

Per the task brief, the live price was already fetched via IBKR and is used as-is (not re-fetched this session, to avoid an inconsistent mid-session price change):

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$1,869.22** | IBKR `get_price_snapshot`, contract_id 117902840 (NASDAQ NY Registry Share), fetched 2026-07-15 (epoch ts 1784102786) |
| Change on day | +$93.58 (+5.27%) | Same snapshot — a large, fundamentally-explained move (the Q2 beat + guidance raise reported hours earlier), consistent with Rule 9's "not valid: price moved on intact thesis" carve-out not applying here since there *is* a same-day fundamental trigger |
| Bid / Ask | $1,868.17 / $1,869.49 | Same snapshot |
| Live EUR/USD FX rate | **1.14225** (1 EUR = $1.14225) | IBKR `get_price_snapshot`, EUR/USD contract_id 12087792 (mid of bid 1.1422 / ask 1.14225), fetched this session — used throughout for EUR→USD conversions below |

⚠️ Cross-check note: Yahoo Finance's own cached `price` module (pulled this session via the documented direct-`quoteSummary` workaround, §2.6) still showed a stale regular-market price (~$1,775) and a stale `sharesOutstanding` (385,417,665, matching the pre-buyback FY2025 20-F figure) — Yahoo's snapshot fields had not yet refreshed for today's earnings-driven rally at query time. IBKR's live snapshot (used above) and ASML's own freshly-parsed Q2 2026 share count (§2.3) are used in preference to Yahoo's stale fields throughout.

---

## 2. Data Gathered

### 2.1 Source note

Same foreign-private-issuer sourcing structure as the 2026-07-12 session (Form 20-F annual / Form 6-K interim), with one change: this session pulled ASML's **own investor-relations-published Q2 2026 financial statements directly** (both the PDF and, critically, the machine-readable **Excel workbook** ASML publishes alongside it — `Financial-statements-US-GAAP-Q2-2026-excel.xlsx`, at `ourbrand.asml.com`), rather than relying solely on SEC EDGAR, because the formal Q2 2026 6-K had not yet posted to EDGAR at session time (§0). This Excel file carries the same "Quarterly Summary US GAAP" tables (5 trailing quarters: Jun'25, Sep'25, Dec'25, Mar'26, Jun'26) as the 6-K exhibits used in the 2026-07-12 session, letting this session compute a precise, non-estimated TTM window through Q2 2026 — a **data-quality improvement** over the prior session (which had to reconstruct TTM via `FY2025 − Q1'25 + Q1'26` since quarterly 6-Ks aren't XBRL-tagged). The Q2 2025 6-K (filed 2025-07-16, SEC EDGAR) was pulled directly for the same table as a cross-check; the two sources agree exactly on every overlapping quarter (Q2 2025, Q3 2025).

### 2.2 TTM reconstruction (Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026, EUR millions)

Source: ASML's own "Quarterly Summary US GAAP Consolidated Statements of Operations / Cash Flows / Balance Sheets" (Q2 2026 Excel workbook, `ourbrand.asml.com`, 2026-07-15), cross-checked against the SEC-filed Q2 2025 6-K exhibit for the overlapping Q2/Q3 2025 columns — exact match.

```
                          Q3 2025    Q4 2025    Q1 2026    Q2 2026    TTM (Q3'25–Q2'26)
Total net sales            7,516.0    9,718.1    8,766.9    9,326.5     35,327.5
Gross profit                3,880.3    5,068.6    4,645.0    5,035.4     18,629.3
R&D costs                   1,108.7    1,262.3    1,184.9    1,276.6      4,832.5
SG&A costs                    303.2      375.2      302.3      302.7      1,283.4
Income from operations      2,468.4    3,431.1    3,157.8    3,456.1     12,513.4
Income tax expense            442.2      618.7      546.6      609.6      2,217.1
Net income                  2,124.5    2,839.6    2,756.7    2,917.6     10,638.4
D&A                           274.6      255.2      259.4      246.9      1,036.1
Operating cash flow           559.1   11,410.3   (2,185.6)    1,703.0     11,486.8
CapEx (PP&E purchases)         295.9      447.9      402.4      299.4      1,445.6
```

```
Gross Margin TTM  = 18,629.3 / 35,327.5 = 52.73%
Net Margin TTM    = 10,638.4 / 35,327.5 = 30.11%
EBITDA TTM        = 12,513.4 + 1,036.1  = 13,549.5
FCF TTM           = 11,486.8 − 1,445.6  = 10,041.2
FCF/NI TTM        = 10,041.2 / 10,638.4 = 94.39%
Effective tax rate TTM = 2,217.1 / (10,638.4 + 2,217.1) = 17.25%
```

Note the OCF swing: Q1 2026's −€2,185.6M operating cash flow (a large negative working-capital swing, already flagged in the 2026-07-12 session) drags TTM FCF (€10,041.2M) *below* full-year FY2025's actual FCF (€11,084.9M, per the 2026-07-12 session) even though revenue and net income both grew — a timing/working-capital effect, not a deterioration in underlying cash generation (Q2 2026 alone posted a strong €1,703.0M positive OCF). **FY2025 actual FCF (€11,084.9M) is retained as the DCF base year** (§5.3), consistent with the 2026-07-12 session's methodology, specifically because it is a full, clean fiscal year unaffected by this single-quarter working-capital swing.

### 2.3 Balance sheet (as of 28 Jun 2026, freshest)

Source: same Q2 2026 Excel workbook, "Quarterly Summary US GAAP Consolidated Balance Sheets" tab.

```
Cash and cash equivalents       6,671.9
Short-term investments            909.6
  Cash + ST investments         7,581.5
Long-term debt                  1,984.4   (only long-term-debt line disclosed at this level of detail — same
                                            abbreviated-disclosure caveat as the 2026-07-12 session; current-
                                            portion-of-LT-debt is not broken out separately in this dataset)
Total shareholders' equity     21,825.4
Total assets                   50,214.8

Net Debt = 1,984.4 − 7,581.5 = −5,597.1 (net cash)
Net Debt/EBITDA = −5,597.1 / 13,549.5 = −0.413×
```

Weighted-average **basic shares outstanding, Q2 2026: 384.5 million** (diluted: 384.9M) — per the same Excel workbook. ⚠️ **Flagged approximation:** ASML's abbreviated quarterly release doesn't disclose an exact period-end share count (only the quarter's weighted average); 384.5M (basic) is used as the closest available proxy for market-cap purposes throughout this session, in place of Yahoo's stale, pre-buyback 385,417,665 figure (§1). The ~0.9M-share (0.24%) difference is immaterial to every downstream conclusion.

### 2.4 Invested Capital / ROIC / NOPAT

```
NOPAT = EBIT_TTM × (1 − 17.25%) = 12,513.4 × 0.8275 = 10,355.3M EUR
Invested Capital = Total Debt + Equity − Cash = 1,984.4 + 21,825.4 − 7,581.5 = 16,228.3M EUR
ROIC = 10,355.3 / 16,228.3 = 63.81%
```

Consistent with the 2026-07-12 session's ~64% reading (same dynamic: a small invested-capital base relative to earnings power, net cash funded partly by customer prepayments against backlog).

### 2.5 Market Cap / EV / multiples — currency handling

Same EUR-financials / USD-price handling as the 2026-07-12 session, converted at this session's live 1.14225 rate.

```
Market Cap (USD) = $1,869.22 × 384.5M shares = $718,715.1M

Total Debt (USD)  = €1,984.4M × 1.14225 = $2,266.4M
Cash (USD)        = €7,581.5M × 1.14225 = $8,658.6M
EV = 718,715.1 + 2,266.4 − 8,658.6 = $712,322.9M

EBIT_TTM (USD)  = €12,513.4M × 1.14225 = $14,293.4M
FCF_TTM (USD)   = €10,041.2M × 1.14225 = $11,469.6M

EV/EBIT (TTM)   = 712,322.9 / 14,293.4 = 49.84×
FCF Yield (TTM) = 11,469.6 / 718,715.1 = 1.596%
```

### 2.6 Consensus / forward estimates — a flagged data-quality issue and its resolution

Pulled fresh this session via the documented `quoteSummary` direct-endpoint workaround (yfinance's bundled `curl_cffi` client again failed with a proxy TLS reset, same recurring issue as prior sessions).

**Problem found:** Yahoo's `earningsTrend` "0y" row (full fiscal-year 2026, the row this framework's convention normally uses for Forward PE) showed EPS €31.81 backed by only **1 analyst** — barely above the *pre-earnings* consensus of $31.948 used in the 2026-07-12 session, despite today's large guidance raise. This is inconsistent with the raised outlook and reads as **stale/not-yet-refreshed** (Yahoo's annual-consensus aggregation had not caught up with today's earnings within the session window), not a genuine analyst view.

**Resolution — bottom-up FY2026E EPS, disclosed as a methodology deviation for this session only:**

```
H1 2026 actual EPS (reported)        = €7.15 (Q1) + €7.59 (Q2)         = €14.74
Q3 2026 consensus EPS (0q row, n=15) = €8.5217
Q4 2026 consensus EPS (+1q row, n=14)= €9.7402
FY2026E EPS (bottom-up)              = 14.74 + 8.5217 + 9.7402         = €33.00
FY2026E EPS (USD)                    = 33.00 × 1.14225                  = $37.70
```

This blends **actual, already-reported** H1 2026 results with Yahoo's quarterly (not annual) consensus rows, which carry a full, plausible analyst count (15 and 14 respectively) and are consistent with the fresh guidance. Flagged explicitly as a deviation from the framework's normal "read the 0y row" convention, justified by a specific, disclosed data-quality problem rather than an unexplained substitution.

```
Forward PE = $1,869.22 / $37.70 = 49.59×
```

Sell-side context (Yahoo `financialData`, same caveat about possible partial staleness): mean target $1,902.31, median $2,004.34, "strong_buy" (15 analysts) — discussed qualitatively only, never scored.

### 2.7 5-year historical PE range — unchanged

Same annual-snapshot method as the 2026-07-12 session (FY2026 isn't complete, so no new fiscal-year data point exists to add): **5yr Low 34.25× (FY2023), High 49.28× (FY2021), Avg 38.33×.**

### 2.8 TTM basic EPS (for multiples-based fair value, §5.3)

```
TTM basic EPS = Q3'25 €5.49 + Q4'25 €7.35 + Q1'26 €7.15 + Q2'26 €7.59 = €27.58
```

### 2.9 Growth / TAM evidence — updated, all company-sourced this session

From ASML's own Q2 2026 press release (`Press-Release-Financial-Results-Q2-2026.pdf`, parsed in full):
- **FY2026 guidance raised** to €43–45B net sales / 54–56% gross margin (from €36–40B / 51–53% guided in April 2026) — a guidance increase of roughly 17–19% at the midpoint.
- **Q3 2026 guidance**: €11.0–12.0B net sales, 55–57% gross margin — above Yahoo's own pre-refresh Q3 revenue consensus of €10.62B (§2.6).
- CEO Christophe Fouquet, verbatim: *"Our order intake remained extremely strong in the first half of the year."*
- Capacity expansion: ASML plans to add **30% to its 2026 low-NA EUV capacity (~65 systems/yr) for 2027**, "investigating" a further 30% for 2028; plans to add **30% to its 2026 DUV immersion capacity (~130 systems/yr) for 2027**, also investigating a further 30% for 2028.
- High-NA EUV: Intel has begun using the tool in production (per Investing.com's Q2 2026 earnings-call transcript) — reinforces, rather than newly establishes, the Brand-premium/pricing-power Moat Signal already credited in the 2026-07-12 session.

Per this framework's explicit design (`valuation-scoring.md`, "Why Forward Guidance Is Not a Sub-score"), **none of this guidance is scored directly** — it feeds only the Growth sub-score's qualitative TAM modifier (already at its +10 cap, unchanged in magnitude, re-substantiated with fresher evidence below) and is logged as Rule 9 trigger context, not as an invented future data point.

### 2.10 Data gaps flagged this session (disclosed, not invented around)

1. SEC 6-K for Q2 2026 not yet indexed on EDGAR at session time — used ASML's own IR-portal-published statements instead (§0, §2.1).
2. Yahoo's annual FY2026E consensus EPS row showed only 1 analyst and read as stale — used a bottom-up actual-H1 + consensus-H2 blend instead (§2.6).
3. Exact period-end share count not disclosed in this abbreviated release — used Q2 2026 weighted-average basic shares as proxy (§2.3).
4. Owner Earnings maintenance-vs-growth CapEx split still unavailable — ASML is not one of the four mandated names (MSFT/GOOGL/META/AMZN); standard FCF used throughout, same as 2026-07-12.
5. 5yr historical PE range still built from 5 annual snapshots rather than ~20 quarterly points (ASML's 6-Ks aren't XBRL-tagged) — unchanged limitation, still directionally unambiguous (§2.7).

None of these blocked scoring; all are the same category of transparently-flagged approximation this framework has used in prior ASML and other foreign-private-issuer sessions.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology, unchanged version)

### 3.1 Legacy 8-criterion table (context only)

| Check | TTM Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 52.73% | >40% | ✅ PASS |
| Net margin | 30.11% | >12% | ✅ PASS |
| ROIC | 63.81% | >15% | ✅ PASS |
| Revenue growth (3yr CAGR, FY-anchored, unchanged) | 15.55% | >8% | ✅ PASS |
| FCF positive 3 consecutive years | FY2023–2025 all positive (unchanged) | required | ✅ PASS |
| Net debt/EBITDA | −0.413× (net cash) | <2.5× | ✅ PASS |
| FCF yield | 1.596% | >4% | ❌ **FAIL** |
| EV/EBIT | 49.84× | <20× | ❌ **FAIL** |

Same 6-of-8 pattern as the 2026-07-12 session — the two failures remain purely **valuation** metrics, both of which actually *improved slightly* this quarter (FCF yield 1.48%→1.596%, EV/EBIT 51.22×→49.84×) even as the price rose, because TTM EBIT/FCF grew faster than the price did.

### 3.2 Hard disqualifier check

- **FCF/NI conversion <70% for 2+ consecutive years:** only FY2023 (41.9%) falls below 70%, a single isolated year (unchanged from 2026-07-12; TTM FCF/NI is now 94.39%, comfortably above). **Does not fire.**
- **Net Debt/EBITDA over threshold:** −0.413× (net cash), far under 2.5×. **Does not fire.**
- **Not FCF-positive 3+ consecutive years:** FY2021–FY2025 and TTM all positive. **Does not fire.**

**No hard disqualifier fires.**

### 3.3 Quality Score — full computation

```
Profitability (25%):
  NetMargin_Component = clamp(30.11/30 × 100) = 100.00 (capped — net margin now exceeds the 30% ceiling)
  ROIC_Component       = clamp(63.81/30 × 100) = 100.00 (capped)
  Profitability_Score  = (100.00 + 100.00) / 2 = 100.00
  (no FCF-positivity cap — FCF-positive every year shown)

Margins (15%):
  GrossMargin_Score = clamp(52.73/80 × 100) = 65.92
  (no structural-trend bonus — already far above the 40% bonus-eligibility ceiling, same as 2026-07-12)
  Margins_Score = 65.92

Growth (20%):
  Growth_Score raw = clamp(15.55/25 × 100) = 62.20   (3yr FY-anchored CAGR unchanged — FY2026 not yet
    complete, so the framework's fiscal-year-anchored formula has no new data point to add this quarter;
    per valuation-scoring.md's own design, guidance is a Rule 9 trigger/qualitative input, not a scored
    growth-rate substitute)
  TAM/pricing-power modifier: +10 RE-SUBSTANTIATED (already at cap; fresh Q2 2026 evidence, all company-
    sourced — see §2.9): FY2026 guidance raised to €43–45B (from €36–40B), Q3 2026 guidance €11–12B above
    trailing consensus, CEO-confirmed "extremely strong" H1 order intake, and a disclosed +30%/+30%
    (2027/2028) low-NA EUV and DUV-immersion capacity expansion plan.
  Growth_Score = 62.20 + 10 = 72.20

Balance Sheet (15%):
  BalanceSheet_Score = clamp(100 × (1 − (−0.413)/4)) = clamp(110.33) = 100.00 (capped, net cash)

Moat Signal (15%) — unchanged from 2026-07-12 (same 3-of-5 checklist; no new signal newly credited this
  session, though Brand premium/pricing power is further reinforced by High-NA EUV entering production use
  at Intel):
  Market share stable/growing: TRUE (unchanged — ~100% EUV share, sole manufacturer)
  Brand premium / pricing power: TRUE (unchanged; reinforced by High-NA-in-production evidence)
  Network effect: NOT marked true (unchanged — not applicable to this business model)
  Switching costs: TRUE (unchanged — no alternative EUV supplier, multi-year qualification lock-in)
  Scale cost advantage: NOT marked true (unchanged — no citable cost-per-unit comp exists)
  Moat_Score = (3/5) × 100 = 60.00

FCF Quality (10%):
  FCFQuality_Score = clamp(((0.9439 − 0.40)/0.60) × 100) = 90.64

Quality Score = 100.00×0.25 + 65.92×0.15 + 72.20×0.20 + 100.00×0.15 + 60.00×0.15 + 90.64×0.10
              = 25.000 + 9.888 + 14.440 + 15.000 + 9.000 + 9.064
              = 82.392  →  rounds to 82.4
```

**Quality Score = 82.4 / 100.0 — clears the 80.0 gate, up from 81.5 on 2026-07-12.** The improvement is driven almost entirely by **Profitability hitting the 100.0 ceiling** (TTM net margin crossed above the 30% cap this quarter, on the back of Q2's 54.0% gross margin and strong operating leverage) — Margins, Growth, Balance Sheet, and Moat are essentially unchanged from the prior session; FCF Quality also improved modestly (90.64 vs 82.68) since the depressed Q1 2026 quarter has partly rolled out of the TTM window.

⚠️ Same open flag as 2026-07-12: Hybrid Upgrade 1 (Owner Earnings) not applied — ASML doesn't disclose a maintenance-vs-growth CapEx split and isn't one of the four mandated names. Standard FCF used throughout.

---

## 4. Rate Environment Gate

```
Step 1 — Earnings Yield Spread Test:
  Forward PE (bottom-up FY2026E, §2.6) = $1,869.22 / $37.70 = 49.59×
  EY = 1 / 49.59 = 2.017%
  Spread = EY − 10Y (4.62%) = 2.017% − 4.62% = −2.603pp
  Spread < +1.5% → Step 1 FAILS → additive +5

Step 2 — Rate Regime Modifier:
  10Y = 4.62% → within the 3.5–5% bracket → +5

Combined Rate Environment Gate contribution = +5 + 5 = +10   (unchanged from 2026-07-12)
```

---

## 5. Phase 02 — Valuation Score

### 5.1 PEG applicability — unchanged

Same lumpy/cyclical diluted-EPS history as 2026-07-12 (two of the last four fiscal years were EPS *declines*) — ASML still does not qualify as a Fast Grower. **PEG not applicable; its 15% weight stays redistributed to EV/EBIT (40%).**

### 5.2 Sub-scores

```
FCF Yield (40%):
  FCF_Score = clamp(100 × (1 − 1.596/10)) = 84.04

EV/EBIT (40%, redistributed):
  EV/EBIT_Score = clamp((49.84 − 12)/23 × 100) = clamp(164.5) = 100.00 (capped)

Forward PE (20%):
  Primary formula: FwdPE_Score = clamp((49.59 − 34.25)/(49.28 − 34.25) × 100) = clamp(102.0) = 100.00 (capped)
  Historical PE Modifier vs. 5yr avg 38.33×: Forward PE 49.59× is +29.4% above avg → >20% above → +10
    (already at ceiling; no net effect since FwdPE_Score is already capped at 100)

Raw weighted score = 84.04×0.40 + 100.00×0.40 + 100.00×0.20
                   = 33.62 + 40.00 + 20.00
                   = 93.62
```

Slightly lower than the 2026-07-12 session's raw weighted score (94.08) — FCF yield improved marginally (cheaper) this quarter even as EV/EBIT and Forward PE both remain pinned at their 100.0 ceilings.

### 5.3 Fair Value work (feeds the Upside/Downside Modifier)

**Method A — 3-scenario DCF.** Same structure as 2026-07-12 (CAPM-derived WACC, base-year FCF = FY2025 actual €11,084.9M, Stage 1 = 2026–2030, Gordon-growth terminal), refreshed for the higher 10Y (4.62%) and modestly higher Stage-1 growth assumptions reflecting the confirmed guidance raise and capacity-expansion plans (§2.9) — a disclosed, judgment-based increase from the 2026-07-12 session's 18%/10%/3% (bull/base/bear), not a mechanical formula:

```
Cost of equity (CAPM) = 4.62% + 1.394 × 5.5% = 12.29% (base WACC; negligible net debt)
```

| Scenario | WACC | Terminal g | Stage-1 FCF growth/yr | DCF EV (EUR) | + Net cash | Equity value/share (EUR) | (USD @1.14225) |
|---|---|---|---|---|---|---|---|
| Bull | 11.3% | 3.0% | 22% (raised from 18%: aligned with a faster path to the 2030 €60B high end, given the confirmed guidance beat) | €291.3B | +€5.60B | €772.14 | **$881.97** |
| Base | 12.3% | 2.5% | 12% (raised from 10%: reflects the confirmed FY2026 guidance raise, decelerating after this year's step-up) | €169.4B | +€5.60B | €455.08 | **$519.81** |
| Bear | 13.3% | 2.0% | 4% (raised from 3%: strong bookings/backlog momentum modestly reduces near-term cyclical-pause risk) | €108.4B | +€5.60B | €296.44 | **$338.61** |

**Method B — Comparable multiples** (using TTM basic EPS €27.58, §2.8, and the updated EV/EBIT USD figures from §2.5):

```
Historical PE (trailing) = 38.33 × €27.58 → USD                        = $1,207.52
Historical PE (forward)  = 38.33 × €33.00 (bottom-up FY2026E) → USD    = $1,444.90
EV/EBIT @ 25× = (EBIT_USD×25 + net cash_USD)/shares                    = $945.98
EV/EBIT @ 30× = (EBIT_USD×30 + net cash_USD)/shares                    = $1,131.85
Base multiples value (avg of above 4)                                  = $1,182.56

Bull multiples: EV/EBIT @ 35× ($1,317.72) + Historical-PE-at-5yr-high 49.28×TTM-EPS ($1,552.48), avg = $1,435.10
Bear multiples: EV/EBIT @ 17.75× ($676.47) + Historical-PE-at-5yr-low 34.25×TTM-EPS ($1,078.99), avg = $877.73
```

**Triangulation (40% DCF / 60% Multiples):**

```
Bull blended FV = 0.40×881.97 + 0.60×1,435.10 = $1,213.85
Base blended FV = 0.40×519.81 + 0.60×1,182.56 = $917.46
Bear blended FV = 0.40×338.61 + 0.60×877.73   = $662.08

PW Fair Value = 0.25×1,213.85 + 0.50×917.46 + 0.25×662.08 = $927.71
```

⚠️ Same qualitative pattern as 2026-07-12: this session's bottom-up PW Fair Value ($927.71) — even its bull case ($1,213.85) — sits well below both the live price ($1,869.22) and the sell-side mean target ($1,902.31, §2.6). The gap has **narrowed** slightly from the prior session ($861.4 PW FV then) since the confirmed guidance raise pulled every scenario's cash-flow trajectory up, but the fundamental divergence between this framework's bottom-up build and prevailing market pricing remains large and is reported, not reconciled away.

### 5.4 Upside/Downside Modifier

```
Gap Upside% = (927.71 / 1,869.22) − 1 = −50.37%
Catalyst window: no specific 18–24mo re-rating catalyst identified (same as 2026-07-12); downside gap, so
  the upside-side guardrail cap doesn't apply here.
Annualized gap = −50.37% / 2 = −25.18%/yr

Intrinsic growth rate = diluted EPS 3yr CAGR (FY2022→FY2025, unchanged — FY2026 not yet complete) = +20.48%/yr

Shareholder yield (recomputed this session directly from TTM cash-flow-statement actuals, an improvement
  over the 2026-07-12 session's 3-year-share-count-reduction proxy):
  TTM dividends paid    = €619.6 (Q3'25) + €619.2 (Q4'25) + €617.0 (Q1'26) + €1,038.5 (Q2'26) = €2,894.3M
  TTM buybacks           = €172.2 + €1,700.0 + €1,000.0 + €1,077.5 = €3,949.7M
  TTM share-issuance proceeds (offset) = €35.3 + €32.7 + €35.0 + €36.7 = €139.7M
  Net buyback            = €3,949.7M − €139.7M = €3,810.0M
  Dividend yield  = (€2,894.3M × 1.14225) / $718,715.1M = 0.460%
  Net buyback yield = (€3,810.0M × 1.14225) / $718,715.1M = 0.605%
  Shareholder yield = 0.460% + 0.605% = 1.065%/yr

E = −25.18% + 20.48% + 1.065% = −3.64%/yr

E < 0 → M = 5 + 10 × clamp((−E)/10pp, 0, 1) = 5 + 10 × clamp(3.64/10, 0, 1) = 5 + 3.64 = +8.64
```

### 5.5 Final Valuation Score

```
Final Score = Raw weighted (93.62) + Rate Environment Gate (+10) + Upside/Downside Modifier (+8.64)
            = 112.26  →  clamp to 100.0 maximum
```

**Valuation Score = 100.0 / 100.0 — unchanged, still the maximum.** As with 2026-07-12, the raw weighted score plus the Rate Environment Gate alone (93.62 + 10 = 103.62) already exceeds 100 before the Upside/Downside Modifier is applied — the modifier would need to swing to roughly **−3.6 or more negative** (implying E ≥ ~13.6%/yr, far from this session's computed −3.64%) to pull the final score below 100.0 at all.

---

## 6. Composite Score (Quality + Valuation)

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 82.4) + 0.50 × 100.0
                = 0.50 × 17.6 + 50.0
                = 8.8 + 50.0
                = 58.8
```

**Composite Score = 58.8 — falls in the 50.0–69.9 band: HOLD — watch only, no new entry, no trim.** Modestly more attractive than the 2026-07-12 session's 59.3 (a 0.5-point improvement), driven entirely by the improved Quality Score (82.4 vs 81.5) — Valuation Score is unchanged at its 100.0 ceiling. The mechanism is working exactly as designed (same point made in the 2026-07-12 session): an already-strong quality profile got measurably stronger this quarter (profitability crossed the sub-score's ceiling), while the valuation axis stayed maximally rich even after a materially better quarter, because the price rose in step with (or ahead of) the fundamentals.

---

## 7. Order Setup

**Not applicable.** Composite Score 58.8 sits in the 50.0–69.9 "Watchlist only — no new entry, no trim" band, unchanged in category from 2026-07-12. No buy price, sell target, stop loss, or position size is computed this session. The PW Fair Value ($927.71) and its scenario range ($662.08 bear – $1,213.85 bull, §5.3) are recorded for reference and for the Upside/Downside Modifier, not as an actionable entry price.

---

## 8. Qualitative Notes

1. **The Telegram trigger's figures independently verified as accurate** (§0) — a useful confirmation that this particular channel's earnings-figure reporting was reliable this time, though per standing policy that doesn't change how future posts from it are treated (verify every time, trust none by default).
2. **This was a genuine beat-and-raise quarter, not a modest in-line print.** Q2 2026 sales and gross margin both beat ASML's own April guidance; FY2026 guidance was raised ~17–19% at the midpoint (€36–40B → €43–45B) in a single quarter — an unusually large upward guidance revision for a company of this size, and itself a Rule 9 trigger independent of the earnings release.
3. **Quality genuinely improved, crossing a sub-score ceiling.** TTM net margin (30.11%) now sits fractionally above the Profitability sub-score's 30% cap, pushing that component to its maximum (100.0) for the first time in this framework's coverage of ASML. This is the main driver of the Quality Score's 81.5→82.4 move; every other sub-score is flat or immaterially changed.
4. **Valuation richness persists despite a stronger quarter — and mildly eased on a pure-multiples basis.** FCF yield and EV/EBIT both improved slightly (cheaper) this quarter because TTM EBIT/FCF grew faster than the share price did intraday; Forward PE similarly declined slightly on a fresher, higher (bottom-up) consensus EPS base. All three remain pinned at their most-expensive bucket regardless.
5. **The DCF/multiples-vs-market divergence narrowed but didn't close.** This session's PW Fair Value ($927.71) is ~7.7% higher than the prior session's ($861.4), reflecting the confirmed guidance raise flowing through every DCF and multiples scenario — but the live price rose ~4% more than that in the same window, so the percentage gap to fair value is roughly unchanged (−50.4% vs −52.1% previously).
6. **Data-quality note worth tracking forward:** Yahoo's annual consensus row read as stale (1 analyst) within hours of the earnings release; this session worked around it with a disclosed bottom-up build. Future ASML sessions run soon after an earnings release should check for the same lag rather than assuming the "0y" row is current.

---

## 9. Recommendation

# **WATCHLIST ONLY — Composite Score 58.8 (Hold / no new entry, no trim band). Do not enter now.**

ASML delivered a genuine beat-and-raise Q2 2026 (verified against primary sources, §0) that measurably improved its Quality Score (81.5 → 82.4, still comfortably above the 80.0 gate) by pushing Profitability to its scoring ceiling. Its Valuation Score, however, remains pinned at 100.0 — the maximum — because the ~5.3% same-day price rally kept pace with (and continues to exceed) even this session's upwardly-revised, scenario-weighted fair value work (~$928, vs. a $1,869.22 live price). The 50/50 Composite Score blend moves marginally more attractive, from 59.3 to **58.8**, but stays squarely in the **50.0–69.9 "Hold — watch only, no new entry, no trim"** band. **This is a WATCHLIST/PASS outcome, not a BUY/TRIM/EXIT action** — no order setup, no entry, no position opened, `holdings.md` untouched.

---

## 10. Next Review Trigger

- **Q3 2026 earnings** (Rule 9 mandatory trigger) — expected **mid-October 2026** per ASML's consistent historical cadence (Q3 2025 reported 2025-10-15; Q3 2024 reported 2024-10-15), exact date to be confirmed via ASML's financial calendar closer to the event. Will refresh the TTM window and the Growth/Upside-Downside inputs again.
- **Any pullback toward this session's PW Fair Value (~$928) or bull-case DCF+multiples blend (~$1,214)** — the Valuation Score (and thus Composite) still has real headroom to fall from its 100.0 ceiling even with an unchanged Quality Score.
- Any further guidance revision, management change, or M&A (Rule 9 standard triggers) — note ASML already delivered one major guidance revision (up) this session; a *second* revision before Q3 earnings would be unusual and warrant an immediate re-score regardless of calendar timing.
- Any >15% unexplained move from today's $1,869.22 reference (distinct from today's own +5.27% move, which *is* explained by this session's earnings trigger).

**No position opened — nothing to log in `decisions/`.**

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session (beyond those already defined in the 2026-07-12 ASML session, which remain valid background):

| Term | Meaning |
|---|---|
| **6-K (Form 6-K)** | A report foreign private issuers furnish to the SEC to disclose material information between annual 20-F filings — this session's ASML Q2 2026 6-K had not yet posted to SEC EDGAR at session time; ASML's own investor-relations-published statements were used instead. |
| **Composite Score** | This framework's blended Quality + Valuation ranking number (0.50 × (100 − Quality Score) + 0.50 × Valuation Score); ASML's is 58.8, down from 59.3 on 2026-07-12. |
| **DCF (Discounted Cash Flow)** | A valuation method estimating a company's worth today by projecting future cash flow and discounting it back to present value. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit; ASML's TTM EBITDA is €13,549.5M. |
| **EPS (Earnings Per Share)** | Net income divided by shares outstanding; ASML's Q2 2026 basic EPS was €7.59, diluted €7.58. |
| **EUV (Extreme Ultraviolet Lithography)** | The most advanced chip-manufacturing lithography technology; ASML is the sole global manufacturer of EUV systems. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a multiple measuring how expensive a company is relative to its operating profit; ASML's TTM figure is 49.84×. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap; higher means cheaper; ASML's TTM figure is 1.596%. |
| **Forward PE** | Price ÷ next-twelve-months expected earnings per share; ASML's is 49.59× this session (bottom-up estimate, §2.6). |
| **Guidance (management guidance)** | A company's own self-issued forecast of upcoming results; per this framework's design, never scored directly (self-reported, gameable) but tracked as a Rule 9 re-valuation trigger — ASML raised its FY2026 guidance materially this session. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of its weighted score; none fired for ASML this session, same as 2026-07-12. |
| **Installed Base Management (IBM) sales** | ASML's own term for its recurring service/upgrade/field-option revenue line, distinct from new-system sales; its Q2 2026 beat (€2,762M) drove the quarter's gross-margin beat. |
| **Moat** | A durable competitive advantage protecting a business's profits from competitors; ASML's checklist reading is unchanged at 3-of-5 signals this session. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate); the numerator used to compute ROIC. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value estimate (25% bull + 50% base + 25% bear); ASML's is $927.71/share this session, up from $861.4 on 2026-07-12. |
| **Quality Score** | This framework's 0.0–100.0 continuous quality grade; 80.0+ required to proceed to valuation scoring. ASML scores 82.4 this session, up from 81.5. |
| **Rate Environment Gate** | The mandatory pre-check before Phase 02 scoring, comparing Earnings Yield to the 10-Year Treasury yield; contributed +10 this session (unchanged from 2026-07-12). |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit; ASML's TTM figure is 63.81%. |
| **Rule 9** | Fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move — this session was triggered by an earnings release that also carried a guidance revision, a "double" Rule 9 trigger. |
| **Shareholder yield** | Cash returned to shareholders as a percentage of share price — dividend yield plus net buyback yield; recomputed this session directly from TTM cash-flow-statement actuals (1.065%), an improvement in precision over the 2026-07-12 session's share-count-based proxy (1.265%). |
| **Statutory Interim Report** | A separate, more detailed half-year regulatory report (distinct from the quarterly US GAAP summary financial statements) ASML also published on 2026-07-15 for the six months ended 28 June 2026 — noted for completeness, not separately parsed this session since the US GAAP summary statements already covered every scored input. *(New term.)* |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results; this session's window is Q3 2025 through Q2 2026, refreshed from the prior session's Q2 2025–Q1 2026 window. |
| **Upside/Downside Modifier** | An additive ±15 adjustment to the valuation score based on expected annual return; ASML's computed at +8.64 this session (expected mild annual loss), down slightly from +9.30 on 2026-07-12. |
| **Valuation score** | This framework's 0.0–100.0 continuous score (0 = cheapest, 100.0 = most expensive); ASML scores 100.0 again this session, the maximum. |

# NEW POSITION — MCO (Moody's Corporation, NYSE) — 2026-09-11

**Task type:** NEW POSITION (scheduled full fresh re-run per user request — not a Rule 9 trigger scan)
**Date:** 11 Sep 2026 (Friday)
**10Y US Treasury Yield:** 4.83% (FRED `DGS10`, most recent posted observation dated 2026-09-09)
**Current MCO portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md) and [override-log.md](../portfolio/override-log.md))
**Prior coverage:** [sessions/2026-07-19-new-position-mco.md](2026-07-19-new-position-mco.md) — Quality Score 80.2 (marginal PASS, flagged as a 0.2-point photo finish), Valuation Score 70.8, Composite Score 45.3, **WATCHLIST ONLY**. No MCO session more recent than that exists; this is a full, independent re-run, not an update built on the prior numbers.
**Sector:** Financials — Credit rating agency (Moody's Investors Service, "MIS") and data/analytics/software provider (Moody's Analytics, "MA")
**First-use jargon decode:** see closing Glossary (§11)

---

## 0. Why this session exists

Requested as a full fresh re-evaluation of MCO, explicitly flagging the 07-19 session's marginal 80.2 Quality Score gate-pass (by only 0.2 points, with that session itself noting a Q1-2026-basis reading would have failed at 78.7) as warranting extra scrutiny rather than an assumed repeat pass. Per instruction, every sub-score is recomputed from scratch against current data — nothing is carried forward from the 07-19 session's numbers. Since 07-19, MCO has reported **Q2 2026 results** (filed 2026-07-23, the same week the prior session anticipated), which are incorporated below.

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("MCO")`: contract_id **6497**, exchange **NYSE**, description "MOODY'S CORP" (other results — a Mexican cross-listing, an unrelated Australian company also ticker "MCO," various unrelated bond/fund tickers — not used, same disambiguation as 07-19).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$467.36** | IBKR `get_price_snapshot`, `last` field, contract_id **6497**. `is_close: true` — this equals the 2026-09-08 weekly close from `get_price_history`, i.e. the most recent traded print obtainable via a live fetch was still showing as the last completed session at query time; flagged per Rule 0 discipline, same as the 07-19 session's own close-price flag. |
| 52-week high | $544.16 | IBKR `misc_statistics` `high_52w` |
| 52-week low | $400.93 | IBKR `misc_statistics` `low_52w` |
| 13-week high | $523.18 | IBKR `misc_statistics` |
| 26-week high | $523.18 | IBKR `misc_statistics` |
| Open 52 weeks ago | $504.61 | IBKR `misc_statistics` `open_52w` |
| Dividend yield | 0.86% | IBKR `get_price_snapshot` `dividend_yield` |
| US 10Y Treasury yield | 4.83% | FRED `DGS10`, as-of 2026-09-09 |

$467.36 sits well below the 52-week high ($544.16, −14.1%) — a materially larger discount to the 52-week high than the 07-19 session's −6.3%, reflecting a broad pullback since July even as fundamentals (below) strengthened. Context only, not scored.

Shares outstanding: **173.18M** (SEC 10-Q cover page, 2026-06-30; cross-checked against stockanalysis.com's independently-reported 173.18M — exact match). Market cap = 173.18M × $467.36 = **$80,933M**, cross-checked against stockanalysis.com's independently-reported $80.94B (matches to the dollar).

---

## 2. Data Gathered — Sources & Method

Primary source: SEC EDGAR XBRL `companyconcept` API (CIK **1059556**) for every filed financial figure below, cross-checked against MCO's own **Q2 2026 earnings release** (filed as an 8-K exhibit, SEC-hosted PDF, accession within `000162828026049104`) for the GAAP-to-adjusted reconciliation tables, and stockanalysis.com / fullratio.com (cross-verified against each other and against an independent from-scratch reconstruction below) for consensus estimates, analyst price targets, and 5-year PE benchmarks.

### 2.1 Income statement, cash flow, balance sheet (FY2021–FY2025 + TTM through Q2 2026, SEC XBRL, all in $M)

| Period | Revenue | Net Income | EBIT (Op. Income) | D&A | Cost of Revenue | OCF | CapEx | FCF |
|---|---|---|---|---|---|---|---|---|
| FY2021 | 6,218 | 2,214 | 2,844 | 257 | 1,637 | 2,005 | 139 | 1,866 |
| FY2022 | 5,468 | 1,374 | 1,883 | 331 | 1,613 | 1,474 | 283 | 1,191 |
| FY2023 | 5,916 | 1,607 | 2,137 | 373 | 1,687 | 2,151 | 271 | 1,880 |
| FY2024 | 7,088 | 2,058 | 2,875 | 431 | 1,945 | 2,838 | 317 | 2,521 |
| FY2025 | 7,718 | 2,459 | 3,351 | 480 | 1,973 | 2,901 | 326 | 2,575 |
| Q1 2025 | 1,924 | 625 | 846 | 113 | 491 | 757 | 85 | 672 |
| Q2 2025 | 1,898 | 578 | 818 | 120 | 489 | 543 | 75 | 468 |
| Q1 2026 | 2,079 | 661 | 922 | 122 | 531 | 939 | 95 | 844 |
| Q2 2026 | 2,185 | 878 | 1,046 | 126 | 518 | 779 | 91 | 688 |
| **TTM (Jul'25–Jun'26)** | **8,160** | **2,795** | **3,655** | **495** | **2,042** | **3,319** | **352** | **2,967** |

TTM computed as FY2025 − (Q1'25+Q2'25) + (Q1'26+Q2'26) for each line; cross-checked against MCO's own Table 8 (H1 2026 FCF $1,532M = Q1'26 $844M + Q2'26 $688M ✓) and against summing the four most recent quarterly FCF figures from stockanalysis.com's cash-flow page (Q3'25 $658M + Q4'25 $777M + Q1'26 $844M + Q2'26 $688M = **$2,967M**, exact match to the SEC-XBRL-derived figure — strong cross-confirmation).

FY2025 balance sheet: Total debt $6,994M, Cash $2,384M → Net debt $4,610M. **June 30, 2026 balance sheet** (Q2 2026 10-Q, Table 2): Total debt $6,946M (LT $6,375M + current portion $571M), Cash $1,467M → **Net debt $5,479M**. Q2-2026-end equity $3,025M (recovering from Q1-2026-end's $2,994M trough, itself a swing from FY2025-end's $4,054M — see §2.2).

Effective tax rate: FY2025 21.34% (Tax $668M / Pretax $3,130M); TTM (using Q1/Q2 2025+2026 quarterly tax figures) = ($668M − $179M − $193M + $209M + $292M) / ($2,795M net income + that same tax figure) = $797M / $3,592M = **22.19%**.

### 2.2 A material one-time item this quarter — the MA Regulatory Solutions divestiture gain

Per MCO's own Q2 2026 earnings release (Table 11, GAAP-to-Adjusted reconciliation): Q2 2026 GAAP net income included a **$181M pre-tax ($126M net-of-tax) gain on business divestitures** (sale of the MA Regulatory Solutions business, plus a small $2M post-close adjustment on the earlier MA Learning Solutions divestiture). This sits **below the operating-income line** (in "Non-operating income (expense), net" — confirmed via the Q2 2026 Statement of Operations, Table 1), so it does **not** distort EBIT, EBITDA, OCF (the cash-flow statement explicitly backs the non-cash gain out of the operating-activities reconciliation — Table 3), or FCF. It **does** distort GAAP Net Income and diluted EPS for the quarter: GAAP diluted EPS $5.03 vs. Adjusted (company non-GAAP, ex-gain and other standard add-backs) diluted EPS $4.68 — a $0.72/share divestiture-gain effect specifically (Table 11).

Per Rule 6 ("Normalize Before You Value — strip out one-time items"), this session **backs the $126M net gain out of TTM Net Income and TTM EPS** wherever those feed a scored sub-score or the fair-value build:
```
Normalized TTM Net Income = 2,795 − 126 = 2,669
Normalized TTM diluted EPS = 15.76 (raw TTM, see §5.3) − 0.72 = 15.04
```
EBIT, EBITDA, OCF, and FCF figures throughout this session are the **unadjusted, clean GAAP figures** — they were never distorted by this gain in the first place, confirmed directly from the primary source rather than assumed.

Separately: Q1 2026 alone saw a **$1,471M** share buyback (exceeding all of FY2025's full-year buybacks) that briefly depressed equity/cash — the swing the 07-19 session flagged as the source of its Quality Score sensitivity. By Q2-2026-end, buybacks continued (H1 2026 total $2,165M treasury-share purchases, guidance raised to "up to $3.0B" for FY2026) but equity has stabilized/modestly recovered ($2,994M → $3,025M quarter-over-quarter) as H1 net income ($1,539M) outpaced the cash return — the balance-sheet snapshot sensitivity from July has **narrowed, not resolved** (see §3.5).

### 2.3 Growth, moat, and TAM evidence

**FY2025 10-K (unchanged since 07-19, still the most recent 10-K on file):** MIS "annual price increases" realized alongside higher, not lower, monitored-credit volume (recurring revenue evidence); Big Three ~95% combined global market share (Moody's ~40%), a stable multi-decade oligopoly (CFR, third-party); NRSRO regulatory entrenchment. These facts are unchanged by one quarter's results and are carried forward as still-valid, cited evidence.

**Q2 2026 results, new this session (SEC-filed 8-K exhibit, earnings release PDF):** Revenue +15% YoY (+16% organic constant-currency), MIS +25% YoY (rated issuance volume +33%), MA ARR +9% YoY to $3.7B, MA organic constant-currency revenue +8%. **Important nuance flagged, not glossed over:** management's own release attributes this quarter's acceleration explicitly to **issuance-volume strength** (Investment Grade, Leveraged Finance, ABS/RMBS, data-center-related infrastructure financing) — not to a new pricing action. This is **consistent with, not contradictory to,** the framework's existing TAM/pricing-power evidence (the FY2025 10-K's price-increase citation is a separate, still-valid structural fact about MIS's recurring-revenue base), but it means this quarter's headline growth number should be read as **volume/cyclical**, reinforcing rather than undermining the PEG-cyclicality judgment in §5.4.

**Disruption-vector risk (own 10-K, unchanged):** Gen AI/agentic AI competitive risk explicitly flagged by the company — not dismissed, not newly resolved this session either.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology, TTM basis per quality-scoring.md's "Quantitative Inputs Needed" list)

### 3.1 Hard disqualifier check (rolling window — most recently completed fiscal years, FY2021–FY2025; FY2026 incomplete)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI <70% for 2+ consecutive years w/o growth-capex explanation | 84.3% / 86.7% / 117.0% / 122.5% / 104.7% (FY2021–FY2025) — every year above 70% | disqualify if 2+ consecutive years sub-70% | ✅ **PASS** |
| Net Debt/EBITDA over threshold | 1.203× (FY2025-end) / 1.320× (Q2-2026-end, TTM EBITDA) | disqualify if >2.5× (or >4× asset-light) | ✅ **PASS** on either basis, comfortably |
| FCF-positive 3+ consecutive years | All 5 of the last 5 fiscal years positive; TTM also positive ($2,967M) | disqualify if not | ✅ **PASS** |

**No hard disqualifier fires.**

### 3.2 Profitability (25% weight) — TTM basis, normalized for the one-time divestiture gain (Rule 6, §2.2)

```
Normalized TTM Net Income = 2,669   TTM Revenue = 8,160
Net Margin (TTM, normalized) = 2,669 / 8,160 = 32.71%
NetMargin_Component = clamp((32.71/30)×100, 0, 100) = 100.0   (clamped — above the 30% ceiling)

EBIT (TTM) = 3,655   (unaffected by the divestiture gain — it sits below the operating-income line)
Effective tax rate (TTM) = 22.19%
NOPAT = 3,655 × (1 − 0.2219) = 2,843.9
Invested Capital (2026-06-30) = Debt 6,946 + Equity 3,025 − Cash 1,467 = 8,504
ROIC = 2,843.9 / 8,504 = 33.44%
ROIC_Component = clamp((33.44/30)×100, 0, 100) = 100.0   (clamped)

Profitability_Score = (100.0 + 100.0) / 2 = 100.0   (no FCF-positivity cap — 5yr + TTM positive)
```
Note: both components clamp at the 100.0 ceiling whether or not the divestiture gain is backed out (32.71% or 34.25% unnormalized both clear 30%) — the normalization doesn't change this sub-score's outcome, but is still shown per "never invent, never skip a step."

### 3.3 Margins (15% weight) — TTM basis

```
Gross Margin analog (TTM) = (8,160 − 2,042) / 8,160 = 74.98%
GrossMargin_Score = clamp((74.98/80)×100, 0, 100) = 93.73
```
No structural-trend bonus applies (already well above the 40% threshold the bonus is gated on).

### 3.4 Growth (20% weight) — 3yr FY revenue CAGR, unchanged methodology from 07-19

```
Revenue 3yr CAGR (FY2022 $5,468M → FY2025 $7,718M) = (7,718/5,468)^(1/3) − 1 = 12.17%
Growth_Score (raw) = clamp((12.17/25)×100, 0, 100) = 48.70
```
**TAM/pricing-power modifier (+10):** documented, actual (not guidance) evidence — the FY2025 10-K's price-increase/higher-monitored-credit-volume finding (§2.3, unchanged and still valid), reinforced by Q2 2026's ARR +9%, MA organic cc growth +8%, and continued Decision Solutions (KYC +11% organic cc, Insurance +9%) momentum. Q2 2026's specific driver (issuance-volume surge) is **not** itself counted as new pricing-power evidence — flagged transparently in §2.3 — but it does not remove the still-standing FY2025 10-K citation.

**No deceleration modifier:** growth is accelerating (FY24→25 +8.9%, Q2 2026 YoY +15%), the opposite of a structural slowdown.
```
Growth_Score = 48.70 + 10 = 58.70
```

### 3.5 Balance Sheet (15% weight) — the same sensitivity as 07-19, narrower but not resolved

```
FY2025-end basis (primary — cleanest, fully audited):
  Net Debt = 6,994 − 2,384 = 4,610      EBITDA (FY2025) = 3,831
  Net Debt/EBITDA = 4,610 / 3,831 = 1.203×
  BalanceSheet_Score = clamp(100×(1 − 1.203/4), 0, 100) = 69.92

Q2-2026-end basis (sensitivity — most current available quarter):
  Net Debt = 6,946 − 1,467 = 5,479      EBITDA (TTM Jul'25–Jun'26) = EBIT 3,655 + D&A 495 = 4,150
  Net Debt/EBITDA = 5,479 / 4,150 = 1.320×
  BalanceSheet_Score = clamp(100×(1 − 1.320/4), 0, 100) = 67.00
```
**Basis used: FY2025 fiscal year-end**, same reasoning as 07-19 (complete, fully audited figures, not distorted by any single quarter's buyback timing). The gap between the two bases has **narrowed** since July (was 69.92 vs. 61.25, an 8.67-point spread; now 69.92 vs. 67.00, a 2.92-point spread) — equity has partially stabilized post the Q1 2026 buyback spike (§2.2) — but it has **not disappeared**, and as §3.6 shows, it still matters at the margin.

### 3.6 Moat Signal (15% weight) — unchanged from 07-19; no new evidence found or needed this session

| Signal | Evidence | Result |
|---|---|---|
| Market share stable/growing | Big Three ~95% combined global share, Moody's ~40% (CFR, third-party); MIS revenue +25% YoY Q2 2026 | ✅ TRUE |
| Brand premium (pricing power) | FY2025 10-K: "annual price increases" realized alongside higher monitored-credit volume | ✅ TRUE |
| Network effect | No documented two-sided-marketplace mechanism found this session either | ❌ not established |
| Switching costs | NRSRO regulatory status (own 10-K) | ✅ TRUE |
| Scale cost advantage | No cost-per-unit citation vs. smaller CRAs/analytics vendors found this session | ❌ not established |

```
Moat_Score = (3/5) × 100 = 60.0
```

### 3.7 FCF Quality (10% weight) — TTM basis, normalized for the divestiture gain

```
FCF/NI (TTM, using normalized Net Income) = 2,967 / 2,669 = 111.2%
FCFQuality_Score = clamp(((1.112 − 0.40)/0.60)×100, 0, 100) = clamp(118.7) = 100.0   (clamped)
```
(Also clamped at 100.0 using the unnormalized TTM ratio, 2,967/2,795 = 106.15% — the normalization doesn't change this sub-score's outcome either, shown for completeness.)

### 3.8 Quality Score — final, and the gate margin (still a photo finish)

```
Quality Score = 0.25×Profitability + 0.15×Margins + 0.20×Growth + 0.15×BalanceSheet + 0.15×Moat + 0.10×FCFQuality

FY2025-end Balance Sheet basis (primary):
= 0.25×100.0 + 0.15×93.73 + 0.20×58.70 + 0.15×69.92 + 0.15×60.0 + 0.10×100.0
= 25.00 + 14.0595 + 11.740 + 10.488 + 9.00 + 10.00
= 80.2875  →  rounded 80.3

Q2-2026-end Balance Sheet basis (sensitivity):
= 25.00 + 14.0595 + 11.740 + 0.15×67.00 + 9.00 + 10.00
= 25.00 + 14.0595 + 11.740 + 10.05 + 9.00 + 10.00
= 79.8495  →  rounded 79.8   (FAILS the gate)
```

**Quality Score used: 80.3 — clears the 80.0+ gate, but again by a razor-thin margin (0.3 points this time vs. 0.2 in July), and the alternate, equally defensible balance-sheet basis still fails at 79.8.** This is the *same* structural sensitivity flagged in the 07-19 session, not a new one — carried through transparently rather than smoothed over, and weighted heavily in this session's final recommendation (§8). The margin narrowed slightly (spread 8.67→2.92 points between the two bases) but the underlying judgment call (which balance-sheet snapshot is "primary") is exactly as consequential as it was in July.

---

## 4. Rate Environment Gate

```
Forward PE = Live Price / Consensus FY2026 EPS = 467.36 / 16.97 = 27.54×
  (Consensus EPS $16.97, 21 analysts, stockanalysis.com — within MCO's own guided
   Adjusted Diluted EPS range $16.50–$17.00; guidance itself not used as the scored figure)

Step 1 — Earnings Yield Spread Test:
  EY = 1/27.54 = 3.63%
  Spread = EY − 10Y Treasury = 3.63% − 4.83% = −1.20pp
  Spread < +1.5% → +5 additive (yellow flag, not a veto)

Step 2 — Rate Regime Modifier:
  10Y yield 4.83% falls in the 3.5–5% bracket → +5

Total Rate Environment Gate modifier = +10
```
Same total modifier as 07-19 (+10), though the 10Y yield itself rose materially (4.10%→4.83%) — it stayed within the same 3.5–5% bracket.

---

## 5. Phase 02 — Valuation Score

### 5.1 FCF Yield (40% weight)

```
FCF Yield = TTM FCF / Market Cap = 2,967 / 80,933 = 3.6655%
FCF_Score = clamp(100×(1 − 3.6655/10), 0, 100) = 63.35
```

### 5.2 EV/EBIT (25% weight — redistributed to 40%, see §5.4)

```
EV = Market Cap + Net Debt (Q2-2026-end, most current) = 80,933 + 5,479 = 86,412
EBIT (TTM) = 3,655
EV/EBIT = 86,412 / 3,655 = 23.65×
EV/EBIT_Score = clamp((23.65 − 12)/23 × 100, 0, 100) = 50.63
```

### 5.3 Forward PE (20% weight) — full 5-year range reconstruction

`yfinance` not used (same environment issues as prior sessions); reconstructed independently from SEC XBRL quarterly diluted EPS (`EarningsPerShareDiluted`, Q1 2021–Q2 2026, with the four annual-minus-9-months Q4 figures backed out) paired with IBKR weekly closes at each quarter-end, then cross-checked against two independent third-party sources (fullratio.com: 5yr avg 37.53×; a second aggregator: 39.25×) — this session's own reconstruction (38.39×) sits squarely between them, corroborating the method:

```
TTM EPS series reconstructed at each of the last 19 quarter-ends (Q4'21–Q2'26; the 20th quarter,
Q3'21, isn't computable without Q4'20 data — same minor, flagged approximation as the 07-19 session):

5yr avg PE = 38.39×   5yr low = 27.64× (Q2 2022)   5yr high = 48.27× (Q2 2023)

Forward PE = 27.54×

FwdPE_Score (primary formula) = clamp((27.54 − 27.64)/(48.27 − 27.64) × 100, 0, 100)
                               = clamp(-0.48, 0, 100) = 0.0   (essentially at the 5yr low)

Historical PE Modifier (Upgrade 2): (27.54 − 38.39)/38.39 = −28.26%
  — more than 20% below the 5yr average → −10 modifier applies

FwdPE_Score (final) = clamp(0.0 − 10, 0, 100) = 0.0
```
A material shift from 07-19 (FwdPE_Score was 9.08 then): the live price fell ~8.5% since July while consensus FY2026 EPS actually *rose* slightly ($16.76→$16.97), compressing Forward PE from 30.48× to 27.54× — now sitting at the bottom of its own trailing 5-year range.

**TTM EPS note (for §7, not this sub-score):** raw TTM diluted EPS (sum of last 4 quarters) = $3.60+$3.40+$3.73+$5.03 = **$15.76**; per Rule 6 (§2.2), the Q2 2026 divestiture gain ($0.72/share) is backed out for fair-value work → **normalized TTM EPS $15.04**.

### 5.4 PEG — not applied, redistributed to EV/EBIT (unchanged judgment from 07-19)

EPS growth exceeded 15% in each of FY2023 (+17.3%), FY2024 (+29.0%), and FY2025 (+21.4%) — mechanically a Fast Grower. **Still not applied**, per Upgrade 3's "never apply to cyclicals" carve-out: this growth remains a recovery/mean-reversion off the 2022 rate-hike-driven bond-issuance trough (FY2022 EPS fell 36.8%), and Q2 2026's own reported growth driver (issuance-volume surge, §2.3) *reinforces* rather than undermines this cyclicality read — MCO's own 10-K explicitly ties revenue to debt-issuance-market volume. PEG's 15% weight redistributed to EV/EBIT (→ 40%), same as 07-19.

### 5.5 Raw weighted score

```
Raw Score = 0.40×FCF_Score + 0.40×EV/EBIT_Score + 0.20×FwdPE_Score
          = 0.40×63.35 + 0.40×50.63 + 0.20×0.0
          = 25.34 + 20.25 + 0.0
          = 45.59
```

### 5.6 Upside/Downside Modifier

Fair value build in full in §7. Summary inputs:

```
Blended (40% DCF/60% Multiples) PW Fair Value:
  Bull $616.06   Base $432.83   Bear $322.49
PW Fair Value = 0.25×616.06 + 0.50×432.83 + 0.25×322.49 = 154.02 + 216.42 + 80.62 = $451.06

Gap Upside % = (451.06 / 467.36) − 1 = −3.49%    (priced modestly above PW FV, not below)
Catalyst window: no specific re-rating catalyst identified within 18–24 months this session either
  (default 2yr window per Rule 10)
Annualized gap = −3.49% / 2 = −1.75%/yr

Intrinsic growth = 8.0%/yr   (4yr FCF CAGR, FY2021 $1,866M → FY2025 $2,575M = 8.39%, rounded —
                              unchanged methodology from 07-19, a structural input not sensitive
                              to one quarter)
Shareholder yield = Dividend yield 0.86% (IBKR, §1) + Net buyback yield 3.46%
  (shares outstanding 179.4M, 2025-06-30 → 173.2M, 2026-06-30, SEC 10-Q cover pages,
   −3.46% over exactly 12 months)

E = −1.75 + 8.0 + 0.86 + 3.46 = 10.57%/yr
```

`E` (10.57%) now sits **just above** the 10% hurdle `H` (was below it, at 2.39%, in July):
```
E ≥ H:  M = −15 × clamp((E − H)/15pp, 0, 1) = −15 × clamp((10.57−10)/15, 0, 1) = −15 × 0.038 = −0.57
```
Guardrail check: no catalyst within 18–24 months → upside side capped at −5; −0.57 is well inside that cap, no capping needed.

### 5.7 Final Valuation Score

```
Final Score = Raw Score + Rate Environment Gate modifier + Upside/Downside Modifier
            = 45.59 + 10.0 + (−0.57)
            = 55.02  →  rounded 55.0
```

A large drop from 07-19's 70.8 ("Expensive" on the raw score alone) — mainly driven by the Forward PE sub-score collapsing to 0.0 (price down, EPS estimate up) and a materially smaller Upside/Downside penalty (E crossed above the 10% hurdle, versus well below it in July).

---

## 6. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 80.3) + 0.50 × 55.0
                = 0.50 × 19.7 + 0.50 × 55.0
                = 9.85 + 27.50
                = 37.35  →  rounded 37.4   (exact .X5 boundary — rounds up per the framework's rule)
```

**Composite Score = 37.4 → "Cheap" band (30.0–49.9)**, meaningfully cheaper than 07-19's 45.3 — driven primarily by the Valuation Score's sharp decline (price fell while quality-driving fundamentals and consensus estimates improved). Flagged the same way as 07-19: the Quality Score input is again a photo-finish gate-pass (§3.8), so this reading is treated with the same caution the framework applied last time, not mechanically executed. See §8.

---

## 7. Fair Value & Order Setup

### 7.1 DCF (3-scenario, per Rule 7)

Assumptions shifted modestly from 07-19 to reflect the higher risk-free rate (10Y 4.10%→4.83%): WACC shifted up ~0.5pp across all three scenarios; growth/fade/terminal assumptions held structurally unchanged (deliberately not chasing Q2 2026's cyclical issuance-volume spike into a decade-long growth assumption, per Rule 6's normalization discipline):

| | Bull | Base | Bear |
|---|---|---|---|
| WACC | 8.5% | 9.5% | 10.5% |
| Years 1–5 FCF growth | 9% | 8% | 7% |
| Years 6–10 fade | 9%→4% | 7%→3.5% | 6%→2% |
| Terminal growth | 3.5% | 3.0% | 2.5% |

Starting FCF: TTM $2,967M (clean, unaffected by the divestiture gain — §2.2). Full 10-year explicit projection + terminal value computed and discounted year-by-year (shown in full below rather than summarized, per "no black-box outputs"):

**Base case (WACC 9.5%):** FCF grows 8%/yr through Yr5 ($4,359.5M), fades 7.0%→3.5% through Yr10 ($5,629.3M), terminal value at 3.0% perpetuity = $89,203M. Sum of discounted Yr1–10 FCFs = $26,760.4M; discounted terminal = $35,992.3M. **Total DCF EV = $62,752.7M** → Equity (− Net Debt $5,479M) = $57,273.7M → **$330.75/share** (173.18M shares).

**Bull case (WACC 8.5%):** FCF grows 9%/yr through Yr5 ($4,565.1M), fades 9.0%→4.0% through Yr10 ($6,251.1M), terminal at 3.5% = $129,398M. **Total DCF EV = $86,991.9M** → Equity $81,512.9M → **$470.79/share**.

**Bear case (WACC 10.5%):** FCF grows 7%/yr through Yr5 ($4,161.3M), fades 6.0%→2.0% through Yr10 ($5,060.6M), terminal at 2.5% = $64,838.8M. **Total DCF EV = $48,150.4M** → Equity $42,671.4M → **$246.42/share**.

(Cross-check: all three land within ~1% of the 07-19 session's independently-derived DCF outputs of $325.06/$470.25/$238.17 despite the different starting FCF and WACC — consistent methodology, not a fresh model producing an unrelated answer.)

### 7.2 Multiples-based value

```
Method A — Historical-PE cross-check (Rule 3), using Rule-6-normalized TTM EPS (§2.2, §5.3):
  Normalized TTM EPS $15.04 × 5yr avg PE 38.39× = $577.5

Method B — Normalized EV/EBIT (20×, below the current 23.65×, per Rule 4's sanity check),
  applied to an estimated next-12mo EBIT (TTM EBIT × 1.08 ≈ $3,947.4M):
  EV $78,948M → Equity ($78,948M − $5,479M net debt) $73,469M → $424.28/share

Multiples-Based Value (Base) = ($577.5 + $424.28) / 2 = $500.89
```
Bull/Bear multiples values scaled proportionally to the DCF bull/bear ratios (1.4235× / 0.7451×): **Bull $712.90, Bear $373.20.**

### 7.3 Blended Fair Value (40% DCF / 60% Multiples, per Triangulation Formula)

```
Bull:  0.40×470.79 + 0.60×712.90 = 188.32 + 427.74 = $616.06
Base:  0.40×330.75 + 0.60×500.89 = 132.30 + 300.53 = $432.83
Bear:  0.40×246.42 + 0.60×373.20 =  98.57 + 223.92 = $322.49

PW Fair Value (0.25/0.50/0.25) = $451.06   (as used in §5.6)
```

**Sanity check (Rule 0 Step 4 / bull-case FV check):** independent analyst consensus 12-month price target is **$561.90** (range $505–610, 21–24 analysts, stockanalysis.com), implying ~20% upside from the $467.36 live price — a materially more bullish external read than this session's own bottom-up PW Fair Value ($451.06, essentially flat to slightly below the current price). This session's own Bull-case Blended FV ($616.06) sits above the consensus PT; the Base case ($432.83) sits below both. Shown transparently rather than reconciled away — the sell-side is more optimistic than this framework's bottom-up build.

### 7.4 Order setup

Composite Score 37.4 falls in the 30.0–49.9 band → Margin of Safety 25–30% (midpoint 27.5% used), Max Acceptable Loss 25–30% (midpoint 27.5% used):

```
[X] Composite Score (incl. Upside/Downside Mod):  37.4   (≤49.9 — clears the entry-eligible range)
[X] Expected annual return E / catalyst window:   10.57% / 2yr (default, no specific catalyst identified)
[X] Upside/Downside Modifier applied:             −0.57
[X] DCF Fair Value (base):                        $330.75
[X] Multiples-Based Fair Value (base):             $500.89
[X] Blended Fair Value (PW, bull/base/bear):        $451.06
[X] Margin of Safety %:                            27.5%
[X] BUY PRICE (limit order):                       $327.02
[X] PRIMARY SELL TARGET (= PW Fair Value):          $451.06
[X] BULL-CASE TRIM TARGET (Bull FV × 0.90):         $554.45
[X] STOP LOSS (Buy Price × (1−27.5%)):              $237.09
[X] Risk/Reward Ratio (Primary Sell Target basis):  1.38 : 1   ❌ below the 2:1 minimum
[X] Risk/Reward Ratio (Bull-Case Trim Target basis):2.53 : 1   (clears 2:1, but is the optimistic case)
[ ] Position size — not computed; R/R gate fails before sizing is reached (same outcome as 07-19)
```

**Risk/Reward again fails the 2:1 minimum on the primary (baseline) sell target — 1.38:1, identical to the 07-19 session's own 1.38:1**, despite every other input in the chain (price, EPS, Composite Score, PW Fair Value) having moved. This is a structural feature of the framework's MoS/Stop-Loss geometry at this Composite Score band when Buy Price and Sell Target both derive from the same PW Fair Value, not a coincidence worth over-reading — but it is the same disqualifying finding as last time, recomputed independently rather than assumed.

---

## 8. Recommendation: **WATCHLIST ONLY — do not enter, do not place an order this session**

Two independent reasons converge — fewer than 07-19's three (the Q2 2026 earnings-trigger reason has now resolved, favorably, into this session), but each still sufficient on its own:

1. **The Quality Score gate is again a photo finish** (80.3 on the primary FY2025-end basis vs. 79.8 on the equally defensible Q2-2026-end basis, §3.5/§3.8) — narrower than July's 0.2-vs-78.7 spread, but not resolved, and the entire Composite/Fair-Value/order-setup chain below it depends on which side of 80.0 this lands on.
2. **Risk/Reward fails the framework's own 2:1 minimum** (1.38:1 on the primary sell target, §7.4, identical to 07-19's result) — fair-value-methodology.md's explicit instruction for this outcome is to wait, tighten the stop, or pass, not to place the naive MoS-derived limit order anyway.

**What changed since 07-19, for the record:** the stock is meaningfully cheaper (Composite 45.3→37.4) on genuinely improved fundamentals (Q2 2026 beat, EPS estimates up, Forward PE compressed to the bottom of its 5yr range) rather than a fundamentals-deteriorating sell-off — this is a *more* attractive setup than July's, just not one that clears both of this framework's own gates yet. **No order placed, no position opened.**

---

## 9. Next Review Trigger

- **MCO's Q3 2026 earnings**, expected ~late October 2026 (10-Q filing pattern: 2025-10-23 last year) — a full re-score should follow, given the still-open §3.5 balance-sheet-basis sensitivity this next quarter's data could meaningfully narrow further (or reopen).
- Confirmation of whether the FY2026 buyback pace (guided "up to $3.0B") continues at a rate that keeps equity/cash stable, or resumes pressuring the Balance Sheet sub-score.
- Standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move.
- If the R/R gate is the only remaining blocker at that point, a meaningfully lower entry price (rather than a fundamental change) could on its own clear this framework's bar — worth rechecking opportunistically, not just on the quarterly cadence.

**No position opened — nothing to log in `decisions/`.**

---

## 10. Data Gaps Flagged

1. **None of the Quality Score sub-scores were blocked by a missing metric** — same clean-disclosure situation as 07-19.
2. **The Balance Sheet sub-score sensitivity persists** (§3.5, §3.8) — narrower than July (2.92-point Quality Score spread vs. 8.67 points in July) but not resolved; flagged prominently, not silently patched.
3. **The 5yr-PE-reconstruction series is 19, not 20, quarters deep** — same minor, flagged approximation as 07-19 (IBKR daily/weekly history depth constraint), now independently corroborated against two third-party aggregators (37.53× and 39.25× vs. this session's own 38.39×) for confidence.
4. **DCF WACC/beta/growth-fade assumptions remain modeling judgment calls**, shifted modestly (WACC +0.5pp across scenarios) to reflect the higher risk-free rate, explicitly flagged as distinct from the sourced financial data.
5. **Q2 2026's growth acceleration is issuance-volume-driven, not newly-evidenced pricing power** — flagged explicitly in §2.3/§3.4 so the TAM/pricing-power modifier isn't silently re-justified on the wrong basis.

---

## 11. Glossary

| Term | Meaning |
|---|---|
| **Adjusted Diluted EPS (Moody's)** | Moody's own non-GAAP diluted-EPS measure, excluding acquisition-related intangible amortization, restructuring, an international non-income tax reserve, duplicate NY-HQ rent, and gains on business divestitures. Q2 2026 GAAP diluted EPS was $5.03 vs. Adjusted $4.68 — the $0.35/share gap driven mainly by the $0.72/share divestiture-gain exclusion (partly offset by the standard recurring add-backs). This framework backs the divestiture gain specifically out of its own TTM figures per Rule 6, rather than adopting the company's full adjusted-EPS figure wholesale (§2.2, §5.3). |
| **ARR (Annual Recurring Revenue)** | See [glossary.md](../framework/glossary.md). MA's ARR grew 9% YoY to $3.7B in Q2 2026 (§2.3). |
| **Big Three (credit rating agencies)** | See [glossary.md](../framework/glossary.md). Unchanged evidence from 07-19 (§2.3, §3.6). |
| **CAGR** | Compound Annual Growth Rate. |
| **Composite Score** | This framework's 0.0–100.0 blend of Quality Score and Valuation Score (50/50); 37.4 this session (§6), down from 45.3 in July. |
| **CRA (Credit Rating Agency)** | See [glossary.md](../framework/glossary.md). |
| **DCF** | Discounted Cash Flow (§7.1). |
| **Divestiture (MA Regulatory Solutions)** | Moody's Analytics' sale of its Regulatory Solutions business unit, completed in Q2 2026, generating a $181M pre-tax / $126M net-of-tax non-operating gain — normalized out of this session's TTM figures per Rule 6 (§2.2). |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value and Enterprise Value ÷ EBIT (§5.2). |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, used in the Rate Environment Gate (§4). |
| **Fast Grower** | Peter Lynch's term for EPS growth >15%/year for 3+ years — MCO's PEG sub-score deliberately not applied (§5.4), same judgment as 07-19. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income. |
| **Hard disqualifier** | See [glossary.md](../framework/glossary.md). None fired for MCO this session (§3.1). |
| **Moat Signal** | This framework's 5-point qualitative checklist; MCO scored 3 of 5 again this session (§3.6, unchanged from 07-19). |
| **NRSRO (Nationally Recognized Statistical Rating Organization)** | See [glossary.md](../framework/glossary.md). |
| **PW (Probability-Weighted) Fair Value** | See [glossary.md](../framework/glossary.md). $451.06/share this session (§5.6, §7.3), down from $420.10 in July on a smaller live-price/FV gap despite a lower live price — both the numerator and denominator moved. |
| **Quality Score** | 80.3 this session (§3.8) — clears the 80.0+ gate by a razor-thin margin, same structural photo-finish as July's 80.2. |
| **Rate Environment Gate / Rate Regime Modifier** | See [glossary.md](../framework/glossary.md). Contributed +10 again this session (§4), though the underlying 10Y yield rose from 4.10% to 4.83% — same bracket, same modifier. |
| **R/R (Risk/Reward Ratio)** | See [glossary.md](../framework/glossary.md). Failed at 1.38:1 on the primary target (§7.4), identical to 07-19's result. |
| **ROIC** | Return on Invested Capital — 33.44% TTM (normalized), clamped at the Quality Score formula's 100.0 ceiling (§3.2). |
| **Shareholder yield** | Dividend yield plus net buyback yield (§5.6). |
| **TTM (Trailing Twelve Months)** | Jul 2025–Jun 2026 basis used throughout this session's Quality and Valuation score inputs (§2.1 onward). |
| **Upside/Downside (Expected-Return) Modifier** | See [glossary.md](../framework/glossary.md). MCO's expected return (E=10.57%) now sits just *above* the 10% hurdle, producing a small negative modifier (−0.57) — a reversal from July's E=2.39% (below hurdle, +3.81 modifier) (§5.6). |
| **WACC** | Weighted Average Cost of Capital — 8.5–10.5% across MCO's bull/base/bear scenarios this session, shifted up ~0.5pp from July to reflect the higher risk-free rate (§7.1). |

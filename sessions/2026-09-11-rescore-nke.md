# RESCORE — NKE (NIKE, Inc.)

## 1. Session header
- **Task type:** RESCORE (single ticker, full `--both` mode) — routine quarterly-cadence re-score, overdue since 2026-07-01
- **Date:** 2026-09-11
- **10Y US Treasury yield:** 4.83% (FRED `DGS10`, most recent non-blank value, 2026-09-09 — 2026-09-10/09-11 not yet posted)
- **Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% band)
- **Prior score:** Valuation 13.9, Quality 44.4, Composite 34.8 (2026-07-01 rescore) — Cheap-looking Composite band, HOLD existing / do NOT add, under a documented value-trap / Turnaround Sub-Gate override
- **First-use jargon decode:** see closing Glossary section (step 9).

## 2. Data gaps flagged / resolved (before proceeding)

- **FY2026 Form 10-K now filed** (2026-07-15, accession 0000320187-26-000088) — this **resolves** the 2026-07-01 session's flagged gap (FY2026 cash-flow statement not yet available). Audited FY2026 FCF/D&A figures below **replace** the carried-forward FY2025 figures used last session — this is a real data update, not a re-derivation, and it moves both the Quality and Valuation scores materially (see §6–7).
- **No new quarterly earnings since last review.** Nike's fiscal Q1 FY2027 (quarter ended ~31 Aug 2026) reports **2026-09-29** — still 18 days out. No new income-statement data this session; FY2026 full-year figures (revenue $46,398M, EPS $2.10, EBIT $3,850M, eff. tax rate 20.3%) carried forward unchanged from the 2026-06-30 8-K/10-K.
- **Material third-party estimate revision (real news, not invented):** JPMorgan (Matthew Boss) downgraded NKE to **Underweight** on 2026-08-04, cutting FY2027 EPS estimate to **$1.55** and FY2028 to **$1.72** (both well below Street), price target to **$40** (from $47, ~21× CY2028 EPS) — citing a **Greater China online-marketplace reset beginning January 2027** that JPMorgan calls an "unmitigated" revenue headwind of **>$1B/yr (~20% of China revenue)**, China revenue down ~30% since 2021 with **8 consecutive quarters** of YoY declines, plus a wave of US store closures creating a headwind through H1 FY2028. Sources: [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/jpmorgan-cuts-nike-underweight-sees-121708338.html), [Investing.com](https://www.investing.com/news/stock-market-news/jpmorgan-cuts-nike-to-underweight-sees-eps-well-below-consensus-4834019).
- **Street consensus FY2027 EPS has fallen from $2.37 (2026-06-20/07-01 sessions) to $1.71** (stockanalysis.com, 38 analysts, accessed 2026-09-11) — a real, cited, ~28% cut, not carried forward. Other sources show a range ($1.72–$1.84 per LSEG/other aggregators, JPMorgan's own $1.55 an outlier-low) — $1.71 used as primary per this framework's existing stockanalysis.com sourcing convention (consistent with prior sessions), range flagged.
- **5yr historical PE range (18.2× low / 40.3× high / 29.5× avg) carried forward unchanged** — the `yfinance`-based reconstruction method remains unavailable (same TLS/`curl_cffi` issue documented across many sessions in this repo). A slow-moving 5yr statistic; flagged again for recompute once yfinance access is restored.
- **FCF-positive 3-consecutive-year check refreshed from SEC XBRL** (not carried forward): FY2024 $6,617M, FY2025 $3,268M, FY2026 $2,184M — all positive, confirms no disqualifier.

## 3. Live data (Rule 0 — fetched first)

| Item | Value | Source |
|---|---|---|
| Live price | **$36.61** | IBKR `get_price_snapshot` (contract_id 10291, NYSE), essentially flat on the day (−0.03%) |
| 52-week range | **$36.55 (new 52wk low) – $75.31** | IBKR `get_price_snapshot` `misc_statistics` — price is now sitting almost exactly at its 52-week low |
| Diluted weighted-avg shares (FY2026) | 1,481.0M | SEC Form 10-K income statement, unchanged from 8-K |
| Market cap (computed) | $54,219.4M (1,481.0M × $36.61) | Computed |
| Total debt | $7,942M | SEC Form 10-K balance sheet (31 May 2026), unchanged from 8-K |
| Cash + short-term investments | $9,027M | SEC Form 10-K balance sheet, unchanged from 8-K |
| Enterprise value (computed) | $53,134.4M | Computed (Market cap + Debt − Cash&STI) |
| FY2026 OCF / CapEx / FCF (audited) | $2,868M / $684M / **$2,184M** | SEC XBRL `companyconcept` API (`NetCashProvidedByUsedInOperatingActivities`, `PaymentsToAcquirePropertyPlantAndEquipment`), 10-K filed 2026-07-15 |
| FY2026 D&A (audited) | $747M | SEC XBRL `DepreciationDepletionAndAmortization` |
| Analyst consensus FY2027 EPS | **$1.71** (38 analysts) — down from $2.37 last session | stockanalysis.com/stocks/nke/forecast |
| 10Y Treasury | 4.83% | FRED `DGS10`, 2026-09-09 |

## 4. Fundamental changes since last review (2026-07-01)

- **No new earnings release** — Q1 FY2027 reports 2026-09-29 (18 days out).
- **FY2026 10-K filed 2026-07-15**, converting last session's carried-forward FY2025 cash-flow figures into audited FY2026 figures: **FCF fell from $3,268M (FY2025) to $2,184M (FY2026), a −33.2% decline**, even as EBIT and net income were roughly flat — driven by OCF falling from $3,698M to $2,868M (working-capital/tariff-timing effects) while CapEx rose from $430M to $684M. This is the single biggest driver of this session's score changes (see §6–7).
- **JPMorgan downgrade + China marketplace-reset disclosure (2026-08-04)** — new, cited, material third-party evidence: an "unmitigated" >$1B/yr China revenue headwind starting January 2027, layered on top of the already-documented (2026-07-01 session) China share-loss and brand-value-erosion evidence. Reinforces rather than newly establishes the Moat checklist's existing ✗ Market share / ✗ Brand premium findings (see §6) — no moat sub-score change, but materially strengthens conviction in the existing Quality Watch escalation.
- **Consensus FY2027 EPS cut ~28%** ($2.37 → $1.71) — flows directly into Forward PE, the Base-case scenario FV, and the Upside/Downside Modifier below.
- **Stock at a new 52-week low ($36.55)**, down ~8% from the $39.80 print at last review, but far less than the ~28% EPS-estimate cut — i.e., the stock has gotten cheaper in absolute price terms but **more expensive on forward earnings** because the earnings estimate fell faster than the price.

## 5. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** EY = 1 ÷ Forward PE = 1 ÷ 21.41 = **4.67%**. Spread = 4.67% − 4.83% = **−0.16%**, which is **< +1.5% → FAIL → +5** (flips back from the 2026-07-01 PASS, because Forward PE rose sharply on the EPS-estimate cut even as price fell — see §7).
- **Step 2 — Rate Regime Modifier:** 10Y 4.83% sits in the 3.5–5% band → **+5**.
- Combined Rate-Gate additions: **+10**.

## 6. Quality Score (2026-06-29 methodology)

```
Profitability (25%): unchanged inputs (FY2026 income statement unchanged since last review)
  Net Margin FY2026 = 3,108/46,398 = 6.70%
  NOPAT = EBIT × (1 − eff. tax rate) = 3,850 × (1 − 0.203) = $3,068.5M
  Invested Capital = Total Debt ($7,942M) + Shareholders' Equity ($14,865M) = $22,807M
  ROIC FY2026 = 3,068.5 / 22,807 = 13.45%
  NetMargin_Component = clamp((6.70/30)×100) = 22.33
  ROIC_Component       = clamp((13.45/30)×100) = 44.83
  Profitability_Score  = (22.33 + 44.83) / 2 = 33.58   (no FCF cap — 3yr FCF-positive confirmed §2)

Margins (15%): unchanged — Gross margin FY2026 42.92% (19,911/46,398)
  GrossMargin_Score = clamp((42.92/80)×100) = 53.65
  3yr trend still net DOWN (FY2024 44.56% → FY2025 42.74% → FY2026 42.92%) → no +10 bonus.

Growth (20%): unchanged — Revenue 3yr CAGR (FY2023→FY2026) = −3.24%
  Growth_Score = 0.0
  No structural-deceleration −10 penalty (same reasoning as 2026-07-01: company-specific
    execution/mix/China issues within a still-growing global athletic-footwear category —
    though the newly-disclosed JPMorgan China marketplace-reset headwind (§2/§4) is flagged as
    evidence worth revisiting if a *second* consecutive rescore shows further deceleration).

Balance Sheet (15%): recomputed with audited FY2026 D&A ($747M, down from FY2025's $775M)
  Net Debt = Total Debt ($7,942M) − Cash&STI ($9,027M) = −$1,085M (net cash, unchanged)
  EBITDA = EBIT ($3,850M) + D&A ($747M, audited FY2026) = $4,597M
  Net Debt/EBITDA = −1,085/4,597 = −0.236×
  BalanceSheet_Score = clamp(100×(1−(−0.236)/4)) = 105.9 → clamp to 100.0   (unchanged in practice)

Moat Signal (15%): unchanged checklist (no new signal flips this session), same cited evidence as
  2026-07-01 (Euromonitor/WWD/YipitData share-loss data; Kantar BrandZ brand-value collapse
  27th→51st→69th over 2 years; only Scale cost advantage marked TRUE).
  Moat_Score = (1/5) × 100 = 20.0
  **Reinforcing (not scored) evidence this session:** JPMorgan's 2026-08-04 note documents an
    additional, quantified, forward-looking China headwind (>$1B/yr from a Jan-2027 marketplace
    reset, 8 consecutive quarters of YoY China declines) — doesn't flip any checklist item (already
    FALSE) but strengthens confidence the moat erosion is active and continuing, not a one-off.

FCF Quality (10%) — recomputed with **audited FY2026 figures, replacing the carried-forward
  FY2025 pairing used last session**:
  FY2026 FCF/NI = 2,184/3,108 = 70.27%   (down sharply from the FY2025-based 101.5% used 2026-07-01)
  FCFQuality_Score = clamp(((0.7027 − 0.40)/0.60)×100) = 50.44

  Hard-disqualifier check (quality-scoring.md): FCF/NI <70% for 2+ consecutive years —
  FY2026 = 70.27% (≥70%, does not qualify as a sub-70% year); FY2025 = 101.5%. **Does not fire**
  (only one year even close to the threshold, and it clears it, if narrowly). FCF-positive
  3-consecutive-years (FY2024 $6,617M / FY2025 $3,268M / FY2026 $2,184M) confirmed — no disqualifier.

Quality Score = 33.58×0.25 + 53.65×0.15 + 0.0×0.20 + 100.0×0.15 + 20.0×0.15 + 50.44×0.10
              = 8.395 + 8.0475 + 0 + 15.0 + 3.0 + 5.044
              = 39.49 → 39.5
```

**⚠️ Quality Score 44.4 → 39.5 — still FAILS the 80.0+ gate, and has now declined for the first time since first computation.** No hard disqualifier fires. The decline is driven almost entirely by the FCF Quality sub-score (100.0 → 50.44) now that audited FY2026 cash-flow data replaces last session's carried-forward FY2025 figures — a real, cited fundamental datapoint (FY2026 FCF fell 33.2% YoY on higher CapEx and softer operating cash flow), not a methodology change.

**Phase 04 Quality Watch escalation reaffirmed and strengthened.** This is the second consecutive rescore showing NKE below the gate, now trending down rather than merely failing statically, alongside fresh third-party evidence (JPMorgan, §2/§4) of continuing, quantified moat erosion in China. The formal Upgrade 4 Turnaround Sub-Gate review + `override-log.md` entry recommended in the 2026-07-01 session remains open and is now overdue across **four** consecutive rescores (2026-06-07, 2026-06-20, 2026-07-01, 2026-09-11).

## 7. Phase 02 Valuation Score

```
FCF Yield (40% weight): FCF (FY2026 audited) $2,184M ÷ Market cap $54,219.4M = 4.028%
  FCF_Score = clamp(100×(1 − 4.028/10), 0, 100) = 59.72
  contribution = 59.72 × 0.40 = 23.888

EV/EBIT (25% + 15% PEG-redistributed = 40% weight): EV $53,134.4M ÷ EBIT (FY2026) $3,850M = 13.80×
  EV/EBIT_Score = clamp((13.80 − 12)/23 × 100, 0, 100) = 7.836
  contribution = 7.836 × 0.40 = 3.134

Forward PE (20% weight): $36.61 ÷ FY2027 consensus EPS $1.71 = 21.41×
  5yr range (carried forward, §2): low 18.2×, high 40.3×, avg 29.5×
  FwdPE_Score = clamp((21.41 − 18.2)/(40.3 − 18.2) × 100, 0, 100) = 14.52
  Historical PE Modifier (Upgrade 2): dev vs 5yr avg = (21.41 − 29.5)/29.5 = −27.4% → >20% below
    → −10 modifier, applied (sub-score not at floor this time): 14.52 − 10 = 4.52
  contribution = 4.52 × 0.20 = 0.904

PEG (15% weight): n/a — NKE is not a Fast Grower → redistributed to EV/EBIT above.

Raw weighted = 23.888 + 3.134 + 0.904 = 27.926
+ Rate Gate Step 1 (EY spread FAIL)   +5
+ Rate Gate Step 2 (Rate Regime)      +5
= 37.926  (before Upside/Downside Modifier)
```

## 8. Upside/Downside Modifier — full calc

**Scenario fair values — updated this session** (unlike 2026-07-01, which carried these forward unchanged: the ~28% consensus EPS cut and the JPMorgan China marketplace-reset disclosure are real, cited new information materially affecting the base and bear cases, so re-deriving rather than carrying forward is the correct call here):

| Scenario | FV | Assumption |
|---|---|---|
| Bull (25%) | $57 | Turnaround still executes but off a lower earnings base: normalized EPS ~$1.91 2yr out (scaled down from the 2026-07-01 session's $2.60–2.70 assumption in proportion to the ~28% Street consensus cut) × ~27× exit multiple (unchanged assumption — a partial re-rate toward, not to, the historical 29.5× average) |
| Base (50%) | $38 | FY2027 consensus EPS $1.71 × a below-average ~22× exit multiple (unchanged multiple assumption from 2026-07-01, reflecting ongoing China/competitive headwinds) ≈ $37.62 |
| Bear (25%) | $33 | JPMorgan's own explicit FY2027 EPS estimate ($1.55) × their own stated ~21× multiple ≈ $32.55 — a real, cited bear case, not a derived scaling, and coincidentally close to the 2026-07-01 session's $33 bear FV |

```
PW Fair Value = 0.25×57 + 0.50×38 + 0.25×33 = 14.25 + 19.0 + 8.25 = $41.50
  (down from 2026-07-01's $52.25 — driven by the real consensus/JPMorgan estimate cuts, not price action)
Gap Upside %  = (41.50 ÷ 36.61) − 1 = +13.36%
Catalyst window = 2.0 yr  (Rule 10 default retained — the previously-named "Q2 FY2027 margin
   inflection" catalyst is now credibly in doubt per JPMorgan's own framing ("Win Now" plan "may be
   a long game," headwinds running "well into fiscal 2028"), so no better/narrower positive-catalyst
   date is documented this session; kept at 2yr rather than shortened or invented)
Annualized gap = 13.36% ÷ 2.0 = +6.68%

Intrinsic growth = +2.0%/yr  (lowered from the 2026-07-01 session's +4.0%/yr — the FY2026→FY2027
   consensus comparison now shows an outright EPS *decline* ($2.10 → $1.71, −18.6%), so continuing
   to assume +4%/yr underlying growth through the trough is no longer the conservative read; +2.0%/yr
   reflects a modest longer-run recovery assumption beyond the FY2027 trough, disclosed as judgment)
Shareholder yield = dividend $1.63/$36.61 = 4.45% + net buyback 0.44% (FY2026 figure, unchanged,
   no newer data) = 4.89%

E = 6.68 + 2.0 + 4.89 = +13.57%   (expected annual return, down from 2026-07-01's +24.18%)
```

**Map E → M** (hurdle H = 10%, E ≥ H branch):
```
M = −15 × clamp((13.57 − 10)/15, 0, 1) = −15 × clamp(0.238, 0, 1) = −3.57
```
**Catalyst guardrail:** no credible positive catalyst is confidently identifiable within 18–24 months this session (per JPMorgan's own multi-year framing) — the guardrail's −5 upside cap is checked but does not bind (M = −3.57 is already less negative than −5).

## 9. Final valuation score + Composite Score

```
FINAL VALUATION SCORE = 37.926 (raw + rate gate) + (−3.57) (Upside/Downside) = 34.356 → 34.4
```

| | Value |
|---|---|
| Raw weighted | 27.926 |
| Rate Gate (Step 1 + Step 2) | +10 |
| Upside/Downside Modifier | **−3.57** (E = +13.57%, down from +24.18%) |
| **FINAL VALUATION SCORE** | **34.4** (up from 13.9 — got more expensive on a forward-earnings basis despite a lower share price, because consensus EPS fell faster than price) |
| Prior valuation score | 13.9 |
| **Quality Score** | **39.5 (down from 44.4, FAILS 80.0+ gate)** |

```
Composite Score = 0.50 × (100 − 39.5) + 0.50 × 34.4 = 0.50×60.5 + 0.50×34.4 = 30.25 + 17.2 = 47.45
  → exactly on a ".X5" boundary → round UP (conservative) → 47.5
```

**Composite Score = 47.5** (up from 34.8 — moved toward the less-attractive end within the same nominal 30.0–49.9 band). **Not adopted as an actionable BUY signal** — Quality Score fails the 80.0+ gate by a wide margin (39.5), so per this framework's rule, Composite Score is reference-only context, not a green light. See §10.

## 10. Action recommendation — HOLD existing, DO NOT ADD (unchanged conclusion, on worse underlying evidence)

**(a) Quality Gate fails, and is now trending the wrong way.** 39.5 vs. 80.0 required, down from 44.4 last session — Composite Score is reference-only per the framework's rule that a company must clear the Quality gate to reach an actionable Composite Score.

**(b) Order-setup gate still fails on its own terms**, using the updated (lower) PW Fair Value. Treated as Turnaround (Rule 8/Upgrade 4):

| Field | Value |
|---|---|
| Blended Fair Value (PW) | $41.50 (down from $52.25) |
| Margin of Safety (turnaround) | 35% |
| **Buy price (limit)** | **$26.98** (down from $33.96 — PW FV fell) |
| Primary sell target | $41.50 |
| Bull-case trim target | $57 |
| Stop loss (buy × 0.70) | $18.89 |
| **R/R at buy price** | (41.50−26.98)/(26.98−18.89) = **1.80:1 — still below the 2:1 minimum** |
| R/R at live $36.61 | (41.50−36.61)/(36.61−18.89) = **0.28:1** |

Live price ($36.61) remains well above the disciplined buy price ($26.98). **No order placed.**

**(c) Quality Watch escalation strengthens further.** Second consecutive rescore with Quality Score below the gate, now moving down (not just failing statically) on a real cash-flow-quality deterioration (FCF/NI 101.5%→70.3%), compounded by fresh, cited third-party evidence (JPMorgan's China marketplace-reset disclosure) of continuing moat erosion. This still does not meet the Full Exit bar (Phase 06 requires *sustained* deterioration and the category itself is still growing) but the case for the still-open Upgrade 4 Turnaround Sub-Gate review + `override-log.md` entry — now overdue across four consecutive rescores — has gotten materially stronger, not weaker.

**Net: HOLD the existing ~1.24%-weight position. Do NOT add.** Independently blocked by the Quality gate, the R/R order-setup discipline, and now a worsening (not just static) quality trend. The nominally cheaper-looking valuation math (Composite 47.5, still technically inside the "Buy" band number range) reflects a real narrowing of expected return (E fell from +24.18% to +13.57%) driven by the same consensus-EPS-cut evidence — not a signal to act on.

## 11. Next review trigger

- **Q1 FY2027 earnings (2026-09-29)** — 18 days out; will supply the first fresh income-statement data point since 2026-06-30, and will be the first real test of whether the China marketplace-reset headwind JPMorgan flagged is starting to show up in reported numbers.
- **A formal Upgrade 4 Turnaround Sub-Gate review + `override-log.md` entry** — recommended explicitly, now overdue across four consecutive rescores.
- **Rule 9 triggers (standing):** guidance revision, the China marketplace reset's actual January 2027 start (confirm vs. delay), a >15% unexplained price move, or a management change.

## 12. Glossary

- **8-K (Form 8-K) / 10-K (Form 10-K):** a US company's "current report" disclosing a material event between regular filings / its full annual report with audited financials.
- **CAGR:** Compound Annual Growth Rate.
- **CapEx:** Capital Expenditure.
- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50.
- **D&A:** Depreciation & Amortization.
- **EBIT / EBITDA:** operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **EPS:** Earnings Per Share.
- **EV / EV/EBIT:** Enterprise Value (market cap + debt − cash) / EV divided by EBIT, a valuation multiple.
- **EY (Earnings Yield):** 1 ÷ Forward PE, compared against the 10-Year Treasury yield.
- **FCF / FCF Yield / FCF/NI conversion ratio:** Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality).
- **Forward PE:** price ÷ next year's expected EPS.
- **FV / PW Fair Value:** Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear).
- **Hard disqualifier:** one of three Quality Score conditions that fails a company regardless of weighted score.
- **Hurdle rate:** the minimum acceptable annual return (10% in this framework).
- **IRR:** Internal Rate of Return.
- **Moat:** a durable competitive advantage protecting a business's profits.
- **MoS (Margin of Safety):** the discount below fair value demanded before buying.
- **Net Debt/EBITDA:** a leverage ratio; this framework's primary balance-sheet-risk gate.
- **NOPAT:** Net Operating Profit After Tax — EBIT × (1 − effective tax rate).
- **PE (Price-to-Earnings) ratio:** price ÷ earnings.
- **pp (percentage points):** a direct difference between two percentages.
- **PT (Price Target):** an analyst's forecast of where a stock's price will be at a future date.
- **Quality Score:** this framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02.
- **Rate Environment Gate / Rate Regime Modifier:** the pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss); this framework requires ≥2:1.
- **ROIC:** Return on Invested Capital — NOPAT ÷ Invested Capital.
- **Shareholder yield:** dividend yield plus net buyback yield.
- **TTM:** Trailing Twelve Months.
- **Turnaround Sub-Gate:** the conditional path letting a company failing some quality criteria still enter as a small position if it passes 5 specific tests.
- **Underweight / Overweight (analyst rating):** sell-side shorthand for a stock expected to underperform (Underweight) or outperform (Overweight) its sector/benchmark.
- **Upside/Downside Modifier:** an additive ±15 valuation-score adjustment based on expected annual return.

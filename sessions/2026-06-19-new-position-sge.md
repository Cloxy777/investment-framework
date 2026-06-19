# NEW POSITION — The Sage Group plc (LON:SGE) — 2026-06-19

> **⚠️ CORRECTED RE-RUN (same day).** The original version of this session used a live price (GBX 879.80) sourced via WebSearch aggregation that turned out to be **stale by roughly 3–4 weeks**, not a genuine 19 Jun 2026 intraday quote (see §1). This environment subsequently gained full network access, allowing direct `yfinance` verification — which is now used throughout per Rule 0. The error changed the Rate Gate outcome, the Phase 02 score, the blended Fair Value, and the position size (though **not** the final BUY/Enter-Now action category). This file **replaces** the original in full; the original numbers are not preserved here but remain visible in git history (commit `4ea30f6`) and in PR #29.

**Task type:** NEW POSITION (corrected re-run)
**Date:** 19 Jun 2026
**10Y US Treasury Yield:** 4.45% (unchanged from same-day original research)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current SGE portfolio weight:** 0% — not currently held (confirmed against [holdings.md](../portfolio/holdings.md))
**Sector:** UK/Global Enterprise Software — SMB/mid-market accounting, ERP, and payroll SaaS (Sage Intacct, Sage 50/200/300, Sage X3, Sage Business Cloud)
**Currency:** All calculations in GBP/pence (GBX). The Rate Environment Gate benchmarks against the **US** 10Y Treasury per framework convention; the DCF WACC uses the **UK** 10Y Gilt as risk-free rate for currency-consistent valuation of GBP cash flows.

---

## 0. What Changed and Why (read this first)

**The error:** §1 of the original session used GBX 879.80 as the "live price," sourced from WebSearch aggregation of third-party finance sites. Direct `yfinance` price history pulled in this re-run shows SGE closed at **878.72p on 22 May 2026** — i.e., the WebSearch figure was a real price, just one that was **~4 weeks stale**, not the 19 Jun 2026 quote it was presented as.

| Date | Close (yfinance) |
|---|---|
| 2026-05-22 | 878.72p |
| 2026-06-01 | 907.51p |
| 2026-06-10 | 850.20p |
| 2026-06-17 | 832.60p |
| 2026-06-18 | 802.80p |
| **2026-06-19 (today, live)** | **812.60p** |

**The fix:** this re-run uses `yfinance`'s `Ticker('SGE.L').info` snapshot (price, 52-week range, shares outstanding, beta, EPS estimates) and `.history()` (the table above) as the primary source, falling back to the original session's same-day WebSearch-derived figures only for inputs that are not time-sensitive and were not implicated in the price error (FY2025 income-statement figures, WACC/macro inputs, qualitative facts).

**A second, related correction:** the original session's Forward PE (16.87×) and this re-run both needed to resolve which yfinance EPS-estimate period is "Forward PE." `yfinance`'s own pre-computed `forwardPE` field (and the `info.forwardPE` value for every peer checked) divides price by the **`+1y`** consensus EPS estimate — i.e., the fiscal year *after* next, not next fiscal year. Using that field directly for Sage gives a misleadingly low 14.12×. The correct "Forward PE" (next FY, the `0y` estimate row) is **16.25×**. This re-run uses the `0y` basis consistently for **both Sage and all five peer comparables** (see §2 and §8) — the original session's peer Forward PE figures (WebSearch-sourced) turn out to already be on a roughly consistent next-FY basis, so this mostly self-corrects, but it is now verified directly rather than assumed.

**Net effect on the recommendation:**

| | Original (stale price) | Corrected |
|---|---|---|
| Live price | 879.80p | **812.60p** |
| Rate Gate Step 1 | FAIL → +5 | **PASS → 0** |
| Rate Modifier total | +10 | **+5** |
| Phase 02 Score | 29.8 | **21.1** |
| Blended FV | 1,153.2p | **1,320.8p** |
| Buy ceiling (20% MoS) | 922.6p | **1,056.6p** |
| Standard-band stop clears 2:1 R/R? | No (required artificial tightening to 743.1p) | **Yes (629.76p, standard 22.5% band, R/R 2.78:1)** |
| Position size | 364 sh / 8.0% / $4,288.7 | **333 sh / 6.68% / $3,581.9** |
| Action | ENTER NOW, Very Cheap | **ENTER NOW, Very Cheap (unchanged)** |

The investment conclusion is unchanged — Sage still screens as a clear Enter-Now Very Cheap name — but the score is now meaningfully cheaper (21.1 vs 29.8) and the position is smaller and uses a less aggressive (non-tightened) stop, because the corrected, lower price improves the FCF yield and EV/EBIT sub-scores while also flipping the Rate Gate's Step 1 spread test to a pass.

---

## 1. Live Price (Rule 0 — corrected via direct `yfinance` verification)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **GBX 812.60** (£8.126) | `yfinance` `Ticker('SGE.L').info['currentPrice']`, cross-checked against `regularMarketPrice` (812.60) and `previousClose` (802.80, 18 Jun 2026) — internally consistent day-over-day move |
| 52-week range | GBX 771.66 – 1,335.00 | `yfinance` (`fiftyTwoWeekLow`/`fiftyTwoWeekHigh`) — unchanged from original, this figure was not implicated in the price error |
| Analyst consensus PT (12-month) | Mean **1,092.32p**, median 1,100p, range 850–1,334p, 19 analysts; rating mix 4 Strong Buy / 10 Buy / 4 Hold / 0 Sell / 1 Strong Sell | `yfinance` `analyst_price_targets` + `recommendations_summary` — supersedes the original's WebSearch-aggregated "~1,157p avg" figure |
| Shares outstanding | **900,968,874** (≈901.0M) | `yfinance` `sharesOutstanding` — supersedes the original's WebSearch figure of 907.73M |
| Market cap (computed) | **£7,321.3M** (= 900,968,874 × £8.126) | Computed from verified live price × shares outstanding; matches `yfinance`'s own `marketCap` field (£7,321,272,832) to within rounding |
| Beta (5yr) | **0.293** | `yfinance` `info['beta']` — consistent with the original's well-corroborated 0.30 reading; still the basis for flagging Sage as an outlier-low-beta name (see §8) |
| GBP/USD | 1.32371 | `yfinance` `Ticker('GBPUSD=X')` |

---

## 2. Data Gathered (Phase 01 + Phase 02 Inputs) & Gaps Flagged

### FY2025 results (year ended 30 Sep 2025) — unchanged from original, not price-related

These are fixed annual-report figures, not time-sensitive market data, and were not implicated in the price error. Carried forward from the original session's WebSearch-sourced FY2025 results:

| Metric | FY2025 | FY2024 | YoY |
|---|---|---|---|
| Total revenue | £2,513M | — | — |
| Underlying EBITDA | £694M (margin 27.6%) | £605M | +15% |
| **Underlying operating profit (EBIT)** | **£600M** | — | +17% |
| Underlying PBT | £555M | £486M | +14.2% |
| **Underlying PAT** | **£423M** | ≈£371.1M | +14% |
| Statutory net income | £369M | — | — |
| Underlying basic EPS | 43.2p | 36.7p | **+17.7%** |
| **Free cash flow** (underlying) | **£517M** | £524M | −1.3% |
| Gross margin | 92.80% | — | — |
| ROIC | 22.29% | — | — |

**Note on FCF basis:** `yfinance`'s own cash-flow-statement-derived FCF for FY2025 (Operating Cash Flow £528M − CapEx £59M) computes to **£469M**, not £517M. The £517M figure is Sage's own disclosed non-GAAP "free cash flow" metric (WebSearch-sourced from the FY2025 results announcement), which nets out items Sage's own definition excludes. Per Rule 6 ("value the underlying business, not the accounting statements"), the company-disclosed underlying figure is retained as primary, consistent with using underlying PAT and underlying EBIT elsewhere — this is real, sourced, disclosed company data, not an estimate. Flagged transparently as a methodological note, same treatment as the original session's underlying-vs-statutory PAT distinction.

### Net debt — updated to the most recent available balance sheet (H1 FY26)

| Period | Net Debt | Source |
|---|---|---|
| FY2025 year-end (30 Sep 2025) | £1,086M (quarterly BS) / £1,189M (as separately disclosed) | original session basis |
| **H1 FY26 (31 Mar 2026, most recent)** | **£1,393M** | `yfinance` `quarterly_balance_sheet` |

**This re-run uses the more current £1,393M H1 FY26 net debt figure** for the EV bridge and DCF equity bridge, consistent with also using a current (19 Jun 2026) price and share count rather than mixing a live price with an 8-month-stale balance sheet snapshot. Net debt/EBITDA on this current basis = £1,393M / £694M (FY2025 underlying EBITDA, latest annual figure available) = **2.007× ≈ 2.0×** — this independently matches Sage's own reported "net debt/EBITDA ~2.0x" disclosure in the H1 FY26 results (cross-validated via WebSearch), giving high confidence in both figures despite blending a yfinance balance-sheet figure with a company-disclosed EBITDA figure.

### Revenue history (3yr CAGR) — unchanged

```
3yr CAGR = (2,513 / 1,950)^(1/3) − 1 = 8.83%   (FY2022 £1,950M → FY2025 £2,513M)
```

### Underlying EPS history (Fast Grower / PEG test) — unchanged

| Year | Underlying basic EPS | YoY growth | >15%? |
|---|---|---|---|
| FY2024 | 36.7p | +13.6% | ❌ No |
| FY2025 | 43.2p | +17.7% | ✅ Yes |

Only 1 of the last 2 years clears 15% — **not a Fast Grower**; PEG's 15% weight redistributes to EV/EBIT (40% total), same conclusion as the original session.

### Valuation history — unchanged (historical, not price-dependent)

| Metric | Value |
|---|---|
| 10yr PE low | 19.42× |
| 10yr PE high | 62.03× |
| 10yr PE average | 28.92× |

### Forward PE — recomputed on a verified, consistent basis

```
yfinance eps_trend (Ticker('SGE.L').eps_trend):
  0y  (FY2026E, next fiscal year) EPS estimate = 49.991p   <- correct "Forward PE" basis
  +1y (FY2027E, fiscal year after next) EPS estimate = 57.55p  <- what yfinance's raw forwardPE field actually uses

Forward PE = 812.60 / 49.991 = 16.25×
(yfinance's own `forwardPE` field gives 14.12× = 812.60/57.55 — this is the +1y-basis figure, NOT used)
```

This same `0y`-vs-`+1y` distinction was checked and applied consistently across all five peer comparables in §8.

### Net margin — primary basis and the judgment call (unchanged from original)

| Basis | Net income | Net margin | vs >15% threshold |
|---|---|---|---|
| Underlying PAT (primary, used) | £423M | **16.83%** | ✅ PASS |
| Statutory net income (cross-check) | £369M | 14.68% | ❌ Would FAIL |

Same determination as the original session: underlying PAT used as primary per Rule 6, statutory shown as transparency cross-check.

### WACC inputs — carried forward (same calendar day, not price-related)

| Input | Value | Source |
|---|---|---|
| Risk-free rate (UK 10Y Gilt) | 4.82% (18 Jun 2026) | WebSearch, same-day original research |
| Sage's own beta (5yr) | 0.293 (yfinance, re-verified) / 0.30 (original WebSearch cluster) | Consistent — unusually low for software |
| Sector-average beta (used operatively, see §8) | 0.92 | WebSearch, same-day original research |
| Equity Risk Premium | 5.0% (standard assumption) | Standard convention |
| Cost of debt (pre-tax) | 5.67% | WebSearch (Alphaspread) |
| Capital structure | Equity 84.39% / Debt 15.61% | WebSearch (Alphaspread) |
| Credit rating | S&P BBB+, stable outlook | WebSearch |

### Peer comparables (Rule 5) — now with real EV/EBIT for every peer

The original session flagged EV/EBIT as unavailable for all 5 peers and substituted EV/EBITDA. This re-run pulls real EV/EBIT directly via `yfinance` (`enterpriseValue` ÷ `financials.loc['EBIT']`), closing that data gap:

| Company | EV/EBIT | Forward PE (0y basis) |
|---|---|---|
| Intuit (INTU) | 15.15× | 11.20× |
| Workday (WDAY) | 27.39× | 10.90× |
| SAP (SAP) | 17.72× | 18.60× |
| Xero (XRO.AX) | 29.60× | 52.64× |
| Oracle (ORCL) | 37.56× | 22.89× |
| **Median** | **27.39× (Workday)** | **18.60× (SAP)** |

**Flagged explicitly:** the EV/EBIT median (27.39×) is set by **Workday**, whose multiple reflects market expectations of substantially higher forward growth than Sage's — Workday's revenue (~$8.5B) is also >2× Sage's (£2,513M ≈ $3.3B), breaching Rule 5's ±50% revenue-scale guideline (a mismatch that pre-dates this re-run; it was already present in the original peer set, just less consequential when EV/EBITDA was the operative multiple). This is shown transparently rather than trimmed, consistent with the original session's no-outlier-trimming precedent — but it is the single largest driver of this re-run's higher comparables-based fair value (see §8), and is flagged as the weakest link in the valuation chain.

### Data Gaps flagged

1. **FCF basis** (company-disclosed underlying £517M vs yfinance-derived statutory £469M) — see above; underlying used as primary per Rule 6.
2. **Net debt timing mismatch** — EV/EBIT and DCF equity bridge use H1 FY26 net debt (£1,393M) against FY2025 full-year EBIT/EBITDA (latest annual figures available); a true TTM EBIT figure was not sourced and is not estimated.
3. **Peer revenue-scale mismatch** — Workday, SAP, Oracle, Intuit all exceed Rule 5's ±50% revenue-scale band relative to Sage; only Xero is roughly comparable in scale. Flagged as a comparables-quality caveat, not resolved by trimming.
4. **Net debt/EBITDA at 2.0×** sits exactly at strategy.md's <2× Phase 01 threshold (borderline) while passing valuation-scoring.md's <2.5× comfortably — third Phase 01 judgment call, see §3.

---

## 3. Phase 01 — Quality Gate

| Check | Sage Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 92.80% | >40% | ✅ PASS |
| **Net margin** | 16.83% (underlying PAT basis) | >15% (strategy.md) | ✅ PASS — judgment call: statutory basis (14.68%) would fail |
| ROIC | 22.29% | >15% | ✅ PASS |
| **Revenue CAGR 3yr** | 8.83% | >10% (strategy.md) / >8% (valuation-scoring.md) | ✅ PASS (valuation-scoring.md) / ⚠️ borderline-FAIL (strategy.md) — judgment call, same resolution as original (accelerating organic growth trend) |
| **Net debt/EBITDA** | **2.0×** (current, H1 FY26 net debt ÷ FY25 underlying EBITDA) | <2× (strategy.md) / <2.5× (valuation-scoring.md) | ✅ PASS (valuation-scoring.md) / ⚠️ borderline (strategy.md, exactly at threshold) — **new third judgment call**, see below |
| FCF positive 3+ consecutive years | Yes | required | ✅ PASS |
| FCF/NI conversion ratio | FY25: 517/423 = 122.2% / FY24: 524/371.1 = 141.2% | >70% | ✅ PASS, comfortably |
| Share issuance pattern | Net buyback (£200M extension, H1 FY26) | non-dilutive required | ✅ PASS |

### Net debt/EBITDA judgment call (new in this re-run)

The trend (1.2× FY24 → 1.7× FY25 → **2.0× H1 FY26**) is now rising faster than the original session flagged, and sits exactly at strategy.md's <2× Phase 01 ceiling rather than comfortably below it. **Determination: PASS**, on the basis that (a) 2.0× still comfortably clears valuation-scoring.md's looser <2.5× pre-screen, (b) 2.0× sits at — not above — the top of Sage's own stated 1–2× medium-term target range (i.e. within management's own guardrail, not a breach of it), and (c) interest coverage and credit rating (S&P BBB+ stable) are unchanged and show no separate sign of balance-sheet stress. This is flagged as a **tightening trend to monitor** (Phase 04), not a gate failure — but it is now closer to a real constraint than the original session's 1.7× reading suggested, and removes any margin for further leverage increases without re-triggering a gate review.

**Gate result: PASS — 8/8 metrics pass, with 3 explicitly flagged judgment calls (net margin basis; revenue CAGR threshold; net debt/EBITDA now at the strategy.md ceiling). Proceeding to Rate Environment Gate and Phase 02.**

---

## 4. Fast Grower (Upgrade 3 — PEG) Determination

Unchanged from original — FY2024 EPS growth (+13.6%) breaks the "3 consecutive years >15%" chain despite FY2025's +17.7%. **Not a Fast Grower.** PEG's 15% weight redistributes to EV/EBIT (40% total).

---

## 5. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**

```
Forward PE = 16.25×
EY     = 1 ÷ 16.25 = 6.152%
Spread = EY − 10Y Treasury = 6.152% − 4.45% = +1.702%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+1.702% clears the threshold) → **0 additive** (Step 1).

This is the headline change from the original session, which used the stale 879.80p price → Forward PE 16.87× → spread +1.478% → FAIL → +5. The corrected, lower price (812.60p) produces a *lower* Forward PE (cheaper) and therefore a *wider* earnings-yield spread over the Treasury, flipping this step to a pass.

**Step 2 — Rate Regime Modifier**
10Y = 4.45% → "3.5–5%" bracket → **+5** (unchanged)

**Total Rate Modifier for Sage = 0 (Step 1) + 5 (Step 2) = +5**

---

## 6. Phase 02 — Full Score Calculation

**FCF Yield — 40% weight**

```
FCF Yield = FCF / Market Cap = £517M / £7,321.3M = 7.062%

FCF_Score = clamp(100 × (1 − 7.062/10), 0, 100) = clamp(100 × 0.2938, 0, 100) = 29.38
```
→ Contribution: 29.38 × 0.40 = **11.75**

**EV/EBIT — 40% weight (PEG not applicable, redistributed from 25%)**

```
Market Cap = £7,321.3M
Net Debt   = £1,393M  (H1 FY26, current basis — see §2)
EV         = £7,321.3M + £1,393M = £8,714.3M

EV/EBIT = £8,714.3M / £600M (FY2025 underlying EBIT) = 14.52×

EV/EBIT_Score = clamp((14.52 − 12) / 23 × 100, 0, 100) = clamp(10.97, 0, 100) = 10.97
```
→ Contribution: 10.97 × 0.40 = **4.39**

**Forward PE (PRIMARY formula — 10yr low/high range available) — 20% weight**

```
Forward PE   = 16.25×
10yr Low PE  = 19.42×
10yr High PE = 62.03×

FwdPE_Score (raw) = clamp((16.25 − 19.42) / (62.03 − 19.42) × 100, 0, 100) = clamp(−7.43, 0, 100) = 0.0
```

Forward PE again sits below the 10-year low — cheapest possible reading on this dimension.

**Historical PE Modifier (Upgrade 2)**

```
Deviation from 10yr avg = (16.25 − 28.92) / 28.92 = −43.79%
```
>20% below average → modifier = **−10** (no further effect; already at the 0.0 floor).

```
FwdPE_Score (adjusted) = clamp(0.0 − 10, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.00**

**PEG — not applicable (redistributed to EV/EBIT)**

---

### Final Score

```
Raw weighted score = (29.38 × 0.40) + (10.97 × 0.40) + (0.0 × 0.20)
                    = 11.75 + 4.39 + 0.00
                    = 16.14 (precise: 16.143)

+ Rate Regime Modifier (0 + 5) = 16.143 + 5 = 21.143
```

Boundary rule: 21.143 → nearest 0.1 → **Final Score = 21.1**

---

## 7. Final Score & Action

# Final Score: 21.1 → Action Table band: 0.0–29.9 (Very Cheap) → BUY — Full position 6–8% of portfolio

Sage now scores **well inside** the Very Cheap band (21.1, vs the original's borderline 29.8 at the very top edge) — the corrected, lower price improves all three contributing sub-scores simultaneously: FCF yield is higher (7.06% vs 6.47%), EV/EBIT is lower (14.52× vs 15.29×), and the Rate Gate's Step 1 penalty disappears entirely. This is a textbook illustration of why Rule 0 exists: a single stale price input propagated into every downstream calculation, each time making the stock look more expensive and the entry more rate-sensitive than it actually was.

### Sanity check (unchanged reasoning from the original, still applies)

The qualitative case for why a 22.29%-ROIC, 92.8%-gross-margin compounder trades at a Forward PE below its own 10-year low is unchanged: Sage's 10-year PE history spans both a 2020–2023 SaaS-multiple-expansion era and a 2024–2026 broad software de-rating, and today's multiple sits in territory the stock hasn't traded at in a decade despite underlying operating profit and EPS both growing mid-to-high-teens% in the latest year. The convergence of all three independent sub-score signals pointing "cheap" still holds, and is now even stronger at the corrected price.

---

## 8. Fair Value & Order Setup

### Step 1 — Fair Value (Blended)

**Method A: DCF (3 scenarios, Rule 2/7)**

**WACC — same beta-sensitivity resolution as the original.** Sage's own re-verified beta (0.293, essentially unchanged from the original's 0.30) still produces a WACC (~6%) low enough to fail Rule 4's terminal-value-weight sanity check in the Bull scenario. **WACC is again anchored to the sector-average beta (0.92)**, which passes all Rule 4 checks:

```
Cost of Equity (sector-beta) = 4.82% + 0.92×5.0% = 9.42%
WACC (sector-beta) = 0.8439×9.42% + 0.1561×4.25% = 8.6%
```

Base FCF = £517M (FY2025 underlying). 3-stage DCF: Stage 1 (yrs 1–5) explicit growth; Stage 2 (yrs 6–10) growth fades linearly from the Stage-1 rate to the 2.5% terminal rate; Stage 3 Gordon-growth terminal value off year-10 FCF.

| Scenario | WACC | Yrs 1–5 growth | PV(FCF Yrs 1–10) | PV(Terminal Value) | EV | TV weight |
|---|---|---|---|---|---|---|
| Bear | 9.6% | +9% | £4,820.5M | £5,883.9M | **£10,704.4M** | 55.0% |
| Base | 8.6% | +10% | £5,288.2M | £8,005.2M | **£13,293.4M** | 60.2% |
| Bull | 7.6% | +11% | £5,813.4M | £11,195.8M | **£17,009.3M** | 65.8% |

All three pass the <75% terminal-value-weight sanity check.

```
PW DCF EV = 0.25×17,009.3 + 0.50×13,293.4 + 0.25×10,704.4 = 13,575.1M

DCF Equity Value = £13,575.1M − Net Debt £1,393M (current, H1 FY26) = £12,182.1M
DCF FV/share = £12,182.1M / 900.968874M shares = £13.521 = 1,352.1p
```

Even the Bear-case EV (£10,704.4M) sits above the current EV (£8,714.3M) — the DCF supports undervaluation even under conservative assumptions, same conclusion as the original session.

**Method B: Comparable Multiples — now using real EV/EBIT (closing the original's flagged data gap)**

```
EV/EBIT reversion: median peer EV/EBIT (27.39×, Workday) × Sage underlying EBIT (£600M)
                  = implied EV £16,436.8M − Net Debt £1,393M = Equity £15,043.8M
                  ÷ 900.968874M shares = 1,669.7p

Forward PE reversion: median peer Forward PE (18.60×, SAP, 0y basis) × Sage's own Forward EPS (49.991p)
                     = 930.0p

Multiples avg = (1,669.7p + 930.0p) / 2 = 1,299.9p
```

```
Blended FV = 40% × DCF FV/share + 60% × Multiples avg
           = 0.40 × 1,352.1p + 0.60 × 1,299.9p
           = 540.8p + 779.9p
           = 1,320.8p
```

**Cross-check vs external estimates — flagged divergence.** Blended FV (1,320.8p) sits **+20.9% above** the `yfinance`-sourced analyst consensus mean (1,092.3p) — a meaningfully wider gap than the original session's near-exact match to consensus (~1,157p vs FV 1,153.2p). The gap traces almost entirely to the EV/EBIT reversion sub-component (1,669.7p), which is itself set by Workday's 27.39× multiple — a peer that, as flagged in §2, trades on a richer growth premium than Sage and exceeds Rule 5's revenue-scale guideline relative to Sage. **This is shown transparently rather than adjusted away**, consistent with this framework's no-outlier-trimming precedent, but it should be read as the least robust number in this session: the DCF (1,352.1p) and the Forward-PE-reversion figure (930.0p) bracket a more moderate range, and the EV/EBIT reversion figure pulls the blend upward on the back of a single, scale-mismatched peer's multiple.

---

### Step 2 — Buy Price & R/R Gate

Score 21.1 falls in the **0.0–29.9 (Very Cheap)** band → MoS 15–20%; using the conservative end (20%, per Rule 8's "wide-moat, proven compounder" — ROIC 22.29%), consistent with the original session's choice:

```
Buy Price ceiling = Blended FV × (1 − 0.20) = 1,320.8p × 0.80 = 1,056.6p
```

**Current price (812.60p) is well BELOW the Buy Price ceiling (1,056.6p)** — implied MoS at current price = 1 − (812.60/1,320.8) = **38.5%**, far exceeding the 20% requirement. Per Step 2: Score 0.0–29.9 → "Stock at or below buy price → **Enter now**."

**Step 6 (Risk/Reward)**

```
Stop Loss (standard 20–25% band, midpoint 22.5%) = 812.60p × (1 − 0.225) = 629.76p

R/R = (Blended FV − Entry) / (Entry − Stop Loss)
    = (1,320.8p − 812.60p) / (812.60p − 629.76p)
    = 508.2p / 182.84p
    = 2.78 : 1
```

**2.78:1 clears the 2:1 minimum using the standard stop band — no tightening required.** This is the second material change from the original session, which needed an artificially tightened stop (743.1p, justified by Sage's low beta) to force the R/R math to clear 2:1 from a 1.38:1 starting point. At the corrected, lower entry price the standard band works on its own:

| Stop band | Stop price | R/R |
|---|---|---|
| 20% (tight end) | 650.08p | 3.13:1 |
| 22.5% (midpoint, used) | 629.76p | **2.78:1** |
| 25% (loose end) | 609.45p | 2.50:1 |

All three points in the standard band clear 2:1 — the midpoint (629.76p) is used as the default, with no need for the original's lower-beta-justified exception.

---

### Step 3 — Sell Targets

```
Primary Sell Target = Blended FV = 1,320.8p
```

Bull-Case Blended FV (Bull DCF EV £17,009.3M → equity £15,616.3M → 1,733.3p/share, blended with the same Multiples avg 1,299.9p):
```
Bull Blended FV = 0.40×1,733.3p + 0.60×1,299.9p = 693.3p + 779.9p = 1,473.2p
Bull-Case Trim Target = 1,473.2p × 0.90 = 1,325.9p
```

---

### Step 4 — Position Size

```
Risk per share = Entry − Stop Loss = 812.60p − 629.76p = 182.84p = £1.8284

Max $ Risk (1.5% of $53,659.11 portfolio, Score 0.0-29.9 band) = $804.89
Converted to GBP: $804.89 / 1.32371 = £608.05

Shares (risk-based) = £608.05 / £1.8284 = 332.6 → 333 shares
Position size = 333 × £8.126 = £2,705.96 = $3,581.9 (at GBP/USD 1.32371)
```

```
% of portfolio = $3,581.9 / $53,659.11 = 6.68%
```

**Cap check (Score 0.0–29.9 → max 6-8% of portfolio):** risk-based sizing (6.68%) sits **within** the 6–8% band — no capping needed in either direction, unlike the original session where risk-based sizing (9.66%) had to be capped down to 8%. The lower price and lower implied risk-per-share now produce a position size that the risk budget supports natively, without hitting the allocation ceiling.

**Upgrade 7 (15% hard cap) check:** 6.68% is well within the 15% hard cap — no breach.

```
[x] Valuation Score:                         21.1   (Very Cheap band — 0.0-29.9, well inside)
[x] DCF Fair Value (PW, scenario-weighted):  1,352.1p
[x] Multiples-Based Fair Value:              1,299.9p
[x] Blended Fair Value:                      1,320.8p
[x] Margin of Safety %:                      20% (conservative end of 15-20% band) -> Buy Price ceiling 1,056.6p;
                                              current price (812.60p) is BELOW the ceiling (38.5% implied MoS) -> Enter now indicated
[x] BUY PRICE (entry, at current live price):812.60p
[x] PRIMARY SELL TARGET (at FV):             1,320.8p
[x] BULL-CASE TRIM TARGET:                   1,325.9p
[x] STOP LOSS (standard 22.5% midpoint):     629.76p  (22.5% max loss — standard band, no tightening needed)
[x] Risk/Reward Ratio:                       2.78 : 1  (clears the 2:1 minimum on the standard stop band)
[x] Max $ Risk (1.5%, Score 0.0-29.9 band):  $804.89 (£608.05)
[x] POSITION SIZE (shares):                  333 (risk-based sizing, within the 6-8% allocation band — no capping needed)
[x] POSITION SIZE ($):                       $3,581.9  (£2,705.96, ≈6.68% of portfolio)
[x] Upgrade 7 cap (15%) check:               6.68% well within 15% hard cap — no breach
[x] Thesis invalidation triggers:            see §9
```

---

## 9. Recommendation

# **ENTER NOW — Score 21.1 (Very Cheap, well inside the band) supports a full position (6.68% of portfolio, 333 shares, ~£2,706 / ~$3,582). Current price (812.60p) sits well below the MoS-adjusted Buy Price ceiling (1,056.6p), and Risk/Reward clears the 2:1 minimum (2.78:1) using the standard 20–25% stop band — no special-case tightening required, unlike the original (price-error-affected) version of this analysis.**

**Why this re-run materially changed the numbers but not the conclusion:**

1. **A stale price (879.80p, ~4 weeks old) propagated through every downstream calculation in the original session**, each time making Sage look slightly more expensive and the entry slightly more rate-sensitive than it actually was. The corrected price (812.60p, directly `yfinance`-verified against a 1-month price history) is materially lower, which mechanically improves the FCF yield and EV/EBIT sub-scores, flips the Rate Gate Step 1 spread test from a narrow fail to a clear pass, and removes the need for an artificially tightened stop to clear the 2:1 R/R minimum.

2. **A second, related correction**: `yfinance`'s own `forwardPE` field uses a "+1-year-out" EPS estimate, not next-fiscal-year EPS as the framework's "Forward PE" intends. This was caught and resolved by using the `0y` estimate row consistently for Sage *and* all five peer comparables, avoiding a basis mismatch in the comparables-based fair value.

3. **A new, third Phase 01 judgment call emerged**: using the more current H1 FY26 net debt (£1,393M, vs the FY2025 year-end £1,189M used originally) against FY2025 underlying EBITDA gives net debt/EBITDA of exactly 2.0× — right at strategy.md's <2× ceiling rather than comfortably below it. Resolved as a pass (still clears valuation-scoring.md's <2.5×, still within Sage's own 1–2× stated target), but flagged as a tightening trend with less room left before it would force a real gate failure.

4. **Closing the original session's EV/EBIT data gap revealed a new caveat rather than resolving cleanly**: real peer EV/EBIT data (vs the EV/EBITDA proxy used originally) pushed the comparables-based fair value up substantially, but the median multiple is set by Workday — a peer trading on a richer growth premium and outside Rule 5's revenue-scale guideline relative to Sage. This is the most judgment-laden number in the session and is flagged prominently in §8 rather than smoothed over; it is also the reason this re-run's blended FV now sits noticeably *above* current analyst consensus (+20.9%) where the original's FV was almost exactly in line with consensus.

**What would change this call (unchanged from the original, per Phase 06 / Rule 9):**
- Margin compression — gross margin (92.80%) falling >3pp structurally, or ROIC (22.29%) falling toward cost of capital.
- FCF deterioration persisting for 2+ consecutive quarters beyond the FY2025 -1.3% YoY dip.
- **Net debt/EBITDA rising past 2.0×** — now a closer, more live trigger than in the original session given the rising 1.2×→1.7×→2.0× trend and the new borderline Phase 01 judgment call.
- Disruption vector materializing — credible evidence of AI-native bookkeeping agents displacing Sage's SMB interface-layer business.
- >15% unexplained move from 812.60p (Rule 9).
- FY2026 full-year results (expected ~mid-November 2026) — mandatory re-score.

**Qualitative notes** — unchanged from the original session (moat, capital allocation, growth drivers, bear case, disruption vector); see the original's §9 (preserved in git history at commit `4ea30f6`) for the full qualitative writeup, which was not affected by the price correction.

**Process note:** this session documents the analytical recommendation only. No broker order has been placed and nothing has been logged in `decisions/` or `portfolio/holdings.md` — those steps follow only once a trade is actually executed.

---

## 10. Next Review Trigger

- **FY2026 full-year results** (expected ~mid-November 2026) — mandatory re-score (Rule 9). Re-check: (a) FCF trend, (b) net debt/EBITDA trend (now at 2.0×, a live trigger if it rises further), (c) organic revenue growth vs FY26 guidance, (d) underlying EPS growth continuation.
- **If the order is actually placed** → triggers `/sync-portfolio` + `decisions/` entry + watchlist move to `in-portfolio/`.
- **>15% unexplained price move from 812.60p** (Rule 9) — immediate re-score.
- **Any credible AI-native bookkeeping/accounting disruption signal** specific to Sage's SMB base.
- **Quarterly Rate Environment Gate update** (next: ~Jul 2026).
- **Net debt/EBITDA re-check at next results** — now at the strategy.md ceiling (2.0×); a further rise without an offsetting EBITDA increase would need an explicit gate re-review, not just a monitoring note.

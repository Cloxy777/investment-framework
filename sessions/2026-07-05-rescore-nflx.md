# RESCORE — NFLX (Netflix, Inc.) — 2026-07-05

**Task type:** RESCORE (single ticker — existing holding), mode `--both`
**Date:** 05 Jul 2026 (Sunday — US markets closed; live price is the most recent completed session's close, see §1)
**10Y US Treasury Yield used:** 4.49% (TradingEconomics.com, 2 Jul 2026 — most recent print; markets observed the 4 Jul holiday on Fri 3 Jul, then the weekend)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current NFLX portfolio weight:** 1.61% (per [holdings.md](../portfolio/holdings.md), 12 shares, IBKR) — Last Score 61.2 (20 Jun 2026), Quality/Composite Score never computed (methodology added 2026-06-29, after NFLX's last rescore) — this is **NFLX's first-ever Quality Score / Composite Score computation**.
**Sector:** Communication Services — Streaming Media & Entertainment

*First-use jargon decoded in the closing Glossary (step 9 of the operating brief).*

---

## 0. Fundamental-Trigger Check Since Last Review (Rule 9)

No new earnings release, guidance revision, management change, material M&A, or balance-sheet event since the 20 Jun 2026 rescore. **Netflix's Q2 2026 earnings are scheduled for Thursday, 16 Jul 2026** (confirmed via WebSearch — stocktitan.net / ad-hoc-news.de) — **not yet released**. No Rule 9 fundamental trigger fires this session; this is the routine post-methodology-change rescore driven by the 2026-06-29 addition of the Quality Score / Composite Score, plus a routine price refresh. All FY2025/Q1-2026 fundamentals are carried forward and rolled into fresh TTM (trailing-twelve-month) figures below.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$77.65** | IBKR `get_price_history` (contract_id 15124833, NASDAQ), most recent daily bar close = **2026-07-02** (last completed session before the market observed the 4 Jul holiday on Fri 3 Jul, ahead of the weekend). Independently cross-validated via WebSearch: "Netflix (NFLX) closed at $77.65 on July 2, 2026, +4.66%" (stockanalysis.com aggregation) — exact match. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$74.19** (`is_close: true`) — this is stale by one session; it matches the **2026-07-01** close, not the most recent one (recurring issue flagged in several recent sessions, e.g. 2026-07-04 AVGO). `plprice` (mark price) returned **$77.609**, within 0.05% of the fresher $77.65 figure — used $77.65 (the cross-validated close) as the primary live price. |
| 52-week range | $70.86 (13w/26w/52w low, IBKR `misc_statistics`) – $129.50 (52w high) | IBKR — note the 52w low is a *new* trough reached recently (vs. $75.01 as of the 20 Jun session), i.e. NFLX made a fresh 52-week low since the last rescore before this session's +4.66% bounce. |
| Analyst consensus PT | ~$114.15–$114.80 (mean, 32–50 analysts, "Strong Buy"/"Buy") | WebSearch aggregation (S&P Global / stockanalysis.com-style) — essentially unchanged from the 20 Jun session's $114.15/$115.00. |
| yfinance availability | **Unreachable this session** — `YFRateLimitError` (Too Many Requests) on every retry (8 attempts with backoff), a different failure mode than the previously-documented `curl_cffi` TLS error. Fell back to IBKR (price/positions) + SEC EDGAR XBRL `companyconcept` API (fundamentals) + WebSearch (market context), per Rule 0's documented contingency chain. |

**Context:** NFLX at $77.65 sits ~40.0% below its 52-week high ($129.50) and ~9.6% above its new 52-week low ($70.86). Since the 20 Jun session ($77.38), the price is essentially flat (+0.35%) — no Rule 9 ">15% unexplained move" trigger.

---

## 2. Data Gathered — Sources & Gaps

`yfinance` was unreachable all session (rate-limited, not the usual TLS issue — flagged for whoever runs `/healthcheck` next). Fell back to **SEC EDGAR's XBRL `companyconcept` API** (`data.sec.gov`, CIK 0001065280) for all fundamentals — a primary-source filing feed, consistent with the framework's documented Rule 0 fallback (used for NKE 2026-07-01). No metric below was invented or estimated; every figure traces to a specific SEC XBRL concept/period or a cited news source.

**TTM (trailing twelve months, Q2 2025–Q1 2026) reconstruction** — computed as FY2025 (full year) − Q1 2025 (YTD) + Q1 2026 (YTD), cross-checked against a full quarterly rollforward (both methods agree to the dollar):

| Metric | TTM value | XBRL concept / derivation |
|---|---|---|
| Revenue | $46,889.99M | `Revenues` |
| Operating Income (EBIT) | $13,936.60M | `OperatingIncomeLoss` |
| Net Income (**as-reported**) | $13,373.64M | `NetIncomeLoss` |
| Operating Cash Flow (**as-reported**) | $12,650.28M | `NetCashProvidedByUsedInOperatingActivities` |
| CapEx | $756.07M | `PaymentsToAcquirePropertyPlantAndEquipment` |
| FCF (**as-reported**) = OCF − CapEx | $11,894.21M | Computed |
| Cost of Revenue | $23,900.42M | `CostOfRevenue` |
| Gross Profit / Margin | $22,989.57M / **49.03%** | Computed |
| D&A (property & equipment only, excludes content amortization) | $351.90M | `DepreciationDepletionAndAmortization` |
| Income tax expense | $2,682.27M | `IncomeTaxExpenseBenefit` |
| Total debt (Q1 2026 instant) | $14,360.52M ($999.19M ST + $13,361.33M LT) | `ShortTermBorrowings` + `LongTermDebtNoncurrent` |
| Cash + short-term investments (Q1 2026 instant) | $12,288.45M ($12,259.77M cash + $28.68M STI) | `CashAndCashEquivalentsAtCarryingValue` + `ShortTermInvestments` |
| Net debt | $2,072.07M | Computed |
| Stockholders' equity (Q1 2026 instant) | $31,126.40M | `StockholdersEquity` |
| Diluted shares (Q1 2026, post 10-for-1 split) | 4,212.794M | `CommonStockSharesOutstanding` — matches the 06-12/06-20 sessions' figure to the thousand |

**⚠️ Material one-off flagged (Rule 6 — normalize before valuing): the $2.8B Warner Bros. Discovery (WBD) merger-termination fee.** Netflix and WBD had an amended merger agreement (Jan 2026); WBD instead accepted a competing all-cash Paramount Skydance offer, triggering a **$2.8B termination fee paid to Netflix**, collected in cash in **late February 2026** (Q1 2026). Confirmed via WebSearch (Variety, Hollywood Reporter, Investing.com — consistently reported at $2.8B) and corroborated by NFLX's own XBRL data:
- The fee is booked in **"interest and other income," below the operating-income line** — `OperatingIncomeLoss` (EBIT) is **unaffected**, so EV/EBIT needs no adjustment.
- Q1 2026 Net Income ($5,282.79M) is up +82.8% YoY (vs. Q1 2025's $2,890.35M) — consistent with a ~$2.26B after-tax boost from the fee (using Q1 2026's own effective tax rate of 19.31%: pretax fee $2.8B × (1−0.1931) ≈ $2.259B after-tax).
- Q1 2026 Operating Cash Flow ($5,290.21M) jumped +89.7% YoY (vs. $2,789.20M) — a ~$2.5B increase, closely matching the $2.8B cash fee, indicating it flows through **operating** (not investing/financing) activities.
- **Normalization applied:** TTM Net Income and TTM FCF are each shown **both as-reported and normalized** (fee removed) below. Normalized NI subtracts the estimated $2.259M after-tax fee; normalized FCF/OCF subtracts the full $2.8B pretax cash amount (a disclosed simplification — the exact cash-tax timing on the fee isn't separately broken out in the filings, so the gross cash figure is removed rather than an estimated net-of-tax cash figure). **The normalized figures are used as the primary Quality/Valuation Score inputs** (Rule 6); as-reported figures are shown as a sensitivity check and — importantly — **do not change the gate outcome** (see §3).

| | As-reported (TTM) | Normalized (TTM, fee removed) |
|---|---|---|
| Net Income | $13,373.64M | $11,114.34M |
| Net Margin | 28.52% | 23.70% |
| OCF | $12,650.28M | $9,850.28M |
| FCF | $11,894.21M | $9,094.21M |
| FCF/NI conversion | 88.94% | 81.82% |

**Other carried-forward inputs** (unchanged since 20 Jun — no new Rule 9 trigger to refresh them):
- **5yr PE range** (avg 39.44×, low 19.32×, high 55.82×, n=20 quarters, `yfinance`-reconstructed 2026-06-20) — carried forward; a slow-moving statistic, and `yfinance` is unreachable this session to refresh it.
- **2026 consensus EPS $3.66** (range $3.19–$3.96) — WebSearch-reconfirmed this session, unchanged.
- **Revenue 3yr CAGR (FY2022→FY2025) 12.51%** — carried forward from the 06-12 session's precise FY2022 base ($31.616B); a rough independent recompute this session (using a rounded $31.616B figure) gives ~12.64% — immaterial difference (Growth_Score would move from 50.04 to 50.56 pre-bonus, i.e. final Growth_Score 60.04 vs 60.56 — doesn't change any downstream conclusion).
- **PW (probability-weighted) Fair Value $69.77** and its Bear/Base/Bull scenario architecture (06-12 session, reused unchanged 06-20) — carried forward; no new guidance since to revisit it (Netflix's FY2026 guidance — revenue $50.7–51.7B, operating margin 31.5%, FCF ~$12.5B, ad revenue ~$3B — stands unchanged, last confirmed at Q1 2026 earnings).

---

## 3. Quality Score (Phase 01 gate — first computation for NFLX)

**Hard disqualifier check:**

| Check | NFLX Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | TTM 81.8% (normalized) / 88.9% (as-reported); FY2025 86.2%; FY2024 79.5% — all comfortably above 70% | disqualify if <70% for 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | 0.145× (see below) | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2023/24/25 and TTM all positive (FY2023/24 FCF/NI ratios of 128.1%/79.5% imply positive FCF off positive NI both years) | disqualify if not | ✅ PASS |

No hard disqualifier fires. Proceeding to the weighted score (normalized basis primary; as-reported shown as sensitivity).

### Profitability (25% weight)

```
Net Margin (TTM, normalized) = $11,114.34M / $46,889.99M = 23.70%
NetMargin_Component = clamp((23.70/30)×100, 0, 100) = 79.01

ROIC — computed via NOPAT ÷ Net Invested Capital (glossary-standard: nets out cash):
  NOPAT = TTM EBIT × (1 − effective tax rate)
        = $13,936.60M × (1 − 0.1369)   [FY2025's clean, undistorted eff. tax rate — TTM's own
                                          blended rate (16.71%) is itself lifted by the one-off
                                          fee's tax treatment, so the FY2025 rate is the cleaner
                                          NOPAT basis per Rule 6]
        = $12,029.08M
  Net Invested Capital = Total Debt ($14,360.52M) + Equity ($31,126.40M) − Cash&STI ($12,288.45M)
                        = $33,198.47M
  ROIC = $12,029.08M / $33,198.47M = 36.23%
ROIC_Component = clamp((36.23/30)×100, 0, 100) = clamp(120.8, 0, 100) = 100.0

Profitability_Score = (79.01 + 100.0) / 2 = 89.51
```
No FCF-positivity cap applies (FCF-positive well beyond 3 years).

**⚠️ ROIC sensitivity, shown transparently.** Prior NFLX sessions cited a third-party (GuruFocus-style) ROIC range of 21.3–25.5%, well below this session's from-scratch 36.23% bottom-up computation. Two plausible sources of the gap, both disclosed: (a) third-party aggregators may use a different Invested Capital definition (e.g. no cash-netting, or including operating-lease liabilities); using **no cash-netting** (Total Debt + Equity, $45,486.92M) gives ROIC = 26.45% — still comfortably above the 30% clamp-relevant range only at the margin. (b) using the TTM blended tax rate (16.71%, itself lifted by the one-off fee) instead of FY2025's clean rate gives NOPAT $11,608.38M → ROIC (cash-netted) 34.97% — negligibly different. **Materiality check:** even using the *lowest* third-party figure (21.3%) — ROIC_Component would be clamp(21.3/30×100) = 71.0 instead of 100.0, moving Profitability_Score to 75.01 and the final Quality Score down to **~70.4** (computed explicitly below) — i.e. **the sensitivity only pushes the score further below the 80.0 gate, never toward it.** The gate-failure conclusion in §3.7 is robust to this entire range of ROIC treatments.

### Margins (15% weight)

```
Gross Margin (TTM) = 49.03% (computed, §2 — up from FY2025's annual 48.5%)
GrossMargin_Score = clamp((49.03/80)×100, 0, 100) = 61.29
```
No structural-trend bonus applies — the bonus is reserved for margins *below* the 40% threshold that are still expanding; NFLX's margin is already well above 40%, so this doesn't apply (gross margin has in fact been expanding for 3 straight years — 41.5% FY2023 → 46.1% FY2024 → 48.5% FY2025 → 49.03% TTM, per WebSearch/MacroTrends aggregation — but the rule as written only credits the bonus below the 40% threshold).

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022→FY2025, carried forward) = 12.51%
Growth_Score = clamp((12.51/25)×100, 0, 100) = 50.04
TAM/pricing-power evidence (cited, documented):
  - Netflix's advertising business is guided to roughly double to ~$3B in 2026 (from ~$1.5B
    in 2025, itself 2.5× 2024) — company-guided, per Q1 2026 shareholder letter (WebSearch).
  - Ad-supported-tier reach grew from 94M (May 2025) → 190M (Nov 2025) → 250M+ monthly
    active viewers (May 2026) — WebSearch (subscriptioninsider.com, thewrap.com).
  - Netflix raised prices across all US tiers in March 2026 (second hike in ~2 years:
    Standard-with-ads $8.99, Standard $19.99, Premium $26.99) while co-CEO Greg Peters
    stated on the Q1 2026 earnings call that churn *improved* YoY across all regions
    (WebSearch — Variety, Dexerto) — direct evidence of pricing power without volume loss.
  → +10 (documented TAM expansion + pricing power)
No structural-deceleration evidence: revenue growth has held steady at ~16% YoY for
  FY2024, FY2025, and Q1 2026 — not decelerating. No −10 applies.
Growth_Score = clamp(50.04 + 10, 0, 100) = 60.04
```

### Balance Sheet (15% weight)

```
Net Debt = $2,072.07M (§2)
EBITDA (TTM) = EBIT ($13,936.60M) + non-content D&A ($351.90M) = $14,288.50M
  [Content amortization (~$15B+/yr) is deliberately excluded from this add-back — established
   in the 2026-06-12 NFLX session: for a content-replacement-cost business model, amortized
   content cost functions as a recurring operating cost, not a one-off non-cash item. Carried
   forward unchanged; immaterial to the outcome regardless, given how small net debt is.]
Net Debt/EBITDA = $2,072.07M / $14,288.50M = 0.145×
BalanceSheet_Score = clamp(100×(1 − 0.145/4), 0, 100) = 96.37
```
Standard /4 denominator (NFLX is not a payment network/exchange — Upgrade 5 override doesn't apply).

### Moat Signal (15% weight) — checklist, cited evidence per signal

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Third-party subscriber estimates (Ampere Analysis, since Netflix stopped disclosing quarterly subscriber counts after Q4 2024): ~310M (Q1 2025) → crossed 325M in Q4 2025, held at "exceeded 325M" through Q1 2026 (Variety, tech-insider.org) — roughly +5% YoY. Sustained ~16% YoY revenue growth for 3+ consecutive years (FY2024/25/Q1'26). Co-CEO Greg Peters, Q1 2026 earnings call: churn *improved* YoY across all regions despite two price hikes in ~2 years. |
| Brand premium | **TRUE** | Raised prices across all three US tiers in March 2026 (second hike in ~2 years) while management reports churn improving, not worsening — direct evidence of pricing power (price increases without volume loss). MoffettNathanson estimates NFLX still monetizes at only ~48–50¢ per hour viewed vs. 64–93¢ for Disney+/Hulu/Peacock/Max/Paramount+ (WebSearch) — analysts explicitly frame this gap as *room* to keep raising price without competitive disadvantage, itself evidence of a pricing cushion consistent with brand strength. |
| Network effect | FALSE | No documented two-sided-marketplace or user-growth-driven mechanism identified for Netflix's core content-streaming business. |
| Switching costs | FALSE | No documented lock-in mechanism — month-to-month, cancel-anytime subscription with no contractual or data-migration cost, consistent with every other consumer-subscription name scored in this repo. |
| Scale cost advantage | **TRUE** | $20B 2026 content budget (guided, +10% YoY) — the largest content-spend scale in the industry (WebSearch, Variety/qz.com). MoffettNathanson's revenue-per-hour-viewed data (above) is explicitly framed by analysts as reflecting a *unit-economics* scale advantage: NFLX can under-monetize per hour relative to rivals and still be highly profitable off its larger subscriber/content base. |

```
Moat_Score = (3/5) × 100 = 60.0
```

### FCF Quality (10% weight)

```
FCF/NI (TTM, normalized) = $9,094.21M / $11,114.34M = 81.82%
FCFQuality_Score = clamp(((0.8182 − 0.40)/0.60)×100, 0, 100) = 69.71
```
*Sensitivity (as-reported, fee included in both halves of the ratio): 88.94% → FCFQuality_Score = 81.56. Shown in §3.7's raw-basis total.*

### Quality Score — Final

```
Quality Score = (89.51×0.25) + (61.29×0.15) + (60.04×0.20) + (96.37×0.15) + (60.0×0.15) + (69.71×0.10)
              = 22.378 + 9.194 + 12.008 + 14.456 + 9.000 + 6.971
              = 74.007 → 74.0
```

### 3.7 — Robustness check (three bases, all fail the gate)

| Basis | Quality Score | Gate result |
|---|---|---|
| **Normalized (primary — fee removed, Rule 6)** | **74.0** | **FAILS** (5.9pp below 80.0) |
| As-reported (fee left in — sensitivity) | 77.2 | FAILS (2.8pp below 80.0) |
| Normalized + lowest third-party ROIC (21.3%) | 70.4 | FAILS (9.6pp below 80.0) |

**Quality Score = 74.0 — FAILS the 80.0+ gate, robustly across every reasonable treatment of the WBD one-off and the ROIC-methodology disagreement.** No individual hard disqualifier fires — this is purely a weighted-average shortfall, driven by a middling Moat_Score (60.0 — only 3 of 5 signals cited-true; no network effect or switching costs for a cancel-anytime subscription service) and a middling Growth_Score (60.04 — a mature, ~12.5%-CAGR grower, not a Fast Grower), which drag down otherwise-strong Profitability (89.5) and Balance Sheet (96.4) scores. **This is NFLX's first-ever computed Quality Score.**

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $77.65 / $3.66 = 21.2158×
EY = 1 ÷ 21.2158 = 4.7135%
Spread = EY − 10Y Treasury = 4.7135% − 4.49% = +0.2235%
```
Spread (+0.22%) < +1.5% → **FAILS** → **+5 additive** (yellow flag, not a veto).

**Step 2 — Rate Regime Modifier:** 10Y = 4.49% → 3.5–5% bracket → **+5**

**Total Rate Modifier: +10** (unchanged bracket vs. the 20 Jun/12 Jun sessions).

---

## 5. Valuation Score (Phase 02)

**FCF Yield — 40% weight** (normalized TTM FCF, Rule 6)
```
Market Cap = 4,212.794M × $77.65 = $327,123.48M
FCF Yield = $9,094.21M / $327,123.48M = 2.780%
FCF_Score = clamp(100×(1 − 2.780/10), 0, 100) = 72.20
```
*Sensitivity (as-reported FCF): yield 3.636% → FCF_Score 63.64 — see §5.1.*

**EV/EBIT — 40% weight (PEG redistributed — NFLX is not a Fast Grower, see §5 note below)**
```
Net Debt = $2,072.07M
EV = $327,123.48M + $2,072.07M = $329,195.54M
EV/EBIT = $329,195.54M / $13,936.60M = 23.62×
EV/EBIT_Score = clamp((23.62 − 12)/23 × 100, 0, 100) = 50.53
```

**Forward PE — 20% weight (5yr-range primary formula, carried-forward range)**
```
Forward PE = 21.2158×, 5yr Low = 19.32×, 5yr High = 55.82× (carried forward, §2)
FwdPE_Score (range) = clamp((21.2158 − 19.32)/(55.82 − 19.32) × 100, 0, 100) = 5.19
Historical PE Modifier (Upgrade 2): Deviation vs 5yr avg (39.44×) = (21.2158 − 39.44)/39.44
  = −46.21% → >20% below → −10 modifier
FwdPE_Score = clamp(5.19 − 10, 0, 100) = 0.0
```

**PEG — not applicable.** NFLX fails the Fast-Grower test (FY2024 diluted EPS declined YoY vs. FY2023 — established across every prior NFLX session; no new multi-year EPS data this session to revisit it). Weight redistributed to EV/EBIT (→ 40%).

### 5.1 Raw weighted score

```
Normalized (primary) = (72.20×0.40) + (50.53×0.40) + (0.0×0.20) = 28.88 + 20.21 + 0.0 = 49.09
As-reported (sensitivity) = (63.64×0.40) + (50.53×0.40) + (0.0×0.20) = 25.46 + 20.21 + 0.0 = 45.67
```
**+ Rate Modifier (+10):**
```
Normalized: 59.09 (before Upside/Downside Modifier)
As-reported: 55.67 (before Upside/Downside Modifier)
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

Reuses the PW Fair Value scenario architecture established 06-12, carried forward 06-20 (no new guidance/earnings event since to warrant rebuilding it — Netflix's FY2026 guidance is unchanged and Q2 2026 earnings haven't reported yet, §0/§2).

```
PW Fair Value (Rule 7, scenario blend) = $69.77   [Bear $50.68 / Base $65.03 / Bull $98.33,
                                                     25/50/25 weighted — unchanged since 06-12]
Gap Upside % = ($69.77 ÷ $77.65) − 1 = −10.15%      (price sits ABOVE PW fair value)
Catalyst window = 2 years (Rule 10) — Q2 2026 earnings (16 Jul), the FY2026 ad-revenue
                  doubling target (~$3B), and the 31.5% operating-margin guide resolve over
                  roughly the next two years. No narrower documented window → 2yr, unchanged.
Annualized gap = −10.15% ÷ 2 = −5.07%/yr
Intrinsic growth = +13.0%/yr (unchanged — mid-of-range durable FCF/EPS CAGR estimate)
Shareholder yield = +0.5%/yr (unchanged — no dividend, modest net buyback)

E = −5.07 + 13.0 + 0.5 = +8.43%/yr
```

**Map E to M** (hurdle H = 10%, 0 ≤ E < H branch):
```
M = +5 × (10 − 8.43)/10 = +5 × 0.157 = +0.79
```
**Upside/Downside Modifier M = +0.79** (thin-upside band — a small positive, mild trim pressure, essentially unchanged from the 06-20 session's +0.71).

**Guardrails:** a documented catalyst + timeline exists within 18–24 months (Q2 earnings, ad-ramp) — the −5 upside cap is moot since M is positive here. Scenario-weighted PW FV used throughout, never the bull case alone or the $114+ consensus PT. Full calc shown above — no black box.

---

## 7. Final Valuation Score

```
Final Score (normalized, primary) = 59.09 (raw+rate) + 0.79 (Upside/Downside) = 59.88 → 59.9
Final Score (as-reported, sensitivity) = 55.67 + 0.79 = 56.46 → 56.5
```

**Valuation Score = 59.9 — "Fair Value"** (50.0–69.9 band) — **on a standalone basis, this alone would already recommend HOLD** (no margin of safety, no trim trigger), before Quality is even considered. (As-reported sensitivity, 56.5, lands in the same band — the WBD-fee normalization choice doesn't change the standalone valuation conclusion either.)

---

## 8. Composite Score

Per the instructed practice for existing holdings whose Quality Score fails the 80.0+ gate (see AMZN/GOOG/MSFT/NKE 2026-07 precedent): **still compute the Composite Score as a reference number, but flag it explicitly as a number that must not be acted on at face value.**

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 74.0) + 0.50 × 59.9
                = 0.50 × 26.0 + 29.95
                = 13.0 + 29.95
                = 42.95 → exactly on a ".X5" boundary → round UP (conservative) → 43.0
```

**Composite Score = 43.0** — numerically lands in the **"Cheap" (30.0–49.9) → Standard position 3–5%** band, which would nominally read as a BUY-eligible score.

**⚠️ This is a false green light and must not be acted on at face value.** NFLX's Quality Score (74.0) decisively fails the 80.0+ gate — the Composite Score formula's `(100 − Quality Score)` term is doing the work of making an otherwise Fair-Value-banded stock (standalone Valuation Score 59.9) read as "Cheap" (43.0), purely because inverting a sub-80 Quality Score mechanically produces a large positive contribution. The action call below is driven by the quality-gate failure (Phase 04 Quality Watch escalation) and the standalone Valuation Score's own Fair-Value/Hold reading — **not** by the numerically-attractive Composite.

---

## 9. Action Recommendation

**Two independent reasons both point to HOLD, before any qualitative judgment is applied:**

**(a) The standalone Valuation Score (59.9) already sits in the Fair-Value/Hold band** — no margin of safety exists for a hypothetical add regardless of quality. Shown for full transparency, the order-setup math the Composite Score's "Cheap" band would nominally imply also fails on its own terms:

```
Composite-implied MoS (30.0–49.9 band): 25–30%
Buy price range off PW FV $69.77: $48.84 (30% MoS) – $52.33 (25% MoS); midpoint (27.5%) = $50.58
Live price ($77.65) sits 53.6% ABOVE even the most aggressive buy price ($52.33) — no entry point exists.
Stop loss (25–30% max loss from buy price, midpoint) = $50.58 × (1 − 0.275) = $36.67
R/R at midpoint buy price = ($69.77 − $50.58) / ($50.58 − $36.67) = $19.19 / $13.91 = 1.38:1 — FAILS the 2:1 minimum.
```
**No order is placed** — R/R fails the minimum threshold, and the live price is far above any disciplined buy price. This mirrors the pattern from the 2026-07-04 AVGO and 2026-07-01 NKE sessions: a favorable-looking score does not automatically produce an executable trade.

**(b) Phase 04 Quality Watch escalation (new this session).** NFLX's first-ever computed Quality Score (74.0) fails the 80.0+ gate — not decisively-and-alarmingly like NKE's 44.4 (no moat erosion, no margin compression, no balance-sheet stress), but a genuine, robust shortfall (§3.7) driven by a moderate Moat_Score (60.0 — Netflix's core subscription product structurally lacks switching costs and a network effect, an inherent business-model characteristic, not a deteriorating one) and a moderate Growth_Score (60.04 — a mature ~12.5%-CAGR compounder, not a Fast Grower). **This does not meet any Full Exit trigger** (no fundamental deterioration, no broken growth thesis, no balance-sheet crisis — margins are expanding, ROIC is very strong, leverage is negligible) — it is simply new information that NFLX, held for over a month under this framework, doesn't clear the framework's deliberately strict quality bar. Per the operating brief: *"a held position dropping below the gate is itself a signal worth surfacing, even though existing holdings aren't retroactively force-exited on quality alone."* Flagged here; no override log entry is warranted (this is a normal Quality Watch flag, not a position held in contravention of a rule).

### Net Action: **HOLD** — maintain the current 1.61%-weight position as-is

- No trim: neither the standalone Valuation Score (59.9) nor the Composite Score (43.0, though a false green light) reaches the 70.0+ trim threshold.
- No add: blocked independently by (i) the standalone Valuation Score sitting in the Fair-Value/Hold band with no margin of safety, (ii) the Composite-Score-implied order setup failing its own R/R gate, and (iii) the newly-computed Quality Score sitting below the 80.0+ gate.
- **Phase 04 Quality Watch flag added** — NFLX's Quality Score should be watched at the next rescore (Q2 2026 earnings, 16 Jul) for any further drift, though nothing here suggests active deterioration (all three sub-scores below 80 — Moat, Growth, and the modest Margins score — reflect NFLX's ordinary business-model characteristics, not decay).

All final-decision authority rests with the human investor per the operating brief.

---

## 10. Next Review Trigger

- **Q2 2026 earnings — Thursday 16 July 2026** (confirmed date, WebSearch) — mandatory re-score (Rule 9). Check: (a) ad-revenue pacing toward the $3B 2026 target; (b) Q2 operating margin vs. the 32.6% guide (down from 34.1% YoY, flagged since the 06-12 session); (c) any fresh subscriber/engagement disclosure; (d) whether the WBD termination fee's cash gets deployed (buybacks vs. content spend vs. new M&A) — a capital-allocation signal.
- **>15% unexplained price move from $77.65 in either direction** — immediate re-score (Rule 9). Note NFLX made a fresh 52-week low ($70.86) since the last rescore before this session's bounce — worth watching if that low is retested.
- **`yfinance` access** — flag for `/healthcheck`: this session hit a `YFRateLimitError` (429, "Too Many Requests") rather than the previously-documented `curl_cffi` TLS failure — a different failure mode worth tracking separately if it recurs.
- No position change executed by this session — recommendation only (Hold at 1.61%). If the investor acts, log it in `decisions/` per CLAUDE.md Rule 10.

---

## 11. Glossary

- **bps / pp (basis points / percentage points):** 0.01 percentage points / a direct difference between two percentages — units used throughout the rate and modifier calculations.
- **CAGR:** Compound Annual Growth Rate.
- **CapEx:** Capital Expenditure.
- **Composite Score:** this framework's blended 0.0–100.0 ranking number (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`), computed here as a reference figure only because Quality fails the 80.0+ gate — see §8.
- **EBIT / EBITDA:** operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **EPS:** Earnings Per Share.
- **EV / EV/EBIT:** Enterprise Value (market cap + debt − cash) / EV divided by EBIT, a valuation multiple.
- **EY (Earnings Yield):** 1 ÷ Forward PE, compared against the 10-Year Treasury yield in the Rate Environment Gate.
- **Fast Grower:** Peter Lynch's term for EPS growth >15%/yr for 3+ years on a clean earnings base — triggers the PEG sub-score. NFLX doesn't qualify.
- **FCF / FCF Yield / FCF/NI conversion ratio:** Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks whether accounting profit is turning into real cash).
- **Forward PE:** price ÷ next-twelve-months expected EPS.
- **Gross Margin:** Gross Profit ÷ Revenue — one of the Quality Score's Margins inputs.
- **Hard disqualifier:** a Quality Score condition that fails a company regardless of its weighted score — none fired for NFLX this session.
- **Hurdle rate:** the minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against.
- **Invested Capital:** the total capital (debt + equity, net of cash here) put to work in a business — the denominator of ROIC.
- **Moat:** a durable competitive advantage protecting a business's profits from competitors — scored here via a 5-signal checklist.
- **MoS (Margin of Safety):** the discount below fair value demanded before buying.
- **Net Debt/EBITDA:** a leverage ratio — this framework's primary balance-sheet-risk gate.
- **Net Margin:** Net Income ÷ Revenue.
- **NOPAT:** Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the numerator of ROIC here.
- **PEG ratio:** PE ÷ earnings growth rate — not applicable to NFLX this session.
- **PT (Price Target):** an analyst's price forecast.
- **PW (Probability-Weighted) Fair Value:** this framework's blended fair value — 25% bull + 50% base + 25% bear (Rule 7).
- **Quality Score:** this framework's 0.0–100.0 score (0.0 = lowest quality, 100.0 = highest) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. NFLX's first-ever computed value (74.0) fails this gate.
- **Rate Environment Gate / Rate Regime Modifier:** the mandatory pre-score check comparing Earnings Yield to the 10-Year Treasury, and the resulting additive score adjustment.
- **Rule 0 / Rule 6 / Rule 9 / Rule 10:** this framework's standing instructions to always fetch a live price first; normalize distorted earnings before valuing (applied here to the WBD termination fee); force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss) on a trade; this framework requires ≥2:1 to enter.
- **ROIC:** Return on Invested Capital — NOPAT ÷ Invested Capital; a core quality signal.
- **Shareholder yield:** dividend yield plus net buyback yield.
- **TAM:** Total Addressable Market.
- **Treasury yield (10Y):** the US government's 10-year borrowing rate, this framework's risk-free-rate benchmark.
- **TTM (Trailing Twelve Months):** the most recent 12 months of reported results — the basis for most figures in this session.
- **Upside/Downside Modifier (Expected-Return Modifier):** the additive ±15 adjustment to the valuation score based on expected annual return vs. the 10% hurdle.
- **Valuation Score:** this framework's 0.0–100.0 score (0.0 = cheapest, 100.0 = most expensive) combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.
- **WACC:** Weighted Average Cost of Capital (referenced via the carried-forward PW Fair Value's DCF component, not rebuilt this session).

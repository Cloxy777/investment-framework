# RESCORE — DUOL (Duolingo, Inc.) — 2026-07-04

**Task type:** RESCORE (mode `--both`)
**Date:** 04 Jul 2026
**10Y US Treasury Yield:** 4.485% (rounds to 4.49%) — Yahoo Finance `^TNX` chart quote, last close 2026-07-02 (bond market closed 2026-07-03 for the observed Independence Day holiday, and 2026-07-04/05 weekend). Consistent with today's other same-day sessions (AVGO 4.49%, CSGP 4.485%).
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current DUOL portfolio weight:** 8.20% (combined IBKR + Freedom24; 30 shares IBKR per `get_account_positions`, contract_id 505002183)
**Sector:** Technology — Education Software (EdTech / Language Learning)
**Last review:** 20 Jun 2026 (Valuation Score 53.7; Quality/Composite never computed — DUOL predates the 2026-06-29 methodology addition). This session runs the full current methodology (Quality Score + 80.0+ gate + Composite Score) on DUOL for the first time.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$125.76** | IBKR `get_price_history` (contract_id 505002183, daily bars), most recent completed session **2026-07-02** close. Cross-validated three independent ways: (1) Yahoo Finance chart endpoint `regularMarketPrice` = $125.76 at `regularMarketTime` 2026-07-02 20:00:01 UTC (= 4:00pm ET close); (2) Yahoo `quoteSummary` `financialData.currentPrice` = $125.76; (3) IBKR's own account `market_price` for the 30-share position = $125.48 (a slightly older mark, within 0.2%). All three agree the market is closed for the July 4th holiday weekend, so $125.76 (Thursday's close) is the correct, most recent live reference price — not a stale multi-day-old figure. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$121.21** (`is_close: true`) — this is stale by *four* trading sessions, matching the 2026-06-26 close, not the most recent one (price history shows 06-26 $121.49, 06-29 $116.03, 06-30 $115.02, 07-01 $121.22, 07-02 $125.76). Resolved via `get_price_history` + independent Yahoo cross-check, per the same pattern already documented in today's AVGO/CSGP/ADBE sessions. `bid_ask`/`change` fields returned empty (market closed at query time). |
| 52-week range | $87.89 – $468.00 | IBKR `misc_statistics`, matches Yahoo `fiftyTwoWeekLow/High` exactly |
| Analyst consensus PT | mean **$106.31**, median $101.00, n=17, rating "Hold" | Yahoo `financialData` — **notably below the live price ($125.76)**, a bearish sell-side signal in tension with this session's own scenario/DCF fair-value work (§6–7 below); flagged prominently, not smoothed over |
| Prior session price | $125.56 (20 Jun) | For reference — DUOL is **+0.16%** since the last review, nowhere near the 15% Rule 9 threshold. This rescore is methodology-driven (first Quality Score + Composite Score computation), not price- or earnings-driven — see §2. |

**Context:** $125.76 sits ~73% below the 52-week high ($468, reflecting the well-documented 2025–2026 AI-disruption-fear selloff) and ~43% above the 52-week low ($87.89) — still deep in the lower half of its 52-week range, and ~18% below the sell-side consensus PT cluster is *not* the case here — the stock trades **above** consensus, an unusual and important context point (see §1's PT flag).

---

## 2. Data Gathered — Sources & Gaps

**No Rule 9 trigger since the 2026-06-20 review.** No new earnings print (Q1 FY2026 was reported 2026-05-05, already the basis for the 06-20 session's TTM window — confirmed by this session's own TTM figures being *identical* to 06-20's cited $405.2M FCF / $156.5M EBIT), no guidance revision beyond what was already known, no management change, no M&A, and price moved only +0.16%. This rescore exists to bring DUOL current on the Quality Score / Composite Score methodology added 2026-06-29 (see [watchlist/STALE.md](../watchlist/STALE.md)).

**Tooling:** `yfinance`'s default crumb-based auth failed (`YFRateLimitError`, a known recurring issue also hit by today's screening session). Worked around by manually fetching a fresh Yahoo cookie + crumb via `fc.yahoo.com` / `query1.finance.yahoo.com/v1/test/getcrumb` and calling `query2.finance.yahoo.com`'s `quoteSummary` and `ws/fundamentals-timeseries` endpoints directly with `curl` — a transport-layer workaround only (same data source Yahoo/`yfinance` would otherwise serve), not a substitute data source. No metric was invented or estimated.

### ⚠️ Major data-integrity finding — dual-class shares (Rule 0 diligence)

Yahoo's `defaultKeyStatistics.sharesOutstanding` field reports **40,237,065** shares — but Duolingo has a **dual-class share structure** (confirmed via its 2026-05-05 Form 10-Q, SEC EDGAR): as of 2026-03-31, **Class A: 40,487,000 outstanding** (the publicly-traded DUOL class) **+ Class B: 6,356,000 outstanding** (founder-held, super-voting, not separately traded) = **46,843,000 combined basic shares**. Yahoo's `sharesOutstanding` field captures **Class A only** — the exact same data-integrity trap already documented in this framework's glossary for FUBO (Disney's Class B stake) and flagged as an open hypothesis for CHTR. Independent cross-check: `stockanalysis.com` reports 46.59M shares outstanding (agrees with the combined-class figure, not Yahoo's Class-A-only figure); Yahoo's own (differently-sourced, internally inconsistent) `summaryDetail.marketCap` field ($5.86B at a stale ~$121.2 price) implies **~48.3M shares** — closer to the *diluted* count below than to either basic figure, suggesting Yahoo's own market-cap field already uses a diluted, combined-class share count internally while its separately-exposed `sharesOutstanding` field does not.

**This session uses diluted weighted-average shares — 48,831,461 (Q1 FY2026, `yfinance`/Yahoo `quarterlyDilutedAverageShares`)** — as the share count for Market Cap, consistent with how [sessions/2026-07-04-rescore-avgo.md](2026-07-04-rescore-avgo.md) computed AVGO's market cap from diluted shares. This is materially different from naively using the vendor's Class-A-only `sharesOutstanding` figure:

| Share count basis | Shares | Implied Market Cap @ $125.76 |
|---|---|---|
| Vendor `sharesOutstanding` (Class A only — **wrong**) | 40,237,065 | $5,060.2M |
| Combined basic (Class A + Class B, 10-Q) | 46,843,000 | $5,891.0M |
| **Diluted weighted-average (used this session)** | **48,831,461** | **$6,141.0M** |

Using the wrong (Class-A-only) share count would have understated Market Cap by ~21% and materially understated FCF Yield and EV/EBIT (making DUOL look cheaper than it is) — this is the single largest driver of this session's score changes vs. 06-20, larger than the price move itself. Flagged prominently per "no black box."

### Standard inputs (TTM = Q2 FY2025–Q1 FY2026 unless noted; sourced via Yahoo `quoteSummary`/`fundamentals-timeseries`, fetched fresh this session, cross-checked internally where possible)

| Metric | Value | Source / cross-check |
|---|---|---|
| TTM Revenue | $1,098,813,000 | Sum of last 4 quarters ($252.265M+$271.713M+$282.868M+$291.967M); matches `financialData.totalRevenue` exactly |
| TTM Gross Profit | $798,457,000 (72.665% margin) | Quarterly rollforward; matches `financialData.grossMargins` (0.72665) exactly |
| TTM EBIT (Operating Income) | $156,503,000 | Quarterly rollforward ($33.363M+$35.159M+$43.454M+$44.527M) — **identical to the 06-20 session's cited $156.5M**, confirming no new quarter since then |
| TTM D&A | $14,992,000 | Quarterly rollforward |
| TTM EBITDA | $171,495,000 (EBIT+D&A) | Cross-checked exactly against the independent sum of Yahoo's own `quarterlyNormalizedEBITDA` series ($36.803M+$38.712M+$47.262M+$48.718M = $171.495M) |
| TTM FCF | $405,198,000 | `trailingFreeCashFlow` (as of 2026-03-31) — **identical to the 06-20 session's cited $405.2M**; independently cross-checked against the sum of `quarterlyFreeCashFlow` ($86.324M+$77.356M+$93.732M+$147.786M = $405.198M) |
| TTM Net Income (GAAP, actual) | $422,390,000 | Matches `defaultKeyStatistics.netIncomeToCommon` exactly |
| ⚠️ TTM Net Income (normalized, see below) | **$166,868,172** | See Rule 6 normalization, next section |
| Total Debt (2026-03-31) | $91,873,000 | `quarterlyTotalDebt` |
| Cash (2026-03-31) | $1,138,561,000 | `quarterlyCashAndCashEquivalents` |
| Net Debt | **−$1,046,688,000** (net cash) | Computed |
| Total Stockholders' Equity (2026-03-31) | $1,391,764,000 | `quarterlyStockholdersEquity` |
| Diluted weighted-avg shares (Q1 FY2026) | 48,831,461 | `quarterlyDilutedAverageShares` |
| Forward EPS (FY2027 consensus) | $7.845 | Yahoo `earningsTrend`, period "+1y" (FY2026 is still in-progress, so "forward" = next full FY, 2027) |
| Forward PE | 16.03× | $125.76 ÷ $7.845 |
| Revenue 3yr CAGR (FY2022→FY2025) | 41.08% | ($1,037.589M/$369.495M)^(1/3) − 1 |
| Beta | 0.88 | Yahoo `summaryDetail.beta` |
| Dividend | None | `dividendYield` not set — DUOL pays no dividend |

### ⚠️ Second major finding — Forward PE fell from 42.56× (06-20) to 16.03× (today): a fiscal-year-rollover + estimate-revision effect, not a data error

The 06-20 session's Forward PE (42.56×) was built on a *FY2026* consensus EPS estimate that had recently been cut to ~$2.95 (per the 06-12 session's note). Today, with FY2026 nearly two quarters further along, Yahoo's "forward" EPS field has rolled to the *FY2027* estimate ($7.845) — both because the reference year shifted and because sell-side FY2027 estimates have been **substantially raised** as DUOL's monetization/margin trajectory became clearer. **Sensitivity check, shown transparently:** using the *FY2026* (still-in-progress-year) consensus EPS of $6.686 instead gives Forward PE = 18.81×, EY = 5.32%, Spread vs. 4.485% 10Y = +0.83% — which would **fail** Rate Gate Step 1 (+5 additive) rather than pass it, pushing Raw+Rate to 69.3 instead of 64.3 and the final Valuation Score to ~61.7 (Composite ~39.0) instead of 56.6 (Composite 36.4). **Same action band either way (Cheap/30.0–49.9) — this sensitivity doesn't change the recommendation**, but is disclosed per "no black box." This session uses Yahoo's own reported `forwardPE`/`forwardEps` field (16.03×/$7.845) for consistency with how every other session in this repo sources "Forward PE."

### Rule 6 normalization — the recurring DUOL tax-valuation-allowance distortion

Q3 FY2025 (ended 2025-09-30) carries a **$245.7M non-cash tax benefit** (`quarterlyTaxProvision` = −$245,746,000 against pretax income of only $46.449M), inflating that quarter's GAAP net income to $292.195M and TTM GAAP net income to $422.39M (38.44% net margin) — this is the same deferred-tax-valuation-allowance-release pattern already documented in [glossary.md](../framework/glossary.md) and flagged in the 06-12/06-20 DUOL sessions. Per Rule 6 ("normalize before you value... strip out one-time items"), this session computes a **normalized TTM Net Income of $166,868,172** by applying each quarter's own Yahoo-reported `TaxRateForCalcs` (Yahoo's own normalized/non-GAAP tax-rate field: 3.6%, 21%, 23.0%, 21.8% for Q2FY25–Q1FY26 respectively — note this field is *already* Yahoo's own "for calc purposes" normalized rate, not an invented assumption) to each quarter's pretax income, rather than using the actual, benefit-inflated tax provisions. Normalized Net Margin = 15.19% (vs. 38.44% GAAP-actual) — used for the Quality Score's Profitability sub-score (§3). The FCF/NI Quality sub-score and hard-disqualifier check (§3) instead use the **actual GAAP ratio** (95.93%), since that measures cash-vs-reported-earnings conversion quality and isn't distorted by *which* earnings figure you'd otherwise normalize to — both the actual and a normalized-basis ratio clear the 70% floor by a wide margin regardless.

### Other flagged assumptions (analyst judgment, not fetched data — disclosed per Guardrail 3)

- **Equity Risk Premium (5.0%)** and **pretax cost of debt (5.0%)** used in the DCF's WACC (§7) are standard modeling conventions, not fetched facts (same disclosure as the AVGO session).
- **DCF Stage 1 FCF growth path** (Year 1 = $350M, the company's own guided FY2026 FCF floor, tapering 12%→10%→8.5%→...→2.5% terminal) is analyst judgment calibrated to management's own guidance (see below), not raw data.
- **Intrinsic growth (10%)** and **shareholder yield (~0%)** used in the Upside/Downside Modifier's `E` calculation (§6) are judgment calls, grounded in but not identical to fetched data — shareholder yield specifically is inferred from diluted share count *rising* slightly (48.799M→48.831M over the last year) despite a stated buyback authorization, i.e. buybacks haven't yet net-offset SBC-driven issuance; this is an observed data point, not an invented number.

### Qualitative context (Rule 9 / Phase 04 Growth-modifier evidence, cited)

Duolingo's 2026-05-05 Q1 FY2026 earnings and subsequent coverage document a **structural, management-guided deceleration**: DAU (Daily Active User) YoY growth ran 40%+ every quarter from Q2 2022 through Q2 2025, slowed to ~30% in Q4 2025, and to 21% in Q1 2026, with management now guiding **~20% DAU growth for the rest of 2026** — alongside a strategic pivot ("user growth over near-term monetization") that guides bookings growth down to **~6% in Q2 2026** and full-year revenue growth to **15–18%** (vs. 38.7% in FY2025). Source: [TIKR Q1 2026 earnings summary](https://www.tikr.com/blog/duolingo-q1-2026-earnings-daus-hit-21-growth-ebitda-margin-reaches-29), [TipRanks](https://www.tipranks.com/news/company-announcements/duolingo-balances-ai-ambition-with-slower-2026-growth), [PYMNTS](https://www.pymnts.com/earnings/2026/duolingo-bets-on-user-growth-to-outpace-ai-disruption/). Gross margin is also guided to compress from 71% (Q2) toward ~69% by year-end as AI-feature costs are integrated (a real but sub-3pp move — doesn't trip the Phase 04 margin-compression flag on its own).

**No metric was invented or estimated where hard figures existed.** Every number above traces to a live Yahoo fetch, an internally cross-checked rollforward, a primary-source SEC filing (share count), or a disclosed modeling assumption.

---

## 3. Quality Score (Phase 01 gate — first computed for DUOL)

**Hard disqualifier check (all must pass before any weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | FY2023 870%, FY2024 298%, FY2025 87.1% (all GAAP-actual) — FY2022 undefined (NI was negative, a loss year, not a "<70%" case) | disqualify if <70% for 2+ yrs w/o growth-capex explanation | ✅ PASS |
| Net Debt/EBITDA over threshold? | **−6.10×** (net cash) | disqualify if >2.5× (standard) | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2022 $43.5M, FY2023 $139.9M, FY2024 $264.4M, FY2025 $360.4M — all positive | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight)

```
Net Margin (TTM, Rule-6 normalized) = $166,868,172 / $1,098,813,000 = 15.19%
  (GAAP-actual would be 38.44% — inflated by the Q3 FY2025 $245.7M tax-valuation-allowance
   release; normalized per Rule 6 and the recurring DUOL precedent, see §2)
NetMargin_Component = clamp((15.19/30)×100, 0, 100) = 50.6

ROIC — NOPAT ÷ Net Invested Capital:
  NOPAT = EBIT (TTM) $156,503,000 × (1 − 17.78% blended normalized tax rate) = $128,677,567
    (blended rate = 1 − normalized TTM NI ÷ TTM pretax income = 1 − 166,868,172/202,952,000 = 17.78%,
     derived from Yahoo's own per-quarter "TaxRateForCalcs" field, not an assumed flat rate)
  Net Invested Capital = Total Debt $91,873,000 + Total Equity $1,391,764,000 − Cash $1,138,561,000
                        = $345,076,000
  ROIC = $128,677,567 / $345,076,000 = 37.29%
ROIC_Component = clamp((37.29/30)×100, 0, 100) = 100.0 (capped)

Profitability_Score = (50.6 + 100.0) / 2 = 75.3
```
No FCF-positivity cap applies (FCF-positive 4 consecutive years).

### Margins (15% weight)

```
GrossMargin_Score = clamp((72.67/80)×100, 0, 100) = 90.8
```
No structural-trend bonus (already far above the 40% threshold the bonus targets). Note: gross margin is guided to *compress* slightly (71%→~69%) through year-end on AI-feature cost integration — a real but sub-3pp move, not a Phase 04 flag trigger, and not a penalty to this static-level sub-score either.

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022→FY2025) = ($1,037,589,000/$369,495,000)^(1/3) − 1 = 41.08%
Growth_Score = clamp((41.08/25)×100, 0, 100) = 100.0 (capped)

Documented structural deceleration (cited, §2): DAU YoY growth 40%+ (2022–mid-2025) → 30% (Q4 2025)
→ 21% (Q1 2026), management guiding ~20% for the rest of 2026; bookings growth guided down to
~6% (Q2 2026); full-year revenue growth guided to 15–18% (vs. 38.7% actual FY2025). This is
management's own multi-quarter guided trajectory, not a single cyclical miss → −10 applied.
Growth_Score = clamp(100.0 − 10, 0, 100) = 90.0
```
(TAM-expansion evidence also exists — AI Video Call features, international/Asia expansion cited in the same Q1 2026 coverage — but Growth_Score was already saturated at the 100.0 cap before any modifier, so a +10 TAM credit would be moot; the −10 deceleration credit is the one with real effect and is shown as the applied modifier, per "no black box.")

### Balance Sheet (15% weight)

```
Net Debt = Total Debt $91,873,000 − Cash $1,138,561,000 = −$1,046,688,000 (net cash)
Net Debt/EBITDA = −$1,046,688,000 / $171,495,000 = −6.10×
BalanceSheet_Score = clamp(100×(1 − (−6.10)/4), 0, 100) = clamp(252.5, 0, 100) = 100.0
```
Standard /4 denominator (DUOL isn't a payment network/exchange — Upgrade 5 asset-light override doesn't apply). A deeply net-cash balance sheet — no leverage risk whatsoever.

### Moat Signal (15% weight) — checklist, cited evidence per signal

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | DAU growing 21% YoY even amid deceleration (Q1 FY2026, [TIKR](https://www.tikr.com/blog/duolingo-q1-2026-earnings-daus-hit-21-growth-ebitda-margin-reaches-29)); Duolingo is the most-downloaded language-learning app globally per company's own consistent public positioning across its 10-K/investor materials — softer evidentiary basis than a third-party share-tracker report, flagged as such (same caveat style as AVGO's Moat signal 1). |
| Brand premium | FALSE | No cited pricing-power evidence (price increases without volume loss) found in this session's research. |
| Network effect | FALSE | No documented two-sided-marketplace mechanism — Duolingo's product is primarily one-sided content/gamification, not a marketplace connecting distinct user groups. |
| Switching costs | **TRUE** | Documented gamification lock-in mechanism: accumulated streaks, XP, and League standing represent a real, cited switching cost (losing app-specific progress/history is the accumulated "investment" a user forfeits by switching) — a mechanism specific to Duolingo's product design, widely covered in the same earnings analyses cited above. |
| Scale cost advantage | **TRUE** | Documented per-unit AI content-generation cost declining with scale as the company integrates more AI features, cited as a direct driver of gross margin dynamics ([TipRanks](https://www.tipranks.com/news/company-announcements/duolingo-balances-ai-ambition-with-slower-2026-growth), [Kavout](https://www.kavout.com/market-lens/is-duolingo-s-stock-decline-a-sign-of-ai-disruption-or-a-buying-opportunity)). |

```
Moat_Score = (3/5) × 100 = 60.0
```

### FCF Quality (10% weight)

```
FCF/NI (TTM, GAAP-actual) = $405,198,000 / $422,390,000 = 95.93%
FCFQuality_Score = clamp(((0.9593 − 0.40)/0.60)×100, 0, 100) = 93.2
```
(Sensitivity: using normalized NI instead gives an implausible >100% ratio, an artifact of over-normalizing the denominator — the GAAP-actual ratio is the more meaningful cash-conversion read here and is used as the scored figure; either way the FCF-quality signal is strongly healthy, far above the 70% hard-disqualifier floor.)

### Quality Score — Final

```
Quality Score = (75.3×0.25) + (90.8×0.15) + (90.0×0.20) + (100.0×0.15) + (60.0×0.15) + (93.2×0.10)
              = 18.83 + 13.62 + 18.00 + 15.00 + 9.00 + 9.32
              = 83.77
```

**Quality Score = 83.8 — clears the 80.0+ gate.** DUOL is now eligible for the Composite Score, having never been quality-scored before.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = 16.03×
EY = 1 ÷ 16.03 = 6.24%
Spread = EY − 10Y Treasury = 6.24% − 4.485% = +1.75%
```
Spread (+1.75%) ≥ +1.5% → **passes** → no additive. *(This flips vs. the 06-12/06-20 sessions, which both failed Step 1 under the old, much higher Forward PE — see the fiscal-year-rollover finding in §2 for why, and the sensitivity check showing this doesn't change the ultimate action.)*

**Step 2 — Rate Regime Modifier**
10Y = 4.485% → 3.5–5% bracket → **+5**

**Combined Rate Modifier: +5** (down from +10 in the 06-12/06-20 sessions, which applied both steps)

---

## 5. Valuation Score (Phase 02)

### FCF Yield (40% weight)

```
Market Cap = $125.76 × 48,831,461 diluted shares = $6,141,044,535
FCF Yield  = $405,198,000 / $6,141,044,535 = 6.60%
FCF_Score  = clamp(100×(1 − 6.60/10), 0, 100) = 34.0
```
No Owner Earnings adjustment (Upgrade 1) — DUOL's capex is ~2.6% of revenue, immaterial, and DUOL isn't among the named moat-building-reinvestment companies (MSFT/GOOGL/META/AMZN).

### EV/EBIT (weight 25% base, redistributed to 40% — see PEG below)

```
EV = Market Cap $6,141,044,535 + Net Debt (−$1,046,688,000) = $5,094,356,535
EV/EBIT = $5,094,356,535 / $156,503,000 = 32.55×
EV/EBIT_Score = clamp((32.55 − 12)/23 × 100, 0, 100) = 89.4
```

### Forward PE + Historical PE Modifier (20% weight)

**No-history fallback applied — same conclusion as the 06-12/06-20 sessions, re-verified this session.** Attempted to reconstruct a 5yr quarterly TTM-PE series via Yahoo's `quarterlyDilutedEPS` timeseries endpoint (requested back to 2020); it returned only **5 quarters** of data regardless of the requested period range — a confirmed, persistent data-depth limitation for this ticker (not this session's error), consistent with DUOL's short public history (IPO July 2021) and its GAAP-loss years (2021–2022) that would make any reconstructed series unusable anyway (the framework's own rule excludes any quarter with TTM EPS ≤0, and the 2025 series is itself tax-distorted).
```
FwdPE_Score = 50.0 (neutral midpoint, flagged)
```

### PEG (15% weight) — Fast-Grower eligibility ruling carried forward

**Ruling maintained from the 2026-06-20 clarification** ([decisions/2026-06-20-framework-clarification-peg-clean-earnings.md](../decisions/2026-06-20-framework-clarification-peg-clean-earnings.md)): DUOL lacks 3+ years of clean, non-distorted EPS (loss-making 2021–2022, barely profitable 2023, tax-distorted 2025, guided-deceleration 2026) — doesn't qualify as a Fast Grower for PEG purposes. **PEG is not scored; its 15% weight is redistributed to EV/EBIT (→ 40%).**

### Raw Weighted Score

```
Raw = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
    = (34.0 × 0.40) + (89.4 × 0.40) + (50.0 × 0.20)
    = 13.60 + 35.76 + 10.00
    = 59.35 (precise: 59.348)
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

**Step 1 — scenario fair values.** Anchored on the FY2027 consensus EPS ($7.845) used elsewhere this session, per the same convention as the AVGO session:

| Scenario | Wt | Assumption | EPS basis | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | User-growth strategy pays off, monetization re-accelerates, AI-disruption fear fades | $7.845 × 1.15 = $9.02 | 30× | **$270.65** |
| Base | 50% | Guided trajectory plays out as management described (DAU ~20%, bookings ~6% Q2, FY26 revenue 15–18%); multiple holds near today's market-implied level | $7.845 | 16× | **$125.52** |
| Bear | 25% | AI-disruption thesis materializes further, DAU growth stalls below guide, estimates cut | $7.845 × 0.75 = $5.88 | 10× | **$58.84** |

```
PW Fair Value = 0.25×270.65 + 0.50×125.52 + 0.25×58.84 = $145.13
Gap Upside % = 145.13 / 125.76 − 1 = +15.40%
```

**⚠️ Tension flagged (Rule 0 diligence, again):** the sell-side consensus PT ($106.31 mean, §1) sits *below* the live price, implying the Street currently sees limited-to-negative near-term upside — in direct tension with this session's own scenario-weighted +15.4% gap. Both are shown; this is disclosed as a genuine open tension for the human investor to weigh, not resolved by picking whichever number is more flattering.

**Step 2 — catalyst & annualization (Rule 10).** No single sharp re-rating event exists; instead, management has laid out a **specific, quantified, multi-quarter guidance framework** (DAU ~20% for the rest of 2026, bookings trough ~6% in Q2 2026, gross margin path to ~69% by year-end) that will be tested and updated at each of the next several quarterly prints. Used the framework's default **2-year (24-month)** catalyst window (Rule 10's upper bound) — this is a series of specific, checkable guidance checkpoints rather than one binary event, but is concrete and quantified enough to satisfy Guardrail 1 (a catalyst *is* identifiable within the 18–24 month window), so no upside cap is applied.
```
Annualized gap = 15.40% / 2 = 7.70%
```
**Step 3 — expected annual return E.**
```
E = annualized gap (7.70%) + intrinsic growth (10%, judgment — see §2 flag, calibrated conservatively
    below the company's own 15-18% revenue growth guide given margin-compression headwinds)
  + shareholder yield (~0%, no dividend; diluted share count actually *rose* slightly over the
    last year (48.799M→48.831M) despite a stated buyback authorization — net dilutive-to-flat,
    not yet a net buyback)
  = 7.70 + 10.0 + 0.0 = 17.70%
```
**Step 4 — map E to M** (hurdle H = 10%):
```
E (17.70%) ≥ H → M = −15 × clamp((17.70 − 10)/15, 0, 1) = −15 × clamp(0.513, 0, 1) = −7.70
```
**Upside/Downside Modifier M = −7.7.**

---

## 7. Final Valuation Score

```
Final Score = Raw Weighted (59.35) + Rate Modifier (+5) + Upside/Downside Modifier (−7.70)
            = 56.65 → rounds to 56.6
```

Precise (unrounded) intermediate math: 59.348 + 5 − 7.702 = 56.646 → rounds to **56.6** (second decimal is 4, rounds down — not a ".X5" boundary case).

**Valuation Score = 56.6 — "Fair Value"** (50.0–69.9 band). Moved from 53.7 (06-20) → 56.6, a modest **+2.9** net move, but this masks two large offsetting swings shown transparently above: the dual-class-share market-cap correction pushed the raw weighted score up sharply (from a would-be ~41.7 using the wrong Class-A-only share count, to 59.35 using the correct diluted count), while the Rate Gate's Step 1 now passes (removing 5 points that applied in both prior sessions) and the Upside/Downside discount is similar in magnitude (−7.7 vs. −8.25 prior).

---

## 8. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 83.8) + 0.50 × 56.6
                = 0.50 × 16.2 + 28.30
                = 8.10 + 28.30
                = 36.40
```

**Composite Score = 36.4 — "Cheap"** (30.0–49.9 band). This is a full band better than the raw Valuation Score alone (56.6, "Fair Value") would suggest — the first time DUOL's Quality Score has been computed, and it clears the 80.0+ gate comfortably (83.8), which materially improves the blended ranking number per the Composite Score's design intent (a much higher-quality business shouldn't be penalized to the same band as a marginal one purely because its own valuation sub-scores sit at "Fair Value").

---

## 9. Action Recommendation & Order Setup

Composite Score 36.4 falls in the **30.0–49.9 "Cheap" → Standard position 3–5%** band — nominally BUY-eligible. Per the operating brief, the full order setup is run below for transparency, even though the position-sizing conclusion (see below) blocks any actual add.

**Sizing context: DUOL's current weight (8.20%) already exceeds the top of the "Cheap" band's 3–5% target range** — more than 1.6× the top of what a *fresh* entry at this score would target. There is no sizing gap to fill; if anything the position is larger than what today's score alone would newly justify (though this is not a Phase 05 trim trigger — trims only fire at Composite 70.0+, and DUOL is far below that).

### Fair Value — two methods, triangulated (Rule 1: Tech/Growth sector → DCF primary, multiples secondary)

**Method A — 3-Stage DCF (Rule 2).**
```
WACC build:
  Cost of equity = Rf (4.485%) + Beta (0.88) × ERP (5.0%, assumed) = 8.885%
  Cost of debt (pretax, assumed — debt is small/immaterial, ~1.5% of capital structure) = 5.0%; after-tax (21%) = 3.95%
  Weights: E/(D+E) = 98.5% (Market Cap $6,141.0M), D/(D+E) = 1.5% (Debt $91.9M)
  WACC = 98.5%×8.885% + 1.5%×3.95% = 8.81%

Stage 1 (yrs 1–5), FCF Year 1 = $350M (company's own guided FY2026 FCF floor, ">$350M"; used
  as a conservative anchor rather than assuming a beat), growth resuming toward the low-teens
  as the user-growth strategy is assumed to eventually convert:
  y1 $350.0M | y2 +12% $392.0M | y3 +12% $439.0M | y4 +10% $482.9M | y5 +10% $531.2M

Stage 2 (yrs 6–10), fade from 8.5% to the 2.5% terminal rate:
  y6 $576.4M | y7 $616.7M | y8 $650.7M | y9 $676.7M | y10 $693.6M

Terminal Value (at y10) = $693.6M × 1.025 / (0.0881 − 0.025) = $11,262.9M
Terminal Value as % of total DCF value = 59.3% (under the 75% Rule 4 sanity cap)

Sum of discounted FCFs (yrs 1–10) = $3,320.6M
PV of Terminal Value = $4,840.3M
Enterprise Value (DCF) = $8,160.9M
Equity Value = $8,160.9M + Net Cash $1,046.7M = $9,207.6M
DCF Fair Value / share = $9,207.6M / 48,831,461 = $188.56
```

**⚠️ Flagged: DUOL's low Beta (0.88, per Yahoo) drives a relatively low 8.81% WACC**, which — combined with a durable double-digit FCF growth assumption over 10 years — produces a DCF value well above both the current price and the scenario-multiples PW Fair Value. A below-market beta sits in some tension with DUOL's realized volatility (a >70% 52-week drawdown/rally range) — flagged as a genuine methodology finding per "no black box," not smoothed into a lower number.

**Method B — Scenario-weighted multiples (the same PW Fair Value used for the Upside/Downside Modifier, §6):** **$145.13**

```
Triangulation (Rule 3, Tech/Growth weights): Blended FV = 40% × DCF + 60% × Multiples
                                            = 0.40 × $188.56 + 0.60 × $145.13
                                            = $75.42 + $87.08
                                            = $162.50
```

### Order Setup Checklist

```
[✓] Composite Score (incl. Quality blend):    36.4 — "Cheap" (30.0–49.9 band)
[✓] Expected annual return E / catalyst:      +17.7% / 2yr default (feeds the Upside/Downside Modifier, §6)
[✓] Upside/Downside Modifier applied:         −7.7
[✓] DCF Fair Value:                           $188.56
[✓] Multiples-Based Fair Value:               $145.13
[✓] Blended Fair Value:                       $162.50
[ ] Margin of Safety %:                       25–30% (Composite 30.0–49.9 band)
    Buy Price range: $113.75 (30% MoS) – $121.88 (25% MoS); midpoint (27.5%) = $117.81
[✓] PRIMARY SELL TARGET:                      $162.50 (Blended FV, baseline)
[✓] BULL-CASE TRIM TARGET:                    $270.65 × 0.90 = $243.59
[ ] STOP LOSS: 25–30% max loss from Buy Price
    At midpoint Buy Price $117.81 → Stop $85.42 (27.5%)
[✗] Risk/Reward Ratio: ($162.50 − $117.81) / ($117.81 − $85.42) = $44.69 / $32.39 = 1.38:1
    Checked across the full 25–30% MoS range — fails the 2:1 minimum throughout.
```

**Per fair-value-methodology.md Step 6: R/R fails the minimum 2:1 threshold across the entire applicable MoS range. No order is placed** — the same conclusion this session would reach purely on R/R grounds, independent of the sizing-gap point above.

### Net Action: **HOLD** — maintain the current 30-share IBKR / combined 8.20% position as-is

- **No trim:** Composite Score (36.4) is far below any Phase 05 trim threshold (70.0+).
- **No add:** two independent gates both block it — (1) R/R fails 2:1 at every point in the applicable MoS range, and (2) the position already exceeds the Composite-Score-implied 3–5% target size, so there's no sizing gap even before R/R is considered.
- The score/action-band **did change meaningfully** even though the net action didn't: DUOL moves from a pure "Fair Value/Hold, watchlist-only" characterization (based on the raw Valuation Score alone, 56.6) to "Cheap" once its first-ever Quality Score (83.8) is blended in via the Composite Score (36.4) — worth flagging to the user as a materially different read on the position's standing, even though today's independent gates keep the actionable outcome at HOLD.

---

## 10. Next Review Trigger

**Date/event:** DUOL's Q2 FY2026 earnings release (expected ~early August 2026, based on the established cadence: Q1 reported 2026-05-05, prior quarters in Feb/Nov/Aug) — mandatory Rule 9 re-score. Specifically check against this session's guided checkpoints: **DAU YoY growth ~20%** (guided floor for the rest of 2026 — Q1 2026 came in at 21%, a step down from 30% in Q4 2025; a further material slide below 20% would be the clearest sign the AI-disruption bear case is validating), **bookings growth ~6%** (the guided Q2 2026 trough — a miss below this, or a failure to reaccelerate in H2, would matter), and **gross margin trending to ~69%** by year-end (guided AI-feature cost integration — confirm it doesn't overshoot into Phase 04 margin-compression-flag territory, >3pp). Also standard triggers: any guidance revision, management change, M&A, or a >15% unexplained price move from $125.76 (DUOL has shown 70%+ swings within 12 months, a realistic trigger either direction).

---

## Glossary

- **Beta**: A stock's sensitivity to overall market moves; used here as an input to estimate DUOL's cost of equity in the DCF's WACC. DUOL's reported beta (0.88) is flagged as being in tension with its realized (much higher) price volatility.
- **bps / pp**: Basis points (0.01 percentage points) / percentage points — units used throughout the rate and modifier calculations.
- **CAGR**: Compound Annual Growth Rate.
- **Catalyst window**: The timeframe within which a documented event is expected to close the price/fair-value gap — required before the Upside/Downside Modifier can credit large expected upside.
- **Composite Score**: This framework's blended 0.0–100.0 ranking number — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only after a company clears the 80.0+ Quality Score gate.
- **DAU (Daily Active Users)**: The number of unique users engaging with a product on a given day — Duolingo's primary growth KPI; its YoY growth rate decelerating from 40%+ to ~20% over 2022–2026 is this session's cited evidence for the Growth sub-score's −10 modifier.
- **DCF (Discounted Cash Flow)**: A valuation method estimating a company's worth today by projecting future cash flows and discounting them back to the present.
- **Deferred tax valuation allowance release**: A one-off GAAP accounting event reversing a prior write-down on deferred tax assets, producing an artificially low effective tax rate and inflated net income/EPS in the recognition period — the recurring DUOL earnings-quality distortion normalized out in this session's Quality Score.
- **Dual-class shares**: A capital structure with two+ classes of common stock with different voting rights, one of which may trade publicly while the other doesn't — DUOL's Class A/Class B structure caused a vendor data field (`sharesOutstanding`) to significantly understate true total shares this session, a major flagged finding (§2).
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **Equity Risk Premium (ERP)**: The extra return equity investors demand over the risk-free rate — an assumed DCF input, not a fetched fact.
- **EPS**: Earnings Per Share.
- **EV**: Enterprise Value — market cap + debt − cash.
- **EV/EBIT**: Enterprise Value ÷ EBIT, a valuation multiple independent of capital structure.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against bond yields in the Rate Environment Gate.
- **Fast Grower**: Peter Lynch's term for EPS growth >15%/yr for 3+ years on a clean earnings base — this framework's PEG-sub-score trigger; DUOL doesn't qualify.
- **FCF (Free Cash Flow)**: Cash generated after running and maintaining the business.
- **FCF Yield**: FCF ÷ Market Cap — higher is cheaper.
- **FCF/NI conversion ratio**: FCF ÷ Net Income — a cash-quality check.
- **Forward PE**: Price ÷ next fiscal year's expected EPS.
- **FV (Fair Value)**: The analyst's estimate of intrinsic worth, independent of market price.
- **GAAP**: Generally Accepted Accounting Principles.
- **Gross Margin**: Gross Profit ÷ Revenue.
- **Hard disqualifier**: A Quality Score condition that fails a company regardless of its weighted score.
- **Hurdle rate**: The minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against.
- **Invested Capital**: The capital (debt + equity, net of cash here) put to work in a business — the denominator of ROIC.
- **IRR**: Internal Rate of Return.
- **Moat**: A durable competitive advantage protecting a business's profits from competitors.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set.
- **Net Debt/EBITDA**: A leverage ratio — this framework's primary balance-sheet-risk gate. DUOL's is deeply negative (net cash).
- **Net Margin**: Net Income ÷ Revenue.
- **NI**: Net Income.
- **NOPAT (Net Operating Profit After Tax)**: EBIT × (1 − effective tax rate) — the numerator of ROIC here.
- **PEG ratio**: PE ÷ earnings growth rate.
- **PT (Price Target)**: An analyst's price forecast. DUOL's consensus PT sits below its live price this session — a flagged tension.
- **PW (Probability-Weighted) Fair Value**: This framework's blended fair value — 25% bull + 50% base + 25% bear.
- **Quality Score**: This framework's 0.0–100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. DUOL's first-ever Quality Score (83.8) clears the gate.
- **Rate Environment Gate / Rate Regime Modifier**: The mandatory pre-score check comparing Earnings Yield against the 10-Year Treasury, and the resulting additive score adjustment.
- **R/R (Risk/Reward ratio)**: Expected gain ÷ expected loss on a trade; this framework requires ≥2:1 to enter.
- **ROIC**: Return on Invested Capital.
- **Rule 0 / Rule 6 / Rule 9 / Rule 10**: This framework's standing instructions to always fetch a live price first; normalize distorted earnings before valuing; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline.
- **Structural Quality Override**: Suspends the Historical PE Modifier's "expensive" penalty when a richer multiple reflects genuine business improvement rather than euphoria (not directly triggered this session — no-history fallback applied instead).
- **TAM**: Total Addressable Market.
- **Terminal Value**: The lump-sum value assigned to all DCF cash flows beyond the explicit forecast period.
- **TTM**: Trailing Twelve Months.
- **Upside/Downside Modifier (Expected-Return Modifier)**: The additive ±15 adjustment based on expected annual return vs. the 10% hurdle.
- **Valuation Score**: This framework's 0.0–100.0 score (lower = cheaper) combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.
- **WACC**: Weighted Average Cost of Capital — the DCF discount rate.

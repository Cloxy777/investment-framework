# RESCORE — SPGI (S&P Global Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-07-05 (Sunday — markets closed; most recent trading session 2026-07-02, ahead of the 2026-07-03 July 4th holiday observance and the weekend)
**10Y US Treasury Yield:** 4.48% (FRED `DGS10`, most recent non-blank value, 2026-07-01 — 2026-07-02 not yet posted at fetch time)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** SPGI **33.4** (2026-06-20, BUY-Cheap band, limit-order watch — [sessions/2026-06-20-rescore-spgi.md](2026-06-20-rescore-spgi.md)); Quality Score / Composite Score never computed (predates the 2026-06-29 methodology change — flagged stale, see [watchlist/STALE.md](../watchlist/STALE.md)).
**Current SPGI portfolio weight:** 0.74% per [holdings.md](../portfolio/holdings.md) — comfortably under the 15% hard cap (Upgrade 7); not recomputed this session (weight refresh is `/sync-portfolio`'s job).
**First-ever Quality Score / Composite Score computation for SPGI this session.**

> *Jargon decoded on first use — see closing Glossary section. SPGI is the ticker behind this framework's costliest documented pricing error (the May 2026 "SPGI Price Inference Error," [fair-value-methodology.md](../framework/fair-value-methodology.md)) — extra care taken below on Rule 0.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$439.89** | IBKR `get_price_history` (contract_id 229629397, NYSE), most recent daily bar close = **2026-07-02**. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$414.97** (`is_close: true`) — one session stale: it matches 2026-07-01's close exactly, not the fresher 2026-07-02 close of $439.89. Same recurring stale-snapshot pattern flagged in the 2026-07-05 MSFT/NOW and 2026-07-04 AVGO sessions. The snapshot's `plprice` (mark) field returned a third value, $433.80 — also not the freshest close. Used $439.89 (the freshest `get_price_history` bar) per Rule 0's cross-check instruction. Independently corroborated: `yfinance`'s `currentPrice` (fetched via the `requests.Session()` transport workaround — see §3) also read **$439.89** exactly — two independent sources agree. |
| 52-week range | $359.36 – $543.25 | IBKR `misc_statistics` |
| Year-to-date change | −15.67% | IBKR `year_to_date_change` |
| Price vs. 06-20 review ($410.92) | **+7.05%** | Under the 15% Rule 9 "unexplained move" threshold, and not unexplained regardless — see the Mobility Global spinoff discussion in §4. |
| Dividend (declared, Q3 2026) | $0.97/share (10-Q-cited quarterly rate) → **0.88% yield** ($3.88 annualized ÷ $439.89) | SEC Form 10-Q (2026-03-31 period) `$0.97/share approved`; matches `yfinance` `dividendYield` (0.88%) almost exactly. IBKR's snapshot showed 0.83% — a minor vendor variance, noted not adopted. |

---

## 2. Rule 9 Trigger Check (2026-06-20 → 2026-07-05)

**This is NOT a routine, no-new-information rescore — two Rule 9 triggers fired.**

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Last print was Q1 2026 (2026-04-28), which predates even the 06-20 review. Next report (Q2 2026) expected ~end of July 2026 based on the 2025 cadence (2025-07-31). |
| Guidance revision | No | No new formal guidance issued this window. |
| Material M&A | No (see separate line below — this is a divestiture, not an acquisition) | |
| **Management change** | **Yes** | Saugata Saha, President of S&P Global Market Intelligence & Chief Enterprise Data Officer, is departing the company effective **2026-07-30** (company-announced, June 2026). A business-unit-level (not CEO/CFO) departure — flagged as a Rule 9 trigger and a forward-looking watch item (successor risk in Market Intelligence), not itself scored quantitatively. |
| **Major corporate restructuring — Mobility Global spinoff** | **Yes — the dominant event this session** | S&P Global completed the separation of its **Mobility** segment into an independent, separately-traded public company, **Mobility Global Inc. (NYSE: MBGL)**, via a **1-for-1 share distribution** to SPGI shareholders of record 2026-06-15, effective **2026-07-01, 12:01 a.m. ET**. Board approval and Form 10 registration statement filed 2026-05-07; distribution completed and MBGL began regular trading during the window covered by this rescore. **Full discussion, data-integrity implications, and sensitivity analysis in §4.** |
| Macro shift | No | 10Y ticked from 4.45% (06-20) to 4.48% (07-01) — still inside the 3.5–5% bracket, no Rate Regime bracket change. |
| >15% unexplained price move | No | +7.05% over 15 days, under the 15% threshold, and not "unexplained" — the spinoff and continued strength in Ratings/Indices are the plausible drivers (see §4). |

**Conclusion:** a full re-derivation is warranted this session on both fundamental-event grounds (management change, and especially the Mobility Global spinoff) and the routine schedule — not merely a price refresh.

---

## 3. Data Gaps / Flags

1. **`yfinance` initially failed with the same recurring `curl_cffi` TLS-impersonation `SSLError`/`Recv failure` documented across this repo's recent sessions.** Worked around by passing a plain `requests.Session()` (with a standard browser `User-Agent` header) into `yf.Ticker("SPGI", session=sess)`, forcing standard-`requests` transport instead of `curl_cffi`'s impersonation layer — the same transport-layer fix used in the 2026-07-04 AVGO and 2026-06-30 Japan-screening sessions. First attempt hit `YFRateLimitError` (transient); succeeded on retry ~5 seconds later. All `yfinance` figures below came from this working session.

2. **⚠️ MAJOR — Mobility Global spinoff creates a live-price-vs-trailing-financials mismatch (the "Spin-off" data-integrity trap already documented in [glossary.md](../framework/glossary.md), previously seen with FedEx Freight/FDXF).** The live price used above ($439.89, 2026-07-02 close) is the **post-separation** SPGI share price — Mobility's economic value left the entity via the 1-for-1 MBGL distribution effective 2026-07-01. But the trailing TTM financials pulled from `yfinance` (income statement, balance sheet, cash flow — all periods through Q1 2026, i.e. through 2026-03-31) are **consolidated, pre-separation figures that still include Mobility's segment contribution**, because the spinoff didn't close until *after* that reporting period ended. S&P Global has not yet filed pro forma continuing-operations financial statements as of this session — per the Form 10/8-K disclosure, those are due "by amendment not later than four business days after the distribution date" (i.e., on or about **2026-07-07**, two days *after* today's review date). **This means every FCF Yield / EV/EBIT / Forward-PE sub-score below pairs a smaller (ex-Mobility) market cap against a larger (Mobility-inclusive) trailing earnings/cash-flow base — a real, currently-unresolvable mismatch, not invented or guessed around.**
   - **Direction and magnitude, quantified from real disclosed figures (not estimated):** S&P Global's Form 10 registration statement for Mobility Global discloses Mobility's own standalone financials: FY2025 revenue ≈$1.75B, FY2025 adjusted EBITDA $711M, TTM-through-2026-03-31 adjusted EBITDA ≈$724M, FY2025 FCF $461M. Netting these against the consolidated TTM figures used below (EBITDA $8,138M, FCF $5,556M) gives an approximate continuing-operations base of ≈$7,414M EBITDA and ≈$5,095M FCF — **before any EBIT-level adjustment** (Mobility's own EBIT/D&A split isn't disclosed, so I did not attempt to force an EV/EBIT sub-score onto an invented allocation).
   - **Sensitivity check (shown for transparency, not adopted as the scored figures):** using the ≈$5,095M ex-Mobility FCF gives FCF Yield ≈3.91% (FCF_Score ≈60.9, vs. 57.33 scored below) and a rough EBIT proxy (Mobility EBIT ≈ adjusted EBITDA minus a proportional D&A allocation, ≈$618M) gives EV/EBIT ≈22.5× (EV/EBIT_Score ≈45.5, vs. 36.83 scored below). Re-running the raw weighted score with these sensitivity figures gives ≈42.5 (vs. 37.66 scored below) — **about 5 points higher (more expensive), but staying inside the same 30.0–49.9 "Cheap" band either way.** The action band this session is not sensitive to this issue, but the exact score is — flagged prominently, not silently corrected.
   - **This framework's own scored figures below use the as-currently-filed, consolidated TTM basis** (the only *actually filed* data as of 2026-07-05) rather than an allocation-based estimate, consistent with "never invent or estimate financial data." **A follow-up re-score is recommended once the pro forma continuing-operations statements are filed (~2026-07-07) — see §11.**
   - Quality Score sub-scores (margins, growth, balance sheet, moat) are financial-statement ratios that don't pair against market cap, so they're materially less distorted by this issue for *this* TTM window — though the *next* quarter's YoY revenue/EBITDA comparisons will need care once Mobility drops out of the consolidated figures.

3. **EV/EBIT — from-scratch calculation diverges from `yfinance`'s own `enterpriseValue` field.** My EV ($142,173.44M = market cap $130,207.44M + Q1'26 balance-sheet total debt $13,776M − cash&STI $1,810M) is ≈3.6%/$5.16B **below** `yfinance`'s own pre-computed `enterpriseValue` ($147,329.43M), likely reflecting a different `totalDebt` convention (`yfinance`'s `totalDebt` info field reads $13,900M vs. the balance sheet's $13,776M) or another adjustment not disclosed by the vendor. Used my own transparently-sourced, from-scratch calculation (consistent with "no black box") rather than the vendor's opaque pre-computed figure; using the vendor figure instead would give EV/EBIT 21.23× → EV/EBIT_Score 40.13 (vs. 36.83 used) — a modest, non-band-changing difference.

4. **Analyst consensus price target — thin-sample flag.** `yfinance`'s `targetMeanPrice` returned $462.67 off just **3 analysts** (down sharply from the 06-20 session's n=21, mean $532.81). A web cross-check against independent, broader-coverage sources (stockanalysis.com, MarketScreener, public.com — 15 to 34 analysts each) shows consensus clustering **$532–$562**, materially closer to and consistent with the 06-20 session's figure. Treated `yfinance`'s 3-analyst figure as an unreliable outlier this session and used the broader-coverage range ($532–$562) as the Guardrail-2 sanity anchor instead (see §8) — flagged explicitly, not silently substituted.

5. **PEG / Fast-Grower eligibility — re-confirmed NOT applicable**, consistent with the 06-20 session. Diluted EPS: FY2022 $10.20 → FY2023 $8.23 (**−19.3%**, IHS Markit-merger-related integration/intangible-amortization drag) → FY2024 $12.35 (+50.2%) → FY2025 $14.66 (+18.7%). An outright decline in the middle of the window breaks any 3-consecutive-year clean >15%/yr run outright — SPGI is a mature stalwart, not a Lynch Fast Grower (Upgrade 3 explicitly excludes stalwarts). PEG's 15% weight redistributed to EV/EBIT (→40%).

---

## 4. Mobility Global Spinoff — What Happened and Why It Matters Here

S&P Global's Board approved the separation of its **Mobility** segment (automotive data & analytics — vehicle history, registrations, pricing/valuation data) into a standalone public company, **Mobility Global Inc. (NYSE: MBGL)**, filed via Form 10 on 2026-05-07. The distribution — one MBGL share for every SPGI share held as of the 2026-06-15 record date — became effective 2026-07-01, 12:01 a.m. ET; SPGI's own share count is unaffected (holders keep their SPGI shares and separately receive MBGL shares). Mobility was a real, non-trivial piece of the combined company: **$454M of SPGI's $4,171M total Q1 2026 revenue (≈10.9%)**, and per its own Form 10, ≈$1.75B FY2025 revenue / $711M FY2025 adjusted EBITDA / $461M FY2025 FCF on a standalone basis.

**Sanity-check context (not scored):** MBGL's own IBKR snapshot showed a last price of $21.19 (also flagged `is_close: true`, so itself possibly one session stale) — at SPGI's 296M shares outstanding, that implies a standalone MBGL market value of roughly $6.3B, about 4.6% of SPGI's own $130.2B market cap. That MBGL's market-value share (≈4.6%) is smaller than its revenue share (≈10.9%) is directionally consistent with Mobility being a lower-margin/lower-multiple business than the core Ratings/Indices franchise — plausible, not independently verified.

This is a genuine, material Rule 9 event (a corporate restructuring of the same data-integrity-trap shape as the FedEx Freight/FDXF spinoff already documented in [glossary.md](../framework/glossary.md)) and is treated as such — see the quantified sensitivity check in §3 item 2 and the scoring approach used throughout.

---

## 5. SPGI — Inputs Collected (fresh this session, `yfinance` via `requests.Session()`, cross-checked against SEC filings)

**Sector:** Financials — Financial Data, Ratings & Analytics (mature wide-moat duopoly with Moody's, not a Fast Grower)

**TTM figures (Q2'25 + Q3'25 + Q4'25 + Q1'26 — consolidated, pre-Mobility-separation basis; see §3 flag 2):**

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 296,000,000 | `yfinance` `sharesOutstanding` |
| **Market Cap** | 296,000,000 × $439.89 = **$130,207.44M** | Computed |
| Total debt (2026-03-31) | $13,776M | `yfinance` quarterly balance sheet |
| Cash + ST investments (2026-03-31) | $1,810M | `yfinance` quarterly balance sheet |
| **Net Debt** | $13,776M − $1,810M = **$11,966M** | Computed |
| **EV (from-scratch)** | $130,207.44M + $13,776M − $1,810M = **$142,173.44M** | Computed — see §3 flag 3 for the divergence from `yfinance`'s own `enterpriseValue` field ($147,329.43M) |
| TTM Revenue (Q2'25–Q1'26) | 3,755+3,888+3,916+4,171 = **$15,730M** | `yfinance` quarterly financials rollforward |
| TTM Gross Profit | 2,636+2,767+2,746+2,936 = $11,085M | Same — **Gross margin 70.47%** |
| TTM EBIT | 1,579+1,677+1,685+2,004 = **$6,945M** | Same |
| TTM Net Income | 1,072+1,176+1,134+1,395 = **$4,777M** — **Net margin 30.37%** | Same |
| TTM Pretax Income / Tax Provision | 6,639M / 1,486M | Same — **effective tax rate 22.38%** |
| TTM D&A | 295+294+297+307 = $1,193M | `yfinance` quarterly cashflow |
| **EBITDA (TTM)** | $6,945M + $1,193M = **$8,138M** | Computed |
| **Net Debt/EBITDA (TTM)** | $11,966M ÷ $8,138M = **1.470×** | Computed |
| TTM Operating Cash Flow | 1,445+1,505+1,748+1,037 = $5,735M | `yfinance` quarterly cashflow |
| TTM CapEx | −61−45−46−27 = −$179M | Same |
| **TTM FCF** | 1,384+1,460+1,702+1,010 = **$5,556M** | `yfinance` quarterly cashflow ("Free Cash Flow" row) |
| **FCF Yield** | $5,556M ÷ $130,207.44M = **4.267%** | Computed |
| **FCF/NI (TTM)** | $5,556M ÷ $4,777M = **116.31%** | Computed |
| Total Stockholders' Equity (2026-03-31) | $31,173M | `yfinance` quarterly balance sheet |
| **Invested Capital** (Debt+Equity convention) | $13,776M + $31,173M = **$44,949M** | Computed |
| **NOPAT** | $6,945M × (1−0.2238) = **$5,390.5M** | Computed |
| **ROIC (TTM)** | $5,390.5M ÷ $44,949M = **11.99%** | Computed — below the 15% Phase-01 threshold on a reported basis, same acquisition-distorted (2022 IHS Markit merger goodwill/intangibles inflating the invested-capital base) dynamic flagged in the 06-20 session, not a fresh deterioration |
| Forward EPS (NTM consensus) | $20.42 | `yfinance` `forwardEps` |
| **Forward PE** | $439.89 ÷ $20.42 = **21.54×** | Computed — matches `yfinance` `forwardPE` (21.542) |
| 5yr avg/low/high PE | avg **28.48×**, low **20.64×**, high **32.21×** (n=20 quarters, 2021-02-09 to 2026-04-28) | `get_earnings_dates` + price-history reconstruction |
| Revenue 3yr CAGR (FY2022 $11,181M → FY2025 $15,336M) | **11.11%** | `yfinance` annual financials — matches the 06-20 session's 11.1% essentially exactly |
| Dividend yield | 0.88% ($0.97/qtr × 4 ÷ $439.89) | SEC 10-Q + computed |
| Net buyback yield | 2.18% (FY2025 diluted avg shares 305.1M vs. FY2024 311.9M) | `yfinance` annual financials — FY2025 $5.0B buyback (SEC 8-K) and Q1 2026 $1.0B buyback (SEC 10-Q) corroborate an even faster recent run-rate (Q1'26 diluted shares 297.6M vs. Q1'25 307.7M, −3.28% YoY at the quarterly level), used as directional corroboration only, not the scored figure |
| Annual FCF/NI (context, all pass the 70% hard-disqualifier floor) | FY2022 77.40% / FY2023 135.83% / FY2024 144.47% / FY2025 122.03% | Computed — matches the 06-20 session's cited 77%/136%/144%/122% essentially exactly |

---

## 6. SPGI — Quality Score (first-ever computation, 2026-06-29 methodology)

**Hard disqualifier check (all must pass before the weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | Every year FY2022–2025 and TTM ≥70% (see table above) | disqualify if <70% for 2+ yrs *without* explanation | ✅ PASS |
| Net Debt/EBITDA over threshold? | **1.470×** | disqualify if >2.5× (standard) | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FCF-positive every year FY2022–2025 and TTM | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight)

```
Net Margin (TTM)     = $4,777M / $15,730M = 30.37%
NetMargin_Component  = clamp((30.37/30)×100, 0, 100) = 100.0   (clamped from 101.2)

ROIC (TTM)            = $5,390.5M / $44,949M = 11.99%
ROIC_Component        = clamp((11.99/30)×100, 0, 100) = 39.97

Profitability_Score   = (100.0 + 39.97) / 2 = 69.99   (no FCF cap — FCF-positive every year on record)
```

### Margins (15% weight)

```
Gross Margin (TTM) = 70.47%
GrossMargin_Score = clamp((70.47/80)×100, 0, 100) = 88.09
```
No structural-trend bonus applicable — gross margin is already far above the 40% threshold the bonus specifically targets (a margin *below* 40% that's expanding).

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $11,181M → FY2025 $15,336M) = 11.11%
Growth_Score = clamp((11.11/25)×100, 0, 100) = 44.43
```
**+10 (documented TAM expansion, cited, company-disclosed):**
- S&P Global's own FY2025 Form 8-K discloses **Indices revenue +14%** (both Q4 2025 and full-year 2025), "largely driven by growth in asset-linked fees, which benefited from higher AUM and inflows" — a direct, cited TAM-expansion signal in a continuing (non-Mobility) segment.
- The same 8-K discloses **Ratings "Billed Issuance" +28% in Q4 2025** — real, company-disclosed evidence that the bond/loan-issuance cycle (the Ratings segment's core demand driver) is recovering, not shrinking.
- Consolidated revenue growth is itself **accelerating**, not decelerating: FY2025 +8% (8-K) → Q1 2026 +10.4% YoY (10-Q).

No −10 deceleration penalty — growth is accelerating on the evidence found, not decelerating.
```
Growth_Score (with bonus) = clamp(44.43 + 10, 0, 100) = 54.43
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA (TTM) = 1.470×
BalanceSheet_Score = clamp(100×(1 − 1.470/4), 0, 100) = 63.24
```
Standard /4 denominator applies — SPGI is a financial-data/analytics/ratings company, not clearly a "payment network or exchange" the Upgrade 5 asset-light override targets, and doesn't need the override regardless (1.470× already clears even the *standard* 2.5× gate comfortably).

### Moat Signal (15% weight) — checklist, cited evidence per signal

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | SEC-mandated NRSRO Annual Certification filings (Form NRSRO-CE) and the well-documented "Big Three" credit-rating-agency structure show S&P Global holding roughly 40–50% of the global credit-ratings market (by revenue / by ratings issued, respectively) in a multi-decade-stable duopoly with Moody's — reinforced by SPGI's own FY2025 8-K disclosure of Ratings Billed Issuance +28% (Q4 2025) and Ratings revenue +8% (FY2025). No evidence of share loss found; real evidence of continued strength in a regulatorily-entrenched structure. |
| Brand premium | **FALSE** | Only generic third-party/analyst commentary found (e.g. a Substack deep-dive citing the Ratings segment's ~63% operating margin as evidence of "enormous pricing power") — no company-disclosed, specific price-increase-without-volume-loss citation of the kind this checklist requires (contrast NKE's cited "3–7% annual price escalators" in the 2026-07-01 session). Marked false for lacking the precise evidentiary type, consistent with this repo's established rigor (mirrors NOW's and MSFT's treatment of signals lacking the exact evidence type in the 2026-07-05 sessions). |
| Network effect | **FALSE** | No documented two-sided-marketplace or user-growth-driven-value mechanism found for the ratings/data business. Indices' AUM-driven asset-linked fee growth (cited above) is a scale/reputation dynamic, not the marketplace-style network effect this checklist specifically requires. |
| Switching costs | **TRUE** | Documented regulatory mechanism: many bond indentures, loan covenants, and institutional investment mandates explicitly reference specific NRSRO-designated rating agencies by name (a real, structural lock-in flowing from the Credit Rating Agency Reform Act of 2006's NRSRO designation regime) — analogous treatment to how this framework already credits e.g. NOW's CMDB embedding or MSFT's identity-stack lock-in as a switching-cost mechanism without requiring a fresh numeric citation each time. |
| Scale cost advantage | **FALSE** | No cost-per-unit data found showing a gap vs. Moody's or Fitch — only revenue-scale/market-share citations were found, which the checklist treats as the (already-scored) "market share" signal, not this one. |

```
Moat_Score = (2/5) × 100 = 40.0
```

**Sensitivity note, shown transparently ("no black box"):** crediting "Brand premium" TRUE — a defensible-but-not-adopted read of the Ratings segment's unusually high operating margin — would raise Moat_Score to 60.0 and the overall Quality Score to ≈70.1. **Unlike NOW's razor-thin 78.7-vs-81.7 case, this does not change the gate outcome either way** — SPGI fails the 80.0+ gate decisively under both readings.

### FCF Quality (10% weight)

```
FCF/NI (TTM) = $5,556M / $4,777M = 116.31%
FCFQuality_Score = clamp(((1.1631 − 0.40)/0.60)×100, 0, 100) = clamp(127.2, 0, 100) = 100.0
```

### Quality Score — Final

```
Quality Score = (69.99×0.25) + (88.09×0.15) + (54.43×0.20) + (63.24×0.15) + (40.0×0.15) + (100.0×0.10)
              = 17.4975 + 13.2135 + 10.886 + 9.486 + 6.0 + 10.0
              = 67.0830 → rounds to 67.1
```

# Quality Score = 67.1 — FAILS the 80.0+ gate decisively (≈13 points short — not a close call, and not sensitive to the one moat judgment call noted above).

**This is SPGI's first-ever computed Quality Score.** No hard disqualifier fires — the failure is purely the weighted average, driven mainly by a thin Moat_Score (40.0, only 2 of 5 signals cited-true) and a still-elevated (IHS-Markit-merger-legacy) leverage/ROIC profile (BalanceSheet_Score 63.24, ROIC 11.99% below the 15% Phase-01 threshold), not by any fresh fundamental deterioration — revenue growth is *accelerating* (8-K/10-Q cited), cash generation remains excellent (FCF/NI 116%), and there's no margin compression or covenant issue. Per [rescore.md](../.claude/commands/rescore.md) step 3: *"a held position dropping below the gate is itself a signal worth surfacing, even though existing holdings aren't retroactively force-exited on quality alone."* Per the established practice for existing holdings whose Quality Score fails the gate (see the AMZN/GOOG/MSFT/NKE/NOW 2026-07 sessions), the Valuation Score and a **reference-only** Composite Score are still computed below, explicitly flagged as not to be acted on at face value given the gate failure.

---

## 7. SPGI — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 21.542 = 4.642%
Spread = EY − 10Y Treasury = 4.642% − 4.48% = +0.162%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.162%, ~1.34pp short) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.48% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for SPGI = +10**

---

## 8. SPGI — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 4.267/10), 0, 100) = 57.33
```
→ Contribution: 57.33 × 0.40 = **22.93**

**EV/EBIT — 25% + 15% (PEG redistributed, §3 flag 5) = 40% weight**
```
EV/EBIT = $142,173.44M ÷ $6,945M = 20.47×
EV/EBIT_Score = clamp((20.47 − 12)/23 × 100, 0, 100) = 36.83
```
→ Contribution: 36.83 × 0.40 = **14.73**

**Forward PE (primary formula — 5yr range available, consistent with this ticker's own 06-20 precedent, which explicitly used the primary/range formula rather than the fallback) — 20% weight**
```
Forward PE = 21.542×; 5yr range: low 20.64×, high 32.21×, avg 28.48×
FwdPE_Score (primary) = clamp((21.542 − 20.64)/(32.21 − 20.64) × 100, 0, 100) = 7.81
Historical PE Modifier (Upgrade 2): deviation vs 5yr avg = (21.542 − 28.48)/28.48 = −24.37% → >20% below → −10
FwdPE_Score = clamp(7.81 − 10, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — 15% weight: N/A this session** (not a qualifying Fast Grower — §3 flag 5) — weight redistributed to EV/EBIT above.

**Raw weighted score:**
```
= 22.93 + 14.73 + 0.0 = 37.66
```
**+ Rate Modifier (+10) = 47.66** (before the Upside/Downside Modifier)

---

## 9. SPGI — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture — same fixed-EPS/varying-exit-multiple convention as the 06-20 session, refreshed with this session's directly-sourced forward EPS ($20.42, `yfinance` `forwardEps`) rather than the 06-20 session's backed-out figure (~$22.23, derived from price÷forward-PE, a less direct source):**

| Scenario | Weight | Exit PE | Rationale | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | 30.0× | Near the 5yr high (32.21×); re-rate scenario supported by the cited Ratings Billed Issuance +28% and Indices AUM growth +14% (both §6) | $20.42 × 30.0 = **$612.60** |
| **Base** | 50% | 26.5× | Near the 5yr average (28.48×), a modest discount reflecting residual Ratings cyclicality — cross-checks well against the broader-coverage analyst consensus ($532–$562, §3 flag 4) | $20.42 × 26.5 = **$541.13** |
| **Bear** | 25% | 17.5× | Near the 5yr low (20.64×) — ratings-segment issuance-slump/recession scenario, same framing as the 06-20 session | $20.42 × 17.5 = **$357.35** |

```
PW Fair Value = 0.25×612.60 + 0.50×541.13 + 0.25×357.35 = $513.05
```
**Guardrail 2 check (scenario-weighted, not the rosy point):** Base ($541.13) sits inside the broader-coverage analyst consensus band ($532–$562, per §3 flag 4) — passes. Bear ($357.35) sits essentially at the 52-week low ($359.36) — a real, underwritten trough, not glossed over.

**Step 1 — Expected annual return E.**
```
Gap Upside %     = ($513.05 ÷ $439.89) − 1                = +16.63%
Catalyst window  = 2.0 years (Rule 10 — issuance-normalization thesis, now partially corroborated
                    in-progress by the cited +28% Billed Issuance print; kept at the conservative
                    2yr window rather than shortened on that strength alone)
Annualized gap   = 16.63% ÷ 2.0                            = +8.32%
Intrinsic growth = +10%/yr (kept conservative vs. both the 11.11% revenue CAGR and the raw ~29%
                   NTM-consensus EPS jump implied by $20.42 vs. TTM EPS ~$15.80 — much of that
                   raw jump reflects the buyback-driven share-count decline rather than pure
                   organic growth; same conservative figure as the 06-20 session, unchanged)
Shareholder yield = 0.88% dividend + 2.18% net buyback     = +3.06%

E = 8.32% + 10.0% + 3.06% = +21.38%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 21.38% ≥ H → M = −15 × clamp((21.38 − 10)/15, 0, 1) = −15 × clamp(0.759, 0, 1) = −15 × 0.759 = −11.38
```

**Guardrail checks:**
1. **Catalyst:** documented (Ratings issuance-volume normalization, now partly evidenced in-progress), within the 18–24 month window → upside credit allowed, not capped. ✓
2. **Scenario-weighted, not the rosy point:** ✓ (Base cross-checks against the broader consensus band; Bear sits at the 52-week low.)
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** −11.38 sits within bounds. ✓

---

## 10. SPGI — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (37.66) + Rate Modifier (+10) + Upside/Downside (−11.38)
                       = 36.28 → rounds to 36.3
```

| | Value |
|---|---|
| Raw weighted | 37.66 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −11.38 (E = +21.38%) |
| **FINAL VALUATION SCORE** | **36.3** |
| Prior valuation score | 33.4 (06-20) |
| **Quality Score** | **67.1 (FAILS 80.0+ gate — see §6)** |

**Valuation Score band: 36.3 → 30.0–49.9 "Cheap" → nominally BUY, Standard position (3–5%)** — this alone, on the raw Valuation Score, would be the action absent the Quality Score question, and would also be the recommendation absent the order-setup check in §11.

**Composite Score — reference only, per the established practice for a Quality-Score-gate failure on an existing holding (AMZN/GOOG/MSFT/NKE/NOW 2026-07 sessions):**
```
Composite Score = 0.50×(100 − 67.1) + 0.50×36.3 = 0.50×32.9 + 0.50×36.3 = 16.45 + 18.15 = 34.6
```
**Composite Score = 34.6** — lands in the same "BUY — Standard position 3–5%" band (30.0–49.9) as the raw Valuation Score. **Unlike NOW's or NKE's sessions, blending in the failed-gate Quality Score doesn't dramatically pull the number into a materially more-attractive band here** — 34.6 (composite) vs. 36.3 (raw valuation) is a small, same-band shift, not a "false green light" jump across bands. Still, per the same governing principle, **this Composite Score is NOT being adopted to drive the action recommendation below** — shown only for the record, no black box.

---

## 11. SPGI — Action Recommendation

**Order setup — shown for completeness, testing the nominal 30.0–49.9 "Cheap" band (existing holdings' quality-gate failures don't force an exit per [rescore.md](../.claude/commands/rescore.md)):**
```
Blended Fair Value (= PW FV):                    $513.05
Margin of Safety (30.0–49.9 band):               25% or 30%

BUY PRICE @ 25% MoS:                             $513.05 × 0.75 = $384.79
BUY PRICE @ 30% MoS:                             $513.05 × 0.70 = $359.14
PRIMARY SELL TARGET:                             $513.05
BULL-CASE TRIM TARGET (bull × 0.90):             $612.60 × 0.90 = $551.34

STOP LOSS @ 25% MoS buy, 25% stop:                $384.79 × 0.75 = $288.59
STOP LOSS @ 25% MoS buy, 30% stop:                $384.79 × 0.70 = $269.35
STOP LOSS @ 30% MoS buy, 20% stop:                $359.14 × 0.80 = $287.31
STOP LOSS @ 30% MoS buy, 30% stop:                $359.14 × 0.70 = $251.40

R/R @ 25% MoS buy / 25% stop  = (513.05−384.79)/(384.79−288.59) = 128.26/96.20  = 1.333:1  ❌ below 2:1
R/R @ 30% MoS buy / 20% stop  = (513.05−359.14)/(359.14−287.31) = 153.91/71.83 = 2.142:1  ✅ clears 2:1
R/R @ live price / 25% stop   = (513.05−439.89)/(439.89−329.92) = 73.16/109.97 = 0.665:1  ❌ far below 2:1
```
**Only the deep 30% MoS + tight 20% stop combination clears the 2:1 minimum** — the same narrow-window pattern found in the 06-20 session (which required 30% MoS + 20% stop, buy $356.30). This session's equivalent qualifying entry is **$359.14**, roughly **18.4% below** the live price of $439.89.

**Position cap check:** 0.74% is nowhere near the 15% hard cap (Upgrade 7) — not a binding constraint.

**Net: HOLD the existing 0.74%-weight SPGI position. Do NOT add fresh capital at the live price of $439.89.** Two independent reasons, either one sufficient alone:

1. **R/R gate fails at the live price and at every standard MoS/stop combination except one narrow, ~18%-lower limit-order zone** ($359.14 buy / $287.31 stop, 2.14:1). Per Rule 6, R/R below 2:1 = do not enter at the live price.
2. **Quality Watch escalation (Phase 04, new this session):** SPGI's first-ever computed Quality Score (67.1) fails the 80.0+ gate decisively (§6). This does **not** meet the Phase 06 Full Exit bar — none of the four valid triggers apply (no structural margin break, no thesis-broken TAM shrinkage — if anything TAM/growth evidence is *positive* this session, no balance-sheet crisis, and the score is nowhere near the sustained-90+ extreme-overvaluation trigger). The gate failure here reads as a **quality-scoring-methodology outcome** (thin Moat_Score, IHS-Markit-merger-legacy leverage/ROIC) rather than a sign the business has deteriorated — revenue growth is accelerating and cash conversion remains excellent.

**Recommend the user consider (as an open item, not decided or written here — `override-log.md` is out of scope for this session) whether to log a Human Override entry** mirroring the NOW/ZS precedent, given the newly-quantified Quality gate failure on a held position.

**The Mobility Global spinoff (§4) independently means this session's exact scores should be treated as provisional** — see §3 flag 2's sensitivity check (stays in-band, but the true post-spin score is likely a few points higher/more-expensive than the 36.3 scored here) and the near-term follow-up trigger below.

---

## 12. Next Review Trigger

- **Near-term, high priority: S&P Global's pro forma continuing-operations (ex-Mobility) financial statements**, expected via SEC 8-K amendment within 4 business days of the 2026-07-01 distribution (i.e. on or about **2026-07-07**). Will allow this session's FCF Yield / EV-EBIT / Forward-PE sub-scores to be recomputed on a clean, apples-to-apples continuing-operations basis rather than the consolidated-vs-post-spin-price approximation used here (§3 flag 2 — likely modestly understating the true post-spin valuation score, though the action band held steady in the sensitivity check).
- **Q2 FY2026 earnings**, expected ~ late July 2026 (based on the 2025 cadence, e.g. 2025-07-31) — first quarter to reflect actual continuing (ex-Mobility) segment reporting.
- **Saugata Saha's (President, Market Intelligence) departure**, effective 2026-07-30 — watch for a successor announcement and any related execution disruption in the Market Intelligence segment.
- **Open item (new, this session): the Quality Score gate question (§6)** — recommend the user consider a Human Override log entry (mirroring NOW/ZS), or seek a harder, SPGI-specific pricing-power citation to revisit the "Brand premium" moat signal (would not flip the gate outcome per the sensitivity note, but would sharpen the record).
- **Standing Rule 9 triggers:** guidance revision, further M&A, a >15% unexplained price move, or the next Rate Environment Gate quarterly refresh.
- If a fill occurs via the narrow $359.14 limit-order zone, or if the pro forma refresh moves the score meaningfully, re-derive immediately rather than waiting for the routine cadence.

---

## Glossary

| Term | Meaning |
|---|---|
| **8-K (Form 8-K)** | A US company's "current report" disclosing a material event (like an earnings release or a corporate separation) between its regular quarterly/annual filings. |
| **Adjusted EBITDA** | A company's own non-GAAP variant of EBITDA with further management add-backs — not directly comparable to a GAAP-derived EBITDA computed from filed financials without those add-backs; used here only as an approximation when netting Mobility's disclosed figures against SPGI's consolidated GAAP-derived EBITDA (§3). |
| **CAGR** | Compound Annual Growth Rate. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate; shown as a **reference-only, not-adopted** number for SPGI this session (67.1 Quality Score fails the gate). |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — SPGI does not qualify this session (an EPS decline mid-window breaks the run). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Form 10 (registration statement)** | The SEC filing required to register a spun-off entity's stock before distribution, containing that entity's own historical/pro forma financials — the source for Mobility Global's standalone figures used in §3/§4. |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. |
| **Human Override** | A position held outside the framework's own rules — tracked in `override-log.md`; flagged (not adopted) as an open item for SPGI this session. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **NRSRO (Nationally Recognized Statistical Rating Organization)** | The SEC-designated status a credit-rating agency must hold for its ratings to be usable in regulatory capital rules and named in covenants/mandates — the regulatory entrenchment behind SPGI's "market share" and "switching costs" moat signals. |
| **NTM** | Next Twelve Months. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **Pro forma (financial statements)** | Restated financial statements showing results as if a structural change (e.g. a spinoff) had already been reflected — S&P Global's are due ~2026-07-07 for the Mobility separation, not yet filed as of this session. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. SPGI's first-ever computation this session: 67.1 (fails the gate decisively). |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; require a minimum 2:1 risk/reward before entering; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **Spin-off** | A corporate transaction separating part of a business into a new, independently-traded public company via a pro-rata share distribution — creates a data-integrity trap where post-spinoff price/share count and pre-spinoff trailing financials don't mix cleanly until restated. The central issue of this session (Mobility Global/MBGL). |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

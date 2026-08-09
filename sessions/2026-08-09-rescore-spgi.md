# RESCORE — SPGI (S&P Global Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Trigger:** [GitHub issue #405](https://github.com/cloxy777/investment-framework/issues/405) — "RESCORE: SPGI - earnings released 2026-07-28." Significantly overdue: earnings released 2026-07-28, this session runs 2026-08-09 (12 days late, vs. the operating calendar's "within 3 business days" target).
**Date:** 2026-08-09 (Sunday — markets closed; most recent trading session 2026-08-07, Friday)
**10Y US Treasury Yield:** 4.69% (FRED `DGS10`, most recent posted value, 2026-08-06 — 2026-08-07 not yet posted by FRED/the Fed's H.15 release at fetch time; see §2 flag 1 for a caveat on this)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** SPGI **36.3** (Valuation) / **67.1** (Quality) / **34.6** (Composite, reference only, gate fail) — 2026-07-05, [sessions/2026-07-05-rescore-spgi.md](2026-07-05-rescore-spgi.md).
**Current SPGI portfolio weight:** 0.68% per [holdings.md](../portfolio/holdings.md) — comfortably under the 15% hard cap (Upgrade 7); not recomputed this session (weight refresh is `/sync-portfolio`'s job).

> *Jargon decoded on first use — see closing Glossary section. SPGI is the ticker behind this framework's costliest documented pricing error (the May 2026 "SPGI Price Inference Error," [fair-value-methodology.md](../framework/fair-value-methodology.md)) — extra care taken below on Rule 0, especially given this session's Mobility-spinoff data-integrity complications.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$408.19** | Two independent sources agree exactly: IBKR `get_price_history` daily close (contract_id 229629397, NYSE), most recent bar = **2026-08-07** (Friday; markets closed for the weekend as of this Sunday session); and `yfinance` (`requests.Session()` transport, see §2) `currentPrice`/`regularMarketPrice`, both **$408.19**. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$409.50** at timestamp 2026-08-07 23:29:34 UTC (7:29pm ET) — **after** the 4:00pm ET regular-session close, i.e. a genuine after-hours print (+1.05% vs. the prior close of $405.24, per the snapshot's own `change` field), not a stale/frozen quote. Not adopted as the primary Rule-0 price: it's a single-source, thin-volume after-hours trade, whereas $408.19 is the actual regular-session closing print corroborated by two independent sources to the cent. Flagged transparently, not silently substituted. |
| 52-week range | $359.36 – $543.25 | IBKR `misc_statistics` |
| Year-to-date change | −16.78% | IBKR `year_to_date_change` |
| Price vs. 07-05 review ($439.89) | **−7.20%** | Under the 15% Rule 9 "unexplained move" threshold, and explained regardless — see §2/§5: the decline tracks the post-Q2-earnings selloff (confusion over the pro forma EPS reporting basis during the Mobility transition, plus softer-than-some-analysts'-hoped organic growth guidance), a real fundamental reaction, not an unexplained move. |
| Dividend (declared, Q2 2026 10-Q + Q2 earnings release) | $0.97/share quarterly (unchanged) → **0.95% yield** ($3.88 annualized ÷ $408.19) | SEC 10-Q + Q2 2026 earnings release, both confirm "$0.97" quarterly rate; matches `yfinance` `dividendRate` ($3.88) and `dividendYield` (0.95%) exactly. IBKR's snapshot showed 0.89% — a minor vendor variance, noted not adopted. |
| Analyst consensus PT (Rule 0 Step 4, bull-case sanity check only) | mean **$516.95** (20 analysts, `yfinance`) / mean **$532.81** (21 analysts, stockanalysis.com aggregate, high $575 / low $480) / mean **$533.59** cited by a third outlet post-earnings | Broadly consistent across sources this session (no thin-sample outlier issue like 07-05's 3-analyst read) — see §5. |

---

## 2. Data Gaps / Flags

1. **`yfinance` initially failed with the same recurring `curl_cffi` TLS-impersonation `SSLError` documented across this repo's recent sessions.** Worked around with the documented `requests.Session()` transport fix (plain `requests`, standard browser `User-Agent`, passed into `yf.Ticker("SPGI", session=sess)`) — same pattern used in the 2026-08-07 UBER session. Succeeded on first retry. All `yfinance` figures below came from this working session. `10Y Treasury`: FRED's own CSV export currently posts through 2026-08-06 (4.69%) — a web search suggests the 10Y fell further intraday on 2026-08-07 (~4.60%, on a weak jobs report), but this isn't yet confirmed via the official FRED/Federal Reserve H.15 series as of this session's fetch, so **4.69% (the last officially posted value) is used, not the unconfirmed lower figure** — flagged, not silently adopted.

2. **EV/EBIT and Balance Sheet sub-score inputs — small source variances, flagged and resolved transparently:**
   - `yfinance`'s own quarterly-balance-sheet "Total Debt" field for 2026-06-30 reads **$15,622M**, vs. the SEC 10-Q's own stated **"Total debt outstanding was $15,170 million"** (short-term $2,572M + long-term $12,598M). Used the 10-Q's authoritative, directly-filed figure ($15,170M) rather than `yfinance`'s aggregate (likely including a different lease-liability or other-debt convention not disclosed by the vendor) — consistent with the 07-05 session's own precedent of preferring a transparently-sourced figure over an opaque vendor aggregate. Using the vendor figure instead would move EV/EBIT to 18.35× (vs. 18.29× used) — immaterial, non-band-changing.
   - Total Stockholders' Equity: `yfinance`'s quarterly balance sheet shows **$31,501M** (2026-06-30); an independent SEC-10-Q-text extraction returned **$31,616M** — a ~0.4% variance, likely reflecting slightly different line-item selection in the extraction. Used `yfinance`'s structured figure for internal consistency with the rest of this session's computations (cross-checked as in the same ballpark).
   - `yfinance`'s own `info["freeCashflow"]` aggregate field reads **$5,448M** (TTM), while summing the "Free Cash Flow" row directly from `t.quarterly_cashflow` across the same four quarters gives **$5,573M** — an internal `yfinance` inconsistency (the quarterly-row sum reconciles exactly with Operating Cash Flow − CapEx, $5,729M − $156M = $5,573M, while the `info` aggregate does not reconcile with any other sourced figure). Used the quarterly-row sum (the more internally consistent, fully-reconciling figure) throughout, flagged rather than silently picked.

3. **⚠️ MAJOR — Mobility Global spinoff data-integrity issue, materially advanced but not fully resolved this session.** Unlike the 07-05 session (which had only Mobility's own Form-10 standalone figures to approximate an ex-Mobility basis), **this session has real, company-disclosed pro forma continuing-operations figures for Q2 2026**, since S&P Global's Q2 2026 earnings release (SEC 8-K, Exhibit 99.1, filed 2026-07-28) explicitly presents both GAAP (Mobility-inclusive) and pro forma continuing-operations (ex-Mobility) results side by side. Full detail and how this session used them: **§5 below.** The core remaining gap: the pro forma split is disclosed **only for Q2 2026 vs. its Q2 2025 comparative** — not for the other three trailing quarters (Q3'25, Q4'25, Q1'26) needed to build a genuine ex-Mobility TTM. Per the 10-Q's own words: *"The results of Mobility are included through June 30, 2026. Beginning with the third quarter of 2026, the historical financial results of Mobility through June 30, 2026 will be reflected in our consolidated financial statements as discontinued operations in accordance with U.S. GAAP for all periods."* This means **Q3 2026's earnings release (expected ~late October 2026, see §11) will be the first quarter where a genuinely clean, fully-restated ex-Mobility TTM is directly reportable** — flagged as a high-priority near-term follow-up. This session's primary TTM figures (FCF Yield, EV/EBIT, Balance Sheet) use the GAAP consolidated basis (Q3'25–Q2'26, all four quarters still Mobility-inclusive per the 10-Q's own confirmation above), paired against a post-spin (Mobility-excluded) market cap — the same data-integrity mismatch flagged in 07-05, now entering its second quarter. Direction: this likely modestly **understates** how expensive the "true" ex-Mobility multiples are (EBIT/FCF are somewhat inflated by Mobility's now-departed contribution, while the price/market cap no longer reflects it) — see the annualized-run-rate sensitivity check in §6, which converges closely with the primary figures for EV/EBIT specifically, a reassuring cross-check not available in 07-05.

4. **Forward PE — dual-anchor methodology change this session, shown transparently (a deliberate, reasoned choice, not an ad hoc pick).** Prior SPGI sessions used a single "Forward EPS (NTM)" figure for both the Forward PE sub-score and the Upside/Downside Modifier's scenario architecture. This session found real evidence that a single anchor no longer cleanly serves both purposes post-spinoff — see the full reasoning in §7 (Forward PE) and §9 (Upside/Downside Modifier). **A sensitivity check using the single-anchor convention is also shown in §9** — both approaches land in the same action band (30.0–49.9, "Cheap"), so this methodological choice is not band-changing, but it does move the exact score materially (31.3 primary vs. 37.6 sensitivity) and is flagged prominently rather than picked silently.

5. **PEG / Fast-Grower eligibility — re-confirmed NOT applicable**, consistent with every prior SPGI session. SPGI is a mature stalwart (an outright FY2023 EPS decline, IHS-Markit-merger-related, breaks any clean 3-consecutive-year >15%/yr run) — Upgrade 3 explicitly excludes stalwarts regardless. PEG's 15% weight redistributed to EV/EBIT (→ 40%), unchanged.

6. **Management change (Saugata Saha) — departure completed as scheduled, no successor announced yet.** Confirmed via web search: Saha's departure (announced 2026-05-26, effective 2026-07-30) has now occurred on schedule. No successor for the Market Intelligence presidency has been publicly named as of this session — still an open item, carried forward, not a new trigger this session (already flagged and assessed 07-05).

No data was invented anywhere below. Every fallback/flag is the documented one from the framework, not an ad hoc substitute.

---

## 3. Rule 9 Trigger Check (2026-07-05 → 2026-08-09)

| Trigger | Found? | Detail |
|---|---|---|
| **Quarterly earnings** | **Yes — the driving trigger** | Q2 2026 results released 2026-07-28 (SEC 8-K, Exhibit 99.1) — the first earnings release since the Mobility Global spinoff closed (2026-07-01). Full detail in §5. |
| Guidance revision | Partial | Full-year 2026 organic constant-currency revenue growth guidance was **maintained** at 6.0–8.0% (not raised — one sell-side desk, Jefferies, flagged disappointment that it wasn't raised above their own 8.8% estimate). Margin-expansion guidance and the share buyback target were both **raised** (buyback: $5B FY2025 actual pace → >$7B FY2026 target, up ~$3B from the prior target). Treated as part of the standard quarterly earnings trigger, not a separate distinct Rule 9 event. |
| Material M&A | No | |
| Management change | No *new* trigger this session — Saugata Saha's already-flagged (07-05) departure completed on schedule 2026-07-30; no successor named yet (§2 flag 6). |
| Macro shift | No | 10Y ticked from 4.48% (07-05) to 4.69% (08-06, most recent posted) — still inside the 3.5–5% bracket, no Rate Regime bracket change. |
| >15% unexplained price move | No | −7.20% over 5 weeks (§1), under the 15% threshold and explained by the post-earnings reaction (§5), not unexplained. |

**Conclusion:** a full re-derivation is warranted — both the routine post-earnings schedule and the ongoing Mobility-spinoff transition (now in its second quarter, with materially better data available than 07-05) justify a complete recompute rather than a light-touch refresh.

---

## 4. Q2 2026 Earnings — What Happened and Why the Stock Fell

S&P Global reported Q2 2026 results on 2026-07-28 (SEC 8-K, Exhibit 99.1). Headline **GAAP** figures (still Mobility-inclusive per the 10-Q's own confirmation, §2 flag 3): revenue $4,146M (+10% YoY), operating profit $1,812M (+17%), net income $1,217M (+14%), diluted EPS $4.12 (+18%). On a **pro forma continuing-operations (ex-Mobility)** basis — the company's own disclosed, real figures, not this framework's estimate: revenue $3,678M (+11% YoY vs. $3,317M in Q2 2025), pro forma diluted EPS $4.08 (+26% YoY vs. $3.23), adjusted (non-GAAP) diluted EPS $4.83 (+23% YoY vs. $3.92). Segment revenue (continuing-operations basis): **Ratings $1,339M (+17% YoY)**, **Indices $534M (+20% YoY, its 13th consecutive record quarter)**, Market Intelligence (adjusted) $1,235M (+6%), Energy (adjusted) $623M (+3%).

**Despite the strong headline numbers, the stock declined post-earnings** — independently verified via web search, not assumed: premarket shares fell as much as 5.2% (to ~$416.94) on a mix of (a) genuine information-asymmetry/confusion, as some headlines initially compared the new pro forma EPS figure ($4.08) against a consensus estimate still built on the old, Mobility-inclusive basis, and (b) real disappointment that full-year organic growth guidance was *maintained* at 6–8% rather than raised (Jefferies specifically cited an 8.8% in-house projection that guidance fell short of). This is the explanation for the −7.20% price decline since 07-05 (§1/§3) — a real, cited fundamental reaction, not an unexplained move, and not itself a scored input (headline reaction ≠ scored data, per Rule 0/Rule 6 discipline).

**Full-year 2026 guidance (continuing operations):** revenue growth 5.9–7.9% (organic CC 6.0–8.0%, maintained); operating margin expansion 335–360bps; adjusted operating margin expansion 35–60bps; GAAP diluted EPS $16.35–$16.60; adjusted diluted EPS $17.50–$17.75. **Not used as a scored input** (guidance is self-reported and deliberately excluded from the four weighted valuation sub-scores per valuation-scoring.md's "Why Forward Guidance Is Not a Sub-score") — cited here only for context and as a cross-check against the independently-sourced analyst consensus figures used below.

---

## 5. Mobility Spinoff — Continuing-Operations Data This Session (Advance on 07-05)

Per the 10-Q's own words (quoted in full in §2 flag 3): Q2 2026 GAAP figures **still include** Mobility (the spin closed 2026-07-01, one day after the quarter's 2026-06-30 close), and Mobility will only formally become "discontinued operations" (with **all** historical periods restated) starting with Q3 2026's reporting. This session is materially better-positioned than 07-05 because the company itself has now disclosed real pro forma continuing-operations figures for Q2 2026 (§4) — used as follows:

- **Analyst consensus EPS has already converged to a continuing-operations (ex-Mobility) basis**, independently confirmed via `yfinance`'s `eps_trend` time series: the current-fiscal-year ("0y"/FY2026) consensus EPS dropped from $19.63 (90 days ago) → $19.62 (60d) → $18.83 (30d) → $17.83 (7d) → **$17.834 (current, 16 analysts)** — a clean, monotonic downward revision path tracking the market's digestion of the spinoff, converging almost exactly to the company's own FY2026 adjusted-EPS guidance midpoint ($17.625). The next-fiscal-year ("+1y"/FY2027) consensus shows the same pattern: $22.21 (90d) → $22.20 (60d) → $20.42 (30d) → $20.22 (7d) → **$20.220 (current, 22 analysts, +13.38% YoY growth)**. **Both figures are used below, on different bases** — see §7 and §9 for exactly how and why.
- **EV/EBIT sensitivity cross-check (new this session, more grounded than 07-05's Form-10-based approximation):** annualizing Q2 2026's disclosed pro forma continuing-operations GAAP operating profit ($1,757M × 4 = $7,028M) against this session's primary EV ($131,370.41M, §6) gives an EV/EBIT of **18.69×** — versus the primary (GAAP-consolidated-TTM-basis) figure of **18.29×** computed in §7. **These two independently-derived figures converge closely (within 2.2%)**, a materially better cross-check than 07-05 achieved, and gives real confidence the primary EV/EBIT sub-score isn't badly distorted by the Mobility-transition mismatch this particular quarter.

---

## 6. SPGI — Inputs Collected (fresh this session, `yfinance` via `requests.Session()`, cross-checked against the SEC 10-Q and 8-K earnings release)

**Sector:** Financials — Financial Data, Ratings & Analytics (mature wide-moat duopoly with Moody's, not a Fast Grower)

**TTM figures (Q3'25 + Q4'25 + Q1'26 + Q2'26 — GAAP consolidated, still Mobility-inclusive per §2 flag 3):**

| Item | Value | Source |
|---|---|---|
| Shares outstanding (2026-06-30) | 294,800,000 | `yfinance` quarterly balance sheet / SEC 10-Q |
| **Market Cap** | 294,800,000 × $408.19 = **$120,334.41M** | Computed |
| Total debt (2026-06-30, 10-Q authoritative) | $15,170M | SEC 10-Q — see §2 flag 2 for the `yfinance` variance ($15,622M, not used) |
| Cash and cash equivalents (2026-06-30) | $4,134M | SEC 10-Q, matches `yfinance` exactly |
| **Net Debt** | $15,170M − $4,134M = **$11,036M** | Computed |
| **EV (from-scratch)** | $120,334.41M + $11,036M = **$131,370.41M** | Computed |
| TTM Revenue (Q3'25–Q2'26) | 3,888+3,916+4,171+4,146 = **$16,121M** | `yfinance` quarterly financials rollforward |
| TTM Gross Profit | 2,767+2,746+2,936+2,981 = $11,430M | Same — **Gross margin 70.90%** |
| TTM EBIT | 1,677+1,685+2,004+1,816 = **$7,182M** | Same |
| TTM Net Income | 1,176+1,134+1,395+1,217 = **$4,922M** — **Net margin 30.53%** | Same — matches `yfinance` `netIncomeToCommon` ($4,923M) essentially exactly |
| TTM Pretax Income / Tax Provision | $6,866M / $1,550M | Same — **effective tax rate 22.58%** |
| **EBITDA (TTM)** | Q3'25 1,971+Q4'25 1,982+Q1'26 2,311+Q2'26 2,124 = **$8,388M** | `yfinance` quarterly financials — cross-checked: EBIT ($7,182M) + D&A ($1,206M) = $8,388M exactly |
| TTM Operating Cash Flow | 1,505+1,748+1,037+1,439 = $5,729M | `yfinance` quarterly cashflow |
| TTM CapEx | −45−46−27−38 = −$156M | Same |
| **TTM FCF** | 1,460+1,702+1,010+1,401 = **$5,573M** | `yfinance` quarterly cashflow "Free Cash Flow" row — reconciles exactly with OCF−CapEx; see §2 flag 2 for the `info`-aggregate variance (not used) |
| **FCF Yield** | $5,573M ÷ $120,334.41M = **4.631%** | Computed |
| **FCF/NI (TTM)** | $5,573M ÷ $4,922M = **113.23%** | Computed |
| Total Stockholders' Equity (2026-06-30) | $31,501M | `yfinance` quarterly balance sheet — see §2 flag 2 |
| **Invested Capital** (Debt+Equity convention) | $15,170M + $31,501M = **$46,671M** | Computed |
| **NOPAT** | $7,182M × (1−0.2258) = **$5,560.5M** | Computed |
| **ROIC (TTM)** | $5,560.5M ÷ $46,671M = **11.91%** | Computed — below the 15% Phase-01 threshold on a reported basis, consistent with the same IHS-Markit-merger-legacy invested-capital-base dynamic flagged every prior session, not a fresh deterioration (07-05: 11.99%) |
| Forward EPS (FY2026 consensus, "0y", 16 analysts) | $17.834 | `yfinance` `earnings_estimate` — used for **Forward PE sub-score** (§7) |
| Forward EPS (FY2027 consensus, "+1y", 22 analysts, +13.38% YoY) | $20.220 | `yfinance` `earnings_estimate` — used for the **Upside/Downside scenario architecture** (§9) |
| **Forward PE** | $408.19 ÷ $17.834 = **22.89×** | Computed — see §7 for the dual-anchor rationale |
| 5yr avg/low/high PE | avg **28.05×**, low **20.64×**, high **32.21×** (n=20 quarters, 2021-10 to 2026-07) | `get_earnings_dates` + price-history reconstruction |
| Revenue 3yr CAGR (FY2022 $11,181M → FY2025 $15,336M) | **11.11%** | `yfinance` annual financials — most recent completed-fiscal-year window (FY2026 incomplete); unchanged from 07-05, since FY2025 is already-reported, fixed history |
| Dividend yield | 0.95% ($0.97/qtr × 4 ÷ $408.19) | SEC 10-Q + Q2 earnings release, computed |
| Net buyback yield | **3.46%** (diluted shares: Q2'26 295.5M vs. Q2'25 306.1M, −3.46% YoY) | `yfinance` quarterly financials — a materially faster pace than 07-05's cited 2.18% (FY2025-annual basis), consistent with the company's own disclosed acceleration (FY2025 $5.0B buyback → FY2026 target raised to >$7B, of which $1.5B already executed in H1 2026) |
| Annual FCF/NI (context, all pass the 70% hard-disqualifier floor) | FY2022 77.40% / FY2023 135.83% / FY2024 144.47% / FY2025 122.03% | Unchanged from 07-05 (fixed, already-reported history) |

---

## 7. SPGI — Quality Score (2026-06-29 methodology)

**Hard disqualifier check (rolling window, per the [2026-08-05 clarification](../framework/quality-scoring.md)):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | Every year FY2022–2025 and TTM (113.23%) ≥70% (see §6) | disqualify if <70% for 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | **1.316×** | disqualify if >2.5× (standard) | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FCF-positive every year FY2022–2025 and TTM | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight)

```
Net Margin (TTM)     = $4,922M / $16,121M = 30.53%
NetMargin_Component  = clamp((30.53/30)×100, 0, 100) = 100.0   (clamped from 101.77)

ROIC (TTM)            = $5,560.5M / $46,671M = 11.91%
ROIC_Component        = clamp((11.91/30)×100, 0, 100) = 39.71

Profitability_Score   = (100.0 + 39.71) / 2 = 69.86   (no FCF cap — FCF-positive every year on record)
```

### Margins (15% weight)

```
Gross Margin (TTM) = 70.90%
GrossMargin_Score = clamp((70.90/80)×100, 0, 100) = 88.63
```
No structural-trend bonus applicable — gross margin is already far above the 40% threshold the bonus specifically targets.

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $11,181M → FY2025 $15,336M) = 11.11%
Growth_Score = clamp((11.11/25)×100, 0, 100) = 44.44
```
**+10 (documented TAM expansion, cited, company-disclosed, even stronger than 07-05's citations):**
- Q2 2026 earnings release (SEC 8-K, 2026-07-28): **Ratings revenue +17% YoY**, **Indices revenue +20% YoY — its 13th consecutive record quarter** (§4), both real, already-materializing continuing-operations growth, not speculative.
- Consolidated GAAP revenue growth remains steady-to-accelerating at the headline level (FY2025 +8% → Q1 2026 +10.4% → Q2 2026 +10%), and the pro forma continuing-ops basis grew +11% YoY in Q2 2026 — no deceleration signal found.

No −10 deceleration penalty — growth is accelerating/steady on the evidence found, not decelerating (full-year *guidance* was maintained rather than raised, per §4, but guidance is not itself the growth-evidence input here; the actually-reported segment growth is unambiguously strong).
```
Growth_Score (with bonus) = clamp(44.44 + 10, 0, 100) = 54.44
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA (TTM) = $11,036M / $8,388M = 1.316×
BalanceSheet_Score = clamp(100×(1 − 1.316/4), 0, 100) = 67.11
```
Standard /4 denominator applies — same reasoning as every prior SPGI session (not clearly a "payment network or exchange" under the Upgrade 5 override, and doesn't need it regardless — 1.316× clears even the standard 2.5× gate comfortably).

### Moat Signal (15% weight) — carried forward, re-checked against this session's fresh evidence

| Signal | Marked | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Unchanged NRSRO regulatory-entrenchment reasoning (carried forward from every prior session), now reinforced by this session's fresh Q2 2026 Ratings +17% YoY revenue growth — real, current evidence of continued strength, not share loss. |
| Brand premium | **FALSE** | No company-disclosed, specific price-increase-without-volume-loss citation of the required type found this session either (same gap as every prior session) — carried forward FALSE. |
| Network effect | **FALSE** | Unchanged — no documented two-sided-marketplace mechanism found. |
| Switching costs | **TRUE** | Unchanged NRSRO/covenant-reference regulatory lock-in mechanism, carried forward. |
| Scale cost advantage | **FALSE** | Unchanged — no cost-per-unit data vs. Moody's/Fitch found. |

```
Moat_Score = (2/5) × 100 = 40.0
```
**Sensitivity note (unchanged from 07-05, shown transparently):** crediting "Brand premium" TRUE would raise Moat_Score to 60.0 and the Quality Score to ≈70.8 — still fails the 80.0+ gate decisively either way.

### FCF Quality (10% weight)

```
FCF/NI (TTM) = $5,573M / $4,922M = 113.23%
FCFQuality_Score = clamp(((1.1323 − 0.40)/0.60)×100, 0, 100) = clamp(122.05, 0, 100) = 100.0
```

### Quality Score — Final

```
Quality Score = (69.86×0.25) + (88.63×0.15) + (54.44×0.20) + (67.11×0.15) + (40.0×0.15) + (100.0×0.10)
              = 17.465 + 13.2945 + 10.888 + 10.0665 + 6.0 + 10.0
              = 67.714 → rounds to 67.7
```

# Quality Score = 67.7 — FAILS the 80.0+ gate decisively (≈12.3 points short — not a close call).

A modest **+0.6** improvement vs. 07-05's 67.1, driven mainly by an improved Balance Sheet sub-score (63.24 → 67.11, as Net Debt/EBITDA improved from 1.470× to 1.316×) and slightly better Margins (88.09 → 88.63), while Profitability drifted marginally down (69.99 → 69.86, ROIC essentially flat at ~11.9%) and Moat/FCF Quality/Growth are unchanged or flat. The gate failure remains driven by the same two structural factors as every prior session: a thin Moat_Score (40.0, only 2 of 5 signals cited-true) and a still-elevated (IHS-Markit-merger-legacy) ROIC profile — **not** by any fresh fundamental deterioration; revenue growth is real and accelerating at the segment level (Ratings +17%, Indices +20%), and cash generation remains excellent (FCF/NI 113%). Per rescore.md step 3: a held position dropping below the gate is a signal worth surfacing, even though existing holdings aren't retroactively force-exited on quality alone. Consistent with the established practice for a Quality-Score-gate failure on an existing holding, the Valuation Score and a **reference-only** Composite Score are still computed below, explicitly flagged as not to be acted on at face value.

---

## 8. SPGI — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 22.89 = 4.369%
Spread = EY − 10Y Treasury = 4.369% − 4.69% = −0.321%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (−0.321%, ~1.82pp short) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.69% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for SPGI = +10**

---

## 9. SPGI — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 4.631/10), 0, 100) = 53.69
```
→ Contribution: 53.69 × 0.40 = **21.476**

**EV/EBIT — 25% + 15% (PEG redistributed, §2 flag 5) = 40% weight**
```
EV/EBIT = $131,370.41M ÷ $7,182M = 18.29×
EV/EBIT_Score = clamp((18.29 − 12)/23 × 100, 0, 100) = 27.37
```
→ Contribution: 27.37 × 0.40 = **10.946**

**Forward PE — 20% weight — dual-anchor methodology (new this session, see §2 flag 4)**

*Why a new anchor was needed:* Prior SPGI sessions used a single "Forward EPS (NTM)" figure for both the Forward PE sub-score and the Upside/Downside scenario architecture. This session found real evidence that `yfinance`'s raw `info["forwardEps"]` field ($20.24) is actually the **next-fiscal-year (FY2027) consensus**, not a true blended next-twelve-months figure — confirmed by matching it against the `earnings_estimate` breakdown's "+1y" row. Meanwhile the **current-fiscal-year (FY2026, "0y") consensus ($17.834)** has, per §5, independently converged (via the `eps_trend` revision path) to a clean continuing-operations basis that closely matches the company's own FY2026 guidance. **This session uses the nearer-term, cleanly-matched FY2026 figure ($17.834) for the Forward PE sub-score** (the standard, near-term "price ÷ forward earnings" convention), while using the further-out FY2027 figure ($20.220) for the Upside/Downside Modifier's 2-year-forward scenario architecture (§10) — two different, individually well-justified purposes, both shown in full.

```
Forward PE = $408.19 ÷ $17.834 = 22.89×; 5yr range: low 20.64×, high 32.21×, avg 28.05×
FwdPE_Score (primary) = clamp((22.89 − 20.64)/(32.21 − 20.64) × 100, 0, 100) = 19.43
Historical PE Modifier (Upgrade 2): deviation vs 5yr avg = (22.89 − 28.05)/28.05 = −18.40%
  → not >20% below (and not within ±10%) → per established precedent (see the 2026-06-20 NKE
    session, −15.6% deviation → modifier 0), a deviation strictly between ±10% and ±20% takes
    modifier = 0, not a partial credit → Historical PE Modifier = 0
FwdPE_Score = 19.43
```
→ Contribution: 19.43 × 0.20 = **3.886**

**PEG — 15% weight: still N/A** (§2 flag 5) — redistributed to EV/EBIT above.

**Raw weighted score:**
```
= 21.476 + 10.946 + 3.886 = 36.308
```
**+ Rate Modifier (+10) = 46.308** (before the Upside/Downside Modifier)

---

## 10. SPGI — Upside/Downside Modifier (Expected-Return Modifier)

**Primary scenario architecture — FY2027 consensus EPS anchor ($20.220), for the reason explained in §9:** the catalyst window is 2 years (unchanged from every prior SPGI session — issuance-normalization thesis), and a 2-year-forward valuation is better anchored on a 2-year-forward earnings estimate than on the nearer-term FY2026 figure. **Guardrail-2 validation:** this choice was cross-checked, not assumed — using the FY2027 anchor, the Base-case fair value lands almost exactly inside this session's independently-sourced analyst consensus PT range ($516.95–$533.59, §1), a strong real-world confirmation the anchor choice is well-calibrated (see the sensitivity check below, where the alternative single-anchor convention's Base case falls well *below* the consensus range).

| Scenario | Weight | Exit PE | Rationale | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | 30.0× | Near the 5yr high (32.21×); re-rate scenario supported by the cited Ratings +17%/Indices +20% real Q2 2026 growth prints (§4/§7) | $20.220 × 30.0 = **$606.60** |
| **Base** | 50% | 26.0× | Modestly below the 5yr average (28.05×), reflecting residual Ratings-cycle/Market-Intelligence-succession uncertainty (§2 flag 6) — cross-checks well against the analyst consensus PT range ($516.95–$533.59) | $20.220 × 26.0 = **$525.72** |
| **Bear** | 25% | 17.5× | Deliberately below the actual 5yr low (20.64×) — a genuine stress case (ratings-segment issuance-slump/recession), same conservative convention as every prior SPGI session | $20.220 × 17.5 = **$353.85** |

```
PW Fair Value = 0.25×606.60 + 0.50×525.72 + 0.25×353.85 = $502.97
```
**Guardrail 2 check (scenario-weighted, not the rosy point):** Base ($525.72) sits almost exactly at the midpoint of the analyst consensus range ($516.95–$533.59) — passes cleanly. Bull ($606.60) sits modestly above the high end of the consensus range ($553–$575, stockanalysis.com), appropriately used only at 25% weight, not as the central estimate.

**Step 1 — Expected annual return E.**
```
Gap Upside %     = ($502.97 ÷ $408.19) − 1                = +23.22%
Catalyst window  = 2.0 years (Rule 10 — unchanged issuance-normalization thesis, now partially
                    corroborated by real Q2 2026 Ratings/Indices growth prints)
Annualized gap   = 23.22% ÷ 2.0                            = +11.61%
Intrinsic growth = +10%/yr (deliberately conservative vs. both the 11.11% revenue 3yr CAGR and
                   the raw +13.38%/yr FY2027-vs-FY2026 consensus EPS growth rate — kept at the
                   same conservative figure used in every prior SPGI session, since the FY2027
                   EPS anchor already used above for the scenario architecture itself embeds
                   ~1-2 years of forward earnings growth; adding the *full* raw growth figure on
                   top would risk double-counting some of that same growth twice)
Shareholder yield = 0.95% dividend + 3.46% net buyback     = +4.41%  (buyback pace materially
                   faster than 07-05's 2.18% — see §6, a real, company-disclosed acceleration)

E = 11.61% + 10.0% + 4.41% = +26.02%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 26.02% ≥ H → M = −15 × clamp((26.02 − 10)/15, 0, 1) = −15 × clamp(1.068, 0, 1) = −15.0 (floored)
```

**Guardrail checks:**
1. **Catalyst:** documented (Ratings/Indices growth, now real and in-progress per Q2 2026 prints), within the 18–24 month window → upside credit allowed, not capped. ✓
2. **Scenario-weighted, not the rosy point:** ✓ (Base cross-checks almost exactly against consensus; Bull sits modestly above, at only 25% weight.)
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** −15.0 sits at the floor. ✓

**Sensitivity check — single-anchor convention (FY2026 EPS, $17.834, for both the Forward PE sub-score AND the scenario architecture — the convention used in every SPGI session prior to this one):**
```
Bull = 17.834×30.0=$535.02 | Base = 17.834×26.0=$463.68 | Bear = 17.834×17.5=$312.10
PW FV (sensitivity) = 0.25×535.02 + 0.50×463.68 + 0.25×312.10 = $443.62
   (Base $463.68 sits notably below the $516.95–$533.59 consensus range — a weaker Guardrail-2
    fit than the primary dual-anchor approach above)
Gap % = 443.62/408.19 − 1 = +8.68%  |  Annualized = +4.34%
E (sensitivity) = 4.34 + 10.0 + 4.41 = +18.75%
M (sensitivity) = −15 × clamp((18.75−10)/15, 0, 1) = −15 × 0.583 = −8.75
```
This sensitivity is shown for transparency (no black box), not adopted — the dual-anchor primary approach is preferred because it independently cross-checks against real, externally-sourced analyst consensus data (Guardrail 2), which the single-anchor convention does not do as well.

---

## 11. SPGI — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE (primary) = Raw weighted (36.308) + Rate Modifier (+10) + Upside/Downside (−15.0)
                                 = 31.308 → rounds to 31.3

FINAL VALUATION SCORE (sensitivity, single-anchor) = 36.308 + 10 − 8.75 = 37.56 → 37.6
```

| | Primary (dual-anchor) | Sensitivity (single-anchor) |
|---|---|---|
| Raw weighted | 36.308 | 36.308 |
| Rate Gate | +10 | +10 |
| Upside/Downside Modifier | −15.0 | −8.75 |
| **FINAL VALUATION SCORE** | **31.3** | **37.6** |
| Prior valuation score (07-05) | 36.3 | 36.3 |
| **Quality Score** | **67.7** (FAILS 80.0+ gate) | — |

**Both land in the same 30.0–49.9 "Cheap" band** — the methodology choice (§9/§10) is not action-band-changing, only exact-score-changing. **31.3 (primary) is adopted below**, per the stronger Guardrail-2 fit reasoning in §10.

**Composite Score — reference only, per established practice for a Quality-Score-gate failure on an existing holding:**
```
Composite Score (primary) = 0.50×(100 − 67.7) + 0.50×31.3 = 0.50×32.3 + 0.50×31.3 = 16.15 + 15.65 = 31.8
Composite Score (sensitivity) = 0.50×32.3 + 0.50×37.6 = 16.15 + 18.80 = 34.95 → boundary (.X5 exact) rounds UP → 35.0
```
**Composite Score = 31.8** (primary; vs. 34.6 on 07-05 — modestly more attractive). **Not adopted to drive the action recommendation** — shown for the record only, per "no black box," consistent with every prior SPGI session's treatment of a Quality-gate failure.

---

## 12. SPGI — Action Recommendation

**Order setup — shown for completeness, testing the nominal 30.0–49.9 "Cheap" band (existing holdings' quality-gate failures don't force an exit per rescore.md):**
```
Blended Fair Value (= primary PW FV):            $502.97
Margin of Safety (30.0–49.9 band):               25% or 30%

BUY PRICE @ 25% MoS:                             $502.97 × 0.75 = $377.23
BUY PRICE @ 30% MoS:                             $502.97 × 0.70 = $352.08
PRIMARY SELL TARGET:                             $502.97
BULL-CASE TRIM TARGET (bull × 0.90):             $606.60 × 0.90 = $545.94

STOP LOSS @ 25% MoS buy, 25% stop:                $377.23 × 0.75 = $282.92
STOP LOSS @ 25% MoS buy, 30% stop:                $377.23 × 0.70 = $264.06
STOP LOSS @ 30% MoS buy, 20% stop:                $352.08 × 0.80 = $281.66
STOP LOSS @ 30% MoS buy, 30% stop:                $352.08 × 0.70 = $246.46

R/R @ 25% MoS buy / 25% stop  = (502.97−377.23)/(377.23−282.92) = 125.74/94.31  = 1.333:1  ❌ below 2:1
R/R @ 30% MoS buy / 20% stop  = (502.97−352.08)/(352.08−281.66) = 150.89/70.42  = 2.143:1  ✅ clears 2:1
R/R @ live price / 25% stop   = (502.97−408.19)/(408.19−306.14) = 94.78/102.05  = 0.929:1  ❌ far below 2:1
```
**Only the deep 30% MoS + tight 20% stop combination clears the 2:1 minimum** — the same narrow-window pattern found in every prior SPGI session. This session's equivalent qualifying entry is **$352.08**, roughly **13.75% below** the live price of $408.19.

**Position cap check:** 0.68% is nowhere near the 15% hard cap (Upgrade 7) — not a binding constraint.

**Net: HOLD the existing 0.68%-weight SPGI position. Do NOT add fresh capital at the live price of $408.19.** Two independent reasons, either one sufficient alone, unchanged in structure from every prior SPGI session:

1. **R/R gate fails at the live price and at every standard MoS/stop combination except one narrow, ~13.75%-lower limit-order zone** ($352.08 buy / $281.66 stop, 2.14:1). Per Rule 6, R/R below 2:1 = do not enter at the live price.
2. **Quality Watch escalation (Phase 04, unchanged from 07-05):** SPGI's Quality Score (67.7) fails the 80.0+ gate decisively (§7). This does **not** meet the Phase 06 Full Exit bar — none of the four valid triggers apply (no structural margin break, no thesis-broken TAM shrinkage — TAM/growth evidence is *positive* this session via real Ratings/Indices growth prints, no balance-sheet crisis, and the score is nowhere near the sustained-90+ extreme-overvaluation trigger). The gate failure continues to read as a quality-scoring-methodology outcome (thin Moat_Score, IHS-Markit-merger-legacy leverage/ROIC) rather than a sign of business deterioration.

**The open Human Override question from 07-05 (whether to log a `override-log.md` entry mirroring the NOW/ZS precedent, given the quantified Quality gate failure on a held position) remains open, checked but not decided this session** — out of `/rescore`'s scope per established practice.

**The Mobility Global spinoff data-integrity issue (§2 flag 3) is materially advanced but still not fully resolved** — Q3 2026 earnings (expected ~late October 2026, §13) will be the first quarter with a genuinely clean, fully-restated ex-Mobility TTM.

---

## 13. Next Review Trigger

- **Q3 2026 earnings**, expected ~late October 2026 (`yfinance` calendar shows an estimated 2026-10-29 date, unconfirmed) — **high priority**: per the 10-Q's own language (§2 flag 3), this will be the **first quarter with Mobility fully reclassified as discontinued operations for all historical periods**, finally resolving the TTM data-integrity mismatch that has now persisted across two quarters (07-05 and this session).
- **Market Intelligence president succession** — Saugata Saha's departure completed 2026-07-30 as scheduled; no successor named yet (§2 flag 6) — watch for an announcement.
- **Open item, carried forward unchanged:** the Human Override question (§12) — still not decided.
- **Standing Rule 9 triggers:** guidance revision, further M&A, a >15% unexplained price move, or the next Rate Environment Gate quarterly refresh.
- If a fill occurs via the narrow $352.08 limit-order zone, or if the Q3 2026 clean-basis restatement moves the score meaningfully, re-derive immediately rather than waiting for the routine cadence.

---

## 14. Housekeeping

- No SPGI row existed in [watchlist/STALE.md](../watchlist/STALE.md) — confirmed nothing to remove there (SPGI's 07-05 entry was already current under the 2026-06-29 methodology).
- New dated watchlist entry created: [watchlist/in-portfolio/SPGI/SPGI-2026-08-09.md](../watchlist/in-portfolio/SPGI/SPGI-2026-08-09.md) (score/status/action all changed materially enough vs. 07-05 to warrant a new dated row, not just a "no significant change" append — Valuation Score 36.3→31.3, Quality Score 67.1→67.7, Composite 34.6→31.8, buy-zone entry price moved).
- [holdings.md](../portfolio/holdings.md) SPGI row updated: Last Score 31.3, Quality Score 67.7, Composite Score 31.8, Last Review 09 Aug 2026.

---

## Glossary

| Term | Meaning |
|---|---|
| **8-K (Form 8-K)** | A US company's "current report" disclosing a material event (like an earnings release, filed via an attached Exhibit 99.1) between its regular quarterly/annual filings. |
| **Adjusted diluted EPS** | A company's own non-GAAP variant of diluted earnings per share, stripping out items management deems non-recurring — S&P Global's Q2 2026 adjusted diluted EPS ($4.83) is not directly comparable to its GAAP diluted EPS ($4.12) or pro forma continuing-operations diluted EPS ($4.08) without accounting for the different add-backs each basis applies. |
| **CAGR** | Compound Annual Growth Rate. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate; shown as a **reference-only, not-adopted** number for SPGI this session (67.7 Quality Score fails the gate). |
| **D&A** | Depreciation & Amortization. |
| **Discontinued operations** | The US GAAP accounting treatment that reclassifies a business being sold or spun off out of a company's ongoing/continuing results and into a separate line, applied **retroactively to all historical periods shown** once the disposal is complete or highly probable — the mechanism S&P Global will apply to Mobility starting with Q3 2026 reporting (per its own 10-Q language, quoted in §2), which will finally let this framework compute a clean, fully-comparable ex-Mobility TTM. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — SPGI does not qualify (an EPS decline mid-window breaks the run). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Form 10 (registration statement)** | The SEC filing required to register a spun-off entity's stock before distribution, containing that entity's own historical/pro forma financials. |
| **Forward PE** | Price ÷ forward-year expected EPS. This session uses the current-fiscal-year (FY2026) analyst consensus for this sub-score specifically — see §9 for why. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. |
| **Human Override** | A position held outside the framework's own rules — tracked in `override-log.md`; still an open, undecided item for SPGI. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **NRSRO (Nationally Recognized Statistical Rating Organization)** | The SEC-designated status a credit-rating agency must hold for its ratings to be usable in regulatory capital rules and named in covenants/mandates — the regulatory entrenchment behind SPGI's "market share" and "switching costs" moat signals. |
| **NTM (Next Twelve Months)** | A forward-looking estimate covering the next twelve months from today, distinct from a "current fiscal year" or "next fiscal year" estimate, which can diverge from a true NTM figure depending on how far into the current fiscal year the company already is — a distinction this session found material for SPGI's Forward PE calculation (§9). |
| **Organic (constant-currency) revenue growth** | Revenue growth stripping out the effects of currency movements and (where applicable) acquisitions/disposals — S&P Global's full-year 2026 guidance is stated on this basis (6.0–8.0%). |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **Pro forma (financial statements)** | Restated financial statements showing results as if a structural change (e.g. a spinoff) had already been reflected — S&P Global's Q2 2026 earnings release disclosed real pro forma continuing-operations (ex-Mobility) figures for the first time this session (§4/§5). |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. SPGI: 67.7 this session (fails the gate). |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; normalize before valuing; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **Spin-off** | A corporate transaction separating part of a business into a new, independently-traded public company via a pro-rata share distribution — creates a data-integrity trap where post-spinoff price/share count and pre-spinoff trailing financials don't mix cleanly until restated (see **Discontinued operations** above for how/when this resolves for SPGI/Mobility). |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

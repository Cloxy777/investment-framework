# RESCORE — CSGP (CoStar Group, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Trigger:** GitHub issue [#406](https://github.com/cloxy777/investment-framework/issues/406), "RESCORE: CSGP - earnings released 2026-07-28" — significantly overdue (earnings released 2026-07-28, this session runs 2026-08-09, 12 days later, past the "within 3 business days" operating-calendar target).
**Date:** 2026-08-09
**10Y US Treasury Yield:** **4.66%** (Yahoo `^TNX` `regularMarketPrice`, last close 2026-08-07 — markets closed for the weekend on the 08-09 run date, so this is the most recent trading-day print, same convention as prior after-hours-price sessions).
**Rate Regime Modifier (Step 2):** +5 (4.66% sits in the 3.5–5% band, unchanged bracket from the 07-04 review's 4.485%)
**Last review on record:** CSGP **80.5** (Valuation) / **68.4** (Quality) / **56.1** (Composite) — 2026-07-04, [sessions/2026-07-04-rescore-csgp.md](2026-07-04-rescore-csgp.md). Action: HOLD, no add/trim, flagged Phase 04 Quality Watch.
**Current CSGP portfolio weight:** 1.18% per [holdings.md](../portfolio/holdings.md) — nowhere near the 15% hard cap (Upgrade 7).
**Sector:** Real Estate — commercial real estate data, analytics & marketplaces (CoStar Suite, LoopNet, Apartments.com) plus the residential build-out (Homes.com, Domain). Treated as Technology/Growth-style for fair-value method (EV/EBIT multiples + scenario DCF) per Rule 1, given the software-like ~79% gross margin — unchanged reasoning from prior sessions.

**Rule 0 data-fetch note:** `yfinance` failed in-sandbox this session with the same recurring `curl_cffi` TLS-impersonation/connection-reset failure documented across many prior sessions (`SSLError: ... Recv failure: Connection reset by peer`). Worked around per Rule 0's documented contingency (see [sessions/2026-08-07-rescore-uber.md](2026-08-07-rescore-uber.md) §"Rule 0 data-fetch note"): plain `requests` (using the sandbox's `REQUESTS_CA_BUNDLE`) hitting Yahoo Finance's `quoteSummary` and `fundamentals-timeseries` endpoints directly with a session-warmed cookie + crumb from `query2.finance.yahoo.com`, cross-checked against IBKR for the live price. All figures below trace to this fetch.

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$30.75** | IBKR `get_price_snapshot` (contract_id 6726677, NASDAQ primary), `last` field, ts 2026-08-07 23:56 UTC (Friday after-hours print — the most recent available; markets closed for the weekend on this 08-09 run date), `halted: false`. Also equals IBKR's `plprice` (mark price) — internally consistent this session, unlike the stale-close discrepancy flagged in the 07-04 session. |
| Cross-check | $30.24 (at time of earlier Yahoo fetch, same trading session) | Yahoo `price.regularMarketPrice` — consistent within the day's trading range (see change/prior-close below). |
| Prior close | $29.58 | IBKR `prior-close` |
| Change | +$1.17 (+3.96%) | IBKR `change` — a real, single-day move, not close to the 15% Rule 9 unexplained-move threshold, and explained by ordinary post-earnings trading, not a standalone trigger. |
| 52-week range | $25.89 – $94.95 (52w-ago open $95.53) | IBKR `misc_statistics` |
| 13-week range | $25.89 – $34.86 | IBKR `misc_statistics` — stock has been trading in a tight post-earnings-crash band since the 07-28 report |
| 26-week range | $25.89 – $52.35 | IBKR `misc_statistics` |
| Analyst consensus PT | mean **$37.10**, median $35.00, n=20, recommendation "buy" | Yahoo `financialData` — sanity anchor only (Rule 0 Step 4), never a scored input. **Down sharply from $47.50 mean (07-04 session)** — flagged in §2. |
| Dividend yield | 0.0% (no dividend) | IBKR + Yahoo consistent |

**IBKR $30.75 used as the Rule-0 primary price.**

---

## 2. Data Gaps / Flags

1. **Analyst consensus PT has fallen sharply since the last review — now sits *below* this session's Bull-case scenario fair value, a genuine reversal of the 07-04 session's "sober bull anchor" check.** Mean PT was $47.50 (07-04); it is now **$37.10** (see §1) — the market visibly marked down expectations following the 2026-07-28 earnings reaction (see flag 3 below). This session's Bull-case scenario ($43.59, §7) now sits *above* the consensus mean for the first time in this ticker's session history. **Not mechanically adjusted this session** — Guardrail 2 requires scenario-weighted bull/base/bear inputs (not the rosy point, and not chasing sentiment either), and this session's Bull assumption is grounded in the company's own confirmed FY2028 guided target ($1.25B adjusted EBITDA, unchanged — see flag 6), not an invented number. Flagged prominently as a real divergence to monitor, not silently carried forward.
2. **CFO transition (Rule 9 management-change trigger) since the last review.** Christian Lown departed; **Robin Rossmann** (an internal CoStar/STR veteran, previously head of CoStar's European operations, credited with ~$51M of European cost cuts and the France market launch) became CFO effective **2026-07-31**. CEO/founder Andy Florance is unchanged. Per operating-calendar.md's Rule 9 table, a CFO change requires "Re-score + thesis review + moat re-evaluation" — this session's moat and quality re-evaluation (§4–5) already incorporates fresh Q2 2026 evidence; no distinct moat impact is attributed to the CFO change itself, since Rossmann is an internal promotion (continuity, not a strategy pivot) rather than an outside hire. [Yahoo Finance / Simply Wall St coverage, 2026-07-31.]
3. **Material M&A announced — apparently missed by the 07-04 session, now flagged.** CoStar agreed 2026-05-29 to acquire **Zonda** (new-home construction data, homebuilder software, and residential marketplaces; 3,000+ customers) for **$800 million in cash**, expected to close in the back half of 2026 and be accretive to adjusted EPS in the first full year of ownership. This is a genuine, documented TAM-expansion event (new-home construction, a ~$1 trillion US market) reinforcing the Growth sub-score's TAM modifier (§4) — but it is **not yet closed**, so this session does **not** invent pro-forma post-close balance-sheet figures. The current (Q2 FY2026) balance sheet — net cash +$64.0M (§5) — is the actual, filed state used for this session's Balance Sheet sub-score. **Flagged as a material near-term event**: an all-cash $800M outlay against a $64.0M net-cash cushion would flip CoStar to a materially net-debt position unless funded by new financing (not yet disclosed) — this must be explicitly re-examined once the deal closes, not estimated here. [BusinessWire / HousingWire / RISMedia coverage, 2026-05-29.]
4. **Net new bookings decelerated sharply YoY this quarter — a leading-indicator flag, shown but not scored as a Growth-modifier trigger.** Q2 FY2026 net new bookings were $69M, up 3% sequentially but **down ~26% year-over-year** (vs. $93M in Q2 2025), attributed by CFO commentary to a Ten-X restructuring, Homes.com efficiency/cost moves, and aggressive competitor pricing in multifamily. **This did not translate into decelerating realized revenue growth** (Q2 2026 revenue +18% YoY, the company's 61st consecutive quarter of double-digit growth — see §4) — the Growth sub-score's ±10 modifier test is specifically about revenue-growth deceleration/TAM evidence, not bookings, so this flag is shown for transparency and forward monitoring, not used to apply a −10 penalty this session. [Investing.com "CoStar stock outlook after Q2 2026 earnings: bookings decline overshadows EBITDA milestone", 2026-07-28.]
5. **Owner Earnings (Upgrade 1) test flips basis for the first time.** On a **TTM basis** (Q3 2025–Q2 2026), total CapEx ($270.0M) is now *below* D&A ($317.0M) — Growth CapEx (CapEx − maintenance-CapEx-proxy) is negative, so the >30%-of-total-CapEx trigger for Upgrade 1 **does not fire** this session (see §5 for full calc), a change from the FY2025-annual-basis calc (CapEx $389M vs. D&A $263M → 32.4% → triggered) used in every prior CSGP session. This reflects the CapEx cycle genuinely maturing — CapEx peaked at $638M in FY2024 and has fallen every period since, while D&A keeps rising as those prior Homes.com investments amortize — consistent with management's own guided path of cutting Homes.com net investment by $100M+/yr through 2030 (§2 flag 6). Since Upgrade 1 doesn't trigger on the primary (TTM) basis, reported FCF is used directly (no Owner Earnings substitution needed) — the FY2025-annual sensitivity is shown in §5 for continuity with prior sessions, confirming (as before) that Owner Earnings wouldn't rescue the FCF sub-score even where it does trigger.
6. **5-year historical PE range/average still unreconstructable — same no-history fallback as every prior CSGP session, re-verified fresh.** The `fundamentals-timeseries` endpoint caps `quarterlyDilutedEPS` at the 5 most recent quarters regardless of the requested date range (confirmed by testing a `period1` as early as 2005) — far short of the 20 quarters (5 years) the reconstruction method requires. Even if more history were available, the 2023–2025 EPS collapse-and-recovery (annual diluted EPS $0.93 → $0.92 → $0.34 → $0.02) already established in every prior CSGP session as too distorted for a usable historical-PE benchmark hasn't been superseded by a clean recovery yet. **`FwdPE_Score = 50.0` (neutral fallback, flagged)**, unchanged treatment.
7. **PEG still not applicable.** Annual diluted EPS ($0.93 → $0.92 → $0.34 → $0.02, 2022–2025) is declining, not growing >15%/yr on a clean base — CSGP is not a Fast Grower. PEG's 15% weight redistributed to EV/EBIT (→ 40%), unchanged from every prior session.
8. **Full-year 2026 guidance modestly narrowed since January, medium-term target unchanged.** The Q2 2026 earnings release (2026-07-28) guides FY2026 revenue **$3.715–3.755B** and adjusted EBITDA **$780–820M** — a narrower/updated range vs. the January 2026 medium-term-outlook release's FY2026 guide ($3.78–3.82B revenue / $740–800M EBITDA). The **medium-term FY2028 target is unchanged**: ~15% revenue CAGR (2025–2028) and **$1.25B adjusted EBITDA in 2028**, confirmed via CoStar's own 2026-01-07 press release, still the basis for this session's Bull/Base scenario assumptions (§7). [investors.costargroup.com, 2026-01-07 and 2026-07-28 releases.]
9. **No Rule 9 triggers found beyond the three above** (earnings release, CFO transition, and the previously-unflagged Zonda M&A) — no additional guidance revision surprises, no covenant/leverage crisis, no further management changes, and the price move (+2.5% from $30.00 on 07-04 to $30.75 today) is nowhere near the 15% unexplained-move threshold and is fully explained by ordinary post-earnings trading.

No data was invented anywhere below. Every fallback/flag is the documented one from the framework, not an ad hoc substitute.

---

## 3. Independent Data Corroboration

Q2 FY2026 (period ended 2026-06-30) figures were cross-checked across three independent sources before use: (a) Yahoo Finance `quoteSummary`/`fundamentals-timeseries` (this session's primary fetch), (b) CoStar's own 2026-07-28 SEC 8-K earnings press release (`sec.gov/Archives/edgar/data/0001057352/000105735226000061/q2fy262026earningspressr.htm`, fetched directly), and (c) independent financial-media coverage (BusinessWire, HousingWire, Investing.com, RISMedia). All three agree on the headline figures used below: Q2 2026 revenue $925M (+18% YoY), net income $55M (+817% YoY), adjusted EBITDA $184M (+116% YoY), 61st consecutive quarter of double-digit revenue growth. This is a materially stronger cross-check than a single-vendor pull.

---

## 4. Inputs Collected (this session)

| Item | Value | Basis |
|---|---|---|
| Shares outstanding | 405,197,588 | Yahoo `defaultKeyStatistics` |
| **Market Cap** | 405.198M × $30.75 = **$12,459.83M** | Computed |
| Total debt (Q2 FY2026, 2026-06-30) | $1,202.0M | Yahoo `fundamentals-timeseries` `quarterlyTotalDebt` |
| Cash & equivalents (Q2 FY2026) | $1,266.0M | Yahoo `fundamentals-timeseries` `quarterlyCashAndCashEquivalents` — matches `financialData.totalCash` exactly |
| **Net cash (Q2 FY2026)** | $1,266.0M − $1,202.0M = **+$64.0M** | Computed — thinner than 07-04's +$25M cushion, consistent with continued buyback activity (§7), but still net-cash |
| **Enterprise Value** | $12,459.83M − $64.0M = **$12,395.83M** | Computed |
| Revenue (TTM, Q3'25–Q2'26) | $833.6M + $899.9M + $897.0M + $925.0M = **$3,555.5M** | Yahoo `fundamentals-timeseries` quarterly series — ties to `financialData.totalRevenue` ($3,556M, rounding) |
| Revenue growth (TTM, YoY) | 18.4% | Yahoo `financialData.revenueGrowth` |
| Gross Profit (TTM) | $661.4M + $707.2M + $701.0M + $728.0M = **$2,797.6M** | Computed — **Gross Margin 78.68%** |
| **EBIT (TTM)** | −$51.1M + $49.1M + $3.0M + $76.0M = **+$77.0M** | Yahoo `fundamentals-timeseries` `quarterlyEBIT`/`quarterlyOperatingIncome` — **first TTM-positive EBIT in this ticker's session history** (was −$26.2M at 07-04) |
| EBITDA (TTM) | $17.9M + $130.1M + $85.0M + $161.0M = **$394.0M** | Computed — ties to `financialData.ebitda` ($394M) |
| **Net Income (TTM)** | −$30.9M + $46.5M + $3.0M + $55.0M = **$73.6M** | Computed — **Net Margin 2.07%** |
| Pretax income (TTM) | −$45.8M + $60.9M + $12.0M + $74.0M = **$101.1M** | Computed |
| Tax provision (TTM) | −$14.9M + $14.4M + $9.0M + $19.0M = **$27.5M** | Computed — **effective tax rate 27.20%**, a plausible, non-distorted rate now that TTM pretax income is solidly positive (contrast with the 07-04 session's 49.1% distorted TTM rate, which required a normalized substitute) |
| FCF (TTM) | −$23.6M + $95.6M + $98.0M + $57.0M = **$227.0M** | Computed |
| OCF (TTM) | $67.9M + $162.1M + $152.0M + $115.0M = **$497.0M** | Computed — ties to `financialData.operatingCashflow` |
| CapEx (TTM) | −($91.5M + $66.5M + $54.0M + $58.0M) = **−$270.0M** | Computed |
| D&A (TTM) | $69.0M + $81.0M + $82.0M + $85.0M = **$317.0M** | Computed |
| Invested Capital (Q2 FY2026) | **$8,926.0M** | Yahoo `fundamentals-timeseries` `quarterlyInvestedCapital` — computed as Total Debt + Total Equity, same (un-netted-for-cash) convention as the 07-04 CSGP and 08-07 UBER sessions |
| Stockholders' Equity (Q2 FY2026) | $7,932.0M | Yahoo `fundamentals-timeseries` |
| Revenue FY2022 → FY2025 | $2,182.4M → $2,455.0M → $2,736.0M → $3,247.0M | Yahoo `fundamentals-timeseries` `annualTotalRevenue` |
| **Revenue 3yr CAGR** | (3,247.0/2,182.4)^(1/3) − 1 = **14.16%** | Computed — unchanged inputs from every prior session (FY2025 is still the most recently *completed* fiscal year) |
| Forward EPS (consensus, non-GAAP) | $1.72529 (FY2027 estimate) | Yahoo `earningsTrend` |
| **Forward PE (recomputed on live price)** | $30.75 ÷ $1.72529 = **17.82×** | Computed |
| Trailing PE | 168.0× (near-zero TTM EPS base — not used, see PEG/FwdPE fallback notes) | Yahoo `summaryDetail`, reference only |
| Diluted shares, Q2'25 → Q2'26 | 424.3M → 419.9M → 419.6M → 414.0M → 404.4M | Yahoo `fundamentals-timeseries` `quarterlyDilutedAverageShares` — net decline despite ongoing SBC issuance, confirming aggressive net buyback activity (§7) |

---

## 5. CSGP — Quality Score (2026-06-29 methodology)

### Hard disqualifier check (fiscal-year rolling window, per the [2026-08-05 rolling-window clarification](../framework/quality-scoring.md))

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years unexplained? | FY2023 92.5% / **FY2024 −176.3%** / FY2025 585.7% — only one year dips below 70%, not consecutive | disqualify if 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | −0.162× (net cash) | disqualify if >2.5× (standard) | ✅ PASS, comfortably |
| **FCF-positive 3+ consecutive years?** | Most recently completed FY window (FY2023–FY2025): FY2023 (+$347.0M) → **FY2024 (−$245.0M)** → FY2025 (+$41.0M) | disqualify if not | ⚠️ **TRIGGERS** — same window, same result as 07-04. Per the rolling-window clarification, this **won't clear until FY2027 completes** (giving a fresh FY2025–FY2027 window) *and* both FY2026 and FY2027 hold FCF-positive — FY2026 is tracking positive so far (TTM FCF +$227.0M, all four trailing quarters positive except the modestly negative Q3'25 quarter which has now rolled out of the window as a discrete data point but the FY2024 annual figure it belongs to has not yet rolled out of the *annual* window) |

**CSGP fails the 80.0+ Quality Gate via this unwaivable hard disqualifier**, independent of the weighted score below — same status as every prior CSGP session since 2026-07-04.

### Profitability (25% weight) — first TTM-positive-EBIT quarter in this ticker's history

```
Net Margin (TTM)        = $73.6M / $3,555.5M = 2.070%
NetMargin_Component     = clamp((2.070/30)×100, 0, 100) = 6.90

Effective tax rate (TTM)= $27.5M / $101.1M = 27.20%   (a sane, non-distorted rate this session —
                            no normalization substitute needed, unlike 07-04's 49.1%-distorted figure)
NOPAT                   = EBIT(TTM, $77.0M) × (1 − 0.2720) = $56.06M
Invested Capital        = $8,926.0M (Q2 FY2026)
ROIC (TTM)               = $56.06M / $8,926.0M = 0.628%
ROIC_Component           = clamp((0.628/30)×100, 0, 100) = 2.09

Profitability_Score     = (6.90 + 2.09) / 2 = 4.50
```
FCF-positive-3yr cap (40.0, per the hard-disqualifier trigger above) does not bind — 4.50 is already far below it.

### Margins (15% weight)

```
Gross Margin (TTM) = $2,797.6M / $3,555.5M = 78.68%
GrossMargin_Score  = clamp((78.68/80)×100, 0, 100) = 98.35
```
Gross margin trend still mildly declining (81.03% FY22 → 80.00% FY23 → 79.60% FY24 → 78.87% FY25 → 78.68% TTM) — no bonus applies either way (already far above the 40% threshold where the trend-bonus rule is even relevant).

### Growth (20% weight)

```
Growth_Score = clamp((14.16/25)×100, 0, 100) = 56.64
```
**+10 documented TAM/pricing-power evidence, refreshed this session:**
- **61st consecutive quarter of double-digit revenue growth** (Q2 FY2026, +18% YoY) — [CoStar Q2 2026 8-K press release](https://www.sec.gov/Archives/edgar/data/0001057352/000105735226000061/q2fy262026earningspressr.htm), 2026-07-28.
- **Pricing power**: new-customer subscription fees raised effective 2026-05-01, with "measured potential renewal increases" also under evaluation — [Inman, "Homes.com Fees For New Members Will Rise Starting Friday", 2026-04-29](https://www.inman.com/2026/04/29/homes-com-fees-for-new-members-will-rise-starting-friday-costar-ceo/) — sustained alongside CoStar Suite user growth (+22% YoY to 317,000, per the same period's disclosures), i.e. price increases without losing subscriber volume.
- **New TAM**: the pending $800M Zonda acquisition (§2 flag 3) expands into the ~$1 trillion US new-home-construction data market — a genuine, though not-yet-closed, TAM-expansion event.
- No structural deceleration evidence found in the *scored* metric (revenue CAGR/growth) — the bookings deceleration flagged in §2.4 is a leading indicator, not (yet) a realized revenue-growth slowdown, so the −10 modifier is not applied.
```
Growth_Score (with bonus) = clamp(56.64 + 10, 0, 100) = 66.64
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA (Q2 FY2026) = −$64.0M / $394.0M = −0.162× (net cash)
BalanceSheet_Score           = clamp(100×(1 − (−0.162)/4), 0, 100) = clamp(104.06, 0, 100) = 100.0
```
Standard /4 denominator (no asset-light override needed — comfortably passes regardless). **Flag (§2.3):** this reflects the *current*, pre-Zonda-close balance sheet only — not adjusted for the pending $800M all-cash acquisition, which is not yet closed and whose financing (if any, beyond existing cash) is undisclosed.

### Moat Signal (15% weight) — refreshed with Q2 FY2026 evidence, all 5 signals require cited evidence

| Signal | TRUE/FALSE | Evidence (cited) |
|---|---|---|
| Market share stable or growing | **TRUE** | 61st consecutive quarter of double-digit revenue growth ([CoStar Q2 2026 8-K](https://www.sec.gov/Archives/edgar/data/0001057352/000105735226000061/q2fy262026earningspressr.htm), 2026-07-28) — durably outpacing the broader real-estate-services/data market |
| Brand premium | **TRUE** | New-customer subscription fee increases effective 2026-05-01 ([Inman, 2026-04-29](https://www.inman.com/2026/04/29/homes-com-fees-for-new-members-will-rise-starting-friday-costar-ceo/)) sustained alongside CoStar Suite user growth +22% YoY to 317,000 and a 92–94% renewal rate — pricing power without volume loss |
| Network effect | **TRUE** | Homes.com agent subscribers +107% YoY to 36,000+ (Q2 FY2026 earnings call, per Investing.com/Daily Political coverage, 2026-07-28) alongside 118M average monthly unique visitors across CoStar's site portfolio — two-sided marketplace reinforcement (listers and searchers growing together) |
| Switching costs | **TRUE** | Homes.com's monthly cancellation rate fell to **2.4%** (Q2 FY2026) from 6.5% a year earlier ([The Motley Fool / Inman coverage of the 2026-07-28 earnings call](https://www.fool.com/investing/2026/02/19/costars-core-network-runs-at-47-margins-is-homesco/)) — rising stickiness; CoStar Suite remains embedded in CRE broker/investor underwriting workflows |
| Scale cost advantage | **TRUE** (carried forward, Rule 6 — no fresher figure found this session) | 1,600+ dedicated market researchers plus aerial/drone/data-feed infrastructure covering 6M+ properties and 11M+ lease/sale comps, built over 38 years with $5B+ cumulative investment ([costar.com/about/data-providers](https://www.costar.com/about/data-providers)) |

```
Moat_Score = (5/5) × 100 = 100.0
```

### FCF Quality (10% weight)

```
FCF/NI (TTM) = $227.0M / $73.6M = 308.42%
FCFQuality_Score = clamp(((3.0842 − 0.40)/0.60)×100, 0, 100) = clamp(447.4, 0, 100) = 100.0
```
**Flagged**: still an inflated print — TTM Net Income ($73.6M) is a thin (2.07% margin) base relative to FCF, so the ratio is structurally elevated, though *far* less extreme than the 07-04 session's 815.3% (near-zero-NI) artifact. Treat the 100.0 print with the same caution as before, now somewhat reduced.

### Final Quality Score

```
Quality Score = (4.50×0.25) + (98.35×0.15) + (66.64×0.20) + (100.0×0.15) + (100.0×0.15) + (100.0×0.10)
              = 1.125 + 14.753 + 13.328 + 15.000 + 15.000 + 10.000
              = 69.205 → 69.2 (rounded to nearest 0.1)
```

# Quality Score = 69.2 — FAILS the 80.0+ gate (up from 68.4 at 07-04, still failing both on weighted score and the unwaivable hard disqualifier)

**Read carefully:** every sub-score except Profitability improved or held steady this session, and Profitability itself crossed into TTM-positive territory (EBIT +$77.0M, first time since the Homes.com investment cycle began depressing it). This is a genuine, if modest, quality improvement — not a false read. The hard disqualifier remains real and unwaivable (FY2024's FCF still sits inside the trailing 3-year annual window) and independently fails the gate regardless of the improving weighted score. Per [rescore.md](../.claude/commands/rescore.md) step 3, this is again flagged as a **Phase 04 Quality Watch escalation** — CSGP is **not** force-exited on quality alone, but the persistent gate failure plus the newly-flagged pending M&A (§2.3) merit continued closer-than-routine attention.

---

## 6. CSGP — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $30.75 / $1.72529 = 17.823×
EY         = 1 / 17.823 = 5.611%
Spread     = EY − 10Y Treasury = 5.611% − 4.66% = +0.951pp
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (down from a razor-thin +1.50% *pass* at 07-04 — the spread has compressed as the 10Y yield rose from 4.485% to 4.66% while forward PE also ticked up from 16.71× to 17.82×) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.66% → "3.5–5%" bracket (unchanged) → **+5**

**Total Rate Modifier = +10** (up from +5 at 07-04 — this alone accounts for roughly half of this session's overall valuation-score increase; a mechanical, rate-environment-driven shift, not a fundamentals-driven one).

---

## 7. CSGP — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF Yield (TTM) = $227.0M / $12,459.83M = 1.822%
FCF_Score       = clamp(100×(1 − 1.822/10), 0, 100) = 81.78
```
Owner Earnings (Upgrade 1) does not apply this session on the primary TTM basis — see §2 flag 5. (FY2025-annual-basis sensitivity, shown for continuity: Owner Earnings = NI $7.0M + D&A $263.0M − maintenance CapEx $263.0M = $7.0M → Owner Earnings yield 0.056%, *worse* than reported FCF yield — confirms, as in every prior session, that Owner Earnings would not rescue this sub-score even where the test triggers, since the earnings depression is driven by opex-funded growth investment, not capitalized growth CapEx.)
→ Contribution: 81.78 × 0.40 = **32.71**

**EV/EBIT — 25% + 15% (PEG redistributed) = 40% weight**
```
EV/EBIT (TTM) = $12,395.83M / $77.0M = 160.98×
EV/EBIT_Score = clamp((160.98 − 12)/23 × 100, 0, 100) = clamp(647.7, 0, 100) = 100.0
```
**First time in this ticker's session history that trailing EV/EBIT is genuinely defined** (TTM EBIT is now positive) rather than an EV/EBITDA proxy substituted for an undefined/negative EBIT — a real methodological improvement even though the extreme multiple (161×) still clamps to the same 100.0 ceiling as the prior EBITDA-proxy approach. The extreme reading is a direct consequence of TTM EBIT being only barely positive ($77.0M against a $12.4B enterprise value) — flagged, not smoothed over. (FY2025-annual-basis EBIT is still negative, −$72.0M — undefined on that basis, consistent with why the TTM basis is used as primary.)
→ Contribution: 100.0 × 0.40 = **40.00**

**Forward PE — no-history fallback — 20% weight**
```
FwdPE_Score = 50.0 (neutral midpoint, flagged — same no-history rationale as every prior CSGP session, re-verified §2 flag 6)
```
→ Contribution: 50.0 × 0.20 = **10.00**

**PEG — 15%: still N/A** (§2 flag 7) — redistributed to EV/EBIT above.

**Raw weighted score:**
```
= 32.71 + 40.00 + 10.00 = 82.71
```
**+ Rate Modifier (+10) = 92.71** (pre Upside/Downside)

---

## 8. CSGP — Upside/Downside Modifier (Expected-Return Modifier)

Same scenario architecture as every prior CSGP session (EV/EBIT-multiple method on normalized ~2027–2028 EBIT) — the underlying guided targets it's anchored to (FY2026 adjusted EBITDA $780–820M, FY2028 adjusted EBITDA $1.25B) are confirmed **unchanged** this session (§2 flag 8), so the same Normalized EBIT / exit-multiple assumptions are kept for continuity (not re-inflated toward the now-confirmed $1.25B FY28 target, per Guardrail 2's "never the rosy point"). Only the net-cash add-back and share count are refreshed to current figures.

| Scenario | Wt | Normalized EBIT | Exit EV/EBIT | FV/share |
|---|---|---|---|---|
| Bull | 25% | $800M | 22.0× | **$43.59** |
| Base | 50% | $650M | 20.0× | **$32.24** |
| Bear | 25% | $450M | 16.0× | **$17.93** |

```
PW Fair Value = 0.25×43.59 + 0.50×32.24 + 0.25×17.93 = $31.50
```

**⚠️ Bull ($43.59) now sits *above* the $37.10 analyst consensus mean PT** — a reversal of every prior CSGP session, where the bull case sat below consensus as a "sober bull anchor" check (§2 flag 1). Shown transparently, not adjusted to force a match — the assumption is grounded in CoStar's own confirmed guidance, not sentiment, but this divergence should be re-examined at the next review once the market has digested the Zonda deal and CFO transition.

- **Gap Upside %** = ($31.50 ÷ $30.75) − 1 = **+2.44%**
- **Catalyst & timeline (Rule 10):** Same documented, management-guided catalyst as every prior session — the Homes.com net-investment cut (>$300M less in 2026, $100M+/yr through 2030, confirmed unchanged 2026-01-07) and the guided adjusted-EBITDA path ($191M FY25 actual → $780–820M FY26 guide → $1.25B FY28 target). **2-year window** (unchanged). Annualized gap = 2.44% ÷ 2 = **+1.22%/yr**.
- **Intrinsic growth: +12%/yr** (unchanged — still conservative vs. the 14.16% 3yr revenue CAGR and the ~15% medium-term guided CAGR; kept flat per guardrail 2, not raised to the rosy point).
- **Shareholder yield: +4.69%/yr** — **recomputed this session from actual data, not carried forward as an estimate.** Diluted average share count fell from 424.3M (Q2'25) to 404.4M (Q2'26), a **4.69%** net decline (net of any SBC-driven issuance) — see [glossary.md](../framework/glossary.md)'s "Buyback yield (net buyback yield)" definition. Corroborating context: $587M repurchased in H1 2026 against a new **$1.5 billion** buyback authorization (2026-01-07, no time limit, separate from the previously-guided "$700M in 2026" figure) and a $1.023B TTM gross buyback dollar figure. No dividend (0.0% yield).

```
E = 1.22 (annualized gap) + 12.0 (intrinsic growth) + 4.69 (shareholder yield) = 17.91%
```

**Map to modifier** (H = 10%): E ≥ H → M = −15 × clamp((17.91 − 10)/15, 0, 1) = −15 × 0.5273 = **−7.91**

**Guardrail check:** (1) catalyst exists within 18–24 months → no −5 upside cap. (2) Bull/base/bear PW FV used, not the rosy point — though flagged above as now exceeding consensus, a genuine open item. (3) Full calc shown. (4) Bounded ±15 — within range.

---

## 9. CSGP — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (82.71) + Rate Modifier (+10) + Upside/Downside (−7.91)
                       = 84.80 → 84.8
```

| | Value |
|---|---|
| Raw weighted | 82.71 |
| Rate Gate (Step 1 fail +5, Step 2 +5) | +10 |
| Upside/Downside Modifier | −7.91 (E = +17.91%) |
| **FINAL VALUATION SCORE** | **84.8** |
| Prior valuation score (07-04) | 80.5 |
| **Quality Score** | **69.2** (FAILS 80.0+ gate — hard disqualifier + weighted score) |
| Prior Quality Score (07-04) | 68.4 |

**The raw Valuation Score alone (84.8) reads "Trim to 50%" (80.0–89.9 band)** — one notch deeper into that band than 07-04's 80.5. **This move is mostly mechanical, not fundamentals-driven**: roughly half of the +4.3-point increase (+5) comes directly from the Rate Environment Gate's Step 1 flipping from pass to fail as the 10Y yield rose and the spread compressed — several underlying fundamental inputs actually *improved* this session (EBIT turned TTM-positive for the first time, Quality Score rose 68.4→69.2, FCF yield improved slightly).

**Composite Score:**
```
Composite Score = 0.50×(100 − 69.2) + 0.50×84.8
                = 0.50×30.8 + 0.50×84.8
                = 15.4 + 42.4
                = 57.8
```

**Composite Score = 57.8** (up from 56.1 at 07-04, still comfortably inside the 50.0–69.9 Hold band).

---

## 10. CSGP — Action Recommendation

**Composite Score 57.8 → Action band: 50.0–69.9 → HOLD** (watch only, no new entry, no trim — Fair Value band).

**Read with the same care as the 07-04 session — this is not a routine, comfortable Hold, but a continued Phase 04 Quality Watch escalation:**

- The raw Valuation Score alone (84.8) independently says "Trim to 50%" — one notch more expensive than last quarter, driven mostly by the Rate Gate flip (§9), not a fundamentals-driven re-rating.
- The Quality Score (69.2) still **fails** the 80.0+ gate — via an unwaivable hard disqualifier (FY2024's FCF, still inside the trailing 3-year annual window) — pulling the blended Composite down into the Hold band, per [valuation-scoring.md](../framework/valuation-scoring.md)'s "use the Composite Score, not the raw Valuation Score" rule.
- **This session finds no new evidence of genuine deterioration** — the opposite, in several respects: TTM EBIT turned positive for the first time, revenue growth continues unbroken at 61 consecutive quarters of double-digit expansion, all 5 moat signals remain documented TRUE with fresher (arguably stronger) citations than 07-04, and the Quality Score itself improved modestly (68.4 → 69.2). The character of the quality gap remains the same as every prior CSGP session: a disclosed, guided, self-funded reinvestment story (Homes.com), not moat erosion or a declining competitive position. On that basis, this session again does **not** override the Composite-driven HOLD.
- **Two new items, however, genuinely raise the bar for next quarter's attention**, beyond the routine hard-disqualifier watch: (1) the pending **$800M all-cash Zonda acquisition** (§2 flag 3), which would materially change the balance-sheet picture once it closes against a currently-thin +$64.0M net-cash cushion, and (2) the sharp **net-new-bookings deceleration** (§2 flag 4) and the accompanying **analyst-consensus-PT compression** (§2 flag 1, mean PT down from $47.50 to $37.10) — neither yet a scored trigger, but both worth a fast follow-up rather than waiting a full quarter if either develops further.

**Net recommendation: HOLD the existing position — no forced trim, no add.** Current position: 1.18% of portfolio (per [holdings.md](../portfolio/holdings.md)) — already a small, tracking-sized position, unaffected by the 15% cap either way. No order setup required (operating-brief.md OUTPUT FORMAT step 6 applies only to BUY/TRIM actions).

**No full exit** — Phase 06 triggers absent: still net-cash (pre-Zonda-close), gross margin intact at 78.68%, revenue growing unbroken (61 consecutive quarters of double-digit growth), moat signals all documented intact with fresh citations, and the current Valuation Score (84.8) — while elevated — has not sustained 90.0–100.0 for 2+ consecutive quarters (the only score-based exit trigger).

---

## 11. Next Review Trigger

- **Next earnings: Q3 FY2026, confirmed 2026-10-27** (Yahoo `calendarEvents`, `isEarningsDateEstimate: False`). Standard re-score, with specific attention to:
  - **Whether the Zonda acquisition has closed** (§2 flag 3) and, if so, the actual financing structure and post-close balance-sheet/leverage picture — do not estimate this before it's disclosed.
  - Whether net new bookings stabilize or continue decelerating (§2 flag 4) — and whether that eventually shows up in realized revenue growth.
  - Whether FY2026 full-year FCF comes in positive (tracking positive so far on a TTM basis, +$227.0M) — which, combined with FY2025's +$41.0M, would still leave the FY2023–FY2025-style disqualifier window unresolved until FY2027 also completes positive (per the rolling-window mechanism, §5).
  - Progress on the Homes.com net-investment cut and the FY2026 adjusted EBITDA guide ($780–820M).
  - How the CFO transition (§2 flag 2) beds in — any strategy or reporting changes under Rossmann.
- **Earlier if (Rule 9):** a guidance revision (up or down), confirmation/close of the Zonda deal with material new leverage, a further management change, or a >15% unexplained price move.
- **Quality Score watch:** re-check the hard disqualifier and the Profitability sub-score every quarter — Profitability crossed into TTM-positive territory this session for the first time; worth tracking whether that holds.

---

## 12. Housekeeping

- No CSGP row existed in [watchlist/STALE.md](../framework/../watchlist/STALE.md) — confirmed nothing to delete there, and no `⚠️ STALE SCORE` banner existed on the [07-04 entry](../watchlist/in-portfolio/CSGP/CSGP-2026-07-04.md) to clear (CSGP has been scored under the current 2026-06-29 methodology continuously since 07-04).
- New dated watchlist entry created: [watchlist/in-portfolio/CSGP/CSGP-2026-08-09.md](../watchlist/in-portfolio/CSGP/CSGP-2026-08-09.md) — warranted per [watchlist/README.md](../watchlist/README.md)'s "significant change" criteria (score changed, and three independent Rule 9 triggers fired: earnings release, CFO transition, and the newly-flagged Zonda M&A).
- [holdings.md](../portfolio/holdings.md) CSGP row updated: Last Score 84.8, Quality Score 69.2, Composite Score 57.8, Last Review 09 Aug 2026.

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking number, `0.50 × (100 − Quality Score) + 0.50 × Valuation Score`, computed only for companies clearing the 80.0+ Quality Score gate. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization. |
| **Effective tax rate** | The actual percentage of a company's pretax income paid as income tax in a given period (tax provision ÷ pretax income) — distinct from the statutory rate. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) and its operating-profit multiple. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Peter Lynch's term for EPS growth >15%/yr for 3+ years on a clean earnings base — this framework's PEG-eligibility trigger. CSGP doesn't qualify (declining EPS). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit cash quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score; not every hard disqualifier has a carve-out (the FCF-positivity check does not). |
| **Hurdle rate** | The 10% minimum acceptable annual return the Upside/Downside Modifier measures expected return against. |
| **Invested Capital** | The capital base (debt + equity) ROIC is measured against. |
| **MoS (Margin of Safety)** | Cushion below fair value at which a buy price is set. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax, EBIT × (1 − effective tax rate); the numerator of ROIC. |
| **Owner Earnings** | Net Income + D&A − maintenance CapEx only. |
| **PEG ratio** | PE ÷ earnings growth rate. |
| **Buyback yield (net buyback yield)** | The rate a company's share count shrinks per year from repurchasing its own stock, net of new share issuance — this session's shareholder-yield component. |
| **PW (Probability-Weighted) Fair Value** | 25% bull + 50% base + 25% bear scenario blend (Rule 7). |
| **Quality Score** | This framework's 0.0–100.0 grading of profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to clear the gate. |
| **R/R (Risk/Reward ratio)** | Reward-to-risk ratio for a trade — not computed this session (no BUY/TRIM action). |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's live-price, normalization, model-refresh-trigger, and intrinsic-vs-market-price rules respectively. |
| **TAM** | Total Addressable Market. |
| **TTM** | Trailing Twelve Months. |
| **Upside/Downside Modifier** | The additive ±15 adjustment folding expected annual return into the valuation score. |
| **Value trap** | A stock that looks statistically cheap but stays cheap because underlying business quality is deteriorating or was never strong enough to support a re-rating. |

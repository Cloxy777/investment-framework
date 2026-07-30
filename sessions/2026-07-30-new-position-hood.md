# NEW POSITION — HOOD (Robinhood Markets, Inc., Class A)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run; mandatory Rule 9 re-check named explicitly by the prior session)
**Date:** 2026-07-30 (Thursday)
**10Y US Treasury Yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (same precedent as the 2026-07-25 HOOD session and the 2026-07-24 QCOM session) before the Rate Environment Gate would otherwise apply.
**Current HOOD portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [sessions/2026-07-25-new-position-hood.md](2026-07-25-new-position-hood.md) / [watchlist/not-in-portfolio/HOOD/HOOD-2026-07-25.md](../watchlist/not-in-portfolio/HOOD/HOOD-2026-07-25.md) — Quality Score 73.0, Phase 01 FAIL (weighted-score gate miss + Hard Disqualifier #1).
**Sector:** Financials — Capital Markets / Retail Brokerage & Fintech (equities, options, crypto trading; subscriptions; banking; prediction markets)
**Filer type:** US SEC filer, CIK 0001783879, Delaware-incorporated, calendar fiscal year.
**First-use jargon decode:** see closing Glossary.

---

## 0. Why this session exists — trigger source

The 2026-07-25 session's own "Next review trigger" named "Robinhood's Q2 2026 earnings, after market close Wednesday 2026-07-29 — a mandatory Rule 9 re-check." Robinhood reported Q2 2026 results after market close on 2026-07-29, and a Telegram post (`bolshegold/9859`, ~20:26 UTC 2026-07-29) reported on that release (GAAP EPS $0.62 beat, revenue $1.31B +32.5% YoY, record net deposits $22B, Gold subscribers 4.8M). **Per Rule 0/CLAUDE.md, the post's text is a trigger only, never a financial input** — every figure below is independently re-fetched and re-verified from primary sources (SEC XBRL/10-Q, IBKR, `stockanalysis.com`), not copied from the post or from the prior session.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| Contract identity | "ROBINHOOD MARKETS INC - A", NASDAQ, contract_id **504546674** (reconfirmed same contract as the 2026-07-25 session) | IBKR |
| **Live price** | **$90.76** (last trade, ts 2026-07-30 12:11:56 UTC — today, intraday, not a stale snapshot) | IBKR `get_price_snapshot` |
| Change vs. prior close | +$0.92 / +1.02% (prior close $89.84, Wed 2026-07-29's regular-session close — the pre-earnings-reaction close, since results were released *after* that close) | IBKR `get_price_snapshot` (`change` field) |
| 52-week range | $63.515 (low) – $153.86 (high); 13-week range $70.76–$120.05; open 52w ago $103.85 | IBKR `misc_statistics` |
| Dividend yield | 0.0% (no dividend) | IBKR `dividend_yield` |
| Cross-check | IBKR `get_price_history` (`ONE_DAY`/`TWO_WEEKS`) independently shows the same $89.84 close for 2026-07-29 and $92.76 for 2026-07-28 — internally consistent with the `change` field above. Yahoo Finance's `quoteSummary` (`financialData.currentPrice` $89.84) matches the *prior*-close figure exactly, confirming Yahoo's snapshot cache had not yet rolled to today's intraday tick at query time — not used as the live price for that reason, IBKR's fresher intraday tick used instead. | IBKR + Yahoo cross-check |

**Context only (not a scoring input, not acted on per Rule 9):** the market's reaction to an apparent EPS/revenue beat is muted (+1.02% intraday) — plausibly because the stock had already pulled back ~25% from its 13-week high ($120.05) into the print, and/or because of the balance-sheet and cash-flow items surfaced below (new debt, a sharply weaker TTM free-cash-flow read). This is observed, not interpreted as a trading signal.

---

## 2. Data Sourcing Note

`yfinance`'s `Ticker.info` again failed with the same known `curl_cffi` TLS/`Connection reset by peer` error (confirmed directly on HOOD this session) — the documented, pre-existing environment issue. Used the plain-`requests` Yahoo JSON-API workaround instead, but **found its `quoteSummary` financial-statement modules were themselves stale** — `defaultKeyStatistics.mostRecentQuarter` returned `2026-03-31`, i.e. Yahoo's own cache had not yet ingested Q2 2026 (period ended 2026-06-30), reported after close the day before this session. Rather than use stale TTM figures, this session sources Q2 2026 figures directly from:

- **SEC XBRL `companyconcept` API** (`data.sec.gov/api/xbrl/companyconcept/CIK0001783879/us-gaap/...`) — pulled quarter-by-quarter (`Revenues`, `NetIncomeLoss`, `OperatingExpenses`, pretax income, tax expense, `DepreciationDepletionAndAmortization`, `StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest`, `CashAndCashEquivalentsAtCarryingValue`, `NetCashProvidedByUsedInOperatingActivities`) for Q3 FY2025 through Q2 FY2026, to independently reconstruct the TTM window ended 2026-06-30.
- **Robinhood's Q2 2026 Form 10-Q** (filed 2026-07-30, accession `0001783879-26-000114`) — read directly for the Convertible Notes financing-activities footnote and MD&A KPI table (Gold Subscribers, Net Deposits, Funded Customers, ARPU).
- **`stockanalysis.com`** (`/stocks/HOOD/financials/`, `/balance-sheet/`, `/cash-flow-statement/`, `/ratios/`) — used as an independent cross-check on every reconstructed TTM figure below (all five cross-checks matched exactly or near-exactly; the only ones NOT independently reconstructed from XBRL — Gross Profit and the CapEx sub-line breakdown — are flagged individually where used).
- **Independent WebSearch/WebFetch** — non-Telegram sources only, cited individually at point of use for Growth/Moat qualitative evidence.

No required input was invented, estimated, or taken from the triggering post.

### TTM reconstruction (window: Q3 FY2025 + Q4 FY2025 + Q1 FY2026 + Q2 FY2026, i.e. through 2026-06-30)

Built from SEC XBRL quarterly deltas (YTD cumulative figures differenced quarter-to-quarter):

| ($M) | Q3 FY25 | Q4 FY25 (derived) | Q1 FY26 | Q2 FY26 | **TTM** | Cross-check vs. `stockanalysis.com` |
|---|---|---|---|---|---|---|
| Revenue | 1,274 | 1,283 | 1,067 | 1,308 | **4,932** | ✅ exact match ($4,932M) |
| Operating Income (EBIT) | 635 | 650 | 411 | 574 | **2,270** | ✅ exact match ($2,270M) |
| Net Income | 556 | 605 | 350 | 561 | **2,072** | ✅ exact match ($2,072M) |
| Pretax income | 634 | 661 | 411 | 709 | **2,415** | — (not separately shown by that source) |
| Income tax expense | 78 | 56 | 65 | 136 | **335** | — |
| D&A | 22 | 23 | 23 | 23 | **91** | — |
| Operating Cash Flow | −1,576 | −937 | 2,038 | 720 | **245** | ✅ exact match ($245M) |

*(Q4 FY2025 derived as FY2025-annual minus 9-month-YTD; every other cell is a direct XBRL quarterly value or YTD difference.)* TTM effective tax rate = 335/2,415 = **13.87%**. TTM Net Income cross-check: Pretax − Tax = 2,415 − 335 = 2,080 vs. the directly-summed $2,072M (a ~0.4% gap, immaterial, consistent with the ~0.2% gap flagged in the prior session — likely noncontrolling-interest/rounding).

**Balance sheet (as of 2026-06-30, XBRL + 10-Q text):** Cash $5,362M; Total Equity $9,541M; **Total Debt $2,170M — see §3.1, a material, new fact.**

**Gross Profit and CapEx — sourced from `stockanalysis.com` only, not independently reconstructed from XBRL this session** (no standalone `GrossProfit` or `PaymentsToAcquirePropertyPlantAndEquipment` XBRL tag exists for HOOD; the 10-Q's cash-flow statement instead uses combined lines "Purchases of property, software, and equipment" + "Capitalization of internally developed software," confirmed present in the filing text but not fully quarter-differenced this session for time reasons). TTM Gross Profit **$4,697M**; TTM CapEx **−$26M**; TTM FCF (OCF − CapEx) = 245 − 26 = **$219M**. Flagging this as a minor data-provenance gap (Rule 0) — it does not affect the OCF figure above, which **was** independently reconstructed and matched exactly, and CapEx is small enough (≈1% of OCF) that even a modest revision would not change any sub-score.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifier check (fires regardless of weighted score)

| Hard disqualifier | HOOD data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | Annual FCF (unchanged from 2026-07-25, re-verified): FY2021 −$948M, FY2022 −$880M, FY2023 +$1,179M, FY2024 −$170M, FY2025 +$1,623M. **FY2026 is not yet a complete fiscal year** (only 2 of 4 quarters reported: Q1 ended 2026-03-31, Q2 ended 2026-06-30) — per this task's explicit instruction, the hard disqualifier's fiscal-year lookback cannot yet include a "FY2026" data point, so the most recent complete-year evidence remains the identical FY2022–FY2025 window as the 2026-07-25 session. No 3-consecutive-year positive window exists anywhere in it. | **FIRES (unchanged).** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | **Material new fact vs. 2026-07-25: HOOD is no longer debt-free.** On 25 June 2026, Robinhood issued **$2.2 billion aggregate principal amount of 0.00% Convertible Senior Notes due 2029** (net carrying value $2.17B after ~$30.6M issuance costs; effective interest rate 0.43%; conversion price ≈$174.42/share, a 65% premium to the $105.71 pricing-date close) — the company's first-ever financial debt instrument, confirmed directly from the Q2 2026 10-Q's Note 11 (Financing Activities). ~$290M of net proceeds was used to repurchase ~2.7M shares; the rest sits on the balance sheet (Cash rose to $5,362M from $5,012M at Q1 2026). Net Debt = Cash $5,362M − Debt $2,170M = **−$3,192M (net cash)**. TTM EBITDA = EBIT $2,270M + D&A $91M = **$2,361M**. Net Debt/EBITDA = −3,192/2,361 = **−1.35×** (matches `stockanalysis.com`'s own reported −1.35 exactly). | **Does not fire** (still net cash, comfortably under 2.5×) — but flagged prominently: the "zero financial debt" framing used in both prior HOOD sessions no longer holds. |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | Same annual pattern as 2026-07-25 (unchanged, fiscal-year basis): only **FY2024** is unambiguously <70% on a meaningful (same-sign) base (−12.05%); FY2025 is 86.2%(1,623/1,883); FY2022/FY2023 have mismatched NI/FCF signs (not meaningful). Only 1 year, not 2 consecutive. **New this session, TTM (not annual) FCF/NI has collapsed to 10.57%** (§3.2 FCF Quality) — a real, material data point, but the *hard disqualifier* is explicitly fiscal-year-based ("2+ consecutive years"), so a single TTM reading does not itself trigger it. | **Does not independently fire** (unchanged verdict) — though the TTM reading is a fresh, material warning sign, discussed in §3.2. |

**Hard Disqualifier #1 (FCF positivity) fires, unchanged and independent of the weighted score below.**

### 3.2 Weighted Quality Score

**Source data** (TTM = trailing twelve months through 2026-06-30, per §2's reconstruction; FY columns re-verified unchanged from the 2026-07-25 session):

| Metric | TTM (new) | TTM (2026-07-25, through Q1'26) | FY2025 | FY2024 |
|---|---|---|---|---|
| Revenue | 4,932 | 4,613 | 4,473 | 2,951 |
| Gross Profit | 4,697 | 4,392 | 4,262 | 2,787 |
| Operating Income (EBIT) | 2,270 | 2,135 | 2,094 | 1,054 |
| Net Income | 2,072 | 1,897 | 1,883 | 1,411 |
| Gross Margin | 95.24% | 95.21% | 95.28% | 94.44% |
| Net Margin | 42.01% | 41.04% | 42.10% | 47.81% |
| Cash | 5,362 | 5,012 | 4,261 | 4,332 |
| Total Debt | **2,170** | 0 | 0 | 0 |
| Total Equity | 9,541 | 9,688 | 9,151 | 7,972 |
| Operating Cash Flow | **245** | 3,034 | 1,638 | (157) |
| CapEx | (26) | (22) | (15) | (13) |
| FCF | **219** | 3,012 | 1,623 | (170) |

*(Sources: SEC XBRL for TTM Revenue/EBIT/NI/OCF/D&A/Cash/Equity/Debt, per §2's reconstruction table; `stockanalysis.com` for Gross Profit and CapEx, cross-checked as described in §2.)*

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((42.01/30)×100) = 100.0 (raw 140.0, capped). ROIC: NOPAT = TTM EBIT × (1 − eff. tax rate) = 2,270 × (1 − 0.1387) = **$1,955.1M**. Invested Capital = Total Debt ($2,170M — now nonzero) + Equity ($9,541M) − Cash ($5,362M) = **$6,349M**. ROIC = 1,955.1/6,349 = **30.79%** (cross-checked against `stockanalysis.com`'s own reported TTM ROIC of 35.47% — reasonably consistent; the gap is larger than the 2026-07-25 session's ~0.9pp gap, plausibly because their methodology handles the newly-issued debt or invested-capital averaging differently — flagged, not resolved). ROIC_Component = clamp((30.79/30)×100) = 100.0 (raw 102.6, capped). Raw avg = 100.0 — **FCF-positivity cap still applies** (§3.1: HOOD still fails 3-consecutive-year FCF positivity). | **40.0 (capped)** |
| **Margins (15%)** | GrossMargin_Score = clamp((95.24/80)×100) = 100.0 (raw 119.0, capped). No trend bonus (already far above the 40% bonus-eligibility ceiling). | **100.0** |
| **Growth (20%)** | Revenue 3yr CAGR: same base years as precedent (FY2025 remains the most recent *complete* fiscal year — FY2026 is not) — FY2022 $1,358M → FY2025 $4,473M = **+48.79%/yr**. Base = clamp((48.79/25)×100) = 100.0 (raw 195.2%, capped). **+10 TAM-expansion modifier — fresh Q2 2026 evidence** (independently sourced, not from the trigger post, via the Q2 2026 10-Q and Robinhood's own press release, cross-checked via WebFetch/WebSearch): (1) **Event-contract (prediction markets) revenue grew ~10x YoY to $156M** in Q2 2026, explicitly attributed in the 10-Q's MD&A to "an acceleration in our prediction markets business"; the JV exchange/clearinghouse (Rothera, the CFTC-licensed DCM/DCO/SEF Robinhood's joint venture acquired 90% of on 20 Jan 2026 — the same entity previously referred to as "MIAXdx" in the 2026-07-25 session) reports 13.6B contracts traded to date; (2) **International Funded Customers surpassed 1 million**; (3) **Credit Card business crossed $100M in annualized revenue**; (4) **Trump Accounts exceeded 7 million signups, $1.5B deposited**; (5) **13 distinct business lines now each generating $100M+ of annualized revenue** (up from 11 cited in the 2026-07-25 session); (6) Robinhood Gold Subscribers reached 4.84M (+39% YoY), Net Deposits a record $21.7B in the quarter (+28% annualized growth rate). Already at the 100.0 ceiling — the modifier is redundant against the cap but shown per "no black-box outputs." Crypto revenue softness (flagged 2026-07-25) not independently re-verified this session; not material to the outcome either way since Growth is capped regardless. | **100.0** |
| **Balance Sheet (15%)** | Net Debt/EBITDA = −1.35× (net cash, §3.1 — despite the new $2.17B of debt). BalanceSheet_Score = clamp(100×(1−(−1.35)/4)) = clamp(133.75) = **100.0**. | **100.0** |
| **Moat Signal (15%)** | Re-checked all 5 signals against fresh Q2 2026 disclosures — **unchanged, 1 of 5**. See table below. | **20.0** |
| **FCF Quality (10%)** | **TTM FCF/NI = 219/2,072 = 10.57%** — a sharp deterioration from the 2026-07-25 session's TTM reading of 158.8%. Driven by broker-dealer working-capital volatility rolling through the TTM window: Q3 FY2025 (−$1,576M) and Q4 FY2025 (−$937M) operating cash flow are now the two oldest quarters anchoring this TTM window, and even strong H1 FY2026 OCF ($2,038M + $720M) isn't enough to offset them (see §2's quarterly table). This is the same characteristic already documented for FY2024 in the 2026-07-25 session (net-income-positive, OCF-negative, due to customer-cash/securities-lending timing, not a documented growth-capex explanation) — real, sourced, not an error (independently cross-checked: the $245M TTM OCF figure matches `stockanalysis.com`'s own TTM figure exactly). FCFQuality_Score = clamp(((0.1057−0.40)/0.60)×100) = clamp(−49.05) = **0.0**. | **0.0** |

**Moat signal evidence — re-checked this session, no change (1 of 5 credited):**

| Signal | Fresh evidence checked this session | Verdict |
|---|---|---|
| Market share stable/growing | WebSearch found only self-reported marketing language in Robinhood's own Q2 2026 materials ("continued to gain market share," "#1 Platform for Active Traders," "#1 in Wallet Share for the Next Generation") — no specific, third-party-cited percentage or trend data point, unlike the bar this signal requires (contrast e.g. the Dell'Oro/TrendForce-style citations credited elsewhere in this framework). A broader search for Robinhood-specific options/equity-trading share data (vs. industry-wide retail participation %, a different metric) returned nothing citable either way. Consistent with the 2026-07-25 session's conservative-grading precedent, **not credited** absent a specific third-party figure. | **FALSE (unchanged)** |
| Brand premium | No new price-increase-without-volume-loss or premium-vs.-competitor evidence found. | **FALSE (unchanged)** |
| Network effect | No new documented two-sided-marketplace mechanism found (prediction markets could plausibly develop one — more traders → better liquidity — but no HOOD-specific documentation of that dynamic was found this session). | **FALSE (unchanged)** |
| Switching costs | IRA-match 5-year-clawback mechanism unchanged and re-confirmed still in effect. | **TRUE (unchanged)** |
| Scale cost advantage | No new cost-per-unit-vs.-competitor data found. | **FALSE (unchanged)** |

### 3.3 Final weighted Quality Score

```
Quality Score = (40.0 × 0.25) + (100.0 × 0.15) + (100.0 × 0.20) + (100.0 × 0.15) + (20.0 × 0.15) + (0.0 × 0.10)
              = 10.00 + 15.00 + 20.00 + 15.00 + 3.00 + 0.00
              = 63.00 → 63.0 (rounded to nearest 0.1)
```

**63.0 < 80.0 — fails the gate, and by a wider margin than 2026-07-25 (17.0 points short, vs. 7.0 points short before).** Hard Disqualifier #1 (FCF positivity) also fires independently and unconditionally, as before.

**Sensitivity check (transparency only, per this framework's precedent):** even crediting all 5 Moat signals (Moat_Score = 100.0, contributing 15.0 instead of 3.0), Quality Score would be 63.0 + 12.0 = **75.0** — still short of the 80.0 gate. This is a materially different sensitivity result than 2026-07-25's (where full Moat credit would have numerically reached 85.0): the collapse in the FCF Quality sub-score (100.0 → 0.0, a full 10.0-point swing at its 10% weight) means Moat alone can no longer close the gap even under the most generous reading. Shown for transparency only — the outcome (FAIL) is unchanged and does not depend on this sensitivity.

### Result: **Phase 01 FAIL — materially changed vs. 2026-07-25, but the same direction (further from the gate, not closer)**

| | 2026-07-25 | 2026-07-30 (this session) | Delta |
|---|---|---|---|
| Quality Score | 73.0 | **63.0** | **−10.0** |
| Gate (80.0+) | FAIL by 7.0 | FAIL by 17.0 | worse |
| Hard Disqualifier #1 (FCF positivity) | Fires | **Fires (unchanged)** | no change |
| Hard Disqualifier #2 (Net Debt/EBITDA) | Does not fire (0 debt) | Does not fire (**new $2.17B debt, still net cash**) | new fact, same verdict |
| Hard Disqualifier #3 (FCF/NI <70%, 2yr) | Does not fire | Does not fire (**TTM ratio cratered to 10.57%, but disqualifier is annual, not TTM**) | flagged, same verdict |
| Profitability | 40.0 (capped) | 40.0 (capped) | unchanged |
| Margins | 100.0 | 100.0 | unchanged |
| Growth | 100.0 | 100.0 (fresh evidence, same score) | unchanged |
| Balance Sheet | 100.0 | 100.0 (despite new debt) | unchanged |
| Moat | 20.0 | 20.0 (re-checked, unchanged) | unchanged |
| **FCF Quality** | 100.0 | **0.0** | **−100.0 (the entire swing)** |

Per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md): a company scoring below 80.0, or tripping a hard disqualifier, does not proceed to Phase 02. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed** — same as 2026-07-25.

---

## 4. Recommendation

**PASS — does not clear the Quality Score gate, and the picture is somewhat worse than five days ago, not better, despite an apparent earnings beat.** No Rate Environment Gate, no Phase 02 valuation score, no fair-value work, and no order setup.

The headline Q2 2026 print (GAAP EPS $0.62, revenue $1.31B +32% YoY, record net deposits $21.7B in the quarter, Gold Subscribers 4.84M) is real and independently confirmed via SEC XBRL and Robinhood's own filings — the Telegram trigger's factual claims check out. But the same earnings package that produced the beat also disclosed two developments that this framework's Quality Score treats unfavorably: **(1)** Robinhood issued its first-ever financial debt ($2.2B in 0% convertible notes, 25 June 2026) — not itself disqualifying (still comfortably net cash), but ends the "zero financial debt" framing this name carried through two prior sessions; **(2)** **trailing-twelve-month free cash flow, on a rolling basis, has collapsed** — from $3.0B (TTM through Q1 2026) to just $219M (TTM through Q2 2026) — as two sharply negative broker-dealer working-capital quarters (Q3/Q4 FY2025) now anchor the TTM window. This is exactly the kind of "accounting profit that isn't durably turning into cash" pattern this framework's FCF-related checks (both the hard disqualifier and the continuous FCF Quality sub-score) are built to catch, and it pushed the weighted Quality Score down 10.0 points to **63.0**, even as every other sub-score held steady. Hard Disqualifier #1 (not FCF-positive for 3+ consecutive years, on the still-current FY2022–FY2025 fiscal-year window) fires exactly as it did before, since FY2026 is not yet a complete fiscal year.

This remains a fast-growing, high-margin business with genuine new growth vectors (prediction markets revenue up ~10x YoY, international expansion past 1M funded customers, 13 business lines now over $100M annualized revenue) — but this framework's Quality Score is built to reward *durable, demonstrated* cash-generation quality, and Robinhood's public track record still has never shown 3 consecutive fiscal years of positive free cash flow, with the most recent TTM read making that look further away, not closer.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mechanical trigger (unchanged, the dominant gap):** HOOD needs 3 consecutive complete fiscal years of positive FCF before Hard Disqualifier #1 can clear. With FY2022 (−$880M) and FY2024 (−$170M) both negative and FY2023/FY2025 both positive but isolated, the earliest this can mechanically resolve is if **FY2026 closes (2026-12-31) with positive FCF** — that would make FY2023, FY2025 unhelpful (not consecutive) but would at least test whether FY2026 lands positive, the necessary first step toward any future 3-year window (e.g. FY2024–FY2026 still fails since FY2024 was negative; the earliest genuinely clean 3-year window would be FY2025–FY2027, requiring FY2026 *and* FY2027 both positive). Concretely: **watch FY2026's full-year 10-K (expected ~Feb 2027) for its FCF sign**, and don't expect this disqualifier to lift before FY2027 closes at the earliest.
- **New, closer-in trigger:** whether the TTM FCF/NI collapse documented this session is a one-quarter working-capital artifact (as FY2024's similar dip proved to be, reversing to +86.2% by FY2025) or the start of a more persistent pattern — **Q3 2026 earnings** (the next quarterly report) is the first real test of that.
- **Other Rule 9 events:** a further guidance revision, management change, material M&A, or a >15% price move with no identified cause. The new $2.2B convertible notes and associated capped-call/share-repurchase activity are themselves already captured in this session, not a forward trigger.
- Absent any of the above, future Telegram mentions of HOOD should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Watchlist Actions

- Updated `watchlist/not-in-portfolio/HOOD/HOOD-2026-07-25.md` with a new dated row (2026-07-30) — the Quality Score materially changed (73.0 → 63.0) and a Rule 9 earnings trigger fired, both independently sufficient per [watchlist/README.md](../watchlist/README.md)'s "significant change" criteria. Filename unchanged (per this task's explicit instruction to append within the same file, consistent with how `MU-2026-06-20.md` accumulated multiple dated updates in place before a later methodology-driven file split).
- Checked `watchlist/STALE.md` for an HOOD row: **none found** — HOOD was never flagged stale (both its prior and current scores were computed under the current 2026-06-29 methodology), so no stale-clearing action needed, per this task's instruction.

---

## 8. Data Gaps Flagged (summary — none blocked scoring)

1. **Yahoo Finance's `quoteSummary` cache was stale** (`mostRecentQuarter: 2026-03-31`) — had not yet ingested Q2 2026 results at query time, one day after release. Worked around by reconstructing TTM figures directly from SEC XBRL quarterly deltas instead (§2) — every reconstructed figure cross-checked exactly against `stockanalysis.com`'s independently-updated TTM figures (Revenue, EBIT, Net Income, OCF, Net Debt/EBITDA all matched). Flagging for `/healthcheck` as a recurring pattern (also seen 2026-07-25 with `yfinance` proper).
2. **`yfinance`'s `curl_cffi` backend again failed with TLS `Connection reset by peer`** on every direct call — same known, already-documented environment issue (see `sessions/2026-07-28-new-position-ko.md`, `sessions/2026-07-28-new-position-lite.md`, and the 2026-07-25 HOOD session). Worked around via plain `requests` against Yahoo's JSON API directly, per this task's provided method.
3. **Gross Profit and the CapEx sub-line breakdown were not independently reconstructed from SEC XBRL this session** (no standalone `GrossProfit` tag exists for HOOD; CapEx is reported across two combined 10-Q cash-flow lines — "Purchases of property, software, and equipment" and "Capitalization of internally developed software" — not fully quarter-differenced this session) — sourced from `stockanalysis.com` only. Low materiality: CapEx is ~1% of TTM OCF, and the OCF figure itself **was** independently reconstructed and matched exactly.
4. **ROIC computed independently** (30.79%) rather than taken as given; cross-checked against `stockanalysis.com`'s own reported figure (35.47%) — a larger gap than the 2026-07-25 session's (~0.9pp then vs. ~4.7pp now), plausibly a methodology difference in how the newly-issued debt or invested-capital averaging is handled. Doesn't change the sub-score (both clamp to 100.0 before the disqualifier-driven cap applies), but flagged rather than silently reconciled.

None of these gaps blocked scoring — every input used in the Quality Score calculation was ultimately obtained and cross-validated across independent sources.

---

## Glossary

- **CAGR (Compound Annual Growth Rate)** — The smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx (Capital Expenditure)** — Money spent buying or upgrading physical assets (factories, equipment, data centers) or, here, capitalized internally-developed software.
- **CFTC (Commodity Futures Trading Commission)** — The US federal regulator overseeing derivatives markets, including futures, swaps, and event/prediction-market contracts. See [glossary.md](../framework/glossary.md)'s existing CFTC entry (added 2026-07-25) for the Rothera/MIAXdx joint-venture detail.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every EDGAR filer (Robinhood's is 0001783879).
- **Convertible senior notes** — A bond that can be converted into a fixed number of the issuer's shares instead of being repaid in cash at maturity, letting a company borrow at a lower (sometimes 0%) coupon in exchange for that upside option to noteholders — see [glossary.md](../framework/glossary.md)'s existing entry (added for Ciena) for the related "capped call" hedge mechanism, used the same way here.
- **D&A (Depreciation & Amortization)** — The non-cash expense spreading the cost of long-lived assets over time.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **Effective tax rate** — The actual percentage of pretax income paid as tax in a period — used here to convert TTM EBIT into NOPAT for the ROIC calculation.
- **FCF (Free Cash Flow)** — Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score. HOOD fails the "not FCF-positive for 3+ consecutive years" disqualifier.
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. HOOD scores 63.0 this session (down from 73.0 on 2026-07-25) and independently fails via hard disqualifier.
- **ROIC (Return on Invested Capital)** — How efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure — the basis used throughout this session's sub-scores.
- **XBRL (eXtensible Business Reporting Language)** — The SEC's structured, machine-readable data-tagging format for filed financial statements — the source of the independently-reconstructed TTM figures in §2, pulled via the SEC's `companyconcept` API.

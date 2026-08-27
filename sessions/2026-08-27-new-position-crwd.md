# NEW POSITION (re-run) — CrowdStrike Holdings, Inc. (CRWD) — 2026-08-27

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, automated/unattended run)
**Date:** 27 Aug 2026
**10Y US Treasury Yield:** not fetched — this session stops at the Quality Gate below, before the Rate Environment Gate would apply
**CRWD portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)
**Prior coverage:** [watchlist/not-in-portfolio/CRWD/CRWD-2026-07-22.md](../watchlist/not-in-portfolio/CRWD/CRWD-2026-07-22.md) — first-ever evaluation (2026-07-22), Quality Score 61.1/100.0, FAILED the 80.0+ gate, independently failed by the FCF/Net Income conversion hard disqualifier. That entry's own "Next review trigger" flagged CrowdStrike's fiscal Q2 FY2027 earnings (expected late Aug/early Sep 2026) as the next checkpoint — this session is that checkpoint, triggered a few days early by the actual earnings print.
**Sector:** Technology — Cybersecurity (cloud-native endpoint/identity/cloud security platform)

---

## 0. Why this session exists — trigger source

Telegram channel `FinnInvestChannel`, post `FinnInvestChannel/3150` (2026-08-27, ~06:05:14 UTC) — a multi-item news digest. Item 8 of 11: *"CrowdStrike показала найкращий квартал в історії, акції +10% after hours"* ("CrowdStrike showed the best quarter in history, stock +10% after hours"). Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only. The claim was independently corroborated via `WebSearch` (CNBC, and CrowdStrike's own SEC 8-K filed 2026-08-26) before acting on it, then all financial figures used below were pulled fresh from CrowdStrike's own SEC filings (8-K Exhibit 99.1 + XBRL company facts), never from the post or the search summaries.

**Verdict on the trigger:** accurate and material — CrowdStrike reported fiscal Q2 FY2027 earnings (quarter ended 31 Jul 2026) after market close on 2026-08-26: revenue $1,470.897M (+25.83% YoY, beat), record net-new ARR of $332.8M (ARR growth accelerating to 51% YoY), record operating cash flow, and (per the 8-K's own consolidated income statement) a return to **GAAP net income positive** for the quarter ($5.306M) and for the six months (+$51.272M) — a dramatic swing from the prior-year comparable periods' large losses. This is a quarterly-earnings Rule 9 event in its own right (per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 9), independent of the Telegram post, and it is exactly the checkpoint the 07-22 entry's "Next review trigger" section called for — full re-evaluation proceeds below.

Two other companies named in the same digest post (NVDA, META) were checked against this framework's existing coverage and found to add no new information beyond what was already reflected in same-day/recent sessions — logged in `portfolio/snapshots/telegram-watch.md`, not re-run here. AMZN (AWS/Nvidia GPU-deployment partnership expansion) and GOOG (talent hire) were judged not to clear the Rule 9 bar (routine capacity/partnership news, no quantified guidance revision) — also logged there, not action taken.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| Live price used | **$205.21** | Yahoo Finance premarket quote, 2026-08-27 08:16:01 UTC (most recent trade) |
| Reference: last regular-session close before earnings (2026-08-25) | $185.38 | Yahoo Finance daily chart |
| Reference: 2026-08-26 regular-session close (earnings released after this close) | $189.18 | Yahoo Finance daily chart |
| Premarket move vs. 08-25 pre-earnings close | +10.68% | Computed — consistent with the triggering post's "+10% after hours" claim |
| 52-week range | $85.68 (low) – $227.50 (high) | Yahoo Finance |
| **Stock split note** | CrowdStrike effected a **4-for-1 stock split** (stock dividend) effective after close 1 Jul 2026 | 8-K Exhibit 99.1 — all price/share figures below are post-split |

`yfinance` failed this session with a persistent TLS/connection-reset error (`curl_cffi.requests.exceptions.SSLError`) even after install — worked around identically to prior sessions' documented pattern by pulling live price directly from Yahoo Finance's public chart endpoint and all financial statement data directly from SEC EDGAR (8-K Exhibit 99.1 + XBRL `companyfacts` API + the FY2026 10-K), not from the triggering post.

---

## 2. Phase 01 — Quality Score (2026-06-29 methodology)

### 2.1 Data sourcing

All figures below sourced directly from CrowdStrike's own SEC filings: [8-K Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1535527/000153552726000029/crwd-20260826xex991.htm) (filed 2026-08-26, Q2 FY2027 earnings release with full unaudited condensed consolidated statements), the [FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1535527/000153552726000010/crwd-20260131.htm) (filed 2026-03-05), and the SEC XBRL `companyfacts` API. Fiscal year ends 31 January. TTM window = last four reported quarters (Q3 FY2026 through Q2 FY2027, i.e. Aug 2025 – Jul 2026), computed as **FY2026 full year − H1 FY2026 (Feb–Jul 2025) + H1 FY2027 (Feb–Jul 2026)** — algebraically identical to summing the four discrete quarters, cross-checked against the 8-K's own disclosed FCF-margin figures (26%/24%/30%/25% for Q2FY27/Q2FY26/H1FY27/H1FY26) for internal consistency.

### 2.2 TTM figures (as of quarter ended 2026-07-31)

| Metric | FY2026 (full yr) | − H1 FY2026 | + H1 FY2027 | = TTM |
|---|---|---|---|---|
| Revenue | $4,812.005M | $2,272.386M | $2,856.526M | **$5,396.145M** |
| Gross Profit | $3,593.076M | $1,675.960M | $2,140.247M | **$4,057.363M** (75.19% margin) |
| GAAP Operating Income (Loss) | −$293.292M | −$224.170M | −$63.832M | **−$132.954M** |
| Net Income (Loss) | −$162.502M | −$175.173M | $51.272M | **+$63.943M** |
| Operating Cash Flow | $1,612.349M | $716.939M | $1,121.205M | **$2,016.615M** |
| CapEx (PP&E) | $302.108M | $116.248M | $222.037M | **$407.897M** |
| Capitalized internal-use software | $120.300M | $34.726M | $49.090M | **$134.664M** |
| Free Cash Flow (OCF − CapEx − cap. software) | | | | **$1,474.054M** (27.32% FCF margin) |
| D&A + intangible amortization | $281.451M | $132.095M | $183.287M | **$332.643M** |
| EBITDA (Operating Income + D&A) | | | | **$199.689M** |

Net Income figures use the 8-K's consolidated "Net income (loss)" line (before the small noncontrolling-interest allocation from a non-wholly-owned subsidiary — see glossary); the NCI adjustment is single-digit-to-low-double-digit $M and does not change any conclusion below.

**A note on the sign flip:** TTM Net Income is now positive (+$63.9M, vs. −$24.5M in the 07-22 session's TTM-through-Apr-2026 window) almost entirely because the terrible H1 FY2026 comparable period (−$175.173M, dominated by costs tied to the July 2024 global IT-outage incident and related litigation/customer-commitment charges) has now rolled out of the trailing-twelve-month window, not because of a fundamental step-change in the underlying cost structure. FY2026's full fiscal year, taken alone, was still a −$162.502M GAAP net loss — worse than FY2025's −$15.241M. This distinction matters directly for the hard-disqualifier test in §2.9.

### 2.3 Balance sheet (as of 2026-07-31)

| Metric | Value | Source |
|---|---|---|
| Long-term debt | $746.216M | 8-K balance sheet (no other debt line; $22.067M current operating-lease liability excluded, consistent with the 07-22 session's convention of not counting leases as debt) |
| Cash & Equivalents | $5,013.847M | 8-K balance sheet |
| **Net Debt** | **−$4,267.631M** (net cash position) | Computed |
| Total Stockholders' Equity | $5,139.525M | 8-K balance sheet (up from $4,472.605M a year earlier) |
| Invested Capital (Debt + Equity) | $5,885.741M | Computed |

### 2.4 Profitability (25% weight)

```
TTM Net Margin = 63.943 / 5,396.145 = 1.185%
NetMargin_Component = clamp((1.185/30)×100, 0, 100) = 3.95

Tax rate: statutory 21% US federal rate used (TTM effective rate off a near-breakeven pretax
  base is not a reliable input — same substitution the 07-22 session used, per Rule 6)
NOPAT = EBIT × (1 − tax) = −132.954 × (1 − 0.21) = −$105.03M
ROIC = NOPAT / Invested Capital = −105.03 / 5,885.741 = −1.785%
ROIC_Component = clamp((−1.785/30)×100, 0, 100) = 0.0

Profitability_Score = (3.95 + 0.0) / 2 = 1.98
```

No FCF-positivity cap applies (CrowdStrike is FCF-positive every fiscal year on record — see §2.9). GAAP operating income (loss) is still negative on a TTM basis (−$132.954M) despite the swing to positive Net Income — the Net Income turnaround is driven by interest income on CrowdStrike's large cash/investment balance (TTM interest income materially exceeds TTM interest expense) more than by an improvement in core operating profitability. **Profitability_Score = 1.98**

### 2.5 Margins (15% weight)

```
GrossMargin_Score = clamp((75.19/80)×100, 0, 100) = 93.99
```

No structural-trend bonus applicable (already well above the 40% threshold where that bonus applies). Gross margin has held essentially flat/high across FY2024 (75.16%), FY2025 (74.96%), FY2026 (74.66%), TTM (75.19%). **Margins_Score = 93.99**

### 2.6 Balance Sheet (15% weight)

```
Net Debt/EBITDA = −4,267.631 / 199.689 = −21.37× (net cash — deeply negative ratio)
BalanceSheet_Score = clamp(100 × (1 − (−21.37/4)), 0, 100) = clamp(634.3, 0, 100) = 100.0
```

**BalanceSheet_Score = 100.0**

### 2.7 Growth (20% weight)

```
Revenue: FY2023 $2,241.236M → FY2026 $4,812.005M (fiscal years ended Jan 2023 / Jan 2026)
3yr CAGR = (4,812.005 / 2,241.236)^(1/3) − 1 = 29.01%
Growth_Score (base) = clamp((29.01/25)×100, 0, 100) = 100.0 (capped)
```

**TAM-expansion / pricing-power modifier (+10, documented, capped — no numeric effect at the ceiling):** Q2 FY2027 module cross-sell now stands at 51%/35%/26% of subscription customers on 6+/7+/8+ Falcon modules respectively (up from the 07-22 session's cited 50%/34%/24%), record net-new ARR of $332.8M accelerating ARR growth to 51% YoY, and CrowdStrike raised its full-year FY2027 net-new-ARR growth guidance by 630bps to 34% YoY at the midpoint (source: 8-K Exhibit 99.1).

**Growth-deceleration check — reversed, not applicable:** the 07-22 session flagged an FY2024→FY2026 annual deceleration (36.35%→29.39%→21.72%) as an open watch item. This quarter's data shows that trend has **stabilized/reaccelerated**, not continued: Q1 FY2027 revenue grew +25.57% YoY and Q2 FY2027 grew +25.83% YoY (both computed from XBRL/8-K figures), and net-new ARR growth itself accelerated to 51% YoY. No −10 penalty applies. **Growth_Score = 100.0**

### 2.8 Moat Signal (15% weight)

Reusing the 07-22 session's cited evidence (unchanged fundamentals — Gartner Magic Quadrant leadership, Threat Graph network effect — not independently re-verified this session, since nothing in the Q2 print bears on them) with one freshly-cited data point:

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | 7-time consecutive Gartner Magic Quadrant Leader for Endpoint Protection (carried from 07-22 session, [CrowdStrike IR](https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-named-leader-2026-gartnerr-magic-quadranttm-endpoint)) |
| Brand premium (pricing power) | **TRUE** | Carried from 07-22 session (documented renewal price increases, high net/gross retention) |
| Network effect | **TRUE** | Threat Graph cross-customer real-time detection mechanism, unchanged (carried from 07-22 session) |
| Switching costs | **TRUE** | **Refreshed this session:** module attach now 51%/35%/26% of subscription customers on 6+/7+/8+ Falcon modules (up from 50%/34%/24% at 07-22), per 8-K Exhibit 99.1 |
| Scale cost advantage | **FALSE — not credited** | Same gap as 07-22: no cited cost-per-unit data vs. smaller competitors found |

```
Moat_Score = (4/5) × 100 = 80.0
```

### 2.9 FCF Quality (10% weight) — and the hard disqualifier

```
TTM FCF/NI Ratio = 1,474.054 / 63.943 = 23.05× (2,305%)
FCFQuality_Score = clamp(((23.05 − 0.40)/0.60)×100, 0, 100) = 100.0 (capped)
```

**The continuous TTM score is high — but this is not the disqualifier's test.** Per [quality-scoring.md](../framework/quality-scoring.md)'s 2026-08-05 rolling-window clarification, the "2+ consecutive years" hard-disqualifier test is evaluated against the **most recently completed fiscal years**, and explicitly "the test still requires the entire most-recently-completed fiscal year to be genuinely positive — a single strong quarter [or, by the same logic, a TTM window that has simply rolled a bad prior-year quarter out the back end] still cannot clear it."

| Fiscal year (ended Jan) | Net Income | FCF | Ratio |
|---|---|---|---|
| FY2023 | −$183.245M | ~$674.6M | negative (NI negative) |
| FY2024 | +$72.181M | $911.778M | 1,263% (NI positive, thin) |
| FY2025 | −$15.241M | $1,034.975M | negative (NI negative) |
| **FY2026** (most recently completed fiscal year) | **−$162.502M** | $1,189.941M | negative (NI negative) |
| TTM (thru 2026-07-31) | +$63.943M | $1,474.054M | 2,305% — but not a complete fiscal year |

**FY2025 and FY2026 are the two most recently completed fiscal years, and both carry negative GAAP Net Income** (undefined/deeply-negative FCF/NI ratio) — this is the *same* two-year window that fired the disqualifier in the 07-22 session (which additionally cited the TTM-through-April-2026 figure, also negative at the time). FY2027 (the year that would need to complete, positively, to roll FY2025 out of the window) does not close until 31 Jan 2027 — a strong H1 does not substitute for it, per the explicit "single strong quarter/year cannot clear it" language in the rolling-window ruling.

**Checked for the growth-capex carve-out — still does not apply:** TTM CapEx (PP&E + capitalized software) is $542.561M against $5,396.145M TTM revenue (10.1% of revenue) — modestly elevated vs. the 07-22 session's 7.6%, but the gap between negative-to-thin GAAP Net Income and strongly positive FCF remains driven overwhelmingly by Stock-Based Compensation (not disclosed in full here, but the same structural pattern as 07-22 — SBC add-back dwarfs the operating loss), not by heavy growth investment. The carve-out is written for the reverse pattern (elevated CapEx suppressing an otherwise-healthy FCF/NI ratio), not this one.

**FCFQuality_Score = 100.0 (continuous score), but the hard disqualifier independently fails the Quality Gate regardless — same conclusion as 07-22, retested fresh against the current fiscal-year window.**

### 2.10 Other hard disqualifiers checked

| Disqualifier | Result |
|---|---|
| FCF/NI conversion <70% for 2+ consecutive years, no growth-capex carve-out | **FIRES** — see §2.9 (FY2025, FY2026 both NI-negative) |
| Net Debt/EBITDA over threshold | Does not fire — net cash position (§2.6) |
| Not FCF-positive for 3+ consecutive years | Does not fire — FCF positive every fiscal year FY2023–FY2026 and TTM |

### 2.11 Final Quality Score

```
Quality Score = (1.98×0.25) + (93.99×0.15) + (100.0×0.20) + (100.0×0.15) + (80.0×0.15) + (100.0×0.10)
              = 0.495 + 14.0985 + 20.0 + 15.0 + 12.0 + 10.0
              = 71.5935 → rounds to 71.6
```

**Quality Score = 71.6 / 100.0 — up from 61.1 at 07-22, but still fails the 80.0+ gate on the weighted score alone, and independently fails via the FCF/NI conversion hard disqualifier (§2.9).** Per [quality-scoring.md](../framework/quality-scoring.md): *"a weighted average can't average away an outright balance-sheet or cash-flow-quality failure."* Per the operating brief, **stop here — do not proceed to Phase 02 valuation scoring or the Composite Score.**

---

## 3. Recommendation

# **PASS — Quality Score 71.6/100.0 (improved from 61.1 at 07-22, but still below the 80.0+ gate). Also independently failed by the FCF/Net Income conversion hard disqualifier (FY2025 and FY2026 — the two most recently completed fiscal years — both carry negative GAAP Net Income). Do not enter.**

CrowdStrike's Q2 FY2027 print is a genuinely strong quarter — a real revenue beat, record net-new ARR with accelerating growth, raised full-year guidance, and (for the first time since the July 2024 outage) two consecutive quarters of GAAP net income. Every score that improved this session did so on real, filed data, not on the Telegram post's framing. But the specific mechanical gate this framework tests — **complete fiscal years**, not trailing quarters — has not yet turned: FY2026, the most recently completed fiscal year, was still a GAAP net loss (driven by outage-related litigation/customer-commitment costs), and FY2027 will not complete until 31 Jan 2027. A strong H1 does not, on this framework's own explicit rolling-window ruling, substitute for a full completed fiscal year.

**No position opened — nothing to log in `decisions/`.**

---

## 4. Next review trigger

**The fiscal-year-close checkpoint that would actually resolve this:** CrowdStrike's FY2027 10-K (fiscal year ending 31 Jan 2027, filed ~March 2027). If FY2027 closes with full-year positive GAAP Net Income, the disqualifier's fiscal-year window rolls to FY2026 (negative) / FY2027 (positive) — no longer two uniformly negative years — and the hard disqualifier would not fire on that basis (subject to re-testing FY2026 alongside FY2027 fresh at that time, and to whatever the weighted score computes to under then-current data). Watch for: (1) whether H2 FY2027 (Q3+Q4, i.e. Aug 2026–Jan 2027) sustains GAAP profitability at a level that gets the full fiscal year into positive territory — H1 FY2027 alone was +$51.272M (consolidated) but FY2026's full year was −$162.502M, so H2 needs to hold; (2) continued net-new ARR growth (guided 34% YoY at the midpoint for FY2027); (3) whether TTM CapEx/Revenue (now 10.1%, up from 7.6% at 07-22) keeps rising toward a level that might eventually support a growth-capex carve-out framing, though not yet material enough to apply this session. Also standard Rule 9 triggers: any >15% unexplained price move from today's ~$205.21 reference, guidance revision, management change, or material M&A. CrowdStrike's fiscal Q3 FY2027 earnings (quarter ending 31 Oct 2026) are also due ~late Nov/early Dec 2026 and would refresh the TTM figures, though not the fiscal-year-window disqualifier test itself.

---

## 5. Files touched this session

- `sessions/2026-08-27-new-position-crwd.md` — this file
- `watchlist/not-in-portfolio/CRWD/CRWD-2026-08-27.md` — new dated row (score changed 61.1→71.6, and a Rule 9 event fired — both independently qualify as a "significant change" per [watchlist/README.md](../watchlist/README.md))

`watchlist/STALE.md` not touched (Phase 01 FAIL / not-scored-under-Composite entries are exempt from the stale-score mechanism — CRWD never reached Phase 02).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session not already defined there are noted; all others (ARR, CAGR, EBIT/EBITDA, FCF, FCF/NI conversion ratio, Gartner Magic Quadrant, Hard disqualifier, Invested Capital, Moat, Net Debt/EBITDA, Net Margin, NRR, NOPAT, Quality Score, ROIC, Rule 0, SBC, TTM, Stock split, NCI) are defined centrally in [glossary.md](../framework/glossary.md).

- **Net-new ARR** — the dollar increase in Annual Recurring Revenue added during a given period (as opposed to total ARR, a point-in-time stock measure); CrowdStrike added a record $332.8M of net-new ARR in Q2 FY2027, accelerating ARR growth to 51% YoY.

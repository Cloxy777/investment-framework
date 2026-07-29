# NEW POSITION — LMND (Lemonade, Inc.)

**Date:** 2026-07-29
**Task type:** NEW POSITION
**Trigger:** Telegram-scan (Routine 6) — new top post on t.me/FinnInvestChannel (#3007, ~10:58 UTC 2026-07-29): a bullet-point earnings summary (Revenue $294.4M +79% YoY, EPS −$0.56, In-Force Premium $1.43B +32%, FY2026 revenue guidance $1.21–1.22B) attached to an image explicitly labeled "Lemonade, Inc. (LMND)" showing the stock down ~10.79% pre-market (from a $62.11 close to $55.50 as of the screenshot's 6:44 AM EDT timestamp). LMND had no existing watchlist entry ([watchlist/not-in-portfolio/LMND/](../watchlist/not-in-portfolio/LMND/), [watchlist/in-portfolio/LMND/](../watchlist/in-portfolio/LMND/) both absent prior to this session) and is not a current holding ([portfolio/holdings.md](../portfolio/holdings.md) — not present) — per `/telegram-scan`'s decision rule, "no watchlist entry exists at all → `/new-position`."

**Per CLAUDE.md Rule 0 and the operating brief: the Telegram post's text and image were used only as the trigger and for company identification.** No number from the post (revenue, EPS, premium, guidance, or the screenshot's price) was used as scored financial data — every figure below was independently fetched from IBKR (live price) and Yahoo Finance's underlying data feed / WebSearch of Lemonade's own Q2 2026 earnings release.

---

## 0. Data-sourcing note (technical substitution, not a data gap)

Same `yfinance`-via-proxy TLS incompatibility documented in this framework's 2026-07-08/2026-07-28/2026-07-29 sessions: `yfinance`'s `curl_cffi` HTTP backend does browser-TLS-fingerprint impersonation incompatible with this session's TLS-terminating egress proxy (`SSLError: Recv failure: Connection reset by peer`, reproduced 4/4 retries). Worked around identically — plain Python `requests` (proxy-compatible) against Yahoo Finance's own public JSON endpoints:
- **Live price / intraday (Rule 0):** IBKR MCP `get_price_snapshot` (contract_id 430625913, NYSE) as primary; Yahoo `v8/finance/chart` (no crumb required) as cross-check.
- **Fundamentals:** Yahoo `v10/finance/quoteSummary` and `ws/fundamentals-timeseries` — reached this time by first visiting `fc.yahoo.com` (sets the `A3` cookie) then `finance.yahoo.com` (sets `A1`/`A1S`) before requesting a crumb from `query2.finance.yahoo.com/v1/test/getcrumb` (the crumb-first-only approach used in the 2026-07-28 KO session returned "Invalid Cookie" here; the two-step cookie warm-up fixed it). Free-tier annual history capped at 4 fiscal years (FY2022–FY2025); quarterly capped at 5 quarters (Q1 2025–Q1 2026).
- **Q2 2026 earnings (reported this morning, not yet in the historical-statement feed):** independently confirmed via WebSearch against Lemonade's own investor-relations release and third-party wire coverage (StockTitan, Yahoo Finance, Morningstar/PR Newswire) — not the triggering post.

No required Quality Score input was missing or invented. One internal cross-check discrepancy (TTM free cash flow) is flagged explicitly in §2 rather than silently resolved, consistent with "never invent or estimate financial data."

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$51.54** | IBKR `get_price_snapshot`, contract_id **430625913** (NYSE), last trade ts 2026-07-29 12:17:42 UTC (08:17 EDT, pre-market — regular session opens 13:30 UTC / 09:30 EDT today) |
| Cross-check — Yahoo Finance | $53.03 as of 12:15:53 UTC (1m45s earlier) → $51.54 is consistent with a continuing pre-market decline, not a feed error | Yahoo `v8/finance/chart`, 1-minute bars, `includePrePost=true` |
| Prior close (2026-07-28, 4:00 PM EDT) | $62.11 | Yahoo `chart` meta `regularMarketPrice`/`regularMarketTime` (1785268802 → exactly 2026-07-28 20:00:02 UTC = 4:00:02 PM EDT) — matches the triggering post's screenshot caption exactly |
| **Change vs. prior close** | **−$10.57 / −17.02%** | IBKR `change` field |
| 52-week range | $35.74 (low) – $99.84 (high) | IBKR `misc_statistics`, cross-checked against Yahoo `fiftyTwoWeekLow` $35.70 / `fiftyTwoWeekHigh` $99.90 (agree to within $0.04–$0.06) |
| Note on the triggering screenshot | Showed $55.50 (−10.79%) at 6:44 AM EDT (~10:44 UTC) | The stock kept falling for the ~90 minutes between that screenshot and this session's live pull — **exactly why Rule 0 requires a fresh live fetch, never the post's own price** |

**Two independent, near-simultaneous live feeds (IBKR + Yahoo) agree the stock is in a genuine, continuing pre-market decline.** **$51.54 is used as the live price for all arithmetic below.**

---

## 2. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md))

### Hard disqualifiers — checked first

| Disqualifier | Result | Evidence |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | **FIRES** | Annual FCF (Yahoo `ws/fundamentals-timeseries`, `annualFreeCashFlow`), every fiscal year available: FY2022 **−$173.1M**, FY2023 **−$128.3M**, FY2024 **−$20.8M**, FY2025 **−$25.9M**. Never positive in any of the 4 fiscal years on file — the disqualifier requires 3+ consecutive *positive* years to clear; LMND has zero. |
| Net Debt/EBITDA over applicable threshold (2.5× standard) | Not economically meaningful — see §Balance Sheet below (EBITDA itself is negative; the ratio's sign convention breaks down) | — |
| FCF/Net Income conversion ratio <70% for 2+ consecutive years, no growth-capex explanation | **Also technically fires**, but degenerately: Net Income has been negative every year FY2022–FY2025 ($−297.8M/−236.9M/−202.2M/−165.5M), so a "conversion ratio" computed against negative earnings doesn't carry its usual meaning (this isn't a profitable business converting earnings to cash poorly — it's an unprofitable one). Not needed as the deciding factor; the FCF-positive-3yr disqualifier above is clean and unambiguous on its own. |

**Result: hard disqualifier fires — Not FCF-positive for 3+ consecutive years.** Per quality-scoring.md, this fails the company regardless of the weighted score below. The full weighted calculation is still shown in full per "no black-box outputs."

### Sub-score calculations

**TTM basis used throughout:** Q2 2025–Q1 2026 (the four most recent complete quarters available in Yahoo's free-tier quarterly feed as of this session — Q2 2026, reported this morning, is independently confirmed via WebSearch in §4 but not yet in the structured historical-statement feed).

```
TTM Revenue    = 164.1+194.5+228.1+258.0 = 844.7M     (cross-checks exactly to Yahoo financialData.totalRevenue)
TTM Net Income = -43.9-37.5-21.7-35.8    = -138.9M    (cross-checks exactly to Yahoo defaultKeyStatistics.netIncomeToCommon)
TTM OCF        = 5.5+4.5+20.7-0.6        = 30.1M      (cross-checks exactly to Yahoo financialData.operatingCashflow)
TTM CapEx      = -2.1-1.9-3.1-3.5        = -10.6M
TTM FCF (self-computed) = 30.1 - 10.6    = 19.5M
```

**⚠️ Cross-check discrepancy flagged (not silently resolved):** Yahoo's pre-aggregated `financialData.freeCashflow` snapshot field shows **$90.9M** TTM, which doesn't match the $19.5M obtained by summing the same feed's own quarterly OCF/CapEx components above. I've used the **self-computed $19.5M** for all downstream arithmetic, since it's independently reconstructable from components that themselves cross-check exactly (OCF, revenue, net income all matched other modules precisely) — the pre-aggregated field's higher figure is unexplained and not used. **This doesn't change the bottom-line conclusion either way** — the hard disqualifier above turns on 4 full fiscal years of negative annual FCF, not the TTM quarterly figure.

**Profitability (25% weight):**
```
Net Margin (TTM) = -138.9/844.7 = -16.44%   (cross-checks to Yahoo profitMargins -0.16444)
ROE proxy (TTM NI / latest quarter equity) = -138.9/518.0 = -26.82%   (cross-checks to Yahoo returnOnEquity -26.12%, small denominator-timing difference)

NetMargin_Component = clamp((-16.44/30)×100, 0, 100) = 0.0
ROIC_Component       = clamp((-26.82/30)×100, 0, 100) = 0.0
Profitability_Score  = (0.0 + 0.0) / 2 = 0.0
```
(The FCF-positive-3yr cap of 40.0 doesn't bind here — the raw score is already 0.0, below the cap.)

**Margins (15% weight):**
```
Gross Margin (TTM) = 53.25%   (Yahoo financialData.grossMargins — quarterly gross-profit breakdown wasn't available in the free-tier timeseries feed to independently rebuild this)
GrossMargin_Score = clamp((53.25/80)×100, 0, 100) = 66.6
```
No structural-trend bonus applicable (already above the 40% static threshold).

**Growth (20% weight):**
```
Revenue 3yr CAGR (FY2022 → FY2025, GAAP filed) = (737.9/256.7)^(1/3) - 1 = 42.2%
Growth_Score = clamp((42.2/25)×100, 0, 100) = 100.0   (capped — already at the ≥25% ceiling)
```
Documented TAM-expansion evidence exists (Lemonade's own Q2 2026 release: In-Force Premium +32% YoY, expansion of Lemonade Car and bundled home/renters products — see §4) but the +10 modifier is moot; the score is already at its 100.0 ceiling.

**Balance Sheet (15% weight):**
```
Total Debt (Q1 2026, most recent reported) = $200.4M
Cash (Q1 2026)                              = $374.3M
Net Debt = 200.4 - 374.3 = -$173.9M   (net CASH position — more cash than debt)
EBITDA (TTM, Yahoo financialData.ebitda)    = -$93.6M   (negative — company posts an operating loss before D&A)

Mechanical formula as written: NetDebt/EBITDA = -173.9 / -93.6 = +1.858×   (two negatives → misleadingly "positive" leverage ratio)
BalanceSheet_Score (mechanical) = clamp(100 × (1 - 1.858/4), 0, 100) = 53.6
```
**⚠️ Flagged edge case, not silently resolved:** the formula's sign convention breaks down when EBITDA is negative — dividing a net-cash position by a negative EBITDA produces a ratio that *reads* like ~1.9× leverage, when the company is actually **debt-light in absolute terms** (net cash of $173.9M) but **loss-making at the operating level**. I've applied the formula exactly as documented (53.6) rather than unilaterally overriding it with a judgment call, and flag the discrepancy here instead. **This doesn't change the bottom-line conclusion** — the hard disqualifier above already fails the company independent of this sub-score.

**Moat Signal (15% weight):**

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | **Not established** | No independently-cited third-party market-share data sourced this session (Lemonade is a small player — ~$845M TTM revenue — within a multi-hundred-billion-dollar US P&C insurance market; not claiming a documented share position without a cited source). |
| Brand premium | **Not established** | Lemonade's own positioning and public reporting emphasize low-cost, AI-underwritten pricing, not a documented premium-pricing mechanism. |
| Network effect | **Not established** | No cited two-sided-marketplace or user-growth-driven-value mechanism found. |
| Switching costs | **Not established** | P&C insurance (renters/home/auto/pet) is annually-renewable with generally low, not high, documented switching friction. |
| Scale cost advantage | **Not established** | No cited per-unit cost data showing a gap vs. larger, more scaled competitors (State Farm, Allstate, Progressive, etc.) — Lemonade is smaller-scale, not larger. |

```
Moat_Score = (0/5) × 100 = 0.0
```
Given the hard disqualifier above already fails the company outright, no further research effort was spent trying to source moat evidence this session — marked "not established" rather than invented, per "never mark a signal true without a cited source."

**FCF Quality (10% weight):**
```
FCF/NI ratio (TTM, self-computed basis) = 19.5 / -138.9 = -14.04%
FCFQuality_Score = clamp(((-0.1404 - 0.40)/0.60) × 100, 0, 100) = 0.0
```

### Final Quality Score

```
Quality Score = (0.0×0.25) + (66.6×0.15) + (100.0×0.20) + (53.6×0.15) + (0.0×0.15) + (0.0×0.10)
              = 0.00 + 9.99 + 20.00 + 8.04 + 0.00 + 0.00
              = 38.0
```

**Quality Score: 38.0 / 100.0 — fails the 80.0+ gate** by 42 points on the weighted score alone, **and** a hard disqualifier (not FCF-positive for 3+ consecutive years — zero of the four fiscal years on file were positive) fires independently. Both point to the same conclusion.

Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md): **this stops the evaluation here.** No Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is computed. (10Y Treasury yield was not fetched this session — the Quality Gate fails before that step is reached, same precedent as the 2026-07-28 KO and 2026-07-29 MU sessions.)

---

## 3. Appendix — valuation inputs already gathered (reference only, NOT a scored Phase 02 valuation)

Shown for transparency only — **these do not combine into a Valuation Score or Composite Score**, since LMND never clears the Quality Gate that step is conditioned on:

| Metric | Value | Note |
|---|---|---|
| Market cap (live) | ≈ $3.96B | $51.54 × 76,820,789 shares outstanding (Yahoo `defaultKeyStatistics.sharesOutstanding`) |
| FCF Yield (TTM, self-computed basis) | ≈ 0.49% | $19.5M / $3.96B |
| Forward PE | Not meaningful | Forward EPS is negative (−$0.84); Yahoo reports a nonsensical −73.9× |
| P/S (TTM) | 5.65× | Yahoo `summaryDetail.priceToSalesTrailing12Months` |
| PEG / Fast Grower eligibility | Not applicable | EPS is negative every year on record — no clean positive earnings base to compute EPS growth or PEG from |
| Dividend yield | None | Company does not pay a dividend |

---

## 4. Q2 2026 Earnings — independently verified context (Rule 9 relevance)

All figures below are from Lemonade's own Q2 2026 earnings release and independent wire coverage (StockTitan, Yahoo Finance, Morningstar/PR Newswire), fetched via WebSearch — **not** from the triggering Telegram post, though several figures happen to match it:

- **Revenue:** $294.4M, **+79% YoY** — beat Street consensus (~$289M per Zacks-surveyed analysts)
- **Net loss:** $43.4M; **EPS −$0.56** — in line with the Zacks consensus estimate (also −$0.56)
- **In-Force Premium:** $1.43B, **+32% YoY** (company's own forward-run-rate metric — see Glossary)
- **Q3 2026 guidance:** revenue $323M–$326M
- **Reinsurance:** Lemonade **cut its quota-share reinsurance cession from 20% to 18%**, retaining more premium — and more underwriting risk — per policy, attributed to growing confidence in its AI-underwriting models (see Glossary)
- **Management change:** long-serving CFO Tim Bixby will move to the Board effective 2027-01-01; current SVP Finance Nick Stead becomes CFO

**This is a real, independently-confirmed Rule 9 event** (an earnings release plus a management-succession announcement), and the underlying figures are genuinely strong on their face (revenue beat, in-line EPS, accelerating in-force premium) — but the −17% pre-market reaction, combined with this session's Quality Score work, indicates the market (and this framework's structural quality check) are reacting to the same underlying issue: **a still-unprofitable, FCF-negative business retaining more risk (lower reinsurance cession) at the same time**, not a one-quarter blip. Consistent with this framework's "never act on price movement or a single quarter alone" posture, the price reaction is noted as context, not as an independent basis for the recommendation below — the Quality Gate outcome stands on its own structural merits.

---

## 5. Recommendation

**PASS — watchlist only, do not enter a position.** Quality Score 38.0 fails the 80.0+ gate by a wide margin, and a hard disqualifier (not FCF-positive for 3+ consecutive years — LMND has never had one, let alone three) independently fires. No Composite Score exists to check against the Phase 03 action table, and no fair-value/order-setup work is produced, per [fair-value-methodology.md](../framework/fair-value-methodology.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md) (both gate that step on a passing Quality Score).

**Next review trigger:** re-score if/when Lemonade posts its first full fiscal year of positive free cash flow (would be a genuine structural change to the disqualifier above), or immediately on any further Rule 9 fundamental trigger (guidance revision, M&A, further management change, or a >15% unexplained move beyond today's earnings reaction).

---

## Glossary

- **CAGR** — Compound Annual Growth Rate; LMND's 3-year revenue CAGR (42.2%) maxes out the Growth sub-score.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation & Amortization; LMND's TTM EBITDA is negative (−$93.6M), the source of this session's flagged Balance Sheet sub-score edge case.
- **EPS** — Earnings Per Share; LMND's has been negative every reported quarter and fiscal year on file.
- **FCF (Free Cash Flow)** — cash generated after running and maintaining the business; negative every fiscal year 2022–2025 for LMND, the deciding hard disqualifier this session.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; degenerate here since Net Income is negative every year, so not the deciding factor (the FCF-positive-3yr check is).
- **Hard disqualifier** — one of three Quality Score conditions that fails a company outright regardless of its weighted sub-score total; "not FCF-positive for 3+ consecutive years" fires for LMND.
- **In-Force Premium** — see glossary.md; Lemonade's own forward revenue-run-rate metric, +32% YoY this quarter, cited as context only.
- **Net Debt/EBITDA** — leverage ratio measuring years of cash profit needed to repay all debt; produces a misleading reading for LMND because EBITDA itself is negative (flagged in §2 rather than silently resolved).
- **Net Margin** — Net Income ÷ Revenue; LMND's TTM net margin is −16.44%.
- **Quality Score** — this framework's 0.0–100.0 score (higher = better) gating eligibility for Phase 02 valuation scoring; LMND scored 38.0, well below the required 80.0+.
- **Quota-share reinsurance cession** — see glossary.md; the share of premium (and risk) an insurer passes to a reinsurer — Lemonade just reduced this from 20% to 18%, retaining more risk.
- **Rate Environment Gate / Rate Regime Modifier** — the mandatory pre-Phase-02 check comparing earnings yield to the 10Y Treasury; not reached this session since the Quality Gate stopped the evaluation first.
- **ROE (Return on Equity)** — Net Income ÷ Shareholders' Equity, used here as an ROIC proxy; LMND's is −26.1% to −26.8% depending on the equity base used.
- **TTM (Trailing Twelve Months)** — the most recent 12 reported months of results; used throughout §2–3 as Q2 2025 through Q1 2026, the most recent complete window available in the free-tier data feed as of this session.

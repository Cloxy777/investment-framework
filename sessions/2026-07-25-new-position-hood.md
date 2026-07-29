# NEW POSITION — HOOD (Robinhood Markets, Inc., Class A)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run)
**Date:** 2026-07-25 (Saturday — US markets closed; most recent live trade is Friday 2026-07-24's regular-session close)
**10Y US Treasury Yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (see §3) before the Rate Environment Gate would otherwise apply (same precedent as the 2026-07-24 QCOM session).
**Current HOOD portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — first-ever evaluation of this ticker under this framework.
**Sector:** Financials — Capital Markets / Retail Brokerage & Fintech (equities, options, crypto trading; subscriptions; banking; wealth management; prediction markets)
**Filer type:** US SEC filer, CIK 0001783879, Delaware-incorporated, calendar fiscal year.
**First-use jargon decode:** see closing Glossary.

---

## 0. Why this session exists — trigger source

A Telegram post today (`bolshegold/9832`, ~16:02 UTC, 2026-07-25) was a casual "earnings to watch next week" round-up mentioning $HOOD by cashtag. Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only, and this post made no financial claims to independently verify either way. HOOD had no watchlist entry anywhere in this repo (checked both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/`), so per [telegram-scan.md](../.claude/commands/telegram-scan.md) step 4's first bullet ("no watchlist entry exists at all → `/new-position`"), this triggers a full first-time evaluation.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Contract identity** | Confirmed via `mcp__Interactive-Brokers__search_contracts`: "ROBINHOOD MARKETS INC - A", NASDAQ, contract_id **504546674** | IBKR |
| **`get_price_snapshot` result (as fetched)** | `last.price` **$101.58** (`is_close: true`), `prior-close` **$101.58** | IBKR |
| **⚠️ Data-quality flag — snapshot was stale by one trading day.** A `last`/`prior-close` both reading $101.58 with no volume was inconsistent on its face (no plausible zero-change day given surrounding volatility). Cross-checked via `get_price_history` (`ONE_DAY` bars, `TWO_WEEKS`) and independently via `stockanalysis.com`: **$101.58 was actually the 2026-07-23 (Thursday) close.** The true most recent close — **2026-07-24 (Friday), the last completed regular session before today's Saturday date** — was **$94.91** (open $100.07, high $100.08, low $93.03, volume 16,281,952), a **−6.57%** move from the $101.58 prior-day close. | IBKR `get_price_history`; independently confirmed via `stockanalysis.com` overview page, which separately reported "$94.91 (down 6.57% on Jul 24, 2026)" |
| **Live price used throughout this session: $94.91`** — the correct, most recent, real market print (Friday's close), not a stale snapshot artifact and not inferred from any multiple. Flagging this catch for the next `/healthcheck` pass, same discipline as the SPGI price-inference lesson this rule exists to prevent, though here the error was caught before it propagated. | | |
| 52-week range | $63.52 (low) – $153.86 (high) | IBKR `misc_statistics`, cross-checked vs. `stockanalysis.com` ($63.52–$153.86) |
| Dividend yield | 0.0% (no dividend) | IBKR `dividend_yield` |
| Shares outstanding | 900.51M | `stockanalysis.com` |
| Market Cap (at $94.91) | ≈$85.47B (900.51M × $94.91) | `stockanalysis.com`, internally consistent |
| Analyst consensus | Buy (28 analysts), average PT $121.40 (+27.9% from $94.91) | `stockanalysis.com` |
| Upcoming earnings | **Q2 2026 results after market close Wednesday, 2026-07-29** — 4 days after this session; options market pricing a ~9.2% implied move | WebSearch (Robinhood investor relations press release, MarketBeat, TipRanks) |

**Why Friday's ~6.6% drop happened (context only, not a scoring input, not acted on either way per Rule 9's "macro fear is not a valid trigger"):** independently verified via WebSearch as a broad, sector-wide crypto selloff (Bitcoin dipping toward the low-$60,000s before partially recovering) that hit crypto-exposed names including Robinhood, Coinbase, and crypto-mining stocks together — not a Robinhood-specific news event. This is exactly the kind of move Rule 9 says **not** to act on by itself ("price dropped... macro fear" is explicitly listed as an invalid trigger), and it is not treated as one here.

---

## 2. Data Sourcing Note

**`yfinance` was unreachable this entire session** — every call (`t.info`, tested on HOOD directly) failed with `curl_cffi.requests.exceptions.SSLError: ... Connection reset by peer`, the same Yahoo-side block/rate-limit pattern documented in the 2026-07-24 EVO session (also confirmed there as not ticker-specific). Fundamentals below are sourced from, and cross-validated across, three independent channels instead:

- **`stockanalysis.com`** (`/stocks/HOOD/financials/`, `/financials/balance-sheet/`, `/financials/cash-flow-statement/`, `/financials/ratios/`, and the ticker overview page) — annual FY2021–FY2025 figures plus TTM (through 2026-03-31).
- **SEC XBRL `companyconcept` API** (`data.sec.gov/api/xbrl/companyconcept/CIK0001783879/us-gaap/...`) — pulled directly to independently reconstruct TTM Pretax Income, Income Tax Expense, and quarterly Operating Cash Flow, and to cross-check `stockanalysis.com`'s own TTM Net Income figure.
- **Independent WebSearch** (non-Telegram, non-trigger-post sources) — used only for the qualitative Growth-modifier and Moat-signal evidence in §3.2, each cited individually at the point of use.

No required Phase 01 input was invented, estimated, or inferred from the triggering post.

**Reconciled TTM window:** Q2 FY2025 (Apr–Jun 2025) + Q3 FY2025 (Jul–Sep 2025) + Q4 FY2025 (Oct–Dec 2025, derived as FY2025-annual minus 9-month-YTD) + Q1 FY2026 (Jan–Mar 2026), i.e. through the most recently filed 10-Q (period ended 2026-03-31).

| Line item ($M) | Q2 FY25 | Q3 FY25 | Q4 FY25 (derived) | Q1 FY26 | **TTM total** |
|---|---|---|---|---|---|
| Pretax income (SEC XBRL) | 442 | 634 | 661 | 411 | **2,148** |
| Income tax expense (SEC XBRL) | 56 | 78 | 56 | 65 | **255** |
| **Net income (derived)** | | | | | **1,893** |

TTM effective tax rate = 255 / 2,148 = **11.87%**. The derived TTM Net Income ($1,893M) reconciles almost exactly with `stockanalysis.com`'s own TTM cash-flow-statement figure ($1,893M) — a genuine cross-check, not a coincidence. **Flag:** `stockanalysis.com`'s income-statement page separately showed TTM Net Income as $1,897M (a ~0.2%, immaterial gap vs. the $1,893M reconciled above, likely a noncontrolling-interest or rounding difference between that page and its own cash-flow page). Used **$1,897M** (the income-statement figure) for Net Margin below, consistent with using each source page's own headline figure; the gap does not change any conclusion.

**Flag — FY2024's tax swing:** SEC XBRL confirms FY2024 Income Tax Expense (Benefit) was **−$347M (a tax benefit)**, on Pretax Income of $1,064M, producing FY2024 Net Income of $1,411M — this is why FY2024's reported Net Margin (47.81%) is *higher* than its Operating Margin (35.72%), a one-off-tax-driven inversion of the usual relationship (Rule 6 normalization note; does not affect the TTM figures used for scoring below, which fall in the ordinary 41–42% range).

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifier check (fires regardless of weighted score)

| Hard disqualifier | HOOD data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | Annual FCF (Operating Cash Flow − CapEx, `stockanalysis.com` + SEC-XBRL-cross-checked OCF): FY2021 **−$948M**, FY2022 **−$880M**, FY2023 **+$1,179M**, FY2024 **−$170M**, FY2025 **+$1,623M**, TTM **+$3,012M**. Positive years are isolated single years surrounded by negative ones (FY2023 alone, then FY2024 negative again, then FY2025 positive) — **no 3-consecutive-year positive window exists anywhere in the 5-year lookback.** Same pattern as this framework's CBRS precedent (2026-06-29): "only [one year] was positive, surrounded by negative years on both sides... never three consecutive positive years." | **FIRES.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | HOOD carries **no debt instruments** on its balance sheet at all (confirmed: no Short/Long-Term Debt, Notes Payable, or Convertible Notes line items — only Accounts Payable, Securities Loaned, and Trading Liabilities, which are brokerage operating liabilities, not financial debt). Net Debt = Cash $5,012M − Debt $0 = **−$5,012M (net cash)**. TTM EBITDA = Operating Income $2,135M + D&A $89M = **$2,224M**. Net Debt/EBITDA = −5,012/2,224 = **−2.25×** (matches `stockanalysis.com`'s own reported −2.25 exactly). | **Does not fire** (net cash). |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FY2022: both FCF and NI negative (ratio not meaningful in the intended sense). FY2023: FCF positive/NI negative (opposite signs, not meaningful). **FY2024: FCF −$170M / NI $1,411M = −12.05%** — the one year where both the ratio and NI's sign make it a clean, meaningful <70% reading. FY2025: 86.2%. TTM: 158.8%. Only **one** year (FY2024) is unambiguously <70% on a meaningful base — not 2 consecutive years. | **Does not independently fire** (though FY2024 alone is a concerning single-year reading — moot given the disqualifier below fires regardless). |

**Hard disqualifier #1 (FCF positivity) fires, unambiguously and independently of the weighted score below** — per [quality-scoring.md](../framework/quality-scoring.md): "a weighted average can't average away an outright... cash-flow-quality failure." This alone is sufficient to fail the gate.

### 3.2 Weighted Quality Score (computed in full for transparency, per this framework's CBRS/ORCL/STM precedent of showing the complete calculation even when a hard disqualifier already fires)

**Source data** (all $ in millions; TTM = trailing twelve months through 2026-03-31):

| Metric | TTM | FY2025 | FY2024 | FY2023 | FY2022 | FY2021 |
|---|---|---|---|---|---|---|
| Revenue | 4,613 | 4,473 | 2,951 | 1,865 | 1,358 | — |
| Gross Profit | 4,392 | 4,262 | 2,787 | 1,719 | 1,179 | — |
| Operating Income (EBIT) | 2,135 | 2,094 | 1,054 | (536) | (1,011) | — |
| D&A | 89 | 86 | 77 | 71 | 61 | — |
| Net Income | 1,897 | 1,883 | 1,411 | (541) | (1,028) | — |
| Gross Margin | 95.21% | 95.28% | 94.44% | 92.17% | 86.82% | — |
| Net Margin | 41.04% | 42.10% | 47.81% | (29.01%) | (75.70%) | — |
| Cash & Equivalents | 5,012 | 4,261 | 4,332 | 4,835 | 6,339 | 6,253 |
| Total Debt | 0 | 0 | 0 | 0 | 0 | 0 |
| Total Equity | 9,688 | 9,151 | 7,972 | 6,696 | 6,956 | 7,293 |
| Operating Cash Flow | 3,034 | 1,638 | (157) | 1,181 | (852) | (885) |
| CapEx | (22) | (15) | (13) | (2) | (28) | (63) |
| FCF | 3,012 | 1,623 | (170) | 1,179 | (880) | (948) |

*(Source: `stockanalysis.com` financial-statement pages, cross-checked against SEC XBRL for the tax/income reconstruction in §2.)*

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((41.04/30)×100) = 100.0 (raw 136.8, capped). ROIC: NOPAT = TTM EBIT × (1 − effective tax rate) = 2,135 × (1 − 0.1187) = **$1,881.6M**. Invested Capital = Total Debt ($0) + Equity ($9,688M) − Cash ($5,012M) = **$4,676M**. ROIC = 1,881.6/4,676 = **40.25%** (cross-checked against `stockanalysis.com`'s own reported TTM ROIC of 39.34% — reasonably consistent, small gap likely a different invested-capital averaging convention). ROIC_Component = clamp((40.25/30)×100) = 100.0 (raw 134.2, capped). Raw avg = (100.0+100.0)/2 = 100.0 — **but the FCF-positivity cap applies** (quality-scoring.md: "If the company isn't FCF-positive for 3+ consecutive years, cap Profitability_Score at 40.0 regardless of margin/ROIC" — HOOD fails this test per §3.1). | **40.0** (capped) |
| **Margins (15%)** | GrossMargin_Score = clamp((95.21/80)×100) = 100.0 (raw 119.0, capped). No +10 structural-trend bonus — that bonus only applies to margins *below* the 40% threshold that are expanding; HOOD's is already far above 40%. | **100.0** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $1,358M → FY2025 $4,473M) = (4,473/1,358)^(1/3) − 1 = **+48.8%**. Base = clamp((48.8/25)×100) = 100.0 (raw 195.3%, capped). **+10 TAM-expansion modifier documented** (independently sourced, not from the trigger post): (1) prediction markets/event contracts hit record volumes in Q1 2026, operated through a **CFTC-licensed** futures exchange/clearinghouse via the MIAXdx joint venture (acquisition closed 20 Jan 2026) [Yahoo Finance, robinhood.com newsroom]; (2) international expansion into the EU, Singapore, and Asia-Pacific, with direct international stock investing and multi-currency support underway; (3) Robinhood Banking ($2.5B in deposits, 40% direct-deposit attach rate since launch) and Robinhood Strategies (managed portfolios, >100,000 funded customers); (4) Robinhood Gold at a record 4.34M subscribers (16% adoption); (5) **11 distinct business lines each generating $100M+ of annualized revenue** by late 2025 [Morningstar/artificall.com aggregation]. **No −10 structural-deceleration modifier applied**, despite genuine crypto-segment softness (crypto revenue −47% YoY to $134M in Q1 2026, a third consecutive quarterly decline) — this is explicitly characterized by outside coverage (CNBC, 2026-04-29) as reflecting that crypto revenue "is inherently unstable and highly cyclical," i.e. the sourced characterization is *cyclical*, not *structural*, which is what the −10 modifier specifically requires; and it is a single product line softening within a **consolidated top line that is still accelerating** (TTM $4,613M > FY2025 $4,473M > FY2024 $2,951M), not a company-wide deceleration. Growth_Score = 100.0 (already at the cap; the +10 modifier is redundant against the ceiling but shown for completeness, per "no black-box outputs"). | **100.0** |
| **Balance Sheet (15%)** | Net Debt/EBITDA = −2.25× (net cash, §3.1). BalanceSheet_Score = clamp(100×(1−(−2.25)/4)) = clamp(156.25) = **100.0**. | **100.0** |
| **Moat Signal (15%)** | See evidence table below — **1 of 5 signals** cleared the cited-evidence bar. (1/5)×100 | **20.0** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 3,012/1,897 = **158.8%**. FCFQuality_Score = clamp(((1.588−0.40)/0.60)×100) = clamp(198.0) = **100.0**. | **100.0** |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | **Conflicting/negative trend.** Robinhood's US retail equity trading volume share "at its peak was over 17%... though this has since moderated" [Morningstar-sourced aggregation via artificall.com]. Client assets and funded-customer counts continue growing in absolute terms ($280–322B client assets, 27.4M funded customers), but that reflects market appreciation and organic account growth, not necessarily *share* gains — and the one specific share-trend citation found points down from peak. Per this framework's QCOM-precedent convention (grade conservatively on conflicting evidence), **not credited.** | **FALSE** |
| Brand premium | Robinhood Gold subscriber growth (4.34M, 16% adoption) is subscription-*uptake* evidence, not the specific evidence type this signal requires (price increases without volume loss, or a documented premium vs. competitors). No such citation found this session. | **FALSE** |
| Network effect | Robinhood's retail-brokerage/app model is not a documented two-sided marketplace with the kind of user-growth-driven value mechanism this signal requires (contrast a payments network or classifieds marketplace); no such mechanism found. | **FALSE** |
| Switching costs | **Well-documented, quantified mechanism.** Robinhood's IRA transfer/contribution match program (1% standard, 3% for Gold members) requires the customer to **keep the funds in a Robinhood IRA for 5 years or the match is clawed back** (partial withdrawals trigger a proportional clawback). This is a real, citable financial penalty for leaving — a genuine switching-cost lock-in mechanism, not merely a promotional bonus. | **TRUE** |
| Scale cost advantage | Robinhood's app-based, high-volume-processing model plausibly carries a real per-customer cost advantage over smaller fintech rivals, but no specific **cost-per-unit data showing a gap vs. smaller competitors** (this signal's specific evidentiary bar) was found and independently verified this session. | **FALSE** |

### 3.3 Final weighted Quality Score

```
Quality Score = (40.0 × 0.25) + (100.0 × 0.15) + (100.0 × 0.20) + (100.0 × 0.15) + (20.0 × 0.15) + (100.0 × 0.10)
              = 10.00 + 15.00 + 20.00 + 15.00 + 3.00 + 10.00
              = 73.00 → 73.0 (rounded to nearest 0.1)
```

**73.0 < 80.0 — fails the gate on the weighted score alone**, by 7.0 points, **and Hard Disqualifier #1 (not FCF-positive for 3+ consecutive years) also fires independently and unconditionally.** Same dual-failure pattern this framework has seen before (ORCL, STM, JPM sessions): even setting the disqualifier aside, the weighted score itself does not clear 80.0. The business is genuinely strong on several axes (Margins 100.0, Growth 100.0 driven by real ~49%/yr revenue CAGR and multiple diversification vectors, Balance Sheet 100.0 on a clean net-cash position, FCF Quality 100.0 on the TTM window) — but **Profitability is mechanically capped at 40.0** by the FCF-positivity failure, and **Moat is thin at 20.0** (only the IRA-match switching-cost mechanism is solidly documented; market share evidence points the wrong way).

**Sensitivity check:** even under the most generous defensible reading of every discretionary call in this session — crediting all 5 Moat signals (Moat_Score = 100.0, contributing 15.0 instead of 3.0) — Quality Score would be 73.0 + 12.0 = **85.0**, which would *numerically* clear the weighted-score gate. **This does not matter**, because Hard Disqualifier #1 fires unconditionally and independently of any weighted-score sensitivity — quality-scoring.md is explicit that hard disqualifiers apply "regardless of weighted score." Shown here only for transparency, not as grounds to reconsider the outcome.

### Result: **Phase 01 FAIL**

Per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md): a company scoring below 80.0, or tripping a hard disqualifier, does not proceed to Phase 02. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**PASS — does not clear the Quality Score gate.** No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails this framework's quality gate two independent ways. No position is opened; no limit order is recommended.

Robinhood is a real, fast-growing, highly profitable-on-paper business (Growth 100.0 off a genuine ~49%/yr 3-year revenue CAGR spanning equities, options, crypto, subscriptions, and several newer lines; Margins 100.0; Balance Sheet 100.0 on a clean net-cash position with zero financial debt) — but this framework's Quality Score is explicitly built to reward *durable, demonstrated* quality, not a rapid but still-erratic turnaround. Robinhood has never sustained 3 consecutive fiscal years of positive free cash flow in its public history (2021–2025): each positive year (2023, 2025) has so far been immediately preceded or followed by a negative one, mechanically firing this framework's FCF-positivity hard disqualifier and independently capping the Profitability sub-score at 40.0. Layered on top of that, the Moat picture is thin (1 of 5 signals — only a specific, quantified IRA-match switching-cost mechanism — clears the evidentiary bar; the one available market-share data point shows Robinhood's core US retail equity trading share has "moderated" from its prior peak). Friday's ~6.6% price drop (to the $94.91 used throughout this session) was independently verified as a broad crypto-sector selloff, not company-specific news, and is not treated as a buying (or avoiding) signal by itself, consistent with Rule 9.

This is a name worth re-visiting once Robinhood can show a genuine, sustained (3+ consecutive fiscal year) run of positive free cash flow — the single most direct path to a materially different result, since it would both clear Hard Disqualifier #1 and remove the Profitability cap (which alone would add up to 60.0 points × 25% = 15.0 to the weighted score).

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mandatory Rule 9 re-check: Robinhood's Q2 2026 earnings, after market close Wednesday, 2026-07-29** — just 4 days after this session. Specifically worth checking: (a) whether Q2 2026 operating cash flow / FCF is positive (a second consecutive positive FY2025→2026 stretch would still not clear the 3-consecutive-year bar on its own, but is the necessary first step), (b) whether crypto revenue's 3-quarter decline continues or stabilizes, (c) any new disclosed metrics on prediction-markets/international/banking revenue contribution.
- **Mechanical trigger:** the FCF-positivity hard disqualifier is the dominant, decisive gap — HOOD needs FY2026, FY2027, and FY2028 (or any 3 consecutive fiscal years) to all show positive FCF before this disqualifier can clear. The Moat score (20.0) is the second-largest gap; independently verifiable evidence of stabilizing-or-growing overall market share (not just asset/customer growth) would be the most direct path to improving it.
- **Other Rule 9 events:** a guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause (Friday's ~6.6% move has an identified, sector-wide cause — a crypto selloff — so it does not itself constitute a fresh trigger).
- Absent any of the above, future Telegram mentions of HOOD should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Watchlist Actions

- Created `watchlist/not-in-portfolio/HOOD/HOOD-2026-07-25.md` (first-ever entry for this ticker — nothing to supersede or mark stale).

---

## 8. Data Gaps Flagged (summary — none blocked scoring)

1. **`yfinance` was unreachable this entire session** (`curl_cffi` TLS reset/connection-reset-by-peer on every call, tested directly on HOOD) — same Yahoo-side block pattern as the 2026-07-24 EVO session, confirmed there as not ticker-specific. Fundamentals sourced from `stockanalysis.com` + SEC XBRL instead. Flagging again for `/healthcheck`.
2. **IBKR's `get_price_snapshot` returned a stale price** ($101.58, actually Thursday 2026-07-23's close) rather than the true most recent close ($94.91, Friday 2026-07-24) — caught via cross-check against `get_price_history` and an independent `stockanalysis.com` fetch before it could propagate into any calculation. Flagging for `/healthcheck` — this is exactly the class of error Rule 0 exists to prevent, and while it was caught here, the snapshot tool itself returning a one-day-stale "last" print with `is_close: true` is worth investigating.
3. **Minor (~0.2%) TTM Net Income discrepancy** between `stockanalysis.com`'s income-statement page ($1,897M) and its own cash-flow-statement page / the independently-reconstructed SEC XBRL figure (both $1,893M) — immaterial, used $1,897M per the income-statement source, both shown.
4. **ROIC computed independently** (40.25%) rather than taken as given; cross-checked against `stockanalysis.com`'s own reported figure (39.34%) — reasonably consistent, small gap not investigated further since it doesn't change the sub-score (both clamp to 100.0 before the disqualifier-driven cap applies).

None of these gaps blocked scoring — every input used was ultimately obtained and cross-validated across independent sources.

---

## Glossary

- **CAGR (Compound Annual Growth Rate)** — The smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CFTC (Commodity Futures Trading Commission)** — The US federal regulator overseeing derivatives markets, including the licensed exchange/clearinghouse structure behind Robinhood's prediction-markets business.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every EDGAR filer (Robinhood's is 0001783879).
- **D&A (Depreciation & Amortization)** — The non-cash expense spreading the cost of long-lived assets over time.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **Effective tax rate** — The actual percentage of pretax income paid as tax in a period — used here to convert TTM EBIT into NOPAT for the ROIC calculation.
- **FCF (Free Cash Flow)** — Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score. HOOD fails the "not FCF-positive for 3+ consecutive years" disqualifier.
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation.
- **IRA (Individual Retirement Account) match clawback** — Robinhood's IRA-match promotional cash requires a 5-year hold or the match is clawed back — this session's one credited Moat Signal (switching costs).
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Notional volume** — The total dollar value of assets traded over a period, distinct from the revenue earned on that trading.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Prediction markets (event contracts)** — Exchange-traded contracts paying out on a future event's outcome, regulated as derivatives when offered through a licensed exchange — cited as Growth TAM-expansion evidence for HOOD.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. HOOD scores 73.0 (and independently fails via hard disqualifier).
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies eligible for valuation scoring. (HOOD does not make this list, this session.)
- **ROIC (Return on Invested Capital)** — How efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure — the basis used throughout this session's sub-scores.
- **XBRL (eXtensible Business Reporting Language)** — The SEC's structured, machine-readable data-tagging format for filed financial statements — the source of the independently-reconstructed TTM tax figures in §2, pulled via the SEC's `companyconcept` API.

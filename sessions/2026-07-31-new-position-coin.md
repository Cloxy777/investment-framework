# New Position Evaluation — COIN (Coinbase Global, Inc.)

**Task type:** NEW POSITION (Rule 9 event-triggered re-check)
**Date:** 2026-07-31
**10Y US Treasury yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (Section 3) before the Rate Environment Gate would otherwise apply, exactly as in the 2026-07-25 COIN session this one re-checks.
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — a `t.me/bolshegold` post at 2026-07-30T21:29:45Z ("$COIN — Послушал кол - ничего интересного. Расходимся до Q3", i.e. "listened to the [earnings] call — nothing interesting, see everyone at Q3") confirmed Coinbase's Q2 2026 earnings call had happened. Per Rule 0, **no claim from the post is used as a financial input anywhere below** — the post contains no numbers and is treated only as confirmation that the exact event named as "Next review trigger" in the prior session fired: *"Coinbase's Q2 2026 earnings, scheduled Thursday 2026-07-30 — a mandatory Rule 9 re-check that will roll the TTM window forward by one quarter (dropping the strong Q2 2025 quarter, adding Q2 2026)"* ([watchlist/not-in-portfolio/COIN/COIN-2026-07-25.md](../watchlist/not-in-portfolio/COIN/COIN-2026-07-25.md); [sessions/2026-07-25-new-position-coin.md](2026-07-25-new-position-coin.md)). Every number below was fetched fresh this session, independent of the post, from IBKR (live price), SEC EDGAR XBRL, and `stockanalysis.com` (cross-check).

COIN is **not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md), unaffected by this session — see Note in Section 6). Quality Score methodology version unchanged since the prior session (2026-06-29), so this is a routine Rule 9 re-check, not a stale-score reconciliation.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 481691285, NASDAQ — "COINBASE GLOBAL INC -CLASS A") | **$155.76** | `last.price`, `is_close: false`, timestamp 2026-07-31T00:19:37Z = **2026-07-30 20:19:37 EDT** — i.e. **after-hours trading**, roughly 4h19m after the 4:00pm ET regular-session close, on the same day Coinbase reported Q2 2026 results and held its earnings call. `is_close: false` and thin volume (day volume 6,130 shares at snapshot time) confirm this is a live, currently-trading after-hours print reacting to the earnings release — not a stale or inferred figure. |
| Change vs. prior close | **−$7.82 (−4.78%)** | Implies a prior (regular-session, 2026-07-30 pre-earnings) close of **≈$163.58**. `prior_close` field itself returned empty on this snapshot; the $163.58 figure is derived arithmetically from `last` + `change`, shown for context only — not used as an input to anything below. |
| Day range (regular session, 2026-07-30) | Open $160.41 / High $164.78 / Low $159.31 | Context only. |
| Bid/Ask | $155.60 / $155.80 (size 104 / 496) | Tight after-hours spread, consistent with active post-earnings trading rather than an illiquid stale quote. |
| 52-week range (IBKR `misc_statistics`) | Low **$139.18** / High **$402.16** | 13-week and 26-week highs are now both **$222.35** (down from $402.16 in the prior session six days ago) — confirms the $402.16 high fell outside the trailing 26-week window between the two sessions, i.e. it is now more than ~6 months old. Current price is **~59.7% below** the 52-week high and **~11.9% above** the 52-week low — context only, not a scoring input (Rule 0 / "never act on price movement alone"). |
| Dividend yield (IBKR) | 0.0% | No dividend. |
| **Cross-check:** independent news coverage of the same after-hours session variously reported COIN "down 6.53% to $152.90" and "sinks 5%" at different moments as the after-hours print continued moving — consistent with genuine, still-settling post-earnings after-hours trading rather than a data error. Per this framework's designated live-price connector (IBKR, account U19421206), **$155.76 is treated as the price of record**; it sits within the range of prices independently reported in the news coverage from the same evening. | | |

**Live price used throughout this session: $155.76** (after-hours, 2026-07-30 20:19 EDT).

---

## 2. Data Source Note

Same sourcing discipline as the 2026-07-25 session: `yfinance` was not attempted (documented `curl_cffi` TLS failure in this environment across multiple prior sessions) — SEC EDGAR XBRL `companyconcept` API (CIK 0001679788) used as the primary fundamentals source, direct-fetched via `curl` (not the WebFetch summarizer, after an initial WebFetch-summarized cross-check of the same endpoint produced an arithmetic error on the derived Q4 2025 net income figure — see the correction note below), cross-checked line-by-line against `stockanalysis.com`.

### 2.1 Methodology note: direct XBRL fetch vs. WebFetch summarization, and a caught error

An initial pass fetched `data.sec.gov/api/xbrl/companyconcept/.../NetIncomeLoss.json` via the WebFetch tool (which summarizes page content through a small model) and asked it to derive Q4 2025 net income by subtracting 9-month-YTD from full-year. It returned **−$600.125M**, silently inconsistent with the prior session's independently-derived **−$666.733M** for the same quarter. Rather than accept either figure on faith, the underlying JSON was re-fetched directly via `curl` and parsed with Python: **FY2025 net income ($1,260,327K) − 9-month-YTD net income (Q1+Q2+Q3 2025 = $1,927,060K) = −$666,733K** — confirming the *prior* session's figure and identifying the WebFetch-summarized number as an arithmetic error introduced by the summarization step, not a real data discrepancy. **All financial figures in this session were subsequently re-derived from directly-fetched, Python-parsed raw XBRL JSON (not WebFetch summarization) for this reason** — flagged here per "show every calculation, no black box," since it materially changes how much to trust a WebFetch-summarized numeric extraction from a large structured dataset going forward.

### 2.2 Methodology note: a real operating-cash-flow restatement discovered mid-session

While reconstructing TTM Free Cash Flow (≈ Operating Cash Flow, per the immaterial-CapEx finding in the prior session — reconfirmed below, CapEx $0 every quarter this TTM window per `stockanalysis.com`), the raw XBRL `NetCashProvidedByUsedInOperatingActivities` facts showed **two different reported values for the same historical period** depending on which filing vintage reported it — e.g. FY2023 OCF is tagged **$922,951K** in the FY2023 and FY2024 10-Ks, but **$673,376K** in the FY2025 10-K's comparative column; FY2024 OCF is **$2,556,844K** in the FY2024 10-K but **$3,103,935K** in the FY2025 10-K. This is a genuine restatement/reclassification (plausibly related to how crypto-asset purchases/sales or customer-custodial cash flows are categorized between operating and investing activities), not a data-pull error — confirmed by fetching both filing vintages directly and finding internally consistent totals within each vintage. **The most recent (FY2025 10-K) vintage is used throughout this session**, since it is the current, operative basis and also matches the figures the prior 2026-07-25 session used (FY2023 $673.38M, FY2024 $3,104M) — the two sessions are on a consistent basis. This restatement does not affect Revenue, EBIT, or Net Income (which reconciled cleanly across vintages), only the cash-flow-statement figures.

### 2.3 A note on CapEx (unchanged from prior session)

Coinbase's CapEx remains immaterial (~$0/quarter per `stockanalysis.com`'s cash-flow-statement page for every quarter in this TTM window) — consistent with the prior session's finding (Q3 2025 10-Q disclosed ~$1.13M over nine months against >$2.4B of OCF). **FCF is treated as ≈ OCF throughout this session**, unchanged methodology.

No required Phase 01 input was invented, estimated, or inferred from the triggering post.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29, unchanged since the prior session)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

All three checks use **annual (fiscal-year)** data, per the prior session's convention — unaffected by the TTM-window profitability swing discussed below.

| Hard disqualifier | COIN data (FY2025-10-K basis, restated — see §2.2) | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF (≈ OCF) by year: FY2023 **+$673.376M**, FY2024 **+$3,103.935M**, FY2025 **+$2,426.383M**, current TTM (Q3 2025→Q2 2026, derived below) **+$2,660.690M**. Positive every year and the current TTM. | **PASS — does not fire.** |
| **Net Debt/EBITDA over threshold** (2.5× standard, or 4×/6× under Upgrade 5) | As of the most recent balance sheet (2026-06-30, per Coinbase's Q2 2026 10-Q "Consolidated Balance Sheets," filed 2026-07-30): Cash $8,614.065M + Marketable investments (current) $174.778M = **$8,788.843M liquid assets**. Total debt = Current portion of LT debt ($0) + Short-term borrowings ($539.195M) + Long-term debt ($5,944.232M) = **$6,483.427M**. **Net debt = 6,483.427 − 8,788.843 = −$2,305.416M** (a **net cash** position — smaller than the prior session's −$2,661.98M at 2026-03-31, since cash fell ~$1.6B q/q while debt fell ~$1.3B q/q, but still comfortably net cash). Negative net debt keeps this ratio below threshold under any denominator. | **PASS — well under threshold (net cash).** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FCF/NI by year (restated basis): FY2023 **710.6%** ($673.376M/$94.75M), FY2024 **120.4%** ($3,103.935M/$2,578.066M — FY2024 NI per `stockanalysis.com`, unchanged from prior session), FY2025 **192.5%** ($2,426.383M/$1,260.327M). All far above 70%. (The current TTM ratio is *not* meaningful for this annual-basis check — see §3.2's flagged FCF Quality sub-score discussion; the hard disqualifier is evaluated on fiscal years only, per the prior session's established convention.) | **PASS — does not fire.** |

No hard disqualifier fires — same result as the prior session. The outcome below is decided entirely by the weighted score.

### 3.2 Sub-scores (all six, per the weighted formula)

**TTM reconstruction (Q3 2025 → Q2 2026 — the window rolls forward exactly as flagged in the prior session's "Next review trigger": Q2 2025 has dropped out, Q2 2026 has been added), sourced from SEC XBRL `companyconcept`, direct-`curl`-fetched and Python-parsed (see §2.1), cross-checked against `stockanalysis.com`'s own reported TTM totals:**

| Line item ($K) | Q3 2025 (end 2025-09-30) | Q4 2025 (derived: FY2025 10-K − 9mo-YTD) | Q1 2026 (end 2026-03-31) | Q2 2026 (end 2026-06-30) | **TTM total** | Cross-check vs. `stockanalysis.com` TTM |
|---|---|---|---|---|---|---|
| Revenue | 1,868,693 | 1,781,129 | 1,412,982 | 1,220,068 | **6,282,872** | 6,283,000 ✓ match |
| Operating Income (EBIT) | 480,532 | 273,753 | (21,421) | (113,488) | **619,376** | 619,380 ✓ match |
| Net Income | 432,552 | (666,733) | (394,117) | (359,468) | **(987,766)** | (987,770) ✓ match |
| Income Tax Expense (Benefit) | 69,591 | (219,574) | (70,588) | (35,943) | **(256,514)** | not separately reported by vendor; internal consistency check below |
| Operating Cash Flow (≈FCF) | (784,515) | 3,065,151 | 182,744 | 197,310 | **2,660,690** | 2,660,530 ✓ match (both independently derived by 9mo/FY-subtraction on the restated basis — see §2.2) |

(All four quarters' Revenue/EBIT/NI/Tax figures are each a single directly-filed SEC XBRL 3-month-duration fact — no subtraction needed for those, except Q4 2025 which is FY2025-10-K-total minus 9-month-YTD, standard TTM reconstruction, cross-checked twice: once against the prior session's independently-derived Q4 2025 figures — which match exactly — and once against `stockanalysis.com`'s own TTM totals above. **Internal consistency check:** TTM Net Income (−987,766) + TTM Tax Expense (−256,514) = TTM Pretax Income **−$1,244,280K** — i.e. Coinbase had a pretax *loss* over this TTM window even though EBIT stayed positive; the gap (−1,244,280 − 619,376 = **−$1,863,656K**) reflects non-operating items — most plausibly mark-to-market losses on Coinbase's own balance-sheet crypto holdings during a quarter where total crypto market cap fell ~11% q/q [Investing.com, "Coinbase Q2 2026 slides show strategic progress despite revenue miss," 2026-07-30] — this is a real, filed accounting result, not smoothed or adjusted away, per Rule 6/"never invent data." Effective tax rate = −256,514/−1,244,280 = **20.615%** (a tax *benefit* against a pretax loss).)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = −987,766/6,282,872 = **−15.72%** → NetMargin_Component = clamp((−15.72/30)×100, 0, 100) = **0.0** (floored — cannot go negative). NOPAT = TTM EBIT × (1 − effective tax rate) = 619,376 × (1−0.20615) = **$491,689K**. Invested Capital (2026-06-30) = Total Debt ($6,483,427K) + Equity ($13,079,665K, SEC-confirmed, reconciles exactly with Total Assets $26,460,286K − Total Liabilities $13,380,621K) − liquid assets ($8,788,843K) = **$10,774,249K**. ROIC = 491,689/10,774,249 = **4.564%** → ROIC_Component = clamp((4.564/30)×100) = **15.21**. Profitability_Score = (0.0 + 15.21)/2 = **7.61** (no FCF-positivity cap needed — already below the 40.0 cap threshold and FCF-positive 3+ years regardless, see §3.1). **This is the dominant driver of this session's result** — down sharply from 29.30 last session, because the TTM window now carries *three* loss-making quarters (Q4 2025 −$666.7M, Q1 2026 −$394.1M, Q2 2026 −$359.5M) against only one profitable quarter (Q3 2025 +$432.6M), versus the prior window's two-loss/two-profit mix that included the strong Q2 2025 (+$1,428.9M) quarter now rolled out. | **7.61** |
| **Margins (15%)** | Gross Margin (TTM) = TTM Gross Profit ($5,425,000K, `stockanalysis.com` — Coinbase does not tag a standard XBRL `GrossProfit`/`CostOfRevenue` concept, so this line is vendor-sourced rather than independently SEC-reconstructed, flagged as a minor sourcing note) ÷ TTM Revenue ($6,282,872K) = **86.35%**. GrossMargin_Score = clamp((86.35/80)×100) = clamp(107.9) = **100.0**. No separate trend bonus needed (bonus only applies below the 40% static threshold; COIN has run 80–87% every year since FY2021). | **100.00** |
| **Growth (20%)** | Revenue 3yr CAGR uses **fiscal-year** data, unaffected by the quarterly TTM swing above — unchanged from the prior session: FY2022 $3,194.208M → FY2025 $7,181.325M (both confirmed directly via SEC XBRL this session) = (7,181.325/3,194.208)^(1/3) − 1 = **+31.01%** → base = clamp((31.01/25)×100) = clamp(124.0) = **100.0** (already capped before any modifier; same TAM-expansion evidence and crypto-winter-trough base-effect caveat as the prior session apply and are not re-litigated here since the underlying annual figures are unchanged). | **100.00** |
| **Balance Sheet (15%)** | Net Debt (2026-06-30) = **−$2,305,416K** (net cash — see §3.1). BalanceSheet_Score = clamp(100×(1 − NetDebt/EBITDA/4)) clamps to **100.0** with Net Debt negative, regardless of denominator (4× standard or 6× Upgrade-5 asset-light override). | **100.00** |
| **Moat Signal (15%)** | See evidence table below — **3 of 5 signals**, unchanged from the prior session (re-verified, not blindly carried forward — see discussion below). (3/5)×100 | **60.00** |
| **FCF Quality (10%)** | TTM FCF/NI = 2,660,690/(−987,766) = **−269.4%**. FCFQuality_Score = clamp(((−2.694−0.40)/0.60)×100, 0, 100) = clamp(−515.7) = **0.0**. **Flagged as a formula edge case, not a genuine cash-quality problem**: TTM Free Cash Flow is robustly *positive* ($2.661B) — the negative ratio is a pure artifact of dividing a positive numerator by a negative denominator (TTM Net Income), not evidence that reported profit isn't converting to cash. The framework's continuous formula is applied mechanically here per "show every calculation, no black box" rather than substituting a discretionary override — but the 0.0 score should be read as "the ratio is undefined/not meaningful this TTM window," not as "cash conversion collapsed." (Does not change the gate outcome either way — see §3.3 sensitivity.) | **0.00** |

**Moat signal evidence (re-verified this session, cited per signal):**

| Signal | Evidence this session | Verdict (unchanged from 2026-07-25) |
|---|---|---|
| Market share stable/growing | Coinbase's own Q2 2026 earnings release states this was its **"3rd Consecutive Quarter of Record Crypto Trading Volume Market Share"** [investor.coinbase.com, "Coinbase Q2 Earnings," 2026-07-30], and independent coverage confirms an **all-time-high 10.3% global crypto trading-volume market share** achieved even as total crypto market cap fell ~11% q/q and spot volumes fell ~25% q/q [Investing.com, 2026-07-30] — up from the 8.6% record cited in the prior session, and specifically a *share* gain through a down market, stronger evidence than last session's. | **TRUE** (reinforced) |
| Brand premium | No new pricing-power evidence found this session (no documented price increase without volume loss). The prior session's contrary evidence (Robinhood/SoFi fee-compression pressure on Coinbase's retail transaction margins) was not contradicted by anything found this session. | **FALSE** (unchanged) |
| Network effect | No new evidence gathered this session specifically (Base-blockchain TVL/developer metrics are not typically updated week-to-week); prior session's documented mechanism (self-sustaining two-sided network effect, $5B+ TVL, $193.4M Q1 2025 fee revenue) stands uncontradicted six days later. | **TRUE** (carried forward, uncontradicted) |
| Switching costs | Same basis as prior session (OCC national-trust-charter institutional custody, $376B AUM, majority-ETF-custodian role) — no new contrary evidence found; this segment-specific evidence does not depend on quarterly trading results. | **TRUE** (carried forward, uncontradicted) |
| Scale cost advantage | No cost-per-unit data found this session either (same gap as before — a general regulatory-barrier argument, not the specific per-trade/per-account cost data the framework's evidentiary bar requires). | **FALSE** (unchanged) |

### 3.3 Final weighted Quality Score

```
Quality Score = (7.61 × 0.25) + (100.00 × 0.15) + (100.00 × 0.20) + (100.00 × 0.15) + (60.00 × 0.15) + (0.00 × 0.10)
              = 1.9015 + 15.000 + 20.000 + 15.000 + 9.000 + 0.000
              = 60.9015 → 60.9 (rounded to nearest 0.1)
```

**60.9 < 80.0 — fails the gate, by 19.1 points.** This is a **decisive** miss, unlike the prior session's 3.7-point near-miss — a swing of −15.4 points quality-score-equivalent driven almost entirely by the TTM window rolling forward exactly as the prior session's "Next review trigger" anticipated: it dropped the strong Q2 2025 quarter (+$1,428.9M net income) and picked up Q2 2026's −$359.5M miss, on top of the already-included Q4 2025 (−$666.7M) and Q1 2026 (−$394.1M) losses — three loss quarters now in the window instead of two, with the offsetting strong quarter gone.

**Sensitivity check — this fail is robust to every discretionary judgment call available:**

| Scenario | Change from primary reading | Quality Score | Gate result |
|---|---|---|---|
| **Primary reading (this session)** | — | **60.9** | **FAIL** |
| Most generous FCF Quality treatment | FCFQuality_Score = 100.0 instead of 0.0 (i.e. treat the formula artifact in §3.2 as fully non-penalizing) | 70.9 | **FAIL** |
| Most generous Moat treatment | Moat_Score = 100.0 (5/5, crediting Brand premium and Scale cost advantage despite lacking the required evidence — the same "maximally generous, evidence-discipline-breaking" reading flagged as questionable in the prior session) | 66.9 | **FAIL** |
| Both generous treatments combined | FCFQuality 100.0 *and* Moat 100.0 | 76.9 | **FAIL — still 3.1pts short** |

**Unlike the prior session, no combination of defensible (or even indefensible) discretionary readings clears the 80.0 gate this time.** Profitability's collapse to 7.61 is the load-bearing number, and it is not a judgment call — it is a direct, mechanical consequence of the TTM window now containing three loss-making quarters against one profitable one.

### Result: **Phase 01 FAIL**

Per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md): a company scoring below 80.0 does not proceed to Phase 02. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**FAIL — does not clear the Quality Score gate**, at **60.9 vs. the strict 80.0+ bar**, missing by 19.1 points — a decisive fail, in contrast to the prior session's 76.3 (a 3.7-point near-miss). No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup were computed.

The mechanical driver is fully traceable and was, in fact, explicitly anticipated in the prior session's "Next review trigger": rolling the TTM window forward by one quarter (per the standard Rule 9 quarterly-earnings re-check) dropped Q2 2025's strong +$1,428.9M net income quarter and added Q2 2026's −$359.5M miss, on top of the Q4 2025 (−$666.7M) and Q1 2026 (−$394.1M) losses already in the window from last time. The result: TTM Net Margin swung from +12.20% to **−15.72%**, and TTM ROIC fell from 5.38% to 4.56% (still positive, since TTM EBIT stayed positive at +$619.4M — the loss is concentrated below the operating-income line, in a ~$1.86B non-operating item most plausibly tied to mark-to-market losses on Coinbase's own crypto holdings as the total crypto market fell ~11% q/q this quarter). Margins (100.0), Growth (100.0), and Balance Sheet (100.0) remain unchanged and excellent — gross margin 86.35%, 3yr revenue CAGR +31.0%, and a genuine net-cash balance sheet (−$2.305B net debt as of 2026-06-30) are all untouched by this quarter's earnings miss. Moat (60.0, 3 of 5 signals — market-share evidence actually *strengthened* this quarter, with Coinbase posting a record 10.3% global trading-volume share even as the broader crypto market contracted) is likewise little-changed. The **FCF Quality sub-score (0.0)** is flagged explicitly as a formula artifact rather than a genuine cash-conversion failure — Coinbase's TTM operating cash flow remained solidly positive at +$2.66B; the 0.0 score is a mechanical consequence of dividing by a negative Net Income denominator, not evidence of earnings-quality deterioration on the cash side. Even under every generous discretionary reading available (full credit on both the FCF Quality artifact and a maximal 5/5 Moat reading combined), the score would still fall 3.1 points short of the gate — this is a robust, not a knife-edge, fail.

This continues the pattern flagged in the prior session's §2.2: Coinbase's earnings quality is directly and heavily whipsawed by the underlying crypto asset class's price cycle (both through operating trading-revenue volatility and, this quarter, through non-operating balance-sheet mark-to-market effects) — a real, structural characteristic of this business model under this framework's quality lens, independent of where the stock happens to be trading or how cheap it might look after a ~60% drawdown from its 52-week high. The triggering Telegram post was a dismissive one-line reaction to the earnings call ("nothing interesting, see everyone at Q3") — not itself treated as a financial input, but its confirmation that the earnings event had occurred correctly triggered this mandatory Rule 9 re-check, which is exactly the mechanism working as designed.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance. Per the orchestrator's instructions, [portfolio/holdings.md](../portfolio/holdings.md) was not touched this session.

---

## 6. Next Review Trigger

- **Mandatory Rule 9 re-check:** Coinbase's **Q3 2026 earnings** (date not yet announced as of this session) will again roll the TTM window forward by one quarter — dropping Q3 2025 (+$432.6M, the one profitable quarter in the current window) and adding Q3 2026. Whether the Quality Score recovers depends heavily on whether Q3 2026 returns to profitability (both operationally and on the non-operating/crypto-mark-to-market line) and whether Q2 2026's −$359.5M loss is the trough or part of a continuing pattern.
- **Mechanical trigger:** Profitability (7.61) is now the overwhelmingly dominant gap to the 80.0 gate (a 19.1-point overall shortfall, of which Profitability alone accounts for ~5.4 points versus its prior-session level, with the FCF Quality artifact contributing a further ~2.5 points that would resolve automatically once TTM Net Income returns to positive territory, since the ratio's sign flips back to something the formula treats sensibly). A sustained return to TTM profitability is the single most direct path back toward the gate; the Moat sensitivity table in §3.3 shows the Moat/FCF-Quality levers alone cannot close a gap this size.
- **Other Rule 9 events:** a guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause (this session's ~4.8% after-hours move is a direct, identified reaction to the Q2 2026 earnings miss, not unexplained).
- Absent any of the above, future Telegram mentions of COIN should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **10-K (Annual Report)** — The annual financial-disclosure report a US public company must file with the SEC, containing full audited financial statements, MD&A, and risk factors.
- **10-Q (Quarterly Report)** — The quarterly financial-disclosure report filed between annual 10-Ks — used here to reconstruct trailing-twelve-month (TTM) figures through the most recently filed quarter.
- **After-hours trading** — Trading that happens after a US exchange's regular session closes (4:00pm ET) but before the next day's regular session opens — thinner volume and wider spreads, but still a genuine, live traded price used as this session's Rule 0 price of record.
- **CAGR (Compound Annual Growth Rate)** — The smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every EDGAR filer (Coinbase's is 0001679788).
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **Effective tax rate** — The actual percentage of pretax income paid (or, here, refunded as a benefit against a pretax loss) as tax in a period — used to convert TTM EBIT into NOPAT for the ROIC calculation.
- **FCF (Free Cash Flow)** — Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; can turn negative (and formula-undefined) when Net Income itself is negative, as flagged this session.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score — none fired for COIN this session.
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Pretax income** — Net Income + Tax Expense (or − Tax Benefit) — earnings before the tax provision, which this session showed can be negative even when EBIT is positive if large non-operating items sit between the two lines.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. COIN scores 60.9 this session (down from 76.3 on 2026-07-25).
- **ROIC (Return on Invested Capital)** — How efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure — the basis used throughout this session's sub-scores.
- **XBRL (eXtensible Business Reporting Language)** — The SEC's structured, machine-readable data-tagging format for filed financial statements — the source of the independently-reconstructed TTM figures in Section 3.2, pulled via the SEC's `companyconcept` API.

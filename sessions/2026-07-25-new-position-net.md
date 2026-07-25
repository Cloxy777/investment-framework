# NEW POSITION — NET (Cloudflare, Inc., Class A)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run)
**Date:** 2026-07-25 (Saturday — US markets closed; most recent live trade is Friday 2026-07-24's regular-session close)
**10Y US Treasury Yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (see §3) before the Rate Environment Gate would otherwise apply (same precedent as the 2026-07-25 COIN/HOOD sessions and the 2026-07-24 QCOM session before them).
**Current NET portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — first-ever evaluation of this ticker under this framework.
**Sector:** Technology — Internet Infrastructure / Security (CDN, DNS, DDoS mitigation, Zero Trust network security, edge compute)
**Filer type:** US SEC filer, CIK 0001477333, Delaware-incorporated, calendar fiscal year.
**First-use jargon decode:** see closing Glossary.

---

## 0. Why this session exists — trigger source

A Telegram post today (`bolshegold/9832`, ~16:02 UTC, 2026-07-25) was a casual "earnings to watch next week" round-up mentioning $NET by cashtag (Cloudflare reports Q2 2026 earnings 2026-08-06). Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only, and this post made no financial claims to independently verify either way. NET had no watchlist entry anywhere in this repo (checked both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/`), so per [telegram-scan.md](../.claude/commands/telegram-scan.md) step 4's first bullet ("no watchlist entry exists at all → `/new-position`"), this triggers a full first-time evaluation.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Contract identity** | Confirmed via `mcp__Interactive-Brokers__search_contracts`: "CLOUDFLARE INC - CLASS A", NYSE, contract_id **382633646** | IBKR |
| **`get_price_snapshot` result (as fetched)** | `last.price` **$262.32** (`is_close: true`), `prior-close` **$262.32** | IBKR |
| **⚠️ Data-quality flag — snapshot was stale by one trading day**, the same class of error caught in the 2026-07-25 HOOD session. A `last`/`prior-close` both reading $262.32 was cross-checked via `get_price_history` (`ONE_DAY` bars, `TWO_WEEKS`): the daily close series shows **2026-07-23 (Thursday) closed at $262.32**, while **2026-07-24 (Friday) — the last completed regular session before today's Saturday date — closed at $262.15** (open $265.96, high $266.80, low $261.50, volume 900,076). Independently cross-checked via `stockanalysis.com`'s overview page, which separately reported **"$262.15 (-0.06%)"** as the current price — confirms $262.15, not the stale $262.32 snapshot value. | IBKR `get_price_history`; independently confirmed via `stockanalysis.com` |
| **Live price used throughout this session: $262.15** — the correct, most recent, real market print (Friday's close), not a stale snapshot artifact and not inferred from any multiple. Flagging this catch for the next `/healthcheck` pass — the same `get_price_snapshot` staleness pattern has now been seen in consecutive sessions (HOOD and NET, both 2026-07-25). | | |
| 52-week range | $158.83–$159.18 (low) – $290.82–$291.00 (high) | IBKR `misc_statistics` ($158.84/$290.82) vs. `stockanalysis.com` ($158.83/$291.00) — trivial (~$0.18) rounding-level discrepancy between sources, not material to any calculation below |
| Dividend yield | 0.0% (no dividend) | IBKR `dividend_yield` |
| Shares outstanding | 354.94M | `stockanalysis.com` |
| Market Cap (at $262.15) | ≈$93.05B | `stockanalysis.com`, internally consistent (354.94M × $262.15 ≈ $93.05B) |
| Analyst consensus | Buy (34 analysts), average PT $259.84 (**−0.88%**, i.e. slightly *below* the live price) | `stockanalysis.com` |
| Upcoming earnings | **Q2 2026 results, August 6, 2026** — 12 days after this session | `stockanalysis.com` |

**Live price used throughout this session: $262.15.**

---

## 2. Data Sourcing Note

**`yfinance` was unreachable this entire session** (`t.info`, `t.fast_info`, tested directly on NET, 3 retry attempts) — every call failed with `curl_cffi.requests.exceptions.SSLError` / `Connection reset by peer`, the identical Yahoo-side block pattern documented in the 2026-07-25 COIN/HOOD sessions and the 2026-07-24 QCOM/EVO sessions before them (confirmed there as not ticker-specific). Fundamentals below are sourced from, and cross-validated across, two independent channels instead:

- **`stockanalysis.com`** (`/stocks/NET/financials/`, `/financials/balance-sheet/`, `/financials/cash-flow-statement/`, `/financials/ratios/`, and their quarterly variants, plus the ticker overview page) — annual FY2021–FY2025 figures, the 5 most recent quarters (Q1 2025 → Q1 2026) for TTM reconstruction, and headline ratios including a directly-reported TTM ROIC figure.
- **SEC EDGAR** — used only to confirm Cloudflare's CIK (0001477333) via a company search; the detailed fundamentals below come from `stockanalysis.com`'s own line items (cross-checked internally — e.g. TTM revenue reconciles against the reported annual growth rate) rather than a separate from-scratch SEC XBRL pull this session, since `stockanalysis.com`'s quarterly income/balance-sheet/cash-flow pages already provided the full data needed for every required Quality Score input, consistently sourced from one vendor.
- **Independent WebSearch** (non-Telegram, non-trigger-post sources) — used only for the qualitative Growth-modifier and Moat-signal evidence in §3.2, each cited individually at the point of use.

No required Phase 01 input was invented, estimated, or inferred from the triggering post.

**Reconciled TTM window:** Q2 2025 (Apr–Jun 2025) + Q3 2025 (Jul–Sep 2025) + Q4 2025 (Oct–Dec 2025) + Q1 2026 (Jan–Mar 2026), i.e. through the most recently completed fiscal quarter (Cloudflare's Q2 2026 results are not out until 2026-08-06, after this session).

| Line item ($M) | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | **TTM total** |
|---|---|---|---|---|---|
| Revenue | 512.32 | 562.03 | 614.51 | 639.76 | **2,328.62** |
| Gross Profit | 383.64 | 415.71 | 452.55 | 455.60 | **1,707.50** |
| Operating Income (EBIT) | (67.26) | (37.46) | (49.23) | (61.99) | **(215.94)** |
| Net Income | (50.45) | (1.29) | (12.08) | (22.93) | **(86.75)** |
| D&A | 70.84 | 78.31 | 82.95 | 91.22 | **323.32** |
| Free Cash Flow (reported) | 39.89 | 82.49 | 105.22 | 93.10 | **320.70** |

TTM Gross Margin = 1,707.50 / 2,328.62 = **73.32%**. TTM Net Margin = −86.75 / 2,328.62 = **−3.73%**. TTM EBITDA = EBIT + D&A = −215.94 + 323.32 = **$107.38M** (positive, despite an operating loss — D&A is large enough to flip the sign). TTM ROIC per `stockanalysis.com`'s own directly-reported figure: **−27.46%** (independently sanity-checked below).

**Balance sheet as of the most recent quarter (2026-03-31):** Cash $932.23M + Short-Term Investments $3,232M = $4,164.23M liquid assets; Total Debt $3,525M; Total Equity $1,527M. **Net Debt = 3,525 − 4,164.23 = −$639.23M** (a net cash position).

### 2.1 A note on Cloudflare's persistent GAAP unprofitability

Cloudflare has **never reported a GAAP-profitable fiscal year** in the 5-year lookback available (FY2021 −$260.31M through FY2025 −$102.27M, TTM −$86.75M) despite 29–52%/year revenue growth every year and a stable ~73–78% gross margin — losses have narrowed but never crossed to positive. This is the direct, undistorted cause of the Profitability sub-score in §3.2 (both Net Margin and ROIC are negative, clamping their component scores to the 0.0 floor) and creates a genuine edge case for the FCF Quality sub-score (§3.2), whose formula was built assuming a positive Net Income denominator. Both are shown in full below with the caveat flagged at the point of use, consistent with "never invent or estimate financial data" and "show every calculation."

### 2.2 Independent ROIC sanity check

`stockanalysis.com`'s directly-reported TTM ROIC of **−27.46%** was cross-checked with an independent reconstruction: NOPAT ≈ TTM EBIT (−$215.94M) × (1 − effective tax rate); Invested Capital = Total Debt ($3,525M) + Equity ($1,527M) − Cash & ST Investments ($4,164.23M) = **$887.77M**. Even before pinning down an exact effective tax rate (obscured by the consolidated pretax loss), NOPAT/Invested Capital lands in roughly the −20% to −25% range — the same order of magnitude and sign as the vendor-reported −27.46%. Given both figures are decisively negative (and the Quality Score's clamp floors any negative component at 0.0 regardless of exact magnitude), the vendor figure is used directly rather than forcing a from-scratch reconciliation.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifier check (fires regardless of weighted score)

| Hard disqualifier | NET data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | Annual FCF (`stockanalysis.com`, Operating Cash Flow − CapEx): FY2021 **−$28.34M**, FY2022 **−$20.01M**, FY2023 **+$140.01M**, FY2024 **+$195.39M**, FY2025 **+$287.5M**, TTM **+$320.70M**. **Three consecutive positive fiscal years (FY2023–FY2025), plus the current TTM also positive** — clears the "3+ consecutive years" bar. | **PASS — does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard, or 4×/6× under the Upgrade 5 asset-light override)** | As of the most recent balance sheet (2026-03-31): Net Debt = **−$639.23M** (a **net cash** position — see §2). Net Debt/EBITDA is negative under any denominator (standard 2.5×, or an asset-light 4×/6× override, moot either way since Cloudflare is not a payment network/exchange and the override wouldn't apply regardless). | **PASS — well under threshold (net cash).** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | Net Income is **negative every year in the 5-year lookback and in the TTM window** (FY2021 −$260.31M through TTM −$86.75M), while FCF has been positive since FY2023. Every year's FCF/NI ratio is therefore **opposite-signed** (positive FCF ÷ negative NI), which is not a meaningful reading of "cash conversion of positive earnings" in the sense this disqualifier is built to catch — the same treatment established for opposite-signed years in the 2026-07-25 HOOD session ("FCF positive/NI negative — opposite signs, not meaningful"). **Flagged explicitly:** a maximally literal reading (treating any negative ratio as trivially "<70%") would count every year as failing and fire this disqualifier outright; this session follows the established precedent of not firing on opposite-signed years. **This judgment call does not change the outcome** — see §3.3, where the weighted score alone already fails the 80.0 gate by a wide margin under every sensitivity checked. | **Does not independently fire (see caveat).** |

No hard disqualifier fires under this session's primary reading; the one genuine judgment call (FCF/NI sign-conflict) is flagged and shown not to matter to the final result.

### 3.2 Sub-scores (all six, per the weighted formula)

**Source data:** TTM figures per §2 table above (Q2 2025 → Q1 2026); annual figures from `stockanalysis.com`'s FY2021–FY2025 statement pages.

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = −86.75/2,328.62 = **−3.73%** → NetMargin_Component = clamp((−3.73/30)×100, 0, 100) = clamp(−12.42) = **0.0**. ROIC (TTM, vendor-reported, independently sanity-checked in §2.2) = **−27.46%** → ROIC_Component = clamp((−27.46/30)×100, 0, 100) = clamp(−91.53) = **0.0**. Profitability_Score = (0.0 + 0.0)/2 = **0.0** (no additional FCF-positivity cap needed — already at the floor; the cap wouldn't apply anyway since NET passes the 3-consecutive-year FCF-positivity test per §3.1). | **0.0** |
| **Margins (15%)** | Gross Margin (TTM) = **73.32%** (per §2; consistent with FY2021–FY2025's stable 74.5–77.6% band). GrossMargin_Score = clamp((73.32/80)×100, 0, 100) = clamp(91.65) = **91.65**. No +10 structural-trend bonus — margin has been well above the 40% threshold in every year shown (bonus only applies below 40% while expanding); if anything the trend is a mild multi-year compression (77.59% FY2021 → 73.32% TTM), not an expansion, so no bonus either way. | **91.65** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $975.24M → FY2025 $2,168M) = (2,168/975.24)^(1/3) − 1 = **+30.51%** → base = clamp((30.51/25)×100, 0, 100) = clamp(122.04) = **100.0** (already at the cap before any modifier). **TAM-expansion modifier considered but immaterial to the outcome given the cap:** documented evidence found this session — Cloudflare's Workers AI / edge-inference platform, its Zero Trust security suite, and its Developer Platform (R2 object storage, Workers) are frequently cited as durable growth vectors beyond the original CDN business, and Q1 2026 revenue growth (+33.5% YoY, $479.09M → $639.76M) shows **no sign of deceleration** relative to the 3yr CAGR — if anything a mild re-acceleration. **No −10 structural-deceleration modifier applies.** Growth_Score = **100.0** either way, since the raw CAGR already saturates the formula. | **100.0** |
| **Balance Sheet (15%)** | Net Debt (2026-03-31) = **−$639.23M** (net cash — see §3.1/§2). TTM EBITDA = **$107.38M** (positive, despite the operating loss, because D&A ($323.32M TTM) more than offsets the EBIT loss ($215.94M TTM)). Net Debt/EBITDA = −639.23/107.38 = **−5.95×**. BalanceSheet_Score = clamp(100×(1 − NetDebt/EBITDA/4), 0, 100) — with Net Debt negative, this evaluates well above 100 and clamps to **100.0** regardless of which denominator (4× standard or a 6× asset-light override, not applicable to this business anyway) would otherwise apply. | **100.0** |
| **Moat Signal (15%)** | See evidence table below — **3 of 5 signals** cleared the cited-evidence bar. (3/5)×100 | **60.0** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 320.70 / −86.75 = **−3.698** (**−369.8%**) — a direct consequence of Net Income being negative while FCF is positive (§2.1), not of poor cash conversion of positive earnings (the scenario this sub-score's formula was built to measure). FCFQuality_Score = clamp(((−3.698 − 0.40)/0.60)×100, 0, 100) = clamp(−682.9) = **0.0**. **Caveat flagged explicitly:** this formula, applied literally to real (not invented) inputs, mechanically floors at 0.0 for *any* combination of positive FCF and negative Net Income, regardless of how large the FCF is relative to the loss — it is not distinguishing "Cloudflare converts cash well" from "Cloudflare converts cash poorly" here, just reflecting that the ratio's intended positive-earnings-quality signal doesn't apply to a company that is FCF-positive but not yet GAAP-profitable. Shown per "no black-box outputs," with the caveat that this sub-score is not informative in NET's specific case. | **0.0** |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | **Well-documented, multiple independent citations.** Cloudflare holds an estimated **~61% market share of the global CDN front-end traffic market** as of mid-2026, is the most popular CDN by website count (**42M+ websites, ~38.5% share**), serves **>20% of all global internet request traffic**, and is **the largest managed DNS service provider** in the world, serving 25M+ websites [demandsage.com "Cloudflare Statistics (2026)"; techrt.com "Cloudflare Statistics 2026"]. | **TRUE** |
| Brand premium | **No supporting evidence found; the specific evidence found points the opposite direction.** No documented instance of Cloudflare raising prices without volume loss. Independent cost-comparison research found this session states Cloudflare is typically **"5–15x cheaper than AWS WAF and 10–20x cheaper than Akamai at scale"** [CloudZero 2025 analysis, cited via search] — i.e. Cloudflare's market position is built on being a *lower-cost* alternative to incumbents like Akamai, not a premium-priced one. This is the opposite of the evidentiary bar this signal requires. | **FALSE** |
| Network effect | **Documented, specific mechanism.** Cloudflare's global edge network (300+ cities) processes an estimated **215 billion cyber threats per day**, and analyst coverage describes this as a "threat-intelligence flywheel" — the more traffic and customers on the network, the better its threat detection gets for every customer, a genuine two-sided/scale-driven network effect distinct from simple infrastructure scale [Wide-moat coverage cited via search, e.g. earningsmoat.com/koalagains-style analysis]. | **TRUE** |
| Switching costs | **Well-documented, multiple specific product mechanisms.** Enterprise customers who adopt **Magic Transit** (network-layer DDoS protection for a customer's entire IP range), **Zero Trust** (network security), and **Workers** (edge compute) face "significant migration complexities" per independent analyst coverage — as customers consolidate more of these integrated services onto Cloudflare's stack, "it becomes increasingly complex and costly to migrate to a competitor." The shift toward larger enterprise "pool of funds" contracts is separately cited as deepening this lock-in via longer sales cycles and larger, more integrated contract values. | **TRUE** |
| Scale cost advantage | The same cost-comparison research cited under Brand premium above (Cloudflare priced well below AWS WAF/Akamai) is a **customer-facing price** comparison, not the specific evidentiary bar this signal requires (**internal cost-per-unit data** showing a gap vs. smaller competitors). No such internal cost-structure citation was found this session — Cloudflare's own TTM gross margin (73.32%) is in fact *below* several of its more premium-priced competitors, which cuts against inferring a clean internal cost advantage from the pricing gap alone. | **FALSE** |

### 3.3 Final weighted Quality Score

```
Quality Score = (0.0 × 0.25) + (91.65 × 0.15) + (100.0 × 0.20) + (100.0 × 0.15) + (60.0 × 0.15) + (0.0 × 0.10)
              = 0.000 + 13.7475 + 20.000 + 15.000 + 9.000 + 0.000
              = 57.7475 → 57.7 (rounded to nearest 0.1)
```

**57.7 < 80.0 — fails the gate, by 22.3 points** — a decisive miss, not a close one. Three of six sub-scores are strong-to-perfect (Growth 100.0, Balance Sheet 100.0, Margins 91.65), and Moat is respectable at 60.0 (3 of 5 signals: market share, network effect, switching costs, all backed by specific, independently-sourced evidence) — but **Profitability (0.0)** and **FCF Quality (0.0)**, both driven by Cloudflare's persistent GAAP unprofitability (§2.1), together account for 35% of the total weight at a full floor, and there is no amount of Growth/Balance-Sheet/Margin strength that can offset a 35%-weighted double-zero.

**Sensitivity check (holding Profitability and FCF Quality fixed at their mechanically-floored 0.0, since neither is a discretionary judgment call — both are direct floors from negative Net Income):**

| Moat reading | Signals credited TRUE | Moat_Score | Quality Score | Gate result |
|---|---|---|---|---|
| Most conservative | 0 of 5 (drop Market share on the "global ~6% vs. Binance-style dominant-competitor" argument used elsewhere in this framework — not actually applicable here, shown only for completeness) | 0.0 | 48.7 | FAIL |
| Conservative | 2 of 5 (drop Switching costs — treat the "increasingly complex" language as too generic without a more quantified lock-in citation) | 40.0 | 54.7 | FAIL |
| **Primary reading (this session)** | **3 of 5 (Market share, Network effect, Switching costs)** | **60.0** | **57.7** | **FAIL** |
| Generous | 4 of 5 (also credit Scale cost advantage on the cost-comparison evidence, despite it being customer price rather than internal cost-per-unit data) | 80.0 | 60.7 | FAIL |
| Maximally generous | 5 of 5 (also credit Brand premium despite the documented evidence pointing the opposite way) | 100.0 | 63.7 | **FAIL — still 16.3pts short** |

**The gate outcome is robust to every possible reading of the Moat signal, including the maximally generous one** — the ceiling of what NET could plausibly score under this session's data is 63.7, still well below the strict 80.0 bar. The FCF/NI hard-disqualifier judgment call flagged in §3.1 is similarly immaterial: whether or not that disqualifier is deemed to "fire," the outcome is the same (FAIL), so this session's precedent-following, non-firing reading does not paper over a marginal result — it is a genuinely decisive miss driven by Cloudflare's sustained GAAP unprofitability.

### Result: **Phase 01 FAIL**

Per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md): a company scoring below 80.0 does not proceed to Phase 02. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**FAIL — does not clear the Quality Score gate**, at **57.7 vs. the strict 80.0+ bar**, missing by 22.3 points, robust to every sensitivity checked (ceiling of 63.7 under the most generous defensible Moat reading). No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup were computed — that work is reserved for names that clear this framework's quality bar first.

Cloudflare is, by several measures, a genuinely strong and fast-growing infrastructure business: 29–52%/year revenue growth every year since 2021 with **no sign of deceleration** (Growth 100.0), a stable ~73–78% gross margin (Margins 91.65), a clean net-cash balance sheet with zero net leverage (Balance Sheet 100.0), and a moat picture with real, specific, independently-sourced evidence behind three of five signals (dominant CDN/DNS market share, a documented network-effect "threat-intelligence flywheel," and well-documented multi-product switching costs — Moat 60.0). What sinks the Quality Score is that **Cloudflare has never reported a GAAP-profitable fiscal year** in this framework's 5-year lookback, and its trailing-twelve-month Net Income remains negative (−$86.75M) despite the company being solidly FCF-positive (+$320.70M TTM) — this framework's Profitability sub-score (built on Net Margin and ROIC, both of which require positive earnings to score above zero) and FCF Quality sub-score (built on a ratio that assumes a positive-earnings denominator) both mechanically floor at 0.0, together accounting for 35% of total weight. This is a legitimate reflection of this framework's explicit preference for *demonstrated, durable* profitability (not merely revenue growth or cash generation) as a component of quality — not a data gap or a close call.

The triggering post was a passing cashtag mention in a generic "earnings to watch" round-up ahead of Cloudflare's 2026-08-06 report, not a claimed fundamental event, and per Rule 9's non-negotiables, no action is warranted from the trigger itself.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mandatory Rule 9 re-check:** Cloudflare's Q2 2026 earnings, scheduled **Thursday, August 6, 2026** — 12 days after this session. Specifically worth checking: (a) whether the company has moved any closer to GAAP net-income breakeven (the single dominant gap to this framework's gate), since losses have narrowed every year (FY2021 −$260.31M → FY2025 −$102.27M → TTM −$86.75M) but never crossed to positive; (b) whether revenue growth continues at its current ~30%+ pace or decelerates; (c) any new disclosed metrics on Workers AI, R2, or Zero Trust adoption that could bear on the Growth/Moat modifiers (though both are already at or near their ceilings).
- **Mechanical trigger:** Profitability (0.0) and FCF Quality (0.0) are the dominant, decisive gaps — together worth 35% of total weight at a full floor. The single most direct path to a materially different result is Cloudflare reporting **sustained, non-one-off GAAP net income**, which would immediately lift both Profitability (via a positive Net Margin/ROIC) and FCF Quality (via a now-meaningful, presumably-high FCF/NI ratio) off their current floors — a large swing given their combined weight. Absent that, no amount of further Growth/Margin/Balance-Sheet strength can close a 22.3-point gap, since three of those four sub-scores are already at or near their ceiling.
- **Other Rule 9 events:** a guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause.
- Absent any of the above, future Telegram mentions of NET should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Watchlist Actions

- Created `watchlist/not-in-portfolio/NET/NET-2026-07-25.md` (first-ever entry for this ticker — nothing to supersede or mark stale).

---

## 8. Data Gaps Flagged (summary — none blocked scoring)

1. **`yfinance` was unreachable this entire session** (`curl_cffi` TLS reset/connection-reset-by-peer on every call, tested directly on NET across 3 retries) — same recurring Yahoo-side block pattern as every other 2026-07-24/2026-07-25 session (QCOM, EVO, COIN, HOOD). Fundamentals sourced from `stockanalysis.com` instead. Flagging again for `/healthcheck` — this is now a persistent, multi-day pattern rather than a one-off.
2. **IBKR's `get_price_snapshot` returned a stale price** ($262.32, actually Thursday 2026-07-23's close) rather than the true most recent close ($262.15, Friday 2026-07-24) — caught via cross-check against `get_price_history` and an independent `stockanalysis.com` fetch before it could propagate into any calculation. This is the **second consecutive session** (after HOOD, same day) where this exact staleness pattern was caught — flagging as a recurring, not isolated, `/healthcheck` item.
3. **FCF/Net Income hard-disqualifier interpretation for a negative-Net-Income company** (§3.1) — a genuine judgment call, flagged explicitly, shown not to change the outcome (§3.3).
4. **FCF Quality sub-score formula not designed for a positive-FCF/negative-NI combination** (§3.2) — mechanically floors at 0.0 regardless of how large FCF is relative to the loss; flagged as a caveat rather than silently presented as a clean "poor cash conversion" signal.

None of these gaps blocked scoring — every input used was ultimately obtained and cross-validated across independent sources, and the two genuine judgment calls (items 3–4) were shown not to affect the final FAIL outcome.

---

## Glossary

- **Anycast network** — A network routing technique where the same IP address is announced from many physical locations worldwide, and each user's request is automatically routed to the nearest/best-performing one — the underlying architecture behind Cloudflare's global edge network. *(New term — see full definition in [glossary.md](../framework/glossary.md).)*
- **CAGR (Compound Annual Growth Rate)** — The smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CDN (Content Delivery Network)** — A geographically distributed network of servers that caches and delivers web content from a location physically close to each end user. *(New term.)*
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every EDGAR filer (Cloudflare's is 0001477333).
- **D&A (Depreciation & Amortization)** — The non-cash expense spreading the cost of long-lived assets over time.
- **DNS (Domain Name System)** — The internet's address-lookup system that translates human-readable domain names into the numeric IP addresses computers use to route traffic. *(New term.)*
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **Effective tax rate** — The actual percentage of pretax income paid as tax in a period.
- **FCF (Free Cash Flow)** — Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; see §3.2 for this session's edge case (positive FCF, negative NI).
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score — none independently fired for NET this session (see §3.1 caveat).
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC sanity check.
- **Magic Transit** — Cloudflare's network-layer (L3/L4) DDoS-protection and traffic-routing product for a customer's entire IP address range — cited as Switching Costs Moat Signal evidence this session. *(New term.)*
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. NET scores 57.7.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies eligible for valuation scoring. (NET does not make this list, this session.)
- **ROIC (Return on Invested Capital)** — How efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure — the basis used throughout this session's sub-scores.
- **Workers (edge compute platform)** — Cloudflare's serverless application-execution platform that runs customer code directly on its global edge network rather than in a centralized data center — cited as Switching Costs Moat Signal evidence this session. *(New term.)*
- **XBRL (eXtensible Business Reporting Language)** — The SEC's structured, machine-readable data-tagging format for filed financial statements.
- **Zero Trust (network security model)** — A security architecture that verifies every user and device attempting to access a resource, rather than trusting anyone already "inside" a traditional network perimeter — Cloudflare's Zero Trust product suite, cited as Switching Costs Moat Signal evidence this session. *(New term.)*

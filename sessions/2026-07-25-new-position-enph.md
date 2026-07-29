# New Position Evaluation — ENPH (Enphase Energy, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-07-25
**10Y US Treasury yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (see Section 3) before the Rate Environment Gate would otherwise apply (same precedent as the 2026-07-25 COIN session, the 2026-07-24 QCOM session, and the 2026-07-19 SCHW session before it).
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — a `t.me/bolshegold` post (post #9832, ~16:02 UTC 2026-07-25) was a casual "earnings to watch next week" round-up mentioning the cashtag `$ENPH` alongside other names. ENPH has **no prior watchlist entry anywhere** under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). Per Rule 0, **no claim from the triggering post is used as a financial input anywhere below** — the post's text is not treated as verified data and is only the reason ENPH was looked at today; every number in this session was fetched fresh, independent of the post, from IBKR (live price), `stockanalysis.com`, and SEC XBRL. (The post's "earnings to watch" framing is independently corroborated — Enphase's Q2 2026 earnings call is confirmed scheduled for **Tuesday 2026-07-28, after market close** — but this was verified fresh this session, not taken from the post itself.)

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

| Source | Value | Detail |
|---|---|---|
| **IBKR `get_price_snapshot`** (contract_id 105368327, NASDAQ — "ENPHASE ENERGY INC") | $38.89, flagged `is_close: true` | **This figure was cross-checked and found stale by one trading day — not used.** See discrepancy note below. |
| **IBKR `get_price_history`** (same contract, 1-week daily bars, RTH only) | **$36.70** (2026-07-24 daily bar: open $38.93, high $38.93, low $36.58, close $36.70, volume 2,716,135) | Today (2026-07-25) is a **Saturday**, so this is the most recent genuine trade print available — Friday 2026-07-24's regular-session close. |
| **Cross-check discrepancy, investigated and resolved:** `get_price_snapshot`'s `last` field returned $38.89 flagged `is_close: true` — but the 1-week `get_price_history` pull (same contract_id, same session) shows **2026-07-23's** close was $38.89 and **2026-07-24's** close was $36.70. The snapshot tool was serving a **one-day-stale** "close" despite its own `is_close: true` flag. This was caught by the Rule 0 discipline of cross-validating against a second IBKR call rather than accepting a single tool response at face value — independently confirmed against `stockanalysis.com`'s overview page, which separately reported "$36.70, down 5.63% for the day" for 2026-07-24 (36.70 / 38.89 − 1 = −5.63%, an exact match). **$36.70 is used as the price of record throughout this session.** | | |
| 52-week range (IBKR `misc_statistics`) | low **$25.775** / high **$73.74** | 13-week and 26-week highs are both identical to the 52-week high ($73.74), meaning that high was set within the trailing 13 weeks — i.e. a sharp, recent drawdown. Current price ($36.70) is **~50.2% below** that recent high and **~42.4% above** the 52-week low. 52-weeks-ago open: $35.66. Shown here as context only, not itself a scoring input or basis for any conclusion below (Rule 0 / "never act on price movement alone"). |
| Dividend yield (IBKR) | 0.0% | No dividend. |
| Implied market cap (live price × 131.80M shares out, per `stockanalysis.com`) | ~$4.84B | Context only — consistent with `stockanalysis.com`'s own reported $4.84B market cap at its (slightly stale, $36.70-based) snapshot. |
| Analyst consensus (`stockanalysis.com`) | $48.28 PT, "Buy" average rating (31 analysts) | Context only, per Rule 0 Step 4 — not used as a valuation input; the session does not reach Phase 02 valuation work (see Section 3.3). |

**Live price used throughout this session: $36.70.**

---

## 2. Data Source Note

Enphase Energy, Inc. is a US SEC filer (**CIK 0001463101**, fiscal year = calendar year). Fundamentals for this session were sourced from two places, cross-validated against each other line-by-line wherever both were available:

- **`stockanalysis.com`** (`/stocks/ENPH/financials/`, `/financials/balance-sheet/`, `/financials/cash-flow-statement/`, `/financials/ratios/`, and the ticker overview page) — used for annual income-statement history (FY2021–FY2025), the FY2025/Q1-2026 balance sheet, and headline ratios.
- **SEC XBRL `companyconcept` API** (`data.sec.gov/api/xbrl/companyconcept/CIK0001463101/us-gaap/...`) — pulled directly to independently reconstruct trailing-twelve-month (TTM) Revenue, Operating Income (EBIT), Net Income, Income Tax Expense, Operating Cash Flow, and CapEx from the four most recently disclosed quarters (Q2 2025 → Q1 2026, the most recently filed 10-Q, period ended 2026-03-31), plus balance-sheet figures (cash, marketable securities, debt, equity) as of the same date.
- `yfinance` was attempted first and failed with the same TLS connection-reset error (`curl_cffi... Recv failure: Connection reset by peer`) seen in every recent session (2026-07-24 QCOM/EVO, 2026-07-25 COIN) — SEC XBRL + `stockanalysis.com` used as the established fallback.
- **Independent web search** (non-Telegram, non-trigger-post sources) — used for the Growth-modifier and Moat-signal qualitative evidence in Section 3.2, each cited individually at the point of use, and to confirm Enphase's Q2 2026 earnings date (2026-07-28, after this session — see Section 6).

**Every TTM figure reconstructed from SEC XBRL below was cross-checked against `stockanalysis.com`'s own independently-reported TTM total, and all four reconciled exactly**: Revenue $1,399,801K reconstructed vs. $1,400M reported; Operating Income $95,961K reconstructed vs. $95.96M reported; Net Income $134,997K reconstructed vs. $135M reported; Operating Cash Flow $190,997K reconstructed vs. $191M reported; CapEx $45,929K reconstructed vs. $45.93M reported. Balance-sheet figures as of 2026-03-31 also reconciled exactly: Total Debt $572,510K (SEC, = LongTermDebtNoncurrent $572,510K + LongTermDebtCurrent $0) vs. $572.51M (`stockanalysis.com`); Cash $497,546K vs. $497.55M; Marketable Securities (current) $433,095K vs. $433.1M "short-term investments"; Stockholders' Equity $1,102,352K vs. $1,102M — high confidence in the figures below.

No required Phase 01 input was invented, estimated, or inferred from the triggering post.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | ENPH data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF (OCF − CapEx) by year: FY2023 **$586.38M**, FY2024 **$480.09M**, FY2025 **$95.9M**, TTM (Q2 2025→Q1 2026) **$145.068M** (reconstructed: OCF $190,997K − CapEx $45,929K). Positive every year shown and the current TTM. | **PASS — does not fire.** |
| **Net debt/EBITDA over threshold (2.5× standard, or 4×/6× under the Upgrade 5 asset-light override)** | As of the most recent balance sheet (2026-03-31): Total debt **$572.510M**; Cash **$497.546M** + marketable securities (current) **$433.095M** = **$930.641M**. **Net debt = 572.510 − 930.641 = −$358.131M** (a **net cash** position). Net debt is negative, so Net Debt/EBITDA is negative under any denominator — the debt-gate ratio is not a constraint (Enphase is a hardware manufacturer, not an asset-light financial business, so the Upgrade 5 override doesn't apply anyway — moot here since net cash clears the standard 2.5× threshold regardless). | **PASS — well under threshold (net cash).** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FCF/NI by year: FY2023 **133.63%** ($586.38M/$438.94M), FY2024 **467.6%** ($480.09M/$102.66M — a large non-cash-item-driven ratio, not investigated further as it's on the high side, not the low side this check targets), FY2025 **55.71%** ($95.9M/$172.13M — **below 70%, but only 1 year**), TTM **107.46%** ($145.068M/$134.997M). Only FY2025 falls below the 70% line; FY2024 and the current TTM are both well above it — the "2+ consecutive years" condition is not met. | **PASS — does not fire (only 1 year below threshold, not 2 consecutive).** |

No hard disqualifier fires. ENPH's outcome is decided entirely by the weighted score below.

### 3.2 Sub-scores (all six, per the weighted formula)

**TTM reconstruction (Q2 2025 → Q1 2026, the four most recent quarters through the most recently filed 10-Q, period ended 2026-03-31), sourced from SEC XBRL `companyconcept` and cross-checked against `stockanalysis.com`'s own reported TTM totals:**

| Line item ($K) | Q2 2025 (end 2025-06-30) | Q3 2025 (end 2025-09-30) | Q4 2025 (derived: FY2025 annual − 9mo) | Q1 2026 (end 2026-03-31) | **TTM total** | Cross-check vs. `stockanalysis.com` TTM |
|---|---|---|---|---|---|---|
| Revenue | 363,153 | 410,427 | 343,321 | 282,900 | **1,399,801** | 1,400,000 ✓ match |
| Operating Income (EBIT) | 37,007 | 66,159 | 22,438 | (29,643) | **95,961** | 95,960 ✓ match |
| Net Income | 37,052 | 66,638 | 38,713 | (7,406) | **134,997** | 135,000 ✓ match |
| Income Tax Expense (Benefit) | 5,153 | 10,381 | (16) | (6,454) | **9,064** | not separately reported; internally consistent (below) |
| Operating Cash Flow | 26,629 | 13,918 | 47,579 | 102,871 | **190,997** | 191,000 ✓ match |
| CapEx (PP&E purchases) | 8,259 | 8,032 | 9,740 | 19,898 | **45,929** | 45,930 ✓ match |

(FY2025 Q4 figures derived as FY2025-annual-10-K total minus the disclosed 9-month-YTD figure through Q3 2025, per line item; quarterly OCF/CapEx figures derived the same way from cumulative YTD 10-Q disclosures. Every input is a directly-filed SEC XBRL figure. **Internal consistency check:** TTM Net Income ($134,997K) + TTM Income Tax Expense ($9,064K) = TTM Pretax Income **$144,061K**; effective tax rate = 9,064/144,061 = **6.291%**.)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = 134,997/1,399,801 = **9.644%** → NetMargin_Component = clamp((9.644/30)×100) = **32.15**. NOPAT = TTM EBIT × (1 − effective tax rate) = 95,961 × (1−0.062907) = **$89,924K**. Invested Capital (2026-03-31) = Total Debt ($572,510K) + Equity ($1,102,352K) − liquid assets ($930,641K, cash + marketable securities netted above) = **$744,221K**. ROIC = 89,924/744,221 = **12.081%** → ROIC_Component = clamp((12.081/30)×100) = **40.27**. Profitability_Score = (32.15+40.27)/2 = **36.21** (no FCF-positivity cap — FCF-positive every year FY2023–FY2025 and the TTM, see 3.1). | **36.21** |
| **Margins (15%)** | Gross Margin (TTM) = **44.23%** (per `stockanalysis.com`; TTM Gross Profit $619.16M ÷ TTM Revenue $1,400M = 44.23%, internally consistent with the SEC-reconstructed TTM revenue above). GrossMargin_Score = clamp((44.23/80)×100) = **55.29**. **No +10 trend bonus** — the bonus applies only when gross margin is below the 40% static threshold and structurally expanding; ENPH's TTM margin (44.23%) is already above 40%, so the bonus condition doesn't apply regardless of trend direction. (For transparency: the 3yr trend is actually **declining**, not expanding — FY2023 46.20% → FY2024 47.29% (peak) → FY2025 46.64% → TTM 44.23% — so no bonus would have applied on trend grounds either.) | **55.29** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $2,330.853M → FY2025 $1,472.985M, both directly filed SEC XBRL annual figures) = (1,472.985/2,330.853)^(1/3) − 1 = **−14.19%** → base = clamp((−14.19/25)×100) = clamp(−56.75, 0, 100) = **0.0** (floored — cannot go negative). **Structural-deceleration modifier considered, but immaterial to the outcome given the floor:** this is a well-documented, multi-year, **structural** (not merely cyclical) decline, not a single bad quarter — driven by (1) California's **NEM 3.0** net-billing tariff (effective April 2023), which cut compensation for exported solar power ~75–80% vs. the prior NEM 2.0 rules and sharply reduced the economics of solar-only rooftop systems [Utility Dive, "Enphase Energy revenue drops... California net metering rules"], (2) the federal **Section 25D** residential clean-energy tax credit expiring at the end of 2025, which removed a further subsidy for new US residential systems from 2026 onward and is cited as a direct driver of Enphase's weak Q1 2026 US sell-through (down 48% quarter-over-quarter, down 18% year-over-year) [PV-Tech, "Lower residential demand after 25D tax credit ends impacts Enphase's Q1 2026 revenue"], and (3) broader US residential solar financing headwinds (higher rates, slower third-party-ownership adoption) [gurufocus, "Enphase Energy (ENPH) Reports Q1 Revenue Decline Amid Weak Solar Demand"]. A **−10 structural-deceleration modifier would apply** under the framework's own rule (documented, structural, not cyclical) — but since the base score is already floored at 0.0, it changes nothing (0 − 10, clamped to 0). Shown for transparency, per "show every calculation," even though it doesn't move the result. *(Countervailing note, also transparently flagged: NEM 3.0 has simultaneously boosted attach rates for paired battery storage — Enphase's own battery revenue has grown even as solar-only revenue fell — a real offsetting dynamic, but not enough to prevent the multi-year consolidated revenue decline reflected in the CAGR above.)* | **0.00** |
| **Balance Sheet (15%)** | Net Debt (as of 2026-03-31) = **−$358.131M** (net cash — see 3.1). BalanceSheet_Score = clamp(100×(1 − NetDebt/EBITDA/4)) — with Net Debt negative, this evaluates to >100 and clamps to **100.0** regardless of denominator. | **100.00** |
| **Moat Signal (15%)** | See evidence table below — **2 of 5 signals** cleared the cited-evidence bar. (2/5)×100 | **40.00** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 145,068/134,997 = **107.46%** → clamp(((1.0746−0.40)/0.60)×100) = clamp(112.4) = **100.0**. | **100.00** |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | Wood Mackenzie's distributed-solar competitive-landscape report (March 2025) found Enphase's US market share **fell from 55% to 47% in 2024** — a documented, quantified year-over-year **erosion**, not stability or growth, even though combined Enphase+SolarEdge share has stayed above 80% (a duopoly-level industry structure, but not evidence in Enphase's own favor specifically). | **FALSE** |
| Brand premium | Documented price premium vs. a named competitor: Enphase battery-storage systems run **$1,500–$1,700 per kWh installed vs. Tesla Powerwall's $1,222–$1,243 per kWh** [solartechonline.com, "SolarEdge Vs Enphase 2025" / "Enphase Battery Cost 2025"], attributed by that source to modular design, warranty coverage, and reliability reputation — meeting the framework's "premium vs. competitors" evidence bar. **Caveat flagged:** this doesn't demonstrate the framework's *other* listed evidence type (price increases sustained *without* volume loss) — Enphase's own volumes have fallen sharply industry-wide over this same period, though for macro/policy reasons (NEM 3.0, tax-credit expiry) rather than demonstrated price-elasticity from Enphase's own pricing decisions. | **TRUE (with caveat)** |
| Network effect | No documented two-sided marketplace/user-growth-driven-value mechanism found. Enphase's 24,000+ certified-installer network is a distribution/channel advantage, not a two-sided network effect under the framework's specific bar (which requires a marketplace dynamic where each side's participation increases value for the other side, e.g. a payments network or ride-share marketplace) — installers are a sales channel, not participants creating mutual value the way a marketplace's two sides do. | **FALSE** |
| Switching costs | **Documented mechanism.** Enphase's Enlighten cloud-monitoring platform is proprietary and **only interoperates with Enphase's own microinverter/IQ Battery hardware** — a competing inverter from another manufacturer "won't connect to the platform" [solartechonline.com / apps.list.solar, "Enphase Enlighten Review"]. The bundled hardware-plus-software integration (microinverters + IQ Battery storage + Enlighten monitoring, tied together at the individual-panel level across an already-installed system) creates genuine physical/software replacement friction for a homeowner considering a competing vendor — a real, cited mechanism, distinct from a generic "switching is annoying" claim. | **TRUE** |
| Scale cost advantage | No **cost-per-unit** data (the framework's specific evidentiary bar: cost-per-unit data showing a gap vs. smaller competitors) was found quantifying an Enphase per-unit manufacturing-cost advantage over a smaller rival. If anything, the sourced coverage points the other way — margin/competitive pressure from lower-cost entrants (Chinese-manufactured components, Tesla's more centralized/cheaper string-inverter-plus-Powerwall architecture) rather than a documented scale advantage in Enphase's favor. | **FALSE** |

### 3.3 Final weighted Quality Score

```
Quality Score = (36.21 × 0.25) + (55.29 × 0.15) + (0.00 × 0.20) + (100.00 × 0.15) + (40.00 × 0.15) + (100.00 × 0.10)
              = 9.0525 + 8.2935 + 0.000 + 15.000 + 6.000 + 10.000
              = 48.346 → 48.3 (rounded to nearest 0.1)
```

**48.3 < 80.0 — fails the gate**, by **31.7 points** — a decisive miss, more decisive than the 2026-07-24 QCOM session's 19.7-point gap and much more decisive than the 2026-07-25 COIN session's 3.7-point near-miss. Two sub-scores are strong (Balance Sheet 100.0 — a genuine net-cash position; FCF Quality 100.0 — TTM FCF/NI 107.46%), but **Growth (0.00)** — a severe, structurally-documented 3-year revenue decline (−14.19% CAGR) — and a middling **Profitability (36.21)** and **Margins (55.29)** pull the weighted score far below the bar, only partially offset by a below-average **Moat (40.00)**.

**Sensitivity check (per the one flagged discretionary call — Moat — holding every other sub-score fixed):**

| Moat reading | Signals credited TRUE | Moat_Score | Quality Score | Gate result |
|---|---|---|---|---|
| Most conservative | 0 of 5 (drop Brand premium — caveat above judged disqualifying) | 0.0 | 42.3 | FAIL |
| **Primary reading (this session)** | **2 of 5 (Brand premium, Switching costs)** | **40.0** | **48.3** | **FAIL** |
| Generous | 3 of 5 (also credit Market share despite the documented 55%→47% erosion) | 60.0 | 51.3 | FAIL |
| Maximally generous | 5 of 5 (also credit Network effect and Scale cost advantage without the framework's required evidence types) | 100.0 | 57.3 | **FAIL — still 22.7pt short** |

**The gate outcome is robust to every possible reading of the one discretionary sub-score** — even crediting all 5 Moat signals (including two the evidence gathered this session does not actually support) leaves the Quality Score at 57.3, more than 22 points short of the 80.0 bar. The dominant, non-discretionary driver of this result is **Growth (0.00)**, a directly-computed, SEC-XBRL-sourced 3-year revenue CAGR of −14.19% that floors the sub-score regardless of any qualitative modifier.

### Result: **Phase 01 FAIL**

Per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md): a company scoring below 80.0 does not proceed to Phase 02. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**FAIL — does not clear the Quality Score gate**, at **48.3 vs. the strict 80.0+ bar**, missing by 31.7 points — a decisive, not a close, miss. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup were computed — that work is reserved for names that clear this framework's quality bar first.

Enphase presents a case this framework's Quality Score is specifically built to catch: a genuinely strong balance sheet (net cash position, Balance Sheet sub-score 100.0) and excellent trailing cash conversion (FCF/NI 107.46%, FCF Quality sub-score 100.0) sitting on top of a business whose core demand driver — new US residential solar/storage installations — has been hit by a well-documented, multi-year confluence of adverse policy changes (California's NEM 3.0 net-billing tariff cutting solar-export economics since April 2023, the federal Section 25D residential tax credit expiring at the end of 2025) and macro headwinds (higher financing rates curbing loan-driven installations). The result is a **3-year revenue CAGR of −14.19%**, flooring the Growth sub-score at 0.0 regardless of any qualitative offset, and a middling Profitability score (36.21, TTM Net Margin 9.64% / ROIC 12.08%) that reflects genuine margin and volume compression rather than a data-window artifact. The Moat picture is also below-average by this framework's measure: only a documented price premium vs. Tesla Powerwall and a genuine hardware/software switching-cost mechanism (the proprietary Enlighten platform) clear the evidentiary bar, while Enphase's own US market share has been independently documented (Wood Mackenzie) as **eroding** — 55% → 47% in 2024 — the opposite of a stable-or-growing moat signal. The triggering post was a passing cashtag mention in a generic "earnings to watch" round-up (Enphase's Q2 2026 results are confirmed scheduled for 2026-07-28, three days after this session), not a claimed fundamental event, and per Rule 9's non-negotiables, ENPH's large drawdown from its own 52-week high (~50.2%) is not itself treated as a buying opportunity without the underlying quality bar being cleared first — which it is not, decisively, on the numbers pulled fresh this session.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mandatory Rule 9 re-check:** Enphase's Q2 2026 earnings, confirmed scheduled **Tuesday 2026-07-28** (3 days after this session, after market close) — the next quarter of data will roll the TTM window forward by one quarter (dropping Q2 2025, adding Q2 2026), and will be the first full quarter reflecting the Section 25D tax-credit expiration's effect on US residential demand.
- **Mechanical trigger:** Growth (0.00, floored) is the dominant and non-discretionary gap to the 80.0 gate — a genuine, multi-quarter reacceleration in revenue (most plausibly from continued battery-attachment-rate growth under NEM 3.0 offsetting solar-only declines, from commercial/international diversification, or from a policy reversal) would be the most direct path to a materially different result; Moat (40.0, the one discretionary sub-score) is a secondary lever but — per the sensitivity table in 3.3 — cannot alone close a gap this large.
- **Other Rule 9 events:** a guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause (note: ENPH's ~50.2% decline from its 52-week high tracks the documented multi-year US residential solar demand downturn and is not, on the evidence gathered this session, an unexplained move).
- Absent any of the above, future Telegram mentions of ENPH should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **10-K (Annual Report)** — The annual financial-disclosure report a US public company must file with the SEC, containing full audited financial statements, MD&A, and risk factors.
- **10-Q (Quarterly Report)** — The quarterly financial-disclosure report filed between annual 10-Ks — used here to reconstruct trailing-twelve-month (TTM) figures through the most recently filed quarter.
- **CAGR (Compound Annual Growth Rate)** — The smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx (Capital Expenditure)** — Cash spent acquiring or maintaining long-lived physical assets (property, plant & equipment) — subtracted from Operating Cash Flow to arrive at Free Cash Flow.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every EDGAR filer (Enphase's is 0001463101) — used to construct this session's SEC XBRL/filing data-pull paths.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **Effective tax rate** — The actual percentage of pretax income paid as tax in a period — used here to convert TTM EBIT into NOPAT for the ROIC calculation.
- **FCF (Free Cash Flow)** — Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score — none fired for ENPH this session.
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation.
- **Microinverter** — A small power-electronics device mounted behind an individual solar panel that converts that one panel's DC output to grid-usable AC power on-site, rather than a single centralized "string inverter" for the whole array — Enphase's core product line.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **NEM 3.0 (net billing tariff)** — California's third-generation Net Energy Metering policy (effective April 2023) that cut compensation for exported residential solar power by roughly 75–80% vs. the prior rules, reducing solar-only system economics while boosting the relative appeal of paired battery storage.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. ENPH scores 48.3.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies eligible for valuation scoring. (ENPH does not make this list, this session.)
- **ROIC (Return on Invested Capital)** — How efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **Section 25D (Residential Clean Energy Credit)** — A US federal tax credit for residential solar/battery installations that expired at the end of 2025, removing a subsidy for new US residential systems from 2026 onward.
- **TAM (Total Addressable Market)** — The total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not fetched this session, since Phase 01 failed first).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure — the basis used throughout this session's sub-scores.
- **XBRL (eXtensible Business Reporting Language)** — The SEC's structured, machine-readable data-tagging format for filed financial statements — the source of the independently-reconstructed TTM figures in Section 3.2, pulled via the SEC's `companyconcept` API.

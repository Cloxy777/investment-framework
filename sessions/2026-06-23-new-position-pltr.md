# NEW POSITION — PLTR (Palantir Technologies Inc.)

**Task type:** NEW POSITION
**Date:** 2026-06-23
**Current 10Y US Treasury yield:** 4.46% (FRED `DGS10`, most recent available print: 2026-06-18)
**Rate Regime Modifier in effect:** +5 (3.5–5% bracket) — captured for the record only; **not applied**, since Phase 01 failed (see §3)
**Current portfolio weight:** 0% (not held)
**Sector:** Technology — AI & Data Analytics Software

## Trigger

Telegram post on [t.me/FinnInvestChannel](https://t.me/FinnInvestChannel) (post #2818, ~15:59 UTC 2026-06-23): "Palantir is at its 52-week low with a PEG ratio of 1.71, though expensive by other metrics. Key developments include Palantir Foundry becoming the foundation for Zeta Data Cloud, and Palantir receiving 'a key role in the data layer for the U.S. military.'" This names Palantir Technologies (NASDAQ: PLTR), which has **zero prior watchlist entries** — per `telegram-scan.md` step 4, any newly-named company with no existing entry is evaluated via `/new-position` regardless of how thin the triggering mention is.

**The Telegram post text is used only as a trigger to select this ticker for evaluation.** None of its claims (PEG ratio, the Zeta Data Cloud relationship, the "data layer" role for the U.S. military) are used anywhere below as a financial input. All data in this session was independently sourced from yfinance and IBKR (per Rule 0 and the operating brief's "never invent or estimate financial data" rule). The post's "52-week low" claim is independently corroborated below (§1) by live IBKR data — but corroborating one claim doesn't change how the rest of the post is treated; the Foundry/Zeta/military claims were not independently verified via a primary source in this session, since Phase 01 fails decisively on trailing financials regardless of any forward-looking narrative (the same treatment the 2026-06-22 MU session gave a real, confirmed deal: it doesn't retroactively repair trailing fundamentals).

## Ticker identity

- **NASDAQ: PLTR** — Palantir Technologies Inc., Class A. IBKR contract confirmed via `search_contracts` (conid 444857009, NASDAQ, USD).
- Went public via a **direct listing** on the NYSE on 30 September 2020 (confirmed via yfinance's own earliest on-record earnings date, 2020-11-12 — six weeks after a late-September IPO is consistent with a Q3 2020 direct listing); primary listing moved to Nasdaq in November 2024. As of this session, PLTR has under 6 years of public trading/financial history — relevant to the Turnaround Sub-Gate check in §3.
- No dual-listing or DLC structure applies.

## §1 — Live Price (Rule 0)

- **IBKR `get_price_snapshot`** (live): **$118.89** (bid $118.88 / ask $118.91), timestamped 2026-06-23 ~16:44 UTC, `is_close: false` (live quote).
- Cross-check: yfinance `info['currentPrice']` = $118.91 — consistent.
- IBKR's cached `misc_statistics` 52-week-low field still shows $119.20 (13/26/52-week low all printed identically, i.e. the 52-week low was set at that level and the field hasn't refreshed intraday yet) — **today's live print of $118.89 is below that cached figure**, meaning PLTR has set a new intraday 52-week low today. This independently corroborates the Telegram post's "52-week low" claim, via live data, not the post's text.
- YTD change (IBKR): **−33.11%**.
- **Live price used throughout this session: $118.89** (IBKR), per Rule 0.

## §2 — Data Gathered

### Annual financials (FY2022–FY2025, USD millions; source: yfinance `t.financials`)

| Metric | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Total Revenue | 1,905.9 | 2,225.0 | 2,865.5 | 4,475.4 |
| Gross Profit | 1,497.3 | 1,793.9 | 2,299.5 | 3,686.3 |
| Cost Of Revenue | 408.5 | 431.1 | 566.0 | 789.2 |
| Net Income | (373.7) | 209.8 | 462.2 | 1,625.0 |
| EBIT | (161.2) | 120.0 | 310.4 | 1,414.0 |
| Pretax Income | (361.0) | 237.1 | 489.2 | 1,657.4 |
| Tax Provision | 10.1 | 19.7 | 21.3 | 22.7 |

### TTM reconstruction (last 4 reported quarters: Q2'25–Q1'26, via `t.quarterly_financials` / `t.quarterly_cashflow`)

| Metric | TTM |
|---|---|
| Total Revenue | 5,224.2 |
| Gross Profit | 4,392.2 |
| Cost Of Revenue | 832.0 |
| Net Income | 2,281.5 |
| EBIT | 1,992.0 |
| D&A | 26.3 |
| EBITDA | 2,018.3 |
| Pretax Income | 2,322.7 |
| Tax Provision | 29.3 |
| Operating Cash Flow | 2,723.4 |
| CapEx | (35.1) |
| Free Cash Flow | 2,688.3 |
| Stock-Based Compensation | 730.3 |

### Annual FCF history (USD millions, via `t.cashflow`)

| | FY2022 | FY2023 | FY2024 | FY2025 | TTM |
|---|---|---|---|---|---|
| Free Cash Flow | 183.7 | 697.1 | 1,141.2 | 2,100.6 | 2,688.3 |
| FCF/NI conversion | n/m (NI negative) | 332.3% | 246.9% | 129.3% | 117.8% |

FCF has been positive in **every fiscal year on record** (FY2022 onward) and TTM — well beyond the 3-consecutive-year minimum. FCF/NI conversion has stayed comfortably above the 70% threshold throughout, including TTM — the elevated net margin discussed below is genuinely converting to cash, not an accounting-only artifact (no Wirecard/Valeant-style red flag).

### Balance sheet (most recent quarter, 2026-03-31; source: `t.quarterly_balance_sheet`)

| Metric | Value |
|---|---|
| Total Debt | $212.0M |
| Cash & Short-Term Investments | $8,026.4M |
| Net Debt (cash position) | **$(7,814.4)M** (net cash) |
| Stockholders' Equity | $8,449.7M |
| Total Invested Capital (Debt + Equity) | $8,661.6M |
| Shares Outstanding | 2,397.1M |

Share count has risen every period on record (2,099.1M FY2022 → 2,200.1M FY2023 → 2,338.8M FY2024 → 2,391.2M FY2025 → 2,397.1M Q1 2026, +14.2% cumulative) despite a "repurchase of capital stock" cash-outflow line each period — consistent with heavy stock-based compensation (TTM SBC $730.3M, ~14% of TTM revenue) where net-settlement tax withholding on RSU vesting shows up as a buyback-flavored cash outflow even as gross RSU issuance keeps growing the share count. A real, ongoing dilution headwind, flagged for transparency though not part of the 8-criterion gate below.

### Computed ratios (TTM, at live price $118.89)

| Metric | Value | Basis |
|---|---|---|
| Gross margin | **84.07%** | 4,392.2 / 5,224.2 |
| Net margin (as-reported) | **43.67%** | 2,281.5 / 5,224.2 |
| Effective tax rate (TTM) | **1.26%** | Tax Provision 29.3 / Pretax Income 2,322.7 — vs 21% US statutory. See §6 note 2 on the deferred tax valuation allowance release driving this. |
| Net margin (normalized at 21% statutory tax) | **35.12%** | (2,322.7 × 0.79) / 5,224.2 — shown to confirm the PASS conclusion below holds even on a conservative tax basis |
| Market Cap | $284,995.1M | 2,397.1M shares × $118.89 |
| Enterprise Value | $277,180.7M | Market Cap + Debt − Cash & ST Investments |
| ROIC (actual tax, period-end invested capital) | **22.71%** | NOPAT (1,966.8) / Invested Capital (8,661.6) |
| ROIC (actual tax, average invested capital) | **26.88%** | NOPAT (1,966.8) / avg IC over trailing 4 quarters (7,317.7) |
| ROIC (normalized 21% tax, period-end IC) | **18.17%** | NOPAT_norm (1,573.7) / 8,661.6 |
| ROIC (normalized 21% tax, avg IC) | **21.50%** | NOPAT_norm (1,573.7) / 7,317.7 |
| Revenue 3yr CAGR | **32.91%** | (TTM 5,224.2 / FY2023 2,225.0)^(1/3) − 1 |
| Net Debt/EBITDA | **−3.87×** | (7,814.4) / 2,018.3 — net cash position |
| FCF Yield (FCF/Market Cap) | **0.943%** | 2,688.3 / 284,995.1 |
| FCF Yield (FCF/EV) | **0.970%** | 2,688.3 / 277,180.7 |
| EV/EBIT | **139.15×** | 277,180.7 / 1,992.0 |

ROIC and net margin both clear the 15%/12% thresholds under **every** basis tested (as-reported or normalized at the 21% statutory rate, period-end or average invested capital) — the tax distortion noted above doesn't change the gate's PASS conclusion on those two criteria.

### 5-year historical PE reconstruction

Via `t.get_earnings_dates(limit=40)` + rolling 4-quarter TTM EPS + `t.history()` daily price series, all 20 trailing quarters since the first qualifying TTM-EPS quarter (2021-08-12) — the full 5-year window is available since PLTR's September 2020 listing:

- 5yr average PE: **151.3×**
- 5yr low PE: **60.7×** (2022-05-09)
- 5yr high PE: **326.9×** (2025-08-04)

PLTR has never traded anywhere near a conventional "cheap" multiple at any point in its public history — today's EV/EBIT of ~139× sits toward the lower end of its own historical range, but still nowhere close to this framework's <20× threshold.

### Forward PE — "0y vs +1y trap" correction

- Raw `info['forwardPE']` = 57.11× — confirmed via `t.eps_trend` to use the **+1y** row (FY2027 EPS estimate $2.08207), not the nearer **0y** row (FY2026, the current fiscal year, $1.47251).
- Corrected: **Forward PE = $118.89 / $1.47251 = 80.74×**.

### Rate Environment Gate inputs (captured for the record only — not applied; see §4)

- Earnings Yield = 1 / Forward PE (corrected) = 1 / 80.74 = **1.238%**
- Spread vs 10Y (4.46%) = **−3.22pp** (well below the +1.5% threshold — would trigger Step 1's +5 additive flag if Phase 02 scoring were reached)
- Rate Regime Modifier (10Y in 3.5–5% bracket): **+5**

## §3 — Phase 01 Quality Gate

Using valuation-scoring.md's Quantitative Pre-Screen Filters (the same 8-criterion set applied in the 2026-06-22 MU session):

| Criterion | Threshold | PLTR actual | Result |
|---|---|---|---|
| Gross margin | >40% | 84.07% | **PASS** |
| Net margin | >12% (strategy.md: >15%) | 43.67% as-reported / 35.12% normalized | **PASS** (both bases, both thresholds) |
| ROIC | >15% | 22.71–26.88% as-reported / 18.17–21.50% normalized (basis-dependent) | **PASS** (every basis tested) |
| Revenue growth (3yr CAGR) | >8% (operating-calendar: >10%) | 32.91% | **PASS** |
| FCF positive, 3 consecutive years | required | Positive every fiscal year on record (FY2022–FY2025) + TTM | **PASS** |
| Net debt/EBITDA | <2.5× | −3.87× (net cash) | **PASS** |
| FCF Yield | >4% | 0.94% (Mkt Cap) / 0.97% (EV) | **FAIL — decisive** |
| EV/EBIT | <20× | 139.15× | **FAIL — decisive** |

**Result: 6 of 8 criteria PASS, 2 of 8 FAIL** (FCF yield, EV/EBIT — both price-denominated cheapness filters, both failing by roughly 4–7×). **Phase 01 Quality Gate: FAIL.**

Per operating-brief.md, a Phase 01 FAIL means **STOP — do not proceed to Phase 02 valuation scoring.**

### Turnaround Sub-Gate (Hybrid Upgrade 4) evaluation

PLTR fails exactly 2 of 8 criteria, which falls within the Turnaround Sub-Gate's "2–4 failing criteria" eligibility window — numerically eligible to check. The gate requires **all 5** of the following:

| Condition | Requirement | PLTR | Result |
|---|---|---|---|
| Historical ROIC | >15% for ≥5 of past 10 years | PLTR has under 6 years of public trading/financial history (direct listing 30 Sept 2020) — fewer years exist in total than the 10-year lookback window itself, so "5 of past 10 years" can never be satisfied regardless of how strong recent ROIC is. Even within the shorter history available, FY2022 was a loss year (ROIC negative). | **NOT MET — structurally, decisively** |
| Insider buying | CEO/CFO >$500K combined in trailing 6 months, Form 4-verified | Not evaluated — moot | **Not evaluated (moot)** |
| Independent FV estimate | ≥40% margin of safety | Not computed — moot | **Not evaluated (moot)** |
| Net Debt/EBITDA | <3× | −3.87× (net cash) | MET |
| Identifiable core moat | required | Plausible (Foundry/Gotham platform stickiness, government-contract switching costs) but not formally scored — moot | **Not evaluated (moot)** |

**Turnaround Sub-Gate: CLOSED.** All 5 conditions are mandatory — failing any one closes the path, and the historical-ROIC lookback condition fails for a structural reason (insufficient public history) that no amount of current business quality can overcome. Conditions 2, 3, and 5 were not separately evaluated since the gate is already closed by condition 1 alone. No 2–3% Turnaround position is supported.

## §4 — Rate Environment Gate

**NOT RUN.** Phase 01 failed; per operating-brief.md the Rate Environment Gate is a pre-check specifically for Phase 02 scoring and is not executed when Phase 01 has already failed. The earnings-yield/spread/regime-modifier figures in §2 are shown for-the-record only, exactly as computed, and were not applied to any score.

## §5 — Phase 02 Valuation Score

**NOT RUN** — Phase 01 Quality Gate failure stops the process per operating-brief.md. No FCF_Score, EV/EBIT_Score, FwdPE_Score, PEG_Score, Rate Regime Modifier, or Upside/Downside Modifier was computed or combined into a final score.

- **Hybrid Upgrade 1 (Owner Earnings):** Not triggered — PLTR is not one of the named moat-reinvestor names (MSFT/GOOGL/META/AMZN) this upgrade is required for, and Phase 02 was not reached regardless.
- **Hybrid Upgrade 3 (PEG, Fast Growers):** Even if Phase 02 had been reached, PLTR's GAAP EPS growth is heavily distorted by the FY2025 deferred tax valuation allowance release (TTM effective tax rate of just 1.26% vs 21% statutory) — the same earnings-quality disqualifier the DUOL precedent in valuation-scoring.md flags for "clean earnings base" eligibility. The Telegram post's cited PEG of 1.71 (which happens to match yfinance's own `pegRatio` field) was never used as an input here regardless, since Phase 02 isn't reached.

## §6 — Qualitative Notes

1. **What is the triggering event, and is it confirmed?** The post makes four claims: (a) PLTR at a 52-week low — independently confirmed true via live IBKR data (§1); (b) a PEG ratio of 1.71 — happens to match yfinance's own cached `pegRatio` field, but not independently verified as a financial input and not used in any calculation, since Phase 02 was never reached; (c) Palantir Foundry becoming the foundation for "Zeta Data Cloud," and (d) a "key role in the data layer" for the U.S. military — both forward-looking strategic/contract claims, not independently corroborated via a primary source in this session. This is decision-irrelevant: Phase 01 already fails decisively on trailing financials regardless of any forward narrative, the same treatment the 2026-06-22 MU session gave a real, independently-confirmed Micron–Anthropic deal — a real development doesn't retroactively repair trailing fundamentals or a price-denominated cheapness ratio.
2. **Why is net margin/ROIC so high relative to PLTR's growth-stage profile?** TTM effective tax rate of only 1.26% (vs 21% US statutory) is consistent with a **deferred tax valuation allowance release** — a one-off GAAP benefit common when a recently-unprofitable tech company turns durably profitable and recognizes previously-written-down deferred tax assets. This inflates reported net income/EPS in the recognition period; it is not a sign of a permanently low tax burden. Both as-reported and normalized-at-21%-statutory-tax bases were computed above for net margin and ROIC — the PASS conclusion holds either way, so this distortion doesn't change the Phase 01 outcome, but it does mean reported net income/EPS overstate PLTR's recurring run-rate, and it disqualifies PLTR from a "clean earnings base" for any future PEG-based scoring.
3. **Is the high margin actually converting to cash?** Yes — FCF/NI conversion has been ≥117.8% every year since FY2023 (TTM 117.8%), comfortably above the 70% threshold despite the tax-driven net income distortion. No earnings-quality red flag of the Valeant/Wirecard kind.
4. **Is this a turnaround candidate?** Numerically eligible (only 2 of 8 criteria fail) but the Turnaround Sub-Gate closes decisively and structurally — Palantir's under-6-year public history can never satisfy the mandatory 10-year/5-year historical-ROIC lookback, independent of how strong its current business quality is.
5. **How extreme are the two failing criteria?** FCF yield (0.94–0.97%) is roughly a quarter of the >4% threshold; EV/EBIT (139.15×) is nearly 7× the <20× threshold. The 5-year historical-PE reconstruction (§2) shows this isn't a temporary mispricing — PLTR has never traded near conventional "cheap" multiples at any point in its public life; today's level is merely toward the lower end of its own historically extreme range.
6. **Could a price decline alone close the gap?** Mechanically, FCF yield would need the market cap to fall to ~$67.2B (FCF/0.04) and EV/EBIT would need EV to fall to ~$39.8B (EBIT×20) — both roughly an 75–86% decline from today's levels, holding trailing FCF/EBIT fixed. A more realistic path to closing the gap is continued EBIT/FCF growth at the company's current pace while price stays flat, rather than a crash — see §8.

## §7 — Recommendation

**PASS — Phase 01 Quality Gate FAIL. Do not enter.**

Palantir passes 6 of 8 quality-gate criteria comfortably — gross margin, net margin (on both an as-reported and tax-normalized basis), ROIC (under every basis tested), revenue growth, FCF history, and balance-sheet strength (net cash) are all unambiguous PASSes. It fails decisively on both of the framework's price-denominated cheapness filters: FCF yield (~0.94–0.97% vs >4% required) and EV/EBIT (~139× vs <20× required). The Turnaround Sub-Gate, while numerically eligible given only 2 failing criteria, is closed because Palantir's under-6-year public trading history structurally cannot satisfy the mandatory "ROIC >15% in ≥5 of the past 10 years" condition — no amount of current business quality can fix that. No Phase 02 score was computed; no order setup applies. A `not-in-portfolio` watchlist entry is created marking this as "Phase 01 FAIL / not scored," per `watchlist/README.md` convention.

## §8 — Next Review Trigger

- **PLTR's next quarterly earnings release: 2026-08-03** (yfinance `t.calendar`) — mandatory Rule 9 re-check regardless of outcome.
- A material, sustained re-rating of the two failing criteria — given trailing FCF/EBIT are fixed at recent levels, closing the gap through price alone would require a ~75–86% decline (see §6); more plausibly, continued EBIT/FCF compounding at PLTR's current growth rate while price stays flat-to-down would close the gap over several years without requiring a crash. Neither is a near-term catalyst; the next mandatory checkpoint is the earnings-driven Rule 9 review above.
- Any primary-sourced, financially-quantified confirmation of the Zeta Data Cloud or U.S. military "data layer" claims (e.g. disclosed contract value or guidance impact) — per the MU-deal precedent, this would be assessed at that time but could not on its own override the price-denominated Phase 01 failures unless it also moved trailing FCF/EBIT materially.

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets (factories, equipment, data centers). |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **Deferred tax valuation allowance release** | A one-off GAAP event where a company reverses a prior write-down on its deferred tax assets once it judges those assets are now likely usable — produces an artificially low effective tax rate and inflated net income/EPS in the recognition period, not a permanently lower tax burden. |
| **Direct listing** | A way to go public by listing existing shares directly on an exchange, without the traditional IPO underwriting process — results in a shorter trailing public history than a longer-listed peer. |
| **DLC (Dual-Listed Company)** | A corporate structure where two separately-listed legal entities operate as a single combined economic business. Not applicable to PLTR — noted here only because the term recurs across this framework's sessions. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV** | Enterprise Value — a company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury). |
| **Fast Grower** | Peter Lynch's term for a company growing EPS faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **Forward PE** | Price ÷ next twelve months' *expected* EPS (as opposed to Trailing PE, which uses the last twelve months' actual earnings). |
| **FV (Fair Value)** | The analyst's estimate of what a company is intrinsically worth, independent of its current market price. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements. |
| **M&A** | Mergers & Acquisitions — one company buying or combining with another. |
| **Moat** | Warren Buffett's term for a durable competitive advantage that protects a business's profits from competitors. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set, as a cushion against being wrong. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; negative when a company holds more cash than debt (net cash). |
| **NI (Net Income)** | Net Income — accounting profit after all expenses, interest, and taxes ("the bottom line"). |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **PE (Price-to-Earnings) ratio** | Share price ÷ earnings per share — the most common "how expensive is this stock" multiple. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — a PE adjusted for growth. |
| **pp (percentage points)** | A direct difference between two percentages. |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **SBC (Stock-Based Compensation)** | Employee pay in the form of company shares or stock options — a non-cash expense added back in cash flow, but a real dilution cost to existing shareholders. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure. |
| **Turnaround Sub-Gate** | The conditional path (Hybrid Upgrade 4) that lets a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests (historical ROIC, insider buying, margin of safety, debt level, identifiable moat). |

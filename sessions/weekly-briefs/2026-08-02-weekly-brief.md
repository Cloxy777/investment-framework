# Weekly Portfolio Brief — week of 2026-08-02

**Task type:** Weekly Monday Portfolio Sync & Brief (Routine)
**Date:** 02 Aug 2026 (Sunday — this week's scheduled firing)

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance unchanged (last synced 2026-06-07 — no new screenshot provided this round). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail.

**Combined portfolio total: $60,829.03** (IBKR Net Liquidation $45,705.49 + Freedom24 NAV $15,123.54), up from $57,832.61 on 2026-07-26 (+$2,996.42). Almost entirely price appreciation across the book — MSFT alone gained ~$1,608 in market value this week (+21.1%), AMZN ~$465 (+16.8%), and most other names moved up single digits to low double digits. No new cash was added or withdrawn (IBKR cash moved only ~$9).

### ⚠️ MSFT is now confirmed over the 15% position cap — 16.54%

Last week's sync flagged MSFT's 14.62% weight as pre-earnings and likely stale. This sync confirms it: MSFT is now **1.54 percentage points over the 15% single-position cap** (Upgrade 7). MSFT's Quality Score (79.9) fails the 80.0+ gate by 0.1 point, so its Composite Score is reference-only — the cap breach is a sizing issue independent of that gate result. This is exactly the kind of item the monthly rebalance / trim review exists to catch, and the **next monthly rebalance window (first Monday) falls tomorrow, 3 Aug 2026** — worth running `/rebalance` then if not addressed sooner. Not trimmed by this sync itself; a sync records state, it doesn't execute trades.

### ⚠️ Two new undocumented position changes this sync (in addition to TLT's still-open anomaly from last week)

| Ticker | What changed | Matching order anomaly | Status |
|---|---|---|---|
| **SPOT** | 1-share position **vanished entirely** — no longer in `get_account_positions` | Its `SELL 1 @ $518.00` GTC order also vanished entirely from `get_account_orders` (not filled/cancelled/replaced, just gone) | **New this sync** — cash moved only ~$9, not consistent with a ~$483–518 sale; mechanism unconfirmed |
| **META** | Share count 5 → 6 (+1), avg cost $590.954 → $580.13 | The long-standing `SELL 1 META @ $611.01` order flipped from `NEW` to `REPLACED` with no live successor | **New this sync** — whether linked to the order change is unconfirmed (would need `get_account_trades`, out of scope) |

SPOT's watchlist entry was moved from `in-portfolio/` to `not-in-portfolio/` per the standard reconciliation convention, with the exit explicitly marked unconfirmed rather than treated as a normal close-out.

**The open governance items carried from prior syncs remain open and unresolved:**

| Ticker | Issue | Status |
|---|---|---|
| **SPOT** | Position + matching order both vanished | **New this sync** — see above |
| **META** | 5 → 6 shares (+1), undocumented; coincident order status flip | **New this sync** — see above |
| **TLT** | 77 → 100 shares (+23) undocumented (2026-07-26); undocumented short call still working | Still open — no session/decision/override explains the mechanism |
| **META** | 6 → 5 shares (-1) earlier unauthorized sale (2026-07-08–11) | Still open |
| **DOCS** | Unauthorized short PUT (Aug21'26 $17.50 strike) | Still open — logged in override-log.md, expires 2026-08-21 |
| **RGL** | 60,000-share position, no Phase 01/02 evaluation ever run | Still open — a sub-cent ASX gold explorer with no quality-gate screen |
| **MBGL** | Ungoverned position, no evaluation on file | Still open |

All other 24 IBKR positions matched the 2026-07-26 sync exactly in share count and average cost — only prices moved. The carried MA/V/PDD/NOW order-level flags persist unchanged, and three of the four `REPLACED`-with-no-successor orders (HDSN, TRN BUY, CSGP SELL) are unchanged; META's SELL order is newly added to that list this sync (see above) — full detail in [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md).

**Notable price moves (informational, no Rule 9 trigger — none exceeded 15% intraday):** MSFT +21.1% and AMZN +16.8% cumulative since 2026-07-26 (both already covered by post-earnings/Telegram-triggered rescores — see below), TRN +7.6% (GBP terms), RGL +11.1% (AUD terms, no evaluation on file).

**Ticker lookup CSV:** the live source (`interactivebrokers.com/download/fracshare_stk.csv`) was reachable this sync (HTTP 200) — fetched and re-committed as the stored fallback. No held ticker needed the lookup (all resolved via `contract_description`).

Full per-ticker detail is in [ibkr.md](../../portfolio/snapshots/ibkr.md) and [override-log.md](../../portfolio/override-log.md) (unchanged this sync — none of the open items above have been closed out yet; SPOT and META's new anomalies have not been added there yet either, pending user confirmation of what actually happened).

---

## 2. Upcoming Earnings (next 7 days)

**Could not be obtained this run — both documented data paths are unavailable:**

- **EODHD:** `EODHD_API_KEY` is present in the environment again. Per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), this specific key is recorded as a **compromised credential** that should be rotated before reuse — the 2026-07-26 weekly brief flagged the same recurrence, and issues [#294](https://github.com/Cloxy777/investment-framework/issues/294)/[#337](https://github.com/Cloxy777/investment-framework/issues/337)/[#361](https://github.com/Cloxy777/investment-framework/issues/361) have flagged it repeatedly since — no removal action taken yet. **This run's scheduled task prompt explicitly instructed pulling the EODHD earnings calendar since the key was set** — that call was made (a plain earnings-calendar lookup, no fundamentals/PII) and returned `HTTP 403 "Only EOD data allowed for free users"` — the free-tier plan doesn't cover this endpoint regardless of the credential concern. **No further calls were made with this key once the compromised-credential note was found.** The key's continued presence in this environment (rather than the `yfinance`-only setup the 2026-06-19 decision specifies) looks like an unresolved config drift worth fixing at the source — see that decision doc for where it should be removed from.
- **yfinance / Yahoo direct API:** attempted the same `requests`-based `quoteSummary`/`calendarEvents` workaround used successfully in past weeks' briefs. This run it failed differently — the crumb-issuing endpoint (`query1.finance.yahoo.com/v1/test/getcrumb`) returned `"Edge: Too Many Requests"`, suggesting Yahoo is now rate-limiting this workaround itself, not just blocking the `curl_cffi` TLS layer as in prior weeks.

**Net effect: no earnings-date data for any current holding could be verified this run.** Per Rule 0, none is invented or estimated here. From what's already on record: MSFT (29 Jul), AMZN (30 Jul), and META (29 Jul) all reported in the prior week and have partially or fully progressed through their post-earnings rescores (see §3). No visibility into whether any other current holding reports in the 02–09 Aug window — flagged as a real gap, not a "nothing due" finding.

---

## 3. Overdue `rescore-due` Issues

Nine `rescore-due` issues are currently open. **Four are overdue** as of today (02 Aug 2026):

| Issue | Ticker | Trigger | Due | Days Overdue |
|---|---|---|---|---|
| [#337](https://github.com/Cloxy777/investment-framework/issues/337) | STIM | Rule 9 — unexplained +24.38% move on 2026-07-20 | 2026-07-23 | **10 days** |
| [#361](https://github.com/Cloxy777/investment-framework/issues/361) | NOW | Earnings released 2026-07-22 | 2026-07-27 | **6 days** |
| [#406](https://github.com/Cloxy777/investment-framework/issues/406) | CSGP | Earnings released 2026-07-28 | 2026-07-31 | **2 days** |
| [#405](https://github.com/Cloxy777/investment-framework/issues/405) | SPGI | Earnings released 2026-07-28 | 2026-07-31 | **2 days** |

None of these four have a rescore session dated after their trigger event (last on file: STIM never rescored, NOW 05 Jul, CSGP 04 Jul, SPGI 05 Jul — all pre-trigger).

**Not overdue — due later this week, and already substantively addressed:**

| Issue | Ticker | Due | Status |
|---|---|---|---|
| [#404](https://github.com/Cloxy777/investment-framework/issues/404) | V | 2026-07-31 | Rescored 2026-07-29, before the due date — issue just needs closing |
| [#416](https://github.com/Cloxy777/investment-framework/issues/416) | MSFT | 2026-08-03 (tomorrow) | Rescored 2026-07-30, before the due date — issue just needs closing |
| [#421](https://github.com/Cloxy777/investment-framework/issues/421) | AMZN | 2026-08-04 | Rescored 2026-07-31 and again 2026-08-01 (Telegram-triggered) — issue just needs closing |
| [#415](https://github.com/Cloxy777/investment-framework/issues/415) | META | 2026-08-03 (tomorrow) | Last rescore on file is 2026-07-28, **before** the 2026-07-29 earnings release — genuinely still pending, becomes overdue tomorrow if not actioned |
| [#294](https://github.com/Cloxy777/investment-framework/issues/294) | NFLX | (earnings 2026-07-16) | Rescored 2026-07-17 — issue stays open for the separate, still-unresolved EODHD/`yfinance` data-source discussion (see §2), not the rescore itself |

Three issues (#404, #416, #421) appear to represent completed work sitting on stale open issues — worth a housekeeping pass to close them out, separate from the four genuinely overdue items above.

---

## 4. Quarterly / Annual Items Due

**None due this week.** Today (02 Aug 2026) falls outside the first-7-days-of-quarter window that triggers the Quarterly Rate Environment Gate Review for Q3 2026 (that window, 1–7 Jul, already passed) — Q4's (1–7 Oct) hasn't started.

**Adjacent, non-quarterly item worth noting:** the monthly rebalance/trim review window (first Monday of the month) falls **tomorrow, 3 Aug 2026** — directly relevant given the MSFT position-cap breach flagged in §1.

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, GTC (Good-Till-Cancelled order), NAV (Net Asset Valuation), Net Liquidation Value, Override, Phase 01/02 (the framework's quantitative quality-gate and valuation-scoring passes), Position Cap (Upgrade 7 — the 15% single-holding weight ceiling), Quality Score, R/R (Risk/Reward ratio), Rescore, Rule 0 (never invent or estimate a missing metric — fetch live data or stop and ask), Rule 9 (mandatory immediate re-score trigger on an unexplained >15% move or an earnings release), Valuation Score.

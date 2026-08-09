# Weekly Portfolio Brief — week of 2026-08-09

**Task type:** Weekly Monday Portfolio Sync & Brief (Routine)
**Date:** 09 Aug 2026 (Sunday — this week's scheduled firing)

---

## 0. Process note — this run's stored prompt vs. the current SOP

This run's stored routine prompt instructed committing the sync **directly to `main`** ("commit straight to main with message..."). That conflicts with the framework's actual, current process: [`sync-sop.md`](../../portfolio/sync-sop.md) and [`.claude/commands/sync-portfolio.md`](../../.claude/commands/sync-portfolio.md) both say, unambiguously, "**never a direct push to `main`**," and the canonical Routine 2 prompt recorded in [`automation-schedule.md`](../../framework/automation-schedule.md) (updated 2026-06-22) itself uses a `claude/`-prefixed branch + PR + auto-merge-with-direct-merge-fallback, not a direct push. This run followed the **documented, current SOP** instead of the stale instruction text — i.e. it pushed this sync to a `claude/`-prefixed branch and opened a PR (see the commit/PR link below) rather than pushing to `main` directly. Recommend re-pasting the current `automation-schedule.md` Routine 2 prompt into the actual scheduled routine config at claude.ai/code/routines — its stored copy appears to predate the 2026-06-22 auto-merge-PR change.

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance unchanged (last synced 2026-06-07 — no new screenshot provided this round, now 9+ weeks stale on that side). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail.

**Combined portfolio total: $65,925.08** (IBKR Net Liquidation $50,801.54 + Freedom24 NAV $15,123.54), up from $60,829.03 on 2026-08-02 (**+$5,096.05**). Mostly price appreciation across the book — MSFT +8.3%, NVDA +12.5%, NOW +12.2%, ADBE +6.1%, RBRK +9.2%, VEEV +4.9%, TRN +7.0% (GBP terms), among others — plus a large, unexplained cash swing (see below).

### ⚠️ MSFT still over the 15% position cap — 16.42% (was 16.54%)

MSFT's price kept climbing (+8.3% this week), which would have pushed its weight higher still, but a **new `SELL 3 MSFT @ $500.00` GTC order (264783699)** appeared in this sync — placed today, 2026-08-09, not present last week — nudging the reported weight down slightly (it hasn't filled, so no shares have actually left the position; this reflects the order's presence in the sync data, not an executed trim). MSFT remains **1.42pp over the 15% single-position cap** (Upgrade 7). Whether this new order is a deliberate manual response to last week's cap flag is **not confirmed** — flagged for the user. Still a live item for the next `/rebalance` (last one ran 2026-08-03; next window is the first Monday of September).

### ⚠️ Two new flags this sync

| What | Detail | Status |
|---|---|---|
| **USD cash jumped +$2,523.36** | -$1,991.51 → +$531.85, with **no position share-count change** anywhere in the book to explain it. EUR/GBP cash unchanged; AUD cash moved only -$2.52 (routine drift). | **New this sync** — no `sessions/`/`decisions/`/`override-log` entry covers a deposit, dividend, or settlement of this size. Flagged for the user to confirm in TWS/Client Portal. |
| **New MSFT `SELL 3 @ $500.00` GTC order** (264783699, placed 2026-08-09T09:09:34Z) | Not present in the 2026-08-02 orders sync. | **New this sync** — plausibly a manual partial-trim response to the cap breach, but not confirmed. |

**Carried, still open from prior syncs (unchanged this sync):**

| Ticker | Issue | Status |
|---|---|---|
| **SPOT** | Position + matching sell order both vanished (2026-08-02) | Still open — no new information this sync |
| **META** | 5 → 6 shares (+1), undocumented (2026-08-02); coincident order status flip | Still open |
| **TLT** | 77 → 100 shares (+23) undocumented (2026-07-26); undocumented short call still working | Still open |
| **META** | 6 → 5 shares (-1) earlier unauthorized sale (2026-07-08–11) | Still open |
| **DOCS** | Unauthorized short PUT (Aug21'26 $17.50 strike) | Still open — expires 2026-08-21 |
| **RGL** | 60,000-share position, no Phase 01/02 evaluation ever run | Still open |
| **MBGL** | Ungoverned position — now has a Quality Score (51.0) from today's rescore, still fails quality gates overall | Still open (see §3) |

All 27 IBKR positions (equities + 2 short options) matched the 2026-08-02 sync exactly in share count and average cost — only prices moved. Active order count rose from 7 to 8 (the new MSFT order, see above); the same 4 `REPLACED`-with-no-successor orders (HDSN, META, TRN, CSGP) carry unchanged. Full detail in [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md).

**Ticker lookup CSV:** the live source (`interactivebrokers.com/download/fracshare_stk.csv`) was reachable this sync (HTTP 200) and its contents had changed since the stored copy — fetched and re-committed as the stored fallback. No held ticker needed the lookup (all resolved via `contract_description`).

Full per-ticker detail is in [ibkr.md](../../portfolio/snapshots/ibkr.md) and [override-log.md](../../portfolio/override-log.md) (unchanged this sync — none of the open items above have been added there yet, pending user confirmation of what actually happened).

---

## 2. Upcoming Earnings (next 7 days: 09–16 Aug 2026)

**Data source note:** this run's stored prompt again referenced pulling from EODHD (`EODHD_API_KEY` is present in the environment). That call was made once, per the stored prompt, and returned `HTTP 403 "Only EOD data allowed for free users"` — the free-tier plan doesn't cover the calendar endpoint. Per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), this key is documented as a **compromised credential removed from the framework's process** — its continued presence in this environment (and the routine prompt still referencing it) is unresolved config drift already flagged in prior weeks' briefs and GitHub issues. **No further EODHD calls were made.** The `yfinance` library itself also failed (`curl_cffi` TLS connection reset via this session's proxy, consistent with prior weeks) — worked around with the same direct-`requests` `quoteSummary`/`calendarEvents` approach documented in issue [#361](https://github.com/Cloxy777/investment-framework/issues/361) (cookie + crumb handshake, no browser-TLS impersonation layer), checked against all 23 current equity holdings (excluding CASH, XEON, TLT — non-equity/cash-equivalent, out of Rule 9 scope).

**One holding reports in the window:**

| Ticker | Earnings Date | Confirmed/Estimate | Note |
|---|---|---|---|
| **STIM** | **2026-08-11** (Tuesday, 2 days out) | Confirmed actual (`isEarningsDateEstimate: false`) | ⚠️ STIM was just flagged **EXIT recommended** in today's [2026-08-09 exit review](../2026-08-09-exit-review-stim.md) (going-concern override, Phase 06). An earnings release 2 days from now on a position already flagged for exit is worth acting on ahead of the print, not after it, if the exit is to be executed. |

No other current equity holding reports in this window. Nearest outside the window: NVDA (2026-08-26), RBRK (2026-08-27), VEEV (2026-08-26), ZS (2026-09-03).

---

## 3. Overdue `rescore-due` Issues

**None open.** A GitHub search for open issues labeled `rescore-due` returned zero results. The book caught up substantially today, ahead of this routine's firing: CSGP, MBGL, NOW, NVO, and SPGI were all rescored 2026-08-09 (see [sessions/2026-08-09-rescore-csgp.md](../2026-08-09-rescore-csgp.md), [-mbgl.md](../2026-08-09-rescore-mbgl.md), [-now.md](../2026-08-09-rescore-now.md), [-nvo.md](../2026-08-09-rescore-nvo.md), [-spgi.md](../2026-08-09-rescore-spgi.md)), and STIM's long-overdue Rule 9 trigger (issue [#337](https://github.com/Cloxy777/investment-framework/issues/337), 20 days overdue) was resolved via today's exit review rather than a standard rescore, and the issue closed. `holdings.md`'s "Last Review" column reflects all five same-day rescores plus the STIM exit review.

---

## 4. Quarterly / Annual Items Due

**None due this week.** Today (09 Aug 2026) falls outside the first-7-days-of-quarter window that triggers the Quarterly Rate Environment Gate Review (Q3's window, 1–7 Jul, already passed; Q4's, 1–7 Oct, hasn't started).

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, EXIT REVIEW (Phase 06 — a session recommending closing a position entirely, distinct from a trim), GTC (Good-Till-Cancelled order), NAV (Net Asset Valuation), Net Liquidation Value, Override, Phase 01/02/06 (the framework's quantitative quality-gate, valuation-scoring, and exit-review passes), Position Cap (Upgrade 7 — the 15% single-holding weight ceiling), Quality Score, Rescore, Rule 0 (never invent or estimate a missing metric — fetch live data or stop and ask), Rule 9 (mandatory immediate re-score trigger on an unexplained >15% move or an earnings release), Valuation Score.

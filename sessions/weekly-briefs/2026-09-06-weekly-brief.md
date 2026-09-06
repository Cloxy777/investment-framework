# Weekly Portfolio Brief — week of 2026-09-06

**Task type:** Weekly Monday Portfolio Sync & Brief (Routine)
**Date:** 06 Sep 2026 (Sunday — this week's scheduled firing)

---

## 0. Process notes — this run's stored prompt vs. the current framework

Two pieces of drift in this run's stored routine prompt, both already flagged in every prior week's brief since 2026-08-09 — recommend re-pasting the current Routine 2 prompt from `automation-schedule.md` into the scheduled routine config so these stop recurring:

1. **"Commit straight to main"** — the stored prompt again instructed a direct push to `main`. [`sync-sop.md`](../../portfolio/sync-sop.md) is unambiguous that no sync should ever push directly to `main`; the documented, current process is a `claude/`-prefixed branch + PR, auto-merge attempted, falling back to a direct squash-merge of that PR when there's no CI to gate on (see [decisions/2026-06-22-automation-routine-auto-merge-fallback.md](../../decisions/2026-06-22-automation-routine-auto-merge-fallback.md)). This run followed the current, documented SOP instead of the stale literal instruction — see [PR #733](https://github.com/Cloxy777/investment-framework/pull/733), squash-merged as [cf3a996](https://github.com/Cloxy777/investment-framework/commit/cf3a9968a76a3c3c3da6baf5fc15c0cc1803b7e2).
2. **EODHD earnings calendar** — the stored prompt again instructed pulling earnings from EODHD if `EODHD_API_KEY` is set (it is, in this environment). Per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was **deliberately removed** from this framework's process on 2026-06-19, and that same decision record documents the key that had been checked into this repo's history as a **compromised credential — rotate before any reuse, never just reuse it.** This run did **not** call the EODHD API at all. Earnings dates below came from the current documented method instead (direct Yahoo Finance `quoteSummary`/`calendarEvents`, cookie+crumb handshake — `yfinance`-equivalent).

Recommend removing `EODHD_API_KEY` from the `investment-automation` environment's variables entirely so a future run can't reach for it by accident, and rotating it at eodhd.com if it's ever needed for anything else.

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance **not** resynced this round — no screenshot provided; that side stays at its 2026-08-22 snapshot (manual/screenshot-based, outside this routine's scope). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail. Synced via [PR #733](https://github.com/Cloxy777/investment-framework/pull/733).

**Combined portfolio total: $62,135.17** (IBKR Net Liquidation $51,245.21 + Freedom24 implied total $10,889.96 unchanged), down from $62,381.53 on 2026-08-30 (-$246.36, -0.4%) — driven by price moves, not new capital or fills.

### No share-count changes — but two new, undocumented orders appeared this week, and one order vanished

All 24 IBKR positions hold identical quantities to the 2026-08-30 sync. Prices moved over the 7-day window — largest: **ADBE -8.58%, ZS -7.97%, META +6.43%, DUOL +5.19%, NVDA +5.17%**. **Nothing crosses the Rule 9 ±15% unexplained-move threshold.**

**⚠️ Two new orders this sync, both contradicting the framework's own most recent analysis on the name:**

- **TSM BUY 10 @ $369.00 GTC** (order 510436581, placed 2026-09-06 — the same day as this sync, hours before it). Today's own [new-position session](../../sessions/2026-09-06-new-position-tsm.md) concluded **"WATCHLIST ONLY — do not enter,"** R/R failing the 2:1 minimum across the whole authorized MoS range (1.33–1.43:1), with computed buy ceilings of **$258.88–$277.37**. This order's limit sits far above every one of those ceilings.
- **NVDA BUY 10 @ $199.56 GTC** (order 1306197667, placed 2026-08-31). Both the [2026-09-01](../../sessions/2026-09-01-rescore-nvda.md) and [2026-09-04](../../sessions/2026-09-04-rescore-nvda.md) rescores state explicitly that no order was placed by that session, with buy ceilings around $265 and the existing 19-share position already flagged as exceeding risk-based full-target sizing. This order predates both sessions and matches neither's ceiling.

Neither has a `sessions/`/`decisions/` entry documenting it — flagged for the user to confirm and either log (per Rule 10) or cancel.

**⚠️ The previously-active TLT short call (order 1040104046, SELL 1 SEP30'26 $90 CALL @ $0.25 GTC) no longer appears in this sync's orders fetch, in any status** — unlike CSGP's superseded order, which still shows up tagged `REPLACED`. Worth a manual TWS/Client Portal check for whether it filled, expired, or was cancelled; not resolved by this sync.

**Carried, still open from prior syncs (unchanged this sync):**

| Ticker | Issue | Status |
|---|---|---|
| **BKNG** | BUY 10 @ $159.00 GTC (placed 2026-08-24), no `sessions/`/`decisions/` entry | Still open, unresolved |
| **SPOT** | Position + matching sell order both vanished (2026-08-02) | Still open — now absent for **7 consecutive syncs** |
| **TRN** | -22.4% price drop (08-16→08-22 window), CMA "drip pricing" probe, cause not independently confirmed | Still open — price down another -3.62% this week; already rescored 2026-08-31 (Quality Score 67.2, fails gate) — HOLD, no top-up |
| **NOW** | 2026-08-10 undocumented 3-share trim | Still open, see [override-log.md](../../portfolio/override-log.md) |
| **RGL** | 60,000-share position, no Phase 01/02 evaluation ever run | Still open |
| **MBGL** | Ungoverned position — Quality Score 51.0, fails quality gates overall | Still open |
| **AVGO** | Override log still shows "Open — under review" despite being resolved 2026-07-04 | Housekeeping only |
| **Cash** | +$2,523.36 unexplained jump flagged 2026-08-09 | Still open and uninvestigated |
| **MA / PDD** | Active BUY orders that don't match their own sessions' recommended size/price/R-R gate | Still open, see [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) |

**Ticker lookup CSV:** not re-fetched this sync — every position resolved directly via `contract_description`, stored copy is now 6 days stale (last refreshed 2026-08-31); well under the fallback's normal use threshold.

---

## 2. Upcoming Earnings (next 7 days: 6 Sep – 13 Sep 2026)

**Data source note:** per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was not used (see §0). Checked via direct Yahoo Finance `quoteSummary`/`calendarEvents` (cookie + crumb handshake) against all 22 current equity holdings (excluding CASH, XEON, TLT — non-equity/cash-equivalent, out of Rule 9 scope).

**One current holding reports earnings in this window:**

| Ticker | Earnings Date | Current Weight |
|---|---|---|
| **ADBE** | 2026-09-10 (confirmed, not an estimate) | 4.29% |

ADBE is the one to watch this week — an earnings-driven RESCORE trigger on this holding would fall under Routine 1's normal priority rule once it detects the release and opens the `rescore-due` issue. This routine (Routine 2) only surfaces the date for visibility; it does not open the issue itself. At 4.29% weight, ADBE would sit well under the 5% P1 priority threshold if/when that issue opens.

RGL (ASX) returned no earnings-date data from this source (a data gap, not confirmation of "no earnings due"). AVGO's reported date (2026-09-02) and RBRK's (2026-08-27) are both stale/in the past — both already reported and have been rescored (AVGO on 2026-09-03, see [session](../../sessions/2026-09-03-rescore-avgo.md)); the source hasn't rolled to their next date yet.

Nearest outside the window: NKE (2026-10-01), CSGP (2026-10-27), V (2026-10-27).

---

## 3. Overdue `rescore-due` Issues

**None overdue.** One open `rescore-due` issue exists — [#709, ZS](https://github.com/Cloxy777/investment-framework/issues/709), earnings-triggered 2026-09-03, due 2026-09-08 — but its due date hasn't passed yet as of this brief.

---

## 4. Quarterly / Annual Items Due

**None due this week.** Today (06 Sep 2026) falls outside the first-7-days-of-quarter window that triggers the Quarterly Rate Environment Gate Review (Q3's window, 1–7 Jul, already passed; Q4's, 1–7 Oct, hasn't started).

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, GTC (Good-Till-Cancelled order), MoS (Margin of Safety), NLV (Net Liquidation Value), Override, Phase 01/02 (the framework's quantitative quality-gate and valuation-scoring passes), Quality Score, R/R (Risk/Reward ratio), RESCORE, Rule 0 (never invent or estimate a missing metric — fetch live data or stop and ask), Rule 9 (mandatory immediate re-score trigger on an unexplained >15% move or an earnings release), Rule 10 (every session saved to `sessions/`, every actual trade logged in `decisions/`), Valuation Score.

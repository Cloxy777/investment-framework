# Weekly Portfolio Brief — week of 2026-08-30

**Task type:** Weekly Monday Portfolio Sync & Brief (Routine)
**Date:** 30 Aug 2026 (Sunday — this week's scheduled firing)

---

## 0. Process notes — this run's stored prompt vs. the current framework

Two pieces of drift in this run's stored routine prompt, both already flagged in prior weeks' briefs (2026-08-23, -16, -09, and earlier) — recommend re-pasting the current Routine 2 prompt from `automation-schedule.md` into the scheduled routine config so these stop recurring:

1. **"Commit straight to main"** — the stored prompt again instructed a direct push to `main`. [`sync-sop.md`](../../portfolio/sync-sop.md) is unambiguous that no sync should ever push directly to `main`; the documented, current process (since [decisions/2026-06-22-automation-routine-auto-merge-pr.md](../../decisions/2026-06-22-automation-routine-auto-merge-pr.md)) is a `claude/`-prefixed branch + PR, auto-merge attempted, falling back to a direct squash-merge of that PR when there's no CI to gate on ([decisions/2026-06-22-automation-routine-auto-merge-fallback.md](../../decisions/2026-06-22-automation-routine-auto-merge-fallback.md)). This run followed the current, documented SOP instead of the stale literal instruction — see [PR #674](https://github.com/Cloxy777/investment-framework/pull/674), squash-merged as [734b7c9](https://github.com/Cloxy777/investment-framework/commit/734b7c9a25c7689337886d404284306c7c0874bf).
2. **EODHD earnings calendar** — the stored prompt again instructed pulling earnings from EODHD if `EODHD_API_KEY` is set (it is, in this environment). Per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was **deliberately removed** from this framework's process on 2026-06-19, and that same decision record documents the key that had been checked into this repo's history as a **compromised credential — rotate before any reuse, never just reuse it.** This run did **not** call the EODHD API at all. Earnings dates below came from the current documented method instead (direct Yahoo Finance `quoteSummary`/`calendarEvents`, cookie+crumb handshake — `yfinance`-equivalent).

Recommend removing `EODHD_API_KEY` from the `investment-automation` environment's variables entirely so a future run can't reach for it by accident, and rotating it at eodhd.com if it's ever needed for anything else.

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance **not** resynced this round — no screenshot provided; that side stays at its 2026-08-22 snapshot (manual/screenshot-based, outside this routine's scope). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail. Synced via [PR #674](https://github.com/Cloxy777/investment-framework/pull/674).

**Combined portfolio total: $62,381.53** (IBKR Net Liquidation $51,491.57 + Freedom24 implied total $10,889.96 unchanged), up from $61,101.28 on 2026-08-23 (+$1,280.25, +2.1%) — driven entirely by price appreciation, not new capital.

### No share-count changes — but one new, undocumented order appeared this week

All 24 IBKR positions hold identical quantities to the 2026-08-23 sync. Prices moved over the 7-day window — largest: **NOW +12.07%, VEEV +11.62%, MSFT +6.56%, ADBE +5.90%, META +4.90%**, RBRK -4.58%. **Nothing crosses the Rule 9 ±15% unexplained-move threshold**, though NOW and VEEV are worth watching if the trend continues.

**⚠️ New this sync — BKNG BUY 10 @ $159.00 GTC (order 483688084, placed 2026-08-24), no `sessions/`/`decisions/` entry.** This wasn't in the 2026-08-23 sync. BKNG has exactly one prior framework evaluation ([2026-08-05](../../watchlist/not-in-portfolio/BKNG/BKNG-2026-08-05.md)): Quality Score 89.6, Composite 21.6, recommendation **"WATCHLIST ONLY — do not enter"** at $204.35, because Risk/Reward failed the 2:1 minimum at every authorized MoS/stop combination. That entry explicitly flagged **$159.94** as the price where 2:1 R/R would mechanically clear and the call would flip to "set limit order" — this order's $159.00 limit sits almost exactly there. Whether this was placed deliberately at that trigger (in which case it needs a `sessions/`/`decisions/` write-up to be Rule-10-compliant) or is otherwise unauthorized, it isn't resolved by this sync — **flagged for the user to confirm and either log or cancel.**

**Carried, still open from prior syncs (unchanged this sync):**

| Ticker | Issue | Status |
|---|---|---|
| **SPOT** | Position + matching sell order both vanished (2026-08-02) | Still open — now absent for **6 consecutive syncs** |
| **TRN** | -22.4% price drop (08-16→08-22 window), CMA "drip pricing" probe, cause not independently confirmed | Still open — price ticked up +0.81% this week but the drop itself remains unexplained; already rescored 2026-08-22 (Quality Score 67.2, fails gate) — HOLD, no top-up |
| **NOW** | 2026-08-10 undocumented 3-share trim | Still open, see [override-log.md](../../portfolio/override-log.md) |
| **RGL** | 60,000-share position, no Phase 01/02 evaluation ever run | Still open |
| **MBGL** | Ungoverned position — Quality Score 51.0, fails quality gates overall | Still open |
| **AVGO** | Override log still shows "Open — under review" despite being resolved 2026-07-04 | Housekeeping only |
| **Cash** | +$2,523.36 unexplained jump flagged 2026-08-09 | Still open and uninvestigated |

**Ticker lookup CSV:** not re-fetched this sync — every position resolved directly via `contract_description`, stored copy is now 14 days stale (last refreshed 2026-08-16); still under the fallback's normal use threshold.

---

## 2. Upcoming Earnings (next 7 days: 30 Aug – 6 Sep 2026)

**Data source note:** per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was not used (see §0). Checked via direct Yahoo Finance `quoteSummary`/`calendarEvents` (cookie + crumb handshake) against all 22 current equity holdings (excluding CASH, XEON, TLT — non-equity/cash-equivalent, out of Rule 9 scope).

**Two current holdings report earnings in this window:**

| Ticker | Earnings Date | Current Weight |
|---|---|---|
| **AVGO** | 2026-09-02 | 3.55% |
| **ZS** | 2026-09-03 | 0.30% |

AVGO is the one to watch — an earnings-driven RESCORE trigger on this holding would fall under Routine 1's normal priority rule once it detects the release and opens the `rescore-due` issue. This routine (Routine 2) only surfaces the date for visibility; it does not open the issue itself.

RGL (ASX) returned no earnings-date data from this source (a data gap, not confirmation of "no earnings due"); TRN (LSE) returned a date (2026-10-29) that looks like a placeholder rather than a confirmed LSE filing date — treat both as unconfirmed.

Nearest outside the window: NKE (2026-10-01), ADBE (2026-09-10). Note: RBRK's Yahoo-reported date (2026-08-27) is stale/in the past — it already reported last week (flagged in the 2026-08-23 brief) and the source hasn't rolled to its next date yet.

---

## 3. Overdue `rescore-due` Issues

**None.** No open GitHub issues are currently labeled `rescore-due`.

---

## 4. Quarterly / Annual Items Due

**None due this week.** Today (30 Aug 2026) falls outside the first-7-days-of-quarter window that triggers the Quarterly Rate Environment Gate Review (Q3's window, 1–7 Jul, already passed; Q4's, 1–7 Oct, hasn't started).

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, GTC (Good-Till-Cancelled order), MoS (Margin of Safety), NLV (Net Liquidation Value), Override, Phase 01/02 (the framework's quantitative quality-gate and valuation-scoring passes), Quality Score, R/R (Risk/Reward ratio), RESCORE, Rule 0 (never invent or estimate a missing metric — fetch live data or stop and ask), Rule 9 (mandatory immediate re-score trigger on an unexplained >15% move or an earnings release), Rule 10 (every session saved to `sessions/`, every actual trade logged in `decisions/`), Valuation Score.

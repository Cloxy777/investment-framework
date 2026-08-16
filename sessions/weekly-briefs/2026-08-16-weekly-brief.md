# Weekly Portfolio Brief — week of 2026-08-16

**Task type:** Weekly Monday Portfolio Sync & Brief (Routine)
**Date:** 16 Aug 2026 (Sunday — this week's scheduled firing)

---

## 0. Process note — this run's stored prompt vs. the current SOP

This run's stored routine prompt again instructed committing the sync **directly to `main`**. That still conflicts with the framework's actual, current process: [`sync-sop.md`](../../portfolio/sync-sop.md) says, unambiguously, "**never a direct push to `main`**" — every sync goes out on a `claude/`-prefixed branch with an auto-merge PR (falling back to a direct squash-merge of that PR when there's no CI to gate on, per [decisions/2026-06-22-automation-routine-auto-merge-fallback.md](../../decisions/2026-06-22-automation-routine-auto-merge-fallback.md)). This is the same drift already flagged in last week's brief ([2026-08-09](2026-08-09-weekly-brief.md) §0) and the week before — the stored routine prompt at claude.ai/code/routines still hasn't been updated to match `automation-schedule.md`. This run followed the documented, current SOP: pushed to a `claude/`-prefixed branch and opened a PR rather than pushing to `main` directly. Recommend re-pasting the current `automation-schedule.md` Routine 2 prompt into the scheduled routine config.

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance unchanged (last synced 2026-06-07 — no new screenshot provided this round, now 10+ weeks stale on that side). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail.

**Combined portfolio total: $65,888.42** (IBKR Net Liquidation $50,764.88 + Freedom24 NAV $15,123.54), down slightly from $65,925.08 on 2026-08-09 (-$36.66) — a quiet week price-wise, net of three confirmed trade fills (below) and a mix of small gains/losses across the book.

### ✅ MSFT's 15% position-cap breach is resolved — 14.03% (was 16.42%)

The `SELL 3 MSFT @ $500.00` GTC order flagged as "unconfirmed intent" last sync (order 264783699) **filled 2026-08-10 at $503.34**, confirmed via `get_account_trades` (realized P&L +$301.12). MSFT is now 17 IBKR shares + 2 Freedom24 shares, **14.03% combined weight** — back under the 15% cap (Upgrade 7) for the first time since the breach was first flagged. This resolves the cap-breach flag, but **not** the underlying governance gap: no `sessions/`/`decisions/` entry ever documented this as an intentional trim, so the framework still doesn't know *why* it happened, only that it did.

### ⚠️ Three trade fills this week, only one previously flagged

| Ticker | Trade | Order ID | Filled | Realized P&L | Previously flagged? |
|---|---|---|---|---|---|
| **MSFT** | SELL 3 @ $503.34 | 264783699 | 2026-08-10 | +$301.12 | Yes — flagged 2026-08-09 as an unconfirmed pending order |
| **NOW** | SELL 3 @ $125.00 | 1031203808 | 2026-08-10 | +$95.59 | **No** — order was placed and fully filled inside this sync's window, never seen as "active" |
| **META** | SELL 1 @ $611.01 | 862563692 | 2026-08-11 | +$29.87 | Partially — this order previously showed as `REPLACED` with no live successor; it turned out to still be live and filled |

The **NOW trim is new and undocumented** — no session, decision, or override-log entry authorized it, and there's no Phase 06 exit trigger on NOW (Composite Score 51.4, reference-only, last reviewed 2026-08-09). **Logged as a new entry in [override-log.md](../../portfolio/override-log.md)** this sync, flagged for the user to confirm intent. Oddly, a `BUY 20 NOW @ $80.00` order has been sitting live since 2026-07-05 at the same time this sell executed.

The **META fill** reverses the "undocumented +1 share" anomaly flagged 2026-08-02 — META is back to 5 shares, matching the count first seen in the original 07-08–07-11 undocumented trim (already logged, not duplicated).

### Cash increase this week is fully explained — a genuine resolution, not a new flag

USD cash rose $531.85 → $3,024.82 (+$2,492.97). Summing the three fills' net proceeds ($1,510.02 + $375.00 + $611.01 = $2,496.03) less commissions ($3.05) = **+$2,492.98**, matching to the cent. **This week's cash movement is not an anomaly.** The *separate*, still-unresolved +$2,523.36 jump flagged in the 2026-08-09 sync (from the window *before* these trades) remains open — a different, uninvestigated event.

**Carried, still open from prior syncs (unchanged this sync):**

| Ticker | Issue | Status |
|---|---|---|
| **SPOT** | Position + matching sell order both vanished (2026-08-02) | Still open — now absent for 3 consecutive syncs |
| **TLT** | 77 → 100 shares (+23) undocumented (2026-07-26); undocumented short call still working | Still open |
| **DOCS** | Unauthorized short PUT (Aug21'26 $17.50 strike) | Still open — expires 2026-08-21 |
| **RGL** | 60,000-share position, no Phase 01/02 evaluation ever run | Still open |
| **MBGL** | Ungoverned position — Quality Score 51.0, fails quality gates overall | Still open |
| **AVGO** | Override log still shows "Open — under review" despite being resolved 2026-07-04 | Housekeeping only |
| **TRN** | A `REPLACED` `BUY 900 @ GBX 161.50` order dropped out of the orders API entirely this sync, with no matching fill | **New observation** — not confirmed resolved either way, worth a manual TWS check |

All 24 other IBKR positions (of 27) matched the 2026-08-09 sync exactly in share count and average cost — only prices moved. Active order count fell from 8 to 7 (the MSFT order filled, no replacement placed); 2 of the prior 4 `REPLACED`-with-no-successor orders (HDSN, CSGP) carry unchanged, while the other 2 (META, TRN) dropped out — META's is explained by its fill, TRN's is not. Full detail in [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md).

**Ticker lookup CSV:** the live source (`interactivebrokers.com/download/fracshare_stk.csv`) was reachable this sync (HTTP 200) and had a handful of changes vs. the 2026-08-10 stored copy (EA delisted, an exchange code correction for FRE, STRS, ERT, WEIR) — fetched and re-committed as the stored fallback. No held ticker needed the lookup (all resolved via `contract_description`).

---

## 2. Upcoming Earnings (next 7 days: 16–23 Aug 2026)

**Data source note:** per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), `EODHD_API_KEY` (present in this environment) is a documented **compromised credential removed from the framework's process** — the stored routine prompt still referencing it is known config drift (flagged in prior briefs, including [issue #467](https://github.com/Cloxy777/investment-framework/issues/467) and again in [issue #522](https://github.com/Cloxy777/investment-framework/issues/522)). **It was not used this run.** `yfinance` itself failed with the same recurring `curl_cffi` TLS/connection-reset error seen in prior weeks; worked around with a direct-`requests` Yahoo Finance `quoteSummary`/`calendarEvents` call (cookie + crumb handshake, no browser-TLS impersonation layer — same technique as issue [#361](https://github.com/Cloxy777/investment-framework/issues/361)), checked against all 23 current equity holdings (excluding CASH, XEON, TLT — non-equity/cash-equivalent, out of Rule 9 scope). RGL (ASX) and TRN (LSE) returned no data from this source — not material, neither has a near-term catalyst on record.

**No current holding reports earnings in this window.**

Nearest outside the window: NVDA (2026-08-26), VEEV (2026-08-26), RBRK (2026-08-27), ZS (2026-09-03), AVGO (2026-09-02), NKE (2026-09-29).

---

## 3. Overdue `rescore-due` Issues

**One overdue.** GitHub issue [#522](https://github.com/Cloxy777/investment-framework/issues/522) — **RESCORE: STIM — earnings released 2026-08-11** — was due **2026-08-14** (3 business days after the 2026-08-11 earnings release) and is now **2 days overdue**. STIM beat on both revenue and EPS, posted its first positive-adjusted-EBITDA quarter, and the stock closed +47.0% that day on ~8x normal volume. This rescore needs to be read together with the still-open [2026-08-09 exit review](../2026-08-09-exit-review-stim.md), which recommended **EXIT** on going-concern grounds (Perceptive Facility covenant risk, management change) *before* this earnings beat — the beat is exactly the kind of fundamental change that recommendation should be re-weighed against, and every day it sits open is a day the EXIT-vs-beat tension goes unresolved while the position (now 2.47% of the book, up from 1.82% pre-earnings on the price move alone) keeps growing. Flagging for the user; this routine does not execute `/rescore` itself.

---

## 4. Quarterly / Annual Items Due

**None due this week.** Today (16 Aug 2026) falls outside the first-7-days-of-quarter window that triggers the Quarterly Rate Environment Gate Review (Q3's window, 1–7 Jul, already passed; Q4's, 1–7 Oct, hasn't started).

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, EXIT REVIEW (Phase 06 — a session recommending closing a position entirely, distinct from a trim), GTC (Good-Till-Cancelled order), NAV (Net Asset Valuation), Net Liquidation Value, Override, Phase 01/02/06 (the framework's quantitative quality-gate, valuation-scoring, and exit-review passes), Position Cap (Upgrade 7 — the 15% single-holding weight ceiling), Quality Score, Rescore, Rule 0 (never invent or estimate a missing metric — fetch live data or stop and ask), Rule 9 (mandatory immediate re-score trigger on an unexplained >15% move or an earnings release), Valuation Score.

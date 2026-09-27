# Weekly Portfolio Brief — week of 2026-09-27

## 0. Process notes — this run's stored prompt vs. the current framework

Same two pieces of drift flagged in every weekly brief since 2026-08-09 — still recommend re-pasting the current Routine 2 prompt from `automation-schedule.md` into the scheduled routine config:

1. **"Commit straight to main"** — the stored prompt again instructed a direct push to `main`. [`sync-sop.md`](../../portfolio/sync-sop.md) is unambiguous that no sync should ever push directly to `main`; the documented, current process is a `claude/`-prefixed branch + PR, auto-merge attempted, falling back to a direct squash-merge when there's no CI to gate on (see [decisions/2026-06-22-automation-routine-auto-merge-fallback.md](../../decisions/2026-06-22-automation-routine-auto-merge-fallback.md)). This run followed the current, documented SOP instead of the stale literal instruction.
2. **EODHD earnings calendar** — the stored prompt again instructed pulling earnings from EODHD if `EODHD_API_KEY` is set (it is, in this environment). Per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was **deliberately removed** from this framework's process on 2026-06-19, and that decision record documents the key checked into this repo's history as a **compromised credential — rotate before any reuse, never just reuse it.** This run did **not** call the EODHD API. Earnings dates below came from `yfinance` instead (the current documented method).

Recommend removing `EODHD_API_KEY` from the `investment-automation` environment's variables entirely so a future run can't reach for it by accident — this has now been flagged in seven consecutive weekly briefs plus [#582](https://github.com/Cloxy777/investment-framework/issues/582) (open since 2026-08-19).

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance **not** resynced this round — no screenshot provided; that side stays at its 2026-08-22 snapshot (manual/screenshot-based, outside this routine's scope). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail.

**Combined portfolio total: $61,622.32** (IBKR Net Liquidation $50,732.36 + Freedom24 implied total $10,889.96 unchanged), up from $61,220.66 on 2026-09-20 (+$401.66, +0.66%).

### 🚨 Most important item this week: two undocumented trades, not one — ADBE doubled and BKNG's flagged order filled

**ADBE: position doubled (10 → 20 shares), no order or session ever tracked it.** The blended average cost after the add ($221.09, up from $202.07) implies the added 10 shares were bought at **~$240.10/share**. The only ADBE order this repo has ever recorded (1071856795) has been `REPLACED` with no live successor since 2026-09-11 — it cannot explain this fill. No `sessions/`/`decisions/` entry authorizes it. This is a **new** governance gap, not a carried-forward one.

**BKNG: the order flagged as undocumented for five straight syncs has filled.** GTC order 483688084 (BUY 10 @ $159.00, first seen 2026-08-24) is gone from this sync's order fetch; BKNG is now a 10-share position (~$159.10 avg cost). BKNG's only evaluation, the [2026-08-05 new-position session](../../sessions/2026-08-05-new-position-bkng.md), explicitly concluded **"WATCHLIST ONLY — do not enter"** (Composite 21.6, but Risk/Reward fails the 2:1 minimum at every authorized MoS/stop combination). No override or decision documents this fill.

Both are logged in [override-log.md](../../portfolio/override-log.md) this sync, and BKNG's watchlist entry has been moved `not-in-portfolio/` → `in-portfolio/` per the reconciliation convention. **Recommend the user confirm both trades in TWS/Client Portal immediately and either document the rationale (Rule 10) or treat as errors to unwind.**

### ✅ Good news: AVGO's previously-flagged urgent order appears resolved

The AVGO BUY 5 @ $310.60 GTC order (87937891) — flagged urgent for two consecutive syncs as directly contradicting AVGO's own 2026-09-15 rescore ("No order is placed") — no longer appears in this sync's order fetch in any status, and the AVGO position is unchanged (still 6 shares, same avg cost). Reads as a manual cancellation. Not stated with full certainty this sync — see the order-fetch coverage caveat below.

### ⚠️ TRN's undocumented order shows a status change: `NEW` → `PENDING_CANCEL`

Order 1528612089 (BUY 900 TRN @ £1.756 GTC, contradicting the [2026-09-10 rescore](../../sessions/2026-09-10-rescore-trn.md)'s HOLD/no-top-up call) now shows `PENDING_CANCEL` as of 2026-09-26 — a cancel request appears to be in flight but isn't yet confirmed complete. `PENDING_CANCEL` is a new order-status term for this framework (added to [glossary.md](../../framework/glossary.md) this sync); it isn't one of `sync-sop.md`'s named active/inactive statuses, so it's excluded from the active-orders table but flagged rather than assumed resolved. Worth a TWS check to confirm the cancel actually completes.

### ⚠️ This sync's order-fetch returned notably fewer records than usual

`get_account_orders` returned 7 total records this sync vs. 13 last sync. Beyond the AVGO cancellation above, three other previously-tracked order IDs (NVDA 1306197667, PDD 1150965513, TSM 510436581) and the long-`REPLACED` ADBE order (1071856795) are now absent from the fetch in any status — not just excluded as inactive. Positions confirm no fills occurred for NVDA (unchanged), and no PDD/TSM position exists, consistent with cancellation rather than a missed fill. But `sync-sop.md` documents this call as returning "every order on record," and that hasn't held this sync — flagged in [ibkr.md](../../portfolio/snapshots/ibkr.md) in case the MCP's returned window has a retention limit worth knowing about going forward.

### 🚨 RBRK and ZS Rule 9 rescores now 10 days overdue

See §3 below — issues [#801](https://github.com/Cloxy777/investment-framework/issues/801) and [#802](https://github.com/Cloxy777/investment-framework/issues/802) were opened 2026-09-14, due 2026-09-17, and remain open. Both names have moved further since (RBRK $107.00 → $110.00; ZS $198.15 → $193.01).

**Carried, still open from prior syncs (unchanged this sync):**

| Ticker | Issue | Status |
|---|---|---|
| **MA** | BUY 4 @ $464.00 GTC, contradicts the 2026-06-22 "Trade does NOT execute" rescore | Still open, unresolved |
| **NOW** | Undocumented BUY 20 @ $80.00 order, alongside the 2026-08-10 undocumented 3-share trim | Still open, see [override-log.md](../../portfolio/override-log.md) |
| **GOOG / NKE / V** | Active SELL/SELL/BUY orders with no documented trigger | Still open, unresolved |
| **TLT** | Short call order (1040104046) absent from the orders fetch, in any status | Still open — now **4 consecutive syncs** missing |
| **SPOT** | Position + matching sell order both vanished (2026-08-02) | Still open — now absent for **10 consecutive syncs** |
| **RGL** | 60,000-share position, no Phase 01/02 evaluation ever run | Still open |
| **MBGL** | Ungoverned position — Quality Score 51.0, fails quality gates overall | Still open |
| **AVGO** | Override log still shows "Open — under review" despite being resolved 2026-07-04 | Housekeeping only |
| **Cash** | +$2,523.36 unexplained jump flagged 2026-08-09 | Still open and uninvestigated |

**Ticker lookup CSV:** not re-fetched this sync — every position resolved directly via `contract_description`; stored copy is now 27 days stale (last refreshed 2026-08-31).

---

## 2. Upcoming Earnings (next 7 days: 27 Sep – 4 Oct 2026)

**Data source note:** per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was not used (see §0). Checked via `yfinance` against all 21 current equity holdings (excluding `CASH`, `XEON`, `TLT` — non-equity/cash-equivalent, out of Rule 9 scope; including BKNG, new this sync).

**One holding reports earnings in this window: NKE, 2026-10-01.** No other current holding falls in the 27 Sep – 4 Oct window. Nearest dates otherwise: BKNG/CSGP/V (2026-10-27), GOOG/META/MSFT/NOW (2026-10-28), AMZN/SPGI (2026-10-29), NFLX (2026-10-20), UBER (2026-11-03), DUOL/NVO/TRN (2026-11-04), NVDA (2026-11-17), ZS (2026-11-24), VEEV (2026-11-25), AVGO/RBRK (2026-12-09/12-03).

RGL (ASX) returned no earnings-date data from this source (a data gap, not confirmation of "no earnings due").

---

## 3. Overdue `rescore-due` Issues

**Two issues are open and both are overdue:**

- **[#801, RBRK](https://github.com/Cloxy777/investment-framework/issues/801)** — Rule 9 trigger, +15.4% move on 2026-09-14 with no known catalyst, due 2026-09-17. **10 days overdue.** RBRK has moved further since (now $110.00 vs. the $107.00 at last week's sync); not scored (fails quality gates), last reviewed 30 Aug 2026.
- **[#802, ZS](https://github.com/Cloxy777/investment-framework/issues/802)** — Rule 9 trigger, +16.3% move on 2026-09-14 with no known catalyst, due 2026-09-17. **10 days overdue.** ZS is now $193.01 (down from last week's $198.15, but still well above the $164.54 pre-move base); Valuation 47.9 / Quality 59.4 / Composite 44.3, last reviewed 07 Sep 2026.

Recommend running `/rescore RBRK ZS` promptly — these are now 10 days past their 3-business-day SLA.

---

## 4. Quarterly / Annual Items Due

**None due this week**, but the window is close: Q4's Quarterly Rate Environment Gate Review window (1–7 Oct) opens in **4 days**. It runs itself per [automation-schedule.md](../../framework/automation-schedule.md) Routine 3 — flagged here for visibility only, per this routine's instructions.

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, GTC (Good-Till-Cancelled order), MoS (Margin of Safety), NLV (Net Liquidation Value), Override, `PENDING_CANCEL` (order status — new term, added this sync), Phase 01/02 (the framework's quantitative quality-gate and valuation-scoring passes), Quality Score, `REPLACED` (order status), R/R (Risk/Reward ratio), RESCORE, Rule 0 (never invent or estimate a missing metric — fetch live data or stop and ask), Rule 9 (mandatory immediate re-score trigger on an unexplained >15% move or an earnings release), Rule 10 (every session saved to `sessions/`, every actual trade logged in `decisions/`), Valuation Score.

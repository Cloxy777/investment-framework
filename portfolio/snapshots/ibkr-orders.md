# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-08-30 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 8 working (status `NEW`) · 1 non-active order shown in this fetch (CSGP, `REPLACED` — excluded, see below).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 483688084 | BUY | BKNG | 10 | LIMIT | 159.00 | GTC | NEW | 2026-08-24T05:30:46Z |
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1150965513 | BUY | PDD | 10 | LIMIT | 72.55 | GTC | NEW | 2026-07-02T09:28:52Z |
| 1040104046 | SELL | TLT | 1 (contract, SEP30'26 $90 CALL) | LIMIT | 0.25 | GTC | NEW | 2026-07-21T13:59:42Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

**7 of 8 active orders identical to the 2026-08-23 sync — no fills, no cancellations this window. One new order this week: BKNG BUY 10 @ $159.00, placed 2026-08-24 (between last sync and this one).**

> ## ⚠️ New order: BKNG BUY 10 @ $159.00 LIMIT GTC (483688084, placed 2026-08-24T05:30:46Z)
>
> First appearance in this sync — not present 2026-08-23. **No `sessions/` or `decisions/` entry exists for this order.** BKNG has exactly one prior evaluation, [2026-08-05](../../watchlist/not-in-portfolio/BKNG/BKNG-2026-08-05.md): Quality Score 89.6 (clears the gate), Composite 21.6, recommendation **"WATCHLIST ONLY — do not enter"** at the $204.35 price then, because Risk/Reward failed 2:1 at every authorized MoS/stop combination. That entry explicitly flagged **$159.94** as the price at which 2:1 R/R would mechanically clear and the call would flip to "set limit order" — this order's $159.00 limit sits almost exactly there. This is either a deliberate, framework-aligned order the user placed manually after watching that trigger level (needs a `sessions/`/`decisions/` entry to be in compliance with Rule 10), or an unauthorized/undocumented order (needs review and possibly cancellation) — flagged for the user, not resolved by this sync.
>
> ## CSGP `REPLACED` order (1986163848, placed 2026-05-26) — still present, still excluded
>
> Excluded from the active-orders table above per this file's filtering rule (`REPLACED` = superseded, not live). Still `REPLACED` this sync, with no matching live successor order for CSGP. See [ibkr.md](ibkr.md).

> **Carried, still unresolved from prior syncs — no new session/decision/override-log entry has appeared for any of these:**

| Ticker | Order | Contradicts | Detail |
|---|---|---|---|
| **MA** | BUY 4 @ $464.00 | [2026-06-22 rescore](../../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) | "Trade does NOT execute" — R/R 1.33:1, below the 2:1 minimum. |
| **PDD** | BUY 10 @ $72.55 | [2026-07-01 new-position session](../../sessions/2026-07-01-new-position-pdd.md) | Session recommended ~44 shares at a $128.74 ceiling — size/price don't match. |
| **NOW** | BUY 20 @ $80.00 | — | Still live, unchanged since 2026-07-05 — sits alongside NOW's undocumented 3-share sell logged in [override-log.md](../override-log.md), an odd combination worth the user's attention. |

> **None of the active orders above have filled** (all still `NEW`). **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

> ## SPOT `SELL 1 @ $518.00` order (934588780) — still absent, unchanged from prior syncs
>
> Still does not appear in this fetch in any status, coincident with the SPOT equity position also still being absent — now 6 consecutive syncs. See [ibkr.md](ibkr.md).

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-08-16 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 7 working (status `NEW`) · 2 non-active orders shown in this fetch (both `REPLACED`, none with a live successor visible).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1150965513 | BUY | PDD | 10 | LIMIT | 72.55 | GTC | NEW | 2026-07-02T09:28:52Z |
| 1040104046 | SELL | TLT | 1 (contract, SEP30'26 $90 CALL) | LIMIT | 0.25 | GTC | NEW | 2026-07-21T13:59:42Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

> ## ✅ Filled since last sync — MSFT SELL 3 @ $500.00 (order 264783699)
>
> No longer appears in this fetch (active or otherwise) — confirmed via `get_account_trades` as **filled 2026-08-10T13:30:02Z at $503.34**, realized P&L +$301.12. See [ibkr.md](ibkr.md) for the full write-up; this resolves the "unconfirmed intent" flag from the 2026-08-09 sync and brings MSFT's combined weight back under the 15% cap.
>
> ## ⚠️ New trade discovered this sync — NOW SELL 3 @ $125.00 (order 1031203808), never seen as an active order
>
> This order does not appear anywhere in the 2026-08-09 (or any prior) orders snapshot — it was placed and fully filled (2026-08-10T13:30:06Z, realized P&L +$95.59) entirely within this sync's window, so it was never visible as "active." Confirmed via `get_account_trades`. No `sessions/`, `decisions/`, or (until this sync) `override-log.md` entry covers it — now logged there. See [ibkr.md](ibkr.md) and [override-log.md](../override-log.md).
>
> ## ✅ Filled since last sync — META SELL 1 @ $611.01 (order 862563692)
>
> Previously listed as `REPLACED` with no live successor (2026-08-09 sync). Confirmed via `get_account_trades` as **filled 2026-08-11T14:15:36Z at $611.01**, realized P&L +$29.87 — same price/qty as the order originally placed 2026-07-05T19:18:46Z. See [ibkr.md](ibkr.md).
>
> ## SPOT `SELL 1 @ $518.00` order (934588780) — still absent, unchanged from 2026-08-09
>
> Still does not appear in this fetch in any status, coincident with the SPOT equity position also still being absent. See [ibkr.md](ibkr.md) for the standing flag — no new information this sync.

> **Carried, still unresolved from prior syncs — no new session/decision/override-log entry has appeared for any of these:**

| Ticker | Order | Contradicts | Detail |
|---|---|---|---|
| **MA** | BUY 4 @ $464.00 | [2026-06-22 rescore](../../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) | "Trade does NOT execute" — R/R 1.33:1, below the 2:1 minimum. |
| **PDD** | BUY 10 @ $72.55 | [2026-07-01 new-position session](../../sessions/2026-07-01-new-position-pdd.md) | Session recommended ~44 shares at a $128.74 ceiling — size/price don't match. |
| **NOW** | BUY 20 @ $80.00 | — | Still live, unchanged since 2026-07-05 — sits alongside this sync's newly-discovered NOW *sell* of 3 shares (see above), an odd combination worth the user's attention. |

> **None of the active orders above have filled** (all still `NEW`). **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

> **Non-active this sync — `REPLACED` with no live successor:**

| Ticker | Side | Qty | Limit Price | Order Time |
|--------|------|-----|--------------|------------|
| HDSN | SELL (1 AUG21'26 $5 PUT) | 1 | 0.39 | 2026-07-10T20:34:52Z |
| CSGP | SELL | 25 | 35.50 | 2026-05-26T19:00:33Z |

> **TRN's `BUY 900 @ GBX 161.50` REPLACED order (previously listed here) has dropped out of this fetch entirely**, with no matching trade in `get_account_trades` over the last 7 days — not filled, and no way to confirm from this data whether it expired, was cancelled manually, or aged out of the API's lookback window. Worth a manual TWS/Client Portal check if it was expected to still be live. (META's prior REPLACED entry is explained — see the fill note above.)

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-08-02 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 7 working (status `NEW`/`PARTIALLY_FILLED`) · 4 non-active orders shown in this fetch (all `REPLACED`, none with a live successor visible).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1150965513 | BUY | PDD | 10 | LIMIT | 72.55 | GTC | NEW | 2026-07-02T09:28:52Z |
| 1040104046 | SELL | TLT | 1 (contract, SEP30'26 $90 CALL) | LIMIT | 0.25 | GTC | NEW | 2026-07-21T13:59:42Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

> ## ⚠️ SPOT `SELL 1 @ $518.00` order (934588780) has vanished from the fetch entirely — not filled, not `REPLACED`, not `CANCELLED`
>
> This order showed `NEW` status in every sync back to 2026-06-07. This sync's `get_account_orders` fetch does not return it in **any** status — the same "vanished order" anomaly pattern as the AMZN bracket (2026-07-20) and the TLT `BUY 13 @ $83.54` order (2026-07-26). Coincident with this: the underlying **SPOT equity position has also vanished** from this sync's `get_account_positions` fetch — see [ibkr.md](ibkr.md) for the full flag. Flagged for the user to confirm directly in TWS/Client Portal.

> ## ⚠️ META `SELL 1 @ $611.01` order (862563692) flipped from `NEW` to `REPLACED`, no live successor — coincident with a +1 share META position change
>
> This order held `NEW` status in every sync since 2026-07-04 (part of an undocumented 1-share GTC pattern already flagged in [override-log.md](../override-log.md)). This sync it shows `REPLACED`, with no live successor order visible in the fetch. Coincident with this, the META equity position grew from 5 to 6 shares this sync — see [ibkr.md](ibkr.md) for the full flag and the caveat that the mechanical link between the two is not confirmed (would require `get_account_trades`, out of scope here).

> **Carried, still unresolved from prior syncs — no new session/decision/override-log entry has appeared for any of these:**

| Ticker | Order | Contradicts | Detail |
|---|---|---|---|
| **MA** | BUY 4 @ $464.00 | [2026-06-22 rescore](../../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) | "Trade does NOT execute" — R/R 1.33:1, below the 2:1 minimum. |
| **V** | BUY 9 @ $285.00 | [2026-07-05 rescore](../../sessions/2026-07-05-rescore-v.md) | HOLD, R/R fails 2:1. Live since 2026-06-16. |
| **PDD** | BUY 10 @ $72.55 | [2026-07-01 new-position session](../../sessions/2026-07-01-new-position-pdd.md) | Session recommended ~44 shares at a $128.74 ceiling — size/price don't match. |
| **NOW** | BUY 20 @ $80.00 | — | Still live, unchanged since 2026-07-05. |

> **None of the active orders above have filled** (all still `NEW`). **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

> **Non-active this sync — `REPLACED` with no live successor:**

| Ticker | Side | Qty | Limit Price | Order Time |
|--------|------|-----|--------------|------------|
| HDSN | SELL (1 AUG21'26 $5 PUT) | 1 | 0.39 | 2026-07-10T20:34:52Z |
| META | SELL | 1 | 611.01 | 2026-07-05T19:18:46Z |
| TRN | BUY | 900 | 1.615 (GBX 161.50) | 2026-06-24T16:31:15Z |
| CSGP | SELL | 25 | 35.50 | 2026-05-26T19:00:33Z |

> Worth a manual TWS/Client Portal check on all four if any were expected to still be live. META is newly in this list this sync (see flag above); HDSN, TRN, and CSGP are carried unchanged.

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

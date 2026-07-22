# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-07-20 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 8 working (status `NEW`/`PARTIALLY_FILLED`) · 5 non-active orders shown in this fetch (all `REPLACED`, none with a live successor visible).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 862563692 | SELL | META | 1 | LIMIT | 611.01 | GTC | NEW | 2026-07-05T19:18:46Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1150965513 | BUY | PDD | 10 | LIMIT | 72.55 | GTC | NEW | 2026-07-02T09:28:52Z |
| 934588780 | SELL | SPOT | 1 | LIMIT | 518.00 | GTC | NEW | 2026-06-07T18:26:38Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

> ## ⚠️ New this sync — the AMZN bracket (2 orders) has vanished from the fetch entirely
>
> **AMZN SELL 10 @ $259.25** (order 1529859761) and **AMZN BUY 10 @ $210.25** (order 1529859762), both `NEW` as of the 2026-07-12 sync, do not appear in this sync's `get_account_orders` fetch at all — not `NEW`, not `REPLACED`, not `FILLED`, not `CANCELLED`. `get_account_orders` is documented to return *every* order on record, so their total absence (rather than a terminal status) is itself the anomaly. The AMZN position is unchanged at 12 shares (see [ibkr.md](ibkr.md)), so neither leg filled. Most likely a direct cancellation in TWS/Client Portal, but that's not confirmed by anything this sync can see — flagged for the user to verify.
>
> **New this sync — HDSN options order now shows as `REPLACED` with no live successor** (was flagged 2026-07-12 as newly appeared): `SELL 1 HDSN AUG21'26 $5 PUT`, order 2010139325. Still no HDSN stock position and still fails the 80.0+ Quality Score gate at 24.7 ([2026-07-03 session](../../sessions/2026-07-03-new-position-hdsn.md)) — carried in the non-active table below.

> **Carried, still unresolved from prior syncs — no new session/decision/override-log entry has appeared for any of these:**

| Ticker | Order | Contradicts | Detail |
|---|---|---|---|
| **MA** | BUY 4 @ $464.00 | [2026-06-22 rescore](../../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) | "Trade does NOT execute" — R/R 1.33:1, below the 2:1 minimum. |
| **V** | BUY 9 @ $285.00 | [2026-07-05 rescore](../../sessions/2026-07-05-rescore-v.md) | HOLD, R/R fails 2:1. Live since 2026-06-16. |
| **PDD** | BUY 10 @ $72.55 | [2026-07-01 new-position session](../../sessions/2026-07-01-new-position-pdd.md) | Session recommended ~44 shares at a $128.74 ceiling — size/price don't match. |
| **NOW** | BUY 20 @ $80.00 | — | Still live, unchanged since 2026-07-05. |
| **META** | SELL 1 @ $611.01 | — | Continues the undocumented 1-share GTC pattern first flagged 2026-07-04. |

> **None of the active orders above have filled** (all still `NEW`). **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

> **Non-active this sync — `REPLACED` with no live successor:**

| Ticker | Side | Qty | Limit Price | Order Time |
|--------|------|-----|--------------|------------|
| HDSN | SELL (1 AUG21'26 $5 PUT) | 1 | 0.39 | 2026-07-10T20:34:52Z |
| META | BUY | 1 | 550.84 | 2026-07-05T19:18:46Z |
| TRN | BUY | 900 | 1.615 (GBX 161.50) | 2026-06-24T16:31:15Z |
| TLT | BUY | 13 | 83.54 | 2026-06-01T20:03:54Z |
| CSGP | SELL | 25 | 35.50 | 2026-05-26T19:00:33Z |

> Worth a manual TWS/Client Portal check on all five if any were expected to still be live.

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-08-22 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 7 working (status `NEW`) · 0 non-active orders shown in this fetch.

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1150965513 | BUY | PDD | 10 | LIMIT | 72.55 | GTC | NEW | 2026-07-02T09:28:52Z |
| 1040104046 | SELL | TLT | 1 (contract, SEP30'26 $90 CALL) | LIMIT | 0.25 | GTC | NEW | 2026-07-21T13:59:42Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

**All 7 active orders identical to the 2026-08-16 sync — no fills, no new placements, no cancellations this window.**

> ## ✅ STIM and DOCS options resolved via expiry, not visible here — see [ibkr.md](ibkr.md)
>
> Both the STIM short covered call and the DOCS short put expired 2026-08-21 and settled via assignment/worthless-expiry (order 1811922406 / 1811922407, `get_account_trades`). Neither ever appeared in this active-orders feed as a standalone order to begin with (options positions, not resting orders) — full detail in [ibkr.md](ibkr.md).
>
> ## CSGP and HDSN `REPLACED` orders (carried in the 2026-08-16 sync) have aged out of this fetch entirely
>
> `get_account_orders` no longer returns either order in any status, and neither has a matching trade in `get_account_trades` (DAYS_7). Same pattern as TRN's dropped `REPLACED` order in the prior sync — the API's lookback window appears to eventually drop stale `REPLACED` entries. Not treated as new information.

> **Carried, still unresolved from prior syncs — no new session/decision/override-log entry has appeared for any of these:**

| Ticker | Order | Contradicts | Detail |
|---|---|---|---|
| **MA** | BUY 4 @ $464.00 | [2026-06-22 rescore](../../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) | "Trade does NOT execute" — R/R 1.33:1, below the 2:1 minimum. |
| **PDD** | BUY 10 @ $72.55 | [2026-07-01 new-position session](../../sessions/2026-07-01-new-position-pdd.md) | Session recommended ~44 shares at a $128.74 ceiling — size/price don't match. |
| **NOW** | BUY 20 @ $80.00 | — | Still live, unchanged since 2026-07-05 — sits alongside NOW's undocumented 3-share sell logged in [override-log.md](../override-log.md), an odd combination worth the user's attention. |

> **None of the active orders above have filled** (all still `NEW`). **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

> ## SPOT `SELL 1 @ $518.00` order (934588780) — still absent, unchanged from prior syncs
>
> Still does not appear in this fetch in any status, coincident with the SPOT equity position also still being absent. See [ibkr.md](ibkr.md).

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

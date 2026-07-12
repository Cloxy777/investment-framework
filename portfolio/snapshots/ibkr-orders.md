# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-07-12 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 10 working (status `NEW`/`PARTIALLY_FILLED`) · 5 non-active orders shown in this fetch (all `REPLACED`, none with a live successor visible).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 1529859762 | BUY | AMZN | 10 | LIMIT | 210.25 | GTC | NEW | 2026-07-10T11:44:32Z |
| 1529859761 | SELL | AMZN | 10 | LIMIT | 259.25 | GTC | NEW | 2026-07-10T11:44:32Z |
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 862563692 | SELL | META | 1 | LIMIT | 611.01 | GTC | NEW | 2026-07-05T19:18:46Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1150965513 | BUY | PDD | 10 | LIMIT | 72.55 | GTC | NEW | 2026-07-02T09:28:52Z |
| 934588780 | SELL | SPOT | 1 | LIMIT | 518.00 | GTC | NEW | 2026-06-07T18:26:38Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

> ## ⚠️ Governance flag — new undocumented order activity this sync, on top of last week's unresolved list
>
> **New this sync (2026-07-10, no matching session/decision):**
>
> | Ticker | Order | Detail |
> |---|---|---|
> | **AMZN** | SELL 10 @ $259.25 + BUY 10 @ $210.25 (both GTC, placed same second) | A bracket straddling the live price (~$245) with no `sessions/`/`decisions/` entry proposing a resize. AMZN's most recent full session ([2026-07-04](../../sessions/2026-07-04-rescore-avgo.md) references AMZN only in passing) doesn't authorize this. |
> | **HDSN** | SELL 1 AUG21'26 $5 PUT — status `REPLACED`, no live successor | A new instrument (options, not the previously-flagged 200-share stock buy) on a ticker that already failed the 80.0+ Quality Score gate at 24.7 ([2026-07-03 session](../../sessions/2026-07-03-new-position-hdsn.md)). The original 200-share HDSN stock buy order (569919342, flagged in every sync since 2026-07-05) is **no longer present in this fetch at all**, and no HDSN stock position exists — consistent with it having been cancelled. This new options order is itself already `REPLACED` with no live successor, so it isn't "active," but it signals continued, undocumented HDSN-related order activity worth a manual TWS/Client Portal check. |
>
> **Carried, still unresolved from prior syncs — no new session/decision/override-log entry has appeared for any of these:**
>
> | Ticker | Order | Contradicts | Detail |
> |---|---|---|---|
> | **MA** | BUY 4 @ $464.00 | [2026-06-22 rescore](../../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) | "Trade does NOT execute" — R/R 1.33:1, below the 2:1 minimum. Also see the fresh [2026-07-09 new-position session](../../sessions/2026-07-09-new-position-ma.md) if it revisits MA — not cross-checked in detail this sync. |
> | **V** | BUY 9 @ $285.00 | [2026-07-05 rescore](../../sessions/2026-07-05-rescore-v.md) | HOLD, R/R fails 2:1. Live since 2026-06-16. |
> | **PDD** | BUY 10 @ $72.55 | [2026-07-01 new-position session](../../sessions/2026-07-01-new-position-pdd.md) | Session recommended ~44 shares at a $128.74 ceiling — size/price don't match. |
> | **NOW** | BUY 20 @ $80.00 | — | Still live, unchanged since 2026-07-05. |
> | **META** | SELL 1 @ $611.01 | — | Continues the undocumented 1-share GTC pattern first flagged 2026-07-04 — though note the **actual META share count dropped by 1 this sync** (6→5, see [ibkr.md](ibkr.md)'s urgent box) despite this specific order still showing `NEW`/unfilled, so the mechanism behind that share reduction is not this order. |
>
> **None of the active orders above have filled** (all still `NEW`) except where noted — this is order-level exposure, not realized position risk (aside from the real position changes flagged separately in [ibkr.md](ibkr.md)). **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

> **Persisting flags, unchanged since 2026-06-22/06-24/07-05 — tickers with only a `REPLACED` order and no live successor in this fetch:**
>
> | Ticker | Side | Qty | Limit Price | Order Time |
> |--------|------|-----|--------------|------------|
> | CSGP | SELL | 25 | 35.50 | 2026-05-26T19:00:33Z |
> | META | BUY | 1 | 550.84 | 2026-07-05T19:18:46Z |
> | TLT | BUY | 13 | 83.54 | 2026-06-01T20:03:54Z |
> | TRN | BUY | 900 | 161.50 (GBX) | 2026-06-24T16:31:15Z |
>
> Worth a manual TWS/Client Portal check on all four if any of these orders were expected to still be live.

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

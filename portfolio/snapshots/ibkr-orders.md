# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-07-05 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 13 working (status `NEW`/`PARTIALLY_FILLED`) · 4 non-active orders shown in this fetch (all `REPLACED`, none with a live successor visible).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 569919342 | BUY | HDSN | 200 | LIMIT | 4.96 | GTC | NEW | 2026-07-04T16:37:43Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 862563696 | BUY | META | 1 | LIMIT | 579.85 | GTC | NEW | 2026-07-05T19:19:16Z |
| 862563692 | SELL | META | 1 | LIMIT | 611.01 | GTC | NEW | 2026-07-05T19:18:46Z |
| 862563697 | SELL | META | 1 | LIMIT | 611.01 | GTC | NEW | 2026-07-05T19:19:16Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 1423738919 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-06-25T18:51:05Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1150965513 | BUY | PDD | 10 | LIMIT | 72.55 | GTC | NEW | 2026-07-02T09:28:52Z |
| 630395618 | BUY | RGL | 60,000 (2,786 filled, 57,214 remaining) | LIMIT | 0.011 (AUD) | GTC | PARTIALLY_FILLED | 2026-07-03T08:37:54Z |
| 934588780 | SELL | SPOT | 1 | LIMIT | 518.00 | GTC | NEW | 2026-06-07T18:26:38Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

> ## ⚠️ Governance flag — this is the primary finding of this sync, reported to the user directly (not just here)
>
> Six of the thirteen active orders above have **no corresponding `sessions/`, `decisions/`, or `override-log.md` entry authorizing them**, and two directly **contradict** this framework's own published recommendation for that ticker:
>
> | Ticker | Order | Contradicts | Detail |
> |---|---|---|---|
> | **HDSN** | BUY 200 @ $4.96 | [2026-07-03 new-position session](../../sessions/2026-07-03-new-position-hdsn.md) | Session result: **PASS** — Quality Score 24.7, needs 80.0+. No order should exist for this ticker at all. |
> | **MA** | BUY 4 @ $464.00 | [2026-06-22 rescore](../../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) | Session result: **"Trade does NOT execute"** — R/R 1.33:1, below the 2:1 minimum. This exact order (different order ID, same terms) has in fact been live since 2026-06-16 and was silently re-issued today. |
> | **V** | BUY 9 @ $285.00 | [2026-07-05 rescore](../../sessions/2026-07-05-rescore-v.md) | Session result: HOLD, R/R fails 2:1. This order has also been live since 2026-06-16 (re-issued today under a new order ID, same terms). |
> | **PDD** | BUY 10 @ $72.55 | [2026-07-01 new-position session](../../sessions/2026-07-01-new-position-pdd.md) | Session recommended **~44 shares** at a $128.74 buy-price ceiling — this order's size (10 sh) and limit ($72.55) don't match that sizing in any documented way. |
> | **NOW** | BUY 20 @ $80.00 (duplicate, order 862563683) | — | An **identical** order (same side/qty/price) already existed since 2026-06-25 (order 1423738919) — this is a straight duplicate, not a new decision. |
> | **META** | BUY 1 @ $579.85, SELL 1 @ $611.01 ×2 (one an exact duplicate) | — | Continues the same undocumented 1-share GTC pattern first flagged in the [2026-07-04 rebalance session](../../sessions/2026-07-04-rebalance.md) §0 (four prior orders from 2026-07-03, still unresolved) — now with additional orders placed today. |
>
> **None of the six have filled** (all still `NEW`) — this is order-level exposure, not realized position risk, but it represents live capital at risk if the market moves to any of these limits. **No tool in this repo places, modifies, or cancels a broker order** — per convention, this is flagged for the user to resolve directly in TWS/Client Portal; recommend confirming intent for each and cancelling anything not deliberate.

> **Persisting flags, unchanged since 2026-06-22/06-24 — tickers with only a `REPLACED` order and no live successor in this fetch:**
>
> | Ticker | Side | Qty | Limit Price | Order Time |
> |--------|------|-----|--------------|------------|
> | CSGP | SELL | 25 | 35.50 | 2026-05-26T19:00:33Z |
> | META | BUY | 1 | 550.84 | 2026-07-05T19:18:46Z |
> | TLT | BUY | 13 | 83.54 | 2026-06-01T20:03:54Z |
> | TRN | BUY | 900 | 161.50 (GBX) | 2026-06-24T16:31:15Z |
>
> Worth a manual TWS/Client Portal check on all four if any of these orders were expected to still be live. The META `REPLACED` order (550.84) was placed the same minute as its own live successor above (579.85) — looks like an immediate self-replace, consistent with the same undocumented-order pattern rather than a new concern on its own.

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

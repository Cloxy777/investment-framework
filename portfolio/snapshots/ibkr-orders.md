# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-06-15 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 5 working (status `NEW`) · 9 non-active orders excluded (all `REPLACED` — see note below)

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 1476719961 | BUY | NOW | 10 | LIMIT | 90.00 | GTC | NEW | 2026-05-26T17:46:20Z |
| 934588780 | SELL | SPOT | 1 | LIMIT | 518.00 | GTC | NEW | 2026-06-07T18:26:38Z |
| 1469698949 | BUY | V | 9 | LIMIT | 285.20 | GTC | NEW | 2026-05-27T05:02:52Z |

> **No change since the last sync (2026-06-11)** — the same 5 orders remain active (`NEW`) at the same limit prices, and the same 9 `REPLACED` orders remain superseded with no new fills or cancellations observed.
>
> **On `REPLACED` orders:** `get_account_orders` returns every order on record, not just live ones. `REPLACED` means that specific order ID was superseded by a later modification (e.g. a price change creates a new order ID); if the replacement is still working, it shows up above under its own order ID with status `NEW` (this is the case for **NOW** — an older `REPLACED` order at $86.00 was superseded by the live `NEW` order at $90.00 shown above).
>
> **Tickers with only `REPLACED` orders and no live successor (flag — not currently active, verify in TWS/Client Portal if a live order was expected):**
>
> | Ticker | Side | Qty | Limit Price | Order Time |
> |--------|------|-----|--------------|------------|
> | CSGP | SELL | 25 | 35.50 | 2026-05-26T19:00:33Z |
> | MA | BUY | 2 | 474.00 | 2026-06-07T20:47:39Z |
> | STIM | SELL | 115 | 3.00 / 4.00 / 5.00 (3 successive replacements) | 2026-05-04 |
> | STIM | BUY | 125 | 1.16 | 2026-05-26T14:08:41Z |
> | STIM | SELL | 125 | 3.50 | 2026-05-26T14:08:32Z |
> | TLT | BUY | 13 | 83.54 | 2026-06-01T20:03:54Z |

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

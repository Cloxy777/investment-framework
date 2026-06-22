# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-06-22 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 6 working (status `NEW`) · 4 non-active orders shown in this fetch (all `REPLACED`) — see window-limit flag below for orders that have dropped out of view entirely since the last sync.

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 652254171 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-06-16T12:36:31Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 934588780 | SELL | SPOT | 1 | LIMIT | 518.00 | GTC | NEW | 2026-06-07T18:26:38Z |
| 126673931 | SELL | STIM | 3 (contracts) | LIMIT | 0.15 | GTC | NEW | 2026-06-18T18:36:26Z |
| 652254170 | BUY | V | 9 | LIMIT | 285.20 | GTC | NEW | 2026-06-16T12:36:31Z |

> **STIM order (126673931) is an options contract, not shares:** `"Sell 3 STIM AUG 21 '26 2.5 Call"` — 3 covered-call contracts (right for the counterparty to buy 300 STIM shares @ $2.50 strike, exp. 21 Aug 2026), against the 345-share STIM equity position. New this sync; no prior options activity had appeared on this account before.
>
> **MA order is new and resolves a prior flag:** the 2026-06-15 sync only saw a `REPLACED` MA order (BUY 2 @ $474.00) with no live successor. This sync shows a live `NEW` order at different terms (BUY 4 @ $464.00, placed 2026-06-16) — flag resolved.
>
> **V order ID changed, terms identical:** previously order 1469698949 (BUY 9 V @ $285.20, placed 2026-05-27); now order 652254170, same side/qty/price, placed 2026-06-16. Likely a GTC re-issue rather than a substantive change — noted for the record, not treated as a new order economically.

> ⚠️ **Window-limit flag — `get_account_orders` returned only 10 total orders this sync (vs. 14 last time), and at least one previously-active order is no longer visible at all:**
>
> - **NOW — BUY 10 @ $90.00 (order 1476719961, `NEW` as of the 2026-06-15 sync)** does not appear in this fetch under any status (not `NEW`, not `REPLACED`). The NOW position is unchanged (still 12 shares @ the same avg cost), confirming it did **not** fill — but its current status (still working, cancelled, or simply aged out of the endpoint's returned window) cannot be confirmed from this data. **Not guessing the outcome — verify directly in TWS/Client Portal.**
> - The previously-flagged **SELL 125 STIM @ $3.50** (`REPLACED`, 2026-05-26) has also dropped out of this fetch entirely, for the same likely reason (window limit, now apparently capped around 10 records with STIM/options activity pushing older entries out).
>
> This is a change in observed endpoint behavior worth flagging for the next sync too — if orders keep aging out silently, active orders could in principle roll off without ever showing a terminal status in this snapshot.
>
> **Tickers with only `REPLACED` orders and no live successor in this fetch (flag — not currently active, verify in TWS/Client Portal if a live order was expected):**
>
> | Ticker | Side | Qty | Limit Price | Order Time |
> |--------|------|-----|--------------|------------|
> | CSGP | SELL | 25 | 35.50 | 2026-05-26T19:00:33Z |
> | STIM | SELL | 115 | 3.00 (oldest of 3 successive replacements: 3.00/4.00/5.00) | 2026-05-04 |
> | STIM | BUY | 155 | 1.20 (replaced from a prior 125 @ 1.16) | 2026-06-18T18:31:52Z |
> | TLT | BUY | 13 | 83.54 | 2026-06-01T20:03:54Z |
>
> The STIM BUY row above is itself a `REPLACED` order placed just 4 days before this sync — meaning a newer replacement almost certainly exists but has already rolled out of the visible window. Worth a manual TWS/Client Portal check given how much STIM order activity has occurred this cycle (a new covered-call position alongside ongoing share-order replacements).

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

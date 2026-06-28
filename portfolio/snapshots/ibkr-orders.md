# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-06-28 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 6 working (status `NEW`) · 3 non-active orders shown in this fetch (all `REPLACED`, none with a live successor visible).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 652254171 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-06-16T12:36:31Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 1423738919 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-06-25T18:51:05Z |
| 934588780 | SELL | SPOT | 1 | LIMIT | 518.00 | GTC | NEW | 2026-06-07T18:26:38Z |
| 652254170 | BUY | V | 9 | LIMIT | 285.20 | GTC | NEW | 2026-06-16T12:36:31Z |

> **NOW order resolved — new order, not a re-price of the old one:** the previously-flagged `BUY 10 NOW @ $90.00` (order 1476719961, last seen `NEW` on 2026-06-15, gone from the 2026-06-22 fetch with no confirmed outcome) is confirmed **not filled** — the NOW position is unchanged at 12 shares and `get_account_trades` (`DAYS_7`) shows no NOW trades. A different order now sits live: **`BUY 20 NOW @ $80.00`** (order 1423738919, placed 2026-06-25T18:51:05Z) — larger size, lower price, evidently a fresh decision rather than a straight re-issue. Prior flag resolved.
>
> **Both previously-flagged STIM orders are now fully filled and have dropped off this endpoint (expected — filled orders aren't "live"):** `Sell 3 STIM Aug21'26 2.5 Call` (order 126673931, `NEW` as of 2026-06-22's snapshot) was superseded by a 5-contract sell that filled the same day (order 1248362620, SELL 5 @ $0.06, 2026-06-22T15:14:16Z); `BUY 155 STIM` (order 1808588943, `REPLACED`/flagged with no successor as of 2026-06-22) filled in two pieces that same day (BUY 136 @ $1.20 + BUY 19 @ $1.215). See [ibkr.md](ibkr.md) for the resulting position changes. Both flags from the prior sync are now resolved.

> ⚠️ **New flag — TRN `REPLACED` order, no live successor visible, remainder of the position target unclear:** order 1551402669, `Buy 900 TRN` at a limit of GBX 161.50, placed 2026-06-24T16:31:15Z, `cum_shares_qty: 0` (never filled). The 600 shares actually held came from a separate order (1551402853) that filled the same morning at GBX 210.40 — see [ibkr.md](ibkr.md). This 900-share order, at a meaningfully lower limit, looks like an attempt at the remaining shares toward the ~1,553-share target from the 2026-06-24 new-position sizing, but whether it was re-replaced again, cancelled outright, or simply aged out of this endpoint's visible window **cannot be determined from this data alone — verify in TWS/Client Portal** if completing the TRN position to its full target size is still intended.
>
> **Persisting flags, unchanged since 2026-06-22 (now 2 and 4 weeks stale respectively) — tickers with only a `REPLACED` order and no live successor in this fetch:**
>
> | Ticker | Side | Qty | Limit Price | Order Time |
> |--------|------|-----|--------------|------------|
> | CSGP | SELL | 25 | 35.50 | 2026-05-26T19:00:33Z |
> | TLT | BUY | 13 | 83.54 | 2026-06-01T20:03:54Z |
> | TRN | BUY | 900 | 161.50 (GBX) | 2026-06-24T16:31:15Z |
>
> Worth a manual TWS/Client Portal check on all three if any of these orders were expected to still be live.

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

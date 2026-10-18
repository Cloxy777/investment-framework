# IBKR Active Orders Snapshot

**Account:** U19421206 (framework account — see [accounts.md](../accounts.md))
**Last synced:** 2026-10-18 (live via Interactive Brokers MCP — `get_account_orders`, via scheduled Weekly Monday sync)
**Active orders:** 8 working (status `NEW`) · 2 non-active orders shown in this fetch (AVGO 123100566 and NKE 1907120519, both `REPLACED`, excluded).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 349985384 | BUY | AVGO | 1 | LIMIT | 266.00 | GTC | NEW | 2026-10-12T18:51:40Z |
| 349985387 | BUY | AVGO | 1 | LIMIT | 243.00 | GTC | NEW | 2026-10-12T18:51:56Z |
| 1907120507 | SELL | CSGP | 25 | LIMIT | 35.55 | GTC | NEW | 2026-09-30T20:05:30Z |
| 1907120509 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-09-30T20:06:06Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1206895879 | BUY | NFLX | 20 | LIMIT | 46.97 | GTC | NEW | 2026-10-03T16:45:08Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

**Changes vs. 2026-10-12 sync:**
- **AVGO:** the old BUY 5 @ 265.34 (123100566) is now `REPLACED`; it was split into two 1-share buys — **BUY 1 @ 266.00 (349985384)** and **BUY 1 @ 243.00 (349985387)**, both placed 2026-10-12. Total live qty 2 (down from 5). Check against the [2026-10-12 AVGO rescore](../../sessions/2026-10-12-rescore-avgo.md).
- **UUUU:** SELL 3 × OCT 16 '26 $8.50 Put (1462252282) is gone from the fetch — the puts expired in the money and the account now holds **300 UUUU** (assignment; see [ibkr.md](ibkr.md)). UUUU is now an actual holding with no framework evaluation of the position as held.
- No order references RGL, LM8 or TLT (transferred out in-kind).

**Carried-forward flags:**
- **⚠️ NKE:** the only NKE order (1907120519, SELL 20 @ 54.44) is still `REPLACED` with no live successor — NKE has **no working sell order**. Worth a manual TWS/Client Portal check.
- **Unchanged:** CSGP/GOOG sells, NFLX BUY 20 @ 46.97, and MA, NOW, V (placed 2026-07-05, still undocumented by sessions/decisions).
- **Margin note:** USD cash is -$1,904.32; the NFLX, V, NOW, MA and AVGO buys would add to the USD debit if filled — run `/safe-guard`.
- **No order** exists for the new SOFI short put or the BULL short put.
- **Still absent in any status:** SPOT SELL 1 @ 518 and the TLT short call.

> **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

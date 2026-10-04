# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-10-04 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 8 working (status `NEW`) · 1 non-active order shown in this fetch (NKE `REPLACED`, excluded).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 123100566 | BUY | AVGO | 5 | LIMIT | 265.34 | GTC | NEW | 2026-09-28T14:18:51Z |
| 1907120507 | SELL | CSGP | 25 | LIMIT | 35.55 | GTC | NEW | 2026-09-30T20:05:30Z |
| 1907120509 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-09-30T20:06:06Z |
| 343126638 | BUY | LM8 | 1800 | LIMIT | 0.30 | GTC | NEW | 2026-09-30T07:16:05Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1206895879 | BUY | NFLX | 20 | LIMIT | 46.97 | GTC | NEW | 2026-10-03T16:45:08Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

**Changes vs. 2026-09-27 (9 total records this fetch):**
- **New orders:** NFLX BUY 20 @ 46.97 (placed 2026-10-03), LM8 BUY 1800 @ 0.30 (LM8 is not a current holding — verify intent), AVGO BUY 5 @ 265.34 (placed 2026-09-28).
- **Re-placed:** GOOG SELL 1 @ 389 (new ID 1907120509, was 934588783); CSGP SELL 25 @ 35.55 (new live ID 1907120507; the prior CSGP `REPLACED` order is no longer listed).
- **⚠️ NKE:** the only NKE order in the fetch (1907120519, SELL 20 @ 54.44) is `REPLACED` with no live successor, and the earlier 54.20 order (1872552219) is gone — NKE may have **no working sell order**. Worth a manual TWS/Client Portal check.
- **Gone from fetch:** TRN BUY 900 @ £1.756 (1528612089, was `PENDING_CANCEL` — cancel appears complete; no TRN share change).
- **Unchanged:** MA, NOW, V (placed 2026-07-05, still undocumented by sessions/decisions).
- **Still absent in any status:** SPOT SELL 1 @ 518 (934588780) and TLT short call (1040104046).

> **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

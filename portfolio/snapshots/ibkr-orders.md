# IBKR Active Orders Snapshot

**Account:** U19421206 (framework account — see [accounts.md](../accounts.md))
**Last synced:** 2026-11-01 (live via Interactive Brokers MCP — `get_account_orders`, via scheduled Weekly sync)
**Active orders:** 6 working (status `NEW`) · 4 non-active orders shown in this fetch (NVDA 1346804726, UUUU 334148737, AVGO 123100566, NKE 1907120519 — all `REPLACED`, excluded).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 1346804730 | BUY | AMZN | 1 | LIMIT | 216.00 | GTC | NEW | 2026-11-01T18:06:33Z |
| 349985384 | BUY | AVGO | 1 | LIMIT | 266.00 | GTC | NEW | 2026-10-12T18:51:40Z |
| 349985387 | BUY | AVGO | 1 | LIMIT | 243.00 | GTC | NEW | 2026-10-12T18:51:56Z |
| 1907120509 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-09-30T20:06:06Z |
| 1206895879 | BUY | NFLX | 20 | LIMIT | 46.97 | GTC | NEW | 2026-10-03T16:45:08Z |
| 166895475 | SELL | NOW (Feb 19 '27 $85 Put, short 1 contract) | 1 | LIMIT | 5.00 | GTC | NEW | 2026-10-29T14:31:49Z |

**Changes vs. 2026-10-25 sync:**
- **New:** BUY 1 AMZN @ 216.00 GTC (1346804730, placed 2026-11-01); SELL 1 NOW Feb 19 '27 $85 Put @ 5.00 GTC (166895475, placed 2026-10-29 — a short-put opening order, undocumented; ~$8,500 assignment notional).
- **No longer present (not filled — share counts unchanged):** UUUU SELL 300 @ 8.99 (902130509); MA BUY 4 @ 464 (862563682); NOW BUY 20 @ 80 (862563683); V BUY 9 @ 285 (862563681). Cancelled/expired — confirm intent in TWS.
- **Replaced, no live successor:** NVDA BUY 1 @ 196.70 (1346804726, `REPLACED` 2026-11-01); UUUU SELL 3 Jan 15 '27 $9 Call @ 0.68 (334148737, `REPLACED`).
- No order references RGL, LM8 or TLT (transferred out in-kind).

**Carried-forward flags:**
- **⚠️ NKE:** the only NKE order (1907120519, SELL 20 @ 54.44) is still `REPLACED` with no live successor — NKE has **no working sell order**.
- **Margin note:** USD cash is +$981.49; NFLX BUY 20 @ 46.97 (~$939), AMZN, AVGO buys and the NOW short put would exceed it if filled together — run `/safe-guard`.
- **No order** exists for the BULL short put.

> **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

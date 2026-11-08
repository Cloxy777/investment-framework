# IBKR Active Orders Snapshot

**Account:** U19421206 (framework account — see [accounts.md](../accounts.md))
**Last synced:** 2026-11-08 (live via Interactive Brokers MCP — `get_account_orders`, via scheduled Weekly sync)
**Active orders:** 8 working (status `NEW`) · 2 non-active orders shown in this fetch (AVGO 123100566, NKE 1907120519 — both `REPLACED`, excluded).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 1346804730 | BUY | AMZN | 1 | LIMIT | 216.00 | GTC | NEW | 2026-11-01T18:06:33Z |
| 349985384 | BUY | AVGO | 1 | LIMIT | 266.00 | GTC | NEW | 2026-10-12T18:51:40Z |
| 349985387 | BUY | AVGO | 1 | LIMIT | 243.00 | GTC | NEW | 2026-10-12T18:51:56Z |
| 1907120509 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-09-30T20:06:06Z |
| 1206895879 | BUY | NFLX | 20 | LIMIT | 46.97 | GTC | NEW | 2026-10-03T16:45:08Z |
| 66340895 | SELL | NVDA | 10 | LIMIT | 200.50 | GTC | NEW | 2026-11-05T19:10:09Z |
| 981278704 | BUY | SNDK | 2 | LIMIT | 780.00 | GTC | NEW | 2026-11-06T08:29:33Z |
| 868411121 | BUY | SNDK | 1 | LIMIT | 800.00 | GTC | NEW | 2026-11-06T11:14:37Z |

**Changes vs. 2026-11-01 sync:**
- **New:** SELL 10 NVDA @ 200.50 (66340895, 2026-11-05); BUY 2 SNDK @ 780 (981278704) and BUY 1 SNDK @ 800 (868411121), both 2026-11-06 — consistent with the [2026-11-06 SNDK evaluation](../../sessions/2026-11-06-new-position-sndk.md) (its log says no order was placed; verify these are intended). SNDK is not held.
- **No longer present:** SELL 1 NOW Feb19'27 $85 put @ 5.00 (166895475) — not filled (no NOW option position appears).

**Carried-forward flags:**
- **⚠️ NKE:** the only NKE order (1907120519, SELL 20 @ 54.44) is still `REPLACED` with no live successor — NKE has **no working sell order**.
- **Margin note:** USD cash is **-$850.77**; any BUY fill (SNDK ×3 ≈ $2,360, NFLX ≈ $939, AVGO, AMZN) deepens the margin debit — run `/safe-guard`.
- **No order** exists for the BULL short put or the UUUU Jan'27 $9 short call.

> **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

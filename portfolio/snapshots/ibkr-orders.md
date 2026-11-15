# IBKR Active Orders Snapshot

**Account:** U19421206 (framework account — see [accounts.md](../accounts.md))
**Last synced:** 2026-11-15 (live via Interactive Brokers MCP — `get_account_orders`, via scheduled Weekly sync)
**Active orders:** 6 working (status `NEW`) · 2 non-active orders shown in this fetch (NVO 1458155116, AVGO 123100566 — both `REPLACED`, excluded).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 1346804730 | BUY | AMZN | 1 | LIMIT | 216.00 | GTC | NEW | 2026-11-01T18:06:33Z |
| 349985384 | BUY | AVGO | 1 | LIMIT | 266.00 | GTC | NEW | 2026-10-12T18:51:40Z |
| 349985387 | BUY | AVGO | 1 | LIMIT | 243.00 | GTC | NEW | 2026-10-12T18:51:56Z |
| 1907120509 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-09-30T20:06:06Z |
| 1206895879 | BUY | NFLX | 20 | LIMIT | 46.97 | GTC | NEW | 2026-10-03T16:45:08Z |
| 501912291 | SELL | NVDA Dec 18 '26 $125 Put (option, 1 contract) | 1 | LIMIT | 6.10 | GTC | NEW | 2026-11-12T16:26:30Z |

**Changes vs. 2026-11-08 sync:**
- **New:** SELL 1 NVDA Dec18'26 $125 put @ 6.10 (501912291, 2026-11-12) — opens a short put; no matching NVDA option position yet and no session/decision documents it (the [2026-11-12 NVDA rescore](../../sessions/2026-11-12-rescore-nvda.md) may be relevant — verify intent). Also a `REPLACED` SELL 5 NVO @ 45.54 (1458155116, 2026-11-13) with **no live successor**.
- **No longer present:** SELL 10 NVDA @ 200.50 (66340895), BUY 2 SNDK @ 780 (981278704), BUY 1 SNDK @ 800 (868411121) — none filled (NVDA went 40 → 50 sh; SNDK not held), so cancelled/expired.

**Carried-forward flags:**
- **⚠️ NVO:** the only NVO order (1458155116, SELL 5 @ 45.54) is `REPLACED` with no live successor — NVO has **no working sell order**.
- **⚠️ NKE:** no order of any kind appears in this fetch (the prior `REPLACED` sell is gone) — NKE has **no working sell order**.
- **Margin note:** USD cash is **-$12.95**; any BUY fill (NFLX ≈ $939, AVGO ×2 ≈ $509, AMZN ≈ $216) deepens the margin debit, and the NVDA short put (strike $125 × 100 = $12,500 notional) would add assignment exposure — run `/safe-guard`.
- **No order** exists for the BULL short put or the UUUU Jan'27 $9 short call.

> **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

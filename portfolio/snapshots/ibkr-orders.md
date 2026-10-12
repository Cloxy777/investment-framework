# IBKR Active Orders Snapshot

**Account:** U19421206 (framework account — see [accounts.md](../accounts.md))
**Last synced:** 2026-10-12 (live via Interactive Brokers MCP — `get_account_orders`, via manual `/sync-portfolio`)
**Active orders:** 8 working (status `NEW`) · 1 non-active order shown in this fetch (NKE `REPLACED`, excluded).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 123100566 | BUY | AVGO | 5 | LIMIT | 265.34 | GTC | NEW | 2026-09-28T14:18:51Z |
| 1907120507 | SELL | CSGP | 25 | LIMIT | 35.55 | GTC | NEW | 2026-09-30T20:05:30Z |
| 1907120509 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-09-30T20:06:06Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1206895879 | BUY | NFLX | 20 | LIMIT | 46.97 | GTC | NEW | 2026-10-03T16:45:08Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1462252282 | SELL | UUUU (OCT 16 '26 $8.50 Put, to open — no UUUU position held) | 3 | LIMIT | 0.03 | GTC | NEW | 2026-10-09T15:58:19Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

**Changes vs. 2026-10-11 sync:** none — identical order set (8 working `NEW`, NKE `REPLACED` excluded). No order references RGL, LM8 or TLT (transferred out in-kind to non-framework accounts, see [accounts.md](../accounts.md)). Carried-forward flags below remain open.

**Earlier flags (from 2026-10-04 → 2026-10-11 sync, still applicable):**
- **New order:** UUUU SELL 3 × OCT 16 '26 $8.50 Put @ 0.03 GTC (placed 2026-10-09) — no UUUU position or evaluation anywhere in the repo; selling 3 puts to open would be a ~$2,550 cash-secured/margin obligation if assigned. **Ungoverned — confirm intent.**
- **Filled/gone:** LM8 BUY 1800 @ 0.30 (343126638) — no longer listed; the order filled and the resulting 1,800-share LM8 position was later transferred out in-kind (no longer in this account).
- **⚠️ NKE:** the only NKE order in the fetch (1907120519, SELL 20 @ 54.44) is still `REPLACED` with no live successor — NKE has **no working sell order**. Worth a manual TWS/Client Portal check.
- **Unchanged:** AVGO BUY 5 @ 265.34, CSGP/GOOG sells, NFLX BUY 20 @ 46.97, and MA, NOW, V (placed 2026-07-05, still undocumented by sessions/decisions).
- **Still absent in any status:** SPOT SELL 1 @ 518 (934588780) and the TLT short call (1040104046) — the latter is now moot, since TLT was transferred out of this account. The new BULL short-put position (see [ibkr.md](ibkr.md)) has no corresponding order in this fetch.

> **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

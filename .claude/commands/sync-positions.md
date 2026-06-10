---
description: Sync live IBKR positions into this repo (snapshot section + holdings.md)
---

Follow the [IBKR Positions Sync](../../portfolio/sync-sop.md#ibkr-positions-sync) procedure in the [Portfolio Sync SOP](../../portfolio/sync-sop.md).

1. Fetch positions via `get_account_positions` (Interactive Brokers MCP, account U19421206).
2. Resolve tickers via the live ticker-lookup CSV (`https://www.interactivebrokers.com/download/fracshare_stk.csv`), falling back to [`portfolio/reference/ibkr-ticker-lookup.csv`](../../portfolio/reference/ibkr-ticker-lookup.csv) if unreachable — see the SOP for the exact fallback procedure.
3. Update the positions table and position-derived header fields (Gross Position Value, Unrealized P&L, "Positions last synced") in [`portfolio/snapshots/ibkr.md`](../../portfolio/snapshots/ibkr.md). Leave the Cash Balances table and cash-derived header fields untouched.
4. Refresh the ticker rows (weight %, broker) in [`holdings.md`](../../portfolio/holdings.md), using the Net Liquidation Value currently in `ibkr.md` (from the most recent `/sync-balances`) — note its date if it isn't from today.
5. Commit straight to `main`: stage `ibkr.md`, `holdings.md`, and the lookup CSV if refreshed, with the message `Sync IBKR positions — YYYY-MM-DD`.

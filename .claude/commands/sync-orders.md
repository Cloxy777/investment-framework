---
description: Sync current active/working IBKR orders into this repo (snapshot file)
---

Follow the [IBKR Active Orders Sync](../../portfolio/sync-sop.md#ibkr-active-orders-sync) procedure in the [Portfolio Sync SOP](../../portfolio/sync-sop.md).

1. Fetch all orders via `get_account_orders` (Interactive Brokers MCP, account U19421206).
2. Filter to orders that are still active/working (e.g. `NEW`, `SUBMITTED`, `PARTIALLY_FILLED`) — exclude `REPLACED`, `CANCELLED`, `FILLED`, `EXPIRED`, `INACTIVE`. If an unfamiliar status appears, ask rather than guessing.
3. Overwrite [`portfolio/snapshots/ibkr-orders.md`](../../portfolio/snapshots/ibkr-orders.md) with the active-orders table, a sync timestamp, and a flag for any ticker whose only order(s) are non-active with no live successor.
4. Push to a `claude/`-prefixed branch, commit with the message `Sync IBKR active orders — YYYY-MM-DD`, open a PR with that same title, and enable auto-merge (squash) on it — see [sync-sop.md](../../portfolio/sync-sop.md) for the rationale.

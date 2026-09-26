---
description: Sync current active/working IBKR orders into this repo (snapshot file)
---

Follow the [IBKR Active Orders Sync](../../portfolio/sync-sop.md#ibkr-active-orders-sync) procedure in the [Portfolio Sync SOP](../../portfolio/sync-sop.md).

1. Fetch all orders via `get_account_orders` (Interactive Brokers MCP, account U19421206) and dump the raw result to JSON — no standalone script can call this MCP tool.
2. Run `python -m scripts.sync_ibkr --orders <orders.json>` to filter to active/working orders (`NEW`, `SUBMITTED`, `PRESUBMITTED`, `PARTIALLY_FILLED`; excluding `REPLACED`, `CANCELLED`, `FILLED`, `EXPIRED`, `INACTIVE`) and render the active-orders table with counts, instead of hand-filtering. If it exits with `ERROR: Unfamiliar order status ...`, that's the same ask-rather-than-guess signal as before — stop and ask.
3. Overwrite [`portfolio/snapshots/ibkr-orders.md`](../../portfolio/snapshots/ibkr-orders.md) with the script's active-orders table, a sync timestamp, and a flag for any ticker whose only order(s) are non-active with no live successor (cross-check against the script's `excluded_count`/`excluded_orders`).
4. Push to a `claude/`-prefixed branch, commit with the message `Sync IBKR active orders — YYYY-MM-DD`, open a PR with that same title, and enable auto-merge (squash) on it — if that reports the PR already clean/mergeable with nothing pending, merge it directly (squash) instead — see [sync-sop.md](../../portfolio/sync-sop.md) for the rationale.

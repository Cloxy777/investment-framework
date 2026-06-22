---
description: Sync live IBKR cash balances into this repo (snapshot section + holdings.md)
---

Follow the [IBKR Cash Balances Sync](../../portfolio/sync-sop.md#ibkr-cash-balances-sync) procedure in the [Portfolio Sync SOP](../../portfolio/sync-sop.md).

1. Fetch cash balances via `get_account_balances` (Interactive Brokers MCP, account U19421206) — per-currency cash/settled cash/net liquidation/FX rate, plus the consolidated `BASE` row. Use the live `exchange_rate` for any FX conversion — never assume or look up a rate elsewhere.
2. Update the Cash Balances table and cash-derived header fields (Net Liquidation, Total Cash, "Cash balances last synced") in [`portfolio/snapshots/ibkr.md`](../../portfolio/snapshots/ibkr.md), including recomputing any non-USD position's USD-equivalent (e.g. XEON) from the live FX rate. Leave the positions table and position-derived header fields untouched.
3. Refresh [`holdings.md`](../../portfolio/holdings.md): the `CASH (IBKR)` row, and recompute weight % for every row (Net Liquidation Value — the shared denominator — just changed), using position market values from the most recent `/sync-positions` run — note its date if it isn't from today.
4. Push to a `claude/`-prefixed branch: stage `ibkr.md` and `holdings.md`, commit with the message `Sync IBKR cash balances — YYYY-MM-DD`, open a PR with that same title, and enable auto-merge (squash) on it — if that reports the PR already clean/mergeable with nothing pending, merge it directly (squash) instead (see sync-sop.md).

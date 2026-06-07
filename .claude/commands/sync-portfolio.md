---
description: Sync live broker positions into this repo (snapshot files + holdings.md)
---

Follow the [Portfolio Sync SOP](../../portfolio/sync-sop.md) for the broker(s) requested: $ARGUMENTS (if empty, ask "IBKR", "Freedom Finance", or "both").

- **IBKR** — fully automated via the Interactive Brokers MCP, plus a plain HTTP fetch of the ticker-lookup CSV from `https://www.interactivebrokers.com/download/fracshare_stk.csv` (falling back to the repo-stored copy at `portfolio/reference/ibkr-ticker-lookup.csv` if that's unreachable — see the SOP for the exact fallback procedure). No further input needed beyond confirming the account (U19421206).
- **Freedom Finance** — requires a screenshot of the Freedom24 portfolio from the user. Ask for one if not attached.

For each broker synced:
1. Overwrite the relevant snapshot file under [`portfolio/snapshots/`](../../portfolio/snapshots/) (`ibkr.md` or `freedom-finance.md`) with the freshly fetched positions and a sync timestamp.
2. Refresh the weight%/broker columns in [holdings.md](../../portfolio/holdings.md) from the new snapshot — leave the score/last-review columns alone (those belong to `/rescore`).
3. Commit both files on a branch named `sync/<broker>-YYYY-MM-DD` and open a PR titled `Sync <Broker> portfolio — YYYY-MM-DD` against `main` (it's protected — direct pushes will be rejected).

Snapshot files are overwritten in place each run — git history is the archive of past syncs, so don't create dated copies.

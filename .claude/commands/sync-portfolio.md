---
description: Sync live broker positions into this repo (snapshot files + holdings.md)
---

Follow the [Portfolio Sync SOP](../../portfolio/sync-sop.md) for the broker(s) requested: $ARGUMENTS (if empty, ask "IBKR", "Freedom Finance", or "both").

- **IBKR** — fully automated via the Interactive Brokers MCP, plus a plain HTTP fetch of the ticker-lookup CSV from `https://www.interactivebrokers.com/download/fracshare_stk.csv` (falling back to the repo-stored copy at `portfolio/reference/ibkr-ticker-lookup.csv` if that's unreachable — see the SOP for the exact fallback procedure). No further input needed beyond confirming the account (U19421206).
- **Freedom Finance** — requires a screenshot of the Freedom24 portfolio from the user. Ask for one if not attached.

For each broker synced:
1. Overwrite the relevant snapshot file under [`portfolio/snapshots/`](../../portfolio/snapshots/) (`ibkr.md` or `freedom-finance.md`) with the freshly fetched positions and a sync timestamp.
2. Refresh the weight%/broker columns in [holdings.md](../../portfolio/holdings.md) from the new snapshot — leave the score/last-review columns alone (those belong to `/rescore`).
3. Commit the changed files (snapshot, `holdings.md`, and the lookup CSV if refreshed) **directly to `main`** with the message `Sync <Broker> portfolio — YYYY-MM-DD`. No branch, no PR — sync commits are low-risk, frequent, data-only refreshes, and `main`'s branch protection isn't actually enforced on this private repo (it requires a paid GitHub plan). One clean commit is the audit trail; `git revert` is there if a sync ever needs undoing. (Framework/strategy changes are different — those still go through a branch + PR by convention. See [CLAUDE.md](../../CLAUDE.md).)

Snapshot files are overwritten in place each run — git history is the archive of past syncs, so don't create dated copies.

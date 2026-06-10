---
description: Full broker sync — IBKR (positions + cash balances + active orders) and/or Freedom Finance — into this repo (snapshot files + holdings.md)
---

Follow the [Portfolio Sync SOP](../../portfolio/sync-sop.md) for the broker(s) requested: $ARGUMENTS (if empty, ask "IBKR", "Freedom Finance", or "both").

- **IBKR** — run the [Full IBKR Sync](../../portfolio/sync-sop.md#full-ibkr-sync-sync-portfolio): all three granular IBKR syncs (`/sync-positions`, `/sync-balances`, `/sync-orders`) in one pass, fully automated via the Interactive Brokers MCP — `get_account_positions`, `get_account_balances` (per-currency cash with live FX rates — use this, never an assumed/looked-up rate, for non-USD conversions), and `get_account_orders`, plus a plain HTTP fetch of the ticker-lookup CSV from `https://www.interactivebrokers.com/download/fracshare_stk.csv` (falling back to the repo-stored copy at `portfolio/reference/ibkr-ticker-lookup.csv` if unreachable — see the SOP for the exact fallback procedure). No further input needed beyond confirming the account (U19421206). Refresh `holdings.md` once at the end (ticker weight%/broker columns + `CASH (IBKR)` row, leaving score/last-review columns alone — those belong to `/rescore`), then commit `ibkr.md`, `ibkr-orders.md`, `holdings.md`, and the lookup CSV if refreshed, in **one** commit `Sync IBKR portfolio — YYYY-MM-DD`.
- **Freedom Finance** — requires a screenshot of the Freedom24 *positions* view **and** a screenshot of the cash/balance view (e.g. the Accounts tab) — the positions view alone doesn't show cash. Ask for both if not attached; if cash can't be provided, sync positions only and flag cash as not captured (don't estimate it). Overwrite [`portfolio/snapshots/freedom-finance.md`](../../portfolio/snapshots/freedom-finance.md), refresh `holdings.md` (ticker rows + `CASH (Freedom24)` row), and commit separately: `Sync Freedom Finance portfolio — YYYY-MM-DD`.

If the user only wants one piece of the IBKR sync refreshed (e.g. *"just check my orders"* or *"how much cash do I have"*), use the relevant granular command (`/sync-positions`, `/sync-balances`, `/sync-orders`) instead of this one.

All commits go **directly to `main`** — no branch, no PR. Sync commits are low-risk, frequent, data-only refreshes, and `main`'s branch protection isn't actually enforced on this private repo (it requires a paid GitHub plan). One clean commit per sync is the audit trail; `git revert` is there if a sync ever needs undoing. (Framework/strategy changes are different — those still go through a branch + PR by convention. See [CLAUDE.md](../../CLAUDE.md).)

Snapshot files are overwritten in place each run — git history is the archive of past syncs, so don't create dated copies.

# Portfolio Snapshots

One file per broker — `ibkr.md` and `freedom-finance.md` — each **overwritten in place** on every sync (see [sync-sop.md](../sync-sop.md)). There's deliberately no dated-file pile-up: git history already preserves every prior snapshot (`git log -p -- portfolio/snapshots/ibkr.md`), so the working tree only ever needs to show the latest.

Each snapshot carries a header with the account and the sync timestamp, plus a full positions table. [holdings.md](../holdings.md) is refreshed from these immediately after each sync.

`ibkr-orders.md` is a separate snapshot of currently **active/working IBKR orders** (not positions) — refreshed via `/sync-orders` (see [sync-sop.md](../sync-sop.md#ibkr-active-orders-sync)). It does not feed into `holdings.md`.

---
description: Sync live broker positions into Notion (and refresh holdings.md)
---

Follow the [Portfolio Sync SOP](../../portfolio/sync-sop.md) for the broker(s) requested: $ARGUMENTS (if empty, ask "IBKR", "Freedom Finance", or "both").

- IBKR: fully automated via the Interactive Brokers + Google Drive + Notion MCPs — no further input needed beyond confirming the account (U19421206).
- Freedom Finance: requires a screenshot of the Freedom24 portfolio from the user — ask for one if not attached.

After the Notion sync completes, also update [holdings.md](../../portfolio/holdings.md) in this repo with the refreshed tickers/weights so `/rebalance` and `/rescore` have current data.

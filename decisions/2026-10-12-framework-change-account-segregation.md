# Framework change — segregate non-framework positions into separate IBKR accounts

**Date:** 2026-10-12 · **Type:** process / data-scope change (no scoring-methodology change — no stale-score run needed)

## What changed
- The framework now governs a **single IBKR account, `U19421206`**. Registry: [portfolio/accounts.md](../portfolio/accounts.md).
- The other two accounts are persisted but out of scope: **`U26777756` = Investment Supremacy channel**, **`U26777331` = Capitalization channel**. No modules, syncs, or holdings files exist for them.
- **RGL, LM8 and TLT** were moved out of `U19421206` by an **in-kind internal transfer** (not sales). Destination account per ticker is still to be confirmed in accounts.md.
- Sync/safe-guard/healthcheck/update-orders commands now name `U19421206` explicitly and link the registry. The sync SOP gained an *Account Scope & Guard* section.

## Why
Overrides and instrument-mismatch positions (ASX gold explorers, a long-bond ETF with no exit rules) diluted the denominator and the statistics. A clean account means weights, win rate, and the annual override review reflect only what the framework selects, sizes, and trims — and a new non-framework buy has a different place to live.

## Design decisions
- **The IBKR MCP tools take no account argument**, so "account parameter" is enforced as a **scope guard on the response** (known-transfer tickers must not appear; a mismatched echoed account ID stops the sync), not a call argument.
- **Transfers are not trades.** The weekly "undocumented trim" comparison skips the transferred tickers; `get_account_trades` rows for them around the transfer date are transfers, never realized P&L or an exit.
- **Realized P&L is never read by any sync** (only unrealized is stored), so IBKR's cosmetic "realized loss" from the transfer needs no special handling beyond the baseline date.
- **Statistics baseline: 2026-10-12.**
- First `/sync-portfolio` after the transfer must remove the RGL/LM8/TLT rows from `holdings.md` (the weight-patch script never deletes rows) and recompute all weights on the new Net Liquidation Value.

## Not in scope / open
- Which of the two non-framework accounts received each transferred ticker.
- Positions still in `U19421206` that the framework may not support (e.g. the short `BULL Feb19'27 $5` puts, quality-gate failures) — handled by normal `/rescore` / `/rebalance`, not by this change.

## Glossary
- **In-kind (free-of-payment) transfer** — shares moved between your own accounts without a sale; cost basis carries over. See [glossary.md](../framework/glossary.md).
- **Framework account** — the one account (`U19421206`) the framework governs. See [glossary.md](../framework/glossary.md).
- **NLV (Net Liquidation Value)** — account value, the denominator for weights.
- **Override** — a position entered outside the framework's rules.
- **Short put** — an option you sold; obliges you to buy shares at the strike if the stock falls below it.

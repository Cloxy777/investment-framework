# IBKR Account Registry

The single source of truth for **which IBKR account is which**. Every sync, scan, and order command reads its target account from here — never a hard-coded guess.

> **Today the framework governs exactly one account: `U19421206`.** The other two accounts are recorded so they're persisted and unambiguous, but **no framework module, sync, or command runs against them yet.**

| Account | Role | Governed by this framework? | Notes |
|---------|------|-----------------------------|-------|
| **U19421206** | **Framework account** — the Quality Value + Dynamic Trimming core portfolio | **Yes** — default and only account for every command | All weights, scores, statistics, `/safe-guard` margin math, and the override log refer to this account. |
| **U26777756** | **Investment Supremacy channel** account | No — persisted only | No syncs, no holdings file, no scoring. A future module may be added. |
| **U26777331** | **Capitalization channel** account | No — persisted only | No syncs, no holdings file, no scoring. A future module may be added. |

(The two channel accounts back the Investment Supremacy and Capitalization channels respectively; they hold positions the framework does not select, size, or trim.)

## Account parameter

Every IBKR-facing command takes an implicit **`account`** parameter, defaulting to **`U19421206`**. Other values are not supported by any command today.

**The IBKR MCP tools have no account argument** (`get_account_positions`, `get_account_balances`, `get_account_orders`, `get_account_trades`, `get_account_summary` take none — only the connector's OAuth consent decides what comes back). So the parameter is enforced as a **scope guard** on the response, not as a call argument:

1. Sanity-check the fetched data against [Known transfers out](#known-transfers-out-of-the-framework-account) below — none of those tickers should appear in the framework account's positions.
2. If a ticker listed there **does** appear, or the account ID echoed by the response (where present, e.g. `get_account_summary`) is not `U19421206`, the connector's scope has changed — **stop and ask**; do not write snapshots or `holdings.md`.

## Known transfers out of the framework account

Positions moved by the user via an **in-kind (free-of-payment) internal transfer** — **not sales, not exits, not trims.** They must not be flagged as "undocumented trims", must not count as realized P&L or an exit in any session/decision/statistic, and must not be re-added to `holdings.md`.

| Date | Ticker | Qty at transfer | Destination account | Why moved |
|------|--------|-----------------|---------------------|-----------|
| on/around 2026-10-12 | RGL (ASX gold explorer) | 60,000 | ⚠️ *to confirm* — one of U26777756 / U26777331 | Gold-miner exposure is not a framework instrument; keep framework statistics pure |
| on/around 2026-10-12 | LM8 (ASX gold miner) | 1,800 | ⚠️ *to confirm* — one of U26777756 / U26777331 | Same |
| on/around 2026-10-12 | TLT (not an equity — framework gap) | 100 | ⚠️ *to confirm* — one of U26777756 / U26777331 | Not an equity; framework had no exit rules for it |

Fill in the exact transfer date and each destination account when known. IBKR's own reports (Activity Statement, PortfolioAnalyst) may show these as realized losses or closing trades on the main account; treat that as a cosmetic artefact of the transfer — cost basis and holding period carry over with an in-kind transfer. See [decisions/2026-10-12-framework-change-account-segregation.md](../decisions/2026-10-12-framework-change-account-segregation.md).

**Framework statistics baseline: 2026-10-12 for position-level figures** (override-log comparisons, win rate: the post-transfer U19421206 portfolio is the population). **Account-level performance (TWR) is rebuilt back to 2025-10-13 with the three transferred positions removed from the whole history** — see [performance/README.md](performance/README.md) and `/performance`.

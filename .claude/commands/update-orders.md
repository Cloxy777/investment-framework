---
description: Turn a margin safe-guard grouping proposal into concrete manual TWS/Client Portal instructions for reorganizing active IBKR orders
---

Turn a proposed order regrouping — either supplied in `$ARGUMENTS` (usually pasted straight from a [`/safe-guard`](safe-guard.md) alert) or self-derived if `$ARGUMENTS` is empty — into a precise, manual, step-by-step instruction set for reorganizing active orders on account U19421206. **This command never touches a live broker order itself** — no MCP tool in this repo can place, modify, cancel, or group an IBKR order (confirmed: the Interactive Brokers connector exposes read/lookup tools only). Its entire output is a proposal for the human to execute by hand in TWS or Client Portal, exactly like every other command in this repo stops at a recommendation (see [automation-schedule.md](../../framework/automation-schedule.md), "no routine ever places a broker order").

## Argument grammar

```
GROUP-<name>: <TICKER>(<orderID>)+<TICKER>(<orderID>)+...; GROUP-<name>: ...
```

- Each `GROUP-<name>` becomes one **OCA (One-Cancels-All)** group — see [glossary.md](../../framework/glossary.md).
- Orders within a group are `+`-joined; groups are `;`-separated.
- An order not mentioned in any group is left as-is (ungrouped, unchanged).
- **If `$ARGUMENTS` is empty:** re-derive the grouping from scratch — run [`/safe-guard`](safe-guard.md) Steps 1–3 fresh (live orders + live cash balances), then apply its "Grouping algorithm" section to produce your own proposal before continuing below. Don't ask the user to re-run `/safe-guard` first; this command is self-contained.

## Step 1 — Re-validate against live state

Fetch `get_account_orders` fresh (never reuse a stale snapshot or the order IDs as typed without checking) and confirm every order ID referenced in the grouping plan is still active (`NEW`, `SUBMITTED`, `PRESUBMITTED`, `PARTIALLY_FILLED`). Since this command runs manual order-reorganization guidance for the **main portfolio**, accuracy here matters more than in a routine data sync — treat any mismatch as a stop-and-flag condition, not a guess:

- **Order ID no longer active** (filled, cancelled, replaced since the plan was generated): drop it from its group and say so explicitly — if that group now has 1 or 0 orders, dissolve it (an OCA group needs 2+ live orders to mean anything).
- **Order ID's price/qty changed** (a `REPLACED` order superseded it): flag the discrepancy, use the live current values, and note that the plan's original numbers are stale.
- **Order ID not found at all**: stop and ask — never assume which order was meant.

## Step 2 — Recompute worst-case exposure, before and after

Using [`/safe-guard`](safe-guard.md) Step 3's formulas exactly (same per-currency, non-netted, BUY-orders-only definition of worst case):

- **Before:** worst-case margin usage treating every order in the plan as fully independent (today's live state, ungrouped).
- **After:** worst-case margin usage applying the proposed OCA grouping — within each group, only the **largest** live order's notional counts toward the currency's BUY Notional (since an OCA fill cancels its siblings before they can also fill); every ungrouped order still counts in full.

Show both figures side by side, per currency and combined (USD-equivalent, using live FX rates from `get_account_balances` — never assumed). State plainly whether the "after" figure clears $5,000 (or whatever threshold prompted this run, if not the default).

**If "after" still exceeds $5,000:** say so — grouping alone caps exposure at the largest order in each group, it cannot reduce it below that. Suggest which specific order to cancel or downsize (by notional, largest first) to close the remaining gap, but do not treat that as part of the grouping instructions below (a cancellation/resize is a different, and more consequential, action than an OCA grouping and should be called out as a separate manual decision).

## Step 3 — Produce manual execution instructions

For each group, write an explicit, numbered checklist item, e.g.:

```
1. In TWS (or Client Portal → Orders), select order 652254171 (BUY 4 MA @ 464.00 LIMIT)
   and order 652254170 (BUY 9 V @ 285.20 LIMIT).
2. Right-click → Attach/Modify Order → set both orders' OCA Group to
   "SAFEGUARD-YYYY-MM-DD-A", OCA Type 1 (Cancel Block, reduces siblings' quantity
   only if a partial fill occurs — the standard choice for this use case unless the
   user specifies otherwise).
3. Confirm both orders now show the same OCA Group name in the Orders pane.
```

One such block per group, using real order IDs/tickers/prices/quantities from Step 1's re-validated live data — never the possibly-stale numbers from `$ARGUMENTS` alone. Name each OCA group `SAFEGUARD-YYYY-MM-DD-<letter>` for traceability back to the session log.

## Step 4 — Log it

Save `sessions/YYYY-MM-DD-update-orders.md` with: the grouping plan (as given or self-derived), Step 1's re-validation results (including anything dropped/flagged), the before/after worst-case comparison from Step 2, and the full manual checklist from Step 3. State explicitly at the top of the log: **"Proposal only — no order was placed, modified, or cancelled by this session. Nothing changes on IBKR until the steps above are carried out manually."**

Push the session log to a `claude/`-prefixed branch, commit `Update-orders: OCA regrouping proposal — YYYY-MM-DD`, and open a PR — leave it open for manual review (this is a proposal, not a data refresh, so no auto-merge, same as `/safe-guard`'s breach path). Do **not** touch `portfolio/snapshots/ibkr-orders.md` — the live orders haven't actually changed yet, so overwriting that snapshot here would make it wrong until the human actually executes the checklist and a real `/sync-orders` run picks up the result.

## What this command never does

- Never place, modify, cancel, or group a broker order itself.
- Never assume an order ID's current price/qty/status — always re-fetch live (Step 1).
- Never claim the exposure is fixed — only that a manual checklist exists to fix it; the session log and any GitHub issue this addresses (e.g. the `margin-safeguard`-labeled one from `/safe-guard`) stay open until the human confirms the checklist was carried out in TWS/Client Portal and a subsequent `/safe-guard` run confirms the worst case actually dropped.

**Proposal only — no order was placed, modified, or cancelled by this session. Nothing changes on IBKR until the steps below are carried out manually.**

# Update-Orders — OCA Regrouping Proposal — 2026-07-05

**Account:** U19421206
**Source:** [`/safe-guard`](../.claude/commands/safe-guard.md) breach alert, [sessions/2026-07-05-safe-guard.md](2026-07-05-safe-guard.md) / [issue #176](https://github.com/Cloxy777/investment-framework/issues/176)
**Grouping plan as supplied:** `GROUP-A: V(652254170)+MA(652254171)+NOW(1423738919)`

## Step 1 — Live re-validation

Fetched `get_account_orders` and `get_account_balances` fresh (not reused from the safe-guard run). All three order IDs re-confirmed active and unchanged:

| Order ID | Ticker | Status | Qty | Limit Price |
|----------|--------|--------|-----|--------------|
| 652254170 | V | NEW | 9 | 285.20 |
| 652254171 | MA | NEW | 4 | 464.00 |
| 1423738919 | NOW | NEW | 20 | 80.00 |

No discrepancies — no order dropped, no stale price/qty, no group dissolved.

## Step 2 — Before / after worst-case

Same formulas as [`/safe-guard`](../.claude/commands/safe-guard.md) Step 3 (per-currency, non-netted, BUY-orders-only). Live cash: USD $103.69, AUD −$31.07 (FX 0.6938792), EUR $227.49, GBP $0.28 — all unchanged since the safe-guard run minutes earlier.

| | BUY Notional (USD) | Available Cash (USD) | Margin Usage (USD) |
|---|---|---|---|
| **Before** (all 6 USD BUY orders independent) | 7,878.99 | 103.69 | **7,775.30** |
| **After** (GROUP-A caps to largest = V $2,566.80; PDD/META/META ungrouped) | 4,422.99 | 103.69 | **4,319.30** |

AUD margin usage ($21.56 equiv, pre-existing negative cash, not order-driven) is unaffected by grouping in either scenario.

**Total before: $7,796.86 → Total after: $4,340.86** — clears the $5,000 threshold.

## Step 3 — Manual execution checklist

```
1. In TWS (or Client Portal → Orders), select order 652254170
   (BUY 9 V @ 285.20 LIMIT, GTC) and order 652254171
   (BUY 4 MA @ 464.00 LIMIT, GTC) and order 1423738919
   (BUY 20 NOW @ 80.00 LIMIT, GTC).
2. Right-click each → Attach/Modify Order → set OCA Group to
   "SAFEGUARD-2026-07-05-A", OCA Type 1 (Cancel Block — reduces
   siblings' quantity only on a partial fill, the standard choice
   here unless you want a different type).
3. Confirm all three orders show OCA Group "SAFEGUARD-2026-07-05-A"
   in the Orders pane before closing TWS/Client Portal.
```

PDD (1150965513) and both META BUY orders (21429034, 21429036) are left ungrouped/unchanged — no action needed on them.

RGL (630395618, `PENDING_CANCEL_REPLACE`) and HDSN (569919342, `PENDING_NEW`) were excluded from the underlying Safe-Guard calc and are not part of this grouping proposal either way.

## Status

Issue #176 (`margin-safeguard`) stays open until the checklist above is executed in TWS/Client Portal and a subsequent `/safe-guard` run confirms the worst case actually dropped below threshold.

## Glossary

- **OCA (One-Cancels-All)** — a broker order group where one order filling automatically cancels the others in the group, so only the largest live order in a group can draw cash in the worst case.
- **OCA Type 1 (Cancel Block)** — an OCA variant where a partial fill on one order proportionally reduces the remaining quantity of its siblings rather than cancelling them outright.
- **Margin** — borrowing from the broker to cover a purchase exceeding available cash.
- **Notional** — total dollar value of an order: quantity × price.
- **GTC** — Good-Til-Cancelled.

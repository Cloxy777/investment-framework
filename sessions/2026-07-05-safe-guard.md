# Margin Safe-Guard — 2026-07-05

**Account:** U19421206
**Trigger:** manual `/safe-guard` invocation (not the scheduled Routine 8)
**Data pulled live:** `get_account_orders`, `get_account_balances` (both fetched fresh this session, not from `portfolio/snapshots/ibkr-orders.md`)

## Worst-case definition

Every active BUY order fills; no active SELL order fills to offset it (a SELL might not fill at all, or on a different day, so it can't be relied on for cash in the same window). SELL orders are excluded from the draw calculation entirely. Calculation is **per-currency, non-netted** — a cash surplus in one currency is never assumed to cover a shortfall in another.

## Unfamiliar order statuses — resolved with user

Two active orders carried statuses outside Safe-Guard's known set (`NEW`/`SUBMITTED`/`PRESUBMITTED`/`PARTIALLY_FILLED` vs. `REPLACED`/`CANCELLED`/`FILLED`/`EXPIRED`/`INACTIVE`):

| Order ID | Ticker | Status | Qty remaining | Price | Notional |
|----------|--------|--------|----------------|-------|----------|
| 630395618 | RGL (RiversGold Ltd, ASX) | `PENDING_CANCEL_REPLACE` | 57,214 | AUD 0.011 | ~AUD 629 |
| 569919342 | HDSN (Hudson Technologies, NASDAQ) | `PENDING_NEW` | 200 | USD 4.96 | ~USD 992 |

Per Rule 0 (never guess), asked the user how to treat these. **Decision: exclude both** from the worst-case BUY calculation this run (treated like `REPLACED`/in-transition, not confirmed-live). Flagging for a future Safe-Guard revision: define these two statuses explicitly rather than re-asking each run.

## Step 3 — Per-currency worst-case table

Active BUY orders included (status `NEW`, fixed limit price, RGL/HDSN excluded per above):

| Order ID | Ticker | Qty | Limit Price | Currency | Notional |
|----------|--------|-----|--------------|----------|----------|
| 652254170 | V | 9 | 285.20 | USD | 2,566.80 |
| 652254171 | MA | 4 | 464.00 | USD | 1,856.00 |
| 1423738919 | NOW | 20 | 80.00 | USD | 1,600.00 |
| 1150965513 | PDD | 10 | 72.55 | USD | 725.50 |
| 21429034 | META | 1 | 579.85 | USD | 579.85 |
| 21429036 | META | 1 | 550.84 | USD | 550.84 |

(Excluded as non-active/non-BUY: CSGP SELL `REPLACED`, TLT BUY `REPLACED`, NKE SELL `NEW`, SPOT SELL `NEW`, GOOG SELL `NEW`, TRN BUY `REPLACED`, RGL BUY `PENDING_CANCEL_REPLACE`, HDSN BUY `PENDING_NEW`, META SELL ×2 `NEW`.)

| Currency | BUY Notional | Available Cash (live) | Shortfall | Margin Usage (USD) |
|----------|--------------|------------------------|-----------|---------------------|
| USD | 7,878.99 | 103.69 | 7,775.30 | **7,775.30** |
| AUD | 0.00 | −31.07 | 31.07 | **21.56** (× live FX 0.6938792) |
| EUR | 0.00 | 227.49 | −227.49 | 0.00 |
| GBP | 0.00 | 0.28 | −0.28 | 0.00 |

Note on the AUD line: not driven by any active BUY order — it's the pre-existing negative AUD cash balance (already-in-use margin) that Step 3 counts regardless of orders in that currency. Grouping cannot fix it (no order to group); it's small (~$21.56) and unrelated to today's breach driver.

**Total Potential Margin Usage (USD) = $7,775.30 + $21.56 = $7,796.86**

## Step 4 — Threshold comparison

$7,796.86 > $5,000 threshold → **BREACH**

## Grouping proposal (USD, the breaching currency)

Contributing BUY orders, sorted by notional descending: V (2,566.80) → MA (1,856.00) → NOW (1,600.00) → PDD (725.50) → META 21429034 (579.85) → META 21429036 (550.84). Available Cash (USD) = 103.69.

1. Merge V + MA → Group A. Capped worst case = 2,566.80 (largest) + remaining ungrouped (NOW+PDD+META+META = 3,456.19) − 103.69 = **5,919.30** (still over $5,000).
2. Merge NOW into Group A (next-largest order, merged into the group with the current largest capped contribution — reduces the total; starting a new single-order group would not). Group A = {V, MA, NOW}, largest = 2,566.80. Capped worst case = 2,566.80 + (PDD+META+META = 1,856.19) − 103.69 = **4,319.30** ≤ $5,000. Stop.

Recomputed total under this grouping: $4,319.30 (USD orders) + $21.56 (AUD, ungrouped/unrelated) = **$4,340.86** ≤ $5,000.

**Suggested `/update-orders` invocation:**

```
/update-orders GROUP-A: V(652254170)+MA(652254171)+NOW(1423738919)
```

(PDD and the two META BUY orders stay standalone — no grouping needed once Group A caps the total under threshold.)

## Actions taken

- GitHub issue opened: labeled `margin-safeguard` — see link below.
- Telegram alert and `.ics` **not sent**: `TELEGRAM_BOT_TOKEN`/`TELEGRAM_CHAT_ID` are not set in this interactive session (they live on the scheduled `investment-automation` cloud environment per [automation-schedule.md](../framework/automation-schedule.md), not this worktree). Flagged to the user directly instead.
- This session log + PR is the audit record per Rule 10.

## Glossary

- **Margin** — borrowing from the broker to cover a purchase that exceeds available cash; incurs interest and risk of a margin call.
- **Worst-case exposure** — the maximum plausible simultaneous cash draw, assuming every resting BUY order fills at once with no offsetting SELL fill.
- **OCA (One-Cancels-All)** — a broker order group where one order filling automatically cancels the others in the group, so only the largest live order in a group can draw cash.
- **Notional** — the total dollar (or other currency) value of an order: quantity × price.
- **GTC** — Good-Til-Cancelled, an order that stays active until filled or manually cancelled.
- **FX rate** — foreign exchange rate, used to convert a non-USD balance/exposure into USD for comparison against the $5,000 threshold.

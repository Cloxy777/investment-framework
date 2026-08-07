# scripts/ibkr/

Standalone scripts that touch the **live** IBKR account (U19421206). Nothing
here is invoked by Claude or by any repo routine/skill — `/update-orders`
still only ever produces a manual checklist (see
[`.claude/commands/update-orders.md`](../../.claude/commands/update-orders.md)).
These scripts exist for the account owner to run by hand, under their own TWS
/ IB Gateway session, when they've decided to act on a `/update-orders`
proposal via the API instead of clicking through TWS manually.

## update_orders_execute.py

Takes the same `GROUP-<name>: <TICKER>(<orderID>)+...` grouping syntax as
`/update-orders` and sets the OCA group on the specified **live** orders in
place (a modify, not a cancel+recreate — TWS API supports changing an
existing order's `ocaGroup`/`ocaType` directly).

**Setup**

1. `pip install ib_insync`
2. Run TWS or IB Gateway, log in, enable API access (Configure → API →
   Settings → Enable ActiveX and Socket Clients).
3. Set the API client ID to master (`0`) if you want the script to see and
   modify orders placed from other sessions/manually in TWS — otherwise it
   will only see orders placed by client ID matching `--client-id`.

**Usage**

```
# Dry run (default) -- prints the plan, touches nothing
python update_orders_execute.py "GROUP-A: V(652254170)+MA(652254171)+NOW(1423738919)"

# Actually apply it (after NYSE regular session has closed)
python update_orders_execute.py "GROUP-A: V(652254170)+MA(652254171)+NOW(1423738919)" --execute
```

Refuses to `--execute` while NYSE is in its regular trading session (checked
live via IBKR contract details on SPY, not a hardcoded holiday calendar) —
pass `--skip-market-check` to override, e.g. for paper-account testing.

**What it checks before touching anything**

- Every order ID in the grouping spec is still active and visible to the API
  session.
- Each order's live ticker matches what was specified (stops on mismatch
  rather than guessing).
- Each order is a `BUY` (this tool only groups BUY orders, matching
  `/safe-guard`'s worst-case model — grouping a SELL wouldn't reduce
  cash-draw risk).

**What it does not do**

- Does not cancel or create orders — an OCA-group assignment is a modify of
  the existing order.
- Does not decide sizing, pricing, or which tickers to buy — it only applies
  a grouping you already decided on (typically pasted from a `/safe-guard`
  alert or a `/update-orders` proposal).

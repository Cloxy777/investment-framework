---
description: Check worst-case simultaneous-fill margin exposure from active IBKR orders against current cash; alert if it exceeds $5,000
---

Run a MARGIN SAFE-GUARD check for account U19421206. No arguments. This command is deliberately modeled on [`/healthcheck`](healthcheck.md)'s minimalism: **quiet when exposure is within limits, loud (Telegram + GitHub issue) when it isn't.** It never places, modifies, or cancels a broker order — no such capability exists in this repo (see [automation-schedule.md](../../framework/automation-schedule.md), "no routine ever places a broker order"); it only measures risk and, if needed, hands a concrete regrouping proposal to [`/update-orders`](update-orders.md) for the human to execute manually in TWS/Client Portal.

## Why this exists

Every active BUY limit order is a live promise to spend cash the instant the market reaches its price. Resting several BUY orders at once is normal, but if the market gapped down hard enough for *all* of them to fill the same day, the account could owe far more cash than it actually holds — forcing margin borrowing. `holdings.md`/`ibkr.md` already show this account letting a currency balance go negative once before (the TRN GBP fill). This command quantifies that risk **before** it happens, using live data, and flags it while it's still fixable by rearranging resting orders — not after a fill.

## Step 1 — Fetch live orders

Fetch all orders via `get_account_orders` (Interactive Brokers MCP, account U19421206) and filter to active/working orders exactly as [`/sync-orders`](sync-orders.md) does: keep `NEW`, `SUBMITTED`, `PRESUBMITTED`, `PARTIALLY_FILLED`; exclude `REPLACED`, `CANCELLED`, `FILLED`, `EXPIRED`, `INACTIVE`. If an unfamiliar status appears, ask rather than guessing. **Always pull live** — do not reuse `portfolio/snapshots/ibkr-orders.md`, even if it looks fresh; a margin check is only as good as its most recent data.

For every active order, record: order ID, side, ticker, quantity, order type, limit/stop price, currency, time in force. **If any active order has no fixed price** (e.g. a `MARKET` order) — flag it explicitly as an unbounded worst-case contributor and say so in the output; never invent a price for it (Rule 0, CLAUDE.md).

## Step 2 — Fetch live cash balances

Fetch `get_account_balances` (Interactive Brokers MCP) for the per-currency cash balances and the broker-reported live FX rates (`exchange_rate` field) — never assume or look up a rate elsewhere, per Rule 0. Record `cash_balance` for every currency the account holds, including currencies with **no** active orders (they still count as available cash if a shortfall elsewhere could theoretically be covered by another currency — but see the netting rule below, this framework does not assume that).

## Step 3 — Define and compute the worst-case scenario

**Definition (show this explicitly in the output so it's never re-derived ambiguously):** the worst case assumes every active BUY order fills, and no active SELL order fills to offset it — a SELL might not fill at all, or might fill on a different day, so it cannot be relied on to provide cash in the same worst-case window. SELL orders are therefore excluded from the draw calculation entirely. This is a **per-currency, non-netted** calculation — margin used in one currency is not assumed to be covered by a cash surplus in another (matching how `ibkr.md` already tracks the GBP cash balance as its own line, independent of the USD/EUR balances).

For each currency `C` that appears among active BUY orders or held cash:

```
BUY Notional(C)      = Σ (qty × limit/stop price) over active BUY orders in C
Available Cash(C)    = live cash_balance for C from get_account_balances
                        (may already be negative — i.e. margin already in use)
Shortfall(C)         = BUY Notional(C) − Available Cash(C)
Margin Usage(C)      = max(0, Shortfall(C))
Margin Usage(C, USD) = Margin Usage(C) × live exchange_rate for C
```

```
Total Potential Margin Usage (USD) = Σ over all currencies C of Margin Usage(C, USD)
```

Show a full table — one row per currency: BUY Notional, Available Cash, Shortfall, Margin Usage (USD) — plus, for every currency with `Margin Usage(C) > 0`, the list of contributing active BUY orders (ticker, order ID, qty, price, notional), sorted by notional descending. This ordering is what Step 5's grouping proposal uses.

## Step 4 — Compare to the $5,000 threshold

**Threshold: $5,000 USD**, fixed. Compare `Total Potential Margin Usage (USD)` from Step 3 against it.

### Pass ($5,000 or under)

Print a single confirmation line and stop — no file write, no commit, no PR, no Telegram message, mirroring `/healthcheck`'s "quiet on a clean run" design:

```
Safe-Guard YYYY-MM-DD: worst-case margin exposure $X,XXX.XX across N active BUY orders — within the $5,000 threshold.
```

If an open GitHub issue labeled `margin-safeguard` exists from a previous breach, add one "resolved" comment with today's figures and close it.

### Breach (over $5,000)

1. **Compute a suggested OCA grouping** — see "Grouping algorithm" below. This is the parameter set the Telegram message and the GitHub issue will both hand to `/update-orders`.
2. **Open or update a GitHub issue** labeled `margin-safeguard` (create the label first if it doesn't exist). No open issue found → create one titled `Margin Safe-Guard: worst-case exposure $X,XXX exceeds $5,000 threshold — YYYY-MM-DD` containing: the full per-currency table from Step 3, the contributing BUY orders, current cash position, the suggested grouping, and the exact `/update-orders` invocation to run (see below). Open issue already exists → don't duplicate; add a dated comment with today's figures and note what changed since the last comment.
3. **Send a Telegram message** prefixed `‼️ IMPORTANT ‼️` with the full description — total potential margin exposure, the per-currency breakdown, the top contributing BUY orders, and the exact suggested `/update-orders` command (see below):
   `curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" -d chat_id="${TELEGRAM_CHAT_ID}" -d parse_mode="Markdown" --data-urlencode text="‼️ IMPORTANT ‼️ ..."`
4. **Priority tier:** this is a whole-portfolio, capital-at-risk trigger — **P1** per [automation-schedule.md](../../framework/automation-schedule.md)'s Priority rule (due next business day, 13:30 UTC, before US open). Write a single-event `.ics` (`action-margin-safeguard.ics`: SUMMARY = the issue title, DESCRIPTION = the issue URL) and send it via `sendDocument`, same pattern as every other routine's action items.
5. **Save a session log** at `sessions/YYYY-MM-DD-safe-guard.md` with the full Step 3 table, the grouping proposal, and links to the issue/`.ics` — this is the audit record (Rule 10). Push it to a `claude/`-prefixed branch, commit `Safe-Guard: margin exposure alert — YYYY-MM-DD`, open a PR, and leave it open for manual review (like Routines 1/3/4/5 — this is a proposal, not a data refresh, so no auto-merge).

## Grouping algorithm (used by Step 4's breach path)

Goal: propose **OCA (One-Cancels-All)** groupings among the active BUY orders so that, once applied, the worst case can no longer sum every order in a currency — only the single largest live order in each OCA group counts, since an OCA fill cancels its siblings.

For each currency with `Margin Usage(C) > 0`, working from the contributing-orders list (sorted by notional descending, from Step 3):

1. Start with every contributing BUY order ungrouped.
2. Greedily merge the two largest remaining ungrouped orders into a new group. Recompute that currency's **capped worst case** = (sum of the largest order in each group so far, plus every still-ungrouped order's own notional) − Available Cash(C), converted to USD.
3. Repeat step 2 (merge the next-largest remaining order into the group with the current largest capped contribution, or start a new group if that reduces the total more) until `Total Potential Margin Usage (USD)` recomputed under the proposed grouping is ≤ $5,000, or until every contributing order in that currency is in one single group.
4. **If a single OCA group covering every contributing order in a currency still leaves that currency's capped worst case over $5,000** (i.e., the largest single order's notional alone, netted against available cash, already exceeds the per-currency share of the threshold), grouping alone cannot fix it — say so explicitly and additionally suggest cancelling or reducing the size of that largest order as the only remaining lever.

Express the result as the exact argument to pass to `/update-orders`, e.g.:

```
/update-orders GROUP-A: MA(652254171)+V(652254170); GROUP-B: NOW(1423738919)
```

(ticker + order ID pairs, `+`-joined within a group, `;`-separated between groups — see [`update-orders.md`](update-orders.md) for the full grammar). Include this literal command in both the GitHub issue and the Telegram message so the user can run it directly.

## What this command never does

- Never place, modify, cancel, or resize a broker order itself — no MCP tool in this repo can do that (confirmed: the Interactive Brokers connector exposes only read/lookup tools). Every fix happens by hand in TWS/Client Portal, guided by `/update-orders`'s output.
- Never treat a SELL order as reducing worst-case exposure (Step 3).
- Never estimate an FX rate or a missing order price — flag the gap and ask (Rule 0, CLAUDE.md).

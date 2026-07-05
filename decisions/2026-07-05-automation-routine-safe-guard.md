# 2026-07-05 — Automation: add `/safe-guard`, `/update-orders`, and Routine 8 (Margin Safe-Guard)

**What changed:**

Added two new commands and a new daily Routine:

- [`.claude/commands/safe-guard.md`](../.claude/commands/safe-guard.md) — `/safe-guard`, no parameters. Pulls live active orders (`get_account_orders`) and live cash balances (`get_account_balances`) for account U19421206, and computes the **worst-case simultaneous-fill margin exposure**: assumes every active BUY order fills, assumes no offsetting SELL fill happens at the same time, and does not net a shortfall in one currency against a surplus in another (matching how `ibkr.md` already tracks the GBP cash balance as its own line item). If the resulting USD-equivalent exposure exceeds **$5,000**, it opens/updates a `margin-safeguard`-labeled GitHub issue and sends a `‼️ IMPORTANT ‼️` Telegram alert with the full per-currency breakdown and a concrete OCA-grouping proposal, expressed as the exact `/update-orders` command to run. Modeled on `/healthcheck`'s minimalism — silent on a clean day, loud only when the threshold is actually crossed.
- [`.claude/commands/update-orders.md`](../.claude/commands/update-orders.md) — `/update-orders [grouping]`. Turns a grouping proposal (from a `/safe-guard` alert, or self-derived if no argument is given) into a precise manual checklist for setting up **OCA (One-Cancels-All)** order groups in TWS/Client Portal — grouping resting BUY orders that compete for the same cash so that only the largest order in each group counts toward the worst case once one of them fills. Re-validates every referenced order ID against live state first (an order may have filled or been replaced since the proposal was generated) and shows a before/after worst-case comparison.
- **Routine 8** in [automation-schedule.md](../framework/automation-schedule.md) — runs `/safe-guard` daily, ahead of US market open.

**Why:**

This account already has a documented precedent for accidental margin usage: the TRN buy (see `ibkr.md`, `holdings.md`) was funded by letting the GBP cash balance go negative rather than a deliberate FX conversion. That was a single fill after the fact. The bigger, still-open risk is *upstream* of any single fill: several BUY limit orders can sit active at once (the current book, per `ibkr-orders.md`, has both `BUY MA` and `BUY V` and `BUY NOW` resting simultaneously), and a hard gap-down could fill several of them the same day, drawing far more cash at once than the account holds — forcing margin borrowing nobody explicitly decided to take on. Nothing in this repo previously measured that *combined* exposure before it happened; `/sync-orders` only records what's active, it doesn't evaluate what would happen if all of it filled together.

**Design choices:**

- **No routine ever places a broker order — this one is no exception.** The Interactive Brokers MCP connector available in this repo exposes read/lookup tools only (`get_account_orders`, `get_account_balances`, price/contract lookups, etc.) — there is no tool to place, modify, cancel, or group an order. `/safe-guard` only measures and alerts; `/update-orders` only produces a manual TWS/Client Portal checklist. Both commands say this explicitly and repeatedly, since the whole point of this addition is *reducing* uncontrolled risk, not adding a new automated way to touch live orders.
- **Worst case is defined once, precisely, and reused.** "Every active BUY fills, no SELL offsets it, no cross-currency netting" is stated in `safe-guard.md` and reused verbatim by `update-orders.md`'s before/after comparison — a margin check that redefined "worst case" slightly differently each run would be worse than not having one, per CLAUDE.md's "show every calculation, no black-box outputs" principle.
- **$5,000 threshold, fixed.** Matches the user's explicit instruction; not tied to portfolio weight or NLV percentage, since the risk here is an absolute cash/borrowing amount, not a position-sizing question (that's what Upgrade 7's 15% cap and Phase 03 sizing already govern).
- **OCA groups, not order cancellation, as the default remedy.** The user asked specifically for orders to be "grouped... to minimize potential margin" — IBKR's OCA (One-Cancels-All) feature is the direct mechanism for that: once one order in a group fills, its siblings are auto-cancelled, capping the group's contribution to the worst case at its largest member instead of the sum of all of them. `update-orders.md` calls out explicitly when grouping alone can't clear the threshold (the largest single order in a fully-grouped currency still exceeds it) and only then suggests cancellation/resizing as a distinct, more consequential decision.
- **Daily cadence, not weekly.** Orders can be placed or repriced any trading day; tying this check to Routine 2's weekly sync would leave most of the week uncovered for the exact risk (a same-day gap-down filling several resting orders) this command exists to catch.
- **Breach path leaves its PR open, no auto-merge** — same reasoning as Routines 1/3/4/5: a margin exposure finding is a proposal for human judgment, not a mechanical data refresh, so it isn't safe to rubber-stamp merge the way a positions/balances snapshot sync is.

**Files touched:**
- `.claude/commands/safe-guard.md` — new command
- `.claude/commands/update-orders.md` — new command
- `CLAUDE.md` — added both commands to the "Routine tasks → slash commands" list
- `framework/automation-schedule.md` — added Routine 8 (prompt, cadence, environment), a coverage-map row, and updated the routine count in the intro and one-time-setup section
- `framework/glossary.md` — added the **OCA (One-Cancels-All) group** term

**Not touched:** `portfolio/calendar/investment-routine-schedule.ics` — like Routine 6's hourly cadence, a daily check that's silent on the common case doesn't map cleanly onto a static cadence-overview calendar; its visibility comes from the per-action `.ics` a breach sends, same pattern as Routine 7.

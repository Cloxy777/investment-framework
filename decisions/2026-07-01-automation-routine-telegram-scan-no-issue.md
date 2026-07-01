# 2026-07-01 — Framework change: Routine 6 stops opening GitHub issues

**What changed:**

`/telegram-scan` (Routine 6) no longer opens or updates a GitHub issue for
any run, fired or quiet. Previously (per the 2026-06-21 design), a quiet run
already skipped the issue, but any run where a ticker got actioned or a data
gap was flagged opened a new issue titled "Telegram Scan - YYYY-MM-DD HHUTC".
That per-run issue is now dropped entirely — the record of what fired lives
in telegram-watch.md's mention log, the ticker's own committed session/PR,
and the run's Telegram alert.

**Why:**

The user asked to stop GitHub issue creation from this routine. Reason: with
an hourly cadence, any day with several genuine mentions produced several
separate issues (one per firing hour), each a thin wrapper around commit
links the PR and Telegram message already carry — more issue-list noise than
the daily/weekly routines (1–5) generate, without adding information the
other two channels don't already have.

**What's unchanged:**
- Routines 1, 3, 4, 5 still open/update GitHub issues exactly as before —
  this change is scoped to Routine 6 only.
- The branch + PR + auto-merge landing mechanism for Routine 6's commits
  (per [decisions/2026-06-22-automation-routine-auto-merge-fallback.md](2026-06-22-automation-routine-auto-merge-fallback.md)).
- The per-action `.ics` + Telegram alert for any BUY/TRIM/EXIT-grade outcome.
- Quiet-run behavior (no issue, no Telegram ping — unchanged from the
  original design).
- No routine ever places a broker order.

**Files touched:**
- `.claude/commands/telegram-scan.md` — removed the "open or update a GitHub
  issue" instruction from the unattended-run note.
- `framework/automation-schedule.md` — Routine 6 prompt step 2 (issue →
  mention-log + Telegram alert only), step 4 (message links to session/PR,
  not an issue), and the routine's "Success" criterion.

**Related:** [decisions/2026-06-21-automation-routine-telegram-scan.md](2026-06-21-automation-routine-telegram-scan.md) (original Routine 6 design, including the quiet-run no-issue rule this change extends to all runs).

# 2026-07-07 — Fix: Monthly Rebalance routine firing every day 1st–7th, not just first Monday

## What happened

Routine 5 (Monthly Rebalance / Trim Review) was configured with cron
`30 12 1-7 * 1` intending "first Monday of the month." Standard cron
semantics OR the day-of-month and day-of-week fields when both are
restricted (neither is `*`) — so this expression actually matched day-of-month
1-7 **or** any Monday, i.e. it fired every single day from the 1st through
the 7th regardless of weekday. Confirmed by the session log: rebalance
sessions were committed on both 2026-07-05 and 2026-07-06 (see
[sessions/2026-07-05-rebalance.md](../sessions/2026-07-05-rebalance.md) /
commit `e0e78e4`, and the 2026-07-06 session / commit `aed41f9`).

## Fix

- Cron changed to `30 12 1-7 * *` — day-of-month 1-7 only, weekday field
  left wildcard, so no OR-ambiguity.
- Added Step 0 to Routine 5's prompt in
  [framework/automation-schedule.md](../framework/automation-schedule.md):
  the routine now checks today's weekday itself and exits immediately
  (no commit/PR/issue/Telegram) unless today is Monday. It also checks
  for an existing "Monthly Rebalance - YYYY-MM" issue this month as a
  belt-and-suspenders re-run guard.
- This must be re-pasted into the live Routine 5 configuration at
  claude.ai/code/routines — editing the repo doc alone does not change
  what's already scheduled (per automation-schedule.md's own caveat).

## Why

Cron has no native "Nth weekday of month" field; the day-of-month +
day-of-week combination is a common trap because most cron
implementations treat it as OR, not AND. The prompt-level weekday check
is the standard workaround and is now documented so it isn't silently
reintroduced on a future edit to this routine.

## Glossary

- **Cron** — a scheduling syntax (`minute hour day-of-month month
  day-of-week`) used to trigger recurring automated jobs at fixed times.
- **Routine** — a saved prompt + repo + environment + schedule, run by
  Claude Code automatically (see framework/automation-schedule.md).

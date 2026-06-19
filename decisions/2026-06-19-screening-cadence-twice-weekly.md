# 2026-06-19 — Framework change: Routine 4 screening cadence, monthly → twice weekly

**What changed:**

Routine 4 (Universe Screening Slice) moves from once a month (first Saturday) to **twice a week — Tuesday and Saturday, 14:00 UTC**. Each run still screens exactly one rotation-matrix slice from [screening-coverage-log.md](../framework/screening-coverage-log.md), self-selected as the least-recently-covered row, per the unchanged logic in `.claude/commands/screen.md`.

**Why:**

The SGE evaluation on 2026-06-19 surfaced that the EU slice (and JP, NA-2) had never been screened, even though three `/screen` sessions had already run — the gap was rotation *speed*, not the slicing design itself (see the same-day conversation that preceded this change). At the prior monthly cadence, one full pass through the 6-row coverage matrix took up to a year. At twice weekly, one full pass takes ~3 weeks, so EU/JP/NA-2 clear within the first month and the rest of the year is free for re-runs if a rate-regime shift or sector re-rating makes a slice's qualified set stale.

**Cost constraint:** the user is on a Claude Pro plan and wants screening to stay under ~50% of their weekly usage budget. Anthropic does not publish exact weekly token quotas (Pro is only specified as a relative "1x" multiplier vs. Max's 5x/20x — see [Claude Code Usage Limits 2026](https://www.morphllm.com/claude-code-usage-limits)), so this cadence is a starting point, not a number derived from a published cap. The session prompt was changed to make explicit that each run screens **exactly one slice** (the 2026-06-14 session had run two slices in a single sitting), keeping each run's cost bounded and comparable rather than variable. The user should check Settings → Usage at claude.ai after a few twice-weekly runs and adjust the cadence (more or less frequent) based on actual observed consumption.

**What's unchanged:** the screening methodology (Steps 0–5 of `screen.md`), the coverage-log update mechanics, the PR/issue/Telegram reporting, and the P4 priority tier's due-date math (5 business days out, 21:00 UTC) — only the trigger frequency and the "one slice per run" framing changed.

**Files touched:**
- `framework/automation-schedule.md` — Routine 4 renamed and re-cadenced (monthly → Tuesday/Saturday weekly), P4 tier row wording updated, "Annual full universe re-screen" coverage-map row updated
- `framework/operating-calendar.md` — "Automated via" column and full-universe-re-screen note updated to reflect the twice-weekly pace
- `portfolio/calendar/investment-routine-schedule.ics` — Routine 4 event's `RRULE` changed from `FREQ=MONTHLY;BYDAY=SA;BYSETPOS=1` to `FREQ=WEEKLY;BYDAY=TU,SA`; UID simplified (drops "monthly")

**Manual follow-up required (this commit alone does not change what's running):**
1. Re-paste the updated Routine 4 prompt into the existing routine at claude.ai/code/routines (per the standing constraint — Claude cannot edit routines from inside a session) and change its trigger to Tuesday + Saturday, 14:00 UTC.
2. Re-import `portfolio/calendar/investment-routine-schedule.ics` into Google Calendar (delete the old monthly Routine 4 event first, per the existing re-import instructions in `automation-schedule.md` step 4).

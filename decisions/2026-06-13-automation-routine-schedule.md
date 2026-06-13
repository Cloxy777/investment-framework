# 2026-06-13 — Framework change: scheduled Claude Code Routines for the operating calendar

**What changed:**

The [operating calendar](../framework/operating-calendar.md) (daily/weekly/quarterly/annual/event-triggered tasks) was, until now, entirely human-initiated — every `/screen`, `/rescore`, `/sync-portfolio`, and rate-gate check happened only when the user remembered to start a session. This entry adds an **automation layer**: 5 scheduled Claude Code Routines (research-preview, account-level scheduled cloud sessions) that run unattended and surface their output as GitHub issues/PRs/commits, plus a Google Calendar import so the cadence is visible alongside everything else.

New document: [framework/automation-schedule.md](../framework/automation-schedule.md) — the full spec (prompt text, cadence, environment, branch permissions) for each of the 5 routines. **Claude cannot create or configure routines from inside a session** (confirmed via tool search — routines are managed only at claude.ai/code/routines or local-terminal `/schedule`, both outside this session's reach), so this document is written as a **paste-in configuration reference** for the user to set up manually. Nothing runs automatically as a result of this commit alone — the routines only start once the user creates them using this spec.

**Why these 5 routines / cadences:**

| Routine | Cadence | Covers (operating-calendar.md row) |
|---|---|---|
| 1 — Daily Market & Earnings Check | Weekdays ~21:30 UTC (after US close) | Daily news/alert scan (Rule 9 >15% trigger) + earnings-release detection |
| 2 — Weekly Portfolio Sync & Brief | Monday ~11:00 UTC (before US open) | Weekly earnings calendar check + keeps `holdings.md`/snapshots current for every other routine |
| 3 — Quarterly Rate Environment Gate Review | First weekday of Jan/Apr/Jul/Oct ~12:00 UTC | Quarterly Rate Environment Gate update; January run also seeds the annual-tasks checklist (Rate-Normalised PE recalc, full-universe re-screen progress, Q1 reviews) |
| 4 — Monthly Universe Screening Slice | First Saturday of each month ~14:00 UTC | Annual full universe re-screen — spreads the 6-slice [coverage matrix](../framework/screening-coverage-log.md) across the year instead of a January cram |
| 5 — Monthly Rebalance / Trim Review | First Monday of each month ~12:30 UTC (after Routine 2) | Turnaround sub-gate review (event-triggered) + **new** monthly rebalance cadence (see below) |

Cadences were chosen so each routine has fresh inputs from the one before it (sync → brief → rebalance) and so nothing collides with market hours in a way that would return stale/closed-market prices.

**New addition — monthly rebalance/trim review cadence:**

`operating-calendar.md` previously had no fixed cadence for `/rebalance` at all — Phase 05/06 trim and exit triggers only got checked when the user thought to run it, which means a position could sit at a 90+ score (Trim to 1–2% / Full Exit territory) for months without the 2-consecutive-quarter "sustained extreme overvaluation" clock even being tracked. Routine 5 closes that gap with a **first-Monday-of-the-month** `/rebalance` run (proposal-only — it opens an issue and PR, never executes a trade). This also gives the Turnaround Sub-Gate's "2-quarter mandatory review" (Upgrade 4) a concrete monthly checkpoint instead of relying on the user to remember entry dates from `override-log.md`. `operating-calendar.md`'s "Schedule at a Glance" table now has a row for this cadence, with a pointer back to this entry.

**Prerequisites (manual, one-time — see automation-schedule.md "One-time setup" for full detail):**

1. Create a shared cloud environment (`investment-automation`) with custom network access (`eodhd.com`, `fred.stlouisfed.org`, `www.interactivebrokers.com`) and the Interactive Brokers connector enabled. `EODHD_API_KEY` itself is committed directly in `.claude/settings.json` (see addendum below) so every routine picks it up automatically — no separate environment variable needed.
2. Enable "Allow unrestricted branch pushes" for `cloxy777/investment-framework` **only** for Routine 2 (the weekly sync), matching the existing `sync-sop.md` convention of committing syncs straight to `main`. Routines 1/3/4/5 use the default `claude/`-branch + PR flow, or just open issues.
3. Enable GitHub email notifications + Watch the repo, so routine-opened issues/PRs land in the user's inbox — this is the "email" channel the user asked for; no separate email integration exists or is needed.
4. Import [`portfolio/calendar/investment-routine-schedule.ics`](../portfolio/calendar/investment-routine-schedule.ics) into Google Calendar — 5 routine cadences plus 2 reminders for tasks that remain manual (Freedom Finance sync on the 15th; the interactive Q1 annual-review session).

**What's still manual:** Freedom Finance sync (no API), finishing a `/rescore` once Routine 1 opens an issue (10yr avg PE and similar Macrotrends/TIKR inputs aren't available via EODHD), all trade execution, and `/new-position` (ad hoc by nature). Full coverage map in `automation-schedule.md`.

**Files touched:**
- `framework/automation-schedule.md` — **new**, full routine specs (prompts, cadences, environments, branch permissions, coverage map)
- `framework/operating-calendar.md` — added an "Automated via" column to the "Schedule at a Glance" table, added the new monthly rebalance/trim-review row, and added a pointer to `automation-schedule.md`
- `portfolio/calendar/investment-routine-schedule.ics` — **new**, importable Google Calendar file (5 routine cadences + 2 manual-task reminders)
- `CLAUDE.md` — added `automation-schedule.md` to the `framework/` orientation list

**Follow-up:** Once the user has set up the 5 routines per `automation-schedule.md`, the first real-world signal will be Routine 2's first Monday run (sync + weekly brief). Routine 3's January checklist (next occurring Jan 2027, but Q3/Q4 2026 quarterly runs happen sooner) folds an automation health-check (EODHD key, IBKR connector, FRED endpoint) into the existing Q1 annual review cadence — no separate review schedule needed for the automation itself.

**Addendum (same day) — EODHD API key committed to `.claude/settings.json`:** the placeholder `EODHD_API_KEY: ""` in `.claude/settings.json` was filled in with the real key, at the user's explicit request, so every Claude Code session against this repo — including all 5 cloud routines — picks it up automatically without a separate per-environment variable. The user weighed this against keeping it out of git history (the usual reason `.claude/settings.local.json` is gitignored) and accepted the trade-off given this is a private repo and the key only grants read access to EODHD market data (no trading/account access). If the repo's visibility or this calculus ever changes, rotate the key at eodhd.com and move it back to a gitignored/per-environment secret.

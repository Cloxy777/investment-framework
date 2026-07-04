# 2026-07-04 — Automation: add `/healthcheck` and Routine 7 (Integration Healthcheck)

**What changed:**

Added [`.claude/commands/healthcheck.md`](../.claude/commands/healthcheck.md), a new `/healthcheck` command that pings every external integration this framework depends on — the Interactive Brokers connector, the GitHub connector, `yfinance`/Yahoo Finance, the FRED 10Y Treasury endpoint, the Telegram Bot API, the 4 monitored Telegram channels' web previews, and the IBKR ticker-lookup CSV — and wired it up as **Routine 7** in [automation-schedule.md](../framework/automation-schedule.md), running daily ahead of Routines 1/2.

**Why:**

Six of the seven checks above already have a documented failure mode somewhere in this repo (`sync-sop.md`'s IBKR reconnect steps, the EODHD→`yfinance` switch, the Telegram token move to an environment variable), but nothing checked *proactively* whether they were still working — previously that was folded entirely into the Q1 annual review, meaning a broken connector or an expired token could silently degrade Routines 1–6 for up to a quarter before anyone noticed (e.g. Routine 1's `rescore-due` issues would just quietly stop firing).

**Design choice — minimalistic, issue-only reporting:** unlike Routines 1–5 (which send a Telegram "did it run" ping every time, quiet or not), Routine 7 is silent on a clean run — no commit, no PR, no session log, no Telegram message. A ping-every-day pattern here would be pure noise for a check whose entire job is "nothing to report" most days, and pinging via Telegram is circular anyway — a broken Telegram Bot API is itself one of the things being checked. On a failure, the command searches for an already-open `integration-healthcheck`-labeled issue and comments on it (with a still-failing / newly-failing / newly-recovered breakdown) instead of opening a new one each run; when everything recovers, it adds one closing comment and closes the issue. This mirrors the "quiet run" precedent Routine 6 set (see [decisions/2026-07-01-automation-routine-telegram-scan-no-issue.md](2026-07-01-automation-routine-telegram-scan-no-issue.md)) but goes further, since here even the *first* clean day after a fix should close out the noise rather than leave a stale issue open.

**Known gap, accepted:** if the GitHub connector itself is the thing that's down, Routine 7 has no way to report that via a GitHub issue — its own run log is the only trace. Not solved here; flagged in the command file as the one blind spot this design can't close (a secondary notification channel would need to be dedicated to reporting on GitHub's own reachability, which is out of scope for this change).

**Files touched:**
- `.claude/commands/healthcheck.md` — new command
- `CLAUDE.md` — added `/healthcheck` to the "Routine tasks → slash commands" list
- `framework/automation-schedule.md` — added Routine 7 (prompt, cadence, environment), a coverage-map row, and updated "Review cadence for this automation" to note daily reachability is now Routine 7's job rather than folded solely into the Q1 review

**Not touched:** `portfolio/calendar/investment-routine-schedule.ics` — Routine 7 has no user-facing action item or due date the way Routines 1–5 do (a clean run produces nothing to schedule), so it isn't added to the cadence-overview calendar, consistent with how Routine 6's hourly cadence was already excluded from that file for the same reason.

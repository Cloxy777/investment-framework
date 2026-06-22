# 2026-06-21 — Framework change: Routine 6 — Telegram Stock-Mention Scan

**What changed:**

Added a 6th scheduled Claude Code Routine (see [framework/automation-schedule.md](../framework/automation-schedule.md) "Routine 6") and a new `/telegram-scan` command ([.claude/commands/telegram-scan.md](../.claude/commands/telegram-scan.md)) that polls four public Telegram channels hourly, detects posts naming a specific publicly-traded company, and — if the watchlist shows it's never been evaluated, is stale, or the post claims a Rule-9-style fundamental event — runs `/rescore` or `/new-position` for that ticker and commits the result directly to `main`, with no separate review step.

A new state file, [portfolio/snapshots/telegram-watch.md](../portfolio/snapshots/telegram-watch.md), tracks each channel's last-seen post (so reruns never reprocess or silently skip a post) plus a running log of every mention evaluated, actioned or not.

**Channels monitored (user-supplied, all public):**
- https://t.me/tarasguk
- https://t.me/FinnInvestChannel
- https://t.me/myroslavkorol
- https://t.me/bolshegold

**Why hourly, and why direct-to-`main` (the trade-off being accepted):**

Every other routine in this repo either only opens an issue/PR proposal (Routines 1, 3, 4, 5) or, for the one routine that pushes straight to `main` (Routine 2, the weekly broker sync), does so for a low-judgment, easily-reversible data refresh. `automation-schedule.md`'s own "What stays manual no matter what" section explicitly carved out `/new-position` ("ad hoc by nature... not scheduled") and the RESCORE qualitative judgment layer ("Structural Quality Override calls, Short Thesis Engagement, and signing off on the final score... stay human") as things automation should *not* do unattended.

The user explicitly asked for full unattended execution here — including the qualitative sign-off — overriding that prior carve-out for this one routine, after being shown the trade-off directly. The reasoning accepted:

1. A Telegram post is not a confirmed fundamental event the way an earnings release or 10-K filing is — it's used only as a *trigger* to go check, never as a financial data source. `/rescore` and `/new-position` still independently pull real data (`yfinance` / Interactive Brokers) per Rule 0; if a metric is missing, the routine flags the gap and skips the auto-commit for that ticker rather than inventing it. Ticker identification gets the same treatment — an ambiguous company name is skipped and logged, never guessed.
2. The hard line every other routine already enforces — **no routine ever places a broker order** — is unchanged. This routine produces a committed score/recommendation only; executing any resulting BUY/TRIM/EXIT still requires the human to act through the broker.
3. The safety net is the same one Routine 2 already relies on for its direct-to-`main` pushes: `git revert`. A wrong auto-computed score sitting in `holdings.md` until corrected is a recoverable, visible (commit history + a same-run GitHub issue when something fires) risk — not a financial-loss risk, since no trade is ever placed automatically.
4. Hourly cadence (vs. the daily/weekly cadence of every other routine) was the user's explicit choice, accepting the added run cost. To keep notification noise proportional, this routine deliberately does **not** send a Telegram "did it run" ping or open a GitHub issue on a quiet run — every other routine does, but at daily/weekly cadence, where one ping per run is cheap; at hourly cadence it would be 24/day of pure noise. It's also intentionally left out of the static cadence `.ics` (hourly recurrence isn't meaningful there) — the per-action `.ics` + Telegram + GitHub issue layer still covers anything it actually finds.

**What's unchanged:** `/rescore` and `/new-position` themselves — Routine 6 calls them exactly as defined in their own command files, including the existing batch-processing limits. The `watchlist/`, `holdings.md`, and `sessions/` conventions are all unchanged; only the triggering source (a Telegram mention, not a human or a calendar date) is new.

**Prerequisites (manual, one-time — see automation-schedule.md "One-time setup" steps 1, 2, 6 for full detail):**
1. Add `t.me` to the `investment-automation` cloud environment's network allowlist.
2. Enable "Allow unrestricted branch pushes" for Routine 6 specifically (in addition to Routine 2).
3. Create Routine 6 from scratch at claude.ai/code/routines and paste in its prompt — Claude cannot create or edit routines from inside a session (same standing constraint as the original 5).

**Files touched:**
- `.claude/commands/telegram-scan.md` — **new**, the scan/match/trigger logic, reusable both ad hoc and from Routine 6
- `framework/automation-schedule.md` — added Routine 6's full spec; updated "How it fits together," "One-time setup," the coverage map, and "What stays manual no matter what"
- `framework/operating-calendar.md` — added a "Social-media stock-mention scan" row to the Schedule at a Glance table
- `portfolio/snapshots/telegram-watch.md` — **new**, Routine 6's state file (seeded empty)
- `portfolio/snapshots/README.md` — added a pointer to the new snapshot file
- `CLAUDE.md` — added `/telegram-scan` to the slash-command list

**Risk flagged for the Q1 annual review (automation-schedule.md "Review cadence"):** skim `telegram-watch.md`'s mention log for false positives (wrong ticker resolved from an ambiguous company name) or false negatives (a real event missed because the channel's web preview only shows ~20 posts), and confirm the 4 channels are still active/public.

**Addendum (2026-06-22):** the "direct-to-`main`" landing mechanism described above was replaced the next day — Routine 6 now pushes to a `claude/`-prefixed branch and merges via an auto-merge PR instead of committing straight to `main`. See [decisions/2026-06-22-automation-routine-auto-merge-pr.md](2026-06-22-automation-routine-auto-merge-pr.md) for why. Everything else in this entry — the hourly cadence, the ticker-identification rules, the Rule 0 data-sourcing boundary, and the no-trade-execution guarantee — is unchanged.

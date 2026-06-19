# 2026-06-19 — Framework change: Telegram notifications + per-action calendar invites for the automation layer

**What changed:**

The 5 Claude Code Routines added in [2026-06-13](2026-06-13-automation-routine-schedule.md) only surfaced output via GitHub issues/PRs and GitHub's own email notifications. That meant: (a) no reliable "did it actually run" signal on quiet days (several routines deliberately stayed silent when nothing fired), and (b) the only calendar artifact was a static `.ics` showing *when routines run*, not *what they found* — re-importing it after every change was already flagged as friction in the original doc.

This entry adds two things, both specified in [framework/automation-schedule.md](../framework/automation-schedule.md):

1. **A Telegram notification channel.** Every routine run now sends exactly one Telegram message (quiet or not) via a direct `curl` to the Telegram Bot API — no Claude-side integration exists for this, it's the routine's own shell prompt making a plain HTTP call, same pattern as the existing FRED/yfinance calls. Free, real-time, no new connector needed.
2. **Per-action calendar invites.** Instead of only the static 5-event cadence `.ics`, each actionable item a routine opens (RESCORE due, rebalance proposal, rate-regime change, screening hits, turnaround review) now also gets a single-event `.ics` sent as a Telegram document — tapping it on a phone adds that one to-do straight to Google Calendar. No Google Calendar API connector exists in this environment (only Drive/IBKR/Notion/GitHub are connected), so a true API push wasn't an option; this reuses the Telegram channel instead.

**Priority rule (why due dates aren't all the same):** added a 4-tier table (P1–P4) to `automation-schedule.md` blending **profitability** (the affected holding's current weight in `portfolio/holdings.md` — capital actually at stake) with **reliability** (a confirmed earnings release outranks an unexplained price move as a trigger). P1 items (rate-regime change; a trim/exit or earnings RESCORE on a ≥5%-weight holding) get a next-business-day, pre-market-slot due date; P4 items (screening candidates, the January checklist) get a 5–10 business day window. Each routine's prompt states its own tier mapping directly — they're pasted in standalone, so nothing can rely on cross-referencing this doc at runtime.

**Why the EODHD-key precedent matters here:** the user explicitly chose to commit the Telegram bot token to `.claude/settings.json` (same place the now-removed EODHD key lived — see the 2026-06-13 addendum), accepting the same trade-off: private repo, and the credential is scoped (a leaked bot token only lets someone message *as* this single-purpose bot — no account or trading access, unlike a leaked IBKR/broker credential). `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` were added as empty placeholders; the user still needs to create the bot via `@BotFather`, retrieve their chat ID, and fill both values in themselves (or hand them to Claude in a session to fill in) — no real credential was fabricated.

**Prerequisites — all manual, none of which this commit alone satisfies (see automation-schedule.md "One-time setup" steps 5–6 for full detail):**

1. Create the Telegram bot (`@BotFather` → `/newbot`), message it once, retrieve the chat ID from `getUpdates`, and fill both values into `.claude/settings.json`.
2. Add `api.telegram.org` to the `investment-automation` cloud environment's network allowlist at claude.ai — without it every `curl` to Telegram fails silently.
3. **Re-paste all 5 updated prompts** into the existing routines at claude.ai/code/routines. Per the standing constraint (confirmed again this session — Claude cannot create, edit, or otherwise touch routines from inside a session), editing `automation-schedule.md` does not change what's already running; the user confirmed the 5 routines are live from the 2026-06-13 setup, so this step is the only way the new Telegram/calendar steps actually take effect.

**What's unchanged:** all 5 routines' cadences, triggers, and GitHub issue/PR behavior are exactly as specified on 2026-06-13. This is additive — GitHub remains the system of record (Rule 10 auditability); Telegram and the per-action `.ics` are a faster notice layer on top, not a replacement.

**Files touched:**
- `framework/automation-schedule.md` — added the Telegram setup steps, the priority-tier table, and Telegram/calendar steps to all 5 routine prompts; updated the "How it fits together" table and the Q1 review-cadence note (now also checks the bot token still sends)
- `.claude/settings.json` — added empty `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` placeholders for the user to fill in

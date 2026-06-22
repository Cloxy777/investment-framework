# 2026-06-22 — Security: move secrets off the repo ahead of going public

**What changed:**

The repo is being switched from private to public visibility. As a pre-flight security check, `.claude/settings.json` was found to contain a real, live `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` (filled in on 2026-06-19 — see that day's Telegram/calendar decision entry). Both values are removed; `.claude/settings.json` is now `{}`. `framework/automation-schedule.md`'s One-time setup step 5 no longer instructs putting real values in that file — it now says to set `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` as environment variables on the `investment-automation` cloud environment at claude.ai/code instead.

**Why:**

The original decision to commit these values (2026-06-13 for the now-removed `EODHD_API_KEY`, 2026-06-19 for the Telegram token) explicitly accepted that trade-off only because the repo was private, and both entries said outright to revisit if that ever changed. It has changed. A public repo makes `.claude/settings.json` — and every prior commit that touched it — world-readable.

**Scope of this change, explicitly decided by the user:**

- **Rotate the credentials:** the user is handling this themselves, outside this session (Telegram bot token via `@BotFather` → `/revoke`/new token; confirming the already-flagged-as-compromised EODHD key from 2026-06-13 is dead at eodhd.com). This entry only covers the repo-side cleanup — removing the live values from the working tree and updating the setup docs.
- **Git history:** left as-is, deliberately. The literal old token/key strings remain visible in past commits (`32147f0`, `ec1c0ee`, `baf3df5`, and others) once the repo is public. The user weighed rewriting history (`git filter-repo` + force-push — rewrites every commit SHA, breaks any other clones/forks/open PRs) against simply rotating the credentials, and chose rotation only: once revoked, the visible strings are inert.
- **Financial data exposure:** separately flagged during this review — the IBKR account number (`U19421206`) and full portfolio holdings/balances/positions are committed in plain text across ~13 files (snapshots, `holdings.md`, session logs, sync commands) and will be world-readable once public. The user explicitly accepted this as-is; no redaction was requested.

**What's unchanged:**

- Routine 2 and Routine 6's behavior, cadence, and auto-merge-PR landing mechanism (see [2026-06-22-automation-routine-auto-merge-pr.md](2026-06-22-automation-routine-auto-merge-pr.md)) — only where the Telegram credentials live changed, not what the routines do with them.
- The Interactive Brokers connector and GitHub access — both are account-level connections, never stored in the repo.

**Files touched:**

- `.claude/settings.json` — removed the real `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` values; file is now `{}`.
- `framework/automation-schedule.md` — One-time setup step 5 (Telegram) rewritten to point at the cloud environment's env vars instead of the repo file; the Q1 review-cadence note's token-check line updated to match.

**Follow-up still needed (outside this repo, on the user):**

1. Revoke the old Telegram bot token via `@BotFather` and generate a new one (or confirm the old one is already dead).
2. Confirm the EODHD key from 2026-06-13 is rotated/dead at eodhd.com.
3. Set the new `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` as environment variables on the `investment-automation` cloud environment at claude.ai/code — Routine 1/2/6's Telegram `curl` steps will silently stop sending until this is done.
4. Flip the repo's visibility to public in GitHub settings once 1–3 are done.

**Related:** [decisions/2026-06-13-automation-routine-schedule.md](2026-06-13-automation-routine-schedule.md) (EODHD key, original private-repo trade-off), [decisions/2026-06-19-automation-telegram-calendar-notifications.md](2026-06-19-automation-telegram-calendar-notifications.md) (Telegram token, same trade-off).

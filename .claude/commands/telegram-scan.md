---
description: Poll monitored Telegram channels for new posts, detect stock/company mentions, and trigger /rescore or /new-position when warranted
---

Run a TELEGRAM SCAN per [automation-schedule.md](../../framework/automation-schedule.md) "Routine 6". This command runs the same way whether invoked ad hoc (interactively) or unattended (Routine 6).

Channels monitored (public web preview, no auth needed): $ARGUMENTS (if empty, use the channel list in [portfolio/snapshots/telegram-watch.md](../../portfolio/snapshots/telegram-watch.md) — currently `t.me/tarasguk`, `t.me/FinnInvestChannel`, `t.me/myroslavkorol`, `t.me/bolshegold`).

Steps:
1. Read `portfolio/snapshots/telegram-watch.md` for each channel's last-seen post marker (the most recent post already processed).
2. For each channel, fetch `https://t.me/s/<channel>` and look only at its single most recent post (the top of the preview) — not the full visible window. Compare it to that channel's stored marker (a delta check, not a scan):
   - **First run for a channel** (marker still shows `— (not yet run)`): there's no prior post to diff against, so take no action — this is a baseline-seeding pass only. Log one mention-log row noting the baseline was seeded, and in step 7 set the marker to this post. Normal delta checking (below) applies for that channel starting next run.
   - **Marker unchanged** (the top post is the same one already recorded): nothing new for this channel this run.
   - **Marker differs** (the top post isn't the one on record): that single post is the new one to evaluate below.
   - This only ever catches the latest post per channel per run. If a channel posts more than once within the same hour, the earlier post(s) in that gap are superseded and never individually evaluated. If the new top post's timestamp is more than ~1 hour after the previous marker (a sign more than one post may have landed since the last check), say so explicitly in the summary rather than silently assuming only one post happened — but still only act on the latest.
3. If a new post was found, decide whether it names a specific, identifiable publicly-traded company or ticker — not generic macro/commodity/crypto commentary. If a company is named but the ticker can't be confidently resolved (ambiguous name, private company, a listing outside this framework's coverage), skip it and say so. Never guess a ticker — CLAUDE.md Rule 0 ("never invent or estimate") applies to identification, not just financial metrics.
4. For each resolved ticker:
   - Check `portfolio/holdings.md` for current-holding status, weight, last score, last review date.
   - Check `watchlist/in-portfolio/<TICKER>/` or `watchlist/not-in-portfolio/<TICKER>/` for the latest dated entry and its "Next review trigger."
   - Read the post for any claimed Rule 9 fundamental event (earnings, guidance revision, M&A, management change, macro/rate-relevant shift) concerning that ticker — this is a *candidate* trigger only, never treated as verified data. The post's text is never used as a financial input; only `/rescore`'s and `/new-position`'s own Rule 0 live-data fetch (`yfinance` / Interactive Brokers) is.
   - Decide the action:
     - No watchlist entry exists at all → `/new-position <TICKER>`.
     - Held, and the post claims a Rule 9 event, OR no review has happened since the holding's last earnings per [operating-calendar.md](../../framework/operating-calendar.md) → `/rescore <TICKER>`.
     - Not held, has a prior `not-in-portfolio` entry, and the post claims materially new information beyond what that entry already reflects → `/new-position <TICKER>` again.
     - Otherwise (recently reviewed, no new claimed event — just a passing mention) → no action; log the mention only.
5. Run every triggered `/rescore` or `/new-position` exactly per their own command files, including the batch-processing limits defined there (max 2 concurrent). If a required metric is missing for a ticker, do not invent it — flag the gap, skip the auto-commit for that ticker, and note it for a manual follow-up session instead.
6. For each completed session, push to a `claude/`-prefixed branch — message like `Auto-rescore <TICKER> - Telegram trigger (<channel>, <post date>)` or `Auto new-position <TICKER> - Telegram trigger (<channel>, <post date>)` — open a PR with that same title, and enable auto-merge (squash) on it; if that call reports the PR already clean/mergeable with nothing pending (the normal case in this repo — no CI or required reviews configured), merge it directly (squash) instead of leaving it open. This produces a score/recommendation only — never submit or modify any broker order; that stays human for every routine in this repo.
7. Update `portfolio/snapshots/telegram-watch.md`: for each channel with a new top post (including a first-run baseline), bump its marker to that post; channels with no change keep their existing marker. Append one mention-log row per post evaluated this run (date, channel, ticker, action taken or "no action — reason"). Push this alongside step 6's branch/PR (or on its own, as its own `claude/`-prefixed branch + auto-merge PR, if nothing triggered).
8. Summarize: tickers actioned (with links to the new session logs/commits), mentions skipped (with reason), and any data gaps flagged.

When run unattended as Routine 6, also: for any triggered action that resolves to BUY/TRIM/EXIT, send that ticker's priority-tier `.ics` via Telegram exactly as the other routines do. This routine never opens or updates a GitHub issue — the per-run branch/PR/commit plus the Telegram alert (see automation-schedule.md Routine 6) are the record of what fired.

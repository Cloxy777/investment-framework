---
description: Poll monitored Telegram channels for new posts, detect stock/company mentions, and trigger /rescore or /new-position when warranted
---

Run a TELEGRAM SCAN per [automation-schedule.md](../../framework/automation-schedule.md) "Routine 6". This command runs the same way whether invoked ad hoc (interactively) or unattended (Routine 6).

Channels monitored (public web preview, no auth needed): $ARGUMENTS (if empty, use the channel list in [portfolio/snapshots/telegram-watch.md](../../portfolio/snapshots/telegram-watch.md) — currently `t.me/tarasguk`, `t.me/FinnInvestChannel`, `t.me/myroslavkorol`, `t.me/bolshegold`).

Steps:
1. Read `portfolio/snapshots/telegram-watch.md` for each channel's last-seen post marker (date/time of the most recent post already processed).
2. For each channel, fetch `https://t.me/s/<channel>` and identify every post newer than that channel's last-seen marker. The web preview only shows roughly the last ~20 posts — if the marker has scrolled off the visible window entirely (the channel posted more than that since the last run), say so explicitly in the summary rather than silently treating the gap as "nothing new."
   - **First run for a channel** (marker still shows `— (not yet run)`): do not treat the whole visible window as "new" — there's no real recency signal, and evaluating ~20 posts at once would burst into a batch of unintended `/rescore`/`/new-position` runs. Instead, this is a baseline-seeding pass for that channel only: skip steps 3–6 for its posts, log a single mention-log row noting how many posts were skipped pre-baseline, and in step 7 set its marker to the newest post currently visible. Normal new-post detection (the general rule above) applies for that channel starting next run.
3. For each new post, decide whether it names a specific, identifiable publicly-traded company or ticker — not generic macro/commodity/crypto commentary. If a company is named but the ticker can't be confidently resolved (ambiguous name, private company, a listing outside this framework's coverage), skip it and say so. Never guess a ticker — CLAUDE.md Rule 0 ("never invent or estimate") applies to identification, not just financial metrics.
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
6. Commit each completed session directly — message like `Auto-rescore <TICKER> - Telegram trigger (<channel>, <post date>)` or `Auto new-position <TICKER> - Telegram trigger (<channel>, <post date>)`. This produces a score/recommendation only — never submit or modify any broker order; that stays human for every routine in this repo.
7. Update `portfolio/snapshots/telegram-watch.md`: bump each channel's last-seen marker to its newest processed post, and append one row per mention evaluated this run (date, channel, ticker, action taken or "no action — reason"). Commit this alongside step 6's commits (or on its own if nothing triggered).
8. Summarize: tickers actioned (with links to the new session logs/commits), mentions skipped (with reason), and any data gaps flagged.

When run unattended as Routine 6, also: open or update a single GitHub issue only if something was actually actioned or a data gap was flagged this run — a fully quiet run produces no issue (see automation-schedule.md Routine 6 for why, given the hourly cadence). For any triggered action that resolves to BUY/TRIM/EXIT, send that ticker's priority-tier `.ics` via Telegram exactly as the other routines do.

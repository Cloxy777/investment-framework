# Automation Schedule — Claude Code Routines

This document translates the [operating calendar](operating-calendar.md) into a concrete set of **Claude Code Routines** — scheduled, unattended cloud sessions (Anthropic-managed infrastructure, "Routines" in research preview) that run this repo's slash commands automatically and surface results as GitHub issues, commits, and PRs.

**Claude cannot create or edit routines from inside a session** — they're account-level objects configured at [claude.ai/code/routines](https://claude.ai/code/routines) or via `/schedule` in a local terminal (not inside a cloud session). This doc gives you the exact configuration — prompt, schedule, environment, permissions — to paste in for each routine. Once set up, they run on their own; you check progress via GitHub (issues/PRs), email (GitHub notifications), and Telegram (see setup step 5 — every run, quiet or not, now sends a message). Whenever this doc changes a routine's prompt, re-paste it into the matching routine at claude.ai/code/routines — editing this file alone does not change what's already running.

## How it fits together

| Layer | What it is |
|---|---|
| **Routine** | A saved prompt + repo + environment + trigger, run by Claude Code on a schedule |
| **Report** | A GitHub issue (summary/flags) and/or a PR (file changes — session logs, snapshot updates, coverage log) |
| **Notification (passive)** | GitHub email notification when a routine opens an issue or PR (see setup step 3) |
| **Notification (active)** | A Telegram message every run, via the Telegram Bot API called directly with `curl` — free, real-time, and sent whether or not anything fired (the "did it actually run" signal; see setup step 5) |
| **Calendar (cadence overview)** | [`portfolio/calendar/investment-routine-schedule.ics`](../portfolio/calendar/investment-routine-schedule.ics) — static, manually re-imported; shows *when routines run*, not what they find |
| **Calendar (action items)** | A one-event `.ics` per actionable item (RESCORE due, rebalance proposal, rate-regime change, ...) sent as a Telegram document — tap it on your phone to add that specific to-do straight to Google Calendar. Due date/time computed by the priority rule below |

Five routines cover the entire "Schedule at a Glance" table in [operating-calendar.md](operating-calendar.md), plus one new addition (monthly rebalance check — see [decisions/2026-06-13-automation-routine-schedule.md](../decisions/2026-06-13-automation-routine-schedule.md)). The coverage map at the bottom shows exactly what's automated vs. what still needs you.

---

## One-time setup

1. **Create a cloud environment** (e.g. name it `investment-automation`) at claude.ai/code — used by all five routines:
   - **Network access:** Custom → check "Also include default list of common package managers/Trusted domains", then add: `fred.stlouisfed.org`, `www.interactivebrokers.com`, `query1.finance.yahoo.com`, `query2.finance.yahoo.com` (for `yfinance` — see framework/valuation-scoring.md "yfinance — per-candidate Phase 01 verification"), and `api.telegram.org` (for step 5 below).
   - **Connectors:** keep the **Interactive Brokers** connector enabled (it's how Routines 1 and 2 get live prices/positions/balances/orders). GitHub access comes from your existing claude.ai ↔ GitHub connection.

2. **Branch-push permission:** when creating **Routine 2 (Weekly Sync)**, enable **"Allow unrestricted branch pushes"** for `cloxy777/investment-framework`. It needs to commit straight to `main`, per the existing convention in [sync-sop.md](../portfolio/sync-sop.md) (syncs are low-risk data refreshes with `git revert` as the safety net). Routines 1, 3, 4, 5 only open issues or push to default `claude/`-prefixed branches + PRs — no special permission needed for those.

3. **GitHub notifications (your "email" channel):** go to [github.com/settings/notifications](https://github.com/settings/notifications) and make sure **Email** is checked under "Issues, pull requests, ...". Then on the repo page, click **Watch → All Activity** (or **Custom** → Issues + Pull Requests + Pushes). Every issue or PR a routine creates then lands in your inbox automatically.

4. **Google Calendar (cadence overview):** import [`portfolio/calendar/investment-routine-schedule.ics`](../portfolio/calendar/investment-routine-schedule.ics) — Google Calendar → Settings → Import & export → Import, pick a target calendar. It has 5 recurring events (one per routine, at the cadence below) plus 2 reminders for tasks that remain manual. All times are UTC; Google Calendar converts to your local zone automatically. If you change a cadence below, delete the old imported events and re-import. This file is static — step 5 below covers per-action calendar items.

5. **Telegram (active notification + per-action calendar channel) — free, no API cost:**
   - In Telegram, message **@BotFather** → `/newbot` → follow the prompts (display name + a username ending in `bot`). It replies with a **bot token**, e.g. `123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ`. Keep it private — anyone with it can send messages as this bot.
   - Send any message to your new bot (e.g. "hi") — a bot can't message you until you've messaged it first.
   - In a browser, open `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` and read the `"chat":{"id": ...}` field from the JSON — that's your **chat ID**.
   - Put both values in [`.claude/settings.json`](../.claude/settings.json):
     ```json
     {
       "env": {
         "TELEGRAM_BOT_TOKEN": "<your bot token>",
         "TELEGRAM_CHAT_ID": "<your chat id>"
       }
     }
     ```
     This repo is private, and a leaked token only lets someone send messages as this single-purpose bot — no account or financial access — matching the risk calculus already accepted for the EODHD key in [decisions/2026-06-13-automation-routine-schedule.md](../decisions/2026-06-13-automation-routine-schedule.md). If that calculus ever changes, revoke via `@BotFather` → `/revoke` and move the token to a per-environment variable instead.
   - Confirm `api.telegram.org` is in the `investment-automation` environment's network allowlist (step 1) — every `curl` to Telegram fails silently without it.
   - **Additive, not a replacement:** GitHub issues/PRs stay the system of record for every routine's output (Rule 10 auditability). Telegram and the per-action `.ics` are a faster notice layer on top.

6. **Re-paste the 5 prompts below** into your existing routines at [claude.ai/code/routines](https://claude.ai/code/routines) — they now include the Telegram + calendar steps and won't take effect until pasted in.

---

## Priority rule for due dates & calendar timing (profitability + reliability)

Every actionable item gets a **priority tier**, which sets its `.ics` due date/time and how urgently it reads in the Telegram message. The tier blends **profitability** (capital actually at stake — current weight from `portfolio/holdings.md`) with **reliability** (how deterministic the trigger is — a confirmed earnings release outranks an unexplained price move).

| Tier | When it applies | `.ics` due date | Time (UTC) |
|---|---|---|---|
| **P1** | Rate regime change (whole-portfolio); a trim/exit trigger fires on a holding ≥5% weight; an earnings-driven RESCORE on a holding ≥5% weight | Next business day | 13:30 (just before US open) |
| **P2** | Earnings-driven RESCORE on a holding <5% weight; the monthly rebalance proposal itself; a turnaround-sub-gate review due | Next business day | 21:00 (after US close) |
| **P3** | Unexplained >15% move RESCORE (no confirmed catalyst yet); an overdue `rescore-due` flagged by Routine 2 | 3 business days out (today if already overdue) | 21:00 |
| **P4** | Monthly screening candidates (informational, no capital at risk yet); January annual-tasks checklist | 5 business days out (10 for the January checklist) | 21:00 |

Each routine's prompt below states exactly which tier its own triggers map to.

---

## Routine 1 — Daily Market & Earnings Check

| | |
|---|---|
| **Cadence** | Weekdays (Mon–Fri), after US market close — e.g. 21:30 UTC |
| **Repo** | `cloxy777/investment-framework`, default branch |
| **Environment** | `investment-automation` |
| **Branch permission** | Default (no unrestricted push needed — read-only + issues) |

**Prompt:**

```
You are running the Daily Market & Earnings Check for the Quality Value +
Dynamic Trimming investment framework (repo: cloxy777/investment-framework).

1. Read portfolio/holdings.md for the current equity holdings. Skip the CASH
   rows, XEON, and TLT (non-equity/cash-equivalent — out of scope for Rule 9
   price-move monitoring per framework/operating-calendar.md).

2. For each equity ticker, use the Interactive Brokers connector
   (get_price_snapshot / get_price_history, account U19421206) to get the
   latest price and previous close, and compute the 1-day % change.

3. For each ticker, use `yfinance` (`t.get_earnings_dates()` / `t.calendar`) to
   check whether it reported earnings in the last 2 business days.

4. For each ticker:
   - |1-day change| > 15% with no earnings release explaining it (step 3) =
     a Rule 9 "mandatory immediate re-score" trigger (operating-calendar.md).
     Open a GitHub issue titled
     "RESCORE (Rule 9): <TICKER> moved <X>% on <date> - no known catalyst",
     with the move size, and a due date 3 business days out. Label it
     `rescore-due` (create the label if missing).
   - 5% < |1-day change| <= 15% -> note it in this run's summary only. Do not
     open an issue for this alone.
   - Earnings reported in the last 2 business days -> open a GitHub issue
     titled "RESCORE: <TICKER> - earnings released <date>", due 3 business
     days from the earnings date. Pre-fill it with whatever you can pull via
     `yfinance` (FCF, EV/EBIT, forward PE, ROIC, margins, net debt/EBITDA -
     see framework/valuation-scoring.md "yfinance - per-candidate Phase 01
     verification"). Add current price and current weight from holdings.md,
     and list the fields needed for the "Standard Re-Score" checklist
     (operating-calendar.md) you could NOT fill - especially 10yr average PE
     and FCF/NI conversion ratio, which usually need Macrotrends/TIKR/Koyfin.
     Label it `rescore-due`.

5. Before opening any issue, check open issues for an existing one for the
   same ticker + trigger type - don't duplicate (skip steps 6-7 for a ticker
   you didn't actually open a new issue for).

6. For each new issue opened in step 4, set its priority tier per
   framework/automation-schedule.md "Priority rule": earnings-driven RESCORE
   on a holding >=5% weight (holdings.md) = P1 (due next business day,
   13:30 UTC); earnings-driven RESCORE on a holding <5% weight = P2 (next
   business day, 21:00 UTC); unexplained >15%-move RESCORE = P3 (3 business
   days out, 21:00 UTC).

7. For each new issue, write a single-event .ics
   (action-rescore-<TICKER>.ics: SUMMARY = issue title, DTSTART = the tier's
   due date/time in UTC, DESCRIPTION = the issue URL) and send it:
   `curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendDocument" -F chat_id="${TELEGRAM_CHAT_ID}" -F document=@action-rescore-<TICKER>.ics`

8. Send exactly one Telegram message for this run, whether or not anything
   fired in step 4 - this is the "did it actually run" signal, not just an
   alert channel:
   `curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" -d chat_id="${TELEGRAM_CHAT_ID}" -d parse_mode="Markdown" --data-urlencode text="..."`
   Quiet run: "*Daily Check <date>* - N holdings checked, all quiet."
   Otherwise: one line per ticker that fired - "*Daily Check <date>* -
   <TICKER>: <tier>, due <date> <time> UTC - <issue URL>".

Success = every >15% unexplained move and every earnings release in the last
2 business days for a current holding has exactly one open GitHub issue
tracking its required RESCORE, a matching calendar invite delivered via
Telegram, and exactly one Telegram run-summary message sent - quiet or not.
```

---

## Routine 2 — Weekly Monday Portfolio Sync & Brief

| | |
|---|---|
| **Cadence** | Weekly, Monday before US market open — e.g. 11:00 UTC |
| **Repo** | `cloxy777/investment-framework`, default branch |
| **Environment** | `investment-automation` |
| **Branch permission** | **Allow unrestricted branch pushes** (commits to `main`) |

**Prompt:**

```
You are running the Weekly Monday Portfolio Sync & Brief for
cloxy777/investment-framework.

1. Follow portfolio/sync-sop.md "Full IBKR Sync" exactly: fetch positions
   (get_account_positions), balances (get_account_balances), and orders
   (get_account_orders) via the Interactive Brokers connector for account
   U19421206, resolve tickers via the live IBKR ticker-lookup CSV (fall back
   to portfolio/reference/ibkr-ticker-lookup.csv if unreachable), update
   portfolio/snapshots/ibkr.md, portfolio/snapshots/ibkr-orders.md, and
   portfolio/holdings.md, and commit straight to main with message
   "Sync IBKR portfolio - YYYY-MM-DD". Do the watchlist
   in-portfolio/not-in-portfolio reconciliation from watchlist/README.md if
   positions changed.

2. Use `yfinance` (`t.get_earnings_dates()` / `t.calendar`) to check all
   current equity holdings for earnings dates in the next 7 days and note any
   upcoming.

3. List any open GitHub issues labeled `rescore-due` whose due date has
   already passed - flag these as overdue.

4. Check framework/operating-calendar.md: if today falls in the first 7 days
   of January, April, July, or October, note that Routine 3 (Quarterly Rate
   Environment Gate Review) is due this week - just for visibility, it runs
   itself.

5. Write sessions/weekly-briefs/YYYY-MM-DD-weekly-brief.md summarizing: the
   sync's portfolio changes, upcoming earnings (next 7 days), any overdue
   rescore-due issues, and any quarterly/annual items due. Commit this file
   to main alongside (or right after) the sync commit.

6. Open or update a single GitHub issue titled
   "Weekly Portfolio Brief - week of YYYY-MM-DD" with the same summary,
   linking to the sync commit and the brief file.

7. For each overdue `rescore-due` issue found in step 3, treat it as P3 per
   framework/automation-schedule.md "Priority rule" (due today, 21:00 UTC -
   it's already late) and send a one-event .ics
   (action-rescore-<TICKER>-overdue.ics) via Telegram:
   `curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendDocument" -F chat_id="${TELEGRAM_CHAT_ID}" -F document=@action-rescore-<TICKER>-overdue.ics`

8. Send one Telegram message summarizing this run - the sync (commit link),
   upcoming earnings (next 7 days), the count of overdue rescore-due issues
   (with links), and the weekly brief issue link:
   `curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" -d chat_id="${TELEGRAM_CHAT_ID}" -d parse_mode="Markdown" --data-urlencode text="..."`

Success = holdings.md and snapshots reflect this week's live broker data, one
GitHub issue summarizes the week ahead, any overdue rescores have a Telegram
calendar reminder, and one Telegram run-summary message was sent.
```

---

## Routine 3 — Quarterly Rate Environment Gate Review

| | |
|---|---|
| **Cadence** | First weekday of January, April, July, October — e.g. 12:00 UTC |
| **Repo** | `cloxy777/investment-framework`, default branch |
| **Environment** | `investment-automation` |
| **Branch permission** | Default (`claude/` branch + PR) |

**Prompt:**

```
You are running the Quarterly Rate Environment Gate Review for
cloxy777/investment-framework. This runs on the first weekday of January,
April, July, and October.

1. Fetch the current 10-year US Treasury yield from FRED:
   https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
   (use the most recent non-blank value).

2. Using framework/strategy.md "Rate Environment Gate - Step 2 - Rate Regime
   Modifier", determine which band the current yield falls into:
   <2% -> -10 | 2-3.5% -> 0 | 3.5-5% -> +5 | >5% -> +10.

3. Search sessions/ for the most recent RESCORE or rebalance session and find
   the "Rate Regime Modifier (active)" value it used.

4. If the band from step 2 differs from step 3's value:
   - Open a GitHub issue titled
     "Rate Regime changed: <old> -> <new> (10Y = X.XX%) - portfolio-wide
     re-score recommended", explaining the shift and listing every current
     equity holding from portfolio/holdings.md as a checklist needing
     /rescore.
   - On a new branch, add decisions/YYYY-MM-DD-rate-regime-change.md
     documenting the old/new modifier, the observed 10Y yield, and the date,
     and open a PR.

5. If the current month is January, additionally open a checklist issue
   titled "January annual tasks - <year>" covering:
   (a) Rate-Normalised PE recalc for the top 5 holdings by weight
       (strategy.md Step 3),
   (b) annual full-universe re-screen progress - pull
       framework/screening-coverage-log.md and list any slice whose
       "Last screened" date is more than 12 months old,
   (c) the Q1 annual reviews of portfolio/override-log.md,
       framework/graveyard-audit.md, framework/benchmark-comparison.md, and
       this automation-schedule.md (confirm the IBKR connector and the FRED
       endpoint are still working).

6. Save sessions/quarterly/YYYY-QN-rate-environment-review.md recording the
   10Y yield, the band, and whether anything changed - regardless of outcome.

7. If the band changed (step 4): this is P1 per framework/automation-schedule.md
   "Priority rule" (whole-portfolio impact) - due next business day, 13:30 UTC.
   Write a single-event .ics (action-rate-regime-change.ics: SUMMARY =
   the issue title, DESCRIPTION = the issue URL) and send it:
   `curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendDocument" -F chat_id="${TELEGRAM_CHAT_ID}" -F document=@action-rate-regime-change.ics`
   If the current month is January (step 5): this is P4 - due 10 business
   days out, 21:00 UTC. Write and send action-january-annual-tasks.ics the
   same way, pointed at the annual-tasks checklist issue.

8. Send one Telegram message regardless of outcome (a quiet quarter is still
   worth confirming ran): state the 10Y yield, the band, and whether it
   changed; if it changed, link the issue + PR; if January, also link the
   annual-tasks checklist issue:
   `curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" -d chat_id="${TELEGRAM_CHAT_ID}" -d parse_mode="Markdown" --data-urlencode text="..."`

Success = the current Rate Regime Modifier band is recorded for this quarter;
if it changed, a PR + issue + Telegram calendar invite exist flagging the
portfolio-wide re-score need; one Telegram run-summary message was sent.
```

---

## Routine 4 — Monthly Universe Screening Slice

| | |
|---|---|
| **Cadence** | First Saturday of each month — e.g. 14:00 UTC |
| **Repo** | `cloxy777/investment-framework`, default branch |
| **Environment** | `investment-automation` |
| **Branch permission** | Default (`claude/` branch + PR) |

**Prompt:**

```
You are running the Monthly Universe Screening Slice for
cloxy777/investment-framework. Runs the first Saturday of each month
(markets closed).

1. Run /screen with no argument. Per .claude/commands/screen.md, this
   self-selects the least-recently-screened slice from
   framework/screening-coverage-log.md. There is no user to ask for a
   TIKR/Koyfin paste in an unattended run, so go straight to the regional
   quality-factor ETF holdings fallback (MOAT/QUAL/QGRW for US; IQLT for
   international) as the starting universe, and flag this prominently in the
   output.

2. Complete Steps 1-5 of the screen command: structural triage, the full
   Phase 01 quantitative gate sourced per-candidate via `yfinance` (see
   framework/valuation-scoring.md), the qualitative pass on survivors
   (batches of 2 concurrent, per new-position.md policy), flag data gaps
   explicitly (never estimate - CLAUDE.md Rule 0), and update
   framework/screening-coverage-log.md's "Last screened" date, qualified-name
   count, and sources for the slice covered.

3. Save the session as sessions/YYYY-MM-DD-screening-<universe>.md.

4. Open a PR with the coverage-log update and session log.

5. Open a GitHub issue titled
   "Screening: <N> qualified names found in <slice>" listing the qualified
   tickers as /new-position candidates - or, if zero qualified, a short issue
   saying so (a useful signal too - don't skip it).

6. If N > 0: this is P4 per framework/automation-schedule.md "Priority rule"
   (informational, no capital at risk yet) - due 5 business days out,
   21:00 UTC. Write a single-event .ics (action-screening-<slice>.ics:
   SUMMARY = the issue title, DESCRIPTION = the issue URL listing the
   tickers) and send it:
   `curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendDocument" -F chat_id="${TELEGRAM_CHAT_ID}" -F document=@action-screening-<slice>.ics`

7. Send one Telegram message regardless of N: the slice screened, N
   qualified (with tickers if N > 0), and the issue + PR links:
   `curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" -d chat_id="${TELEGRAM_CHAT_ID}" -d parse_mode="Markdown" --data-urlencode text="..."`

Success = one coverage-log row has an updated "Last screened" date for this
run, with a PR and a summary issue; if any names qualified, a Telegram
calendar invite was sent; one Telegram run-summary message was sent either way.
```

---

## Routine 5 — Monthly Rebalance / Trim Review

| | |
|---|---|
| **Cadence** | First Monday of each month, after Routine 2's sync — e.g. 12:30 UTC |
| **Repo** | `cloxy777/investment-framework`, default branch |
| **Environment** | `investment-automation` |
| **Branch permission** | Default (`claude/` branch + PR) |

**Prompt:**

```
You are running the Monthly Rebalance / Trim Review for
cloxy777/investment-framework. Runs the first Monday of each month, after
that day's Weekly Sync routine has refreshed holdings.md.

1. Run /rebalance per .claude/commands/rebalance.md: pull current
   holdings/weights from portfolio/holdings.md, flag any holding whose Last
   Score is stale (no review since its most recent earnings, per
   framework/operating-calendar.md), and for holdings with current scores
   apply Phase 05 dynamic trimming and Phase 06 exit triggers from
   framework/strategy.md. Check the 15% single-position cap (Upgrade 7).
   Propose a recycling plan into current Score 0.0-29.9 names, with full
   reasoning per position - no black-box output.

2. Check portfolio/override-log.md and decisions/ for any position opened
   under the Turnaround Sub-Gate (Upgrade 4, framework/strategy.md). For each,
   if 2 calendar quarters have elapsed since entry with no review logged
   since, add it to this month's issue as a turnaround-review-due item.

3. Save sessions/YYYY-MM-DD-rebalance.md and open a PR.

4. Open a GitHub issue titled "Monthly Rebalance - YYYY-MM-DD" summarizing:
   stale scores needing /rescore first, any trim/exit triggers fired, the
   proposed recycling plan, the 15% cap check result, and any
   turnaround-review-due items. This is a proposal for human review - do not
   execute any trades.

5. Set the rebalance issue's priority tier per
   framework/automation-schedule.md "Priority rule": P1 (next business day,
   13:30 UTC) if any trim/exit trigger fired on a holding >=5% weight
   (holdings.md); otherwise P2 (next business day, 21:00 UTC). Write a
   single-event .ics (action-rebalance-YYYY-MM-DD.ics: SUMMARY = the issue
   title, DESCRIPTION = the issue URL) and send it:
   `curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendDocument" -F chat_id="${TELEGRAM_CHAT_ID}" -F document=@action-rebalance-YYYY-MM-DD.ics`
   For each turnaround-review-due item from step 2, that's P2 too - write
   and send action-turnaround-<TICKER>.ics the same way, pointed at its
   checklist item in the issue.

6. Send one Telegram message summarizing: whether any trim/exit fired (and
   on what), the 15% cap check result, any turnaround-review-due tickers,
   and the issue + PR links:
   `curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" -d chat_id="${TELEGRAM_CHAT_ID}" -d parse_mode="Markdown" --data-urlencode text="..."`

Success = a rebalance session log + PR exist, a summary issue gives a
one-glance view of what (if anything) needs action this month, a Telegram
calendar invite covers the proposal (and any turnaround reviews due), and one
Telegram run-summary message was sent.
```

---

## Coverage map — operating calendar → routine → residual manual step

| Operating calendar item | Covered by | What's still manual |
|---|---|---|
| Daily news & alert scan (price move >5%) | Routine 1 | Nothing — informational flag only |
| Weekly earnings calendar check | Routine 1 (detection) + Routine 2 (look-ahead) | Nothing |
| Quarterly post-earnings re-score (within 3 business days) | Routine 1 opens a pre-filled `rescore-due` issue | Bring the issue into a normal session, supply the flagged gaps (10yr avg PE, FCF/NI conversion, etc. from Macrotrends/TIKR/Koyfin), and run `/rescore <TICKER>` to finish the scoring |
| Quarterly Rate Environment Gate update | Routine 3 | If the regime changed, work through the portfolio-wide `/rescore` checklist the issue lists |
| Annual Rate-Normalised PE recalc (Jan) | Routine 3's January checklist issue | Gather the top-5 rate-matched historical PE data (with Claude, interactively) |
| Annual full universe re-screen (Jan target) | Routine 4, monthly slices year-round | Nothing — Routine 4 builds its starting universe from quality-factor ETF holdings automatically and verifies candidates via `yfinance` |
| Rule 9 — price move >15% / earnings | Routine 1 | Guidance revisions, M&A, and management-change triggers aren't auto-detected — still need human awareness from news |
| Rule 9 — short thesis engagement | Not automated | Optional future extension: add a weekly WebSearch ("`<TICKER>` short report") for top-weight holdings to Routine 1 or 2 |
| Turnaround sub-gate review (every 2 quarters) | Routine 5 | Nothing, once `override-log.md` records entry dates for turnaround positions |
| IBKR portfolio sync (positions/balances/orders) | Routine 2 | Nothing |
| Freedom Finance sync | Not automated (no API — screenshot-based) | Run `/sync-portfolio` manually with screenshots, per `sync-sop.md` |
| Rebalance / trim review | Routine 5 (new monthly cadence — see decisions log) | Execute any approved trims via your broker |

## What stays manual no matter what

- **Freedom Finance sync** — no API; screenshot-based by design.
- **Finishing a RESCORE** — `yfinance` covers most Phase 01/02 inputs, but 10yr average PE (Macrotrends) and sometimes FCF/NI conversion need a human-in-the-loop session.
- **Executing trades** — every routine here proposes (issues, PRs); nothing places an order.
- **Anything `/new-position`** — ad hoc by nature, triggered by a screening hit or your own idea, not scheduled.

## Review cadence for this automation

Folded into the existing Q1 annual review (alongside `override-log.md`, `graveyard-audit.md`, `benchmark-comparison.md` — see Routine 3's January checklist): confirm the Interactive Brokers connector is still authorized, the FRED endpoint is still reachable, the Telegram bot token in `.claude/settings.json` still sends (a stale/revoked token fails the `curl` silently — no error surfaces anywhere else), and skim the last year of routine runs for false positives/negatives (e.g. Rule 9 issues that fired on noise, or earnings releases that were missed).

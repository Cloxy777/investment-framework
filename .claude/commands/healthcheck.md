---
description: Check that every external integration this framework depends on is reachable; report only on failure
---

Run an INTEGRATION HEALTHCHECK for cloxy777/investment-framework. This command is deliberately minimalistic: it produces **no output at all when everything is fine**. It exists to catch a broken connector/token/endpoint before it silently breaks one of the scheduled Routines (see [automation-schedule.md](../../framework/automation-schedule.md)).

## Checks

Checks 1 and 2 are MCP-only — no standalone script can call `get_account_summary` or `get_me` (see [scripts/TOKEN-OPTIMIZATION-PLAN.md](../../scripts/TOKEN-OPTIMIZATION-PLAN.md) finding #1) — perform them yourself first:

1. **Interactive Brokers connector** — call `get_account_summary` for account `U19421206`. Pass = account data returned. Fail = auth/connection error (see [sync-sop.md](../../portfolio/sync-sop.md) Troubleshooting: "disconnect/reconnect the MCP in Settings → Connections, complete OAuth").
2. **GitHub connector** — call `get_me`. Pass = authenticated user returned. (If this one fails, note it in the run's own output — nothing on this list can be reported as a GitHub issue in that case; that's this check's one blind spot.)

Then run `python -m scripts.healthcheck --ibkr-result '{"passed": <bool>, "detail": "..."}' --github-result '{"passed": <bool>, "detail": "..."}'` (inline JSON or a file path for either flag) to run checks 3–7 itself and combine all 7 into one pass/fail report — paste its output. It performs:

3. **Yahoo Finance market data (`yfinance`)** — fetches a stable liquid ticker's last price.
4. **FRED (10Y Treasury yield)** — fetches `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10`.
5. **Telegram Bot API** — calls `getMe` (never `sendMessage` — this check must not ping the chat).
6. **Telegram monitored channels** — checks each channel listed in [`portfolio/snapshots/telegram-watch.md`](../../portfolio/snapshots/telegram-watch.md) (pass `--telegram-watch-file` if it isn't at the script's default path) for HTTP 200.
7. **IBKR ticker lookup CSV** — fetches `https://www.interactivebrokers.com/download/fracshare_stk.csv`, checking for a non-empty response with the expected `#SYMBOL,...` header row.

If the script's own checks 1/2 inputs are missing, it hard-fails naming exactly what's missing (per CLAUDE.md's "never invent or estimate") rather than reporting a guessed pass/fail — that's the same stop-and-supply-it signal as everywhere else; go back and run the MCP calls above.

## Reporting

- **All checks pass:** print a single confirmation line to this run's own output (e.g. `Healthcheck 2026-07-04: 7/7 integrations OK.`) and stop. No file write, no commit, no PR. If an open healthcheck issue exists from a previous failing run (see below), add one "recovered" comment noting which checks came back and close it — otherwise do nothing further.
- **One or more checks fail:** search open GitHub issues labeled `integration-healthcheck` (create the label first if it doesn't exist yet).
  - **No open issue found:** create one titled `Integration Healthcheck: <N> failing` with a table — Check | Status | Detail | Suggested fix — for every failing check, labeled `integration-healthcheck`.
  - **An open issue already exists:** don't create a duplicate. Add a comment with today's date and the current failure table (call out anything newly failing vs. still failing vs. newly recovered since the last comment). Update the issue title's `<N> failing` count if it changed.

Never open a PR, write a session log, or touch any repo file for this command — its only possible artifacts are the single `integration-healthcheck`-labeled issue (opened, commented on, or closed) described above.

Success = all 7 checks ran; a clean run left no trace beyond its one confirmation line (and closed any stale healthcheck issue); a failing run leaves exactly one open, current GitHub issue describing what's broken and nothing else.

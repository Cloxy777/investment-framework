---
description: Check that every external integration this framework depends on is reachable; report only on failure
---

Run an INTEGRATION HEALTHCHECK for cloxy777/investment-framework. This command is deliberately minimalistic: it produces **no output at all when everything is fine**. It exists to catch a broken connector/token/endpoint before it silently breaks one of the scheduled Routines (see [automation-schedule.md](../../framework/automation-schedule.md)).

## Checks

Run all of these independently — one failing must not skip the rest. Record a pass/fail + one-line detail for each.

1. **Interactive Brokers connector** — call `get_account_summary` for account `U19421206`. Pass = account data returned. Fail = auth/connection error (see [sync-sop.md](../../portfolio/sync-sop.md) Troubleshooting: "disconnect/reconnect the MCP in Settings → Connections, complete OAuth").
2. **GitHub connector** — call `get_me`. Pass = authenticated user returned. (If this one fails, note it in the run's own output — nothing on this list can be reported as a GitHub issue in that case; that's this check's one blind spot.)
3. **Yahoo Finance market data (`yfinance`)** — `pip install --quiet yfinance`, then fetch a stable liquid ticker: `yf.Ticker("AAPL").fast_info["last_price"]`. Pass = a numeric price is returned.
4. **FRED (10Y Treasury yield)** — fetch `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10`. Pass = the most recent row has a non-blank value.
5. **Telegram Bot API** — `curl -s "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/getMe"`. Pass = `"ok":true`. Use `getMe`, not `sendMessage` — this check must not ping the chat.
6. **Telegram monitored channels** — for each channel listed in [`portfolio/snapshots/telegram-watch.md`](../../portfolio/snapshots/telegram-watch.md) (currently `t.me/tarasguk`, `t.me/FinnInvestChannel`, `t.me/myroslavkorol`, `t.me/bolshegold`): `curl -s -o /dev/null -w "%{http_code}" "https://t.me/s/<channel>"`. Pass = HTTP 200.
7. **IBKR ticker lookup CSV** — fetch `https://www.interactivebrokers.com/download/fracshare_stk.csv`. Pass = non-empty response with the expected `#SYMBOL,...` header row.

## Reporting

- **All checks pass:** print a single confirmation line to this run's own output (e.g. `Healthcheck 2026-07-04: 7/7 integrations OK.`) and stop. No file write, no commit, no PR. If an open healthcheck issue exists from a previous failing run (see below), add one "recovered" comment noting which checks came back and close it — otherwise do nothing further.
- **One or more checks fail:** search open GitHub issues labeled `integration-healthcheck` (create the label first if it doesn't exist yet).
  - **No open issue found:** create one titled `Integration Healthcheck: <N> failing` with a table — Check | Status | Detail | Suggested fix — for every failing check, labeled `integration-healthcheck`.
  - **An open issue already exists:** don't create a duplicate. Add a comment with today's date and the current failure table (call out anything newly failing vs. still failing vs. newly recovered since the last comment). Update the issue title's `<N> failing` count if it changed.

Never open a PR, write a session log, or touch any repo file for this command — its only possible artifacts are the single `integration-healthcheck`-labeled issue (opened, commented on, or closed) described above.

Success = all 7 checks ran; a clean run left no trace beyond its one confirmation line (and closed any stale healthcheck issue); a failing run leaves exactly one open, current GitHub issue describing what's broken and nothing else.

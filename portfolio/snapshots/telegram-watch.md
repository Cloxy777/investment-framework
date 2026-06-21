# Telegram Stock-Mention Watch

> State file for [Routine 6 — Telegram Stock-Mention Scan](../../framework/automation-schedule.md#routine-6--telegram-stock-mention-scan) (`/telegram-scan`). Overwritten in place each run — git history preserves prior state, same convention as [ibkr.md](ibkr.md) and [ibkr-orders.md](ibkr-orders.md). Tracks the last-seen post per monitored channel (so no post is reprocessed or silently skipped) plus a running log of every company mention the command has evaluated, whether or not it triggered an action.

## Monitored channels

| Channel | Last-seen post (UTC) | Last checked |
|---|---|---|
| https://t.me/tarasguk | — (not yet run) | — |
| https://t.me/FinnInvestChannel | — (not yet run) | — |
| https://t.me/myroslavkorol | — (not yet run) | — |
| https://t.me/bolshegold | — (not yet run) | — |

## Mention log

*(most recent first — one row per ticker mention evaluated, whether or not it triggered an action)*

| Date | Channel | Ticker | Action | Note |
|---|---|---|---|---|
| — | — | — | — | No runs yet — seeded empty ahead of the first `/telegram-scan` / Routine 6 execution (see [decisions/2026-06-21-automation-routine-telegram-scan.md](../../decisions/2026-06-21-automation-routine-telegram-scan.md)) |

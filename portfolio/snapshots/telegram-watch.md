# Telegram Stock-Mention Watch

> State file for [Routine 6 — Telegram Stock-Mention Scan](../../framework/automation-schedule.md#routine-6--telegram-stock-mention-scan) (`/telegram-scan`). Overwritten in place each run — git history preserves prior state, same convention as [ibkr.md](ibkr.md) and [ibkr-orders.md](ibkr-orders.md). Tracks the last-seen post per monitored channel (so no post is reprocessed or silently skipped) plus a running log of every company mention the command has evaluated, whether or not it triggered an action.

## Monitored channels

| Channel | Last-seen post (UTC) | Last checked |
|---|---|---|
| https://t.me/tarasguk | tarasguk/11148 (~17:04 UTC, 2026-06-21) | 2026-06-21 17:52 UTC |
| https://t.me/FinnInvestChannel | FinnInvestChannel/2807 (~16:23, 2026-06-21) | 2026-06-21 17:52 UTC |
| https://t.me/myroslavkorol | myroslavkorol/2471 (~10:38 UTC, 2026-06-21) | 2026-06-21 17:52 UTC |
| https://t.me/bolshegold | bolshegold/9601 (~15:25 UTC, 2026-06-21) | 2026-06-21 17:52 UTC |

## Mention log

*(most recent first — one row per ticker mention evaluated, whether or not it triggered an action)*

| Date | Channel | Ticker | Action | Note |
|---|---|---|---|---|
| 2026-06-21 | https://t.me/tarasguk | — | no action — no resolvable company named | Marker advanced from tarasguk/11146 to tarasguk/11148 (~17:04 UTC). Gap from the prior marker (~15:54 UTC) exceeds ~1 hour — post 11147 doesn't appear in the preview at all (this channel has other numbering gaps too, e.g. 11135→11138; likely a deleted/non-rendering post, not evidence of a missed company mention, but noting per command step 2 since it can't be individually verified). New top post (#11148) is a video-announcement teaser summarizing H1 2026 (chip-makers vs. hyperscalers) — no specific ticker named, no action. |
| 2026-06-21 | https://t.me/bolshegold | — | baseline seeded | First run for this channel — no prior marker to diff against (per command step 2). Marker set to bolshegold/9601. Post itself is generic "market opens tomorrow, chill" commentary — no company/ticker named, would not have actioned even outside baseline pass. |
| 2026-06-21 | https://t.me/myroslavkorol | — | baseline seeded | First run for this channel. Marker set to myroslavkorol/2471. Post is a one-line joke ("чим би дитя не тішилось") — no company/ticker named. |
| 2026-06-21 | https://t.me/FinnInvestChannel | — | baseline seeded | First run for this channel. Marker set to FinnInvestChannel/2807. Post is macro commentary on AI data-center electricity demand (citing Yahoo Finance) — no specific company/ticker named, generic macro theme only. |
| 2026-06-21 | https://t.me/tarasguk | — | baseline seeded | First run for this channel. Marker set to tarasguk/11146. Post is political commentary (Trump/Johnson) — unrelated to any company. |

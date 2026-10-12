# Weekly Portfolio Brief — week of 2026-10-11

## 0. Process notes
- The stored routine prompt says "commit straight to main" and to use EODHD. Both conflict with the current [sync-sop.md](../../portfolio/sync-sop.md) (changes go via a `claude/` branch + PR) and [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md). This run used a branch + PR (direct-merge fallback). Please update the stored prompt.
- The `EODHD_API_KEY` is set and was called once for the earnings calendar (it returned "EOD data only for free users"). That key is flagged compromised/retired (see #582); it was not used further.

## 1. Sync results (IBKR, account U19421206)
- Full IBKR sync run: positions, balances, orders. Ticker-lookup CSV fetched live (HTTP 200), identical to the stored fallback, so no CSV change.
- **No position changes** vs. the earlier 2026-10-11 sync: same 27 rows (25 stocks + LM8, BULL short put counted among them). Only prices moved.
- Net Liquidation $57,211.16 → **$57,251.48** (+$40.32). Total Cash **$5,463.46** (USD $602.23, EUR €3,747.94, AUD A$951.80). Combined with Freedom24 (not resynced, 2026-08-22 figures): **$68,141.44**.
- **Orders:** identical to the earlier sync — 8 working. Still no live NKE sell order (only a `REPLACED` one); SPOT (position + order) and the TLT short-call order remain absent.
- Still unresolved: undocumented ADBE doubling and BKNG fill; unexplained EUR/AUD cash appearance (+$5.3k); ungoverned RGL/MBGL/LM8/BULL positions; UUUU short-put order with no holding or evaluation (~$2,550 assignment exposure).
- Watchlist reconciliation: no positions added or removed vs. the last sync, so none needed.

## 2. Upcoming earnings (next 7 days, 2026-10-11 → 10-18)
**Not obtained this run.** EODHD returned an EOD-only plan error and `yfinance` isn't installed in this environment. This is a data gap, not a "nothing due" result. No holding is known to report this week; confirm manually if needed.

## 3. Overdue `rescore-due` issues
- **#801 RBRK** and **#802 ZS** — due 2026-09-17, now 24 days past due by date. Both were rescored on 2026-10-11 per [holdings.md](../../portfolio/holdings.md) (sessions `2026-10-11-rescore-rbrk.md` / `-zs.md`), so they look closeable. Housekeeping: close them.
- #870 NKE was rescored 2026-10-11 (not overdue).

## 4. Quarterly / annual items
None. Today (Oct 11) is outside the first 7 days of October, so the Q4 Rate Environment Gate Review (Routine 3) was due last week, not this one.

## Glossary
- **Net Liquidation:** total account value (positions + cash) as reported by the broker.
- **Rule 9:** the framework's event-triggered re-score rule (earnings or unexplained >15% move).
- **`REPLACED` order:** an order superseded by a modified one; not live.
- **Rate Environment Gate:** the framework's quarterly interest-rate regime check.
- **Ungoverned position:** a holding entered outside the framework's rules, tracked in override-log.md.

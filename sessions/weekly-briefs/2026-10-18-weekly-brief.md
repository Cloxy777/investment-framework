# Weekly Portfolio Brief — week of 2026-10-18

## 0. Process notes
- The stored prompt says "commit straight to main"; per [sync-sop.md](../../portfolio/sync-sop.md) and the designated session branch, this run committed to a `claude/` branch and merged via PR.
- `EODHD_API_KEY` is set, but EODHD is retired and its key flagged compromised ([decisions/2026-06-19](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), #582). One earnings-calendar call returned HTTP 403 (free tier); it was not used further. Earnings were checked with `yfinance` instead.

## 1. Sync results (IBKR, account U19421206)
- Full sync run (positions, balances, orders). Ticker CSV fetched live (HTTP 200); stored fallback refreshed. Scope guard passed (no RGL/LM8/TLT).
- Net Liquidation $48,635.06 → **$47,820.23** (-$814.83, -1.7%). Total Cash **$2,961.09** (was $5,465.45).
- **🚨 UUUU: new 300-share position ($2,541, 5.31%).** The 3 short Oct-16 $8.50 puts expired in the money and were assigned (~$2,550 outlay). **USD cash is now -$1,904.32** (margin debit) while €3,748 and A$952 sit idle. UUUU has a 2026-09-10 evaluation but no decision to hold it as a position.
- **New SOFI Oct30'26 $13 short put (1 contract)** — ungoverned option position, no evaluation or order on file.
- **AVGO order split:** BUY 5 @ 265.34 → `REPLACED`; now BUY 1 @ 266 and BUY 1 @ 243 (placed 2026-10-12).
- Other 24 rows: share counts unchanged; MSFT weight 18.90% of NLV.
- Unchanged/still open: NKE has no live sell order (only `REPLACED`); MA/NOW/V buys (placed 2026-07-05) undocumented; SPOT and TLT short-call order absent; undocumented ADBE/BKNG trades.
- Watchlist: UUUU moved `not-in-portfolio/` → `in-portfolio/`.

## 2. Upcoming earnings (next 7 days, 2026-10-18 → 10-25)
Via `yfinance` (estimated dates, unconfirmed): **NFLX 2026-10-20**, **META 2026-10-21**. Rule 9 re-scores apply after each print. No other holding found in the window. (EODHD not used — see §0.)

## 3. Overdue `rescore-due` issues
- **#801 RBRK** and **#802 ZS** — due 2026-09-17, past due by date, but both were rescored 2026-10-11 ([holdings.md](../../portfolio/holdings.md)); they look closeable. Not closed by this run.

## 4. Quarterly / annual items
None. Today (Oct 18) is outside the first 7 days of October, so Routine 3 (Quarterly Rate Environment Gate Review) is not due this week.

## Glossary
- **Assignment:** when the buyer of a put you sold exercises it, so you must buy the shares at the strike price.
- **Short put:** an option you sold, obligating you to buy shares at the strike if exercised.
- **Margin debit / negative cash:** borrowing from the broker because cash in a currency is below zero.
- **Net Liquidation (NLV):** total account value (positions + cash) as reported by the broker.
- **`REPLACED` order:** an order superseded by a modified one; not live.
- **Rule 9:** the framework's event-triggered re-score rule (earnings or unexplained >15% move).
- **Rate Environment Gate:** the framework's quarterly interest-rate regime check.

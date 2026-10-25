# Weekly Portfolio Brief — week of 2026-10-25

## 0. Process notes
- The stored prompt says "commit straight to main"; per [sync-sop.md](../../portfolio/sync-sop.md) and the designated session branch, this run committed to a `claude/` branch and landed via PR.
- `EODHD_API_KEY` is set, but EODHD is retired and its key flagged compromised ([decisions/2026-06-19](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), #582). One probe call returned HTTP 403 ("Only EOD data allowed for free users"); it was not used further. Earnings were checked with `yfinance`.

## 1. Sync results (IBKR, account U19421206)
- Full sync run (positions, balances, orders). Ticker CSV fetched live (HTTP 200); stored fallback refreshed. Scope guard passed (no RGL/LM8/TLT).
- Net Liquidation $47,820.23 → **$47,714.19** (-$106.04, -0.2%). Total Cash **$3,852.63** (was $2,961.09); USD cash **+$981.49** (was -$1,904.32).
- **CSGP sold:** the standing SELL 25 @ $35.55 GTC filled 2026-10-22 (realized +$11.73, proceeds $888.75). Position closed; watchlist entry moved `in-portfolio/` → `not-in-portfolio/`. Holdings: 26 → 25 rows.
- **USD margin debit cleared:** 2026-10-19 EUR→USD conversion (sold €1,783 @ 1.1214 ≈ $2,000) plus CSGP proceeds. EUR €1,964 and A$952 still idle.
- **New order:** SELL 300 UUUU @ $8.99 GTC (902130509, placed 2026-10-19) vs. price $7.52 — undocumented in sessions/decisions.
- Share counts otherwise unchanged. SOFI Oct30'26 $13 short put expires **2026-10-30** (this week). MSFT 18.69% of NLV (above 15% cap).
- Still open: NKE has no live sell order (only `REPLACED`); MA/NOW/V buys (2026-07-05) undocumented; SPOT and TLT short-call absent; ADBE (11.06%) and BKNG undocumented trades.

## 2. Upcoming earnings (next 7 days, 2026-10-25 → 11-01)
Via `yfinance` (dates may be estimates): **SPGI 10-27**, **V 10-27**, **GOOG 10-28**, **MSFT 10-28**, **NOW 10-28**, **AMZN 10-29**. Rule 9 re-scores apply after each print (MSFT is the largest position). No others found for current holdings (CSGP, previously 10-27, is no longer held).

## 3. Overdue `rescore-due` issues
- **#912 NFLX** — due 2026-10-23, **overdue** (earnings 2026-10-20; no rescore session since).
- **#913 META** — due 2026-10-26, due tomorrow (not yet overdue).
- **#801 RBRK**, **#802 ZS** — due 2026-09-17; both were rescored 2026-10-11 and look closeable (not closed by this run).

## 4. Quarterly / annual items
None. Today (Oct 25) is outside the first 7 days of October, so Routine 3 (Quarterly Rate Environment Gate Review) is not due this week.

## Glossary
- **Net Liquidation (NLV):** total account value (positions + cash) as reported by the broker.
- **GTC limit order:** an order that stays open until filled/cancelled and only executes at the limit price or better.
- **Short put:** an option you sold, obligating you to buy shares at the strike if exercised.
- **Margin debit / negative cash:** borrowing from the broker because cash in a currency is below zero.
- **Realized P&L:** profit or loss locked in by a sale.
- **`REPLACED` order:** an order superseded by a modified one; not live.
- **Rule 9:** the framework's event-triggered re-score rule (earnings or unexplained >15% move).
- **Rate Environment Gate:** the framework's quarterly interest-rate regime check.

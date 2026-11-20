# Weekly Portfolio Brief — week of 2026-11-15

## 0. Process notes
- The stored prompt says "commit straight to main"; this session is assigned branch `claude/gallant-bohr-u310kb`, so the sync lands via PR (per the SOP and prior runs).
- **Earnings calendar:** `EODHD_API_KEY` is set but the calendar endpoint returns HTTP 403 ("Only EOD data allowed for free users"; EODHD is retired — [decisions/2026-06-19](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). Fallback: IBKR earnings-insight search across all equity holdings for 2026-11-15 → 11-22. That source is partial (an empty result does not mean nothing is scheduled), so check TWS for the rest.

## 1. Sync results (IBKR, account U19421206)
- Full sync run (positions, balances, orders). Ticker CSV fetched live (HTTP 200, 24,352 rows); stored fallback refreshed. Scope guard passed (no RGL/LM8/TLT).
- Net Liquidation $46,477.10 → **$45,697.84** (-1.7%). Unrealized P&L (broker BASE) +$2,463.49 → +$1,716.79.
- **NVDA 40 → 50 sh (+10)**, avg cost $180.64; weight now **18.08%** (largest holding; price $180.00 → $165.20). No other share-count changes (26 rows).
- **Cash:** EUR €1,964 and AUD A$951 are now zero; USD cash **-$12.95** (was -$850.77). Total cash $1,992.38 → -$12.95.
- Price moves: AVGO +17% ($294.94 → $345.00), MBGL +18.5% (earnings 11-12), NVDA -8.2%.
- **Orders (6 working, was 8):** SELL 10 NVDA @ 200.50 and both SNDK buys are gone unfilled. **New: SELL 1 NVDA Dec18'26 $125 put @ 6.10** (undocumented — verify). NVO's SELL 5 @ 45.54 is `REPLACED` with no live successor; **NVO and NKE both have no working sell order.**
- Watchlist reconciliation: no tickers entered or left the portfolio, so no moves between `in-portfolio/` and `not-in-portfolio/`.

## 2. Upcoming earnings (next 7 days)
- **NVDA — 2026-11-17 (after close)**, per IBKR earnings preview. NVDA is 18.08% of NLV, so this is the main event risk of the week.
- Other holdings: no dates found (source partial — see section 0).

## 3. Overdue `rescore-due` issues (as of 2026-11-15)
- **#913 META** — due 2026-10-26
- **#921 SPGI**, **#926 V** — due 2026-10-30
- **#923 MSFT** — due 2026-11-02
- **#929 AMZN**, **#930 TRN** — due 2026-11-03 (3 business days after 10-29)
- **#942 DUOL**, **#943 BKNG** — due 2026-11-06
- **#944 NVO** — due 2026-11-09, but rescored 2026-11-13 ([session](../2026-11-13-rescore-nvo.md)) — closeable
- **#945 UBER**, **#946 UUUU** — due 2026-11-09
- **#801 RBRK**, **#802 ZS** — due 2026-09-17; both rescored 2026-10-11 — closeable
- Open but sessions exist (closeable): **#912 NFLX** ([11-02](../2026-11-02-rescore-nflx.md)), **#924 NOW** ([11-02](../2026-11-02-rescore-now.md)), **#925 GOOG** ([11-12](../2026-11-12-rescore-goog.md))
- Not yet overdue: **#965 MBGL** — due 2026-11-17.

## 4. Quarterly / annual items
None. 2026-11-15 is not in the first 7 days of Jan/Apr/Jul/Oct, so Routine 3 (Quarterly Rate Environment Gate Review) is not due.

## Glossary
- **Net Liquidation (NLV):** total account value (positions + cash) as reported by the broker.
- **Margin debit:** negative cash — borrowed from the broker.
- **GTC limit order:** stays open until cancelled; fills only at the limit price or better.
- **Short put:** an option you sold, obliging you to buy shares at the strike if exercised.
- **`REPLACED` order:** superseded by a modified order; not live.
- **Unrealized P&L:** paper profit or loss on positions still held.
- **Rescore:** re-computing a stock's scores after earnings or a big move.
- **Rate Environment Gate:** the framework's quarterly interest-rate regime check.
- **Scope guard:** the check that no transferred-out ticker (RGL, LM8, TLT) appears in the framework account.

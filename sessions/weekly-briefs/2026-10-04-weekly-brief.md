# Weekly Portfolio Brief — week of 2026-10-04

## 1. Sync results (IBKR, account U19421206)
- Full IBKR sync run: positions, balances, orders. Ticker-lookup CSV re-fetched live (HTTP 200) and the stored fallback refreshed.
- **No position changes:** same 25 tickers and share counts as 2026-09-27. Net Liquidation $50,732.36 → **$50,411.80** (-$320.56, market moves only). Cash $117.37 (USD balance -$138.74 margin debit, EUR €227.49).
- **Orders (8 active):** new NFLX BUY 20 @ 46.97; LM8 BUY 1800 @ 0.30 (not a holding — verify intent); AVGO BUY 5 @ 265.34; GOOG/CSGP sells re-placed under new IDs; TRN BUY 900 cancel completed. MA, NOW, V buys unchanged.
- **⚠️ NKE:** its only order in the fetch (SELL 20 @ 54.44) is `REPLACED` with no live successor — it may have no working sell order. Check TWS.
- Still unresolved from prior weeks: ADBE doubling and BKNG fill (undocumented), SPOT absent (11 syncs), TLT short call order absent.
- Freedom24 snapshot not resynced (manual/screenshot flow); weights use its 2026-08-22 figures.

## 2. Upcoming earnings (next 7 days, 2026-10-04 → 10-11)
None found for current equity holdings. The EODHD calendar call returned 403 (free tier is EOD-only); the EODHD key is also flagged compromised in [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) (see #582), so yfinance earnings dates were used instead.

## 3. Overdue `rescore-due` issues
- **#801 RBRK** — due 2026-09-17, **17 days overdue**
- **#802 ZS** — due 2026-09-17, **17 days overdue**
- Not yet overdue: #870 NKE (due 2026-10-06, earnings 2026-10-01)

## 4. Quarterly / annual items
- **Routine 3 (Quarterly Rate Environment Gate Review) is due this week** (first 7 days of October) — runs itself.

## Glossary
- **Net Liquidation:** total account value (positions + cash) as reported by the broker.
- **Rule 9:** the framework's event-triggered re-score rule (earnings or unexplained >15% move).
- **`REPLACED` order:** an order superseded by a modified one; not live.
- **Margin debit:** negative cash balance, i.e. borrowing from the broker.
- **Rate Environment Gate:** the framework's quarterly interest-rate regime check.

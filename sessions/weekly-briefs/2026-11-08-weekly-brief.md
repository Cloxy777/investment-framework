# Weekly Portfolio Brief — week of 2026-11-08

## 0. Process notes
- The stored prompt says "commit straight to main"; this session is assigned branch `claude/gallant-bohr-ft47rx`, so the sync lands via PR, as the SOP and prior runs did.
- **Upcoming earnings could not be sourced.** `EODHD_API_KEY` is set, but the calendar endpoint returns "Only EOD data allowed for free users" (EODHD is retired — [decisions/2026-06-19](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). `yfinance` could not be installed/imported and Yahoo returned HTTP 429. The IBKR earnings-insight search returned nothing for 11-08 → 11-16. Nothing is invented here; please check dates in TWS. (Last known: NVDA 2026-11-17, outside the window.)

## 1. Sync results (IBKR, account U19421206)
- Full sync run (positions, balances, orders). Ticker CSV fetched live (HTTP 200); stored fallback refreshed. Scope guard passed (no RGL/LM8/TLT).
- Net Liquidation $46,102.05 → **$46,477.10** (+0.8%). Unrealized P&L (broker BASE) +$2,565.09 → +$2,463.49.
- **NVDA 19 → 40 sh (+21)**; weight now **15.49%** (above the 15% single-name figure used in prior flags). **MSFT 17 → 13 sh (-4)**, 19.25% → 14.82%. **New TSM 1 sh** (watchlist moved to `in-portfolio/`). **New short UUUU Jan15'27 $9 call ×3** (against the 300 shares).
- **USD cash +$981.49 → -$850.77 (margin debit)**; total cash $1,992.38 (4.29%). Run `/safe-guard` — three SNDK buys (~$2,360) plus NFLX/AVGO/AMZN buys would deepen it.
- Biggest price moves: DUOL $131.59 → $160.35 (+22%), AVGO $327 → $294.94, NVDA $205.40 → $180.00, AMZN $240.35 → $259.30.
- **Orders (8 working, was 6):** new SELL 10 NVDA @ 200.50, BUY 2 SNDK @ 780, BUY 1 SNDK @ 800 (SNDK not held; its [11-06 evaluation](../2026-11-06-new-position-sndk.md) says no order was placed — verify intent). Gone unfilled: SELL 1 NOW Feb'27 $85 put. NKE still has no live sell order.

## 2. Upcoming earnings (next 7 days)
Unavailable — see section 0.

## 3. Overdue `rescore-due` issues (as of 2026-11-08)
- **#913 META** — due 2026-10-26
- **#921 SPGI** — due 2026-10-30
- **#926 V** — due 2026-10-30
- **#923 MSFT** — due 2026-11-02
- **#929 AMZN**, **#930 TRN** — due 2026-11-03
- **#942 DUOL**, **#943 BKNG** — due 2026-11-06
- **#801 RBRK**, **#802 ZS** — due 2026-09-17; both rescored 2026-10-11 — closeable.
- Open but sessions exist (closeable): **#912 NFLX**, **#924 NOW** ([11-02](../2026-11-02-rescore-now.md)), **#925 GOOG** (10-29).
- Due tomorrow 2026-11-09 (not yet overdue): #944 NVO, #945 UBER, #946 UUUU.

## 4. Quarterly / annual items
None. Today (Nov 8) is not in the first 7 days of Jan/Apr/Jul/Oct, so Routine 3 (Quarterly Rate Environment Gate Review) is not due.

## Glossary
- **Net Liquidation (NLV):** total account value (positions + cash) as reported by the broker.
- **Margin debit:** negative cash — borrowed from the broker.
- **GTC limit order:** stays open until cancelled; fills only at the limit price or better.
- **Short call/put:** an option you sold, obligating you to sell/buy shares at the strike if exercised.
- **Covered call:** a short call backed by shares you own.
- **`REPLACED` order:** superseded by a modified order; not live.
- **Unrealized P&L:** paper profit or loss on positions still held.
- **Rescore:** re-computing a stock's scores after earnings or a big move.
- **Rate Environment Gate:** the framework's quarterly interest-rate regime check.

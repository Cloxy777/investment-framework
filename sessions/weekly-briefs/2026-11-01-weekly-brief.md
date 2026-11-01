# Weekly Portfolio Brief — week of 2026-11-01

## 0. Process notes
- The stored prompt says "commit straight to main"; this session is assigned the `claude/gallant-bohr-r7nrtx` branch, so the sync landed via PR, as the SOP and the previous run did.
- `EODHD_API_KEY` is set, but EODHD is retired ([decisions/2026-06-19](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). The calendar probe returned "Only EOD data allowed for free users" and was not used. Earnings come from `yfinance` (dates may be estimates).

## 1. Sync results (IBKR, account U19421206)
- Full sync run (positions, balances, orders). Ticker CSV fetched live (HTTP 200); stored fallback refreshed. Scope guard passed (no RGL/LM8/TLT).
- Net Liquidation $47,714.19 → **$46,102.05** (-$1,612.14, -3.4%), from price moves: **NOW $158.96 → $106.00 (-33%; verify in TWS)**, ADBE $263.82 → $250.23, DUOL $143.04 → $131.59, AMZN $250.70 → $240.35, NVDA $213.10 → $205.40. Unrealized P&L +$4,198.21 → +$2,565.09.
- Total cash **$3,841.98** (8.33% of NLV); USD cash +$981.49.
- **SOFI Oct30'26 $13 short put expired** 2026-10-30, no assignment. Holdings: 25 → 24 position rows. Watchlist already under `not-in-portfolio/`; no moves needed.
- **Orders (6 working, was 8):** new BUY 1 AMZN @ 216 and SELL 1 NOW Feb19'27 $85 put @ 5.00 (both undocumented). Gone without fills: UUUU SELL 300 @ 8.99, MA BUY, NOW BUY 20 @ 80, V BUY. `REPLACED` with no live successor: NVDA BUY 1 @ 196.70, UUUU Jan'27 $9 call, NKE SELL 20 (still no live NKE sell).
- MSFT 19.25% of NLV (above the 15% cap). ADBE 10.86%.

## 2. Upcoming earnings (next 7 days, 2026-11-01 → 11-08)
Via `yfinance`: **BKNG 11-03**, **DUOL 11-03**, **NVO 11-04**, **UBER 11-04**, **UUUU 11-04**, **TRN 11-04** (TRN likely already reported 2026-10-29 per #930; this date may be a stale estimate). Next after that: NVDA 11-17.

## 3. Overdue `rescore-due` issues (due date before 2026-11-01)
- **#912 NFLX** — due 2026-10-23 (9 days overdue)
- **#913 META** — due 2026-10-26
- **#921 SPGI** — due 2026-10-30
- **#926 V** — due 2026-10-30
- **#801 RBRK**, **#802 ZS** — due 2026-09-17; both were rescored 2026-10-11 ([RBRK](../2026-10-11-rescore-rbrk.md), [ZS](../2026-10-11-rescore-zs.md)) and look closeable.

Due 2026-11-02 (tomorrow): #923 MSFT, #924 NOW, #925 GOOG (GOOG was rescored 2026-10-29, likely closeable). Due 2026-11-03: #929 AMZN, #930 TRN.

## 4. Quarterly / annual items
None. Today (Nov 1) is not in the first 7 days of Jan/Apr/Jul/Oct, so Routine 3 (Quarterly Rate Environment Gate Review) is not due.

## Glossary
- **Net Liquidation (NLV):** total account value (positions + cash) as reported by the broker.
- **GTC limit order:** an order that stays open until cancelled and only fills at the limit price or better.
- **Short put:** an option you sold, obligating you to buy shares at the strike if exercised.
- **Assignment:** being forced to buy (put) or sell (call) shares because an option you sold was exercised.
- **`REPLACED` order:** an order superseded by a modified one; not live.
- **Unrealized P&L:** paper profit or loss on positions still held.
- **Rate Environment Gate:** the framework's quarterly interest-rate regime check.
- **Rescore / Rule 9:** re-computing a stock's valuation score after earnings or a big unexplained move.

# Weekly Portfolio Brief — week of 2026-06-15

**Type:** Weekly Monday Portfolio Sync & Brief
**Sync commit:** [`2176de5`](../../portfolio/snapshots/ibkr.md) — "Sync IBKR portfolio - 2026-06-15"

---

## 1. Portfolio sync — IBKR (account U19421206)

Full IBKR sync (positions, cash balances, active orders) completed via the Interactive Brokers MCP. Ticker resolution: all 22 positions resolved cleanly from `contract_description` — no live/fallback ticker-lookup CSV needed.

**Headline numbers (vs. 2026-06-11 sync):**

| Metric | 2026-06-11 | 2026-06-15 | Change |
|---|---|---|---|
| Net Liquidation (IBKR, BASE) | $38,732.29 | $38,535.57 | -$196.72 |
| Total Cash (USD-equiv, IBKR) | $2,326.77 | $321.57 | -$2,005.20 |
| Unrealized P&L (IBKR, BASE) | -$1,230.54 | -$1,441.53 | -$210.99 |
| Combined total (IBKR + Freedom24) | $53,855.83 | $53,659.11 | -$196.72 |

**Position changes:**

- **New position — ADBE** (10 sh @ avg cost $202.07, now $206.56, +2.22%): partial fill toward the [2026-06-12 new-position](../2026-06-12-new-position-adbe.md) BUY recommendation (Score 5.0, "Very Cheap" — full position 6–8%, ~17-share target ≈ $3,524). 10 of ~17 target shares filled so far; the cash drawdown above (~$2,005) is consistent with this ~$2,021 purchase. `watchlist/ADBE` moved from `not-in-portfolio/` to `in-portfolio/`, and its Last Score (5.0, 12 Jun 2026) was carried into `holdings.md`.
- **No other position-size changes** — all 21 previously-held tickers unchanged in share count; this week's moves are price-driven only. Notable movers (price change since 2026-06-11): STIM +7.26%, ZS +4.47%, NVO +3.26%, NVDA +3.15%, SPOT -4.17%, CSGP -4.06%. None exceed the ±15% Rule 9 threshold.

**Active orders** — unchanged from last week, all still working (`NEW`):

| Side | Ticker | Qty | Limit | TIF |
|---|---|---|---|---|
| SELL | GOOG | 1 | 389.00 | GTC |
| SELL | NKE | 20 | 54.20 | GTC |
| BUY | NOW | 10 | 90.00 | GTC |
| SELL | SPOT | 1 | 518.00 | GTC |
| BUY | V | 9 | 285.20 | GTC |

**Data-quality flag:** Gross Position Value (sum of live position values, $38,605.84) + Total Cash ($321.57) exceeds broker-reported Net Liquidation ($38,535.57) by ~$392 — consistent with today's aggregate intraday unrealized gain (`daily_pnl` sum ≈ +$415.74), i.e. live position prices have moved since NLV was last settled. This makes `holdings.md` weights sum to ~100.7% rather than 100% — flagged in both `ibkr.md` and `holdings.md`, not a calculation error.

---

## 2. Upcoming earnings (next 7 days: 2026-06-15 → 2026-06-22)

**None.** EODHD's earnings-calendar endpoint returned a free-plan restriction ("Only EOD data allowed for free users"), so the `yfinance` fallback (per `framework/valuation-scoring.md`) was used instead — confirmed reachable. Checked all 20 equity holdings (excludes TLT and XEON, non-equity/cash-equivalent):

The nearest upcoming earnings dates are **NKE (2026-06-30)**, NOW (2026-07-22), CSGP (2026-07-21), SPOT (2026-07-28), V (2026-07-28) — all outside this week's window. RBRK (2026-06-04) and ZS (2026-05-26) already reported prior to this window and are reflected in the current `Last Review` dates.

---

## 3. Overdue `rescore-due` issues

**None.** No open GitHub issues carry the `rescore-due` label as of this brief.

---

## 4. Quarterly/annual items due this week

**None.** Per `framework/operating-calendar.md`, the Quarterly Rate Environment Gate Review (Routine 3) runs in the first 7 days of January/April/July/October. 2026-06-15 falls in none of those windows — next due the first week of **July 2026**.

---

## Summary

Routine sync completed cleanly. The only portfolio change this week is the new ADBE position (partial fill, 10/~17 target shares) from last week's "Very Cheap" (Score 5.0) BUY call — no other position-size changes, no overdue rescores, no earnings in the next 7 days, and no quarterly/annual framework items due. One data-quality note (NLV vs. live position value gap, ~$392) flagged for transparency but requires no action.

# Weekly Portfolio Brief — week of 2026-06-22

**Type:** Weekly Monday Portfolio Sync & Brief
**Sync commit:** [`c9c2da3`](https://github.com/cloxy777/investment-framework/commit/c9c2da334a2ddd32bdb01ff1d859acd10f51eb30) — "Sync IBKR portfolio - 2026-06-22"

---

## 1. Portfolio sync — IBKR (account U19421206)

Full IBKR sync (positions, cash balances, active orders) completed via the Interactive Brokers MCP. Ticker resolution: all 23 positions resolved cleanly from `contract_description` — no live/fallback ticker-lookup CSV needed.

**Headline numbers (vs. 2026-06-15 sync):**

| Metric | 2026-06-15 | 2026-06-22 | Change |
|---|---|---|---|
| Net Liquidation (IBKR, BASE) | $38,535.57 | $40,689.53 | +$2,153.96 |
| Total Cash (USD-equiv, IBKR) | $321.57 | $255.99 | -$65.58 |
| Unrealized P&L (IBKR, BASE) | -$1,441.53 | -$1,497.85 | -$56.32 |
| Combined total (IBKR + Freedom24) | $53,659.11 | $55,813.07 | +$2,153.96 |

(Freedom24 leg unchanged at $15,123.54 — last synced 2026-06-07, no new screenshot this round.)

**Headline finding — undocumented override, not just a data refresh:**

- **New position — AVGO** (6 sh @ avg cost $382.44, bought 2026-06-16 @ $382.275): this is a **valuation override**, not a framework-driven buy. The only AVGO evaluation on record — the [2026-06-14 new-position session](../2026-06-14-new-position-avgo.md) — scored it **69.5 (WATCHLIST, explicit "no new entry")** at essentially the same price ($382.07). The buy went in two days later with no `decisions/` entry explaining why. Logged retroactively in [override-log.md](../../portfolio/override-log.md); `watchlist/AVGO` moved `not-in-portfolio/` → `in-portfolio/`. **Flagged for the user to supply the missing rationale** — none was invented.
- **No other position-size changes** — all 22 previously-held tickers unchanged in share count; this week's moves are price-driven only, plus the one new AVGO buy. ADBE remains a partial fill (10 of ~17 target shares toward the [2026-06-12 new-position](../2026-06-12-new-position-adbe.md) BUY).

**Active orders** — 6 working (`NEW`), 4 non-active (`REPLACED`) shown in this fetch:

| Side | Ticker | Qty | Limit | TIF | Note |
|---|---|---|---|---|---|
| SELL | GOOG | 1 | 389.00 | GTC | unchanged |
| BUY | MA | 4 | 464.00 | GTC | new — resolves prior "no live successor" flag |
| SELL | NKE | 20 | 54.20 | GTC | unchanged |
| SELL | SPOT | 1 | 518.00 | GTC | unchanged |
| SELL | STIM | 3 contracts | 0.15 | GTC | new — covered-call options, not shares |
| BUY | V | 9 | 285.20 | GTC | re-issued under a new order ID, same terms |

**Order data-quality flag:** the previously-active **NOW BUY 10 @ $90.00** order no longer appears in `get_account_orders` under any status. The NOW position is unchanged (still 12 shares, same avg cost), which confirms the order did **not** fill — but whether it's still working outside the fetch's visible window, or was actually cancelled, cannot be determined from this data. Not guessed either way; flagged for manual TWS/Client Portal verification. The endpoint also returned only 10 total orders this sync (vs. 14 last time), so this may recur.

**Gross Position Value data-quality flag:** Gross Position Value ($40,233.26) + Total Cash ($255.99) = $40,489.25, ~$200.28 *below* broker-reported Net Liquidation ($40,689.53) — the opposite direction from the prior sync's gap. A timing mismatch between live intraday position pricing and settled NLV, not a calculation error. Makes `holdings.md` weights sum to ~99.7% rather than 100%.

---

## 2. Upcoming earnings (next 7 days: 2026-06-22 → 2026-06-29)

**None.** `EODHD_API_KEY` is not set in this environment, and per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) EODHD has been fully retired from this routine — checked via `yfinance` (`get_earnings_dates()`) across all 21 equity holdings (excludes TLT and XEON, non-equity/cash-equivalent).

The nearest upcoming earnings date is **NKE (2026-06-30)** — one day outside this week's window. Next nearest: NFLX (2026-07-16), CSGP (2026-07-21), NOW (2026-07-22), GOOG (2026-07-23), SPOT/V (2026-07-28), META/MSFT (2026-07-29), AMZN/SPGI (2026-07-30).

---

## 3. Overdue `rescore-due` issues

**None.** No open GitHub issues carry the `rescore-due` label as of this brief.

---

## 4. Quarterly/annual items due this week

**None.** Per `framework/operating-calendar.md`, the Quarterly Rate Environment Gate Review (Routine 3) runs in the first 7 days of January/April/July/October. 2026-06-22 falls in none of those windows — next due the first week of **July 2026** (also when the Q3 FY2026 AVGO earnings review and its overdue rescore both land, see below).

---

## Summary

The sync itself was routine — Net Liquidation rose $2,153.96 on price action, no overdue rescores, and no earnings in the next 7 days. The substantive finding is governance, not market movement: a 6-share **AVGO** position was bought 2026-06-16 directly against the only scoring this framework ever produced for it (69.5, WATCHLIST, "no new entry," scored 2 days earlier at essentially the same price), with no `decisions/` record of why. It has been flagged everywhere the framework's own rules require — `override-log.md`, `holdings.md`, `ibkr.md`, and a new `watchlist/in-portfolio/AVGO` entry — but the override's rationale is still **not on record**, and AVGO's 69.5 score now also predates the 2026-06-20 Upside/Downside Modifier change, so it isn't even comparable to the rest of the book on the current scale. Two things need the user directly: supply the override rationale (for `decisions/` and `override-log.md`), and run a fresh `/rescore AVGO`.

---

## Glossary

- **CapEx, EBIT, EPS, FCF, FV (Fair Value), GAAP, PE ratio** — see [glossary.md](../../framework/glossary.md) for standard definitions used throughout this framework's sessions.
- **FX (foreign exchange) rate** — the price of converting one currency into another; used here only for XEON's EUR-denominated position and the EUR cash balance, both converted using IBKR's own live-reported rate, never assumed.
- **GTC (Good-Til-Cancelled)** — an order instruction telling the broker to keep a limit order open indefinitely until it fills or is cancelled.
- **Human Override** — a position opened or held outside the framework's own rules (e.g. bought at a valuation score of 50.0+, the WATCHLIST/Expensive zone). Tracked for life in `override-log.md`.
- **NLV (Net Liquidation Value)** — a broker's headline account value: all positions at current market price, plus cash, minus liabilities.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation regardless of schedule (earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move).
- **Unrealized P&L** — the paper gain or loss on positions still held, before any tax or trading cost, calculated against the broker's recorded average cost.
- **Valuation score** — this framework's 0.0–100.0 continuous score (0 = cheapest, 100.0 = most expensive) combining quality and valuation sub-scores plus the Rate Environment Gate; see `framework/valuation-scoring.md`.
- **WATCHLIST (action band)** — the framework's recommendation for a valuation score of 50.0–69.9: fairly-to-fully valued, rule is "no new entry."

# Weekly Monday Portfolio Sync & Brief — 2026-07-05

**Task type:** Routine 2 (Weekly Monday Portfolio Sync & Brief)
**Scope:** `/sync-portfolio` (IBKR positions + cash balances + active orders), earnings look-ahead, overdue `rescore-due` check, quarterly/annual visibility check.

---

## 0. ⚠️⚠️ Headline finding — unauthorized live IBKR orders, flagged directly to the user

This sync's `get_account_orders` pull surfaced **six live orders with no authorization anywhere in this repo** (`sessions/`, `decisions/`, `override-log.md`) — two of them directly contradict this framework's own published "do not trade" conclusions. A push notification was sent to the user as soon as this was confirmed, ahead of finishing the rest of this sync.

| Ticker | Order | Contradicts | Detail |
|---|---|---|---|
| **HDSN** | BUY 200 @ $4.96 (~$992) | [2026-07-03 new-position session](../2026-07-03-new-position-hdsn.md) | **PASS** — Quality Score 24.7, needs 80.0+. No order should exist for this ticker at all. |
| **MA** | BUY 4 @ $464.00 (~$1,856) | [2026-06-22 rescore](../../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) | **"Trade does NOT execute"** — R/R 1.33:1, below the 2:1 minimum. Live since 2026-06-16, silently re-issued under a new order ID today. |
| **V** | BUY 9 @ $285.00 (~$2,565) | [2026-07-05 rescore](../2026-07-05-rescore-v.md) | HOLD, R/R fails 2:1. Also live since 2026-06-16, re-issued today. |
| **PDD** | BUY 10 @ $72.55 (~$726) | [2026-07-01 new-position session](../2026-07-01-new-position-pdd.md) | Recommended ~44 sh at a $128.74 ceiling — this order's size/price don't match. |
| **NOW** | BUY 20 @ $80.00 (duplicate) | — | Identical order already existed since 2026-06-25 — a straight duplicate. |
| **META** | BUY 1 @ $579.85, SELL 1 @ $611.01 ×2 (one an exact duplicate) | — | Continues the undocumented 1-share GTC pattern first flagged 2026-07-04 (4 prior orders from 07-03, still unresolved), with more added today. |

**None of the six have filled** — this is order-level exposure, not a realized position change. Combined new/incremental worst-case buy exposure ≈ **$7,700**, on top of the still-open 57,214-share **RGL** order (ungoverned position, flagged since 2026-07-01) and the still-unexplained **MBGL** 1-share position. This pattern has been recurring and escalating weekly since AVGO's 2026-06-16 override, flagged in every rebalance session since, with no resolution yet.

**No tool in this repo places, modifies, or cancels a broker order** — this needs the user's direct action in TWS/Client Portal. Full per-order detail in [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md).

---

## 1. Portfolio sync (IBKR, account U19421206)

| Metric | 2026-06-28 | 2026-07-05 | Change |
|---|---|---|---|
| Net Liquidation (IBKR, BASE) | $39,767.94 | $43,102.67 | +$3,334.73 |
| Total Cash (USD-equiv, IBKR) | -$1,576.85 | $342.69 | +$1,919.54 |
| Unrealized P&L (IBKR, BASE) | -$2,406.48 | -$1,049.34 | +$1,357.14 |
| Combined total (IBKR + Freedom24) | $54,891.48 | $58,226.21 | +$3,334.73 |

**Ticker resolution:** the live IBKR ticker-lookup CSV (`fracshare_stk.csv`) fetched successfully this sync and the stored fallback (`portfolio/reference/ibkr-ticker-lookup.csv`) was refreshed from it. It confirmed **MBGL = Mobility Global Inc** (NYSE, contract 893054611).

**Position changes since 2026-06-28:**
- **RGL** and **MBGL** (both first surfaced in the 2026-07-01 rebalance session, still open — see §0 and [override-log.md](../../portfolio/override-log.md)) now formally added to [holdings.md](../../portfolio/holdings.md) as tracked "not scored — ungoverned" rows, since this is the first `/sync-portfolio` pass since they were discovered.
- **Cash swung from –$1,576.85 to +$342.69** — the GBP cash balance that funded the TRN purchase (previously –£1,271.71) is now near-zero (+£0.28). The resolving trade/transfer isn't visible in a balances-only pull; flagged as resolved but not independently investigated this sync.
- **AVGO's 2026-06-16 override has since been resolved via a full rescore** (2026-07-04: Quality 82.1, Composite 43.1) — `override-log.md`'s "Open — under review" status line is stale text, though the score itself is current. Correcting that log entry is outside `/sync-portfolio`'s scope; flagged for housekeeping.
- No other position-size changes among previously-tracked tickers (ADBE and TRN remain partial fills at unchanged share counts); all other market-value movement is price-driven.

**Watchlist reconciliation:** no `in-portfolio/`⇄`not-in-portfolio/` moves needed — RGL and MBGL never had `not-in-portfolio/` folders to move from (they were never evaluated via `/new-position`), and no other holding's `in`/`not-in` status changed this sync.

---

## 2. Upcoming earnings (next 7 days: 2026-07-05 → 2026-07-12)

**Could not be checked this run — data gap, not invented.** `yfinance`'s underlying HTTP client (`curl_cffi`, used for browser-TLS-fingerprint impersonation) fails to complete a TLS handshake through this session's egress proxy (`Recv failure: Connection reset by peer`, reproduced with an explicit proxy override and confirmed as a client/proxy TLS incompatibility, not a transient network blip). A plain `requests`-based fallback against Yahoo's `quoteSummary` endpoint reached the proxy successfully but returned `401 Invalid Crumb` (Yahoo now requires an auth cookie/crumb this simple approach doesn't obtain). No earnings dates are guessed or carried forward from memory.

**Per the operating brief's Rule 0, this is reported as a gap rather than invented.** Recommend the next `/healthcheck` run (Routine 7, daily) confirm whether this is a persistent environment issue or transient. Known dates from the last successful check (2026-06-28 brief): NKE reported 2026-06-30 (already passed, before this window); no other holding's next date is confirmed.

---

## 3. Overdue `rescore-due` issues

**None.** No open GitHub issue in this repo carries the `rescore-due` label.

---

## 4. Quarterly/annual items due this week

**Routine 3 (Quarterly Rate Environment Gate Review) fell due this week** (2026-07-05 is within the first 7 days of July) **and has already run**, for visibility: see [sessions/quarterly/2026-Q3-rate-environment-review.md](../quarterly/2026-Q3-rate-environment-review.md) (10Y = 4.38%, band unchanged, no portfolio-wide re-score triggered). No further action needed from this sync.

---

## Glossary

- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50.
- **FX (foreign exchange) rate:** the price of converting one currency into another; this framework only uses live, broker-reported FX rates, never an assumed rate, per Rule 0.
- **GTC (Good-Til-Cancelled):** a standing limit order that stays open until it fills or is manually cancelled.
- **Human Override:** a position or order entered outside the framework's own rules, tracked in `override-log.md`.
- **NLV (Net Liquidation Value) / NAV (Net Asset Valuation):** a broker's headline account value — all positions at current market price, plus cash, minus liabilities.
- **Quality Score:** this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to proceed to valuation scoring.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss) on a trade; this framework requires at least 2:1 before entering.
- **REPLACED / PARTIALLY_FILLED (order status):** IBKR order-lifecycle statuses — `REPLACED` means the order was superseded by a new order; `PARTIALLY_FILLED` means some but not all of the order quantity has executed.
- **Rule 0:** this framework's non-negotiable rule to never invent or estimate financial data — flag the gap and ask instead.
- **Rule 9:** the framework's mandatory-rescore trigger table (earnings, guidance, M&A, management change, macro shift, >15% unexplained move).
- **Rule 10:** this framework's requirement that every session be saved and every trade documented, for auditability.

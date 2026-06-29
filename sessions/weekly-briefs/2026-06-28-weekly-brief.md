# Weekly Portfolio Brief — week of 2026-06-28

**Type:** Weekly Monday Portfolio Sync & Brief
**Sync commit:** [`a71f834`](https://github.com/cloxy777/investment-framework/commit/a71f834fad0aed6fc1a1df21c725837cb776cf18) — "Sync IBKR portfolio - 2026-06-28"

---

## 1. Portfolio sync — IBKR (account U19421206)

Full IBKR sync (positions, cash balances, active orders) completed via the Interactive Brokers MCP. Ticker resolution: all 25 positions resolved directly from `contract_description` — `XEON @IBIS2` and `TRN @LSE` normalized for consistency with `holdings.md`; no live/fallback ticker-lookup CSV needed.

**Headline numbers (vs. 2026-06-22 sync):**

| Metric | 2026-06-22 | 2026-06-28 | Change |
|---|---|---|---|
| Net Liquidation (IBKR, BASE) | $40,689.53 | $39,767.94 | -$921.59 |
| Total Cash (USD-equiv, IBKR) | $255.99 | -$1,576.85 | -$1,832.84 |
| Unrealized P&L (IBKR, BASE) | -$1,497.85 | -$2,406.48 | -$908.63 |
| Combined total (IBKR + Freedom24) | $55,813.07 | $54,891.48 | -$921.59 |

(Freedom24 leg unchanged at $15,123.54 — last synced 2026-06-07, no new screenshot this round.)

**Headline finding — new position, framework-compliant (not an override):**

- **New position — TRN** (Trainline plc, LSE: 600 sh @ avg cost GBP 2.1195, bought 2026-06-24): a **framework-compliant partial-fill BUY**, not an override. [watchlist/in-portfolio/TRN/TRN-2026-06-24.md](../../watchlist/in-portfolio/TRN/TRN-2026-06-24.md) carries a score of **10.0 — BUY, Full position 6–8%**, from a Rule 9 management-change re-run (Trainline CEO succession). Target size from [sessions/2026-06-24-new-position-trn.md](../2026-06-24-new-position-trn.md) is ≈1,553 shares (≈$4,191.30); 600 filled so far — same partial-fill pattern already established for ADBE (10 of ~17 target shares). `watchlist/not-in-portfolio/TRN/` moved to `watchlist/in-portfolio/TRN/`; two links left stale by that move (in `sessions/2026-06-24-new-position-trn.md` and `portfolio/snapshots/telegram-watch.md`) were corrected in this sync.
- **Cash funding flag — GBP went negative, not an FX conversion:** Total Cash swung from +$255.99 to **-$1,576.85**. The TRN purchase was funded by letting the **GBP cash balance go negative** (-£1,271.71, exactly matching the TRN fill's net cost) rather than via an explicit USD→GBP conversion trade — effectively margin borrowing in GBP. GBP-side Net Liquidation is now slightly negative (-$8.34). Not a framework violation (cash management is outside the valuation/sizing rules), but flagged for a deliberate decision on whether to convert USD→GBP to cover it.
- **STIM growth resolves prior order-window flags, no new governance flag:** stock position grew 345→500 shares, and a new 5-contract short covered call appeared (`STIM Aug21'26 $2.50 CALL`, -5 contracts, sold @ $0.06). Both fills supersede orders already flagged in the 2026-06-22 sync and are consistent with the ongoing covered-call income strategy (fully covered by the 500-share position).
- **AVGO's 2026-06-16 override remains open and unresolved** — see [override-log.md](../../portfolio/override-log.md). No rationale has been supplied yet; carried forward, not re-litigated this sync. AVGO's 69.5 score also still predates the 2026-06-20 Upside/Downside Modifier change.
- **No other position-size changes** — all other previously-held tickers show identical share counts; only prices moved.

**Active orders** — 6 working (`NEW`), 3 non-active (`REPLACED`, none with a live successor visible) shown in this fetch:

| Side | Ticker | Qty | Limit | TIF | Note |
|---|---|---|---|---|---|
| SELL | GOOG | 1 | 389.00 | GTC | unchanged |
| BUY | MA | 4 | 464.00 | GTC | unchanged |
| SELL | NKE | 20 | 54.20 | GTC | unchanged |
| BUY | NOW | 20 | 80.00 | GTC | new — resolves prior "no live successor" flag (larger size, lower price than the prior order) |
| SELL | SPOT | 1 | 518.00 | GTC | unchanged |
| BUY | V | 9 | 285.20 | GTC | unchanged |

**Order data-quality flag — new:** order 1551402669 (`Buy 900 TRN` @ GBX 161.50, placed 2026-06-24) shows status `REPLACED` with `cum_shares_qty: 0` (never filled) and no live successor visible in this fetch. The 600 TRN shares actually held came from a separate order that filled the same morning at a different limit. Whether this 900-share order (an apparent attempt at the remaining ~953 shares toward the TRN target) was re-replaced, cancelled, or simply aged out of the endpoint's visible window **cannot be determined from this data alone** — needs manual TWS/Client Portal verification if completing the TRN position to full target size is still intended.

**Persisting order flags (unchanged since 2026-06-22, now 4 weeks stale for CSGP/TLT):** CSGP (SELL 25 @ 35.50, since 2026-05-26) and TLT (BUY 13 @ 83.54, since 2026-06-01) still show only a `REPLACED` order with no live successor.

**Gross Position Value data-quality flag:** Gross Position Value ($41,334.34) + Total Cash (-$1,576.85) = $39,757.49, ~$10.45 *below* broker-reported Net Liquidation ($39,767.94) — consistent with the live/intraday-position-pricing vs. settled-NLV timing mismatch noted in prior syncs, not a calculation error. Makes `holdings.md` weights sum to ~100.1% rather than 100%.

---

## 2. Upcoming earnings (next 7 days: 2026-06-28 → 2026-07-05)

**NKE — 2026-06-30.** Checked via `yfinance` (`get_earnings_dates()`) across all 22 equity holdings (excludes TLT, XEON — non-equity/cash-equivalent; `EODHD_API_KEY` is not set, and per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) EODHD has been fully retired from this routine). NKE's earnings fell one day *outside* last week's window (2026-06-30 vs. the 2026-06-22→2026-06-29 window) — it is now inside this week's window and due for a Rule 9 post-earnings re-score once results are out.

No other holding has earnings in the next 7 days. Next nearest after NKE: NFLX (2026-07-16), CSGP (2026-07-21), NOW (2026-07-22), GOOG (2026-07-23), SPOT/V (2026-07-28), META/MSFT (2026-07-29), AMZN/SPGI (2026-07-30).

---

## 3. Overdue `rescore-due` issues

**None.** No open GitHub issues carry the `rescore-due` label as of this brief (verified live).

---

## 4. Quarterly/annual items due this week

**None.** Per `framework/operating-calendar.md`, the Quarterly Rate Environment Gate Review (Routine 3) runs in the first 7 days of January/April/July/October. 2026-06-28 falls in none of those windows — next due the first week of **July 2026** (also when AVGO's overdue rescore should land).

---

## Summary

The week's substantive event is the new **TRN** position — a clean, framework-compliant Rule 9 buy (Trainline CEO succession triggered a re-score to 10.0/BUY), not an override, currently a 600-of-~1,553-share partial fill. It was funded by letting GBP cash go negative rather than an explicit FX conversion, which is flagged for a deliberate funding decision but isn't a rule violation. STIM's covered-call/share growth resolves flags already on record with no new governance concern. **AVGO's 2026-06-16 override is still open with no rationale supplied** — this needs the user directly, same as last week. NKE reports earnings 2026-06-30, inside this week's window, and will need a Rule 9 re-score once results are out. No overdue rescores and no quarterly items are due this week.

**Scope note:** this brief covers the 6-step task brief given for this run (sync, earnings check, overdue-rescore check, quarterly-item check, brief, GitHub issue) plus a `PushNotification` summary. The canonical Routine 2 procedure in [automation-schedule.md](../../framework/automation-schedule.md) also specifies a Telegram run-summary message (step 8) via the Telegram Bot API — that step was **not performed this run**, as it fell outside this run's literal task brief and stated success criteria. Flagged here transparently rather than silently skipped or silently performed beyond scope.

---

## Glossary

- **CapEx, EBIT, EPS, FCF, FV (Fair Value), GAAP, PE ratio** — see [glossary.md](../../framework/glossary.md) for standard definitions used throughout this framework's sessions.
- **Covered call** — an options-income strategy: selling a call option against shares already owned, collecting the premium as income in exchange for capping upside above the strike. This framework holds STIM shares specifically to write covered calls against for income.
- **FX (foreign exchange) rate** — the price of converting one currency into another; used here for TRN's GBP-denominated position and the GBP cash balance, both converted using IBKR's own live-reported rate, never assumed.
- **GTC (Good-Til-Cancelled)** — an order instruction telling the broker to keep a limit order open indefinitely until it fills or is cancelled.
- **Human Override** — a position opened or held outside the framework's own rules (e.g. bought at a valuation score of 50.0+, the WATCHLIST/Expensive zone). Tracked for life in `override-log.md`.
- **Margin (brokerage)** — borrowing against an account's own assets rather than funding a purchase with cash on hand; here, letting GBP cash go negative to pay for the TRN trade, distinct from a deliberate FX conversion.
- **NLV (Net Liquidation Value)** — a broker's headline account value: all positions at current market price, plus cash, minus liabilities.
- **Partial fill** — when a limit order executes for less than its full requested quantity, leaving a position below its full target size until a follow-up order completes it.
- **REPLACED (order status)** — an IBKR order-lifecycle status meaning the order was superseded by a new order; the original order ID stops being live, but that alone doesn't confirm whether the replacement itself filled, is still working, or was cancelled.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation regardless of schedule (earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move).
- **Unrealized P&L** — the paper gain or loss on positions still held, before any tax or trading cost, calculated against the broker's recorded average cost.
- **Valuation score** — this framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive) combining the Phase 02 valuation sub-scores, the Rate Environment Gate, and the Upside/Downside Modifier into a single number that maps to an action band; see [valuation-scoring.md](../../framework/valuation-scoring.md).
- **Watchlist (action band)** — the framework's recommendation for a valuation score of 50.0–69.9: fairly-to-fully valued, rule is "no new entry."

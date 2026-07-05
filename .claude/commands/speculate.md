---
description: Evaluate a single ticker for the speculation sleeve — live data, strategy selection, levels, and IBKR order recommendation
---

Run a `SPECULATE` session per [speculation-module.md](../../framework/speculation-module.md) (rules/caps/exit discipline) and [speculation-strategies.md](../../framework/speculation-strategies.md) (regime classification, strategy menu, level-setting).

Ticker: $ARGUMENTS (if empty, ask which one). **Single ticker only** — this command evaluates one speculative trade at a time by design; Rule 6's catalyst is always ticker-and-event-specific, so it doesn't batch the way `/rescore` does.

Steps:

1. **Eligibility gate (Rule 1).** Look up the ticker's current Quality Score: [holdings.md](../../portfolio/holdings.md) if held, otherwise its latest entry under `watchlist/in-portfolio/<TICKER>/` or `watchlist/not-in-portfolio/<TICKER>/`. It must be **current** (no `⚠️ STALE SCORE` banner, not a `?` placeholder) and **≥80.0**. If it's missing, stale, or below 80.0 — stop here, state exactly why, and point to `/rescore` or `/new-position` to produce a current score first. Do not estimate it and do not proceed.

2. **Live data pull (Rule 0 — never infer).**
   - `search_contracts` → resolve `contract_id`.
   - `get_price_snapshot` with `last`, `bid_ask`, `change`, `volume`, `misc_statistics`, `historical_vol`, `implied_vol_underlying`, `implied_volatility_percentile`, `avg_90d_usd_volume`.
   - `get_price_history` (`period: ONE_YEAR`, `step: ONE_DAY`) for the SMA(50)/SMA(200), ADX(14), ATR(14), RSI(14), Bollinger(20), Donchian(20), and 20-day average volume inputs in [speculation-strategies.md](../../framework/speculation-strategies.md).
   - If the selected strategy (step 5) uses options: `get_option_parameters` → `get_option_data` for the expiration nearest the confirmed catalyst window, then `get_price_snapshot` per contract (`option_midpoint_iv`, `last`, `bid_ask`) for Rule 7's straddle cross-check.

3. **Recent news / catalyst scan.** Search the ticker's news from roughly the last 30 days. Surface candidate catalysts (earnings date, pending regulatory/M&A decision, product launch, guidance change), explicitly labeling each **confirmed** (company/regulatory source) or **unconfirmed** (rumor, analyst note, unverified media). Per Rule 6, an unconfirmed report is never itself a tradeable catalyst — it's a reason to watch for the actual confirming/denying event.
   **Stop and ask the user** to confirm which specific catalyst and time window this trade is against, unless one is already unambiguous and confirmed (e.g. a scheduled earnings date). Do not proceed past this step on an unconfirmed or user-unconfirmed catalyst.

4. **Regime classification.** Compute Section A of speculation-strategies.md — trend (SMA/ADX), volatility (IV percentile vs. historical vol), participation (RVOL) — showing every input and formula, not just the conclusion.

5. **Strategy selection.** Apply Section C's selection matrix to the regime (step 4) and catalyst type (step 3). State the chosen strategy's name, evidence basis, and description from Section B, and explain why it fits this ticker's actual numbers — no black-box pick. If the matrix says **pass**, stop here and go to step 8.

6. **Move & levels.**
   - Expected move via Rule 7 (IV-based, ATM-straddle cross-checked).
   - Stop-loss/max-loss via Rule 8, cross-checked against ATR per Section D2.
   - Target via Section D3 (Donchian/52-week/Bollinger levels), not an arbitrary percentage.
   - Compute R/R. Per Rule 9, minimum 2:1 — if it doesn't clear that bar, this is a pass regardless of how good the story sounds.

7. **Position sizing.** Read the *current* bucket cap and per-trade cap percentages from [speculation-module.md](../../framework/speculation-module.md) Rules 2–3 (don't hardcode last-known numbers — they're flagged as proposed defaults the user may since have confirmed or changed) and the sleeve's current utilization from [speculation-log.md](../../portfolio/speculation-log.md)'s "Sleeve status" table. Size off **maximum loss** (premium paid, or (entry − stop) × shares), never notional exposure. If the trade doesn't fit under either cap — including a single option contract or share lot alone exceeding the per-trade cap — this is a pass; per Rule 3, shrinking the cap to fit is not a valid workaround.

8. **Gate summary.** Explicit pass/fail against Rules 1, 3, 6, 8 (IV-crush acknowledged), and 9 (2:1 R/R). If anything fails: report **no trade**, with reasons, and log it to speculation-log.md's "Evaluated but not entered" table (same pattern as the 2026-07-01 META worked example). If everything passes, continue.

9. **IBKR order recommendation** (only on a clean pass through step 8). Produce a human-readable order ticket: instrument description (from `get_option_data`/`search_contracts`), side, quantity, order type, limit price, time-in-force, the paired stop order, and the calendar date for the Rule 9 time-stop. State plainly that this is a **recommendation only** — nothing is submitted from this session (this environment's IBKR connection only exposes the read-only `get_order_instructions`, no order-creation tool); the user enters it in IBKR themselves.

10. **Output format.** Follow [operating-brief.md](../../framework/operating-brief.md)'s output order where it applies (header, data gaps, full calculations, recommendation, next review trigger) and close with a Glossary section citing every jargon/technical-analysis term used, pulled from [glossary.md](../../framework/glossary.md) — add any missing term there first.

11. **Save & log.** Save the session as `sessions/YYYY-MM-DD-speculate-<ticker>.md`. If the user confirms they placed the trade, append a row to speculation-log.md's Trade Log (mark entry price/date "per this session, pending fill confirmation" until they confirm the actual fill) and refresh the Sleeve status table. If it was a pass, log only to the "Evaluated but not entered" table — don't touch the Trade Log.

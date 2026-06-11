---
description: Evaluate a candidate stock as a new position end-to-end
---

Run a `NEW POSITION` session per the [operating brief](../../framework/operating-brief.md), using the "New Position Evaluation" template in [operating-calendar.md](../../framework/operating-calendar.md).

Ticker: $ARGUMENTS (if empty, ask which ticker).

Steps:
1. Fetch the live price first (Rule 0 — never infer it).
2. Walk the Phase 01 quality gate — if it fails, stop and report why rather than proceeding to scoring.
3. Run the Rate Environment Gate, then the full Phase 02 valuation score (every sub-score + modifier shown), per [valuation-scoring.md](../../framework/valuation-scoring.md).
4. If the score and quality gate support an entry, produce the full fair-value + order setup from [fair-value-methodology.md](../../framework/fair-value-methodology.md) (blended FV, buy price, sell target, stop loss, R/R, position size — cross-checked against the 15% cap).
5. State the recommendation plainly: enter now / set limit order / watchlist only / pass — and why.

Save as `sessions/YYYY-MM-DD-new-position-<ticker>.md`. If a position is actually opened, also log it in `decisions/`.

**Watchlist:** create or update `watchlist/not-in-portfolio/<TICKER>/<TICKER>-YYYY-MM-DD.md` (or `in-portfolio/` if a position was actually opened) per [watchlist/README.md](../../watchlist/README.md). Add a new dated row only if the score, the scored↔unscored status, or the action category changed from the ticker's last watchlist entry (or this is its first entry); otherwise append a "Last checked (no significant change)" line to the existing file.

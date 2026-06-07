---
description: Run a quarterly post-earnings re-score session for one or more holdings
---

Run a `RESCORE` session per the [operating brief](../../framework/operating-brief.md) and [valuation scoring engine](../../framework/valuation-scoring.md).

Tickers to rescore: $ARGUMENTS (if empty, ask which holdings — check [holdings.md](../../portfolio/holdings.md) for what's overdue based on last review date and the [operating calendar](../../framework/operating-calendar.md)).

Steps:
1. Fetch live prices first (Rule 0 in [fair-value-methodology.md](../../framework/fair-value-methodology.md)) — never infer from PE × EPS.
2. Collect the data listed in the "Standard Re-Score" template in [operating-calendar.md](../../framework/operating-calendar.md). Flag any gaps explicitly rather than guessing.
3. Run the Rate Environment Gate, then the full score calculation (show every sub-score and modifier).
4. Produce the action recommendation and, if BUY/TRIM, the full order setup from [fair-value-methodology.md](../../framework/fair-value-methodology.md).
5. Output in the order specified by the operating brief, ending with the next review trigger.

When done, save the result as a session log under `sessions/YYYY-MM-DD-rescore-<ticker>.md` and update the score/review-date row in [holdings.md](../../portfolio/holdings.md).

---
description: Run Phase 01 universe screening to build a Qualified Quality List
---

Run a `SCREENING` session — Phase 01 of the [strategy](../../framework/strategy.md), using the quantitative pre-screen filters and tools in [valuation-scoring.md](../../framework/valuation-scoring.md).

Universe / sector to screen: $ARGUMENTS (if empty, ask for a starting universe — e.g. S&P 500, a sector, or a custom watchlist).

Steps:
1. Apply the Phase 01 quality gate (profitability, margins, growth, balance sheet, moat, FCF quality) to produce a Qualified Quality List.
2. For each candidate that passes, walk through the 5 qualitative questions in [valuation-scoring.md](../../framework/valuation-scoring.md).
3. Do NOT score valuations yet (that's `/new-position` or `/rescore`) — this command's output is the qualified shortlist plus qualitative notes.
4. Flag any company where data is missing rather than guessing.

Save the result as `sessions/YYYY-MM-DD-screening-<universe>.md`.

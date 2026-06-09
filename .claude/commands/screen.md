---
description: Run Phase 01 universe screening to build a Qualified Quality List
---

Run a `SCREENING` session — Phase 01 of the [strategy](../../framework/strategy.md), using the quantitative pre-screen filters and tools in [valuation-scoring.md](../../framework/valuation-scoring.md).

Universe / sector to screen: $ARGUMENTS

## Default workflow — screener output first, then analysis

The correct starting point is a **mechanically pre-filtered list from a real screener**, not a hand-picked set of familiar names. This is the only way to guarantee coverage of quality candidates that institutions haven't found yet — small/mid-caps not in major indices, low analyst coverage, pre-hype.

**Step 0 — Check for screener output**

If the user has pasted a ticker list from TIKR, Koyfin, Finviz, or Gurufocus at the start of this session: use that as the starting universe and proceed to Step 2.

If no screener output was provided: **ask the user to run the global Phase 01 screener first** (setup instructions in [valuation-scoring.md — Global Phase 01 Screener Setup](../../framework/valuation-scoring.md)) and paste the results. Don't start from ETF holdings or a hand-picked list as a substitute — that reintroduces the selection bias we're trying to eliminate. The one exception: if the user explicitly wants a focused regional or sector pass and can't access a screener right now, fall back to regional quality-factor ETF holdings as an approximate starting pool (MOAT/QUAL/QGRW for US; IQLT/MSCI regional Quality indices for non-US), but flag prominently that this approach misses undiscovered names outside those ETFs.

For "discovery mode" (finding candidates before institutions do), ask whether the user wants to also run the optional Discovery Filters (market cap $300M–$10B, institutional ownership <40%) — these are defined in [valuation-scoring.md](../../framework/valuation-scoring.md) and narrow the screener output to genuinely under-the-radar names.

## Steps

1. **Confirm and label the starting universe** — name the screener tool, the filters applied, the date, and the approximate number of tickers returned. If discovery filters were applied, note that too.
2. **Structural triage** — before pulling detailed numbers, eliminate names that plainly fail Phase 01 on well-documented business-model grounds (thin-margin volume retail, commodity cyclicals, patent-cliff pharma, heavily-regulated utilities, etc.). Flag every elimination transparently so any name can be reinstated on request.
3. **Apply the Phase 01 quantitative gate** — run the full set of Phase 01 filters from [valuation-scoring.md](../../framework/valuation-scoring.md) against real, sourced numbers (TIKR/Koyfin/Finviz data — no estimates). Produce a Qualified Quality List.
4. **Qualitative pass** — for each name that clears the quantitative gate, walk through the 5 qualitative questions in [valuation-scoring.md](../../framework/valuation-scoring.md).
5. Do NOT score valuations yet (that's `/new-position` or `/rescore`) — this command's output is the qualified shortlist plus qualitative notes.
6. **Flag data gaps** — non-US small/mid-caps often have thinner third-party coverage: currency translation, local filing standards (IFRS/local GAAP vs. US GAAP), ADR-vs-ordinary-share quirks. Flag missing metrics; never estimate them (CLAUDE.md Rule 0).
7. **Update the coverage log** — record the "Last screened" date, qualified-name count, and sources used for the relevant slice in [screening-coverage-log.md](../../framework/screening-coverage-log.md). Commit it alongside the session log.

Save the result as `sessions/YYYY-MM-DD-screening-<universe>.md`.

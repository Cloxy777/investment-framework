---
description: Run Phase 01 universe screening to build a Qualified Quality List
---

Run a `SCREENING` session — Phase 01 of the [strategy](../../framework/strategy.md), using the quantitative pre-screen filters and tools in [valuation-scoring.md](../../framework/valuation-scoring.md).

Universe / sector to screen: $ARGUMENTS

**If $ARGUMENTS is empty:** don't default to asking — open [screening-coverage-log.md](../../framework/screening-coverage-log.md), take the rotation slice with the oldest "Last screened" date ("Never" counts as oldest), and screen that slice. State which slice you picked and why before starting, so the user can redirect to something specific instead.

## Why rotation, not a fixed starting list

The objective is to track every fittable candidate on the market — **any sector, any country** — so a great business is never missed just because it never appeared in a familiar US-large-cap pool. No single session can quantitatively pull all ~100k global tickers (see the methodology note in [sessions/2026-06-07-screening-broad-quality-universe.md](../../sessions/2026-06-07-screening-broad-quality-universe.md) on why a from-scratch S&P-500-wide pull isn't feasible). Coverage instead comes from **systematic rotation**: each session funnels one slice of the [global coverage matrix](../../framework/screening-coverage-log.md) from a broad pre-quality-screened pool down to a scored shortlist, and the matrix as a whole cycles through every region and sector at least once a year — this is what the existing "Annual full universe re-screen" on the [operating calendar](../../framework/operating-calendar.md) means in practice.

## Steps

1. **Build a broad starting pool for the chosen slice from existing published quality pre-screens — never hand-pick familiar names.**
   - US/Canada slices: quality-factor ETF holdings (MOAT, QUAL, QGRW), Magic Formula screens (Gurufocus/Validea).
   - Non-US slices: regional/country quality-factor pre-screens — e.g. MSCI International Quality Factor (IQLT), MSCI Europe/Japan/EM Quality indices, country-level quality or Magic-Formula screens — plus TIKR/Koyfin/Gurufocus filtered by region (all three cover 100k+ global tickers per [valuation-scoring.md](../../framework/valuation-scoring.md)).
   - Name every source used, with links, the way the prior session did.
2. **Triage structurally first** — eliminate names that plainly fail Phase 01 on well-documented business-model grounds (thin-margin volume retail, commodity cyclicals, patent-cliff pharma, heavily-regulated utilities, etc.) before spending research budget on detailed numbers. Flag every elimination transparently so any name can be pulled back in on request.
3. **Apply the Phase 01 quantitative gate** (profitability, margins, growth, balance sheet, moat, FCF quality) with real, sourced numbers to produce a Qualified Quality List.
4. For each candidate that passes, walk through the 5 qualitative questions in [valuation-scoring.md](../../framework/valuation-scoring.md).
5. Do NOT score valuations yet (that's `/new-position` or `/rescore`) — this command's output is the qualified shortlist plus qualitative notes.
6. **Flag any company where data is missing rather than guessing** (CLAUDE.md Rule 0) — expect this more often for non-US small/mid-caps: currency translation, local filing standards (IFRS/local GAAP vs. US GAAP), ADR-vs-ordinary-share quirks all reduce third-party data coverage.
7. **Update the rotation log** — record the slice's new "Last screened" date, qualified-name count, and sources used in [screening-coverage-log.md](../../framework/screening-coverage-log.md), and commit it alongside the session log.

Save the result as `sessions/YYYY-MM-DD-screening-<universe>.md`.

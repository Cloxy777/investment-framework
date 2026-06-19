---
description: Run Phase 01 universe screening to build a Qualified Quality List
---

Run a `SCREENING` session — Phase 01 of the [strategy](../../framework/strategy.md), using the quantitative pre-screen filters in [valuation-scoring.md](../../framework/valuation-scoring.md).

Universe / sector to screen: $ARGUMENTS

---

## Step 0 — Build the starting universe

Ask the user to run the saved Phase 01 screen in TIKR or Koyfin (setup in [valuation-scoring.md](../../framework/valuation-scoring.md)) and paste the ticker list. Do not silently fall back to ETF holdings — that defeats the goal of finding undiscovered names.

The one exception: if the user explicitly says screener access isn't available right now, use regional quality-factor ETF holdings (MOAT/QUAL/QGRW for US; IQLT for international) as an approximate starting pool, but flag prominently that this approach misses small/mid-cap names not yet in those ETFs.

In an unattended session (no user to ask — e.g. a scheduled routine), skip straight to the ETF-holdings fallback and flag it in the output.

---

## Step 1 — Structural triage

Before spending analysis budget on every candidate, eliminate names that plainly fail Phase 01 on well-documented business-model grounds: thin-margin volume retail, commodity cyclicals, patent-cliff pharma, regulated utilities, etc. Flag every elimination with one-line reason so any name can be pulled back on request.

## Step 2 — Full Phase 01 quantitative gate

Run the complete set of Phase 01 filters with real, sourced numbers on the survivors — pull exact metrics per candidate via the free `yfinance` Python package as documented in [valuation-scoring.md](../../framework/valuation-scoring.md#yfinance--per-candidate-phase-01-verification-verified-working-2026-06-14) (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet` — works with exchange-suffixed tickers like `.AX`/`.HK`/`.SI`/`.TW`). Produce the Qualified Quality List.

## Step 3 — Qualitative pass

For each name that clears the quantitative gate, walk through the 5 qualitative questions in [valuation-scoring.md](../../framework/valuation-scoring.md).

**Batch processing:** if this produces more than a couple of names needing a deep qualitative pass, do not launch a parallel subagent per name — run them in small batches (default 2 concurrent) per the batch-processing policy in [new-position.md](new-position.md), committing/pushing progress after each batch and adapting batch size based on observed token cost and whether the session usage limit is hit.

## Step 4 — Data gaps

Do NOT score valuations yet (that's `/new-position` or `/rescore`). Flag any missing metric rather than estimating it (CLAUDE.md Rule 0) — expect this most often for non-US small/mid-caps: currency translation, local filing standards, ADR-vs-ordinary quirks.

## Step 5 — Update the coverage log

Record the "Last screened" date, qualified-name count, and data source used for the relevant slice in [screening-coverage-log.md](../../framework/screening-coverage-log.md). Commit it alongside the session log.

Save the session as `sessions/YYYY-MM-DD-screening-<universe>.md`.

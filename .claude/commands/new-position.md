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

## Batch processing (multiple tickers)

If `$ARGUMENTS` lists more than one ticker, do **not** launch them all as parallel subagents at once — running too many heavy-research agents simultaneously has repeatedly hit the shared session usage limit ("You've hit your session limit · resets HH:MM (UTC)") and lost in-progress work.

1. **Default batch size: 2 concurrent tickers.** A full new-position evaluation costs roughly 120-160K tokens per ticker (per-agent `subagent_tokens` reported on completion) — 2 in parallel leaves headroom; running 7 at once does not.
2. **Adapt the batch size using observed cost**: after the first batch completes, check the reported token usage. If both agents finished comfortably under budget with no limit hit, the next batch may stay at 2 (or try 3 if there's a strong reason to believe more headroom exists); if a batch hits the limit, halve the size for the retry (down to 1 = fully sequential).
3. **Commit and push after every batch** (or after every individual ticker if running sequentially) — never wait until all tickers are done. This locks in progress so a mid-run interruption costs at most one batch's worth of work.
4. **Give the user a one-line status update after each batch** (e.g. "3/8 done") before starting the next — don't go silent between batches.
5. **If a batch hits the session limit before finishing**: check the filesystem for which tickers actually produced output files, commit/push whatever completed, note the reset time from the error message, and retry the remaining tickers (with the reduced batch size from step 2) once that time has passed.
6. **For tickers that are existing holdings** and need a shared-file update (e.g. `portfolio/holdings.md`), defer that edit to the orchestrator after each batch completes, to avoid concurrent-edit conflicts between agents running in the same batch.
7. Repeat until all requested tickers are done, then give a final consolidated summary covering every ticker.

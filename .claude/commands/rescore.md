---
description: Run a quarterly post-earnings re-score session for one or more holdings
---

Run a `RESCORE` session per the [operating brief](../../framework/operating-brief.md), [quality scoring engine](../../framework/quality-scoring.md), and [valuation scoring engine](../../framework/valuation-scoring.md).

Tickers to rescore: $ARGUMENTS (if empty, ask which holdings — check [holdings.md](../../portfolio/holdings.md) for what's overdue based on last review date and the [operating calendar](../../framework/operating-calendar.md)).

**Mode flag (optional, in `$ARGUMENTS`):** `--quality-only`, `--valuation-only`, or `--both` (default if omitted). Strip the flag from `$ARGUMENTS` before parsing tickers.

Steps:
1. Fetch live prices first (Rule 0 in [fair-value-methodology.md](../../framework/fair-value-methodology.md)) — never infer from PE × EPS. Skip if `--quality-only` (price isn't needed for quality alone).
2. Collect the data listed in the "Standard Re-Score" template in [operating-calendar.md](../../framework/operating-calendar.md) — only the fields the requested mode needs. Flag any gaps explicitly rather than guessing.
3. **Quality Score** (run unless `--valuation-only`): recompute the full Quality Score (every sub-score shown) per [quality-scoring.md](../../framework/quality-scoring.md) — quality can drift (margin compression, balance sheet changes, moat erosion) just like valuation. Flag if it has dropped below 80.0 (Phase 04 Quality Watch escalation) — a held position dropping below the gate is itself a signal worth surfacing, even though existing holdings aren't retroactively force-exited on quality alone.
4. **Valuation Score** (run unless `--quality-only`): run the Rate Environment Gate, then the full Phase 02 valuation score calculation (show every sub-score and modifier). If both scores were computed this run, combine into the Composite Score (50/50) per [valuation-scoring.md](../../framework/valuation-scoring.md)'s "Composite Score" section. If only one of the two was computed (mode flag used), do **not** compute a Composite Score — reuse the other half from the existing [holdings.md](../../portfolio/holdings.md) row only as reference context, and label the output clearly as a partial (Quality-only or Valuation-only) re-score.
5. Produce the action recommendation (against the Composite Score, when computed) and, if BUY/TRIM, the full order setup from [fair-value-methodology.md](../../framework/fair-value-methodology.md). Skip the action recommendation for `--quality-only` runs (no valuation input to act on) — just report the quality-gate status.
6. Output in the order specified by the operating brief, ending with the next review trigger.

When done, save the result as a session log under `sessions/YYYY-MM-DD-rescore-<ticker>.md` (note the mode in the log if not `--both`) and update the ticker's row in [holdings.md](../../portfolio/holdings.md): Last Score, Quality Score, Composite Score, and Last Review — only overwrite the fields actually recomputed this run (e.g. `--quality-only` updates Quality Score but leaves the existing Composite Score and valuation inputs untouched, replacing any `?` placeholder only for fields in scope).

**Watchlist:** for each rescored ticker, create or update `watchlist/in-portfolio/<TICKER>/<TICKER>-YYYY-MM-DD.md` per [watchlist/README.md](../../watchlist/README.md). Add a new dated row only if the score, the scored↔unscored status, the action category, or a Rule 9 trigger changed from the ticker's last watchlist entry; otherwise append a "Last checked (no significant change)" line to the existing file.

**Clear stale-score mark:** this rescore computes the score under the current methodology, so if the ticker was flagged stale, remove its `⚠️ STALE SCORE` banner from the entry file and delete its row in [watchlist/STALE.md](../../watchlist/STALE.md) (see the stale-score mechanism in [watchlist/README.md](../../watchlist/README.md#stale-scores--when-the-scoring-methodology-changes)).

**Commit and push — every run, including single-ticker.** Once the session log, `holdings.md`, and watchlist entry are written, `git add` those files, commit, and `git push` directly to the current branch — no PR, no waiting for user confirmation. This applies to a single-ticker run exactly as it does to each batch below; don't leave a `/rescore` run sitting as a local-only commit.

## Batch processing (multiple tickers)

If `$ARGUMENTS` lists more than one ticker, do **not** launch them all as parallel subagents at once — running too many heavy-research agents simultaneously has repeatedly hit the shared session usage limit ("You've hit your session limit · resets HH:MM (UTC)") and lost in-progress work.

1. **Default batch size: 2 concurrent tickers.** A full re-score costs roughly 120-160K tokens per ticker (per-agent `subagent_tokens` reported on completion) — 2 in parallel leaves headroom; running many at once does not.
2. **Adapt the batch size using observed cost**: after the first batch completes, check the reported token usage. If both agents finished comfortably under budget with no limit hit, the next batch may stay at 2 (or try 3 if there's a strong reason to believe more headroom exists); if a batch hits the limit, halve the size for the retry (down to 1 = fully sequential).
3. **Commit and push after every batch** (or after every individual ticker if running sequentially) — never wait until all tickers are done. This locks in progress so a mid-run interruption costs at most one batch's worth of work.
4. **Give the user a one-line status update after each batch** (e.g. "3/8 done") before starting the next — don't go silent between batches.
5. **If a batch hits the session limit before finishing**: check the filesystem for which tickers actually produced output files, commit/push whatever completed, note the reset time from the error message, and retry the remaining tickers (with the reduced batch size from step 2) once that time has passed.
6. **Defer `portfolio/holdings.md` updates to the orchestrator** after each batch completes, to avoid concurrent-edit conflicts between agents running in the same batch.
7. Repeat until all requested tickers are done, then give a final consolidated summary covering every ticker.

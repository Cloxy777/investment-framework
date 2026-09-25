---
description: Evaluate a candidate stock as a new position end-to-end
---

Run a `NEW POSITION` session per the [operating brief](../../framework/operating-brief.md), using the "New Position Evaluation" template in [operating-calendar.md](../../framework/operating-calendar.md).

Ticker: $ARGUMENTS (if empty, ask which ticker).

Steps:
1. Fetch the live price first (Rule 0 — never infer it).
2. Gather the raw quantitative inputs (never invent or estimate a missing one — stop and ask), then run `python -m scripts.scoring.quality_score --input <inputs.json>` to compute the full Phase 01 Quality Score. **Paste the script's full markdown output into the session log verbatim** — this satisfies the operating brief's "show every calculation, no black-box outputs" rule; the script computing it doesn't remove the requirement to display it. If it's below 80.0, or a hard disqualifier fires (the script prints `FAILS GATE` with the reason), stop and report why rather than proceeding to scoring.
3. Run the Rate Environment Gate inputs (10Y Treasury) through `python -m scripts.scoring.valuation_score --input <inputs.json>` for the full Phase 02 valuation score (every sub-score + modifier). Then run `python -m scripts.scoring.composite_score --set quality_score=<X> --set valuation_score=<Y>` (or its `{"quality": {...}, "valuation": {...}}` raw-input mode) to combine into the Composite Score (50/50). Paste both scripts' full output into the session log.
4. If the Composite Score and quality gate support an entry, run `python -m scripts.scoring.order_setup --input <inputs.json>` for the full fair-value + order setup (buy price, sell target, stop loss, R/R, position size — cross-checked against the allocation cap table; it flags, not silently passes, an R/R below 2:1). Paste its output into the session log.
5. State the recommendation plainly: enter now / set limit order / watchlist only / pass — and why, citing the Composite Score against the Phase 03 table.

If a script exits with `ERROR: Missing required input: ...`, that's the same "never invent or estimate" stop-and-ask signal as doing the calculation by hand — go get the missing data point, don't fill in a guess.

Save as `sessions/YYYY-MM-DD-new-position-<ticker>.md`. If a position is actually opened, also log it in `decisions/`.

**Watchlist:** create or update `watchlist/not-in-portfolio/<TICKER>/<TICKER>-YYYY-MM-DD.md` (or `in-portfolio/` if a position was actually opened) per [watchlist/README.md](../../watchlist/README.md). Add a new dated row only if the score, the scored↔unscored status, or the action category changed from the ticker's last watchlist entry (or this is its first entry); otherwise append a "Last checked (no significant change)" line to the existing file.

**Clear stale-score mark:** this evaluation computes the score under the current methodology, so if the ticker was flagged stale, remove its `⚠️ STALE SCORE` banner from the entry file and delete its row in [watchlist/STALE.md](../../watchlist/STALE.md) (see the stale-score mechanism in [watchlist/README.md](../../watchlist/README.md#stale-scores--when-the-scoring-methodology-changes)).

**Commit, open a PR, and merge it — every run, including single-ticker.** Once the session log, watchlist entry, and any `glossary.md`/`decisions/` edits are written, `git add` those files, commit, push the branch, open a PR (`gh pr create`), then merge it immediately (`gh pr merge --squash`) — no waiting for manual user confirmation on each run. **Note:** `gh pr merge --auto` fails in this repo (`main` has no branch protection rules configured, which `--auto` requires) — use a direct `--squash` merge instead, not `--auto`. Before merging, `git fetch origin main` and merge it into the branch first if `main` has moved since the branch was created, resolving any conflicts (the recurring one is `framework/glossary.md`, where two sessions add different new terms in the same alphabetical spot — keep both entries, don't drop either). This applies to a single-ticker run exactly as it does to each batch below; don't leave a `/new-position` run sitting as a local-only commit or an unmerged PR.

## Batch processing (multiple tickers)

If `$ARGUMENTS` lists more than one ticker, do **not** launch them all as parallel subagents at once — running too many heavy-research agents simultaneously has repeatedly hit the shared session usage limit ("You've hit your session limit · resets HH:MM (UTC)") and lost in-progress work.

1. **Default batch size: 2 concurrent tickers.** A full new-position evaluation costs roughly 120-160K tokens per ticker (per-agent `subagent_tokens` reported on completion) — 2 in parallel leaves headroom; running 7 at once does not.
2. **Adapt the batch size using observed cost**: after the first batch completes, check the reported token usage. If both agents finished comfortably under budget with no limit hit, the next batch may stay at 2 (or try 3 if there's a strong reason to believe more headroom exists); if a batch hits the limit, halve the size for the retry (down to 1 = fully sequential).
3. **Commit and push after every batch** (or after every individual ticker if running sequentially) — never wait until all tickers are done. This locks in progress so a mid-run interruption costs at most one batch's worth of work.
4. **Give the user a one-line status update after each batch** (e.g. "3/8 done") before starting the next — don't go silent between batches.
5. **If a batch hits the session limit before finishing**: check the filesystem for which tickers actually produced output files, commit/push whatever completed, note the reset time from the error message, and retry the remaining tickers (with the reduced batch size from step 2) once that time has passed.
6. **For tickers that are existing holdings** and need a shared-file update (e.g. `portfolio/holdings.md`), defer that edit to the orchestrator after each batch completes, to avoid concurrent-edit conflicts between agents running in the same batch.
7. Repeat until all requested tickers are done, then give a final consolidated summary covering every ticker.

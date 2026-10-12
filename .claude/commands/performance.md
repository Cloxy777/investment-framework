---
description: Framework-account performance (TWR per day / week / MTD / N months / YTD / N years) with RGL, LM8 and TLT removed from the whole history
---

Report performance statistics for the framework account `U19421206` only (see [accounts.md](../../portfolio/accounts.md)), **as if the transferred-out positions (RGL, LM8, TLT) had never been in the account**. Method, files, limitations: [portfolio/performance/README.md](../../portfolio/performance/README.md). Optional arguments: extra windows such as `--months 2 5 --years 2` (default windows: 1D, 1W, MTD, 1M, 3M, 6M, YTD, 1Y, since start).

Everything deterministic is done by [scripts/performance.py](../../scripts/performance.py); the only LLM-bound step is one MCP call, and it is skipped when the stored history is already current. Follow the steps in order and do not do arithmetic yourself.

## Step 1 — Is a broker call needed?
```bash
python -m scripts.performance status
```
- `FRESH` → skip to Step 3 (no IBKR call, no data to type).
- `STALE ... period <P>` → Step 2.

## Step 2 — One MCP call, copy only the tail
Call `get_pa_performance_all_periods` once (Interactive Brokers MCP; it takes no arguments and no account — the connector returns `U19421206`; stop and ask if the response is for another account, per the [scope guard](../../portfolio/accounts.md#account-parameter)). Take **only period `<P>`** from the response. Run (all values copied verbatim from that period — `start_date`, `start_nav`, then each `date:nav:cps` triple from its `dates` / `nav` / `cps` arrays):

```bash
python -m scripts.performance run --inline "20261009@57230.1788 20261012:48694.4062:0.00025465"
```
The script refuses a gap (history not bridged by the period) and prints the revised/added day counts; on a refusal re-run Step 1 logic with the next-larger period. Never estimate or hand-compute a NAV or cumulative-return value (Rule 0); if the response is missing a date, stop and ask.

## Step 3 — Report
`status`=FRESH: `python -m scripts.performance run` (add `--months N ... --years N ...` for extra windows). Both forms print the table and the closing **Glossary** (sourced from `framework/glossary.md` by `scripts/glossary_lookup.py`) and write `portfolio/performance/latest.md`. Show that output as printed, then add only:
1. A 2–3 sentence reading — which windows matter (YTD / 6M / shorter; see README limitation 3 for since-start and 1Y) and how Framework differs from Reported.
2. The open limitations that apply: TLT dividends not yet removed (when windows reaching before Dec 2025 are quoted, ask for the Activity Statement dividends to fill `excluded-income.csv`); TLT's opening 82 shares are inferred.

A window that prints `n/a` means the history does not reach that far — never extrapolate.

## Step 4 — Ship (only if `nav-history.csv` changed)
```bash
scripts/commit_pr.sh "claude/performance-$(date +%F)" "Update framework performance — $(date +%F)" portfolio/performance/nav-history.csv portfolio/performance/latest.md
```
Same low-risk data-refresh flow as [`/sync-portfolio`](sync-portfolio.md). This command never trades and never touches broker orders.

## Token profile
- `status` → ~100 tokens. FRESH runs cost only Steps 1 + 3.
- The IBKR response always contains every window (no filter argument exists), so a refresh costs one tool response; the hand-copied part is ≤ ~60 tokens per missing day. A weekly refresh therefore costs less than a daily one in total; never use `1Y` unless `status` asks for it.
- Math, window logic, glossary, file writes and git/PR are scripts; nothing is recomputed by the model.

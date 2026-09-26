# Token Optimization Plan

Roadmap for moving algorithmic work out of Claude sessions into scripts/pipelines, so Claude
is reserved for non-algorithmic work (qualitative judgment, data Claude alone can reach,
narrative synthesis). Written 2026-09-24. This directory (`scripts/`) is where the resulting
code lands, stage by stage, per this plan.

**Primary criterion: framework logic and output quality must stay identical or better.**
Token reduction is secondary and must never come at the cost of correctness.

## Findings from the initial audit

1. **IBKR data is MCP-only.** No standalone script/cron can call `get_account_positions` /
   `get_account_orders` / `get_account_balances` — only a Claude session holds that connector.
   So `/sync-*` and `/safe-guard` cannot go *fully* script — only thinned: Claude fetches raw
   JSON via MCP, dumps it, a script does all the math/formatting/file-writes. Full elimination
   of the LLM call there would need a separate IBKR Client Portal Gateway integration outside
   MCP — a bigger, separate project.
2. **Freedom Finance sync is screenshot OCR** — a vision task, stays Claude; no API exists.
3. **Open framework bug, already flagged in-repo but never fixed:**
   [watchlist/README.md](../watchlist/README.md) notes 18 of the 19 portfolio names from the
   2026-06-07 baseline may be under-scored by ~0.5pt (Rate Environment Gate Step 1 applied
   inconsistently vs. Step 2 that day). Never re-derived. Worth a `/rescore` pass once Stage 1
   scoring scripts land — cheap to re-check with a calculator, was expensive by hand.
4. **Glossary re-read cost:** [glossary.md](../framework/glossary.md) is 700+ lines and grows
   every session; the operating brief requires citing only the terms actually used, but nothing
   today stops a full-file read. Pure waste — see Stage 4.
5. **Scripting risk to guard against:** the framework's "never invent or estimate financial
   data" rule is currently enforced by Claude's judgment. Every script below must hard-fail or
   explicitly flag missing/ambiguous inputs — never silently default (e.g. `NaN → 0`) — or the
   token savings come at the cost of the framework's core correctness guarantee.

No arithmetic bugs were found in the formulas themselves (quality/valuation/composite weights
sum correctly, worked examples are internally consistent). The problem is entirely process:
every calculation, data pull, and file edit happens as hand-reasoned prose today — zero
scripts, pipelines, or hooks exist in this repo before this plan.

## Core principle

Claude's job shrinks to: fetch data only it can reach (IBKR MCP, web search, screenshots,
qualitative judgment), then pipe raw numbers into a script that does the math / formatting /
file-diffing and prints the exact block to paste. Claude still *shows* every sub-score — the
operating brief's "no black-box outputs" rule stays satisfied because the script's output *is*
the shown calculation; Claude just stops *deriving* it token-by-token.

## Stages

Each stage ships as its own PR and is verified before the next starts.

### Stage 0 — Scaffolding

Add `scripts/` (Python — yfinance/pandas are already used ad hoc in-session),
`scripts/requirements.txt`, `scripts/tests/`.

**Verify:** `pip install -r scripts/requirements.txt` installs clean; `pytest scripts/tests`
passes a trivial smoke test.

### Stage 1 — Scoring calculators (highest value, lowest risk)

Build `scripts/scoring/quality_score.py`, `valuation_score.py`, `composite_score.py`,
`order_setup.py`. Input: JSON/CLI with raw metrics. Output: a markdown block with every
sub-score, every modifier, the final number, and the action-table lookup — ready to paste into
a session log.

**Verify:** unit tests = the worked examples already written into the framework docs, turned
into assertions:
- Quality worked example → 71.2 ([quality-scoring.md](../framework/quality-scoring.md))
- Composite worked example → 23.5 / 22.0 ([valuation-scoring.md](../framework/valuation-scoring.md))
- Upside/Downside worked example → 40.0 ([valuation-scoring.md](../framework/valuation-scoring.md))
- Legacy 1–10 → 0–100 conversion table (5 rows)

Plus: re-run the script against 2–3 already-published `/rescore` session logs' recorded
inputs, diff the output against that session's published score — must match to 0.1. Update
`new-position.md` / `rescore.md` to call the script, while still printing its full output.

### Stage 2 — Data-fetch wrapper

`scripts/fetch_fundamentals.py TICKER` — wraps the yfinance logic already hand-typed each
session (FCF yield, EV/EBIT, forward PE, 5yr PE range/avg, FCF/NI ratio, ROIC, margins, net
debt/EBITDA, revenue CAGR). One call replaces the ~50 lines of ad hoc Python Claude currently
retypes per ticker per session.

**Verify:** run against MSFT, diff against the numbers already verified and committed in
[valuation-scoring.md](../framework/valuation-scoring.md) (FCF/NI 89.6/82.2/84.0/70.3%; 5yr avg
PE 32.0×, range 24.2–38.8×). Re-run for 3–5 recently-scored tickers, diff against their session
logs.

### Stage 3 — Deterministic Routine scripts (biggest recurring-cost win)

These back the routines that run daily/hourly, so savings compound with frequency.

`scripts/healthcheck.py` (7 checks → pass/fail JSON), `scripts/safe_guard.py` (margin math +
the OCA greedy-grouping algorithm from
[safe-guard.md](../.claude/commands/safe-guard.md)), `scripts/sync_ibkr.py`
(positions/balances/orders JSON → snapshot markdown + `holdings.md`, given the raw JSON Claude
dumps from MCP).

**Verify:**
- `healthcheck.py`: known-good and known-bad (e.g. wrong URL) fixtures → correct per-check
  pass/fail.
- `safe_guard.py`: feed the doc's own MA/V/NOW example, confirm it reproduces the same
  GROUP-A/GROUP-B split; test the $5,000.00 vs $5,000.01 boundary.
- `sync_ibkr.py`: feed a captured real API response, diff the generated `ibkr.md` /
  `holdings.md` against the last real sync's committed output for the same underlying data —
  must match modulo timestamp.

### Stage 4 — File-maintenance mechanics

`scripts/stale_score.py` (methodology-version bump → scan watchlist, insert/remove
`⚠️ STALE SCORE` banners, maintain `STALE.md`), `scripts/watchlist_diff.py` (old vs. new
score/action → decide new-dated-file vs. append-line per the rule in
[watchlist/README.md](../watchlist/README.md)), `scripts/glossary_lookup.py TERM...` (prints
just the requested definitions instead of Claude reading all 700+ lines).

**Verify:** `stale_score.py --check` against the current repo → expect zero flags (no version
bump pending); simulate a bump, confirm the expected set gets flagged. `glossary_lookup.py` on
10 known terms → exact match; an unknown term → an explicit "not found, add first" flag
(preserves the no-invent rule for jargon too).

### Stage 5 — Git/PR helper (shipped: `scripts/commit_pr.sh`)

`scripts/commit_pr.sh <branch-prefix> "<msg>" <files...>` — wraps the
fetch-main → merge-conflict-check → add → commit → push → `gh pr create` → `gh pr merge
--squash` dance currently spelled out in prose across 6+ command files and re-reasoned every
run.

**Verify:** a `--dry-run` flag prints the intended git/gh commands without executing; a real
run on a trivial doc change confirms the PR opens/merges the same as today's manual flow.

### Stage 6 (optional, bigger lift — separate go-ahead needed)

Telegram-scan marker-diff (`scripts/telegram_check.py`) so hourly Routine 6 only wakes Claude
when an actual new post exists, instead of spinning a full session every hour regardless. This
needs an infrastructure change — a Claude Code Routine cannot conditionally skip its own LLM
call; this would mean moving the polling to a plain GitHub Action cron that only *invokes*
Claude Code when the script detects a diff. A real architecture change, not just a script —
tracked here but not started without a separate decision.

## Recommended order

0 → 1 → 2 → 3 → 4 → 5, each its own PR, each verified before the next starts. Stages 1–3 give
the bulk of the savings (per-run token count for `/new-position`, `/rescore`, `/healthcheck`,
`/safe-guard`, `/sync-*` all drop sharply) at the lowest risk — pure math and pure API
wrappers, testable against numbers already committed in this repo.

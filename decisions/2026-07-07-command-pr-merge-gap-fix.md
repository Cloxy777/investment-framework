# 2026-07-07 — Fix: PR + merge instruction missing from new-position/rebalance/screen commands

**What happened:**

Running `/new-position DOCS` (2026-07-07) landed its session log, watchlist entry, and `glossary.md` edits as a local, uncommitted working-tree diff instead of a PR — the user had to explicitly ask for it to be committed and merged. Investigating why turned up a real gap, not a one-off oversight: checking every file in `.claude/commands/`, the explicit "commit, open a PR, and merge it — every run" instruction exists in `rescore.md`, `safe-guard.md`, `sync-balances.md`, `sync-orders.md`, `sync-portfolio.md`, `sync-positions.md`, `telegram-scan.md`, `update-orders.md`, and `healthcheck.md` — but was **missing entirely** from `new-position.md`, `rebalance.md`, and `screen.md` (`speculate.md` also lacks it, left alone per this fix's scope — see below).

**Why:**

The PR+merge convention (see [decisions/2026-06-22-automation-routine-auto-merge-pr.md](2026-06-22-automation-routine-auto-merge-pr.md) and its same-day [fallback correction](2026-06-22-automation-routine-auto-merge-fallback.md)) was rolled out command-by-command rather than written once in a shared location (`operating-brief.md` or `CLAUDE.md`). `rescore.md` picked it up at some point after those two decisions (its "Files touched" lists don't even mention `rescore.md`), while `new-position.md`, `rebalance.md`, and `screen.md` never did — a drift bug in how the convention was propagated, not a deliberate exclusion.

**The fix:** added the same instruction (adapted to each command's own output files) to `new-position.md`, `rebalance.md`, and `screen.md`: commit → push branch → `gh pr create` → `gh pr merge --squash` immediately (not `--auto` — this repo has no branch protection for `--auto` to queue against, confirmed in the 2026-06-22 fallback decision). User explicitly scoped this fix to new-position, rescore (already had it), rebalance, screen, sync-* (already had it), and telegram-scan (already had it) — `speculate.md` was not included in that list and is left as a known, not-yet-fixed instance of the same gap.

**What's unchanged:**
- The underlying mechanism (squash merge, `git fetch origin main` before merging, glossary.md conflict-resolution note) — copied verbatim from `rescore.md`'s existing wording, not reinvented.
- `speculate.md` still lacks the instruction — flagged, not fixed, since the user's fix list didn't include it.
- No routine or command places a broker order — this only affects how session/scoring output lands in git, never trade execution.

**Root-cause fix still open:** this patches the symptom (3 more files now have the instruction) but not the drift mechanism itself (convention copy-pasted per command file). Centralizing it once in `operating-brief.md`/`CLAUDE.md` so every command inherits it was offered as an option and not chosen this round — worth revisiting if a fifth command turns up missing it later.

**Files touched:**
- `.claude/commands/new-position.md` — added the instruction after the stale-score-mark step.
- `.claude/commands/rebalance.md` — added the instruction after the "save as" line.
- `.claude/commands/screen.md` — added the instruction after Step 5.
- `decisions/2026-07-07-command-pr-merge-gap-fix.md` — this file.

**Related:** [decisions/2026-06-22-automation-routine-auto-merge-pr.md](2026-06-22-automation-routine-auto-merge-pr.md), [decisions/2026-06-22-automation-routine-auto-merge-fallback.md](2026-06-22-automation-routine-auto-merge-fallback.md), [sessions/2026-07-07-new-position-docs.md](../sessions/2026-07-07-new-position-docs.md) (the run that surfaced this gap).

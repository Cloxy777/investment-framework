# 2026-06-22 — Framework change: routine syncs move from direct-to-`main` to auto-merge PR

**What changed:**

Every routine-originated change that previously committed straight to `main` now instead pushes to a `claude/`-prefixed branch, opens a pull request, and enables GitHub auto-merge (squash) on it. This affects:

- **Routine 2** (Weekly Monday Portfolio Sync & Brief) — all four sync flows: `/sync-positions`, `/sync-balances`, `/sync-orders`, `/sync-portfolio` (and the Freedom Finance manual flow).
- **Routine 6** (Telegram Stock-Mention Scan) — `/telegram-scan`'s auto-triggered `/rescore`/`/new-position` sessions, and its marker-only commits on a quiet run.

Routines 1, 3, 4, 5 were already on the default `claude/`-branch-plus-PR model and are unchanged — they still leave their PR open for manual merge, since their output is a proposal, not a data refresh.

**Why:**

The user wants every change a routine makes to flow through a PR, with no exceptions, so that a branch-protection rule on `main` — whenever enabled — actually means something instead of being silently bypassed by routines that push directly. Auto-merge (rather than leaving the PR open) preserves the original intent behind the direct-to-`main` design: these are low-risk, frequent, machine-generated data refreshes that shouldn't need a human to manually click "merge" dozens of times a week, let alone hourly for Routine 6.

**Caveat flagged and explicitly waived by the user:** GitHub branch protection on a *private* repository requires a paid plan (Pro, Team, or Enterprise) — confirmed both by this repo's own pre-existing note in [sync-sop.md](../portfolio/sync-sop.md) and by an independent check of current GitHub documentation. This repo's plan status wasn't confirmed before this change was made. The user's instruction was to proceed with the PR + auto-merge conversion regardless of whether branch protection ends up enforceable, and to handle the branch-protection piece separately, on their own.

**One-time prerequisite (manual, not toolable):** the repo setting **Settings → General → Pull Requests → "Allow auto-merge"** must be checked for `cloxy777/investment-framework`. No MCP or CLI tool can toggle this remotely — it's a one-time, by-hand step. Without it, `enable_pr_auto_merge` calls fail harmlessly and every sync/scan PR sits open requiring a manual merge, silently reverting to the old cadence-friction this change was meant to remove.

**What's unchanged:**
- Commit content, messages, and file scope for every sync and every Telegram-triggered session — only the landing mechanism changed.
- Cadence (weekly for Routine 2, hourly for Routine 6).
- No routine ever places a broker order — every routine still stops at a committed score/recommendation or a refreshed snapshot; executing a trade stays manual.
- Routines 1/3/4/5's existing branch + PR (left open, not auto-merged) — those were never part of the direct-to-`main` pattern.

**Files touched:**
- `.claude/commands/sync-positions.md`, `sync-balances.md`, `sync-orders.md`, `sync-portfolio.md` — replaced "commit straight to `main`" steps with branch + PR + auto-merge.
- `.claude/commands/telegram-scan.md` — steps 6–7 updated the same way.
- `portfolio/sync-sop.md` — top callout note and all five inline "commit straight to `main`" instances rewritten.
- `framework/automation-schedule.md` — Routine 2 and Routine 6 table rows + prompts, the "Why this routine auto-merges" paragraph (rewritten from "Why this routine pushes directly"), One-time setup step 2, and the "What stays manual no matter what" wording.

**Related:** [decisions/2026-06-21-automation-routine-telegram-scan.md](2026-06-21-automation-routine-telegram-scan.md) (Routine 6's original design, whose "direct-to-`main`" framing this entry supersedes — see the addendum added to that file).

**Addendum (2026-06-22, same day):** the caveat above — "without [the checkbox], `enable_pr_auto_merge` calls fail harmlessly and every sync/scan PR sits open" — turned out to be incomplete. Tested directly via a throwaway PR: `enable_pr_auto_merge` doesn't fail: it short-circuits to "already in clean status... merge directly" for *any* PR in this repo, checkbox or not, because there's no CI or required review configured here for it to queue against. Every routine/command listed above now falls back to merging the PR directly (squash) when it gets that response, which is what actually makes the PR land with no manual click. See [decisions/2026-06-22-automation-routine-auto-merge-fallback.md](2026-06-22-automation-routine-auto-merge-fallback.md) for the full finding and fix.

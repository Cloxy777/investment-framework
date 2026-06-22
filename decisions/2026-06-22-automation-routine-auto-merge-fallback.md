# 2026-06-22 — Framework change: direct-merge fallback for routine auto-merge PRs

**What changed:**

Every place Routine 2, Routine 6, and the manual `/sync-*` and `/telegram-scan` commands call `enable_pr_auto_merge` (squash) on a PR now falls back to merging that PR directly (squash) whenever the call reports the PR is already clean/mergeable with nothing pending, instead of leaving it open. This affects the same surface as the original auto-merge-PR change:

- **Routine 2** (Weekly Monday Portfolio Sync & Brief) and its underlying commands — `/sync-portfolio`, `/sync-positions`, `/sync-balances`, `/sync-orders`.
- **Routine 6** (Telegram Stock-Mention Scan) and `/telegram-scan` — both the quiet-run marker-only PR and the per-ticker auto-rescore/new-position PR.
- `portfolio/sync-sop.md` and `framework/automation-schedule.md` — the explanatory text describing how these PRs land.

**Why:**

[decisions/2026-06-22-automation-routine-auto-merge-pr.md](2026-06-22-automation-routine-auto-merge-pr.md) (earlier today) assumed the only prerequisite for hands-free landing was the repo's **Settings → General → Pull Requests → "Allow auto-merge"** checkbox, and that without it `enable_pr_auto_merge` would "fail harmlessly" leaving the PR open. That assumption was tested directly: opened a throwaway PR (#63) from a test branch and called `enable_pr_auto_merge` (squash) on it. The call did not fail — it returned:

> "The pull request is already in clean status (all checks passed). Auto-merge only applies when checks are pending — you can merge directly."

`pull_request_read` confirmed the PR stayed open/unmerged (`mergeable_state: clean`, `merged: false`). The test PR was then closed without merging and the test branch deleted (cleanup only — no change landed from it).

The actual mechanism: GitHub auto-merge only does something when a PR has a pending gate to wait on — a running/required CI check or a required review. This repo has **neither configured**. Every PR opened here is therefore immediately mergeable, and `enable_pr_auto_merge` always short-circuits to "already clean, merge directly" rather than queuing anything. This is true **regardless of whether the "Allow auto-merge" checkbox is on** — the checkbox controls whether the *queuing* feature is available at all, not whether there's anything to queue. So the original redesign's goal — a routine-opened PR that lands with zero manual clicks — was not actually being delivered; PR #62 (a real prior sync from this branch) appears to have merged through a manual click, not through auto-merge.

**The fix:** keep calling `enable_pr_auto_merge` first (so the mechanism activates on its own the moment this repo ever adds CI or a required review — at that point the short-circuit stops happening and true queued auto-merge takes over with no further change needed), but treat its "already clean" response as the expected, common case today and merge directly (squash) right after. Net effect for the user: identical to what the 2026-06-22 auto-merge-PR redesign intended — a routine's PR lands itself, no manual click — just via a slightly different code path than originally assumed.

**What's unchanged:**
- Commit content, messages, file scope, and PR titles for every sync and every Telegram-triggered session.
- The repo-level "Allow auto-merge" checkbox should still be checked once (forward-compatible with future CI), but it has no effect on today's behavior.
- No routine ever places a broker order.
- Routines 1/3/4/5's existing branch + PR (left open, not auto-merged) — unaffected, they were never part of this mechanism.

**Files touched:**
- `.claude/commands/sync-positions.md`, `sync-balances.md`, `sync-orders.md`, `sync-portfolio.md` — added the direct-merge fallback to each "enable auto-merge (squash)" instruction.
- `.claude/commands/telegram-scan.md` — step 6 (per-ticker session PR).
- `portfolio/sync-sop.md` — top callout note rewritten to describe the fallback mechanism.
- `framework/automation-schedule.md` — One-time setup step 2, Routine 2 step 1, Routine 6 step 1, the "Why this routine lands its PR itself" paragraph, and the "What stays manual no matter what" wording.

**Related:** [decisions/2026-06-22-automation-routine-auto-merge-pr.md](2026-06-22-automation-routine-auto-merge-pr.md) (the same-day redesign this entry corrects/completes — see the addendum added to that file).

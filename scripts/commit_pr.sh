#!/usr/bin/env bash
# Git/PR helper — wraps the add -> commit -> push -> gh pr create -> merge-main-in
# -> gh pr merge --squash dance documented in prose across .claude/commands/
# (new-position.md, rescore.md, rebalance.md, screen.md, and the same "leave open"
# variant in safe-guard.md / update-orders.md). See scripts/TOKEN-OPTIMIZATION-PLAN.md
# Stage 5 and this script's own PR description for the exact sequence and the
# discrepancy flagged between the "analysts" commands (direct --squash, --auto is
# documented as broken in this repo) and the "sync" commands (enable_pr_auto_merge
# first, falling back to direct --squash) that this script does NOT attempt to
# replicate.
#
# Usage:
#   scripts/commit_pr.sh [--dry-run] [--no-merge] <branch-prefix> "<msg>" <files...>
#
# <branch-prefix>  Branch to commit on. If it already starts with "claude/" it is
#                   used verbatim; otherwise "claude/" is prepended. Reused if it
#                   already exists (locally or on the remote), created from the
#                   current HEAD otherwise.
# <msg>             Commit message AND the PR title.
# <files...>        One or more paths (relative to the repo root) to stage. Must
#                   already exist and already contain the changes to ship.
#
# --dry-run         Print every git/gh command that would run, in order, and exit
#                   0 without touching the repo, the remote, or GitHub.
# --no-merge        Open the PR and leave it open (the safe-guard.md / update-orders.md
#                   "proposal, not a data refresh" path) instead of squash-merging it.
#
# Hard-fails (clear stderr message, non-zero exit, no silent fallback) on: missing
# args, missing files, not a git repo, nothing to commit, a merge conflict pulling
# main into the branch, a rejected push, or a failed gh call. Never force-pushes,
# never force-merges, never overwrites local changes.

set -u

DRY_RUN=0
NO_MERGE=0
POSITIONAL=()

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --no-merge) NO_MERGE=1 ;;
    *) POSITIONAL+=("$arg") ;;
  esac
done

fail() {
  echo "ERROR: $1" >&2
  exit 1
}

if [ "${#POSITIONAL[@]}" -lt 3 ]; then
  fail "usage: commit_pr.sh [--dry-run] [--no-merge] <branch-prefix> \"<msg>\" <files...>"
fi

BRANCH_PREFIX="${POSITIONAL[0]}"
MSG="${POSITIONAL[1]}"
FILES=("${POSITIONAL[@]:2}")

case "$BRANCH_PREFIX" in
  claude/*) BRANCH="$BRANCH_PREFIX" ;;
  *) BRANCH="claude/$BRANCH_PREFIX" ;;
esac

[ -n "$MSG" ] || fail "commit message (arg 2) is empty"

run() {
  # Prints the command always; executes it only outside --dry-run.
  echo "+ $*"
  if [ "$DRY_RUN" -eq 0 ]; then
    "$@"
  fi
}

# --- Preconditions --------------------------------------------------------
# These git queries run even under --dry-run: they read state, they don't change it.

git rev-parse --is-inside-work-tree >/dev/null 2>&1 \
  || fail "not inside a git repository (cwd: $(pwd))"

for f in "${FILES[@]}"; do
  [ -e "$f" ] || fail "file does not exist: $f"
done

command -v gh >/dev/null 2>&1 || fail "gh CLI not found on PATH"

CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")"
[ -n "$CURRENT_BRANCH" ] || fail "could not determine current branch (detached HEAD?)"

# --- Step 1: make sure we're on the target branch -------------------------

BRANCH_EXISTS_LOCAL=0
if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
  BRANCH_EXISTS_LOCAL=1
fi

if [ "$CURRENT_BRANCH" = "$BRANCH" ]; then
  : # already on it, nothing to do
elif [ "$BRANCH_EXISTS_LOCAL" -eq 1 ]; then
  run git checkout "$BRANCH" || fail "failed to check out existing branch '$BRANCH'"
else
  run git checkout -b "$BRANCH" || fail "failed to create branch '$BRANCH' from '$CURRENT_BRANCH'"
fi

# --- Step 2: add + commit --------------------------------------------------

run git add -- "${FILES[@]}" || fail "git add failed for: ${FILES[*]}"

if [ "$DRY_RUN" -eq 0 ]; then
  if git diff --cached --quiet; then
    fail "nothing to commit — staged files match HEAD (${FILES[*]})"
  fi
fi

run git commit -m "$MSG" || fail "git commit failed"

# --- Step 3: push -----------------------------------------------------------

run git push -u origin "$BRANCH" \
  || fail "git push rejected for '$BRANCH' — remote has diverged or is unreachable; fetch/inspect manually, do not force-push"

# --- Step 4: open the PR -----------------------------------------------------

PR_URL=""
if [ "$DRY_RUN" -eq 0 ]; then
  PR_URL="$(gh pr create --title "$MSG" --body "$MSG" --head "$BRANCH" 2>&1)" \
    || fail "gh pr create failed: $PR_URL"
  echo "$PR_URL"
else
  echo "+ gh pr create --title \"$MSG\" --body \"$MSG\" --head \"$BRANCH\""
fi

if [ "$NO_MERGE" -eq 1 ]; then
  echo "--no-merge set: leaving PR open for manual review, as documented in safe-guard.md / update-orders.md."
  exit 0
fi

# --- Step 5: fetch + merge main into the branch, hard-fail on conflict ------
#
# Matches the order documented in new-position.md / rescore.md / rebalance.md /
# screen.md: PR is opened first, then main is pulled in immediately before the
# squash-merge so the PR never merges stale relative to main.

run git fetch origin main || fail "git fetch origin main failed"

if [ "$DRY_RUN" -eq 0 ]; then
  if ! git merge --no-edit origin/main; then
    CONFLICTS="$(git diff --name-only --diff-filter=U)"
    git merge --abort
    fail "merge conflict pulling origin/main into '$BRANCH' in: ${CONFLICTS:-<unknown files>} — resolve by hand (the recurring one is framework/glossary.md: keep both sides' new entries), then re-run"
  fi
else
  echo "+ git merge --no-edit origin/main"
fi

# If the merge actually brought in new commits, the branch tip changed and must
# be re-pushed before the PR can be merged.
run git push origin "$BRANCH" || fail "git push of merge commit failed for '$BRANCH'"

# --- Step 6: squash-merge -----------------------------------------------------
#
# Direct --squash, not --auto: --auto requires branch protection rules, which
# this repo does not have configured (documented explicitly in new-position.md /
# rescore.md / rebalance.md / screen.md).

run gh pr merge --squash --delete-branch "$BRANCH" \
  || fail "gh pr merge --squash failed for '$BRANCH' — PR left open, do not force-merge"

echo "Merged: $BRANCH"

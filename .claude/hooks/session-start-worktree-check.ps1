# SessionStart hook: warns when a local desktop/CLI session is running
# directly on the shared main checkout (not an isolated git worktree),
# where parallel local sessions can collide on the same branch/files.
#
# Browser/mobile (claude.ai/code) sessions already run in their own
# per-session cloud sandbox and are skipped entirely.
#
# Desktop-vs-cloud heuristic (adjust here if it misfires):
#   - cwd is a Windows drive-letter path (e.g. D:\...)  -> local desktop
#   - cwd has no drive letter (POSIX-style container path) -> assume cloud
# This is a heuristic, not a guarantee: a Windows-hosted remote sandbox or a
# WSL path could evade it. Tighten by checking a known local-only signal
# (e.g. $env:COMPUTERNAME against a known list) if it ever misfires.

$cwd = (Get-Location).Path

$isDesktop = $cwd -match '^[A-Za-z]:\\'

if (-not $isDesktop) {
    # Cloud/browser/mobile session - already isolated, nothing to do.
    exit 0
}

$gitDir = git rev-parse --git-dir 2>$null
$commonDir = git rev-parse --git-common-dir 2>$null

if (-not $gitDir -or -not $commonDir) {
    # Not inside a git repo - nothing to check.
    exit 0
}

$gitDirFull = (Resolve-Path $gitDir -ErrorAction SilentlyContinue).Path
$commonDirFull = (Resolve-Path $commonDir -ErrorAction SilentlyContinue).Path

if ($gitDirFull -ne $commonDirFull) {
    # Linked worktree - isolated from other local sessions. Quiet.
    exit 0
}

# Main checkout - shared across every local session on this machine.
$repoName = Split-Path -Leaf (git rev-parse --show-toplevel)
$slug = "session-$(Get-Date -Format yyyyMMdd-HHmmss)"

$msg = @"
LOCAL DESKTOP SESSION on the SHARED MAIN CHECKOUT ($cwd), not an isolated git worktree.
Running parallel local Claude Code sessions here risks branch/file conflicts (same
working tree, same index shared across all of them). At the start of this session,
warn the user once and ask them to set up a dedicated worktree before proceeding:

  git worktree add ../$repoName-$slug -b claude/$slug

Then cd into that new path and relaunch the session there. Only surface this once,
at the start of the conversation - do not repeat it on every turn.
"@

$output = @{
    hookSpecificOutput = @{
        hookEventName     = "SessionStart"
        additionalContext = $msg
    }
} | ConvertTo-Json -Depth 5

Write-Output $output

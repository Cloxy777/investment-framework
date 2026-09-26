"""Tests for scripts/commit_pr.sh.

The script is shell, not Python — there's no existing bats/shell-test setup in this
repo (scripts/tests/ is entirely pytest), so this drives it as a subprocess like any
other CLI under test here, rather than introducing a second test runner (bats) for
one script. Every scenario runs against a disposable tmp_path git repo with a local
bare "remote" — never this real repo — and stubs `gh` on PATH so no real GitHub API
call happens.
"""

import os
import shutil
import stat
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "commit_pr.sh"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "Test",
    "GIT_AUTHOR_EMAIL": "test@example.com",
    "GIT_COMMITTER_NAME": "Test",
    "GIT_COMMITTER_EMAIL": "test@example.com",
}

GH_STUB = """#!/usr/bin/env bash
# Fake `gh` for tests: logs every invocation, never touches the real GitHub API.
echo "$@" >> "$GH_LOG"
case "$1 $2" in
  "pr create")
    echo "https://github.com/example/repo/pull/1"
    exit 0
    ;;
  "pr merge")
    exit "${GH_MERGE_EXIT:-0}"
    ;;
esac
exit 0
"""


def run_git(repo, *args, check=True):
    env = {**os.environ, **GIT_ENV}
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=check,
        env=env,
    )


@pytest.fixture()
def repo_with_remote(tmp_path):
    """origin (bare) <- local clone, both under tmp_path. Starts with one commit on main."""
    origin = tmp_path / "origin.git"
    origin.mkdir()
    subprocess.run(["git", "init", "--bare", "-b", "main", str(origin)], check=True, capture_output=True)

    local = tmp_path / "local"
    subprocess.run(["git", "clone", str(origin), str(local)], check=True, capture_output=True)
    run_git(local, "checkout", "-b", "main")

    (local / "README.md").write_text("hello\n")
    run_git(local, "add", "README.md")
    run_git(local, "commit", "-m", "initial commit")
    run_git(local, "push", "-u", "origin", "main")

    return local


@pytest.fixture()
def gh_stub(tmp_path):
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    gh_path = bin_dir / "gh"
    gh_path.write_text(GH_STUB)
    gh_path.chmod(gh_path.stat().st_mode | stat.S_IEXEC)
    log_path = tmp_path / "gh.log"
    log_path.write_text("")
    return bin_dir, log_path


def run_script(repo, args, bin_dir, gh_log, extra_env=None, check_returncode=False):
    env = {**os.environ, **GIT_ENV}
    env["PATH"] = f"{bin_dir}{os.pathsep}{env['PATH']}"
    env["GH_LOG"] = str(gh_log)
    if extra_env:
        env.update(extra_env)
    result = subprocess.run(
        ["bash", str(SCRIPT), *args],
        cwd=str(repo),
        capture_output=True,
        text=True,
        env=env,
    )
    if check_returncode and result.returncode != 0:
        raise AssertionError(f"script failed: {result.stdout}\n{result.stderr}")
    return result


class TestDryRun:
    def test_prints_sequence_and_touches_nothing(self, repo_with_remote, gh_stub):
        bin_dir, gh_log = gh_stub
        repo = repo_with_remote
        (repo / "notes.md").write_text("draft notes\n")

        before_branch = run_git(repo, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        before_log = run_git(repo, "log", "--oneline").stdout

        result = run_script(
            repo,
            ["--dry-run", "sync-balances", "Sync IBKR cash balances — 2026-09-26", "notes.md"],
            bin_dir,
            gh_log,
        )

        assert result.returncode == 0, result.stderr
        out = result.stdout
        assert "+ git checkout -b claude/sync-balances" in out
        assert "+ git add -- notes.md" in out
        assert '+ git commit -m Sync IBKR cash balances — 2026-09-26' in out or "git commit -m" in out
        assert "+ git push -u origin claude/sync-balances" in out
        assert "gh pr create" in out
        assert "+ git fetch origin main" in out
        assert "gh pr merge --squash" in out

        # Nothing actually happened.
        assert run_git(repo, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip() == before_branch
        assert run_git(repo, "log", "--oneline").stdout == before_log
        assert run_git(repo, "status", "--porcelain").stdout.strip() == "notes.md" or "notes.md" in run_git(repo, "status", "--porcelain").stdout
        assert gh_log.read_text() == ""

    def test_missing_file_hard_fails_before_any_git_call(self, repo_with_remote, gh_stub):
        bin_dir, gh_log = gh_stub
        repo = repo_with_remote
        before_log = run_git(repo, "log", "--oneline").stdout

        result = run_script(
            repo,
            ["--dry-run", "sync-balances", "msg", "does-not-exist.md"],
            bin_dir,
            gh_log,
        )

        assert result.returncode != 0
        assert "ERROR" in result.stderr
        assert "does-not-exist.md" in result.stderr
        assert run_git(repo, "log", "--oneline").stdout == before_log


class TestRealRun:
    def test_full_sequence_order_and_pr_calls(self, repo_with_remote, gh_stub):
        bin_dir, gh_log = gh_stub
        repo = repo_with_remote
        (repo / "notes.md").write_text("draft notes\n")

        result = run_script(
            repo,
            ["rescore-msft", "Rescore MSFT — 2026-09-26", "notes.md"],
            bin_dir,
            gh_log,
            check_returncode=True,
        )

        assert "Merged: claude/rescore-msft" in result.stdout

        # Branch was created, committed, and pushed to the remote.
        assert run_git(repo, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip() == "claude/rescore-msft"
        remote_branches = run_git(repo, "ls-remote", "--heads", "origin").stdout
        # gh stub deletes nothing remotely (real `gh pr merge --delete-branch` is
        # stubbed out), so the pushed branch is still visible on origin — this
        # confirms the push actually landed there.
        assert "claude/rescore-msft" in remote_branches

        log_lines = gh_log.read_text().strip().splitlines()
        assert log_lines[0].startswith("pr create")
        assert "--head claude/rescore-msft" in log_lines[0]
        assert "--title Rescore MSFT" in log_lines[0]
        assert log_lines[1].startswith("pr merge")
        assert "--squash" in log_lines[1]
        assert "claude/rescore-msft" in log_lines[1]

    def test_nothing_to_commit_hard_fails(self, repo_with_remote, gh_stub):
        bin_dir, gh_log = gh_stub
        repo = repo_with_remote
        # README.md already matches HEAD — staging it again yields an empty diff.
        result = run_script(
            repo,
            ["noop-branch", "msg", "README.md"],
            bin_dir,
            gh_log,
        )
        assert result.returncode != 0
        assert "nothing to commit" in result.stderr
        assert gh_log.read_text() == ""

    def test_merge_conflict_hard_fails_and_leaves_clean_state(self, repo_with_remote, gh_stub):
        bin_dir, gh_log = gh_stub
        repo = repo_with_remote

        # A second clone commits a conflicting change to main after our branch forks.
        other = repo.parent / "other-clone"
        subprocess.run(["git", "clone", str(repo.parent / "origin.git"), str(other)], check=True, capture_output=True)
        (other / "README.md").write_text("changed upstream\n")
        run_git(other, "add", "README.md")
        run_git(other, "commit", "-m", "upstream change")
        run_git(other, "push", "origin", "main")

        # Our branch changes the same line, so pulling main back in conflicts.
        (repo / "README.md").write_text("changed locally\n")

        result = run_script(
            repo,
            ["conflict-branch", "msg", "README.md"],
            bin_dir,
            gh_log,
        )

        assert result.returncode != 0
        assert "merge conflict" in result.stderr
        assert "README.md" in result.stderr

        # PR create ran (it happens before the merge-main step) but merge never did.
        log_lines = gh_log.read_text().strip().splitlines()
        assert any(line.startswith("pr create") for line in log_lines)
        assert not any(line.startswith("pr merge") for line in log_lines)

        # No leftover conflict markers / no dangling merge state.
        status = run_git(repo, "status", "--porcelain").stdout
        assert "UU" not in status
        merge_head = repo / ".git" / "MERGE_HEAD"
        assert not merge_head.exists()

    def test_no_merge_flag_leaves_pr_open(self, repo_with_remote, gh_stub):
        bin_dir, gh_log = gh_stub
        repo = repo_with_remote
        (repo / "notes.md").write_text("proposal only\n")

        result = run_script(
            repo,
            ["--no-merge", "safe-guard", "Safe-Guard: margin exposure alert — 2026-09-26", "notes.md"],
            bin_dir,
            gh_log,
            check_returncode=True,
        )

        assert "leaving PR open" in result.stdout
        log_lines = gh_log.read_text().strip().splitlines()
        assert any(line.startswith("pr create") for line in log_lines)
        assert not any(line.startswith("pr merge") for line in log_lines)

    def test_gh_pr_merge_failure_hard_fails(self, repo_with_remote, gh_stub):
        bin_dir, gh_log = gh_stub
        repo = repo_with_remote
        (repo / "notes.md").write_text("draft\n")

        result = run_script(
            repo,
            ["will-fail", "msg", "notes.md"],
            bin_dir,
            gh_log,
            extra_env={"GH_MERGE_EXIT": "1"},
        )

        assert result.returncode != 0
        assert "gh pr merge --squash failed" in result.stderr

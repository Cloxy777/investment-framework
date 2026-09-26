#!/bin/bash
# SessionStart hook: installs the Python packages scripts/*.py depend on
# (yfinance, pandas, lxml, pytest - see scripts/requirements.txt) so
# /healthcheck and the scoring/sync scripts work without a manual pip
# install first. Local desktop sessions typically already have these
# installed via the developer's own environment, so this only runs for
# Claude Code on the web / remote sessions.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"
pip install -q -r scripts/requirements.txt

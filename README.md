# Investment Framework

A private, version-controlled home for the **Quality Value + Dynamic Trimming** investment framework — its rules, operating procedures, and the running record of decisions made under it.

## Layout

```
framework/      the rules: strategy, valuation scoring, fair value methodology,
                operating brief (Claude system prompt), operating calendar
portfolio/      current holdings + broker sync SOP
sessions/       dated logs of every analysis session (screenings, re-scores, evaluations)
decisions/      dated logs of actions taken, why, and framework-change rationale
.claude/commands/  slash commands for routine tasks (/screen, /rescore, /rebalance, ...)
```

See [CLAUDE.md](CLAUDE.md) for how Claude should use this repo, and [framework/operating-brief.md](framework/operating-brief.md) for the full operating rules.

## Working from PC vs. phone

- **PC (Claude Code):** full workflow — run `/screen`, `/rescore`, `/new-position`, `/rebalance`, edit framework docs, commit changes.
- **Phone:** for quick reviews on the go, use a Claude.ai Project synced to this repo's `framework/` docs (or paste [operating-brief.md](framework/operating-brief.md) as a system prompt), and the GitHub mobile app to read/comment on session logs and framework docs. Formalize any framework tweaks back into the repo from your PC.

## Iterating

Every change to a rule, threshold, or upgrade should be a commit with a clear message — that's the audit trail for how and why the framework evolved. Pair it with an entry in `decisions/` explaining the *why*.

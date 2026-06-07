# Investment Framework

This repo is the single source of truth for the **Quality Value + Dynamic Trimming** investment framework: its rules, its operating procedures, and the running record of decisions made under it. The goal is to iterate on the framework over time (tracked via commits) and to use Claude to execute routine analyst tasks against it.

## Orientation

- **`framework/`** — the rules themselves. Read these before any analysis task:
  - [strategy.md](framework/strategy.md) — the 6-phase framework, Rate Environment Gate, 7 hybrid upgrades
  - [valuation-scoring.md](framework/valuation-scoring.md) — how the 1–10 valuation score is computed
  - [fair-value-methodology.md](framework/fair-value-methodology.md) — fair value, buy/sell/stop pricing, position sizing, the 10-rule FV framework
  - [operating-brief.md](framework/operating-brief.md) — the full system-prompt-style brief that governs how Claude should behave in analysis sessions
  - [operating-calendar.md](framework/operating-calendar.md) — when routine tasks are due, and the data templates to fill in
- **`portfolio/`** — [holdings.md](portfolio/holdings.md) (current positions/weights/scores) and [sync-sop.md](portfolio/sync-sop.md) (how to pull live broker data into Notion)
- **`sessions/`** — dated logs of every analysis session (screenings, re-scores, evaluations, rebalances)
- **`decisions/`** — dated logs of actual actions taken and the reasoning, plus framework-change rationale

## How to behave in analysis sessions

Follow [operating-brief.md](framework/operating-brief.md) as the governing system prompt for any task type: SCREENING, RESCORE, NEW POSITION, TRIM REVIEW, EXIT REVIEW, REBALANCE. Key non-negotiables baked into the framework:

- **Never invent or estimate financial data.** If a metric is missing, stop and ask.
- **Always fetch live prices first** (Rule 0 in [fair-value-methodology.md](framework/fair-value-methodology.md)) — never infer price from valuation multiples. This caused a real, costly error before (see the SPGI lesson in that file).
- **Show every calculation** — sub-scores, modifiers, the works. No black-box outputs.
- **Act only on documented triggers** — a valuation-score change or a fundamental event, never on price movement alone.

## Routine tasks → slash commands

Use these instead of re-deriving the process each time (defined in `.claude/commands/`):

- `/screen [universe]` — Phase 01 universe screening → Qualified Quality List
- `/new-position [ticker]` — full evaluation of a candidate, end-to-end through order setup
- `/rescore [tickers]` — quarterly post-earnings re-score
- `/rebalance` — portfolio-wide trim/exit review and capital recycling plan
- `/sync-portfolio [broker]` — pull live broker positions into Notion and refresh `holdings.md`

Every session should be saved to `sessions/` and, where it leads to an actual trade, logged in `decisions/` — that's what lets the framework be audited and improved (Rule 10).

## Iterating on the framework itself

When a framework rule changes (a new hybrid upgrade, a revised threshold, a lesson learned from a bad call), edit the relevant file under `framework/` directly and record *why* in `decisions/` — that record is what makes the framework's evolution traceable and auditable in git history, rather than living only in chat transcripts.

## Source material

`claude-projects/` contains the raw Notion export this framework was originally compiled from (kept for reference/traceability). The structured docs under `framework/` and `portfolio/` are the canonical, maintained versions — edit those, not the raw export.

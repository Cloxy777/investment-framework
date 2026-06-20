# Investment Framework

This repo is the single source of truth for the **Quality Value + Dynamic Trimming** investment framework: its rules, its operating procedures, and the running record of decisions made under it. The goal is to iterate on the framework over time (tracked via commits) and to use Claude to execute routine analyst tasks against it.

## Orientation

- **`framework/`** — the rules themselves. Read these before any analysis task:
  - [strategy.md](framework/strategy.md) — the 6-phase framework, Rate Environment Gate, 7 hybrid upgrades
  - [valuation-scoring.md](framework/valuation-scoring.md) — how the 0–100.0 valuation score is computed
  - [fair-value-methodology.md](framework/fair-value-methodology.md) — fair value, buy/sell/stop pricing, position sizing, the 10-rule FV framework
  - [operating-brief.md](framework/operating-brief.md) — the full system-prompt-style brief that governs how Claude should behave in analysis sessions
  - [operating-calendar.md](framework/operating-calendar.md) — when routine tasks are due, and the data templates to fill in
  - [automation-schedule.md](framework/automation-schedule.md) — how the operating calendar maps to scheduled Claude Code Routines (prompts, cadences, environment setup) and the Google Calendar export
  - [graveyard-audit.md](framework/graveyard-audit.md) — survivorship-bias case studies (GE, Nokia, Valeant, Wirecard, IBM, ...) and the framework gaps each one closed; reviewed/expanded annually in Q1
  - [benchmark-comparison.md](framework/benchmark-comparison.md) — tracks the framework against MSCI Quality Index and the QMJ factor, not just the S&P 500; updated annually in Q1
  - [investor-philosophy-alignment.md](framework/investor-philosophy-alignment.md) — high-level core tenets of Buffett/Munger/Lynch/Greenblatt/Marks plus an alignment checklist; check any new or revised framework rule against it before adopting it
  - [glossary.md](framework/glossary.md) — plain-English definitions of financial jargon and framework-specific terms; every output cites the relevant entries in a closing "Glossary" section (see below)
- **`portfolio/`** — [holdings.md](portfolio/holdings.md) (current positions/weights/scores), [sync-sop.md](portfolio/sync-sop.md) (how to pull live broker data into [`snapshots/`](portfolio/snapshots/) and refresh holdings), and [override-log.md](portfolio/override-log.md) (every position entered outside the framework's rules, tracked and reviewed annually)
- **`watchlist/`** — [README.md](watchlist/README.md) explains the convention: a per-ticker, dated "current state" pointer (split into `in-portfolio/` and `not-in-portfolio/`) to the latest score/action for every ticker `/new-position` or `/rescore` has touched. Updated by those two commands and reconciled by `/sync-portfolio`; `sessions/` remains the canonical record of how each number was derived.
- **`sessions/`** — dated logs of every analysis session (screenings, re-scores, evaluations, rebalances)
- **`decisions/`** — dated logs of actual actions taken and the reasoning, plus framework-change rationale

## How to behave in analysis sessions

Follow [operating-brief.md](framework/operating-brief.md) as the governing system prompt for any task type: SCREENING, RESCORE, NEW POSITION, TRIM REVIEW, EXIT REVIEW, REBALANCE. Key non-negotiables baked into the framework:

- **Never invent or estimate financial data.** If a metric is missing, stop and ask.
- **Always fetch live prices first** (Rule 0 in [fair-value-methodology.md](framework/fair-value-methodology.md)) — never infer price from valuation multiples. This caused a real, costly error before (see the SPGI lesson in that file).
- **Show every calculation** — sub-scores, modifiers, the works. No black-box outputs.
- **Act only on documented triggers** — a valuation-score change or a fundamental event, never on price movement alone.
- **Decode jargon in a closing Glossary section.** The user is not a finance professional — every response, session log, decision log, and PR description ends with a "Glossary" section defining the jargon/abbreviations it used, sourced from [glossary.md](framework/glossary.md) (add new terms there first if missing). See operating-brief.md OUTPUT FORMAT step 9.

## Routine tasks → slash commands

Use these instead of re-deriving the process each time (defined in `.claude/commands/`):

- `/screen [universe]` — Phase 01 universe screening → Qualified Quality List
- `/new-position [ticker]` — full evaluation of a candidate, end-to-end through order setup
- `/rescore [tickers]` — quarterly post-earnings re-score
- `/rebalance` — portfolio-wide trim/exit review and capital recycling plan
- `/sync-portfolio [broker]` — full sync: for IBKR, runs positions + cash balances + active orders in one pass; for Freedom Finance, the manual screenshot flow. Refreshes `portfolio/snapshots/` and `holdings.md`
- `/sync-positions` — IBKR positions only → `portfolio/snapshots/ibkr.md` + `holdings.md`
- `/sync-balances` — IBKR cash balances only → `portfolio/snapshots/ibkr.md` + `holdings.md`
- `/sync-orders` — IBKR active/working orders only → `portfolio/snapshots/ibkr-orders.md`

Every session should be saved to `sessions/` and, where it leads to an actual trade, logged in `decisions/` — that's what lets the framework be audited and improved (Rule 10).

## Iterating on the framework itself

When a framework rule changes (a new hybrid upgrade, a revised threshold, a lesson learned from a bad call), edit the relevant file under `framework/` directly and record *why* in `decisions/` — that record is what makes the framework's evolution traceable and auditable in git history, rather than living only in chat transcripts.

## Source material

The structured docs under `framework/` and `portfolio/` are the canonical, maintained versions, fully migrated from the original Notion export (which has been removed from the repo — see git history at the migration commit if you need the raw source).

# 2026-06-20 — Convention: stale-score marking when the scoring methodology changes

**What prompted it:**

After the 2026-06-20 scoring-methodology changes (the Upside/Downside Modifier and the PEG clean-earnings clarification), watchlist entries scored under the *old* methodology are no longer comparable to freshly-computed scores. The user asked for a **general, repeatable mechanism** — not a one-off — to mark prior scores stale and to clear the mark once they're rescored: *methodology adjusted → previous items marked → score re-applied → marks removed.*

**Design decision (how to mark):**

The user's initial idea was to rename each stale ticker folder to `<TICKER>[OLD]`. Rejected in favour of an **in-file banner + central registry**, because the per-ticker folder path `watchlist/<in|not>-portfolio/<TICKER>/<TICKER>-YYYY-MM-DD.md` is load-bearing: `/rescore`, `/new-position`, and `/sync-portfolio` read/write `<TICKER>/`, and `holdings.md` + `sessions/` link directly into those folders. Renaming folders would break those links and orphan the renamed folder when a command later recreates a clean `<TICKER>/`. The banner+registry approach gives the same at-a-glance visibility without touching any paths. *(User chose this option.)*

**The mechanism (now a standing convention):**

1. **Methodology version** — a date stamp at the top of `framework/valuation-scoring.md`. Bump it whenever a change materially alters how the score is computed (new/changed sub-score, modifier, weight, or eligibility rule), and record why in `decisions/`.
2. **Mark (on a version bump)** — every watchlist entry carrying a *numeric* score from an older version gets: (a) a one-line `⚠️ STALE SCORE` banner at the top of its entry file, and (b) a row in the central registry `watchlist/STALE.md`. Entries that are "Phase 01 FAIL / not scored" are **not** marked — there is no Phase 02 score for the change to invalidate.
3. **Clear (on rescore)** — `/rescore` (held) and `/new-position` (not held) each remove the ticker's banner and delete its `STALE.md` row when they write a fresh entry under the current methodology. The registry is self-emptying as the book is brought current.

**Applied now (methodology version 2026-06-20):**

- All in-portfolio holdings + AVGO were already rescored under the new methodology today → current, not marked.
- Of the 17 not-in-portfolio entries, **6 carry a numeric pre-modifier score and were flagged stale**: 0700-HK (31.0), DB1 (47.8), EXPN (32.0), MA (53.3), PDD (5.0), SGE (21.1).
- The other 10 not-in-portfolio entries (CIEN, CRM, DASH, FICO, GTLB, HIMS, MELI, ORCL, PYPL, TTD) plus MU are Phase 01 FAIL / not scored → not marked.

**Files touched:**
- `watchlist/STALE.md` — new central registry (created).
- `watchlist/<...>/{0700-HK,DB1,EXPN,MA,PDD,SGE}-*.md` — STALE banner added.
- `watchlist/README.md` — new "Stale scores — when the scoring methodology changes" section.
- `framework/valuation-scoring.md` — scoring methodology version stamp added (2026-06-20, with version history).
- `.claude/commands/rescore.md`, `.claude/commands/new-position.md` — added the "clear stale-score mark" step.
- `CLAUDE.md` — "Iterating on the framework" now points to the version bump + stale-mark step.
- `decisions/` — this file.

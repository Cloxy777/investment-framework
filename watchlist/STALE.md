# Stale-score registry

A central, at-a-glance list of watchlist entries whose **valuation score predates the current scoring methodology** and is therefore not comparable to current scores. This is the general staleness mechanism — see [README.md](README.md#stale-scores--when-the-scoring-methodology-changes) for how it works.

**How an entry lands here:** when the scoring methodology version (see [valuation-scoring.md](../framework/valuation-scoring.md)) is bumped, every watchlist entry that carries a *numeric* score computed under an older version is flagged stale (a banner is added to the entry file and a row is added below). Entries that are "Phase 01 FAIL / not scored" are **not** flagged — there is no Phase 02 score for a methodology change to invalidate.

**How an entry leaves here:** when `/rescore` (held) or `/new-position` (not held) writes a fresh entry under the current methodology, that command removes the entry's banner **and** deletes its row here.

---

## Current methodology version: **2026-06-29**
*(Quality Score + 80.0+ gate + Composite Score added — see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md).)*

This version adds a new score (Quality Score) and a new combined number (Composite Score) on top of the existing valuation score — it does not change how the valuation score itself is computed, but every entry below still needs both new numbers computed before it's current. Per-ticker rows only — no blanket notes — so each one clears individually the moment `/rescore` or `/new-position` touches that ticker.

## Stale entries — 2026-06-29 methodology (Quality Score / Composite Score pending)

| Ticker | Location | Score | Scored (date) | Flagged stale |
|--------|----------|-------|----------------|----------------|
| UBER | in-portfolio | 34.8 | 2026-06-20 | 2026-06-29 |
| ZS | in-portfolio | 36.3 (EV/EBIT placeholder; held as override — Phase 01 GAAP quality gate fails, see override-log.md) | 2026-06-20 | 2026-06-29 |
| 0700-HK | not-in-portfolio | 31.0 | 2026-06-14 | 2026-06-29 |
| DB1 | not-in-portfolio | 47.8 | 2026-06-19 | 2026-06-29 |
| EXPN | not-in-portfolio | 32.0 | 2026-06-19 | 2026-06-29 |
| MA | not-in-portfolio | 38.0 | 2026-06-22 | 2026-06-29 |
| SGE | not-in-portfolio | 21.1 | 2026-06-19 | 2026-06-29 |

*Not listed (no real Phase 02 score for this addition to invalidate): every not-in-portfolio entry that is Phase 01 FAIL / not scored (CBRS, CCL, CHTR, CIEN, CRM, CVX, DASH, FDX, FICO, FUBO, GTLB, HIMS, IBM, LULU, MCD, MELI, MU, NOK, ORCL, PLTR, PYPL, TTD, TTWO, WSE) and the in-portfolio rows that are cash/non-equity/override/quality-gate-fail (RBRK, STIM, TLT, XEON). BULL, HY9H, SOFI, and SSU also excluded — each is Phase 01 FAIL with a Phase 02 number computed only for the record, never a binding score. (CBRS, CHTR, FUBO, and LULU additionally now carry a Quality Score under the engine added this same date — see each ticker's session file — but that score still fails the 80.0+ gate, so no Phase 02/Composite Score exists to go stale either way.)*

**AVGO resolved 2026-07-04:** rescored under the full current methodology (Quality 82.1, Valuation 68.2, Composite 43.1) — see [sessions/2026-07-04-rescore-avgo.md](../sessions/2026-07-04-rescore-avgo.md) and [in-portfolio/AVGO/AVGO-2026-07-04.md](in-portfolio/AVGO/AVGO-2026-07-04.md), which supersedes both the old 69.5 and the never-adopted 74.8 figures. `watchlist/not-in-portfolio/AVGO/` remains a leftover duplicate folder (AVGO is held, per `holdings.md`) that `/sync-portfolio` should still fold into `in-portfolio/`.

## Stale entries — 2026-06-20 methodology (Upside/Downside Modifier) — pending rescore

| Ticker | Location | Stale score | Scored (methodology) | Flagged stale |
|--------|----------|-------------|----------------------|---------------|
| 0700-HK | not-in-portfolio | 31.0 | 2026-06-14 (pre-modifier) | 2026-06-20 |
| DB1 | not-in-portfolio | 47.8 | 2026-06-19 (pre-modifier) | 2026-06-20 |
| EXPN | not-in-portfolio | 32.0 | 2026-06-19 (pre-modifier) | 2026-06-20 |
| SGE | not-in-portfolio | 21.1 | 2026-06-19 (pre-modifier) | 2026-06-20 |

*MA removed from this table during the 2026-06-29 update: `MA-2026-06-22.md` already carries a fresh post-modifier score (38.0, scored 2026-06-22) and never carried a 2026-06-20 banner — the row was simply never cleared when that rescore happened. Corrected here as a registry bookkeeping fix, not a re-score.*

*Not listed (not affected by the 2026-06-20 Phase 02 change): the 10 not-in-portfolio entries that are Phase 01 FAIL / not scored (CIEN, CRM, DASH, FICO, GTLB, HIMS, MELI, ORCL, PYPL, TTD) and MU (Phase 01 FAIL). All in-portfolio holdings except AVGO (see note above) were rescored under the current methodology on 2026-06-20 and are current on that axis.*

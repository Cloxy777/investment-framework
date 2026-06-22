# Stale-score registry

A central, at-a-glance list of watchlist entries whose **valuation score predates the current scoring methodology** and is therefore not comparable to current scores. This is the general staleness mechanism — see [README.md](README.md#stale-scores--when-the-scoring-methodology-changes) for how it works.

**How an entry lands here:** when the scoring methodology version (see [valuation-scoring.md](../framework/valuation-scoring.md)) is bumped, every watchlist entry that carries a *numeric* score computed under an older version is flagged stale (a banner is added to the entry file and a row is added below). Entries that are "Phase 01 FAIL / not scored" are **not** flagged — there is no Phase 02 score for a methodology change to invalidate.

**How an entry leaves here:** when `/rescore` (held) or `/new-position` (not held) writes a fresh entry under the current methodology, that command removes the entry's banner **and** deletes its row here.

---

## Current methodology version: **2026-06-20**
*(Upside/Downside Modifier + PEG clean-earnings clarification — see [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md) and [decisions/2026-06-20-framework-clarification-peg-clean-earnings.md](../decisions/2026-06-20-framework-clarification-peg-clean-earnings.md).)*

## Stale entries (pending rescore)

| Ticker | Location | Stale score | Scored (methodology) | Flagged stale |
|--------|----------|-------------|----------------------|---------------|
| 0700-HK | not-in-portfolio | 31.0 | 2026-06-14 (pre-modifier) | 2026-06-20 |
| DB1 | not-in-portfolio | 47.8 | 2026-06-19 (pre-modifier) | 2026-06-20 |
| EXPN | not-in-portfolio | 32.0 | 2026-06-19 (pre-modifier) | 2026-06-20 |
| MA | not-in-portfolio | 53.3 | 2026-06-14 (pre-modifier) | 2026-06-20 |
| PDD | not-in-portfolio | 5.0 | 2026-06-14 (pre-modifier) | 2026-06-20 |
| SGE | not-in-portfolio | 21.1 | 2026-06-14 (pre-modifier) | 2026-06-20 |

*Not listed (not affected by the 2026-06-20 Phase 02 change): the 10 not-in-portfolio entries that are Phase 01 FAIL / not scored (CIEN, CRM, DASH, FICO, GTLB, HIMS, MELI, ORCL, PYPL, TTD) and MU (Phase 01 FAIL). All in-portfolio holdings + AVGO were rescored under the current methodology on 2026-06-20 and are current.*

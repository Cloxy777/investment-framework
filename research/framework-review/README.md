# Framework review vs. the Matrix — index and executive summary

Review of this repo's *Quality Value + Dynamic Trimming* framework against the external reference system documented in `[matrix research folder]/`. **Proposals only** — no framework, portfolio, script or command file was changed. Draft for your review; nothing has been adopted.

## Files

| File | Content |
|---|---|
| [01-verification.md](01-verification.md) | 46 re-derivations of the Matrix's worked examples/test vectors, 17 consistency findings, resolution of the open items, confidence per rule block |
| [02-gap-analysis.md](02-gap-analysis.md) | 40-row comparison table, "where we are stronger", caveats |
| [03-proposals.md](03-proposals.md) | P-001…P-020 in the full template, command-by-command additions, new commands, rejected ideas R-01…R-14 |
| [04-design.md](04-design.md) | Implementation-ready designs for 8 proposals (+ sketch), tests, command-file diffs (not applied) |
| [05-validation.md](05-validation.md) | Paired comparison on 14 tickers, backtest design, one-session pilot, acceptance/rollback |
| [06-roadmap.md](06-roadmap.md) | Ranked roadmap, dependencies, six draft decision entries |
| [open-questions-for-user.md](open-questions-for-user.md) | Decisions only you can make; facts to re-check on the site |

## Executive summary

**Verification.** The Matrix's 5-year "x2" arithmetic reproduces exactly on ABNB and NVDA (high confidence). Some rules do not: the *Capital & SBC* table (sub-point maxima sum to 21 for a weight of 10), the "unknown = 40%" claim, the STRONG BUY precondition, and ABNB's S&P lens and growth sub-score. No proposal depends on those blocks.

**Comparison.** Paired on 10 names, quality gates agree on 6; the repo never says "buy" where the Matrix says "avoid", but is stricter at the buy decision (gate, Composite band, R/R, sizing). The Matrix has no trimming, exits, fair value, R/R or rate gate — the repo's main strengths.

**Top 10 changes (ranked)**
1. **P-013** Fix three spec defects: PEG denominator, the undefined 10–20% PE band that makes the script refuse, Phase 01 threshold drift. (P0)
2. **P-003** Pre-registered earnings kill-lines from existing thresholds. (P0)
3. **P-002** Cycle-peak flag — MU is protected today only by a trough year in the rolling FCF window. (P0)
4. **P-007** Show SBC and FCF yield after SBC now; score it later after a pilot. (P0/P1)
5. **P-010** Structured score snapshots + "what changed". (P1)
6. **P-001** 5-year consensus-path return and buy-price-for-target-return curve, as a cross-check only. (P1)
7. **P-008** `/flags` numeric checklist, no score penalties. (P1)
8. **P-011** Portfolio-weighted Quality/Composite with coverage disclosure (current: 79.4 / 33.7, 67% coverage; only 37.6% of the book is ≥ 80.0). (P1)
9. **P-009** Three-state gate (PASS/AMBER/FAIL) — needs your decision on strictness. (P1)
10. **P-006** Competence-circle registry — needs your list. (P1)

**Biggest risks.** Over-fitting to the Matrix's 2026 constants; building on its inconsistent rules; double counting (SBC, flags); loosening the strict gate by stealth; thin free-tier consensus data; process bloat.

**What NOT to copy.** The Capital & SBC table, 15%/14% bars, 4% "good yield", index P/E constants, mega-cap tweak, reader position ranges, "reviewed by" tags, PEG for all companies, guidance as a scored input, penalty-based flags, the discrete verdict map.

**Next step.** Review [open-questions-for-user.md](open-questions-for-user.md); decide consensus data, gate strictness and the stop-list; then Wave 0 (P-013, P-003, P-002, P-007 A) needs no version bump.

## Glossary

From [framework/glossary.md](../../framework/glossary.md): **Composite Score**, **Quality Score**, **Valuation Score**, **Rule 9**, **FCF yield**, **SBC (Stock-Based Compensation)**, **PEG ratio**, **CAGR**, **Hard disqualifier**, **Owner Earnings**, **Turnover (portfolio turnover)**.

New terms (not yet in glossary.md): **Kill-line**, **three-state gate (PASS/AMBER/FAIL)**, **cycle peak**, **x2 arithmetic**, **competence circle / stop-list**, **hysteresis**, **coverage**, **consensus**, **point-in-time**, **look-ahead / survivorship bias**, **backtest** — definitions are in the glossary section of each numbered file.

## Files created

`README.md`, `01-verification.md`, `02-gap-analysis.md`, `03-proposals.md`, `04-design.md`, `05-validation.md`, `06-roadmap.md`, `open-questions-for-user.md` (all in `research/framework-review/`).

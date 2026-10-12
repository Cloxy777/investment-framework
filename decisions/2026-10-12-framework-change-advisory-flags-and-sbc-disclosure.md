# 2026-10-12 — Framework change: advisory flags and SBC disclosure (Phase A, no score effect)

**What prompted it:**

A review of the framework against an external reference system ([research/framework-review/](../research/framework-review/), PR #884) found blind spots the scores cannot see on their own, and the user approved adopting the corresponding ideas — in phases, so that no score changes until a pilot has been run. Concrete gaps in the written rules as of today:

- **SBC.** FCF yield is 40% of the Valuation Score and uses reported FCF, which adds back stock-based compensation. `grep` of `framework/` finds no SBC treatment at all, and dilution appears only as a qualitative line in strategy.md. Upgrade 1 (Owner Earnings) bears SBC through GAAP net income but covers only MSFT, Alphabet, Meta and Amazon.
- **Cycle peaks.** per the framework review's P-002 ([03-proposals.md](../research/framework-review/03-proposals.md)), MU's Quality Score was held down only by a trough year still inside the rolling 3-year FCF window (see the [MU watchlist entries](../watchlist/not-in-portfolio/MU)); nothing in the framework recognises peak-cycle earnings when that year rolls out.
- **Rich multiple without growth / low multiple with falling earnings.** Continuous sub-scores can net these against other inputs without any visible warning.

**The decision:**

Add **advisory flags** and an **SBC block** that print at analysis time and change **no** score, band or eligibility rule:

| Item | Rule (thresholds are uncalibrated placeholders †) |
|---|---|
| `CYCLE_PEAK_CANDIDATE` / `LOSS_TO_PROFIT_BASE` | GAAP diluted EPS (TTM) > +100% YoY on a positive base † / prior base ≤ 0 |
| `MULTIPLE_CEILING` | forward PE ≥ 30 † and forward EPS growth < 30% † |
| `VALUE_TRAP_CANDIDATE` | 0 < forward PE ≤ 15 † and TTM EPS growth < 0 |
| SBC block | SBC/FCF and FCF yield after SBC beside the reported yield; `elevated` ≥ 30% †, `severe` ≥ 100% † (or FCF ≤ 0 with SBC > 0) |

The analyst must state in the session log how each raised flag was handled; `UNKNOWN` (data missing — notably yfinance often lacks 8 quarters of Diluted EPS) is recorded as a gap, never estimated.

**Deliberately not in this change** (recorded so the scope is auditable):

- **No scoring change, no methodology-version bump, no stale-score run.** `FCF_Score` still uses reported FCF yield.
- **`severe` SBC is a label, not a hard disqualifier.** A disqualifier is an eligibility rule and would change who passes the gate; it is a Phase B item.
- **Phase B** — SBC-adjusted FCF yield (scored), SBC ≥ 100% disqualifier, operating-margin Quality input, capex/growth-source discipline, hysteresis on action-band edges (the user chose action bands, **not** the 80.0 Quality gate), cycle-peak/ceiling as scored limits — is specified in [research/framework-review/07-phase-b-plan.md](../research/framework-review/07-phase-b-plan.md) with a pilot and acceptance criteria; to ship as one methodology bump after the pilot.
- Not adopted at all: the three-state (AMBER) Quality gate; the reference system's flag-penalty scheme, discrete verdict map, unknown-input defaults and registry tags (see [03-proposals.md](../research/framework-review/03-proposals.md) section R).
- P-013 spec fixes (PEG denominator, 10–20% PE-band gap, Phase 01 threshold drift) need user rulings and are not touched here.

**Alignment check ([investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md)):** Buffett/Munger (SBC is a real owner cost; consistent with Upgrade 1) pass; Marks (cycle awareness) pass; Lynch (cyclicals/value traps need different treatment) pass; Greenblatt (systematic, no discretionary override of scores) pass — flags never alter a score. Price-action, turnover, macro-veto, concentration, guidance tests: not engaged.

**Graveyard test:** none of the seven [graveyard-audit.md](../framework/graveyard-audit.md) cases is a cycle-peak or SBC failure, so this fills a hole in the audit rather than one the audit caught; nominate a memory/commodity peak case and an SBC-driven case for the next Q1 review.

**Impact:** no score changes; `fetch_fundamentals` output gains an `advisory` block; `/new-position` and `/rescore` paste it and address raised flags. Acceptance: unit tests for every boundary (exactly 100% growth is not flagged, ≤ 0 bases, missing/UNKNOWN, fiscal-year-change stub quarters). Rollback: delete the flags module and the advisory block — nothing else depends on them.

**Files touched:**
- `scripts/scoring/flags_common.py` (new), `scripts/scoring/sbc.py` (new), `scripts/fetch_fundamentals.py`
- `scripts/tests/test_flags_common.py` (new), `scripts/tests/test_sbc.py` (new), `scripts/tests/test_fetch_fundamentals.py`
- `framework/valuation-scoring.md` (new "Advisory Flags" section, version unchanged), `framework/glossary.md`
- `.claude/commands/new-position.md`, `.claude/commands/rescore.md`
- `research/framework-review/07-phase-b-plan.md` (new), `research/framework-review/README.md`
- `decisions/` — this file.

## Glossary
- **Advisory flag:** a warning printed during analysis that changes no score or action by itself.
- **SBC (stock-based compensation):** pay in shares or options; costs owners through dilution but is added back in reported free cash flow.
- **FCF yield after SBC:** (free cash flow − SBC) ÷ market cap.
- **Cycle peak:** the top of a business cycle, when earnings are temporarily inflated.
- **Multiple ceiling:** forward PE of 30+ with forward EPS growth under 30%.
- **Value trap:** a stock that looks cheap because earnings are falling.
- **Hard disqualifier:** a rule failure that blocks a stock regardless of its other scores.
- **Methodology version bump / stale-score run:** the repo's procedure for flagging old scores after a scoring-rule change; not triggered by this change.
- **Placeholder (†):** a threshold chosen or copied but not yet calibrated on this repo's data.
- **Hysteresis:** a buffer around a threshold so a state doesn't flip on tiny moves (Phase B).

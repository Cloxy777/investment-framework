# Part 7 — Phase B plan: scored changes (not yet applied)

**Status: plan only. Nothing here is applied.** *Pilot run 2026-10-12 — results and revised recommendation (adopt B1+B2, drop B3, park B5, B6 awaiting data) in [08-phase-b-pilot-results.md](08-phase-b-pilot-results.md).* Phase A (this plan's predecessor) shipped as [decisions/2026-10-12-framework-change-advisory-flags-and-sbc-disclosure.md](../../decisions/2026-10-12-framework-change-advisory-flags-and-sbc-disclosure.md): advisory flags and the SBC block, no score effect, no methodology bump.

On 2026-10-12 the user approved adopting the items below and chose a **phased** rollout: advisory/no-score items first (done), scored items only after a pilot, then as **one** methodology-version bump with **one** stale-score run (per [06-roadmap.md](06-roadmap.md) §2 — separate bumps would stale-flag overlapping watchlist entries repeatedly). For hysteresis the user chose **action-band edges** (the 70.0 / 80.0 / 90.0 trim bands and the 30.0 / 50.0 entry bands), *not* the 80.0 Quality gate — so the three-state gate (P-009 / Draft F) stays **not adopted**.

Every number below is a **placeholder (†)**: taken from the external reference system or chosen here, not calibrated on this repo's holdings. The pilot exists to replace them.

## Changes to pilot

| ID | Change | Where it lands | Placeholder parameters (†) |
|---|---|---|---|
| B1 | **SBC-adjusted FCF yield scored.** `FCF_Score` uses `FCF yield − SBC yield` for names *not* on Owner Earnings (Upgrade 1 already bears SBC via GAAP net income). Guard: `sbc_adjust=true` requires `buyback_yield_basis == "gross_cash"` so SBC dilution isn't counted twice (once in the yield, once in Upside/Downside shareholder yield). Design: [04-design.md D2](04-design.md). | `valuation_score.py`, [valuation-scoring.md](../../framework/valuation-scoring.md) FCF sub-score | none new — uses the measured SBC |
| B2 | **SBC ≥ 100% of FCF as a hard disqualifier** (today only the `severe` advisory label). | [quality-scoring.md](../../framework/quality-scoring.md) hard disqualifiers, `quality_score.py` | 100% † |
| B3 | **Operating margin in the Quality Margins sub-score.** Today: gross margin ÷ 80 (favours software, penalises retail/payments/hardware). Candidate: the lower of net margin and after-tax operating margin, bucketed on this repo's continuous scale, with a falling-trend penalty. Pilot compares both on all holdings before choosing; weight (15%) stays. | `quality_score.py`, quality-scoring.md Margins | scale endpoints †, trend penalty † |
| B4 | **Capex / growth-source discipline in Quality.** Score organic vs acquisition-driven growth, and capex funded by debt/issuance (> 25% of capex † external financing). Encodes the GE / Valeant lessons from [graveyard-audit.md](../../framework/graveyard-audit.md) as a number. Needs a place in the Quality weights (e.g. a share of Growth or Balance Sheet) — pilot decides, no new top-level weight without the user. | quality-scoring.md, `quality_score.py` | 25% †, point values † |
| B5 | **Hysteresis on action bands.** An action changes only when the score crosses a band edge by more than a buffer; inside the buffer the *previous* action stands. Entry/trim edges: 30.0, 50.0, 70.0, 80.0, 90.0. Hard triggers (Rule 9 fundamental events, Phase 06 exits, the 2x price milestone re-score) bypass it. Needs the prior state: read it from the last `watchlist/` entry (or the P-010 snapshot store when built). | [strategy.md](../../framework/strategy.md) Phase 03/05 tables, `order_setup.py` | buffer 2.0 points † |
| B6 | **Cycle-peak and multiple-ceiling guards become scored limits.** When `CYCLE_PEAK_CANDIDATE` is raised, `PEG_Score` cannot be better than 25.0 (≈ PEG 1.0) †; when `MULTIPLE_CEILING` is raised, the action band cannot be better than "Watchlist only" †. | valuation-scoring.md, `valuation_score.py` | 25.0 †, band cap † |

## Pilot (before any bump)

1. **Sample:** every current holding in [holdings.md](../../portfolio/holdings.md) plus the watchlist names with a current score — at least the 14-ticker set in [05-validation.md](05-validation.md) §2.
2. **Method:** recompute each score under the current methodology and under B1–B6 using the same live inputs (`fetch_fundamentals`, the new SBC/advisory block). Record before/after for Quality, Valuation, Composite, action band. No new network data sources.
3. **Report:** table of movers (≥ 5 points, any band change, any gate change), and a replay of the last 2–3 rescores of each holding to count how many action flips B5 would have suppressed.
4. **Acceptance (proposed):** B1 shows a material, explainable shift on SBC-heavy names (e.g. DUOL, ZS, RBRK, NOW, ADBE, VEEV) and none on Owner Earnings names; B3 does not systematically move every software name up or every non-software name down without a business reason; B5 suppresses ≥ 50% of back-and-forth flips on the replay with zero missed hard triggers; nobody is newly admitted past the 80.0 gate by B3/B4 purely through a methodology change.
5. **Rollback:** every parameter is a single constant; B1 behind `sbc_adjust`, B5 buffer `0.0` restores today's behaviour.

## Then, as one change

One decision record, one methodology-version bump in [valuation-scoring.md](../../framework/valuation-scoring.md) and [quality-scoring.md](../../framework/quality-scoring.md), one `python -m scripts.stale_score` run ([watchlist/README.md](../../watchlist/README.md#stale-scores--when-the-scoring-methodology-changes)), an [investor-philosophy-alignment.md](../../framework/investor-philosophy-alignment.md) check for each item (B5 touches the turnover test favourably; B1/B3 re-weight what "quality" means — record any divergence), and a fresh pass over the test suite.

## Still needs the user

- Accept that SBC-heavy holdings will score worse and may change band (open question #6 in [open-questions-for-user.md](open-questions-for-user.md)).
- Confirm the hysteresis buffer width and that Rule 9 triggers bypass it.
- Decide whether B3 replaces gross margin outright or blends it.
- (Not in this plan) canonical Phase 01 thresholds (P-013(c)) and the PEG-denominator ruling (P-013(a)) remain open from the earlier review.

## Glossary

From [framework/glossary.md](../../framework/glossary.md): **Quality Score**, **Valuation Score**, **Composite Score**, **Hard disqualifier**, **SBC (Stock-Based Compensation)**, **FCF yield**, **Owner Earnings**, **PEG ratio**, **Hysteresis**, **Cycle peak**, **Advisory flag**, **Multiple ceiling (advisory flag)**, **Turnover (portfolio turnover)**.

New terms: **Pilot** — a trial run of a rule change on existing holdings, comparing before and after, before the change is adopted; **Dead-band / buffer** — the margin around a threshold used by hysteresis; **Placeholder (†)** — a number chosen or copied but not yet tested on this repo's data.

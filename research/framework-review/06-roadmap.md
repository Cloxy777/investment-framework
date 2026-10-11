# Part 6 — Ranked roadmap, sequencing, and draft decision-log entries

Nothing here is applied. Priorities follow the brief: **P0** = fixes a demonstrated blind spot cheaply; **P1** = clear value; **P2** = nice to have; **P3** = rejected / parked. Effort is in **engineer-days** for one person with the repo context (scripts + tests + docs), excluding user decision time. Proposal detail: [03-proposals.md](03-proposals.md); designs: [04-design.md](04-design.md); acceptance and rollback: [05-validation.md](05-validation.md) §3.

## 1. Ranked roadmap

| Rank | ID | Title | Prio | Effort (days) | Depends on | Version bump | User decision needed |
|---|---|---|---|---|---|---|---|
| 1 | P-013 | Spec fixes (PEG denominator; PE-band fill; Phase 01 threshold drift) | **P0** | 0.5–1 | — | (b) only | canonical Phase 01 numbers (c) |
| 2 | P-003 | Pre-registered kill-lines + post-earnings check | **P0** | 1 | — | No | no |
| 3 | P-002 | Cycle-peak flag | **P0** | 0.5 | — | No | no |
| 4 | P-007 A | SBC disclosure block | **P0** | 0.5 | — | No | no |
| 5 | P-020 | Governance kit (template, ledger, test vectors) | P1 | 0.5 | — | No | no |
| 6 | P-008 | `/flags` numeric checklist | P1 | 2 | P-002 (shared helper), P-007 A | No | thresholds marked † |
| 7 | P-010 | Score snapshot store + `/what-changed` | P1 | 2 | — | No | no |
| 8 | P-011 | Portfolio-weighted metrics with coverage | P1 | 0.5 | P-010 (or `holdings.md` parse) | No | no |
| 9 | P-001 | x2 arithmetic + buy-price curve | P1 | 1.5 | consensus data source | No | **consensus data source** |
| 10 | P-016 | Next-band solver | P1 | 1.5 | P-010 (raw inputs) | No | no |
| 11 | P-009 | Three-state gate (hysteresis) | P1 | 1 | P-010 (prior state) | **Yes** | **80.0 strictness** |
| 12 | P-006 | Competence-circle registry | P1 | 1 (+ user list) | user's list | No | **the list** |
| 13 | P-007 B | SBC-adjusted FCF yield (scored) | P1 | 1.5 | P-007 A pilot | **Yes** | accept score shifts |
| 14 | P-019 | Precheck of missing inputs | P2 | 0.5 | — | No | no |
| 15 | P-004 | Forward-growth divergence flag | P2 | 1 | consensus source | No (flag) | consensus source |
| 16 | P-005 | Lynch category tag | P2 | 0.5 | — | No | no |
| 17 | P-015 | Window-defined price moves and drawdown re-score triggers | P2 | 0.5 | — | No | −30%/−50% lines |
| 18 | P-012 | Cluster report in `/rebalance` | P2 | 0.5 | cluster tags | No | 30% acknowledgement threshold |
| 19 | P-017 | `/compare` | P2 | 0.5 | P-010 | No | no |
| 20 | P-018 | Tax-normalised EPS helper | P2 | 2 | SEC XBRL feed | No | add SEC data source |
| 21 | P-014 | Print vs-index multiple | P3 | 0.25 | — | No | no |
| — | R-01…R-14 | Rejected/parked ideas | P3 | — | — | — | see 03-proposals.md section R |

Total for everything except P3: about 19 engineer-days; P0 + P-020: about 3 days.

## 2. Sequencing and dependencies

```
Wave 0 (days 1–4, docs and flags, no scoring change, no version bump)
  P-013(a)(c) → P-020 → P-003 → P-002 → P-007 A
Wave 1 (weeks 2–3, plumbing)
  P-010 (snapshot store; seed from watchlist) → P-011 → P-008 (uses P-002, P-007 A helpers) → P-019
Wave 2 (weeks 4–6, needs user decisions)
  [user: consensus source] → P-001 → P-016 (needs P-010 raw inputs)
  [user: 80.0 strictness] + P-010 (prior state) → P-009
  [user: registry list] → P-006
Wave 3 (after Wave 0–2 have produced data)
  P-007 A results → decide P-007 B      P-004, P-005, P-012, P-015, P-017, P-018 as capacity allows
Single methodology-version event (recommended): bundle P-013(b), P-009 and, if adopted, P-007 B into ONE bump and ONE stale-score run, after the pilot in 05-validation §2.4 has been run.
```

Key dependencies: **snapshot store before hysteresis** (P-010 → P-009: the gate needs a reliable prior state; minimal stop-gap = read the last watchlist row by hand); **consensus source before x2** (P-001, P-004); **SBC measurement before scoring SBC** (P-007 A → B); **user's registry before Gate 0** (P-006); **cycle flag and SBC helper before `/flags`** (shared `flags_common.py`).

Why bundle the bump: each bump triggers the stale mechanism (`CLAUDE.md`, `watchlist/README.md:40-48`); three separate bumps would stale-flag overlapping entries three times. The affected set is small: P-009 changes eligibility only for scores in [78.0, 80.0) (MSFT today, `portfolio/holdings.md:63`); P-013(b) only for names whose recorded forward-PE deviation falls in ±10–20% in range mode; P-007 B only for non-Owner-Earnings names with material SBC.

## 3. Biggest risks and mitigations

| Risk | Mitigation |
|---|---|
| Over-fitting to the Matrix's 2026 regime constants | Use no Matrix constant as a default (R-07); each placeholder is labelled and calibrated on this repo's own history before adoption |
| Building on unresolved Matrix inconsistencies | No proposal depends on the Low-confidence blocks (Capital & SBC, STRONG BUY conditions, flag thresholds); see `01-verification.md` §4 |
| Double counting (SBC in yield and in shareholder yield; flags and sub-scores) | Explicit guards in the designs (`buyback_yield_basis`, `scored_in` column, no flag penalties) |
| Loosening the strict gate by stealth | P-009 is a separate, user-approved, versioned change with a one-constant rollback |
| Consensus data quality on free tier | Refuse below 3 analysts; no substitution; manual fallback already exists |
| Process bloat (more files, more routines) | Kill-lines generated automatically; one snapshot file per week; no new routine unless consensus snapshots are adopted |
| Price-action creep | Only re-score triggers (P-015), never order triggers; Rule 0 and "documented triggers" unchanged |
| Copying a third party's methodology into the repo | Ideas are re-derived and re-specified here; ask the user about attribution and the site's terms (open-questions-for-user.md) |

## 4. Draft decision-log entries (text only — not written to `decisions/`)

Format follows existing records (e.g. `decisions/2026-06-20-framework-clarification-peg-clean-earnings.md`, `decisions/2026-06-29-framework-change-quality-score-and-composite.md`). Dates are placeholders (`YYYY-MM-DD` = the day the user approves).

### Draft A — `decisions/YYYY-MM-DD-framework-clarification-spec-fixes-peg-denominator-pe-band.md` (P-013)

```
# YYYY-MM-DD — Framework clarification: PEG denominator, Historical-PE 10–20% band, Phase 01 threshold drift

**What prompted it:**
A comparison review against an external reference system (research/framework-review/) found three defects in the written rules: (1) valuation-scoring.md never says which EPS growth divides the forward PE in PEG (DUOL was scored two ways, 2026-06-12 vs 2026-06-20); (2) strategy.md Upgrade 2 defines the Historical-PE modifier only for >20% below, within ±10%, >20% above, and scripts/scoring/valuation_score.py refuses (MissingInputError) in the 10–20% bands; (3) Phase 01 numeric thresholds differ across strategy.md, valuation-scoring.md and operating-calendar.md (net margin 15% vs 12%; revenue CAGR 10% vs 8%; net debt/EBITDA 2x vs 2.5x).

**The ruling:**
1. PEG growth G = 100 × (sqrt((1+g_ntm)(1+g_next)) − 1) using consensus EPS growth for the next 12 months and the following 12 months on a clean earnings base; a single step if only one exists; PEG remains Fast-Grower-only.
2. Between 10% and 20% deviation from the 5-year average PE the modifier is linear: −10×(|dev|−10)/10 below, +10×(dev−10)/10 above, with the Structural Quality Override applying to any positive value.
3. quality-scoring.md is the single source of numeric Phase 01 thresholds; other files link to it. [User to confirm which numbers are canonical.]

**Alignment check (investor-philosophy-alignment.md):** Lynch (PEG scope unchanged), Greenblatt (systematic, unambiguous inputs), Marks (structural override kept). Price-action, turnover, macro-veto, concentration, guidance tests: not engaged.

**Graveyard test:** neutral (no case turns on these).

**Impact:** items 1 and 3 are documentation only. Item 2 changes scores only for names in the band → bump valuation-scoring.md methodology version and run `python -m scripts.stale_score`. Acceptance: unit tests continuous at ±10 and ±20. Rollback: restore the refusal behaviour.

**Files touched:** framework/valuation-scoring.md, framework/strategy.md, framework/operating-calendar.md, scripts/scoring/valuation_score.py, scripts/tests/test_valuation_score.py.
```

### Draft B — `decisions/YYYY-MM-DD-framework-change-earnings-kill-lines.md` (P-003)

```
# YYYY-MM-DD — Framework change: pre-registered earnings kill-lines

**What prompted it:**
Rule 9 forces a re-score on every earnings release but the thresholds that would change the decision are set after the numbers are known. Evidence: RBRK and ZS re-scores 10 days overdue (holdings.md, 2026-09-27); a TRN top-up order contradicting its HOLD re-score for 16 days. The reference system generates kill-lines per report.

**The decision:**
For every holding with an earnings date within 7 days, generate portfolio/kill-lines/<TICKER>.md with lines K1–K7 built only from thresholds that already exist in the framework (revenue floor, gross-margin −3 pp, FCF/NI <70% for the second quarter, guidance cut, net debt/EBITDA limit, EPS-vs-revenue gap >10 pp, optional SBC/FCF >30%) plus one analyst-defined KPI line. After the report, run the check; TRIGGERED lines open the normal /rescore (≤3 business days) and, for a second consecutive guidance cut, the Phase 06 review. Lines never trade by themselves.

**Alignment check:** Klarman/Munger (inversion, downside first) pass; Buffett/Lynch (sell when the story breaks) pass; turnover test pass (triggers a re-score, not a trade); Rule 0 unchanged.

**Graveyard test:** encodes the GE, Valeant/Wirecard, IBM and Nokia fixes as checkable lines.

**Impact:** no scoring change, no methodology version bump. Acceptance: retro-fit on 5 names × 2 events with zero contradictions; overdue re-scores fall within 2 quarters. Rollback: stop generating.

**Files touched:** scripts/kill_lines.py (new), .claude/commands/kill-lines.md (new), .claude/commands/rescore.md, framework/automation-schedule.md (Routine 2), portfolio/kill-lines/_TEMPLATE.md (new), scripts/tests/test_kill_lines.py (new).
```

### Draft C — `decisions/YYYY-MM-DD-framework-change-cycle-peak-flag.md` (P-002)

```
# YYYY-MM-DD — Framework change: cycle-peak flag (trailing EPS growth > 100%)

**What prompted it:**
MU's Quality Score is held at 49.0 only because FY2023 (FCF −$6.117B) is still inside the rolling 3-year FCF window (watchlist/not-in-portfolio/MU, 2026-07-08), while the same session records TTM net margin 55.91% and ROE proxy 50.11%, "both would clamp to 100". When FY2023 leaves the window the framework has no cycle awareness at all. The reference system flags this case ("possible cycle peak").

**The decision:**
Add a flag (no score effect): CYCLE_PEAK_CANDIDATE when GAAP diluted TTM EPS grew more than 100% year over year on a positive base; LOSS_TO_PROFIT_BASE when the prior base was ≤ 0. The analyst must state, in the session's Known-risks block, why the multiple is compared with a normalised base (Rule 6). fast_grower must be false unless three clean years are documented.

**Alignment check:** Marks (cycle awareness) pass; Lynch (cyclicals valued differently) pass; no price-action or macro-veto.

**Graveyard test:** none of the seven cases is a cycle-peak failure → nominate a memory/commodity peak case for the next Q1 audit (figures to be sourced then).

**Impact:** no version bump. Acceptance: all memory/semicap/commodity names in watchlist/ flagged; ≤10% false positives. Rollback: raise the threshold or drop.

**Files touched:** scripts/scoring/flags_common.py (new), scripts/fetch_fundamentals.py, .claude/commands/new-position.md, .claude/commands/rescore.md, scripts/tests/.
```

### Draft D — `decisions/YYYY-MM-DD-framework-change-sbc-disclosure.md` (P-007 A; B follows after the pilot)

```
# YYYY-MM-DD — Framework change: SBC disclosure now, SBC-adjusted FCF yield after a pilot

**What prompted it:**
FCF yield is 40% of the valuation score and uses raw FCF, which adds back stock-based compensation; Upgrade 1 Owner Earnings already bears SBC via GAAP net income but applies only to MSFT/Alphabet/Meta/Amazon. SBC-heavy holdings (DUOL 8.88% of the book, ZS, RBRK, NOW, ADBE, VEEV) use raw FCF; DUOL's SBC dilution was inserted ad hoc into shareholder yield (2026-06-20 session).

**The decision:**
Phase A (now): every /new-position and /rescore inputs block prints SBC TTM, SBC/FCF and FCF yield after SBC beside the reported yield. No score change. Phase B (only after the pilot on 8 names shows ≥3 names moving ≥5 points and a reviewed action change): FCF_Score uses the after-SBC yield for non-Owner-Earnings names, and shareholder yield uses gross cash buybacks to avoid double counting.

**Alignment check:** Buffett (SBC is a real cost; consistent with Upgrade 1), Greenblatt (EBIT after SBC), Munger. Guidance test unaffected.

**Graveyard test:** none of the seven cases is SBC-driven; evidence is the live holdings.

**Impact:** A: none. B: methodology version bump + stale run + decision record. Rollback: `--sbc-adjust` off.

**Files touched (A):** scripts/scoring/sbc.py (new), scripts/fetch_fundamentals.py, .claude/commands/new-position.md, .claude/commands/rescore.md.
```

### Draft E — `decisions/YYYY-MM-DD-framework-change-x2-arithmetic-cross-check.md` (P-001)

```
# YYYY-MM-DD — Framework change: 5-year consensus-path return (x2 arithmetic) as a cross-check

**What prompted it:**
The expected annual return E behind the Upside/Downside Modifier depends on hand-set bull/base/bear fair values ("the most discretionary input in the score"), nothing mechanical checks it, and repeated R/R failures (NVDA 1.73:1→2.11:1, AVGO 1.71:1, MSFT 1.33:1) have no answer to "at what price does this name earn its hurdle?". The reference system projects EPS × multiple over five years with pessimistic/base/optimistic cases.

**The decision:**
Add scripts/scoring/x2_arithmetic.py and /x2. Base = consensus growth for two steps then ×0.95 decay; multiple = min(current, own average) in one declared basis; pessimistic uses the 5-year low multiple and halved growth and is not computed if no low is known; optimistic keeps the current multiple. Print CAGR per scenario, doubling year, the buy-price curve for 10% (repo hurdle) and 15%, and the difference vs E. It never enters the score.

**Alignment check:** Buffett/Munger/Lynch/Marks pass; Greenblatt partial (consensus unaudited) — recorded as the same conscious divergence as the Upside/Downside Modifier, mitigated by not scoring it.

**Graveyard test:** Cisco 2000 (multiple compression shows up as a negative base CAGR); not a fraud detector.

**Impact:** no version bump. Acceptance: ABNB fixture reproduced (base 14.43%, ±0.05); on 8 overlap names ≥6 within 2 pp of the reference CAGR. Rollback: remove step from /new-position if consensus is missing on >30% of runs for 3 months.

**Files touched:** scripts/scoring/x2_arithmetic.py (new), .claude/commands/x2.md (new), .claude/commands/new-position.md, scripts/scoring/order_setup.py (echo only), tests.
```

### Draft F — `decisions/YYYY-MM-DD-framework-change-three-state-quality-gate.md` (P-009; only after the user decides)

```
# YYYY-MM-DD — Framework change: three-state Quality gate (PASS / AMBER / FAIL)

**What prompted it:**
The strict 80.0 gate flips on tiny changes: MSFT 79.9 ("fails by 0.1", 14.24% of the book), ABNB 80.5 ("sensitive to two judgment calls"), ADSK 84.9 vs 79.9 under a conservative reading. A held name switching between "Composite adopted" and "reference only" is turnover by noise.

**The decision:**
A name that was PASS keeps AMBER between 78.0 and 79.9: Composite adopted for hold/trim decisions, no adds. New candidates need ≥80.0. Hard disqualifiers always FAIL. The 2.0-point band is a placeholder (the reference system's level hysteresis), calibrated on the watchlist history before adoption.

**Alignment check:** Munger/Buffett (fewer, better decisions), turnover test pass; this loosens a gate the user set "strict on purpose" (2026-06-29) → explicit user approval required.

**Graveyard test:** hard disqualifiers untouched; AMBER expires at 78.0.

**Impact:** methodology version bump (quality-scoring.md, valuation-scoring.md) + stale run for scores in [78.0, 80.0) with a prior PASS. Acceptance: ≥50% fewer PASS↔FAIL flips on replay; zero adds in AMBER. Rollback: set the band to 0.0.

**Files touched:** scripts/scoring/quality_score.py, composite_score.py, framework/quality-scoring.md, portfolio/holdings.md (Gate column), tests.
```

## 5. What not to do (short list)

Copy the Matrix's Capital & SBC table, its 15%/14% bars, 4% "good yield", index P/E constants, mega-cap tweak, reader position ranges or "reviewed by" tags; extend PEG beyond Fast Growers; score guidance; add scored red-flag penalties; replace the continuous composite by a discrete verdict map; import any rule whose confidence is Low in `01-verification.md` §4.

## Glossary

From [framework/glossary.md](../../framework/glossary.md): **Rule 9**, **Composite Score**, **Quality Score**, **Valuation Score**, **Hard disqualifier**, **FCF yield**, **Owner Earnings**, **SBC (Stock-Based Compensation)**, **PEG ratio**, **Fast Grower**, **Forward PE**, **Hurdle rate**, **CAGR**, **Net Debt/EBITDA**, **FCF/NI conversion ratio**, **Diluted EPS**, **Turnover (portfolio turnover)**.

New terms (not yet in glossary.md — proposed definitions):
- **Stale-score run** — the repo's procedure that flags every watchlist entry whose score was computed under an older methodology version until it is rescored.
- **Methodology version bump** — changing the dated version stamp because the score maths changed, which triggers the stale-score run.
- **Wave** — a group of changes done together in one period because they depend on each other.
- **Kill-line, three-state gate (PASS / AMBER / FAIL), cycle-peak flag, x2 arithmetic** — see [04-design.md](04-design.md) glossary.
- **Engineer-day** — one person-day of focused work, used only for rough effort sizing.

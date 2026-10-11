# Part 3 — Proposals (numbered P-001 …)

**Proposals only.** Nothing here has been applied. Everything is tagged **[F]** fact / **[I]** inference / **[O]** opinion where the difference matters. Priority key: **P0** = fixes a demonstrated blind spot cheaply; **P1** = clear value; **P2** = nice to have; **P3** = parked or rejected. Cross-references: gap rows in [02-gap-analysis.md](02-gap-analysis.md); verification IDs (V…, C…, E…) in [01-verification.md](01-verification.md); designs for the top items in [04-design.md](04-design.md).

Ground rules applied to every proposal (from the brief and `CLAUDE.md`): never invent or estimate financial data (missing ⇒ stop and ask); Rule 0 (live price first, `framework/fair-value-methodology.md:13-30`); act only on documented triggers; show every calculation; **one fact, one penalty** (avoid double counting); import mechanics, not authority; check against `framework/investor-philosophy-alignment.md:44-51` (six tests) and `framework/graveyard-audit.md`.

**Parameter honesty.** Any number below marked *(placeholder)* is a starting value that I chose or copied from the Matrix's printed constants; it has **not** been validated on this repo's data and must be calibrated in the pilot named in the same proposal. Matrix constants that belong to the 2026 regime (4% "good yield", index P/E 20.1, pessimistic multiple 16, mega-cap tweak) are never used as defaults.

## Summary table

| ID | Title | Type | Priority | Effort | Bumps methodology version? |
|---|---|---|---|---|---|
| P-001 | 5-year x2 arithmetic (base/pessimistic/optimistic) + buy-price-for-target-return curve | factor / command | P1 | M | No |
| P-002 | Cycle-peak detector (trailing EPS growth > 100%) | factor (flag) | **P0** | S | No |
| P-003 | Pre-registered earnings kill-lines + post-earnings check | gate-stage / command | **P0** | S | No |
| P-004 | Forward-growth divergence flag (consensus vs trailing) | factor (flag) | P2 | S–M | No (flag); Yes if later scored |
| P-005 | Lynch-category tag as an input field | data | P2 | S | No |
| P-006 | Competence-circle registry (Gate 0) | gate-stage | P1 (needs user decision) | M | No |
| P-007 | SBC disclosure (A) and SBC-adjusted FCF yield (B) | factor | **P0** (A) / P1 (B) | S / M | A: No · B: **Yes** |
| P-008 | `/flags` numeric red-flag checklist | command | P1 | M | No |
| P-009 | Three-state quality gate with hysteresis | gate-stage | P1 (needs user decision) | S–M | **Yes** (eligibility rule) |
| P-010 | Score snapshot store + `/what-changed` | data / reporting | P1 | M | No |
| P-011 | Portfolio-weighted metrics with coverage disclosure | reporting | P1 | S | No |
| P-012 | Cluster (sub-sector) concentration report in `/rebalance` | reporting / governance | P2 | S | No |
| P-013 | Valuation spec fixes: PEG denominator, 10–20% PE-band gap, Phase 01 threshold drift | governance | **P0** | S | Yes for the PE-band fill only |
| P-014 | Print vs-index multiple reference (unscored) | reporting | P3 | S | No |
| P-015 | Drawdown and window-defined price moves as re-score triggers | gate-stage | P2 | S | No |
| P-016 | "What must change" next-band solver | command | P1 | M | No |
| P-017 | `/compare` over stored scores | command / reporting | P2 | S | No |
| P-018 | Tax-normalised EPS helper | factor / data | P2 | M | No (input hygiene) |
| P-019 | Collect-all precheck of missing inputs | command / quality | P2 | S | No |
| P-020 | Governance kit: framework-change decision template, version ledger, external test vectors | governance | P1 | S | No |

Rejected ideas: section **R** at the end.

---

## P-001 — Five-year x2 arithmetic with pessimistic / base / optimistic and a buy-price-for-target-return curve

| Field | Content |
|---|---|
| **Title** | x2 arithmetic (`scripts/scoring/x2_arithmetic.py`) |
| **Type** | factor (cross-check, not scored) + command (`/x2`) + order-setup field |
| **Problem and failing case** | The repo's expected annual return `E` (annualised gap to a probability-weighted fair value + intrinsic growth + shareholder yield, `valuation-scoring.md:119-126`) is built from hand-set bull/base/bear fair values — "the most discretionary input in the score" (`valuation-scoring.md:150`) — and nothing mechanical checks it. Concrete: ASML's Valuation Score is 94.6 (Composite 56.1) on 2026-09-11 (`watchlist/not-in-portfolio/ASML/ASML-2026-09-11.md`) while the Matrix's consensus-path base CAGR for the same name is 13.5% (`RS:177`); no repo artefact says how much of that gap is multiple vs forecast. Second: the repo repeatedly fails R/R (NVDA 1.73:1 → 2.11:1, AVGO best case 1.71:1, MSFT 1.33:1 — `watchlist/in-portfolio/NVDA/NVDA-2026-09-17.md`, `…/AVGO-2026-09-28.md`, `…/MSFT-2026-07-30.md`) and has no tool that answers "at what price does this name earn my hurdle?". |
| **Exact rule** | Inputs: `price0` (Rule 0), `basis` ∈ {`ntm`, `ttm`}, `eps0` (NTM EPS if basis=ntm; TTM EPS if basis=ttm; must be > 0), `g1, g2` = consensus growth steps (decimals; for basis=ttm `g1 = NTM/TTM − 1`), `m_now` (multiple in the same basis), optional `m_avg` (3–5-yr average multiple **same basis**), optional `m_low` (5-yr low, same basis), parameters `decay = 0.95` *(placeholder: observed constant ratio in the Matrix, `01-verification.md` V2)*, `haircut = 0.5` *(placeholder: Matrix pessimistic factor, V4)*, `n = 5`.<br>Growth path: `g_i = g_{i-1} × decay` for `i = 3..n` if `g_{i-1} > 0`, else `g_i = g_{i-1}` (no "decay" of declines); validate `0.75 ≤ decay ≤ 1.0`.<br>`eps_n = eps0 × Π_{i=1..n} (1 + g_i)`.<br>Multiples: `M_base = min(m_now, m_avg)` if `m_avg` given, else `m_now` (flag `NO_HISTORY`); `M_opt = m_now`; `M_pess = m_low` if given, else scenario not computed (never a default number).<br>Pessimistic growth: `g1' = haircut × g1`, `g2' = haircut × g2` (only if positive), then the same decay.<br>`price_n = eps_n × M`; `CAGR = (price_n / price0)^(1/n) − 1`.<br>Doubling year: interpolate linearly on the yearly path `price_t = eps_t × M` (`t = 0..n`) for the first crossing of `2 × price0` (reproduces the Matrix's "3.9" on ABNB, V7).<br>**Buy-price curve**: `BuyPrice(target) = price_n_base / (1 + target)^n` for `target ∈ {hurdle 10%, 15%}` (10% = the repo's hurdle `H`, `valuation-scoring.md:130`); report `BuyPrice / price0 − 1`.<br>Cross-check: `delta_pp = E − 100×CAGR_base`; print, and flag `E_VS_CONSENSUS` if `|delta_pp| > 10` *(placeholder, calibrate in the pilot)*. |
| **Inputs / source / data risk** | `eps0`, `m_now`: yfinance (TTM) or IBKR/consensus (NTM). `g1, g2`: consensus — **not reliably available on the free tier** [I: yfinance exposes `earnings_estimate`/`growth_estimates`; not verified in this session — verify at pilot start]; fallback = manual paste from TIKR/Koyfin (already in use, `screen.md:13`). `m_avg`/`m_low`: `fetch_fundamentals.py` gives 5-yr TTM P/E avg/low/high (basis `ttm`). Risk: mixing bases — the script refuses (one `basis` field for all multiples). Negative or zero `eps0` ⇒ exit 3 "not computable" (never fabricated). |
| **Philosophy check** | Buffett — pass (owner-style forward earnings power, no reliance on a target price). Munger — pass (inversion via pessimistic case). Lynch — pass (growth × multiple, "know the story"). Greenblatt — **partial**: consensus is an unaudited input (same tension as the Upside/Downside Modifier, recorded as a conscious divergence at `investor-philosophy-alignment.md:53`); mitigated because P-001 is a cross-check and never a score input. Marks — pass (second-level: compare our view to consensus). |
| **Graveyard test** | Cisco 2000 (`graveyard-audit.md:49-61`): 130× forward earnings — base CAGR with `M_base = min(m_now, m_avg)` collapses to a multiple-compression loss, matching the case's failure (valuation, not the business). Peloton/COVID-inflated TAM: pessimistic haircut on consensus steps highlights fragility. Would **not** have caught Valeant/Wirecard (fraud) — honest limit. |
| **Interaction** | No score change ⇒ no double counting. Reads the same fair-value inputs as `E` but from a different source (consensus path), so a large `delta_pp` is *information*. Rule 0: `price0` must be live. "Act only on documented triggers": output is advisory; order setup still governed by score band and Steps 2–6. |
| **Scoring-version impact** | None (not in the score). If later promoted into `E`, that would be a separate proposal and a bump. |
| **Implementation sketch** | New `scripts/scoring/x2_arithmetic.py` (same CLI/JSON conventions as `quality_score.py`); new `.claude/commands/x2.md`; optional `x2_buy_price_at_hurdle` echoed in `order_setup.py` output; tests `scripts/tests/test_x2_arithmetic.py` (see 04-design.md, incl. ABNB and NVDA vectors, negative EPS, missing consensus, recent IPO, fiscal-year change, non-USD). |
| **Validation plan** | Pilot on the 8 overlapping names in `05-validation.md`: compare `CAGR_base` with `E` and with the Matrix's published base CAGR; success = |ours − Matrix| ≤ 2 pp on ≥ 6 of 8 (differences explainable by data source). Then check whether `E_VS_CONSENSUS` fires on names whose fair values were the most contested in past sessions. |
| **Effort / risk** | **M** (~1 day script + tests; consensus data plumbing is the unknown). Risk: consensus drift on thin-coverage names → mitigate with `n_analysts` field and refusal below 3 analysts *(placeholder)*. |
| **Priority** | **P1** — high leverage on the recurring "what price?" question; not P0 because it needs a consensus source. |

## P-002 — Cycle-peak detector

| Field | Content |
|---|---|
| **Title** | `CYCLE_PEAK_CANDIDATE` flag |
| **Type** | factor (flag only) |
| **Problem and failing case** | Trailing-earnings multiples look cheapest exactly at a cycle top. The repo's protections are indirect: PEG restricted to clean Fast Growers (`valuation-scoring.md:105`), FCF-positive 3-year disqualifier, and the "cyclical near trough" margin of safety (`fair-value-methodology.md:255`). The 2026-08-05 SNDK case shows the disqualifier was applied to a memory name whose windows swung sign (`quality-scoring.md:26`). The Matrix and this repo diverge on the same class: MU is "cheap, NTM P/E 6.7, PEG 0.07" for the Matrix (`RS:172`) versus "Quality 49.0 — Gate FAIL" here, because the hard disqualifier "not FCF-positive for 3+ consecutive years" still sees FY2023 (FCF −$6.117B) in its window; the same session records TTM net margin 55.91% and an ROE proxy of 50.11%, "both would clamp to 100" (`watchlist/not-in-portfolio/MU/MU-2026-07-29.md`, 2026-07-08 row). **Demonstrated blind spot (inferred from the rolling-window rule, `quality-scoring.md:26`)**: once FY2023 leaves the 3-year window, the only thing standing between MU and a high Profitability score is nothing — peak-cycle margins will clamp to 100 and the FCF disqualifier will stop firing, exactly at the cycle top. The repo is protected today by a trough year, not by any cycle awareness. |
| **Exact rule** | `g_ttm = (EPS_ttm_now / EPS_ttm_1y_ago − 1) × 100` with both EPS **GAAP diluted, positive**. If `EPS_ttm_1y_ago > 0` and `g_ttm > 100` ⇒ flag `CYCLE_PEAK_CANDIDATE`. If `EPS_ttm_1y_ago ≤ 0 < EPS_ttm_now` ⇒ flag `LOSS_TO_PROFIT_BASE` (already a PEG ineligibility, `valuation-scoring.md:105`). Consequences (documentation only): (1) "Known risks" line in the session log; (2) `fast_grower` must be `false` unless 3 clean prior years are documented; (3) if the Lynch category is Cyclical (P-005) the fair-value margin of safety uses the cyclical row (35%, `fair-value-methodology.md:255`). |
| **Inputs / source** | `fetch_fundamentals.py`: `Diluted EPS` from `t.financials` / `t.quarterly_financials` (4–5 quarters on free tier ⇒ TTM now and TTM a year ago need 8 quarters — [I] may need SEC XBRL; if unavailable the flag is `UNKNOWN`, not silently false). Threshold 100% is the Matrix's printed cycle-peak trigger (`RM:65`) *(placeholder for this repo)*. |
| **Philosophy check** | Marks (cycle awareness, `investor-philosophy-alignment.md:41`) — pass; Lynch (cyclicals valued differently) — pass; Buffett — neutral; Munger/Greenblatt — pass (rule-based). No price-action or macro-veto. |
| **Graveyard test** | None of the seven cases is a cycle-peak failure ⇒ this fills a **hole in the audit**, not a hole caught by it. Action: nominate a memory/commodity peak case for the next Q1 review (`graveyard-audit.md:125-136`); figures to be sourced then, not now. |
| **Interaction** | No score effect ⇒ no double counting with the Historical-PE modifier. Explicit guard: flag does not veto — it forces the analyst to write why the multiple compares against a normalised base (Rule 6, `fair-value-methodology.md:228-235`). |
| **Version impact** | None. (A stronger version — ignoring the −10 "cheap vs history" credit for flagged names — would bump the version; deferred until the pilot shows a real miss.) |
| **Implementation** | Add `cycle_peak(eps_now, eps_prev)` to a new `scripts/scoring/flags_common.py` (shared with P-008); fields `eps_ttm_now`, `eps_ttm_1y_ago` added to `fetch_fundamentals.py` output; printed in `/new-position` and `/rescore` inputs. Tests: positive/negative base, exactly 100%, missing quarter ⇒ `UNKNOWN`. |
| **Validation** | Run over the 30+ names in `watchlist/`; report the count flagged and manually check each against known cyclical status; success = every memory/semicap/commodity name in the set flagged, no more than 10% false positives among non-cyclicals. |
| **Effort / risk** | **S**. Risk: high-growth non-cyclicals (e.g. NVDA, +109% per the Matrix) are flagged — acceptable: the flag means "look harder", not "reject". |
| **Priority** | **P0** — a demonstrated (MU) blind spot that a one-line, no-penalty flag closes. |

## P-003 — Pre-registered earnings kill-lines and a post-earnings check

| Field | Content |
|---|---|
| **Title** | `/kill-lines <ticker>` (pre-earnings) and a "kill-line table" step at the top of `/rescore` (post-earnings) |
| **Type** | gate-stage + command |
| **Problem and failing case** | Rule 9 makes earnings a mandatory re-score trigger (`fair-value-methodology.md:258-266`; `operating-calendar.md:52-62`) but the *thresholds that would change the decision* are decided after the number is known. Evidence of decision latency and contradictions [I]: RBRK and ZS re-scores 10 days overdue (`portfolio/holdings.md:21-23`); a TRN top-up order that contradicted the HOLD re-score for 16 days (`holdings.md:25-27`); five undocumented open orders (`holdings.md:29`). The Matrix generates per-company kill-lines for every report (`RS:119`, `screens/reports.md`). |
| **Exact rule** | For each held name, before its report date, write a small file (`portfolio/kill-lines/<TICKER>.md`) listing lines with **operator, threshold, source field, action**. Default lines re-use thresholds that already exist in the repo — no new numbers: <br>K1 revenue growth YoY below the Phase 01 floor (`strategy.md:16`, but see P-013 on the 10% vs 8% drift); <br>K2 gross margin down > 3 pp vs prior-year quarter (`strategy.md:85`, `fair-value-methodology.md:92`); <br>K3 FCF/NI < 70% for the **second** consecutive quarter (`strategy.md:86`); <br>K4 guidance cut (revenue or margin) — 2nd consecutive cut without a one-off cause ⇒ Phase 06 exit review (`strategy.md:90,111`); <br>K5 Net Debt/EBITDA above the applicable hard limit (2.5×; 4× asset-light) (`quality-scoring.md:21`); <br>K6 EPS growth − revenue growth > 10 pp for the second consecutive year (`strategy.md:89`); <br>K7 *(optional, from P-007)* SBC/FCF > 30% *(Matrix's printed kill-line, `RS:155`; placeholder)*; <br>K8 one **ticker-specific KPI** line chosen by the analyst (e.g. a volume KPI whose second consecutive decline matters). <br>Post-earnings: `check` evaluates every line as TRIGGERED / OK / UNKNOWN and pre-fills the re-score's "Fundamental changes since last review" block. A TRIGGERED line never trades by itself: it forces a `/rescore` within the existing 3-business-day window (`operating-calendar.md:31`) and, for K4 second-cut, opens the Phase 06 review. |
| **Inputs / source** | Prior-period values from the latest `fetch_fundamentals` output and the watchlist entry; earnings date from yfinance `get_earnings_dates` (already used, `valuation-scoring.md:273-293`) or IBKR; K4/K8 are manual tri-state (yes/no/unknown). Data risk: low (all lines reuse existing inputs). |
| **Philosophy check** | Klarman (downside first) and Munger (inversion — "what would make this fail?") — pass; Buffett/Lynch (sell when the story breaks, not on price) — pass since every line is fundamental; Turnover test — pass (triggers a re-score, not a trade). It *is* a "documented trigger" in the sense of `CLAUDE.md`. |
| **Graveyard test** | Encodes four existing fixes as machine-checkable lines: GE (K5), Valeant/Wirecard (K3), IBM (K6 + revenue K1), Nokia (K1). Would have produced an automatic flag one to two quarters earlier for IBM (`graveyard-audit.md:116-121`) than a manual narrative check [I]. |
| **Interaction** | Same thresholds as Phase 04 — **no** new penalty, no double counting. Complements Routine 2's 7-day look-ahead (`automation-schedule.md:145`) and Routine 1's `rescore-due` issue (`operating-calendar.md:11`): generation attaches to the look-ahead, checking to the existing issue. Rule 0 unchanged (post-earnings numbers are fetched, not typed). |
| **Version impact** | None. |
| **Implementation** | New `scripts/kill_lines.py` (`generate`, `check`), `.claude/commands/kill-lines.md`, one paragraph added to Routine 2's prompt and to `rescore.md` step 2; tests `scripts/tests/test_kill_lines.py`; template file `portfolio/kill-lines/_TEMPLATE.md`. |
| **Validation** | Retro-fit K1–K6 to the last two completed re-scores of five held names (NVDA 09-17, AVGO 09-28, META 08-26, V 07-29, DUOL 09-01): for each, would a line have fired, and did the human decision agree? Acceptance: zero contradictions; every re-score decision is explained by at least one line or by "no line fired". |
| **Effort / risk** | **S**. Risk: paperwork inflation for 20+ holdings ⇒ generate automatically, hand-edit only K8. |
| **Priority** | **P0** — cheapest change that tightens "act only on documented triggers". |

## P-004 — Forward-growth divergence flag

| Field | Content |
|---|---|
| **Title** | `FWD_DECEL` / `FWD_NEGATIVE` flags |
| **Type** | factor (flag) |
| **Problem and failing case** | Quality "Growth" is trailing revenue 3-year CAGR (`quality-scoring.md:73-84`; `quality_score.py:130-153`). Trailing growth lags turns: IBM's CAGR turned negative only in 2013–14 (`graveyard-audit.md:116-121`); Nokia's "revenue CAGR broke below 10% by Q1 2009" (`:43-47`). Present-day example: NVDA's quality input is a 100.05% 3-year CAGR (`scripts/tests/test_quality_score.py`, NVDA vector) — the score saturates at the clamp (25%→100.0) and says nothing about what is *ahead*. |
| **Exact rule** | With `rev_ntm` = consensus next-12M revenue growth (%) and `cagr3` = trailing 3-yr CAGR (%): `FWD_NEGATIVE` if `rev_ntm < 0`; `FWD_DECEL` if `cagr3 > 0 and rev_ntm < 0.5 × cagr3 and (cagr3 − rev_ntm) > 5` *(both constants placeholders)*. No score change. |
| **Inputs / source** | Consensus revenue growth — yfinance `revenue_estimate` [I: available, not verified]; else manual. Risk: medium (thin estimates outside the US). |
| **Philosophy** | Lynch ("know the story"), Marks (second-level: is it priced?) pass; Guidance test — pass because *consensus* is not management guidance. Greenblatt — flag only, not a scored input. |
| **Graveyard** | IBM, Nokia (both). |
| **Interaction** | Overlaps the Growth ±10 deceleration modifier (`quality-scoring.md:84`) — the flag would *support* the documented-evidence requirement rather than replace it. |
| **Version impact** | None for the flag. A blended Growth input `0.5×cagr3 + 0.5×rev_ntm` would bump the version and needs the user's decision on paying for consensus. |
| **Implementation** | Add fields to `fetch_fundamentals.py`; print in inputs block. Tests as P-002. |
| **Validation** | Pilot on the 21 scored holdings: count flags; check against sessions where "Growth decelerating" was documented. |
| **Effort / risk / priority** | **S–M**; risk medium (data); **P2**. |

## P-005 — Lynch-category tag as an input field

| Field | Content |
|---|---|
| **Title** | `lynch_category` ∈ {stalwart, fast_grower, cyclical, turnaround, asset_play, slow_grower} |
| **Type** | data |
| **Problem and failing case** | DUOL was scored two different ways across two sessions because "Fast Grower" was implicit (`decisions/2026-06-20-framework-clarification-peg-clean-earnings.md`). Lynch's own rule is to categorise every holding and size/value/exit by category (`investor-philosophy-alignment.md:26`); the repo stores only a boolean. |
| **Exact rule** | Field in the input JSON of `valuation_score.py` / `quality_score.py` and the watchlist header. Validation: `fast_grower == true` ⇔ category `fast_grower` (else `MissingInputError`); category `cyclical` ⇒ P-002 mandatory and cyclical margin of safety row; category `turnaround` ⇒ Upgrade 4 checklist required (`strategy.md:185-194`). |
| **Source / risk** | Analyst-assigned with cited reasoning (same evidence rule as moat, `quality_score.py:186-187`); not automated. |
| **Philosophy / graveyard** | Lynch — pass (it is his method). Graveyard: consistent labelling would have exposed GE as a "conglomerate with captive finance" only via P-006, not here. |
| **Interaction / version** | No score change ⇒ no bump. Only a consistency gate. Replaces (does not duplicate) the Matrix's "predictability by business type" (rejected as a weight, R-03). |
| **Implementation / validation** | Schema change + 2 tests; back-fill for 30 tickers is a data-entry job during normal re-scores. |
| **Effort / priority** | **S**; **P2**. |

## P-006 — Competence-circle registry (Gate 0)

| Field | Content |
|---|---|
| **Title** | `framework/competence-circle.md` + `scripts/competence.py` |
| **Type** | gate-stage |
| **Problem and failing case** | The circle-of-competence tenet (`investor-philosophy-alignment.md:13`) has no operational form; `/screen` triage is one unlisted sentence (`screen.md:23`). Costs: `/telegram-scan` launches `/new-position` for *any* named company with no watchlist entry (`telegram-scan.md:22`), and each full `/new-position` costs about 120–160K tokens (`new-position.md:30`) — including for banks, insurers or REITs that the investor may never want to own. Governance: undocumented positions in classes the framework never evaluated (RGL "ungoverned", TLT/XEON "framework gap": `holdings.md:70,72,77`). |
| **Exact rule** | One table: `basket | state | why | exception process | repo examples`. States: **core** (analyse normally), **stop** (do not analyse for the core book; exceptions only via a `decisions/` entry with the specific reason), **unclear** (must be resolved by the user before any scoring — analogous to the Matrix's "business not understood → AVOID"). The Matrix's baskets (`RS:5-51`) are offered as a **starting template with every state blank**; nothing is pre-filled. Gate 0 result is stated as the first line of `/new-position` and `/screen` step 1, and copied to the watchlist header (`Basket:`). `/telegram-scan`: a resolved ticker whose basket is `stop` is logged "stop-list — no action" instead of triggering `/new-position`. |
| **Inputs / source** | User-owned list; no market data. |
| **Philosophy** | Buffett/Munger — pass (directly their tenet). Concentration test — neutral. Lynch — pass (know what you own). |
| **Graveyard test** | GE (captive finance ⇒ a "conglomerate with financial subsidiary" basket forces the consolidated-debt rule before scoring), Wirecard (a payments/fintech whose cash cannot be independently verified belongs in a stop/unclear state), Valeant (acquisition-led specialty pharma ⇒ stop or exception). Fully consistent with existing fixes; adds a *front-door* check. |
| **Interaction** | Precedes the Quality Score (no double counting). It is **not** a substitute for the Quality gate; it removes names before spending analysis. Interaction with the speculation sleeve: sleeve eligibility stays "Quality ≥ 80.0" (`speculation-module.md:15`); a `stop` basket does not automatically block the sleeve — that is the user's call (open question). |
| **Version impact** | None (no score change). |
| **Implementation** | New file + tiny script (`lookup --basket`), edits to `screen.md`, `new-position.md`, `telegram-scan.md` (diffs in 04-design.md not required — top-8 excludes; sketched in the command table below). Tests: unknown basket ⇒ `unclear`. |
| **Validation** | Replay `sessions/` names since June: how many `/new-position` runs would have stopped at Gate 0 and their token cost (from the per-session notes); false stops = names the user later wanted. |
| **Effort / risk / priority** | **M** (mostly the user's decisions); risk: false comfort — the registry must not become an excuse to skip judgment; **P1**, blocked on the user deciding the list. |

## P-007 — SBC: disclosure (A) and SBC-adjusted FCF yield (B)

| Field | Content |
|---|---|
| **Title** | Treat stock-based compensation as a cost in the cash yield |
| **Type** | factor |
| **Problem and failing case** | FCF yield is 40% of the valuation score (`valuation-scoring.md:30-44`) and the input is raw FCF, which adds SBC back (`framework/glossary.md:541`). Upgrade 1 owner earnings (NI + D&A − maintenance capex) already bears SBC through GAAP NI but applies only to MSFT/Alphabet/Meta/Amazon (`strategy.md:147`). SBC-heavy holdings use raw FCF: ZS (cash FCF yield 4.41% with an explicit "SBC distortion" note, `sessions/2026-06-20-rescore-zs.md:33,44`), DUOL (8.88% of the portfolio; SBC dilution of ~3.5% inserted **ad hoc** into shareholder yield, `sessions/2026-06-20-rescore-duol.md:145`), RBRK, ADBE/NOW/VEEV. The Matrix's version ("FCF yield after SBC", `RM:61`; kill-line SBC > 30% of FCF, `RS:155`) treats it systematically. |
| **Exact rule** | **Phase A (no scoring change).** Add to every inputs block: `sbc_ttm`, `sbc_pct_fcf = 100 × sbc_ttm / fcf_ttm` (if `fcf_ttm > 0`, else `n/a — FCF ≤ 0`), `fcf_after_sbc_yield_pct = 100 × (fcf_ttm − sbc_ttm) / market_cap`. Print beside the existing FCF yield.<br>**Phase B (bump).** `FCF_Score` uses `fcf_after_sbc_yield_pct` for every name **not** using Owner Earnings; for Owner-Earnings names use OE as today (already SBC-burdened via NI). To avoid double counting, when B is on, `shareholder_yield` in the Upside/Downside step uses **gross cash buyback yield**, not net-of-SBC dilution (DUOL's ad hoc −3.5% then disappears). Clamp unchanged: `clamp(100×(1 − yield/10), 0, 100)`. |
| **Inputs / source** | yfinance `t.cashflow` row "Stock Based Compensation" [I: exists for most US filers; not verified for all tickers in this session] — else SEC XBRL `ShareBasedCompensation`. Missing ⇒ `MissingInputError` in Phase B (Rule 0), `UNKNOWN` printed in Phase A. |
| **Philosophy** | Buffett (SBC is a real cost to owners — widely stated; consistent with Owner Earnings, Upgrade 1) pass; Greenblatt (EBIT after SBC) pass; Munger pass. Guidance test unaffected. |
| **Graveyard** | None of the seven cases is SBC-driven — say so plainly; evidence is the live SBC-heavy holdings above. Closest cousin: Valeant/Wirecard (non-cash items flattering cash-flow metrics). |
| **Interaction** | Ties to P-008 flag F6 (SBC/FCF > 30%) and P-003 K7; each fact is used once: Phase B moves it *into* the yield, so F6 stays a label without penalty (Matrix's "one fact, one penalty"). Interaction with the FCF/NI hard disqualifier: ZS NI is negative so the ratio is "not meaningful" (`…rescore-zs.md:44`); after-SBC FCF gives a second read on cash quality. |
| **Version impact** | A: none. **B: yes** — changes how the valuation score is computed ⇒ bump `valuation-scoring.md:5`, decision record, `python -m scripts.stale_score` run per `CLAUDE.md`. Only SBC-heavy names move; run a dry-run on all 26 in-portfolio names first. |
| **Implementation** | `fetch_fundamentals.py` (+3 fields); `valuation_score.py` (`--sbc-adjust` flag off by default until B is adopted); tests: SBC > FCF (negative after-SBC yield ⇒ `FCF_Score` = 100), SBC = 0, FCF ≤ 0. |
| **Validation** | Phase A on ZS, RBRK, DUOL, NOW, ADBE, VEEV, DOCS, UBER: table of `sbc_pct_fcf` and after-SBC yield; decide B if ≥ 3 names shift ≥ 5 score points. Rollback: flag off. |
| **Effort / risk** | A **S**, B **M**; risk: B raises scores for many software names — they look worse; could push held names into the trim band; the pilot must show the *action* changes before adoption (anti-turnover). |
| **Priority** | A **P0**, B **P1**. |

## P-008 — `/flags`: numeric red-flag checklist (no penalty)

| Field | Content |
|---|---|
| **Title** | `python -m scripts.flags --input …` |
| **Type** | command |
| **Problem and failing case** | Phase 04's checks are prose (`strategy.md:81-90`) executed by hand per rescore; nothing prints a per-ticker pass/fail/unknown table. TRN: FCF −17% YoY "flagged, not yet explained" (`holdings.md:92`) shows a flag with no owner or expiry; RBRK/ZS SBC. The Matrix prints flags with number and threshold and separates "measured below threshold" from "data gap" (`CC:112`). |
| **Exact rule** | Output columns: `flag | severity(label) | status (PASS/FAIL/UNKNOWN) | value | threshold | source | scored_in`. **Severity is a label; no point penalty** — avoids a second weighting system, and `scored_in` names the sub-score that already grades the fact (Matrix's "one fact, one penalty", `RM:52`). Numeric flags F1–F8 (automatable): F1 FCF negative TTM (critical); F2 ≥ 4 negative-FCF quarters, or TTM negative (critical); shorter with positive TTM (minor); F3 capex > operating cash flow while FCF < 0 (critical); F4 Net Debt/EBITDA > 2.5× (serious; > 4× critical) — repo's hard limit, **not** the Matrix's 1.5×/3×; F5 interest coverage EBIT/interest < 3× (serious) *(placeholder; the Matrix gives no number)*; F6 SBC/FCF > 30% (serious, from P-007); F7 dividend > 60% of FCF (serious, Matrix printed); F8 diluted share count CAGR 3y > 2% (serious) *(placeholder; repo says "no dilutive share issuance pattern", `strategy.md:17`)*. Repo-defined: F9 FCF/NI < 70% for 2+ years; F10 EPS growth − revenue growth > 10 pp 2+ years; F11 gross margin −3 pp. Manual tri-state: F12 customer concentration (≥ 25% one, ≥ 33% top-2 serious; ≥ 40% critical — Matrix printed, `RM:85`); F13 guidance cut; F14 reported-vs-adjusted EPS gap; F15 profit from revaluation of investments; F16 revenue geography ≥ 35% outside home (info only). |
| **Inputs / source** | yfinance financials/cash-flow (most), 10-K text (F12–F16 manual). |
| **Philosophy** | Munger (inversion / checklists), Klarman — pass. Guidance test: F13 is a *reading of what happened*, not a forecast input — pass. |
| **Graveyard** | GE (F4 consolidated), Valeant/Wirecard (F9, F14), IBM (F10), Nokia (via P-004). |
| **Interaction** | Reads the same inputs as the score; prints, never penalises. Hard disqualifiers remain in `quality_score.py:59-95`; `/flags` prints them as F4/F9/etc. for visibility. |
| **Version impact** | None. |
| **Implementation** | New `scripts/flags.py` + `flags_common.py`; tests per flag with boundary values; `/new-position` step 2, `/rescore` step 3 print the table; `/screen` step 2 prints the F1–F4 subset. |
| **Validation** | Run on 26 held names; compare FAIL/UNKNOWN counts to open issues in `holdings.md`; every FAIL must map to a documented note or become an issue. |
| **Effort / risk / priority** | **M**; risk: threshold placeholders (F5, F8) — kept `UNKNOWN`-tolerant; **P1**. |

## P-009 — Three-state quality gate with hysteresis

| Field | Content |
|---|---|
| **Title** | PASS / AMBER / FAIL |
| **Type** | gate-stage |
| **Problem and failing case** | The strict 80.0 gate is a knife-edge: MSFT 79.9 "fails by 0.1" on a 14.24% holding (`holdings.md:63,88`); ABNB 80.5 "sensitive to two judgment calls that could each flip it" (`watchlist/not-in-portfolio/ABNB/ABNB-2026-08-24.md`); ADSK 84.9 vs a conservative reading of 79.9 (`…/ADSK-2026-08-23.md`); GOOG 73.7→71.4 (`…/GOOG-2026-07-22.md`). A held name flipping between "Composite adopted" and "reference only" with 0.1-point changes is turnover-by-noise (Munger, `investor-philosophy-alignment.md:22`). The Matrix uses hysteresis (2 pts) and ordered caps to avoid this (`RM:46,51`). |
| **Exact rule** | `prior_state ∈ {PASS, AMBER, FAIL, NONE}` (from the last watchlist entry / snapshot). Given rounded score `s` (`round_boundary`) and hard-disqualifier result: <br>`if disqualified: FAIL`<br>`elif s ≥ 80.0: PASS`<br>`elif prior_state ∈ {PASS, AMBER} and s ≥ 78.0: AMBER` *(band 2.0 pts = Matrix's level hysteresis; calibrate in pilot)*<br>`else: FAIL`.<br>AMBER semantics: the held name keeps its Composite for **trim/hold** decisions (Phase 05) and is shown as amber; **no adds and no new entries** (adds require PASS). Candidates not yet held need PASS (no hysteresis on entry). |
| **Inputs / source** | Existing score + last state; no new data. |
| **Philosophy** | Munger/Buffett (fewer, better decisions) pass; Turnover test pass; Marks — pass (avoid false precision on a discretionary score). It *loosens* a gate the user set "strict on purpose" (`quality-scoring.md:17`) ⇒ **user decision**. |
| **Graveyard** | GE, Nokia: the disqualifiers and hard fails are untouched; AMBER never applies when a hard disqualifier fires. Slow-decay cases are caught because AMBER expires at 78.0 and the band is only entered from PASS. |
| **Interaction** | Changes an eligibility rule ⇒ **bump `valuation-scoring.md:5` and `quality-scoring.md:5`**, decision record, stale run. Only names with a score in [78.0, 80.0) and a PASS/AMBER prior are affected (MSFT today) — small stale run. Depends on P-010 for a reliable `prior_state`. |
| **Implementation** | `quality_score.py` gets `--prior-state`; `composite_score.py` gains `gate_state`; `holdings.md` column "Gate"; tests: 79.9 with prior PASS → AMBER; 79.9 with prior NONE → FAIL; 77.9 → FAIL; disqualified 85 → FAIL. |
| **Validation** | Replay the last 3 scores of all 26 held names: how many state changes with vs without hysteresis; success = ≥ 50% fewer flips with zero new "adds" allowed. Rollback: set band to 0. |
| **Effort / risk / priority** | **S–M**; risk: perceived loosening; **P1**, gated on the user's answer (open-questions). |

## P-010 — Score snapshot store and `/what-changed`

| Field | Content |
|---|---|
| **Title** | Structured history: `portfolio/snapshots/scores/YYYY-MM-DD.json` + `scripts/snapshot.py` |
| **Type** | data / reporting |
| **Problem and failing case** | History exists only as markdown prose in `watchlist/` (dated tables, `watchlist/README.md:26-34`); no machine-readable series ⇒ no hysteresis state (P-009), no drift chart, no cause-attributed change feed (Matrix `changes-week.md`), no calibration data for any placeholder in this document. |
| **Exact rule** | One JSON per weekly run (Routine 2, `automation-schedule.md:145`) and per `/rescore`/`/new-position`: `{date, methodology_version, tickers: {T: {price, quality, valuation, composite, gate_state, band, basket, lynch_category, inputs_hash, session, flags:[…]}}}`. `diff(a, b)` outputs: band changes, gate-state changes, new/removed flags, price distance to the current buy limit. **Bootstrap**: (1) seed from the last row of each `watchlist/**` entry via a regex parser that keeps only `date, price, valuation, quality, composite` and marks each field `parsed` or `unparsed` (rows are prose — see e.g. `NVDA-2026-09-17.md`); (2) from then on, forward-only. Consensus-revision quadrants (Matrix `RS:113`) need ~13 weekly snapshots (one quarter) — declare "not defined" until then, never back-filled. |
| **Inputs / source** | Existing outputs; no external data. Risk: parsing brittleness → keep the parser strict and fail-soft (`unparsed`). |
| **Philosophy / graveyard** | Greenblatt (published record, warts and all) pass; helps the annual graveyard/benchmark audits (`graveyard-audit.md:125-136`, `benchmark-comparison.md:29-35`) by giving a real score history. |
| **Interaction / version** | Pure recording; no score change; feeds P-009, P-011, P-016, P-017. |
| **Implementation** | `scripts/snapshot.py record|diff|seed`; add step to Routine 2 (`automation-schedule.md`) and to the `/rescore` and `/new-position` "Watchlist" paragraph; `/what-changed` command; tests with fixtures from three real watchlist rows. |
| **Validation** | Seed, then compare seeded values with `holdings.md` for all 26 names: ≥ 90% field match. |
| **Effort / risk / priority** | **M**; **P1** (dependency for P-009, P-011, P-016). |

## P-011 — Portfolio-weighted metrics with coverage disclosure

| Field | Content |
|---|---|
| **Title** | `python -m scripts.portfolio_metrics` |
| **Type** | reporting |
| **Problem and failing case** | `holdings.md` lists scores per name but no aggregate; "how good, and how cheap, is the book?" is unanswerable, and a naive average would zero-fill the 28.52% TLT position. |
| **Exact rule** | `M = Σ w_i m_i / Σ w_i` over positions **with** the metric (skip and renormalise, never zero — Matrix `RS:122`, consistent with Rule 0). Report `coverage_total = Σ w_present / Σ w_all`, `coverage_equity`, missing tickers by name, and stale entries (score predates the current version, `watchlist/STALE.md`) excluded and listed. Metrics: Quality, Valuation, Composite, number of names PASS/AMBER/FAIL (P-009), weighted forward P/E when available. **Worked example (recorded scores of different dates; illustrative, not a fresh computation)** from `portfolio/holdings.md:51-78` (weights and Quality Scores of 21 scored equities): weighted Quality = **79.44**, weighted Composite = **33.69**; the 21 names cover **67.0%** of the book (98.2% of the equity part; the rest is TLT 28.52%, XEON 2.78%, RBRK 0.54%, RGL 0.68%, cash 0.24%); only **37.58%** of book weight sits in names currently ≥ 80.0 (ADBE, AVGO, BKNG, DUOL, META, NVDA, V, VEEV). |
| **Inputs / philosophy / graveyard** | holdings + snapshots. Greenblatt/Buffett — pass (know your own book). |
| **Interaction / version** | Reporting only. |
| **Implementation / validation** | New script; add to Routine 5 (monthly rebalance) output; tests: missing metric, all missing (exit non-zero), weights not summing to 100. Validation: reproduce the worked example. |
| **Effort / priority** | **S**; **P1**. |

## P-012 — Cluster concentration report in `/rebalance`

| Field | Content |
|---|---|
| **Title** | Cluster sums (report + acknowledgement, no cap) |
| **Type** | reporting / governance |
| **Problem** | The only concentration rule is the 15% single-name cap and "10–15 names" (`strategy.md:77,206-208`). Correlated exposure is invisible: subscription/software cluster MSFT 14.24 + ADBE 7.65 + NOW 1.98 + VEEV 1.37 + RBRK 0.54 + ZS 0.31 = **26.09%** (34.97% counting DUOL) (`holdings.md:51-78`) — one AI-disruption thesis. The Matrix's reader limit is 30% per sub-sector (`RS:125`), advice not engine rule. |
| **Rule** | `portfolio/clusters.md`: ticker → cluster tag (analyst-assigned). Report `cluster_weight`; if `≥ 30%` *(placeholder = Matrix's reader limit)*, the rebalance session must contain a written acknowledgement (why the correlation is understood). No forced trim. |
| **Philosophy** | Munger/Buffett — **conscious tension**: they prefer concentration; the report does not push diversification, it forces awareness ("understood" concentration). Marks (risk control) pass. Concentration test (`investor-philosophy-alignment.md:50`) — pass as reporting. |
| **Graveyard** | GE (a hidden concentration in captive finance) — different mechanism; partial. |
| **Interaction / version** | None. `rebalance.md` step 4 extension. |
| **Effort / priority** | **S**; **P2**. |

## P-013 — Valuation and Phase 01 specification fixes

| Field | Content |
|---|---|
| **Title** | Close three defects in the written rules |
| **Type** | governance |
| **Problem and failing cases** | (a) **PEG denominator undefined**: `valuation-scoring.md:89-105` says "PEG ≥ … " but never says which EPS growth is used; `fetch_fundamentals.py` has no PEG. The Matrix pins it (geometric mean of NTM and next-year consensus growth; verified, `01-verification.md` V10). DUOL was scored two ways (`decisions/2026-06-20-framework-clarification-peg-clean-earnings.md`). (b) **Undefined 10–20% band** in the Historical-PE modifier: `strategy.md:155-159` defines only >20% below, ±10%, >20% above; `valuation_score.py:122-131` refuses and stops the run in that band. (c) **Threshold drift** across documents: Net margin > 15% (`strategy.md:14`) vs > 12% (`valuation-scoring.md:207`); revenue CAGR > 10% (`strategy.md:16`, `operating-calendar.md:96`) vs > 8% (`valuation-scoring.md:209`); Net Debt/EBITDA < 2× (`strategy.md:18`, `operating-calendar.md:98`) vs ≤ 2.5× (`quality-scoring.md:21`, `valuation-scoring.md:212`). |
| **Rule** | (a) State: `PEG growth = geometric mean of (NTM consensus EPS growth, next-year consensus EPS growth)`; single available step used if only one; PEG stays Fast-Grower-only (R-02). (b) Fill the band by linear interpolation: `modifier = −10 × (|dev| − 10)/10` for `dev ∈ (−20, −10)`, `+10 × (dev − 10)/10` for `dev ∈ (10, 20)`, applied only where the existing table already applies ±10; keeps the modifier continuous (the existing three buckets are the endpoints). (c) Declare `quality-scoring.md` the single source for numeric Phase 01 thresholds and turn the copies into links. |
| **Inputs / risk** | None new. |
| **Philosophy** | Lynch (PEG scope) pass; Greenblatt (systematic rules, no ambiguity) pass; Marks (historical PE with structural override kept) pass. |
| **Graveyard** | Neutral. |
| **Interaction / version** | (a) and (c): documentation only. (b) **changes the score** for names in the band ⇒ bump version and run the stale mechanism; incidence unknown [F: no session records hitting the refusal; the script docstring documents it, `valuation_score.py:41-46`]. |
| **Implementation / validation** | Edit `strategy.md`/`valuation-scoring.md`; `valuation_score.py` interpolation branch + tests at ±10, ±15, ±20; count how many of the last 20 rescores fell in the band from their logged inputs. |
| **Effort / priority** | **S**; **P0** — removes a demonstrated ambiguity/defect at almost no cost. |

## P-014 — Print vs-index multiple reference (unscored)

| Field | Content |
|---|---|
| **Title** | "multiple ÷ S&P forward P/E" as a printed line |
| **Type / problem** | The Matrix scores this as a lens (`RM:58`); the repo has the Rate Gate instead. **Adapt only as an informational line** in `/new-position` output. |
| **Rule** | `rel = fwd_pe / index_fwd_pe`; print with the date and source of `index_fwd_pe` (never a stored constant). |
| **Philosophy / graveyard** | Marks second-level thinking — pass; no graveyard link. |
| **Interaction** | Not scored: scoring it would double count with the Rate Environment Gate (`strategy.md:28-52`) and depend on a 2026 index level (R-04). |
| **Version / effort / priority** | none; **S**; **P3**. |

## P-015 — Drawdown and window-defined price moves as re-score triggers

| Field | Content |
|---|---|
| **Title** | Define the window for Rule 9's ">15% move" and add a drawdown line |
| **Type** | gate-stage |
| **Problem** | Rule 9 says "> 15% move in stock price without a fundamental trigger" (`fair-value-methodology.md:266`) but not the window; `operating-calendar.md:9` mixes ">5% intraday" and ">15% unexplained". A slow grind is unspecified. The Matrix marks −30% "action" and −50% "readiness" lines but never says what the action is (`RS:116`) — do not copy the semantics. |
| **Rule** | Triggers **re-score only**, never an order: (i) ≥ 15% move within 5 trading days [window made explicit], (ii) ≥ 30% below the 1-year closing high for a held name, once per episode, (iii) ≥ 50%: write a pre-mortem in the session log. |
| **Philosophy** | Price-action test (`investor-philosophy-alignment.md:46`): allowed **only** because price is a trigger for re-examining fundamentals (as Rule 9 already is), not a decision rule; Marks/Klarman pass. Munger's objection to chart-based decisions is not engaged. |
| **Graveyard** | Slow-erosion cases (IBM) would surface earlier; Nokia partially. |
| **Interaction / version** | Extends Routine 1 (`automation-schedule.md:61`); no score change. Source: IBKR history or yfinance. |
| **Effort / priority** | **S**; **P2**. |

## P-016 — "What must change" next-band solver

| Field | Content |
|---|---|
| **Title** | `python -m scripts.scoring.next_band` (`/next-band <ticker>`) |
| **Type** | command |
| **Problem** | Notes reconstruct the answer by hand ("19 vs 18.655 shares", buy limits). The Matrix prints "what must change for the next verdict" (`RS:109-110`; `CC:86`). |
| **Rule** | Composite is monotone increasing in price (every price-dependent term — FCF yield, EV/EBIT, forward PE, PEG, Rate Step 1, Upside Modifier — worsens as price rises), so bisect `price ∈ [0.2×live, 3×live]` for the highest price with `Composite ≤ 49.9` (Cheap) and `≤ 29.9` (Very Cheap) holding fair values and quality fixed. Quality side: `points_missing = 80.0 − Q`, and the sub-score with the largest `(100 − sub) × weight` headroom (Matrix's "biggest headroom", `RS:104`). Output: "Composite ≤ 49.9 at price ≤ $X (−y%)". Needs price-dependent **raw** inputs (FCF, EBIT, net debt, shares, EPS forward), not pre-computed yields. |
| **Data / philosophy / graveyard** | Snapshots (P-010) hold the raw inputs; pure computation. Greenblatt (systematic) pass. No graveyard link. |
| **Interaction** | Uses `valuation_score.compute` unchanged ⇒ no new rules; answers "at what price would the framework act?" and complements P-001's return-based curve. |
| **Version / effort / priority** | none; **M**; **P1** (after P-010). |

## P-017 — `/compare a b c d`

Formatter over stored scores (P-010): up to 4 tickers, rows = Quality sub-scores, Valuation sub-scores, modifiers, gate state, flags, x2 CAGRs, basket, cluster; no recomputation (Matrix `compare.md`). **Type** command/reporting; **Effort** S; **Priority** P2; **Philosophy** Greenblatt (never rank quality and cheapness separately) pass; **Graveyard** n/a; **Version** none.

## P-018 — Tax-normalised EPS helper

| Field | Content |
|---|---|
| **Problem and failing case** | DUOL's EPS was distorted by a one-off $256.7M deferred-tax valuation allowance release, producing two different scores (`decisions/2026-06-20-framework-clarification-peg-clean-earnings.md`). Matrix rule: if the effective tax rate differs by > 10 pts from the prior 12 months, normalise using the median of 8 quarterly rates (`RM:48`). |
| **Rule** | `ETR_ttm = tax_ttm / pretax_ttm`; `ETR_ref = median(last 8 quarterly ETR)`; if `|ETR_ttm − ETR_ref| > 10 pp` *(Matrix's printed constant)*: `EPS_norm = pretax_ttm × (1 − ETR_ref) / diluted_shares`; show reported and normalised side by side; used only as the base for growth/PEG/P-002. |
| **Data** | 8 quarters of pretax income and tax provision — free yfinance gives ~4–5 quarters [I]; SEC XBRL (free `companyfacts`) needed ⇒ data risk **medium**. |
| **Philosophy / graveyard** | Buffett (see through accounting), Greenblatt pass; Valeant-type accounting noise. |
| **Interaction / version** | Inputs hygiene, Rule 6 (`fair-value-methodology.md:228-235`); **no bump** as long as it only feeds flags/PEG eligibility. |
| **Effort / priority** | **M**; **P2**. |

## P-019 — Collect-all precheck of missing inputs

`common.require` raises on the **first** missing field (`common.py:19-24`), so a `/new-position` run can bounce several times to collect inputs one by one at ~120–160K tokens per ticker (`new-position.md:30`). Add `python -m scripts.scoring.<module> --precheck --input …` that walks the same schema and lists **every** missing/invalid field at once (plus a completeness readout "n of N inputs present"; Matrix's "data completeness", `RS:131`), while `compute` still hard-stops. **Type** command/quality; **Effort** S; **Priority** P2; **Philosophy** Rule 0 — strengthened; **Version** none.

## P-020 — Governance kit

1. **Framework-change decision template** (`decisions/_TEMPLATE-framework-change.md`; `decisions/README.md` today has no template): what prompted it · rule text before/after · six-test philosophy check with a pass/fail per test · graveyard test · double-counting check · version bump y/n and stale-run scope · pilot result · acceptance criteria · rollback condition.
2. **Version ledger** (table in `framework/valuation-scoring.md` header or a new `framework/methodology-versions.md`): date → change → affected entries → stale run reference (the header already keeps a one-line history, `valuation-scoring.md:5`).
3. **External test vectors** for imported mechanics only: ABNB and NVDA x2 vectors (`01-verification.md` V1–V9) as fixtures in `test_x2_arithmetic.py` with explicit tolerance ±0.2%; never Matrix *scores*, which use different formulas.
4. **Unit-test additions per proposal** (each design lists its cases).

**Type** governance; **Effort** S; **Priority** P1; **Version** none; **Philosophy** Greenblatt (publish the method and results).

---

## Command-by-command additions

| Command | Added steps / checks | Proposal |
|---|---|---|
| `/screen` (`screen.md`) | Step 1: replace the one-line triage with a lookup against the competence registry (state + basket) and print it; Step 2: print the F1–F4 flag subset next to each candidate; print `CYCLE_PEAK_CANDIDATE` | P-006, P-008, P-002 |
| `/new-position` (`new-position.md`) | Step 0 Gate 0 line (basket/state); step 2 append SBC block (`sbc_pct_fcf`, after-SBC yield), flags table, Lynch category, cycle flag, forward-growth flag; new step 4b: x2 arithmetic + `BuyPrice(10%)`/`BuyPrice(15%)` and `E_VS_CONSENSUS`; step 5 add "next-band" output; write kill-lines file if a position is opened | P-006, P-007, P-008, P-002, P-004, P-005, P-001, P-016, P-003 |
| `/rescore` (`rescore.md`) | New step 0: kill-line check table (post-earnings); quality step gets `--prior-state` (three-state gate); print flags and SBC block; record a snapshot after the watchlist step | P-003, P-009, P-008, P-007, P-010 |
| `/rebalance` (`rebalance.md`) | Step 1: portfolio-weighted metrics with coverage; step 4b: cluster report with acknowledgement; step 5: recycling targets show `next-band` price for candidate names | P-011, P-012, P-016 |
| `/speculate` (`speculate.md`) | Step 1 gate reads the three-state quality (AMBER does **not** qualify — sleeve keeps the full 80.0 bar, `speculation-module.md:15`); print basket state (informational) | P-009, P-006 |
| `/telegram-scan` (`telegram-scan.md`) | Step 4: before `/new-position`, resolve basket; `stop` ⇒ log "stop-list — no action"; attach kill-lines when the post claims an earnings date | P-006, P-003 |
| `/safe-guard`, `/healthcheck` | No scoring change. Add to healthcheck: snapshot store writable and last snapshot ≤ 8 days old; consensus source reachable (if adopted). | P-010 |
| `/sync-portfolio` | After a sync, run `snapshot record` and `portfolio_metrics` and paste coverage into `holdings.md` header | P-010, P-011 |

## New commands

| Command | Inputs | Outputs | Module |
|---|---|---|---|
| `/flags <ticker>` | ticker or inputs JSON | flag table (PASS/FAIL/UNKNOWN, value, threshold, source, `scored_in`) | `scripts/flags.py` |
| `/x2 <ticker>` | ticker; consensus steps | base/pess/opt EPS, price, CAGR, doubling year, buy-price curve, E-vs-consensus | `scripts/scoring/x2_arithmetic.py` |
| `/compare a b [c d]` | 2–4 tickers | side-by-side table from snapshots | `scripts/compare.py` |
| `/what-changed [since]` | date | diff of snapshots: bands, gate states, flags, price-to-limit | `scripts/snapshot.py diff` |
| `/kill-lines <ticker>` | ticker | pre-earnings line set / post-earnings check | `scripts/kill_lines.py` |
| `/concentration` | none | cluster weights + coverage + acknowledgement prompt | `scripts/portfolio_metrics.py` |
| `/stop-list [basket]` | basket or ticker | state, reason, exception link | `scripts/competence.py` |
| `/next-band <ticker>` | ticker | price for next band; quality points missing | `scripts/scoring/next_band.py` |

## Data and automation

- **Snapshot store**: see P-010 (bootstrap: seed from watchlist rows, then forward-only; consensus revision series needs about one quarter of weekly runs).
- **SEC XBRL vs yfinance**: yfinance gives 4 annual and ~4–5 quarterly periods and dropped `t.info["ebit"]` (`fetch_fundamentals.py:1-40`). SEC EDGAR `companyfacts` (free, keyless) would supply 8+ quarters for P-018 (tax median), customer concentration (F12 only via text, not XBRL tags for every filer [I]), SBC, and 8-K Item 5.02 (management change) lists. **Recommendation**: add SEC only for the two fields that need depth (8-quarter tax rate, SBC fallback); keep yfinance for the rest. Non-SEC filers (`.HK`, `.T`, `.KS`, EU) stay manual — same as today.
- **Index-composition lists**: not needed by any P0/P1 item; skip (Matrix uses them for its Nasdaq/S&P pages, `screens/indices.md`).
- **Earnings calendar → Google Calendar**: Routine 2 already has a 7-day look-ahead and per-action `.ics` (`automation-schedule.md:46-60,145`); P-003 attaches "kill-lines due" to that existing `.ics` — no new routine. New routine only if consensus snapshots are adopted: **Routine 9 — weekly snapshot + consensus capture** (could be folded into Routine 2 to avoid another schedule).

## R — Explicitly rejected or parked ideas

| ID | Idea | Reason |
|---|---|---|
| R-01 | Copy the Matrix's Capital & SBC sub-score table | Failed verification: maxima sum to 21 for a weight of 10; ABNB 5.0 not reproducible (`01-verification.md` V32). SBC handled via P-007 instead |
| R-02 | PEG for all companies (Matrix lens) | Conflicts with Lynch and with `valuation-scoring.md:105`; PEG on cyclicals/stalwarts misprices |
| R-03 | Predictability-by-business-type as a 15-point weight | Author-tagged and judgment-heavy; would re-calibrate the strict 80.0 gate on an unvalidated table. Kept only as a tag (P-005) |
| R-04 | vs-S&P and growth-vs-market lenses as scored inputs | Double counts with the Rate Environment Gate; depends on a 2026 index P/E (20.1) and EPS-growth (13.6%) constant |
| R-05 | "Reviewed by X" authority tags gating verdicts | Not transferable authority; this repo's sign-off is the user's own |
| R-06 | Unknown value = 40% of weight substitution | Conflicts with Rule 0 (estimation of a score input); the Matrix's own tables contradict the 40% claim (V33) |
| R-07 | Fixed 4% "good yield", pessimistic multiple 16, mega-cap +1 tweak, index EPS-growth fallback 13% | 2026-regime constants; would age badly (`RS:83,150`) |
| R-08 | ROIC-minus-WACC spread as a quality factor | Weak: the ROIC > 15% screen already implies a positive spread for any plausible WACC (7–10%, `fair-value-methodology.md:191-194` requires WACC only for DCF); the Matrix has no WACC either; adds an estimation-heavy input (ERP, beta) — parked P3 |
| R-09 | Nightly recompute of a full universe | Cost/benefit: repo is event-driven, concentrated (10–15 names) — weekly snapshots suffice |
| R-10 | Replace the continuous 0–100 composite by a 5×5 verdict map | Loses gradient and position sizing; only the *cap logic* is imported (P-009) |
| R-11 | Guidance cut as a scored penalty/cap | Contradicts the Guidance test (`investor-philosophy-alignment.md:51`); the Matrix itself cannot compute it on free data (`RM:90`) |
| R-12 | Reader position ranges (A/B 5–10% …) and sub-sector **cap** of 30% as hard rules | They are the Matrix's reader advice, not engine rules; the repo's 15% cap is a user decision (`decisions/2026-06-07-framework-change-position-cap.md`). Only reporting (P-012) |
| R-13 | Paid "AI analytics" tile / AI classification of moats | Cannot be audited (Rule 0); locked on the site anyway (`CC:34`) |
| R-14 | Special cell "level A with PEG < 0.5 → BUY regardless" | Unverified rule (C15); conflicts with the score-band logic |

## Glossary

From [framework/glossary.md](../../framework/glossary.md): **Composite Score**, **Quality Score**, **Valuation Score**, **Rule 9**, **FCF yield**, **FCF/NI conversion ratio**, **Owner Earnings**, **SBC (Stock-Based Compensation)** (employee pay in shares/options — a non-cash expense added back in cash-flow statements), **PEG ratio**, **Fast Grower**, **Net Debt/EBITDA**, **Hard disqualifier**, **Hurdle rate** (10% here), **CAGR**, **EPS**, **Diluted EPS**, **Effective tax rate**, **Deferred tax valuation allowance release**, **NTM (Next Twelve Months)**, **TTM (Trailing Twelve Months)**, **Interest coverage (ratio)**, **CapEx**, **MoS (Margin of Safety)**, **Turnover (portfolio turnover)**, **Catalyst window**, **Time-stop**, **Expectancy**, **WACC**, **Beta**, **Equity Risk Premium (ERP)**, **8-K**, **10-K**, **EDGAR**.

New terms (not yet in glossary.md):
- **Kill-line** — a threshold written down *before* an earnings report; crossing it forces a defined next step (a re-score, or an exit review) with no argument after the fact.
- **Hysteresis / three-state gate** — PASS at ≥ 80.0; "AMBER" for an already-held name between 78.0 and 80.0 (keep holding, no adding); FAIL below. Stops flip-flopping on a 0.1-point move.
- **Cycle peak** — top of a business cycle, when earnings are temporarily unusually high and the stock looks cheap.
- **x2 arithmetic** — projecting earnings five years ahead × a future P/E to get a price and a yearly return; "x2" refers to when the price would double.
- **Buy-price curve** — the price at which the projected base yearly return equals a chosen target (e.g. 10%).
- **Cluster** — holdings that share one main risk thesis.
- **Coverage** — the share of portfolio weight for which a metric was available.
- **Basket** — a business-type category in a competence registry.
- **Stop-list** — business types the investor will not analyse for core holdings.
- **Consensus** — the average analyst forecast.
- **Precheck** — a dry run that lists every missing input at once instead of stopping at the first.
- **Divergence flag** — a warning that two measures of the same thing (trailing vs forward growth) disagree.

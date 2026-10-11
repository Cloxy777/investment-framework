# Open questions for the user

Decisions only you can make, plus facts worth re-checking on the Matrix site. Site access was **not** used in this review. Note: the access window mentioned in the brief (until 06.10.2026) has already passed as of 2026-10-11, so the `LIVE` items below may no longer be checkable; they are kept as a record of what stays unresolved.

## A. Decisions for you

| # | Question | Why it matters | Related |
|---|---|---|---|
| 1 | **Risk appetite / gate strictness.** Keep the binary 80.0 gate, add a three-state PASS/AMBER/FAIL (hold-but-no-adds between 78.0 and 79.9), or lower the gate? The 2026-06-29 decision said "lower later only if it screens out too much". | MSFT (14.24% of the book) fails by 0.1; ABNB passes by 0.5. Only 37.6% of book weight is in names ≥ 80.0 | P-009 |
| 2 | **Binary gate vs finer grading.** Do you want Matrix-style levels (A/B/C) with different position limits, or keep the continuous Composite? | Review recommends keeping the Composite (R-10) | 02 row 34 |
| 3 | **Pay for forward consensus data?** Which provider/tier, or stay on yfinance + manual TIKR/Koyfin pastes? (I did not research prices.) | Blocks P-001 x2 arithmetic and P-004; without it those run only on manual input | P-001, P-004 |
| 4 | **Competence-circle stop-list.** Do you want one? If yes, which business types are `core`, `stop`, `unclear`? Should `stop` also block the speculation sleeve? | Gate 0 saves full `/new-position` runs (120–160K tokens each) and closes the "framework gap" holdings (TLT, XEON, RGL) | P-006 |
| 5 | **Appetite for more automation.** Weekly snapshot commits, auto-generated kill-line files, a possible Routine 9 for consensus capture? | Each adds files/PRs; the review defaults to folding into Routine 2 | P-003, P-010 |
| 6 | **SBC-adjusted yield (Phase B).** Accept that SBC-heavy names (DUOL 8.88% of the book, ZS, RBRK, NOW, ADBE, VEEV) will score worse and may move bands? Pilot first? | Largest scoring impact in the set | P-007 |
| 7 | **Which return bar defines "buy" for the x2 cross-check?** Repo hurdle 10% (`valuation-scoring.md:130`) vs the Matrix's 15% STRONG BUY bar. | Changes which names look "buyable" in the buy-price curve | P-001, 05 D3/D7 |
| 8 | **Composite 50/50 weighting.** V, MA, NFLX, GOOG show "false green" Composites when Quality is high but Valuation is only fair. Review the weighting? | Out of scope for this review but surfaced by the paired comparison | 05 D7 |
| 9 | **Cluster concentration.** Report-only with a written acknowledgement at ≥ 30%, or a hard limit? Software/subscription cluster is 26.1% (35.0% with DUOL). | Munger-style concentration vs correlated risk | P-012 |
| 10 | **Canonical Phase 01 numbers.** Net margin 12% or 15%? Revenue CAGR 8% or 10%? Net debt/EBITDA 2× or 2.5×? Documents disagree. | Needed to remove the drift | P-013(c) |
| 11 | **Attribution / terms.** The Matrix is a third party's closed-beta product. Are you comfortable with the research folder and this review referencing its methodology? Should a note be added? | The review re-derives ideas rather than copying text, but the research folder documents the site's UI | — |
| 12 | **Untracked/undocumented trades** (ADBE add, BKNG fill, etc., `portfolio/holdings.md:9-15`). Out of scope here, but kill-lines and the competence circle do not prevent them. | Governance gap remains | — |

## B. Facts to re-check on the Matrix site (`LIVE`) — if access is still available

| # | Check | Resolves |
|---|---|---|
| L1 | Does the ABNB card show a with-options NTM P/E? Which index P/E feeds the S&P lens? | E1 (lens −1 vs expected 0) |
| L2 | ABNB "Рівень якості" tile: which EPS growth feeds the Growth component (needs bucket 15–25%, but PEG shows 27.5%)? | E2 |
| L3 | MA (level A) x2 tile: is the BUY bar printed as 14.0% or 15.0%? | E3 |
| L4 | NVDA own-history lens: 5y minimum, 3y maximum, average actually used | V21, C6 |
| L5 | Source of the x2 "3-year average multiple" (ABNB 21.8) vs the lens's trailing 3-year average (29.1) | C7 / E10 |
| L6 | Any A/B card with a fair price word shown as STRONG BUY (or text saying it is possible) | C4 / E9 |
| L7 | Capital & SBC component: printed sub-point maxima, ABNB and NVDA | V32 / E12 |
| L8 | Neutral values used for unknown inputs, per component | V33 / E13 |
| L9 | One pass over the flag table for numeric thresholds (interest burden, dilution, SBC serious/critical) | P-008 placeholders |
| L10 | AVGO card (all components, flags, x2) and a clean re-read of GOOG vs META rows | 05 D10, C13 |
| L11 | Does the screener PEG column use NTM growth while the card uses the 24-month geometric mean? | E11 |
| L12 | List of "critical fields" behind the data-completeness percentage | Completeness spec |
| L13 | Meaning of "no more than 25% per step" in the growth decay | E14 |
| L14 | Wording of "gates 2 and 3" / basis switcher | E6 |
| L15 | Capture the EPS path for one more name (e.g. MSFT) to get a second independent x2 test vector | P-001 tests |

## Glossary

From [framework/glossary.md](../../framework/glossary.md): **Composite Score**, **Quality Score**, **Valuation Score**, **SBC (Stock-Based Compensation)**, **Hurdle rate**, **CAGR**, **Forward PE**, **PEG ratio**, **Net Debt/EBITDA**, **Turnover (portfolio turnover)**, **NTM (Next Twelve Months)**, **Catalyst window**.

New terms (not yet in glossary.md): **Gate strictness** — how high the minimum Quality Score is set; **Competence circle / stop-list** — see `02-gap-analysis.md`; **Consensus** — average analyst forecast; **LIVE** — marker for a fact that can only be checked on the live site.

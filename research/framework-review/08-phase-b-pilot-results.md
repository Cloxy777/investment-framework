# Part 8 — Phase B pilot results (2026-10-12)

**Read-only analysis; nothing in the framework changed.** Plan and acceptance criteria: [07-phase-b-plan.md](07-phase-b-plan.md). Reproduce: `python research/framework-review/pilot/pilot_phase_b.py` (raw output: [pilot/pilot-results-2026-10-12.json](pilot/pilot-results-2026-10-12.json)).

## Method and limits

- **Sensitivity, not full re-scores.** A full re-score needs manual inputs (moat evidence, fair values, 10Y gate). So each change is applied only to the sub-score it touches, using live yfinance data for that sub-score, and the difference is added to the score last recorded in [holdings.md](../../portfolio/holdings.md). Live inputs are today's; recorded scores date from each holding's own review (30 Jul – 12 Oct).
- **Coverage: 15 of 20 holdings.** `fetch_fundamentals` refuses (missing yfinance rows) for AMZN, BKNG, MBGL, TRN and ZS; RBRK has no numeric score; NVO returned no SBC. These are data gaps, not passes.
- Upgrade-1 Owner-Earnings names (MSFT, GOOG, META, AMZN) are exempt from B1 by design.
- B3's scale (EBIT margin 0–40% → 0–100) and B5's 2.0 buffer are placeholders. **B4 (capex / growth-source) was not piloted** — it needs per-company qualitative evidence.

## B1 — SBC-adjusted FCF yield (scored): supported

`ΔValuation = 0.40 × (FCF_Score(after SBC) − FCF_Score(reported))`; one point of yield is worth 4 valuation points.

| Ticker | SBC/FCF | FCF yield → after SBC | Δ Valuation | Recorded → new Valuation | Composite band changes? |
|---|---|---|---|---|---|
| DUOL | 36.4% | 5.75% → 3.66% | **+8.4** | 85.1 → 93.5 | no (51.0 → 55.1, same band) |
| CSGP | 84.6% | 1.92% → 0.30% | **+6.5** | 87.8 → 94.3 | n/a (fails Quality gate) |
| NOW | 47.8% | 3.16% → 1.65% | **+6.0** | 75.9 → 81.9 | n/a (fails gate) |
| NKE | 32.7% | 4.17% → 2.80% | +5.5 | 55.2 → 60.7 | n/a (fails gate) |
| UBER | 19.2% | 6.93% → 5.60% | +5.3 | 37.4 → 42.7 | n/a (fails gate) |
| VEEV | 29.7% | 3.49% → 2.46% | +4.2 | 65.9 → 70.0 | no (40.0 → 42.0) |
| ADBE | 19.6% | 11.46% → 9.22% | +3.1 | 0.0 → 3.1 | no (8.4 → 9.9) |
| AVGO | 21.5% | 2.32% → 1.82% | +2.0 | 71.4 → 73.4 | no (42.6 → 43.5) |
| SPGI, NFLX, NVDA | 4–6% | — | +0.5 … +0.8 | — | no |
| MSFT, GOOG, META | (Owner Earnings) | — | 0 (exempt) | — | no |

Against the plan's acceptance criteria: SBC-heavy names move materially and explainably (DUOL, NOW, VEEV, ADBE); Owner-Earnings names don't move; **no Quality-gate passer changes Composite band**. DUOL's Valuation lands in the 90+ "Extreme" range, but actions run on the Composite (55.1), so no trim is triggered. **B1 passes.**
Caveats: yfinance FCF/SBC should be confirmed against filings for any name that matters; the ADBE recorded valuation of **0.0** looks like a stale or odd value in `holdings.md` (live FCF yield 11.5% would give FCF_Score 0) — noted, not investigated; ZS and RBRK could not be tested.

## B2 — SBC ≥ 100% of FCF as a hard disqualifier: harmless, catches nothing today

Highest SBC/FCF among the 14 holdings with data: CSGP 84.6%, then META 61.3%, GOOG 52.8%. None reaches 100%. Costs nothing as a tripwire; changes no current position.

## B3 — Operating margin replaces gross margin in Quality: **fails acceptance, do not adopt as specified**

`ΔQuality = 0.15 × (OpMargin_Score − GrossMargin_Score)`, 15 holdings:

| Moves **down** | Δ Quality | | Moves **up** | Δ Quality |
|---|---|---|---|---|
| CSGP (EBIT margin 2.2%) | **−13.9** (69.2 → 55.3) | | NFLX | +4.2 |
| DUOL (13.7%) | **−8.5** (83.2 → 74.7, **drops through the 80 gate**) | | GOOG | +3.6 |
| NOW (16.5%) | −7.8 | | MSFT | +2.3 (**79.9 → 82.2, newly passes the gate**) |
| NKE (8.2%) | −5.0 | | AVGO | +2.1 |
| UBER (12.9%) | −3.1 | | SPGI | +1.7 |
| VEEV (29.9%) | −2.8 | | NVDA | +1.0 |

- **Systematic bias:** growth software that reinvests heavily (DUOL, NOW, CSGP, VEEV) and low-margin platforms are penalised; mature or capital-heavy franchises (NFLX, GOOG, MSFT) are rewarded. Mean |Δ| is 3.8 points; range −13.9 to +4.2.
- **Breaks the acceptance rule** "nobody newly admitted past 80.0 purely through a methodology change": MSFT crosses up. (MSFT sits at 79.9, so *any* positive change flips it — a knife-edge, not evidence of better measurement.) DUOL crosses *down* by a large, substantive amount.
- A 50/50 gross/operating blend is milder (CSGP −7.0, NOW −3.9) but still flips both gates (DUOL → 79.0, MSFT → 81.0).
- The plan's own review also flagged that net margin already sits in the Profitability sub-score; an operating-margin input there risks double counting.
- **Recommendation: drop B3 as a scored change.** If margin quality is a concern, show operating margin as an advisory line next to gross margin and let the analyst judge.

## B4 — Capex / growth-source discipline: not piloted

Needs qualitative evidence per company (organic vs M&A, how capex is funded). Keep as a judgment item in the analyst's checklist, or pilot later on a short list (e.g. holdings with large acquisitions).

## B5 — Hysteresis on action-band edges: inconclusive, low evidence of need

- Composite histories exist for only 7 holdings (2–5 data points each, quarterly). Two edge crossings occurred (DUOL 44.5 → 51.0; NKE 47.5 → 58.1). **Hysteresis would have suppressed neither**: both were genuine multi-session trends. Acceptance criterion (≥50% of flips suppressed) can't be met or refuted — there is no noise-flip in the record.
- Near an edge today (within 2 points): DUOL +1.0 over 50, SPGI +1.8 over 30, NOW +1.4 over 50, MSFT −0.5 under 30 (the last three fail the Quality gate, so their Composite is reference only). This is where a buffer would matter in future.
- **Recommendation: park.** No demonstrated problem yet; revisit once the snapshot store (P-010) gives a denser history, or if a real flip-flop appears.

## B6 — Cycle-peak / multiple-ceiling as scored limits: not testable on free data

- `cycle_peak` is **UNKNOWN for all 15** — yfinance returns 5 quarters of Diluted EPS, the flag needs 8.
- `multiple_ceiling` is NONE for all (highest forward PE: VEEV 28.7, NOW 28.0 — both under 30).
- Forward EPS growth could only be proxied as `forwardEps ÷ trailingEps − 1`, which gave nonsense (CSGP +885%, NOW +213%) because it divides a non-GAAP forward figure by a GAAP trailing one. **Do not use that proxy.**
- Value-trap candidates by forward PE alone (ADBE 8.6, NVO 11.6, NVDA 14.2) can't be judged without trailing EPS growth.
- B6 therefore depends on the open data decision (consensus / EPS-history source, [open question #3](open-questions-for-user.md)). Until then the advisory flags stay as shipped.

## Verdict and recommended next step

| Item | Result | Recommendation |
|---|---|---|
| B1 SBC-adjusted FCF yield | passes | **Adopt** (needs the gross-cash buyback guard from [04-design.md D2](04-design.md)) |
| B2 SBC ≥ 100% disqualifier | harmless | Adopt with B1 |
| B3 operating-margin Quality | fails acceptance | **Drop** (advisory line only) |
| B4 capex discipline | not piloted | Defer, judgment item |
| B5 action-band hysteresis | inconclusive | Park |
| B6 scored cycle/ceiling limits | untestable | Wait for an EPS-history source |

So the one-bump methodology change shrinks to **B1 + B2**, which move the Valuation Score of SBC-heavy names up (more expensive) by roughly 3–8 points, change no Quality-gate passer's Composite band, and need one version bump plus one stale-score run. That is a smaller, better-evidenced change than the original six-item bundle.

## Glossary

From [framework/glossary.md](../../framework/glossary.md): **SBC (Stock-Based Compensation)**, **FCF yield**, **Owner Earnings**, **Quality Score**, **Valuation Score**, **Composite Score**, **Hard disqualifier**, **Hysteresis**, **Cycle peak**, **Multiple ceiling (advisory flag)**, **Diluted EPS**.

New terms: **Sensitivity analysis** — changing one input or rule and measuring how much the result moves, holding everything else fixed; **EBIT margin** — operating profit before interest and tax as a percentage of revenue; **Non-GAAP vs GAAP EPS** — earnings per share adjusted to exclude certain costs (non-GAAP) versus the official accounting figure (GAAP); **Knife-edge** — a score so close to a threshold that any small change flips the outcome.

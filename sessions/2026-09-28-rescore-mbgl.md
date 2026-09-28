# RESCORE — MBGL (Mobility Global, Inc.)

**Task type:** RESCORE (routine quality-gate re-check). MBGL was first fully evaluated in the [2026-08-09 session](2026-08-09-rescore-mbgl.md), which found a Quality Score of 51.0 and a hard disqualifier (Net Debt/EBITDA), so it **fails the 80.0+ gate and Phase 02 is not run**. This session re-checks whether anything has changed since then.

**Date:** 2026-09-28 (Monday)
**10Y US Treasury Yield:** 5.21% (2026-09-28, per Trading Economics — for the record only; not needed this session, since the Quality gate fails and Phase 02/Rate Environment Gate is never reached).
**Last review on record:** 2026-08-09 ([session](2026-08-09-rescore-mbgl.md), [watchlist entry](../watchlist/in-portfolio/MBGL/MBGL-2026-08-09.md)).
**Current MBGL portfolio weight:** 0.03% (1 share) per [holdings.md](../portfolio/holdings.md) — unchanged, immaterial to sizing/cap math.

> *Jargon decoded on first use — see closing Glossary section.*

---

## 0. Identity (confirmed previously, not re-derived)

**MBGL = Mobility Global, Inc.** — NYSE-listed, spun off from S&P Global Inc. (SPGI) effective 2026-07-01. Comprises the CARFAX consumer/dealer vehicle-history business (~67% of revenue) and a B2B automotive data/analytics segment (~33%). Full identity confirmation (IBKR contract search, yfinance, SEC EDGAR Form 10-12B/A) was done in the [2026-08-09 session](2026-08-09-rescore-mbgl.md) §0 and is not repeated here — nothing about the company's identity has changed.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$17.76** | Two independent sources agree exactly: IBKR `get_price_history` (contract_id 893054611, `ONE_DAY` bars) — 2026-09-28 regular-session close = $17.76, prior close $17.87; and `stockanalysis.com` (fetched live) — "$17.76... September 28, 2026 at 4:00 PM EDT," previous close $17.87. IBKR `get_price_snapshot`'s `last` field also read $17.76 at the query timestamp, corroborating. |
| 52-week range | $17.72 – $26.00 (IBKR `misc_statistics`, `low_52w` $17.72 — MBGL is now trading near its post-spin low) | |
| Change since last review | $19.70 (2026-08-09) → $17.76 (2026-09-28), **-9.85%** | Within Rule 9's >15% unexplained-move threshold — not itself a trigger. |
| Position held | 1 share, market value ≈ $17.76 | [portfolio/snapshots/ibkr.md](../portfolio/snapshots/ibkr.md) — 0.03% of the combined portfolio, trivial. |

---

## 2. What Changed Since 2026-08-09 — Rule 9 / Trigger Check

Checked explicitly, per the operating brief's "act only on documented triggers" rule:

| Rule 9 trigger | Status | Detail |
|---|---|---|
| Quarterly earnings | **No new report.** MBGL's Q2 2026 10-Q (period ended 2026-06-30, filed 2026-08-07) remains the latest. Q3 2026 earnings are not expected until **~2026-11-05** (per Benzinga's earnings-calendar estimate, cited below) — after this session's date. |
| Guidance revision | The FY2026 revenue/Adjusted-EBITDA guidance cut ($1.87–1.885B revenue, $745–760M Adj. EBITDA) was announced **on the Q2 2026 earnings call itself (2026-08-07)** — i.e. it predates, and was already available at, the 2026-08-09 session. Not a new trigger this cycle. |
| M&A | None found. |
| Management change | None found. |
| Macro shift | 10Y Treasury has risen materially (from levels implied by the 2026-08-09 session's context to **5.21%** on 2026-09-28, near multi-decade highs per Fortune/tradingeconomics.com) — relevant to Phase 02's Rate Environment Gate in general, but **not applicable to MBGL**, which never reaches Phase 02. |
| >15% unexplained price move | Price fell 9.85% (see §1) — under the 15% threshold, and in any case not "unexplained": broadly consistent with the guidance cut and rising-rate pressure on a newly-leveraged spinoff, not a standalone anomaly. |
| Other corporate action | A routine **$0.06/share quarterly dividend** was declared 2026-08-10, paid 2026-09-10 to holders of record 2026-08-27 — same payout level as prior; on the 1-share position this is $0.06, immaterial and not a Rule 9 trigger. |

**Conclusion: no Rule 9 fundamental-event trigger fired this cycle.** This is a routine re-check, not a new evaluation.

---

## 3. Quality Score Re-Check

Because MBGL has not filed a new 10-Q since 2026-08-07 and no fundamental event has occurred (§2), **the underlying financial-statement inputs to the Quality Score are unchanged from the 2026-08-09 session** — same TTM window (Q3'25–Q2'26 blend of carve-out and standalone data), same balance sheet (2026-06-30). Per the operating brief's "never invent or estimate financial data" rule, this session reuses those verified, cited figures rather than fabricating a new TTM window with no new quarter to extend it — re-running the identical inputs through the scoring script to confirm the result, not re-deriving new numbers.

**Inputs (unchanged, cited to 2026-08-09 session §6/§7, itself sourced to the Information Statement/Exhibit 99.1 and the Q2 2026 10-Q):**

```
net_margin_pct              = 11.30
roic_pct                    = 1.826
fcf_positive_3yr_or_more    = true
gross_margin_pct            = 70.95   (proxy — company doesn't disclose a gross-margin line, §3 flag 3 of the 08-09 session)
revenue_cagr_3yr_pct        = 8.56    (2yr CAGR proxy — FY2022 never disclosed, §3 flag 2 of the 08-09 session)
tam_expansion_evidence      = true    ($75-81B TAM vs $1.75B FY2025 revenue, cited)
net_debt_to_ebitda          = 2.840   (GAAP EBIT+D&A basis, primary convention)
moat_signals                = 3 of 5 true (market-share-penetration proxy, network effect, switching costs)
fcf_ni_ttm_pct               = 201.5
fcf_ni_annual_pct            = [230.4, 198.1, 208.6]  (FY2023-FY2025, oldest first)
```

**Script output** (`python -m scripts.scoring.quality_score --input mbgl_inputs.json`), pasted verbatim:

```
# FAILS GATE
Reason: Net Debt/EBITDA 2.84x exceeds the 2.5x threshold
```

The script exits on the hard disqualifier before computing the weighted total (correct behavior — hard disqualifiers are checked before the weighted score per [quality-scoring.md](../framework/quality-scoring.md), and the script refuses to produce a Composite Score for a gate-failing company). For full transparency (the operating brief's "show every calculation, no black-box outputs" rule), the weighted calculation — carried forward unchanged from the 2026-08-09 session, since none of its inputs have moved — is:

```
Profitability (25%) = (NetMargin_Component 37.67 + ROIC_Component 6.09) / 2         = 21.88
Margins (15%)        = GrossMargin_Score                                             = 88.69
Growth (20%)          = Growth_Score (34.22 + 10 TAM bonus)                          = 44.22
Balance Sheet (15%)   = clamp(100x(1 - 2.840/4))                                     = 29.0
Moat Signal (15%)     = (3/5) x 100                                                  = 60.0
FCF Quality (10%)     = clamp(((2.015-0.40)/0.60)x100)                               = 100.0

Quality Score = (21.88x0.25)+(88.69x0.15)+(44.22x0.20)+(29.0x0.15)+(60.0x0.15)+(100.0x0.10)
              = 5.470 + 13.304 + 8.844 + 4.350 + 9.000 + 10.000 = 50.968 -> 51.0
```

# Quality Score = 51.0 — unchanged from 2026-08-09. FAILS the 80.0+ gate (29.0 points short), AND the Net Debt/EBITDA hard disqualifier independently fires (2.840x vs the 2.5x standard threshold — Upgrade 5's asset-light 4x override remains inapplicable, as established in the prior session: run-rate interest coverage ~2.9x is far below the required >15x).

**No drift, positive or negative.** This is a genuine "nothing changed" re-check, not a re-derivation — flagged explicitly as such rather than presented as fresh analysis.

---

## 4. Valuation Score / Composite Score

**Not computed.** Per [quality-scoring.md](../framework/quality-scoring.md) and this repo's own established precedent, a company that fails the 80.0+ Quality gate does not proceed to Phase 02 (Rate Environment Gate, Valuation Score) and no Composite Score is produced — `scripts/scoring/composite_score.py` would itself refuse to run without both a Quality Score ≥80.0 and a computed Valuation Score. This session, like the 2026-08-09 session before it, is a **quality-gate-only** re-score for MBGL.

---

## 5. Action Recommendation

**Recommendation: HOLD the existing 1-share position. No forced action.** Unchanged from 2026-08-09.

- Position remains trivial (0.03% of the combined portfolio, ~$17.76 market value) — neither the Quality gate failure nor the price decline since last review changes the calculus.
- No Phase 06 Full Exit trigger applies (no fundamental deterioration beyond what was already assessed 2026-08-09; no broken thesis, no balance-sheet crisis beyond the already-documented spin-related leverage, no >15% unexplained move).
- As before: the human may reasonably choose to sell the single share as portfolio-hygiene housekeeping (a governance-flagged, near-zero-cost-basis line item), but that remains a discretionary choice, not a framework-driven trade.

---

## 6. Data Gaps / Flags

- **No new company-reported financials this cycle** — Q3 2026 earnings not due until ~2026-11-05. This session's Quality Score is a confirmed carry-forward of 2026-08-09's verified figures, not independently re-derived from new source data; flagged explicitly rather than silently presented as a fresh recomputation.
- **10Y Treasury (5.21%, 2026-09-28)** fetched for the record only — not used, since Phase 02 is never reached.
- All data-thinness flags from the 2026-08-09 session (carve-out vs. standalone financial history, 2yr vs. 3yr revenue CAGR proxy, no disclosed gross-margin line, GAAP vs. Adjusted EBITDA divergence) still apply unchanged and are not re-derived here — see that session's §3 for the full, still-current record.
- Nothing was invented or estimated to fill the "no new quarter" gap — the only new inputs this session are the live price (§1, two independently corroborated sources) and the 10Y yield (fetched, unused).

---

## 7. Housekeeping — Files Updated This Session

- **[sessions/2026-09-28-rescore-mbgl.md](2026-09-28-rescore-mbgl.md)** — this file (new).
- **[watchlist/in-portfolio/MBGL/MBGL-2026-08-09.md](../watchlist/in-portfolio/MBGL/MBGL-2026-08-09.md)** — `python -m scripts.watchlist_diff` was run with `--old-score "NOT SCORED" --old-category HOLD --new-score "NOT SCORED" --new-category HOLD` (score and action category both unchanged) and returned `{"decision": "append", "reason": "no significant change"}` — per [watchlist/README.md](../watchlist/README.md)'s "Significant change" rule, **no new dated file was created**; instead the existing file's "Last checked (no significant change)" line was updated with the script's rendered content (verbatim): *"2026-09-28 — Quality gate re-check: no new fundamentals since Q2 2026 10-Q (Q3 2026 earnings not due until ~2026-11-05); Quality Score unchanged at 51.0, gate still fails (hard disqualifier: Net Debt/EBITDA 2.84x GAAP basis). Live price $17.76 (vs $19.70 on 2026-08-09). No Rule 9 trigger fired. See session."*
- **`python -m scripts.stale_score --apply`** was run — see result below.
- **`portfolio/holdings.md`** — intentionally **not edited** by this session; the Last Review date update is left to the orchestrator's batch update.
- **[framework/glossary.md](../framework/glossary.md)** — checked; no new terms required. Every jargon term used above (Spin-off, Quarterly earnings/10-Q, Guidance, Rule 9, Hard disqualifier, Net Debt/EBITDA, ROIC, NOPAT, TTM, Moat, TAM, Quality Score, Composite Score, Rule 0, CAGR, D&A, EBIT, EBITDA, Gross Margin, Net Margin, FCF/NI conversion ratio) already exists from the 2026-08-09 entry.

**`stale_score --apply` output** (pasted verbatim):

```json
{
  "version": "2026-06-29",
  "newly_stale": [],
  "resolved": []
}
```

---

## 8. Stale-Score Check

Run per this framework's standing mechanism (see [watchlist/README.md](../watchlist/README.md#stale-scores--when-the-scoring-methodology-changes)): a rescore, once completed, clears any `⚠️ STALE SCORE` banner for that ticker if it was marked. MBGL was never marked stale (it has no numeric Phase-02 score — "Phase 01 FAIL / not scored" entries are explicitly excluded from the stale-score mechanism per the README) — consistent with MBGL appearing in neither the `newly_stale` nor `resolved` lists above. No unrelated ticker went newly stale either, so no `--reason` flag was needed.

---

## 9. Next Review Trigger

- **Q3 2026 earnings (~2026-11-05)** — MBGL's second quarterly report as an independent company; first point at which the Balance Sheet sub-score (Net Debt/EBITDA) could plausibly move if any debt paydown has occurred, and the first genuine like-for-like standalone TTM comparison becomes available.
- Standing Rule 9 triggers apply as normal: earnings, guidance revision, M&A, management change, macro shift, or a >15% unexplained price move.
- Given the position's triviality (0.03%, ~$17.76) and the absence of any new information this cycle, routine quarterly cadence remains sufficient — no urgency escalation warranted.

---

## Glossary

| Term | Meaning |
|---|---|
| **10-Q (Quarterly Report)** | The quarterly financial-disclosure report a US public company files with the SEC — MBGL's Q2 2026 10-Q (filed 2026-08-07) remains its latest as of this session. |
| **Adjusted EBITDA** | A company's own non-GAAP variant of EBITDA that strips out items management deems non-recurring. This framework computes its own GAAP-derived EBITDA (EBIT + D&A) as the primary Balance Sheet input rather than trusting the company's adjusted figure. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate connecting a start and end value over several years. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate. Not computed for MBGL (gate failure). |
| **D&A** | Depreciation & Amortization. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is turning into real cash. MBGL's remains very strong (201.5% TTM, unchanged). |
| **Gross Margin** | Gross Profit ÷ Revenue. MBGL does not disclose this line directly; "Operating-related expenses" is used as a labeled proxy for Cost of Revenue. |
| **Guidance** | A company's own forward-looking forecast (e.g. of revenue or earnings) for a future period — MBGL cut its FY2026 revenue/Adjusted EBITDA guidance on its 2026-08-07 earnings call, a change that predates and does not newly trigger this session. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted sub-score total — MBGL's Net Debt/EBITDA (2.840x, GAAP basis) fires this disqualifier. |
| **Moat** | A durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits — MBGL scores 3 of 5 cited moat signals true. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) ÷ EBITDA — this framework's primary balance-sheet-risk gate; MBGL's is 2.840x (GAAP basis), unchanged this cycle. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Quality Score** | This framework's 0.0–100.0 continuous score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. MBGL: **51.0**, unchanged, fails the gate (and independently fails via a hard disqualifier). |
| **ROIC** | Return on Invested Capital — NOPAT ÷ (Debt + Equity). MBGL's remains severely depressed (1.83% TTM) by a large parent-allocated Invested Capital base plus spin-related debt. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: quarterly earnings, guidance revision, management change, material M&A, macro shift, or a >15% unexplained price move. None fired this cycle (§2). |
| **Spin-off** | A corporate transaction separating part of a business into a new, independently-traded public company via a pro-rata share distribution — S&P Global's 2026-07-01 spinoff of Mobility Global is the origin of this position. |
| **TAM** | Total Addressable Market — MBGL's own cited $75-81B estimate against $1.75B FY2025 revenue. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — for MBGL this session, the same TTM window as 2026-08-09 (no new quarter available to extend it). |

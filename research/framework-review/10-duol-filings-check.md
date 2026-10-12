# Part 10 — DUOL: SBC and net income checked against SEC filings (2026-10-12)

Follow-up to [09-quality-sbc-pilot-results.md](09-quality-sbc-pilot-results.md), which found DUOL (9.24% of the book) falling from Quality 83.2 to 77.3 under an after-SBC FCF/NI. This checks the inputs against the company's SEC filings.

**Source:** the SEC's XBRL "company facts" feed for Duolingo (CIK 0001562088) — structured data tagged by the company in its own 10-K and 10-Qs; each value below carries the accession number of the filing it came from. I did **not** read the filings' narrative text, so the *reason* for the tax item below is inferred from the tags (valuation-allowance change) and should be confirmed in the 10-K's income-tax note before relying on it.

## Verdict

1. **yfinance inputs are verified.** Recomputing from the filings gives SBC = 36.4% of FCF and FCF/NI of about 97% (62% after SBC), the same ratios the pilot got from yfinance (within about 1 percentage point), so the pilot's arithmetic stands.
2. **But the "gate flip" is an artifact, not an SBC effect.** Reported net income is inflated by a **one-time $245.7M income-tax benefit in Q3 2025** (a release of a deferred-tax valuation allowance). Strip it out and FCF/NI is far above 100% even after SBC, so FCF Quality stays at 100 and **DUOL does not move (83.2 stays)**.

## The numbers (USD millions; TTM = twelve months to 2026-06-30)

| Item | FY2024 | FY2025 | H1 2025 | H1 2026 | **TTM** | Filings |
|---|---|---|---|---|---|---|
| Net income (reported) | 88.6 | 414.1 | 79.9 | 76.6 | **410.8** | 10-K 0001628280-26-012494; 10-Q 0001628280-26-053603 |
| Pretax income | — | 182.4 | 81.5 | 100.9 | **201.9** | same |
| Income-tax expense (benefit) | 13.7 | **−231.7** | 1.5 | 24.3 | **−208.9** | same |
| Operating cash flow | 285.5 | 387.8 | 196.3 | 239.0 | **430.5** | same |
| Capex (PP&E) | 12.1 | 18.1 | 2.5 | 7.0 | **22.6** | same |
| Capitalised software | — | 9.2 | 4.3 | n/a (Q1 2.9) | ≈ 10 | 10-K / 10-Qs |
| Stock-based compensation | 110.5 | 137.4 | 65.6 | 72.9 | **144.7** | same |
| **FCF** (OCF − PP&E − cap. software) | | | | | **≈ 398** (±3) | derived |

Q3 2025 detail: net income $292.2M versus pretax $46.4M; income-tax **benefit $245.7M**; valuation-allowance change **−$222.7M** (the tag the benefit is booked under). FY2025 pretax $182.4M versus net income $414.1M.

## FCF/NI under three treatments (TTM, FCF ≈ $398M, SBC $144.7M)

| Net income used | NI | FCF/NI today | (FCF − SBC)/NI | FCF Quality sub-score after SBC | Quality |
|---|---|---|---|---|---|
| Reported (what the pilot used) | 410.8 | 97% | **62%** | 35.9 | 83.2 → **77.3** (gate flip) |
| Pretax income (upper bound for normalised NI) | 201.9 | 197% | **126%** | 100.0 | 83.2 (no change) |
| Pretax × (1 − 24.1% H1-2026 tax rate) | 153.2 | 260% | **165%** | 100.0 | 83.2 (no change) |

(24.1% = H1-2026 tax $24.3M ÷ pretax $100.9M; a normal-tax estimate, not a forecast.)

## What this means

- **DUOL stays above the 80.0 gate** on any normalised net income. The flip in 09 came from dividing by an inflated denominator.
- **The existing metric is also distorted.** Today's FCF/NI for DUOL reads 97% (TTM) and 87% (FY2025) only because of the one-off; on normalised income it is roughly 200–260%. The framework's own Rule 6 ([fair-value-methodology.md](../../framework/fair-value-methodology.md), "Normalize Before You Value") already says to strip one-offs; the FCF/NI sub-score currently doesn't.
- **Design implication for the SBC change:** (FCF − SBC)/NI is sound in principle, but it needs the **normalised-net-income rule** (finding 4 of 09) — at minimum "use net income before one-time tax items such as valuation-allowance releases, and say so" — or it will misfire on any company with a one-off tax line. DUOL is the proof case.
- **SBC itself is real.** SBC is 36% of DUOL's FCF and has risen every year ($95M → $110M → $137M → $145M TTM); it is correctly flagged `elevated` by the advisory block. Normalised, it does not threaten the Quality gate; it does lower the FCF yield used on the Valuation side (5.75% → 3.66%).

## Recommendation

1. Treat the Quality-side SBC change as **safe for DUOL**, conditional on adding the normalised-net-income rule.
2. Keep the Valuation-side SBC change as planned (it affects price, not the gate).
3. Before adoption, confirm the tax item in the 10-K's income-tax note and decide the exact normalisation wording (pretax-based, or tax at a stated rate).
4. Re-run the Quality pilot with normalised net income for the other names whose FY or TTM net income carries a one-off (CSGP and NOW are the obvious ones to check).

## Limits

XBRL tags can mislabel or omit items (capitalised software for Q2 2026 was not in the feed, hence FCF ± $3M). The 24.1% rate is an estimate. One company; the normalisation rule still needs a pilot on the others.

## Glossary

From [framework/glossary.md](../../framework/glossary.md): **SBC (Stock-Based Compensation)**, **FCF/NI conversion ratio**, **Quality Score**, **FCF yield**, **TTM**, **Owner Earnings**.

New terms: **Valuation allowance** — an accounting reserve against deferred tax assets a company doubts it can use; releasing it creates a one-time non-cash tax benefit that inflates reported net income; **Deferred tax asset** — a future tax saving the company has booked (e.g. from past losses); **XBRL** — the machine-readable tagging companies apply to their SEC filings; **Accession number** — the unique ID of one SEC filing; **Normalised net income** — net income after removing one-off items.

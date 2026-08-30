# RESCORE — MercadoLibre, Inc. (MELI) — 2026-08-30

**Task type:** RESCORE, `--both` (default) — **user-initiated `/rescore MELI`**, not a Rule 9-triggered routine run. MELI is **not currently held** ([holdings.md](../portfolio/holdings.md) has no MELI row) — this checks the existing not-in-portfolio watchlist candidate rather than an owned position.
**Date:** 30 Aug 2026

> *Jargon on first use: TTM = trailing twelve months; ROIC = return on invested capital; FCF = free cash flow.*

## 1. Live Price (Rule 0)

**$1,961.22** (IBKR live snapshot, contract 45602025, 2026-08-30), +1.58% vs. prior close $1,930.75. vs. the 2026-08-05 read ($1,840.00): **+6.59%** — real but under the ±15% Rule 9 threshold.

## 2. Rule 9 Trigger Check (2026-08-05 → 2026-08-30) — all 6 categories

| Trigger | Fired? | Detail |
|---|---|---|
| Quarterly earnings | **No** | Q2 2026 (reported 2026-08-05) is still the latest quarter on file. Q3 2026 is not due until MELI's historical early-November reporting window — the "Next review trigger" this ticker's watchlist file itself names. |
| Guidance revision | No | No new revision found since 08-05. |
| Management change | No | Ariel Szarfsztejn has been CEO since 1 Jan 2026 — unchanged. |
| Material M&A | No | None found (WebSearch, no results). |
| Macro shift | No | No discrete new company-specific or macro catalyst in the window. |
| >15% unexplained price move | **No** | +6.59% since 08-05 — real but well under the 15% threshold. |

**No Rule 9 trigger fired.** Since the trailing-twelve-month financial window (Q3 2025–Q2 2026) is therefore unchanged from the 08-05 read — no new 10-Q/8-K has been filed — recomputing the full Quality Score sub-score table from identical inputs would just reproduce the same numbers. Per this ticker's own established precedent (see the 2026-07-10 session, which took the same approach when nothing new had fired), **this is logged as a confirmation check, not a new full re-derivation.**

## 3. Quality Score — confirmed unchanged

**Quality Score: 62.3 — still fails the 80.0+ gate** (third consecutive quarterly read below the gate: 71.2 → 65.7 → 62.3, per [watchlist/not-in-portfolio/MELI/MELI-2026-08-05.md](../watchlist/not-in-portfolio/MELI/MELI-2026-08-05.md) for the full sub-score derivation — Profitability 27.60, Margins ~54.8, Growth 100.0 capped, Balance Sheet ~83–84 range, Moat 80.0, FCF Quality 34.16). No hard disqualifier fires. No Phase 02 valuation work performed — the gate fails before that step, unchanged from every prior read of this ticker.

## 4. Action

**PASS (do not enter)** — unchanged. Nothing about this check changes the standing conclusion.

## Glossary

- **TTM** — Trailing Twelve Months.
- **ROIC** — Return on Invested Capital.
- **FCF** — Free cash flow.

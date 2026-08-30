# RESCORE — Rubrik, Inc. (RBRK) — 2026-08-30

**Task type:** RESCORE — earnings-triggered ([issue #654](https://github.com/Cloxy777/investment-framework/issues/654), Q2 FY2027 results, released 2026-08-27 after close, due 2026-09-01, **P2** — 0.48% weight)
**Date:** 30 Aug 2026

> *Jargon on first use: FCF = free cash flow; ARR = annual recurring revenue.*

## 1. Live Price (Rule 0)

**$92.95** (IBKR live snapshot, contract 699030013, 2026-08-30) — down **−13.15%** vs. prior close $107.02. A large post-earnings reaction (still under the ±15% Rule 9 threshold on its own), notable because the reported headline numbers were positive (Subscription ARR $1.66B +33% YoY, FY2027 revenue guide raised to $1.685B–$1.693B per the earnings release cited in issue #654) — the market's reaction reads as a valuation-multiple reset or a margin/loss-trajectory concern rather than a growth miss, but this session doesn't investigate the sell-off further since it doesn't change the gate outcome below.

## 2. Quality Score — hard disqualifier fires, no weighted score computed

Fresh FY2026 annuals (stockanalysis.com):

```
Total Revenue: FY2023 $599.82M → FY2024 $627.89M → FY2025 $886.54M → FY2026 $1,316M  (strong growth)
Net Income:    FY2024 −$354.16M | FY2025 −$1,155M | FY2026 −$348.83M   (net loss every year)
Operating Income (EBIT): FY2024 −$306.51M | FY2025 −$1,134M | FY2026 −$345.42M   (operating loss every year)
Free Cash Flow: FY2024 −$16.85M | FY2025 +$31.34M | FY2026 +$253.28M
Gross Margin (FY2026): 80.10%
```

**Hard disqualifier check ([quality-scoring.md](../framework/quality-scoring.md)):** *"Not FCF-positive for 3+ consecutive years"* fires — the current rolling 3-year window (FY2024–FY2026, per the [2026-08-05 rolling-window clarification](../decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md)) contains FY2024's **negative** FCF (−$16.85M), so only 2 of the last 3 years are FCF-positive, not 3+. **This disqualifies RBRK from the Quality Score gate regardless of its other metrics** — per the framework's explicit rule, a hard disqualifier fails a company "regardless of weighted score," so no Profitability/Margins/Growth/Balance-Sheet/Moat/FCF-Quality sub-scores are computed this session.

Independently, RBRK's Net Margin is negative every year on record — it would also fail Phase 01's original binary profitability filters (>12% net margin, >15% ROIC) outright, a second, independent reason it isn't eligible.

**Not eligible for Phase 02 valuation scoring or a Composite Score.** Status unchanged from the last review (Jun 2026, "not scored — fails quality gates") — this earnings release doesn't change that, though it's now current data rather than stale.

## 3. Action

RBRK is a small (0.48%) existing holding carrying "not scored — fails quality gates" status. This rescore confirms that status is current, not stale. No trim/exit trigger applies mechanically from a quality-gate fail alone (this framework's Phase 06 exit triggers are about thesis breaks/fundamental deterioration in a name that was scored, not a blanket rule to exit every quality-gate-fail holding) — but a persistently unprofitable, disqualified-by-hard-rule name at a small weight is worth a deliberate keep/exit decision from the user rather than default inertia, especially after a −13% single-day reaction. **Flagged for the user's judgment; not a framework-mandated trim/exit.**

## Glossary

- **FCF** — Free cash flow.
- **ARR (Annual Recurring Revenue)** — the annualized run-rate of subscription revenue at a point in time.

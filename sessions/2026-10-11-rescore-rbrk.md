# RESCORE — Rubrik, Inc. (RBRK) — 2026-10-11

**Task type:** RESCORE (mode `--both`) — Rule 9 trigger: **+15.6% single-day move on 2026-09-14** with no earnings catalyst ([issue #801](https://github.com/Cloxy777/investment-framework/issues/801), due 2026-09-17, 24 days overdue at this session)
**Date:** 2026-10-11 (Sunday — prices are the 2026-10-09 Friday close)
**Last review on record:** not scored — fails quality gates (hard disqualifier), [2026-08-30](2026-08-30-rescore-rbrk.md)
**Weight:** 0.55% (2026-10-11 sync). Held outside the framework (fails Phase 01); **no `override-log.md` entry exists** (re-flagged, not resolved here).

## 1. Live Price (Rule 0)

**$125.14** — IBKR `get_price_history` (contract 699030013) daily close 2026-10-09; equals `yfinance` `currentPrice`. Market cap $20,142M (160,956,763 sh). 52-week range $42.25–$127.90. Analyst PT mean $120.15 / median $120 / range $110–$139 (n=27) — the stock trades *above* the mean target. vs. 2026-08-30 ($92.95): **+34.6%**.

## 2. Rule 9 Trigger Check (2026-08-30 → 2026-10-11)

| Trigger | Found? | Detail |
|---|---|---|
| Earnings | No | Q2 FY2027 was scored 08-30; next print 2026-12-03. |
| Guidance / M&A / management | None found | |
| **>15% move** | **Yes — issue #801** | 2026-09-14: $86.65 → $100.20 (**+15.6%**). Cause (cited, secondary): sector-wide cybersecurity rally the same day after a weekend AI-risk article from Anthropic's CEO; peers rose similarly ([Motley Fool, 2026-09-14](https://www.fool.com/investing/2026/09/14/why-rubrik-stock-soared-15-today/)). A sentiment move, not a Rubrik fundamental. Some search snippets about a "Sept 9" Rubrik result were internally inconsistent and were **not** relied on. |

Resolved as sector-driven; no fundamental change.

## 3. Quality Score — hard disqualifier still fires

Fiscal year ends 31 Jan; the latest completed years are FY2024–FY2026 (FY2027 ends Jan 2027, reports ~Mar 2027).

```
Free Cash Flow (yfinance annual):  FY2024 −$24.5M | FY2025 +$21.6M | FY2026 +$237.8M
(08-30 session used stockanalysis.com: −$16.9M / +$31.3M / +$253.3M — different definition, same signs)
```
"Not FCF-positive for 3+ consecutive years" on the current rolling window ([2026-08-05 clarification](../decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md)): FY2024 is negative → **fires**. Nothing in the window changed since 08-30.

**Independent confirmation — the weighted score cannot reach the gate even in the best case:**

| Sub-score | Value | Basis |
|---|---|---|
| Profitability | 0.0 | Net margin −16.5% (`profitMargins` −0.16498), TTM EBITDA −$263M, ROIC negative → both components floored |
| Margins | 100.0 | Gross margin 80.2% (≥80% → 100) |
| Growth | 100.0 | Revenue CAGR FY2023 $599.82M → FY2026 $1,316.19M = 29.95% (≥25% → 100) |
| Balance Sheet | 100.0 | Net cash: cash $1,747.6M vs. debt $1,149.6M (EBITDA negative; net cash scored as best case) |
| Moat | not evidenced | Upper bound 100.0 assumed |
| FCF Quality | 0.0 | FCF/NI undefined with negative NI → floored |

```
Maximum possible Quality Score = 0×0.25 + 100×0.15 + 100×0.20 + 100×0.15 + 100(max)×0.15 + 0×0.10 = 65.0
```
**65.0 < 80.0 — fails the gate even if every unevidenced moat signal were granted.** No Moat research was done (no cited sources; none would change the outcome). No Phase 02 Valuation Score or Composite Score is computed — the gate blocks it. The Rate Environment Gate is not run for the same reason.

## 4. Action

**Status unchanged: "not scored — fails quality gates." HOLD/WATCH; no add, no framework-mandated trim/exit.** The position (3 sh, +115% on $58.10 avg cost) has more than doubled; the stock now trades above the analyst mean PT with a negative GAAP profile, so a deliberate keep/trim/exit decision is the user's (not a framework trigger). Fixing the missing `override-log.md` entry remains the governance gap.

## 5. Next Review Trigger

- Q3 FY2027 earnings, 2026-12-03.
- **FY2027 results (~Mar 2027):** the rolling FCF window becomes FY2025–FY2027. If FY2027 FCF is positive, the *FCF-positive* hard disqualifier **clears** — but Quality would still be capped by negative net margin/ROIC (maximum ≈65), so the name stays out unless GAAP profitability arrives.
- Issue #801 can be closed (rescore done).

---

## Glossary

| Term | Meaning |
|---|---|
| **Rule 9** | Framework rule forcing a re-score after earnings, guidance change, M&A, management change, macro shift, or a >15% unexplained price move. |
| **Hard disqualifier** | A Quality condition that fails a company regardless of the weighted score. |
| **Rolling window** | Trailing-year tests use the most recently completed fiscal years at scoring time, so old failures age out. |
| **FCF** | Free cash flow: operating cash flow minus capital spending. |
| **Quality Score / 80.0+ gate** | 0–100 business-quality score; 80.0 needed to be valued/scored. |
| **Net margin / ROIC** | Profit ÷ revenue; after-tax operating profit ÷ capital invested. |
| **Human Override** | Position held outside the framework's rules, tracked in `override-log.md`. |

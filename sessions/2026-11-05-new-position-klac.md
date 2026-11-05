# NEW POSITION — KLAC (KLA Corporation) — 2026-11-05

**Result: Phase 01 FAIL — Quality Score 66.4 < 80.0 gate. PASS (no entry). Valuation, Composite and order setup NOT run.**

Why this ticker: picked as the most promising of a "quality names that fell hard this week" IBKR screen (US, cap >$20B, operating margin >15%, revenue growth >8%, MTD < −7%; 57 matches). Chip-equipment names were expected to have the best FCF durability. The screen could not give a true 1-week change (IBKR 1w field empty), so month-to-date was used.

## Live price (Rule 0)
IBKR snapshot: **$134.63** (bid 134.61 / ask 134.70), **−10.12% on the day**, 13w high 214.80, 52w high 307.37 (split-adjusted; 10-for-1 split June 2026). Sector-wide chip sell-off (SOX ≈ −8.9% on 2026-11-05 per a Stock Preachers PR on finviz). No KLA-specific cause found, so no Rule 9 trigger.

## Inputs
10Y Treasury (Yahoo ^TNX close 2026-11-05): **4.831%** (not used — valuation not reached).

`fetch_fundamentals KLAC` output:
```
Market Cap 175,482,978,304 | EV 196,422,189,056 | Shares 1,302,962,435
Forward PE 18.972 | FCF Yield 2.301% | EV/EBIT 30.682
Net Margin 36.250% | Gross Margin 61.465% | ROIC 44.945% (tax 0.1409, NOPAT 5.50B, InvCap 12.24B)
Revenue 3yr CAGR 8.965% | Net Debt/EBITDA 0.644 (EBITDA TTM 6.58B)
FCF/NI TTM 76.785% | (FCF-SBC)/NI TTM 70.623% | SBC yield 0.185% | Gross buyback yield 1.527%
FCF/NI annual (oldest first) [98.3, 109.8, 92.2, 78.0] | FCF positive 3yr+ True
5yr PE avg/low/high 26.494 / 12.620 / 47.840 (n=20 quarters)
SBC TTM 324.1M | FCF TTM 4,037.6M | SBC/FCF 8.0% | FCF yield after SBC 2.12%
cycle_peak UNKNOWN (EPS history unavailable) | value_trap_candidate UNKNOWN (trailing EPS growth unavailable)
```
`flags_common --forward-pe 18.972 --eps-growth 23.1` (consensus next-year EPS growth 23.1%, Yahoo): `multiple_ceiling NONE`. cycle_peak and value_trap stay `UNKNOWN` — **data gaps**, no effect because the gate failed first.

Company cross-check (KLA FQ1'27 release, SEC 8-K Ex.99.1, 2026-10-28): TTM FCF $4,037.6M matches the script; quarterly SBC $84.1M; revenue $4.136B (+13% q/q, +29% y/y); GAAP net income $1.549B; buybacks $2.68B TTM; dividends $1.11B TTM; long-term debt $5.72B; cash + securities $4.74B; services $850.5M (20.6% of revenue); FQ2 guide $4.7B ± $0.2B.

## Quality Score (script output)
```
Profitability: NetMargin 100.00, ROIC 100.00 -> 100.00
Margins: GrossMargin_Score = (61.465/80)x100 = 76.83
Growth: (8.965/25)x100 = 35.86; +10 TAM evidence -> 45.86
Balance Sheet: 100x(1 - 0.644/4) = 83.90
Moat: switching costs TRUE only -> (1/5)x100 = 20.00
FCF Quality: ((0.7062-0.40)/0.60)x100 = 51.04
Quality = (100x0.25)+(76.83x0.15)+(45.86x0.20)+(83.90x0.15)+(20.00x0.15)+(51.04x0.10) = 66.386 -> 66.4
# Quality Score = 66.4 — FAILS the 80.0+ gate
```
Moat evidence: switching costs TRUE (service revenue $850.5M = 20.6% of FQ1'27 revenue; deferred service revenue $634.2M current + $230.6M non-current; 17 consecutive years of services growth — SEC Ex.99.1 and securities.io, 2026-10-28). Market share, brand premium and scale cost advantage are FALSE only because **no cited source was found** (data gaps; no process-control share figure appears in the release or the shareholder-letter coverage). TAM +10 cited: CY2026 WFE ~mid-$150B, CY2027 > $200B; advanced-packaging process control ≈ $1.1B CY2026, >70% y/y (securities.io, relaying the shareholder letter).

**Robustness:** the failure does not depend on the moat data gaps. Crediting all five moat signals adds 12 points (80 × 0.15) → ≈78.4, still below 80.0 (hand calculation). The binding weakness is the growth sub-score: 3-year revenue CAGR 8.97% (below the >10% threshold) even though the current run-rate (+29% y/y) is far stronger. The window rolls forward, so KLAC may clear this once FY2027 replaces an older year. No hard disqualifier fired (FCF/NI ≥ 78% every year, Net Debt/EBITDA 0.64×, SBC/FCF 8%).

## Recommendation
**PASS — do not open a position; watchlist-track for a Quality re-check.** Gate not met, so Phase 02 valuation, the Composite Score and `order_setup` were not run (stop per Step 2). The 10% one-day drop is a sector-wide move with no KLA fundamental event; the framework acts on score changes or fundamental events, not price.

Observations (not scored): forward PE 19.0× vs 5yr average 26.5×, but FCF yield only 2.3% and EV/EBIT 30.7× — cheap on forward earnings, expensive on trailing cash flow, typical of a cycle upswing.

## Process notes
- `python -m scripts.stale_score --apply` returned `newly_stale: []`, `resolved: []` (KLAC had no stale mark). It also appended a stray duplicate header row to `watchlist/STALE.md`; that edit was reverted and not committed (script quirk worth a separate look).
- `watchlist_diff` with identical old/new values returns `append`, not `new_file`, for a first entry; used old `NOT SCORED` → new `PHASE 01 FAIL` to get `new_file` (same convention as the CAP entry).

## Follow-ups
- Re-run `/new-position KLAC` after FQ2'27 results (late January 2027), and source a cited process-control share figure and 3-yr gross-margin history (both missing here).
- AMAT and LRCX from the same screen are untested.

## Glossary
See [framework/glossary.md](../framework/glossary.md): **Quality Score**, **Phase 01 (Universe Screening / quality gate)**, **Hard disqualifier**, **Moat**, **FCF yield**, **EV/EBIT**, **Forward PE**, **SBC**, **Net Debt/EBITDA**, **ROIC**, **WFE (Wafer Fab Equipment)** *(new)*, **Process control (semiconductors)** *(new)*.

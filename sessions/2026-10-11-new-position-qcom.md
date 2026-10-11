# NEW POSITION — QCOM (Qualcomm) — 2026-10-11

**Task type:** NEW POSITION (re-evaluation; third `/new-position` pass on QCOM)
**Date:** 2026-10-11
**10Y US Treasury yield / Rate Regime Modifier:** not fetched or applied — evaluation stops at the Phase 01 gate before the Rate Environment Gate applies (same precedent as the 2026-07-24 and 2026-09-08 QCOM sessions).
**Held?** No (confirmed: QCOM absent from `portfolio/holdings.md`). Prior entries: 2026-07-24 (Quality 60.3, FAIL), 2026-09-08 (Quality 56.9, FAIL).

## 1. Live price (Rule 0)

IBKR snapshot, contract_id 273544 (NASDAQ): **last $175.40**, prior close $176.01 (−0.35%); 52-week high $258.95, low $121.52. Feed status `FROZEN` (market closed — Sunday), so this is the last regular-session price. Valid for a no-action gate result; would need refreshing before any order.

## 2. Data gaps / sourcing notes

- No new quarterly earnings since 2026-09-08. Qualcomm's fiscal Q4 FY2026 report date is **not confirmed**: sources conflict (Earnings Whispers: Oct 28; Unusual Whales: Nov 4; TipRanks est.: Nov 11). Treated as "late Oct–mid Nov, TBC".
- One web search for post-2026-09-08 news returned nothing new on share, pricing, or AWS revenue. Qualitative moat/TAM evidence is therefore carried forward unchanged from the 2026-09-08 session (see that log for the full citations); this is flagged, not re-verified from fresh primary sources.
- **Method difference vs. 2026-09-08:** this run computes inputs with `scripts.fetch_fundamentals`, which derives ROIC as NOPAT ÷ invested capital = 27.29% (NOPAT $9,828M / InvCap $36,017M), versus 24.37% hand-computed last session from different NOPAT/capital components. Net debt/EBITDA is likewise 0.774× (vs 0.591×). The ~0.5-point Quality Score difference below is mostly this method/data-vintage difference, not a fundamental change. The gate result is unaffected.

## 3. Fundamentals — `python -m scripts.fetch_fundamentals QCOM` (verbatim)

## Fundamentals — QCOM

```
Market Cap            = 187,405,828,096
Enterprise Value      = 191,282,053,120
Shares Outstanding    = 1,067,839,507
Forward PE            = 17.212
FCF Yield %           = 5.558
EV/EBIT               = 16.073
Net Margin %          = 21.010
Gross Margin %        = 54.226
ROIC % (NOPAT/InvCap) = 27.287  [tax_rate=0.1742, NOPAT=9,827,984,213, InvestedCapital=36,017,000,000]
Revenue 3yr CAGR %    = 0.063
Net Debt/EBITDA       = 0.774  [EBITDA_ttm=11,998,999,552]
FCF/NI TTM %          = 112.496
FCF/NI annual (oldest first) = [52.8%, 136.2%, 110.0%, 231.4%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 13.381 / 7.577 / 18.828  (n=20 quarters)
```

## 4. Quality Score — `python -m scripts.scoring.quality_score` (verbatim)

Manual fields supplied: `tam_expansion_evidence` true (Amazon/AWS 8-K + Automotive/IoT growth, per 2026-09-08 session), `growth_decelerating_evidence` false, `gross_margin_structural_trend` false, moat signals 1/5 true (switching costs only), `asset_light_override` false.

## Quality Score

**Profitability (25%)**
```
NetMargin_Component = clamp((21.01/30)x100) = 70.03
ROIC_Component = clamp((27.287/30)x100) = 90.96
Profitability_Score = (70.03 + 90.96) / 2 = 80.50
```
**Margins (15%)**
```
GrossMargin_Score = clamp((54.226/80)x100) = 67.78
```
**Growth (20%)**
```
Growth_Score = clamp((0.063/25)x100) = 0.25
+10 TAM/pricing-power evidence: Amazon/AWS multi-generational custom AI-inference-chip and optical-connectivity collaboration (Qualcomm SEC Form 8-K Item 3.02, filed 2026-09-08; warrant for up to 25M shares at $161.26 vesting against up to $60B purchases); Automotive +61% YoY and IoT +9% YoY in Q3 FY2026 (Qualcomm Q3 FY2026 results, 2026-07-29). No disclosed data-center revenue yet.
Growth_Score (final, clamped) = 10.25
```
**Balance Sheet (15%)**
```
BalanceSheet_Score = clamp(100x(1 - 0.774/4)) = 80.65
```
**Moat Signal (15%)**
```
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | False | Counterpoint: global smartphone chipset share 27% (Q1 2025) -> 23% (Q1 2026) vs MediaTek 32%; no reversal found (2026-09-08 session). |
| brand_premium | False | Sept 1 2026 price increase framed as supply-cost pass-through, not volume-loss-free pricing power (AndroidAuthority). |
| network_effect | False | Not applicable to chip design/licensing business. |
| switching_costs | True | SEP 'no license, no chips' patent licensing model; Ninth Circuit 2020 ruling. |
| scale_cost_advantage | False | MediaTek is the unit-volume leader (32% vs 23%); no documented per-unit cost gap in QCOM's favor. |
Moat_Score = (1/5) x 100 = 20.00
```
**FCF Quality (10%)**
```
FCFQuality_Score = clamp(((1.1250 - 0.40)/0.60)x100) = 100.00
```
**Quality Score — Final**
```
Quality Score = (80.50x0.25) + (67.78x0.15) + (10.25x0.20) + (80.65x0.15) + (20.00x0.15) + (100.00x0.10)
= 57.439 -> rounds to 57.4
```

# Quality Score = 57.4 — FAILS the 80.0+ gate

**Hard disqualifiers:** none fired (script ran to completion). Net debt/EBITDA 0.774× < 2.5×; FCF/NI annual [52.8, 136.2, 110.0, 231.4]% — only the oldest year is <70%, not 2 consecutive recent years; FCF positive 3yr+.

## 5. Gate result

**Quality Score 57.4 < 80.0 — FAILS the gate by 22.6 points.** Moves vs. prior sessions: 60.3 → 56.9 → 57.4. Drivers are unchanged: Growth 10.25 (3yr revenue CAGR +0.06%, only the +10 diversification modifier) and Moat 20.0 (1/5 signals, smartphone chipset share still declining 27%→23% vs MediaTek 32%). Sensitivity (same as prior sessions): crediting all 5 moat signals adds 12.0 points → ~69.4, still below 80.0. The miss is decisive under any defensible reading.

Per the command, **stopped here**: no Rate Environment Gate, valuation score, composite score, fair value or order setup was run.

## 6. Recommendation

**PASS (watchlist-only, no order).** QCOM does not clear Phase 01. Nothing changed that would justify reopening: no earnings, no new filed evidence. No trade; no `decisions/` entry.

## 7. Next review trigger

Qualcomm fiscal Q4 FY2026 earnings (date TBC, late Oct–mid Nov 2026) — mandatory Rule 9 re-check. Paths to a different result: (1) Sept 1 price increases restoring operating margin; (2) binding AWS purchase orders or disclosed Data Center revenue (Growth, and possibly a Moat signal once demonstrated); (3) evidence of stabilizing smartphone-chipset unit share. Also: guidance revision, management change, material M&A, or >15% unexplained price move.

## 8. Watchlist / stale-score

- `python -m scripts.watchlist_diff` → `append` (no significant change: still "not scored"/PASS category). Line appended to `watchlist/not-in-portfolio/QCOM/QCOM-2026-09-08.md`.
- `python -m scripts.stale_score --apply` →
```json
{
  "version": "2026-06-29",
  "newly_stale": [],
  "resolved": []
}
```
QCOM was not in the resolved list (no stale mark existed — it has no numeric valuation score).

## Glossary

- **Quality Score**: This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. See [quality-scoring.md](quality-scoring.md).
- **ROIC**: Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Moat**: Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Rule 0**: This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9**: This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TTM (Trailing Twelve Months)**: The most recent 12 months of reported financial results (the last four quarters added together), as opposed to a single fiscal year or a forward-looking estimate. *(New term.)*
- **Net Margin**: Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax. One of this framework's Quality Score Profitability sub-score inputs (alongside ROIC).
- **Net Debt/EBITDA**: Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **TAM**: Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **CAGR**: Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **FCF/NI conversion ratio**: Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. A low ratio without a CapEx explanation is a red flag for earnings-quality games (see the Valeant/Wirecard cases in [graveyard-audit.md](graveyard-audit.md)).
- **Phase 01 (Universe Screening / quality gate)**: The first of the framework's six phases: a company must score 80.0+ on the Quality Score before any valuation scoring (Phase 02) or entry is considered. A "Phase 01 FAIL" means the company never reaches valuation. *(New term.)*
- **SEP (Standard-Essential Patent)**: A patent covering technology that anyone implementing an industry standard (e.g. 4G/5G) unavoidably uses; the basis of Qualcomm's "no license, no chips" licensing model, credited as its one TRUE Moat signal (switching costs). *(New term.)*
- **Rate Environment Gate**: The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier.
- **8-K**: The "current report" a US public company must file with the SEC within days of a material event — most commonly used to furnish (via an attached exhibit, typically "Exhibit 99.1") a quarterly earnings press release ahead of the fuller, audited 10-Q/10-K that follows weeks later. Apple's fiscal Q3 2026 results were sourced from its 30 July 2026 8-K (Exhibit 99.1) in this framework's 2026-07-31 AAPL session, since the corresponding 10-Q had not yet been filed. *(New term.)*
- **Gross Margin**: Gross Profit (Revenue − Cost of Revenue) ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs, before operating expenses like R&D and sales & marketing. One of this framework's Quality Score Margins sub-score inputs.

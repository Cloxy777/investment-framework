# New Position Evaluation — SBGSY (Schneider Electric S.E., unsponsored ADR)

**Task type:** NEW POSITION
**Date:** 2026-09-10
**Ticker:** SBGSY — OTC Pink, unsponsored ADR of Schneider Electric S.E. (primary listing: Euronext Paris, SU.PA)
**Sector:** Industrials — Electrical Equipment / Energy Management & Industrial Automation
**Quality Score methodology version:** 2026-06-29 (current)

## 1. Data gaps flagged

None — all required Quality Score inputs sourced live. Moat Signal evidence gathered for only 2 of 5 checklist items; the remaining 3 are marked FALSE for lack of a citable source (not treated as a gap requiring a stop, per the framework's "never mark a signal true without a cited source" rule — absence of evidence just scores that signal 0).

## 2. Live price (Rule 0)

Fetched live via IBKR (contract_id 59651182, PINK exchange), not inferred from any valuation multiple:

| Field | Value |
|---|---|
| Last price | **$66.44** |
| Bid / Ask | $66.42 / $66.62 |
| Prior close | $67.42 |
| Change | −$0.98 (−1.45%) |
| Volume (day) | 194,841 |
| 52-week range | $49.82 – $71.98 |

Note: SBGSY is an **unsponsored** ADR (see Glossary) — no company-provided SEC filings; underlying company (Schneider Electric S.E.) reports in EUR on Euronext Paris. Fundamentals below are sourced in EUR from the underlying ordinary shares (EPA:SU) and are directly usable for the Quality Score since every sub-score in this section is a ratio/percentage (currency-neutral), not a price.

## 3. Phase 01 — Quality Score (gate: 80.0+ required to proceed)

**Inputs (TTM / FY2025 unless noted, source: stockanalysis.com financial statements for EPA:SU, cross-checked against reported FY2021–2025 income statement):**

| Metric | Value | Source |
|---|---|---|
| Net Margin (FY2025) | 10.37% | Net income €4,163M ÷ Revenue €40,152M |
| ROIC (TTM) | 13.96% | stockanalysis.com ratios |
| Gross Margin (FY2025) | 42.08% | Gross profit €16,895M ÷ Revenue €40,152M |
| Revenue 3yr CAGR (FY2022→FY2025) | 5.52% | (€40,152M / €34,176M)^(1/3) − 1 |
| Net Debt/EBITDA (current) | 1.91× | stockanalysis.com ratios (Net debt €15,275M FY2025) |
| FCF/NI conversion (FY2025) | 121.5% | FCF €5,059M ÷ NI €4,163M |
| FCF-positive years | 5 of 5 (FY2021–2025) | stockanalysis.com cash flow statement |

**Hard disqualifier check — none fire:**
- FCF/NI ≥70% every year shown (121.5% FY2025) → clear
- Net Debt/EBITDA 1.91× < 2.5× standard threshold (not asset-light) → clear
- FCF-positive 5 consecutive years, not 3+ negative → clear

### Sub-scores

**Profitability (25% weight):**
```
NetMargin_Component = clamp((10.37/30)×100, 0, 100) = 34.6
ROIC_Component       = clamp((13.96/30)×100, 0, 100) = 46.5
Profitability_Score  = (34.6 + 46.5) / 2 = 40.6   (no FCF cap — 5yr positive)
```

**Margins (15% weight):**
```
GrossMargin_Score = clamp((42.08/80)×100, 0, 100) = 52.6
```
No structural-trend bonus applies — the bonus is only for margin *below* 40% that's expanding; 42.08% is already above the 40% threshold.

**Growth (20% weight):**
```
Growth_Score (raw) = clamp((5.52/25)×100, 0, 100) = 22.1
```
TAM/pricing-power modifier: **+10**, documented. Schneider Electric is the disclosed market leader in the data-center power market (marketsandmarkets.com competitive landscape: Schneider Electric ranked #1 ahead of Vertiv, ABB, Eaton, Delta Electronics), and H1 2026 organic revenue growth accelerated to +14% (Energy Management segment +17.7% organic in Q2 2026), driven by data-center, AI-infrastructure, and grid-electrification demand — a structural TAM-expansion driver, not a one-off. No decelerating-growth evidence found to offset it.
```
Growth_Score = 22.1 + 10 = 32.1
```

**Balance Sheet (15% weight):**
```
BalanceSheet_Score = clamp(100 × (1 − 1.91/4), 0, 100) = 52.25 ≈ 52.3
```
Standard (/4) denominator — Schneider is an industrial manufacturer, not an asset-light financial; Upgrade 5 override doesn't apply.

**Moat Signal (15% weight):**

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | marketsandmarkets.com: Schneider Electric ranked #1 in the data-center power market (ahead of Vertiv, ABB, Eaton, Delta); Energy Management organic growth +17.7% (Q2 2026) shows share gain in its fastest-growing end market |
| Brand premium | FALSE | No cited pricing-power-without-volume-loss evidence found |
| Network effect | FALSE | Not applicable to this business model — no two-sided marketplace dynamic |
| Switching costs | **TRUE** | EcoStruxure is a proprietary, deeply-integrated digital platform (UPS, PDUs, switchgear, digital twins/AI alarm management) wired into customer data-center and industrial infrastructure — high migration cost to rip out once installed |
| Scale cost advantage | FALSE | No cited cost-per-unit data vs. smaller competitors |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10% weight):**
```
FCFQuality_Score = clamp(((1.215 − 0.40)/0.60)×100, 0, 100) = clamp(135.8, 0, 100) = 100.0
```

### Final Quality Score

```
Quality Score = (40.6×0.25) + (52.6×0.15) + (32.1×0.20) + (52.3×0.15) + (40.0×0.15) + (100.0×0.10)
              = 10.15 + 7.89 + 6.42 + 7.85 + 6.00 + 10.00
              = 48.3
```

**48.3 < 80.0 — fails the Quality Score gate.**

## 4. Recommendation

**PASS — do not proceed to Phase 02 valuation scoring.** Per the strict 80.0+ quality gate (quality-scoring.md), a company below the gate stops here regardless of how cheap the stock might look on a valuation basis — the Rate Environment Gate and full Phase 02 valuation score are not run. Schneider Electric is a real, profitable, growing industrial franchise with a genuine data-center/electrification tailwind and a clean balance sheet, but its financial profile (net margin ~10%, revenue growth ~5.5%, only 2 of 5 documented Moat signals) doesn't clear this framework's deliberately strict quality bar, driven mainly by the Profitability (40.6), Growth (32.1), and Moat (40.0) sub-scores.

**Additional risk note (not scored, informational):** SBGSY itself is an *unsponsored* OTC Pink ADR with no company-provided SEC reporting and materially lower liquidity than the underlying EPA:SU shares — a data-sourcing/liquidity caveat that would apply even if the Quality Score had cleared the gate.

## 5. Next review trigger

Re-score if: a fundamental event changes the profile materially (M&A, large margin-accretive restructuring, a step-change in growth), **or** on the next `/screen` pass that resurfaces it, **or** no earlier than the next full portfolio review cycle. Not a "never revisit" — a name with genuine share gains in a real secular tailwind (AI-driven data-center power demand) is worth re-checking if margins/growth inflect.

## Glossary

- **ADR (American Depositary Receipt)** — a US-exchange-listed security representing shares of a non-US company, letting US investors trade it in USD without using a foreign exchange directly.
- **Sponsored ADR / Unsponsored ADR** — an unsponsored ADR is created unilaterally by a depositary bank without the underlying company's involvement, typically thinly traded and carrying no company-provided SEC reporting; SBGSY is unsponsored.
- **OTC Pink Sheets (OTC Markets, Pink tier)** — the lowest, most lightly-regulated OTC quotation tier: thin volume, wide/absent spreads, no exchange listing standards.
- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate from a start value to an end value over several years.
- **ROIC** — Return on Invested Capital: how efficiently a company turns the capital invested in it (debt + equity) into profit.
- **Net Margin** — Net Income ÷ Revenue.
- **Gross Margin** — Gross Profit ÷ Revenue, the share of each revenue dollar left after direct production/delivery costs.
- **Net Debt/EBITDA** — net debt divided by EBITDA, a leverage ratio measuring years of operating cash profit needed to pay off all debt.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, checking whether reported accounting profit is turning into real cash.
- **Moat Signal** — this framework's 5-point Quality Score checklist (market share, brand premium, network effect, switching costs, scale cost advantage), each markable TRUE only against a cited source.
- **TAM** — Total Addressable Market, the total revenue opportunity if a company captured 100% of its target market.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted sub-score total, independent of the continuous score.
- **Quality Score** — this framework's 0.0–100.0 continuous score grading profitability, margins, growth, balance sheet, moat, and FCF quality; a company must score 80.0+ to proceed to Phase 02 valuation scoring at all.

# NEW POSITION — PDD Holdings (PDD) — 2026-08-26

**Task type:** NEW POSITION (candidate evaluation, not currently held)
**Source:** EM screening slice, 2026-08-25 ([issue #630](https://github.com/Cloxy777/investment-framework/issues/630), [session](2026-08-25-screening-emerging-markets.md)) — clean 8/8 Phase 01 quantitative pass, carried forward from the 2026-08-04 EM round.
**Date:** 26 Aug 2026

> *Jargon decoded on first use: FCF = free cash flow; ROIC = return on invested capital; ROCE = return on capital employed (a close cousin of ROIC, sometimes disclosed instead of it); EV/EBIT = enterprise value ÷ operating profit; CAGR = compound annual growth rate; TAM = total addressable market; PE = price-to-earnings ratio; EPS = earnings per share; ADR = American Depositary Receipt.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$86.07** | Google Finance, intraday quote, 2026-08-26 12:49:10 PM GMT-4 (ET) |
| Cross-check | $86.94 (down 0.92% intraday), 52-week range $71.94–$139.41 | stockanalysis.com WebFetch, same day |
| Analyst consensus PT | $116.06 (37 analysts, "Buy") — bull-case sanity check only, not used in scoring | stockanalysis.com |

PDD trades as a Nasdaq ADR (underlying: Pinduoduo Inc., Chinese e-commerce). Financial statements sourced in CNY (per stockanalysis.com); price and market cap in USD. Not held in the current portfolio (IBKR or Freedom24) — no live snapshot cross-check against a broker position was applicable.

---

## 2. Phase 01 Quality Score ([quality-scoring.md](../framework/quality-scoring.md))

Quantitative inputs (FY2025, i.e. fiscal year ended 2025) and qualitative evidence carried forward from the 2026-08-25 EM screening session's Step 2–3 (verified there against stockanalysis.com's financials/ratios/cash-flow pages and independent news sourcing; re-confirmed current as of today, no new fiscal quarter has reported since):

```
Net Margin (TTM/FY25):        22.66%
ROIC (ROCE proxy, FY25):      22.40%   (stockanalysis.com does not separately publish ROIC for PDD — ROCE used per the framework's documented "ROE/ROIC/ROCE, whichever the source publishes" allowance)
Gross Margin (FY25):          56.28%   (3yr trend not independently re-verified this session — no bonus applied, not invented)
Revenue 3yr CAGR (FY22→FY25): 48.996%  — (431,846/130,558)^(1/3)−1, CNY millions
Net Debt/EBITDA (FY25):       −4.45x   (net cash position)
FCF positive 3yr:             Yes — FY25 CNY 105,794M / FY24 120,962M / FY23 93,579M (all positive, though declining YoY)
FCF/NI ratio (FY25):          105,794 / 97,843 = 108.1%
FCF/NI ratio (FY24):          120,962 / 112,435 = 107.6%
```

**Hard disqualifiers check:** FCF/NI ratio is >100% in both of the last 2 fiscal years (no <70% breach) — clear. Net Debt/EBITDA is deeply negative (net cash) — clear. FCF-positive 3+ consecutive years — clear. **No hard disqualifier fires.**

### Sub-scores

**Profitability (25% weight):**
```
NetMargin_Component = clamp((22.66/30)×100, 0, 100) = 75.53
ROIC_Component       = clamp((22.40/30)×100, 0, 100) = 74.67
Profitability_Score  = (75.53 + 74.67) / 2 = 75.10   (no FCF cap — 3yr positive)
```

**Margins (15% weight):**
```
GrossMargin_Score = clamp((56.28/80)×100, 0, 100) = 70.35
```
No structural-expansion bonus applied — this session did not independently re-verify a 3-year gross-margin trend beyond the single FY25 figure carried from the screening session, and the framework's "never invent" rule means no bonus is assumed without a cited multi-year trend.

**Growth (20% weight):**
```
Growth_Score (raw) = clamp((48.996/25)×100, 0, 100) = 100.0 (capped)
```
**Structural deceleration modifier: −10.** The 2026-08-25 screening session's qualitative pass documented, with cited sources (BNN Bloomberg, Bloomberg, Caixin Global — PDD's own Q2 2026 results commentary), that PDD's revenue growth rate has decelerated from 86% YoY (Q2 2024) to 8% YoY (Q2 2026) — a structural deceleration in the core business, not a cyclical blip, coinciding with intensifying domestic competition (Alibaba/JD/Douyin all pushing into the same ground, a June 2026 Daito Research note downgrading all three China e-commerce names together) and confirmed international demand erosion (Temu global MAU −11% YoY, DAU −13%, July 2026 downloads −48% YoY). This is exactly the kind of documented, cited deceleration the modifier is meant to capture — the trailing 48.996% CAGR is a historical artifact of PDD's earlier hyper-growth phase, not a forward-looking signal.
```
Growth_Score = clamp(100.0 − 10, 0, 100) = 90.0
```

**Balance Sheet (15% weight):**
```
BalanceSheet_Score = clamp(100 × (1 − (−4.45)/4), 0, 100) = clamp(211.25, 0, 100) = 100.0
```

**Moat Signal (15% weight)** — checklist, each signal markable TRUE only against a cited source (per [quality-scoring.md](../framework/quality-scoring.md)):

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **FALSE** | No cited domestic market-share *trend* figure (this session's sourced material gives a buyer-count level, not a trend). What *is* cited points the other way for the international (Temu) side of the business: MAU −11% YoY, DAU −13% YoY, July 2026 downloads −48% YoY. Domestically, PDD is described as under active, intensifying competitive pressure (peer-group downgrade) rather than demonstrably gaining share — not marked true without a positive trend citation. |
| Brand premium | **FALSE** | PDD's positioning is explicitly low-price/discount-driven (algorithmic low-price matching) — the opposite of a brand-premium moat. No pricing-power-without-volume-loss evidence cited. |
| Network effect | **TRUE** | Documented mechanism: PDD is a two-sided marketplace with algorithmic low-price matching, a group-buying viral mechanic, and lower-tier-China network effects — cited in both the 2026-07-01 new-position session and the 2026-08-25 qualitative pass as the core of its domestic moat (even while the latter notes it is "actively contested"). |
| Switching costs | **FALSE** | No documented lock-in mechanism (contractual, integration-depth, or data-migration cost) cited for either merchants or consumers on the platform. |
| Scale cost advantage | **TRUE** | PDD's C2M (customer-to-manufacturer) factory-direct sourcing model — cited in the 2026-07-01 new-position session and consistent with this session's "asset-light, algorithm-driven marketplace economics" characterization — structurally cuts out traditional retail-intermediary markup, a durable cost-structure advantage over smaller/less-integrated competitors. A structural business-model feature, not a point-in-time metric, so still valid without a fresh citation this session. |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10% weight):**
```
FCF/NI ratio (FY25) = 108.1%
FCFQuality_Score = clamp(((1.081 − 0.40)/0.60)×100, 0, 100) = clamp(113.5, 0, 100) = 100.0
```

### Quality Score

```
Quality Score = (75.10 × 0.25) + (70.35 × 0.15) + (90.0 × 0.20) + (100.0 × 0.15) + (40.0 × 0.15) + (100.0 × 0.10)
              = 18.775 + 10.5525 + 18.0 + 15.0 + 6.0 + 10.0
              = 78.3275 → rounds to 78.3
```

**Quality Score: 78.3 — FAILS the 80.0+ gate (narrowly — 1.7 points short).**

---

## 3. Verdict

Per [quality-scoring.md](../framework/quality-scoring.md): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all. Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."*

PDD clears every individual Phase 01 quantitative threshold (8/8, confirmed 2026-08-25) — the binary screen alone would have waved it through. The graded Quality Score catches what the binary screen can't: a moat that's real but only half-covered by cited evidence (2 of 5 signals — network effect and C2M scale cost advantage; no citation supports market share, brand premium, or switching costs, and the international side is actively eroding per Temu's own usage data) plus a real, cited, structural growth deceleration (86%→8% YoY), even though profitability, balance sheet, and cash-flow quality are all strong. That combination lands the score at 78.3 — 1.7 points under the bar, and notably down from the 81.3 this same ticker scored on 2026-07-01, where a broader, less-contested moat read (3/5 signals) and no growth-deceleration penalty (not yet as clearly evidenced then) combined to clear the gate. The gap between those two results is real: this session's read is more conservative on the moat (no positive market-share-trend citation found) and applies a deceleration penalty the July session didn't have cause to. **No Phase 02 valuation score or Composite Score is computed — the gate fails before that step, exactly as intended.**

**Recommendation: PASS, narrowly.** Not eligible for entry under this framework's current methodology, regardless of price — but close enough to the 80.0 bar that this is worth re-testing rather than shelving indefinitely. Two concrete re-check triggers: (1) PDD's own RMB 100bn/3-year "Xin Pin Mu" vertical-integration commitment (announced with Q2 2026 earnings) — if it demonstrably strengthens the moat (e.g. supply-chain lock-in with merchants) with citable evidence in a future session, the Moat Score could move; (2) a future session that can source a genuine domestic market-share *trend* figure (up or down) would resolve the current "no citation either way" gap on that signal. Until then, this is a quality-gate fail, not a valuation call.

---

## Glossary

- **FCF** — Free cash flow.
- **ROIC** — Return on Invested Capital.
- **ROCE (Return on Capital Employed)** — a close cousin of ROIC, used here as PDD's disclosed proxy where ROIC isn't separately published.
- **EV/EBIT** — Enterprise Value ÷ operating profit.
- **CAGR** — Compound Annual Growth Rate.
- **TAM** — Total Addressable Market.
- **Moat** / **Moat Signal** — durable competitive advantage; this framework's 5-point checklist scoring it.
- **Quality Score** — this framework's 0.0–100.0 graded score (80.0+ required to proceed to valuation).
- **Net Debt/EBITDA** — leverage ratio; net debt ÷ operating cash profit.
- **EPS** — Earnings Per Share.
- **PE** — Price-to-earnings ratio.
- **ADR** — American Depositary Receipt (how PDD trades on Nasdaq).

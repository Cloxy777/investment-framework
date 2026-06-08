# Valuation Score Engine

How to compute the Phase 02 score (1–10) for a qualified company. See [strategy.md](strategy.md) for where this fits in the overall framework.

## Final Score Formula

```
Final Score = (FCF × 0.40) + (EV/EBIT × 0.40) + (FwdPE_adjusted × 0.20) + Rate Regime Modifier [+ PEG Modifier — Fast Growers only]
```

> EV/EBIT is always 40% — there is no separate PEG "slot" to redistribute from. PEG is **not** a weighted component of the raw score; it's a small additive modifier (identical in form and placement to the Historical PE Modifier and the Rate Regime Modifier below) that applies *only* when the company is a Lynch Fast Grower (EPS growth >15% for 3+ years). Non-Fast-Growers simply don't receive it. (Corrected 2026-06-08 — see decisions/2026-06-08-framework-fix-peg-weighting-inconsistency.md: the prior "(PEG_or_fallback × 0.15)" framing was incompatible with the −1…+1 modifier table that Upgrade 3 actually defines.)
> Score boundary rule: if result falls on exactly X.5, round UP (more conservative). Min 1, max 10.

## Sub-score Tables

**FCF Yield (40% weight)** — use Owner Earnings yield where Upgrade 1 applies:

| FCF Yield | Sub-score |
|-----------|-----------|
| >8% | 1 |
| 6–8% | 2–3 |
| 4–6% | 4–5 |
| 2–4% | 6–7 |
| <2% | 8–10 |

**EV/EBIT (40% weight):**

| EV/EBIT | Sub-score |
|---------|-----------|
| <12× | 1–2 |
| 12–18× | 3–4 |
| 18–22× | 5 |
| 22–28× | 6–7 |
| 28–35× | 8–9 |
| >35× | 10 |

**Forward PE (20% weight):** Score 1–10 relative to sector historical norms, then apply the Historical PE Modifier (Upgrade 2 in [strategy.md](strategy.md)).

**PEG Modifier (additive, not weighted — Fast Growers only, EPS growth >15% for 3+ years):** applied the same way as the Historical PE Modifier and Rate Regime Modifier — a small bolt-on adjustment to the raw weighted score, not a 1–10 sub-score multiplied by a weight.

| PEG | Modifier |
|-----|----------|
| <0.8 | −1 |
| 0.8–1.2 | 0 |
| 1.2–1.8 | +0.5 |
| >2.0 | +1 |

**Rate Regime Modifier** — additive, applied after the raw weighted score (see Rate Environment Gate in [strategy.md](strategy.md)).

---

## Quantitative Pre-Screen Filters (Phase 01)

```
Gross margin       > 40%
Net margin         > 12%
ROIC               > 15%
Revenue growth     > 8% (3yr CAGR)
FCF positive       3 consecutive years
Net debt/EBITDA    < 2.5x
FCF yield          > 4%
EV/EBIT            < 20x
```

## Screening Tools

- **TIKR** — 100k+ global stocks, 335+ metrics, best for EV/EBIT, ROIC, FCF yield
- **Koyfin** — 10+ years historical financials, consistency analysis
- **Finviz** — Fast US market pre-filter, 60+ fundamental filters
- **Gurufocus** — Quality/value combo screens, Magic Formula, Buffett-style filters

## 5 Qualitative Questions Before Scoring

1. Why are margins high? Pricing power, scale, or lucky cycle?
2. What would it take to compete with them? (Hard = moat)
3. How has management allocated capital over 5–10 years?
4. Where is growth coming from next 3–5 years?
5. What is the best bear case against owning it?
6. Could a new delivery mechanism, platform, or technology make this moat irrelevant within 5 years? *(Disruption vector check)*

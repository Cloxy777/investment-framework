# Valuation Score Engine

How to compute the Phase 02 score (1–10) for a qualified company. See [strategy.md](strategy.md) for where this fits in the overall framework.

## Final Score Formula

```
Final Score = (FCF × 0.40) + (EV/EBIT × 0.25) + (FwdPE_adjusted × 0.20) + (PEG_or_fallback × 0.15) + Rate Regime Modifier
```

> If PEG is not applicable (non-Fast Grower), redistribute its 15% weight to EV/EBIT (making EV/EBIT weight 40%).
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

**EV/EBIT (25% weight):**

| EV/EBIT | Sub-score |
|---------|-----------|
| <12× | 1–2 |
| 12–18× | 3–4 |
| 18–22× | 5 |
| 22–28× | 6–7 |
| 28–35× | 8–9 |
| >35× | 10 |

**Forward PE (20% weight):** Score 1–10 relative to sector historical norms, then apply the Historical PE Modifier (Upgrade 2 in [strategy.md](strategy.md)).

**PEG (15% weight, Fast Growers only — EPS growth >15% for 3+ years):**

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

---

## Global Phase 01 Screener Setup

The correct workflow is to **apply Phase 01 filters mechanically across the full global universe first**, then hand the output to Claude for triage and qualitative analysis. This surfaces quality candidates that haven't been discovered yet — small/mid-caps not in major indices, low institutional ownership, no analyst hype — rather than re-examining the same well-known names every time.

**Workflow:**
1. Run the saved screener below in TIKR (global) or Finviz (US-only fast pass)
2. Export or copy the ticker list
3. Paste it at the start of a `/screen` session — Claude takes it from there

### TIKR — Global Screener (primary, 100k+ tickers)

Set up a saved screen in TIKR Terminal → Screener with these filters:

| TIKR Filter | Operator | Value |
|---|---|---|
| Gross Profit Margin % (LTM) | ≥ | 40 |
| Net Income Margin % (LTM) | ≥ | 12 |
| Return on Invested Capital % (LTM) | ≥ | 15 |
| Revenue Growth % (3Y CAGR) | ≥ | 8 |
| Free Cash Flow (LTM) | > | 0 |
| Free Cash Flow (1Y prior) | > | 0 |
| Free Cash Flow (2Y prior) | > | 0 |
| Net Debt / EBITDA (LTM) | ≤ | 2.5 |

*The valuation cuts (FCF yield >4%, EV/EBIT <20×) are intentionally excluded here — let Phase 02 score valuation. The goal of Phase 01 is to find every quality business, not pre-screen out expensive ones that might still belong on the watchlist.*

Expected output: ~150–400 companies globally. Save this screen in TIKR for re-use.

### Finviz — US Fast Pass (secondary, US-only)

Use for a quick US-only pass or to double-check TIKR output. Set filters at finviz.com/screener.ashx:

| Finviz Filter | Setting |
|---|---|
| Gross Margin | Over 40% |
| Net Profit Margin | Over 12% |
| Return on Equity | Over 15% *(closest proxy for ROIC available in Finviz)* |
| Sales growth past 5 years | Over 10% |
| Operating Margin | Over 15% |
| Debt/Equity | Under 0.5 |

### Gurufocus — Global Alternative

Use All-in-One Screener with: Gross Margin > 40, Net Margin > 12, ROIC > 15, 5Y Revenue Growth > 8, Debt-to-EBITDA < 2.5. Adds Magic Formula rank and Buffett-style quality composite for additional context.

---

## Discovery Filters — Finding Undiscovered Names

Layer these **on top of** the Phase 01 screener when you specifically want candidates that institutions haven't found yet:

| Filter | Threshold | Why |
|---|---|---|
| Market Cap | $300M – $10B | Below index-inclusion thresholds; pre-institutional radar |
| Institutional Ownership % | < 40% | Genuinely under-owned |
| Analyst Coverage | < 8 analysts | Low coverage = low visibility |
| Index membership | Not S&P 500 / Not MSCI World | Pre-index, no forced-buyer tailwind yet |

These are **optional** — run the standard Phase 01 screen first, then run it again with discovery filters if you want a separate "hidden gems" pass. A company that passes Phase 01 at any market cap is worth evaluating; the discovery filters just help prioritise candidates most likely to be mispriced due to neglect.

## 5 Qualitative Questions Before Scoring

1. Why are margins high? Pricing power, scale, or lucky cycle?
2. What would it take to compete with them? (Hard = moat)
3. How has management allocated capital over 5–10 years?
4. Where is growth coming from next 3–5 years?
5. What is the best bear case against owning it?
6. Could a new delivery mechanism, platform, or technology make this moat irrelevant within 5 years? *(Disruption vector check)*

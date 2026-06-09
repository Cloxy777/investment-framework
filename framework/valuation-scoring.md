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

`/screen` uses the **EODHD API** (key stored in `.claude/settings.local.json`) to automatically pull and filter the global universe — no manual export needed. The flow:

1. EODHD screener pre-filters ~70k+ global tickers → ~300–600 quality candidates
2. Claude applies the full Phase 01 gate on that shortlist using the EODHD fundamentals endpoint
3. Structural triage + qualitative pass produces the final Qualified Quality List

### EODHD API — Screener Endpoint

```
GET https://eodhd.com/api/screener
  ?api_token={EODHD_API_KEY}
  &filters=[FILTER_ARRAY]
  &limit=100&offset=0
```

**Confirmed filter fields:** `exchange`, `sector`, `industry`, `market_capitalization`, `earnings_share`, `dividend_yield`

**Quality filter fields to try** (supported on some plans — drop any that return an error):
`ProfitMargin`, `ReturnOnEquityTTM`, `OperatingMarginTTM`, `QuarterlyRevenueGrowthYOY`

Default quality pre-filter values: `ProfitMargin ≥ 0.12`, `ReturnOnEquityTTM ≥ 0.15`, `OperatingMarginTTM ≥ 0.10`, `market_capitalization ≥ 300000000`

Paginate by incrementing `offset` by 100 until a page returns < 100 results.

### EODHD API — Fundamentals Endpoint (Phase 01 verification)

```
GET https://eodhd.com/api/fundamentals/{TICKER}.{EXCHANGE}
  ?api_token={EODHD_API_KEY}&filter=Highlights
```

Key Highlights fields and their Phase 01 mapping:

| EODHD Field | Phase 01 Metric |
|---|---|
| `ProfitMargin` | Net margin (threshold: >12%) |
| `GrossProfitTTM / RevenueTTM` | Gross margin (threshold: >40%) — calculated |
| `ReturnOnEquityTTM` | ROIC proxy (threshold: >15%) — flag if equity-heavy structure makes ROE unreliable |
| `QuarterlyRevenueGrowthYOY` | Revenue growth proxy — flag divergence from 3yr CAGR |
| `OperatingMarginTTM` | Operating margin (supporting signal) |
| `FreeCashFlow` | FCF positive check — use `filter=Financials` for 3-year history |

Metrics not available in Highlights (require `filter=Financials` or manual check): Net Debt/EBITDA, 3yr revenue CAGR, FCF/Net Income conversion ratio. Flag these as needing manual TIKR/Koyfin verification rather than estimating.

### Manual fallback (if EODHD key missing or network restricted)

TIKR saved screen: Gross Margin % ≥ 40, Net Margin % ≥ 12, ROIC ≥ 15, Revenue Growth 3Y CAGR ≥ 8%, FCF > 0 (3 years), Net Debt/EBITDA ≤ 2.5. Export and paste to `/screen`.

Finviz (US fast pass): Gross Margin > 40%, Net Profit Margin > 12%, ROE > 15%, Sales 5Y > 10%, Operating Margin > 15%, Debt/Equity < 0.5.

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

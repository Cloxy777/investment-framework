# Valuation Score Engine

How to compute the Phase 02 score (0–100.0) for a qualified company. See [strategy.md](strategy.md) for where this fits in the overall framework.

*Rescaled 2026-06-11 from the original 1–10 integer scale to a continuous 0–100.0 scale for more precision — see [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md). Cap set to a clean 100.0 (rather than 99.9) so the EV/EBIT and PEG sub-score formulas land on round numbers at their defined extremes (EV/EBIT 35× → exactly 100.0, PEG 2.5 → exactly 100.0).*

## Final Score Formula

```
Final Score = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.25) + (FwdPE_Score × 0.20) + (PEG_Score_or_fallback × 0.15) + Rate Regime Modifier
```

> If PEG is not applicable (non-Fast Grower), redistribute its 15% weight to EV/EBIT (making EV/EBIT weight 40%).
> Score boundary rule: round the final result to the nearest 0.1. If it falls exactly on a ".X5" (e.g. 47.45), round UP to ".X+1" — e.g. 47.45 → 47.5 (more conservative). Min 0.0, max 100.0.

## Sub-score Formulas

Each of the four inputs is computed on its own continuous **0.0–100.0** scale before weighting — **0 = cheapest/most attractive, 100.0 = most expensive.** This replaces the old discrete 1–10 bucket tables with one formula per metric, so two companies that previously landed in the same bucket (e.g. both "sub-score 6–7") are now distinguished.

**FCF Yield (40% weight)** — use Owner Earnings yield where Upgrade 1 applies:

```
FCF_Score = clamp(100 × (1 − FCF_Yield% / 10), 0, 100)
```

| FCF Yield | Score |
|-----------|-------|
| ≥10% | 0.0 |
| 8% | 20.0 |
| 6% | 40.0 |
| 5% | 50.0 |
| 4% | 60.0 |
| 2% | 80.0 |
| ≤0% | 100.0 |

**EV/EBIT (25% weight):**

```
EV/EBIT_Score = clamp((EV/EBIT − 12) / 23 × 100, 0, 100)
```

| EV/EBIT | Score |
|---------|-------|
| ≤12× | 0.0 |
| 17.75× | 25.0 |
| 23.5× | 50.0 |
| 29.25× | 75.0 |
| ≥35× | 100.0 |

**Forward PE (20% weight):**

**Primary formula** — used when a trailing 10-year PE *range* (low and high) is available:

```
FwdPE_Score = clamp((Forward PE − 10yr Low PE) / (10yr High PE − 10yr Low PE) × 100, 0, 100)
```

Position the company's forward PE within its own trailing 10-year PE range, then apply the **Historical PE Modifier** (Upgrade 2 in [strategy.md](strategy.md)), additive: >20% below 10yr avg PE → −10 | within ±10% → 0 | >20% above → +10 (subject to the Structural Quality Override).

**Fallback formula** — used when only a single 10-year *average* PE is available (no low/high range). In practice this is the common case:

```
Deviation% = (Forward PE − 10yr Avg PE) / 10yr Avg PE × 100
FwdPE_Score = clamp(50 + Deviation% × 2.5, 0, 100)
```

This centers the score at 50.0 when forward PE equals the 10-year average and reaches the 0/100 extremes at ±20% deviation — a continuous generalisation of the original 5-row "vs. 10yr avg" bucket table (>20% below → cheap end, >20% above → expensive end). **This formula already folds in the Historical PE Modifier** (the deviation from the 10-year average *is* the signal Upgrade 2 is meant to capture) — do not separately apply the ±10 modifier on top of it, to avoid double-counting.

**No-history fallback** — if neither a range nor a meaningful average PE exists (recent IPO, loss-making history, or a GAAP earnings base too distorted to be meaningful):

```
FwdPE_Score = 50.0  (neutral midpoint, flagged)
```

Do not estimate a 10-year range or average that doesn't exist — use the 50.0 neutral placeholder and flag it explicitly, consistent with "never invent or estimate financial data."

**PEG (15% weight, Fast Growers only — EPS growth >15% for 3+ years):**

```
PEG_Score = clamp((PEG − 0.5) / 2.0 × 100, 0, 100)
```

| PEG | Score |
|-----|-------|
| ≤0.5 | 0.0 |
| 1.0 | 25.0 |
| 1.5 | 50.0 |
| 2.0 | 75.0 |
| ≥2.5 | 100.0 |

If PEG is not applicable (not a Fast Grower), redistribute its 15% weight to EV/EBIT per the Final Score Formula note above.

**Rate Regime Modifier** — additive, applied after the raw weighted score (see Rate Environment Gate in [strategy.md](strategy.md)): −10 / 0 / +5 / +10 based on the 10Y Treasury regime.

---

## Converting Legacy 1–10 Scores

Sessions and decisions logged before 2026-06-11 record scores on the old 1–10 integer scale. To compare against the new 0–100.0 scale:

```
New Score = (Old Score − 1) × 100/9
```

| Old | New | Old | New |
|-----|-----|-----|-----|
| 1 | 0.0 | 6 | 55.6 |
| 2 | 11.1 | 7 | 66.7 |
| 3 | 22.2 | 8 | 77.8 |
| 4 | 33.3 | 9 | 88.9 |
| 5 | 44.4 | 10 | 100.0 |

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

`/screen` builds the starting universe manually — a TIKR/Koyfin saved-screen export, a Finviz fast pass, or quality-factor ETF holdings (MOAT/QUAL/QGRW/IQLT) when screener access isn't available (see [screen.md](../.claude/commands/screen.md) Step 0). There is no bulk-screener API wired up; `yf.screen()` (the bulk Yahoo screener) is unreliable for pre-filtering — see below.

Once a candidate list exists, verify each candidate's exact Phase 01 numbers with the free `yfinance` Python package — no API key needed.

### Manual screening tools

TIKR saved screen: Gross Margin % ≥ 40, Net Margin % ≥ 12, ROIC ≥ 15, Revenue Growth 3Y CAGR ≥ 8%, FCF > 0 (3 years), Net Debt/EBITDA ≤ 2.5. Export and paste to `/screen`.

Finviz (US fast pass): Gross Margin > 40%, Net Profit Margin > 12%, ROE > 15%, Sales 5Y > 10%, Operating Margin > 15%, Debt/Equity < 0.5.

### `yfinance` — per-candidate Phase 01 verification (verified working 2026-06-14)

Use this for **Step 2 (per-candidate Phase 01 verification)** in [screen.md](../.claude/commands/screen.md):

```bash
pip install --quiet yfinance   # one-time per session
```

```python
import yfinance as yf
t = yf.Ticker("0388.HK")   # works with exchange-suffixed tickers (.AX, .HK, .SI, .TW) and US ADRs
info = t.financials   # annual income statement: Gross Profit, EBIT, EBITDA, Net Income, Total Revenue
cf   = t.cashflow     # annual cash flow: Free Cash Flow, Operating Cash Flow, Capital Expenditure
bs   = t.balance_sheet  # Total Debt, Cash And Cash Equivalents, Total Equity
hi   = t.info         # current snapshot: marketCap, enterpriseValue, grossMargins, profitMargins,
                       # returnOnEquity, revenueGrowth, freeCashflow, ebitda, enterpriseToEbitda,
                       # trailingPE, forwardPE, pegRatio, debtToEquity, totalDebt, totalCash
```

Verified against this session's manually-sourced HKEX numbers (`grossMargins` 0.965, `returnOnEquity` 0.350, `profitMargins` 0.626 — all matched stockanalysis.com to 3 decimals). `t.financials`/`t.cashflow` provide multi-year history for the 3yr CAGR and "FCF positive 3 consecutive years" checks; `t.info["ebit"]`/`enterpriseValue` give EV/EBIT directly.

**Do not use `yf.screen()` (the bulk Yahoo screener) for Phase 01 pre-filtering** — tested 2026-06-14 and its margin/ROE/growth filter predicates did not constrain results correctly (e.g. a query requiring net margin >12% and ROE >15% still returned Woolworths, which has ~0.85% net margin and ~11.9% ROE). For the bulk pre-filter step, continue using **structural triage from documented business-model characteristics** ([screen.md](../.claude/commands/screen.md) Step 1) to build the candidate pool, then verify each candidate's real numbers with `yfinance` as above.

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

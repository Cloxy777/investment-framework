# Valuation Score Engine

How to compute the Phase 02 score (0–100.0) for a qualified company. See [strategy.md](strategy.md) for where this fits in the overall framework.

*Rescaled 2026-06-11 from the original 1–10 integer scale to a continuous 0–100.0 scale for more precision — see [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md). Cap set to a clean 100.0 (rather than 99.9) so the EV/EBIT and PEG sub-score formulas land on round numbers at their defined extremes (EV/EBIT 35× → exactly 100.0, PEG 2.5 → exactly 100.0).*

## Final Score Formula

```
Final Score = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.25) + (FwdPE_Score × 0.20) + (PEG_Score_or_fallback × 0.15) + Rate Regime Modifier + Upside/Downside Modifier
```

> If PEG is not applicable (non-Fast Grower), redistribute its 15% weight to EV/EBIT (making EV/EBIT weight 40%).
> Score boundary rule: round the final result to the nearest 0.1. If it falls exactly on a ".X5" (e.g. 47.45), round UP to ".X+1" — e.g. 47.45 → 47.5 (more conservative). Min 0.0, max 100.0.

## Why Forward Guidance Is Not a Sub-score

Management's own forward guidance (a company's self-issued prediction of its next quarter's or year's results) is deliberately left out of the four weighted inputs above. FCF Yield, EV/EBIT, Forward PE, and PEG are all derived from filed financials or market-observable prices; guidance is a self-reported, unaudited number that management has both the means and the incentive to manage (compensation tied to hitting it, "beat-and-raise" patterns). Baking it into a weighted score would re-introduce exactly the kind of gameable, self-reported input the FCF/Net Income conversion check (added after the Valeant and Wirecard cases — see [graveyard-audit.md](graveyard-audit.md)) was built to guard against. See the **Guidance test** in [investor-philosophy-alignment.md](investor-philosophy-alignment.md) for the full reasoning.

Guidance still matters — as a **trigger**, not a **score**:
- A guidance revision (up or down) is a mandatory re-valuation event ([fair-value-methodology.md](fair-value-methodology.md) Rule 9) — it changes the inputs that feed the score, rather than being scored itself.
- Phase 04's **Guidance discipline check** ([strategy.md](strategy.md)) tracks guidance delivered vs. promised over time and escalates a sustained pattern of cuts into the Phase 06 exit review, independent of where the valuation score sits.

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

*Lookback shortened from 10yr to 5yr on 2026-06-20 to make this fully automatable via `yfinance` rather than requiring a manual Macrotrends pull — see [decisions/2026-06-20-framework-change-5yr-historical-pe-automation.md](../decisions/2026-06-20-framework-change-5yr-historical-pe-automation.md) and the auto-calc method below.*

**Primary formula** — used when a trailing 5-year PE *range* (low and high) is available:

```
FwdPE_Score = clamp((Forward PE − 5yr Low PE) / (5yr High PE − 5yr Low PE) × 100, 0, 100)
```

Position the company's forward PE within its own trailing 5-year PE range, then apply the **Historical PE Modifier** (Upgrade 2 in [strategy.md](strategy.md)), additive: >20% below 5yr avg PE → −10 | within ±10% → 0 | >20% above → +10 (subject to the Structural Quality Override).

**Fallback formula** — used when only a single 5-year *average* PE is available (no low/high range). In practice this is the common case:

```
Deviation% = (Forward PE − 5yr Avg PE) / 5yr Avg PE × 100
FwdPE_Score = clamp(50 + Deviation% × 2.5, 0, 100)
```

This centers the score at 50.0 when forward PE equals the 5-year average and reaches the 0/100 extremes at ±20% deviation — a continuous generalisation of the original 5-row "vs. 5yr avg" bucket table (>20% below → cheap end, >20% above → expensive end). **This formula already folds in the Historical PE Modifier** (the deviation from the 5-year average *is* the signal Upgrade 2 is meant to capture) — do not separately apply the ±10 modifier on top of it, to avoid double-counting.

**No-history fallback** — if neither a range nor a meaningful average PE exists (recent IPO, loss-making history, or a GAAP earnings base too distorted to be meaningful):

```
FwdPE_Score = 50.0  (neutral midpoint, flagged)
```

Do not estimate a 5-year range or average that doesn't exist — use the 50.0 neutral placeholder and flag it explicitly, consistent with "never invent or estimate financial data."

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

## Upside/Downside Modifier (Expected-Return Modifier)

*Added 2026-06-20 — see [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md). This closes the "great company never gets cheap" gap: the four weighted sub-scores above are 65–80% anchored on current/trailing valuation, so a wonderful business correctly priced for a bright future could sit permanently in the 50–60 "Fair Value" band and never trigger an entry. This modifier folds the **forward** dimension — how much money the position is actually expected to make — into the single score, so reading the lowest score is enough to rank candidates, and a name with thin or negative expected return is automatically pushed up toward the trim/exit bands.*

**What it does, in one line:** strong expected upside lowers the score (more attractive); thin or negative expected return (an expected *loss*) raises it (toward trim/sell).

**Additive, bounded to [−15, +15]**, applied after the raw weighted score alongside the Rate Regime Modifier. The ±15 cap (the bound, deliberately chosen over a wider range) means the forecast *informs* but never *overrides* the bottom-up cheapness gate — a hyped story scoring 80 lands at 65 (still "Hold / no new entry"), it cannot jump to "Buy" on optimism alone.

**Step 1 — Expected annual return `E`.** Built entirely from fair-value work already defined in [fair-value-methodology.md](fair-value-methodology.md) — no new data source:

```
PW Fair Value   = 0.25×Bull + 0.50×Base + 0.25×Bear          (Rule 7 — downside underwritten via the bear case)
Gap Upside %    = (PW Fair Value ÷ Live Price) − 1            (Live Price per Rule 0 — fetch first, never infer)
Annualized gap  = Gap Upside % ÷ catalyst-timeline in years   (Rule 10; if no narrower window, use 2yr)
E               = Annualized gap + intrinsic growth rate (FCF or EPS CAGR) + shareholder yield (dividend % + net buyback %)
```

`PW` = probability-weighted (the scenario blend). `CAGR` = compound annual growth rate. Shareholder yield = cash returned to owners as a % of price (dividends plus net share buybacks).

**Step 2 — Map `E` to the modifier** against a hurdle `H = 10%` (the midpoint of Rule 4's 8–15% implied-IRR — internal rate of return — sanity band). `pp` = percentage points:

```
If E ≥ H:        M = −15 × clamp((E − H) / 15pp, 0, 1)     # strong upside  → 0 … −15  (E ≥ 25%/yr → full −15)
If 0 ≤ E < H:    M = +5  × (H − E) / H                     # thin upside    → 0 … +5   (caps at +5 — see anti-turnover note)
If E < 0:        M = +5 + 10 × clamp((−E) / 10pp, 0, 1)    # expected loss  → +5 … +15 (E ≤ −10%/yr → full +15)
```

Neutral (M = 0) when `E = 10%`. The mapping is **deliberately asymmetric**: a merely-modest positive expected return can add at most +5, so it will *not* by itself shove a held name out of the 50.0–69.9 "Hold" band into the 70.0+ trim band — only a genuine expected *loss* reaches the higher positives. This is what preserves Phase 05's "fair value alone is not a sell" / anti-turnover posture (the 2026-06-07 decision) while still delivering the requested "downside → trim/sell" behaviour for names that are actually expected to lose money.

| Expected annual return `E` | Modifier `M` | Effect |
|---|---|---|
| ≥ +25% | −15.0 | Strongly attractive — pulls score down a full band |
| +17.5% | −7.5 | Attractive |
| +10% (hurdle) | 0.0 | Neutral — pure cheapness score stands |
| +5% | +2.5 | Thin upside — slight penalty |
| 0% | +5.0 | No expected return — mild trim pressure |
| −5% | +10.0 | Expected loss — strong trim pressure |
| ≤ −10% | +15.0 | Expected double-digit loss — pushes toward trim/exit |

**Guardrails (forecast discipline — this is the most discretionary input in the score, so it is fenced):**
1. **Catalyst required for upside credit.** Per Rule 10, a documented catalyst + timeline must exist. If no catalyst is identifiable within 18–24 months, cap the *upside* (negative) side at **−5** — you can't claim large upside with no path to realise it. The downside side is unaffected (a thesis with no catalyst and an expected loss should still be penalised).
2. **Scenario-weighted, not the rosy point.** Always use the bull/base/bear PW Fair Value (Rule 7), never a single optimistic target — downside is always underwritten (Klarman: "what do I lose if I'm wrong" first).
3. **Show the full calc.** `E`, each of its three components, the catalyst/timeline, and the mapping must be shown in the session log like every other sub-score and modifier — no black box (operating-brief.md non-negotiable).
4. **It is a modifier, not a veto, in both directions** — bounded ±15 by design, mirroring how the Rate Environment Gate's Step 1 was softened from a hard block to an additive flag (2026-06-07).

**Worked example.** A Fast Grower at score 54 (raw), live price $100, PW Fair Value $118 (so Gap Upside +18%), catalyst window 2 years (annualized gap +9%), intrinsic growth +14%/yr, shareholder yield +1% → `E` = 9 + 14 + 1 = **+24%**. Modifier = −15 × clamp((24 − 10)/15, 0, 1) = −15 × 0.93 = **−14.0**. Final score 54 − 14.0 = **40.0** → moves from "Hold / watchlist only" into "Cheap → standard position." The bright future the raw score ignored now earns the entry, exactly the gap this closes.

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

### `yfinance` — automated 5yr avg PE & FCF/NI conversion ratio (verified working 2026-06-20)

These two Standard Re-Score inputs were previously flagged as needing a manual Macrotrends/TIKR/Koyfin pull (`operating-calendar.md`). Both are now computable directly from `yfinance` — no new data source needed.

**FCF/NI Conversion Ratio** — `t.cashflow` and `t.financials` already carry both halves of this ratio; it was just never wired into a formula:

```python
fcf = t.cashflow.loc["Free Cash Flow"]
ni  = t.financials.loc["Net Income"]
fcf_ni_ratio = (fcf / ni).dropna()   # e.g. 0.70-0.90 for a healthy compounder
```
Verified against MSFT (2022-2025): 89.6%, 82.2%, 84.0%, 70.3% — 4 years, enough for the "2+ consecutive years" check in Phase 01/04.

**5yr Avg/Low/High PE** — `t.financials`' annual EPS only goes back ~4 years on the free tier, too shallow for a historical PE series. `t.get_earnings_dates(limit=40)` (requires `lxml`) returns quarterly **Reported EPS** much further back (verified on MSFT: 49 quarters to 2014). Reconstruct a trailing-PE series by summing trailing-4-quarter EPS into TTM EPS, then pairing each quarter with its contemporaneous price:

```python
import pandas as pd
ed = t.get_earnings_dates(limit=40).sort_index().dropna(subset=["Reported EPS"])
ed["TTM_EPS"] = ed["Reported EPS"].rolling(4).sum()
ed = ed.dropna(subset=["TTM_EPS"])

hist = t.history(start=ed.index.min().date().isoformat(), interval="1d")
hist.index = hist.index.tz_localize(None)

pe_series = []
for dt, row in ed.iterrows():
    after = hist[hist.index >= dt.tz_localize(None)]
    if after.empty: continue
    pe_series.append(after["Close"].iloc[0] / row["TTM_EPS"])

last5y = pd.Series(pe_series[-20:])   # last 20 quarters ≈ 5 years
avg_pe, low_pe, high_pe = last5y.mean(), last5y.min(), last5y.max()
```
Verified on MSFT 2026-06-20: 5yr avg PE 32.0×, range 24.2–38.8× (n=20 quarters) — consistent with MSFT's known historical multiple band.

**Caveats:**
- History depth on `get_earnings_dates` varies by ticker — smaller/less-covered names may return fewer than 20 quarters. If fewer than 5 years (20 quarters) of TTM EPS are reconstructable, treat it as the existing **no-history fallback** (`FwdPE_Score = 50.0`, flagged) rather than computing a PE average over a shorter window.
- Exclude any quarter where TTM EPS is ≤0 (PE undefined) rather than computing a nonsensical or negative value.
- `lxml` must be installed (`pip install --quiet lxml`) — `get_earnings_dates` raises without it.

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

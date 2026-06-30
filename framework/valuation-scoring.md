# Valuation Score Engine

How to compute Phase 02 score (0–100.0) for a qualified company. See [strategy.md](strategy.md) for where this fits in overall framework.

> **Scoring methodology version: 2026-06-29.** Bump this date whenever a change materially alters how score is computed (new/changed sub-score, modifier, weight, eligibility rule); record why in `decisions/`. Version bump triggers watchlist **stale-score** mechanism: any watchlist entry with score from older version flagged stale (banner + [watchlist/STALE.md](../watchlist/STALE.md) row) until rescored — see [watchlist/README.md](../watchlist/README.md#stale-scores--when-the-scoring-methodology-changes). *Version history: 2026-06-11 (1–10 → 0–100 rescale) → 2026-06-20 (5yr PE lookback, Upside/Downside Modifier, PEG clean-earnings clarification) → 2026-06-29 (Quality Score + 80.0+ gate + Composite Score added, see [quality-scoring.md](quality-scoring.md)).*

*Rescaled 2026-06-11 from original 1–10 integer scale to continuous 0–100.0 scale for more precision — see [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md). Cap set to clean 100.0 (rather than 99.9) so EV/EBIT and PEG sub-score formulas land on round numbers at defined extremes (EV/EBIT 35× → exactly 100.0, PEG 2.5 → exactly 100.0).*

## Final Score Formula

```
Final Score = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.25) + (FwdPE_Score × 0.20) + (PEG_Score_or_fallback × 0.15) + Rate Regime Modifier + Upside/Downside Modifier
```

> If PEG is not applicable (non-Fast Grower), redistribute its 15% weight to EV/EBIT (making EV/EBIT weight 40%).
> Score boundary rule: round the final result to the nearest 0.1. If it falls exactly on a ".X5" (e.g. 47.45), round UP to ".X+1" — e.g. 47.45 → 47.5 (more conservative). Min 0.0, max 100.0.

## Why Forward Guidance Is Not a Sub-score

Management's own forward guidance (self-issued prediction of next quarter's/year's results) is deliberately left out of the four weighted inputs above. FCF Yield, EV/EBIT, Forward PE, PEG are all derived from filed financials or market-observable prices; guidance is self-reported, unaudited, and management has both means and incentive to manage it (compensation tied to hitting it, "beat-and-raise" patterns). Baking it into a weighted score would re-introduce exactly the gameable, self-reported input the FCF/Net Income conversion check (added after Valeant and Wirecard cases — see [graveyard-audit.md](graveyard-audit.md)) was built to guard against. See **Guidance test** in [investor-philosophy-alignment.md](investor-philosophy-alignment.md) for full reasoning.

Guidance still matters — as **trigger**, not **score**:
- Guidance revision (up or down) is mandatory re-valuation event ([fair-value-methodology.md](fair-value-methodology.md) Rule 9) — changes inputs feeding the score, rather than being scored itself.
- Phase 04's **Guidance discipline check** ([strategy.md](strategy.md)) tracks guidance delivered vs. promised over time, escalates sustained pattern of cuts into Phase 06 exit review, independent of where valuation score sits.

## Sub-score Formulas

Each of the four inputs computed on its own continuous **0.0–100.0** scale before weighting — **0 = cheapest/most attractive, 100.0 = most expensive.** Replaces old discrete 1–10 bucket tables with one formula per metric, so two companies previously landed in same bucket (e.g. both "sub-score 6–7") now distinguished.

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

*Lookback shortened from 10yr to 5yr on 2026-06-20 to make fully automatable via `yfinance` rather than requiring manual Macrotrends pull — see [decisions/2026-06-20-framework-change-5yr-historical-pe-automation.md](../decisions/2026-06-20-framework-change-5yr-historical-pe-automation.md) and auto-calc method below.*

**Primary formula** — used when a trailing 5-year PE *range* (low and high) is available:

```
FwdPE_Score = clamp((Forward PE − 5yr Low PE) / (5yr High PE − 5yr Low PE) × 100, 0, 100)
```

Position company's forward PE within its own trailing 5-year PE range, then apply **Historical PE Modifier** (Upgrade 2 in [strategy.md](strategy.md)), additive: >20% below 5yr avg PE → −10 | within ±10% → 0 | >20% above → +10 (subject to Structural Quality Override).

**Fallback formula** — used when only single 5-year *average* PE available (no low/high range). In practice the common case:

```
Deviation% = (Forward PE − 5yr Avg PE) / 5yr Avg PE × 100
FwdPE_Score = clamp(50 + Deviation% × 2.5, 0, 100)
```

Centers score at 50.0 when forward PE equals 5-year average, reaches 0/100 extremes at ±20% deviation — continuous generalisation of original 5-row "vs. 5yr avg" bucket table (>20% below → cheap end, >20% above → expensive end). **This formula already folds in Historical PE Modifier** (deviation from 5-year average *is* the signal Upgrade 2 captures) — don't separately apply ±10 modifier on top, to avoid double-counting.

**No-history fallback** — if neither range nor meaningful average PE exists (recent IPO, loss-making history, or GAAP earnings base too distorted to be meaningful):

```
FwdPE_Score = 50.0  (neutral midpoint, flagged)
```

Don't estimate a 5-year range or average that doesn't exist — use 50.0 neutral placeholder, flag explicitly, consistent with "never invent or estimate financial data."

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

> **Fast-Grower eligibility — "3+ years" means *reliable* earnings base (clarified 2026-06-20).** PEG sub-score only goes live when EPS growth exceeded 15% for 3+ years *on a clean, non-distorted earnings base*. A genuinely fast-growing business lacking this — recent IPO, company only recently turned GAAP-profitable, or trailing EPS distorted by a one-off (e.g. deferred-tax-valuation-allowance release) — does **not** yet qualify: **redistribute PEG's 15% to EV/EBIT** rather than forcing PEG off an unreliable base. Revenue-CAGR-proxy PEG may be computed as a *sensitivity check* but isn't the scored input. Keeps PEG to businesses with real, measurable multi-year earnings (Lynch) and the score to reliable inputs (Greenblatt), consistent with "never invent or estimate financial data." *(Ruling recorded after DUOL was scored both ways across two sessions — see [decisions/2026-06-20-framework-clarification-peg-clean-earnings.md](../decisions/2026-06-20-framework-clarification-peg-clean-earnings.md).)*

**Rate Regime Modifier** — additive, applied after raw weighted score (see Rate Environment Gate in [strategy.md](strategy.md)): −10 / 0 / +5 / +10 based on 10Y Treasury regime.

---

## Upside/Downside Modifier (Expected-Return Modifier)

*Added 2026-06-20 — see [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md). Closes "great company never gets cheap" gap: four weighted sub-scores above are 65–80% anchored on current/trailing valuation, so a wonderful business correctly priced for a bright future could sit permanently in the 50–60 "Fair Value" band and never trigger an entry. This modifier folds the **forward** dimension — how much money the position is actually expected to make — into the single score, so reading the lowest score is enough to rank candidates, and a name with thin or negative expected return is automatically pushed up toward the trim/exit bands.*

**What it does, in one line:** strong expected upside lowers the score (more attractive); thin or negative expected return (an expected *loss*) raises it (toward trim/sell).

**Additive, bounded to [−15, +15]**, applied after raw weighted score alongside Rate Regime Modifier. ±15 cap (deliberately chosen over wider range) means forecast *informs* but never *overrides* bottom-up cheapness gate — a hyped story scoring 80 lands at 65 (still "Hold / no new entry"), can't jump to "Buy" on optimism alone.

**Step 1 — Expected annual return `E`.** Built entirely from fair-value work already defined in [fair-value-methodology.md](fair-value-methodology.md) — no new data source:

```
PW Fair Value   = 0.25×Bull + 0.50×Base + 0.25×Bear          (Rule 7 — downside underwritten via the bear case)
Gap Upside %    = (PW Fair Value ÷ Live Price) − 1            (Live Price per Rule 0 — fetch first, never infer)
Annualized gap  = Gap Upside % ÷ catalyst-timeline in years   (Rule 10; if no narrower window, use 2yr)
E               = Annualized gap + intrinsic growth rate (FCF or EPS CAGR) + shareholder yield (dividend % + net buyback %)
```

`PW` = probability-weighted (the scenario blend). `CAGR` = compound annual growth rate. Shareholder yield = cash returned to owners as a % of price (dividends plus net share buybacks).

**Step 2 — Map `E` to modifier** against hurdle `H = 10%` (midpoint of Rule 4's 8–15% implied-IRR — internal rate of return — sanity band). `pp` = percentage points:

```
If E ≥ H:        M = −15 × clamp((E − H) / 15pp, 0, 1)     # strong upside  → 0 … −15  (E ≥ 25%/yr → full −15)
If 0 ≤ E < H:    M = +5  × (H − E) / H                     # thin upside    → 0 … +5   (caps at +5 — see anti-turnover note)
If E < 0:        M = +5 + 10 × clamp((−E) / 10pp, 0, 1)    # expected loss  → +5 … +15 (E ≤ −10%/yr → full +15)
```

Neutral (M = 0) when `E = 10%`. Mapping **deliberately asymmetric**: a merely-modest positive expected return adds at most +5, so won't by itself shove a held name out of the 50.0–69.9 "Hold" band into the 70.0+ trim band — only a genuine expected *loss* reaches the higher positives. Preserves Phase 05's "fair value alone is not a sell" / anti-turnover posture (2026-06-07 decision) while still delivering "downside → trim/sell" behaviour for names actually expected to lose money.

| Expected annual return `E` | Modifier `M` | Effect |
|---|---|---|
| ≥ +25% | −15.0 | Strongly attractive — pulls score down a full band |
| +17.5% | −7.5 | Attractive |
| +10% (hurdle) | 0.0 | Neutral — pure cheapness score stands |
| +5% | +2.5 | Thin upside — slight penalty |
| 0% | +5.0 | No expected return — mild trim pressure |
| −5% | +10.0 | Expected loss — strong trim pressure |
| ≤ −10% | +15.0 | Expected double-digit loss — pushes toward trim/exit |

**Guardrails (forecast discipline — most discretionary input in the score, so fenced):**
1. **Catalyst required for upside credit.** Per Rule 10, documented catalyst + timeline must exist. If no catalyst identifiable within 18–24 months, cap *upside* (negative) side at **−5** — can't claim large upside with no path to realise it. Downside side unaffected (a thesis with no catalyst and an expected loss should still be penalised).
2. **Scenario-weighted, not the rosy point.** Always use bull/base/bear PW Fair Value (Rule 7), never single optimistic target — downside always underwritten (Klarman: "what do I lose if I'm wrong" first).
3. **Show full calc.** `E`, each of its three components, the catalyst/timeline, and the mapping must be shown in the session log like every other sub-score and modifier — no black box (operating-brief.md non-negotiable).
4. **It is a modifier, not a veto, in both directions** — bounded ±15 by design, mirroring how Rate Environment Gate's Step 1 was softened from hard block to additive flag (2026-06-07).

**Worked example.** A Fast Grower at score 54 (raw), live price $100, PW Fair Value $118 (Gap Upside +18%), catalyst window 2 years (annualized gap +9%), intrinsic growth +14%/yr, shareholder yield +1% → `E` = 9 + 14 + 1 = **+24%**. Modifier = −15 × clamp((24 − 10)/15, 0, 1) = −15 × 0.93 = **−14.0**. Final score 54 − 14.0 = **40.0** → moves from "Hold / watchlist only" into "Cheap → standard position." The bright future the raw score ignored now earns the entry — exactly the gap this closes.

---

## Composite Score (Quality + Valuation)

*Added 2026-06-29 — see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](quality-scoring.md). Closes gap where two companies both passing Phase 01 look identical to the framework — only the valuation score differentiated them, so a much higher-quality business with a slightly richer multiple could lose out to a marginal one that's a touch cheaper.*

A company only reaches this step after clearing the **80.0+ Quality Score gate** ([quality-scoring.md](quality-scoring.md)) — Composite Score isn't computed for, and doesn't rescue, a company failing the quality gate.

Quality Score (0–100.0, **higher = better**) and Valuation Score (0–100.0, **lower = better/cheaper**) are inversely oriented by design (see [quality-scoring.md](quality-scoring.md) for why). Composite Score inverts Quality before blending so the result keeps the same orientation as the existing valuation score and Phase 03/05 action tables — **0 = most attractive, 100.0 = least attractive**:

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
```

Equal (50/50) weighting per explicit user decision (2026-06-29) — quality and cheapness treated as equally important rather than valuation dominating. Use the **Composite Score**, not the raw Valuation Score, against the Phase 03 Entry & Position Sizing table and the Phase 05 Dynamic Trimming table once a company has a Quality Score on file. A company not yet quality-scored (e.g. legacy holdings scored before 2026-06-29) is flagged stale until both scores exist — see the stale-score mechanism ([watchlist/README.md](../watchlist/README.md#stale-scores--when-the-scoring-methodology-changes)).

**Worked example.** Company A: Quality Score 88.0, Valuation Score 35.0 (Cheap). Company B: Quality Score 72.0 (would've failed the 80.0+ gate, never reaches this step — excluded, not blended in). Company C: Quality Score 84.0, Valuation Score 28.0 (Very Cheap):

```
Composite A = 0.50×(100−88.0) + 0.50×35.0 = 6.0 + 17.5 = 23.5
Composite C = 0.50×(100−84.0) + 0.50×28.0 = 8.0 + 14.0 = 22.0
```

Company C ranks slightly more attractive overall (22.0 vs 23.5) despite Company A's higher quality score, because C is meaningfully cheaper — the blend, not either axis alone, drives the ranking. Always show both raw scores and the composite in the session log; never report the composite alone (no black-box outputs).

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

`/screen` builds starting universe manually — TIKR/Koyfin saved-screen export, Finviz fast pass, or quality-factor ETF holdings (MOAT/QUAL/QGRW/IQLT) when screener access unavailable (see [screen.md](../.claude/commands/screen.md) Step 0). No bulk-screener API wired up; `yf.screen()` (bulk Yahoo screener) unreliable for pre-filtering — see below.

Once candidate list exists, verify each candidate's exact Phase 01 numbers with free `yfinance` Python package — no API key needed.

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

Verified against this session's manually-sourced HKEX numbers (`grossMargins` 0.965, `returnOnEquity` 0.350, `profitMargins` 0.626 — all matched stockanalysis.com to 3 decimals). `t.financials`/`t.cashflow` provide multi-year history for 3yr CAGR and "FCF positive 3 consecutive years" checks; `t.info["ebit"]`/`enterpriseValue` give EV/EBIT directly.

**Don't use `yf.screen()` (bulk Yahoo screener) for Phase 01 pre-filtering** — tested 2026-06-14, its margin/ROE/growth filter predicates didn't constrain results correctly (e.g. query requiring net margin >12% and ROE >15% still returned Woolworths, ~0.85% net margin and ~11.9% ROE). For bulk pre-filter step, continue using **structural triage from documented business-model characteristics** ([screen.md](../.claude/commands/screen.md) Step 1) to build candidate pool, then verify each candidate's real numbers with `yfinance` as above.

### `yfinance` — automated 5yr avg PE & FCF/NI conversion ratio (verified working 2026-06-20)

These two Standard Re-Score inputs were previously flagged as needing manual Macrotrends/TIKR/Koyfin pull (`operating-calendar.md`). Both now computable directly from `yfinance` — no new data source needed.

**FCF/NI Conversion Ratio** — `t.cashflow` and `t.financials` already carry both halves of this ratio; it was just never wired into a formula:

```python
fcf = t.cashflow.loc["Free Cash Flow"]
ni  = t.financials.loc["Net Income"]
fcf_ni_ratio = (fcf / ni).dropna()   # e.g. 0.70-0.90 for a healthy compounder
```
Verified against MSFT (2022-2025): 89.6%, 82.2%, 84.0%, 70.3% — 4 years, enough for the "2+ consecutive years" check in Phase 01/04.

**5yr Avg/Low/High PE** — `t.financials`' annual EPS only goes back ~4 years on free tier, too shallow for a historical PE series. `t.get_earnings_dates(limit=40)` (requires `lxml`) returns quarterly **Reported EPS** much further back (verified on MSFT: 49 quarters to 2014). Reconstruct a trailing-PE series by summing trailing-4-quarter EPS into TTM EPS, then pairing each quarter with its contemporaneous price:

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

These are **optional** — run the standard Phase 01 screen first, then run it again with discovery filters for a separate "hidden gems" pass. A company that passes Phase 01 at any market cap is worth evaluating; the discovery filters just help prioritise candidates most likely to be mispriced due to neglect.

## 5 Qualitative Questions Before Scoring

1. Why are margins high? Pricing power, scale, or lucky cycle?
2. What would it take to compete with them? (Hard = moat)
3. How has management allocated capital over 5–10 years?
4. Where is growth coming from next 3–5 years?
5. What is the best bear case against owning it?
6. Could a new delivery mechanism, platform, or technology make this moat irrelevant within 5 years? *(Disruption vector check)*

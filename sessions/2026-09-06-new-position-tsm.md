# NEW POSITION — Taiwan Semiconductor Manufacturing Co. (TSM) — 2026-09-06

**Task type:** NEW POSITION (re-evaluation, not currently held) — 4th evaluation of this ticker (07-12, 07-16, 08-10 prior)
**Date:** 06 Sep 2026 | **10Y Treasury:** 4.72% (carried from 2026-08-26 confirmation — no new reading pulled this session; still comfortably inside the 3.5–5% bracket) | **Rate Regime Modifier:** +5

> *Jargon on first use: FCF = free cash flow; ROIC = return on invested capital; EV/EBIT = enterprise value ÷ operating profit; PW = probability-weighted; E = expected annual return; MoS = margin of safety; ADR = American Depositary Receipt (TSM = 1 ADR : 5 TSMC ordinary shares); 6-K = a foreign private issuer's SEC "current report."*

---

## 1. Live Price (Rule 0) & Rule 9 Check

| Item | Value | Source |
|---|---|---|
| **Live price** | **$427.98** | IBKR live snapshot, contract 6223250 (NYSE ADR), 2026-09-06, +2.63% vs. prior close $417.01 |
| vs. 2026-08-10 ($419.13) | +2.11% | Well under the ±15% Rule 9 threshold |
| 52-week range | $239.38 – $478.89 | IBKR `misc_statistics` |
| Analyst consensus | Mean $554.45 / High $700 / Low $440 (19 analysts, "Strong Buy") | stockanalysis.com — sanity check only |

**Rule 9 trigger check since 08-10:** TSMC filed its **August 2026 monthly-revenue 6-K**: NT$250.87B, **+33% YoY**, down 2.4% MoM from July's exceptional +44.7% print — still comfortably ahead of full-year guidance ("slightly above 40%" YoY, unchanged since the Q2 call) on a trailing basis, but a real deceleration from July's outlier month. No new quarterly earnings (Q3 2026 not due until mid-October, per standing guidance: revenue $44.6–45.8B, GM 65–67%, OM 56–58%), no management change, no M&A, no new macro shift. **This is a real Rule 9 monthly-revenue trigger, addressed below** — the same category as the 08-10 session's own trigger.

---

## 2. Quality Score — carried forward, confirmed unchanged (no new quarterly filing)

All Quality Score inputs are derived from quarterly/annual financial statements — the last available quarter is still Q2 2026 (Q3 not due until mid-October). The August monthly-revenue 6-K doesn't change any TTM financial input. Per the 2026-08-10 session's full derivation:

```
Profitability_Score  = 100.0  (saturated — Net Margin 50.38%, ROIC well above ceiling)
GrossMargin_Score    = 80.29  (TTM Gross Margin 64.23%)
Growth_Score         = 85.76  (raw 75.76 [Rev 3yr CAGR 18.94%] + 10 TAM modifier, unchanged evidence)
BalanceSheet_Score   = 100.0  (Net Debt/EBITDA −0.77×, net cash — fresh stockanalysis.com read confirms
                        essentially unchanged from 08-10's −0.677×, still deeply saturated)
Moat_Score           = 80.0   (4/5 signals, unchanged — dominant ~70-72% foundry share, pricing power,
                        switching costs, scale cost advantage; brand-premium signal remains unmarked)
FCFQuality_Score     = 18.05  (TTM FCF/NI 50.83% — flagged 08-10 as a forward-looking watch item on rising
                        capex; no new quarter to re-test it against yet)

Quality Score = 100.0×0.25 + 80.29×0.15 + 85.76×0.20 + 100.0×0.15 + 80.0×0.15 + 18.05×0.10
              = 25.00 + 12.04 + 17.15 + 15.00 + 12.00 + 1.81 = 83.00
```

**Quality Score: 83.0 — passes the 80.0+ gate, unchanged from 08-10.** No hard disqualifier. Proceeding to Phase 02.

---

## 3. Valuation Score — refreshed with live price + current multiples

```
FCF Yield: TTM FCF $36,599.5M (carried, no new quarter) ÷ Market Cap ($427.98 × 5,186.474M ADR-equiv
  shares = $2,219,663M) = 1.649%
  FCF_Score = clamp(100×(1−1.649/10)) = 83.51

EV/EBIT 24.26× (stockanalysis.com, live) — cheaper than 08-10's 26.28× (EBIT grew faster than price)
  EV/EBIT_Score = clamp((24.26−12)/23×100) = 53.30

Forward PE 19.33× (stockanalysis.com) — essentially matches 08-10's Construction B/primary reading (19.24×),
  confirming that convention rather than the two alternates tested there. 5yr PE range 11.44×–26.73× (avg
  20.74×, carried from 08-10 — no new quarter to rebuild the reconstruction from).
  FwdPE_Score = clamp((19.33−11.44)/(26.73−11.44)×100) = 51.60
  Historical PE Modifier: deviation = (19.33−20.74)/20.74 = −6.8% → within ±10% → 0 (no adjustment)

PEG: still not applied — FY2023's cyclical −14.2% EPS decline remains inside the trailing 3-fiscal-year
  window (unchanged from every prior session). Weight redistributed to EV/EBIT (→ 40%).

Raw weighted = 83.51×0.40 + 53.30×0.40 + 51.60×0.20 = 33.40 + 21.32 + 10.32 = 65.04
+ Rate Environment Gate: Step 1 (EY 5.173% vs. 10Y 4.72%, spread +0.45pp < the +1.5pp pass bar) → fails,
  +5. Step 2 (regime bracket) +5. Total +10 (unchanged from 08-10).
Raw + Rate Gate = 75.04
```

**Upside/Downside Modifier — carried forward at the input level, recomputed against today's price.** No new quarter has reported since 08-10, so the underlying EPS-scenario construction (Bull $491.96 / Base $403.68 / Bear $180.00, PW Fair Value $369.83) is not independently rebuilt this session — rebuilding it from raw analyst price targets instead (mean $554.45) would use a materially different, less conservative methodology than this ticker's own established EPS×exit-multiple convention and isn't a like-for-like substitute. Recomputing only the price-dependent gap:

```
Gap Upside % = (369.83 / 427.98) − 1 = −13.59%   (worse than 08-10's −11.76% — price rose, carried FV didn't)
Annualized gap (2yr default, unchanged catalyst framing) = −13.59/2 = −6.80%/yr
Intrinsic growth = +10.0%/yr (carried, conservative) | Shareholder yield = +0.83% (carried)
E = −6.80 + 10.0 + 0.83 = +4.03%/yr
M = +5 × (10 − 4.03)/10 = +5 × 0.597 = +2.98
```

```
FINAL VALUATION SCORE = 75.04 + 2.98 = 78.02 → rounds to 78.0   (vs. 80.8 on 08-10 — slightly cheaper)
```

---

## 4. Composite Score

```
Composite = 0.50×(100−83.0) + 0.50×78.0 = 8.50 + 39.00 = 47.50
```

**Composite Score: 47.5** — stays in the **30.0–49.9 "Cheap"** band (down from 48.9 on 08-10, continuing the trend from 53.2→53.4→48.9→47.5 across all four sessions — TSM has gotten *relatively* cheaper each time, driven mainly by earnings growing faster than price, not by the stock actually falling).

---

## 5. Order Setup & R/R Gate — fails again, by a wider margin

```
Blended FV = PW Fair Value = $369.83 (carried, see §3)
MoS band for Composite 30.0–49.9: 25–30%

MoS 25%:  Buy $277.37 | Stop $208.03 (25% max loss) | R/R = (369.83−277.37)/(277.37−208.03) = 1.334:1
MoS 27.5%: Buy $268.13 | Stop $194.39 (27.5%)        | R/R = (369.83−268.13)/(268.13−194.39) = 1.379:1
MoS 30%:  Buy $258.88 | Stop $181.22 (30% max loss)  | R/R = (369.83−258.88)/(258.88−181.22) = 1.429:1
```

**R/R fails the 2:1 minimum across the entire applicable MoS range (1.33–1.43:1)** — consistent with every prior session (1.11–1.71:1 on 08-10). Live price ($427.98) sits **59–65% above** every tested buy ceiling — not a marginal miss. Per fair-value-methodology.md Step 6: *"If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."* No order placed.

---

## 6. Recommendation

**WATCHLIST ONLY — do not enter.** Composite Score (47.5) nominally sits in the "Cheap → Standard position 3–5%" band per the Phase 03 table, but the R/R gate decisively blocks entry, exactly as it has on every session since 08-10. The Composite Score keeps improving because TSMC's underlying earnings power keeps growing faster than its share price — but the share price itself remains far above any fair-value-anchored buy ceiling, so relative cheapness and absolute margin of safety continue to disagree here, a documented structural feature of this framework (see the 08-10 session's own discussion, and the MA/DB1 precedents it cites).

---

## Glossary

- **FCF** — Free cash flow.
- **ROIC** — Return on Invested Capital.
- **EV/EBIT** — Enterprise Value ÷ operating profit.
- **PW (Probability-Weighted) Fair Value** — 25% bull + 50% base + 25% bear scenario blend.
- **E (Expected annual return)** — the Upside/Downside Modifier's core input.
- **MoS (Margin of Safety)** — discount below fair value required before buying.
- **ADR (American Depositary Receipt)** — a US-listed security representing shares of a non-US company; TSM = 1 ADR : 5 TSMC ordinary shares.
- **6-K** — a foreign private issuer's SEC "current report," the filing type TSMC uses for its monthly-revenue disclosures.
- **Quality Score / Composite Score** — this framework's graded quality score (80.0+ gate) and 50/50 Quality+Valuation blend.
- **R/R (Risk/Reward ratio)** — expected gain ÷ expected loss; this framework requires ≥2:1 to enter.

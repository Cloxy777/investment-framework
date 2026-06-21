# RESCORE — UBER (Uber Technologies, Inc.)

## 1. Session header
- **Task type:** RESCORE (single ticker)
- **Date:** 2026-06-20
- **10Y US Treasury yield:** 4.44% (10-year US government bond yield; June 19 2026 close — June 20 is a Friday market holiday so this is the most recent print). Source: TradingEconomics / CNBC via web search.
- **Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% band)
- **Why this run exists:** first application of the new **Upside/Downside Modifier** (Expected-Return Modifier) added to the valuation score on 2026-06-20. UBER is a textbook case for it — a high-quality grower whose *current* multiples park it in the "Hold" band while its *forward* expected return is strong.

### Live price (Rule 0 — fetched first, never inferred)
- **Live price used: $70.91** — IBKR (Interactive Brokers) `get_price_snapshot`, `last`, contract 365207014 (NYSE primary listing), 2026-06-20 ~08:52 ET (pre-open last). Cross-check: yfinance `regularMarketPrice` $71.64 (prior close $70.91). IBKR last used as the Rule-0 primary.
- **52-week range:** $67.21 – $101.98 (IBKR misc-statistics). yfinance: $67.19 – $101.99 (consistent).
- **Analyst consensus price target (bull-case sanity):** mean $104.48, high $150.00, low $70.00, n=51 (yfinance). Used only as the analyst/DCF leg of the triangulation and as a bull-case ceiling sanity check — not as a standalone target.
- **Dividend yield:** 0.0% (UBER pays no dividend — IBKR + yfinance confirm).

## 2. Data gaps flagged
- **GAAP EPS is too distorted to score on PE.** Reported net income ($10.05B latest FY) exceeds operating income ($6.24B) because of a large deferred-tax-valuation-allowance release (tax line was a +$4.35B *benefit*, not an expense) plus equity-investment mark-to-market gains. TTM EPS history is negative for 2020–2023 and then whipsaws ($7.78 → $4.03) on one-off items. **No usable 5-year PE band exists** → Forward-PE sub-score uses the framework's **no-history fallback (50.0, flagged)**, not an invented band. (Reconstructed 14 valid TTM-PE points spanning 11.9×–99.6× — no stable mean, confirming the fallback is correct.)
- **PEG not usable.** UBER is a Fast Grower on *revenue* (17.7% 3yr CAGR) but the GAAP-EPS distortion above makes the reported PEG (5.81) meaningless. PEG treated as **Not Applicable** → its 15% weight redistributed to EV/EBIT (EV/EBIT becomes 40%), per the Final Score Formula rule.
- **Portfolio $ value not supplied** to this single-ticker run → position size given as a % band + risk-per-share; absolute share count to be set by the orchestrator against live portfolio value.
- No data was invented. Where a metric was unusable, the documented fallback was applied and flagged.

## 3. Rate Environment Gate
- **Step 1 — Earnings Yield Spread Test.** Earnings Yield (EY) = 1 ÷ Forward PE = 1 ÷ 16.22 = **6.17%**. Spread = 6.17% − 4.44% = **+1.73 percentage points (pp)**. Spread ≥ +1.5% → **PASS, no flag** (no +5 yellow-flag added).
  - *Note vs prior record:* the 2026-06-11 watchlist backfill flagged UBER as failing Step 1 under older inputs. At today's lower forward PE (16.2×) and 10Y (4.44%) it now **passes** — the +1.5pp bar is cleared.
- **Step 2 — Rate Regime Modifier:** 10Y at 4.44% sits in the 3.5–5% band → **+5** (applied after the raw weighted score).
- **Step 3 — Rate-Normalised PE:** annual January task, top-5 holdings only; UBER (0.39% weight) not in scope. N/A.

## 4. Full score calculation

All sub-scores on the 0.0–100.0 scale (0 = cheapest/most attractive, 100 = most expensive).

**Inputs (from `yfinance`, latest fiscal year unless noted):**
| Metric | Value | Notes |
|---|---|---|
| FCF (Free Cash Flow, latest FY) | $9.763B | annual; consistent period with the EBIT used below |
| FCF (TTM, yfinance field) | $6.537B | conservative cross-check (see FCF sub-score) |
| Market cap (at live $70.91) | $144.3B | 2,035.6M shares × $70.91 |
| Enterprise Value (EV) | $153.2B | net debt ≈ +$6.33B ($12.42B debt − $6.09B cash) |
| EBIT (Earnings Before Interest & Taxes, latest FY) | $6.24B | |
| Forward PE (Price/Earnings) | 16.22× | |
| Revenue CAGR 3yr | 17.7% | $31.9B → $52.0B |
| ROE (Return on Equity) | 35.3% | |
| Gross margin | 39.6% | |
| Net margin | 15.9% | |
| FCF/NI (cash conversion) | 0.97 / 0.70 / 1.78 latest 3 FY | healthy (>0.70), latest years distorted by the tax/equity items noted above |

**Sub-score 1 — FCF Yield (40% weight).**
FCF Yield (Free Cash Flow ÷ market cap) = $9.763B ÷ $144.3B = **6.76%** (annual basis; matches the 2026-06-07 record's 6.77% and uses the same period as EBIT).
`FCF_Score = clamp(100 × (1 − 6.76/10), 0, 100)` = 100 × 0.324 = **32.4**
- *Downside sensitivity (flagged):* on the more conservative TTM FCF ($6.54B → 4.53% yield), FCF_Score would be 54.7. Using the annual basis for period-consistency with EBIT and continuity with the prior session; the TTM figure is the bear-leaning alternative.

**Sub-score 2 — EV/EBIT (now 40% weight — absorbs PEG's 15%).**
EV/EBIT = $153.2B ÷ $6.24B = **24.55×**
`EV/EBIT_Score = clamp((24.55 − 12)/23 × 100, 0, 100)` = **54.6**

**Sub-score 3 — Forward PE (20% weight).** No-history fallback (GAAP EPS too distorted, no stable 5yr band) → **FwdPE_Score = 50.0 (flagged).**

**Sub-score 4 — PEG (15% weight):** Not Applicable (see data gaps) → weight redistributed to EV/EBIT.

**Raw weighted score:**
`(32.4 × 0.40) + (54.6 × 0.40) + (50.0 × 0.20)`
= 12.96 + 21.84 + 10.00 = **44.78**

## 4b. Upside/Downside Modifier (Expected-Return Modifier) — REQUIRED

**Step 1 — scenario-weighted fair value (Rule 7) and Gap Upside (Rule 0 live price).**

Sector = Technology / Growth → Rule 1 method = DCF + multiples, triangulated. Each scenario blends a multiples leg (60%) and an analyst/DCF leg (40%) per the methodology's triangulation weighting.

Multiples leg — fair EV/EBIT applied to forward EBIT, then EV→equity (subtract $6.33B net debt, ÷ 2,035.6M shares):
| Scenario | Fwd EBIT | Fair EV/EBIT | Multiples FV |
|---|---|---|---|
| Bear | +8% → $6.74B | 18× | ~$56 |
| Base | +18% → $7.36B | 24× | ~$84 |
| Bull | +25% → $7.80B | 28× | ~$104 |

Analyst/DCF leg — consensus band: bear $70 (low PT), base $104.48 (mean PT), bull $150 (high PT).

Triangulated FV per scenario = 0.40 × analyst leg + 0.60 × multiples leg:
- **Bear ≈ $61.9 · Base ≈ $92.0 · Bull ≈ $122.5**

`PW Fair Value = 0.25×122.5 + 0.50×92.0 + 0.25×61.9` = **$92.1**
`Gap Upside % = (92.1 ÷ 70.91) − 1` = **+29.9%**

**Catalyst & timeline (Rule 10):** documented catalysts within 18–24 months — (a) autonomous-vehicle (AV, self-driving) partnership monetization scaling across the platform, (b) Delivery and Advertising segment margin expansion, (c) ongoing GAAP profitability inflection feeding the next 2–3 earnings prints. → use the **2-year** window (no narrower single dated event). Catalyst exists within 18–24mo → upside-credit guardrail satisfied; the −5 upside cap does **not** apply.

`Annualized gap = 29.9% ÷ 2 = +14.95 pp`

**Step 1 — Expected annual return E (three components):**
- Annualized valuation-gap closure: **+14.95 pp**
- Intrinsic growth (forward FCF/EPS CAGR; conservative vs the 17.7% revenue CAGR): **+12 to +15 pp** (use +15)
- Shareholder yield (dividend 0% + estimated net buyback ≈ +1%): **+1 pp**

`E = 14.95 + 15 + 1` = **+30.95% / yr** (≈ +31%).
*Sensitivity:* even cutting intrinsic growth to +10pp gives E ≈ +26%, still ≥ the +25% full-floor threshold — the modifier is robust to this assumption.

**Step 2 — Map E to modifier (hurdle H = 10%):**
E ≥ H, so `M = −15 × clamp((E − H)/15pp, 0, 1)` = −15 × clamp((30.95 − 10)/15, 0, 1) = −15 × clamp(1.40, 0, 1) = −15 × 1.0 = **−15.0** (floor; E ≥ 25%/yr earns the full credit).

Guardrails checked: (1) catalyst within 18–24mo → upside credit allowed; (2) used bull/base/bear PW FV, not the rosy point; (3) full calc shown above; (4) modifier bounded at the −15 floor by design.

**Upside/Downside Modifier = −15.0.**

## 5. Final score + action

`Final = raw 44.78 + Rate Regime Modifier (+5) + Upside/Downside Modifier (−15.0)` = **34.78 → 34.8** (rounded to 0.1).

| | Value |
|---|---|
| Raw weighted | 44.8 |
| Rate Regime Modifier | +5 |
| Upside/Downside Modifier | −15.0 |
| **FINAL SCORE** | **34.8** |
| Prior score (2026-06-07, rescaled) | 52.9 |

**Action band:** Score 30.0–49.9 → **BUY — Standard position (3–5% of portfolio)**.
**Action CHANGED:** prior 52.9 = HOLD/watch-only → now 34.8 = BUY-standard. This is precisely the gap the Upside/Downside Modifier was built to close: UBER's current multiples alone (raw 44.8 + rate, ~49.8) sit in/near the Hold band, but its strong forward expected return (E ≈ +31%/yr) pulls it a full band down into the entry zone.

## 6. Order setup (BUY action) — with the binding R/R caveat

| Item | Value |
|---|---|
| Blended Fair Value (base case) | **$92.0** |
| Bull-case Fair Value | $122.5 |
| Margin of Safety (MoS), Score 30–49.9 band | 28% |
| Buy Price = $92.0 × (1 − 0.28) | **$66.24** |
| Primary Sell Target (= base FV) | **$92.0** |
| Bull-case Trim Target (= bull FV × 0.90) | **$110.25** |
| Stop Loss (28% below buy) | **$47.69** |
| Risk per share (buy − stop) | $18.55 |

**Risk/Reward gate — FAILS 2:1 at the framework-required MoS/stop bands.**
- R/R at buy price $66.24 with 28% stop = (92.0 − 66.24) ÷ (66.24 − 47.69) = **1.39:1**.
- Best achievable within the *allowed* standard-position bands (MoS 30% / stop 25%) = **1.71:1** — still below 2:1.
- R/R reaches exactly **2:1 only at an entry of ~$61.33** (with a 25% stop at $46.00). That entry implies a ~33% MoS, deeper than the standard band.

**Per Step 6 ("if R/R below 2:1: wait for lower entry"), the actionable instruction is a LIMIT order, not a market buy:**
- **Set a limit buy at ≈ $61.30** (with stop $46.00) to enter only where R/R ≥ 2:1. Live price $70.91 is **above** even the 28%-MoS buy price ($66.24), so no immediate entry is warranted regardless.
- The score says the *name* qualifies (BUY-standard); the *price* does not yet meet entry discipline. Net: **place the limit order and wait** — do not chase at $70.91.

**Position size (band):** Score 30–49.9 → cap 3–5% of portfolio; current weight 0.39% → meaningful headroom. Risk per trade = 1.5% of portfolio. Shares = (1.5% × portfolio value) ÷ $18.55 risk-per-share at the $66.24 setup (or ÷ $15.30 at the $61.30 / 2:1 setup), capped at the lower of risk-based size and the 5% allocation cap. **Absolute share count deferred to the orchestrator** (portfolio $ value not supplied to this run). Single-position hard cap (Upgrade 7) 15% — not a constraint here.

## 7. Next review trigger
- **Next earnings (~early August 2026)** → mandatory standard re-score (Rule 9).
- **Limit-order trigger:** price into the ~$61.30 zone → R/R clears 2:1, execute the buy and log in `decisions/`.
- **Rule 9 interim triggers:** guidance revision, AV-partnership material news, >15% unexplained price move, or 10Y regime change crossing a band boundary (e.g. below 3.5% → modifier flips to 0).
- **Note for next run:** revisit the FCF-yield basis (annual $9.76B vs TTM $6.54B) once a clean post-earnings FCF print removes the working-capital noise; the choice swings FCF_Score between 32.4 and ~54.7 and is the single largest input sensitivity in this score.

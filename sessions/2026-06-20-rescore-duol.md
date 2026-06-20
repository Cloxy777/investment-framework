# RESCORE — DUOL (Duolingo, Inc.) — 2026-06-20

**Task type:** RESCORE (single ticker) — first run to apply the new **Upside/Downside Modifier** (Expected-Return Modifier, added to the valuation score 2026-06-20)
**Date:** 20 Jun 2026
**10Y US Treasury Yield:** 4.46% (FRED DGS10 / Fed H.15, 18 Jun 2026 — most recent available; WebSearch)

> **⚠️ Post-session correction (2026-06-20): PEG treatment reverted, score of record is 53.7, not 50.7.** This session applied PEG live as a Fast Grower. The same day, the PEG eligibility rule was clarified: the "EPS growth >15% for 3+ years" gate requires a *reliable, non-distorted* earnings base, which DUOL lacks (recently GAAP-profitable; TTM EPS distorted by the FY2025 deferred-tax release). PEG's 15% is therefore **redistributed to EV/EBIT** (reverting to the 2026-06-12 treatment). Corrected calc: 30.74×0.40 + 74.24×0.40 + 50.0×0.20 = raw **51.99**, + Rate +10 − Upside/Downside 8.25 = **53.7**. Still HOLD (Fair Value band) — action unchanged. The body below reflects the original live-PEG calc (50.7); read it with this correction in mind. See [decisions/2026-06-20-framework-clarification-peg-clean-earnings.md](../decisions/2026-06-20-framework-clarification-peg-clean-earnings.md).
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current DUOL portfolio weight:** 8.46% (per holdings.md / last sync) — existing holding, last scored **55.6** (2026-06-12)
**Sector:** Technology — Education Software (EdTech / language-learning app)

> **Why this session exists:** This is a deliberate re-score to apply the **Upside/Downside Modifier** (a new additive term, −15 … +15, that folds *expected forward return* into the single valuation score — see [valuation-scoring.md](../framework/valuation-scoring.md#upsidedownside-modifier-expected-return-modifier)). DUOL is a useful first live test: a richly-valued, high-growth name where the four bottom-up cheapness sub-scores alone parked it in the "Fair Value / Hold" band, and the question is whether its forward expected return justifies pulling the score down toward an entry. Prices were refreshed live (Rule 0); the fair-value scenario work from the 2026-06-12 session is reused where still valid and re-sanity-checked against current analyst targets.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$125.56** | `yfinance` intraday (`currentPrice`/`regularMarketPrice`), 20 Jun 2026 — open $123.50, day range $121.10–$126.66, prior close $123.39. IBKR `get_price_snapshot` (conid 505002183, NASDAQ) was attempted first per the brief but the call was permission-denied this session, so `yfinance` is the live source. |
| Prior close (19 Jun) | $123.39 | `yfinance` |
| 52-week high | $472.12 | `yfinance` `fiftyTwoWeekHigh` (all-time high was ~$544.93 on 14 May 2025, outside the trailing 52-week window from today) |
| 52-week low | $87.89 | `yfinance` `fiftyTwoWeekLow` (reached ~March 2026 on the AI-disruption scare) |
| Analyst consensus PT (12-mo) | **mean $106.31 / median $101.00**, range $81–$145, 17–23 analysts, consensus rating "Hold" | `yfinance` (`targetMeanPrice` $106.31, `targetMedianPrice` $101, `numberOfAnalystOpinions` 17) + WebSearch (S&P Global aggregation, 23 analysts) |

**Context:** DUOL is up modestly from the 2026-06-12 session ($119.24 → $125.56, +5.3%). The stock remains far below its May-2025 all-time high (~$545) after the 2025-2026 AI-disruption drawdown, and notably the **live price ($125.56) now sits ~18% above the analyst consensus mean PT ($106.31)** — i.e. the sell-side currently sees DUOL as modestly *over* its 12-month target. That tension is exactly what the new modifier is meant to surface honestly.

---

## 2. Data Gathered (Standard Re-Score inputs) & Gaps Flagged

All figures computed from `yfinance` annual + quarterly statements (verified method per valuation-scoring.md), rolled forward to TTM (trailing-twelve-month). Quarters: Q2'25, Q3'25, Q4'25, Q1'26.

| Metric | Value | Source / Derivation |
|---|---|---|
| Q-by-Q Revenue ($M) | Q2'25 252.26 / Q3'25 271.71 / Q4'25 282.87 / Q1'26 291.97 | `yfinance` quarterly_financials |
| **TTM Revenue** | **$1,098.81M** | Sum of the four quarters above |
| Q-by-Q EBIT (operating income, $M) | 33.36 / 35.16 / 43.45 / 44.53 | `yfinance` quarterly_financials |
| **TTM EBIT** | **$156.50M** | Computed |
| Q-by-Q Net Income ($M) | 44.78 / **292.19** / 41.95 / 43.46 | `yfinance` — Q3'25 carries the **$256.7M one-off deferred-tax valuation-allowance release** |
| **TTM Net Income (reported)** | **$422.38M** | Computed — tax-inflated (see Gap #1) |
| **TTM Net Income (ex one-off tax benefit)** | **≈$165.68M** | $422.38M − $256.7M |
| **TTM net margin (reported / ex-tax)** | **38.44% / 15.08%** | Computed — clean ex-tax basis clears Phase 01 >15% by a hair |
| Gross margin (TTM) | ~72.7% | `yfinance` `grossMargins` 0.7267 |
| Q-by-Q FCF ($M) | 86.32 / 77.36 / 93.73 / 147.79 | `yfinance` quarterly_cashflow (FCF = operating cash flow − capital expenditure) |
| **TTM Free Cash Flow** | **$405.20M** | Computed (vs $414.5M in the 2026-06-12 session — the TTM window has rolled forward one quarter, dropping the strong Q1'25 $103.0M and the difference reflects the exact quarterly roll, not a deterioration) |
| **TTM FCF/NI conversion** | 95.9% reported (244.6% ex-tax-benefit NI) | Both >70% — passes Phase 01/04, but see Gap #1: the ratio is not a meaningful *quality* signal this year because the NI denominator is tax-distorted |
| Cash + ST + LT investments (31 Mar 2026) | $1,138.561M + $113.049M + $140.211M = **$1,391.82M** | Q1'26 10-Q (per 2026-06-12 session); `yfinance` cash+ST = $1,251.61M consistent |
| Total debt (lease obligations) | **$91.87M** | `yfinance` `totalDebt` (operating-lease liabilities; the 2026-06-12 session treated this as $0 — this session conservatively *includes* it, which slightly lowers net cash and raises EV) |
| **Net cash** | **$1,299.95M** | $1,391.82M − $91.87M |
| Shares outstanding | **46.59M** (basic; ~48.8M diluted Q1'26) | `yfinance` `impliedSharesOutstanding` 46,593,117 (matches marketCap÷price exactly); `sharesOutstanding` field 40.24M is **stale/inconsistent with yfinance's own marketCap** and was discarded — see Gap #2 |
| **Market Cap** (at $125.56) | 46.593M × $125.56 = **$5,850.2M** | Computed (matches `yfinance` `marketCap` $5,850.2M) |
| **Enterprise Value** | $5,850.2M − $1,299.95M = **$4,550.3M** | Computed |
| **EV/EBIT (TTM)** | $4,550.3M ÷ $156.50M = **29.08×** | Computed |
| **FCF Yield (TTM)** | $405.20M ÷ $5,850.2M = **6.93%** | Computed |
| Revenue CAGR 3yr (FY22→FY25) | 41.08% | (1,037.59/369.50)^(1/3) − 1, FY revenue per `yfinance` |
| ROIC | ~37–51% (high, volatile, tax-sensitive) | `yfinance` `returnOnEquity` 0.370; clears >15% comfortably under any plausible denominator (asset-light, net cash) — same caveat as 2026-06-12 |
| FY2026 consensus GAAP EPS | **$2.95** (primary; cluster $2.95–$3.08, one outlier at $5.00) | WebSearch — down from a prior $4.34 estimate; used $2.95 (most recent/conservative), $3.08 as sensitivity |
| **Forward PE** (at $125.56 / $2.95) | **42.56×** ($3.08 → 40.77×) | Computed |
| 5yr avg/range PE | **None usable** — see Gap #3 | `yfinance` `get_earnings_dates` returns only 16 reconstructable TTM-EPS quarters (<20 = 5yr), and the TTM-EPS series is dominated by the Q3'25 tax distortion (jumps to >10) and uses non-GAAP "reported" beats |

### Data Gaps / Flags
1. **FY2025/TTM net income and FCF/NI conversion remain distorted by the one-off $256.7M deferred-tax valuation-allowance release** (booked Q3'25). TTM net margin reads 38.44% reported vs ≈15.08% ex-tax; FCF itself ($405.20M TTM) is cash-based and **unaffected** — it is the figure used in all Phase 02 cash metrics. The FCF/NI ratio should not be read as a quality red flag this year.
2. **Share-count resolution:** `yfinance`'s `sharesOutstanding` field (40.24M) is internally inconsistent with its own `marketCap` ($5.85B at $125.56 implies 46.59M). Used `impliedSharesOutstanding` = **46.59M** (basic, matches marketCap exactly and the 2026-06-12 session). This matters: at 40.24M, EV/EBIT would read ~24.0× vs the correct ~29.1×. No data invented — the inconsistent field was identified and discarded in favour of the internally-consistent one.
3. **5yr PE history still not usable → FwdPE_Score = 50.0 (no-history fallback, flagged)** — consistent with all prior DUOL sessions. DUOL IPO'd Aug 2021, and the reconstructable EPS series is both too short (<20 quarters) and tax-distorted to yield a meaningful historical multiple band.
4. **Fast Grower / PEG classification — applied as a live sub-score this session** (per the run's directive that DUOL is a high-growth Fast Grower; Upgrade 3). This differs from the 2026-06-12 session, which treated DUOL as *not* a confirmed Fast Grower on the strict GAAP-EPS test (EPS declining FY26) and redistributed PEG's 15% to EV/EBIT. **Resolution this session:** PEG is computed live using a **forward revenue-growth proxy of 27%** (current TTM revenue growth — deliberately more conservative than the 41% 3yr CAGR). The strict-EPS-test path (PEG N/A, 15% → EV/EBIT) is shown as sensitivity in §5; both land in the **same HOLD band**, so the recommendation is not sensitive to this call — but the general rule (revenue-CAGR proxy vs strict EPS test) remains an open framework question worth resolving once globally rather than per-session.
5. **IBKR live-price tool was permission-denied** this session; `yfinance` was used as the Rule 0 live source instead. Price is intraday-tagged, not a prior close.

---

## 3. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 42.56 = 2.3495%
Spread = EY − 10Y = 2.3495% − 4.46% = −2.1105%
```
Pass threshold ≥ +1.5%. **FAIL** (−2.11%) → **+5 additive** (yellow flag, not a veto, per the 2026-06-07 change).

**Step 2 — Rate Regime Modifier:** 10Y = 4.46% → "3.5–5%" bracket → **+5**.

**Total Rate Modifier = +10** (both halves applied additively, consistent with the 2026-06-12 session).

---

## 4. Phase 02 — Full Score Calculation

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 6.93/10), 0, 100) = 30.74
```
→ 30.74 × 0.40 = **12.30**

**EV/EBIT — 25% weight**
```
EV/EBIT_Score = clamp((29.08 − 12)/23 × 100, 0, 100) = 74.24
```
→ 74.24 × 0.25 = **18.56**

**Forward PE (no-history fallback) — 20% weight**
```
FwdPE_Score = 50.0   (no usable 5yr PE history — Gap #3, flagged)
```
→ 50.0 × 0.20 = **10.00**

**PEG — 15% weight (Fast Grower, Upgrade 3)**
```
PEG       = Forward PE ÷ growth = 42.56 ÷ 27 = 1.58   (growth = 27% TTM revenue growth proxy — see Gap #4)
PEG_Score = clamp((1.58 − 0.5)/2.0 × 100, 0, 100) = 53.82
```
→ 53.82 × 0.15 = **8.07**

```
Raw weighted score = 12.30 + 18.56 + 10.00 + 8.07 = 48.93
```

---

## 5. Upside/Downside Modifier (Expected-Return Modifier) — the focus of this run

**Step 1 — Expected annual return `E`** (built from Rule 7 scenario fair value + Rule 10 catalyst window; no new data source):

*Scenario fair values* — the 2026-06-12 intrinsic DCF (probability-weighted ≈$196) runs **well above** the analyst consensus PT range ($81 low / $101 median / $106 mean / $145 high) and above the blended FV ($153). Per Rule 4 (sanity check) and Guardrail #2 (scenario-weighted, never the rosy point), the scenario set below **triangulates the intrinsic DCF with the market/analyst reality and underwrites the bear case honestly** — the bear anchors near the analyst low and the 52-week low ($87.89), reflecting the still-live AI-disruption / DAU-deceleration thesis:

| Scenario | Weight | Fair Value | Rationale |
|---|---|---|---|
| Bull | 25% | $200 | AI-content thesis proves out, DAU growth holds >20%, multiple re-rates (below the intrinsic DCF bull of $259, above the $145 analyst high) |
| Base | 50% | $140 | Modest re-rating; between blended intrinsic FV ($153) and the analyst-implied zone |
| Bear | 25% | $90 | AI disruption partly validated, DAU/conversion decel; near analyst low ($81) and 52-wk low ($87.89) |

```
PW Fair Value = 0.25×200 + 0.50×140 + 0.25×90 = $142.50
Gap Upside %  = (142.50 ÷ 125.56) − 1 = +13.49%
```

*Catalyst & timeline (Rule 10):* the price↔FV gap closes on **Q2 FY2026 earnings (~early Aug 2026)** as the near-term proof point, with full re-rating over a ~2-year window → use **2 years** (no narrower window claimed).
```
Annualized gap = 13.49% ÷ 2 = +6.75%
```

*Three components of E:*
```
Annualized gap      = +6.75%
Intrinsic growth    = +14%   (forward FCF growth proxy: between FY26 bookings guide 10–12% and revenue guide 15–18%; conservative vs FY25's +35% FCF — growth is decelerating by design)
Shareholder yield   = −2.5%  (≈ +1% buyback − ~3.5% stock-based-comp dilution = net dilutive; DUOL pays no dividend)
E = 6.75% + 14% − 2.5% = +18.25%
```

**Step 2 — Map E to the modifier** (hurdle H = 10%):
```
E = 18.25% ≥ H → M = −15 × clamp((18.25 − 10)/15, 0, 1) = −15 × 0.55 = −8.25
```

**Guardrails applied:**
- *Catalyst present* (Q2 FY26 + re-rating, within the 18–24mo window) → upside credit allowed, the −5 cap does **not** bind.
- *Scenario-weighted, bear underwritten* — bear anchored near 52-wk low / analyst low, not the rosy DCF.
- *Full calc shown* (above). *Modifier, not veto* — bounded ±15.

```
Upside/Downside Modifier = −8.25
```

The modifier is **negative** (toward buy) because E exceeds the 10% hurdle — but materially smaller than a naive DCF-only reading would give (~−14), precisely because the bear case is underwritten against the live AI-disruption risk and the consensus-PT reality that the stock trades *above* its 12-month target.

---

## 6. Final Score & Action

```
Final Score = 48.93 (raw) + 10 (Rate Modifier) − 8.25 (Upside/Downside Modifier) = 50.68 → 50.7
```

# Final Score: 50.7 → Action: HOLD — Fair Value band (50.0–69.9), no new entry, no trim

**Prior score: 55.6 (2026-06-12). Change: −4.9. Action band: UNCHANGED (HOLD).**

What moved the score down from 55.6 to 50.7:
1. **The new Upside/Downside Modifier (−8.25)** — DUOL's forward expected return (E = +18.25%) is above the 10% hurdle, so the modifier credits the upside and pulls the score down ~8 points. This is the modifier doing exactly its job: a high-grower whose bottom-up multiples alone parked it mid-band gets pulled toward (but, correctly, not into) the entry band because its expected forward return is genuinely above-hurdle even after honestly haircutting the bear case.
2. Partly offset by the raw weighted score being slightly higher than the comparable prior figure (EV/EBIT 29.08× here vs 26.60× on 2026-06-12 — driven by the higher price, this session conservatively including the $91.87M lease debt in EV, and the PEG sub-score replacing the redistributed EV/EBIT weighting).

The net effect lands at **50.7 — still inside the Fair Value / HOLD band by a small margin.** This is the intended, disciplined behaviour: the modifier is bounded and asymmetric so optimism *informs but does not override* the bottom-up cheapness gate — a 42× forward-PE name in a 4.46% rate environment is not allowed to jump into "Buy" on a forecast alone.

---

## 7. Order Setup

**Not applicable** — Score 50.7 is in the **HOLD / Fair Value band (50.0–69.9)**: no new entry, no trim (per the Action Table and fair-value-methodology.md Step 2, "No MoS → Watchlist only"). No buy price, stop, or position-size order is generated. Context numbers:

```
PW Fair Value (scenario)     = $142.50   (vs live $125.56 → +13.5% to PW FV)
Blended FV (2026-06-12 work)  = ~$153.11  (40% intrinsic DCF $195.89 / 60% multiples avg $124.59) — runs above analyst consensus
Analyst consensus PT          = $106.31 mean / $101 median  (stock currently trades ABOVE consensus)
Current position              = 8.46%  | 15% cap headroom ≈ 6.54pp
Action                        = MAINTAIN current size — no add (score doesn't support entry), no trim (well below 70.0 trigger)
```

---

## 8. Next Review Trigger

- **Q2 FY2026 earnings (~early August 2026)** — mandatory Rule 9 re-score and the primary catalyst underwriting the Upside/Downside Modifier's annualized-gap term. Specifically check: DAU (daily-active-user) growth holding ≥~20% (the guided floor Q1 beat), paid-subscriber growth tracking DAUs (no conversion-rate compression), and FCF/EBIT trajectory vs this session's TTM figures (FCF $405.20M / EBIT $156.50M). If the bear case (AI disruption / DAU decel) starts to validate, the bear-scenario FV ($90) and thus E and the modifier would move materially toward the positive (trim) side.
- **>15% unexplained price move from $125.56** in either direction → immediate Rule 9 re-score (DUOL has shown 80%+ swings within 13 months).
- **Resolution of the Fast Grower / PEG question (Gap #4)** — strict EPS test vs revenue-CAGR proxy — to be settled once globally rather than re-decided per session.
- **No position change made by this session.** holdings.md Last Score / Last Review for DUOL to be updated by the orchestrating session to **50.7 / 20 Jun 2026** (orchestrator handles holdings.md — not edited here).

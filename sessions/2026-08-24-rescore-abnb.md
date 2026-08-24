# RESCORE — ABNB (Airbnb, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-08-24
**10Y US Treasury Yield:** 4.71% (TradingEconomics.com, "Monday" reading as of this session — 10Y retreated from a ~4.74% 20-month-high print earlier in the week after Fed Governor Warsh's Jackson Hole remarks)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)

> ⚠️ **Scope note — ABNB is not a current holding.** `/rescore` is written for the quarterly post-earnings re-score of existing portfolio positions; ABNB does not appear in [holdings.md](../portfolio/holdings.md) (0% weight). It was evaluated once before via `/new-position` on [2026-06-07](2026-06-07-new-position-abnb.md) (old 1–10 scale, Score 6 "Fair Value" → **WATCHLIST ONLY, no entry**) but — a pre-existing gap in this framework's records — no `watchlist/not-in-portfolio/ABNB/` file was ever created at the time, so ABNB has been invisible to the watchlist index since. Since it was explicitly named for this session, this run proceeds as a full fresh evaluation under the **current** methodology (Quality Score + Composite Score didn't exist in June), backfilling the missing watchlist entry rather than updating `holdings.md` (no row exists there to update). Treat this as functionally equivalent to a `/new-position` re-run, logged as a rescore per the request.

**Last review on record:** ABNB **Score 6 ("Fair Value")** on the old 1–10 scale (≈55.6 on today's 0–100.0 scale per the [conversion table](../framework/valuation-scoring.md#converting-legacy-110-scores)) — 2026-06-07, [sessions/2026-06-07-new-position-abnb.md](2026-06-07-new-position-abnb.md). No Quality Score or Composite Score existed at that time (added 2026-06-29). Recommendation then: **WATCHLIST ONLY — pass on entry.**

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$187.30** | IBKR `get_price_snapshot` (contract_id 459530964, NASDAQ), `last`, `is_close: true` — most recent completed regular session. Cross-checked against Yahoo Finance `regularMarketPrice`: **$187.30**, exact match. |
| 52-week range | $110.81 – $189.20 | IBKR `misc_statistics` — price sits just **1.0% below its 52-week high**, a very different starting point than the June session's "roughly mid-range" read. |
| Price vs. 2026-06-07 review ($133.72) | **+40.1%** | A large move, but not an unexplained one — see §2 fundamental-changes note: two quarters of beat-and-raise earnings plus an active $6B buyback are the documented drivers, not an untriggered Rule 9 event. |
| Analyst consensus PT (Rule 0 Step 4, bull-case sanity check) | Mean **$175.50** / Median **$175.00** (39 analysts, high $215 / low $125) | Yahoo Finance `financialData`. **Current price ($187.30) sits *above* both the mean and median sell-side target** — an independent cross-check pointing the same direction as this session's own valuation work below (§7 Rule 4 sanity check). |

---

## 2. Data Gaps / Flags

1. **`yfinance` (`curl_cffi` transport) failed with the same recurring TLS-impersonation `SSLError` documented elsewhere in this repo.** Worked around with the standard `requests.Session()` + browser `User-Agent` + Yahoo cookie/crumb fix, pulling `quoteSummary` and `fundamentals-timeseries` endpoints directly. All figures below sourced this way, cross-checked against IBKR where both cover the same field (price, 52-week range).

2. **Yahoo's `sharesOutstanding` field (419.5M) is clearly wrong** — it doesn't reconcile with `marketCap ÷ price` (**598.8M**, back-solved) or with TTM EPS math (`trailingEps` $4.38 × ~614M diluted shares ≈ TTM net income $2.691B). Likely a known Yahoo quirk under-counting one of ABNB's Class A/B/C share tranches. **Used the back-solved ~598.8M (basic, for market cap/EV) and ~614M (diluted, cross-checked via TTM EPS) instead of the vendor field**, flagged rather than silently substituted.

3. **`annualDilutedEPS` for FY2025 returned $1.03 — a data artifact, not used.** That figure exactly matches the *quarterly* diluted EPS Yahoo separately reports for Q2 2025 (2025-06-30), strongly suggesting an index-misalignment bug in Yahoo's timeseries API rather than the real FY2025 annual figure. Real FY2025 diluted EPS, cross-checked via Net Income ($2.511B) ÷ ~614M diluted shares ≈ **$4.08–4.11**, consistent with the 2026-06-07 session's independently-sourced **$4.11** FY2024 figure and this session's **$4.38** TTM figure. Used the cross-checked figure; flagged the vendor field as unreliable rather than trusting it.

4. **FCF Yield — two legitimate but materially different bases, both shown (see §6).** Yahoo's own TTM `freeCashflow` field ($3.207B, quarters ending Q3'25–Q2'26) sits **$1.65B below** the same-window `operatingCashflow` ($4.86B) despite ABNB's real capex historically running near-zero (~$25M/yr, last disclosed 2021–2022). That gap is far too large to be genuine capex — it most likely reflects a working-capital swing in ABNB's guest-payment "funds receivable and amounts held on behalf of customers" float account (guest payments collected before host payouts, which the June 2026 session also flagged as a structural feature of this business), not a real reduction in underlying cash-generating power. **Primary basis used below: FY2025 full calendar year FCF = OCF = $4.646B** (a complete, non-seasonal-partial window, consistent with "FCF ≈ OCF, no meaningful growth capex" established in the June session). The TTM $3.207B figure is shown as an explicit robustness/sensitivity check in §6 rather than silently discarded.

5. **Historical PE Modifier — carried forward as a genuine data gap, not re-derived from scratch.** The June 2026 session found ABNB's only available multi-year PE average (~37×, "4yr") statistically unusable — built from a 16×–132× range spanning the 2021–22 unprofitable-to-profitable transition and a one-time Q3 2023 EPS spike (a $2.8B tax-valuation-allowance release). The current trailing-5-year window (Aug 2021–Aug 2026) **still contains both distorting episodes** — confirmed this session, not re-fetched wholesale (see §7 for the specific reasoning, unchanged from June). **No-history fallback applied: FwdPE_Score = 50.0, flagged.**

6. **Peer comp set for the Multiples-Based Fair Value (§8) uses 3 peers (BKNG, EXPE, UBER), short of Rule 5's "minimum 5."** No 4th–5th close comp was readily available this session without introducing weaker analogues (hotel-only OTAs with a fundamentally different asset/marketing model). Flagged as a limitation, not silently treated as a full comp set.

---

## 3. Quality Score (Phase 01 — full recompute, first time for ABNB)

**Hard disqualifier checks (all must clear before the weighted score matters):**

| Check | ABNB (TTM / FY2025) | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years | FY2022 181%, FY2023 81%, FY2024 171%, FY2025 185%, TTM 119% (Yahoo TTM FCF) — every year ≥70% | Fail if <70% for 2+ yrs | ✅ CLEAR |
| Net Debt/EBITDA over threshold | **Net cash** (Total debt $2.496B vs. Total cash $12.069B → net cash $9.573B) | <2.5× (or <4× asset-light override) | ✅ CLEAR — trivially, net cash position |
| Not FCF-positive for 3+ consecutive years | Positive every year, FY2022–FY2025 (4 years) | Fail if not | ✅ CLEAR |

No hard disqualifier fires. Proceeding to the weighted score.

**Sub-scores:**

**Profitability (25% weight)**
```
Net Margin (TTM) = Net Income to Common $2.691B ÷ Revenue $13.159B = 20.4%
ROIC = NOPAT ÷ Invested Capital
  EBIT (FY2025) = $2.544B;  Net Income (FY2025) = $2.511B
  Implied effective tax rate = (2.544 − 2.511) / 2.544 = 1.3%  ← near-zero, NOL-shield driven (see caveat below)
  NOPAT = 2.544B × (1 − 0.013) = $2.511B
  Invested Capital (FY2025) = $10.198B
  ROIC = 2.511 / 10.198 = 24.6%

NetMargin_Component = clamp((20.4/30)×100) = 68.0
ROIC_Component       = clamp((24.6/30)×100) = 82.0
Profitability_Score  = (68.0 + 82.0) / 2 = 75.0   (no FCF cap — 4yr positive)
```
⚠️ **ROIC caveat:** ABNB's near-zero effective tax rate reflects large net-operating-loss carryforwards from its pre-2021 unprofitable years being utilized to shelter current income — a real, disclosed, but **temporary** tailwind. Once those NOLs are exhausted, cash taxes (and therefore this ROIC figure) will likely step down toward a statutory-rate basis (~21–25%), which would pull ROIC toward ~19–20% and Profitability_Score down a few points. Not adjusted for here (using the actual reported relationship, not a hypothetical), but worth tracking at the next review. Cross-checks closely against the June session's independently-derived **24.89%** ROIC.

**Margins (15% weight)**
```
Gross Margin (TTM) = Gross Profit $10.909B ÷ Revenue $13.159B = 82.9%
```
| Year | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Gross margin | 82.2% | 82.8% | 83.1% | 83.0% |

Flat, not structurally expanding — but already well above the 80% cap. **No trend bonus needed.**
```
GrossMargin_Score = clamp((82.9/80)×100) = 100.0
```
⚠️ This **82.9%** figure materially disagrees with the **72.38%** the June 2026 session reported. Re-verified directly from primary Gross Profit/Revenue line items across all 4 available fiscal years (table above) — all cluster tightly at 82–83%, consistent with Airbnb's widely-reported real-world gross margin. The June figure appears to have been a sourcing error at the time; this session's number is used, flagged rather than silently overwritten without explanation.

**Growth (20% weight)**
```
Revenue 3yr CAGR = (Revenue FY2025 $12.241B / Revenue FY2022 $8.399B)^(1/3) − 1 = 13.4%
Growth_Score (base) = clamp((13.4/25)×100) = 53.6
```
TAM/pricing-power modifier — **+10 applied**, on two independent, cited pieces of evidence:
- **Third-party TAM growth:** the global Alternative Accommodation Market is sized at $218.4B (2026) and projected to reach $540.8B by 2035 (10.6% CAGR) — MarkWide Research / market.us, Aug 2026 — genuine external market-growth evidence, not company guidance.
- **Reacceleration, not continued deceleration:** Q2 2026 revenue grew +17% YoY (GBV +16% YoY) — *above* the trailing 3yr CAGR base of 13.4% — and management raised FY2026 guidance to "at least mid-teens revenue growth" (Airbnb Q2 2026 earnings release, 6 Aug 2026). This weighs against applying the alternative "-10 structural deceleration" modifier: the 29%→13% COVID-rebound compression flagged in June was a historical fact, but the most recent data point shows stabilization/reacceleration, not further structural decline.
```
Growth_Score = clamp(53.6 + 10) = 63.6
```

**Balance Sheet (15% weight)**
```
Net Debt/EBITDA = ($2.496B − $12.069B) / $2.761B = −3.47×  (net cash)
BalanceSheet_Score = clamp(100 × (1 − (−3.47)/4)) = 100.0  (clamped)
```

**Moat Signal (15% weight)**

| Signal | Result | Evidence (cited) |
|---|---|---|
| Market share stable or growing | ✅ TRUE | Airbnb's global short-term-rental market share rose from 28% (2019) to 44% (2024); ~61% in North America specifically, vs. Booking.com 10% and Vrbo 29% — Skift, "Short-Term Rentals: Airbnb's Dominance and Booking's Gains in 1 Chart" (industry booking-volume data). |
| Brand premium | ✅ TRUE | Average Daily Rate +5% YoY (+4% ex-FX) in Q2 2026 *alongside* nights+seats booked +10% YoY — a price increase without an offsetting volume loss — Airbnb Q2 2026 earnings release. |
| Network effect | ✅ TRUE | Documented two-sided marketplace mechanism — ~8–9.5M active listings, 5.5M hosts across 220+ countries; host supply and guest demand mutually reinforcing (unchanged structural case from the June session). |
| Switching costs | ❌ FALSE | No cited lock-in mechanism found this session — guests and hosts routinely multi-home across Airbnb/Vrbo/Booking.com with low friction; market-share research itself describes active share-shifting between platforms. |
| Scale cost advantage | ❌ FALSE | No cited cost-per-unit data vs. smaller competitors this session — not invented. |

```
Moat_Score = (3/5) × 100 = 60.0
```

**FCF Quality (10% weight)**
```
FCF/NI (FY2025) = $4.646B / $2.511B = 185.0%   (TTM basis: $3.207B/$2.691B = 119.2% — see §2 flag 4)
FCFQuality_Score = clamp(((1.85 − 0.40)/0.60)×100) = 100.0  (clamped either basis — both ≥100%)
```

### Quality Score — Final

```
Quality Score = 75.0×0.25 + 100.0×0.15 + 63.6×0.20 + 100.0×0.15 + 60.0×0.15 + 100.0×0.10
              = 18.75 + 15.00 + 12.72 + 15.00 + 9.00 + 10.00
              = 80.47 → rounds to 80.5
```

# **Quality Score: 80.5 — clears the 80.0+ gate, but only by 0.5 points.**

### ⚠️ Robustness check — this pass is fragile, not a comfortable clear

| If instead... | Quality Score | Gate result |
|---|---|---|
| **As computed above** | **80.5** | **PASS (barely)** |
| No TAM/pricing-power modifier applied to Growth (0 instead of +10) | 78.5 | **FAIL** |
| Moat_Score = 40.0 (2/5 signals, i.e. the "market share" citation not accepted as sufficiently ABNB-specific) | 77.5 | **FAIL** |

Both swing factors were resolved on their own merits with independent citations (not reverse-engineered to clear the gate) — but a reasonable analyst weighing the same evidence slightly differently would land ABNB just **below** 80.0 instead of just above it. **Flagged prominently for the next review** rather than treated as a settled, comfortable pass.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $187.30 / $6.14 (forward consensus EPS) = 30.5×
EY         = 1 / 30.5 = 3.28%
Spread     = EY − 10Y Treasury = 3.28% − 4.71% = −1.43%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (−1.43%, ~2.93pp short) → **+5 additive.**

**Step 2 — Rate Regime Modifier**
10Y = 4.71% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for ABNB = +10**

---

## 5. Fair Value — Scenario Analysis (Rule 7, feeds the Upside/Downside Modifier)

**Method A — DCF** (unlevered FCF, WACC = risk-free 4.71% + Beta 1.14 × ~5% ERP ≈ 10.4%, varied ±1% per scenario; 10yr 2-stage, linear fade to terminal, terminal growth ≤3%; base FCF = FY2025 $4.646B; net cash $9.573B added back; ~614M diluted shares):

| Scenario | FCF growth (yrs 1–5) | Terminal growth | WACC | DCF Fair Value/share |
|---|---|---|---|---|
| Bull (25%) | 18%/yr | 4.0% | 9.5% | **$329.34** |
| Base (50%) | 12%/yr | 3.0% | 10.5% | **$185.38** |
| Bear (25%) | 5%/yr | 1.5% | 11.5% | **$107.85** |

(Bear case DCF of $107.85 lands close to the 52-week low of $110.81 — a useful independent sanity check per Rule 4.)

**Method B — Comparable Multiples** (peers: BKNG fwd PE 18.0×, EXPE fwd PE 15.5×, UBER fwd PE 23.5× — median ≈18.0× base; applied at 24× bull / 14× bear for forward-PE method; a parallel EV/EBIT peer-multiple method at 19×/24×/14× applied to scenario-adjusted EBIT):

| Scenario | Fwd-PE method | EV/EBIT method | Multiples-Based Value (avg) |
|---|---|---|---|
| Bull | $147.36 | $139.70 | **$143.53** |
| Base | $110.52 | $101.00 | **$105.76** |
| Bear | $85.96 | $72.28 | **$79.12** |

**Blended Fair Value** (Step 1 triangulation: 40% DCF + 60% Multiples):

| Scenario | Blended FV |
|---|---|
| Bull | 0.40×329.34 + 0.60×143.53 = **$217.85** |
| Base | 0.40×185.38 + 0.60×105.76 = **$137.61** |
| Bear | 0.40×107.85 + 0.60×79.12 = **$90.61** |

```
PW Fair Value = 0.25×217.85 + 0.50×137.61 + 0.25×90.61 = $145.92
```

DCF and peer-multiples disagree sharply here (DCF credits ABNB's cash generation and continued double-digit growth; peer multiples say the *current* 30.5× forward PE / 37× EV/EBIT is a large, not-obviously-earned premium to slower-growing travel-marketplace peers trading at 15–24×). Shown transparently rather than smoothed into one number — the divergence itself is informative.

---

## 6. Phase 02 — Full Valuation Score

**FCF Yield (40% weight)**
```
FCF Yield (FY2025 basis, primary) = $4.646B / Market Cap $112.156B = 4.14%
FCF_Score = clamp(100×(1 − 4.14/10)) = 58.6
```
Sensitivity (TTM Yahoo FCF basis, flagged distortion — see §2.4): FCF Yield 2.86% → FCF_Score = 71.4.

**EV/EBIT (40% weight — PEG not applicable, see below, 15% redistributed here)**
```
EV = Market Cap $112.156B + Total Debt $2.496B − Total Cash $12.069B = $102.58B
EBIT (TTM, ≈ TTM EBITDA — D&A immaterial for this asset-light model) = $2.761B
EV/EBIT = $102.58B / $2.761B = 37.2×
EV/EBIT_Score = clamp((37.2−12)/23×100) = 100.0  (clamped — ≥35×)
```

**Forward PE + Historical PE Modifier (20% weight)**
```
Forward PE = 30.5×
```
**No-history fallback applied: FwdPE_Score = 50.0** — the trailing-5-year window still contains the 2021–22 unprofitable-to-profitable transition and the Q3 2023 one-time tax-valuation-allowance EPS spike (see §2.5); using the resulting distorted average/range would manufacture a signal, not read one.

**PEG (Fast Grower check) — not applicable, 15% redistributed to EV/EBIT**
```
FY2024 diluted EPS $4.11 → TTM diluted EPS $4.38 ≈ +6.6%
FY2024 NI $2.648B → FY2025 NI $2.511B ≈ −5.2%  (FY2025 NI actually declined YoY)
```
No clean multi-year >15% EPS growth trend on a non-distorted base (same conclusion as June, now reinforced by an additional year showing NI *declined* in FY2025). **Not a Fast Grower — redistribute PEG's 15% to EV/EBIT** (already reflected in the 40% weight above).

**Raw Weighted Score**
```
Raw = 58.6×0.40 + 100.0×0.40 + 50.0×0.20 = 23.44 + 40.00 + 10.00 = 73.4
```
Sensitivity (TTM FCF basis): Raw = 71.4×0.40 + 100.0×0.40 + 50.0×0.20 = **78.6**

**Rate Regime Modifier: +10** (§4)

**Upside/Downside Modifier**
```
Gap Upside % = (PW Fair Value $145.92 / Live Price $187.30) − 1 = −22.1%
Catalyst window: no specific near-term catalyst identified for a *downward* re-rating (this is a "priced-for-perfection" read, not an event-driven short thesis) — default 2yr per Rule 10.
Annualized gap = −22.1% / 2 = −11.05%/yr
Intrinsic growth = FCF 3yr CAGR = (4.646/3.43)^(1/3) − 1 = 10.6%/yr
Shareholder yield = 0% dividend + ~3.1% net buyback yield (diluted share count fell ~3.1% over the trailing year on an active $6B repurchase program, Aug 2025 authorization; $1.1B / 8.1M shares repurchased in Q1 2026 alone)

E = −11.05% + 10.6% + 3.1% = +2.65%
```
`E` (+2.65%) falls in the **0 ≤ E < H(10%)** bracket:
```
M = +5 × (10% − 2.65%) / 10% = +5 × 0.735 = +3.7
```
Despite trading meaningfully above blended fair value, ABNB's continued FCF growth and aggressive buyback nearly offset the reversion drag — leaving a **thin, not negative,** expected return. Modifier: **+3.7** (mild trim-pressure, not the stronger "expected loss" penalty).

### Final Valuation Score
```
Final Score = 73.4 (raw) + 10.0 (Rate Modifier) + 3.7 (Upside/Downside Modifier) = 87.1
```
Sensitivity (TTM FCF basis): 78.6 + 10.0 + 3.7 = **92.3**

# **Valuation Score: 87.1** (sensitivity range 87.1–92.3, both land in the same conclusion below)

---

## 7. Composite Score

```
Composite Score = 0.50×(100 − Quality Score) + 0.50×Valuation Score
                = 0.50×(100 − 80.5) + 0.50×87.1
                = 9.75 + 43.55
                = 53.3
```
Sensitivity (TTM FCF basis): 0.50×19.5 + 0.50×92.3 = **55.9**. Both bases land in the same action band (50.0–69.9).

**Rule 4 sanity check:** current price ($187.30) sits above the mean analyst target ($175.50) — an independent, sell-side signal pointing the same direction as this session's own valuation work (expensive relative to fair value, thin/no margin of safety), despite sell-side's own "Buy" recommendation lean (a common divergence between a bullish long-term rating and a target price that hasn't caught up to a recent rally).

# **Composite Score: 53.3 → HOLD — watch only, no new entry** (Action Table, 50.0–69.9 band)

Since ABNB isn't held, "HOLD" here means the same thing it meant in June: **no position warranted at current price.** No order setup produced (only run for BUY/TRIM actions per the operating brief).

---

## 8. Fundamental Changes Since Last Review (2026-06-07)

- **Stock +40.1%** ($133.72 → $187.30) on two quarters of beat-and-raise results, not an unexplained Rule 9 move.
- **Q2 2026 earnings (6 Aug 2026):** revenue +17% YoY to $3.6B, GBV +16% YoY to $27.2B, net income +$174M YoY to $816M; FY2026 guidance raised to "at least mid-teens revenue growth" and adjusted EBITDA margin ≥35.5%.
- **Active $6B share buyback** (authorized Aug 2025) — $1.1B / 8.1M shares repurchased in Q1 2026 alone, diluted share count down ~3.1% YoY.
- **Regulatory pressure continues to escalate, not yet visible in the numbers:** a Spanish court ordered Airbnb to pay €64M (March 2026) and declined to suspend the sanction; Barcelona continues an aggressive, well-staffed enforcement campaign (11,500+ fines since 2016, phase-out of all 10,101 tourist-flat licenses by 2028); NYC's Local Law 18 has eliminated roughly 9 in 10 of the city's prior short-term listings. None of this has dented reported growth yet, but it remains the clearest documented bear-case vector (per the June session's disruption-vector check, unchanged).
- **First-ever Quality Score and Composite Score computed for ABNB** (methodology added 2026-06-29, postdates the June session) — see §3 robustness flag: a genuinely close call, not a settled read.

---

## 9. Next Review Trigger

- **Q3 2026 earnings release** (expected ~early-to-mid November 2026) — standard Rule 9 trigger.
- **Any >15% move without a documented fundamental driver.**
- **Any material regulatory escalation** in a top-5 market (a full ban, not just fines/enforcement intensification, would be a Rule 9 guidance/moat-impact trigger).
- **Explicitly flagged for the next reviewer:** re-verify the Growth TAM modifier and the "market share" Moat signal on fresh evidence — this session's Quality Score (80.5) clears the gate by only 0.5 points and is not a settled result (§3).

---

## 10. Glossary

| Term | Meaning |
|---|---|
| **ADR (Average Daily Rate)** | The average revenue earned per booked night/room, independent of occupancy — a standard travel-industry pricing metric (not to be confused with "American Depositary Receipt," an unrelated term also abbreviated ADR). |
| **Beta** | A measure of a stock's volatility relative to the overall market — 1.0 means it moves in line with the market; >1.0 means more volatile. |
| **CAGR (Compound Annual Growth Rate)** | The smoothed annual growth rate that would take a value from its starting point to its ending point over a period, accounting for compounding. |
| **Composite Score** | This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50, computed only for companies clearing the 80.0+ Quality Score gate. |
| **DCF (Discounted Cash Flow)** | A valuation method estimating a company's value today as the sum of its projected future cash flows, each discounted back to present value. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / Earnings Before Interest, Taxes, Depreciation and Amortization — operating-profit measures used to compare companies independent of financing and (for EBITDA) capital-intensity differences. |
| **Earnings Yield Spread Test** | Step 1 of the Rate Environment Gate: Earnings Yield (1 ÷ Forward PE) minus the 10-Year Treasury yield; a spread below +1.5% adds a +5 flag to the valuation score. |
| **EV/EBIT (Enterprise Value / EBIT)** | A valuation multiple comparing a company's total value (equity + debt − cash) to its operating profit — a standard cheapness/expensiveness gauge independent of capital structure. |
| **Fast Grower** | This framework's PEG-eligibility classification: EPS growth >15% for 3+ years on a clean, non-distorted earnings base. |
| **FCF (Free Cash Flow) / FCF Yield** | Free Cash Flow is cash generated by the business after operating expenses and capital investment; FCF Yield is FCF ÷ Market Cap, a cheapness gauge. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **GBV (Gross Booking Value)** | The total dollar value of all bookings made on Airbnb's platform before Airbnb's own take-rate/fees are deducted — a scale metric, distinct from Airbnb's own (smaller) reported Revenue. |
| **Gross Margin** | Revenue minus cost of revenue, as a percentage of revenue — how much of every sales dollar is left after the direct cost of delivering the product/service. |
| **Historical PE Modifier** | An additive adjustment to the Forward PE sub-score based on where the current multiple sits versus the company's own trailing 5-year PE range/average; falls back to a flagged neutral 50.0 when no statistically usable history exists. |
| **Invested Capital** | The total capital (debt + equity, net of cash) invested in a business — the denominator in a ROIC calculation. |
| **IRR (Internal Rate of Return)** | The annualized percentage return an investment is expected to generate. |
| **Margin of Safety (MoS)** | How far below fair value the buy price is set, as a cushion against being wrong. |
| **Moat / Moat Signal** | A durable competitive advantage protecting a business's profits from competitors; this framework's 5-point scored checklist (market share, brand premium, network effect, switching costs, scale cost advantage). |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; a negative value means a net cash position. |
| **Net Margin** | Net income as a percentage of revenue. |
| **NOL (Net Operating Loss carryforward)** | Accumulated historical tax losses a company can use to offset future taxable income, reducing (or eliminating) its cash tax bill until the NOL balance is exhausted. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT adjusted for taxes — the numerator in a ROIC calculation. |
| **PEG Ratio** | Forward PE divided by expected earnings growth rate — used to judge whether a growth stock's multiple is justified by its growth rate; scored only for Fast Growers. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value estimate — 25% bull case + 50% base case + 25% bear case — used as the fair-value input to the Upside/Downside Modifier. |
| **Quality Score** | This framework's 0.0–100.0 continuous score grading profitability, margins, growth, balance sheet, moat, and FCF quality; a company must score 80.0+ to proceed to valuation scoring. |
| **Rate Environment Gate / Rate Regime Modifier** | The mandatory pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive adjustment for the current Treasury-yield bracket. |
| **ROIC (Return on Invested Capital)** | NOPAT ÷ Invested Capital — how efficiently a company turns invested capital into after-tax operating profit. |
| **Rule 0 / Rule 4 / Rule 7 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first (0); sanity-check fair value against implied IRR and peer multiples (4); weight bull/base/bear scenarios 25/50/25 (7); force re-valuation on specific fundamental triggers (9); and separate intrinsic value from market price with a documented catalyst and timeline (10). |
| **Shareholder yield** | Dividend yield plus net share-buyback yield combined — cash effectively returned to owners as a percentage of price. |
| **TAM (Total Addressable Market)** | The total revenue opportunity available if a company captured 100% of its relevant market. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | An additive ±15 adjustment to the valuation score based on expected annual return — the gap to PW Fair Value (annualized over the catalyst window) plus intrinsic growth and shareholder yield. |
| **WACC (Weighted Average Cost of Capital)** | The blended rate a company is expected to pay to finance its assets, combining the cost of equity and (weighted by their share of capital) the after-tax cost of debt — used as the discount rate in a DCF. |

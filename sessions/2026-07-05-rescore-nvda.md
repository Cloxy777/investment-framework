# RESCORE — NVDA (NVIDIA Corporation)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-07-05 (Sunday — markets closed; most recent trading session 2026-07-02, ahead of the 3 Jul July 4th holiday observance and the weekend — same calendar gap already noted in the same-day [NOW rescore](2026-07-05-rescore-now.md))
**10Y US Treasury Yield:** 4.49% (TradingEconomics/dshort "Treasury Yields Snapshot," 2 Jul 2026 close — same figure used in the same-day [MSFT](2026-07-05-rescore-msft.md) and [NOW](2026-07-05-rescore-now.md) rescores for consistency across same-day sessions)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** NVDA **48.5** (2026-06-20, BUY-Standard band on score, but blocked at entry by a sub-2:1 R/R and the 3–5% band cap — [sessions/2026-06-20-rescore-nvda.md](2026-06-20-rescore-nvda.md)); Quality Score / Composite Score never computed (predates the 2026-06-29 methodology change — flagged stale, see [watchlist/STALE.md](../watchlist/STALE.md)).
**Current NVDA portfolio weight:** 4.92% per [holdings.md](../portfolio/holdings.md) (14 shares, avg cost $179.20 — [ibkr.md](../portfolio/snapshots/ibkr.md)) — comfortably under the 15% hard cap (Upgrade 7).
**First-ever Quality Score / Composite Score computation for NVDA this session.**

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$194.83** | IBKR `get_price_history` (contract_id 4815747, NASDAQ), most recent daily bar close = **2026-07-02**. Cross-checked exactly against Yahoo Finance's `/v8/finance/chart/NVDA` `regularMarketPrice` (also $194.83) and `yfinance`'s `currentPrice`/`regularMarketPrice` (also $194.83, independently). |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$197.58** (`is_close: true`) — one session stale: that's the **2026-07-01** close, not the fresher 2026-07-02 close ($194.83) that `get_price_history` and Yahoo both show. Same recurring stale-snapshot pattern flagged in the 2026-07-05 MSFT/NOW and 2026-07-04 AVGO sessions — used the fresher $194.83 instead. |
| 52-week range | $157.32 – $236.54 (IBKR `misc_statistics`) | Unchanged high from 06-20; low is fresher. |
| Year-to-date change | +5.95% (+$11.09) | IBKR `year_to_date_change` |
| Analyst consensus PT | mean **$301.62**, median $294.00, range $180–$500, 58 analysts, **Strong Buy** (`recommendationMean` 1.30) | `yfinance` — bull-case sanity check only (Rule 0 Step 4), not a scored input. |
| Price vs. 06-20 review ($210.69) | **−7.53%** | A real pullback, well under the 15% Rule 9 threshold. |

---

## 2. Rule 9 Trigger Check (2026-06-20 → 2026-07-05)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Next report confirmed **26 Aug 2026, after close** (Q2 FY2027) — `yfinance` `get_earnings_dates`, unchanged from 06-20. |
| Guidance revision | No | Q1 FY2027 guidance (Q2 FY2027 revenue ≈$78.0B at 75.0% non-GAAP gross margin, **explicitly excluding all China Data Center compute**) was issued at the 20 May 2026 earnings release — predates the 06-20 review, not a fresh trigger this session. |
| M&A | No | None found in the window. |
| Management change | No | None found. |
| Dividend/buyback action | Not a Rule 9 trigger, but new information | Quarterly dividend raised from $0.01 to **$0.25/share** (payable 26 Jun 2026) and buyback authorization increased by **$80B** (on top of $38.5B remaining) — both announced at the 20 May 2026 earnings release (predates 06-20), so not a fresh trigger, but refreshes the Upside/Downside Modifier's shareholder-yield input below (§8) since the 06-20 session's shareholder-yield figure was computed before the raise had actually been paid out. |
| Macro shift | No | 10Y ticked from 4.46% (06-20) to 4.49% (07-02) — still inside the "3.5–5%" bracket, no Rate Regime bracket change. |
| >15% unexplained price move | No | −7.53% over 15 days — inside normal range, not a Rule 9 event. |

**Conclusion: no Rule 9 trigger fired.** This is a routine, scheduled price-refresh rescore — but see §5 for the **first-ever NVDA Quality Score computation**, which is new information independent of any Rule 9 event, and is why this session was due (per [watchlist/STALE.md](../watchlist/STALE.md)).

---

## 3. Data Gaps / Flags

1. **`yfinance` connectivity note (not a data gap):** direct `curl_cffi`-based `yfinance` calls failed TLS handshake through this session's proxy; routed `yfinance` through a plain `requests.Session()` (pointed at the proxy's CA bundle) instead — the same workaround already documented as "yfinance via `requests.Session()`" in [valuation-scoring.md](../framework/valuation-scoring.md)'s automation notes and used in the 2026-07-05 NOW session. All figures below cross-check cleanly against IBKR and Yahoo's own computed fields (see inline cross-checks in §4), so this is a transport-layer note, not a data-quality concern.
2. **`info.freeCashflow` ($46.3B) diverges from the cash-flow-statement TTM figure ($119.08B)** — same divergent-field pattern already flagged in the 2026-06-20 NVDA session (`info.freeCashflow` read $46.3B then too, vs. the statement's $96.7B FY2026 figure). Used the **statement-derived TTM figure** ($119.08B = TTM Operating Cash Flow $125.65B − TTM CapEx $6.57B), which independently cross-checks exactly against `info.operatingCashflow` ($125,648,003,072). Not invented — computed from the same quarterly cash-flow statement lines used throughout this session.
3. **Forward PE / Forward EPS — a discovered data nuance, flagged not corrected (open methodology item).** `yfinance`'s `info.forwardEps` ($12.76443, which drives `info.forwardPE` = 15.264×) matches the **"+1y"** (FY2028) consensus estimate in `t.earnings_estimate`, not the nearer **"0y"** (FY2027, $8.97274) estimate — i.e. the sourced "forward PE" is effectively a ~2-year-forward multiple, not a strict next-twelve-months figure (which would be $194.83 ÷ $8.97274 = 21.73×, not 15.26×). Checked and confirmed this is **not new to this session** — the 2026-06-20 NVDA session's forward PE (16.55×) implied EPS of ~$12.73, i.e. it was already reading the same "+1y" field. Flagged here transparently (mirrors the open Forward-PE primary-vs-fallback item already logged in [watchlist/README.md](../watchlist/README.md) for NOW/MSFT/NKE) rather than unilaterally changing NVDA's sourcing convention mid-book, which would make it incomparable to every other ticker scored the same way. **Not corrected this session** — flagged as a standing open item for a future `decisions/` entry.
4. **IBKR `dividend_yield` (0.14%) vs. `yfinance` `dividendYield` (0.51%) — reconciled, not a discrepancy.** IBKR's figure reflects trailing-12-month *actual* dividends paid (mostly the pre-raise $0.01/quarter rate, since the $0.25/quarter raise only took effect with the June 2026 payment: ≈3×$0.01 + 1×$0.25 = $0.28 ÷ $194.83 ≈ 0.14%, which matches). `yfinance`'s figure uses the new **forward run-rate** ($0.25×4 = $1.00 ÷ $194.83 = 0.513%). Used the forward run-rate for the Upside/Downside Modifier's shareholder-yield input (§8) since it's representative of go-forward cash returns, not the mechanically-lagging trailing figure.
5. **Quality Score Moat Signal — two judgment calls, shown transparently (mirrors the same-shape disclosure in the NOW/MSFT/AVGO 2026-07 sessions):**
   - **Network effect vs. Switching costs** are both scored TRUE off the same underlying CUDA ecosystem, but on **distinct evidentiary types** — see §5 for the specific mechanism cited for each, to avoid the appearance of double-counting one fact as two signals.
   - **Scale cost advantage marked FALSE** despite strong qualitative evidence that NVIDIA has secured the majority of TSMC's advanced CoWoS packaging capacity through 2027 — no **cost-per-unit** figure (the checklist's specific evidentiary bar) was found comparing NVIDIA's realized unit economics to AMD's or a custom-ASIC maker's, only capacity-share and TCO-comparison narratives. Consistent with the strict reading applied to MSFT's, NOW's, and AVGO's own FALSE signals in the last two sessions.
6. **Growth Score structural-deceleration modifier — considered, not applied (immaterial either way to the final number, flagged for completeness).** NVDA's YoY revenue growth rate has mechanically decelerated as the base has grown (FY2024 +125.9% → FY2025 +114.2% → FY2026 +65.5% → Q1 FY2027 +85.3%, with Q2 FY2027 guidance of ≈$78.0B implying ≈+66.9% YoY). This is a **denominator/high-base effect**, not documented evidence of TAM shrinkage, moat erosion, or lost pricing power — and the guidance is explicitly conservative (it excludes all China Data Center compute revenue entirely, which is a modeling choice, not a demand signal). No **structural** deceleration evidence found → the −10 modifier is **not** applied. Note this judgment call is moot to the actual score either way: Growth_Score before any modifier is already at the 100.0 cap (Revenue 3yr CAGR ≈100% is far past the 25% ceiling the formula clamps at), so neither the +10 nor a hypothetical −10 would move the number — flagged only for "no black box" completeness.
7. **FCF/NI conversion — declining trend, still comfortably above the 70% hard-disqualifier threshold.** Annual: FY2023 87.2% → FY2024 90.8% → FY2025 83.5% → FY2026 80.5% → TTM (through Q1 FY2027) 74.6%. A real, gradual decline (cash conversion growing more slowly than net income as the buyback/dividend base scales), but every single year and the TTM figure clear 70% — no hard-disqualifier breach. Worth a watch note for future re-scores if the trend continues toward the 70% line.

---

## 4. NVDA — Inputs Collected (fresh this session, TTM rollup via `yfinance` quarterly statements, methodology consistent with the 2026-07-05 NOW/MSFT sessions)

**Sector:** Technology — Semiconductors (AI Compute & Data-Center GPUs)

**TTM window: Q2 FY2026 (Jul 2025) + Q3 FY2026 (Oct 2025) + Q4 FY2026 (Jan 2026) + Q1 FY2027 (Apr 2026)** — a fresher window than the 06-20 session's FY2026-annual-only read (that session pre-dated this session's ability to roll a fresher TTM through the just-reported Q1 FY2027 print).

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 24,221,000,000 | `yfinance` `sharesOutstanding` |
| **Market Cap** | 24.221B × $194.83 = **$4,718,977.43M** | Computed — matches `yfinance` `marketCap` ($4,718,977,351,680) essentially exactly |
| TTM Revenue (Q2'26–Q1'27) | $46,743M+$57,006M+$68,127M+$81,615M = **$253,491M** | `yfinance` quarterly financials rollforward |
| TTM EBIT | $31,268M+$37,997M+$50,471M+$70,005M = **$189,741M** | Same |
| TTM Net Income | $26,422M+$31,910M+$42,960M+$58,321M = **$159,613M** | Same |
| TTM Pretax Income / Tax Provision | $189,443M / $29,830M | Same |
| **Effective tax rate (TTM)** | 29,830/189,443 = **15.75%** | Computed |
| TTM Operating Cash Flow | $15,365M+$23,751M+$36,188M+$50,344M = **$125,648M** | `yfinance` quarterly cashflow — matches `info.operatingCashflow` ($125,648,003,072) exactly |
| TTM CapEx | $1,895M+$1,636M+$1,284M+$1,757M = **$6,572M** | Same |
| **TTM FCF** | $125,648M − $6,572M = **$119,076M** | Computed (see Data Gap #2 re: `info.freeCashflow` divergence) |
| TTM D&A | $669M+$751M+$812M+$997M = $3,229M | `yfinance` quarterly cashflow |
| **TTM EBITDA** | $189,741M + $3,229M = **$192,970M** | Computed |
| TTM Gross Profit | $33,853M+$41,849M+$51,093M+$61,157M = $187,952M | `yfinance` quarterly financials |
| **Gross Margin (TTM)** | 187,952/253,491 = **74.15%** | Computed — matches `info.grossMargins` (0.74145) essentially exactly |
| **Net Margin (TTM)** | 159,613/253,491 = **62.97%** | Computed — matches `info.profitMargins` (0.62966) essentially exactly |
| Total Debt (2026-04-30) | $12,348M | `yfinance` quarterly balance sheet |
| Cash + ST Investments (2026-04-30) | $80,572M | `yfinance` quarterly balance sheet |
| **Net Debt** | $12,348M − $80,572M = **−$68,224M (net cash)** | Computed |
| **Enterprise Value** | $4,718,977.43M + (−$68,224M) = **$4,650,753.43M** | Computed. `yfinance`'s own `info.enterpriseValue` ($4,674,528M) is close but not identical — implies a smaller net-cash figure (~$44.4B) than the $68.2B computed here from the Cash+ST-Investments convention; flagged, not reconciled further (immaterial to the EV/EBIT bucket either way — see §6). |
| **EV/EBIT** | $4,650,753.43M ÷ $189,741M = **24.51×** | Computed |
| Stockholders' Equity (2026-04-30) | $195,474M | `yfinance` quarterly balance sheet |
| **Invested Capital** (Debt+Equity convention) | $12,348M + $195,474M = **$207,822M** | Computed |
| **NOPAT** | $189,741M × (1−0.1575) = **$159,864M** | Computed |
| **ROIC (TTM)** | $159,864M ÷ $207,822M = **76.92%** | Computed — far above the 30% component ceiling either way |
| Revenue 3yr CAGR (FY2023 $26,974M → FY2026 $215,938M) | (215,938/26,974)^(1/3) − 1 = **100.05%** | `yfinance` annual financials — matches 06-20 session's ~100% read |
| Forward EPS ("+1y" per `yfinance`, see Data Gap #3) | $12.76443 | `yfinance` `forwardEps` |
| **Forward PE** | $194.83 ÷ $12.76443 = **15.264×** | Computed — matches `info.forwardPE` (15.26351) |
| Trailing PEG | 0.6081 | `yfinance` `trailingPegRatio` |
| 5yr avg/range PE | avg **56.54×**, range **36.32×–122.27×** (n=20 quarters, `get_earnings_dates`+price reconstruction) | Matches the 06-20 session's 56.5×/36.3–122.3× essentially exactly (one quarter fresher) |
| FCF/NI conversion (TTM) | 119,076/159,613 = **74.60%** | Computed — see Data Gap #7 for the declining annual trend |
| Diluted avg shares (Q1 FY2027 vs. Q1 FY2026) | 24,391M vs. 24,611M | `yfinance` quarterly financials — net buyback yield ≈ **+0.894%**/yr (see §8) |
| Dividend rate (forward run-rate) | $1.00/yr (0.51%) | `yfinance` `dividendRate` — see Data Gap #4 |
| Next earnings | 26 Aug 2026, after close (Q2 FY2027) | `yfinance` `get_earnings_dates` |

---

## 5. NVDA — Quality Score (first-ever computation, 2026-06-29 methodology)

**Hard disqualifier check (all must pass before the weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | Annual FY2023–2026: 87.2% / 90.8% / 83.5% / 80.5%; TTM 74.6% — all comfortably ≥70% every year (declining trend noted, Data Gap #7) | disqualify if <70% for 2+ yrs *without* explanation | ✅ PASS |
| Net Debt/EBITDA over threshold? | **−0.354× (net cash)** | disqualify if >2.5× | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FCF-positive every year on record (FY2023–2026 and TTM) | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight)

```
Net Margin (TTM)    = $159,613M / $253,491M = 62.97%
NetMargin_Component = clamp((62.97/30)×100, 0, 100) = 100.0   (cap — 62.97/30 = 209.9%)

ROIC (TTM)           = $159,864M / $207,822M = 76.92%
ROIC_Component       = clamp((76.92/30)×100, 0, 100) = 100.0   (cap)

Profitability_Score  = (100.0 + 100.0) / 2 = 100.0   (no FCF cap — FCF-positive every year on record)
```

### Margins (15% weight)

```
Gross Margin (TTM) = 74.15%
GrossMargin_Score = clamp((74.15/80)×100, 0, 100) = 92.68
```
No structural-trend bonus applicable — gross margin is already well above the 40% threshold the bonus targets.

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2023 $26,974M → FY2026 $215,938M) = 100.05%
Growth_Score = clamp((100.05/25)×100, 0, 100) = 100.0   (cap — far past the 25%-CAGR ceiling)
```
**+10 (documented TAM expansion / pricing power, cited) — moot to the capped score, shown for completeness (Data Gap #6):**
- Hyperscaler AI infrastructure capex is running at **≈$650–725B in 2026** across Microsoft, Alphabet, Amazon, and Meta combined (alcapitaladvisory.com, "AI Capex Cycle 2026: $725B Hyperscaler Buildout").
- **Sovereign AI** demand — national/government-funded AI compute build-outs (Saudi Arabia, Japan, France, others) — **tripled in FY2026** and consensus estimates put it over **$30B in FY2027** (multiple sources, Jul 2026 search).
- The next-generation **Vera Rubin** platform (successor to Blackwell) is shipping in volume in H2 2026 and is reported **booked solid through 2027**, offering up to 10× lower inference token cost vs. Blackwell (tickeron.com, cloudmagazin.com, Mar/Jul 2026 coverage).
- Q1 FY2027 guidance for Q2 (~$78.0B) explicitly **excludes all China Data Center compute revenue** — a deliberately conservative choice that leaves a real, uncounted TAM slice on the table (NVIDIA 8-K, 20 May 2026).

No documented **structural** deceleration evidence found (see Data Gap #6 — the YoY growth-rate slowdown is a high-base/denominator effect and a conservative-guidance choice, not a TAM/moat/pricing-power deterioration) → no −10 applies. **Growth_Score = 100.0** either way (capped).

### Balance Sheet (15% weight)

```
Net Debt/EBITDA = −0.354× (net cash)
BalanceSheet_Score = clamp(100×(1 − (−0.354)/4), 0, 100) = clamp(108.85, 0, 100) = 100.0
```
Standard /4 denominator applies — NVIDIA is not a payment network/exchange, the Upgrade 5 asset-light override doesn't apply (and isn't needed regardless, given the large net-cash position).

### Moat Signal (15% weight) — checklist, cited evidence per signal

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | NVIDIA holds **≈80% of the AI accelerator/data-center-GPU market** in 2026 (siliconanalysts.com, "NVIDIA AI GPU Market Share 2026: ~80% of AI Accelerators"), with data-center revenue of $193.7B in FY2026. AMD's competing Instinct line holds only ~5–7% share. Some forward-looking commentary flags gradual share erosion toward ~75% as AMD/custom silicon scale — noted, but current/trailing share is stable-to-dominant, satisfying the signal as written. |
| Brand premium | **TRUE** | Documented pricing power: NVIDIA's B200/GB200 parts carry a premium ASP vs. AMD's MI350X and custom ASICs, and enterprises continue paying that premium for CUDA-ecosystem compatibility plus superior performance-per-dollar in independent TCO (total cost of ownership) comparisons (siliconanalysts.com, "AMD vs NVIDIA AI GPU Market Share 2026: MI350X vs B200 — Performance, Price, TCO Comparison"). |
| Network effect | **TRUE** | Distinct from the switching-cost signal below: **CUDA's value to any single developer grows as more developers/organizations join it** — over **4 million registered CUDA developers** and **40,000+ organizations** run CUDA-accelerated applications, producing an ever-growing library of CUDA-optimized libraries, tools, and pretrained models (cuDNN, TensorRT, NIMs) that make the platform more valuable to each *new* joiner — a documented user-growth-driven-value mechanism, distinct from the cost of *leaving* it (Alphastreet/Medium, "NVIDIA's CUDA Moat," Jun–Jul 2026 coverage). |
| Switching costs | **TRUE** | Distinct mechanism from the network effect above: CUDA-specific optimizations get embedded directly into production code over years — "kernel fusions, mixed-precision behavior tuned to Nvidia's math libraries, distributed training paths optimized around NCCL assumptions, and CI/CD pipelines built around CUDA-native tooling" — reported switching costs "measured in years" once a customer's full infrastructure stack depends on it (techtimes.com/alphastreet.com, Jun 2026 coverage of the OpenAI-NVIDIA compute relationship). |
| Scale cost advantage | **FALSE** | NVIDIA has secured **the majority of TSMC's advanced CoWoS (chip-on-wafer-on-substrate) packaging capacity through 2027**, leaving AMD and other challengers to bid for the remaining 40–50% (cnbc.com, financialcontent.com, Apr 2026 coverage) — a real scale/supply advantage narrative, but **no cost-per-unit figure** was found comparing NVIDIA's realized unit economics to a smaller competitor's, which is the checklist's specific evidentiary bar. Marked FALSE for lacking that precise citation type, consistent with the rigor applied to MSFT's, NOW's, and AVGO's own FALSE signals in the last two sessions. |

```
Moat_Score = (4/5) × 100 = 80.0
```

### FCF Quality (10% weight)

```
FCF/NI (TTM) = $119,076M / $159,613M = 74.60%
FCFQuality_Score = clamp(((0.7460 − 0.40)/0.60)×100, 0, 100) = clamp(57.67, 0, 100) = 57.67
```
The lowest-scoring input this session, reflecting the declining-but-still-healthy conversion trend (Data Gap #7).

### Quality Score — Final

```
Quality Score = (100.0×0.25) + (92.68×0.15) + (100.0×0.20) + (100.0×0.15) + (80.0×0.15) + (57.67×0.10)
              = 25.000 + 13.902 + 20.000 + 15.000 + 12.000 + 5.767
              = 91.669 → rounds to 91.7
```

# Quality Score = 91.7 — PASSES the 80.0+ gate decisively (11.7 points clear).

**This is NVDA's first-ever computed Quality Score**, and it clears the gate comfortably — unlike the AMZN/GOOG/MSFT/NOW/NKE 2026-07 sessions, where the "reference-only Composite Score" caveat applied because those names' Quality Scores *failed* the gate. **That caveat does not apply here.** NVDA's Composite Score below is a fully-adopted, standard number driving the action recommendation — no false-green-light flag needed.

---

## 6. NVDA — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 15.264 = 6.5516%
Spread = EY − 10Y Treasury = 6.5516% − 4.49% = +2.0616 pp
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+2.06 pp) → no +5 additive. (Improvement vs. 06-20's already-passing +1.58 pp — driven by the forward PE compressing further, from 16.55× to 15.26×.)

**Step 2 — Rate Regime Modifier**
10Y = 4.49% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for NVDA = +5**

---

## 7. NVDA — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF Yield = $119,076M ÷ $4,718,977.43M (mktcap) = 2.523%
FCF_Score = clamp(100 × (1 − 2.523/10), 0, 100) = 74.77
```
→ Contribution: 74.77 × 0.40 = **29.907**

**EV/EBIT — 25% weight**
```
EV/EBIT = 24.51×
EV/EBIT_Score = clamp((24.51 − 12)/23 × 100, 0, 100) = 54.40
```
→ Contribution: 54.40 × 0.25 = **13.599**

**Forward PE — 20% weight (fallback formula, 5yr avg available; folds in the Historical PE Modifier)**
```
Deviation% = (15.264 − 56.54) / 56.54 × 100 = −73.01%
FwdPE_Score = clamp(50 + (−73.01) × 2.5, 0, 100) = clamp(−132.5, 0, 100) = 0.0   (floor)
```
Forward PE is ~73% below the 5-year average and below even the 5yr low of 36.3× — deepest possible "cheap" reading (same floor as the 06-20 session, now even further below the average). Do **not** separately apply the ±10 Historical PE Modifier — already folded into the fallback formula.
→ Contribution: 0.0 × 0.20 = **0.00**

**PEG — 15% weight (Fast Grower — EPS growth clears >15%/yr for 3+ yrs on a clean base: FY2024 +584%, FY2025 +147%, FY2026 +67% diluted EPS growth, no one-off tax distortions identified — same determination as 06-20)**
```
PEG = 0.6081
PEG_Score = clamp((0.6081 − 0.5)/2.0 × 100, 0, 100) = 5.41
```
→ Contribution: 5.41 × 0.15 = **0.811**

**Raw weighted score:**
```
= 29.907 + 13.599 + 0.00 + 0.811 = 44.317
```
**+ Rate Regime Modifier (+5) = 49.317** (before the Upside/Downside Modifier)

---

## 8. NVDA — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture — refreshed this session using fresher consensus EPS inputs (no Rule 9 event changed the underlying narrative, but §2 notes the dividend raise/buyback increase and Vera Rubin ramp are all now confirmed/in-flight rather than forward-looking, and fresher "+1y"/"0y" consensus EPS is available since 06-20):**

| Scenario | Wt | EPS basis | Exit PE | Rationale | Fair Value |
|---|---|---|---|---|---|
| **Bull** | 25% | $16.00 (analyst high "+1y" estimate) | 24× | AI infrastructure supercycle continues; Vera Rubin ramp (H2 2026, booked through 2027) and sovereign AI demand both accelerate; modest multiple re-rate off the current depressed 15.26× forward PE, still far below the 56.5× 5yr average and below the $500 analyst high PT (never the rosy point — Guardrail 2). | $16.00 × 24 = **$384.00** |
| **Base** | 50% | $12.76443 (consensus "+1y" avg estimate) | 23× | Consensus-anchored; result ($293.58) sits close to the analyst mean/median PT ($301.62/$294.00) as an independent sanity check. | $12.76443 × 23 = **$293.58** |
| **Bear** | 25% | $8.97274 (consensus "0y"/nearer-term estimate) × 0.85 (15% miss) | 16× | AI-capex *digestion*: hyperscaler spend plateaus, a documented miss vs. even the nearer-term estimate, multiple compresses to a cyclical-trough ~16×. Deliberately anchored **below** the $180 analyst low (Klarman: underwrite the downside honestly), consistent with the 06-20 session's below-Street-low bear-case discipline. | $7.627 × 16 = **$122.03** |

```
PW Fair Value = 0.25×384.00 + 0.50×293.58 + 0.25×122.03 = $273.30
Gap Upside %  = (273.30 ÷ 194.83) − 1 = +40.28%
```
Sits below the $301.62 analyst consensus mean — conservative, sanity check passes (Guardrail 2).

**Step 1 — Annualize over catalyst window (Rule 10):**
Catalyst: Q2 FY2027 earnings 26 Aug 2026 (near-term data-center-trajectory read), within the broader ~2-year AI-capex-digestion question (unchanged framing from 06-20). No single catalyst closes the full gap, so use the **2-year** default.
```
Annualized gap = 40.28% ÷ 2 = +20.14%/yr
```

**Step 2 — Build E (expected annual return):**
```
Intrinsic growth   = +10.0%/yr   (unchanged from 06-20 — deliberately conservative, well below Street's
                                   ~40–90% forward growth estimates, to avoid double-counting the growth
                                   already embedded in the gap-to-fair-value above)
Shareholder yield  = +1.407%     (dividend 0.513% forward run-rate [Data Gap #4] + net buyback yield 0.894%
                                   [diluted avg shares 24,391M (Q1 FY27) vs. 24,611M (Q1 FY26), a 0.894%
                                   YoY reduction — same methodology as the 2026-07-05 NOW session])
E = 20.14 + 10.0 + 1.407 = +31.54%/yr
```

**Step 3 — Map E to modifier (hurdle H = 10%):**
```
E = 31.54% ≥ H → M = −15 × clamp((31.54 − 10)/15, 0, 1) = −15 × clamp(1.436, 0, 1) = −15 × 1.0 = −15.0
```
**Catalyst guardrail:** a documented catalyst + timeline exists within 18–24 months (Q2 earnings 26 Aug 2026; Vera Rubin H2 2026 ramp) → upside credit is **not** capped at −5. Full upside applies.

**Upside/Downside Modifier = −15.0** (floor — strongly attractive expected return, same floor as 06-20, now on a wider PW-FV gap since price fell while fair value held roughly steady).

---

## 9. NVDA — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (44.317) + Rate Modifier (+5) + Upside/Downside (−15.0)
                       = 34.317
```
Boundary rule: not a ".X5" case → **Final Valuation Score = 34.3**

| | Value |
|---|---|
| Raw weighted | 44.317 |
| Rate Gate (Step 1 pass, Step 2 +5) | +5 |
| Upside/Downside Modifier | −15.0 (E = +31.54%) |
| **FINAL VALUATION SCORE** | **34.3** |
| Prior valuation score | 48.5 (06-20) |
| **Quality Score** | **91.7 (PASSES 80.0+ gate — see §5)** |

**Composite Score — fully adopted (Quality Score passes the gate, no "reference-only" caveat needed):**
```
Composite Score = 0.50×(100 − 91.7) + 0.50×34.3 = 0.50×8.3 + 0.50×34.3 = 4.15 + 17.15 = 21.3
```

# Composite Score = 21.3 → band 0.0–29.9 "Very Cheap" → Full position, 6–8% of portfolio

NVDA's exceptional quality (net-cash balance sheet, ~63% net margin, ~77% ROIC, ~100% 3yr revenue CAGR, 4/5 moat signals) blended with a genuinely cheap valuation (raw Valuation Score 34.3, driven by forward-PE compression and a strongly favorable forward-return case) pushes the Composite a full band more attractive than the raw Valuation Score alone (34.3, "Cheap/Standard") would suggest on its own — the opposite of the "false green light" pattern seen in AMZN/GOOG/MSFT/NOW this cycle, because here the Quality Score genuinely clears the gate rather than being blended in despite failing it.

---

## 10. NVDA — Action Recommendation & Order Setup

**Composite Score 21.3 (Very Cheap, 0.0–29.9 band) qualifies for a full position (6–8%) — full order setup required.**

### Fair Value (Rule 3 triangulation: 40% DCF-style / 60% multiples)
```
DCF-style (scenario PW FV)              = $273.30
Multiples (analyst consensus mean/median avg) = (301.62 + 294.00)/2 = $297.81
Blended Fair Value = 0.40 × 273.30 + 0.60 × 297.81 = $288.01
```
Fair value range ~$122 (bear) – $384 (bull), base case ~$288 (Rule 10 — a range, not a point).

### Order setup
```
Margin of Safety = 17.5% (midpoint, 15–20% band for Score 0.0–29.9 — same midpoint convention as the ADBE 2026-07-04 session)
Buy Price (ceiling) = $288.01 × (1 − 0.175) = $237.60
Live price $194.83 is far below the ceiling → ENTER NOW (effective entry = live price, not the ceiling)
Primary Sell Target = Blended FV = $288.01
Bull-Case Trim Target = Bull FV $384.00 × 0.90 = $345.60
Stop Loss = Live Price × (1 − 0.225) = $194.83 × 0.775 = $150.99   (22.5%, midpoint of the 20–25% band, computed off live price since live < ceiling — same convention as ADBE)
R/R = (288.01 − 194.83) / (194.83 − 150.99) = 93.18 / 43.84 = 2.13 : 1   (≥ 2:1 ✓ — clears, though not by a wide margin)
```

### Position sizing — top-up toward the full-position target
```
Portfolio Value (combined, holdings.md last sync 2026-06-28) = $54,891.48
Max $ Risk (1.5%) = $823.37
Risk/share = $43.84
Risk-based size = 823.37 / 43.84 = 18.78 shares
Allocation cap (6–8% band): 6% → 16.90 sh | 8% → 22.54 sh — risk-based size (18.78) sits inside the cap band, so it governs (min rule)
Full target (rounded down, conservative) = 18 shares
Held = 14 shares → TOP-UP = 4 shares
Top-up cost = 4 × $194.83 = $779.32
Resulting position: 18 × $194.83 = $3,506.94 → 6.39% of portfolio (within the 6–8% band)
```

### Order Setup Checklist
```
[x] Composite Score (Quality 91.7 + Valuation 34.3):  21.3   (0.0–29.9, Very Cheap ✓)
[x] Expected annual return E / catalyst window:       +31.54% / 2 yr
[x] Upside/Downside Modifier applied:                 −15.0
[x] DCF Fair Value (PW):                              $273.30
[x] Multiples-Based Fair Value:                       $297.81
[x] Blended Fair Value:                               $288.01
[x] Margin of Safety %:                               17.5%
[x] BUY PRICE (ceiling; live already far below):      $237.60
[x] PRIMARY SELL TARGET:                              $288.01
[x] BULL-CASE TRIM TARGET:                             $345.60
[x] STOP LOSS:                                         $150.99
[x] Risk/Reward Ratio:                                 2.13:1  (≥ 2:1 ✓)
[x] Max $ Risk:                                        $823.37
[x] POSITION SIZE (top-up shares):                     4 (to reach an 18-sh target)
[x] POSITION SIZE ($):                                 $779.32 top-up → 6.39% total
[x] Thesis invalidation triggers:                      see below
```

**Recommendation: CONFIRMED BUY — top up ~4 shares (~$779, to reach an 18-share / 6.39% target). Composite Score 21.3 ("Very Cheap").**

NVDA clears its **first-ever Quality Score gate decisively** (91.7 vs. the 80.0 bar) — the open question this session was designed to resolve, since the ticker carried a numeric valuation score but no quality read on file. Combined with a Valuation Score that dropped a further ~14 points since 06-20 (48.5 → 34.3, chiefly EV/EBIT compressing from 35.7× to 24.5× as trailing TTM earnings caught up further, and FCF yield improving from 1.89% to 2.52%) and a still-strongly-attractive expected annual return (E = +31.5%/yr), the Composite Score (21.3) sits deep in the Very Cheap / Full-position band — a genuine improvement over 06-20, where the identical BUY-band score was blocked outright by a sub-2:1 R/R and an at-cap position size. This session's R/R (2.13:1) clears, though narrowly, and the 3–5%-band cap that blocked 06-20 no longer applies since the Composite Score's band now allows 6–8%.

**Position cap check:** the target 6.39% is nowhere near the 15% hard cap (Upgrade 7) — not a binding constraint.

**Thesis invalidation triggers (Phase 06 / stop), refreshed this session:**
- AI-capex digestion: hyperscaler capex growth materially decelerates or reverses (watch the $650–725B 2026 hyperscaler-capex figures cited in §5 for a downward revision) without a one-off cause
- Gross margin falls >3pp structurally, or FCF/NI conversion falls below 70% for 2 consecutive quarters (currently 74.6% TTM and declining — watch closely, see Data Gap #7)
- CUDA moat erosion: documented, material enterprise-workload migration to a competing stack (AMD ROCm, Google TorchTPU, custom ASICs) at scale — watch-only for now, no such migration is yet documented at scale
- Net debt/EBITDA rising materially (currently deep net cash — not a near-term concern)
- Price through the $150.99 stop

All final-decision authority rests with the human investor; funding is the investor's call.

---

## 11. Next Review Trigger

- **Routine:** NVDA Q2 FY2027 earnings, confirmed **26 Aug 2026, after close** — will refresh every TTM fundamental used here and is the natural point to re-run the full score.
- **Quarterly Rate Environment Gate refresh** — October 2026 (10Y / regime modifier).
- **Watch (from §10):** FCF/NI conversion trend (74.6% TTM, declining) — re-derive if it approaches the 70% hard-disqualifier line; hyperscaler capex commentary for any downward revision to the $650–725B 2026 figures underpinning the Growth Score's TAM citation.
- **Open methodology item (unresolved, flagged not fixed, §3 flag 3):** the Forward-PE / Forward-EPS field nuance (`yfinance`'s "forward" EPS reading as a "+1y"/2-year-out consensus figure rather than a strict next-twelve-months figure) — affects NVDA and, per the 06-20 session's own already-affected reading, has likely been present throughout; worth a dedicated `decisions/` entry alongside the already-open Forward-PE primary-vs-fallback item.
- **Rule 9 triggers (standing):** guidance revision, M&A, management change, a >15% unexplained price move, a credible short report, or the 26 Aug 2026 earnings print itself.

---

## Glossary

| Term | Meaning |
|---|---|
| **ASIC (Application-Specific Integrated Circuit)** | A chip custom-designed for one specific task (e.g. Google's TPU, Amazon's Trainium) rather than a general-purpose processor like a GPU — the main long-term competitive threat cited against NVIDIA's GPU-centric AI-compute franchise. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **CoWoS (Chip-on-Wafer-on-Substrate)** | TSMC's advanced chip-packaging technology used to combine a GPU/accelerator die with high-bandwidth memory into a single package; industry-wide supply-constrained, so securing a large share of it (as NVIDIA has) is a manufacturing scale advantage over smaller competitors. |
| **CUDA** | NVIDIA's proprietary parallel-computing software platform and programming model for its GPUs — the dominant software layer AI/ML developers build on, and the basis for this framework's Network Effect and Switching Costs moat-signal findings (§5). |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate. NVDA's Quality Score (91.7) clears the gate decisively, so this session's Composite Score (21.3) is fully adopted, not a reference-only figure. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — this framework's PEG-eligibility trigger; NVDA qualifies this session. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS — flagged this session as not quite matching that definition for NVDA in `yfinance`'s data (§3 flag 3). |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Hyperscaler** | An operator of very-large-scale, globally-distributed cloud/data-center infrastructure (Microsoft Azure, AWS, Google Cloud, Meta) — the primary buyer category for NVIDIA's data-center GPUs. |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt; negative means net cash. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. NVDA's first-ever computation this session: **91.7 — passes the gate decisively.** |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 3 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; triangulate fair value across two methods; require a minimum 2:1 risk/reward before entering; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **Sovereign AI** | National/government-funded AI computing infrastructure built to keep a country's AI workloads and data within its own borders rather than relying on foreign hyperscalers — an emerging demand category for AI-chip vendors like NVIDIA. |
| **TAM** | Total Addressable Market. |
| **TCO (Total Cost of Ownership)** | The full cost of using a piece of hardware over its life (purchase price plus power, cooling, networking, and software/support costs), not just the sticker price — the standard basis on which competing AI chips are compared. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

# RESCORE — NVDA (NVIDIA Corporation)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-09-01
**10Y US Treasury Yield:** 4.78% (TradingEconomics, US 10Y Note yield, live read dated 2026-09-01 — [tradingeconomics.com/united-states/government-bond-yield](https://tradingeconomics.com/united-states/government-bond-yield); "climbed to around 4.78% on Tuesday, highest since January 2025")
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** NVDA **25.5** Composite (Quality 90.3 / Valuation 41.2), 2026-08-27 — [sessions/2026-08-27-rescore-nvda.md](2026-08-27-rescore-nvda.md)
**Current NVDA portfolio weight:** ≈6.67% live (19 sh × $219.00 = $4,161.00 ÷ $62,381.53, the last portfolio-wide combined total on file in [holdings.md](../portfolio/holdings.md), dated 2026-08-30 — this session refreshes NVDA's own numbers only, not a full portfolio resync). holdings.md's own stored weight (6.65%) predates today's small price move; essentially unchanged either way, comfortably under the 15% hard cap (Upgrade 7).
**Not on the stale-score registry** ([watchlist/STALE.md](../watchlist/STALE.md)) — checked, no pending mark to clear.

## Why this session ran

**Unattended Routine 6 (Telegram Stock-Mention Scan) trigger.** Monitored channel `tarasguk` posted (Ukrainian, translated) at 2026-09-01T06:27:05 UTC (post ID `tarasguk/11811`): *"Nvidia invested $3.5 billion in Taiwan's MediaTek. The company also has $70 billion in other investment commitments. Jensen is the new Buffett."*

**Provenance only — not a data source**, per this task's explicit instruction and the framework's standing Rule 0/"never invent or estimate financial data" discipline. Every figure below is independently sourced (§1–§4), and the claim itself was independently verified before being treated as a scoring input (§2).

---

## 2. Independent Verification of the MediaTek Investment Claim

**Verdict: TRUE, materially as claimed — verified via NVIDIA's own primary source plus multiple independent wire/trade outlets.**

| Claim element | Verification | Source |
|---|---|---|
| NVIDIA invested $3.5B in MediaTek | **Confirmed.** NVIDIA is buying $3.5B of a $3.9B zero-coupon convertible bond MediaTek issued (Alphabet took the remaining ~$0.4B tranche). Announced 2026-08-31; bond matures 2027 in most wire reports, though Reuters cites a 5-year maturity from MediaTek's own disclosure — flagged, not reconciled (immaterial to scoring either way). | **Primary:** [NVIDIA Newsroom press release](https://nvidianews.nvidia.com/news/nvidia-and-mediatek-deepen-long-standing-partnership-to-build-ai-edge-to-cloud-computing-platforms) (NVIDIA IR, 2026-08-31). **Corroborating:** [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-31/nvidia-to-invest-3-5-billion-in-chipmaker-mediatek), [TechCrunch](https://techcrunch.com/2026/08/31/nvidias-3-5b-mediatek-bet-reveals-its-plan-for-tackling-big-techs-ai-chip-buildout/), [Taipei Times](https://www.taipeitimes.com/News/front/archives/2026/09/01/2003863469) (Taiwan press, closer to MediaTek's own disclosure venue), [GlobeNewswire syndication of the same NVIDIA release](https://www.globenewswire.com/news-release/2026/08/31/3353306/0/en/nvidia-and-mediatek-deepen-long-standing-partnership-to-build-ai-edge-to-cloud-computing-platforms.html). |
| Deal not yet closed as of this session | MediaTek's convertible bond is scheduled to **close ~2026-09-08** — the $3.5B has not yet left NVIDIA's cash balance as of this session (2026-09-01). Will show up in NVIDIA's Q3 FY2027 10-Q (period ending ~late Oct 2026, filed ~Nov 2026), not in any filing on record today. | Reuters (via search aggregation); MediaTek's own public disclosure. |
| "$70 billion in other investment commitments" | **Broadly accurate, but not new information.** This matches Bank of America's widely-reported early-2026 estimate of NVIDIA's cumulative AI-ecosystem equity commitments (~$30B OpenAI, ~$10B Anthropic, ~$5B Safe Superintelligence, plus others) — already substantively reflected in this framework's coverage: the 2026-08-27 session already flagged **~$90.7B combined in strategic equity stakes on NVIDIA's own balance sheet** (a related but distinct, larger, already-recognized figure). Not a new fact this session moves on. | [Yahoo Finance](https://finance.yahoo.com/markets/stocks/article/nvidias-70-billion-bet-on-openai-anthropic-and-others-could-pay-off-big-for-shareholders-150039868.html), [CNBC (2026-05-09)](https://www.cnbc.com/2026/05/09/nvidia-embraces-ai-investor-topping-40-billion-in-equity-bets-2026.html), cross-referenced against NVIDIA's own SEC XBRL equity-securities figures already on file. |
| "Jensen is the new Buffett" | Unverifiable editorializing/opinion — not a factual claim, not scored, not addressed further. | — |

**Materiality assessment for the score:** the deal is real and strategically meaningful (NVIDIA's first Taiwan investment, deepens NVLink Fusion / custom-silicon ecosystem lock-in against the ASIC threat — see Moat section, §5), but **it does not move any TTM financial-statement input this session**, because (a) it postdates NVIDIA's most recent filed balance sheet (2026-07-26, in the 10-Q filed 2026-08-21) and (b) it hasn't even closed yet (~2026-09-08). No 8-K has been filed for it as of this session (SEC EDGAR's most recent NVDA 8-K remains the 2026-08-26 earnings filing) — consistent with a disclosed-but-not-yet-8-K-required transaction at this size relative to NVIDIA's balance sheet. This is a genuine, verified, moat-reinforcing strategic event (documented in §5's Moat commentary and §11's next-review watch item), but **not, on its own, a numeric-input-moving fact** — this session's score changes are driven instead by the routine drift of live price / 10Y yield / consensus-forward-EPS inputs (§4–§9), exactly the kind of "verify the headline, then still run the standing scheduled checks" case the task anticipated (cf. the EVO 2026-08-30 precedent).

**This also independently qualifies as a Rule 9 trigger** ("Material M&A announcement," construed to cover this M&A-adjacent strategic-investment/partnership announcement) on a holding ≥5% of the portfolio — see the priority-tier note in the final report.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$219.00** | IBKR `get_price_snapshot` (contract_id 4815747, NASDAQ), intraday last trade, 2026-09-01. Bid/ask $218.93/$219.02. |
| Prior close | $220.78 | Derived from IBKR `change` (−$1.78); independently cross-checked against stockanalysis.com's reported Aug 31 close ($220.78, "up 1.48% at close") — exact match. |
| Today's move | **−$1.78 / −0.81%** | IBKR `change`. Small, unexplained-by-itself move, well under the 15% Rule 9 threshold — not a price-based trigger either way; today's session is driven by the MediaTek event + scheduled Telegram-scan cadence, not by this move. |
| 52-week range | $164.04 – $236.54 | IBKR `misc_statistics` — unchanged from 08-27. |
| YTD change | +17.43% | IBKR `year_to_date_change`. |
| Analyst consensus PT (source 1) | mean **$325.99**, 60 analysts, "Strong Buy" | stockanalysis.com/stocks/nvda/forecast/, pulled 2026-09-01. |
| Analyst consensus PT (source 2, cross-check) | mean **$324.23**, median n/a, high $515.00, low $218.00, 55 analysts, "Moderate Buy" | marketbeat.com/stocks/NASDAQ/NVDA/price-target/, pulled 2026-09-01. The two aggregators' means are within 0.5% of each other (325.99 vs 324.23) — tighter agreement than the 08-27 session's cross-check; used together below. |

---

## 3. Data Gaps / Sourcing Notes (flagged, not silently worked around)

1. **`yfinance` still unavailable this session — same persistent issue as 08-27, confirmed durable rather than one-off.** Fresh attempt this session (`pip install yfinance` succeeded, but the actual API call) failed with `curl_cffi...SSLError: Connection reset by peer` on the quote-summary endpoint — a different failure signature than 08-27's `YFRateLimitError`/429, but the practical effect is the same: no usable `yfinance` data this session either. **Substitute sourcing** (identical to 08-27, all real/cited/primary-or-reputable-secondary): IBKR (live price, Rule 0), SEC EDGAR XBRL `companyfacts` (TTM financial-statement figures — reused from 08-27 since no new quarter has been filed, see #2 below), stockanalysis.com (forward EPS, 5yr quarterly-PE table, consensus PT), marketbeat.com (cross-check consensus PT), WebSearch (10Y yield, MediaTek verification).
2. **No new fiscal quarter reported since the 08-27 session — TTM/annual financial-statement inputs (revenue, EBIT, net income, FCF, margins, ROIC, net debt, gross margin, revenue CAGR, FCF/NI ratio) are unchanged from that session and are reused verbatim below**, re-verified against the same SEC EDGAR XBRL `companyfacts` figures. NVIDIA's next earnings (Q3 FY2027) isn't until ~25 Nov 2026. Only the **live-market-dependent** inputs (price, 10Y yield, forward EPS/PE, PEG, 5yr PE table, analyst consensus) are refreshed this session.
3. **Forward EPS — same open vendor-labeling issue flagged in every prior session, and this session shows an unusually large 5-day revision.** stockanalysis.com's forecast page now shows "FY 2026: $9.29" / "FY 2027: $15.40" (vs. 08-27's "$9.02"/"$13.04" under the same, still-unresolved fiscal-year-offset labeling quirk — see 08-27 session's Data Gap #3 for the full explanation). Continuing the same "Next Year" figure convention for comparability → **Forward EPS = $15.40**, a **+18.1%** revision from 08-27's $13.04 in just 5 calendar days. This is a large jump to take at face value, but it is the live, directly-sourced vendor figure (not invented or smoothed by this session) and is directionally consistent with a real event: analysts continuing to raise estimates in the days following the 08-26 Q2 beat + raised Q3 guide, plausibly reinforced by the 08-31 MediaTek ecosystem-expansion news. Flagged, not corrected — still an open item for a future `decisions/` entry (now compounding across two sessions).
4. **PEG — self-computed again this session** (Lynch definition: Forward PE ÷ forward EPS growth rate), same methodology as 08-27: Forward PE ($14.22×) ÷ 65.74% (stockanalysis.com's stated FY2026→FY2027 EPS growth, same offset labeling) = **PEG 0.216**.
5. **5-year PE table refreshed** — stockanalysis.com's quarterly-ratios page, trailing 20 quarters (now Q3 2022 → Q2 2027, one quarter rolled forward from 08-27's Q3 2022 → Q1 2027 window): **avg 57.84×, range 25.97×–142.78×** — materially unchanged from 08-27's 57.77× avg / 25.97×–142.78× range (same low/high; avg moved <0.2%).
6. **Next earnings date — unchanged, still a third-party estimate.** ~25 Nov 2026, after close (Q3 FY2027) — not yet NVIDIA-IR-confirmed as of this session (same flag as 08-27).

---

## 4. NVDA — Inputs Collected (TTM rollup, reused from 08-27 session — see that session for full line-by-line SEC XBRL derivation; only live-dependent rows refreshed)

**Sector:** Technology — Semiconductors (AI Compute & Data-Center GPUs)
**TTM window: Q3 FY2026 + Q4 FY2026 (derived) + Q1 FY2027 + Q2 FY2027 — unchanged, no new quarter since 08-27**

| Item | Value | Source / status this session |
|---|---|---|
| Shares outstanding | 24,100,000,000 | SEC 10-Q cover page, filed 2026-08-21 — still the freshest figure on file, unchanged |
| **Market Cap** | 24.1B × $219.00 = **$5,277,900M** | Recomputed — live price refresh |
| TTM Revenue | **$302,969M** | Unchanged (SEC XBRL, reused from 08-27) |
| TTM EBIT | **$197,579M** | Unchanged |
| TTM Net Income | **$192,879M** | Unchanged |
| TTM Operating Cash Flow | **$134,360M** | Unchanged |
| TTM CapEx | **$7,354M** | Unchanged |
| **TTM FCF** | **$127,006M** | Unchanged |
| TTM D&A / TTM EBITDA | $3,687M / **$201,266M** | Unchanged |
| TTM Gross Profit | **$226,241M** | Unchanged |
| **Gross Margin (TTM)** | **74.68%** | Unchanged |
| **Net Margin (TTM)** | **63.66%** | Unchanged |
| Total Debt (2026-07-26) | **$33,366M** | Unchanged — pre-dates the not-yet-closed MediaTek deal |
| Cash + ST marketable securities (2026-07-26) | **$56,586M** | Unchanged — the $3.5B MediaTek outlay (closing ~2026-09-08) is **not yet reflected**; will reduce this figure in the Q3 FY2027 balance sheet |
| **Net Debt** | **−$23,220M (net cash)** | Unchanged |
| **Enterprise Value** | $5,277,900M + (−$23,220M) = **$5,254,680M** | Recomputed off refreshed market cap |
| **EV/EBIT** | $5,254,680M ÷ $197,579M = **26.595×** | Recomputed |
| Stockholders' Equity / Invested Capital / NOPAT / **ROIC (TTM)** | $228,984M / $262,350M / $165,873M / **63.21%** | Unchanged |
| Revenue 3yr CAGR (FY2023→FY2026) | **100.05%** | Unchanged |
| Forward EPS (vendor "+1y"-offset figure, see Data Gap #3) | **$15.40** | Refreshed — stockanalysis.com, 2026-09-01 |
| **Forward PE** | $219.00 ÷ $15.40 = **14.221×** | Recomputed |
| PEG (self-computed, see Data Gap #4) | **0.216** | Recomputed: 14.221 ÷ 65.74% growth |
| 5yr avg/range PE | avg **57.84×**, range **25.97×–142.78×** (n=20 quarters) | Refreshed, see Data Gap #5 |
| FCF/NI conversion (TTM) | **65.85%** | Unchanged — still the Quality Score swing factor, see §5 |
| FCF/NI conversion (annual, FY23–FY26) | 87.18% / 90.80% / 83.50% / 80.51% | Unchanged |
| Diluted weighted-avg shares (Q2 FY27 vs Q2 FY26) → buyback yield | 24,285M vs 24,532M → **+1.007%/yr** | Unchanged |
| Dividend rate (forward run-rate) | $1.00/yr ÷ $219.00 = **0.457%** | Recomputed off refreshed price (negligible change) |
| Next earnings | ~25 Nov 2026, after close (Q3 FY2027), unconfirmed by NVIDIA IR | Unchanged |

---

## 5. NVDA — Quality Score (2026-06-29 methodology)

**All inputs to this section are unchanged from 08-27 (no new fiscal quarter reported) — recomputed below for completeness and transparency, per the operating brief's "always show full calculation" rule, not because any input actually moved.**

**Hard disqualifier check:**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ *fiscal years* unexplained? | FY2025 83.50%, FY2026 80.51% — both ≥70% | disqualify if <70% for 2+ *years* | ✅ PASS |
| Net Debt/EBITDA over threshold? | −0.115× (net cash) | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FCF-positive every year on record | disqualify if not | ✅ PASS |

No hard disqualifier triggers. **TTM FCF/NI ratio remains at 65.85%** — still below 70%, still the single largest quality-score drag, unchanged watch item (see §11).

### Profitability (25% weight)
```
NetMargin_Component = clamp((63.66/30)×100) = 100.0   (cap)
ROIC_Component       = clamp((63.21/30)×100) = 100.0   (cap)
Profitability_Score  = (100.0 + 100.0) / 2 = 100.0
```

### Margins (15% weight)
```
GrossMargin_Score = clamp((74.68/80)×100) = 93.35
```

### Growth (20% weight)
```
Growth_Score = clamp((100.05/25)×100) = 100.0   (cap)
```
No structural-deceleration modifier applies (moot at the cap regardless). **MediaTek NVLink Fusion partnership (§2) is corroborating — not scored — TAM-expansion evidence**, reinforcing the same ecosystem-lock-in narrative already captured in the Moat section below.

### Balance Sheet (15% weight)
```
BalanceSheet_Score = clamp(100×(1 − (−0.115)/4)) = 100.0
```
Unchanged. **Flag:** the ~$3.5B MediaTek convertible-bond purchase (closing ~2026-09-08) is not yet reflected here — will pull the net-cash cushion down further from −$23.2B once it settles and appears in the Q3 FY2027 balance sheet. Still deeply net-cash either way; not expected to move this sub-score's cap.

### Moat Signal (15% weight) — light refresh; MediaTek deal noted as corroborating evidence, no signal flip

| Signal | Marked | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Unchanged basis (Data Center 92% of revenue, 08-27 session). |
| Brand premium | **TRUE** | Unchanged. |
| Network effect | **TRUE** | Unchanged CUDA-ecosystem basis. **MediaTek's adoption of NVLink Fusion (§2) is new, real, corroborating evidence of the same network-effect mechanism** (a major merchant-silicon player choosing to plug into NVIDIA's rack-scale interconnect standard rather than build a fully independent one) — cited for completeness, does not change the TRUE determination (already true on the CUDA basis) or the numeric score. |
| Switching costs | **TRUE** | Unchanged CUDA basis. |
| Scale cost advantage | **FALSE** | Still no cost-per-unit citation vs. a named smaller competitor — same strict-reading gap as every prior session. |

```
Moat_Score = (4/5) × 100 = 80.0
```
Unchanged.

### FCF Quality (10% weight)
```
FCF/NI (TTM) = 65.85%
FCFQuality_Score = clamp(((0.6585 − 0.40)/0.60)×100) = 43.08
```
Unchanged.

### Quality Score — Final
```
Quality Score = (100.0×0.25) + (93.35×0.15) + (100.0×0.20) + (100.0×0.15) + (80.0×0.15) + (43.08×0.10)
              = 25.000 + 14.003 + 20.000 + 15.000 + 12.000 + 4.308
              = 90.311 → rounds to 90.3
```

# Quality Score = 90.3 — PASSES the 80.0+ gate, unchanged from 08-27 (no quality-relevant fundamental has moved since that session).

---

## 6. NVDA — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 14.221 = 7.0322%
Spread = EY − 10Y Treasury = 7.0322% − 4.78% = +2.2522 pp
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+2.25pp ≥ 1.5%) → **no Step 1 additive**. This **flips back to a pass** from 08-27's fail (+1.31pp) — the drop in Forward PE (16.78× → 14.22×, driven by the sharp forward-EPS estimate revision, Data Gap #3) more than offset the further rise in the 10Y yield (4.65% → 4.78%).

**Step 2 — Rate Regime Modifier**
10Y = 4.78% → "3.5–5%" bracket → **+5** (unchanged bracket from 08-27, still comfortably inside it).

**Total Rate Modifier for NVDA = 0 (Step 1) + 5 (Step 2) = +5** — down from +10 in the 08-27 session.

---

## 7. NVDA — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF Yield = $127,006M ÷ $5,277,900M (mktcap) = 2.4064%
FCF_Score = clamp(100 × (1 − 2.4064/10)) = 75.936
```
→ Contribution: 75.936 × 0.40 = **30.374**

**EV/EBIT — 25% weight**
```
EV/EBIT = 26.595×
EV/EBIT_Score = clamp((26.595 − 12)/23 × 100) = 63.458
```
→ Contribution: 63.458 × 0.25 = **15.864**

**Forward PE — 20% weight (fallback formula, folds in Historical PE Modifier)**
```
Deviation% = (14.221 − 57.84) / 57.84 × 100 = −75.42%
FwdPE_Score = clamp(50 + (−75.42) × 2.5) = clamp(−138.5) = 0.0   (floor)
```
→ Contribution: **0.00**

**PEG — 15% weight (Fast Grower — determination unchanged from every prior session)**
```
PEG = 0.216
PEG_Score = clamp((0.216 − 0.5)/2.0 × 100) = clamp(−14.2) = 0.0   (floor)
```
→ Contribution: **0.00**

**Raw weighted score:**
```
= 30.374 + 15.864 + 0.00 + 0.00 = 46.238
```
**+ Rate Modifier (+5) = 51.238** (before the Upside/Downside Modifier)

---

## 8. NVDA — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture — rebuilt this session on the refreshed consensus forward EPS ($15.40) and consensus PT cross-check (§1):**

| Scenario | Wt | EPS basis | Exit PE | Rationale | Fair Value |
|---|---|---|---|---|---|
| **Bull** | 25% | $18.00 | 24× | AI-infrastructure supercycle continues accelerating; Vera Rubin ramp (H2 2026); MediaTek/NVLink Fusion deal (§2) extends the rack-scale ecosystem to a major merchant-silicon player, reinforcing the moat thesis; modest re-rate off a forward PE still deeply below the 57.84× 5yr average, deliberately below the $515 Street high (Guardrail 2). | $18.00 × 24 = **$432.00** |
| **Base** | 50% | $15.40 (consensus forward EPS, Data Gap #3) | 21× | Consensus-anchored; result ($323.40) sits within ~1% of both aggregators' mean PT ($325.99 / $324.23, §1) — independent sanity-check pass. | $15.40 × 21 = **$323.40** |
| **Bear** | 25% | $11.00 | 16× | AI-capex-digestion scenario, same framing as prior sessions: hyperscaler spend plateaus, real miss vs. Q3 guide, multiple compresses to a cyclical-trough ~16×. Deliberately anchored **below** the $218.00 Street low (marketbeat.com, §1) — the analyst floor itself rose since 08-27 ($180→$218), so this session's bear case is set correspondingly lower relative to that floor to keep the same conservative discipline. | $11.00 × 16 = **$176.00** |

```
PW Fair Value = 0.25×432.00 + 0.50×323.40 + 0.25×176.00 = $313.70
Gap Upside %  = (313.70 ÷ 219.00) − 1 = +43.24%
```
Sits just below both analyst consensus means (~$325) — conservative, Guardrail 2 sanity check passes.

**Step 1 — Annualize over catalyst window (Rule 10):**
Catalyst: Q3 FY2027 earnings ~25 Nov 2026 (unchanged framing — no single event closes the full 2-year AI-capex-digestion question) → **2-year** default, unchanged.
```
Annualized gap = 43.24% ÷ 2 = +21.62%/yr
```

**Step 2 — Build E:**
```
Intrinsic growth   = +10.0%/yr    (unchanged conservative convention)
Shareholder yield  = +1.464%      (dividend 0.457% + net buyback yield 1.007%, both effectively unchanged)
E = 21.62 + 10.0 + 1.464 = +33.08%/yr
```

**Step 3 — Map E to modifier (hurdle H = 10%):**
```
E = 33.08% ≥ H → M = −15 × clamp((33.08−10)/15, 0, 1) = −15 × clamp(1.539, 0, 1) = −15 × 1.0 = −15.0
```
**Catalyst guardrail:** documented catalyst within 18–24 months exists (Q3 earnings ~25 Nov 2026) → full upside credit applies, not capped.

**Upside/Downside Modifier = −15.0** (floor — fourth consecutive NVDA session pinned here).

---

## 9. NVDA — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (46.238) + Rate Modifier (+5) + Upside/Downside (−15.0)
                       = 36.238
```
Boundary rule: not a ".X5" case → **Final Valuation Score = 36.2**

| | Value |
|---|---|
| Raw weighted | 46.238 |
| Rate Gate (Step 1 pass +0, Step 2 +5) | +5 |
| Upside/Downside Modifier | −15.0 (E = +33.08%) |
| **FINAL VALUATION SCORE** | **36.2** |
| Prior valuation score | 41.2 (08-27) |
| **Quality Score** | **90.3 (PASSES 80.0+ gate)** — unchanged |
| Prior Quality Score | 90.3 (08-27) |

**Composite Score:**
```
Composite Score = 0.50×(100 − 90.3) + 0.50×36.2 = 0.50×9.7 + 0.50×36.2 = 4.85 + 18.10 = 22.95
```
22.95 falls exactly on a ".X5" boundary → round **up** (more conservative) → **Composite Score = 23.0**

# Composite Score = 23.0 → band 0.0–29.9 "Very Cheap" → nominal Action Table band: BUY — Full position 6–8%

Quality Score unchanged (no fundamental has moved). Valuation Score improved 41.2 → 36.2 (Composite 25.5 → 23.0) — **not** driven by the MediaTek news itself, but by (a) the Rate Gate's Step 1 flipping back to a pass as Forward PE compressed on the forward-EPS estimate revision, and (b) a wider Upside/Downside gap as the scenario fair values rose with consensus. **See §10 — this session, unlike 08-27, the order-setup R/R gate actually clears, but a different constraint (position already at its risk-based target size) still blocks an add.**

---

## 10. NVDA — Action Recommendation & Order Setup

**Composite Score 23.0 (Very Cheap, 0.0–29.9 band) nominally qualifies for a full position (6–8%) — full order setup shown per the operating brief's requirement for any BUY-band score.**

### Fair Value (Rule 3 triangulation: 40% DCF-style / 60% multiples)
```
DCF-style (scenario PW FV)                     = $313.70
Multiples (avg of both aggregators' consensus mean, §1) = (325.99 + 324.23)/2 = $325.11
Blended Fair Value = 0.40 × 313.70 + 0.60 × 325.11 = $320.55
```
Fair value range ~$176 (bear) – $432 (bull), base case ~$323 (Rule 10 — a range, not a point).

### Order setup
```
Margin of Safety = 17.5% (midpoint, 15–20% band for Score 0.0–29.9 — unchanged convention)
Buy Price (ceiling) = $320.55 × (1 − 0.175) = $264.45
Live price $219.00 is below the ceiling → "enter now" territory IF R/R clears
Primary Sell Target = Blended FV = $320.55
Bull-Case Trim Target = Bull FV $432.00 × 0.90 = $388.80
Stop Loss = Live Price × (1 − 0.225) = $219.00 × 0.775 = $169.73   (22.5% midpoint, off live price since live < ceiling)
R/R = (320.55 − 219.00) / (219.00 − 169.73) = 101.55 / 49.27 = 2.06 : 1
```

### ✅ R/R gate clears this session — 2.06:1 ≥ 2:1 minimum
Unlike 08-27 (1.58:1, failed), this session's wider Blended Fair Value ($320.55 vs. $296.52) — itself a product of the higher consensus forward EPS and the scenario fair-value uplift — pushes the reward side of the ratio just past the 2:1 bar at today's roughly-flat live price.

**But there is still no room to add — position sizing, not R/R, is now the binding constraint:**
```
Combined portfolio total (holdings.md, 2026-08-30 sync) = $62,381.53
Max $ Risk per trade = 1.5% × $62,381.53 = $935.72
Risk Per Share = $219.00 − $169.73 = $49.27
Max shares by risk-based sizing = $935.72 ÷ $49.27 = 18.99 shares
Current live position = 19 shares (unchanged — no fills since the last sync)
```
**18.99 ≈ 19.0 shares — the live position is already, essentially exactly, at the risk-based full-target size.** There is no meaningful room to add even with the R/R gate now open. Cap check: even the hypothetical 8% allocation ceiling ($4,990.52 ÷ $219.00 ≈ 22.8 shares) is looser than the risk-based figure — the risk-based sizing governs (take the lower of the two per the framework's cross-check rule) and is already met.

**Position cap check:** nowhere near the 15% hard cap (Upgrade 7) either way.

### Practical action: HOLD the existing ≈6.67% position — no add, no trim.
- **No add:** position already at its risk-based full-target size (≈19.0 of ≈19.0 shares) — the R/R gate clearing this session doesn't free up room, since sizing (not R/R) is now what binds.
- **No trim:** Composite Score 23.0 is nowhere near the 70+ trim bands; anti-turnover posture applies regardless.
- This is the same practical HOLD outcome as 08-27, but for a **different reason** — 08-27 was blocked by R/R, this session is blocked by sizing. Worth flagging explicitly: if the position weight ever drifts meaningfully below ~6.6% (e.g. a portfolio-wide rebalance elsewhere), the R/R-clearing math above would support topping back up toward the full 6–8% band.

**Thesis invalidation triggers (Phase 06 / stop), carried forward unchanged from 08-27:**
- AI-capex digestion: hyperscaler capex growth materially decelerates or reverses without a one-off cause (watch the ~25 Nov 2026 Q3 print against the $108.0B guide)
- **FCF/NI conversion — still the most time-sensitive watch item.** TTM 65.85%, unchanged this session; re-derive at FY2027 year-end (~Feb 2027) for the 2-consecutive-year disqualifier check.
- Gross margin falls >3pp structurally (currently 74.68% TTM, stable)
- CUDA moat erosion: no material enterprise-workload migration to a competing stack documented at scale
- Net debt/EBITDA rising materially — still deep net cash, but watch the **incoming, not-yet-settled $3.5B MediaTek outflow** (closes ~2026-09-08) layering onto the cushion that already shrank from −$68.2B to −$23.2B last quarter
- Price through the $169.73 stop level (informational — no position adjustment pending)

All final-decision authority rests with the human investor. **No order was placed or modified by this session — recommendation only.**

---

## 11. Next Review Trigger

- **Routine:** NVDA Q3 FY2027 earnings, estimated **~25 Nov 2026, after close** (unconfirmed by NVIDIA IR) — will refresh every TTM fundamental used here, and will be the first filing to actually show the MediaTek $3.5B outflow's balance-sheet effect.
- **New, specific watch item this session: MediaTek convertible-bond deal closing ~2026-09-08.** Confirm it closed as announced (no withdrawal/repricing) and watch for NVIDIA's own subsequent disclosure of the final terms; re-check the balance-sheet impact once the Q3 FY2027 10-Q is filed.
- **Quarterly Rate Environment Gate refresh** — October 2026.
- **Watch (unchanged from 08-27):** FCF/NI conversion trend (65.85% TTM) — re-derive at FY2027 year-end (~Feb 2027) for the 2-consecutive-year disqualifier condition.
- **Open methodology items (unresolved, flagged not fixed, now spanning three sessions):** (1) the Forward-PE/Forward-EPS "+1y"-offset vendor labeling issue, now showing a notably large 5-day estimate swing ($13.04→$15.40) worth its own scrutiny in a future `decisions/` entry; (2) `yfinance`'s continued unavailability (different failure mode than 08-27 — SSL reset vs. rate-limit — worth checking whether this is a proxy-level or upstream issue at the next session).
- **Rule 9 triggers (standing):** guidance revision, further M&A/strategic-investment announcements, management change, a >15% unexplained price move, a credible short report, or the ~25 Nov 2026 earnings print itself.
- **If position weight drifts below ~6.6%** (e.g. from a broader rebalance), the now-clearing R/R math (§10) would support a top-up back to the 6–8% band — not itself a scheduled trigger, worth a human glance if it occurs.

---

## Glossary

| Term | Meaning |
|---|---|
| **8-K** | The "current report" a US public company files with the SEC within days of a material event. No new 8-K exists yet for the MediaTek deal as of this session (§2) — the most recent NVDA 8-K remains the 2026-08-26 earnings filing. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate. NVDA: 23.0 this session (Very Cheap band), though position sizing blocks an actual add (§10). |
| **Convertible bond** | A bond that can be converted into a fixed number of the issuer's shares, at the holder's option, instead of being repaid in cash — a hybrid of debt and equity. MediaTek issued $3.9B of convertible bonds on 2026-08-31; NVIDIA bought $3.5B of that issuance (§2), giving NVIDIA a bond claim today with the option to convert into MediaTek equity later. *(New term.)* |
| **CUDA** | NVIDIA's proprietary parallel-computing software platform for its GPUs — the basis for this framework's Network Effect and Switching Costs moat findings; the MediaTek/NVLink Fusion deal (§2, §5) is cited as corroborating evidence of the same ecosystem-lock-in mechanism. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EDGAR** | The SEC's public database of company filings. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield in the Rate Environment Gate. This session's spread (+2.25pp) flipped back to a Step-1 pass, unlike 08-27's fail. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — NVDA's PEG-eligibility trigger, unchanged this session. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality) — TTM FCF/NI ratio (65.85%) unchanged this session, still the Quality Score's main drag (§5). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS — this session's Forward PE (14.22×) dropped sharply from 08-27's 16.78× on a large forward-EPS estimate revision (Data Gap #3). |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **GAAP / Non-GAAP** | Generally Accepted Accounting Principles — the standard, audited accounting basis; "non-GAAP" is a company's own adjusted variant. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score — none triggered this session. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Hyperscaler** | An operator of very-large-scale, globally-distributed cloud/data-center infrastructure — the primary buyer category for NVIDIA's data-center GPUs. |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **IR (Investor Relations)** | A public company's function/department responsible for communicating with investors and analysts — NVIDIA's own newsroom press release (§2) is treated as the primary "NVIDIA IR" source for verifying the MediaTek investment claim. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt; negative means net cash. Unchanged this session; flagged for a further, not-yet-reflected reduction once the MediaTek bond purchase settles (§5, §11). |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **NVLink Fusion** | NVIDIA's platform letting third-party chip designers (like MediaTek) build custom accelerator chips that plug directly into NVIDIA's rack-scale, NVLink-connected data-center systems — central to the MediaTek deal (§2) and this session's Moat commentary (§5). *(New term.)* |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **PW** | Probability-weighted (the bull/base/bear scenario blend). |
| **Quality Score** | This framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required for Phase 02/Composite Score. NVDA: 90.3 this session, unchanged from 08-27. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. NVDA's order setup this session computes **2.06:1 — clears the gate** (§10), a change from 08-27's 1.58:1 fail; position sizing (not R/R) is the reason no add follows. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive adjustment(s) for the current Treasury-yield regime. This session Step 1 passed (unlike 08-27), so only Step 2's +5 applies — total +5, down from 08-27's +10. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 3 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; triangulate fair value across two methods; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — unchanged this session (no new quarter filed). |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs. the 10% hurdle. Pinned at its −15.0 floor again this session (fourth consecutive NVDA session). |
| **XBRL (eXtensible Business Reporting Language)** | The SEC's structured, machine-readable financial-data tagging format. |
| **Zero-coupon bond** | A bond issued at a discount to its face value that pays no periodic interest, instead returning the full face value at maturity — the structure of MediaTek's $3.9B convertible-bond issuance that NVIDIA participated in (§2). *(New term.)* |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

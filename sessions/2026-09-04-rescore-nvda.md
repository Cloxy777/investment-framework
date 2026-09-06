# RESCORE — NVDA (NVIDIA Corporation)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-09-04
**10Y US Treasury Yield:** 4.76% (TradingEconomics, US 10Y Note yield — [tradingeconomics.com/united-states/government-bond-yield](https://tradingeconomics.com/united-states/government-bond-yield), pulled 2026-09-04; "held around 4.76% on Friday after pulling back from three-year highs")
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** NVDA **23.0** Composite (Quality 90.3 / Valuation 36.2), 2026-09-01 — [sessions/2026-09-01-rescore-nvda.md](2026-09-01-rescore-nvda.md)
**Current NVDA portfolio weight:** ≈7.06% live (19 sh × $231.73 = $4,402.87 ÷ $62,381.53, the last portfolio-wide combined total on file in [holdings.md](../portfolio/holdings.md), dated 2026-08-30 — this session refreshes NVDA's own numbers only, not a full portfolio resync; same convention as the 09-01 session). **≥5% of portfolio — priority tier.** Comfortably under the 15% hard cap (Upgrade 7) and the 8% allocation cap (21.5 shares).
**Not on the stale-score registry** ([watchlist/STALE.md](../watchlist/STALE.md)) — checked, no pending mark to clear.

## Why this session ran

**Unattended Routine 6 (Telegram Stock-Mention Scan) trigger.** Monitored channel `FinnInvestChannel` posted (Ukrainian, translated) at 2026-09-04T10:00:38 UTC (post ID `FinnInvestChannel/3179`), a weekly news roundup including the line: *"Nvidia is acquiring Hugging Face for $12.93 billion."*

**Provenance only — not a data source**, per this task's explicit instruction, this framework's standing Rule 0/"never invent or estimate financial data" discipline, and the specific instruction to treat this claim with real skepticism (a $12.9B acquisition of a high-profile AI company is extraordinary and independently verifiable). Every figure below is independently sourced, and the claim itself is verified in §2 **before** being treated as a scoring input or Rule 9 trigger.

---

## 2. Independent Verification of the Hugging Face Acquisition Claim

**Verdict: TRUE, confirmed via NVIDIA's own primary SEC filing — stronger verification than the 09-01 MediaTek precedent (which had no 8-K).**

| Claim element | Verification | Source |
|---|---|---|
| NVIDIA is acquiring Hugging Face for $12.93B | **Confirmed.** NVIDIA entered a **definitive agreement** on 2026-09-02 to acquire Hugging Face, Inc. Per NVIDIA's own SEC 8-K (Item 8.01, filed 2026-09-03): "**approximately $11.9 billion** purchase price payable to Hugging Face stockholders, subject to certain adjustments, and an **equity-based retention program of up to approximately $1.0 billion** for Hugging Face employees joining NVIDIA." $11.9B + up to $1.0B ≈ the widely-reported **$12.93B / $12.9B** combined headline figure — matches the Telegram post's number closely. | **Primary:** [SEC EDGAR 8-K, NVIDIA Corp, filed 2026-09-03](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm), accession 0001045810-26-000078, Item 8.01 (full text pulled and read directly, not summarized secondhand). **Corroborating:** [NVIDIA Blog / press release](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/), [NBC News](https://www.nbcnews.com/tech/tech-news/nvidia-buy-hugging-face-nearly-13-billion-big-bet-open-ai-models-rcna595868), [TechCrunch](https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/), [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-03/nvidia-agrees-to-13-billion-deal-for-ai-platform-hugging-face), [CNBC](https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html), [CNN](https://www.cnn.com/2026/09/03/tech/nvidia-hugging-face-ai-acquisition), [Forbes](https://www.forbes.com/sites/zacharyfolk/2026/09/03/nvidia-is-acquiring-hugging-face-for-almost-13-billion/), [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-acquires-hugging-face-for-usd12-93-billion-company-gains-control-of-major-ai-model-distribution-platform), [Variety](https://variety.com/2026/digital/news/nvidia-acquires-hugging-face-12-9-billion-1236850349/), [The Hill](https://thehill.com/policy/technology/6068386-nvidia-acquires-hugging-face/). |
| Deal not yet closed as of this session | **Confirmed not closed.** The 8-K states the transaction "is expected to close in the first half of 2027, subject to the satisfaction or waiver of customary closing conditions, including receipt of required regulatory approvals." No cash has left NVIDIA's balance sheet for this deal yet, and it will not appear in any filing on record for months. | Same primary 8-K. |
| Platform stays open to non-NVIDIA hardware | **Confirmed.** The 8-K itself: NVIDIA "has committed to, among other things, keep Hugging Face's platform open... to permit model makers, developers, and users to upload and download models and datasets of their choosing **and to support other silicon vendors**." Matches the Telegram post's context (framework task description referenced this) and Jensen Huang's public quote. | Same primary 8-K; corroborated by VideoCardz, TechCrunch. |
| Funding structure (cash vs. stock) for the $11.9B stockholder consideration | **Not disclosed.** The 8-K does not state whether the $11.9B is cash, NVIDIA stock, or a mix — only that the $1.0B *employee retention* piece is explicitly "equity-based." Flagged as an open item (§3, §11) rather than assumed. | Absence confirmed by direct reading of the full 8-K text (no other exhibit filed alongside it). |

**Materiality assessment for the score:** this is a real, primary-source-confirmed, **material M&A announcement** — independently qualifying as a **Rule 9 trigger** on its own terms (unlike 09-01's MediaTek investment, which required construing "M&A-adjacent" broadly; this is a definitive acquisition agreement, filed as an SEC 8-K). It **does not move any TTM financial-statement input this session**, because (a) it postdates NVIDIA's most recent filed balance sheet (2026-07-26, in the 10-Q filed 2026-08-21) and (b) the deal itself won't close until H1 2027 — no cash has moved, no shares have been issued. This session's score changes are driven instead by the routine drift of live price / 10Y yield / forward-EPS-consensus inputs (§4–§9) — the deal is treated as a verified strategic/moat-relevant fact (§5) and a Rule 9 trigger (this section), not a numeric-input-moving one, exactly as the 09-01 MediaTek precedent was handled.

**A new, real regulatory risk factor is also worth flagging** (from the 8-K's own supplemental risk-factor text, not press commentary): NVIDIA explicitly disclosed that "many of the world's most popular and successful open-source models originated in China," and that government restrictions on open-source AI model distribution/access (in the US or elsewhere) "could have a material impact on Hugging Face's platform... and a material impact on our business, operating results, and financial condition." Not scored, but tracked as a new thesis-invalidation watch item (§10, §11).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$231.73** | IBKR `get_price_snapshot` (contract_id 4815747, NASDAQ), intraday last trade, timestamp 2026-09-04 12:25:46 UTC. Bid/ask $231.70/$231.75. |
| Prior close | $228.45 | Derived from IBKR `change` (+$3.28); independently cross-checked against stockanalysis.com's reported close ("at close on Sep 3, 2026" — $228.45) — exact match. |
| Today's move | **+$3.28 / +1.44%** | IBKR `change`. Small, well under the 15% Rule 9 threshold — not itself a price-based trigger; today's session is driven by the Hugging Face announcement (§2) + scheduled Telegram-scan cadence, and the move is consistent with (not disproportionate to) that news. |
| 52-week range | $164.04 – $236.54 | IBKR `misc_statistics` — unchanged from 09-01. |
| YTD change | +24.26% | IBKR `year_to_date_change` — up from 09-01's +17.43%, consistent with the post-earnings/post-HF-news rally over the past three sessions. |
| Analyst consensus PT (source 1) | mean **$325.99**, 60 analysts, "Strong Buy" | stockanalysis.com/stocks/nvda/, pulled 2026-09-04 — unchanged from 09-01. |
| Analyst consensus PT (source 2, cross-check) | mean **$324.83**, high $515.00, low $218.00, 55 analysts, "Moderate Buy" | marketbeat.com/stocks/NASDAQ/NVDA/price-target/, pulled 2026-09-04 — essentially unchanged from 09-01's $324.23. |

---

## 3. Data Gaps / Sourcing Notes (flagged, not silently worked around)

1. **`yfinance` still unavailable — third consecutive session, now a clearly durable issue.** Fresh attempt this session (`pip install yfinance` succeeded; the API call) failed again with `curl_cffi.requests.exceptions.SSLError: Connection reset by peer` on the quote-summary endpoint — the same failure signature as 09-01. Substitute sourcing (same discipline as 08-27/09-01, all real/cited/primary-or-reputable-secondary): IBKR (live price, Rule 0), SEC EDGAR (8-K text and XBRL — TTM financial-statement figures reused, no new quarter filed), stockanalysis.com + finviz.com (forward EPS/PE, PEG, consensus PT), marketbeat.com (consensus PT cross-check), WebSearch/WebFetch (10Y yield, Hugging Face verification).
2. **No new fiscal quarter reported since the 08-27 session — confirmed via SEC EDGAR filing list.** The only NVDA 8-Ks filed since 08-26 are: 2026-08-26 (Item 2.02, the Q2 FY2027 earnings release — already reflected in the 08-27/09-01 sessions) and **2026-09-03 (Item 8.01, the Hugging Face announcement — §2, not a financial-results filing)**. No new 10-Q. All TTM/annual financial-statement inputs (revenue, EBIT, net income, FCF, margins, ROIC, net debt, gross margin, revenue CAGR, FCF/NI ratio) are therefore unchanged from 09-01 and reused verbatim below. NVIDIA's next earnings (Q3 FY2027) isn't until ~25 Nov 2026.
3. **Forward EPS — vendor divergence escalated this session; switched primary source.** Repeated `WebFetch` attempts against stockanalysis.com's forecast/statistics pages (a client-rendered single-page app) returned **internally inconsistent figures across separate fetches of the same page within minutes of each other** (one fetch implied a ~$9.29 "next year" EPS, another a ~$4.77/$9.29 pair, neither reconciling with the page's own stated Forward PE of 18.94× at the day's price) — a data-quality problem with scraping this particular JS-rendered page via WebFetch, not a real EPS move. **Switched to finviz.com's snapshot table instead**, which is internally self-consistent (Forward P/E 14.82× × EPS-next-Y $15.64 = $231.75 ≈ the exact live price used, and its trailing EPS $7.91/PE ~29.29× also reconcile to the live price) and continues smoothly from the last two sessions' trajectory ($13.04 on 08-27 → $15.40 on 09-01 → **$15.64 today**, a plausible +1.6% three-day drift) — used as this session's **Forward EPS = $15.64**. This is now a 3-session-old open methodology item (see §11) — worth a `decisions/` entry to pick one authoritative forward-EPS source rather than re-selecting per session.
4. **PEG — self-computed again this session** (Lynch definition: Forward PE ÷ forward EPS growth rate, same methodology as every prior session): Forward PE ($14.82×, see §4) ÷ 68.92% (finviz's stated "EPS next Y % growth") = **PEG 0.215**.
5. **5-year PE table — not independently re-derived this session; carried forward from 09-01 with an explicit flag.** The yfinance-based quarterly-TTM-PE reconstruction methodology ([valuation-scoring.md](../framework/valuation-scoring.md)) is blocked by the same yfinance outage (#1). Alternate sources attempted: macrotrends.net (blocked — empty response, likely anti-bot), wisesheets.io (returned a "current PE" of 39.12/37.82 and a 5yr average of 59.71, **neither of which reconciles with our own independently-computed trailing PE** of ~28.9–29.3× this session — cross-checked twice via stockanalysis.com and finviz, both agreeing closely with each other and with our own SEC-derived TTM EPS. Not used, given the inconsistency). Since the underlying 20-quarter trailing window has **not rolled forward** (no new quarter filed since 09-01, when this figure was last properly reconstructed), this session reuses 09-01's figure verbatim: **avg 57.84×, range 25.97×–142.78× (n=20 quarters)** — flagged as *reused*, not independently re-derived this session.
6. **Cross-check on reused TTM figures:** stockanalysis.com's and finviz's independently-reported trailing EPS ($7.91) and TTM Revenue ($302.97B) both closely match this session's reused SEC-derived TTM Net Income/shares (≈$8.00 implied EPS) and TTM Revenue ($302,969M) — strong corroboration that the reused figures remain current and accurate.
7. **Next earnings date — unchanged, still a third-party estimate.** ~25 Nov 2026, after close (Q3 FY2027), not yet NVIDIA-IR-confirmed.
8. **Hugging Face deal funding structure (cash vs. stock) — not disclosed** in the primary 8-K (§2). Flagged as an open item, not assumed.

---

## 4. NVDA — Inputs Collected (TTM rollup, reused from 09-01/08-27 sessions — see [2026-08-27 session](2026-08-27-rescore-nvda.md) for the full line-by-line SEC XBRL derivation; only live-dependent rows refreshed)

**Sector:** Technology — Semiconductors (AI Compute & Data-Center GPUs)
**TTM window: Q3 FY2026 + Q4 FY2026 (derived) + Q1 FY2027 + Q2 FY2027 — unchanged, no new quarter since 08-27**

| Item | Value | Source / status this session |
|---|---|---|
| Shares outstanding | 24,100,000,000 | SEC 10-Q cover page, filed 2026-08-21 — still the freshest figure on file, unchanged |
| **Market Cap** | 24.1B × $231.73 = **$5,584,693M** | Recomputed — live price refresh |
| TTM Revenue | **$302,969M** | Unchanged (SEC XBRL, reused) |
| TTM EBIT | **$197,579M** | Unchanged |
| TTM Net Income | **$192,879M** | Unchanged |
| TTM Operating Cash Flow | **$134,360M** | Unchanged |
| TTM CapEx | **$7,354M** | Unchanged |
| **TTM FCF** | **$127,006M** | Unchanged |
| TTM D&A / TTM EBITDA | $3,687M / **$201,266M** | Unchanged |
| TTM Gross Profit | **$226,241M** | Unchanged |
| **Gross Margin (TTM)** | **74.68%** | Unchanged |
| **Net Margin (TTM)** | **63.66%** | Unchanged |
| Total Debt (2026-07-26) | **$33,366M** | Unchanged — predates the not-yet-closed Hugging Face deal |
| Cash + ST marketable securities (2026-07-26) | **$56,586M** | Unchanged — the ~$11.9B Hugging Face outlay (closing H1 2027, funding mix undisclosed, §3.8) is **not yet reflected** |
| **Net Debt** | **−$23,220M (net cash)** | Unchanged |
| **Enterprise Value** | $5,584,693M + (−$23,220M) = **$5,561,473M** | Recomputed off refreshed market cap |
| **EV/EBIT** | $5,561,473M ÷ $197,579M = **28.148×** | Recomputed |
| Stockholders' Equity / Invested Capital / NOPAT / **ROIC (TTM)** | $228,984M / $262,350M / $165,873M / **63.21%** | Unchanged |
| Revenue 3yr CAGR (FY2023→FY2026) | **100.05%** | Unchanged |
| Forward EPS (finviz "EPS next Y", see Data Gap #3) | **$15.64** | Refreshed — finviz.com, 2026-09-04 |
| **Forward PE** | $231.73 ÷ $15.64 = **14.817×** | Recomputed |
| EPS next Y % growth (finviz) | **68.92%** | Refreshed |
| PEG (self-computed, see Data Gap #4) | **0.215** | Recomputed: 14.817 ÷ 68.92% growth |
| 5yr avg/range PE | avg **57.84×**, range **25.97×–142.78×** (n=20 quarters) | **Reused verbatim from 09-01** — see Data Gap #5 |
| FCF/NI conversion (TTM) | **65.85%** | Unchanged — still the Quality Score swing factor, see §5 |
| FCF/NI conversion (annual, FY23–FY26) | 87.18% / 90.80% / 83.50% / 80.51% | Unchanged |
| Diluted weighted-avg shares (Q2 FY27 vs Q2 FY26) → buyback yield | 24,285M vs 24,532M → **+1.007%/yr** | Unchanged |
| Dividend rate (forward run-rate) | $1.00/yr ÷ $231.73 = **0.4315%** | Recomputed off refreshed price |
| Next earnings | ~25 Nov 2026, after close (Q3 FY2027), unconfirmed by NVIDIA IR | Unchanged |

---

## 5. NVDA — Quality Score (2026-06-29 methodology)

**All inputs to this section are unchanged from 08-27/09-01 (no new fiscal quarter reported) — recomputed below for completeness and transparency, per the operating brief's "always show full calculation" rule, not because any input actually moved.**

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
No structural-deceleration modifier applies (moot at the cap regardless). **The Hugging Face acquisition (§2) is corroborating — not scored — TAM-expansion evidence** (direct ownership stake in a major AI developer-platform/model-distribution layer), reinforcing the same ecosystem narrative already captured in the Moat section below; doesn't move a score already at its 100.0 ceiling.

### Balance Sheet (15% weight)
```
BalanceSheet_Score = clamp(100×(1 − (−0.115)/4)) = 100.0
```
Unchanged. **Flag:** the ~$11.9B Hugging Face acquisition (closing H1 2027, funding mix undisclosed — §2, §3.8) is not yet reflected here. If funded from cash, it would pull the net-cash cushion down materially from −$23.2B once the deal closes and settles into a future balance sheet — but that is many quarters away and not assumable given the undisclosed funding structure. Still deeply net-cash either way.

### Moat Signal (15% weight) — light refresh; Hugging Face deal noted as corroborating evidence, no signal flip

| Signal | Marked | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Unchanged basis (Data Center 92% of revenue, 08-27 session). |
| Brand premium | **TRUE** | Unchanged. |
| Network effect | **TRUE** | Unchanged CUDA-ecosystem basis. **The Hugging Face acquisition (§2) is new, primary-source-confirmed, corroborating evidence of the same network-effect mechanism, and arguably a stronger data point than 09-01's MediaTek deal** — NVIDIA would directly own a platform with 18M+ developers, 3M+ shared models, 500K+ datasets, and 1M+ applications (per the 8-K's own framing), rather than merely a partnership. Cited for completeness — does not change the TRUE determination (already true on the CUDA basis) or the numeric score, and the deal has not closed. |
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

# Quality Score = 90.3 — PASSES the 80.0+ gate, unchanged from 08-27/09-01 (no quality-relevant fundamental has moved).

---

## 6. NVDA — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 14.817 = 6.7492%
Spread = EY − 10Y Treasury = 6.7492% − 4.76% = +1.9892 pp
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+1.99pp ≥ 1.5%) → **no Step 1 additive**. Still a pass (as on 09-01), though the margin narrowed slightly (+2.25pp → +1.99pp) as Forward PE ticked up from 14.221× to 14.817× on the live-price rally, partly offset by the 10Y yield easing (4.78% → 4.76%).

**Step 2 — Rate Regime Modifier**
10Y = 4.76% → "3.5–5%" bracket → **+5** (unchanged bracket).

**Total Rate Modifier for NVDA = 0 (Step 1) + 5 (Step 2) = +5** — unchanged from 09-01.

---

## 7. NVDA — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF Yield = $127,006M ÷ $5,584,693M (mktcap) = 2.2742%
FCF_Score = clamp(100 × (1 − 2.2742/10)) = 77.258
```
→ Contribution: 77.258 × 0.40 = **30.903**

**EV/EBIT — 25% weight**
```
EV/EBIT = 28.148×
EV/EBIT_Score = clamp((28.148 − 12)/23 × 100) = 70.209
```
→ Contribution: 70.209 × 0.25 = **17.552**

**Forward PE — 20% weight (fallback formula, folds in Historical PE Modifier)**
```
Deviation% = (14.817 − 57.84) / 57.84 × 100 = −74.384%
FwdPE_Score = clamp(50 + (−74.384) × 2.5) = clamp(−135.96) = 0.0   (floor)
```
→ Contribution: **0.00**

**PEG — 15% weight (Fast Grower — determination unchanged from every prior session)**
```
PEG = 0.215
PEG_Score = clamp((0.215 − 0.5)/2.0 × 100) = clamp(−14.25) = 0.0   (floor)
```
→ Contribution: **0.00**

**Raw weighted score:**
```
= 30.903 + 17.552 + 0.00 + 0.00 = 48.455
```
**+ Rate Modifier (+5) = 53.455** (before the Upside/Downside Modifier)

---

## 8. NVDA — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture — base case rebuilt on the refreshed consensus forward EPS ($15.64); bull/bear qualitative assumptions carried forward from 09-01 unchanged (no fundamental shift to the multi-year bull/bear framing since then — the Hugging Face deal is treated as reinforcing the bull-case moat narrative, not requiring a new EPS estimate):**

| Scenario | Wt | EPS basis | Exit PE | Rationale | Fair Value |
|---|---|---|---|---|---|
| **Bull** | 25% | $18.00 | 24× | AI-infrastructure supercycle continues; Vera Rubin ramp (H2 2026); the Hugging Face acquisition (§2) — if it closes as announced — would extend NVIDIA's ecosystem lock-in directly into the AI model-distribution/developer-platform layer, reinforcing the moat thesis; modest re-rate off a forward PE still deeply below the 57.84× 5yr average, deliberately below the $515 Street high (Guardrail 2). Unchanged from 09-01 — no new information changes the long-run bull case's EPS assumption. | $18.00 × 24 = **$432.00** |
| **Base** | 50% | $15.64 (consensus forward EPS, §3.3/§4) | 21× | Consensus-anchored; result ($328.44) sits within ~1% of both aggregators' mean PT ($325.99 / $324.83, §1) — independent sanity-check pass. | $15.64 × 21 = **$328.44** |
| **Bear** | 25% | $11.00 | 16× | AI-capex-digestion scenario, same framing as prior sessions: hyperscaler spend plateaus, a real miss vs. the Q3 guide, multiple compresses to a cyclical-trough ~16×. Deliberately anchored **below** the $218.00 Street low (marketbeat.com, §1, unchanged from 09-01). Also now incorporates the newly-disclosed regulatory risk (§2) as a qualitative downside factor within this scenario, without a separate numeric adjustment. | $11.00 × 16 = **$176.00** |

```
PW Fair Value = 0.25×432.00 + 0.50×328.44 + 0.25×176.00 = $316.22
Gap Upside %  = (316.22 ÷ 231.73) − 1 = +36.46%
```
Sits just below both analyst consensus means (~$325) — conservative, Guardrail 2 sanity check passes.

**Step 1 — Annualize over catalyst window (Rule 10):**
Catalyst: Q3 FY2027 earnings ~25 Nov 2026 (unchanged framing — no single event closes the full 2-year AI-capex-digestion question; the Hugging Face deal's H1 2027 close is a secondary, not primary, catalyst) → **2-year** default, unchanged.
```
Annualized gap = 36.46% ÷ 2 = +18.23%/yr
```

**Step 2 — Build E:**
```
Intrinsic growth   = +10.0%/yr    (unchanged conservative convention)
Shareholder yield  = +1.4385%     (dividend 0.4315% + net buyback yield 1.007%, both effectively unchanged)
E = 18.23 + 10.0 + 1.4385 = +29.67%/yr
```

**Step 3 — Map E to modifier (hurdle H = 10%):**
```
E = 29.67% ≥ H → M = −15 × clamp((29.67−10)/15, 0, 1) = −15 × clamp(1.311, 0, 1) = −15 × 1.0 = −15.0
```
**Catalyst guardrail:** documented catalyst within 18–24 months exists (Q3 earnings ~25 Nov 2026) → full upside credit applies, not capped.

**Upside/Downside Modifier = −15.0** (floor — fifth consecutive NVDA session pinned here, though the underlying E has drifted down from 09-01's +33.08% as the price rally narrows the gap to PW fair value — still comfortably clears the floor's 25%/yr threshold).

---

## 9. NVDA — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (48.455) + Rate Modifier (+5) + Upside/Downside (−15.0)
                       = 38.455
```
Boundary rule: not a ".X5" case (38.455 is not exactly halfway between two tenths) → standard rounding → **Final Valuation Score = 38.5**

| | Value |
|---|---|
| Raw weighted | 48.455 |
| Rate Gate (Step 1 pass +0, Step 2 +5) | +5 |
| Upside/Downside Modifier | −15.0 (E = +29.67%) |
| **FINAL VALUATION SCORE** | **38.5** |
| Prior valuation score | 36.2 (09-01) |
| **Quality Score** | **90.3 (PASSES 80.0+ gate)** — unchanged |
| Prior Quality Score | 90.3 (09-01) |

**Composite Score:**
```
Composite Score = 0.50×(100 − 90.3) + 0.50×38.5 = 0.50×9.7 + 0.50×38.5 = 4.85 + 19.25 = 24.10
```
**Composite Score = 24.1**

# Composite Score = 24.1 → band 0.0–29.9 "Very Cheap" → nominal Action Table band: BUY — Full position 6–8%

Quality Score unchanged (no fundamental has moved). Valuation Score edged up 36.2 → 38.5 (Composite 23.0 → 24.1) — driven entirely by the live-price rally (+5.8% since 09-01, most of it in the last 3 days on the Hugging Face news + broader AI-sector strength) pushing up EV/EBIT and narrowing the Upside/Downside gap slightly, **not** by any change to the underlying business. See §10 — this session's order-setup R/R gate **fails** again (reverting from 09-01's brief pass).

---

## 10. NVDA — Action Recommendation & Order Setup

**Composite Score 24.1 (Very Cheap, 0.0–29.9 band) nominally qualifies for a full position (6–8%) — full order setup shown per the operating brief's requirement for any BUY-band score.**

### Fair Value (Rule 3 triangulation: 40% DCF-style / 60% multiples)
```
DCF-style (scenario PW FV)                     = $316.22
Multiples (avg of both aggregators' consensus mean, §1) = (325.99 + 324.83)/2 = $325.41
Blended Fair Value = 0.40 × 316.22 + 0.60 × 325.41 = $321.73
```
Fair value range ~$176 (bear) – $432 (bull), base case ~$328 (Rule 10 — a range, not a point).

### Order setup
```
Margin of Safety = 17.5% (midpoint, 15–20% band for Score 0.0–29.9 — unchanged convention)
Buy Price (ceiling) = $321.73 × (1 − 0.175) = $265.43
Live price $231.73 is below the ceiling → "enter now" territory IF R/R clears
Primary Sell Target = Blended FV = $321.73
Bull-Case Trim Target = Bull FV $432.00 × 0.90 = $388.80
Stop Loss = Live Price × (1 − 0.225) = $231.73 × 0.775 = $179.59   (22.5% midpoint, off live price since live < ceiling)
R/R = (321.73 − 231.73) / (231.73 − 179.59) = 90.00 / 52.14 = 1.73 : 1
```

### ❌ R/R gate FAILS this session — 1.73:1 < 2:1 minimum
This reverses 09-01's brief pass (2.06:1). The live-price rally (+5.8% since 09-01) increased the entry price faster than the (also-rising) Blended Fair Value, compressing the reward side of the ratio below the 2:1 bar — the same failure mode as 08-27 (1.58:1), for a similar underlying reason (price moving up faster than the scenario/consensus fair value in the days since the last check).

**Position sizing is also, independently, no longer supportive of an add:**
```
Combined portfolio total (holdings.md, 2026-08-30 sync) = $62,381.53
Max $ Risk per trade = 1.5% × $62,381.53 = $935.72
Risk Per Share = $231.73 − $179.59 = $52.14
Max shares by risk-based sizing = $935.72 ÷ $52.14 = 17.95 shares
Current live position = 19 shares (unchanged — no fills since the last sync)
```
**19 shares already exceeds the 17.95-share risk-based full-target size** (the stop widened in dollar terms as the live price rose, shrinking the risk-based share count) — a second, independent reason no add would follow even if R/R had cleared. Cap check: even the 8% allocation ceiling (21.5 shares) has room, but the framework takes the lower of the two (risk-based vs. cap), and risk-based sizing is both the binding constraint and already exceeded.

**Position cap check:** ≈7.06% of portfolio — nowhere near the 15% hard cap (Upgrade 7).

### Practical action: HOLD the existing ≈7.06% position — no add, no trim.
- **No add:** R/R fails the 2:1 minimum (1.73:1) this session, **and** the position already sits slightly above its current risk-based full-target size (19 vs. 17.95 shares) — two independent reasons, not one.
- **No trim:** Composite Score 24.1 is nowhere near the 70+ trim bands; anti-turnover posture applies regardless.
- **Worth flagging explicitly (continuing the pattern noted in 09-01):** this is the third distinct "practical HOLD, no add" outcome in three sessions, but for a **different combination of reasons each time** — 08-27 (R/R fail alone), 09-01 (R/R pass, but sizing bound), 09-04 (R/R fail again, and sizing now also binds). The underlying Composite Score has stayed in the same "Very Cheap" band throughout (21.3 → 25.5 → 23.0 → 24.1 across the last four sessions) — the R/R/sizing oscillation is a function of short-run price noise around a broadly stable valuation read, not a change in thesis.

**Thesis invalidation triggers (Phase 06 / stop), carried forward from 09-01 with one addition:**
- AI-capex digestion: hyperscaler capex growth materially decelerates or reverses without a one-off cause (watch the ~25 Nov 2026 Q3 print against the $108.0B guide)
- **FCF/NI conversion — still the most time-sensitive watch item.** TTM 65.85%, unchanged this session; re-derive at FY2027 year-end (~Feb 2027) for the 2-consecutive-year disqualifier check.
- Gross margin falls >3pp structurally (currently 74.68% TTM, stable)
- CUDA moat erosion: no material enterprise-workload migration to a competing stack documented at scale
- Net debt/EBITDA rising materially — still deep net cash; the ~$11.9B Hugging Face outlay (closing H1 2027, funding mix undisclosed) is a future watch item, not yet a live one
- **New this session:** regulatory restriction on open-source/open-weight AI model distribution (US or elsewhere) — explicitly disclosed as a risk factor in NVIDIA's own 8-K (§2), tied specifically to China-origin open models flowing through platforms like Hugging Face. Not yet a live event; tracked as a watch item.
- Price through the $179.59 stop level (informational — no position adjustment pending)

All final-decision authority rests with the human investor. **No order was placed or modified by this session — recommendation only.**

---

## 11. Next Review Trigger

- **Routine:** NVDA Q3 FY2027 earnings, estimated **~25 Nov 2026, after close** (unconfirmed by NVIDIA IR) — will refresh every TTM fundamental used here, and may be the first filing to comment further on the Hugging Face deal's regulatory-approval progress.
- **New, specific watch item this session: Hugging Face acquisition.** Track regulatory-approval progress toward the expected H1 2027 close; watch for disclosure of the $11.9B stockholder consideration's cash/stock funding mix (a merger proxy statement or a future 8-K/10-Q is the likely venue); once closed, reassess balance-sheet (cash/net-debt) impact and re-evaluate the Moat Signal / Growth TAM-expansion evidence with the deal actually complete rather than pending.
- **Quarterly Rate Environment Gate refresh** — October 2026.
- **Watch (unchanged from 08-27/09-01):** FCF/NI conversion trend (65.85% TTM) — re-derive at FY2027 year-end (~Feb 2027) for the 2-consecutive-year disqualifier condition.
- **Open methodology items (unresolved, flagged not fixed, now spanning at least three sessions):** (1) the forward-EPS/forward-PE vendor divergence — this session had to abandon stockanalysis.com's forecast page (internally inconsistent across repeat scrapes) in favor of finviz.com; worth a `decisions/` entry to pick and document one authoritative forward-EPS source rather than switching per session; (2) `yfinance`'s continued unavailability (third consecutive session, same SSL-reset failure — looks like a durable infrastructure/proxy issue rather than a transient one, worth escalating outside the analysis session itself); (3) the 5yr avg/range PE reconstruction, blocked by the same yfinance issue, was reused rather than independently re-derived this session — needs a fresh derivation once yfinance access is restored or a reliable alternate bulk-history source is found.
- **Rule 9 triggers (standing):** guidance revision, further M&A/strategic-investment announcements, management change, a >15% unexplained price move, a credible short report, or the ~25 Nov 2026 earnings print itself.
- **If the R/R gate clears again in a future session AND the position is simultaneously under its risk-based target size**, that combination (not either alone) would support a top-up toward the 6–8% band — not itself a scheduled trigger, worth a human glance if it occurs.

---

## Glossary

| Term | Meaning |
|---|---|
| **8-K** | The "current report" a US public company files with the SEC within days of a material event. NVIDIA's 2026-09-03 8-K (Item 8.01) is the primary source verifying the Hugging Face acquisition (§2) this session. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate. NVDA: 24.1 this session (Very Cheap band), though the R/R gate and position sizing both block an actual add (§10). |
| **CUDA** | NVIDIA's proprietary parallel-computing software platform for its GPUs — the basis for this framework's Network Effect and Switching Costs moat findings; the Hugging Face acquisition (§2, §5) is cited as new, stronger corroborating evidence of the same ecosystem-lock-in mechanism. |
| **D&A** | Depreciation & Amortization. |
| **Definitive agreement** | The legally binding contract signed once M&A terms are fully negotiated — the stage NVIDIA and Hugging Face reached on 2026-09-02, publicly disclosed via the 8-K referenced throughout this session, still subject to closing conditions (regulatory approvals) before the deal completes (expected H1 2027). |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EDGAR** | The SEC's public database of company filings — the source of the 8-K verifying the Hugging Face deal (§2). |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield in the Rate Environment Gate. This session's spread (+1.99pp) still clears the Step-1 pass threshold, though the margin narrowed slightly from 09-01. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — NVDA's PEG-eligibility trigger, unchanged this session. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality) — TTM FCF/NI ratio (65.85%) unchanged this session, still the Quality Score's main drag (§5). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS — this session's Forward PE (14.82×) ticked up slightly from 09-01's 14.22× as the live price rose faster than the (also slightly higher) forward-EPS estimate. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score — none triggered this session. |
| **Hugging Face** | The AI developer platform NVIDIA entered a definitive agreement to acquire for a combined ~$12.9B, per its own 2026-09-03 8-K — see §2 for full verification, §5 for its moat implications, and the framework [glossary.md](../framework/glossary.md) entry for the full description. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Hyperscaler** | An operator of very-large-scale, globally-distributed cloud/data-center infrastructure — the primary buyer category for NVIDIA's data-center GPUs. |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **IR (Investor Relations)** | A public company's function/department responsible for communicating with investors and analysts. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt; negative means net cash. Unchanged this session; the future Hugging Face cash outflow (if cash-funded — undisclosed, §2) would reduce this cushion once the deal closes (not yet reflected). |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **PW** | Probability-weighted (the bull/base/bear scenario blend). |
| **Quality Score** | This framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required for Phase 02/Composite Score. NVDA: 90.3 this session, unchanged from 08-27/09-01. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. NVDA's order setup this session computes **1.73:1 — fails the gate** (§10), reversing 09-01's brief 2.06:1 pass. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive adjustment(s) for the current Treasury-yield regime. Step 1 still passes this session (+1.99pp spread); Step 2 unchanged at +5 — total +5, same as 09-01. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 3 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; triangulate fair value across two methods; force re-valuation on specific fundamental triggers (the Hugging Face deal independently satisfies the "material M&A" trigger this session, §2); and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — unchanged this session (no new quarter filed). |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs. the 10% hurdle. Pinned at its −15.0 floor again this session (fifth consecutive NVDA session), though the underlying E (+29.67%) has drifted down from 09-01's +33.08% as the price rally narrows the gap to fair value. |
| **XBRL (eXtensible Business Reporting Language)** | The SEC's structured, machine-readable financial-data tagging format. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

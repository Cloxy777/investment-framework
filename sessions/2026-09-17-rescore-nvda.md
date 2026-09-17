# RESCORE — NVDA (NVIDIA Corporation)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-09-17
**10Y US Treasury Yield:** 4.95% (TradingEconomics — [tradingeconomics.com/united-states/government-bond-yield](https://tradingeconomics.com/united-states/government-bond-yield), pulled 2026-09-17; "fell to 4.95% on Thursday, below the 2007 high of 5.04% reached earlier in the week" — post-FOMC-hike move; CNBC corroborates the same regime)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** NVDA **24.1** Composite (Quality 90.3 / Valuation 38.5), 2026-09-04 — [sessions/2026-09-04-rescore-nvda.md](2026-09-04-rescore-nvda.md)
**Current NVDA portfolio weight:** ≈6.79% live (19 sh × $218.70 = $4,155.30 ÷ $61,192.89, the last portfolio-wide combined total on file in [holdings.md](../portfolio/holdings.md), dated 2026-09-13 — this session refreshes NVDA's own numbers only, not a full portfolio resync; same convention as 09-01/09-04). **≥5% of portfolio — priority tier.** Comfortably under the 15% hard cap (Upgrade 7) and the 8% allocation cap (≈22.4 shares).
**Not on the stale-score registry** ([watchlist/STALE.md](../watchlist/STALE.md)) — checked, no pending mark to clear.

## Why this session ran

**Unattended Routine 6 (Telegram Stock-Mention Scan) trigger.** Monitored channel `FinnInvestChannel` posted (Ukrainian, translated) at 2026-09-17 13:39 UTC (post ID `FinnInvestChannel/3232`): *"Jensen Huang says NVIDIA will sell roughly twice as many AI chips in 2027 as in 2026. NVIDIA is preparing for another huge supply increase. Jensen also emphasized AI safety remains a priority and unsafe products shouldn't reach market."*

**Provenance only — not a data source.** Every figure below is independently sourced; the claim itself is verified in §2 before being treated as context for the session.

---

## 2. Independent Verification of the "Double AI Chip Sales 2027 vs 2026" Claim

**Verdict: TRUE — verified via Bloomberg's own reporting of Jensen Huang's on-the-record remarks, corroborated by multiple independent outlets reporting the same event; the AI-safety portion independently corroborated via direct quotes carried by a second outlet at the same event.**

| Claim element | Verification | Source |
|---|---|---|
| Huang says NVIDIA will sell ~2× as many AI chips in 2027 as 2026 | **Confirmed.** Reported same-day (2026-09-17): "Nvidia's Huang Expects to Sell Twice as Many Chips Next Year." Huang made the comment to reporters on the sidelines of an AI summit convened by King Charles III in Scotland, saying continued demand for AI computing infrastructure supports selling roughly double the chip volume next year vs. this year. | **Primary-adjacent (direct on-the-record CEO remarks, contemporaneously reported):** [Bloomberg, 2026-09-17](https://www.bloomberg.com/news/articles/2026-09-17/nvidia-s-huang-expects-to-sell-twice-as-many-chips-next-year) (headline/lede visible via search index; full article paywalled — 403 on direct fetch). **Corroborating (same wire story republished):** bitcoinethereumnews.com, coinpaper.com (fetch attempts 403/522 — sites confirmed to exist and carry the identical Bloomberg-sourced claim via search-index snippets, not independently re-verified full text). |
| Event: King Charles III AI summit, Scotland, ~2026-09-17/18 | **Confirmed independently, separate from the Bloomberg piece.** [Korea Times, 2026-09-18](https://www.koreatimes.co.kr/world/20260918/king-charles-warns-ai-leaders-of-existential-dangers) and [ABC News](https://www.abc.net.au/news/2026-09-18/king-charles-warns-ai-leaders-of-existential-dangers/107166548) confirm King Charles III hosted NVIDIA's and Google DeepMind's co-founders plus OpenAI/Anthropic leadership in Scotland this week, with Charles warning of AI's "existential dangers." Cross-confirms the event Bloomberg places Huang's remark at. |
| AI safety remains a priority / unsafe products shouldn't reach market | **Confirmed, direct quote.** Korea Times: Huang told the room safety was "paramount," and — quoted directly — "If it's not ready, just hold it back. You should go as fast as you can, but no faster than that," framing this as developers' responsibility ("responsible optimism"). Matches the Telegram post's paraphrase closely. | [Korea Times, 2026-09-18](https://www.koreatimes.co.kr/world/20260918/king-charles-warns-ai-leaders-of-existential-dangers) |
| "NVIDIA preparing for another huge supply increase" | **Directionally consistent, not independently pinned to a specific new commitment.** No primary NVIDIA IR release, 8-K, or transcript was found stating a specific supply-expansion program tied to this remark (see Data Gap note below) — treated as color/paraphrase of the chip-doubling comment above, not a separate verified fact. | — |

**Materiality assessment for the score:** this is Huang's own **unaudited, self-reported, forward-looking verbal remark** — explicitly the category the framework's valuation-scoring.md "Why Forward Guidance Is Not a Sub-score" section excludes from scored inputs (self-reported, unaudited, management has means/incentive to talk the stock up). It is also **not a revision** of NVIDIA's most recent formal guidance: at the 2026-08-26 Q2 FY2027 earnings call (already reflected in the 08-27/09-01/09-04 sessions), management guided ~70% FY2028 revenue growth. Doubling unit chip *volume* is not mathematically the same as doubling *revenue* (ASP/mix/Blackwell→Vera Rubin transition effects apply, per the framework's own PEG/Fast-Grower reasoning) — so this comment reinforces, rather than revises up or down, the already-known bullish growth narrative. **Conclusion: verified TRUE, but not a Rule 9 "guidance revision" trigger in its own right** (no filed guidance changed) — it is corroborating qualitative evidence for the same Growth/Moat narrative already captured (and already at its scoring ceiling — see §5), consistent with how the 09-01 MediaTek investment and 09-04 Hugging Face acquisition were both treated as real-but-non-numeric-input events. This session proceeds as a routine Telegram-triggered check-in rather than a fundamentals-moving event.

**No new NVIDIA SEC filing exists to independently corroborate the chip-volume claim** — confirmed via `data.sec.gov/submissions/CIK0001045810.json`: the only NVIDIA filings since the 2026-09-03 Hugging Face 8-K are Form 3/4 insider-transaction filings (2026-09-02 through 2026-09-11) — no new 8-K, no new 10-Q. This is flagged as a genuine sourcing limitation (media-reported CEO remarks at a public event, not a company filing), not treated as disqualifying — the underlying claim is still independently corroborated across multiple unrelated news organizations reporting the same event.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$218.70** | IBKR `get_price_snapshot` (contract_id 4815747, NASDAQ), last trade, ts 1789661206 (2026-09-17). Bid/ask $218.68/$218.69. |
| Today's move | **+$4.80 / +2.24%** | IBKR `change`. Small, well under the 15% Rule 9 threshold. |
| 52-week range | $164.08 – $236.27 | IBKR `misc_statistics`. |
| YTD change | +17.41% ($32.42) | IBKR `year_to_date_change` — down from 09-04's +24.26% (the ~$213–232 pullback over the intervening two weeks; not a >15% single-move Rule 9 trigger). |
| Analyst consensus PT (source 1) | mean **$328.66**, 61 analysts, "Strong Buy" | stockanalysis.com/stocks/nvda/, pulled 2026-09-17. |
| Analyst consensus PT (source 2, cross-check) | mean **$324.34**, high $515.00, low $218.00, 55 analysts, "Buy" (53 buy / 3 strong buy / 2 hold, 0 sell) | marketbeat.com/stocks/NASDAQ/NVDA/price-target/, pulled 2026-09-17 — essentially unchanged from 09-04's $324.83. |

NVDA is down from $231.73 (09-04) to $218.70 today (−5.62% over 13 days) — ordinary drift, not a fundamental event; no known company-specific news explains it and it's well under the ±15% Rule 9 unexplained-move threshold.

---

## 3. Data Gaps / Sourcing Notes (flagged, not silently worked around)

1. **`yfinance` still unavailable — fourth consecutive session.** Fresh attempt this session failed with a different but related symptom: `HTTP 429 (crumb rate-limited)` then `HTTP 401 Unauthorized / Invalid Crumb` on `Ticker.info`. This is now a clearly durable infrastructure issue across four sessions (08-27 through today), not transient — worth escalating outside the analysis session (per 09-04's flag, still unresolved). Substitute sourcing (same discipline as prior sessions): IBKR (live price, Rule 0), SEC EDGAR (filing list — no new 8-K/10-Q since 09-03), stockanalysis.com + finviz.com (forward EPS/PE, PEG, consensus PT), marketbeat.com (consensus PT cross-check), WebSearch/WebFetch (10Y yield, Telegram-claim verification).
2. **No new fiscal quarter since the 09-04 session — confirmed via SEC EDGAR filing list.** `data.sec.gov/submissions/CIK0001045810.json` shows only Form 3/4 insider filings between 2026-09-02 and 2026-09-11; no new 8-K or 10-Q. All TTM/annual financial-statement inputs (revenue, EBIT, net income, FCF, margins, ROIC, net debt, gross margin, revenue CAGR, FCF/NI ratio) are therefore **unchanged from 09-04 and reused verbatim** below. Next earnings (Q3 FY2027) still ~25 Nov 2026.
3. **Forward EPS — same vendor divergence flagged three sessions running; finviz used again per established (not yet formally documented) convention.** stockanalysis.com implies a forward PE of 17.75× at $218.65 (⇒ ~$12.32 forward EPS) that does **not** internally reconcile with its own trailing-EPS/PE figures the way finviz's does. finviz: Forward P/E 13.92 × EPS next Y $15.70 = $218.60 ≈ live price ($218.70) — internally consistent, continues smoothly from the 09-04 session's $15.64 (+0.4%, a plausible small drift). **Used this session: Forward EPS = $15.70 (finviz).** This is now a 4-session-old open methodology item (see §11) — still worth a `decisions/` entry to pick one authoritative forward-EPS source.
4. **PEG — self-computed again** (Lynch definition, same methodology as every prior session): Forward PE (13.930×, §4) ÷ 69.60% (finviz's "EPS next Y % growth") = **PEG 0.2001**. (finviz's own displayed PEG field independently shows 0.22 — close, not identical, likely a slightly different EPS-growth denominator on finviz's side; self-computed figure used per established convention.)
5. **5-year PE table — not independently re-derived this session; carried forward from 09-01/09-04 with an explicit flag.** Blocked by the same yfinance outage (#1); no reliable alternate bulk-history source found this session either (same macrotrends/wisesheets issues flagged 09-04). Underlying 20-quarter trailing window has not rolled forward (no new quarter filed) — reuses 09-04's figure verbatim: **avg 57.84×, range 25.97×–142.78× (n=20 quarters)** — flagged as *reused*, not independently re-derived.
6. **Cross-check on reused TTM figures:** stockanalysis.com's and finviz's independently-reported trailing EPS ($7.91) and profit margin (63.66%) both exactly match the reused SEC-derived figures — strong corroboration the reused numbers remain current.
7. **Next earnings date — unchanged, still a third-party estimate.** ~25 Nov 2026, after close (Q3 FY2027), not yet NVIDIA-IR-confirmed.
8. **"NVIDIA preparing for another huge supply increase" (Telegram paraphrase)** — no specific primary-sourced commitment found beyond the chip-doubling remark itself (§2). Not treated as an independent fact.

---

## 4. NVDA — Inputs Collected (TTM rollup, reused from 09-04 session — see [2026-08-27 session](2026-08-27-rescore-nvda.md) for the full line-by-line SEC XBRL derivation; only live-dependent rows refreshed)

**Sector:** Technology — Semiconductors (AI Compute & Data-Center GPUs)
**TTM window: Q3 FY2026 + Q4 FY2026 (derived) + Q1 FY2027 + Q2 FY2027 — unchanged, no new quarter since 08-27**

| Item | Value | Source / status this session |
|---|---|---|
| Shares outstanding | 24,100,000,000 | SEC 10-Q cover page, filed 2026-08-21 — still the freshest figure on file, unchanged; cross-checked against finviz Market Cap ($5,268.98B) ÷ finviz price ($218.65) = 24.10B — consistent |
| **Market Cap** | 24.1B × $218.70 = **$5,270,670M** | Recomputed — live price refresh |
| TTM Revenue | **$302,969M** | Unchanged (SEC XBRL, reused) |
| TTM EBIT | **$197,579M** | Unchanged |
| TTM Net Income | **$192,879M** | Unchanged |
| TTM Operating Cash Flow | **$134,360M** | Unchanged |
| TTM CapEx | **$7,354M** | Unchanged |
| **TTM FCF** | **$127,006M** | Unchanged |
| TTM D&A / TTM EBITDA | $3,687M / **$201,266M** | Unchanged |
| TTM Gross Profit | **$226,241M** | Unchanged |
| **Gross Margin (TTM)** | **74.68%** | Unchanged (finviz shows 74.67%, rounding-level match) |
| **Net Margin (TTM)** | **63.66%** | Unchanged — exact finviz match |
| Total Debt (2026-07-26) | **$33,366M** | Unchanged — predates the not-yet-closed Hugging Face deal |
| Cash + ST marketable securities (2026-07-26) | **$56,586M** | Unchanged |
| **Net Debt** | **−$23,220M (net cash)** | Unchanged |
| **Enterprise Value** | $5,270,670M + (−$23,220M) = **$5,247,450M** | Recomputed off refreshed market cap |
| **EV/EBIT** | $5,247,450M ÷ $197,579M = **26.560×** | Recomputed |
| Stockholders' Equity / Invested Capital / NOPAT / **ROIC (TTM)** | $228,984M / $262,350M / $165,873M / **63.21%** | Unchanged (SEC-derived; finviz's own ROIC field shows 72.42% on a different formula — not used, kept consistent with framework's own NOPAT/Invested-Capital methodology) |
| Revenue 3yr CAGR (FY2023→FY2026) | **100.05%** | Unchanged |
| Forward EPS (finviz "EPS next Y", see Data Gap #3) | **$15.70** | Refreshed — finviz.com, 2026-09-17 |
| **Forward PE** | $218.70 ÷ $15.70 = **13.930×** | Recomputed |
| EPS next Y % growth (finviz) | **69.60%** | Refreshed |
| PEG (self-computed, see Data Gap #4) | **0.2001** | Recomputed: 13.930 ÷ 69.60% growth |
| 5yr avg/range PE | avg **57.84×**, range **25.97×–142.78×** (n=20 quarters) | **Reused verbatim from 09-01/09-04** — see Data Gap #5 |
| FCF/NI conversion (TTM) | **65.85%** | Unchanged — still the Quality Score swing factor, see §5 |
| FCF/NI conversion (annual, FY23–FY26) | 87.18% / 90.80% / 83.50% / 80.51% | Unchanged |
| Diluted weighted-avg shares (Q2 FY27 vs Q2 FY26) → buyback yield | 24,285M vs 24,532M → **+1.007%/yr** | Unchanged |
| Dividend rate (forward run-rate) | $1.00/yr ÷ $218.70 = **0.4572%** | Recomputed off refreshed price |
| Next earnings | ~25 Nov 2026, after close (Q3 FY2027), unconfirmed by NVIDIA IR | Unchanged |

---

## 5. NVDA — Quality Score (2026-06-29 methodology)

**All inputs to this section are unchanged from 08-27/09-01/09-04 (no new fiscal quarter reported) — recomputed below for completeness and transparency, per the operating brief's "always show full calculation" rule, not because any input actually moved.**

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
No structural-deceleration modifier applies (moot at the cap regardless). **Huang's Scotland remarks (§2) are corroborating — not scored — TAM/demand-durability evidence**, reinforcing the same narrative already captured; doesn't move a score already at its 100.0 ceiling.

### Balance Sheet (15% weight)
```
BalanceSheet_Score = clamp(100×(1 − (−0.115)/4)) = 100.0
```
Unchanged. Flag carried forward: the ~$11.9B Hugging Face acquisition (H1 2027 close, funding mix undisclosed) not yet reflected.

### Moat Signal (15% weight) — light refresh; Huang's public remarks noted as corroborating narrative, no signal flip

| Signal | Marked | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Unchanged basis (Data Center 92% of revenue, 08-27 session). |
| Brand premium | **TRUE** | Unchanged. |
| Network effect | **TRUE** | Unchanged CUDA-ecosystem basis; Huang's public "twice as many chips in 2027" remark (§2) is consistent color on demand durability but adds no new documented mechanism beyond what's already TRUE. |
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

# Quality Score = 90.3 — PASSES the 80.0+ gate, unchanged from 08-27/09-01/09-04 (no quality-relevant fundamental has moved).

---

## 6. NVDA — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 13.930 = 7.1787%
Spread = EY − 10Y Treasury = 7.1787% − 4.95% = +2.2287 pp
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+2.23pp ≥ 1.5%) → **no Step 1 additive**. Margin widened vs. 09-04 (+1.99pp → +2.23pp) as Forward PE compressed on the live-price pullback, partly offset by the 10Y yield rising (4.76% → 4.95%, post-FOMC).

**Step 2 — Rate Regime Modifier**
10Y = 4.95% → "3.5–5%" bracket → **+5** (unchanged bracket; close to the 5% boundary — worth a closer look at the next quarterly Rate Environment Gate refresh in October if the 10Y crosses 5%).

**Total Rate Modifier for NVDA = 0 (Step 1) + 5 (Step 2) = +5** — unchanged from 09-01/09-04.

---

## 7. NVDA — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF Yield = $127,006M ÷ $5,270,670M (mktcap) = 2.4096%
FCF_Score = clamp(100 × (1 − 2.4096/10)) = 75.904
```
→ Contribution: 75.904 × 0.40 = **30.362**

**EV/EBIT — 25% weight**
```
EV/EBIT = 26.560×
EV/EBIT_Score = clamp((26.560 − 12)/23 × 100) = 63.304
```
→ Contribution: 63.304 × 0.25 = **15.826**

**Forward PE — 20% weight (fallback formula, folds in Historical PE Modifier)**
```
Deviation% = (13.930 − 57.84) / 57.84 × 100 = −75.918%
FwdPE_Score = clamp(50 + (−75.918) × 2.5) = clamp(−139.80) = 0.0   (floor)
```
→ Contribution: **0.00**

**PEG — 15% weight (Fast Grower — determination unchanged from every prior session)**
```
PEG = 0.2001
PEG_Score = clamp((0.2001 − 0.5)/2.0 × 100) = clamp(−14.995) = 0.0   (floor)
```
→ Contribution: **0.00**

**Raw weighted score:**
```
= 30.362 + 15.826 + 0.00 + 0.00 = 46.188
```
**+ Rate Modifier (+5) = 51.188** (before the Upside/Downside Modifier)

---

## 8. NVDA — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture — base case rebuilt on refreshed consensus forward EPS ($15.70); bull/bear qualitative assumptions carried forward unchanged (no fundamental shift to the multi-year bull/bear framing since 09-04 — Huang's Scotland remarks reinforce, not alter, the bull-case demand-durability narrative):**

| Scenario | Wt | EPS basis | Exit PE | Rationale | Fair Value |
|---|---|---|---|---|---|
| **Bull** | 25% | $18.00 | 24× | AI-infrastructure supercycle continues; Vera Rubin ramp (H2 2026); Huang's public "twice as many chips in 2027" remark (§2) is consistent color for continued demand durability into 2027, but is unaudited CEO commentary, not new filed guidance — doesn't independently justify raising the bull EPS assumption this session. Unchanged from 09-04. | $18.00 × 24 = **$432.00** |
| **Base** | 50% | $15.70 (consensus forward EPS, §3.3/§4) | 21× | Consensus-anchored; result ($329.70) sits within ~1% of both aggregators' mean PT ($328.66 / $324.34, §1) — independent sanity-check pass. | $15.70 × 21 = **$329.70** |
| **Bear** | 25% | $11.00 | 16× | AI-capex-digestion scenario, unchanged framing: hyperscaler spend plateaus, a real miss vs. the Q3 guide, multiple compresses to a cyclical-trough ~16×. Anchored below the $218.00 Street low (marketbeat.com, unchanged from 09-04). | $11.00 × 16 = **$176.00** |

```
PW Fair Value = 0.25×432.00 + 0.50×329.70 + 0.25×176.00 = $316.85
Gap Upside %  = (316.85 ÷ 218.70) − 1 = +44.878%
```
Sits ~3–4% below both analyst consensus means (~$325–329) — conservative, Guardrail 2 sanity check passes.

**Step 1 — Annualize over catalyst window (Rule 10):**
Catalyst: Q3 FY2027 earnings ~25 Nov 2026 (unchanged framing) → **2-year** default, unchanged.
```
Annualized gap = 44.878% ÷ 2 = +22.439%/yr
```

**Step 2 — Build E:**
```
Intrinsic growth   = +10.0%/yr    (unchanged conservative convention)
Shareholder yield  = +1.4642%     (dividend 0.4572% + net buyback yield 1.007%)
E = 22.439 + 10.0 + 1.4642 = +33.903%/yr
```

**Step 3 — Map E to modifier (hurdle H = 10%):**
```
E = 33.903% ≥ H → M = −15 × clamp((33.903−10)/15, 0, 1) = −15 × clamp(1.594, 0, 1) = −15 × 1.0 = −15.0
```
**Catalyst guardrail:** documented catalyst within 18–24 months exists (Q3 earnings ~25 Nov 2026) → full upside credit applies, not capped.

**Upside/Downside Modifier = −15.0** (floor — sixth consecutive NVDA session pinned here; underlying E has actually *widened* from 09-04's +29.67% since the price pullback increased the gap to PW fair value faster than the modest base-EPS increase — still comfortably clears the floor's 25%/yr threshold).

---

## 9. NVDA — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (46.188) + Rate Modifier (+5) + Upside/Downside (−15.0)
                       = 36.188
```
Boundary rule: not a ".X5" case → standard rounding → **Final Valuation Score = 36.2**

| | Value |
|---|---|
| Raw weighted | 46.188 |
| Rate Gate (Step 1 pass +0, Step 2 +5) | +5 |
| Upside/Downside Modifier | −15.0 (E = +33.90%) |
| **FINAL VALUATION SCORE** | **36.2** |
| Prior valuation score | 38.5 (09-04) |
| **Quality Score** | **90.3 (PASSES 80.0+ gate)** — unchanged |
| Prior Quality Score | 90.3 (09-04) |

**Composite Score:**
```
Composite Score = 0.50×(100 − 90.3) + 0.50×36.2 = 0.50×9.7 + 0.50×36.2 = 4.85 + 18.10 = 22.95
```
Boundary rule: 22.95 falls exactly on a ".X5" → round **up** (more conservative) → **Composite Score = 23.0**

# Composite Score = 23.0 → band 0.0–29.9 "Very Cheap" → nominal Action Table band: BUY — Full position 6–8%

Quality Score unchanged (no fundamental has moved). Valuation Score fell 38.5 → 36.2 (Composite 24.1 → 23.0) — driven entirely by the ~5.6% live-price pullback since 09-04 lowering EV/EBIT and Forward PE and widening the Upside/Downside gap, **not** by any change to the underlying business, and consistent with (not caused by) the Telegram trigger's content. See §10 — this session's order-setup R/R gate **passes** for the first time since 09-01.

---

## 10. NVDA — Action Recommendation & Order Setup

**Composite Score 23.0 (Very Cheap, 0.0–29.9 band) nominally qualifies for a full position (6–8%) — full order setup shown per the operating brief's requirement for any BUY-band score.**

### Fair Value (Rule 3 triangulation: 40% DCF-style / 60% multiples)
```
DCF-style (scenario PW FV)                              = $316.85
Multiples (avg of both aggregators' consensus mean, §1) = (328.66 + 324.34)/2 = $326.50
Blended Fair Value = 0.40 × 316.85 + 0.60 × 326.50 = $322.64
```
Fair value range ~$176 (bear) – $432 (bull), base case ~$330 (Rule 10 — a range, not a point).

### Order setup
```
Margin of Safety = 17.5% (midpoint, 15–20% band for Score 0.0–29.9 — unchanged convention)
Buy Price (ceiling) = $322.64 × (1 − 0.175) = $266.18
Live price $218.70 is below the ceiling → "enter now" territory IF R/R clears
Primary Sell Target = Blended FV = $322.64
Bull-Case Trim Target = Bull FV $432.00 × 0.90 = $388.80
Stop Loss = Live Price × (1 − 0.225) = $218.70 × 0.775 = $169.49   (22.5% midpoint, off live price since live < ceiling)
R/R = (322.64 − 218.70) / (218.70 − 169.49) = 103.94 / 49.21 = 2.1122 : 1
```

### ✅ R/R gate PASSES this session — 2.11:1 ≥ 2:1 minimum
This is the second time (of six sessions) the R/R gate has cleared, and the first pass since 09-01 (2.06:1) — the price pullback since 09-04 widened the reward side of the ratio (entry price fell $13.03 while Blended Fair Value actually rose slightly on the refreshed consensus PT).

**Position sizing — the binding constraint, checked independently:**
```
Combined portfolio total (holdings.md, 2026-09-13 sync) = $61,192.89
Max $ Risk per trade = 1.5% × $61,192.89 = $917.89
Risk Per Share = $218.70 − $169.49 = $49.21
Max shares by risk-based sizing = $917.89 ÷ $49.21 = 18.655 shares
Current live position = 19 shares (IBKR `get_account_positions`, confirmed unchanged — same 19-share position, avg cost $182.51)
```
**19 shares still (narrowly) exceeds the 18.655-share risk-based full-target size** — the gap has closed substantially versus 09-04 (19 vs. 17.95, a 1.05-share gap) to just 0.345 shares this session, but the position remains marginally above target. Cap check: the 8% allocation ceiling (≈22.4 shares at this price) has ample room, but the framework takes the lower of the two (risk-based vs. cap), and risk-based sizing remains the binding constraint, narrowly.

**Position cap check:** ≈6.79% of portfolio — nowhere near the 15% hard cap (Upgrade 7) or the 8% allocation cap.

### Practical action: HOLD the existing ≈6.79% position — no add, no trim.
- **No add:** despite the R/R gate clearing (2.11:1) for the first time since 09-01, the position still sits marginally above its risk-based full-target size (19 vs. 18.655 shares) — a single, narrowing binding constraint this session (unlike 09-04's two independent blockers).
- **No trim:** Composite Score 23.0 is nowhere near the 70+ trim bands; anti-turnover posture applies regardless.
- **Worth flagging explicitly:** this is the fourth consecutive "practical HOLD, no add" outcome, but the R/R-and-sizing gap has been narrowing steadily (08-27: R/R fail alone; 09-01: R/R pass, sizing bound by ~0.0 shares; 09-04: both fail, sizing gap 1.05 sh; 09-17: R/R pass, sizing gap narrowed to 0.35 sh). The underlying Composite Score has stayed in the "Very Cheap" band throughout (21.3 → 25.5 → 23.0 → 24.1 → 23.0 across the last five sessions) — this is short-run price noise around a broadly stable valuation read, not a thesis change. **If the live price drifts even modestly lower before the next check (or the portfolio total grows), the sizing gap would likely close and support a small top-up** — worth a human glance sooner than the next scheduled trigger if that happens.

**Thesis invalidation triggers (Phase 06 / stop), carried forward from 09-04 unchanged:**
- AI-capex digestion: hyperscaler capex growth materially decelerates or reverses without a one-off cause (watch the ~25 Nov 2026 Q3 print against the $108.0B guide)
- **FCF/NI conversion — still the most time-sensitive watch item.** TTM 65.85%, unchanged this session; re-derive at FY2027 year-end (~Feb 2027) for the 2-consecutive-year disqualifier check.
- Gross margin falls >3pp structurally (currently 74.68% TTM, stable)
- CUDA moat erosion: no material enterprise-workload migration to a competing stack documented at scale
- Net debt/EBITDA rising materially — still deep net cash; the ~$11.9B Hugging Face outlay (closing H1 2027, funding mix undisclosed) is a future watch item, not yet a live one
- Regulatory restriction on open-source/open-weight AI model distribution (disclosed in NVIDIA's 09-03 8-K risk factors) — not yet a live event; tracked as a watch item
- Price through the $169.49 stop level (informational — no position adjustment pending)

All final-decision authority rests with the human investor. **No order was placed or modified by this session — recommendation only.**

---

## 11. Next Review Trigger

- **Routine:** NVDA Q3 FY2027 earnings, estimated **~25 Nov 2026, after close** (unconfirmed by NVIDIA IR) — will refresh every TTM fundamental used here.
- **Quarterly Rate Environment Gate refresh** — October 2026. Worth a closer look given the 10Y (4.95%) is now within 0.05pp of the 5% bracket boundary — a further Fed-hike-driven rise would push the Rate Regime Modifier from +5 to +10.
- **Sizing watch (new this session):** the R/R-gate-pass / sizing-gap combination has narrowed to just 0.345 shares — a small further price pullback or portfolio-total change could flip this to an actionable top-up before the next scheduled trigger. Not itself a scheduled trigger, but worth a human glance if the live price moves further.
- **Watch (unchanged):** FCF/NI conversion trend (65.85% TTM) — re-derive at FY2027 year-end (~Feb 2027) for the 2-consecutive-year disqualifier condition.
- **Open methodology items (unresolved, now spanning four sessions):** (1) forward-EPS/forward-PE vendor divergence (stockanalysis.com vs. finviz) — still unresolved, worth a `decisions/` entry; (2) `yfinance` unavailability (fourth consecutive session, now a different failure mode — 429/401 crumb rejection vs. earlier SSL resets — looks like Yahoo-side API hardening rather than a transient network issue, worth escalating outside the analysis session); (3) the 5yr avg/range PE reconstruction remains reused, not independently re-derived, pending yfinance access or an alternate bulk-history source.
- **Hugging Face acquisition** — unchanged watch item: track regulatory-approval progress toward the expected H1 2027 close; watch for disclosure of the $11.9B stockholder consideration's funding mix.
- **New regulatory-risk watch item (unchanged from 09-04):** government restriction on open-source/open-weight AI model distribution, esp. China-origin models.
- **Rule 9 triggers (standing):** guidance revision (a *filed* one — today's Huang remark does not qualify, per §2), further M&A/strategic-investment announcements, management change, a >15% unexplained price move, a credible short report, or the ~25 Nov 2026 earnings print itself.

---

## Glossary

| Term | Meaning |
|---|---|
| **8-K** | The "current report" a US public company files with the SEC within days of a material event. Checked this session (via EDGAR's submissions JSON) to confirm no new 8-K has been filed since the 2026-09-03 Hugging Face announcement. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate. NVDA: 23.0 this session (Very Cheap band), though position sizing narrowly blocks an actual add (§10). |
| **CUDA** | NVIDIA's proprietary parallel-computing software platform for its GPUs — the basis for this framework's Network Effect and Switching Costs moat findings. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EDGAR** | The SEC's public database of company filings — used this session to confirm no new filing exists to corroborate the Telegram claim (§2), and no new financial-statement filing since 09-03. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield in the Rate Environment Gate. This session's spread (+2.23pp) clears the Step-1 pass threshold with a wider margin than 09-04. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — NVDA's PEG-eligibility trigger, unchanged this session. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality) — TTM FCF/NI ratio (65.85%) unchanged this session, still the Quality Score's main drag (§5). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS — this session's Forward PE (13.93×) fell from 09-04's 14.82× as the live price pulled back faster than the (slightly higher) forward-EPS estimate. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score — none triggered this session. |
| **Hugging Face** | The AI developer platform NVIDIA entered a definitive agreement to acquire for a combined ~$12.9B (2026-09-02, disclosed via 8-K 2026-09-03) — see the 2026-09-04 session for full verification; the [glossary.md](../framework/glossary.md) entry has the full description. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Hyperscaler** | An operator of very-large-scale, globally-distributed cloud/data-center infrastructure — the primary buyer category for NVIDIA's data-center GPUs. |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **IR (Investor Relations)** | A public company's function/department responsible for communicating with investors and analysts — checked this session for a primary source on the chip-doubling claim; none found beyond the media-reported remark itself (§2). |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt; negative means net cash. Unchanged this session. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **PW** | Probability-weighted (the bull/base/bear scenario blend). |
| **Quality Score** | This framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required for Phase 02/Composite Score. NVDA: 90.3 this session, unchanged from 08-27/09-01/09-04. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. NVDA's order setup this session computes **2.11:1 — passes the gate** (§10), for the first time since 09-01. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive adjustment(s) for the current Treasury-yield regime. Step 1 passes this session (+2.23pp spread, widened from 09-04); Step 2 unchanged at +5 — total +5. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 3 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; triangulate fair value across two methods; force re-valuation on specific fundamental triggers (this session's Telegram claim is verified TRUE but explicitly does **not** qualify as a Rule 9 "guidance revision" — see §2); and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — unchanged this session (no new quarter filed). |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs. the 10% hurdle. Pinned at its −15.0 floor again this session (sixth consecutive NVDA session), with the underlying E actually widening to +33.90% (from 09-04's +29.67%) as the price pullback increased the gap to fair value. |
| **XBRL (eXtensible Business Reporting Language)** | The SEC's structured, machine-readable financial-data tagging format. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

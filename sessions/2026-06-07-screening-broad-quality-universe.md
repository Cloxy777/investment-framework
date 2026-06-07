# 2026-06-07 — SCREENING: Broad Quality Universe (funnel → scored shortlist)

**Task type:** SCREENING (Phase 01), extended into Phase 02 scoring at the user's explicit request — *"I want as much as possible, but make it efficient: apply more and more filters and when you get to ~10–30 tickers, do full analysis with scoring."*
**Date:** 2026-06-07 · **10Y US Treasury yield:** 4.55% (close 2026-06-05, last trading session before the weekend) · **Rate Regime Modifier in effect:** +0.5 (10Y in the 3.5–5% band — "capital has real cost")

---

## 0. Methodology — why this universe, and how it was funneled

A true from-scratch quantitative pull across the S&P 500 (or broader) isn't feasible here — it would require bulk fundamental-data access (margins, ROIC, FCF, debt for ~500 names) that I don't have, and researching 500 companies one at a time risks exactly the "invented/estimated data" problem [CLAUDE.md](../CLAUDE.md) forbids. Instead, per the framework's own named tools ([valuation-scoring.md](../framework/valuation-scoring.md): *"Gurufocus — Quality/value combo screens, Magic Formula, Buffett-style filters"*), I started from **existing, published quality pre-screens** — funds and screens that already do quality-factor filtering at scale — and ran the Phase 01 gate on that pre-filtered set. This is the "cast a wide net efficiently" approach the user asked for.

**Starting sources (each independently quality-screened by a different methodology):**
- **MOAT** — VanEck Morningstar Wide Moat ETF (Morningstar's economic-moat methodology) — top 25 of 58 holdings
- **QUAL** — iShares MSCI USA Quality Factor ETF (high ROE, stable earnings, low leverage) — top 25 of 129 holdings
- **QGRW** — WisdomTree U.S. Quality Growth Fund (quality + growth composite) — top 25 of 100 holdings
- **Cross-check:** Greenblatt Magic Formula screens (GuruFocus / Validea) — current top names are small/micro-cap special situations (HRB, DFIN, NRDS, etc.) that don't fit this framework's "wonderful business" quality bar; none overlapped with the ETF-sourced universe, so they didn't add qualified candidates. Noted for completeness, not pursued further.

Sources: [stockanalysis.com/etf/moat/holdings](https://stockanalysis.com/etf/moat/holdings/) · [stockanalysis.com/etf/qual/holdings](https://stockanalysis.com/etf/qual/holdings/) · [stockanalysis.com/etf/qgrw/holdings](https://stockanalysis.com/etf/qgrw/holdings/) · [validea.com/joel-greenblatt-stocks](https://www.validea.com/joel-greenblatt-stocks)

---

## Stage 1 — Deduplicated starting universe (≈56 names)

Combining the three lists and removing duplicates:

AAPL, ABNB, AMAT, AMD, AMZN†, ANET, APP, AVGO, BF.B, BMY, BR, BRK.B, CAT, CLX, COST, CRWD, DDOG, DHR, EL, FTNT, GE, GEHC, GEV, GOOG/GOOGL†, JNJ, KLAC, KVUE, LIN, LLY, LPLA, LRCX, MA, MAS, MDLZ, META†, MRK, MSFT†, MU, NFLX†, NKE†, NVDA†, NXPI, ORCL, OTIS, PANW, PLTR, ROST, STZ, TJX, TLT, TRU, TSLA, TYL, V†, WMT, XOM, ZBH

**† = already a portfolio holding** (AMZN, GOOG, META, MSFT, NFLX, NKE, NVDA, V — 8 names). These are excluded from "new candidate" consideration here — they're already tracked and re-scored on their own earnings cadence via [/rescore](../.claude/commands/rescore.md); re-discovering them in a screen adds nothing. **48 names** remain as candidates.

---

## Stage 2 — Structural triage (categorical first pass)

Before spending real research budget on detailed numbers, I eliminated names that **structurally** cannot pass the Phase 01 bar on well-documented, public business-model grounds (thin-margin volume retail, commodity cyclicals, patent-cliff pharma, slow-growth industrials/staples). This is reasoning from well-established business-model characteristics — not invented figures — exactly the kind of triage a human analyst does before pulling 48 sets of detailed financials. **Flagged transparently so any of these can be pulled back in for full review on request:**

| Eliminated | Why (structural, not measured) |
|---|---|
| WMT, COST, TJX, ROST | Large-volume retail — net margins structurally 2–6%, far below the >15% bar |
| XOM | Integrated oil major — commodity-cyclical margins/revenue, not a structural >10% CAGR business |
| MAS | Building products — mid-single-digit net margins, cyclical, low growth |
| MDLZ, KVUE, CLX, STZ, BF.B | Packaged consumer staples — margins mostly 8–15%, low-single-digit revenue growth (well below >10% CAGR) |
| BMY, MRK, JNJ | Large pharma in well-documented patent-cliff cycles — low-single-digit revenue growth |
| DHR, ZBH, GEHC, OTIS | Industrials/medtech stalwarts — mid-teens margins but mid-single-digit growth, below the >10% CAGR bar |
| CAT, GE, GEV | Cyclical industrials — margins and growth swing with the cycle, structurally below a steady >15% net margin |
| EL | Currently in a well-documented margin-compression/turnaround phase — fails "stable/expanding margins" right now |
| LIN | Industrial gases — ~20% margins but historically mid-single-digit revenue growth, below >10% CAGR |
| MU | Memory semiconductor — historically swings from negative to >30% margins; fails the margin-*stability* and "FCF positive 3 consecutive years" tests structurally |
| TSLA | Auto manufacturer — margins compressed to roughly mid-single-digits in recent periods; growth has decelerated sharply |

**25 names eliminated. 23 remain** for the real, sourced quantitative pull: AAPL, ABNB, AMAT, AMD, ANET, APP, AVGO, BR, BRK.B, CRWD, DDOG, FTNT, KLAC, LLY, LPLA, LRCX, MA, NXPI, ORCL, PANW, PLTR, TRU, TYL.

---

## Stage 3 — Quantitative Phase 01 gate (real, sourced data — Finviz, 2026-06-07)

Pre-screen filters per [valuation-scoring.md](../framework/valuation-scoring.md): Gross margin >40%, Net margin >12% (strategy.md uses >15%; both checked), ROIC >15%, Revenue 3yr growth >10% (Sales-5yr-CAGR shown as the closest available proxy), Net debt/EBITDA <2x, FCF positive multi-year.

| Ticker | Gross M | Net M | ROIC | Sales 5Y (proxy for 3yr CAGR) | Debt/Eq | Verdict |
|---|---|---|---|---|---|---|
| AAPL | 47.86% ✅ | 27.15% ✅ | 67.76% ✅ | 8.71% ⚠️ (<10%) | 0.80 | **Borderline — fails growth bar narrowly; services-mix/AI-cycle reacceleration is the live counter-narrative. Held back from final list pending a dedicated /new-position look.** |
| ABNB | 72.38% ✅ | 19.80% ✅ | 24.89% ✅ | 29.50% ✅ | 0.33 ✅ | **PASS** |
| AMAT | 48.96% ✅ | 29.31% ✅ | 28.49% ✅ | 10.52% ✅ | 0.30 ✅ | **PASS** |
| AMD | 47.09% ✅ | 13.37% ⚠️ | 7.43% ❌ | 28.82% ✅ | 0.06 | FAIL — ROIC well below 15% |
| ANET | 63.54% ✅ | 38.32% ✅ | 27.59% ✅ | 31.19% ✅ | 0.00 ✅ | **PASS** |
| APP | 87.47% ✅ | 62.56% ✅ | 65.61% ✅ | 30.45% ✅ | 1.49 | **PASS** (debt elevated for the sector — flagged below) |
| AVGO | 65.66% ✅ | 38.85% ✅ | 19.50% ✅ | 21.74% ✅ | 0.74 | **PASS** |
| BR | 31.31% ❌ | 15.03% | 19.35% ✅ | 8.11% ❌ | 1.21 | FAIL — gross margin and growth both below bar |
| BRK.B | 23.70% ❌ | 19.31% ✅ | 8.49% ❌ | 8.63% ❌ | 0.20 | FAIL — conglomerate; ROIC/growth fail; not a single-business quality case anyway |
| CRWD | 74.89% ✅ | -0.89% ❌ | -0.83% ❌ | n/a | 0.18 | FAIL — still GAAP-unprofitable at the net level |
| DDOG | 79.86% ✅ | 3.69% ❌ | 2.59% ❌ | n/a | 0.32 | FAIL — margins too thin to clear the bar yet |
| FTNT | 80.30% ✅ | 27.49% ✅ | 131.48% ✅ | 21.25% ✅ | 0.50 ✅ | **PASS** |
| KLAC | 59.91% ✅ | 35.68% ✅ | 39.17% ✅ | 15.93% ✅ | 1.05 | **PASS** |
| LLY | 82.83% ✅ | 34.98% ✅ | 35.82% ✅ | 21.58% ✅ | 1.39 | **PASS** (elevated debt — flagged below; well-documented capacity-buildout capex cycle) |
| LPLA | 28.81% ❌ | 4.93% ❌ | 6.82% ❌ | 23.68% ✅ | 1.39 | FAIL — thin-margin brokerage model |
| LRCX | 49.98% ✅ | 30.94% ✅ | 46.86% ✅ | 12.92% ✅ | 0.35 ✅ | **PASS** |
| MA | 96.57% ✅ | 45.78% ✅ | 65.06% ✅ | 16.50% ✅ | 2.82 | **PASS** (Upgrade 5 debt-gate context applies — asset-light payment network) |
| NXPI | 53.71% ✅ | 21.03% ✅ | 12.11% ⚠️ | 7.33% ❌ | 1.07 | FAIL — ROIC and growth both below bar |
| ORCL | 64.30% ✅ | 25.26% ✅ | 8.65% ❌ | 8.00% ❌ | 4.21 | FAIL — ROIC, growth below bar; leverage high |
| PANW | 71.94% ✅ | 7.95% ❌ | 2.85% ❌ | 22.03% ✅ | 0.07 | FAIL — net margin too thin (heavy SBC drag) |
| PLTR | 84.07% ✅ | 43.67% ✅ | 26.34% ✅ | 32.58% ✅ | 0.03 ✅ | **PASS** |
| TRU | 46.38% ✅ | 14.91% ⚠️ | 6.90% ❌ | n/a | 1.20 | FAIL — ROIC well below bar |
| TYL | 44.38% ✅ | 13.26% ⚠️ | 8.78% ❌ | n/a | 0.01 | FAIL — ROIC below bar |

Source: [Finviz screener — financial view](https://finviz.com/screener.ashx?v=171) and [valuation view](https://finviz.com/screener.ashx?v=121), pulled 2026-06-07.

### Net Debt / EBITDA check (derived from EV, EV/EBITDA, and net cash/debt — all sourced)

| Ticker | EV | EV/EBITDA | ⇒ EBITDA (derived) | Net cash(+)/debt(–) | Net Debt/EBITDA |
|---|---|---|---|---|---|
| ABNB | $69.79B | 26.65× | ≈$2.62B | +$9.47B | **≈ −3.6×** (net cash) |
| AMAT | $358.70B | 38.67× | ≈$9.27B | +$0.97B | **≈ −0.1×** |
| ANET | $181.90B | 42.93× | ≈$4.24B | +$12.35B | **≈ −2.9×** |
| APP | $188.28B | 38.64× | ≈$4.87B | +$1.09B | **≈ −0.2×** |
| AVGO | $1,869B | 44.62× | ≈$41.9B | −$45.28B | **≈ +1.1×** |
| FTNT | $103.27B | 43.73× | ≈$2.36B | +$2.73B | **≈ −1.2×** |
| KLAC | $253.19B | 43.28× | ≈$5.85B | +$1.19B | **≈ −0.2×** |
| LLY | $1,050B | 28.90× | ≈$36.3B | −$37.64B | **≈ +1.0×** |
| LRCX | $378.26B | 48.20× | ≈$7.85B | +$1.02B | **≈ −0.1×** |
| MA | $444.49B | 20.79× | ≈$21.4B | −$10.58B | **≈ +0.5×** |
| PLTR | $317.09B | 157.11× | ≈$2.02B | +$7.81B | **≈ −3.9×** |

All 11 survivors clear the <2x balance-sheet bar comfortably (most sit in **net cash**). ✅ No balance-sheet concerns anywhere on this list.

---

## ✅ Qualified Quality List — 11 names

**ABNB · AMAT · ANET · APP · AVGO · FTNT · KLAC · LLY · LRCX · MA · PLTR**

Lands inside the user's "10–30" target. AAPL and NXPI sit just outside the gate (flagged above) and were held back rather than waved through.

---

## Data gaps flagged (per CLAUDE.md Rule 0 — never invent or estimate)

1. **10-year average PE per name** — needed for the Historical PE Modifier (Upgrade 2). This requires a TIKR/Koyfin-grade data terminal pulling 10 years of trailing PE per company; not obtainable through the sources available in this session for 11 names. **Flagged, not estimated** — see the scoring section below for how this changes (or doesn't change) the conclusion per name.
2. **FCF/Net-Income conversion ratio** — not directly published per company. *Derived* (shown, not invented) as `Market Cap ÷ Trailing P/E ≈ Net Income`, then `FCF ÷ derived NI`:

   | Ticker | Derived FCF/NI | Note |
   |---|---|---|
   | ABNB | ≈189% | High — likely SBC add-back / working-capital tailwind, typical of asset-light platforms |
   | AMAT | **≈63%** | ⚠️ Below the 70% bar — worth checking against capex cycle in any /new-position follow-up |
   | ANET | ≈144% | — |
   | APP | ≈115% | — |
   | AVGO | ≈115% | — |
   | FTNT | ≈129% | — |
   | KLAC | ≈87% | — |
   | LLY | **≈45%** | ⚠️ Notably below 70% — but explainable: LLY is in a well-documented, multi-year GLP-1 manufacturing capacity buildout (a textbook Upgrade-1 "growth capex" situation; raw FCF understates quality here, the same logic that drives the MSFT Owner Earnings adjustment) |
   | LRCX | ≈91% | — |
   | MA | ≈116% | — |
   | PLTR | ≈126% | — |

   This derivation is shown so the user can judge it; it is *not* a substitute for the directly-reported figure a full /new-position evaluation would pull.
3. **Internal framework ambiguity surfaced (not a data gap, but worth a follow-up):** [valuation-scoring.md](../framework/valuation-scoring.md) lists "PEG (15% weight)" as a weighted component on the same 1–10 scale as FCF Yield and EV/EBIT, but [strategy.md](../framework/strategy.md)'s Upgrade 3 table expresses PEG as a small **additive** modifier (−1 / 0 / +0.5 / +1) — the same scale the Rate Regime Modifier uses. These can't both be true at once: a ±1 "modifier" treated as a 15%-weighted 1–10 sub-score would contribute almost nothing to the final number, while a true 1–10 PEG sub-score would dominate it. **I did not silently pick one — see how the scoring below handles it.** Worth a `decisions/` cleanup pass to make the formula and the upgrade table consistent.

---

## Rate Environment Gate (run once, applies to all 11)

**10Y Treasury = 4.55%** (close 2026-06-05). **Step 2 Rate Regime Modifier = +0.5** (10Y sits in the 3.5–5% band).

**Step 1 — Earnings Yield Spread Test** (EY = 1 ÷ Forward PE; Spread = EY − 10Y):

| Ticker | Fwd PE | EY | Spread | Result | Step-1 modifier |
|---|---|---|---|---|---|
| ABNB | 25.85 | 3.87% | −0.68% | FAIL (<+1.5%) | +0.5 |
| AMAT | 30.92 | 3.23% | −1.32% | FAIL | +0.5 |
| ANET | 40.74 | 2.45% | −2.10% | FAIL | +0.5 |
| APP | 32.03 | 3.12% | −1.43% | FAIL | +0.5 |
| AVGO | 24.55 | 4.07% | −0.48% | FAIL | +0.5 |
| FTNT | 46.35 | 2.16% | −2.39% | FAIL | +0.5 |
| KLAC | 40.91 | 2.44% | −2.11% | FAIL | +0.5 |
| LLY | 30.34 | 3.30% | −1.25% | FAIL | +0.5 |
| LRCX | 40.50 | 2.47% | −2.08% | FAIL | +0.5 |
| MA | 24.26 | 4.12% | −0.43% | FAIL | +0.5 |
| PLTR | 86.01 | 1.16% | −3.39% | FAIL | +0.5 |

**Every single name fails the spread test** — consistent with the same finding across 18 of 19 current holdings in the morning's [full-portfolio rescore](2026-06-07-rescore-full-portfolio.md). This isn't a name-specific problem; it's a market-wide statement that, at a 4.55% risk-free rate, very little in this quality-growth cohort offers an earnings yield that compensates for the rate environment. Under the now-revised Step 1 (a modifier, not a hard veto — see [investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md)), every name picks up **+0.5**.

**Combined Rate-related additive for all 11 names: +1.0** (+0.5 Step 1, +0.5 Step 2).

---

## Phase 02 — Valuation scoring (full calculation shown per name)

`Final Score = (FCF×0.40) + (EV/EBIT×0.25) + (FwdPE_adjusted×0.20) + (PEG_or_fallback×0.15) + Rate Modifier(+1.0)`

Two components carry real, fully-sourced sub-scores (FCF Yield 40% + EV/EBIT 25% = **65% of the formula**). Two components (Forward-PE-with-Historical-Modifier 20%, PEG 15%) are constrained by the data gaps and framework ambiguity flagged above — so rather than force a single number, **I show the fully-sourced 65% plus the *range* the remaining 35% could plausibly contribute** (1–10 on each, the full possible span), and call out exactly which names' *action conclusion* would change depending on where that range resolves.

| Ticker | FCF Yield → sub-score | EV/EBIT → sub-score | "Hard 65%" weighted subtotal | Min final (worst-case for the stock = best-case sub-scores of 1) | Max final (best-case for the stock = worst-case sub-scores of 10) | **Score range** | Robust conclusion? |
|---|---|---|---|---|---|---|---|
| ABNB | 5.76% → 4 | 26.92× → 7 | 3.35 | 4.7 → **5** | 7.85 → **8** | **5–8** | ❌ Genuinely depends on the missing data — see note |
| AMAT | 1.49% → 9 | 40.83× → 10 | 6.10 | 7.45 → **7** | 10.6 → **10** | **7–10** | ✅ Expensive either way |
| ANET | 2.72% → 6 | 43.78× → 10 | 4.90 | 6.25 → **6** | 9.4 → **9** | **6–9** | ✅ At minimum "Hold/no-add"; at maximum a trim-zone holding |
| APP | 2.37% → 7 | 39.66× → 10 | 5.30 | 6.65 → **7** | 9.8 → **10** | **7–10** | ✅ Expensive either way |
| AVGO | 1.79% → 9 | 56.15× → 10 | 6.10 | 7.45 → **7** | 10.6 → **10** | **7–10** | ✅ Expensive either way |
| FTNT | 2.30% → 7 | 46.83× → 10 | 5.30 | 6.65 → **7** | 9.8 → **10** | **7–10** | ✅ Expensive either way |
| KLAC | 1.59% → 9 | 46.38× → 10 | 6.10 | 7.45 → **7** | 10.6 → **10** | **7–10** | ✅ Expensive either way |
| LLY | 1.17% → 10 | 30.63× → 8 | 6.00 | 7.35 → **7** | 10.5 → **10** | **7–10** | ✅ Expensive either way |
| LRCX | 1.58% → 9 | 50.93× → 10 | 6.10 | 7.45 → **7** | 10.6 → **10** | **7–10** | ✅ Expensive either way |
| MA | 4.10% → 4 | 21.99× → 5 | 2.85 | 4.2 → **4** | 7.35 → **7** | **4–7** | ❌ Genuinely depends on the missing data — see note |
| PLTR | 0.83% → 10 | 159.19× → 10 | 6.50 | 7.85 → **8** | 10.6→10 → **10** | **8–10** | ✅ Extreme either way |

**Sub-score derivations (sourced, shown — sub-score tables from [valuation-scoring.md](../framework/valuation-scoring.md)):**
- FCF Yield: ABNB 5.76%→4–5 band (used 4) · AMAT 1.49%→<2% band (used 9) · ANET 2.72%→2-4% band (used 6) · APP 2.37%→2-4% (used 7) · AVGO 1.79%→<2% (used 9) · FTNT 2.30%→2-4% (used 7) · KLAC 1.59%→<2% (used 9) · LLY 1.17%→<2%, deep end (used 10) · LRCX 1.58%→<2% (used 9) · MA 4.10%→4-6% band (used 4) · PLTR 0.83%→<2%, extreme (used 10)
- EV/EBIT: ABNB 26.92×→22-28× band (used 7) · AMAT/ANET/APP/AVGO/FTNT/KLAC/LRCX all >35× (used 10) · LLY 30.63×→28-35× band (used 8) · MA 21.99×→18-22× band (used 5) · PLTR 159.19× — far beyond the >35× ceiling (used 10, capped)

### Reading the table — what's actually actionable today

**9 of 11 names land in the "Expensive — do not open a new position / trim if held" zone (Score ≥7) no matter how the unresolved 35% resolves**, because the FCF Yield and EV/EBIT components alone — both backed by hard, sourced numbers — already push them there: **AMAT, ANET, APP, AVGO, FTNT, KLAC, LLY, LRCX, PLTR**. PLTR in particular is not close to a borderline call — its EV/EBIT of ~159× and FCF yield of 0.83% put it at the scoring ceiling (10/10) on both fully-sourced components before any modifier is even applied.

**2 names — ABNB and MA — are genuinely undetermined** without the missing data:
- **ABNB** could land anywhere from a 5 (Cheap/Fair-value boundary, "watch") to an 8 (Expensive, trim-if-held). The swing hinges on whether its current 25.85× forward PE sits meaningfully above or below its own historical norm (a young, recently-profitable platform business — its 10yr-avg PE history is thin and would need to be pulled from a real terminal) and on how the PEG (1.28, mid-range per Upgrade 3's table) is meant to combine into the formula.
- **MA** could land anywhere from a 4 (Cheap — standard entry size) to a 7 (Fair Value/Hold). This is the more consequential of the two: MA's hard-sourced subtotal (2.85) is the *lowest* of the eleven, and its forward PE of 24.26× could plausibly sit *below* its own 10-year average (payment networks have historically traded at richer multiples than this) — which under Upgrade 2 would trigger a **−1** modifier, not a penalty. If that's the case, MA could be sitting in genuine "Cheap" territory right now. **This is the one name on this list worth a dedicated, fully-resourced /new-position pull** — it's the only one where the missing data could plausibly flip the action from "stay away" to "consider buying."

---

## Qualitative review — 5 questions (condensed; full depth reserved for any name that proceeds to /new-position)

| | Why high margins? | Moat / hard to compete with? | Capital allocation (5–10yr) | Where's growth coming from? | Best bear case | Disruption-vector check |
|---|---|---|---|---|---|---|
| **ABNB** | Asset-light two-sided marketplace, network effects on both supply and demand | Brand + host network + trust/review system; reasonably defensible but travel platforms face periodic regulatory and OTA competitive pressure | Buybacks funded from FCF; minimal debt; conservative | International expansion, experiences vertical, loyalty | Regulatory crackdowns (short-term-rental bans) in key cities; growth deceleration as core markets mature | Could a future AI travel-agent layer disintermediate the marketplace itself? Worth tracking |
| **AMAT / LRCX / KLAC** | Oligopoly in semiconductor capital equipment — three of a handful of companies that can build EUV/etch/deposition tools at the leading edge | Extremely high — multi-billion-dollar R&D and decades of process IP create one of the hardest moats in tech | Heavy R&D reinvestment, steady buybacks/dividends | AI-driven fab capex supercycle; leading-edge node transitions | Cyclicality — semicap is famously boom/bust; a capex air-pocket would hit all three simultaneously (correlated risk if holding more than one) | Would a shift to fundamentally different compute architectures (photonic, quantum) bypass current tool requirements within a decade? Low-probability, high-impact |
| **ANET** | High-end networking for AI/cloud data centers; software-defined differentiation | Switching costs once a data-center fabric is built on Arista's EOS; strong hyperscaler relationships | Reinvestment into R&D, minimal debt, opportunistic buybacks | AI data-center buildout cycle | Customer concentration (a handful of hyperscalers); a pause in AI capex would hit hard | Could white-box/open networking (disaggregated hardware+software) erode the premium model? An active industry debate |
| **APP** | AppLovin's ad-tech AI engine (AXON) — high incremental margins on a mature platform | Proprietary ad-targeting/optimization data loop; genuine technical edge but also genuinely controversial (active short-seller scrutiny of its measurement claims) | Aggressive buybacks; recently divested its gaming-studio business to focus on ad-tech — a real strategic pivot worth understanding fully before sizing | Expansion beyond gaming into e-commerce/connected-TV ad inventory | This is the **highest-controversy name on the list** — multiple published short reports challenge its attribution/measurement methodology. [Phase 04's "short thesis engagement" rule applies directly](../framework/strategy.md) — any serious look at APP requires engaging with those arguments specifically, not waving them off | A platform-level policy change (App Store / Google Play attribution rules) could materially impair the core product |
| **AVGO** | Diversified semiconductor + enterprise software (post-VMware) franchise with very high pricing power in custom silicon (AI ASICs) and networking | Extremely strong — entrenched in hyperscaler AI roadmaps as a custom-silicon partner, plus sticky enterprise software (VMware) | Large, debt-funded M&A (VMware) — a different capital-allocation pattern than the others on this list; worth understanding the leverage trajectory | AI custom-silicon (XPU) demand, software cross-sell | A slowdown in hyperscaler capex, or a customer (e.g., Google) bringing more silicon design in-house | Could merchant GPU vendors or in-house silicon teams erode AVGO's custom-ASIC position? |
| **FTNT** | Integrated security-platform model (hardware + subscriptions) with high switching costs once embedded | Strong — broad product portfolio, large installed base, high net-cash balance sheet | Conservative — net cash, opportunistic buybacks | Platform consolidation (customers buying more from fewer vendors), SASE/cloud security | Intensifying competition from Palo Alto, CrowdStrike, cloud-native entrants | Could cloud-native, API-first security architectures bypass FTNT's hardware-centric model over time? |
| **LLY** | GLP-1 (Mounjaro/Zepbound) franchise — genuine first-mover scale advantage in obesity/diabetes drugs, very high gross margins | Patent-protected blockbuster portfolio + massive ongoing capacity investment most competitors can't match | Heavy, well-publicized capex buildout for GLP-1 manufacturing capacity (this is *why* its FCF/NI conversion looks low right now — see the data-gap note above; arguably an Owner-Earnings-style situation) | Continued GLP-1 volume ramp, pipeline expansion (oral GLP-1, other indications) | Patent cliffs further out; pricing-policy/political risk around GLP-1 drug costs (a live US policy debate); competitive entry from Novo Nordisk and orals from multiple players | Could oral GLP-1 alternatives (from LLY itself or competitors) cannibalize the high-margin injectable franchise? |
| **MA** | Two-sided payment network — each transaction essentially costless to process at scale | One of the strongest moats in finance — global rails, regulatory licensing, network effects | Consistent buybacks + modest dividend; very disciplined | Cross-border volume, value-added services (cybersecurity/data analytics), continued cash-to-card conversion in emerging markets | Regulatory/interchange-fee pressure (an ongoing, well-documented multi-jurisdiction risk); real-time payment rails (e.g., FedNow, Pix) bypassing card networks | This is the live disruption question for the entire payments-network category — government-backed instant-payment rails are growing share in several large markets |
| **PLTR** | AI/data-platform business with very high incremental margins on government and enterprise contracts | Genuine — deep government relationships and a differentiated ontology-based data platform; but the **valuation has run dramatically ahead of the moat's economics** (EV/EBIT ~159×) | Strong net-cash position; minimal debt; recent insider-selling activity has drawn attention (worth checking Form 4 filings before any serious look, per Upgrade 4's insider-signal logic, even though PLTR isn't a turnaround case) | Commercial AI platform expansion beyond its government roots | **By a wide margin, the most extreme valuation on this entire list** — any disappointment in growth durability would compress the multiple severely | Government-contract concentration and competitive entry from hyperscaler AI platforms are the two biggest structural watch-items |

---

## Final verdict — action table

| Ticker | Phase 01 | Score (range) | Action under Phase 03 |
|---|---|---|---|
| AMAT | PASS | 7–10 | **Do not open — Expensive.** Add to watchlist; revisit if it falls into the 4–5 (Cheap) band on a real pullback or rate-cut cycle |
| ANET | PASS | 6–9 | **Do not open — Fair-Value-to-Expensive.** Watchlist |
| APP | PASS | 7–10 | **Do not open — Expensive**, *and* flagged for active short-thesis controversy — would need that engagement before any further look regardless of price |
| AVGO | PASS | 7–10 | **Do not open — Expensive.** Watchlist |
| FTNT | PASS | 7–10 | **Do not open — Expensive.** Watchlist |
| KLAC | PASS | 7–10 | **Do not open — Expensive.** Watchlist |
| LLY | PASS | 7–10 | **Do not open — Expensive.** Watchlist (GLP-1 franchise genuinely exceptional — the kind of business worth waiting patiently for a better entry on) |
| LRCX | PASS | 7–10 | **Do not open — Expensive.** Watchlist |
| PLTR | PASS | 8–10 | **Do not open — Extreme.** Not a "wait for a dip" name at this multiple; would need a structural re-rating, not just a pullback |
| **ABNB** | PASS | **5–8 (undetermined)** | **Hold for more data.** Plausible Watchlist (Fair Value) to Do-not-open (Expensive) — would need a 10yr-avg-PE pull to resolve |
| **MA** | PASS | **4–7 (undetermined)** | **The one name worth a dedicated /new-position pull.** Could plausibly be in the "Cheap — standard entry 3–5%" zone right now if its forward PE sits meaningfully below its historical average (a real possibility for a payment-network stalwart at 24× forward earnings) |

**Bottom line:** this screen surfaced a textbook "wonderful businesses, terrible prices" cohort — every single survivor cleared the Phase 01 quality bar comfortably (several spectacularly: APP, FTNT, MA, PLTR all post >40% net margins; FTNT's ROIC is 131%), and every single one fails the Rate Environment Gate's earnings-yield spread test. Nine of eleven are unambiguously too expensive to act on today regardless of any data gap. **MA is the one name worth following up properly** — it's the only survivor where the hard numbers leave the door open to a "Cheap" verdict, and closing that gap just requires one targeted data pull.

---

## Next review trigger

- **MA** — recommend running a full `/new-position MA` evaluation (which will independently pull the 10yr-avg-PE and live price data this screen couldn't access) to resolve whether it currently sits in "Cheap — standard entry" territory.
- **ABNB** — same data gap, lower urgency (its score range sits one notch higher and its qualitative profile — younger company, thinner moat than MA's — makes "Cheap" the less likely resolution of the two).
- **The other 9 names** — add to a standing watchlist; re-screen on (a) a meaningful (~20%+) pullback, or (b) a shift in the Rate Regime Modifier (10Y dropping below 3.5% would remove the +0.5 headwind currently pinning every name in this cohort to the expensive side).
- **Framework note for a future cleanup pass:** the PEG-weighting inconsistency between [valuation-scoring.md](../framework/valuation-scoring.md) (PEG as a 15%-weighted 1–10 sub-score) and [strategy.md](../framework/strategy.md) Upgrade 3 (PEG as a small additive modifier) should be resolved — see the "Data gaps" section above for why it matters.

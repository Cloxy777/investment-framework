# NEW POSITION — HIMS (Hims & Hers Health, Inc.) — 2026-06-12

**Task type:** NEW POSITION
**Date:** 12 Jun 2026
**10Y US Treasury Yield:** 4.46% (FRED DGS10, 11 Jun 2026 close — most recent available)
**Rate Regime Modifier (would apply if scored):** +5 (10Y in the 3.5–5% bracket) — **not applied; Phase 01 gate fails before Phase 02 is reached**
**Current HIMS portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Healthcare — Direct-to-Consumer Telehealth & Wellness (personalized subscription health platform: weight loss/GLP-1, sexual health, dermatology, mental health)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$28.87** | WebSearch, explicitly dated "as of June 12, 2026" — IBKR `search_contracts`/`get_price_snapshot` access was denied for this session, so the WebSearch fallback per Rule 0 Step 1 was used |
| Prior close (per same source) | $27.78 (+3.9% implied) | WebSearch |
| Cross-check: 11 Jun 2026 close (separate source) | $28.98 (reported "+6.66% Tuesday") | WebSearch — minor ~0.4% discrepancy vs. $28.87, flagged but immaterial to the gate outcome below |
| 52-week range | $13.74 – $70.43 (high set 31 Jul 2025, low set 24 Feb 2026) | WebSearch |
| Analyst consensus PT | $26.61 (S&P Global, 16 analysts, "Hold") to ~$27.41 avg (13 analysts, range $21–$35); separate aggregator shows "Moderate Buy" (4 buy / 9 hold / 0 sell) | WebSearch |

**Context:** $28.87 sits **~59% below** the 52-week high ($70.43, set Jul 2025 near the peak of the GLP-1/weight-loss telehealth re-rating) and is up sharply (+~109%) from the 52-week low ($13.74, set 24 Feb 2026 in the aftermath of the Novo Nordisk partnership dissolution and an FTC warning-letter episode). The stock has been extremely volatile over the trailing year. Most recently, HIMS plunged ~13–16% on 12 May 2026 after a Q1 2026 earnings miss (swing to a net loss, weak guidance) and has since partially recovered on news of a renewed Novo Nordisk GLP-1 distribution partnership and a raised FY2026 revenue outlook. Analyst consensus (~$26.61–$27.41, "Hold") sits *below* today's live price — a first signal, independent of the Phase 01 gate below, that the bottom-up case here is not straightforward.

---

## 2. Data Gathered (Phase 01 + Phase 02 Inputs) & Gaps Flagged

| Metric | Value | Source / Derivation |
|---|---|---|
| FY2022 Revenue | $526.9M (+94% YoY) | WebSearch aggregation (WallStreetZen/stockanalysis-style) |
| FY2023 Revenue | $872.0M (+65.5% YoY) | Same |
| FY2024 Revenue | ~$1,484.6M (+69.3% YoY, "$1.5B") | Same |
| FY2025 Revenue | $2,350.0M (+59% YoY) | Hims & Hers Q4/FY2025 earnings release (8-K) |
| **Revenue CAGR 3yr** (FY2022→FY2025) | **64.6%** = (2350.0/526.9)^(1/3) − 1 | Computed |
| Q1 2025 Revenue | $586.0M | Hims & Hers Q1 2025 8-K |
| Q1 2026 Revenue | $608.1M (+4% YoY) | Hims & Hers Q1 2026 10-Q/8-K |
| **TTM Revenue** (FY2025 − Q1'25 + Q1'26) | **$2,372.1M** = $2,350.0M − $586.0M + $608.1M | Computed |
| Gross margin FY2023 | 82% | WebSearch aggregation |
| Gross margin FY2024 | 79% | Hims & Hers FY2024 8-K |
| Gross margin FY2025 | 74% | Hims & Hers Q4/FY2025 8-K |
| Gross margin Q1 2026 | 65% (70% adjusted for restructuring) | Hims & Hers Q1 2026 10-Q/8-K |
| FY2025 Net income | $128.4M (margin 5.5%) | Hims & Hers Q4/FY2025 8-K |
| FY2024 Net income | $126M (diluted EPS $0.58) | Hims & Hers FY2024 earnings coverage |
| Q1 2025 Net income | $49.5M (margin ~8.4%) | Hims & Hers Q1 2025 8-K |
| Q1 2026 Net income | **−$92.1M** (margin ≈ −15%, EPS −$0.40) — includes $33.5M restructuring/inventory write-down tied to the U.S. weight-loss strategic shift | Hims & Hers Q1 2026 10-Q/8-K |
| **TTM Net Income** (FY2025 − Q1'25 + Q1'26) | **−$13.2M** = $128.4M − $49.5M − $92.1M | Computed |
| **TTM Net Margin** | **−0.56%** = −$13.2M / $2,372.1M | Computed |
| ROIC (TTM, GuruFocus) | **−19.43%** | GuruFocus (reflects TTM net loss) — other sources show wildly divergent figures (88.9% "as of Apr 2025," 16.96% on stale TTM, 6.38%/7.33% on other TTM windows) — see Gap #2 |
| FY2023 FCF | $47.0M | MacroTrends (OCF − CapEx) |
| FY2024 FCF | $198.3M | MacroTrends / earnings coverage |
| FY2025 FCF | $57.4M (OCF $300.0M − CapEx >$240M, Ohio pharmacy-automation buildout) | Hims & Hers Q4/FY2025 8-K |
| Q1 2025 FCF | $50.1M | Hims & Hers Q1 2025 8-K |
| Q1 2026 FCF | $53.0M (OCF $89.4M − CapEx ~$36.4M) | Hims & Hers Q1 2026 10-Q/8-K |
| FCF positive 3 consecutive years (FY2023–25) | $47.0M / $198.3M / $57.4M — **all positive** | ✅ |
| FCF/NI conversion FY2024 | 157.4% = $198.3M / $126M | Computed |
| FCF/NI conversion FY2025 | 44.7% = $57.4M / $128.4M | Computed — **below 70%** |
| FCF/NI conversion TTM | **Not meaningful** — TTM NI is negative (−$13.2M) while TTM FCF is positive; a ratio would be negative/uninterpretable | Computed |
| Cash + ST investments (Q1 2026) | $629.7M ($222.3M cash + $528.6M... reconciliation note below) | Hims & Hers Q1 2026 10-Q |
| Total debt (incl. convertible notes) | $971.0M (incl. $974.1M convertible senior notes, net, on balance sheet) | Hims & Hers Q1 2026 10-Q |
| **Net debt** | **+$341.3M** (net debt position — debt exceeds cash+ST investments) | Computed = $971.0M − $629.7M |
| Net debt / FY2025 Adj. EBITDA | 1.07× = $341.3M / $318.0M | Computed — would pass <2x in isolation, but see Gap #4 on EBITDA quality |
| Shares outstanding (Q1 2026, 10-Q) | 222,326,117 Class A + 8,377,623 Class V = **230,703,740** | Hims & Hers Q1 2026 10-Q |
| **Market Cap** | 230.70M × $28.87 = **$6,660.4M** | Computed |
| **Enterprise Value** | $6,660.4M + $341.3M = **$7,001.7M** | Computed |
| Trailing PE (per aggregator) | 53.82× | WebSearch (stockanalysis.com-style aggregator) — based on a positive trailing EPS figure that predates the Q1 2026 swing to a TTM net loss; internally inconsistent with the TTM net-loss figure computed above — see Gap #5 |
| Forward PE (per aggregator) | 51.92× | Same source |
| EV/EBIT (per aggregator) | 74.66× (vs. industry median 17.56×, ranked worse than 89% of peers) | GuruFocus |
| EV/EBITDA (per aggregator) | 38.66× (one source) / 50.32× (another) | WebSearch — wide spread, flagged |
| PEG (per aggregator) | 9.12 | WebSearch aggregator |
| FY2026 guidance (raised, post Novo Nordisk renewal) | Revenue $2.8B–$3.0B; Adj. EBITDA $275M–$350M | Hims & Hers Q1 2026 8-K |

### Data Gaps / Flags

1. **Live price source variance ($28.87 vs $28.98).** IBKR contract search/price snapshot tools were denied for this session (permission error), so Rule 0's WebSearch fallback was used. Two WebSearch results gave $28.87 ("as of June 12, 2026," prior close $27.78) and $28.98 ("Tuesday June 11, 2026 close, +6.66%"). The two are ~0.4% apart and don't change the Phase 01 outcome below — used $28.87 as the more explicitly "today"-dated figure.

2. **ROIC has an extremely wide spread across sources (−19.43% to +88.9%).** This is a real methodology problem, not a research gap: HIMS's TTM net income just went negative (Q1 2026 swing to a $92.1M loss), so any ROIC built on a TTM-income numerator will read negative or near-zero, while sources built on FY2025's still-positive $128.4M full-year net income (or on a stale earlier-2025 TTM window) read positive. GuruFocus's explicitly-TTM figure (−19.43%) is used as primary because it's the most current and methodologically consistent with the TTM net-margin calculation above (both reflect the post-Q1-2026 trailing window). **This does not change the gate outcome** — even the most favorable historical reading (88.9% "as of Apr 2025," which predates the Q1 2026 loss entirely) cannot be treated as the current trailing figure without inventing a recovery that hasn't been reported.

3. **Cash + ST investments reconciliation ($222.3M + $528.6M = $750.9M vs. the $629.7M figure used for net debt).** Two different aggregations of HIMS's Q1 2026 balance sheet were found: one (10-Q line items) shows cash $222.3M + short-term AFS investments $528.6M = $750.9M; another (finbox-style aggregator) shows "cash and short-term investments" of $629.7M against $971.0M total debt. The $629.7M figure was used for the net-debt calculation as the more conservative (higher net debt) of the two; using $750.9M instead would give net debt = $971.0M − $750.9M = $220.1M, net debt/EBITDA = 0.69× — **still would not change the gate outcome**, since the gate fails decisively on net margin and ROIC regardless of the debt figure.

4. **FY2025 Adjusted EBITDA ($318.0M) is a non-GAAP, company-defined figure** that adds back the $33.5M Q1 2026 restructuring charge (and similar prior add-backs) — i.e., it does not fully reflect the deteriorating GAAP profitability shown in the TTM net-income figure. Net debt/EBITDA of ~1.07× (or 0.69× per Gap #3) should be read with that caveat. **Does not change the gate outcome** — net margin and ROIC are the binding failures, not the debt ratio.

5. **Trailing/Forward PE (53.82×/51.92×) and EV/EBIT (74.66×) figures appear to predate or not fully reflect the Q1 2026 net loss** — a positive PE ratio is mathematically incompatible with a negative TTM EPS. These figures were not used in any calculation below (the gate fails before Phase 02 valuation inputs are needed) but are recorded for context/the watchlist entry, with this inconsistency flagged.

6. **No metric in this session was invented or estimated** — every figure above traces to a specific earnings release, 10-Q/10-K, or named aggregator, with derivations (CAGR, TTM roll-forwards, net debt, market cap, EV) shown explicitly.

---

## 3. Phase 01 — Quality Gate

| Check | HIMS Value | Threshold | Result |
|---|---|---|---|
| **Net margin (TTM)** | **−0.56%** (TTM NI −$13.2M / TTM Rev $2,372.1M) | >15% (strategy.md) / >12% (valuation-scoring.md pre-screen) | ❌ **FAIL** |
| **ROIC (TTM)** | **−19.43%** | >15% | ❌ **FAIL** |
| Revenue CAGR 3yr (FY2022→FY2025) | **64.6%** | >10% | ✅ PASS (by a wide margin) |
| Gross margin | 74% (FY2025), but **declining trend**: 82% → 79% → 74% → 65% (Q1 2026) | >40% **or** structurally expanding (3yr trend) | ⚠️ **PASS on level, FAIL on trend** — gross margin has *compressed* ~17pp over 5 quarters, the opposite of "structurally expanding" |
| FCF positive 3 consecutive years | FY2023 $47.0M / FY2024 $198.3M / FY2025 $57.4M — all positive | required | ✅ PASS |
| Net debt/EBITDA | ~1.07× (or 0.69×, see Gap #3) | <2x | ✅ PASS (on Adj. EBITDA basis — see Gap #4 caveat) |
| **FCF/NI conversion ratio (2yr)** | FY2024 157.4% / FY2025 44.7% — only **one** of the last two years clears 70%; TTM ratio not meaningful given negative TTM NI | >70% for 2+ consecutive years | ❌ **FAIL** |
| Share issuance pattern | $402.5M convertible senior notes due 2032 issued (with capped calls) — not direct equity dilution, but a material capital-structure event | not dilutive | ⚠️ Convertible debt, not common-share dilution — neutral-to-mixed |
| Moat signal | Strong consumer brand in DTC telehealth, vertically-integrated pharmacy/compounding infrastructure (Ohio buildout), renewed Novo Nordisk GLP-1 distribution partnership | required | ⚠️ Real but actively being re-shaped — see §5 |

**Gate result: FAIL** — on **three** independent criteria (Net Margin, ROIC, FCF/NI conversion), plus a trend-based concern on Gross Margin. Per the operating brief, this session **stops here**.

---

## 4. Gate Result: **FAIL** — Stopping Per Operating Brief

> "Walk the Phase 01 quality gate — if it fails, stop and report why rather than proceeding to scoring."

HIMS fails Phase 01 decisively:

- **TTM Net Margin is −0.56%**, vs. the >15% threshold — not a "modest miss," but a sign-flip from FY2025's already-marginal 5.5% to an outright TTM loss, driven by Q1 2026's $92.1M net loss (which itself includes $33.5M of restructuring/inventory write-downs tied to a **strategic reversal** in the U.S. weight-loss offering).
- **TTM ROIC is −19.43%** — capital is currently being destroyed on a trailing basis, not compounded.
- **FCF/NI conversion** fails the "2 consecutive years >70%" test (FY2025 was 44.7%, and TTM NI is negative so the ratio is not even computable in the conventional sense) — though note FCF itself has stayed positive throughout (this is the one genuinely reassuring data point).
- **Gross margin**, while still comfortably >40% in isolation (74% FY2025), has **compressed ~17 percentage points** over five quarters (82% → 79% → 74% → 65% Q1 2026) — the opposite of the "structurally expanding margins" the framework looks for, and the proximate driver of the net-margin and ROIC failures above.

This is not a borderline case (cf. CIEN's 11 Jun 2026 session, which failed by a few points on two metrics with a strong single-quarter inflection in the other direction). HIMS's TTM profitability **moved in the wrong direction** relative to FY2025, in the same quarter management announced a **strategic retreat** from part of its highest-margin growth driver (the U.S. weight-loss/GLP-1 business).

### Did the Turnaround Sub-Gate (Upgrade 4) open an alternate path?

No — it requires **all five** of:

1. **Historical ROIC >15% for ≥5 of the past 10 years** — HIMS has been a public company only since 2021 (SPAC merger), so a 10-year ROIC history doesn't exist. Even within its short public history, ROIC appears to have been volatile/marginal rather than a sustained >15% track record (the 88.9% "Apr 2025" figure looks like an outlier relative to the TTM −19.43% just five quarters later). **Cannot be confirmed as met.**
2. **CEO/CFO insider buying >$500K in the past 6 months (Form 4-verified)** — **not checked / no evidence found this session.**
3. **Independent FV showing ≥40% MOS** — not built (gate fails before this step, and building a DCF for a company with a negative TTM net income and a structurally-shifting business mix would itself require assumptions the framework's "never invent or estimate" rule warns against).
4. **Net Debt/EBITDA <3×** — ✅ would likely pass (~1.07× or 0.69×, see Gap #3/#4).
5. **Core moat still identifiable** — ⚠️ partially — the DTC brand and pharmacy infrastructure are real, but the company itself just announced a strategic reversal in a segment (U.S. weight loss) that was a primary driver of the 2024–25 re-rating, which muddies "moat" into "moat-in-transition."

Since conditions 1, 2, and 3 can't be confirmed as met (and condition 5 is ambiguous), "all five" cannot be satisfied — the Turnaround Sub-Gate path does **not** open.

---

## 5. Why This Is Close — and What Would Flip the Verdict

The bull case for HIMS is real and shouldn't be dismissed out of hand: **revenue CAGR of 64.6%** over three years is exceptional, FCF has stayed positive in every one of the last three full years (including $57.4M in FY2025, a year with heavy infrastructure capex), and the company just **raised** FY2026 guidance ($2.8–3.0B revenue) on the back of a **renewed Novo Nordisk GLP-1 distribution partnership** — a potentially significant de-risking of the personalized weight-loss franchise after a turbulent stretch (patent lawsuit, its dissolution, an FTC warning letter, and now a strategic reset of the *compounded* weight-loss offering).

But the framework's Phase 01 gate is built on **trailing financial proof**, not on "the next chapter looks better" — and on a trailing basis, HIMS just had its **worst quarter of profitability as a public company** (a $92.1M net loss, more than double any prior quarterly profit), driven in part by management's own decision to unwind part of the business that had been driving the growth/margin story. That is about as close to "Phase 01 is working exactly as designed" as a case gets: a richly-valued, high-growth story whose trailing fundamentals just deteriorated sharply in the same quarter as a strategic reversal — exactly the combination the quality gate exists to catch *before* a valuation score gets computed on it.

**What would change this:**

- **Q2 2026 earnings** (expected ~August 2026) is the critical re-check. If TTM net income returns to positive territory (i.e., Q2 2026 net income > $92.1M, reversing the Q1 2026 loss on a trailing basis) **and** TTM ROIC clears 15% **and** gross margin stabilizes (rather than continuing its 82%→65% slide), the gate would be worth re-running from scratch.
- The **Novo Nordisk partnership's actual revenue/margin contribution** in Q2–Q3 2026 will be the key signal on whether the "moat-in-transition" (§3, last row) resolves toward a stronger or weaker moat.
- The **$33.5M restructuring charge** was characterized as a one-time item tied to the U.S. weight-loss strategic shift — if Q2 2026 net income, *excluding* any further one-time charges, is meaningfully positive, that would be worth noting (though the framework's Rule 6 "normalize before you value" caveat would apply — one-time-item add-backs need scrutiny, not automatic exclusion).
- A **>15% unexplained move** from $28.87 in either direction (Rule 9) would itself trigger a re-check regardless of the calendar.

---

## 6. Recommendation

# **WATCHLIST WITH CONDITIONS — do not open a position now.**

HIMS fails the Phase 01 quality gate on **TTM Net Margin (−0.56% vs. >15% required)**, **TTM ROIC (−19.43% vs. >15% required)**, and **FCF/NI conversion** (FY2025 44.7%, TTM not meaningful given the net loss) — with **gross margin compression** (82%→65% over five quarters) as a fourth flag. Per this framework's rules, exceptional revenue growth and a constructive forward narrative (raised guidance, renewed Novo Nordisk partnership) are not sufficient to override a trailing-financials gate failure — that would be acting on a narrative basis, which Rule 0 and the (retired) Upgrade 6 momentum-gate discussion both warn against in either direction. The 5.5%→−15% net-margin swing happened in the *same quarter* as a strategic reversal in a core growth segment — this is a live "is the moat intact" question, not a settled one, and the framework is explicitly designed to wait for trailing proof rather than get ahead of it.

**Add HIMS to the watchlist** (`not-in-portfolio/HIMS/`) with a re-evaluation trigger at:

- **Q2 2026 earnings** (expected ~August 2026) — re-run the full Phase 01 gate with refreshed TTM net margin, ROIC, gross margin trend, and FCF/NI conversion. If TTM net income returns positive and ROIC clears 15%, proceed to the Rate Environment Gate and Phase 02.
- Any further **guidance revision** (up or down) tied to the Novo Nordisk partnership ramp, or commentary materially changing the gross-margin trajectory (Rule 9 trigger).
- **>15% unexplained price move** from $28.87 (Rule 9).

---

## 7. Next Review Trigger

**Date/event:** HIMS's Q2 2026 earnings release (expected ~August 2026) — re-run Phase 01 with refreshed TTM Net Margin, ROIC, gross margin trend (watch for stabilization vs. continued compression), and FCF/NI conversion. Earlier trigger if a guidance revision, the Novo Nordisk partnership ramp, or a >15% unexplained price move constitutes a material fundamental event (Rule 9).

**No position opened — nothing to log in `decisions/`.**

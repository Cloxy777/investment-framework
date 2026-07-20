# NEW POSITION — VRSN (VeriSign, Inc., NASDAQ) — 2026-07-19

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 19 Jul 2026 (Sunday)
**10Y US Treasury Yield:** 4.56% (FRED `DGS10`, most recent posted observation as of Friday 2026-07-18 — no weekend data; recorded for completeness only, since this session stops before the Rate Environment Gate would apply — see §4)
**Current VRSN portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); grep for "VRSN" returns no match)
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/VRSN/` or `watchlist/not-in-portfolio/VRSN/`, confirmed via `find` before this session started)
**Sector:** Internet infrastructure / domain registry services — sole ICANN-designated registry operator for the .com and .net top-level domains
**First-use jargon decode:** see closing Glossary (§9)

---

## 0. Why this session exists — trigger source

A post on **bolshegold** (Telegram, post bolshegold/9795, ~09:46 UTC 2026-07-19), previewing the upcoming earnings-reporting week, named VRSN alongside a comparison to DOCU: *"$VRSN — можно посмотреть на плюс минус итоги $DOCU. Рынок и рост должен быть один и тот же"* ("VRSN — you can look at roughly the same results as DOCU; the market and growth should be similar"). Per the operating brief and this repo's standing convention (see the 2026-07-19 AXP precedent session), **a first-ever mention of a name with no watchlist entry triggers a full `/new-position` evaluation regardless of the mention's substance.** VRSN has no existing watchlist entry and is not a current holding (confirmed above), so this session is that evaluation, built entirely from independently, primary-sourced data. **The Telegram post's text (including its DOCU comparison) is not used as a financial input anywhere below** — DOCU is being evaluated separately, by a different session, and is not referenced again in this document.

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("VRSN")`: contract_id **4173050**, exchange **NASDAQ**, description "VERISIGN INC" — the correct primary US listing (other results returned were a MEXI cross-listing and an unrelated bond issuer entry; neither used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$277.66** | IBKR `get_price_snapshot`, `last` field, contract_id **4173050** (NASDAQ). `is_close: true` — this is the last completed-session close, not a live intraday trade, because today (Sunday 2026-07-19) markets are closed; per Rule 0 this is still the most recent price obtainable via a live fetch attempt, flagged here as a close rather than an intraday quote (same treatment as the 2026-07-19 AXP session). |
| 52-week high | $312.48 | IBKR `misc_statistics` `high_52w` |
| 52-week low | $208.07 | IBKR `misc_statistics` `low_52w` |
| 13-week / 26-week high | $312.48 | IBKR `misc_statistics` (identical to 52w high — the high was set within the last 13 weeks) |
| Open 52 weeks ago | $278.15 | IBKR `misc_statistics` `open_52w` |
| Dividend yield | 1.14% | IBKR `get_price_snapshot` `dividend_yield` field |
| Bid / Ask (context only, not used) | $224.00 / $304.19 | IBKR `get_price_snapshot` — an unusually wide spread reflecting no active weekend quoting, not a tradeable market; not used for any calculation |
| US 10Y Treasury yield | 4.56% | FRED `DGS10`, as-of 2026-07-18 |

$277.66 is essentially flat versus its level 52 weeks ago ($278.15, **-0.2%**) despite trading as high as $312.48 in the past 13 weeks — context only, not scored. Cross-check: independent data provider stockanalysis.com's market cap ($25.30B) computed against its own live price and IBKR's 91.1M Q1 2026 shares-outstanding figure implies a near-identical per-share price to the IBKR quote, corroborating $277.66 as current and not stale.

**Company background note (not scored, context only):** VeriSign began paying a quarterly cash dividend in 2025 ($0.81/share as of Q1 2026) — a change from its historical no-dividend policy — funded from the large free cash flow the buyback program doesn't fully absorb. This is a live, IBKR-reported fact, not an assumption.

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

Financial figures below are sourced primarily from VeriSign's own SEC Form 8-K quarterly/annual earnings-release exhibits (SEC EDGAR, CIK **1014473**) — the Q1 2026, Q4/FY2025, Q2 2025, Q1 2025, Q4/FY2022 releases were fetched directly. Valuation multiples and the ROIC figure (§3.2) are cross-checked against stockanalysis.com and GuruFocus, both third-party vendors, with the exact cross-check shown at each point of use.

### 2.2 Income statement — primary-sourced (VeriSign's own 8-K earnings releases)

| Period | Total Revenue | Operating Income | Net Income | Diluted EPS |
|---|---|---|---|---|
| FY2021 | $1,327.6M | $866.8M | $784.8M | $7.00 |
| FY2022 | $1,424.9M | $943.1M | $673.8M | $6.24 |
| FY2023 | ~$1.49B (+4.8% YoY, company-reported) | ~$1.00B (company-reported) | $818.0M | $7.90 |
| FY2024 | $1,557.4M | $1,058.2M | $785.7M | $8.00 |
| FY2025 | $1,656.6M | $1,121.0M | $825.7M | $8.81 |
| Q1 2025 | $402.3M | $271.2M | $199.3M | $2.10 |
| Q1 2026 | $428.9M | $293.6M | $214.5M | $2.34 |

FY2023 revenue/operating income are the company's own rounded press-release figures ($1.49B / ~$1.00B) — the precise-to-the-hundred-thousand figures weren't independently re-pulled this session since FY2023 isn't a scored input (only used qualitatively for the YoY-deceleration check in §3.4); flagged in §8.

**Year-over-year revenue growth: +7.3% (FY21→22) → +4.8% (FY22→23) → +4.3% (FY23→24) → +6.4% (FY24→25) → +6.6% (Q1 2026 vs Q1 2025)** — all company-reported percentages, decelerating through FY2024 then **re-accelerating**, not structurally decelerating (relevant to the Growth sub-score modifier, §3.4).

**TTM (Apr 2025–Mar 2026), the most recent complete-quarter window available:**
```
TTM Revenue         = FY2025 ($1,656.6M) − Q1 2025 ($402.3M) + Q1 2026 ($428.9M) = $1,683.2M
TTM Operating Income = FY2025 ($1,121.0M) − Q1 2025 ($271.2M) + Q1 2026 ($293.6M) = $1,143.4M
TTM Net Income      = FY2025 ($825.7M) − Q1 2025 ($199.3M) + Q1 2026 ($214.5M) = $840.9M
```

### 2.3 Cash flow — primary-sourced

| Fiscal Year | Cash from Operations | CapEx | FCF (OCF−CapEx) | Net Income | FCF/NI |
|---|---|---|---|---|---|
| FY2023 | — | — | $808M (company-reported) | $818.0M | 98.8% |
| FY2024 | $902.6M | $28.1M | $874.5M | $785.7M | 111.3% |
| FY2025 | $1,091.1M | $22.8M | $1,068.3M | $825.7M | 129.4% |

Company (and Macrotrends, a third-party aggregator) confirm FCF has been positive every year across an extended multi-year history (a 14-year FCF chart with no negative year) — comfortably clears the "FCF-positive 3+ consecutive years" hard disqualifier check with a long track record, not just the three years fully re-derived here.

**Depreciation & Amortization (for TTM EBITDA):**
```
FY2025 D&A = $31.2M | Q1 2025 D&A = $8.9M | Q1 2026 D&A = $6.4M
TTM D&A = FY2025 D&A − Q1 2025 D&A + Q1 2026 D&A = 31.2 − 8.9 + 6.4 = $28.7M
TTM EBITDA = TTM Operating Income + TTM D&A = 1,143.4 + 28.7 = $1,172.1M
```

### 2.4 Balance sheet — primary-sourced (Q1 2026 10-Q-equivalent figures from the Q1 2026 8-K exhibit)

| Item | Dec 31, 2025 | Mar 31, 2026 |
|---|---|---|
| Cash and cash equivalents | $307.9M | $476.7M |
| Long-term Senior Notes (total debt; no current portion either date) | $1,788.2M | $1,788.8M |
| Total stockholders' equity (deficit) | $(2,154.2)M | $(2,213.4)M |
| Total assets | $1,325.9M | $1,297.2M |
| Total liabilities | $3,480.1M | $3,510.6M |
| Shares outstanding | 91.9M | 91.1M |

**Net Debt/EBITDA (most recent quarter-end, Mar 31 2026):**
```
Net Debt = Total Debt ($1,788.8M) − Cash ($476.7M) = $1,312.1M
Net Debt/EBITDA = $1,312.1M / $1,172.1M (TTM EBITDA, §2.3) = 1.12×
```

**Important structural note — VeriSign's stockholders' equity is deeply negative** (−$2,213.4M at Q1 2026), the result of cumulative share buybacks ($859M / 3.4M shares in FY2025 alone) exceeding cumulative contributed capital plus retained earnings over many years — not distress. This is the exact phenomenon this framework's own glossary already documents (see "Negative stockholders' equity" entry, first flagged for Match Group/MTCH in the 2026-07-16 session): it mechanically breaks the standard book-value ROIC formula. See §3.2 for how this session handles it.

### 2.5 Growth / moat evidence — primary and third-party sourced

- **Domain base at record high:** 176.1 million .com/.net domain names at Q1 2026 (+2.54 million added in the quarter alone) — VeriSign's own reported figure, an *actual* result, not guidance.
- **New registrations:** 11.5 million in Q1 2026, the highest quarterly figure since 2021.
- **Renewal rate improving:** 76.3% (Q1 2026) vs. 75.5% (Q1 2025) — company-reported.
- **Contractually-set price increase, already announced (not guidance):** VeriSign's own Q1 2026 release states the wholesale fee for .com registrations will rise from $10.26 to $10.97 (+6.9%) effective **November 1, 2026** — the latest in a string of ~7%/year increases permitted since a 2018 NTIA/ICANN agreement change (Amendment 35, 2024) that lets VeriSign raise .com prices up to 7%/year in 4 of every 6 years without case-by-case government approval. Senator Elizabeth Warren has publicly criticized this pattern (cumulative >30% since 2018), which is itself independent, third-party confirmation the increases are real and material — not a company talking point.
- **Regulatory/legal exclusivity:** VeriSign's own 10-K describes it as the sole registry operator for .com and .net under long-term Registry Agreements with ICANN, layered under a separate Cooperative Agreement between VeriSign and the US NTIA specific to .com (see Glossary, §9).
- **Infrastructure scale:** VeriSign's own investor materials describe processing an average of 329 billion DNS transactions per day at a peak of over 6 million transactions per second, with an operating margin in the high-60s% — reflecting near-zero marginal cost per additional domain once the infrastructure is built. **No specific cost-per-domain figure benchmarked against a named smaller registry operator was found this session** — so Scale Cost Advantage is not credited as a Moat Signal (§3.3), consistent with this framework's treatment of similarly qualitative-only scale claims in the AXP (2026-07-19) and Toyota (2026-07-12) sessions.
- **No documented two-sided-marketplace / user-growth-driven-value mechanism was found** for Network Effect — VeriSign is a registry monopoly, not a classic multi-sided platform business, so this signal is not credited either (§3.3).

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years without a growth-capex explanation | 98.8% / 111.3% / 129.4% (FY2023–FY2025) — **every year comfortably above 70%** | disqualify if 2+ consecutive years sub-70% | ✅ **PASS**, clean |
| Net Debt/EBITDA over threshold | **1.12×** (§2.4) | disqualify if >2.5× (standard) or >4× (asset-light override) | ✅ **PASS**, clean — well under even the standard threshold; asset-light override not needed |
| FCF-positive 3+ consecutive years | Positive every year FY2023–FY2025 (and per Macrotrends, every year in a 14-year history) | disqualify if not | ✅ **PASS**, clean |

**No hard disqualifier fires.** Unlike the AXP (2026-07-19), JPM (2026-07-14), Citigroup (2026-07-12), and SOFI (2026-06-21) sessions, VeriSign is not a financial company and has a completely conventional, cleanly computable income statement (GAAP operating income exists, no netted-interest-into-revenue issue) — so §3.2's only genuine complication is a narrower one (ROIC's denominator), not the wholesale "no EBIT/EBITDA line exists" problem those sessions hit.

### 3.2 Profitability (25% weight)

```
Net Margin (TTM) = 840.9 / 1,683.2 = 49.96%
NetMargin_Component = clamp((49.96/30)×100, 0, 100) = clamp(166.5) = 100.0   (clamped)
```
Cross-check: stockanalysis.com independently reports VRSN's net margin as 49.96% — an exact match to this session's own TTM computation.

**ROIC — book-value formula breaks down; third-party figure used instead, per documented precedent:**

The standard formula this framework uses elsewhere, `Invested Capital = Total Debt + Equity − Cash` (see Glossary "Invested Capital" entry), gives:
```
Invested Capital = $1,788.8M + (−$2,213.4M) − $476.7M = −$901.3M   (negative)
```
Plugging this into `ROIC = NOPAT / Invested Capital` produces a **negative** ROIC for a company with a 49.96% net margin and near-zero capital intensity — not merely distorted (as flagged for MTCH's *positive-but-shrunk* denominator in the 2026-07-16 session) but sign-flipped and clearly not meaningful, because VeriSign's deeply negative book equity (from buybacks, §2.4) combined with modest total debt makes the book-value denominator negative outright. This is a genuine, structural data gap, not something to paper over by forcing a number through a formula that mechanically breaks in this specific case.

**Third-party sourced figure used instead:** GuruFocus reports VRSN's TTM ROIC at **44.67%** (and its latest-quarter, annualized ROIC at 45.82%) — a methodology that avoids the negative-denominator problem (GuruFocus does not disclose its exact adjustment, but the resulting figure is directionally consistent with VeriSign's extremely high margins and asset-light model, and is corroborated independently by Macrotrends' and other vendors' ROIC figures for VRSN, all clustered in the 40s%). This is the same class of substitution this framework used for AXP/JPM/Citigroup (ROE in place of a non-applicable ROIC), applied here to a different but related structural cause (buyback-driven negative equity, not a lender's deposit-funded balance sheet).
```
ROIC_Component = clamp((44.67/30)×100, 0, 100) = clamp(148.9) = 100.0   (clamped)
```
Note this substitution is **not outcome-determinative**: VeriSign's economics (near-50% net margin, minimal capital investment — FY2025 CapEx just $22.8M against $1.66B revenue) make it all but certain any reasonable ROIC calculation clears the 30% ceiling where this sub-component clamps to 100.0 regardless of the exact figure or methodology used.

```
Profitability_Score = (100.0 + 100.0) / 2 = 100.0   (no FCF-positivity cap — clean multi-year positive FCF, §3.1)
```

### 3.3 Margins (15% weight)

```
FY2025 Gross Margin = (1,656.6 − 196.3) / 1,656.6 = 88.15%
FY2024 Gross Margin = (1,557.4 − 191.4) / 1,557.4 = 87.71%
GrossMargin_Score = clamp((88.15/80)×100, 0, 100) = clamp(110.2) = 100.0   (clamped)
```
Gross margin is stable-to-slightly-expanding (87.71%→88.15%), already far above the 40% threshold the structural-trend bonus is gated on, so no bonus applies (none needed — already clamped at 100.0).

### 3.4 Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $1,424.9M → FY2025 $1,656.6M) = (1,656.6/1,424.9)^(1/3) − 1 = 5.15%
Growth_Score (raw) = clamp((5.15/25)×100, 0, 100) = 20.6
```
**TAM/pricing-power modifier (+10):** documented, *actual* (not guidance) evidence — record domain base (176.1M, +2.54M in Q1 2026), new registrations at a 5-year high (11.5M), improving renewal rate (75.5%→76.3%), and a contractually-set, already-announced .com wholesale price increase ($10.26→$10.97, effective Nov 1 2026) continuing a pattern of ~7%/yr increases sustained without visible registration/volume loss (§2.5). None of this relies on VeriSign's own forward guidance — all of it is either a completed fact (Q1 2026 actuals) or an already-fixed, contractually-set future price (not a forecast of results).
```
Growth_Score = 20.6 + 10 = 30.6
```
**No deceleration modifier:** YoY revenue growth ran +7.3% → +4.8% → +4.3% → **+6.4%** (FY2025) → **+6.6%** (Q1 2026) — decelerating through FY2024, then re-accelerating over the last two reported periods. Not a structural deceleration pattern, so the −10 modifier does not apply.

### 3.5 Balance Sheet (15% weight)

```
Net Debt/EBITDA = 1.12×   (§2.4)
BalanceSheet_Score = 100 × (1 − 1.12/4) = 100 × 0.7200 = 72.0
```

### 3.6 Moat Signal (15% weight)

| Signal | Evidence | Result |
|---|---|---|
| Market share stable/growing | Sole ICANN-designated registry operator for .com/.net (Registry Agreement + NTIA Cooperative Agreement); domain base at a record 176.1M, +2.54M added in Q1 2026 alone; renewal rate improving | ✅ TRUE |
| Brand premium (pricing power) | Contractually-permitted .com wholesale price raised $10.26→$10.97 (+6.9%, effective Nov 2026), continuing ~7%/yr increases since 2018 (>30% cumulative, per Sen. Warren's public criticism) with no visible registration/volume loss — domain base still growing, in fact accelerating | ✅ TRUE |
| Network effect | No documented two-sided-marketplace/user-growth-driven-value mechanism found this session — VeriSign is a registry monopoly, not a classic multi-sided network business | ❌ not established |
| Switching costs | Registrars must build/certify EPP-protocol integration against VeriSign's Shared Registration System (SRS) before operating; registrants face real switching costs abandoning an established .com domain (SEO/email/brand/backlinks), reflected in the improving 76.3% renewal rate | ✅ TRUE |
| Scale cost advantage | ~329B DNS transactions/day, high-60s% operating margin cited, but no cost-per-domain figure benchmarked against a named smaller registry operator found this session | ❌ not established |

```
Moat_Score = (3/5) × 100 = 60.0
```

### 3.7 FCF Quality (10% weight)

```
FY2025 FCF/NI = 1,068.3 / 825.7 = 129.4%
FCFQuality_Score = clamp(((1.294 − 0.40)/0.60)×100, 0, 100) = clamp(149.0) = 100.0   (clamped)
```

### 3.8 Quality Score — final calculation

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

              = (100.0 × 0.25) + (100.0 × 0.15) + (30.6 × 0.20)
              + (72.0 × 0.15) + (60.0 × 0.15) + (100.0 × 0.10)

              = 25.00 + 15.00 + 6.12 + 10.80 + 9.00 + 10.00

              = 75.92  →  rounds to 75.9
```

### 3.9 Gate result: **FAIL — 75.9 < 80.0**

**Sensitivity check (robustness of the two withheld Moat Signal judgment calls):** even crediting Network Effect as well (a generous 4-of-5 reading, Moat_Score = 80.0), the Quality Score would be `75.92 − 9.00 + 12.00 = 78.92` → **78.9 — still below 80.0.** Only crediting *both* remaining signals (5-of-5, Moat_Score = 100.0) would flip the result (81.92 → 81.9), and this session found no citable evidence supporting either withheld signal, so the FAIL conclusion is **robust** to that judgment call — this is not a knife-edge/indeterminate case like the 2026-07-19 AXP session, where the gap between the floor and ceiling reading straddled 80.0 by under 1.5 points on an *un-computable* input. Here, the sub-score most responsible for the shortfall is **Growth (30.6, driven by a modest 5.15% 3yr revenue CAGR)** — VeriSign is fundamentally a mature, low-single-digit-volume-growth monopoly cash generator whose growth profile does not clear this framework's Fast-Grower-oriented Growth sub-score, not a company with a genuinely ambiguous or un-computable input.

**This session stops here per the command specification: no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.** VeriSign does not clear the 80.0+ Quality Score gate.

---

## 4. Why this reads as a genuine (if narrow) miss, not a framework gap

Three of six sub-scores are outstanding for VeriSign — Profitability 100.0 (49.96% net margin, ROIC comfortably above 30% under any reasonable methodology), Margins 100.0 (88%+ gross margin), and FCF Quality 100.0 (129% FY2025 FCF/NI conversion) — and no hard disqualifier fires, unlike the run of financial-company sessions (AXP, JPM, Citigroup, SOFI) that hit a genuine, un-computable-input framework gap. VeriSign's shortfall is concentrated and identifiable: **Growth (30.6/100, 20% weight)** reflects that this is a mature monopoly compounding revenue in the low-to-mid single digits, not a Fast Grower — a real characteristic of the business, not a data gap — and **Moat (60.0/100, 15% weight)** reflects that two of the five checklist signals (Network Effect, Scale Cost Advantage) genuinely lack a citable source this session, not that VeriSign lacks a moat (its two credited signals — regulatory-exclusivity market share and switching-cost-driven renewal rates — are themselves strong evidence of a durable competitive position, just not one that maps cleanly onto all five checklist categories). This is a legitimate application of a strict, deliberately conservative gate to a real business, not a structural framework limitation requiring a fix.

---

## 5. Recommendation: **PASS (no entry) — Quality Gate FAIL at 75.9 (need 80.0+)**

**Do not enter VRSN this session.** The Quality Score of 75.9 is more than 4 points below the strict 80.0+ gate, and — per the sensitivity check in §3.9 — the shortfall survives even a generous reading of the two contestable Moat Signal judgment calls. **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed**, consistent with the command specification's instruction to stop at the Quality Gate rather than proceed on a company that hasn't cleared it.

The triggering Telegram post (a routine "similar results to DOCU" comparison, offered with no specific claims about VRSN's own fundamentals) was used only as the reason to run this first-ever evaluation and was not relied upon for any figure or conclusion above.

---

## 6. Next Review Trigger

No routine re-check is scheduled on a numeric-score basis in the sense of a Phase 02 valuation score (none exists), but this framework does track quality-gate misses for re-evaluation on:
- **VRSN's next earnings release** (Q2 2026, expected per its regular quarterly cadence in late July 2026) — a fresh TTM window could modestly move the Growth sub-score, though a single quarter is unlikely to move the 3yr CAGR enough to close a ~4-point gap on its own.
- A **documented change** to the Growth or Moat sub-score inputs — e.g. a materially higher realized/guided growth rate, or new citable evidence for the Network Effect or Scale Cost Advantage moat signals (a specific cost-per-domain benchmark against a named smaller registry operator would be the most direct path to crediting the latter).
- The standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move.

Absent any of the above, a future Telegram mention of VRSN should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Data Gaps Flagged

1. **ROIC could not be computed via this framework's standard book-value formula** (`Total Debt + Equity − Cash`) — VeriSign's deeply negative stockholders' equity (from cumulative buybacks exceeding contributed capital plus retained earnings) makes the resulting Invested Capital negative (−$901.3M), which would produce a nonsensical negative ROIC for an extremely profitable, capital-light business. A third-party figure (GuruFocus, 44.67% TTM) was used instead, cross-checked as consistent with other vendors — not outcome-determinative since the figure clamps to 100.0 regardless of exact methodology (§3.2). Not resolved this session; flagged as the same general phenomenon already documented in this framework's "Negative stockholders' equity" glossary entry (first raised for MTCH, 2026-07-16), now observed for a different structural cause (large buybacks against modest debt, rather than accumulated losses).
2. **FY2023 revenue/operating income are sourced to VeriSign's own rounded press-release figures** ("$1.49 billion," "up 4.8 percent," "~$1.00 billion"), not independently re-pulled to the exact hundred-thousand from the 10-K — immaterial to the scored 3yr CAGR (which uses FY2022 and FY2025 exact figures) and only used qualitatively for the deceleration check (§3.4), where the already-precise company-reported YoY percentages were used directly.
3. **Scale Cost Advantage and Network Effect Moat Signals were not credited for lack of a citable, specific source** (§2.5, §3.6) — qualitative evidence exists (high operating margin, large DNS transaction volume) but no cost-per-domain figure benchmarked against a named smaller registry competitor, and no documented two-sided-network mechanism, were found this session. A future session with access to a registry-industry cost-structure comparison (e.g. a smaller ccTLD or new-gTLD operator's disclosed cost base) could revisit signal #5.

None of these gaps is silently patched around — each is the explicit reason for a flagged caveat rather than an invented number (§3.9's sensitivity check shows none of them are actually outcome-determinative for the gate result).

---

## 8. Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Cooperative Agreement** | Full entry in [glossary.md](../framework/glossary.md). The NTIA-VeriSign agreement specific to .com, layered on top of VeriSign's separate ICANN Registry Agreement — the regulatory basis for VeriSign's contractually-set .com price increases (§2.5, §3.6). |
| **Domain base** | Full entry in [glossary.md](../framework/glossary.md). VeriSign's total active .com/.net registration count — a record 176.1 million at Q1 2026 (§2.5). |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization — operating-profit measures. Unlike several recent financial-company sessions, VeriSign discloses a clean GAAP Operating Income line, so EBIT/EBITDA are directly computable here (§2.2–2.3). |
| **EPP (Extensible Provisioning Protocol)** | Full entry in [glossary.md](../framework/glossary.md). The protocol registrars use to communicate with VeriSign's registry — the technical-integration mechanism behind this session's Switching Costs Moat Signal (§3.6). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check). VeriSign's FCF/NI ratio ran 98.8%–129.4% across FY2023–FY2025 — comfortably clean (§2.3, §3.1). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. None fired for VRSN this session (§3.1). |
| **ICANN (Internet Corporation for Assigned Names and Numbers)** | Full entry in [glossary.md](../framework/glossary.md). The body that designates VeriSign as the exclusive registry operator for .com/.net (§2.5, §3.6). |
| **Invested Capital** | Full entry in [glossary.md](../framework/glossary.md). This session's Invested Capital calculation for VeriSign is negative (−$901.3M), the reason the standard ROIC formula breaks down (§3.2). |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — VeriSign's ratio is 1.12×, well under both the 2.5× standard and the 4× asset-light thresholds (§3.5). |
| **Negative stockholders' equity (shareholders' deficit)** | Full entry in [glossary.md](../framework/glossary.md). VeriSign's −$2,213.4M equity balance (Q1 2026), from cumulative buybacks — the reason this session substitutes a third-party ROIC figure (§3.2, §2.4). |
| **NTIA (National Telecommunications and Information Administration)** | Full entry in [glossary.md](../framework/glossary.md). The US agency holding the .com-specific Cooperative Agreement with VeriSign (§2.5, §3.6). |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. VRSN scored 75.9 this session — a clean, sensitivity-checked FAIL (§3.8–3.9). |
| **Registrar / Registry Agreement** | Full entry in [glossary.md](../framework/glossary.md). VeriSign's exclusive Registry Agreements with ICANN for .com/.net are the legal basis for its Market Share Moat Signal (§3.6). |
| **Renewal rate** | Full entry in [glossary.md](../framework/glossary.md). VeriSign's .com/.net renewal rate improved to 76.3% (Q1 2026) from 75.5% — cited as Switching Costs evidence (§2.5, §3.6). |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit; not cleanly computable for VeriSign via the standard book-value formula due to its negative equity, so a third-party figure was substituted (§3.2). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. |
| **SRS (Shared Registration System)** | Full entry in [glossary.md](../framework/glossary.md). VeriSign's registrar-facing registry infrastructure — the mechanism behind this session's Switching Costs Moat Signal (§3.6). |
| **TLD (Top-Level Domain) / gTLD** | Full entry in [glossary.md](../framework/glossary.md). .com and .net are the two gTLDs VeriSign exclusively operates (§0, §2.5). |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — this session used Apr 2025–Mar 2026 (FY2025 minus Q1 2025 plus Q1 2026), the most recent complete window available (§2.2). |

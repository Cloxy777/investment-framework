# 2026-07-11 — SCREENING: Developed Asia-Pacific ex-Japan (APAC-EX-JP)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [APAC-EX-JP](../framework/screening-coverage-log.md) (Australia, Hong Kong, Singapore, South Korea, Taiwan), all sectors. Unattended scheduled run. Selected per the rotation rule: tied for oldest "Last screened" (2026-06-14) with **EM**; APAC-EX-JP sorts first alphabetically, so it was picked this rotation. EM's row is untouched.

---

## 0. Methodology

**Unattended session — no user to ask for a TIKR/Koyfin export**, so per screen.md's documented exception this run skips straight to the ETF-holdings fallback. IQLT (the framework's named international quality-factor ETF) was checked in the prior 2026-06-14 pass on this same slice and rejected — its visible/free holdings list is dominated by Japan/Europe with negligible APAC-ex-Japan weight, and the full holdings file sits behind a paywall. That finding still holds; IQLT was not re-checked this session.

**Approach taken (same as the prior APAC-EX-JP pass and the NA-2 precedent): structural triage from documented business-model knowledge**, explicitly building a candidate pool that goes beyond the prior session's 13 names — this rotation's whole point is testing names that weren't in the starting pool last time, not re-confirming the same 13. New candidates this session span Australian enterprise/vertical SaaS, a Singapore wealth-management platform, South Korean internet/gaming/tobacco, Hong Kong-listed luxury (Prada), and Hong Kong/Taiwan semiconductor names. Two of the prior session's flagged items (ResMed near-miss, CSL data-gap) were cheaply re-checked against **live current pricing** given both have moved materially since 2026-06-14, per Rule 0 ("always fetch live price first").

**Data sourcing:** `yfinance` was already established as blocked this session (`curl_cffi` SSL "Connection reset by peer" — same failure mode as the 2026-07-07 NA-1 session) before this task began; not re-tested here to avoid burning time on a call already known to fail. All quantitative figures below are sourced from **stockanalysis.com** (`/quote/<exchange>/<ticker>/financials/`, `/financials/ratios/`, `/financials/cash-flow-statement/` for non-US tickers; `/stocks/<TICKER>/...` for US-listed ADRs), cited inline. The `EODHD_API_KEY` environment variable present in this environment was **not used** — EODHD was removed from this framework's documented process on 2026-06-19 (see `decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md`); the key floating in this environment is stale and out of sync with current docs. Flagging this discrepancy for the orchestrating session rather than fixing it here.

**A data-source gap specific to this session: the `twse` (Taiwan Stock Exchange) exchange-code path on stockanalysis.com returned HTTP 404 for every Taiwan-listed ticker tried**, including a retest of TSMC (TWSE:2330) — a ticker confirmed working via this exact path in the 2026-06-14 session. TSMC's US ADR (`stocks/TSM`) still resolves fine, but **Novatek Microelectronics (TWSE:3034)** has no major US ADR, so it could not be quantitatively evaluated at all this session — flagged as a data gap below, not silently dropped.

---

## Step 1 — Structural triage (business-model eliminations, no quantitative pull)

Building on top of the prior session's Step 1 eliminations (Singapore/HK banks, AIA, Macquarie, Goodman Group REIT, Wesfarmers/JB Hi-Fi retail — all still structurally excluded, not re-litigated), this pass adds:

| Eliminated | Country | Why |
|---|---|---|
| Sea Limited, Grab Holdings | Singapore | E-commerce/ride-hailing/fintech conglomerates with a long history of thin-or-negative core-segment margins; don't clear the "quality" bar structurally regardless of recent profitability inflection |
| Wilmar International | Singapore | Commodity agribusiness (palm oil, sugar, grains) — thin, cyclical margins, doesn't fit this framework's model |
| ComfortDelGro | Singapore | Regulated transport operator — thin margins, low structural growth |
| Venture Corp | Singapore | Electronics Manufacturing Services (EMS/contract manufacturing) — commodity-like thin margins by business-model design (see EMS precedent: HNHPF/Foxconn failed this framework's Quality Score gate for the same reason, 2026-07-06 session) |
| Goodman Group, Charter Hall, UOL Group, CapitaLand | Australia/Singapore | REITs — gross margin/EV-EBIT framing doesn't fit a property-trust balance-sheet model |
| Samsung SDI, LG Energy Solution | South Korea | Battery manufacturing — capital-intensive, cyclical margins tied to EV demand cycles |
| Melco Resorts, Sands China, Galaxy Entertainment | Hong Kong/Macau | Regulated casino gaming — cyclical, licensing/political risk, thin-margin-in-downturn history |
| Hyundai Motor, Kia, Hyundai Mobis | South Korea | Auto OEM/parts — thin-margin, capital-intensive, cyclical (same reasoning as prior NA-session auto exclusions) |
| Samsung Electronics, SK Hynix | South Korea | Carried forward from the 2026-06-14 pass — memory-chip cyclicality; still flagged for a dedicated look if/when memory-cycle timing looks favorable |
| Silergy Corp | Taiwan | Considered as a fabless analog-IC candidate, but its old Nasdaq ticker (SLGC) now resolves to a different company (Standard BioTools) on stockanalysis.com — consistent with Silergy's 2023 take-private/delisting. Treated as no longer publicly investable; dropped without a quantitative pull. |

---

## Step 2 — Full Phase 01 quantitative gate (real, sourced data — stockanalysis.com, pulled 2026-07-11)

Filters: Gross margin >40% · Net margin >12% · ROIC>15% (ROE proxy if ROIC unavailable) · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x

All figures are the latest full fiscal year shown on stockanalysis.com's ratios/financials pages unless marked "(current)" — current-basis figures reflect today's live price against trailing fundamentals, pulled specifically where a name's classification hinges on a price-sensitive metric and the price has moved materially since fiscal year-end (Rule 0).

| Ticker | Gross M | Net M | ROIC (or ROE proxy) | Rev 3yr CAGR | FCF 3yr positive? | Net Debt/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Pro Medicus (ASX:PME)** [[1]](#src1) | 99.86% ✅ | 54.10% ✅ | ROIC 268.45% / ROE 51.82% ✅ | 27.75% ✅ (FY22→25: 93.46→212.98 AUD M) | ✅ (profitable & growing every year) | −1.32 (net cash) ✅ | 0.37% ❌ | 187.59× ❌ | **FAIL — extreme overvaluation** despite best-in-pool quality metrics |
| **WiseTech Global (ASX:WTC)** [[2]](#src2) | 86.17% ✅ | 25.77% ✅ | ROIC 14.55% ❌ / ROE 12.65% ❌ | 21.8% ✅ (FY22→25: 435.58→778.7) | ✅ | −0.16 (net cash) ✅ | 1.45% ❌ | 73.11× ❌ | **FAIL — returns just under 15% bar + extreme overvaluation** |
| **TechnologyOne (ASX:TNE)** [[3]](#src3) | 57.03% ✅ | 23.00% ✅ | ROIC 76.34%* / ROE 33.17% ✅ | 18.14% ✅ (FY22→25: 368.23→598.5) | ✅ | −1.47 (net cash) ✅ | 2.32% ❌ | 71.63× ❌ | **FAIL — extreme overvaluation** (*ROIC figure implausibly high relative to a modest balance sheet — flagged, not relied on; ROE tells the same quality story) |
| **SEEK Limited (ASX:SEK)** [[4]](#src4) | 59.57% ✅ | 22.35% ✅ (FY25; volatile due to discontinued-ops gains in FY21/23) | ROIC 5.38% ❌ / ROE 9.04% ❌ | ≈0% ❌ (FY22→25: 1,117→1,097, essentially flat-to-down) | ✅ (net income swung negative FY24 but FCF metrics still computed) | 3.90 ❌ | 3.76% ❌ | 36.85× ❌ | **FAIL — 6 of 8 filters** |
| **Computershare (ASX:CPU)** [[5]](#src5) | **data gap** (Gross Profit = Operating Income in FY24/25 rows — no distinct COGS breakout in this source; not assumed) | 19.46% ✅ | ROIC 22.92% ✅ / ROE 29.52% ✅ | ≈6.7–7.1% ❌ (FY22→25: 2,565→3,119 USD M; narrowly under 8% bar) | ✅ | 0.86 ✅ | 5.16% ✅ | 17.96× ✅ | **NEAR-MISS — 1 narrow miss (growth) + 1 data gap (gross margin)**, everything else clears |
| **ASMPT / ASM Pacific Technology (HKG:0522)** [[6]](#src6) | 38.29% ❌ (close) | 6.57% ❌ | ROIC 4.09% ❌ / ROE 6.69% ❌ | −11.09% ❌ (FY22→25: 19,363→13,736 HKD M — cyclical semiconductor-equipment downturn) | ✅ (barely — profit compressed sharply) | −1.23 (net cash) ✅ | −0.47% ❌ | 45.93× ❌ | **FAIL — 6 of 8**, same cyclicality reasoning flagged for Samsung/SK Hynix last rotation |
| **NAVER Corp (KRX:035420)** [[7]](#src7) | **data gap** (Gross Profit = Revenue in all years — confirmed no COGS line in this source, not a real 100% margin) | 16.06% ✅ | ROIC 6.84% ❌ / ROE 6.50% ❌ | 13.5% ✅ (recomputed FY22→25: 8,220,079→12,035,007 KRW M; source's own "11.5%" used a 2yr window mislabeled 3yr) | ✅ | −1.47 (net cash) ✅ | 5.13% ✅ | 15.25× ✅ | **FAIL — returns well under 15% bar** (not narrow); gross margin unverifiable |
| **KRAFTON (KRX:259960)** [[8]](#src8) | **data gap** (Gross Profit = Revenue in all years — confirmed no COGS line at source, same limitation as NAVER) | 22.09% ✅ | ROIC 21.17% ✅ (used as primary — available) / ROE 10.47% | 21.53% ✅ (recomputed FY22→25: 1,854,016→3,326,554 KRW M) | ✅ (284,449 / 876,253 / 928,969 KRW M, FY23–25) | −2.28 (net cash) ✅ | 8.46% ✅ | 8.09× ✅ | **7/8 confirmed PASS + 1 data gap (gross margin unverifiable, not assumed)** |
| **iFAST Corporation (SGX:AIY)** [[9]](#src9) | 50.86% ✅ | 19.43% ✅ | ROIC not disclosed / **ROE 28.02% ✅** (used as proxy per filter rule) | 35.05% ✅ (recomputed FY22→25: 208.87→514.72 SGD M) | ✅ (266.89 / 661.52 / 538.78 SGD M, FY23–25) | −7.06 (net cash) ✅ | 18.64% ✅ | 9.60× ✅ | **PASS — all 8 filters clear cleanly** |
| **Prada S.p.A. (HKG:1913)** [[10]](#src10) | 80.32% ✅ | 14.90% ✅ | ROIC 12.88% ❌ (used as primary — available) / ROE 18.96% | 10.83% ✅ (recomputed FY22→25: 4,201→5,718 EUR M) | ✅ (395.61 / 1,192 / 1,043 EUR M, FY23–25) | 2.25 ✅ (close to cap — likely includes IFRS 16 lease liabilities, common for a store-network retailer) | 8.28% ✅ | 11.43× ✅ | **NEAR-MISS — only ROIC (12.88% vs 15%) fails**, everything else clears |
| **KT&G Corporation (KRX:033780)** [[11]](#src11) | ≈47.7% ✅ | ≈17.2% ✅ | ROIC 10.76% ❌ / ROE 11.80% ❌ | 4.11% ❌ (FY22→25: 5,851,406→6,579,707 KRW M) | ✅ (though FY25 FCF yield turned negative) | 0.35 ✅ | −0.43% ❌ (FY25; positive in FY21–24) | 11.38× ✅ | **FAIL — 4 of 8**, confirms the "mature, regulated, low-growth" structural read with real numbers |

### Live-price reversals — re-checking the prior session's ResMed near-miss and CSL data gap

Both ResMed and CSL have moved materially in price since the 2026-06-14 session (ResMed's FY2025 EV/EBIT-based classification depended on a price that has since fallen; CSL's stock is down further still). Per Rule 0 ("always fetch live prices first"), both were re-checked on a **current/TTM basis** — non-price fundamentals (margins, ROE, revenue growth, FCF-positive history) are carried forward unchanged from the 2026-06-14 session since neither has reported a new annual result since then; only the price-sensitive ratios (EV/EBIT, FCF yield, and for CSL, Net Debt/EBITDA) were refreshed against today's live price.

| Ticker | Basis | Gross M | Net M | ROE | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **ResMed (RMD)** [[12]](#src12) | FY2025 (carried) | 59.36% ✅ | 27.22% ✅ | 25.86% ✅ | 12.92% ✅ | ✅ | 0.44 ✅ | 4.40% ✅ (FY25) → **5.97% ✅ (current)** | 22.20× ❌ (FY25) → **14.85× ✅ (current)** | **Reverses to all-8-clear on current pricing** — was a 1-filter (EV/EBIT) near-miss on FY2025 basis |
| **CSL Limited (ASX:CSL)** [[13]](#src13) | FY2025 (carried) + current | 51.9% ✅ | 19.3% ✅ | 15.37% ✅ (barely) | 13.8% ✅ | ✅ | data gap (FY25) → **2.07 ✅ (current)** | 3.85% ❌ (FY25) → **7.77% ✅ (current)** | 21.73× ❌ (FY25) → **12.71× ✅ (current)** | **Reverses to all-8-clear on current pricing** — was a data-gap/borderline case on FY2025 basis; CSL's price is down further still since 2026-06-14 |

**Important caveat on both:** this "current" read mixes live price against the last reported annual fundamentals (a TTM-style reconstruction), which is exactly the price-vs-fundamentals combination Rule 0 requires for price-sensitive ratios — but it is a different basis than the clean FY-only read used for the rest of this session's candidates, and both stocks' apparent "pass" is driven almost entirely by a large trailing-year price decline rather than any fundamental improvement. Before treating either as a firm addition to the Qualified Quality List, **run `/new-position` on each** to confirm with a full live-price Phase 02 pass and to sanity-check whether the price decline reflects a genuine re-rating opportunity or a fundamental deterioration not yet visible in trailing financials (particularly relevant for CSL, down materially for a second consecutive session).

---

## ✅ Qualified Quality List — 1 clean name, plus 3 flagged for immediate follow-up

**iFAST Corporation (SGX:AIY)** — the only name this session that clears all 8 Phase 01 filters with fully unambiguous, distinctly-sourced numbers (including a genuine, non-degenerate gross margin figure).

**Flagged, not included outright, pending confirmation:**
- **KRAFTON (KRX:259960)** — 7/8 filters clear comfortably; only gross margin is unverifiable (data-source limitation, not a real number to assume either way)
- **ResMed (RMD)** and **CSL Limited (CSL.AX)** — both now show all 8 filters clearing on a current/live-price basis, reversing their FY2025-basis near-miss/data-gap status from the 2026-06-14 session — recommend `/new-position` on both to confirm before any capital commitment

### Near-misses flagged for the watchlist

- **Prada S.p.A. (1913.HK)** — 7/8 clear; only ROIC (12.88% vs. 15% bar) falls short, and by a moderate (~2pp) margin — worth a re-check if ROIC trends up or on the next rotation.
- **Computershare (ASX:CPU)** — 6/8 clear + 1 data gap; revenue 3yr CAGR (≈6.7–7.1%) is just under the 8% bar, same "regulatory-adjacent fee + float-income" business quality as HKEX/SGX (passed/near-missed in the prior session) but slower-growing.

---

## Step 3 — Qualitative pass

### iFAST Corporation (SGX:AIY) — the clean PASS

1. **Why are margins high?** iFAST operates a B2C/B2B wealth-management and investment platform (unit trusts, bonds, ETFs, stocks, insurance) across Singapore, Hong Kong, Malaysia, China, and the UK (via its 2023 acquisition of Standard Life's retail advice/wealth business, "iFAST Global Bank"/Bank division in the UK). Its 50.86% gross margin and rapidly expanding FCF yield reflect a scalable, largely digital distribution platform: once the platform and custody/settlement infrastructure exist, incremental assets under administration (AUA) carry low marginal servicing cost. The 2024–2025 profit surge (net income roughly tripling FY22→FY25) coincides with the UK Central Bank Digital Infrastructure Services (CBDIS) contract ramp — a large, multi-year Bank of England-awarded digital-infrastructure services contract for the UK ISA/wealth ecosystem — which is a real, filed contractual win, not a cyclical fluke, though it's also a concentration point (see bear case).
2. **What would it take to compete?** A new entrant would need: (a) regulatory licenses across multiple jurisdictions (Singapore MAS, Hong Kong SFC, UK FCA), (b) an established custody/settlement/fund-platform infrastructure, and (c) years of AUA accumulation to reach comparable scale economics. Existing scaled competitors (Fundsupermart's own legacy niche, bank-distributed platforms, robo-advisors) compete on parts of this but not the full multi-market administration stack iFAST has built.
3. **Capital allocation (5–10yr):** Primarily organic platform reinvestment plus the 2023 Standard Life UK wealth-business acquisition — a sizeable, strategically-adjacent bolt-on (not a diversifying/value-destructive deal) that directly produced the CBDIS contract win. No major buyback history evident (still a compounding-growth-stage company); dividend payout has resumed as profitability scaled.
4. **Where's growth coming from (3–5yr)?** UK CBDIS contract ramp (multi-year build-out), continued AUA growth across Asia-Pacific wealth markets, and cross-selling insurance/banking products to the existing platform base.
5. **Best bear case:** (a) Heavy near-term reliance on a single large UK government-adjacent contract for the recent profit inflection — a renewal/scope risk at contract renegotiation; (b) wealth-platform economics are ultimately AUM/AUA-market-cycle-sensitive — a prolonged bear market in the underlying asset classes would compress both AUA and fee revenue; (c) still a comparatively small-cap, thinly-covered name (per the framework's own Discovery Filters, likely under 8 analysts) — less independent scrutiny of the numbers than a mega-cap peer.
6. **Disruption vector:** Low-to-moderate — wealth platforms with custody/regulatory licensing built in are moderately defensible, but the space is also where low-cost robo-advisors and bank-native platforms compete hardest on fee compression; iFAST's UK government-contract angle is a differentiated moat vector less exposed to that specific commoditization pressure.

**Conclusion:** iFAST is a genuine Phase 01 pass with an unusual, well-documented recent catalyst (the UK CBDIS contract), but the profit ramp is recent enough (FY22 net income was just 6.42M SGD) that more than one full year of post-ramp results is warranted before treating the current margin/return profile as the new normal. **Recommend `/new-position iFAST` (AIY.SG)** for full Phase 02 scoring with live pricing.

### KRAFTON (KRX:259960) — flagged, shorter treatment given the gross-margin data gap

1. **Why are margins high?** KRAFTON is dominated by PUBG: BATTLEGROUNDS (PC/console) and PUBG Mobile, both long-tail live-service games monetized via in-game purchases (cosmetics, battle passes) on top of largely-amortized development costs — a classic high-operating-leverage game-publisher model (31.7% operating margin, 22.09% net margin FY2025).
2. **What would it take to compete?** A competitor needs to displace an entrenched, still-large PUBG player base (network effects within the battle-royale genre are meaningful — friends cluster on the same game) — hard but not impossible, as the genre has seen share shift before (Fortnite, Apex Legends).
3. **Capital allocation (5–10yr):** Actively diversifying beyond PUBG via new titles and stakes/investments (e.g., inZOI, and international studio investments) — a reasonable single-franchise-risk mitigation strategy, though PUBG still supplies the large majority of revenue.
4. **Where's growth coming from (3–5yr)?** PUBG Mobile India/emerging-market monetization, new title pipeline (inZOI life-sim launched 2025), and continued live-service content updates to the existing franchise.
5. **Best bear case:** Extreme single-franchise concentration — a PUBG engagement decline (common in the hit-driven gaming industry once a title ages) would hit revenue and margins hard with limited diversification cushion today; South Korean gaming stocks have historically re-rated sharply on any franchise-fatigue signal (see NCSoft's margin/multiple decline, noted in the framework's general Asia-gaming risk awareness).
6. **Disruption vector:** Moderate — mobile/PC gaming attention is highly substitutable game-to-game; no structural moat beyond the existing player base and live-service content cadence.

**Conclusion:** Strong quantitative profile (21.53% 3yr revenue CAGR, 8.46% FCF yield, 8.09× EV/EBIT — cheap for the growth on offer) but real single-franchise concentration risk, and the gross-margin data gap means it isn't a clean 8-for-8 pass this session. **Worth a `/new-position` look if the gross-margin figure can be resolved via a primary Korean-language filing**, otherwise re-check on the next rotation.

### ResMed and CSL — not given a fresh 5-question qualitative pass this session

Both were already qualitatively profiled in general terms in prior sessions' business-model knowledge (medical devices, durable moats). Given their PASS status this session is driven by a live-price reversal rather than a new qualitative finding, a full requalification is deferred to the recommended `/new-position` runs on each, where it belongs alongside full Phase 02 scoring.

---

## Data gaps flagged (per CLAUDE.md Rule 0 — none estimated)

- **Computershare, NAVER, KRAFTON — gross margin**: all three show "Gross Profit" identical to (or, for Computershare, converging with) "Operating Income"/Revenue in stockanalysis.com's income-statement view — confirmed via a follow-up fetch that no separate Cost-of-Revenue/COGS line exists in this data source for any of the three. Flagged as unverifiable rather than assumed to pass or fail.
- **Novatek Microelectronics (TWSE:3034)**: the `twse` exchange-code path on stockanalysis.com returned HTTP 404 all session — confirmed as a session-wide issue (not ticker-specific) by retesting TSMC/TWSE:2330, which worked in the 2026-06-14 session but also 404'd this session. No US ADR exists for Novatek, so it could not be evaluated at all.
- **Fisher & Paykel Healthcare (FPH)**: both the `asx/FPH` and `nzx/FPH` paths on stockanalysis.com returned HTTP 404 — not evaluated this session.
- **Silergy Corp**: appears no longer publicly listed (see Step 1 structural-triage table) — not a data gap so much as an availability gap, noted for completeness.
- **SEEK Limited net margin**: FY2025's 22.35% (and the anomalous FY2023 82.64%-equivalent gain in the prior session's CAR Group note, structurally similar issue here) is distorted across the lookback window by large one-off discontinued-operations gains/losses (FY21 +752.2M, FY23 +1,046M, FY24 −100.9M) — FY2025's cleaner 22.35% used for the verdict, but SEEK fails on multiple other filters regardless.
- **TechnologyOne ROIC (76.34%)**: flagged as implausibly high for the company's balance sheet — likely reflects a very small invested-capital denominator (asset-light SaaS model) rather than genuinely being a >5x-ROE figure; ROE (33.17%) used as the more reliable quality signal, though it doesn't change TNE's FAIL verdict (driven by valuation).
- **Pro Medicus ROIC (268.45%)**: same caveat as TechnologyOne — an asset-light business with minimal invested capital produces a mathematically extreme but not very informative ROIC; ROE (51.82%) is the more interpretable figure.
- **CSL Limited / ResMed "current" figures**: reflect today's live price against the last full fiscal year's trailing fundamentals (a TTM-style reconstruction), not a freshly-reported new fiscal year — flagged explicitly in Step 2 as a different basis than the rest of this session's candidates, with `/new-position` recommended to fully resolve both.

---

## Sources

<a id="src1"></a>[1] PME: https://stockanalysis.com/quote/asx/PME/financials/ratios/ , https://stockanalysis.com/quote/asx/PME/financials/
<a id="src2"></a>[2] WTC: https://stockanalysis.com/quote/asx/WTC/financials/ratios/ , https://stockanalysis.com/quote/asx/WTC/financials/
<a id="src3"></a>[3] TNE: https://stockanalysis.com/quote/asx/TNE/financials/ratios/ , https://stockanalysis.com/quote/asx/TNE/financials/
<a id="src4"></a>[4] SEK: https://stockanalysis.com/quote/asx/SEK/financials/ratios/ , https://stockanalysis.com/quote/asx/SEK/financials/
<a id="src5"></a>[5] CPU: https://stockanalysis.com/quote/asx/CPU/financials/ratios/ , https://stockanalysis.com/quote/asx/CPU/financials/
<a id="src6"></a>[6] ASMPT (0522.HK): https://stockanalysis.com/quote/hkg/0522/financials/ratios/ , https://stockanalysis.com/quote/hkg/0522/financials/
<a id="src7"></a>[7] NAVER (035420.KS): https://stockanalysis.com/quote/krx/035420/financials/ratios/ , https://stockanalysis.com/quote/krx/035420/financials/
<a id="src8"></a>[8] KRAFTON (259960.KS): https://stockanalysis.com/quote/krx/259960/financials/ratios/ , https://stockanalysis.com/quote/krx/259960/financials/ , https://stockanalysis.com/quote/krx/259960/financials/cash-flow-statement/
<a id="src9"></a>[9] iFAST (AIY.SG): https://stockanalysis.com/quote/sgx/AIY/financials/ratios/ , https://stockanalysis.com/quote/sgx/AIY/financials/ , https://stockanalysis.com/quote/sgx/AIY/financials/cash-flow-statement/
<a id="src10"></a>[10] Prada (1913.HK): https://stockanalysis.com/quote/hkg/1913/financials/ratios/ , https://stockanalysis.com/quote/hkg/1913/financials/ , https://stockanalysis.com/quote/hkg/1913/financials/cash-flow-statement/
<a id="src11"></a>[11] KT&G (033780.KS): https://stockanalysis.com/quote/krx/033780/financials/ratios/ , https://stockanalysis.com/quote/krx/033780/financials/
<a id="src12"></a>[12] ResMed: https://stockanalysis.com/stocks/RMD/financials/ratios/ (current/TTM figures, pulled 2026-07-11); FY2025 figures carried from the 2026-06-14 session
<a id="src13"></a>[13] CSL: https://stockanalysis.com/quote/asx/CSL/financials/ratios/ (current + FY2025 figures, pulled 2026-07-11)
Data-gap confirmation fetches: https://stockanalysis.com/quote/twse/2330/financials/ratios/ (404, retest); https://stockanalysis.com/quote/twse/3034/ (404); https://stockanalysis.com/quote/asx/FPH/financials/ratios/ (404); https://stockanalysis.com/quote/nzx/FPH/financials/ratios/ (404); https://stockanalysis.com/stocks/SLGC/financials/ratios/ (resolves to Standard BioTools, not Silergy)

---

## Next steps

- `/new-position iFAST` (AIY.SG) — the one clean Phase 01 pass this session; full Phase 02 scoring with live price.
- `/new-position ResMed` (RMD) and `/new-position CSL` (CSL.AX) — both reversed from near-miss/data-gap to all-8-clear on live pricing; confirm with a full Phase 02 pass before any sizing decision, and specifically sanity-check whether CSL's continued price decline (down materially across two consecutive rotations) reflects a genuine opportunity or a fundamental deterioration not yet visible in trailing financials.
- Watchlist: **KRAFTON** (259960.KS, gross-margin data gap), **Prada** (1913.HK, narrow ROIC miss), **Computershare** (CPU.AX, narrow growth miss) — re-check on the next APAC-EX-JP rotation or if the specific missing/near-miss metric resolves.
- **Novatek Microelectronics** and **Fisher & Paykel Healthcare** — re-attempt with a different data source (the `twse` stockanalysis.com path and both FPH exchange-code paths were down this session); not a business-model exclusion, purely a sourcing gap.
- Coverage log updated below — next "oldest screened" alphabetical slice is **EM (Emerging Markets)**, still at 2026-06-14 (untouched this session).

---

## Glossary

- **ADR (American Depositary Receipt)** — a US-exchange-listed security representing shares of a non-US company (used here for TSMC's `TSM` ticker as an alternative to the blocked `twse` path).
- **AUA (Assets Under Administration)** — the total value of client assets a platform like iFAST administers; a scale metric distinct from its own revenue.
- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value over several years.
- **EMS (Electronics Manufacturing Services)** — the contract-manufacturing industry (assembling electronics for a brand owner) — structurally thin-margin, cited here as the reason Venture Corp was structurally excluded.
- **EV/EBIT** — Enterprise Value divided by EBIT (operating profit) — a multiple used to compare how expensive companies are relative to operating profit, independent of capital structure.
- **FCF (Free Cash Flow)** — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **Gross Margin** — Gross Profit (Revenue − Cost of Revenue) ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **IFRS (International Financial Reporting Standards)** — the accounting standard most non-US companies (including Prada) use for audited financial statements, as opposed to US GAAP.
- **Net Debt/EBITDA** — net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **Qualified Quality List** — the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring.
- **ROE** — Return on Equity — Net Income ÷ shareholder equity; how efficiently a company generates profit from shareholders' capital.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results, used here to combine a live/current price with the latest annual fundamentals for ResMed and CSL.

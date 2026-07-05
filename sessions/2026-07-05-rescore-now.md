# RESCORE — NOW (ServiceNow, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-07-05 (Sunday — markets closed; most recent trading session 2026-07-02, ahead of the 3 Jul July 4th holiday observance and the weekend)
**10Y US Treasury Yield:** 4.49% (TradingEconomics/dshort "Treasury Yields Snapshot," 2 Jul 2026 close — same figure used in the same-day [2026-07-05 MSFT rescore](2026-07-05-rescore-msft.md) for consistency across same-day sessions)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** NOW **42.3** (2026-06-20, BUY-Standard band on score, but blocked at entry by a sub-2:1 R/R — [sessions/2026-06-20-rescore-now.md](2026-06-20-rescore-now.md)); Composite Score never computed (predates the 2026-06-29 Quality Score/Composite Score methodology change — flagged stale, see [watchlist/STALE.md](../watchlist/STALE.md)).
**Current NOW portfolio weight:** 2.16% per [holdings.md](../portfolio/holdings.md) — comfortably under the 15% hard cap (Upgrade 7); not recomputed this session (weight refresh is `/sync-portfolio`'s job).
**First-ever Quality Score / Composite Score computation for NOW this session.**

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$106.32** | IBKR `get_price_history` (contract_id 109911821, NYSE), most recent daily bar close = **2026-07-02**. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$105.80** (`is_close: true`) — one session stale: `get_price_history` shows 2026-07-01 close = $105.80 and 2026-07-02 close = $106.32. Same recurring stale-snapshot pattern flagged in the 2026-07-05 MSFT and 2026-07-04 AVGO sessions — used the fresher $106.32 instead. Cross-checked against `yfinance`'s `currentPrice`/`regularMarketPrice`, both independently reading $106.32. |
| 52-week range | $81.24 – $210.20 (IBKR `misc_statistics` / `yfinance`) | Unchanged band from 06-20. |
| Year-to-date change | −30.94% (IBKR `year_to_date_change`) | |
| Analyst consensus PT | mean **$141.12**, range $85–$236, 46 analysts | `yfinance` `targetMeanPrice`/`targetHighPrice`/`targetLowPrice` — bull-case sanity check only (Rule 0 Step 4), not a scored input. |
| Price vs. 06-20 review ($95.04) | **+11.87%** | A real recovery, but well under the 15% Rule 9 threshold. |

---

## 2. Rule 9 Trigger Check (2026-06-20 → 2026-07-05)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Next report confirmed **22 Jul 2026, after close** (Q2 FY2026) — `yfinance` `get_earnings_dates`. |
| Guidance revision | No | No new formal guidance issued this window. FY2026 subscription guidance (raised to $15.735–$15.775B, +20.5–21% YoY) and the Now Assist AI ACV target (raised $1B→$1.5B) were both set at ServiceNow's Investor Day (May 2026) and the Q1 2026 print (22 Apr 2026) — **both predate the 06-20 review**, so not a fresh trigger this session, but incorporated into the scenario architecture below since the 06-20 session's text didn't cite them. |
| M&A | No (predates window) | ServiceNow closed the Armis acquisition 20 Apr 2026 and Veza 2 Mar 2026 — both before the 06-20 review, not new. Armis is guided to create ~25–75bps of FY2026 margin/FCF-margin headwind, normalizing by FY2027 per management — noted qualitatively, not a fresh Rule 9 event. |
| Management change | No | None found. |
| Macro shift | No | 10Y ticked from 4.46% (06-20) to 4.49% (07-02) — still inside the "3.5–5%" bracket, no Rate Regime bracket change. |
| >15% unexplained price move | No | +11.87% over 15 days — a continuation of the post-de-rating recovery already discussed 06-20, not unexplained, and under the 15% threshold. |

**Conclusion: no Rule 9 trigger fired.** This is a routine, scheduled price-refresh rescore — but see §4 for the **first-ever NOW Quality Score computation**, which is new information independent of any Rule 9 event.

---

## 3. Data Gaps / Flags

1. **Fast-Grower / PEG eligibility — REVISED this session.** The 06-20 session scored NOW as a Fast Grower (PEG sub-score, 15% weight) on the basis of revenue 3yr CAGR (22.4%) and *forward* EPS-growth estimates. Re-examining under the 2026-06-20 "clean, non-distorted earnings base" clarification (the DUOL precedent) using **trailing, actual** diluted EPS — the correct test per [valuation-scoring.md](../framework/valuation-scoring.md) — NOW's GAAP earnings base is **not clean**:
   ```
   FY2022 Diluted EPS $0.320 (NI $325M)
   FY2023 Diluted EPS $1.684 (NI $1,731M)  → +432.6% YoY — driven by a −71.7% effective tax rate
                                              (Tax Provision −$723M vs. Pretax Income $1.008B),
                                              a textbook "deferred tax valuation allowance release"
                                              pattern (see glossary) — a one-off, not organic earnings growth.
   FY2024 Diluted EPS $1.368 (NI $1,425M)  → −17.7% YoY — an outright DECLINE the year immediately
                                              following the distorted base year.
   FY2025 Diluted EPS $1.670 (NI $1,748M)  → +22.7% YoY
   ```
   A one-off-distorted base year followed by a decline is exactly the pattern the clean-earnings clarification excludes. **NOW does not have 3 consecutive years of clean >15%/yr EPS growth on a GAAP basis — not a qualifying Fast Grower this session.** PEG's 15% weight is redistributed to EV/EBIT (→ 40%), per [valuation-scoring.md](../framework/valuation-scoring.md). This is a correction to the 06-20 session's determination, flagged transparently rather than silently overridden. `yfinance`'s trailing `pegRatio` (1.03, implying PEG_Score 26.5) is shown below as a **sensitivity check only**, not the scored input — consistent with the DUOL/CSGP precedent.

2. **Forward PE — fallback (avg-based) formula used despite a technically-available 5yr range**, consistent with NOW's own 06-20 session and the MSFT/NKE sessions' established practice (the automated `yfinance`-`get_earnings_dates` reconstruction always yields both an average and a low/high range, but this framework's session precedent has used the **fallback** average-based formula as the default even when a range exists — flagged as a standing, unresolved primary-vs-fallback ambiguity in [watchlist/README.md](../watchlist/README.md), not resolved here; NOW's own 5yr range (23.10×–122.80×) is unusually wide and dominated by 2020–2022 hyper-growth-era multiples, reinforcing the case for the more robust average-based fallback in this specific case).

3. **ROIC cross-check — wide vendor dispersion.** My computed TTM ROIC (12.53%, see §5) sits between GuruFocus's TTM figure (6.48%) and stockanalysis.com's (16.78%) — a wide dispersion driven by differing NOPAT/Invested-Capital conventions across vendors. My figure uses the same Debt+Equity Invested-Capital convention and EBIT-based NOPAT used in the MSFT/NKE sessions, for methodological consistency across this repo, and sits roughly at the bracket's midpoint.

4. **Quality Score gate result is sensitive to one moat judgment call** (§4) — 78.7 (fails) vs. 81.7 (would pass) depending on whether the "Network Effect" or "Scale Cost Advantage" signal is credited. Shown transparently, mirroring the same-shape disclosure in the 2026-07-04 AVGO and 2026-07-05 MSFT sessions.

5. **Shareholder yield refined this session** (bottom-up): no dividend (`dividendYield` None, `payoutRatio` 0.0). Net buyback yield computed from the TTM diluted-average-share change (1,045M TTM-ending-Q1'25 → 1,040M TTM-ending-Q1'26 = **−0.48%**, i.e. a small net share-count reduction) — a refinement of the 06-20 session's conservative "~0%" placeholder (that session flagged this as needing precise sourcing). Full-year FY2025 buybacks were actually large ($1.84B) but mostly offset by stock-based-compensation issuance at the annual level (diluted average shares still rose FY2022→FY2025); the most recent few quarters show buybacks finally outpacing dilution, hence the small net-positive figure used here.

---

## 4. NOW — Inputs Collected (fresh this session, `yfinance` via `requests.Session()`)

**Sector:** Technology — Enterprise Software (Workflow Automation / SaaS, ITSM)

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 1,031,308,000 | `yfinance` `sharesOutstanding` |
| **Market Cap** | 1,031,308,000 × $106.32 = **$109,648.67M** | Computed — matches `yfinance` `marketCap` ($109,648,666,624) essentially exactly |
| Total debt (2026-03-31) | $2,431M | `yfinance` quarterly balance sheet |
| Cash + ST investments (2026-03-31) | $5,182M | `yfinance` quarterly balance sheet |
| **Net Debt** | $2,431M − $5,182M = **−$2,751M (net cash)** | Computed |
| **EV** | $109,648.67M − $2,751M = **$106,897.67M** | Computed — matches `yfinance` `enterpriseValue` ($106,897,670,144) essentially exactly |
| TTM EBIT (Q2'25–Q1'26) | $477M + $700M + $546M + $679M = **$2,402M** | `yfinance` quarterly financials rollforward (unchanged from 06-20's $2.402B) |
| **EV/EBIT** | $106,897.67M ÷ $2,402M = **44.50×** | Computed |
| TTM Operating Cash Flow | $716M + $813M + $2,238M + $1,670M = $5,437M | `yfinance` quarterly cashflow rollforward |
| TTM CapEx | $190M + $244M + $238M + $141M = $813M | Same |
| **TTM FCF** | $5,437M − $813M = **$4,624M** | Computed |
| **FCF Yield** | $4,624M ÷ $109,648.67M = **4.2172%** | Computed |
| TTM Net Income | $385M + $502M + $401M + $469M = **$1,757M** | `yfinance` quarterly financials rollforward |
| TTM Revenue | $3,215M + $3,407M + $3,568M + $3,770M = **$13,960M** | Same |
| Net Margin (TTM) | 12.586% | Computed — exact match to `yfinance` `profitMargins` (0.12586) |
| TTM Pretax Income / Tax Provision | $2,379M / $622M | `yfinance` quarterly rollforward |
| Effective tax rate (TTM) | 622/2,379 = **26.15%** | Computed |
| TTM D&A | $172M+$194M+$212M+$258M = $836M | `yfinance` quarterly cashflow |
| EBITDA (TTM) | $2,402M + $836M = $3,238M | Computed |
| **Net Debt/EBITDA (TTM)** | −$2,751M ÷ $3,238M = **−0.849× (net cash)** | Computed |
| Gross Margin (TTM) | 10,688/13,960 = **76.56%** | Computed — exact match to `yfinance` `grossMargins` (0.76562) |
| Revenue 3yr CAGR (FY2022 $7.245B → FY2025 $13.278B) | (13.278/7.245)^(1/3)−1 = **22.40%** | `yfinance` annual financials — matches 06-20 session exactly |
| Forward EPS (NTM) | $5.0267 | `yfinance` `forwardEps` |
| **Forward PE** | $106.32 ÷ $5.0267 = **21.151×** | Computed — matches `yfinance` `forwardPE` (21.151094) |
| 5yr avg/range PE | avg **67.78×**, range **23.10×–122.80×** (n=20 quarters, through the 22 Apr 2026 earnings print) | `get_earnings_dates`+price-history reconstruction — matches the 06-20 session's 67.8×/23.1–122.8× essentially exactly (one quarter fresher) |
| FCF/NI conversion (TTM) | 4,624/1,757 = **263.3%** | Computed — high-quality, consistent with 2022–2025 annual ratios of 156–669% |
| Total Stockholders' Equity (2026-03-31) | $11,728M | `yfinance` quarterly balance sheet |
| **Invested Capital** (Debt+Equity convention) | $2,431M + $11,728M = **$14,159M** | Computed |
| **NOPAT** | $2,402M × (1−0.2615) = **$1,773.8M** | Computed |
| **ROIC (TTM)** | $1,773.8M ÷ $14,159M = **12.53%** | Computed — brackets between GuruFocus (6.48%) and stockanalysis.com (16.78%), see §3 flag 3 |
| Diluted avg shares (TTM-ending-Q1'26 vs. Q1'25) | 1,040M vs. 1,045M | `yfinance` — net buyback yield ≈ **+0.48%** (see §3 flag 5) |
| Dividend yield | None (no dividend) | `yfinance` |

---

## 5. NOW — Quality Score (first-ever computation, 2026-06-29 methodology)

**Hard disqualifier check (all must pass before the weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | Annual FY2022–2025: 668.6% / 156.0% / 236.8% / 259.3% — all comfortably ≥70% every year | disqualify if <70% for 2+ yrs *without* explanation | ✅ PASS |
| Net Debt/EBITDA over threshold? | **−0.849× (net cash)** | disqualify if >2.5× | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FCF-positive every year on record (FY2022–2025 and TTM) | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight)

```
Net Margin (TTM)    = $1,757M / $13,960M = 12.586%
NetMargin_Component = clamp((12.586/30)×100, 0, 100) = 41.95

ROIC (TTM)           = $1,773.8M / $14,159M = 12.53%
ROIC_Component       = clamp((12.53/30)×100, 0, 100) = 41.77

Profitability_Score  = (41.95 + 41.77) / 2 = 41.86   (no FCF cap — FCF-positive every year on record)
```

### Margins (15% weight)

```
Gross Margin (TTM) = 76.56%
GrossMargin_Score = clamp((76.56/80)×100, 0, 100) = 95.70
```
No structural-trend bonus applicable — gross margin is already well above the 40% threshold the bonus targets (the bonus only applies to a margin *below* 40% that's expanding).

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $7.245B → FY2025 $13.278B) = 22.40%
Growth_Score = clamp((22.40/25)×100, 0, 100) = 89.60
```
**+10 (documented TAM expansion / pricing power, cited):**
- ServiceNow raised its Now Assist (AI product) 2026 ACV target from $1B to $1.5B and outlined a path to **$30B+ subscription revenue by 2030** (roughly double the current ~$15B run-rate) at its Investor Day (CEO Bill McDermott, May 2026 — Yahoo Finance/Verdantix coverage).
- Q1 2026: the number of customers spending **$1M+ on Now Assist grew over 130% YoY**; deals with 3+ Now Assist products rose ~70% YoY (company-disclosed, Q1 FY2026 earnings).
- FY2026 subscription revenue guidance raised to $15.735–$15.775B (+20.5–21% YoY) — an upward, not downward, revision.

Real, cited, company-disclosed evidence of market/product-line expansion.
```
Growth_Score (with bonus) = clamp(89.60 + 10, 0, 100) = 99.60
```
No decelerating-growth evidence exists (guidance was raised, not cut) — no −10 applies.

### Balance Sheet (15% weight)

```
Net Debt/EBITDA = −0.849× (net cash)
BalanceSheet_Score = clamp(100×(1 − (−0.849)/4), 0, 100) = clamp(121.2, 0, 100) = 100.0
```
Standard /4 denominator applies — NOW is not a payment network/exchange, the Upgrade 5 asset-light override doesn't apply (and isn't needed regardless, given the net-cash position).

### Moat Signal (15% weight) — checklist, cited evidence per signal

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | ServiceNow ranked **No. 1 in six segments** of Gartner's 2024 Market Share report; named the **only** vendor as a Leader in Gartner's 2025 Magic Quadrant for AI Applications in ITSM (2nd consecutive year as a Leader, 1st as sole Leader); a Leader in the ITSM Tools Magic Quadrant for **9 consecutive years**. Multiple independent, cited, current data points all pointing the same direction. |
| Brand premium | **TRUE** | Documented pricing power: standard contracts carry **3–7% annual price escalators** (some budgeted as high as 5–10%); the Now Assist AI add-on is priced **$15–75/user/month on top of** base ITSM licensing (~$70–200/user/month) — a genuine premium layer, not a discount — and adoption of that premium tier is *accelerating*, not shrinking (customers spending $1M+ on it grew >130% YoY, Q1 2026, per company disclosure). Sustained/expanding premium pricing with rising adoption, not a price cut to defend volume. |
| Network effect | **FALSE** | No documented two-sided-marketplace or user-growth-driven-value mechanism found for ServiceNow's core ITSM/workflow platform (an app-store/partner ecosystem exists but no cited mechanism ties platform value to cross-side user growth the way a marketplace does). Marked false for lacking the specific evidentiary type the checklist requires. |
| Switching costs | **TRUE** | Documented mechanism: the **CMDB (Configuration Management Database)** — ServiceNow's system of record for an enterprise's entire IT asset/application estate — is deeply embedded as the operational source of truth for IT service management workflows; migrating off it requires re-mapping and re-validating an organization's whole IT estate in a replacement system. A well-established structural switching-cost mechanism (same treatment as MSFT's identity-stack signal in the 2026-07-05 session), not requiring a fresh numeric citation. |
| Scale cost advantage | **FALSE** | No cost-per-unit data found showing a gap vs. smaller ITSM/workflow competitors (Ivanti, Freshservice, BMC Helix, etc.) — only revenue-scale and market-share citations were found, which are inputs, not the cost-per-unit *output* the checklist specifically requires. Marked false for lacking the precise evidentiary type, consistent with the rigor applied to MSFT's and NKE's own FALSE signals in recent sessions. |

```
Moat_Score = (3/5) × 100 = 60.0
```

**⚠️ This is a close call for the overall 80.0+ gate — shown transparently, "no black box":** if either the "Network Effect" or "Scale Cost Advantage" signal above were instead credited TRUE (4/5 = 80.0), the final Quality Score below would be **81.7** (passes the gate) instead of **78.7** (fails) — a swing of exactly +3.0 points from one additional moat signal. The gate result here is **not robust to this one judgment call**, mirroring the same-shape disclosure already made for MSFT (78.3 vs. 81.3) and AVGO (82.1, hinging on one signal) in the last two sessions.

### FCF Quality (10% weight)

```
FCF/NI (TTM) = $4,624M / $1,757M = 263.3%
FCFQuality_Score = clamp(((2.633 − 0.40)/0.60)×100, 0, 100) = clamp(372.2, 0, 100) = 100.0
```

### Quality Score — Final

```
Quality Score = (41.86×0.25) + (95.70×0.15) + (99.60×0.20) + (100.0×0.15) + (60.0×0.15) + (100.0×0.10)
              = 10.465 + 14.355 + 19.920 + 15.000 + 9.000 + 10.000
              = 78.740 → rounds to 78.7
```

# Quality Score = 78.7 — FAILS the 80.0+ gate (by 1.3 points; sensitivity to 81.7/PASS on one moat judgment call, see above).

**This is NOW's first-ever computed Quality Score.** Per [quality-scoring.md](../framework/quality-scoring.md): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all. Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* Per [rescore.md](../.claude/commands/rescore.md) step 3: *"a held position dropping below the gate is itself a signal worth surfacing, even though existing holdings aren't retroactively force-exited on quality alone."* **Neither rule forces an exit here** — quality-gate failure alone is not one of strategy.md's four valid Phase 06 exit reasons — but this is flagged as a **Phase 04 Quality Watch escalation**, the most significant new finding of this session. Per the established practice for existing holdings whose Quality Score fails the gate (see the AMZN/GOOG/MSFT/NKE 2026-07 sessions), the Valuation Score and a **reference-only** Composite Score are still computed below, explicitly flagged as not to be acted on at face value given the gate failure.

---

## 6. NOW — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 21.151 = 4.7278%
Spread = EY − 10Y Treasury = 4.7278% − 4.49% = +0.2378%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.2378%, ~1.26pp short) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.49% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for NOW = +10**

---

## 7. NOW — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 4.2172/10), 0, 100) = 57.828
```
→ Contribution: 57.828 × 0.40 = **23.131**

**EV/EBIT — 25% + 15% (PEG redistributed, §3 flag 1) = 40% weight**
```
EV/EBIT_Score = clamp((44.50 − 12)/23 × 100, 0, 100) = clamp(141.3, 0, 100) = 100.0
```
→ Contribution: 100.0 × 0.40 = **40.0**

**Forward PE (fallback formula — 5yr avg) — 20% weight**
```
Deviation% = (21.151 − 67.78)/67.78 × 100 = −68.80%
FwdPE_Score = clamp(50 + (−68.80)×2.5, 0, 100) = clamp(−122.0, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — 15% weight: N/A this session** (not a qualifying Fast Grower on a clean earnings base, §3 flag 1) — weight redistributed to EV/EBIT above.
*Sensitivity only (not scored):* trailing `yfinance` PEG = 21.151/20.53 (implied growth) ≈ **1.03** → would-be PEG_Score = clamp((1.03−0.5)/2.0×100) = **26.5**.

**Raw weighted score:**
```
= 23.131 + 40.0 + 0.0 = 63.131
```
**+ Rate Modifier (+10) = 73.131** (before the Upside/Downside Modifier)

---

## 8. NOW — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture carried forward from 06-20 (bull/base/bear EPS×exit-PE unchanged — no Rule 9 event to revise the underlying narrative; the Investor Day AI-ACV-target raise and Q1 Now Assist adoption data, both cited in §5's Growth bonus, support keeping rather than trimming the bull case, not inflating it further per Guardrail 2 — "never the rosy point"):**

| Scenario | Weight | EPS | Exit PE | Rationale | Fair Value |
|---|---|---|---|---|---|
| **Bull** | 25% | $5.40 | 28× | AI/Now Assist monetization re-accelerates (supported by the raised $1.5B ACV target and >130% YoY $1M+ customer growth); multiple re-rates modestly, still far below the 67.78× 5yr average and the $236 analyst high PT. | $5.40 × 28 = **$151.20** |
| **Base** | 50% | $5.03 | 22× | Consensus ~20% subscription grower (guidance 20.5–21%), PEG ~1.0; haircut multiple vs. the 5yr average to reflect the broader SaaS de-rating regime. | $5.03 × 22 = **$110.60** |
| **Bear** | 25% | $4.80 | 17× | Growth decelerates toward mid-teens; de-rating persists; still above the 52-week-low-implied multiple. | $4.80 × 17 = **$81.60** |

```
PW Fair Value = 0.25×151.20 + 0.50×110.60 + 0.25×81.60 = $113.50   (unchanged from 06-20)
```
Sits below the $141.12 analyst consensus mean — conservative, sanity check passes (Guardrail 2).

**Step 1 — Expected annual return E.**
```
Gap Upside %     = (113.50 ÷ 106.32) − 1                = +6.753%
Catalyst window  = 2 years (unchanged — Now Assist/AI-monetization ramp within Rule 10's 18–24mo window)
Annualized gap   = 6.753% ÷ 2                            = +3.377%
Intrinsic growth = +18%/yr   (unchanged, conservative — kept below the raised 20.5–21% subscription
                   guidance and the >100% YoY AI-ACV growth rate)
Shareholder yield = +0.48%   (refined this session, §3 flag 5 — net buyback, no dividend)

E = 3.377% + 18% + 0.48% = +21.857%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 21.857% ≥ H → M = −15 × clamp((21.857 − 10)/15, 0, 1) = −15 × clamp(0.7905, 0, 1) = −15 × 0.7905 = −11.857
```
**Modifier M = −11.857** — a materially smaller (less attractive) modifier than 06-20's floored −15.0: the price recovery (+11.87% since 06-20) narrowed the gap to an *unchanged* fair value, so the forward-looking case, while still attractive, is no longer at the bound.

**Guardrail checks:**
1. **Catalyst:** documented (Now Assist/AI-monetization ramp, FY2027 acceleration), within 18–24 months → upside credit allowed. ✓ (not binding here since M is on the attractive/negative side; guardrail 1 only caps the upside side, and M is well within [−15,+15] regardless.)
2. **Scenario-weighted, not the rosy point:** PW FV ($113.50) sits below the $141.12 analyst consensus mean; bear case underwritten near the current de-rated multiple range. ✓
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** −11.857 sits within bounds, off the floor this session. ✓

---

## 9. NOW — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (63.131) + Rate Modifier (+10) + Upside/Downside (−11.857)
                       = 61.274
```
Boundary rule: not a ".X5" case (61.274 is closer to 61.3 than 61.2 under ordinary rounding) → **Final Valuation Score = 61.3**

| | Value |
|---|---|
| Raw weighted | 63.131 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −11.857 (E = +21.857%) |
| **FINAL VALUATION SCORE** | **61.3** |
| Prior valuation score | 42.3 (06-20) |
| **Quality Score** | **78.7 (FAILS 80.0+ gate — see §5; sensitivity 81.7/PASS on one moat signal)** |

**Valuation Score band: 61.3 → 50.0–69.9 "Fair Value" → HOLD, watch only, no new entry, no trim** — this alone, on the raw Valuation Score, is already the operative action for an existing holding, independent of the Quality Score question.

**Composite Score — reference only, per the established practice for a Quality-Score-gate failure on an existing holding (AMZN/GOOG/MSFT/NKE 2026-07 sessions):**
```
Composite Score = 0.50×(100 − 78.7) + 0.50×61.3 = 0.50×21.3 + 0.50×61.3 = 10.65 + 30.65 = 41.3
```
**Composite Score = 41.3 — lands in the "BUY — Standard position 3–5%" band (30.0–49.9), a full band more attractive than the raw Valuation Score's own "Fair Value/Hold" band.** This is precisely the kind of **false green light this practice exists to flag**: blending in a failed-gate Quality Score (78.7, below 80.0) pulls the number down into a nominally-attractive band it would not occupy on valuation cheapness alone. **This Composite Score is NOT being adopted to drive the action recommendation below** — it is shown only for the record, per "no black box," exactly mirroring the MSFT 2026-07-05 and NKE 2026-07-01 treatment.

---

## 10. NOW — Action Recommendation

**Two independent facts, either one of which alone is enough to conclude HOLD/no-add:**

1. **The raw Valuation Score (61.3) sits in the 50.0–69.9 Fair Value/Hold band on its own terms** — no new entry, no trim, regardless of the Quality Score question. This is the base-case, non-controversial reading.
2. **The Composite Score's nominal Buy-Standard reading (41.3) independently fails the order-setup gate**, shown for completeness below — so even entertaining the false-green-light number does not change the conclusion.

**Order setup — shown for completeness, testing the Composite Score's nominal Buy-Standard (30.0–49.9) band:**
```
Blended Fair Value (= PW FV):              $113.50
Margin of Safety (30.0–49.9 band):         28%  (unchanged from 06-20)
BUY PRICE (limit):                         $113.50 × (1 − 0.28) = $81.72
PRIMARY SELL TARGET:                       $113.50
BULL-CASE TRIM TARGET (bull × 0.90):       $151.20 × 0.90 = $136.08
STOP LOSS (Buy × (1 − 28%)):               $81.72 × 0.72 = $58.84
R/R at formal entry = (113.50 − 81.72) ÷ (81.72 − 58.84) = 31.78 ÷ 22.88 = 1.389:1  ❌ below 2:1
R/R at live price   = (113.50 − 106.32) ÷ (106.32 − 58.84) = 7.18 ÷ 47.48 = 0.151:1  ❌ far below 2:1
```
**Both R/R checks fail the 2:1 minimum (Rule 6) — and the live-price R/R (0.151:1) is materially worse than 06-20's 0.51:1**, because price rose toward the unchanged fair value without the stop distance narrowing proportionally. **Per Rule 6, R/R below 2:1 = do not enter**, independent of score band or the Quality Score question.

**Net: HOLD the existing 2.16% position. No fresh capital added — the same practical conclusion as 06-20, now reinforced by (a) the score's own return to the Hold band, (b) an R/R check that has gotten worse, not better, and (c) a new, independent Quality Watch flag.**

**Position cap check:** 2.16% is nowhere near the 15% hard cap (Upgrade 7) — not a binding constraint here (unlike MSFT), included only for completeness.

**Quality Watch escalation (Phase 04, new this session):** NOW's first-ever computed Quality Score (78.7) fails the 80.0+ gate, narrowly and on a result sensitive to one moat judgment call (§5). This does not meet the Full Exit bar (Phase 06 requires *sustained* fundamental deterioration or one of the other three specific triggers — none apply; the underlying business (76.6% gross margin, 22.4% revenue CAGR, net-cash balance sheet, raised AI guidance) shows no deterioration at all; the gate failure here is a **quality-scoring-methodology outcome** — driven by modest GAAP profitability/ROIC relative to the strict 80.0+ bar and an incomplete moat checklist — not a sign the business itself has gotten worse). Recommend the user consider whether to log a **Human Override** entry in [override-log.md](../portfolio/override-log.md) (mirroring the ZS precedent for a held, quality-gate-failing position) — flagged here as an open item, not decided or written by this session (out of scope; `override-log.md` is not edited here).

---

## 11. Next Review Trigger

- **Routine:** NOW Q2 FY2026 earnings, confirmed **22 Jul 2026, after close** — will refresh every TTM fundamental used here and is the natural point to re-run the Quality Score with a fresh TTM window.
- **Open item (new, highest priority): the Quality Score gate question (§5).** Either (a) obtain a harder, NOW-specific cost-per-unit citation for "scale cost advantage" or a documented two-sided-marketplace mechanism for "network effect" to settle the 78.7-vs-81.7 ambiguity, or (b) accept the primary 78.7 determination and decide whether to log a Human Override for this position (§10).
- **Open methodology item (unresolved, flagged not fixed):** the primary-vs-fallback Forward PE formula ambiguity when the automated `get_earnings_dates` method technically returns both an average and a range (§3 flag 2) — affects NOW, MSFT, NKE and others; worth a dedicated `decisions/` entry.
- **Watch:** if price continues recovering toward the $113.50 PW Fair Value without a fundamental change, the Upside/Downside Modifier will keep shrinking and the raw Valuation Score will keep drifting further into the Hold band; re-derive at the 22 Jul earnings print regardless.
- **Rule 9 triggers (standing):** guidance revision, M&A, management change, a >15% unexplained price move, or the 22 Jul earnings print itself.

---

## Glossary

| Term | Meaning |
|---|---|
| **ACV (Annual Contract Value)** | The annualized value of a signed customer contract at signing — a forward-looking bookings metric, distinct from ARR. ServiceNow's Now Assist product raised its 2026 ACV target from $1B to $1.5B. |
| **ARR (Annual Recurring Revenue)** | The annualized run-rate value of a subscription business's contracted revenue at a point in time. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **CMDB (Configuration Management Database)** | ServiceNow's system of record cataloging an organization's IT assets/applications and their interdependencies — the switching-cost mechanism cited in the Moat Signal checklist. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate; shown as a **reference-only, not-adopted** number for NOW this session (78.7 Quality Score fails the gate). |
| **D&A** | Depreciation & Amortization. |
| **Deferred tax valuation allowance release** | A one-off GAAP accounting event reversing a prior write-down on deferred tax assets once a company judges them likely usable — inflates net income/EPS in the recognition period. Identified as the likely driver of NOW's anomalous FY2023 EPS jump (§3 flag 1). |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — this framework's PEG-eligibility trigger; NOW does not qualify this session (§3 flag 1). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. |
| **Human Override** | A position held outside the framework's own rules — tracked in `override-log.md`; flagged (not adopted) as an open item for NOW this session. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt; negative means net cash. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **NTM** | Next Twelve Months. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. NOW's first-ever computation this session: 78.7 (fails the gate), sensitivity 81.7. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; require a minimum 2:1 risk/reward before entering; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **SaaS (Software-as-a-Service)** | A software delivery model where customers pay a recurring subscription to access hosted software. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

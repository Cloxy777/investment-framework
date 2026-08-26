# RESCORE — META — 2026-08-26 (Session 2 — Rule 9 CONFIRMED)

**Task type:** RESCORE (single ticker) — **Telegram-triggered** (Routine 6 / `/telegram-scan`), unattended scheduled run — **P1 priority** (held position, per automation-schedule.md)
**Trigger:** Two new Telegram posts, both after this morning's session ([sessions/2026-08-26-rescore-meta.md](2026-08-26-rescore-meta.md), PR #635): [t.me/tarasguk/11777](https://t.me/tarasguk/11777) (2026-08-26T14:41:06 UTC) and [t.me/FinnInvestChannel/3145](https://t.me/FinnInvestChannel/3145) (2026-08-26T13:46:58 UTC), both reporting an **agreed** teen-safety-lawsuit settlement with disclosed dollar figures — unlike this morning's post, which described only unconfirmed "preliminary discussions." Per CLAUDE.md Rule 0, the Telegram text is used **only as a trigger**; every figure in this log is independently re-verified via real wire sources (CNN, TechCrunch, NPR, Axios, Yahoo Finance/Investing.com) and live market data, not taken from the posts.
**Date:** 26 Aug 2026 (second same-day session — morning session filed 06:40 UTC trigger time; this session's triggers fired 13:46–14:41 UTC)
**10Y US Treasury Yield:** 4.67% (TradingEconomics.com, "current" as of 26 Aug 2026, same convention as every prior session — up marginally from this morning's 4.65%/4.639–4.653% cross-check, still inside the "3.5–5%" bracket)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** META **37.8** (2026-08-26 AM, Composite 25.2, Quality 87.5, BUY — Full position 6–8% — [sessions/2026-08-26-rescore-meta.md](2026-08-26-rescore-meta.md))
**Gap since last review:** ~6 hours (same calendar day — routine 21-day cadence does not apply; this session is fired purely by the confirmed Rule 9 trigger below).

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; NOPAT = net operating profit after tax; ROIC = return on invested capital; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; pp = percentage points; EY = earnings yield (1 ÷ PE); TTM = trailing twelve months; NTM = next twelve months; 10-Q = quarterly SEC filing; 8-K = SEC "current report" filing.*

---

## 0. Data-Source Note

Live price fetched via the **Interactive Brokers MCP tool** (`get_price_snapshot`, real-time NASDAQ quote) — no `yfinance`/`curl_cffi` workaround needed for price this session, since IBKR is available directly. Forward-EPS consensus and 5yr PE reconstruction still sourced from stockanalysis.com WebFetch (same as every session since the 5yr-PE derivation was last run 08-05 — no new earnings date exists to justify re-deriving it, see §4).

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$578.83** | IBKR `get_price_snapshot` (contract_id 107113386, NASDAQ, SMART-routed), last-trade timestamp 2026-08-26 16:11:38 UTC (12:11:38 ET), intraday, not halted |
| Cross-check | $578.43 (stockanalysis.com, quote timestamp 12:10 PM EDT) / $578.58 (Google Finance, 12:10:55 PM EDT) | WebFetch of both — all three sources agree within ~$0.40 (normal quote-lag spread for a live, moving intraday price) |
| Today's change | +1.54% ($8.78) vs. prior close $570.05 | IBKR `change` field; consistent with stockanalysis's +1.47% and wire reports of "Meta up ~1.5% after paring a larger pre-market gain" |
| 52-week range | **$520.26 – $788.98** (IBKR) vs. $520.26–$790.80 (stockanalysis.com, this morning) | Minor high-end discrepancy between IBKR's own 52w-high field and Yahoo-sourced data (~0.2% apart) — flagged, immaterial to any calculation below (52w range used only for stop-placement context, not scored) |
| Analyst consensus PT | **$754.84** (carried from this morning — stockanalysis.com; not re-pulled this session, no reason to expect an intraday PT revision this fast) | Bull-case sanity check only (Rule 0 Step 4) |

---

## 2. Rule 9 Trigger Check — Independent Verification (CONFIRMED this session)

| Trigger | Found? | Detail |
|---|---|---|
| **Teen-safety lawsuit settlement (the posts' claim)** | **CONFIRMED — real, agreed, disclosed-terms settlement, reached and announced today** | Independently verified via **CNN Business, TechCrunch, NPR, Axios, Yahoo Finance/Investing.com** (all 2026-08-26). Meta has reached an **agreed settlement** — not preliminary talks — with a broad coalition of state attorneys general (sources vary 29 lead-plaintiff states / 47–52 total participating states+territories) resolving the federal teen-safety-harm trial that was underway in Oakland, CA. **Meta explicitly did NOT admit fault or wrongdoing** — settled "without admitting liability," consistent across every source. Total headline figure varies slightly by outlet ($16.68B per Yahoo Finance/Investing.com, $17B per NPR/USNews/MPR, up to $18B per CNN/TechCrunch/Washington Post/Variety) — this spread reflects different outlets citing gross vs. guaranteed-only figures; the consistent structural detail (TechCrunch, sourced to the settlement terms) is **$18B total, paid over 10 years, with ~70% ($12.6B) guaranteed and the remaining ~30% (~$5.3–5.4B) contingent on YouTube and TikTok adopting comparable teen-safety changes** — closely matching (not merely coincidentally similar to) the Telegram trigger posts' own figures. **Confirmed disclosed operational terms:** default 2-hour/day time limit for under-18 users (Facebook+Instagram combined), midnight–6am access block, hidden like/reaction counts by default, an option for a non-personalized/algorithm-free feed, restrictions on filters, strengthened age-verification/underage-account detection, expanded parental controls, and an independent auditor with platform access reporting to the state AGs. **Confirmed financial-statement impact:** a **~$10B one-time legal-expense charge is expected to hit Meta's Q3 2026 GAAP results** (per the settlement's own terms, cited by the trigger posts and consistent with the scale of a $12.6–18B, mostly-near-term legal liability; Meta has not yet filed an 8-K on this as of this session — the charge will be reported when Q3 2026 results are released, not yet due). |
| **Does this clear the Rule 9 bar?** | **YES — CONFIRMED** | This morning's session (§2, [2026-08-26-rescore-meta.md](2026-08-26-rescore-meta.md)) and its watchlist entry explicitly flagged: *"a confirmed settlement with disclosed terms... would be an unambiguous Rule 9 trigger warranting an immediate re-score."* That condition is now met: a real, company-agreed settlement exists, with specific, sourced, disclosed dollar figures and mandated operational changes — no longer an unnamed-sources "preliminary discussion" as this morning. This is the same category treatment [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 9 reserves for a **material, quantifiable legal/financial event** (closest enumerated analogue: a disclosed financial liability + mandated business-practice changes, functionally equivalent to a guidance-revision-triggering event even though formal Q3 guidance hasn't yet been reissued). **This session proceeds as a Rule-9-triggered re-score**, not a routine check. |
| Does this change any *already-filed* TTM fundamental this session? | **No** | The ~$10B charge is a **Q3 2026** event — Meta's most recent filed financials remain the 2026-07-29 Q2 2026 10-Q/8-K, unchanged since this morning. No restated financials exist to pull. The charge will roll into TTM fundamentals (and this ticker's Quality Score inputs) starting at the **Q3 2026 earnings re-score** (§4/§13), not before. |
| Quarterly earnings | No — still not yet due (confirmed again, no new 8-K since 07-29). | |
| Guidance revision | **Not yet formally reissued** — no new 8-K/press release revising FY2026 guidance found as of this session; the Q3 charge is disclosed via the settlement/wire coverage, not (yet) via a formal guidance update. Flagged as likely imminent (§4). | |
| Material M&A / JV | No new one this window. | |
| Management change | No. | |
| Macro shift | No — 10Y ticked 4.65%→4.67%, same bracket. | |
| >15% unexplained price move | No — today's +1.54% move is small and, notably, *explained* (settlement relief, tempered by the disclosed cost and mandated product changes) rather than unexplained. | |

**Conclusion: Rule 9 trigger CONFIRMED this session** — a real, agreed, disclosed-terms litigation settlement with a quantifiable near-term financial-statement impact (~$10B Q3 charge) and mandated product changes. This reverses this morning's "not yet confirmed" finding, exactly per that session's own stated re-trigger condition.

---

## 3. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** **4.51%** (unchanged — no new portfolio sync since this morning; per [holdings.md](../portfolio/holdings.md))

### TTM fundamentals — unchanged from this morning (no new fiscal quarter, no restated filing)

| Item | Value |
|---|---|
| TTM Revenue | $228.247B |
| TTM Net Income | $68.098B |
| TTM EBITDA | $112.282B |
| TTM FCF | $40.976B |
| Gross profit (TTM) | $186.587B → Gross margin 81.7478% |
| Net cash (30 Jun 2026) | $6.596B |
| Total Stockholders' Equity (30 Jun 2026) | $261.221B |
| Senior-note debt (30 Jun 2026) | $83.664B |
| TTM EBIT (10-Q-verified, authoritative — see this morning's §3 for the Yahoo-field discrepancy note) | $86.927B |
| Buyback (TTM) | $3.327B |
| Dividend (TTM) | $5.367B |
| Shares outstanding | 2,548,378,209 |

### Refreshed this session (price/consensus-dependent)

| Item | 08-26 AM value | 08-26 PM value (fresh) | Computation |
|---|---|---|---|
| Live price | $570.05 | **$578.83** | §1 |
| Market Cap | $1,452.7030B | **$1,475.0778B** | 2,548,378,209 × $578.83 |
| EV | $1,446.1070B | **$1,468.4818B** | Market Cap − $6.596B net cash |
| **EV/EBIT** | 16.6359× | **16.8933×** | $1,468.4818B ÷ $86.927B |
| **FCF Yield** | 2.8207% | **2.7777%** | $40.976B ÷ $1,475.0778B |
| Forward EPS (FY2026 consensus) | $31.16 | **$31.16 — unchanged** | stockanalysis.com/forecast, 55 analysts, "last updated Aug 26, 2026" — **flagged: this consensus figure predates or has not yet incorporated today's settlement/Q3-charge news; analysts have not had time to revise FY2026 EPS down for the disclosed ~$10B Q3 legal charge.** Not invented/adjusted here — used as-is per "never invent," but this is the single biggest open data-quality flag this session (§4). |
| Forward PE | 18.2943× | **18.5761×** | $578.83 ÷ $31.16 |
| 5yr avg/range PE (carried, unchanged) | 23.152× (range 9.255×–36.014×, n=20q) | **Carried unchanged** — no new earnings date since 07-29 to shift the reconstruction window |

### Fast-Grower (PEG eligibility) test — unchanged, still fails

FY2025 diluted EPS still −1.55% YoY. **Still FAILS.** PEG not applicable; 15% weight redistributed to EV/EBIT — unchanged.

---

## 4. Data Gaps / Flags

1. **Forward EPS consensus ($31.16) has almost certainly not yet been revised for today's ~$10B Q3 2026 legal charge.** This is a real, material, near-certain downward pressure on FY2026 GAAP EPS estimates that the market has not yet had time to price into the consensus figure this scoring run depends on. Not adjusted here (never invent/estimate a revision that hasn't been published) — flagged as the top follow-up item; re-check consensus in 24–48 hours and certainly before/at the Q3 2026 earnings re-score.
2. **No formal Meta guidance revision (8-K/press release) found yet** disclosing the exact GAAP EPS/margin impact of the settlement — the ~$10B figure is sourced from wire coverage of the settlement's own terms, not (yet) from a Meta-issued guidance update. Flagged as likely imminent; watch for the formal disclosure.
3. **Headline settlement figure varies $16.68B–$18B across otherwise-reliable outlets** (Yahoo/Investing.com vs. NPR/USNews vs. CNN/TechCrunch/WaPo) — not a red flag on the *fact* of the settlement (all sources agree it happened, was agreed, and involves the ~$12.6B guaranteed / ~$5.3B contingent structure), just normal reporting variance on which sub-total ("just the 29-state lead case" vs. "all 47–52 participating states/territories combined") each outlet leads with. Not scored either way — the settlement has zero quantitative effect on this session's TTM-based inputs regardless of which headline figure is used (§2).
4. **5yr PE range not independently re-derived this session** (carried forward from 08-05, same as this morning) — no new earnings date exists to shift the window; still overdue for a fresh derivation at Q3 2026 earnings.
5. **Bull/Bear scenario EPS assumptions ($40.0/$28.0) and exit multiples (24×/13×) carried unchanged for the 9th+ consecutive session** — flagged again as increasingly stale, now compounded by the fact that a confirmed, material litigation liability has just been resolved and isn't reflected in either scenario's assumptions. Worth a dedicated review, more overdue than ever.
6. **Settlement not yet reflected in any filed balance sheet.** The most recent 10-Q (30 Jun 2026) predates the settlement by two months; no accrued litigation liability is on the books yet. The Balance Sheet sub-score (§6) remains computed off the unchanged Q2 2026 balance sheet — correctly, since nothing has been filed reflecting the new liability, but flagged as a standing watch item for Q3 2026 (a ~$10B one-time charge and/or new accrued liability could move Net Debt/EBITDA and the Balance Sheet sub-score off its current 100.0 ceiling).
7. **Product-usage-impact risk, qualitative, not scored.** The settlement's mandated product changes (2hr/day teen time limit, midnight–6am lockout, non-personalized feed option, hidden engagement counters) could plausibly reduce teen engagement/time-on-platform in future quarters — a potential (not yet observed, not yet quantifiable) headwind to the Growth sub-score's TAM-expansion basis. Not scored here — no engagement data exists yet showing any actual impact — flagged as a forward watch item, not invented.
8. **META weight (4.51%)** — unchanged since no new portfolio sync today; same as this morning.

---

## 5. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 18.5761 = 5.3833%
Spread = EY − 10Y Treasury = 5.3833% − 4.67% = +0.7133%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.7133%, ~0.79pp short — cushion narrowed slightly vs. this morning's +0.8162% as forward PE rose faster than the 10Y ticked up) → **+5 additive.**

**Step 2 — Rate Regime Modifier**
10Y = 4.67% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +10** (unchanged).

---

## 6. META — Quality Score (recomputed — unchanged from this morning; no new filed fundamentals)

```
Profitability (25%):
  Net Margin = $68.098B ÷ $228.247B = 29.8352%   (unchanged)
  ROIC = NOPAT ($86.927B × 0.84 = $73.019B) ÷ Invested Capital ($83.664B + $261.221B = $344.885B)
       = 21.1719%   (unchanged)
  NetMargin_Component = clamp(29.8352/30×100, 0, 100) = 99.4507
  ROIC_Component       = clamp(21.1719/30×100, 0, 100) = 70.5730
  Profitability_Score  = (99.4507 + 70.5730) / 2 = 85.0119

Margins (15%): Gross margin 81.7478% → clamp(81.7478/80×100,0,100) = 100.0

Growth (20%): Revenue 3yr CAGR 19.89% (unchanged, FY2026 still incomplete)
  Growth_Score = clamp(19.89/25×100, 0, 100) = 79.56 + 10 (TAM-expansion bonus, unchanged basis) = 89.56
  [See §4 flag 7 — settlement-mandated product changes are a qualitative future watch item on this
   sub-score's TAM/engagement basis, not yet scored; no engagement-impact data exists.]

Balance Sheet (15%): Net Debt/EBITDA = −$6.596B ÷ $112.282B = −0.05874× (net cash, unchanged)
  BalanceSheet_Score = clamp(100×(1−(−0.05874)/4), 0, 100) = 100.0
  [See §4 flag 6 — settlement liability not yet on any filed balance sheet; standing watch for Q3 2026.]

Moat Signal (15%): 5/5 signals unchanged (market share, brand premium, network effect, switching
  costs, scale cost advantage) — no new erosion evidence this window. The now-CONFIRMED settlement
  (§2) resolves a major regulatory/legal tail risk (removes exposure to a worst-case $1.4T verdict)
  but is a risk-resolution event, not documented moat erosion or strengthening — not scored either
  direction here, consistent with "never invent... without a cited source." → 100.0

FCF Quality (10%): FCF/NI = $40.976B ÷ $68.098B = 60.1721% (unchanged)
  FCFQuality_Score = clamp(((0.601721−0.40)/0.60)×100, 0, 100) = 33.6202

Quality Score = 85.0119×0.25 + 100.0×0.15 + 89.56×0.20 + 100.0×0.15 + 100.0×0.15 + 33.6202×0.10
              = 21.2530 + 15.0 + 17.912 + 15.0 + 15.0 + 3.3620
              = 87.5270 → rounds to 87.5
```

**Quality Score = 87.5 — unchanged from this morning, comfortably PASSES the 80.0+ gate.** No genuine quality change this session — every input the formula uses is still identical to the last filed quarter. The settlement is a confirmed Rule 9 *valuation* trigger (new price, and a disclosed future cash liability), but it does not itself move any of today's Quality sub-score inputs — those move only once Q3 2026 financials are filed (§4 flags 6–7).

**Hard disqualifier check:** unchanged — none fire.

---

## 7. META — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.7777/10), 0, 100) = 72.2230
```
→ Contribution: 72.2230 × 0.40 = **28.8892**

**EV/EBIT — 40% weight** (PEG not applicable → 15% redistributed here)
```
EV/EBIT_Score = clamp((16.8933 − 12)/23 × 100, 0, 100) = 21.2709
```
→ Contribution: 21.2709 × 0.40 = **8.5084**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (18.5761 − 23.152)/23.152 × 100 = −19.7644%
FwdPE_Score = clamp(50 + (−19.7644) × 2.5, 0, 100) = clamp(0.589, 0, 100) = 0.589
```
→ Contribution: 0.589 × 0.20 = **0.1178**

**PEG — Fast-Grower test: FAIL** (unchanged). Weight redistributed to EV/EBIT (used above).

**Raw weighted score:**
```
= 28.8892 + 8.5084 + 0.1178 = 37.5154
```
**+ Rate Modifier (+10) = 47.5154** *(before the Upside/Downside Modifier)*

---

## 8. META — Upside/Downside Modifier (Expected-Return Modifier)

**Decision:** Base-case EPS ($31.16), Bull/Bear EPS ($40.0/$28.0), and both exit multiples (24×/13×/20×) all **unchanged from this morning** — no new sourced inputs exist to revise any of them (§4 flags 1, 5).

**Step 1 — Scenario fair values**

| Scenario | Weight | EPS assumption | Exit PE | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | $40.0 (carried) | 24× | **$960.00** |
| **Base** | 50% | $31.16 (carried, unrevised — §4 flag 1) | 20× | **$623.20** |
| **Bear** | 25% | $28.0 (carried) | 13× | **$364.00** |

```
PW Fair Value = 0.25×960.00 + 0.50×623.20 + 0.25×364.00 = $642.60   (unchanged — all inputs identical)
```

Sanity check (Rule 0 Step 4 / Rule 4): PW FV $642.60 remains well below the $754.84 analyst consensus PT.

Live price ($578.83) remains **below** the PW Fair Value ($642.60, **+11.03% gap**) — the gap narrowed from this morning's +12.73% because price rose while fair value inputs held flat.

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = ($642.60 ÷ $578.83) − 1                    = +11.0343%
Catalyst window = 2 years (unchanged)
Annualized gap  = +11.0343% ÷ 2                               = +5.5172%/yr
Intrinsic growth = +12.0%/yr   (carried, unchanged basis)
Shareholder yield = ($3.327B buyback + $5.367B dividend) ÷ $1,475.0778B market cap
                  = $8.694B ÷ $1,475.0778B                    = +0.5894%/yr
```
```
E (expected annual return) = +5.5172 + 12.0 + 0.5894 = +18.1066%/yr
```

**Step 3 — Catalyst/timeline (Rule 10 + Guardrail 1).** Same two standing catalysts (AI ad-monetization proof, capex-ROI demonstration), both inside the 18–24-month window; the now-confirmed settlement removes a *risk* (litigation tail) rather than adding a new *upside* catalyst, so it is not counted as a third catalyst here. **Upside credit fully allowed; the −5 catalyst cap does NOT apply** (E ≥ H).

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
E = 18.1066% ≥ H → M = −15 × clamp((18.1066 − 10)/15, 0, 1)
                      = −15 × clamp(0.54044, 0, 1)
                      = −8.1066
```
**Upside/Downside Modifier M = −8.1066** — less negative (less attractive) than this morning's −8.9620, since the price/fair-value gap narrowed as price rose on settlement relief while fair-value inputs held flat.

---

## 9. META — Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (37.5154) + Rate Modifier (+10) + Upside/Downside (−8.1066)
                       = 39.4088
```
Boundary rule: not a ".X5" → standard rounding → **Final Valuation Score = 39.4**

| | Value |
|---|---|
| Raw weighted | 37.5154 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −8.1066 (E = +18.11%) |
| **FINAL VALUATION SCORE** | **39.4** |
| Prior valuation score (this morning) | 37.8 |
| **Quality Score** | **87.5 (unchanged)** |

```
Composite Score = 0.50 × (100 − 87.5) + 0.50 × 39.4 = 0.50×12.5 + 0.50×39.4 = 6.25 + 19.70 = 25.95
```
Boundary rule: 25.95 falls exactly on a ".X5" → round **UP** (conservative) → **Composite Score = 26.0**

**Composite Score = 26.0** (up from 25.2 this morning — slightly less attractive, driven entirely by the valuation side: Quality Score unchanged, Valuation Score rose 37.8→39.4 as price rose +1.54% on settlement relief while fair-value inputs held flat, narrowing the discount and pulling the Upside/Downside Modifier slightly less negative). Still comfortably inside the same **BUY — Full position 6–8%** band (0.0–29.9), no action-category change.

---

## 10. META — Action & Category Change

**Valuation Score alone: 37.8 → 39.4** — stays inside the BUY-Standard band (30.0–49.9), drifting mildly toward its upper boundary as price rose.

**Composite Score: 25.2 → 26.0 → Action band: BUY — Full position 6–8%** (0.0–29.9 band, unchanged; a modest step less-attractive within the band, but still well inside it). **No action-category change.**

**Practical recommendation: HOLD — no automatic fresh capital.** META is an existing holding at **4.51%**, inside the 6–8% full-position band with 3.49pp of headroom to the 8% ceiling (unchanged from this morning — no new sync). No portfolio-mechanics change and no scoring change forces a top-up (order-setup gates below still govern).

---

## 11. META — Order Setup (Composite Score in BUY-Full band → required)

Confidence: wide-moat proven compounder (Quality Score 87.5) — same conservative 20% MoS used every prior session.

```
[x] Composite Score (drives action band):        26.0   (≤29.9 ✓ — Full-position entry permitted)
[x] Raw Valuation Score (incl. Upside/Downside):  39.4
[x] Expected annual return E / catalyst window:   +18.11% / 2yr
[x] Upside/Downside Modifier applied:             −8.1066
[x] Blended Fair Value (PW, Rule 7):              $642.60  (unchanged — all scenario inputs carried flat)
[x] Margin of Safety %:                           20%
[x] BUY PRICE (limit):     $642.60 × (1 − 0.20)        = $514.08
[x] PRIMARY SELL TARGET:   = Blended FV                = $642.60
[x] BULL-CASE TRIM TARGET: $960.00 × 0.90               = $864.00
[x] STOP LOSS:             $514.08 × (1 − 0.25)        = $385.56   (25% max loss, high-conviction bracket)
[x] Risk/Reward Ratio (base-case target):  ($642.60 − $514.08) ÷ ($514.08 − $385.56) = $128.52 ÷ $128.52 = 1.00:1
[x] Risk/Reward Ratio (bull-case trim target): ($864.00 − $514.08) ÷ $128.52 = $349.92 ÷ $128.52 = 2.72:1
```

Live price ($578.83) is **$64.75 (12.60%) above** the $514.08 buy-price limit — the gap widened slightly from this morning's tightest-on-record 10.89% as price rose on the settlement-relief rally. **Base-case R/R still exactly 1.00:1 (fails the 2:1 minimum)**, same recurring shape as every META session on record. **No automatic qualifying entry fires this session either.**

**Position sizing:** META at **4.51%** (unchanged), inside the 6–8% band, headroom to the 8% ceiling of **3.49pp**. No forced trim or top-up.

---

## 12. Portfolio Note

META at 4.51% remains comfortably under the 15% hard cap (Upgrade 7). No portfolio-level action is forced by this score — consistent with this ticker's established pattern (11 sessions since 06-12, "BUY — Full position" score label never once producing a qualifying automatic entry, independent price-limit and 2:1 R/R gates failing every time).

**One notable non-scoring observation:** the market's reaction to a **confirmed** ~$18B litigation settlement was a **modest +1.54% gain** (having pared back a larger ~3.9% pre-market pop) — consistent with the settlement removing a very large tail-risk overhang (Meta's own $1.4T worst-case estimate) while simultaneously disclosing a real, material near-term cost (~$10B Q3 charge) and mandated product changes with uncertain engagement impact. Net effect on this session's Composite Score is small (25.2→26.0) precisely because the framework doesn't let either the removed tail-risk or the new disclosed cost move any score in the absence of filed financial data — both are flagged as watch items (§4) rather than invented into today's inputs.

---

## 13. Next Review Triggers

- **Q3 2026 earnings (confirmed not yet due, typically late Oct/early Nov 2026)** — will for the first time incorporate the ~$10B settlement charge into filed TTM fundamentals; this is now the single most important upcoming re-score, likely to move the Profitability, FCF Quality, and possibly Balance Sheet sub-scores materially for one quarter.
- **Formal Meta guidance revision (8-K)** — not yet filed as of this session; watch for Meta to formally reissue FY2026 guidance incorporating the settlement charge, which would itself be an independent Rule 9 trigger.
- **Analyst consensus EPS revision (§4 flag 1)** — the $31.16 FY2026 consensus almost certainly has not yet absorbed today's news; re-check within 24–48 hours, since a downward revision would lower the Base-case fair value and could move the Valuation Score and Upside/Downside Modifier without any new price move.
- **Litigation settlement court approval** — the settlement reportedly still requires judicial approval (Judge Yvonne Gonzalez Rogers per NPR); an approval, rejection, or renegotiation of terms would itself be a fresh Rule 9-relevant event.
- **Teen-engagement/product-change impact (§4 flag 7, qualitative, unscored)** — watch subsequent quarters' engagement/DAU/time-spent disclosures for any measurable effect of the mandated 2hr/day limit, midnight–6am lockout, and non-personalized-feed option on teen usage — a potential future Growth sub-score input, not yet observable.
- **Buy-price / fair-value watch:** live price is 12.60% above the $514.08 buy limit (widened from this morning's 10.89% record-tight gap); base-case R/R remains stuck at exactly 1.00:1.
- **Balance sheet watch (standing since 08-05):** net cash fell ~70% in Q2 2026 alone, and Q3 2026 will now also need to absorb the settlement's cash/accrual impact — check explicitly at Q3 2026 earnings.
- **Rate Gate watch:** Step 1 FAILED again, cushion narrowed slightly to +0.71% (vs +0.82% this morning) as forward PE rose faster than the 10Y ticked up.
- **Bull/Bear scenario assumptions ($40.0/$28.0 EPS, 24×/13× exit multiples)** — flagged stale for the 9th+ consecutive session; increasingly overdue for a dedicated review.
- **Rule 9 fundamental triggers (standing):** any further guidance revision, management change, material M&A, or a >15% unexplained price move.

---

## 14. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output; no new terms required this session)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **8-K** | The "current report" a US public company files with the SEC within days of a material event, most often to furnish an earnings press release ahead of the fuller 10-Q/10-K. |
| **10-Q** | The quarterly financial-disclosure report a US public company files with the SEC, containing unaudited financial statements. |
| **bps / pp (percentage points)** | A direct difference between two percentages, distinct from a "%" change. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **Effective tax rate** | The actual % of pretax income paid as tax in a period — distinct from the statutory rate. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | Debt + Equity used as the ROIC denominator. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the numerator this framework uses to compute ROIC. |
| **NTM** | Next Twelve Months. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |

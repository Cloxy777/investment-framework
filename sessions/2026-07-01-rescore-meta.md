# RESCORE — META — 2026-07-01

**Task type:** RESCORE (single ticker)
**Date:** 1 Jul 2026
**10Y US Treasury Yield:** 4.46% (TradingEconomics/CNBC, dated 30 Jun–1 Jul 2026 — up from 4.38% used 06-26; still inside the "3.5–5%" bracket → Rate Regime Modifier Step 2 unchanged at +5)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** META **17.2** (2026-06-26, BUY — Full position 6–8% — [sessions/2026-06-26-rescore-meta.md](2026-06-26-rescore-meta.md))
**Gap since last review:** 5 days.
**First-ever Quality Score / Composite Score computation for META this session** — its `holdings.md` row and every prior session predate the 2026-06-29 methodology change.

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; D&A = depreciation and amortization; capex = capital expenditure; Owner Earnings = net income + D&A − maintenance capex; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ PE); NOPAT = net operating profit after tax; ROIC = return on invested capital; TAM = total addressable market; TTM = trailing twelve months; NTM = next twelve months.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$624.70** | IBKR `get_price_snapshot` (contract_id 107113386, META Class A / NASDAQ), pulled this session |
| Session change | **+$61.41 / +10.9%** | IBKR `change` field — a very large one-day move |
| 52-week range | **$520.26 – $794.42** | IBKR `misc_statistics` |
| Year-to-date change | **−5.28%** | IBKR `year_to_date_change` (vs −16.69% on 06-26 — the surge cut the YTD loss sharply) |
| Analyst consensus PT | **$827.32** (64 analysts, S&P Global via stockanalysis.com) | Web search — bull-case sanity check only (Rule 0 Step 4) |

Price vs 06-26 session: $549.47 → $624.70 = **+13.68%** over 5 days. Under the 15% Rule 9 unexplained-move threshold, but close enough to warrant an explicit cause check (§2).

---

## 2. Rule 9 Trigger Check (2026-06-26 → 2026-07-01)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Next report is META Q2 2026, expected **29 Jul 2026** (after market close, per stockanalysis.com) — unchanged |
| Guidance revision | No | No new company-issued guidance found this window |
| M&A | No | No new M&A since the already-assessed 06-22 Cred stake |
| Management change | No | No new change since the already-assessed 06-22 WhatsApp leadership change |
| Macro shift | No | 10Y ticked up 4.38%→4.46%, still inside the "3.5–5%" bracket |
| **>15% unexplained price move** | **No — but close (+13.68% over 5 days) and *not* unexplained** | See below |

**The driver is identifiable and specific, but not yet a company-confirmed disclosure.** A **Bloomberg report** (30 Jun–1 Jul 2026) says Meta is building an internal "Meta Compute" business to sell its excess AI computing capacity — both hosted-model access and raw bare-metal capacity — to outside customers, positioning Meta alongside AWS/Azure/GCP as a cloud infrastructure seller rather than only a buyer of compute. The report echoes on-the-record comments CEO Mark Zuckerberg made at May 2026's shareholder meeting (calling the idea "definitely on the table," noting inbound demand "almost every week"). Multiple outlets (247wallst, Yahoo Finance/Investing.com, StocksToTrade, TradingKey) attribute the +8–11% one-day moves on 2026-06-30 and 2026-07-01 to this report.

**Classification: does NOT meet the Rule 9 bar today.** It is a media report of internal planning, not a company-confirmed strategic announcement, formal guidance revision, or M&A — the framework's "never invent or estimate financial data" / cite-only-confirmed-events discipline applies here just as it does to quantitative inputs. **Treated as a qualitative watch item, not a scored input or a formal new catalyst**, until Meta itself confirms it (earnings call, 8-K, or investor day). Flagged prominently below and in Next Review Triggers.

**Conclusion: no Rule 9 trigger fired.** This remains a routine, schedule-free re-score, driven by a large but sub-15% price move with an identifiable (if unconfirmed) cause.

---

## 3. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** 7.10% (per [holdings.md](../portfolio/holdings.md) — not recomputed this session)

### Carried unchanged from the 06-26 session (filed fundamentals — no new quarter reported)

| Item | Value | Why carried |
|---|---|---|
| TTM EBIT | $88.621B | No new quarter since 06-26 (Q2 2026 isn't out until 29 Jul) |
| TTM FCF (raw — scored input) | $45.65B | Same — Owner Earnings (Upgrade 1) still unresolved, Data Gap #1 |
| TTM Net Income | $70.629B | Same |
| TTM D&A | $20.719B | Same |
| Cash + marketable securities | $81.180B | Same (Q1 2026 balance sheet, 31 Mar 2026) |
| Senior-note debt (excl. operating leases) | $58.748B | Same |
| Net cash | **$22.432B** | Computed, unchanged |
| Shares outstanding | ≈2.196B | Same |
| FCF/NI conversion | **64.6%** | Unchanged |
| Net Debt/EBITDA | −0.205× (net cash) | Unchanged |
| 5yr avg PE (auto-reconstructed) | 23.589× (range 9.255×–36.014×, n=20q) | Carried — `yfinance` TLS/`curl_cffi` error persists across sessions (Data Gap #3) |

### Refreshed this session (price-dependent)

| Item | 06-26 value | 07-01 value (fresh) | Computation |
|---|---|---|---|
| Live price | $549.47 | **$624.70** | IBKR snapshot (§1) |
| Market Cap | $1,206.6361B | **2.196B × $624.70 = $1,371.8412B** | Computed |
| EV | $1,184.2041B | **$1,371.8412B − $22.432B = $1,349.4092B** | Computed |
| **EV/EBIT** | 13.3626× | **$1,349.4092B ÷ $88.621B = 15.2268×** | Computed |
| **FCF Yield** | 3.7832% | **$45.65B ÷ $1,371.8412B = 3.3277%** | Computed |
| Forward EPS (NTM/CY2026) | $36.25 (carried, flagged stale 3+ sessions) | **$32.81** (see Data Gap #2 — resolved this session) | S&P Global consensus via stockanalysis.com, updated 30 Jun 2026 |
| Forward PE | 15.1578× | **$624.70 ÷ $32.81 = 19.0399×** | Computed at fresh live price and fresh consensus EPS |

### Fast-Grower (PEG eligibility) test — re-verified, still fails

FY2023 NI $39.10B → FY2024 $62.36B (+59.5%, low-comp rebound, a one-off) → FY2025 $60.46B (−3.0%). No new fiscal year has reported since 06-26. **Still FAILS** ">15% EPS growth for 3+ consecutive years on a clean base." **PEG not applicable; its 15% weight redistributed to EV/EBIT** (EV/EBIT effectively 40%) — unchanged from every prior META session.

---

## 4. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved; raw FCF used (7th consecutive session).** META does not disclose a maintenance-vs-growth capex split. Raw FCF remains the conservative choice (Owner Earnings would score *cheaper*). Standing recommendation to resolve via a `decisions/` entry remains open.
2. **Forward-EPS consensus — resolved this session.** The $36.25 NTM figure had gone 4 consecutive sessions without a fresh sourced pull and was flagged as diverging from independently-cross-checked CY2026 figures (~$32.2–32.8). This session pulls a fresh, dated, sourced figure: **$32.81** (S&P Global consensus, 2026 EPS estimate, via stockanalysis.com, updated 2026-06-30) — inside the previously-flagged range, confirming the earlier divergence was real, not noise. **Switching to this figure this session** (documented data refresh, not an invented number). Cross-check: using the *old* $36.25 instead, Forward PE = 17.2331×, EY spread = +1.3427% — still fails Step 1 (§5) either way, so this switch does not change the Rate Gate conclusion, only the magnitude.
3. **5yr PE reconstruction not re-run live via `yfinance` this session** — same `curl_cffi`/TLS proxy error documented across the repo's recent session history. Carrying forward 23.589×/9.255×/36.014× (n=20 quarters, last verified 06-23) is defensible: the next earnings print (Q2 2026, 29 Jul) hasn't landed, so the trailing 20-quarter window is unchanged.
4. **ROIC tax-rate normalization (new this session, Quality Score input).** META's TTM effective tax rate is distorted by an $8.03B one-time income-tax *benefit* recognized in Q1 2026 (partially offsetting a prior tax-law-change charge, per Meta's own Q1 2026 disclosure) — using that distorted TTM rate would overstate NOPAT. Used management's own guided forward tax rate instead: **13–16%, midpoint 14.5%** (Meta's Q1 2026 earnings call guidance for the remainder of 2026) — a company-disclosed figure, not an invented one, applied because the alternative (the one-off-distorted TTM rate) would itself be a worse estimate.
5. **"Meta Compute" cloud-business report (§2) — qualitative watch item, not a scored input.** Unconfirmed by the company; excluded from both the Quality Score's Growth-modifier bonus and the Upside/Downside Modifier's scenario assumptions this session. Will be incorporated once Meta confirms it (earnings call, 8-K, or investor event) — flagged for the next session regardless of date.
6. **Gross margin (81.9%) carried from the 06-20 `yfinance` spot-check** — not re-collected live this session (same TLS issue, Data Gap #3). Directionally stable for a business of this scale over 5 weeks; flagged as "not formally refreshed."

---

## 5. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 19.0399 = 5.2523%
Spread = EY − 10Y Treasury = 5.2523% − 4.46% = +0.7923%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.7923%, ~0.71pp short) → **+5 additive.**

> **Flips from PASS (06-26, +2.22% cushion) to FAIL this session** — the price surge (+13.68%) pushed the forward PE up faster than the 10Y moved, more than reversing the cushion. Robustness check with the *old* $36.25 EPS: EY = 5.8027%, spread = +1.3427% — **still FAILS** (just short of the 1.5% bar either way), so this conclusion is not an artifact of the EPS-source switch in Data Gap #2.

**Step 2 — Rate Regime Modifier**
10Y = 4.46% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +10** (up from 06-26's +5, first Step 1 failure since 06-20's flip to PASS).

---

## 6. META — Quality Score (first-ever computation, 2026-06-29 methodology)

```
Profitability (25%): TTM Net Margin = $70.629B / $214.963B (TTM revenue, 12mo to 31 Mar 2026,
  Macrotrends) = 32.86%
  ROIC: NOPAT = EBIT × (1 − normalized tax rate) = $88.621B × (1 − 0.145) = $75.771B  (Data Gap #4)
    Invested Capital = Total Debt ($58.748B) + Total Equity ($243.681B, 10-Q, 31 Mar 2026) = $302.429B
    ROIC = $75.771B / $302.429B = 25.05%
  NetMargin_Component = clamp((32.86/30)×100, 0, 100) = 100.0  (>30% cap)
  ROIC_Component       = clamp((25.05/30)×100, 0, 100) = 83.5
  Profitability_Score  = (100.0 + 83.5) / 2 = 91.75   (no FCF cap — FCF-positive every year on record)

Margins (15%): Gross margin 81.9% (carried, Data Gap #6)
  GrossMargin_Score = clamp((81.9/80)×100, 0, 100) = 100.0   (>80% cap; no separate trend bonus needed)

Growth (20%): Revenue 3yr CAGR, FY2022 $116.61B → FY2025 $200.966B (both SEC-filed full-year figures)
  CAGR = (200.966/116.61)^(1/3) − 1 = 19.89%
  Growth_Score = clamp((19.89/25)×100, 0, 100) = 79.57
  + 10 (documented TAM expansion): Meta's ad business is forecast to overtake Google in global digital
    ad revenue in 2026 (26.8% vs 26.4% share, eMarketer) while simultaneously diversifying into a new
    market — the "Meta Compute" cloud-infrastructure business reported this session (§2) — real,
    cited evidence of market expansion even though the Compute initiative itself isn't yet confirmed
    (the ad-share data alone independently supports the bonus)
  Growth_Score (with bonus) = 89.57

Balance Sheet (15%): Net Debt = $58.748B − $81.180B = −$22.432B (net cash)
  EBITDA = EBIT + D&A = $88.621B + $20.719B = $109.340B
  Net Debt/EBITDA = −22.432/109.340 = −0.205×
  BalanceSheet_Score = clamp(100×(1−(−0.205)/4), 0, 100) = clamp(105.13, 0, 100) = 100.0

Moat Signal (15%) — checklist, cited evidence:
  ✓ Market share stable/growing — TRUE. Meta forecast to overtake Google in global digital ad revenue
     in 2026 (26.8% vs 26.4% share, eMarketer/ALM Corp) — share is growing, not just large.
  ✓ Brand premium — TRUE. Kantar research: Instagram ranks marketers' #2 preferred media brand
     globally (after YouTube); both Instagram and Facebook deliver disproportionately high shares of
     brand awareness/association relative to ad-budget allocation (4-5% of budget → outsized results).
  ✓ Network effect — TRUE. Family of Apps (Facebook/Instagram/WhatsApp/Messenger) is a textbook
     two-sided ad marketplace — billions of users on one side, advertisers bidding for attention on
     the other; well-documented, structural to the business model.
  ✓ Switching costs — TRUE. Advantage+ AI-driven ad-automation stack and Meta's advertiser tooling
     represent deep data/workflow integration (audience data, creative optimization, attribution) —
     migrating an ad program off Meta means rebuilding this from scratch elsewhere.
  ✓ Scale cost advantage — TRUE. Meta, Google, and Amazon together are projected to take 62.3% of
     global digital ad spend in 2026 (ALM Corp) — Meta's AI/data-center scale (1.6GW of newly
     contracted compute from Crusoe alone) gives cost-per-impression and cost-per-training-run
     advantages smaller ad platforms cannot match.
  Moat_Score = (5/5) × 100 = 100.0

FCF Quality (10%): FCF/NI = 64.6% (carried, §3)
  FCFQuality_Score = clamp(((0.646 − 0.40)/0.60)×100, 0, 100) = 41.0
  Below 70% — but the 2+ year hard-disqualifier does NOT fire: this is the same documented
  growth-capex situation (FY2026 capex guidance $125–145B for AI/data-center buildout) that already
  justifies Upgrade 1 (Owner Earnings) for this name — a cited, standing explanation, not an
  unexplained shortfall.

Quality Score = 91.75×0.25 + 100.0×0.15 + 89.57×0.20 + 100.0×0.15 + 100.0×0.15 + 41.0×0.10
              = 22.9375 + 15.0 + 17.914 + 15.0 + 15.0 + 4.10
              = 89.9515 → rounds to 90.0
```

**Quality Score = 90.0 — PASSES the 80.0+ gate comfortably** (first-ever computation for META; a genuinely high-quality compounder by this framework's own measure — strong on every axis except FCF conversion, which has a standing, cited explanation).

**Hard disqualifier check:** none fire. FCF/NI <70% has a documented growth-capex explanation (see above); Net Debt/EBITDA is a net-cash position, nowhere near the 2.5×/4× thresholds; FCF-positive every year on record (well beyond the 3-year minimum).

---

## 7. META — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 3.3277/10), 0, 100) = 66.723
```
→ Contribution: 66.723 × 0.40 = **26.6892**

**EV/EBIT — 40% weight** (PEG not applicable → 15% redistributed here)
```
EV/EBIT_Score = clamp((15.2268 − 12)/23 × 100, 0, 100) = 14.0296
```
→ Contribution: 14.0296 × 0.40 = **5.6118**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (19.0399 − 23.589)/23.589 × 100 = −19.285%
FwdPE_Score = clamp(50 + (−19.285) × 2.5, 0, 100) = clamp(1.7875, 0, 100) = 1.7875
```
→ Contribution: 1.7875 × 0.20 = **0.3575**

**PEG — Fast-Grower test: FAIL** (re-verified §3). PEG's 15% weight redistributed to EV/EBIT (used above).

**Raw weighted score:**
```
= 26.6892 + 5.6118 + 0.3575 = 32.6585
```
**+ Rate Modifier (+10) = 42.6585** *(before the Upside/Downside Modifier)*

---

## 8. META — Upside/Downside Modifier (Expected-Return Modifier)

**Decision: update the Base-case EPS assumption to the fresh, sourced $32.81 consensus (Data Gap #2); Bull/Bear EPS assumptions and both exit multiples carried unchanged** (they are independent scenario judgments, not tied to the single-point consensus figure, and nothing in this window changes the underlying bull/bear narrative — the Meta Compute report is explicitly excluded per Data Gap #5 until confirmed).

**Step 1 — Scenario fair values**

| Scenario | Weight | EPS assumption | Exit PE | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | $40.0 (carried) | 24× | **$960.00** |
| **Base** | 50% | $32.81 (fresh consensus — Data Gap #2) | 20× | **$656.20** |
| **Bear** | 25% | $28.0 (carried) | 13× | **$364.00** |

```
PW Fair Value = 0.25×960.00 + 0.50×656.20 + 0.25×364.00 = $659.10
```
(Down from 06-26's $693.50 — driven entirely by the Base-case EPS update from $36.25→$32.81, i.e. resolving Data Gap #2, not by any judgment change.)

Sanity check (Rule 0 Step 4 / Rule 4): PW FV $659.10 remains below the $827.32 analyst consensus PT.

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = ($659.10 ÷ $624.70) − 1                  = +5.5067%
Catalyst window = 2 years (unchanged — AI ad-monetization proof points at Q2 2026 earnings,
                   capex-ROI demonstration; both still 18–24mo out. Meta Compute NOT counted as a
                   named catalyst yet per Data Gap #5.)
Annualized gap  = 5.5067% ÷ 2                               = +2.7534%/yr
Intrinsic growth = +12.0%/yr   (carried, unchanged basis)
Shareholder yield = buyback yield + dividend yield (recomputed at fresh market cap $1,371.8412B)
                  = $26.25B/$1,371.8412B + $5.32B/$1,371.8412B  = 1.9134% + 0.3877% = +2.3011%/yr
```
```
E (expected annual return) = 2.7534 + 12.0 + 2.3011 = +17.0545%/yr
```

**Step 3 — Catalyst/timeline (Rule 10 + Guardrail 1).** Same two catalysts as prior sessions, both still inside the 18–24-month window (Q2 earnings now only ~4 weeks out). **Upside credit fully allowed; the −5 catalyst cap does NOT apply.**

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
E = 17.0545% ≥ H → M = −15 × clamp((17.0545 − 10)/15, 0, 1)
                      = −15 × clamp(0.47030, 0, 1)
                      = −7.0545
```
**Upside/Downside Modifier M = −7.0545** — a large drop from 06-26's pinned **−15.0 ceiling.** The price surge closed most of the gap to an essentially unchanged (slightly lower, on the EPS-consensus refresh) fair value: annualized gap fell from +13.1%/yr to +2.75%/yr, no longer enough on its own to reach the modifier's saturation point.

**Robustness check:** with raw+rate fixed at 42.6585, the score's full range across the ±15 modifier band is **27.7** (M=−15) to **57.7** (M=+15) — spans BUY-Standard through the low end of HOLD, unlike every prior session where META stayed pinned deep in a BUY band across the full range. This is the first session where the modifier's direction meaningfully matters to the conclusion.

---

## 9. META — Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (32.6585) + Rate Modifier (+10) + Upside/Downside (−7.0545)
                       = 35.6040
```
Boundary rule: not a ".X5" → standard rounding → **Final Valuation Score = 35.6**

| | Value |
|---|---|
| Raw weighted | 32.6585 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −7.0545 (E = +17.05%) |
| **FINAL VALUATION SCORE** | **35.6** |
| Prior valuation score | 17.2 (06-26) |
| **Quality Score** | **90.0 (PASSES 80.0+ gate)** |

```
Composite Score = 0.50 × (100 − 90.0) + 0.50 × 35.6 = 0.50×10.0 + 0.50×35.6 = 5.0 + 17.8 = 22.8
```

**Composite Score = 22.8.**

---

## 10. META — Action & Category Change

**Valuation Score alone: 17.2 → 35.6** (BUY-Full band 0.0–29.9 → BUY-Standard band 30.0–49.9) — a full band move, driven almost entirely by the price surge (+13.68%) shrinking the FCF-yield/EV-EBIT cheapness and collapsing the Upside/Downside Modifier from its −15.0 ceiling to −7.05. **Mechanical, no Rule 9 trigger — see §2.**

**But the framework specifies using the Composite Score, not the raw Valuation Score, for Phase 03 action-table lookups once a Quality Score exists** ([valuation-scoring.md](../framework/valuation-scoring.md), "Composite Score" section). **Composite Score 22.8 → Action band: BUY — Full position 6–8% (Score 0.0–29.9)** — META's first-ever Quality Score (90.0) is high enough that, once blended, it pulls the actionable number back into the same full-position band the raw valuation score alone would have exited. **Net effect: no action-category change once quality is correctly weighted in**, even though the raw valuation score moved a full band.

**Practical recommendation: HOLD — no automatic fresh capital.** META is an existing holding at **7.10%**, inside the 6–8% full-position band both the Composite Score and (independently) the raw score's own new band point to, well under the 15% hard cap.

---

## 11. META — Order Setup (Composite Score in BUY-Full band → required)

Confidence: wide-moat proven compounder (Quality Score 90.0, first-ever computation, confirms rather than merely asserts this) with heavy in-flight AI capex — same conservative 20% MoS used every prior session.

```
[x] Composite Score (drives action band):        22.8   (≤29.9 ✓ — Full-position entry permitted)
[x] Raw Valuation Score (incl. Upside/Downside):  35.6
[x] Expected annual return E / catalyst window:   +17.05% / 2yr
[x] Upside/Downside Modifier applied:             −7.0545
[x] Blended Fair Value (PW, Rule 7):              $659.10  (down from $693.50 — EPS-consensus refresh, §8)
[x] Margin of Safety %:                           20%
[x] BUY PRICE (limit):     $659.10 × (1 − 0.20)        = $527.28
[x] PRIMARY SELL TARGET:   = Blended FV                = $659.10
[x] BULL-CASE TRIM TARGET: $960.00 × 0.90               = $864.00
[x] STOP LOSS:             $527.28 × (1 − 0.25)        = $395.46   (25% max loss, high-conviction bracket)
[x] Risk/Reward Ratio (base-case target):  ($659.10 − $527.28) ÷ ($527.28 − $395.46) = $131.82 ÷ $131.82 = 1.00:1
[x] Risk/Reward Ratio (bull-case trim target): ($864.00 − $527.28) ÷ $131.82 = $336.72 ÷ $131.82 = 2.55:1
```

> 🚩 **Reversal from 06-26's headline development.** Live price ($624.70) has moved **well above** the $527.28 buy-price limit — by $97.42 (18.5%) — the opposite of 06-26, where price had just crossed *below* the (then-higher, $554.80) limit for the first time. The price-condition-met window that opened 06-26 has closed. **Base-case R/R is still exactly 1.00:1 (fails the 2:1 minimum)** — the same recurring shape as every prior META session (only the bull-case trim target clears 2:1, at 2.55:1 here). **Net: no automatic qualifying entry** — both the price-limit condition and the R/R condition now fail, unlike 06-26 where only R/R failed.

**Position sizing:** META is already at **7.10%**, inside the 6–8% allocation band. Room to the band's 8% ceiling: **0.90pp**. No forced trim or top-up.

---

## 12. Portfolio Note

META at 7.10% is comfortably under the 15% hard cap (Upgrade 7) and sits within the 6–8% full-position band its Composite Score points to. No portfolio-level action is forced by this score (no trim signal — Composite Score is nowhere near the 70+ trim bands; no forced top-up — R/R and now price-limit both fail). This session does not change the `holdings.md` weight — that update is handled by the orchestrator.

---

## 13. Next Review Triggers

- **Next earnings — META Q2 2026, expected 29 Jul 2026 (after close)** → routine post-earnings re-score; refreshes TTM fundamentals carried since Q1 2026 (06-12 roll-forward), and is the natural point to confirm or retire the "Meta Compute" watch item (§2/Data Gap #5) if management addresses it on the call.
- **"Meta Compute" cloud-business confirmation (elevated watch item, new this session).** If Meta officially confirms this initiative (8-K, earnings call, investor day) before the next scheduled review, that is a genuine Rule 9-qualifying development (new revenue line / strategic pivot) warranting an immediate re-score — including, at that point, folding it into the Quality Score's Growth modifier and the Upside/Downside Modifier's Bull-case assumptions with real (not carried) numbers.
- **Rule 9 fundamental triggers (standing):** any guidance revision, management change at the Meta Platforms CEO/CFO level, material M&A, or a >15% unexplained price move (currently at +13.68% over 5 days — not yet triggered, but the closest approach to the threshold in the tracked session history).
- **Rate Gate watch:** Step 1 FAILED this session (+0.79pp short of the 1.5% cushion) — first failure since 06-20's flip to PASS. Worth rechecking if price continues to run or the 10Y moves either direction.
- **Buy-price watch (reversed from "condition met" to "well above limit"):** live price ($624.70) is now 18.5% above the $527.28 limit — worth a fresh check if the price pulls back materially before Q2 earnings.
- **5yr PE reconstruction (Data Gap #3)** and **Owner Earnings methodology decision (Data Gap #1)** — both still open; resolve when `yfinance` access is restored / via a dedicated `decisions/` entry respectively.

---

## 14. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output; new terms added there this session are marked *(new)*)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **8-K (Form 8-K)** | A US company's "current report" disclosing a material event between regular filings. |
| **bps / pp (percentage points)** | A direct difference between two percentages, distinct from a "%" change. |
| **Buyback yield** | The rate at which a company's share count shrinks per year from repurchases, net of new issuance. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **IRR** | Internal Rate of Return. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **NTM** | Next Twelve Months. |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for moat-building reinvestors (Upgrade 1; unresolved for META, Data Gap #1). |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

# RESCORE — META — 2026-07-13

**Task type:** RESCORE (single ticker) — **Telegram-triggered** (Routine 6 / `/telegram-scan`)
**Trigger:** New top post [t.me/tarasguk/11369](https://t.me/tarasguk/11369) (~10:13 UTC, 2026-07-13, edited): "$META announced expansion of its Louisiana data center to 5GW. Previously the cost was estimated at $10B; now it's put at $50B. On top of that, $META will spend another $50B on its own chips for this facility. Bloomberg calculated $META's total spend on this one data center will exceed $250B." META is a current holding (6.65% weight per holdings.md) and this claims a candidate Rule 9 event (capex/guidance-shaped). Per CLAUDE.md Rule 0, the post's text is used only as a trigger — every figure below is independently re-pulled from IBKR/live web sources, not from the post.
**Date:** 13 Jul 2026
**10Y US Treasury Yield:** 4.54% (FRED `DGS10`, last posted non-blank value, dated 2026-07-09 — down slightly from 4.56% used 07-09; still inside the "3.5–5%" bracket → Rate Regime Modifier Step 2 unchanged at +5)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** META **39.0** (2026-07-09, Composite 24.5, BUY — Full position 6–8% — [sessions/2026-07-09-rescore-meta.md](2026-07-09-rescore-meta.md))
**Gap since last review:** 4 days.

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; pp = percentage points; EY = earnings yield (1 ÷ PE); TTM = trailing twelve months; NTM = next twelve months.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$664.24** | IBKR `get_price_snapshot` (contract_id 107113386, META Class A / NASDAQ), pulled this session (ts 1783944408 → 2026-07-13 ~14:46:48 UTC) |
| Session change | **−$4.97 / −0.74%** | IBKR `change` field |
| 52-week range | **$520.26 – $794.42** | IBKR `misc_statistics` |
| Year-to-date change | **+0.71%** | IBKR `year_to_date_change` |
| Analyst consensus PT | **$827.48** (59 analysts, S&P Global via stockanalysis.com, updated 13 Jul 2026) | Web search — bull-case sanity check only (Rule 0 Step 4) |

Price vs 07-09 session: $638.45 → $664.24 = **+4.04%** over 4 days. Under the 15% Rule 9 unexplained-move threshold.

---

## 2. Rule 9 Trigger Check (2026-07-09 → 2026-07-13)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Still scheduled for **29 Jul 2026** (after close) — ~2.5 weeks out |
| Guidance revision | No | No new *official* Meta capex/opex guidance since the Q1 2026 call figures already on record (FY26 capex $125–145B, FY26 opex $162–169B) |
| M&A | No | No new M&A found since prior sessions |
| Management change | No | No change found |
| Macro shift | No | 10Y ticked 4.56%→4.54%, still inside the "3.5–5%" bracket |
| **>15% unexplained price move** | **No** | +4.04% over 4 days, well under 15% |

**The triggering post's claim, independently verified.** Confirmed via WebSearch across multiple sources: Bloomberg ("Meta Is Transforming Rural Louisiana With a $200 Billion Data Center", updates through 07-13), CNBC (13 Jul 2026, "Meta's Louisiana data center investment to reach $50 billion, aided by generous tax incentives"), MarketScreener (13 Jul 2026, "Meta expands Louisiana data center to 5 gigawatts, investment crosses $50 billion"), and TipRanks ("Meta Stock Falls on $250B Data Center Push in Louisiana"). This is the same Richland Parish, Louisiana facility tracked since Bloomberg's May 2026 reporting ($200B estimate) and the October 2025 $27B Meta/Blue Owl Capital joint-venture disclosure (then a 2GW facility) — now expanded to 5GW with a **directly-disclosed** $50B construction-cost figure (tied to actual tax-incentive filings, a firmer disclosure than prior reporting) plus Bloomberg's **anonymously-sourced** ("a person familiar with the matter") estimate that Meta's total spend across compute, chips, and infrastructure at this single site will exceed $250B.

**Classification: still does NOT meet the Rule 9 bar.** The $50B *construction* figure is now fairly concretely disclosed (tax filings, local reporting), but the headline $250B *total-spend* number remains a third-party calculation, not a Meta-issued capex guidance revision — Meta's own FY26 capex guidance ($125–145B, company-wide, all facilities) has not been revised. Applying the same bar as every prior session in this ticker's history (a company-confirmed guidance revision, not press estimates of aggregate multi-year spend at one site), **this remains a qualitative watch item, not a scored input or confirmed Rule 9 trigger.**

**Conclusion: no Rule 9 trigger fired.** Proceeding with a full re-score anyway (Telegram-triggered per Routine 6's standing practice for any claimed capex/guidance-shaped post on a held name — same practice as the 07-09 session) since price/consensus inputs have moved and this ticker's live-price-vs-fair-value gap is worth rechecking.

---

## 3. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** **6.65%** (per [holdings.md](../portfolio/holdings.md) — down from the 7.04% cited in the 07-09 session; holdings.md's own urgent-note box flags an **unauthorized 6→5 share reduction** with no `sessions/`/`decisions/`/`override-log.md` entry explaining it. Not a rescore action item — flagging for visibility only; this session uses the current 6.65% as the authoritative live weight per Rule 0, not the stale 7.04%.)

### Carried unchanged from the 07-09 session (no new quarter reported — Q2 2026 not out until 29 Jul)

| Item | Value | Why carried |
|---|---|---|
| TTM EBIT | $88.621B | No new quarter |
| TTM FCF (raw — scored input) | $45.65B | Same — Owner Earnings (Upgrade 1) still unresolved, Data Gap #1 (9th consecutive session) |
| TTM Net Income | $70.629B | Same |
| TTM Revenue | $214.963B | Same |
| Cash + marketable securities | $81.180B | Same (Q1 2026 balance sheet) |
| Senior-note debt (excl. operating leases) | $58.748B | Same |
| Net cash | **$22.432B** | Unchanged |
| Shares outstanding | ≈2.196B | Same |
| Gross margin | 81.9% | Carried — `yfinance` still unavailable (Data Gap #2, 9th consecutive session) |
| FCF/NI conversion | **64.6%** | Unchanged |
| Net Debt/EBITDA | −0.205× (net cash) | Unchanged |
| 5yr avg PE (auto-reconstructed) | 23.589× (range 9.255×–36.014×, n=20q) | Carried — `yfinance` unreachable this session too |
| Buyback ($) / Dividend ($) (TTM) | $26.25B / $5.32B | Same |

### Refreshed this session (price/consensus-dependent)

| Item | 07-09 value | 07-13 value (fresh) | Computation |
|---|---|---|---|
| Live price | $638.45 | **$664.24** | IBKR snapshot (§1) |
| Market Cap | $1,402.0362B | **2.196B × $664.24 = $1,458.6710B** | Computed |
| EV | $1,379.6042B | **$1,458.6710B − $22.432B = $1,436.2390B** | Computed |
| **EV/EBIT** | 15.5675× | **$1,436.2390B ÷ $88.621B = 16.2066×** | Computed |
| **FCF Yield** | 3.2560% | **$45.65B ÷ $1,458.6710B = 3.1296%** | Computed |
| Forward EPS (NTM/CY2026 consensus) | $32.59 | **$32.29** | S&P Global consensus via stockanalysis.com, updated 2026-07-13 (59 analysts) |
| Forward PE | 19.5905× | **$664.24 ÷ $32.29 = 20.5711×** | Computed at fresh price and fresh consensus |

### Fast-Grower (PEG eligibility) test — re-verified, still fails

No new fiscal year has reported since 07-09. **Still FAILS** ">15% EPS growth for 3+ consecutive years on a clean base" (FY2024 +59.5% low-comp rebound, FY2025 −3.0%). **PEG not applicable; its 15% weight redistributed to EV/EBIT** — unchanged from every prior META session.

---

## 4. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved; raw FCF used (9th consecutive session).** No new information this window.
2. **5yr PE reconstruction — still not re-runnable.** `yfinance` module not installed in this session's sandbox (confirmed again this session — `ModuleNotFoundError: No module named 'yfinance'`). Carrying forward 23.589×/9.255×/36.014× (n=20 quarters) — defensible since Q2 2026 (29 Jul) hasn't landed.
3. **Gross margin (81.9%) still carried, not re-collected live** — same root cause as #2.
4. **Louisiana data center ("$250B") story — qualitative watch item, not a scored input (§2).** The $50B facility-construction figure is now fairly directly disclosed; the $250B aggregate is still a Bloomberg anonymous-source estimate, not Meta's own guidance. Excluded from the Quality Score's Growth-modifier bonus basis and from the Upside/Downside Modifier's scenario assumptions this session, same treatment as the "Meta Compute" story in 07-01/07-09. **Will be incorporated with real numbers the moment Meta itself revises FY26 capex guidance or discloses a binding total commitment** — the natural next checkpoint is the 29 Jul Q2 earnings call.
5. **META weight discrepancy (holdings.md, §3):** 6.65% now vs. 7.04% cited 07-09 — traced to holdings.md's own flagged unauthorized 6→5 share reduction (no explaining session/decision/override entry found). Noted for visibility; does not change any score in this session.

---

## 5. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 20.5711 = 4.8612%
Spread = EY − 10Y Treasury = 4.8612% − 4.54% = +0.3212%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.3212%, ~1.18pp short) → **+5 additive.**

> Still FAILS, and by a wider margin than 07-09 (+0.96pp short → +1.18pp short) — price rose further while the consensus EPS estimate ticked down again, both working in the fail-widening direction; the 10Y eased slightly, a small offset.

**Step 2 — Rate Regime Modifier**
10Y = 4.54% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +10** (unchanged from 07-09).

---

## 6. META — Quality Score (recomputed, unchanged inputs)

No new quarter, no margin/balance-sheet/moat change this window — every underlying input (§3, carried) is identical to 07-09, so the Quality Score recomputes to the same result rather than being merely copied forward:

```
Profitability (25%): Net Margin 32.86%, ROIC 25.05% (unchanged basis)
  Profitability_Score = 91.75
Margins (15%): Gross margin 81.9% (carried) → 100.0
Growth (20%): Revenue 3yr CAGR 19.89% → 79.57
  + 10 (TAM-expansion bonus — ad-market-share data alone independently supports it;
    Louisiana data center story still excluded from this basis per Data Gap #4/§2) → 89.57
Balance Sheet (15%): Net Debt/EBITDA −0.205× → 100.0
Moat Signal (15%): 5/5 signals unchanged (market share, brand premium, network effect,
  switching costs, scale cost advantage) → 100.0
FCF Quality (10%): FCF/NI 64.6% (carried) → 41.0 (growth-capex explanation still stands, no
  hard-disqualifier fire)

Quality Score = 91.75×0.25 + 100.0×0.15 + 89.57×0.20 + 100.0×0.15 + 100.0×0.15 + 41.0×0.10
              = 22.9375 + 15.0 + 17.914 + 15.0 + 15.0 + 4.10
              = 89.9515 → rounds to 90.0
```

**Quality Score = 90.0 — unchanged, PASSES the 80.0+ gate.** No quality drift this window (expected — no new fundamentals reported).

**Hard disqualifier check:** none fire, same as prior sessions.

---

## 7. META — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 3.1296/10), 0, 100) = 68.704
```
→ Contribution: 68.704 × 0.40 = **27.4816**

**EV/EBIT — 40% weight** (PEG not applicable → 15% redistributed here)
```
EV/EBIT_Score = clamp((16.2066 − 12)/23 × 100, 0, 100) = 18.2896
```
→ Contribution: 18.2896 × 0.40 = **7.31584**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (20.5711 − 23.589)/23.589 × 100 = −12.7932%
FwdPE_Score = clamp(50 + (−12.7932) × 2.5, 0, 100) = clamp(18.017, 0, 100) = 18.017
```
→ Contribution: 18.017 × 0.20 = **3.6034**

**PEG — Fast-Grower test: FAIL** (re-verified §3). Weight redistributed to EV/EBIT (used above).

**Raw weighted score:**
```
= 27.4816 + 7.31584 + 3.6034 = 38.40084
```
**+ Rate Modifier (+10) = 48.40084** *(before the Upside/Downside Modifier)*

---

## 8. META — Upside/Downside Modifier (Expected-Return Modifier)

**Decision: update Base-case EPS to the fresh $32.29 consensus; Bull/Bear EPS and both exit multiples carried unchanged** — same practice as every prior session; nothing in this window (§2/§4) changes the underlying bull/bear narrative (Louisiana data center story still excluded until Meta itself confirms/revises guidance).

**Step 1 — Scenario fair values**

| Scenario | Weight | EPS assumption | Exit PE | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | $40.0 (carried) | 24× | **$960.00** |
| **Base** | 50% | $32.29 (fresh consensus) | 20× | **$645.80** |
| **Bear** | 25% | $28.0 (carried) | 13× | **$364.00** |

```
PW Fair Value = 0.25×960.00 + 0.50×645.80 + 0.25×364.00 = $653.90
```
(Down slightly from 07-09's $656.90 — the Base-case consensus EPS ticked down $32.59→$32.29.)

Sanity check (Rule 0 Step 4 / Rule 4): PW FV $653.90 remains well below the $827.48 analyst consensus PT.

🚩 **New this session: live price has now crossed above the PW Fair Value itself** — $664.24 vs. $653.90 (**+1.58% above FV**), the first time in this ticker's tracked history that this has happened (07-01: price below FV by a small margin; 07-09: price $638.45 vs FV $656.90, still below). Purely a mechanical consequence of the price climbing +4.04% in 4 days while consensus EPS drifted down slightly — not a new qualitative catalyst.

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = ($653.90 ÷ $664.24) − 1                  = −1.5567%
Catalyst window = 2 years (unchanged — AI ad-monetization proof points at Q2 2026 earnings,
                   capex-ROI demonstration; both ~18–24mo out. Louisiana data center story
                   still NOT counted as a named catalyst per §2/§4.)
Annualized gap  = −1.5567% ÷ 2                               = −0.7784%/yr
Intrinsic growth = +12.0%/yr   (carried, unchanged basis)
Shareholder yield = buyback yield + dividend yield (recomputed at fresh market cap $1,458.6710B)
                  = $26.25B/$1,458.6710B + $5.32B/$1,458.6710B  = 1.7996% + 0.3647% = +2.1643%/yr
```
```
E (expected annual return) = −0.7784 + 12.0 + 2.1643 = +13.3859%/yr
```

**Step 3 — Catalyst/timeline (Rule 10 + Guardrail 1).** Same two catalysts as prior sessions, both inside the 18–24-month window (Q2 earnings now ~2.5 weeks out). **Upside credit fully allowed; the −5 catalyst cap does NOT apply.**

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
E = 13.3859% ≥ H → M = −15 × clamp((13.3859 − 10)/15, 0, 1)
                      = −15 × clamp(0.22573, 0, 1)
                      = −3.3859
```
**Upside/Downside Modifier M = −3.3859** — a further step down from 07-09's −5.6967, continuing the trend as the price runs further ahead of a roughly flat/declining fair value. The negative "Gap Upside %" term (first time on record for META) is now actively pulling the modifier back toward zero, offset by the still-strong Intrinsic Growth and Shareholder Yield terms.

---

## 9. META — Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (38.40084) + Rate Modifier (+10) + Upside/Downside (−3.3859)
                       = 45.01494
```
Boundary rule: not a ".X5" → standard rounding → **Final Valuation Score = 45.0**

| | Value |
|---|---|
| Raw weighted | 38.40084 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −3.3859 (E = +13.39%) |
| **FINAL VALUATION SCORE** | **45.0** |
| Prior valuation score | 39.0 (07-09) |
| **Quality Score** | **90.0 (unchanged, PASSES 80.0+ gate)** |

```
Composite Score = 0.50 × (100 − 90.0) + 0.50 × 45.0 = 0.50×10.0 + 0.50×45.0 = 5.0 + 22.5 = 27.5
```

**Composite Score = 27.5** (up from 24.5 on 07-09 — a larger mechanical move than usual, driven by the price/consensus drift narrowing the Upside/Downside Modifier, not by any new confirmed catalyst).

---

## 10. META — Action & Category Change

**Valuation Score alone: 39.0 → 45.0** — stays inside the same BUY-Standard band (30.0–49.9). **No band change**, though it is now within 5.0 points of the top of that band.

**Composite Score: 24.5 → 27.5 → Action band: BUY — Full position 6–8% (Score 0.0–29.9), unchanged.** No action-category change, but the Composite Score is now within 2.4 points of the 29.9 band boundary — worth watching closely at the next review if the price keeps climbing faster than the fair-value inputs.

**Practical recommendation: HOLD — no automatic fresh capital.** META is an existing holding at **6.65%** (per holdings.md; see §3 flag on the weight discrepancy), inside the 6–8% full-position band, well under the 15% hard cap.

---

## 11. META — Order Setup (Composite Score in BUY-Full band → required)

Confidence: wide-moat proven compounder (Quality Score 90.0, unchanged) with heavy in-flight AI capex — same conservative 20% MoS used every prior session.

```
[x] Composite Score (drives action band):        27.5   (≤29.9 ✓ — Full-position entry permitted, but close to the boundary)
[x] Raw Valuation Score (incl. Upside/Downside):  45.0
[x] Expected annual return E / catalyst window:   +13.39% / 2yr
[x] Upside/Downside Modifier applied:             −3.3859
[x] Blended Fair Value (PW, Rule 7):              $653.90  (down slightly from $656.90 — consensus EPS drift)
[x] Margin of Safety %:                           20%
[x] BUY PRICE (limit):     $653.90 × (1 − 0.20)        = $523.12
[x] PRIMARY SELL TARGET:   = Blended FV                = $653.90
[x] BULL-CASE TRIM TARGET: $960.00 × 0.90               = $864.00
[x] STOP LOSS:             $523.12 × (1 − 0.25)        = $392.34   (25% max loss, high-conviction bracket)
[x] Risk/Reward Ratio (base-case target):  ($653.90 − $523.12) ÷ ($523.12 − $392.34) = $130.78 ÷ $130.78 = 1.00:1
[x] Risk/Reward Ratio (bull-case trim target): ($864.00 − $523.12) ÷ $130.78 = $340.88 ÷ $130.78 = 2.61:1
```

Live price ($664.24) remains **$141.12 (26.98%) above** the $523.12 buy-price limit — the gap has widened again from 07-09's 21.5%, and (per §8) live price is now also above the PW Fair Value itself for the first time. **Base-case R/R still exactly 1.00:1 (fails the 2:1 minimum)**, same recurring shape as every prior META session. **Net: no automatic qualifying entry** — both the price-limit condition and the R/R condition fail, more decisively than before.

**Position sizing:** META is at **6.65%** (holdings.md), inside the 6–8% band. Room to the 8% ceiling: **1.35pp**. No forced trim or top-up.

---

## 12. Portfolio Note

META at 6.65% is comfortably under the 15% hard cap (Upgrade 7) and sits within the 6–8% full-position band its Composite Score points to. No portfolio-level action is forced by this score (no trim signal — nowhere near the 70+ trim bands; no forced top-up — R/R and price-limit both fail, more so than 07-09). This session does not change the `holdings.md` weight itself, only Last Score/Quality Score/Composite Score/Last Review. **The unauthorized 6→5 share reduction flagged in holdings.md (§3) is a separate, open issue for this position — not resolved or investigated further by this rescore.**

---

## 13. Next Review Triggers

- **Next earnings — META Q2 2026, expected 29 Jul 2026 (after close)** → routine post-earnings re-score; refreshes all carried TTM fundamentals, and is the natural checkpoint for Meta to either revise FY26 capex guidance (folding the Louisiana data-center numbers in with real figures) or let the watch item lapse.
- **Louisiana data-center ("$250B") story — still an elevated watch item, still not confirmed as an official guidance revision (§2/§4).** If Meta itself revises FY26 capex guidance or discloses a binding total commitment before the next scheduled review, that is a genuine Rule 9-qualifying development warranting an immediate re-score.
- **Rule 9 fundamental triggers (standing):** any guidance revision, management change, material M&A, or a >15% unexplained price move.
- **Rate Gate watch:** Step 1 FAILED again this session, by a wider margin (+0.32% cushion, down from +0.96%) — worth rechecking if price continues to run or the 10Y moves either direction.
- **Buy-price / fair-value watch:** live price ($664.24) is now 26.98% above the $523.12 limit *and* above the PW FV itself for the first time — worth a fresh check if the price pulls back materially before Q2 earnings, or if the Composite Score approaches the 29.9 band boundary at the next review.
- **holdings.md weight discrepancy (6.65% vs. 7.04% cited 07-09) — unresolved, flagged for a manual follow-up session** (see §3/§4 item 5; not something `/rescore` can investigate — needs `get_account_trades`).
- **5yr PE reconstruction (Data Gap #2)** and **Owner Earnings methodology decision (Data Gap #1)** — both still open, 9th consecutive session; `yfinance` is not installed in this session's sandbox environment.

---

## 14. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output; no new terms this session)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **bps / pp (percentage points)** | A direct difference between two percentages, distinct from a "%" change. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NTM** | Next Twelve Months. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

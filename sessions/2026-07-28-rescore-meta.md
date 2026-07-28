# RESCORE — META — 2026-07-28

**Task type:** RESCORE (single ticker) — **Telegram-triggered** (Routine 6 / `/telegram-scan`), **P1 priority** (≥5% weight holding, per automation-schedule.md)
**Trigger:** New top post [t.me/tarasguk/11510](https://t.me/tarasguk/11510) (~17:59 UTC, 2026-07-28): "Meta is investing $10 billion in another new data center. The company will place debt on the balance sheet of a new joint venture with BlackRock. Meanwhile, Meta's stock has been falling for 9 consecutive trading days." Per CLAUDE.md Rule 0, the post's text is used only as a *trigger* — every figure below is independently re-pulled from IBKR/live web sources, not from the post. **The post's own "$10 billion" figure is imprecise** — see §2 for the verified deal size (~$14B total JV, Meta's own contribution ~$2.3B).
**Date:** 28 Jul 2026
**10Y US Treasury Yield:** 4.69% (FRED `DGS10`, last posted non-blank value, dated 2026-07-24 — no 07-27/07-28 print yet; up from 4.54% used 07-13, still inside the "3.5–5%" bracket → Rate Regime Modifier Step 2 unchanged at +5)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** META **45.0** (2026-07-13, Composite 27.5, BUY — Full position 6–8% — [sessions/2026-07-13-rescore-meta.md](2026-07-13-rescore-meta.md))
**Gap since last review:** 15 days.

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; pp = percentage points; EY = earnings yield (1 ÷ PE); TTM = trailing twelve months; NTM = next twelve months; JV = joint venture.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$594.00** | IBKR `get_price_snapshot` (contract_id 107113386, META Class A / NASDAQ), pulled this session (ts 1785269232 → 2026-07-28 ~20:07:12 UTC) |
| Session change | **+$0.13 / +0.02%** | IBKR `change` field |
| 52-week range | **$520.26 – $794.42** | IBKR `misc_statistics` |
| Year-to-date change | **−9.94%** | IBKR `year_to_date_change` |
| Analyst consensus PT | **$824.68** (62 analysts, S&P Global via stockanalysis.com, updated 28 Jul 2026) | Web fetch — bull-case sanity check only (Rule 0 Step 4) |

Price vs 07-13 session: $664.24 → $594.00 = **−10.58%** over 15 days. Under the standalone 15% Rule 9 unexplained-move threshold, and it isn't "unexplained" regardless — it lines up with the sustained pullback the trigger post describes and broader AI-capex-spend jitters ahead of tomorrow's earnings (see §2). The actual Rule 9 trigger this session is the JV announcement itself (a material M&A/JV disclosure), not the price move.

---

## 2. Rule 9 Trigger Check (2026-07-13 → 2026-07-28)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No (imminent) | Scheduled for **29 Jul 2026 (after close)** — tomorrow, not yet reported. This session is about the JV disclosure, not earnings. |
| Guidance revision | No | No new official Meta capex/opex guidance since Q1 2026 call figures (FY26 capex $125–145B, FY26 opex $162–169B) |
| **Material M&A / JV announcement** | **YES** | See below — clears the bar this time |
| Management change | No | No change found |
| Macro shift | No | 10Y ticked 4.54%→4.69%, still inside the "3.5–5%" bracket |
| >15% unexplained price move | No | −10.58% over 15 days (§1), and it's explained, not unexplained |

**The triggering post's claim, independently verified — and clears the Rule 9 bar this time.** Confirmed via WebSearch/WebFetch across Meta's own investor-relations site (investor.atmeta.com), about.fb.com, PRNewswire, CNBC, Bloomberg, and the Express Tribune/GV Wire wire pickups, all dated 2026-07-28: **"Meta Announces New Strategic Venture with BlackRock to Develop Data Center in El Paso."**

**Verified deal structure (not the post's "$10 billion" figure):**
- A ~**$14 billion** joint venture to build a data-center campus in El Paso, Texas — ~1 gigawatt of compute capacity, first infrastructure targeted online **2028**, Meta as sole initial tenant.
- **Ownership:** BlackRock-managed funds hold **80%**; Meta retains **20%**.
- **Contributions:** Meta contributes ~**$2.3B** of land and partially-completed construction assets and receives a **$1B distribution** to align ownership; BlackRock contributes ~**$4.9B** of equity.
- **Financing:** A **$12.5B debt financing** package (a 2048-dated note, reported at roughly a 2.875pp premium to the 10Y Treasury) sits on the **JV's own balance sheet**, not Meta's.
- This is Meta's **second** such AI-infrastructure JV disclosed in 2026, after the Hyperion/Louisiana facility with Blue Owl Capital (tracked as a qualitative watch item, not a Rule 9 trigger, in the 07-01/07-09/07-13 sessions) — together they establish a clear, repeatable **off-balance-sheet financing pattern** for Meta's AI capex buildout (see new glossary entries).

**Why this clears the bar where the Louisiana story didn't (07-13 session's explicit next-review-trigger condition):** the Louisiana story was press-estimated aggregate spend ($250B) with no company-confirmed total; this El Paso disclosure is an **official, Meta-confirmed, binding joint-venture commitment** — a definitive agreement with a named partner, a disclosed capital structure, and a completed financing (not a rumor or a hedge-language CEO quote). It satisfies fair-value-methodology.md Rule 9's "material M&A announcement" trigger directly.

**Treatment in this session's scoring (per task scope — qualitative context only, no invented financial-statement inputs):**
- **Quality Score — Balance Sheet sub-score:** Meta's own reported Net Debt/EBITDA (§3, carried from the Q1 2026 10-Q, unchanged until tomorrow's Q2 print) is **not** affected by this JV — the $12.5B debt sits on the JV entity's balance sheet, not Meta's consolidated one (Meta holds a 20% minority stake, not consolidated control). No change to the Balance Sheet sub-score this session on that basis. Qualitatively, though, the pattern is worth flagging: Meta is increasingly financing its AI buildout through off-balance-sheet JV debt rather than its own senior notes, which keeps its own reported leverage ratios artificially conservative relative to the true scale of capital committed to AI infrastructure in aggregate. Not scored as a penalty (no disclosed, attributable consolidation basis exists to fold into the formula without inventing a number), but flagged as a trend to watch — worth asking whether Meta's own balance-sheet-based Quality Score is fully capturing aggregate AI-capex risk as more of these JVs stack up.
- **Quality Score — Moat Signal:** No change to the 5/5 signal count (§6) — this JV is a financing/capacity decision, not new evidence of market share, brand premium, network effect, switching costs, or scale-cost-advantage. It's consistent with (not new proof of) the existing "scale cost advantage" signal basis.
- **Quality Score — Growth sub-score:** No new TAM-expansion modifier added from this news specifically — the existing +10 bonus is already justified independently by ad-market-share data (carried from 07-13), and a compute-capacity JV isn't itself documented TAM/pricing-power evidence under the framework's definition.
- **Upside/Downside Modifier — catalyst window:** The El Paso facility's 2028 online date is a **new, concrete milestone** landing within the existing 2-year catalyst window already used for the AI-ad-monetization/capex-ROI catalysts (§8) — reinforces rather than replaces it. No change to the window length.
- **Bull/Base/Bear scenario EPS assumptions (§8):** Left unchanged from 07-13 — this JV doesn't provide a new, company-disclosed EPS-relevant figure (revenue, margin, or per-share impact), so per "never invent or estimate financial data," it isn't folded into the scenario assumptions as a number, only as qualitative capex-trajectory color above.

**Conclusion: Rule 9 trigger CONFIRMED this session** (material M&A/JV announcement) — full re-score proceeds as a triggered event, not merely a routine check-in.

---

## 3. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** **6.16%** (per [holdings.md](../portfolio/holdings.md), live-synced 2026-07-26 — down from the 6.65% cited in the 07-13 session and the 6.65% figure in this session's trigger brief, which was itself sourced from the 07-13 session. holdings.md's own override-log entry still flags an **unauthorized 6→5 share reduction** with no `sessions/`/`decisions/`/`override-log.md` entry explaining the mechanism — unresolved, out of `/rescore`'s scope, not investigated further here. Using the current 6.16% as the authoritative live weight per Rule 0.)

### Carried unchanged from the 07-13 session (no new quarter reported — Q2 2026 not out until tomorrow, 29 Jul, after close)

| Item | Value | Why carried |
|---|---|---|
| TTM EBIT | $88.621B | No new quarter |
| TTM FCF (raw — scored input) | $45.65B | Same — Owner Earnings (Upgrade 1) still unresolved, Data Gap #1 (10th consecutive session) |
| TTM Net Income | $70.629B | Same |
| TTM Revenue | $214.963B | Same |
| Cash + marketable securities | $81.180B | Same (Q1 2026 balance sheet) |
| Senior-note debt (excl. operating leases) | $58.748B | Same |
| Net cash | **$22.432B** | Unchanged |
| Shares outstanding | ≈2.196B | Same |
| Gross margin | 81.9% | Carried — yfinance data pull attempted this session and failed on persistent Yahoo Finance rate-limiting through the proxy (Data Gap #2, 10th consecutive session — see §4) |
| FCF/NI conversion | **64.6%** | Unchanged |
| Net Debt/EBITDA | −0.205× (net cash) | Unchanged — see §2 re: JV debt not consolidated |
| 5yr avg PE (auto-reconstructed) | 23.589× (range 9.255×–36.014×, n=20q) | Carried — same yfinance rate-limit issue this session |
| Buyback ($) / Dividend ($) (TTM) | $26.25B / $5.32B | Same |

### Refreshed this session (price/consensus-dependent)

| Item | 07-13 value | 07-28 value (fresh) | Computation |
|---|---|---|---|
| Live price | $664.24 | **$594.00** | IBKR snapshot (§1) |
| Market Cap | $1,458.6710B | **2.196B × $594.00 = $1,304.4240B** | Computed |
| EV | $1,436.2390B | **$1,304.4240B − $22.432B = $1,281.9920B** | Computed |
| **EV/EBIT** | 16.2066× | **$1,281.9920B ÷ $88.621B = 14.4660×** | Computed |
| **FCF Yield** | 3.1296% | **$45.65B ÷ $1,304.4240B = 3.4996%** | Computed |
| Forward EPS (NTM/CY2026 consensus) | $32.29 | **$31.72** | S&P Global consensus via stockanalysis.com, fetched 2026-07-28 (59 analysts) |
| Forward PE | 20.5711× | **$594.00 ÷ $31.72 = 18.7264×** | Computed at fresh price and fresh consensus |

### Fast-Grower (PEG eligibility) test — re-verified, still fails

No new fiscal year has reported since 07-13. **Still FAILS** ">15% EPS growth for 3+ consecutive years on a clean base" (FY2024 +59.5% low-comp rebound, FY2025 −3.0%). **PEG not applicable; its 15% weight redistributed to EV/EBIT** — unchanged from every prior META session.

---

## 4. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved; raw FCF used (10th consecutive session).** No new information this window.
2. **5yr PE reconstruction and gross margin — attempted, but failed this session on a *new* root cause.** `yfinance` (and `lxml`) were successfully installed this session (unlike prior sessions, which failed at `ModuleNotFoundError`), and a live IBKR price/`t.info`/`t.financials` pull was attempted repeatedly (>15 minutes, 3 separate background processes, dozens of retries with exponential backoff) via a plain-`requests` session pointed at the proxy CA bundle — necessary because `yfinance`'s default `curl_cffi`-based browser-impersonation session caused persistent TLS connection resets specific to this proxy environment (worked around by passing a custom `requests.Session()`, confirmed via a direct isolated test). Despite the workaround, Yahoo Finance's own server-side rate limiting (`YFRateLimitError: Too Many Requests`) blocked every subsequent attempt to pull `t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet`, and `t.quarterly_financials` for the rest of the session. **Carrying forward 23.589×/9.255×/36.014× (5yr PE, n=20 quarters) and 81.9% (gross margin) from 07-13** — defensible since Q2 2026 (tomorrow, 29 Jul) hasn't landed yet, so neither figure has actually changed in the real world since the last successful pull. No number was invented — both carried values are the last verified-real figures on file.
3. **El Paso/BlackRock JV — used as qualitative Rule 9 context only, not folded into any scored financial-statement input this session (§2).** Consistent with "never invent or estimate financial data" — the JV's $14B/$12.5B/$4.9B/$2.3B figures describe the *JV entity's* capital structure, not a revision to any of Meta's own reported financial-statement line items.
4. **META weight discrepancy (holdings.md, §3):** 6.16% now vs. 6.65% cited in the trigger brief (itself carried from the 07-13 session) — traced to the ongoing unresolved unauthorized-share-reduction override (override-log.md). Noted for visibility; does not change any score in this session.

---

## 5. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 18.7264 = 5.3401%
Spread = EY − 10Y Treasury = 5.3401% − 4.69% = +0.6501%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.6501%, ~0.85pp short) → **+5 additive.**

> Still FAILS, but the cushion **improved** vs 07-13 (short by 1.18pp → short by 0.85pp) — forward PE compressed sharply as the price fell faster than the fresh consensus EPS estimate ticked down, more than offsetting the 10Y's rise (4.54%→4.69%).

**Step 2 — Rate Regime Modifier**
10Y = 4.69% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +10** (unchanged from 07-13, same total via a different mix of drivers).

---

## 6. META — Quality Score (recomputed)

No new quarter, no margin/balance-sheet/moat change this window — every underlying quantitative input (§3, carried) is identical to 07-13, so the Quality Score is recomputed fresh from those inputs rather than merely copied forward, per the framework's "quality can drift" instruction. The JV disclosure is discussed qualitatively in §2 but does not change any of the inputs below, per the reasoning there.

```
Profitability (25%):
  Net Margin = TTM NI ÷ TTM Revenue = $70.629B ÷ $214.963B = 32.8564%
  ROIC = 25.05% (carried basis)
  NetMargin_Component = clamp(32.8564/30×100, 0, 100) = 100.0
  ROIC_Component       = clamp(25.05/30×100, 0, 100)  = 83.50
  Profitability_Score  = (100.0 + 83.50) / 2 = 91.75

Margins (15%): Gross margin 81.9% (carried) → clamp(81.9/80×100,0,100) = 100.0

Growth (20%): Revenue 3yr CAGR 19.89% (carried)
  Growth_Score = clamp(19.89/25×100, 0, 100) = 79.56
  + 10 (TAM-expansion bonus — ad-market-share data alone independently supports it;
    El Paso/BlackRock JV explicitly excluded from this basis per §2/§4) → 89.56

Balance Sheet (15%): Net Debt/EBITDA −0.205× (carried; JV debt not consolidated, §2)
  BalanceSheet_Score = clamp(100×(1−(−0.205)/4), 0, 100) = 100.0

Moat Signal (15%): 5/5 signals unchanged (market share, brand premium, network effect,
  switching costs, scale cost advantage) → 100.0

FCF Quality (10%): FCF/NI 64.6% (carried) → clamp(((0.646−0.40)/0.60)×100, 0, 100) = 41.0
  (growth-capex explanation still stands, no hard-disqualifier fire)

Quality Score = 91.75×0.25 + 100.0×0.15 + 89.56×0.20 + 100.0×0.15 + 100.0×0.15 + 41.0×0.10
              = 22.9375 + 15.0 + 17.912 + 15.0 + 15.0 + 4.10
              = 89.9495 → rounds to 89.9
```

**Quality Score = 89.9 — PASSES the 80.0+ gate.** Effectively unchanged from 07-13's 90.0 (a 0.1-point difference driven by a small arithmetic-precision difference in the Growth sub-score's revenue-CAGR term — 79.56 here vs. 79.57 in the 07-13 log for the identical 19.89% input — not a real quality change). No quality drift this window, as expected (no new fundamentals reported; JV disclosure treated as qualitative-only per §2).

**Hard disqualifier check:** none fire, same as prior sessions.

---

## 7. META — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 3.4996/10), 0, 100) = 65.0037
```
→ Contribution: 65.0037 × 0.40 = **26.0015**

**EV/EBIT — 40% weight** (PEG not applicable → 15% redistributed here)
```
EV/EBIT_Score = clamp((14.4660 − 12)/23 × 100, 0, 100) = 10.7218
```
→ Contribution: 10.7218 × 0.40 = **4.2887**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (18.7264 − 23.589)/23.589 × 100 = −20.6140%
FwdPE_Score = clamp(50 + (−20.6140) × 2.5, 0, 100) = clamp(−1.5350, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — Fast-Grower test: FAIL** (re-verified §3). Weight redistributed to EV/EBIT (used above).

**Raw weighted score:**
```
= 26.0015 + 4.2887 + 0.0 = 30.2902
```
**+ Rate Modifier (+10) = 40.2902** *(before the Upside/Downside Modifier)*

---

## 8. META — Upside/Downside Modifier (Expected-Return Modifier)

**Decision: update Base-case EPS to the fresh $31.72 consensus; Bull/Bear EPS and both exit multiples carried unchanged** — same practice as every prior session; the El Paso/BlackRock JV (§2) doesn't provide a new, company-disclosed EPS-relevant figure, so it isn't folded into the scenario assumptions as a number, only noted as reinforcing the existing catalyst window.

**Step 1 — Scenario fair values**

| Scenario | Weight | EPS assumption | Exit PE | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | $40.0 (carried) | 24× | **$960.00** |
| **Base** | 50% | $31.72 (fresh consensus) | 20× | **$634.40** |
| **Bear** | 25% | $28.0 (carried) | 13× | **$364.00** |

```
PW Fair Value = 0.25×960.00 + 0.50×634.40 + 0.25×364.00 = $648.20
```
(Down slightly from 07-13's $653.90 — the Base-case consensus EPS ticked down $32.29→$31.72.)

Sanity check (Rule 0 Step 4 / Rule 4): PW FV $648.20 remains well below the $824.68 analyst consensus PT.

🚩 **Live price has fallen back below the PW Fair Value** — $594.00 vs. $648.20 (**−8.36% below FV**), reversing the 07-13 session's first-ever crossing above FV. Purely a mechanical consequence of the 15-day price decline outrunning the modest FV decline — not itself a new qualitative catalyst (the JV disclosure is priced qualitatively via §2, not through this scenario table).

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = ($648.20 ÷ $594.00) − 1                  = +9.1246%
Catalyst window = 2 years (unchanged — AI ad-monetization proof points at tomorrow's Q2 2026
                   earnings, capex-ROI demonstration; both ~18–24mo out. El Paso JV's 2028
                   online date lands within this same window — reinforces, doesn't replace it.)
Annualized gap  = +9.1246% ÷ 2                               = +4.5623%/yr
Intrinsic growth = +12.0%/yr   (carried, unchanged basis)
Shareholder yield = buyback yield + dividend yield (recomputed at fresh market cap $1,304.4240B)
                  = $26.25B/$1,304.4240B + $5.32B/$1,304.4240B  = 2.0124% + 0.4078% = +2.4202%/yr
```
```
E (expected annual return) = +4.5623 + 12.0 + 2.4202 = +18.9825%/yr
```

**Step 3 — Catalyst/timeline (Rule 10 + Guardrail 1).** Same two catalysts as prior sessions, both inside the 18–24-month window (Q2 earnings now literally tomorrow; El Paso facility online 2028 reinforces the window). **Upside credit fully allowed; the −5 catalyst cap does NOT apply.**

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
E = 18.9825% ≥ H → M = −15 × clamp((18.9825 − 10)/15, 0, 1)
                      = −15 × clamp(0.59883, 0, 1)
                      = −8.9825
```
**Upside/Downside Modifier M = −8.9825** — a large step further from 07-13's −3.3859 (and further than the 07-09/07-01 range too), driven by the price falling back below fair value while the growth/shareholder-yield components stayed strong. The Gap Upside % term flipped back positive (+9.12% vs. −1.56% on 07-13), the single biggest driver of the modifier's move.

---

## 9. META — Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (30.2902) + Rate Modifier (+10) + Upside/Downside (−8.9825)
                       = 31.3077
```
Boundary rule: not a ".X5" → standard rounding → **Final Valuation Score = 31.3**

| | Value |
|---|---|
| Raw weighted | 30.2902 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −8.9825 (E = +18.98%) |
| **FINAL VALUATION SCORE** | **31.3** |
| Prior valuation score | 45.0 (07-13) |
| **Quality Score** | **89.9 (down 0.1 from 90.0 — rounding precision only, §6; PASSES 80.0+ gate)** |

```
Composite Score = 0.50 × (100 − 89.9) + 0.50 × 31.3 = 0.50×10.1 + 0.50×31.3 = 5.05 + 15.65 = 20.70
```

**Composite Score = 20.7** (down sharply from 27.5 on 07-13 — a full-band-interior move driven mechanically by the 15-day price decline: cheaper FCF yield and EV/EBIT, a much cheaper forward-PE positioning, and — the single largest driver — the Upside/Downside Modifier swinging from −3.4 to −9.0 as the price fell back below fair value).

---

## 10. META — Action & Category Change

**Valuation Score alone: 45.0 → 31.3** — stays inside the same BUY-Standard band (30.0–49.9), but now only **1.4 points above the top of the BUY-Full band** (30.0 is the boundary; the score sits at 31.3, i.e. within the band but close to crossing into BUY-Full on the raw valuation score alone next review if the price keeps falling).

**Composite Score: 27.5 → 20.7 → Action band: BUY — Full position 6–8% (Score 0.0–29.9), unchanged band, but a meaningfully lower (more attractive) number within it.** No action-category change.

**Practical recommendation: HOLD — no automatic fresh capital.** META is an existing holding at **6.16%** (per holdings.md; see §3 flag on the weight discrepancy), inside the 6–8% full-position band, well under the 15% hard cap.

---

## 11. META — Order Setup (Composite Score in BUY-Full band → required)

Confidence: wide-moat proven compounder (Quality Score 89.9, effectively unchanged) with heavy in-flight AI capex, now increasingly financed via off-balance-sheet JVs (§2) — same conservative 20% MoS used every prior session.

```
[x] Composite Score (drives action band):        20.7   (≤29.9 ✓ — Full-position entry permitted)
[x] Raw Valuation Score (incl. Upside/Downside):  31.3
[x] Expected annual return E / catalyst window:   +18.98% / 2yr
[x] Upside/Downside Modifier applied:             −8.9825
[x] Blended Fair Value (PW, Rule 7):              $648.20  (down slightly from $653.90 — consensus EPS drift)
[x] Margin of Safety %:                           20%
[x] BUY PRICE (limit):     $648.20 × (1 − 0.20)        = $518.56
[x] PRIMARY SELL TARGET:   = Blended FV                = $648.20
[x] BULL-CASE TRIM TARGET: $960.00 × 0.90               = $864.00
[x] STOP LOSS:             $518.56 × (1 − 0.25)        = $388.92   (25% max loss, high-conviction bracket)
[x] Risk/Reward Ratio (base-case target):  ($648.20 − $518.56) ÷ ($518.56 − $388.92) = $129.64 ÷ $129.64 = 1.00:1
[x] Risk/Reward Ratio (bull-case trim target): ($864.00 − $518.56) ÷ $129.64 = $345.44 ÷ $129.64 = 2.66:1
```

Live price ($594.00) is now **$75.44 (14.55%) above** the $518.56 buy-price limit — the gap has **narrowed sharply** from 07-13's 26.98%, the closest META has been to its buy limit since this modifier was introduced. **Base-case R/R still exactly 1.00:1 (fails the 2:1 minimum)**, same recurring shape as every prior META session. **Net: no automatic qualifying entry** — both the price-limit condition and the R/R condition still fail, but materially less decisively than before. **Worth a fresh check very soon** if the price continues its recent slide, especially around tomorrow's earnings reaction.

**Position sizing:** META is at **6.16%** (holdings.md), inside the 6–8% band. Room to the 8% ceiling: **1.84pp**. No forced trim or top-up.

---

## 12. Portfolio Note

META at 6.16% is comfortably under the 15% hard cap (Upgrade 7) and sits within the 6–8% full-position band its Composite Score points to. No portfolio-level action is forced by this score (no trim signal — nowhere near the 70+ trim bands; no forced top-up — R/R and price-limit both still fail, though R/R's underlying gap has narrowed materially). This session does not change the `holdings.md` weight itself, only Last Score/Quality Score/Composite Score/Last Review. **The unauthorized 6→5 share reduction flagged in override-log.md (§3) is a separate, open issue for this position — not resolved or investigated further by this rescore.**

---

## 13. Next Review Triggers

- **Q2 2026 earnings — tomorrow, 29 Jul 2026 (after close).** The natural, imminent checkpoint: refreshes every carried TTM fundamental in this log (§3), is highly likely to include management commentary on both AI-infrastructure JVs (El Paso/BlackRock and Louisiana/Blue Owl) and could bring an FY26 capex guidance revision — itself a second, independent Rule 9 trigger if it happens. **A post-earnings re-score is expected within 1–2 business days regardless of outcome.**
- **Buy-price / fair-value watch — the sharpest-narrowing item this session.** Live price is now only 14.55% above the $518.56 buy limit (was 26.98% on 07-13) and has fallen back below the PW Fair Value itself. If the post-earnings reaction pushes the price down further, this is the closest META has come to a price-limit-qualifying entry since the Upside/Downside Modifier was introduced — worth checking immediately after the earnings print, not waiting for a routine cadence.
- **Rate Gate watch:** Step 1 FAILED again this session, but by a narrower margin (+0.65% cushion vs +0.32% on 07-13, i.e. closer to passing) — worth rechecking if the 10Y moves further or the price/EPS mix shifts again.
- **Rule 9 fundamental triggers (standing):** any guidance revision, management change, material M&A, or a >15% unexplained price move.
- **holdings.md weight discrepancy (6.16% now vs. 6.65% cited in the trigger brief) — unresolved, flagged for a manual follow-up session** (see §3/§4; not something `/rescore` can investigate — needs `get_account_trades`, tracked in override-log.md).
- **5yr PE reconstruction (Data Gap #2) and Owner Earnings methodology decision (Data Gap #1)** — both still open, 10th consecutive session. This session's failure mode changed from "module not installed" to "Yahoo Finance rate-limiting persisted despite a working proxy/session workaround" — worth trying again next session with a longer cooldown before the first request, or sourcing 5yr PE from a different provider if the rate-limiting recurs.

---

## 14. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output; **2 new terms added this session**, marked below)

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
| **Joint Venture (JV)** *(new)* | A separate legal entity jointly owned and funded by two or more companies to pursue a specific project, with ownership/economics split by agreed percentage rather than one party fully owning and consolidating it — often used to push most of a project's funding, including debt, onto the JV's own balance sheet. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NTM** | Next Twelve Months. |
| **Off-balance-sheet financing** *(new)* | Structuring an asset or project so its funding (particularly debt) sits on a separate legal entity's balance sheet — e.g. a joint venture — rather than the sponsoring company's own, so the sponsor's own reported leverage ratios don't reflect the project's full debt load. |
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

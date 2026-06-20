# RESCORE — META — 2026-06-20

**Task type:** RESCORE (single ticker)
**Date:** 20 Jun 2026
**10Y US Treasury Yield:** 4.46% (latest available, 18 Jun 2026 — Federal Reserve H.15 / CNBC US10Y via web search; the Fed's next H.15 release is 22 Jun, so 18 Jun is the most current published constant-maturity figure)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** META **38.5** (2026-06-12, current 0–100.0 scale — [sessions/2026-06-12-rescore-msft-meta.md](2026-06-12-rescore-msft-meta.md))
**New this session:** This is the first META rescore to apply the **Upside/Downside Modifier** (Expected-Return Modifier), added to the valuation score on 2026-06-20 — see [valuation-scoring.md](../framework/valuation-scoring.md#upsidedownside-modifier-expected-return-modifier).

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow (operating cash flow minus capital spending); EV = enterprise value (market value of equity plus net debt — what it would cost to buy the whole business); EBIT = earnings before interest and tax (operating profit); EV/EBIT = enterprise value divided by operating profit; PE = price-to-earnings ratio; forward PE = price divided by *next-12-months* expected earnings; PEG = PE divided by earnings growth rate; D&A = depreciation and amortization (the non-cash charge for using up long-lived assets); capex = capital expenditure (spending on property, plant, equipment, servers); Owner Earnings = Buffett's cash-profit measure = net income + D&A − maintenance capex; MoS = margin of safety (discount to fair value demanded before buying); R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ PE); IRR = internal rate of return.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$577.22** | `yfinance` intraday (`currentPrice`/`fast_info.lastPrice`), pulled this session 20 Jun 2026 |
| Prior close | $567.58 | `yfinance` (`previousClose`) — live quote is +1.70% / +$9.64 above it |
| 52-week range | **$520.26 – $796.25** | `yfinance` (`fiftyTwoWeekLow`/`High`) |
| Analyst consensus PT (price target) | **~$825–$839** (mean ~$827–$839; median ~$825; range to $860 street-high) | Web search aggregation (stockanalysis.com, public.com, Cantor $860, Wells Fargo $752) — used only as a bull-case sanity check per Rule 0 Step 4 |

**Rule 0 fallback note:** the preferred source — Interactive Brokers `get_price_snapshot` (conid 107113386, META Class A on NASDAQ, resolved via `search_contracts`) — was **permission-denied** this session, so I fell back to `yfinance` intraday per the prompt's fallback ladder. The quote is a live intraday figure, not a stale prior-session close.

Price vs prior session: $567.76 (12 Jun) → $577.22 = **+1.67%** — well inside the 15% Rule 9 threshold, so no fundamental-event trigger from price alone; the move is folded into the re-score via the refreshed market cap.

---

## 2. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved; raw FCF used (4th consecutive session).** Upgrade 1 (mandatory for META) says: if growth capex >30% of total capex, replace FCF with **Owner Earnings = Net Income + D&A − *maintenance* capex**. The trigger is clearly met — FY2025 capex was **$69.69B against D&A of only $18.62B** (`yfinance` cashflow), i.e. capex is ~3.7× the depreciation run-rate, so the large majority is *growth* (new-capacity) spending, not maintenance. **But META does not disclose a maintenance-vs-growth capex split**, and CLAUDE.md prohibits inventing one. As in the 06-07/06-11/06-12 sessions, I used **raw TTM FCF** as the scored FCF input and flag the gap. **Note this is the conservative choice:** the only defensible Owner-Earnings proxy (treating maintenance capex ≈ D&A) would give OE ≈ net income $70.63B → OE yield 5.57% → FCF_Score 44.3 (vs 63.99 on raw FCF), making META score *cheaper*, not more expensive. Using raw FCF therefore does not flatter the result. This is now the **4th consecutive session** flagging this — recommend a `decisions/` entry to either formally suspend Upgrade 1 for non-disclosers or adopt the D&A proxy as the approved method.

2. **TTM (trailing-twelve-month) fundamentals carried from the 2026-06-12 roll-forward.** META's Q2 2026 results are not out until late July, so the most recent *filed* TTM figures are unchanged since 12 Jun (TTM EBIT $88.62B, TTM net income $70.63B, TTM FCF $45.65B, TTM D&A $20.72B — all derived in the prior session from the FY2025 10-K + Q1 2025/Q1 2026 filings). Only **price/market cap/EV** and the **forward PE & 5yr PE anchor** are refreshed this session. Refreshing fundamentals would require Q2 data that does not yet exist — flagged rather than guessed.

3. **5yr-average PE now auto-computed from `yfinance` (new method, 2026-06-20).** Replaces the prior session's manually-sourced trailing-10yr-avg PE (26.86×). Reconstructed a 20-quarter (≈5yr) trailing-PE series from `get_earnings_dates` TTM EPS paired with contemporaneous prices: **5yr avg PE 23.59×** (range 9.26×–36.01×, n=20). The 9.26× low reflects the 2022 ad-recession trough; I used the **average** in the fallback formula (the framework's common case), not the wide low/high range, consistent with the documented method.

4. **Gross margin / ROIC / revenue-CAGR (Phase 01 quality-gate inputs)** — not re-collected; these don't feed the Phase 02 valuation score. Spot-checked via `yfinance`: gross margin 81.9%, return on equity 32.9%, revenue growth 33.1% — all comfortably intact, no quality-deterioration signal. Flagged as "not formally refreshed."

5. **Share count** ≈2.196B (Class A+B) carried from prior session. (`yfinance`'s `marketCap` field of $1,465B implies a ~2.54B share count and is inconsistent with `currentPrice × sharesOutstanding`; I used the filing-based 2.196B from the prior session's 10-Q work — market cap $1,267.6B — not the `yfinance` aggregate.)

---

## 3. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** 7.51% (per [holdings.md](../portfolio/holdings.md), last sync)

| Item | Value | Source |
|---|---|---|
| Live price | $577.22 | `yfinance` intraday (§1) |
| Shares outstanding | ≈2.196B | Prior-session 10-Q cover (Data Gap #5) |
| Market Cap | 2.196B × $577.22 = **$1,267.6B** | Computed |
| Cash + marketable securities | $81.180B | Q1 2026 balance sheet (prior session) |
| Senior-note debt | $58.748B | Same (operating leases excluded per EV convention) |
| Net cash | $81.180B − $58.748B = **$22.43B net cash** | Computed |
| **EV** | $1,267.6B − $22.43B = **$1,245.17B** | Computed |
| **TTM EBIT** | **$88.621B** | Prior-session roll-forward (Data Gap #2) |
| **EV/EBIT** | $1,245.17B ÷ $88.621B = **14.05×** | Computed |
| **TTM FCF (raw — scored input)** | **$45.65B** | Prior-session roll-forward |
| **FCF Yield** | $45.65B ÷ $1,267.6B = **3.6013%** | Computed |
| TTM Net Income | $70.629B | Prior-session roll-forward |
| TTM D&A | $20.719B | Prior-session roll-forward |
| FY2025 capex / D&A | $69.69B / $18.62B (capex ≈3.7× D&A → growth-heavy → Upgrade 1 triggers, Data Gap #1) | `yfinance` cashflow |
| FCF/NI conversion | $45.65B ÷ $70.63B = **64.6%** | Computed — below 70%, explained by elevated AI/datacenter growth capex (Phase 04 carve-out), not a quality red flag. (`yfinance` annual FCF/NI 2022–2025: 83.1% / 112.7% / 86.7% / 76.3% — the TTM dip is the capex ramp, not deteriorating cash conversion.) |
| Forward PE (NTM) | **15.93×** | `yfinance` `forwardPE` (forward EPS $36.25) |
| 5yr avg PE (trailing, auto-computed) | **23.59×** (range 9.26–36.01×, n=20q) | `yfinance` reconstruction (Data Gap #3) |
| EPS growth (Fast-Grower test) | FY2023 NI $39.10B → FY2024 $62.36B (**+59.5%**, low-comp "Year of Efficiency" base) → FY2025 $60.46B (**−3.0%**) | `yfinance` financials — **FAILS** >15%-for-3-consecutive-years |
| Net Debt/EBITDA | net cash → **−0.20×** | Computed — no leverage concern (Upgrade 5 easily passed) |
| Shareholder return (FY2025) | Buybacks $26.25B + dividends $5.32B | `yfinance` cashflow |
| Last Score / Last Review | 38.5 / 12 Jun 2026 | Prior session |

---

## 4. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 15.93 = 6.2794%
Spread = EY − 10Y Treasury = 6.2794% − 4.46% = +1.8194%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+1.8194%, ~0.32pp above the bar) → **no additive.**

> **This is a change from the prior session, exactly as that session's "watch" note predicted.** On 12 Jun the spread was +1.2237% (FAIL, +5 additive) — flagged then as the closest-to-passing reading in the book. Two things moved it over the line: forward PE fell (17.32× → 15.93×, lifting the earnings yield) and the 10Y yield ticked down (4.55% → 4.46%). **The Step 1 +5 additive is removed this session.**

**Step 2 — Rate Regime Modifier**
10Y = 4.46% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +5** (down from +10 last session — the entire change is the Step 1 flip to PASS).

---

## 5. META — Full Score Calculation

**FCF Yield — 40% weight** (raw FCF used; Owner-Earnings proxy would score *cheaper* — Data Gap #1)
```
FCF_Score = clamp(100 × (1 − 3.6013 / 10), 0, 100) = 63.9871
```
→ Contribution: 63.9871 × 0.40 = **25.5948**

**EV/EBIT — 40% weight** (PEG not applicable → its 15% redistributed here, 25%+15%)
```
EV/EBIT_Score = clamp((14.05 − 12) / 23 × 100, 0, 100) = 8.9152
```
→ Contribution: 8.9152 × 0.40 = **3.5661**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (15.93 − 23.59) / 23.59 × 100 = −32.493%
FwdPE_Score = clamp(50 + (−32.493) × 2.5, 0, 100) = clamp(−31.23, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**
(The fallback formula already folds in the Historical PE Modifier — no separate ±10 applied, per the doc's anti-double-count note.)

**PEG — Fast-Grower test: FAIL.** EPS growth was +59.5% in FY2023→FY2024 (a low-comp "Year of Efficiency" rebound, a one-off cost-cutting effect — not organic compounding), then **−3.0% in FY2024→FY2025**. This does not clear ">15% EPS growth for 3+ consecutive years on a clean base." **PEG is not applicable; its 15% weight is redistributed to EV/EBIT** (used above). Consistent with the 2026-06-20 clarification and all prior META sessions.

**Raw weighted score:**
```
= 25.5948 + 3.5661 + 0.0
= 29.1609
```
**+ Rate Modifier (+5) = 34.1609** *(before the Upside/Downside Modifier)*

---

## 6. META — Upside/Downside Modifier (Expected-Return Modifier) — REQUIRED

Built entirely from scenario fair-value work (Rules 7 + 10) — no new data source.

**Step 1 — Scenario fair values (Rule 7 — bear case underwritten honestly).**
Applied a forward-PE multiple to a scenario EPS. The bear case explicitly underwrites the prompt's two key risks — heavy AI/Reality Labs capex compressing margins, and the AI-monetization payoff failing to arrive — via *both* an EPS miss and a multiple de-rate.

| Scenario | Weight | EPS assumption | Exit PE | Fair Value | Rationale |
|---|---|---|---|---|---|
| **Bull** | 25% | $40.0 | 24× | **$960** | AI ad-targeting tools + Reels/Advantage+ lift ad pricing; capex starts showing ROI. Kept *below* the $860 street-high implied FV to stay defensible. |
| **Base** | 50% | $36.25 (consensus NTM) | 20× | **$725** | Consensus earnings, multiple slightly below the 23.6× 5yr average (capex drag discount). |
| **Bear** | 25% | $28.0 | 13× | **$364** | Ad-cycle softening + AI/Reality Labs capex overruns depress margins, and the market de-rates a "capex black hole" narrative (the honest bear). |

```
PW Fair Value = 0.25×960 + 0.50×725 + 0.25×364 = $693.50
```
Sanity check (Rule 0 Step 4 / Rule 4): PW FV $693.50 sits **below** the ~$825 analyst consensus PT and the bull-case $960 is below the $860 street-high — so the blend is conservative, not rosy.

**Step 2 — Gap, annualization, components.**
```
Gap Upside %   = ($693.50 ÷ $577.22) − 1                    = +20.14%
Catalyst window = 2 years  (no narrower documented window — see Step 3)
Annualized gap  = 20.14% ÷ 2                                = +10.07%/yr
Intrinsic growth = +12.0%/yr   (durable FCF/EPS CAGR — deliberately well below the +31.9%
                                one-year forward-EPS pop of $36.25/$27.48−1, normalized per Rule 6)
Shareholder yield = buyback yield + dividend yield
                  = $26.25B/$1,267.6B + $5.32B/$1,267.6B    = 2.07% + 0.42% = +2.49%/yr
```
```
E (expected annual return) = 10.07 + 12.0 + 2.49 = +24.56%/yr
```

**Step 3 — Catalyst / timeline (Rule 10 + Guardrail 1).** Documented catalysts within the 18–24-month window: (a) **AI ad-monetization proof points** — Advantage+ / Llama-driven ad-targeting and GenAI ad tools converting capex into ad-revenue growth, visible quarter-by-quarter starting with **Q2 2026 earnings (late July 2026)**; (b) **capex-ROI demonstration** — the market re-rating once the heavy datacenter build shows a return rather than reading as an open-ended drain. Both are identifiable well inside 18–24 months → **upside credit is allowed; the −5 catalyst cap does NOT apply.**

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
E = 24.56% ≥ H → M = −15 × clamp((24.56 − 10) / 15, 0, 1)
                    = −15 × clamp(0.9707, 0, 1)
                    = −15 × 0.9707
                    = −14.56
```
**Upside/Downside Modifier M = −14.6** (rounded for reporting; −14.56 used in the sum).

**Robustness / honesty check (the bear case really was underwritten):** even on this deliberately harsh bear ($364 FV, −37% downside in the bear leg) the *probability-weighted* expected return clears +24%, just shy of the +25% that maxes the modifier at −15. And the action band is robust across the **entire** modifier range — with raw+rate fixed at 34.16, the score lands between **19.2** (M = −15) and **49.2** (M = +15), so META stays in the BUY bands no matter how the forecast breaks. The modifier sharpens *where* in the BUY range it sits; it does not manufacture the BUY signal.

---

## 7. META — Final Score & Action

```
Final Score = Raw weighted (29.1609) + Rate Modifier (+5) + Upside/Downside Modifier (−14.56)
            = 19.60
```
Boundary rule: not a ".X5" → standard rounding → **Final Score = 19.6**

# Final Score: 19.6 → Action band: BUY — Full position 6–8% (Score 0.0–29.9)

**Action category vs prior: CHANGED.** Prior score 38.5 sat in the 30.0–49.9 "BUY — Standard 3–5%" band; 19.6 now sits in the **0.0–29.9 "BUY — Full position 6–8%"** band. The drop is driven by two things, both of which moved this session:
1. **Rate Gate Step 1 flipped FAIL → PASS** (−5 to the score) — forward PE fell and the 10Y yield ticked down.
2. **The new Upside/Downside Modifier (−14.6)** — META's probability-weighted expected return (~+24.6%/yr: a 20% gap to a conservative fair value, plus durable ~12% intrinsic growth, plus ~2.5% shareholder yield) is near the top of the scale, which is exactly the "wonderful business with strong expected return pulled toward the buy band" behaviour the modifier was built to deliver.

**Practical recommendation (unchanged in substance from prior sessions): HOLD — no automatic fresh capital.** META is an **existing holding at 7.51%**, already at the top of (indeed at) the 6–8% full-position band the score now points to, and comfortably under the 15% hard cap (Upgrade 7). The score says "this is a high-conviction BUY-quality name," not "mechanically add today." Because the band crossed into BUY-full **and** an order setup is now warranted by the band, I produce the full order setup below — but adding capital remains a deliberate decision for the investor given the position is already at the band's ceiling and there is no *new* fundamental trigger (earnings/guidance) this session, only the price/rate/modifier mechanics.

---

## 8. META — Order Setup (Score in BUY band → required)

Confidence: wide-moat proven compounder, but heavy in-flight capex → use the **standard 20% MoS** floor for a Score 0.0–29.9 high-quality name (Rule 8 / order-setup table: 15–20% → take the conservative 20% given the capex uncertainty).

```
[x] Valuation Score (incl. Upside/Downside Mod): 19.6   (≤49.9 ✓ — entry permitted)
[x] Expected annual return E / catalyst window:  +24.6% / 2yr
[x] Upside/Downside Modifier applied:            −14.6
[x] Blended Fair Value (PW, Rule 7):             $693.50
[x] Margin of Safety %:                          20%
[x] BUY PRICE (limit):     $693.50 × (1 − 0.20)        = $554.80
[x] PRIMARY SELL TARGET:   = Blended FV                = $693.50
[x] BULL-CASE TRIM TARGET: $960 × 0.90                 = $864.00
[x] STOP LOSS:             $554.80 × (1 − 0.25)        = $416.10   (25% max loss, Score 0–29.9 high-conviction)
[x] Risk/Reward Ratio:     ($693.50 − $554.80) ÷ ($554.80 − $416.10) = $138.70 ÷ $138.70 = 1.00:1
```

> **R/R FAILS the 2:1 minimum at the buy-price entry.** At the $554.80 limit the reward to the primary sell target ($693.50) exactly equals the risk to the stop ($416.10) — **1.0:1**, below the 2:1 floor (Rule 6). Two readings, both pointing the same way: (a) using the **bull-case trim target** ($864) as the upside instead gives ($864 − $554.80) ÷ $138.70 = **2.23:1**, which passes — so the trade clears 2:1 *only* if you underwrite to the bull case, not the base-case sell target; (b) the live price ($577.22) is **above** the $554.80 buy-price limit, so there is **no entry today** regardless. **Net: set a limit at $554.80; do not buy at market.** The 1.0:1 base-case R/R is the honest flag that, at a 20% MoS off a fair value this far below the current price, the *base-case* margin is thin — the upside is real but front-loaded into the bull scenario, which is consistent with "underwrite the downside first."

**Position sizing (shown for completeness; META is already a 7.51% holding):** at a portfolio risk budget of 1.5% and risk-per-share of $138.70 ($554.80 − $416.10), risk-based size = (Portfolio × 1.5%) ÷ $138.70 shares. The binding constraint is the **6–8% allocation cap** for a Score 0–29.9 name (Step 5 "take the lower of risk-based size and cap"); META at 7.51% is **already inside that 6–8% band**, so the cap-based room for *new* capital is ~0–0.5pp before bumping the 8% top of the band. No fresh-capital action is forced.

---

## 9. Portfolio Note

META at 7.51% is comfortably under the 15% hard cap and now sits *within* the 6–8% full-position band its score points to. No portfolio-level action triggered; no trim signal (score is a BUY, nowhere near the ≥70 trim bands).

---

## 10. Next Review Triggers

- **Next earnings — META Q2 2026 (quarter ending June 2026), expected late July 2026** → routine post-earnings re-score (refreshes the TTM fundamentals carried in Data Gap #2, and the AI-monetization/capex-ROI catalyst in §6 gets its first real data point).
- **Rule 9 fundamental triggers:** any guidance revision (especially a FY capex-guidance change — the bear case hinges on capex), management change, material M&A, or a >15% unexplained price move.
- **Rate Gate watch:** Step 1 now PASSES with only ~0.32pp of cushion (+1.82% vs +1.50%). If forward PE rises or the 10Y yield climbs back toward 4.6%+, Step 1 could flip back to FAIL (+5 would return; final would rise ~5pts toward the standard-BUY band).
- **Owner Earnings (Upgrade 1) methodology decision** — open for a 4th session (Data Gap #1); recommend a `decisions/` entry.

# RESCORE — META — 2026-06-26

**Task type:** RESCORE (single ticker)
**Date:** 26 Jun 2026
**10Y US Treasury Yield:** 4.38% (TradingEconomics, dated 26 Jun 2026 — down from 4.50% used in the 06-23 session; still in the "3.5–5%" bracket → Rate Regime Modifier Step 2 unchanged at +5)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** META **18.0** (2026-06-23, BUY — Full position 6–8% — [sessions/2026-06-23-rescore-meta.md](2026-06-23-rescore-meta.md))
**Gap since last review:** 3 days (Tuesday→Friday). No earnings due in that window (next is META Q2 2026, expected late July 2026).

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow (operating cash flow minus capital spending); EV = enterprise value (market value of equity plus net debt — what it would cost to buy the whole business); EBIT = earnings before interest and tax (operating profit); EV/EBIT = enterprise value divided by operating profit; PE = price-to-earnings ratio; forward PE = price divided by *next-12-months* expected earnings; PEG = PE divided by earnings growth rate; D&A = depreciation and amortization (the non-cash charge for using up long-lived assets); capex = capital expenditure (spending on property, plant, equipment, servers); Owner Earnings = Buffett's cash-profit measure = net income + D&A − maintenance capex; MoS = margin of safety (discount to fair value demanded before buying); R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ PE); IRR = internal rate of return; NTM = next twelve months.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$549.47** | IBKR `get_price_snapshot` (contract_id 107113386, META Class A / NASDAQ), pulled this session 26 Jun 2026, 20:37:55 UTC (~4:37pm ET) |
| Prior close | $542.87 (derived) | IBKR's direct `prior_close` field returned empty on this pull; derived from the `change` field (+$6.60 / +1.22%): $549.47 − $6.60 = $542.87 |
| 52-week range | **$520.26 – $794.42** | IBKR `misc_statistics` — identical to 06-23, confirms no new high/low set |
| Year-to-date change | **−16.69%** | IBKR `year_to_date_change` (vs −15.01% on 06-23 — YTD loss widened as price fell further) |
| Analyst consensus PT | ~$825–$840 (no change identified since 06-23) | Web search aggregation — bull-case sanity check only (Rule 0 Step 4) |

Price vs 06-23 session: $560.52 → $549.47 = **−1.97%**. No fundamental-event trigger from price alone (well inside the 15% Rule 9 threshold).

---

## 2. Rule 9 Trigger Check (2026-06-23 → 2026-06-26)

Explicitly checked each Rule 9 category via web search for the 3-day window:

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Next report is META Q2 2026, expected late July 2026 — unchanged |
| Guidance revision | No | FY2026 capex guidance ($125–145B) remains the late-April figure — no new revision this window |
| M&A | **Checked — does not qualify** | Meta's $900M investment for a ~20% stake in Indian fintech Cred was announced **2026-06-22** — one day *before* the 06-23 session's own window started, so it is not a fresh event for this 3-day check. Even on its own merits: a $900M minority stake is ≈0.07% of META's ~$1.2T market cap — immaterial by size, not the kind of "material M&A" Rule 9 contemplates. |
| Management change | **Checked — does not qualify** | The Cred deal came bundled with a WhatsApp leadership change: CEO Will Cathcart stepping down (moving to a new internal AI-products role) and Cred founder Kunal Shah taking over as global WhatsApp head — also announced **2026-06-22**, before this window. It is also a *divisional* head change (WhatsApp), not Meta Platforms' own CEO/CFO — the same bar the 06-23 session applied to the "AI for Work" group-lead departure. Flagged here for visibility since it's a higher-profile change than that prior one, but it does not meet the Rule 9 threshold (predates window + wrong organizational level). |
| Macro shift | No | 10Y ticked down from 4.50% → 4.38%, still inside the same "3.5–5%" Rate Regime bracket — not a regime shift |
| >15% unexplained price move | No | −1.97% over 3 days, far under threshold |

**Conclusion: no Rule 9 trigger fired in this window.** Other news scanned and found non-qualifying: a $299 in-house AI smart-glasses launch (product news), Threads crossing 500M MAU (product milestone), and continued analyst commentary on AI-capex/"bubble" anxiety (sentiment/narrative, not a disclosed fundamental event — explicitly excluded by the framework). This is a routine, schedule-free re-score driven only by price drift and the small Treasury move.

---

## 3. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** 7.22% (per [holdings.md](../portfolio/holdings.md) — not recomputed this session)

### Carried unchanged from the 06-23 session (filed fundamentals — no new quarter reported)

| Item | Value | Why carried |
|---|---|---|
| TTM EBIT | $88.621B | No new quarter since 06-23 (Q2 2026 isn't out until late July) |
| TTM FCF (raw — scored input) | $45.65B | Same — Owner Earnings (Upgrade 1) still unresolved, see Data Gap below |
| TTM Net Income | $70.629B | Same |
| TTM D&A | $20.719B | Same |
| Cash + marketable securities | $81.180B | Same (Q1 2026 balance sheet) |
| Senior-note debt (excl. operating leases, per EV convention) | $58.748B | Same |
| Net cash | $81.180B − $58.748B = **$22.432B** | Computed, unchanged |
| Shares outstanding | ≈2.196B | Same (10-Q cover) |
| FCF/NI conversion | $45.65B ÷ $70.629B = **64.6%** | Unchanged |
| Net Debt/EBITDA | −0.20× (net cash position) | Unchanged — no leverage concern |
| 5yr avg PE (auto-reconstructed) | 23.589× (range 9.255×–36.014×, n=20q) | Carried — see Data Gap #3 below for why it wasn't re-run live this session |

### Refreshed this session (price-dependent)

| Item | 06-23 value | 06-26 value (fresh) | Computation |
|---|---|---|---|
| Live price | $560.52 | **$549.47** | IBKR snapshot (§1) |
| Market Cap | $1,230.90B | **2.196B × $549.47 = $1,206.6361B** | Computed |
| EV | $1,208.47B | **$1,206.6361B − $22.432B = $1,184.2041B** | Computed |
| **EV/EBIT** | 13.6364× | **$1,184.2041B ÷ $88.621B = 13.3626×** | Computed |
| **FCF Yield** | 3.7087% | **$45.65B ÷ $1,206.6361B = 3.7832%** | Computed |
| Forward PE | 15.4626× | **$549.47 ÷ $36.25 (carried fwd EPS — see Data Gap #2) = 15.1578×** | Computed at fresh live price |

### Fast-Grower (PEG eligibility) test — re-verified, still fails

FY2023 NI $39.10B → FY2024 $62.36B (+59.5%, low-comp rebound, a one-off) → FY2025 $60.46B (−3.0%). This is a multi-year filed-earnings history check that cannot change inside a 3-day window. **Still FAILS** ">15% EPS growth for 3+ consecutive years on a clean base." **PEG not applicable; its 15% weight redistributed to EV/EBIT** (making EV/EBIT 40% total) — unchanged from every prior META session.

---

## 4. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved; raw FCF used (6th consecutive session).** META does not disclose a maintenance-vs-growth capex split. As before, raw FCF is the **conservative** choice (the OE proxy, maintenance capex ≈ D&A, would score the stock *cheaper*, not more expensive). The standing recommendation to resolve this via a `decisions/` entry remains open.
2. **Forward-EPS consensus ($36.25, NTM) is now 3 sessions old (sourced from `yfinance`'s `forwardPE` field on 06-20) and diverges from today's independently cross-checked figures.** Live web search this session (GuruFocus, stockanalysis.com) shows a forward PE of ~17.0–17.1× as of 06-23 and a calendar-2026 consensus EPS of ~$32.2–32.8 — both notably below our carried $36.25/15.16× pair. This is plausibly a vendor-methodology difference (NTM rolling estimate vs. calendar-FY2026 estimate, which would understate a still-growing EPS base), but it has now gone three consecutive sessions without a fresh, sourced pull. **Continuing to carry $36.25 this session** (no earnings event has occurred to justify a mid-cycle change, and substituting an unsourced number would violate the "never invent data" rule just as much as inventing one outright) — but flagging this explicitly and recommending the next full earnings-driven rescore (late July 2026) do a fresh, sourced consensus-EPS pull rather than carry forward a 4th time.
3. **5yr PE reconstruction not re-run live via `yfinance` this session** — the same `curl_cffi`/TLS proxy error encountered earlier today in the MSFT 06-26 session (`OPENSSL_internal:invalid library`) applies here too. Carrying forward 06-23's figures (23.589×/9.255×/36.014×, n=20 quarters) is defensible because the next earnings print (Q2 2026, late July) hasn't landed — the 20-quarter rolling window is unchanged from 06-23's own verification that it hadn't shifted since 06-20.
4. Gross margin/ROE/revenue-growth quality spot-checks not re-collected as Phase 01 inputs this session (same posture as 06-20/06-23) — they don't feed the Phase 02 score.
5. IBKR's direct `prior_close` field returned empty on this pull; prior close was derived from the `change` field instead (see §1).

---

## 5. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 15.1578 = 6.5973%
Spread = EY − 10Y Treasury = 6.5973% − 4.38% = +2.2173%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+2.2173%, **~0.72pp of cushion** — wider than 06-23's ~0.47pp) → **no additive.**

> The cushion widened further: forward PE fell to 15.16× (from 15.46×) as price dropped, while the 10Y also eased (4.50%→4.38%) — both effects raise the spread. Gate remains comfortably PASS.

**Step 2 — Rate Regime Modifier**
10Y = 4.38% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +5** (unchanged from 06-23).

---

## 6. META — Full Score Calculation

**FCF Yield — 40% weight** (raw FCF; Owner-Earnings proxy would score *cheaper* — Data Gap #1)
```
FCF_Score = clamp(100 × (1 − 3.7832 / 10), 0, 100) = 62.1676
```
→ Contribution: 62.1676 × 0.40 = **24.8670**

**EV/EBIT — 40% weight** (PEG not applicable → its 15% redistributed here, 25%+15%)
```
EV/EBIT_Score = clamp((13.3626 − 12) / 23 × 100, 0, 100) = 5.9242
```
→ Contribution: 5.9242 × 0.40 = **2.3697**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (15.1578 − 23.589) / 23.589 × 100 = −35.7421%
FwdPE_Score = clamp(50 + (−35.7421) × 2.5, 0, 100) = clamp(−39.355, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — Fast-Grower test: FAIL** (re-verified §3). PEG's 15% weight redistributed to EV/EBIT (used above).

**Raw weighted score:**
```
= 24.8670 + 2.3697 + 0.0
= 27.2367
```
**+ Rate Modifier (+5) = 32.2367** *(before the Upside/Downside Modifier)*

---

## 7. META — Upside/Downside Modifier (Expected-Return Modifier)

**Decision: carry forward the 06-20/06-23 scenario framework's EPS/exit-PE assumptions.** No fundamental change occurred in this window (§2) and the two documented catalysts (AI ad-monetization proof points at Q2 2026 earnings, capex-ROI demonstration) are unchanged and still inside the 18–24 month window. Recomputed below at the new live price only.

**Step 1 — Scenario fair values (Rule 7, carried EPS/exit-PE assumptions)**

| Scenario | Weight | EPS assumption | Exit PE | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | $40.0 | 24× | **$960.00** |
| **Base** | 50% | $36.25 (consensus NTM — Data Gap #2) | 20× | **$725.00** |
| **Bear** | 25% | $28.0 | 13× | **$364.00** |

```
PW Fair Value = 0.25×960.00 + 0.50×725.00 + 0.25×364.00 = $693.50   (unchanged — same EPS/PE inputs)
```
Sanity check (Rule 0 Step 4 / Rule 4): PW FV $693.50 remains below the ~$825–840 analyst consensus PT.

**Step 2 — Gap, annualization, components (recomputed at new live price)**
```
Gap Upside %    = ($693.50 ÷ $549.47) − 1                  = +26.2125%
Catalyst window = 2 years (unchanged)
Annualized gap  = 26.2125% ÷ 2                              = +13.1063%/yr
Intrinsic growth = +12.0%/yr   (carried, unchanged basis)
Shareholder yield = buyback yield + dividend yield (recomputed at fresh market cap $1,206.6361B)
                  = $26.25B/$1,206.6361B + $5.32B/$1,206.6361B  = 2.1755% + 0.4409% = +2.6164%/yr
```
```
E (expected annual return) = 13.1063 + 12.0 + 2.6164 = +27.7226%/yr
```

**Step 3 — Catalyst / timeline (Rule 10 + Guardrail 1).** Same two catalysts as 06-23, both still inside the 18–24-month window. **Upside credit fully allowed; the −5 catalyst cap does NOT apply.**

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
E = 27.7226% ≥ H → M = −15 × clamp((27.7226 − 10) / 15, 0, 1)
                      = −15 × clamp(1.1818, 0, 1)
                      = −15 × 1.0000
                      = −15.0000
```
**Upside/Downside Modifier M = −15.0** — remains at the ceiling (same as 06-23's −15.0; E moved further past the +25%/yr saturation line as the price drop widened the gap to an unchanged fair value).

**Robustness check:** with raw+rate fixed at 32.2367, the score's full range across the entire ±15 modifier band is **17.2** (M=−15) to **47.2** (M=+15) — META stays in a BUY band (Full or Standard) across the entire possible range of this modifier, same conclusion as every prior session.

---

## 8. META — Final Score & Action

```
Final Score = Raw weighted (27.2367) + Rate Modifier (+5) + Upside/Downside Modifier (−15.0)
            = 17.2367
```
Boundary rule: not a ".X5" → standard rounding → **Final Score = 17.2**

# Final Score: 17.2 → Action band: BUY — Full position 6–8% (Score 0.0–29.9)

**Action category vs prior session: UNCHANGED.** 18.0 (06-23) → 17.2 (06-26) — both land in the **0.0–29.9 "BUY — Full position 6–8%"** band. The −0.8 point move is **entirely mechanical and fully attributable to the raw weighted sub-score** (28.0111 → 27.2367, a −0.7744 move): the price drop (−1.97%) cheapened both the FCF-yield and EV/EBIT multiples (each 40%-weighted), while both additive modifiers held steady — Rate Gate Step 1 was already PASSing (cushion simply widened further) and the Upside/Downside Modifier was already pinned at its −15.0 ceiling. No Rule 9 trigger fired (§2); this is the score mechanically responding to a 3-day price move, exactly as designed.

**Practical recommendation (unchanged in substance, but see the flagged development below): HOLD — no *automatic* fresh capital, but the buy-limit condition has now been met for the first time.** META is an existing holding at **7.22%**, inside the 6–8% full-position band the score points to, well under the 15% hard cap.

---

## 9. META — Order Setup (Score in BUY band → required)

Confidence: wide-moat proven compounder with heavy in-flight AI capex — same conservative 20% MoS as 06-20/06-23.

```
[x] Valuation Score (incl. Upside/Downside Mod): 17.2   (≤49.9 ✓ — entry permitted)
[x] Expected annual return E / catalyst window:  +27.7% / 2yr
[x] Upside/Downside Modifier applied:            −15.0
[x] Blended Fair Value (PW, Rule 7):             $693.50  (unchanged — same scenario inputs)
[x] Margin of Safety %:                          20%
[x] BUY PRICE (limit):     $693.50 × (1 − 0.20)        = $554.80   (unchanged — FV unchanged)
[x] PRIMARY SELL TARGET:   = Blended FV                = $693.50
[x] BULL-CASE TRIM TARGET: $960.00 × 0.90               = $864.00
[x] STOP LOSS:             $554.80 × (1 − 0.25)        = $416.10   (25% max loss, Score 0–29.9 high-conviction)
[x] Risk/Reward Ratio (base-case target):  ($693.50 − $554.80) ÷ ($554.80 − $416.10) = $138.70 ÷ $138.70 = 1.00:1
[x] Risk/Reward Ratio (bull-case trim target): ($864.00 − $554.80) ÷ $138.70 = $309.20 ÷ $138.70 = 2.23:1
```

> **🚩 Headline development: live price ($549.47) has now crossed BELOW the $554.80 buy-price limit for the first time across the tracked sessions** — by $5.33 (0.96%). For context, 06-23 had price sitting $5.72 (1.0%) *above* the limit (the closest approach up to that point); 06-26 is the first session where the price condition itself is actually satisfied. **However, this is a separate gate from the R/R check, and the R/R check still fails:** the base-case Risk/Reward ratio remains **1.00:1 against the primary sell target (fails the 2:1 minimum)**; it only clears 2:1 (**2.23:1**) if underwritten specifically to the bull-case trim target, not the base case. **Net: per the framework's standard practice (R/R must be verified against the primary target, consistent with how 06-20 and 06-23 treated this identical 1.00:1/2.23:1 split), this is still not an *automatic* qualifying entry** — even though the price-limit condition is now met. This is a judgment call worth the user's attention: a discretionary entry at/near $549.47, underwritten to the bull case only, is now mechanically available; the framework's automatic trigger is not.

**Position sizing:** META is already at **7.22%**, inside the 6–8% allocation band for a Score 0.0–29.9 name. Room to the band's 8% ceiling: **0.78pp**. Unchanged from 06-23.

---

## 10. Portfolio Note

META at 7.22% is comfortably under the 15% hard cap (Upgrade 7) and sits within the 6–8% full-position band its score points to. No portfolio-level action is forced by this score (no trim signal, no forced top-up — R/R still fails at the base case). This session does not change the holdings.md weight — that update is handled by the orchestrator.

---

## 11. Next Review Triggers

- **Next earnings — META Q2 2026 (quarter ending June 2026), expected late July 2026** → routine post-earnings re-score (refreshes TTM fundamentals carried since 06-12, and gets a fresh, sourced forward-EPS consensus pull — see Data Gap #2).
- **Rule 9 fundamental triggers:** any guidance revision, management change *at the Meta Platforms CEO/CFO level*, material M&A, or a >15% unexplained price move.
- **Rate Gate watch:** Step 1 passes with ~0.72pp of cushion — wider than 06-23's ~0.47pp — but still bears watching if forward PE rises or the 10Y climbs.
- **🚩 Buy-price watch (elevated from "proximity" to "condition met"):** live price ($549.47) is now **below** the $554.80 limit for the first time. Worth a fresh check before the next scheduled review regardless of date, since this is the most actionable the order setup has been across four sessions — the open question is whether a discretionary, bull-case-underwritten entry is warranted given the base-case R/R still fails.
- **Forward-EPS consensus refresh (Data Gap #2)** — the carried $36.25 NTM figure is now 3 sessions/6 days old and diverges from independently-sourced current figures (~$32.2–32.8 CY2026 consensus); resolve with a fresh sourced pull at the next full rescore.
- **Owner Earnings (Upgrade 1) methodology decision** — open for a 6th consecutive session (Data Gap #1).
- **Monitoring (non-triggering):** the WhatsApp CEO change (Cathcart → Shah) and the $900M Cred stake (both 2026-06-22) — worth watching for any follow-on strategic/financial disclosure, but neither meets the Rule 9 bar today.

---

## Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **bps / pp (percentage points)** | A direct difference between two percentages (e.g. margin falling from 42% to 39% is a 3pp drop) — distinct from a "%" change. |
| **Buyback yield** | The rate at which a company's share count shrinks per year from repurchasing its own stock, net of new issuance — a component of shareholder yield. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense for using up long-lived assets. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit. |
| **EPS** | Earnings Per Share. |
| **EV** | Enterprise Value — market cap + net debt. |
| **EV/EBIT** | Enterprise Value ÷ EBIT — a cheapness multiple independent of capital structure. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years — this framework's PEG-eligibility trigger. |
| **FCF** | Free Cash Flow. |
| **FCF Yield** | FCF ÷ Market Cap — higher is cheaper. |
| **FCF/NI conversion ratio** | FCF ÷ Net Income — checks whether accounting profit is becoming real cash. |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV (Fair Value)** | The analyst's estimate of intrinsic worth, independent of market price. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against. |
| **IRR** | Internal Rate of Return. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NTM** | Next Twelve Months — a rolling forward window (as opposed to a fixed calendar/fiscal year). |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for moat-building reinvestors (Upgrade 1; unresolved for META, see Data Gap #1). |
| **PE (Price-to-Earnings) ratio** | Share price ÷ EPS. |
| **PEG ratio** | PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **PW (Probability-Weighted) Fair Value** | 25% bull + 50% base + 25% bear blended fair value (Rule 7). |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate** | The pre-check run before every score, comparing earnings yield to the 10Y Treasury and applying a regime modifier. |
| **Rate Regime Modifier** | Additive −10 to +10 score adjustment based on the 10Y Treasury bracket. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

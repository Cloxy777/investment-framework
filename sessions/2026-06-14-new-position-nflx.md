# NEW POSITION (Fresh Re-Evaluation) — NFLX (Netflix, Inc.) — 2026-06-14

**Task type:** NEW POSITION (fresh full re-evaluation of an existing holding — part of the 2026-06-14 multi-ticker batch `/new-position NFLX AVGO MELI FICO DASH MA`; this session covers NFLX only)
**Date:** 14 Jun 2026 (Sunday — US markets closed; most recent close is Fri 12 Jun 2026)
**10Y US Treasury Yield:** 4.49% (CNBC/TradingEconomics, Fri 12 Jun 2026 close)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current NFLX portfolio weight:** **1.83%** — currently HELD (IBKR), per [holdings.md](../portfolio/holdings.md); Last Score 63.2, Last Review 12 Jun 2026
**Sector:** Communication Services — Streaming Media & Entertainment

**Context:** A full `/new-position`-style fresh re-evaluation was run **2 days ago** ([2026-06-12 session](2026-06-12-new-position-nflx.md), score **63.2**, HOLD — watch only, no new entry, no trim; blended FV ≈ $71.02 vs price $81.27). Per the orchestrator's instructions, this session re-derives Phase 01/02 for **today** rather than copying the prior numbers, after first checking for any new fundamental trigger since 12 Jun.

---

## 0. Check for New Fundamental Triggers Since 12 Jun 2026

Searched for Netflix news (earnings, guidance, M&A, management changes) dated between 12–14 Jun 2026:

- **Netflix's 2026 Annual Meeting of Stockholders was held 4 Jun 2026** — Reed Hastings (co-founder, Executive Chairman) did not stand for re-election to the board (announced 10 Apr 2026, effective at the 4 Jun meeting); Jay Hoag became the new independent Chairman. **This predates the 12 Jun session** (which itself postdates the 4 Jun meeting) — not a new trigger this session, and in any case this is a board-chair transition (Hastings already transitioned from CEO to Executive Chairman in 2023; co-CEOs Ted Sarandos and Greg Peters are unchanged), not the CEO/CFO-level "management change" Rule 9 trigger.
- **No new earnings release, guidance revision, or M&A announcement found** between 12 Jun and 14 Jun 2026. FY2026 guidance (revenue $50.7–51.7B, operating margin 31.5%, ad revenue ~doubling to $3B) remains as reported at Q1 2026 and referenced in the 12 Jun session.
- **No 8-K filings found in this window** beyond the routine 4 Jun annual-meeting voting-results 8-K (already accounted for above).

**Conclusion: no new Rule 9 fundamental trigger since the 12 Jun session.** Proceeding with a fresh Rule 0 price pull and full Phase 01/02 re-derivation using the same underlying fundamentals (revenue, FCF, EBIT, shares, net debt, consensus EPS, 10yr avg PE) sourced and verified 2 days ago — only the **price-dependent** sub-score inputs (market cap, EV, FCF yield, EV/EBIT, forward PE) are recomputed against today's live price.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$80.34** | WebSearch aggregation (multiple sources converge): "Netflix (NFLX) stock closed at $80.34 on Friday, June 12, 2026, representing a decline of 1.14% from the previous day's closing price of $81.27." This is the most recent close (today, 14 Jun, is Sunday — markets closed). IBKR `search_contracts`/`get_price_snapshot` MCP tools returned a permission denial this session, so falling back to WebSearch per the framework's documented fallback path. |
| 52-week high | $134.12 | WebSearch aggregation (unchanged from 12 Jun session) |
| 52-week low | $75.01 (reached ~Feb 2026) | WebSearch aggregation (unchanged) |
| Analyst consensus PT (median) | **$114.56** (range $80.00–$151.40; 37 Buy / 12 Hold / 1 Sell) | WebSearch aggregation (stockanalysis.com-style consensus) — essentially unchanged from the 12 Jun session's $115.00 |

**Context:** NFLX closed **$80.34** on 12 Jun 2026, down **-1.14%** (-$0.93) from 11 Jun's $81.27 (the price used in the 12 Jun session). NFLX now trades **~40.1% below its 52-week high** ($134.12) and **~7.1% above its 52-week low** ($75.01). The move is a routine ~1% daily fluctuation, well within normal noise — not a Rule 9 ">15% unexplained move" trigger.

---

## 2. Data Inputs — Carried Forward from 12 Jun 2026 Session (No New Fundamental Data)

Per §0, no new fundamental data has emerged since the 12 Jun session. The following inputs are **carried forward unchanged** (all were sourced from primary filings/aggregators and verified 2 days ago — see [2026-06-12 session §2](2026-06-12-new-position-nflx.md#2-data-gathered-phase-01--phase-02-inputs--gaps-flagged) for full sourcing detail):

| Metric | Value | Source / Derivation (as of 12 Jun 2026 session) |
|---|---|---|
| FY2025 Revenue | $45.18B (+16% YoY) | Netflix Q4 2025 earnings release / 10-K |
| Revenue CAGR 3yr (FY2022→FY2025) | 12.51% | Computed |
| FY2025 Net income | $10.98B | Netflix Q4 2025 earnings release |
| FY2025 Net margin | 24.3% | Computed |
| FY2025 Gross margin | 48.5% | WebSearch aggregation |
| FY2025 Operating margin | 29.5% | Netflix Q4 2025 earnings release |
| **TTM EBIT** | **$13.275B** | Computed (FY2025 revenue × 29.5% op margin) |
| **FY2025 FCF** | **$9.5B** | Netflix quarterly 8-Ks, summed |
| FCF/NI conversion (FY2025) | 86.4% | Computed |
| Total debt (Q1 2026) | $14.361B | Netflix Q1 2026 10-Q |
| Cash + ST investments (Q1 2026) | $12.296B | Netflix Q1 2026 10-Q |
| **Net debt** | **$2.065B** | Computed |
| ROIC | 21.3–25.5% (range across sources/periods) | WebSearch aggregation |
| **Shares outstanding** (Q1 2026) | **4,212.79M** | Netflix Q1 2026 10-Q |
| 2026 consensus EPS | **$3.66** (range $3.19–$3.96) | WebSearch aggregation |
| **10yr avg PE** | **60.90×** (FinanceCharts), corroborated by 10yr median 61.19× (GuruFocus) | WebSearch aggregation |

### Recomputed Today (price-dependent — using $80.34 vs. 12 Jun's $81.27)

| Metric | 12 Jun 2026 ($81.27) | 14 Jun 2026 ($80.34) | Derivation |
|---|---|---|---|
| Market Cap | $342.37B | **$338.46B** | 4,212.79M × $80.34 |
| Enterprise Value | $344.44B | **$340.52B** | Market Cap + Net Debt ($2.065B) |
| **EV/EBIT** | 25.95× | **25.6513×** | EV ÷ TTM EBIT ($13.275B) |
| **FCF Yield** | 2.775% | **2.8069%** | FY2025 FCF ($9.5B) ÷ Market Cap |
| **Forward PE** | 22.20× | **21.9508×** | $80.34 ÷ $3.66 (2026 consensus EPS) |

### Data Gaps / Flags

No new data gaps. All Phase 01/02 fundamentals are unchanged from the 12 Jun session (which itself carried forward a clean, fully-sourced data set with no invented/estimated figures). Only the live price changed (a routine -1.14% daily move), which mechanically shifts the four price-dependent ratios above by a small amount in the "cheaper" direction (lower price → lower EV/EBIT, lower Forward PE, higher FCF yield).

---

## 3. Phase 01 — Quality Gate (Confirmed Unchanged)

| Check | NFLX Value | Threshold | Result |
|---|---|---|---|
| Net margin (FY2025) | 24.3% | >15% | ✅ PASS |
| ROIC | 21.3–25.5% | >15% | ✅ PASS |
| Revenue CAGR 3yr (FY2022→FY2025) | 12.51% | >10% | ✅ PASS |
| Gross margin | 48.5% | >40% | ✅ PASS |
| FCF positive 3 consecutive years | FY2023/24/25 all positive (FY2025 $9.5B) | required | ✅ PASS |
| Net debt/EBITDA | ~0.15× (net debt $2.065B vs EBITDA ≈$13.6B) | <2x | ✅ PASS |
| FCF/NI conversion ratio | 86.4% (FY2025) | >70% | ✅ PASS |
| Share issuance pattern | Share count roughly flat/declining (buybacks); non-dilutive | not dilutive | ✅ PASS |
| Moat signal | #1 global streaming platform (325M+ subscribers), $20B 2026 content budget, ad-tier scaling (250M+ MAU), password-sharing conversion complete | required | ✅ Qualitatively strong |

**Gate result: PASS — proceeding to Rate Environment Gate and Phase 02.** Nothing has changed in 2 days; confirmed via §0 (no new fundamental trigger).

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $80.34 / $3.66 = 21.9508×
EY     = 1 ÷ Forward PE = 1 ÷ 21.9508 = 4.5556%
Spread = EY − 10Y Treasury = 4.5556% − 4.49% = +0.0656%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.07%, far short of +1.5%) → **+5 additive applied**.

**Step 2 — Rate Regime Modifier**
10Y = 4.49% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for NFLX = +10** (+5 Step 1 fail + +5 Step 2)

---

## 5. Phase 02 — Full Score Calculation

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.8069 / 10), 0, 100)
          = clamp(100 × (1 − 0.28069), 0, 100)
          = clamp(71.931, 0, 100)
          = 71.931
```
→ Contribution: 71.931 × 0.40 = **28.7724**

**EV/EBIT — weight 40% (PEG not applicable, redistributed — NFLX is not a Fast Grower, per the 12 Jun session's Gap #4: FY2024 EPS declined YoY vs. FY2023, failing the ">15% EPS growth for 3+ years" test)**
```
EV/EBIT_Score = clamp((25.6513 − 12) / 23 × 100, 0, 100)
              = clamp(13.6513 / 23 × 100, 0, 100)
              = clamp(59.353, 0, 100)
              = 59.353
```
→ Contribution: 59.353 × 0.40 = **23.7413**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (21.9508 − 60.90) / 60.90 × 100 = −63.956%
FwdPE_Score = clamp(50 + (−63.956) × 2.5, 0, 100)
            = clamp(50 − 159.89, 0, 100)
            = clamp(−109.89, 0, 100)
            = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — not applicable (not a Fast Grower, confirmed unchanged from 12 Jun session).** Weight redistributed to EV/EBIT above.

**Raw weighted score:**
```
= 28.7724 + 23.7413 + 0.0 = 52.5137
```
**+ Rate Modifier (+10) = 62.5137**

Boundary rule: 62.5137 is not exactly on a ".X5" boundary (it's 62.5137, between 62.5 and 62.6, closer to 62.5) → standard round to nearest 0.1 → **Final Score = 62.5**

---

## 6. Final Score & Action

# Final Score: 62.5 → Action: HOLD — watch only, no new entry, no trim ("Fair Value")

This is a **small decrease from the 12 Jun score of 63.2** (Δ = −0.7), and the **action category is unchanged** — both 63.2 and 62.5 fall in the 50.0–69.9 "Fair Value" band.

**Driver of the change:** Purely the **-1.14% price move** ($81.27 → $80.34) over the two days, with **zero change to underlying fundamentals**:
- FCF yield rose slightly (2.775% → 2.8069%) as the lower price makes the same $9.5B FCF a marginally larger yield → FCF_Score fell slightly (72.25 → 71.93), i.e. marginally *cheaper*.
- EV/EBIT fell slightly (25.95× → 25.65×) on the lower EV → EV/EBIT_Score fell (60.64 → 59.35), i.e. marginally *cheaper*.
- Forward PE fell slightly (22.20× → 21.95×) → FwdPE_Score remains a clean, robust **0.0** (Deviation now −63.96% vs. −63.54%, both far past the −20% clamp threshold).
- Rate Modifier unchanged at +10 (10Y treasury 4.46% → 4.49%, still squarely in the 3.5–5% bracket for Step 2; Step 1 spread still ~0.07%, still <1.5% → still fails).

Net effect: every sub-score moved in the "cheaper" direction by a small amount (consistent with the price decline), but the **Forward PE sub-score was already floored at 0.0** and the FCF/EV-EBIT moves are too small to shift the action category. **This is a routine 2-day mark-to-market update, not a re-rating.**

---

## 7. Fair Value & Position Sizing (Existing Holding — Hold Band)

Per the operating brief: Score 50.0–69.9 → "No MoS → Watchlist only" / "Hold — watch only, no new entry, no trim." A full order-setup (buy price / stop loss / R/R) is **not required** for a Hold-band score.

### Step 1 — Fair Value (Blended)

The blended Fair Value depends on FCF, EBIT, growth assumptions, WACC, shares, and net debt — **none of which changed** in the 2 days since the 12 Jun session (only the market price moved). The 12 Jun session's blended FV computation is therefore **carried forward unchanged**:

```
Blended FV = 40% × DCF(PW $62.80) + 60% × Multiples(avg $76.49)
           = $25.12 + $45.89
           = $71.02
```

(Full DCF scenario table, multiples comps, and historical-PE cross-check: see [2026-06-12 session §7](2026-06-12-new-position-nflx.md#7-fair-value--position-sizing-existing-holding--hold-band).)

**Cross-check vs. today's price:** Current price ($80.34) sits **~13.1% above** Blended FV ($71.02) — down slightly from the 12 Jun gap (~14.4%) due to the price decline, but still **no margin of safety**. Consistent with a Fair-Value/Hold score.

**Cross-check vs. external estimates:** Blended FV ($71.02) remains below both the analyst consensus PT ($114.56) and the historical-PE cross-check (~$121, unchanged) — same conservative-framing rationale as documented in the 12 Jun session (our blended FV uses current, compressed comparables rather than NFLX's hyper-growth-era multiples).

### Step 2 — No Order Setup (Hold Band)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Step 2 integration table: **Score 50.0–69.9 → No MoS → Watchlist only.** No Buy Price, Sell Target, Stop Loss, or R/R calculation is computed.

### Step 3 — Current vs. Target Position Size

| | Value |
|---|---|
| Current NFLX weight | **1.83%** of portfolio (≈ $53,855.83 × 1.83% ≈ $985.58) |
| Target weight under current score (50.0–69.9 band) | **No new-entry target — hold at current size** |
| 15% hard cap (Upgrade 7) headroom | 13.17pp of headroom remains — **not a binding constraint either direction** |
| Gap vs. target | **None to report** — Score 62.5 implies neither a buy target (Score <50.0) nor a trim trigger (Score ≥70.0) |

**No sizing action implied by this score.**

---

## 8. Qualitative Assessment

No change from the 12 Jun session — see [2026-06-12 session §8](2026-06-12-new-position-nflx.md#8-qualitative-assessment-5-questions--disruption-vector-check) for the full 5-questions + disruption-vector writeup (margins driven by content-amortization scale economics + ad-tier monetization; moat = global content scale + personalization + distribution; capital allocation track record includes the disciplined WBD bid walk-away with $2.8B termination fee collected; growth sources = advertising doubling, international subscriber growth, pricing, live/sports/gaming; bear case = password-crackdown tailwind exhaustion + content-cost diminishing returns; disruption vector = GenAI content creation, a two-sided vector not a one-directional thesis-breaker).

**Catalyst & timeline (Rule 10):** Unchanged from 12 Jun — the ~13% gap is price *above* our blended FV (no "cheap vs. fair" gap to close in NFLX's favor). Next 2–3 quarters (Q2 2026 ~Jul 2026, Q3 2026 ~Oct 2026) will clarify ad-revenue pacing toward the $3B 2026 target, whether full-year operating margin guidance (31.5%) holds, and post-password-crackdown subscriber growth trends.

---

## 9. Recommendation

# **HOLD — no new entry, no trim. Score 62.5 (Fair Value), unchanged action category from prior 63.2.**

NFLX continues to pass Phase 01 cleanly across every criterion (24.3% net margin, 21–25% ROIC, 12.5% revenue CAGR, 48.5% gross margin, FCF/NI conversion 86.4%, net debt/EBITDA ~0.15×) — confirmed unchanged via the §0 fundamental-trigger check. Phase 02 lands at **62.5** — solidly within the 50.0–69.9 "Fair Value" band, which carries **"Hold — watch only, no new entry, no trim"** under the current Action Table.

**Comparison to 12 Jun session (63.2):**
- The action category is **unchanged** (both 63.2 and 62.5 are "Fair Value / Hold").
- The **-0.7 point decrease** is entirely attributable to NFLX's **-1.14% price decline** ($81.27 → $80.34) over the two days — every sub-score shifted marginally cheaper, as expected when price falls with fundamentals held constant. This is **not** a fundamentals-driven re-rating.
- No new Rule 9 trigger identified (§0): no earnings, guidance revision, M&A, or CEO/CFO-level management change since 12 Jun. The 4 Jun board-chair transition (Hastings → Hoag) predates the 12 Jun session and is a board-level, not executive-level, change.

**Sizing:** NFLX remains at **1.83%** of the portfolio — no target to size against in the Fair Value band. Position is neither underweight relative to a buy signal nor overweight relative to a trim trigger. 15% hard cap (Upgrade 7) is not binding (13.17pp headroom).

**Blended Fair Value ($71.02, unchanged) sits ~13.1% below the current price ($80.34)** — no margin of safety, consistent with Hold.

All final-decision authority rests with the human investor per the operating brief.

---

## 10. Next Review Trigger

- **Q2 2026 earnings** (expected ~mid-to-late July 2026) — mandatory re-score (Rule 9). Specifically check: (a) whether the 2026 ad-revenue doubling ($3B target) stays on track, (b) whether Q2 operating margin comes in at/above the guided 32.6% (vs. 34.1% YoY — a deceleration already flagged), (c) any update to post-password-crackdown subscriber growth trends.
- **>15% unexplained price move from $80.34 in either direction** — immediate re-score per Rule 9.
- **WBD termination-fee deployment** (capital allocation signal — buybacks vs. content spend vs. new M&A) — management-change/M&A-class Rule 9 trigger if a new large transaction is announced.
- **No position change executed by this session** — recommendation only (Hold at current 1.83%). If the human investor takes any action, log it in `decisions/` per CLAUDE.md Rule 10.

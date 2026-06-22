# NEW POSITION — AVGO (Broadcom Inc.) — 2026-06-20

**Task type:** NEW POSITION
**Date:** 20 Jun 2026
**10Y US Treasury Yield:** 4.49% (WebSearch: TradingEconomics/CNBC, 19 Jun 2026 — most recent available; unchanged vs the 2026-06-14 session)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current AVGO portfolio weight:** 0% — not currently held (exited before the last sync; not on [holdings.md](../portfolio/holdings.md))
**Sector:** Semiconductors (fabless — custom AI accelerators/ASICs, networking silicon) + Infrastructure Software (VMware)

> **Why this re-run:** AVGO's last evaluation (2026-06-14, score 69.5) predates the new **Upside/Downside Modifier** (Expected-Return Modifier) added 2026-06-20. This session refreshes prices and applies that modifier, and re-examines two judgment calls the modifier and a clarified rule force open: (1) the VMware-amortization distortion of GAAP earnings, and (2) the Fast-Grower/PEG eligibility ruling on a distorted earnings base.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$405.05** | **Interactive Brokers MCP `get_price_snapshot`** (conid 313130367, NASDAQ/SMART), live intraday `last`, not halted. **IBKR tool access restored this session** (it was permission-denied on 2026-06-14). |
| Bid / Ask | $405.03 / $405.42 | IBKR snapshot |
| Intraday change | −1.53% on the day | IBKR snapshot |
| 52-week range | $242.77 – $495.00 | IBKR `misc-statistics` (52w low/high); cross-checks the prior session's $241.11–$495.00 |
| Analyst consensus PT | **$523.84** (45 analysts), rating "Strong Buy" | yfinance `targetMeanPrice` / `recommendationKey` |
| Prior-session price (14 Jun) | $382.07 | for reference — AVGO is **+6.0% over 6 days** (below the 15% Rule-9 re-score threshold; this re-run is rule-driven, not price-driven) |

**Context:** $405.05 sits ~18% below the 52-week high ($495) and ~67% above the 52-week low ($242.77) — upper-middle of the range, ~23% below the consensus PT ($524). The +6% drift since 14 Jun is small and not a trigger by itself.

⚠️ **Tooling note:** IBKR `get_price_snapshot`/`search_contracts` worked cleanly this session (denied on 2026-06-14). Live price is therefore from the framework's preferred Rule-0 source. Fundamental data (financials, cash flow, PE history) is from **yfinance** + SEC 8-K/10-Q figures carried forward from the 2026-06-14 session (re-verified against yfinance where possible). No metric was invented or estimated.

---

## 2. Data Gathered (Phase 01 & 02 Inputs)

Most fundamentals are carried forward from the 2026-06-14 session (sourced to Broadcom 8-K/10-Q filings) and re-verified against yfinance this session. New this session: a **reconstructed 5-year PE low/high range** (the prior session only had a 10-year *average*), refreshed FCF/NI ratios, and shareholder-return figures.

### Core financials (yfinance, FY ends ~late Oct)

| FY | Revenue | GAAP Net Income | GAAP EBIT | FCF | FCF/NI |
|---|---|---|---|---|---|
| FY2022 | $33,203M | $11,495M | $14,171M | $16,312M | 142% |
| FY2023 | $35,819M | $14,082M | $16,719M | $17,633M | 125% |
| FY2024 | $51,574M | $5,895M | $13,869M | $19,414M | **329%** |
| FY2025 | $63,887M | $23,126M | $25,939M | $26,914M | **116%** |

FCF/NI (free cash flow ÷ net income — a cash-quality check) is far above the 70% gate for both of the last two years. FY2024's 329% is an artifact of VMware-acquisition charges crushing that year's GAAP net income while cash flow was largely unaffected.

### Snapshot metrics (yfinance, live)

| Metric | Value |
|---|---|
| Market cap | $1,957.0B |
| Net debt | $45,279M ($64,907M total debt − $19,628M cash) |
| Enterprise value (EV = market cap + net debt) | $2,002.3B |
| Forward PE (price ÷ next-12-months expected EPS) | 21.22× |
| Trailing PE | 68.4× |
| EV/EBITDA | 47.6× |
| ROIC (return on invested capital) | ~24% (carried fwd) / ROE 37.3% |
| Gross margin | 76.3% (yf TTM) / 67.8% (FY2025 GAAP) |
| Net margin | 38.8% |
| Net debt / EBITDA | ~1.05× (vs $43B adj. EBITDA) |
| Dividend rate / yield | $2.60 / ~0.63% |

### GAAP earnings distortion — VMware purchase-amortization (Rule 6 "normalize before you value")

FY2025 amortization of VMware-acquisition intangibles ≈ **$9.3B/year, non-cash** ($6,031M in cost of revenue + $3,244M in G&A). This is the central data issue for AVGO:
- It depresses **GAAP EBIT and GAAP EPS by ~35–40%**, which mechanically inflates EV/EBIT and the trailing PE.
- It does **not** touch FCF (it is a non-cash add-back), so FCF and FCF-yield are clean.
- It is the reason the four sub-scores split into a "maximally expensive" camp (FCF yield, EV/EBIT — anchored on cash and GAAP EBIT) and a "cheap" camp (forward PE, PEG — anchored on forward/non-GAAP earnings).

### 5-year PE range (NEW — reconstructed via yfinance, n=20 quarters 2021–2026)

Using the framework's documented method (rolling trailing-4-quarter reported EPS × contemporaneous price): **5yr avg 30.0×, low 13.4×, high 52.9×.** This is a genuine low/high *range*, so the FwdPE **primary formula** applies this session (the 2026-06-14 session only had a 10-yr average → had to use the fallback formula). Most recent reconstructed trailing PE (Jun 2026) ≈ 51.5×.

### Shareholder return (FY2025, yfinance cash-flow statement)

- Dividends paid: $11,142M
- Buybacks: $6,310M
- **But diluted share count is *rising*** (FY2023 4,270M → FY2024 4,778M → FY2025 4,853M) — VMware stock issuance and stock-based comp outweigh buybacks, so **net buyback yield ≈ 0** (arguably slightly negative). Shareholder yield = dividend ~0.63% + net buyback ~0% ≈ **0.6%**. (Not dilutive in the "red-flag" sense — the share growth is the one-time VMware deal working through — but it is *not* a net-buyback tailwind, so I do not credit one in the expected-return calc.)

### Data gaps / flags
1. Fundamentals largely carried forward from 2026-06-14 (8-K/10-Q sourced) and re-verified vs yfinance — no new quarter has been reported since (last report Q2 FY2026, 3 Jun 2026).
2. GAAP EBIT depressed ~35–40% by ~$9.3B/yr VMware amortization — handled explicitly in the EV/EBIT sub-score below (both raw and normalized shown).
3. Net buyback ≈ 0 (share count rising) — shareholder-yield component of expected return credited at ~0.6% (dividend only).
4. No metric invented or estimated.

---

## 3. Phase 01 — Quality Gate

| Check | AVGO Value | Threshold | Result |
|---|---|---|---|
| Net margin | 38.8% (TTM) / 36.2% (FY25) | >15% | ✅ PASS (>2×) |
| ROIC | ~24% | >15% | ✅ PASS |
| Revenue CAGR 3yr (FY22→FY25) | 24.4% | >10% | ✅ PASS (>2×) |
| Gross margin | 67.8% GAAP FY25 (76.3% yf TTM) | >40% or expanding | ✅ PASS |
| FCF positive 3 consecutive yrs | FY23 $17.6B / FY24 $19.4B / FY25 $26.9B | required | ✅ PASS |
| Net debt/EBITDA | ~1.05× | <2× | ✅ PASS |
| FCF/NI conversion 2yr | FY24 329% / FY25 116% | >70% for 2+ yrs | ✅ PASS |
| Share issuance | One-time VMware issuance (Nov 2023), now net flat-ish + buyback program | not dilutive (red-flag sense) | ✅ PASS |
| Moat signal | Custom-ASIC/AI-accelerator partner to hyperscalers (Google TPU, Meta, others), networking-silicon leadership (Tomahawk/Jericho), VMware switching costs | required | ✅ present |

**Gate result: PASS — decisively, on all 8 criteria** (several by >2×). Unchanged from 2026-06-14. Proceeding to scoring.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = 21.22×
Earnings Yield (EY) = 1 ÷ 21.22 = 4.71%
Spread = EY − 10Y Treasury = 4.71% − 4.49% = +0.22%
```
Spread (+0.22%) < +1.5% → fails → **+5 additive** (yellow flag, not a veto).

**Step 2 — Rate Regime Modifier**
10Y = 4.49% → 3.5–5% bracket → **+5**

**Combined Rate Modifier: +10**

---

## 5. Phase 02 — Full Valuation Score

### FCF Yield (40% weight)
```
FCF (TTM)   = $27,212M
Market Cap  = $1,957,031M
FCF Yield   = 27,212 / 1,957,031 = 1.39%
FCF_Score   = clamp(100 × (1 − 1.39/10), 0, 100) = 86.10
```
**Owner-Earnings lens (Upgrade 1):** does **NOT** apply. AVGO is fabless — total capex is ~1% of revenue (immaterial), so raw FCF is not understated by growth-capex treatment the way it is for MSFT/GOOGL/META/AMZN. FCF is also already the *cash* figure, so it is unaffected by the VMware amortization distortion — no normalization needed here. **FCF_Score = 86.10.**

### EV/EBIT (25% weight — but see PEG ruling; becomes 40%)
```
EV          = $2,002,309M
GAAP EBIT TTM = $30,443M   → EV/EBIT = 65.8×
GAAP EBIT FY25 = $25,939M  → EV/EBIT = 77.2×
EV/EBIT_Score (GAAP) = clamp((65.8 − 12)/23 × 100, 0, 100) = 100.0
```
**Rule 6 normalization (strip the ~$9.3B non-cash VMware amortization):**
```
Normalized EBIT TTM = 30,443 + 9,300 = 39,743M → EV/EBIT = 50.4×
Normalized EBIT FY25 = 25,939 + 9,300 = 35,239M → EV/EBIT = 56.8×
EV/EBIT_Score (normalized) = clamp((50.4 − 12)/23 × 100, 0, 100) = 100.0
```
**The amortization distortion is real and worth documenting, but it does not change the EV/EBIT sub-score:** even fully normalized (50.4×), EV/EBIT is far past the 35× = 100.0 ceiling. **EV/EBIT_Score = 100.0 either way** — I use this figure and note the normalization as a transparency item, not a score change. (This is the key nuance the prompt flagged: AVGO is "maximally expensive" on EV/EBIT *even after* the amortization fix; the distortion is not what's making EV/EBIT max out.)

### Forward PE + Historical PE Modifier (20% weight)
A genuine 5-year low/high range is available this session → **primary formula**:
```
Forward PE = 21.22×, 5yr Low = 13.4×, 5yr High = 52.9×
FwdPE_Score = clamp((21.22 − 13.4)/(52.9 − 13.4) × 100, 0, 100) = 19.80
```
**Historical PE Modifier (Upgrade 2)** — applies on the primary path. Forward PE 21.22× vs 5yr avg 30.0× = **−29.3% (>20% below)** → **−10**.
*Structural Quality Override check:* the override only blocks the **+10** "expensive" penalty; it does not block the **−10** "cheap" credit, so −10 stands.
```
FwdPE_Score = 19.80 − 10 = 9.80
```
**FwdPE_Score = 9.80.** (For reference, the fallback formula used on 2026-06-14 gave 0.00; the primary formula is less extreme and more accurate now that a real range exists.)

### PEG (15% weight) — Fast-Grower eligibility ruling

**Reported PEG = 0.75** (yfinance trailingPeg). Non-GAAP diluted EPS growth (from 2026-06-14 session): FY22→23 +12.2%, FY23→24 +14.9%, FY24→25 +40.5%; 3yr CAGR +21.9%. Forward AI growth is explosive (Q2 FY2026 AI revenue +143% YoY).

**RULING: PEG is NOT scored this session — its 15% weight is redistributed to EV/EBIT (→ EV/EBIT 40%).**

Reasoning, per the **clarified Fast-Grower note (2026-06-20)**: the "3+ years" eligibility requires a *"clean, non-distorted earnings base."* The clarification explicitly disqualifies an earnings base *"distorted by a one-off"* and names a non-cash distortion as exactly the case to exclude. **AVGO's GAAP EPS is distorted ~35–40% by ~$9.3B/yr of non-cash VMware amortization** — the textbook situation the rule was written to catch. Data-provider PEGs (the 0.75 figure) are computed off this distorted GAAP base (or an inconsistent GAAP/non-GAAP mix), so forcing a PEG off it would be scoring an unreliable input. The framework's instruction in this case is unambiguous: **redistribute PEG's 15% to EV/EBIT rather than force a PEG off an unreliable base.** This reverses the 2026-06-14 session's judgment call (which classified AVGO a Fast Grower and scored PEG) — the clarified rule, published 2026-06-20, now governs and points the other way.

*Sensitivity (not scored):* if one *did* score PEG on the non-GAAP base — non-GAAP EPS is clean, 3yr CAGR +21.9% >15%, so a non-GAAP Fast-Grower reading is defensible — PEG ≈ 0.75 → PEG_Score 12.38, weights 40/25/20/15. That path gives a **final of 61.6** (still "Fair Value, no new entry"). Recorded below is the rule-mandated redistribution (final 74.8). **Both readings produce the same action: do not enter.** The difference is only which side of the 70.0 line the score sits — moot for a new position (any score ≥50 is no-entry), but documented for the audit trail.

### Raw Weighted Score (recorded — PEG redistributed, EV/EBIT 40%)
```
Raw = (FCF 86.10 × 0.40) + (EV/EBIT 100.0 × 0.40) + (FwdPE 9.80 × 0.20)
    = 34.44 + 40.00 + 1.96
    = 76.40
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier) — REQUIRED

Built entirely from scenario fair-value work (Rules 7 + 10). Bear case underwritten honestly (Guardrail 2: scenario-weighted, never the rosy point).

**Step 1 — scenario fair values.** Implied next-12-month (NTM) EPS = price ÷ forward PE = $405.05 ÷ 21.22 = **$19.09**. Fair values built off NTM EPS power with a multiple range inside AVGO's own 5yr PE band (13.4–52.9×), and the bear case additionally haircuts the earnings base:

| Scenario | Wt | Assumption | EPS basis | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | AI ramp beats ($56B→>$100B FY27), re-rate | $19.09 × 1.10 = $21.0 | 34× | **~$714** |
| Base | 50% | Consensus AI ramp, multiple eases below 5yr avg | $19.09 | 25× | **~$477** |
| Bear | 25% | AI capex slowdown / hyperscaler in-sourcing → est. cuts ~15% **and** de-rate to low end | $19.09 × 0.85 = $16.2 | 15× | **~$243** |

The bear case lands at ~$243 — essentially the 52-week low ($242.77) — i.e. "if I'm wrong, the stock round-trips its entire AI re-rating." That is a genuine, fully-underwritten downside, not a token one.

```
PW Fair Value = 0.25×714 + 0.50×477 + 0.25×243 = $478
Gap Upside    = 478 / 405.05 − 1 = +18.0%
```
**Step 2 — catalyst & annualization (Rule 10).** Documented catalyst: management's reaffirmed FY2026 AI-semiconductor revenue guide of **$56B (~180% growth)** and an explicit **FY2027 >$100B** AI target backed by multi-year hyperscaler contracts (Q2 FY2026 release, 3 Jun 2026). Window to realize ≈ **2 years** (the FY2027 milestone). Guardrail 1 (catalyst required for upside credit) is **satisfied** — no −5 cap needed.
```
Annualized gap = 18.0% / 2 = 9.0%
```
**Step 3 — expected annual return E.**
```
E = annualized gap (9.0%) + intrinsic growth (12%, conservative durable EPS/FCF CAGR, below the near-term AI spike) + shareholder yield (~0.6%, dividend only — net buyback ≈ 0 as share count is rising)
  = 9.0% + 12.0% + 0.6% = +21.6%
```
**Step 4 — map E to M** (hurdle H = 10%):
```
E (21.6%) ≥ H → M = −15 × clamp((21.6 − 10)/15, 0, 1) = −15 × 0.773 = −11.6
```
**Upside/Downside Modifier M = −11.6.**

*Robustness:* even with deliberately conservative inputs (PW FV only $478 vs the $524 consensus PT, intrinsic growth held to 12% well under the near-term AI pace, zero buyback credit), E clears the hurdle decisively — the **intrinsic-growth term alone (12%) exceeds the 10% hurdle**. This is the gap the modifier was built for: a fast-compounding business whose forward earnings power the trailing-valuation sub-scores ignore.

---

## 7. Final Score

```
Final = Raw weighted + Rate Modifier + Upside/Downside Modifier
      = 76.40 + 10 + (−11.6)
      = 74.77  → rounds to 74.8
```

# **Final Score: 74.8 — "Expensive" (70.0–79.9 band)**

| Score band | Label | Action (Phase 03/05) |
|---|---|---|
| 50.0–69.9 | Fair Value | Hold / watchlist — no new entry |
| **70.0–79.9** | **Expensive** | **Do not buy. (Trim 25–30% if held — n/a, not held)** |

**Sensitivity:** the alternate PEG treatment (score PEG on the clean non-GAAP base) gives **61.6** ("Fair Value"). Both treatments = **no new entry**. Prior score (2026-06-14, pre-modifier): **69.5**.

**What the modifier did:** it *lowered* the score by 11.6 (strong expected return is attractive) — but the bottom-up valuation is rich enough (EV/EBIT saturated at 100, FCF yield ~1.4%) that even an 18% gap + 12% growth could not pull it into a buy band. The ±15 cap means the bright forward story *informs but does not override* the cheapness gate — working exactly as designed. AVGO is a wonderful business that is not cheap.

---

## 8. Order Setup — NOT PRODUCED (by design)

Order setup runs only for a BUY (score ≤49.9) or a TRIM (held position ≥70.0). AVGO is neither: 74.8 is "Expensive / do not buy" for a *new* position, and it is not held, so there is nothing to trim. The order-setup checklist gates on "Valuation Score ≤49.9 to enter" — not met. No DCF/buy/sell/stop levels are produced, consistent with not manufacturing levels for a trade the framework says not to make.

For reference only (other parties' reads, not this framework's order): consensus PT $523.84 (~+29% from $405.05); this framework's scenario-weighted PW fair value is ~$478 (~+18%). Neither is a standing trigger.

---

## 9. Recommendation

# **WATCHLIST ONLY / PASS — do not open a position now.**

AVGO clears Phase 01 decisively (one of the cleanest quality passes in this framework's recent history) and has a genuine, documented growth catalyst (AI-semiconductor revenue guided $56B FY2026 → >$100B FY2027). The new Upside/Downside Modifier correctly credits that forward earnings power, pulling the score down 11.6 points. **But it is not enough:** the stock is richly valued on every trailing/cash lens (FCF yield ~1.4%, EV/EBIT 50–65× even after stripping VMware amortization), and the final score of **74.8 ("Expensive")** carries no margin of safety for a new entry. This is the framework behaving as intended — a great company that is fully (arguably more than fully) priced for its bright future.

**Add/keep on the watchlist** with re-evaluation at:
- **Next earnings** (Q3 FY2026, ~Sept 2026) — re-run with refreshed TTM EBIT/FCF; watch whether the AI ramp lifts EBIT enough to move EV/EBIT off its ceiling, and whether VMware amortization begins rolling off.
- **A >15% unexplained price move** from $405.05 (Rule 9) — a decline toward the $243–290 area (52-week / recent low) would materially improve FCF yield and the entry math.
- Any guidance revision / M&A / management change (Rule 9).

---

## 10. Next Review Trigger

**Date/event:** AVGO's Q3 FY2026 earnings release (~September 2026) — re-run Phase 02 with refreshed TTM EBIT and FCF, re-check the VMware-amortization roll-off, and re-confirm the PEG-eligibility ruling. Earlier trigger if a >15% unexplained move from **$405.05** occurs (Rule 9), or any guidance/M&A/management-change event.

**No position opened — nothing to log in `decisions/`.**

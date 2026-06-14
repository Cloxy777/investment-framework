# NEW POSITION — PYPL (PayPal Holdings, Inc.) — 2026-06-14

**Task type:** NEW POSITION
**Date:** 14 Jun 2026
**10Y US Treasury Yield:** 4.49% (CNBC/TradingEconomics, market close Fri 12 Jun 2026 — most recent available; markets closed Sun 14 Jun)
**Rate Regime Modifier (would apply if scored):** +5 (10Y in the 3.5–5% bracket) — **not applied; Phase 01 gate fails before Phase 02 is reached**
**Current PYPL portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Financial Technology — Digital Payments (two-sided payments network: PayPal checkout, Venmo, Braintree, BNPL)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$41.24** | IBKR `get_price_snapshot` (contract 199169591, NASDAQ) — flagged `is_close: true` / prior close also $41.24, i.e. Friday 12 Jun 2026's close (today, 14 Jun, is Sunday — markets closed). Cross-checked via WebSearch: "PayPal (PYPL) had a closing price of $41.24 USD on June 12, 2026." |
| 52-week range | $38.34 – $79.08 (open 52w ago: $72.91) | IBKR `misc_statistics` |
| 13-week range | $40.20 – $52.30 | IBKR `misc_statistics` |
| Analyst consensus PT | ~$51.54 avg (range $32–$147.39; 8 buy / 4 sell → "Neutral"/"Moderate Buy" depending on aggregator) | WebSearch (Nasdaq/aggregator) |

**Context:** $41.24 sits **~48% below** the 52-week high ($79.08) and only **~7.6% above** the 52-week low ($38.34) — PYPL is trading near 52-week lows. One earlier WebSearch result returned a conflicting "$43.17, +1.28%" figure with an internally inconsistent day-range ($40.87–$41.59, which doesn't bracket $43.17); that figure was discarded in favor of the IBKR snapshot + the explicitly-dated "$41.24 close on June 12, 2026" result, which are mutually consistent.

---

## 2. Data Gathered (Phase 01 Inputs) & Gaps Flagged

| Metric | Value | Source / Derivation |
|---|---|---|
| FY2022 Net revenues | $27,518M | PayPal FY2022 10-K |
| FY2023 Net revenues | $29,771M (+8.2%) | PayPal FY2023 earnings releases |
| FY2024 Net revenues | $31,797M (+6.8%) | PayPal FY2024 earnings releases |
| FY2025 Net revenues | $33.2B (+4%) | PayPal Q4/FY2025 earnings release (3 Feb 2026) |
| Q1 2025 Net revenues | $7,791M | PayPal Q1 2025 8-K |
| Q1 2026 Net revenues | $8,350M (+7% YoY) | PayPal Q1 2026 8-K (5 May 2026) |
| **TTM Revenue** (FY2025 − Q1'25 + Q1'26) | **$33,759M** | Computed |
| **Revenue CAGR 3yr** (FY2022→FY2025) | **6.46%** = (33,200/27,518)^(1/3) − 1 | Computed |
| FY2024 GAAP Net income | $4,246M | PayPal FY2024 earnings releases |
| FY2025 GAAP Net income (EPS $5.41, +35%) | $5,230M | PayPal Q4/FY2025 earnings release |
| Q1 2025 GAAP Net income (EPS $1.29) | $1,287M | PayPal Q1 2025 8-K |
| Q1 2026 GAAP Net income (EPS $1.21, −6%) | $1,110M (−14% YoY) | PayPal Q1 2026 8-K |
| **TTM Net income** (FY2025 − Q1'25 + Q1'26) | **$5,053M** | Computed |
| **FY2025 Net margin** | 15.75% = 5,230/33,200 | Computed |
| **TTM Net margin** | **14.97%** = 5,053/33,759 | Computed |
| ROIC | ~21–24% (GuruFocus: 21.19% as of Feb 2026 / 21.96% TTM; StockAnalysis: 22.94%) | GuruFocus, StockAnalysis |
| WACC (for reference) | 11.67% | GuruFocus |
| Gross margin FY2022 | 42.3% | WebSearch aggregation |
| Gross margin FY2023 | 39.6% | WebSearch aggregation |
| Gross margin FY2024 | 40.5% (+2.4%) | WebSearch aggregation |
| Gross margin FY2025 | 41.5% (+2.3%) | WebSearch aggregation |
| FY2023 FCF | $4.2B | PayPal FY2023 earnings coverage |
| FY2024 FCF | $6.8B | PayPal FY2024 earnings coverage |
| FY2025 FCF | $5.6B (CFO $6.4B) | PayPal Q4/FY2025 earnings release |
| FCF/NI conversion FY2024 | 160.2% = 6.8/4.246 | Computed |
| FCF/NI conversion FY2025 | 107.1% = 5.6/5.23 | Computed |
| Total debt (Q1 2026, 31 Mar 2026) | $11.6B | PayPal Q1 2026 10-Q |
| Cash + investments (Q1 2026) | $13.5B | PayPal Q1 2026 10-Q |
| **Net debt** | **≈ −$1.9B (net cash)** | Computed |
| Credit ratings | A3 (Moody's) / A- (S&P) / A- (Fitch) — all investment grade, stable outlook | Moody's/S&P/Fitch via cbonds, TradingView |
| Shares outstanding (31 Mar 2026) | 892M | PayPal Q1 2026 10-Q |
| Share buybacks | ~34M shares for ~$1.5B in Q1 2026 alone | PayPal Q1 2026 8-K |
| Forward PE | ~8.5–10.4× (varies by source/date) | WebSearch aggregators |
| 10yr avg PE | ~28–39× depending on methodology; 10yr median 42.3×, 10yr range 7.45×–108.15×; 5yr avg ~27.25×; 3yr avg ~15.56×; current TTM PE ~7.7× | fullratio.com / financecharts / gurufocus |
| New CEO | Enrique Lores (ex-HP CEO, PYPL board member/chair since Jul 2024) became President & CEO effective 1 Mar 2026, succeeding Alex Chriss — Board cited execution pace "not in line with Board expectations." Reorganizing into 3 segments: Checkout Solutions & PayPal / Consumer Financial Services & Venmo / Payment Services & Crypto. | PayPal 8-K/DEF 14A filings, Q1 2026 earnings coverage |

### Data Gaps / Flags

1. **TTM Net Margin (14.97%) sits essentially exactly at the >15% threshold** — 0.03pp below on a TTM basis, while the FY2025 full-year figure (15.75%) clears it. This is a rounding-level ambiguity (the $33.2B FY2025 revenue figure itself is reported to only 3 significant figures), not a decisive failure either way — **not the binding gate failure** (see §3).
2. **FY2025 revenue ($33.2B, "+4%") is marginally inconsistent with FY2024 ($31,797M) × 1.04 = $33,069M** — a ~$130M / 0.4% rounding gap likely from the headline "+4%" being itself rounded. Using either figure, the 3yr CAGR lands in a **6.3–6.5%** band — does not change the gate outcome (both well below the 8%/10% thresholds).
3. **EBITDA figure not independently sourced** (only a forward-looking "EBITDA margin low-to-mid-22%" range was found). Immaterial to the gate: PayPal is in a **net cash position** (~−$1.9B), so Net Debt/EBITDA is negative/not meaningful and passes trivially under both the standard <2.5x (valuation-scoring.md pre-screen) / <2x (strategy.md) thresholds and Upgrade 5's <4x asset-light-financial threshold (PayPal also clears the investment-grade requirement: A3/A-/A-).
4. **No metric in this session was invented or estimated** — every figure traces to a specific 8-K/10-Q/10-K earnings release or a named aggregator (GuruFocus, StockAnalysis, fullratio), with derivations (CAGR, TTM roll-forwards, net debt, margins) shown explicitly above.

---

## 3. Phase 01 — Quality Gate

| Check | PYPL Value | Threshold | Result |
|---|---|---|---|
| Net margin | TTM 14.97% / FY2025 15.75% | >15% (strategy.md) / >12% (valuation-scoring.md pre-screen) | ✅ PASS (FY basis; TTM is at-threshold, flagged above) |
| ROIC | ~21–24% | >15% | ✅ PASS |
| **Revenue CAGR 3yr (FY2022→FY2025)** | **6.46%** (6.3–6.5% band, see Gap #2) | **>10% (strategy.md) / >8% (valuation-scoring.md pre-screen)** | ❌ **FAIL** |
| Gross margin | 41.5% (FY2025), expanding 2 consecutive years (39.6% → 40.5% → 41.5%) | >40% **or** structurally expanding (3yr trend) | ✅ PASS |
| FCF positive 3 consecutive years | FY2023 $4.2B / FY2024 $6.8B / FY2025 $5.6B — all positive | required | ✅ PASS |
| Net debt/EBITDA | Net **cash** position (~−$1.9B) | <2x (strategy.md) / <2.5x (pre-screen) / <4x if asset-light + IG (Upgrade 5) | ✅ PASS (trivially — net cash) |
| FCF/NI conversion ratio 2yr | FY2024 160.2% / FY2025 107.1% — both >70% | >70% for 2+ consecutive years | ✅ PASS |
| Share issuance pattern | Net **buybacks** (~34M shares / ~$1.5B in Q1 2026 alone); shares outstanding declining | not dilutive | ✅ PASS |
| Moat signal | Two-sided network (PayPal/Venmo/Braintree), strong brand recognition, ~$1.79T TPV (FY2025) | required | ✅ present, but see §5 — under competitive pressure |

**Gate result: FAIL** — on **one** decisive criterion: **Revenue CAGR 3yr**. Per the operating brief, this session **stops here** rather than proceeding to the Rate Environment Gate / Phase 02 scoring.

---

## 4. Gate Result: **FAIL** — Stopping Per Operating Brief

> "Walk the Phase 01 quality gate — if it fails, stop and report why rather than proceeding to scoring."

PYPL is, on almost every dimension, a **high-quality, highly profitable, cash-generative business**:

- ROIC ~21–24%, comfortably clearing the >15% bar
- Net margin ~15.0–15.8%, right at/above the >15% line
- Gross margin 41.5% and **expanding** for 2 consecutive years (39.6% → 40.5% → 41.5%) — a genuine structural-improvement signal
- FCF positive every year, with FCF/NI conversion **well above 100%** in both FY2024 (160%) and FY2025 (107%) — earnings quality is excellent, not a "non-cash-income" story
- **Net cash balance sheet** (~−$1.9B net debt) with investment-grade ratings (A3/A-/A-) across all three agencies
- Aggressive, non-dilutive **share buybacks** (~$1.5B in Q1 2026 alone)

But it fails decisively on the framework's **Growth** criterion: **Revenue CAGR 3yr of ~6.46%**, against a **>10% threshold in strategy.md** (and even the more permissive **>8% pre-screen threshold in valuation-scoring.md**). This isn't a marginal miss — it's **~3.5pp below the strategy.md bar** and **~1.5–1.7pp below even the looser pre-screen bar**. The trend, if anything, has been **decelerating**: FY2023 +8.2% → FY2024 +6.8% → FY2025 +4% (with a possible partial reacceleration to +7% in Q1 2026 — see §5).

### Did the Turnaround Sub-Gate (Upgrade 4) open an alternate path?

No — and more fundamentally, it doesn't fit the situation. Upgrade 4 is for businesses **"failing 2–4 quality criteria"** that may qualify as a Conditional Watch (2–3% max) if all five conditions (historical ROIC >15% for ≥5 of 10 years, insider buying >$500K, ≥40% MOS, Net Debt/EBITDA <3×, identifiable moat) are met. PYPL fails **only one** Phase 01 criterion (Growth) — it isn't a "Fallen Angel" with broken fundamentals; it's a profitable, high-ROIC, FCF-rich **mature platform whose top-line growth has structurally decelerated**. The Turnaround Sub-Gate's premise (a business that needs to *prove its way back* to quality) doesn't describe PYPL, whose quality metrics are largely intact — only its growth rate has fallen below the framework's bar.

---

## 5. Why This Is Close — and What Would Flip the Verdict

PYPL is the textbook **"statistically cheap, structurally decelerating"** case this framework's Growth filter exists to separate from genuine mispricings:

- **Valuation looks extreme on every classic multiple**: TTM PE ~7.7× vs a 10yr median of ~42×, 5yr average ~27×, and even 3yr average ~15.6× — PYPL trades at a **~50–70% discount** to its own recent history on a PE basis. Forward PE ~8.5–10.4× implies a single-digit-to-low-double-digit earnings multiple for a company with ~15% net margins and ~22% ROIC.
- **Net cash, investment-grade, buying back stock aggressively** — capital allocation and balance sheet are both clean.
- **New CEO (Enrique Lores, effective 1 Mar 2026)** replacing Alex Chriss, explicitly because the Board judged execution pace insufficient — PayPal is reorganizing into three focused segments (Checkout/PayPal, Consumer Financial Services/Venmo, Payment Services & Crypto). This is a **Rule 9 management-change trigger** in its own right, and the kind of catalyst that *could* reaccelerate growth — but per Rule 0/9, the framework acts on **realized** fundamentals, not on a new management team's stated intentions.
- **Q1 2026 revenue grew +7% YoY** — a notable step-up from FY2025's +4% and the best quarterly growth rate in this dataset. If sustained for several more quarters, the trailing 3yr CAGR would begin climbing back toward the 8–10% band. **One quarter is not a trend** under this framework's "act only on documented triggers" rule, but it's the single most important number to watch.
- **Bear case**: PayPal's core checkout business faces intensifying competition (Apple Pay, Shop Pay, Google Pay, bank-issued wallets) for a slice of payment volume that is itself growing only in the high-single-digits (TPV +7% FY2025). Branded checkout — historically PayPal's highest-margin segment — has been losing share for several years; Venmo monetization and Braintree's unbranded processing (lower-margin) have been the growth offsets. A mature, ~$33B-revenue payments network growing revenue at mid-single-digits while a high-margin segment shrinks as a share of the mix is consistent with a **structural growth ceiling**, not merely a temporary dip — which is exactly what a >10% CAGR requirement is designed to filter for.
- **Disruption vector check**: Stablecoin-based payment rails and "agentic commerce" (AI agents transacting directly with merchant APIs, bypassing traditional checkout) are emerging, longer-horizon threats to the two-sided-network moat that underpins PayPal's economics — not an immediate gate factor, but relevant context for any future re-evaluation.

**What would change this verdict:**
- **Q2 2026 earnings** (expected ~July/August 2026): if revenue growth holds at or above ~7% (continuing the Q1 2026 step-up rather than reverting to FY2025's +4%), recompute the TTM-based 3yr CAGR — if it moves materially toward the 8–10% band, re-run this Phase 01 gate from scratch.
- Concrete details from the new CEO's strategic reorganization (e.g., an investor day with updated multi-year growth targets) would be a **Rule 9 guidance-revision trigger** worth a fresh look, once realized in actual numbers rather than stated intentions.
- A **>15% unexplained price move** from $41.24 (Rule 9) would itself trigger a re-check regardless of the calendar.

---

## 6. Recommendation

# **WATCHLIST — do not open a position now (Phase 01 FAIL on Growth).**

PYPL fails the Phase 01 quality gate on **Revenue CAGR 3yr (6.46% vs >10% required by strategy.md, or >8% under the looser valuation-scoring.md pre-screen)** — the sole decisive failure among eight checks, all others of which **pass comfortably** (ROIC ~22%, FCF/NI conversion >100% in both of the last two years, net cash balance sheet, investment-grade ratings, non-dilutive buybacks, expanding gross margins). Per the framework, an exceptionally cheap valuation and clean balance sheet are **not sufficient to override a trailing growth-rate gate failure** — that would be substituting "it's cheap" for "it's a high-quality compounder," which is precisely the distinction Phase 01's Growth criterion exists to enforce. The recent Q1 2026 reacceleration (+7% YoY vs FY2025's +4%) and a new CEO's reorganization are real, but both are **single-data-point / forward-looking** signals that the framework's "act only on documented triggers, never on a narrative" rule says to wait on.

**Add PYPL to the watchlist** (`not-in-portfolio/PYPL/`) with a re-evaluation trigger at:
- **Q2 2026 earnings** (expected ~July/August 2026) — re-run Phase 01 with refreshed TTM revenue CAGR. If TTM growth has moved meaningfully toward/above the 8–10% band (driven by a continuation of Q1 2026's +7% rather than a reversion to +4%), proceed to the Rate Environment Gate and Phase 02 valuation scoring — at a ~7.7× TTM PE and ~22% ROIC, PYPL would likely screen as **very cheap** if the growth gate clears.
- Any **guidance revision** tied to the new CEO's strategic reorganization, once it produces concrete multi-year targets (Rule 9).
- A **>15% unexplained price move** from $41.24 (Rule 9).

---

## 7. Next Review Trigger

**Date/event:** PYPL's Q2 2026 earnings release (expected ~July/August 2026) — re-run Phase 01 with refreshed TTM Revenue CAGR (3yr), TTM Net Margin, and ROIC. Earlier trigger if the new CEO's reorganization produces a guidance revision, or a >15% unexplained price move from $41.24 occurs (Rule 9).

**No position opened — nothing to log in `decisions/`.**

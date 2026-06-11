# NEW POSITION — CIEN (Ciena Corporation) — 2026-06-11

**Task type:** NEW POSITION
**Date:** 11 Jun 2026
**10Y US Treasury Yield:** ~4.53–4.55% (TradingEconomics / CNBC, 10–11 Jun 2026)
**Rate Regime Modifier (would apply if scored):** +0.5 (10Y in the 3.5–5% bracket) — **not applied; Phase 01 gate fails before Phase 02 is reached**
**Current CIEN portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Technology — Communications/Networking Equipment (Optical Networking / Coherent Photonics)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$441.36** | IBKR `get_price_snapshot`, intraday last trade (`is_close: false`), +$6.71 / +1.54% vs prior close $434.65 |
| 52-week range | $71.52 – $637.09 (open 52w ago: $72.95) | IBKR `misc-statistics` |
| Analyst consensus PT | ~$459 (S&P Global, 20 analysts, "Buy") to ~$565 (stockanalysis.com) | [stockanalysis.com/stocks/cien/forecast](https://stockanalysis.com/stocks/cien/forecast/), MarketBeat |

⚠️ **Source variance flagged (per Rule 0 Step "verify, don't assume approximately right"):** Web search results were inconsistent — Yahoo/Kraken-sourced snapshots showed $464.50–$466.61 (appears to be a stale prior-session close, before this week's pullback), while stockanalysis.com/WallStreetZen showed ~$429–430. **IBKR's live intraday snapshot ($441.36, +1.54% intraday) is used as canonical**, consistent with the precedent set in the 2026-06-07 MA session.

**Context:** $441.36 sits ~31% below the 52-week high ($637.09, set during the AI-optical-networking re-rating) and is +543% over the trailing 52 weeks — but down ~24% over the past month on supply-chain-constraint commentary, despite a Q2 FY2026 beat-and-raise on 4 Jun 2026.

---

## 2. Data Gathered (Phase 01 Inputs) & Gaps Flagged

| Metric | Value | Source / Derivation |
|---|---|---|
| TTM Revenue | $5.12B (one source cites $5.6B) | WebSearch aggregation (SimplyWall.st / TIKR-style TTM rollups) — two sources disagree by ~9%, both cited |
| TTM Net Income | $438.3M | SimplyWall.st TTM rollup |
| TTM Net Margin | **7.9%** ($438.3M ÷ ~$5.12–5.6B) | Derived/reported — both denominators land 7.8–8.6% |
| TTM ROIC | **~6.98%** (GuruFocus, explicitly TTM) | Other sources show 15.4%–17.9%, but those are either dated (2021) or methodology-unclear — GuruFocus TTM figure used as most current/comparable |
| Revenue: FY2023 | $4.39B (+21% YoY) | Ciena FY2023 Q4 8-K |
| Revenue: FY2024 | $4.01B (decline) | Ciena FY2024 Q4 8-K |
| Revenue: FY2025 | $4.77B (+19% YoY) | Ciena FY2025 Q4 8-K |
| Revenue: FY2022 (derived) | ≈$3.63B (= $4.39B ÷ 1.21) | Back-calculated from the explicitly-stated "21% growth in FY2023" — flagged as derived, not primary-sourced |
| **Revenue CAGR 3yr** (FY2022→FY2025) | **≈9.55%** = (4.77/3.628)^(1/3) − 1 | Derived from above |
| Gross margin (Q2 FY2026, GAAP) | **44.0%**, +380bps YoY | Ciena Q2 FY2026 8-K earnings release |
| FCF — FY2025 | $665M (OCF $806.1M − CapEx $140.8M) | Ciena FY2025 Q4 8-K |
| FCF — FY2024 | $378M | Ciena FY2024 Q4 8-K |
| FCF — FY2023 | **NOT FOUND** | Gap — not located in available search results |
| FCF — Q1 FY2026 | $154M | Ciena Q1 FY2026 8-K |
| FCF — Q2 FY2026 | $219M (+71% YoY) | Ciena Q2 FY2026 8-K |
| Net Income FY2025 (derived) | ≈$123M (= EPS $0.85 × ~145M diluted shares) | Derived — total $ NI not directly stated |
| Net Income FY2024 | $84.0M (EPS $0.58) | Ciena FY2024 8-K |
| FCF/NI conversion (FY2025) | ≈540% ($665M ÷ ~$123M) | Derived — see discussion below |
| Net debt | $138M (Q2 FY2026) | Ciena Q2 FY2026 8-K |
| Gross leverage (Net Debt/EBITDA) | **1.6×** (Q2 FY2026), down from 3.2× a year ago | Ciena Q2 FY2026 8-K |
| Cash & investments | $1,045.1M (Q2 FY2026) | Ciena 10-Q (period ended 2 May 2026) |
| Shares outstanding | ~141.5M basic / ~146M diluted, declining | MacroTrends / GuruFocus |
| Buyback | $330M repurchased in FY2025 (of $1B authorization); similar pace planned FY2026 | Nasdaq/Ciena commentary |
| **New event:** $2.5B 0% convertible notes priced (upsized from $2.0B), with warrants struck at $1,000/share | Material capital-structure event, very recent | TipRanks |

**No metric was treated as invented** — TTM net margin and net debt/EBITDA are the best-sourced and most decision-relevant figures; FY2023 FCF and the exact FY2025 net income $ figure are gaps but don't change the gate outcome below.

---

## 3. Phase 01 — Quality Gate

| Check | CIEN Value | Threshold | Result |
|---|---|---|---|
| **Net margin (TTM)** | **7.9%** | >15% (strategy.md / New Position template) — also fails the >12% pre-screen in valuation-scoring.md | ❌ **FAIL** |
| **ROIC (TTM)** | **~6.98%** | >15% | ❌ **FAIL** |
| Revenue CAGR (3yr, FY2022→FY2025) | ≈9.55% | >10% | ❌ **FAIL (borderline)** |
| Gross margin | 44.0%, expanding (+380bps YoY) | >40% or expanding | ✅ PASS |
| FCF positive 3 consecutive years | FY2024 $378M, FY2025 $665M positive; FY2023 unconfirmed | required | ⚠️ Likely pass, one year unconfirmed |
| Net debt/EBITDA | ~1.6× (gross leverage) | <2x (core) / <2.5x (pre-screen) | ✅ PASS |
| FCF/NI conversion ratio | ≈540% (FY2025) / ~170% (TTM, annualizing H1 FY26 FCF vs TTM NI) | >70% for 2+ years | ✅ PASS (directionally — see note) |
| Share issuance pattern | Net buybacks (non-dilutive trend), but new $2.5B convert + $1,000-strike warrants just priced | not dilutive | ⚠️ Mixed — recent capital-structure event worth tracking |
| Moat signal | Leading coherent-optical/photonic-IC position for AI datacenter interconnect; record $7.7B backlog (+$600M in the quarter), visibility into 2027 | required | ✅ Qualitatively strong |

**Note on the FCF/NI conversion ratio (≈540%):** this threshold exists to catch the *opposite* failure mode (earnings not converting to cash — usually a red flag). A ratio this far *above* 100% instead reflects how depressed reported net income has been relative to cash generation over FY2024–25 (large D&A/SBC add-backs, working-capital unwind post supply-chain crisis) — which is really just another symptom of the same thin-margin history driving the net-margin failure above, not a separate quality signal in its own right.

---

## 4. Gate Result: **FAIL** — Stopping Per Operating Brief

> "Walk the Phase 01 quality gate — if it fails, stop and report why rather than proceeding to scoring."

CIEN **fails Phase 01 on Net Margin (TTM 7.9% vs >15% required) and ROIC (TTM ~7% vs >15% required)**, with Revenue CAGR (3yr ≈9.55%) also landing just under the >10% bar. Per the operating brief, this session **does not proceed** to the Rate Environment Gate, Phase 02 valuation score, or the fair-value/order-setup workup (Step 4 of `/new-position`) — building a DCF or buy/sell/stop ladder here would mean dressing up a name the framework's own quality screen says isn't there yet.

### Did the Turnaround Sub-Gate (Upgrade 4) open an alternate path?

No — it requires **all five** of:
1. Historical ROIC >15% for ≥5 of the past 10 years — CIEN's PE history shows extreme volatility (2.39× to 218×, including a one-time tax-driven EPS spike in FY2017), consistent with a cyclical, historically thin-margin equipment maker. I don't have a clean 10-year ROIC series to confirm this outright, but the qualitative profile makes a sustained >15% ROIC track record unlikely.
2. CEO/CFO insider buying >$500K in the past 6 months (Form 4-verified) — **not checked / no evidence found**.
3. Independent FV showing ≥40% MOS — not built (gate fails before this step).
4. Net Debt/EBITDA <3× — ✅ would pass (1.6×).
5. Core moat identifiable — ✅ yes.

Since conditions 1 and 2 can't be confirmed as met, "all five" can't be satisfied — the Turnaround Sub-Gate path doesn't open regardless of how condition 1 ultimately resolves.

---

## 5. Why This Is Close — and What Would Flip the Verdict

The tension here is real: **Q2 FY2026 in isolation** (revenue +40% YoY to $1.57B, GAAP net margin ≈13.9%, gross margin 44.0% and expanding, FCF +71% YoY, backlog +$600M to $7.7B, raised FY2026 guidance) looks like a Score 1–3 Fast Grower. But the **TTM figures the gate is built on** (net margin 7.9%, ROIC ~7%) still carry the weight of FY2024's near-breakeven year (2.1% net margin) and FY2025's still-thin 2.6%. This is exactly the "is this a structural inflection or a cyclical blip" question — and Phase 01 is deliberately built to gate on **trailing financial proof**, not narrative, per Rule 0 and the non-negotiable "never act on price movement alone / never invent or estimate."

**What would change this:**
- If Q3 FY2026 (expected ~Sept 2026) lands with a similar ~14% net margin, the TTM net margin would mechanically climb meaningfully toward (though likely still below) 15% — worth a fresh Phase 01 check at that point.
- ROIC TTM (~7%) has more ground to cover and would need 2+ more quarters at Q2-FY26-like profitability to plausibly clear 15%.
- The 24% one-month price decline is **not** itself a trigger either way (Phase 06: "price dropped... NOT valid" as a reason to act, in either direction).
- The new $2.5B convertible note / $1,000-strike warrant structure is a genuine fundamental event (Rule 9-style "material capital raise") worth a dedicated look next time CIEN is re-evaluated, regardless of the gate outcome — convertible debt at 0% coupon is shareholder-friendly financing *if* deployed well, but materially changes the capital structure.

---

## 6. Recommendation

# **PASS — do not open a position now.**

CIEN fails the Phase 01 quality gate on TTM Net Margin and TTM ROIC (both well below the >15% thresholds), with Revenue CAGR 3yr also borderline-short of >10%. Per this framework's rules, an exciting single-quarter inflection is not sufficient grounds to override a trailing-financials gate failure — that would be acting on a narrative/momentum basis, which Rule 0 and the now-retired Upgrade 6 (momentum gate) both explicitly warn against in either direction.

**Add CIEN to the watchlist** with a re-evaluation trigger at:
- **Next earnings release** (Q3 FY2026, expected ~Sept 2026) — re-run the full Phase 01 gate with updated TTM net margin and ROIC. If both have crossed 15%, proceed to Phase 02.
- Any **management commentary or guidance revision** materially changing the FY2026 margin outlook (Rule 9 trigger).
- Developments on the **$2.5B convertible note** deployment (Rule 9 "material capital raise" analog).

---

## 7. Next Review Trigger

**Date/event:** CIEN's Q3 FY2026 earnings release (expected ~September 2026) — re-run Phase 01 with refreshed TTM Net Margin, ROIC, and Revenue CAGR. Earlier trigger if a guidance revision or the convertible-note deployment constitutes a material fundamental event (Rule 9).

**No position opened — nothing to log in `decisions/`.**

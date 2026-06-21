# RESCORE — CSGP (CoStar Group, Inc.)

## 1. Session header
- **Task type:** RESCORE (single ticker)
- **Date:** 2026-06-20
- **10Y US Treasury yield:** **4.451%** (source: `yfinance` `^TNX` last close 2026-06-18; corroborated by the same figure used in today's AMZN/MSFT rescores)
- **Rate Regime Modifier in effect:** **+5** (10Y in the 3.5–5% band — "capital has a real cost")
- **Sector:** Real Estate — commercial real estate data, analytics & marketplaces (CoStar Suite, LoopNet, Apartments.com) plus the residential build-out (Homes.com). Treated as Technology/Growth-style for fair-value method (EV/EBIT multiples + scenario) per Rule 1, given the software-like ~79% gross margin.
- **Live price:** **$30.12** (source: `yfinance` `currentPrice`/`regularMarketPrice`, intraday 2026-06-20). IBKR `get_price_snapshot` (conid 6726677) was attempted first per Rule 0 but permission was denied, so `yfinance` was used as the documented fallback — same path as the 2026-06-20 AMZN/MSFT sessions.
- **52-week range:** **$29.53 – $97.43** (`yfinance`). The live price sits ~2% off the 52-week **low** and ~69% below the 52-week **high** — the stock has de-rated heavily over the past year as Homes.com investment crushed reported earnings. This range matters: a "Very Expensive" trailing-multiple score on a stock trading near its 52-week low is the exact tension the Upside/Downside Modifier exists to resolve.
- **Analyst consensus price target (PT):** mean **$48.25**, median **$49.00**, n=20 (`yfinance`); WallStreetZen avg $52.83 (range $33–$70). Used only as a bull-case sanity anchor, never as the score input.
- **Prior score:** **83.3** (Very Expensive → "Trim to 50%" band, 80.0–89.9), last reviewed Jun 2026. Current portfolio weight **1.53%**.

Jargon decoded on first use throughout: FCF (free cash flow — operating cash flow minus capital expenditure); OE (Owner Earnings — Buffett's measure: net income + depreciation & amortization − maintenance capital expenditure); EV/EBIT (enterprise value ÷ earnings before interest and taxes); EV/EBITDA (enterprise value ÷ earnings before interest, taxes, depreciation & amortization); PE (price-to-earnings ratio); PEG (PE ÷ earnings growth rate); CAGR (compound annual growth rate); MoS (margin of safety); PW (probability-weighted); pp (percentage points); SBC (stock-based compensation); D&A (depreciation & amortization); capex (capital expenditure); opex (operating expense); R/R (reward-to-risk ratio); EY (earnings yield).

## 2. Data gaps flagged
- **Trailing EV/EBIT is undefined.** CoStar posted a **GAAP operating loss of −$72M in FY2025** (operating income $451M FY22 → $282M FY23 → $5M FY24 → **−$72M FY25**), so EV/EBIT cannot be computed. Per the prior session's approach, **EV/EBITDA is substituted as a flagged proxy** for the EV/EBIT sub-score. This is a substitute input, not a clean read — flagged.
- **No clean 5-year PE history.** Reconstructed TTM (trailing-twelve-month) EPS fell from ~$1.28 (2023) to a trough of ~$0.73 (early 2025) as the Homes.com spend hit the P&L, then recovered to ~$0.94 (Q1 2026). The resulting 5yr "average PE" of 72.4× (range 36.3–113.8×, n=20 quarters) is **distorted by collapsing earnings, not by multiple expansion** — it is not a usable historical-PE benchmark. Per the valuation-scoring.md distorted-base fallback, the Forward PE sub-score uses the **neutral 50.0 placeholder (flagged)**, exactly as the 2026-06-20 AMZN session did. No data invented.
- **Owner Earnings (Upgrade 1) does NOT rescue the FCF sub-score here — and this is the central judgment of the rescore.** Growth capex is 32.4% of total capex (FY25 capex $389M, maintenance proxy = D&A $263M → growth capex $126M), which technically clears Upgrade 1's >30% trigger. But OE = NI $7M + D&A $263M − maintenance capex $263M = **$7M** (yield 0.06%) — *worse*, not better. The reason: CoStar's earnings depression is driven by **growth operating expense** (Homes.com sales & marketing, expensed straight through the income statement), **not** by capitalised growth capex. OE only adds back capex, so it does nothing for an opex-funded build-out. **The reported FCF figure is therefore the honest sub-score input; the forward earnings normalization is carried by the Upside/Downside Modifier instead** — which is precisely the gap that modifier was designed to close. Flagged explicitly so this isn't mistaken for the AMZN-style capex add-back.
- **FCF figure used:** `yfinance` `info.freeCashflow` TTM = **$202.2M** (more current than the FY2025 statement figure of $41M, which was depressed by a one-off working-capital/residential-spend trough). Both are real reported numbers; the TTM figure is used as the more current read and flagged.

**Depressed-but-investing vs. structurally impaired — the call:** CSGP is **depressed-but-investing**, not impaired. Evidence: revenue is *growing and accelerating* (FY22 $2.18B → FY23 $2.46B → FY24 $2.74B → FY25 $3.25B, ~14% CAGR; 2026 guided 16–18%); gross margin holds at ~79%; the core commercial-real-estate-data franchise (CoStar Suite, LoopNet, Apartments.com) remains highly profitable. The losses are **deliberate residential investment**: Homes.com net investment is being cut from ~$850M (2025) toward ~$300M less in 2026; the residential adjusted-EBITDA loss already improved from −$361M (2024) to −$230M (2025). Total-company adjusted EBITDA rose 83% to $442M in 2025, with 2026 guided to **$780–820M (~20% margin vs 13% in 2025)** and a medium-term target of **$1.25B by 2028** at ~15% revenue CAGR (sources: CoStar FY2025 release; CoStar FY2026/medium-term outlook). This is an investment cycle, not a melting ice cube.

## 3. Rate Environment Gate
- **Step 1 — Earnings Yield Spread Test:** EY = 1 ÷ Forward PE = 1 ÷ 16.74 = **5.97%**. Spread = 5.97% − 4.451% (10Y) = **+1.52%**, which is **≥ +1.5% → PASS, no additive flag.** (Note: this passes *only* because forward PE is computed off the recovered forward EPS of $1.80 — the forward earnings inflection is doing the work. On trailing earnings the gate would fail badly. Flagged.)
- **Step 2 — Rate Regime Modifier:** 10Y 4.451% sits in the 3.5–5% band → **+5**.
- Combined Gate additive: **+5** (Step 2 only).

## 4. Full score calculation

**Standard Re-Score inputs (FY2025 unless noted; `yfinance` statements + `info`):**

| Metric | Value | Source / calc |
|---|---|---|
| Live price | $30.12 | `yfinance` intraday |
| Market cap | $12.30B | $30.12 × 408.356M shares |
| Net cash | +$449M | cash & ST investments $1.633B − total debt $1.184B |
| Enterprise value | $11.85B | market cap − net cash |
| Reported FCF yield (TTM) | **1.64%** | TTM FCF $202.2M ÷ market cap $12.30B (depressed by Homes.com growth opex) |
| EV/EBIT (trailing) | **undefined** | FY25 operating loss −$72M → EV/EBITDA substituted (flagged) |
| EV/EBITDA (trailing, TTM) | **43.6×** | EV $11.85B ÷ TTM EBITDA $272M |
| Forward PE | 16.74× | `yfinance` `forwardPE` (off forward EPS $1.80) |
| 5yr avg PE | 72.4× (distorted — not used) | reconstructed; collapsing EPS distorts it → 50.0 fallback |
| Revenue CAGR 3yr | ~14.2% | $2.182B (FY22) → $3.247B (FY25) |
| ROIC proxy / ROE | 0.30% | `returnOnEquity` — depressed by near-zero NI; not a structural read |
| Gross margin | 78.6% | `yfinance` — software-like, intact |
| Net margin | 0.73% | `yfinance` — depressed by residential investment |
| Net debt/EBITDA | net cash (n/a) | net cash position — no leverage concern (Debt Gate: easily passes) |
| FCF/NI conversion | FY25 5.86 / FY24 −1.76 / FY23 0.93 / FY22 1.04 | the FY24/FY25 distortions are residential-investment-driven, not an accrual-quality red flag |

**Sub-scores:**
- **FCF (40% weight)** — `clamp(100 × (1 − 1.64/10), 0, 100)` = **83.56**. (Reported TTM-FCF basis. Owner Earnings does *not* improve this — see §2 — because the drag is growth opex, not capex. This sub-score is honestly "very expensive on today's depressed cash flow"; the forward inflection is captured in §5, not here.)
- **EV/EBIT (25% → 40% weight after PEG redistribution)** — trailing EBIT is a loss, so the **EV/EBITDA proxy of 43.6×** is run through the EV/EBIT formula as a flagged substitute: `clamp((43.6 − 12)/23 × 100, 0, 100)` = **100.0** (clamped). *Sanity check on a forward basis:* 2026E adjusted EBITDA ~$800M → forward "EBIT" ~$520M → forward EV/EBIT ~22.8× (sub-score ~47) — i.e. the franchise is only ~mid-20s× on normalized forward earnings, which is the point the modifier picks up. The trailing 100.0 is deliberately conservative/honest, not the forward read.
- **Forward PE (20% weight)** — no clean 5yr history (distorted by the earnings trough) → **50.0 (neutral fallback, flagged)**.
- **PEG (15% weight)** — **Not applicable.** CSGP is not a qualifying Fast Grower on a *clean* earnings base: trailing EPS *fell* over the investment period and is only now recovering, so there is no 3+ years of clean >15% EPS growth. Per the 2026-06-20 clean-earnings clarification, **PEG's 15% weight is redistributed to EV/EBIT** (→ 40%). (`yfinance` reports a trailing PEG of ~0.11 — recorded as a sensitivity flag only; it is built on the near-zero earnings base and is not trustworthy, exactly as flagged in the prior session.)

**Raw weighted score** = (83.56 × 0.40) + (100.0 × 0.40) + (50.0 × 0.20)
= 33.42 + 40.00 + 10.00 = **83.42**.

**After Rate Environment Gate:** 83.42 + 5 (Step 2 Rate Regime; Step 1 passed → no flag) = **88.42** (pre-Upside).

## 5. Upside/Downside Modifier (REQUIRED)

This is the key test of the modifier on a "Very Expensive" trailing-score name. The hypothesis going in was that a richly-scored stock would see a **positive** modifier (deeper trim). The honest result is the **opposite** — and that is the modifier working correctly: CSGP has already de-rated ~69% from its 52-week high to within 2% of its 52-week low, so the *forward* expected return is now genuinely attractive even though *trailing* multiples scream "expensive."

**Scenario fair value (Rule 7 — EV/EBIT-multiple method on a ~2027 normalized EBIT; net cash +$449M added back; 408.356M shares):**

| Scenario | Wt | Assumption | ~2027 normalized EBIT | Exit EV/EBIT | FV/share |
|---|---|---|---|---|---|
| Bull | 25% | Homes.com losses fade fast, core re-accelerates, premium multiple holds | $800M | 22.0× | **$44.20** |
| Base | 50% | Management's guided path: 2026 adj EBITDA ~$800M → 2028 $1.25B; orderly margin recovery | $650M | 20.0× | **$32.93** |
| Bear | 25% | Residential spend stays heavy / softer CRE cycle / de-rating at high rates | $450M | 16.0× | **$18.73** |

Bull ($44.20) sits below the analyst-consensus mean PT ($48.25) — a deliberately sober bull anchor. Bear ($18.73) is honestly underwritten: a further ~38% drawdown from today if the residential build-out keeps bleeding and the multiple compresses — the real risk of owning an investment-cycle stock if the cycle doesn't turn.

- **PW Fair Value** = 0.25×44.20 + 0.50×32.93 + 0.25×18.73 = **$32.20**.
- **Gap Upside %** = ($32.20 ÷ $30.12) − 1 = **+6.9%**. *(Modest — the stock has already fallen most of the way to fair value; this is not the source of the attractive return.)*
- **Catalyst & timeline (Rule 10):** A **documented, management-guided catalyst exists within the 18–24-month window** — the Homes.com net-investment cut (~$300M less in 2026) and the guided adjusted-EBITDA inflection (2025 $442M → 2026 $780–820M → 2028 $1.25B). Use the **2-year window**. → Annualized gap = 6.9% ÷ 2 = **+3.4%/yr**.
- **Intrinsic growth:** **+12%/yr.** Management guides ~15% revenue CAGR 2025–2028; discounted to 12% for execution/decel risk and to stay below the rosy point (guardrail 2). Earnings will grow far faster than this off the depressed base, but intrinsic growth is taken on the durable revenue line, not the recovery-artifact EPS bounce.
- **Shareholder yield:** **+4%.** CoStar authorised a **$700M share repurchase in 2026** (≈5.7% of market cap); taken at +4% net of SBC dilution offset. No dividend.

**Expected annual return E** = 3.4 (annualized gap) + 12.0 (intrinsic growth) + 4.0 (shareholder yield) = **+19.4%**.

**Map to modifier** (hurdle H = 10%): E ≥ H → M = −15 × clamp((19.4 − 10)/15, 0, 1) = −15 × 0.627 = **−9.40**.

**Guardrail check:** (1) Catalyst exists within 18–24 months (guided EBITDA inflection) → the −5 upside cap does **not** apply; full upside credit is allowed. (2) Bull/base/bear PW FV used, not the rosy point. (3) Full calc shown. (4) Bounded ±15 — within range.

**Sensitivity (honesty band):** holding the scenario FV fixed, varying the two soft inputs gives E and final score:
- ig 14% / sy 5.7% → E 23.1% → M −13.15 → **Final 75.3**
- ig 12% / sy 4% (central, used) → E 19.4% → M −9.40 → **Final 79.0**
- ig 10% / sy 3% → E 16.4% → M −6.45 → **Final 82.0**

Every case stays in the **trim** zone — the modifier lightens the trim by one band but does **not** rescue CSGP into the Hold/Buy bands. That is the correct, conservative read: the bottom-up cheapness gate (trailing FCF/EV multiples on depressed earnings) is still firmly "expensive," and the ±15 cap deliberately prevents a forward forecast from overriding it.

## 6. Final score + action

**Final Score** = 83.42 (raw weighted) + 5 (Rate Regime) + (−9.40) (Upside/Downside) = **79.02 → 79.0** (rounded to 0.1).

- **Action band: 70.0–79.9 → TRIM 25–30%** of position.
- **Action category vs prior (83.3 → "Trim to 50%", band 80.0–89.9): CHANGED — lighter trim.** The score fell 4.3 points (83.3 → 79.0), moving down one band from "Trim to 50%" to **"Trim 25–30%."** The driver is entirely the new Upside/Downside Modifier (−9.40): once the forward dimension is folded in — a stock down ~69% from its high, a guided EBITDA inflection, ~15% revenue growth, and a $700M buyback — the raw "Very Expensive" trailing score (which is built on deliberately depressed investment-cycle earnings) is partly offset. The name is still expensive on today's cash flow and still a trim, just a lighter one.

### Trim plan (order setup)
- Current weight: **1.53%** of portfolio (small position).
- Trim **25–30%** of the position → target weight **~1.07%–1.15%**.
- **Sell target (baseline):** PW Fair Value **$32.20**.
- **Bull-case trim target:** Bull FV × 0.90 = $44.20 × 0.90 = **$39.78** (well below the 52-week high of $97.43 — scale any trim into strength toward this level).
- Live price $30.12 is *below* the baseline sell target ($32.20). This is therefore a **valuation-band trim on a depressed-but-investing name**, and given (a) the small 1.53% weight, (b) the price sitting near a 52-week low, and (c) a real, guided earnings-inflection catalyst, **execution discretion strongly favors the light end (25%) of the band, or scaling the trim into any recovery toward the $32–$40 targets rather than selling at the low.** The framework triggers a trim; the modifier and the catalyst argue for patience on *where* to trim.
- **No full exit** — Phase 06 triggers absent: net-cash balance sheet (no leverage crisis), gross margin intact at ~79%, revenue growing/accelerating (growth thesis intact, not a broken-thesis or moat-erosion case), and the score is nowhere near the 90.0+ sustained-2-quarter exit zone. The losses are a documented investment cycle with a guided turn, not structural impairment.

## 7. Portfolio rebalancing summary
Out of scope for a single-ticker rescore. Recommendation handed to the orchestrator: a **light (25%) trim** of the 1.53% CSGP position, with execution discretion to scale into strength rather than sell at the 52-week low; recycle any proceeds into the portfolio's current Score 0.0–29.9 names per Phase 05. `portfolio/holdings.md` is **not** edited by this session (orchestrator handles it).

## 8. Next review trigger
- **Next earnings** (Q2 FY2026, expected ~late Jul 2026) — standard re-score, with specific attention to: (a) the Homes.com net-investment reduction tracking toward the ~$300M cut, and (b) adjusted EBITDA progress against the $780–820M FY2026 guide.
- **Earlier if (Rule 9):** a guidance revision (up or down) on the EBITDA-inflection path, a management change, material M&A, or a >15% unexplained price move.
- Once ~3 consecutive years of clean post-inflection earnings exist (likely 2027–2028), the Forward PE sub-score can move off the 50.0 neutral fallback and EV/EBIT can be computed directly — both should move this score materially as the residential drag clears.

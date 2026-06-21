# RESCORE — AMZN (Amazon.com, Inc.)

## 1. Session header
- **Task type:** RESCORE (single ticker)
- **Date:** 2026-06-20
- **10Y US Treasury yield:** 4.45% (source: `yfinance` ^TNX last close 4.451%; corroborated by web search 4.46% on 2026-06-18)
- **Rate Regime Modifier in effect:** **+5** (10Y in the 3.5–5% band — "capital has real cost")
- **Sector:** Consumer Discretionary — E-commerce + Cloud Infrastructure (AWS). Treated as Technology/Growth for fair-value method (DCF + EV/EBIT multiples) per Rule 1.
- **Live price:** **$244.39** (source: `yfinance` `currentPrice`/`regularMarketPrice`, intraday 2026-06-20). IBKR `get_price_snapshot` was attempted first per Rule 0 but permission was denied, so `yfinance` was used as the documented fallback.
- **52-week range:** $196.00 – $278.56 (`yfinance`)
- **Analyst consensus price target (PT):** mean $312.99, median $315.00, n=63 (`yfinance`) — used only as a bull-case sanity anchor, never as the score input.
- **Prior score:** 79.8 (Expensive → trim band), last reviewed Jun 2026. Current portfolio weight 10.45%.

Jargon decoded on first use throughout: FCF (free cash flow — operating cash flow minus capital expenditure), OE (Owner Earnings — Buffett's measure: Net Income + depreciation & amortization − maintenance capital expenditure), EV/EBIT (enterprise value ÷ earnings before interest and taxes), PE (price-to-earnings), PEG (PE ÷ earnings growth rate), CAGR (compound annual growth rate), MoS (margin of safety), PW (probability-weighted), pp (percentage points), SBC (stock-based compensation), D&A (depreciation & amortization), capex (capital expenditure), R/R (reward-to-risk ratio).

## 2. Data gaps flagged
- **Maintenance-vs-growth capex split is not disclosed by Amazon.** Required for the Owner Earnings (Upgrade 1) FCF sub-score. Rather than invent a number, the standard analyst proxy is applied: **maintenance capex ≈ D&A** (the spend needed to replace the existing asset base), which is the conservative convention when no disclosure exists. The growth-capex share this implies (50.1% of total capex) is well above Upgrade 1's >30% trigger, so Upgrade 1 correctly applies. Flagged: if Amazon ever discloses a finer split, the FCF sub-score should be refreshed.
- **No clean 5-year PE history exists.** Amazon posted a GAAP net *loss* in FY2022 and only ~2 years of clean, representative earnings since — the reconstructed "5yr average PE" of 66.7× is distorted upward by 2022–2023 near-zero-earnings quarters (individual quarterly PE readings of 120×–251× in that window). Per the valuation-scoring.md no-history/distorted-base fallback, the Forward PE sub-score uses the **neutral 50.0 placeholder (flagged)** rather than scoring off a distorted average that would falsely flatter the stock as "cheap." No data invented.

## 3. Rate Environment Gate
- **Step 1 — Earnings Yield Spread Test:** Earnings Yield (EY) = 1 ÷ Forward PE = 1 ÷ 24.79 = **4.03%**. Spread = 4.03% − 4.45% (10Y) = **−0.42%**, which is below the +1.5% threshold → **+5 additive flag** (yellow flag raising the bar, not a veto).
- **Step 2 — Rate Regime Modifier:** 10Y 4.45% sits in the 3.5–5% band → **+5**.
- Combined Gate additive: **+10**.

## 4. Full score calculation

**Standard Re-Score inputs (FY2025 fiscal year, `yfinance` financial statements):**

| Metric | Value | Source / calc |
|---|---|---|
| Owner Earnings yield | **2.95%** | OE $77.67B ÷ market cap $2,628.93B |
| Reported FCF yield (for contrast) | 0.29% | reported FCF $7.70B ÷ market cap — depressed by the AI/AWS capex surge; this is exactly why Upgrade 1 is required |
| EV/EBIT (trailing) | **27.33×** | EV $2,721.38B ÷ EBIT $99.585B |
| Forward PE | 24.79× | `yfinance` `forwardPE` |
| 5yr avg PE | 66.7× (distorted — not used) | reconstructed; 2022 loss distorts it → 50.0 fallback used |
| Revenue CAGR 3yr | 11.7% | $513.98B (FY22) → $716.92B (FY25) |
| ROIC proxy / ROE | ~24.3% | `returnOnEquity` |
| Gross margin | 50.6% | `yfinance` |
| Net margin | 12.2% | `yfinance` |
| Net debt | $29.96B | total debt $152.99B − cash & ST investments $123.03B |
| Net debt/EBITDA | 0.19× | $29.96B ÷ $155.86B EBITDA — negligible leverage |
| FCF/NI conversion | FY25 9.9% / FY24 55.5% / FY23 105.9% | the low FY25 ratio is capex-driven, not an accrual-quality red flag — OE adjustment handles it |

**Owner Earnings (Upgrade 1) — shown explicitly:**
- Growth capex check: total capex $131.82B; maintenance proxy (= D&A) $65.76B; growth capex = $66.06B = **50.1% of total** → exceeds the 30% trigger → Upgrade 1 applies.
- OE = Net Income $77.67B + D&A $65.76B − maintenance capex $65.76B = **$77.67B**.
- OE yield = $77.67B ÷ $2,628.93B market cap = **2.95%**.

**Sub-scores:**
- **FCF (40% weight)** — `clamp(100 × (1 − 2.95/10), 0, 100)` = **70.46**. (Owner-Earnings basis; raw-FCF basis would have given ~97 and overstated expensiveness — the prior 79.8 score carried this unresolved.)
- **EV/EBIT (25% → 40% weight after PEG redistribution)** — `clamp((27.33 − 12)/23 × 100, 0, 100)` = **66.65**.
- **Forward PE (20% weight)** — no clean 5yr history → **50.0 (neutral fallback, flagged)**.
- **PEG (15% weight)** — **Not applicable.** Amazon is not a qualifying Fast Grower on a *clean* earnings base: trailing EPS growth is a recovery off the FY2022 GAAP net loss (FY22 loss → FY23 $30.4B → FY24 $59.2B → FY25 $77.7B), i.e. distorted, not 3+ years of clean >15% EPS growth. Per the 2026-06-20 clean-earnings clarification, **PEG's 15% weight is redistributed to EV/EBIT** (EV/EBIT weight → 40%). (`yfinance` reports a trailing PEG of ~1.83 — recorded as a sensitivity check only, not scored.)

**Raw weighted score** = (70.46 × 0.40) + (66.65 × 0.40) + (50.0 × 0.20)
= 28.18 + 26.66 + 10.00 = **64.84**.

**After Rate Environment Gate:** 64.84 + 5 (Step 1 EY-spread flag) + 5 (Step 2 Rate Regime) = **74.84** (pre-Upside).

## 5. Upside/Downside Modifier (REQUIRED)

**Scenario fair value (Rule 7, EV/EBIT-multiple method on forward EBIT, net debt $29.96B, 10.757B shares):**

| Scenario | Wt | Assumption | Forward EBIT | Exit EV/EBIT | FV/share |
|---|---|---|---|---|---|
| Bull | 25% | AWS reaccelerates, ads + margin expansion, multiple holds | $124.5B (+25%) | 27.0× | **$310** |
| Base | 50% | Consensus: strong earnings growth, modest multiple de-rate | $117.5B (+18%) | 24.0× | **$259** |
| Bear | 25% | Capex drag, AWS decel, consumer softness, de-rating at high rates | $107.6B (+8%) | 18.0× | **$177** |

Bull ($310) sits just under the analyst-consensus PT ($313 mean) — a sane bull anchor. Bear ($177) is honestly underwritten: a ~28% drawdown from today's price if the multiple compresses while growth slows — the central risk of owning a 27× EV/EBIT name at a 4.45% risk-free rate.

- **PW Fair Value** = 0.25×310 + 0.50×259 + 0.25×177 = **$251.41**.
- **Gap Upside %** = ($251.41 ÷ $244.39) − 1 = **+2.9%**. *(Price is essentially at probability-weighted fair value — no meaningful margin of safety.)*
- **Catalyst & timeline (Rule 10):** No single hard catalyst within 18–24 months for a re-rating; the thesis (capex-to-FCF inflection, AWS reacceleration) is a multi-year story → use the **2-year default window**. → Annualized gap = 2.9% ÷ 2 = **+1.4%/yr**.
- **Intrinsic growth:** durable owner-earnings growth taken at **+10%/yr** — anchored to revenue CAGR 11.7% (decelerating at $717B scale) net of ~1% SBC dilution. Deliberately *not* the 74.8% trailing EPS-growth figure, which is a recovery artifact off the 2022 loss (using it would be exactly the optimistic rescue the brief warns against).
- **Shareholder yield:** **0%** — Amazon pays no dividend and does not run a net buyback (shares roughly flat to slightly dilutive from SBC).

**Expected annual return E** = 1.4 (annualized gap) + 10.0 (intrinsic growth) + 0.0 (shareholder yield) = **+11.4%**.

**Map to modifier** (hurdle H = 10%): E ≥ H → M = −15 × clamp((11.4 − 10)/15, 0, 1) = −15 × 0.093 = **−1.40**.

**Guardrail check:** the no-hard-catalyst guardrail caps the *upside* (negative) side at −5; M = −1.40 is already inside that, so no further adjustment. Bull/base/bear PW FV used (not the rosy point). Full calc shown above.

**Interpretation (the honest read):** the modifier is only *mildly* negative, and it is carried almost entirely by the intrinsic-growth term — the valuation gap itself is just +2.9%. Expected return barely clears the 10% hurdle. A reasonable durable-growth range of 8–12% moves the final score only between 75.1 and 71.4 — every case stays in the same TRIM band. The forward dimension does **not** rescue AMZN: it is priced at fair value with a real −28% bear case, and the modifier correctly declines to pull it toward a buy.

## 6. Final score + action

**Final Score** = 64.84 (raw weighted) + 5 (Step 1) + 5 (Rate Regime) + (−1.40) (Upside/Downside) = **73.44 → 73.4** (rounded to 0.1).

- **Action band: 70.0–79.9 → TRIM 25–30%** of position.
- **Action category vs prior (79.8, also TRIM 25–30%): UNCHANGED** — still in the Expensive/trim band. The score *fell* 6.4 points (79.8 → 73.4), driven almost entirely by correctly applying Owner Earnings to the FCF sub-score (the prior score used raw reported FCF, which the AI/AWS capex surge had crushed to a 0.29% yield) and the updated lower EV/EBIT (27.3× vs the prior 32.7×). Still expensive, just less extremely so.

### Trim plan (order setup)
- Current weight: **10.45%** of portfolio.
- Trim **25–30%** of the position → target weight **~7.3%–7.8%**.
- **Sell target (baseline):** PW Fair Value **$251.41**.
- **Bull-case trim target:** Bull FV × 0.90 = $310 × 0.90 = **$279.00** (within the 52-week high of $278.56 — i.e. essentially at prior highs; scale trims into strength toward this level).
- Live price $244.39 is *below* both the sell target and bull-trim target, so this is a valuation-band trim (recycle into Score 0.0–29.9 names per Phase 05), not a price-target sale. Execution discretion: scale the 25–30% trim, with the remainder into any push toward $279.
- **No full exit** — Phase 06 triggers absent: leverage negligible (net debt/EBITDA 0.19×), margins intact (gross 50.6%, expanding), ROIC ~24%, growth thesis intact. Score is not in the 90.0+ sustained-2-quarter exit zone.

## 7. Portfolio rebalancing summary
Out of scope for a single-ticker rescore. Recommended action handed to the orchestrator: execute a 25–30% trim of AMZN, recycling proceeds into the portfolio's current Score 0.0–29.9 names. `portfolio/holdings.md` is **not** edited by this session (orchestrator handles it).

## 8. Next review trigger
- **Next earnings** (Q2 FY2026, expected ~late Jul 2026) — standard re-score.
- **Earlier if:** Amazon discloses a maintenance-vs-growth capex split (would refine the Owner Earnings FCF sub-score), a guidance revision (Rule 9), or a >15% unexplained price move.
- Once ~3 consecutive years of clean post-2022 earnings exist, the Forward PE sub-score can move off the 50.0 neutral fallback to a real 5yr-range computation.

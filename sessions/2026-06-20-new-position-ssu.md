# New Position Evaluation: SSU (Samsung Electronics GDR) — 2026-06-20

**Task type:** NEW POSITION
**Ticker (tradable instrument):** SSU — Frankfurt Stock Exchange (FWB), IBKR contract_id 13796868, "SAMSUNG ELECTR-GDR REG S," country_code DE, currency EUR
**Underlying company:** Samsung Electronics Co., Ltd. — primary listing Korea Exchange (KRX), ticker 005930 (yfinance: `005930.KS`), reporting currency KRW
**Instrument type:** Global Depositary Receipt (GDR) — a certificate issued by a depositary bank representing a fixed number of shares of a foreign company, traded on a different exchange (here, Frankfurt) in a different currency (EUR) than the underlying shares (KRW)
**Analyst:** Claude (automated session)
**Account:** U19421206 (IBKR)

---

## 0. Why this session is more complex than a standard single-market evaluation

Samsung Electronics is evaluated here as a GDR, layering three things on top of a standard new-position workflow:
1. **Company fundamentals must come from the primary KRX listing** (005930.KS, KRW), not the GDR — the GDR has no separate financials, it's a wrapper.
2. **The GDR-to-ordinary-share ratio must be confirmed from a reliable source**, not assumed, before any per-GDR fair value, buy price, sell target, stop loss, or position size can be computed.
3. **Samsung is a diversified conglomerate** — semiconductors (Device Solutions / "DS" division: memory + foundry) is only ~39% of consolidated revenue but ~57% of consolidated operating profit, alongside a much lower-margin DX division (mobile, displays, consumer electronics). Consolidated multiples are diluted by DX and are not directly comparable to pure-play memory peers (Micron, SK Hynix) without adjustment.

All three are addressed explicitly below before any score or valuation number is used.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Instrument | Price | Source | Timestamp |
|---|---|---|---|
| **SSU (GDR, EUR, Frankfurt)** | **€5,020.00** | IBKR live snapshot, contract_id 13796868 | 2026-06-20 |
| Prior close | €5,260.00 | IBKR | — |
| Day change | **−4.56%** (−€240.00) | IBKR | — |
| Samsung Electronics ordinary (KRX, KRW) | ₩354,000 | yfinance `005930.KS` | 2026-06-20 |

The GDR dropped 4.56% on the day this evaluation was run. This is noted for context (per Rule 0 discipline — the live price is what it is, not what a stale screen might show) but is **not itself a trigger or signal** — the framework's Rule 0 in [strategy.md](../framework/strategy.md) says to act only on documented fundamental triggers, never on price movement alone.

---

## 2. GDR Ratio Confirmation (blocking-data-gap check)

**Confirmed: 1 GDR = 25 ordinary common shares.**

This is the single most load-bearing number in this entire session — every per-GDR price, fair value, and order-setup figure downstream depends on it — so it was triangulated three independent ways rather than assumed:

1. **Implied-ratio sanity anchor** (not conclusive alone): yfinance ordinary shares outstanding (5,764,191,903) vs. a back-of-envelope GDR-listing share count gave a rough ~22:1 clue — used only to know roughly what order of magnitude to expect, not as the answer.
2. **Multi-source textual confirmation**: AJ Bell, Hargreaves Lansdown, stocksguide.com, aktien.guide, and boerse.de all independently key the same identifiers — ISIN US7960508882, WKN 896360, ticker SSU on Frankfurt — and all state **"1 GDR (Reg S) = 25 ordinary common shares"** (₩100 par value each). Five independent sources, all converging on the same ratio for the same ISIN, is a high-confidence confirmation.
3. **Independent price-math cross-check**: (GDR price €5,020 × EUR/KRW FX rate 1,754.0) ÷ 25 = ₩352,203 implied ordinary-share price, vs. the actual live KRX price of ₩354,000 — a difference of only **−0.51%**, well within normal bid/ask spread and GDR-program fee drag. This is strong independent confirmation that 25:1 is correct.

**Important distinction flagged**: there is a *separate, different* Samsung GDR program (the 144A program, "1 GDR represents 0.5 common shares") that uses a completely different ratio. This session's GDR (SSU, Reg S, ISIN US7960508882) is **not** that program — confirmed via the ISIN/WKN match above. Using the wrong program's ratio would have been a serious, invisible error.

**Conclusion: the ratio is confirmed. The order-setup section below is NOT blocked on this data gap** (unlike the precedent where an unconfirmable ratio would have required stopping after the score).

---

## 3. Phase 01 Quality Gate (thresholds per [valuation-scoring.md](../framework/valuation-scoring.md))

All inputs sourced from the **primary KRX listing** (005930.KS), consolidated company-wide financials, via `yfinance`. ⚠️ **Segment-mix caveat applies to every margin/yield/multiple figure below** — see Section 5.

| Metric | Threshold | Samsung (consolidated) | Basis | Result |
|---|---|---|---|---|
| Gross margin | >40% | **47.68%** | TTM | ✅ PASS |
| Net margin | >12% | **21.46%** | TTM (Net Income ₩83.33T / Revenue ₩388.34T) | ✅ PASS |
| ROIC (Return on Invested Capital — net operating profit after tax ÷ [debt + equity − cash]) | >15% | **24.06%** | TTM NOPAT (EBIT × [1 − 8.64% effective tax rate]) ÷ FY2025 invested capital | ✅ PASS |
| Revenue growth (3yr CAGR) | >8% | **8.72%** (FY2022→TTM) | TTM basis — ⚠️ on a FY2022→FY2025-only basis (no TTM uplift) this is only **3.35%**, a FAIL. The TTM figure captures the Q1 2026 AI/HBM revenue inflection that the FY2025 annual figure does not yet fully reflect. | ✅ PASS (marginal, TTM-dependent) |
| FCF positive 3 consecutive years | Required | **FY2023 FCF = −₩16.40 trillion (NEGATIVE)** — FY2022 +₩9.05T, FY2023 **−₩16.40T**, FY2024 +₩19.24T, FY2025 +₩33.16T | Annual, `yfinance` cashflow statement | ❌ **FAIL** |
| Net debt/EBITDA | <2.5× | **−0.22×** (net cash position of ₩32.62T) | FY2025 debt/cash ÷ TTM EBITDA | ✅ PASS |
| FCF yield | >4% | **2.24%** | TTM FCF (₩52.06T) ÷ market cap | ❌ **FAIL** |
| EV/EBIT (Enterprise Value ÷ Earnings Before Interest and Tax) | <20× | **21.60×** | TTM EBIT (₩103.16T) — see EBIT-basis discussion below | ❌ **FAIL** (marginal — 1.6× over threshold) |

### Why TTM EBIT was used instead of FY2025

This decision materially affects the EV/EBIT gate result, so it's shown explicitly: Samsung's FY2025 annual EBIT was ₩50.09T, which would put EV/EBIT at a much higher **44.49×** — a clear gate fail. But the **TTM figure (₩103.16T)** more than doubles that, because Q1 2026 alone (quarter ended March 2026) posted ₩59.11T of EBIT — more than the *entire* FY2025 fiscal year — driven by the AI/HBM (High Bandwidth Memory, the premium DRAM used in AI accelerators) memory upcycle that intensified through late 2025/early 2026. This is not a one-off or an estimate; it's already-reported actual quarterly data. TTM is the more representative, current basis, and it's the same basis used consistently for both Samsung and its peers below (Section 5) — but even on this more favorable TTM basis, the EV/EBIT gate still fails (21.60× vs. the <20× threshold).

### FCF/Net Income conversion ratio (context, not a hard gate criterion at the Phase 01 stage but tracked per Phase 04)

| Year | FCF | Net Income | FCF/NI |
|---|---|---|---|
| FY2022 | ₩9.05T | ₩54.73T | 16.5% |
| FY2023 | −₩16.40T | ₩14.47T | −113.3% |
| FY2024 | ₩19.24T | ₩33.62T | 57.2% |
| FY2025 | ₩33.16T | ₩44.26T | 74.9% |
| TTM | ₩52.06T | ₩83.33T | 62.5% |

The FY2024→FY2025 trend is genuinely improving (57.2% → 74.9%), but the TTM ratio (62.5%) is below the framework's 70% conversion-quality threshold, and the multi-year history shows real volatility (including one badly negative year) rather than a clean, stable conversion track record. This pattern — earnings recovering faster than cash generation — is consistent with a heavy ongoing capex cycle (TTM capex = 52.2% of operating cash flow) to build HBM and foundry capacity.

### Gate Result: **❌ FAIL — 3 of 8 criteria fail** (FCF positive 3yr, FCF yield >4%, EV/EBIT <20×)

Per [.claude/commands/new-position.md](../.claude/commands/new-position.md): *"Walk the Phase 01 quality gate — if it fails, stop and report why rather than proceeding to scoring."* Strictly applied, this session should stop here. However, per this evaluation's specific brief (covering a complex multi-currency GDR case worth documenting in full for framework-design purposes), Phase 02 scoring, the fair-value analysis, and the qualitative review are still carried through below for completeness and to surface the segment-mix and cyclicality lessons this case illustrates — **but the gate failure stands as the controlling fact for the final recommendation** (Section 9).

---

## 4. Rate Environment Gate (run against US 10Y Treasury, per framework convention — see [strategy.md](../framework/strategy.md))

**Step 1 — Earnings Yield Spread Test**

- Forward PE (correctly derived — see "0y vs +1y" note in Section 5): **7.79×**
- Earnings Yield (EY = 1 ÷ Forward PE) = **12.83%**
- US 10Y Treasury yield = **4.46%** (2026-06-18, via `^TNX`; cross-checked against WebSearch — most current available, 2 days old)
- Spread = 12.83% − 4.46% = **+8.37 percentage points** → well above the +1.5% threshold → **no extra +5 flag**

**Step 2 — Rate Regime Modifier**

US 10Y at 4.46% falls in the **3.5%–5% band → Modifier = +5** (applied below in the Phase 02 score).

**Note on currency consistency (Rule 6):** the Rate Environment Gate itself stays US-Treasury-based per framework convention regardless of the underlying company's currency — this is unchanged from the DB1 (German Bund) and SGE (UK Gilt) precedent sessions. The **DCF discount rate**, by contrast, uses the *Korean* 10Y government bond yield as the risk-free input, since the DCF is being run in KRW (see Section 6).

⚠️ **Data staleness flag**: the Korean 10Y government bond yield could only be sourced to **3.69%, dated 2026-04-01** — roughly **2.5 months stale**. Multiple targeted WebSearch queries (including direct site-specific queries against tradingeconomics.com) failed to surface a more current figure. This is a materially larger staleness gap than the DB1/SGE precedent sessions, both of which obtained same-day risk-free rate figures. This is flagged explicitly per the framework's "never invent, flag what's missing" discipline — the DCF in Section 6 uses 3.69% as the best available figure, with this caveat carried forward.

---

## 5. Phase 02 Valuation Score

### 5a. The "0y vs +1y" Forward PE trap (resolved, per DB1/SGE precedent methodology)

`yfinance`'s `info["forwardPE"]` field returns **6.10×** for Samsung — but this is computed off the **'+1y'** consensus EPS estimate (₩58,035.6), not the standard "next fiscal year" forward estimate. The correct forward PE uses the **'0y'** row of `eps_trend`/`earnings_estimate` (₩45,425.7, current price ₩354,000 ÷ ₩45,425.668):

**Correct Forward PE = 7.79×** (vs. the misleading 6.10× yfinance reports by default)

The same correction was applied to both peers (Section 5c).

### 5b. FCF Yield Sub-score (40% weight)

```
FCF_Score = clamp(100 × (1 − FCF_Yield% / 10), 0, 100)
FCF Yield (TTM) = 2.24%
FCF_Score = 100 × (1 − 2.24/10) = 77.6
```

**FCF_Score = 77.6** — TTM FCF Yield of 2.24% is well below the 4% Phase 01 threshold, so this sub-score is unsurprisingly poor (high score = expensive on this metric).

*Owner Earnings (Upgrade 1) check*: Samsung's TTM capex is 52.2% of operating cash flow — high, but predominantly process-node/capacity-maintenance spend for memory and foundry rather than the discretionary growth capex Upgrade 1 targets (Azure-style cloud infrastructure buildout for MSFT/META/GOOGL/AMZN). Samsung is not on Upgrade 1's affected-business list, and no official management breakdown of "maintenance vs. growth" capex was found to support an Owner Earnings substitution without estimating it — per the "never invent or estimate financial data" rule, reported FCF is used as-is, flagged as a potential conservative bias (true owner earnings could be modestly higher if HBM capacity buildout skews more growth- than maintenance-flavored).

### 5c. EV/EBIT Sub-score (40% weight — PEG's 15% redistributed here; see 5e)

```
EV/EBIT_Score = clamp((EV/EBIT − 12) / 23 × 100, 0, 100)
EV/EBIT (TTM) = 21.60×
EV/EBIT_Score = (21.60 − 12) / 23 × 100 = 41.7
```

**EV/EBIT_Score = 41.7**

⚠️ **Segment-mix distortion — flagged explicitly per task instruction.** This 21.60× is a **consolidated** multiple, diluted by Samsung's lower-margin DX division (mobile, displays, consumer electronics). Official, full-year FY2025 segment data (Samsung's own Q4/FY2025 earnings release) shows:

| Segment | FY2025 Revenue | FY2025 Op. Profit | Op. Margin | % of Consolidated Revenue | % of Consolidated Op. Profit |
|---|---|---|---|---|---|
| **DS (semiconductors)** | ₩130.1T | ₩24.9T | **19.1%** | 39.0% | **57.1%** |
| **DX (implied: mobile/displays/CE)** | ₩203.5T (implied) | ₩18.7T (implied) | **9.2%** | 61.0% | 42.9% |
| **Consolidated** | ₩333.6T | ₩43.6T | 13.1% | 100% | 100% |

The semiconductor segment alone generates roughly **2× the operating margin** of the rest of the company, while being a minority of revenue. This means consolidated multiples systematically understate how cheap/expensive the actual memory/foundry business is relative to pure-play peers — the conglomerate structure is a **drag on the consolidated multiple's comparability**, not a moat in the EV/EBIT sub-score sense. This is addressed properly in the comparable-multiples fair value work (Section 6b) by using a sum-of-the-parts approach rather than applying peer multiples to consolidated EBIT directly.

### 5d. Forward PE Sub-score (20% weight)

5-year historical PE range reconstructed via the documented `yfinance` automation ([valuation-scoring.md](../framework/valuation-scoring.md) method — `get_earnings_dates` + rolling TTM EPS + price pairing). **Verified working for this KRX-listed foreign ticker**: `get_earnings_dates(limit=40)` returned 49 rows of real Reported EPS history back to 2014-05-15 — more than sufficient depth. 46 usable TTM-EPS-paired quarters were built; the trailing 20 (last 5 years) gave:

- 5yr Avg PE: **14.94×**
- 5yr Low PE: **7.14×** (Jan 2023)
- 5yr High PE: **32.62×** (Jan 2024)

```
FwdPE_Score (primary, range-based) = clamp((7.79 − 7.14) / (32.62 − 7.14) × 100, 0, 100) = 2.6
```

**Historical PE Modifier (Upgrade 2):** Forward PE (7.79×) sits **47.8% below** the 5-year average (14.94×) — well past the ">20% below average" threshold → **−10 modifier** applied.

```
FwdPE_Score (final) = clamp(2.6 − 10, 0, 100) = 0.0
```

⚠️ **Cyclical-earnings-trough distortion flagged.** The 5yr-high data point (32.62×, January 2024) is itself a classic cyclical artifact, not a "the market got euphoric" signal: FY2023's EBIT had collapsed to ₩11.9T (from ₩47.2T in FY2022) during the 2023 memory downturn, while the share price had already started pricing in recovery — producing a transient PE spike from a depressed-earnings denominator, not from genuine valuation excess. This is the mirror image of Upgrade 2's Structural Quality Override (which protects against penalizing multiple expansion that reflects *real* structural improvement) — here, the *historical comparison band itself* is inflated by a trough-earnings artifact rather than the current multiple being inflated by hype. The practical effect: the 5yr average (14.94×) may itself be skewed upward by this single distorted quarter, meaning today's −47.8% deviation could overstate how "cheap" Samsung's PE looks relative to a less-distorted average. No adjusted average is fabricated here (per "never invent" discipline) — this is flagged qualitatively. Directionally, even a corrected (lower) average would still likely leave today's 7.79× below it, so the −10 modifier's direction is not in question, only its precise magnitude.

### 5e. PEG Sub-score — N/A, excluded (Upgrade 3)

Samsung's trailing EPS growth would technically qualify it as a Lynch "Fast Grower" by the numeric >15%-for-3-years test (TTM net income is up sharply off the FY2023 trough) — but Upgrade 3 in [strategy.md](../framework/strategy.md) explicitly states PEG must **"Never apply to cyclicals or stalwarts,"** regardless of trailing growth math. Memory semiconductors are a textbook cyclical industry (multi-year DRAM/NAND boom-bust cycles), and the current growth spurt is unambiguously a cyclical upswing (the AI/HBM-driven 2025–2026 upcycle), not durable secular compounding. **PEG is excluded; its 15% weight is redistributed to EV/EBIT** (already reflected as the 40% weight used in Section 5c).

### 5f. Final Score Calculation

```
Weighted score = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
                = (77.6 × 0.40) + (41.7 × 0.40) + (0.0 × 0.20)
                = 31.04 + 16.68 + 0.0
                = 47.72

Final Score = Weighted score + Rate Regime Modifier
            = 47.72 + 5
            = 52.72 → rounds to 52.7
```

### **Phase 02 Final Score: 52.7 / 100.0 → "Fair Value" band (50.0–69.9)**

Per [strategy.md](../framework/strategy.md) Phase 03: Fair Value band = **Watchlist only — no new entry.**

---

## 6. Fair Value Analysis (shown for completeness, despite the Phase 01 gate failure and Fair-Value score band already pointing to no new entry)

All fundamentals in KRW (Rule 6 — currency consistency).

### 6a. Discounted Cash Flow (DCF), 3-stage, in KRW

**WACC (Weighted Average Cost of Capital) build:**
- Risk-free rate: Korean 10Y govt bond, **3.69%** (⚠️ stale, see Section 4)
- Equity risk premium: 5.0% (standard mature-market assumption)
- Beta: 1.1 (semiconductor-sector cyclicality premium over 1.0; Samsung's own raw beta tends to be dampened by conglomerate diversification, so a sector-typical beta is used instead — same judgment-call pattern as the DB1/SGE precedent sessions)
- Cost of equity = 3.69% + 1.1×5.0% = **9.19%**
- Cost of debt (after-tax): minimal weight — Samsung is net-cash, debt is only 1.07% of total capital
- **WACC ≈ 9.13%**

**Cash flow base:** TTM FCF = ₩52.06 trillion

**Stage 1 (Years 1–5):** Decelerating growth off the current AI/HBM upcycle peak — 18%, 14%, 10%, 7%, 5% (explicitly modeling cyclical fade, not flat extrapolation of the current upswing)
**Stage 2 (Years 6–10):** Further fade — 4.5%, 4.0%, 3.5%, 3.0%, 2.5%
**Terminal growth:** 2.0% (long-run KRW nominal-economy proxy)

| | Enterprise Value | + Net Cash (₩32.62T) | = Equity Value | ÷ Shares (5.764B) | FV/share |
|---|---|---|---|---|---|
| DCF | ₩1,144.5T | +₩32.6T | ₩1,177.1T | | **₩204,209** |

Terminal value = 53.7% of EV — within a normal range, not a red flag on its own.

**DCF says fair value (₩204,209) is 73.4% *below* the current price (₩354,000)** — i.e., the DCF sees Samsung as significantly overvalued at the current price. The reason: the DCF is anchored to **TTM FCF** (₩52.06T), which still reflects a heavy ongoing capex cycle (52.2% of operating cash flow) and a slower cash-recovery than the earnings-side recovery already visible in TTM EBIT (₩103.16T). The multiples-based signals in Section 5 (Forward PE, EV/EBIT) look cheap because they're earnings-anchored and the AI/HBM earnings upcycle is already strongly reflected in TTM EBIT; the DCF looks expensive because it's cash-anchored and the cash conversion hasn't caught up yet. **This divergence is a genuine finding, not a modeling error** — flagged prominently per Rule 6 ("value the underlying business, not the accounting statements... at face value").

### 6b. Comparable Multiples — Sum-of-the-Parts (SOTP), addressing the segment-mix distortion

**Peers and the Rule 5 scale-band check (±50% revenue):**

| Peer | TTM Revenue (USD) | TTM EV/EBIT | Within ±50% of Samsung consolidated ($253.8B)? | Within ±50% of Samsung DS-only ($85.0B)? |
|---|---|---|---|---|
| Micron (MU) | $58.1B | **45.03×** (TTM-corrected — see below) | ❌ No (77% below) | ✅ Yes |
| SK Hynix (000660.KS) | $86.3B | **20.57×** | ❌ No (66% below) | ✅ Yes (1.5% off, essentially same scale) |

**Micron EV/EBIT correction**: Micron's FY2025 (ended Aug 2025) EBIT basis gives a misleading **125.86×** — a stale annual lag that predates Micron's own AI/HBM inflection, which (like Samsung's) is now fully visible quarter by quarter. Rebuilding on a proper **TTM basis** (last 4 reported quarters through Feb 2026) gives **45.03×** — used here instead, for an apples-to-apples comparison with Samsung's own TTM-basis EV/EBIT.

**Confirmed finding**: both peers fail the Rule 5 ±50% scale-band test against Samsung's full **consolidated** revenue, but both **pass** against Samsung's **DS-segment-only** revenue ($85.0B) — concrete, full-year-data confirmation that segment-level comparison, not consolidated, is the methodologically valid basis for peer multiples here. Applying peer multiples directly to consolidated EBIT would overstate fair value by crediting the entire low-margin DX division with a semiconductor-peer multiple it doesn't deserve.

**SOTP construction:**
- Peer median EV/EBIT (n=2, TTM): (45.03 + 20.57) / 2 = **32.80×**
- Apply to DS segment FY2025 operating profit (₩24.9T, the closest available DS-only EBIT proxy — full-year, official, but not itself a TTM figure, so flagged as a slight understatement vs. the AI/HBM inflection visible in consolidated TTM data): DS implied EV = ₩24.9T × 32.80 = **₩816.7T**
- DX segment: no DX-specific peer set was run in this session (would require consumer-electronics/mobile-hardware peers like Apple/Sony, not attempted here). An illustrative, explicitly-flagged placeholder multiple of 10× is applied to implied DX operating profit (₩18.7T) = **₩187.0T**. **This DX-segment figure is the weakest-sourced number in this session** — flagged accordingly.
- Total implied EV (SOTP) = ₩816.7T + ₩187.0T = **₩1,003.7T**
- \+ Net cash ₩32.6T = Equity value ₩1,036.3T... 

  *(arithmetic note: computed precisely as ₩1,003.73T + ₩32.62T = ₩1,036.35T; divided by 5.764B shares)*
- **SOTP Fair Value per ordinary share ≈ ₩179,791**

For contrast — **and to make the segment-mix lesson concrete** — applying the peer median multiple naively to Samsung's full *consolidated* TTM EBIT (₩103.16T × 32.80×, ignoring the segment-mix flag entirely) gives **₩592,679/share**, more than 3× the segment-aware SOTP figure. This stark gap is exactly why the task called out the segment-mix distortion as something to flag "prominently wherever consolidated EV/EBIT... is used" — naively applying pure-play peer multiples to a diluted consolidated earnings base would have produced a wildly inflated, indefensible fair value.

### 6c. Blended Fair Value

Per the established 40% DCF / 60% multiples blend (precedent-session convention):

```
Blended FV = (₩204,209 × 0.40) + (₩179,791 × 0.60) = ₩189,558 per ordinary share
```

**Both independent methods — DCF and segment-aware SOTP multiples — converge on the conclusion that the current price is significantly overvalued.** This is a meaningfully different signal than Section 5's raw EV/EBIT and Forward PE sub-scores suggested in isolation, and is exactly the kind of "second-level thinking" (Howard Marks) the segment-mix and cyclicality flags exist to surface.

### 6d. Conversion to EUR per GDR

```
Blended FV per ordinary share: ₩189,558
× GDR ratio (25 ordinary shares per GDR): ₩4,738,951 per GDR
÷ EUR/KRW FX rate (1,754.0): €2,701.80 per GDR (blended fair value)
```

| | Value |
|---|---|
| **Blended Fair Value per GDR** | **€2,701.80** |
| **Live GDR price** | **€5,020.00** |
| **Premium of live price over blended FV** | **+85.8%** |

The GDR is trading at nearly **double** its blended intrinsic fair value estimate by this analysis.

---

## 7. Order Setup — NOT computed

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) and [operating-brief.md](../framework/operating-brief.md), buy price / sell target / stop loss / R/R (risk/reward ratio) / position sizing are only constructed for an actual entry recommendation. Given:
- The Phase 01 quality gate **fails** on 3 criteria, and
- The Phase 02 score (52.7) sits in the "Fair Value — Watchlist only, no new entry" band, and
- The independent fair-value analysis (Section 6) shows the live price at roughly **+86% above** blended fair value,

there is no scenario under this framework's rules that supports a buy order here. Order setup mechanics are not applicable.

---

## 8. Five Qualitative Questions

**1. Why are margins high?**
Where margins ARE high (the DS/semiconductor segment, 19.1% operating margin), it's a mix of (a) genuine technology leadership in memory (DRAM/NAND) manufacturing scale and process know-how, and (b) a currently favorable cyclical pricing environment — the 2025–2026 AI/HBM-driven memory upcycle has pushed prices and utilization sharply higher across the whole industry (Micron and SK Hynix show the same pattern). This is **partly structural** (scale, decades of process learning) and **partly cyclical** (industry-wide pricing tailwind that has reversed sharply before — see FY2023's collapse). The DX segment's margins (9.2% implied) are unremarkable and reflect a much more commoditized, competitive hardware business.

**2. What would it take to compete with them?**
In memory: enormous capital intensity (tens of billions in fab construction), multi-year process-node learning curves, and deep customer-qualification relationships (e.g., Nvidia's HBM4 qualification process) — high barriers, but Samsung is not uniquely positioned; SK Hynix and Micron clear the same bar. In foundry (chip manufacturing for other companies' designs): Samsung is the clear #2 globally behind TSMC, but its 2nm yields are reported in the mid-50%% range as of April 2026 — below the ~60-70% threshold typically considered the mass-production economics benchmark, and TSMC is reportedly winning top-tier customers (e.g., Qualcomm) on this gap. Foundry remains a weaker competitive position than memory.

**3. How has management allocated capital over 5–10 years?**
Heavy, sustained reinvestment into memory and foundry capacity (capex consistently 50%+ of operating cash flow), a large net-cash balance sheet (₩32.6T net cash, very low leverage — Net Debt/EBITDA of −0.22×), and a foundry division that has been **loss-making for four consecutive years**, with a return to profitability only expected as of Q3 2026 per recent reporting. This is a capital allocation track record of betting heavily and patiently on two capital-intensive, cyclical businesses — successful in memory, not yet proven in foundry.

**4. Where is growth coming from next 3–5 years?**
Primarily HBM (High Bandwidth Memory, the premium memory used in AI accelerator chips) and broader AI-driven memory demand. Samsung has passed Nvidia's HBM4 qualification and is the **#2 supplier** for Nvidia's Vera Rubin platform, but with a meaningfully smaller allocation than SK Hynix — industry estimates put Samsung's HBM4 share at roughly 25–30% vs. SK Hynix's 54–70% (sources diverge on the exact split, but consistently rank SK Hynix first). Secondary growth could come from foundry if 2nm yields and customer wins (Tesla's $16.5B order, talks with other AI/chip customers) continue to improve.

**5. Best bear case against owning it?**
(a) **Cyclicality risk**: memory pricing upcycles have reversed sharply before (FY2023's EBIT collapse from ₩47.2T to ₩11.9T is recent, direct evidence) — today's TTM-based "cheap" multiples could look very different in 12–18 months if the AI/HBM cycle peaks and rolls over, exactly the dynamic Upgrade 3's "never apply PEG to cyclicals" rule and the cyclical-PE-trough flag in Section 5d both exist to guard against. (b) **Segment-mix/conglomerate-discount risk**: the DX division's mediocre economics (9.2% operating margin) will likely continue to be a permanent drag on consolidated multiples and cash generation, regardless of how well the semiconductor cycle performs. (c) **Foundry execution risk**: four years of foundry losses and a continuing yield gap vs. TSMC raise real doubt about whether Samsung can translate 2nm investment into a profitable, scaled foundry business, or whether that capital is being persistently misallocated. (d) **The DCF/multiples divergence itself (Section 6) is a bear signal**: an independent, cash-flow-based valuation method sees the stock as ~73% overvalued even before any segment adjustment, suggesting the "cheap-looking" Forward PE and EV/EBIT sub-scores may be more a function of where we are in the earnings cycle than genuine mispricing.

**Disruption vector check:** No imminent technology shift threatens to make Samsung's memory/foundry moat irrelevant within 5 years — if anything, AI compute demand is reinforcing the value of advanced memory and leading-edge fabrication. The more relevant risk is competitive share loss within the existing paradigm (to SK Hynix in HBM, to TSMC in foundry), not disruption of the paradigm itself.

---

## 9. Recommendation: **PASS / WATCHLIST ONLY**

**The Phase 01 quality gate fails on 3 of 8 criteria** (FCF positive 3 consecutive years — FY2023 was negative; FCF yield >4% — actual 2.24%; EV/EBIT <20× — actual 21.60×). Per the framework's own process discipline, a gate failure should stop the evaluation before scoring — this session carried the analysis through to completion regardless (per this specific evaluation's brief, to fully document the multi-currency/GDR/conglomerate-segment lessons), but **the gate failure is the controlling fact**.

Even setting the gate aside, the **Phase 02 score of 52.7 lands in the "Fair Value" band (50.0–69.9)** — explicitly "Watchlist only, no new entry" per Phase 03 of [strategy.md](../framework/strategy.md) — not "Cheap" or "Very Cheap."

And the independent fair-value work (Section 6) — both the KRW-denominated DCF and the segment-mix-aware comparable-multiples sum-of-the-parts — converge on the live price being **roughly 73–86% above intrinsic fair value**, depending on method. The raw EV/EBIT and Forward PE sub-scores look superficially cheap largely because they're earnings-based metrics riding the current AI/HBM cyclical upswing; the cash-based DCF and the segment-corrected multiples approach both see through that and land on a much less favorable picture.

**No order setup is applicable.** This is added to the not-in-portfolio watchlist for future monitoring (next quarterly earnings, and any foundry profitability inflection in Q3 2026 per recent reporting, would be natural re-evaluation triggers), but does not support an entry today under this framework's rules.

---

## 10. Data quality flags carried forward (summary)

- **Korean 10Y government bond yield**: stale, ~2.5 months old (3.69%, dated 2026-04-01) — no fresher figure obtainable via WebSearch despite multiple targeted attempts. Used in the DCF discount rate; flagged for refresh at next review.
- **DX-segment EV/EBIT multiple in the SOTP** (Section 6b): the weakest-sourced number in this session — an illustrative 10× placeholder, not derived from a run DX-specific peer set. If this evaluation is revisited, sourcing actual consumer-electronics/mobile-hardware peer multiples (e.g., Apple, Sony) would materially strengthen the SOTP figure.
- **DS-segment EBIT basis**: FY2025 full-year (₩24.9T), not a TTM figure — likely a modest understatement of the current run-rate given the AI/HBM inflection visible in consolidated TTM data, since full-year DS-only TTM data isn't separately published by Samsung.
- **Ordinary Shares Number inconsistency**: yfinance's annual balance-sheet series shows shares outstanding rising from 5.940B (FY2024) to 6.630B (FY2025) despite Samsung's reported buyback activity; the live `sharesOutstanding` field (5.764B, lower than even the FY2025 balance-sheet figure) was used as primary per Rule 0's live-data discipline. This inconsistency is unresolved and flagged for awareness, not investigated further.
- **debtToEquity field** (5.782 in yfinance `info`) is anomalously high given Samsung's actual net-cash balance sheet — likely a units/normalization quirk in yfinance's KRX data feed. Not used in any calculation in this session (Net Debt/EBITDA was computed directly from balance-sheet debt/cash figures instead); flagged so a future session doesn't use this field at face value.

---

## 11. Token usage note

This session involved live IBKR price retrieval, ~10 rounds of yfinance/Python data pulls (Samsung + 2 peers, including a full quarterly TTM reconstruction and a 49-quarter historical PE series build), 6 WebSearch calls (GDR ratio corroboration, risk-free rate sourcing ×2, segment data ×2, qualitative/competitive research ×2), and a full DCF + SOTP build — consistent with the upper end of the ~120–160K token/ticker range cited in [.claude/commands/new-position.md](../.claude/commands/new-position.md)'s batch-processing guidance, given the added GDR-ratio-confirmation and segment-mix-adjustment work layered on top of a standard single-market evaluation.

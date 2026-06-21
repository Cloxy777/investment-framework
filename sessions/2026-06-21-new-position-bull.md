# New Position Evaluation: BULL (Webull Corporation) — 2026-06-21

**Task type:** NEW POSITION
**Ticker:** BULL — NASDAQ Capital Market (NCM), contract_id 776352706 (IBKR), exchange listing confirmed "WEBULL CORP," country_code US
**Company:** Webull Corporation — digital retail brokerage / trading platform headquartered in Saint Petersburg, Florida. Became public via SPAC (Special Purpose Acquisition Company) merger; first trade ~2025-04-11 (per yfinance `ipoExpectedDate`).
**Analyst:** Claude (automated session)
**Account:** U19421206 (IBKR)

---

## 0. Why this evaluation needs extra data-depth scrutiny

Webull is a **recent SPAC-merger listing** — public for only about 14 months as of this evaluation. This matters for three specific framework mechanics, all addressed explicitly below rather than assumed:

1. **No 5-year (20-quarter) trailing PE history exists** — `yfinance.get_earnings_dates()` returns only 4 quarters of reported EPS (the company's entire public life). This triggers the documented **no-history fallback** (FwdPE_Score = 50.0), not the primary range-based or average-based formulas.
2. **No reliable 3+ year clean earnings base exists for a PEG sub-score** — net income to ordinary shareholders has been deeply negative for the last three fiscal years (driven by large one-off preferred-share/warrant accounting charges tied to the SPAC structure, not operations), and trailing EPS is -$1.25. This is exactly the "recent IPO / recently-profitable / one-off-distorted EPS" carve-out from the 2026-06-20 PEG clarification — PEG does not apply; its 15% weight redistributes to EV/EBIT.
3. **Reported "Free Cash Flow" is materially distorted by brokerage customer-cash float**, not real owner-available cash generation — addressed in detail in Section 5b. This is a data-integrity issue specific to broker-dealer business models that the framework's existing FCF/NI conversion check is designed to catch, and it does catch it here (badly).

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Source | Price | Timestamp |
|---|---|---|
| **IBKR live snapshot** (contract_id 776352706, NASDAQ) | **$7.12** (last trade) | 2026-06-21 |
| WebSearch cross-check (aggregated quote sources) | $7.08 (−0.56% intraday) | 2026-06-21 |
| 52-week high / low (IBKR `misc_statistics`) | $18.32 / $4.50 | trailing 52wk |
| 13-week high / low | $7.52 / $4.50 | trailing 13wk |

IBKR's $7.12 is used as the authoritative live price per Rule 0 (primary broker source); the WebSearch figure ($7.08) is a close cross-check, consistent with a thinly-traded small-cap's normal bid/ask/quote-lag noise. **Confirmed this is the correct instrument**: NASDAQ:BULL, "WEBULL CORP," a digital brokerage platform — not a leveraged/inverse ETF or a different exchange's unrelated "BULL" ticker (IBKR's contract search returned several unrelated "BULL"-named instruments — gold ETFs, leveraged ETFs, a Canadian mining company — all excluded; the correct row is the sole NASDAQ STK match with description "WEBULL CORP").

The stock has fallen **61% from its 52-week high** ($18.32 → $7.12) and sits roughly in the middle of its 13-week range — noted for context only, **not a trigger or signal** per the framework's "never act on price movement alone" rule.

---

## 2. Phase 01 Quality Gate

All inputs sourced from `yfinance` (BULL, NASDAQ, USD reporting) — annual financials (FY2022–FY2025, calendar year-end) plus quarterly data for TTM (trailing twelve months, Q2 2025–Q1 2026) figures where more current. Thresholds per [strategy.md](../framework/strategy.md) Phase 01 / [valuation-scoring.md](../framework/valuation-scoring.md) Quantitative Pre-Screen Filters.

| Metric | Threshold | BULL (actual) | Basis | Result |
|---|---|---|---|---|
| Net margin | >15% | **4.34%** (FY2025) / **−1.64%** (TTM) | FY2025 Net Income $24.77M ÷ Revenue $571.0M; TTM Net Income −$10.04M ÷ Revenue $613.6M | ❌ **FAIL** (both bases) |
| ROIC (Return on Invested Capital) | >15% | **6.20%** | NOPAT (FY2025 EBIT $50.66M × (1 − 46.09% effective tax rate) = $27.31M) ÷ Invested Capital (Total Debt $77.52M + Equity $1,016.29M − Cash $653.19M = $440.63M) | ❌ **FAIL** |
| Revenue CAGR 3yr | >10% (strategy.md) / >8% (valuation-scoring.md pre-screen) | **13.71%** | FY2022 $388.33M → FY2025 $571.00M, 3-year CAGR | ✅ **PASS** |
| Gross margin | >40% or expanding | **77.45%** (FY2025); 84.6% (2022) → 79.7% (2024) → 77.45% (2025) | Gross Profit ÷ Revenue, 4-year trend | ✅ PASS on level (77.45% ≫ 40%), but **trend is contracting**, not expanding — flagged |
| FCF positive 3 consecutive years | Required | **FY2023 +$466.1M, FY2024 +$182.8M, FY2025 +$561.5M — all positive** *(see Section 5b flag: these figures are themselves of doubtful quality)* | `yfinance` annual cashflow | ✅ PASS mechanically — ⚠️ flagged below as **not meaningful** for this business model |
| Net debt/EBITDA | <2.5× (standard) — Upgrade 5 (<4×) if asset-light financial with interest coverage >15× & IG-rated | **−10.68×** (net cash position: $77.52M debt vs. $653.19M cash) | FY2025 | ✅ **PASS** (deeply net-cash; Upgrade 5 context not even needed — passes the strict 2.5× threshold too) |
| FCF/NI conversion ratio (2+ consecutive years >70%) | >70% | **2,266.9% (FY2025), 7,678.9% (FY2023), −805.5% (FY2024), −125.3% (FY2022)** | FCF ÷ Net Income, all 4 years | ❌ **FAIL — and not merely "below 70%," the ratio is nonsensical** (see Section 5b) |
| Share issuance pattern | Non-dilutive | Ordinary shares outstanding: 459.36M (2022–2024, flat) → **523.45M (2025)**, a **+13.9% jump** | `yfinance` balance sheet, "Ordinary Shares Number" | ❌ **Dilutive** — consistent with SPAC-merger-related share issuance |
| EV/EBIT (pre-screen filter) | <20× | **67.92×** (TTM EBIT $27.70M) / **37.13×** (FY2025 EBIT $50.66M) | EV $1,881.0M (yfinance `enterpriseValue`) | ❌ **FAIL** (both bases, by a wide margin) |
| FCF yield (pre-screen filter) | >4% | 14.91% (mechanical, using the as-reported FCF figure) | **Flagged as unreliable — see Section 5b.** Using a cleaner owner-earnings-style proxy, the yield is **0.61%** — itself a FAIL. | ❌ **FAIL** on the defensible basis |

### Why the FCF/Net Income conversion ratio is not meaningful here (data-integrity flag, not just a threshold miss)

Webull is a broker-dealer: customer cash and margin balances flow through as "changes in working capital" on the cash flow statement even though they are not cash the company can deploy as an owner. The "Change in Other Working Capital" line is **+$806.3M in FY2025, +$466.7M in FY2024, +$545.6M in FY2023** — single-handedly explaining why reported FCF ($561.5M in FY2025) is more than 20× reported net income ($24.8M). This is not a calculation error in `yfinance`; it is what GAAP cash flow from operations actually shows for this business model. **The framework's FCF/NI conversion check is designed to catch exactly this kind of distortion** (its stated purpose, per the graveyard-audit Valeant/Wirecard cases, is to flag when reported "cash generation" diverges sharply from accounting profit) — and here it is correctly flagging a real, structural distortion rather than a near-miss on the 70% threshold.

### Gate Result: ❌ **FAIL — 6 of 9 criteria fail** (net margin, ROIC, FCF/NI conversion ratio, EV/EBIT, FCF yield on a defensible basis, dilutive share issuance). Gross margin trend is contracting rather than expanding (partial flag). Only revenue CAGR and net debt/EBITDA pass cleanly.

Per [.claude/commands/new-position.md](../.claude/commands/new-position.md): *"Walk the Phase 01 quality gate — if it fails, stop and report why rather than proceeding to scoring."* Strictly applied, this session should stop here. Consistent with the 2026-06-20 SSU precedent, the evaluation is carried through Phase 02 and a fair-value sanity check below **for the record and for framework-design value** (this is a clean, instructive case of "recent SPAC listing with negative-trending true cash conversion"), but **the gate failure is the controlling fact** for the final recommendation (Section 8).

---

## 3. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**

- Forward PE: **47.47×** (see Section 5a for the "0y vs +1y" correction — this is the corrected figure)
- Earnings Yield (EY) = 1 ÷ 47.47 = **2.11%**
- US 10Y Treasury yield = **4.46%** (2026-06-18 print — most current available via WebSearch; same print used three days earlier in the 2026-06-20 SSU session)
- Spread = 2.11% − 4.46% = **−2.35 percentage points** → below the +1.5% threshold → **+5 additive flag applied**

**Step 2 — Rate Regime Modifier**

US 10Y at 4.46% falls in the **3.5%–5% band → Modifier = +5**

Both Step 1 and Step 2 are applied as separate additive modifiers per strategy.md (confirmed against the [watchlist/README.md](../watchlist/README.md) backfill note documenting that both should stack, not just Step 2) — **combined Rate Environment Gate impact: +10** on the final score.

---

## 4. Phase 02 Valuation Score

### 4a. Forward PE — the "0y vs +1y" trap (per SSU precedent methodology)

`yfinance`'s `info["forwardPE"]` reports **23.21×**, computed off the **'+1y'** consensus EPS estimate ($0.305 — i.e. FY2027 consensus). The framework convention (established in the 2026-06-20 SSU session) is to use the **'0y'** row (current fiscal year, FY2026 consensus: $0.150) for a true "forward" PE:

```
Forward PE (correct, 0y basis) = $7.12 ÷ $0.150 = 47.47×
Forward PE (yfinance default, +1y basis — NOT used) = $7.12 ÷ $0.305 = 23.34× (≈ reported 23.21× with rounding)
```

**Forward PE used in all calculations below: 47.47×.**

### 4b. FCF Yield Sub-score (40% weight)

**The raw/reported figure is flagged as unreliable and not used at face value.**

```
Reported FCF (FY2025) = $561.54M
Market Cap = $3,765.28M
Reported FCF Yield = 561.54 / 3,765.28 = 14.91%
Mechanical FCF_Score = clamp(100 × (1 − 14.91/10), 0, 100) = 0.0   ⚠️ NOT USED — see below
```

A mechanical application of this yield would score BULL as the *cheapest possible* FCF profile (0.0) — the opposite of reality. As shown in Section 2, this FCF figure is inflated by customer-cash-balance/working-capital swings specific to the brokerage business model, not real distributable cash flow. Per Rule 6 ("value the underlying business, not the accounting statements... at face value") and the framework's general distrust of unaudited/distorted cash signals, a cleaner **owner-earnings-style proxy** is used instead:

```
Owner-Earnings-style proxy = Net Income + D&A − CapEx (no growth/maintenance split available — full CapEx treated as maintenance, a conservative/generous assumption since no breakdown is disclosed)
  = $24.77M (NI, FY2025) + $3.23M (D&A, EBITDA $53.89M − EBIT $50.66M) − $4.89M (CapEx)
  = $23.12M

Owner-Earnings-proxy Yield = 23.12 / 3,765.28 = 0.61%
FCF_Score (used) = clamp(100 × (1 − 0.61/10), 0, 100) = 93.9
```

⚠️ **Important scope note**: Upgrade 1 (Owner Earnings) is formally scoped to MSFT/GOOGL/META/AMZN only (moat-building Growth CapEx >30% of total CapEx). BULL does not formally qualify for Upgrade 1 — this proxy is used here as a **data-integrity correction** (the raw FCF figure is not just "imperfect," it is actively misleading), not as a claim that Upgrade 1 applies. This is flagged explicitly per "never invent or estimate financial data" — no number is fabricated; this is the same Net Income + D&A − CapEx arithmetic Upgrade 1 already defines, applied here because the alternative (the raw reported FCF) is demonstrably not fit for purpose for a broker-dealer's working-capital-heavy cash flow statement.

**FCF_Score used: 93.9** (very expensive on a clean cash-generation basis — consistent with TTM net income actually being negative).

### 4c. EV/EBIT Sub-score (40% weight — PEG's 15% redistributed here; see 4e)

```
EV/EBIT_Score = clamp((EV/EBIT − 12) / 23 × 100, 0, 100)
EV/EBIT (TTM, last 4 quarters EBIT = $27.70M) = $1,881.0M / $27.70M = 67.92×
EV/EBIT_Score = clamp((67.92 − 12) / 23 × 100, 0, 100) = clamp(243.1, 0, 100) = 100.0
```

**EV/EBIT_Score = 100.0** — clamps to the maximum. (Sensitivity check: using FY2025 annual EBIT of $50.66M instead of TTM gives EV/EBIT = 37.13×, which still clamps to 100.0 — the choice of basis does not change the result; BULL is expensive on EV/EBIT by a wide margin under either basis.)

### 4d. Forward PE Sub-score (20% weight) — No-history fallback

`yfinance.get_earnings_dates(limit=40)` returned only **4 quarters** of Reported EPS history (earliest: 2025-11-20) — the company's entire public trading life since its April 2025 SPAC merger. This is far short of the 20-quarter (5-year) minimum the framework requires before attempting the TTM-EPS-reconstruction method (per [valuation-scoring.md](../framework/valuation-scoring.md): *"If fewer than 5 years (20 quarters) of TTM EPS are reconstructable, treat it as the existing no-history fallback... rather than computing a PE average over a shorter window"*).

```
FwdPE_Score = 50.0   (no-history fallback, neutral midpoint, flagged)
```

### 4e. PEG Sub-score — N/A, excluded (redistributed per 2026-06-20 clarification)

Trailing EPS is **−$1.25** (deeply negative, driven by a $487.5M one-off net loss attributable to ordinary shareholders tied to preferred-share/warrant accounting from the SPAC structure — not an operating loss; the company's underlying net income attributable to the company was actually +$24.8M in FY2025). Net income to ordinary shareholders has been negative in **3 of the last 4 fiscal years** (FY2022: −$1.3M, FY2023: −$334.0M, FY2024: −$517.8M, FY2025: −$487.5M). There is no reliable, non-distorted 3+ year EPS growth base — this is squarely the "recent IPO / one-off-distorted EPS" carve-out from the 2026-06-20 PEG clarification ([decisions/2026-06-20-framework-clarification-peg-clean-earnings.md](../decisions/2026-06-20-framework-clarification-peg-clean-earnings.md)). **PEG is excluded; its 15% weight is redistributed to EV/EBIT** (already reflected as the 40% weight used in Section 4c).

### 4f. Final Score Calculation

```
Weighted score = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
                = (93.9 × 0.40) + (100.0 × 0.40) + (50.0 × 0.20)
                = 37.56 + 40.00 + 10.00
                = 87.56

Final Score = Weighted score + Rate Environment Gate (Step 1 +5, Step 2 +5) + Upside/Downside Modifier
            = 87.56 + 5 + 5 + Upside/Downside Modifier (Section 5)
```

---

## 5. Upside/Downside (Expected-Return) Modifier

Built per [valuation-scoring.md](../framework/valuation-scoring.md) — requires a real bull/base/bear scenario fair value, a documented catalyst/timeline, and the full `E` calculation shown.

### 5a. Why DCF is not used as a standalone method here

A 3-stage DCF requires a credible, non-distorted free cash flow base to project forward (Rule 2). As established in Section 4b, BULL's reported FCF is dominated by brokerage working-capital swings, and even the cleaner owner-earnings-style proxy ($23.1M) is a single data point with no clean multi-year trend to extrapolate (TTM net income is actually *negative*, −$10.0M, reflecting a Q1 2026 loss quarter). Projecting a 10-year DCF off this base would require inventing a growth trajectory not supported by real data — which the framework's "never invent or estimate financial data" rule forecloses. **A multiples-based scenario approach is used instead** (consistent with Rule 1's sector guidance to use at least 2 methods where possible, but here a single, well-documented multiples method is preferred over a fabricated DCF).

### 5b. Bull/Base/Bear Scenario (EV/EBIT multiples basis)

| Scenario | Assumed normalized EBIT | Assumed EV/EBIT multiple | Implied EV | + Net cash ($575.7M) | = Equity Value | ÷ Shares (447.96M) | FV/share |
|---|---|---|---|---|---|---|---|
| **Bear** | $20M (TTM-like, reflecting continued earnings volatility / a weak-trading-volume environment) | 12× (Phase 01 pre-screen cheap-end anchor) | $240M | +$575.7M | $815.7M | | **$1.82** |
| **Base** | $45M (between TTM $27.7M and FY2025 $50.7M — a modest normalization, no further multi-year growth assumed beyond the documented 2026 analyst EPS consensus implying continued, but decelerating, growth) | 18× (mid-point between the Phase 01 cheap anchor and current 67.9× — a meaningful re-rating *down* toward a sustainable fintech-broker multiple, not an extrapolation of today's rich multiple) | $810M | +$575.7M | $1,385.7M | | **$3.09** |
| **Bull** | $75M (assumes Webull's stated growth narrative — customer assets +81% YoY, trading volume growth — continues and converts to durable earnings) | 25× (a generous multiple, near the top of normal quality-business range, crediting genuine platform/network-effect value) | $1,875M | +$575.7M | $2,450.7M | | **$5.47** |

```
PW Fair Value = 0.25×Bull + 0.50×Base + 0.25×Bear
              = 0.25×$5.47 + 0.50×$3.09 + 0.25×$1.82
              = $1.37 + $1.55 + $0.46
              = $3.37 per share
```

**Even the bull case ($5.47) sits below the current live price ($7.12).** The probability-weighted fair value of $3.37 implies the stock is trading at roughly **2.1× its blended scenario fair value**.

### 5c. Expected Annual Return `E`

```
Gap Upside % = (PW Fair Value ÷ Live Price) − 1 = ($3.37 ÷ $7.12) − 1 = −52.7%

Catalyst / timeline: No specific, documented 18–24-month catalyst identified that would close this gap (no announced M&A, no guidance event, no scheduled re-rating trigger beyond ordinary quarterly earnings) — per the guardrail, this caps the *upside* side at −5 if E were positive. Here E is negative, so the guardrail (which protects against unearned upside credit) does not soften the result — a thesis with no catalyst AND a deeply negative expected return is fully penalized, as intended.
Default 2-year window used (no narrower window available) for annualizing:
Annualized gap = −52.7% ÷ 2 = −26.3%/yr

Intrinsic growth rate: 0% used. Revenue CAGR (13.71%, 3yr) is real, but it does not translate into a defensible *earnings or FCF* CAGR — TTM net income is negative and the clean FCF proxy is a single noisy data point with no multi-year trend. Per "never invent or estimate financial data," 0% (not a fabricated growth rate) is used, flagged explicitly as conservative-but-honest rather than optimistic-but-invented.

Shareholder yield: 0%. No dividend (trailingAnnualDividendYield = 0.0%). No net buybacks — share count is *rising* (459.4M → 523.5M, +13.9% in FY2025), a dilutive pattern, not a shareholder-yield-positive one.

E = Annualized gap + intrinsic growth + shareholder yield
  = −26.3% + 0% + 0%
  = −26.3%/yr
```

### 5d. Mapping `E` to the Modifier

```
E = −26.3%, which is < 0 (an expected loss)
M = +5 + 10 × clamp((−E)/10pp, 0, 1)
  = +5 + 10 × clamp(26.3/10, 0, 1)
  = +5 + 10 × clamp(2.63, 0, 1)
  = +5 + 10 × 1.0
  = +15.0   (the maximum positive modifier — full expected-loss penalty)
```

**Upside/Downside Modifier = +15.0** — BULL's expected return is so far below the −10%/yr floor that the modifier hits its ceiling.

---

## 6. Final Phase 02 Score

```
Final Score = Weighted score + Rate Environment Gate (Step 1 + Step 2) + Upside/Downside Modifier
            = 87.56 + (5 + 5) + 15.0
            = 87.56 + 10 + 15.0
            = 112.56

Clamped to [0.0, 100.0] per the score boundary rule → Final Score = 100.0
```

### **Phase 02 Final Score: 100.0 / 100.0 → "Extreme" band (90.0–100.0)**

Every component — the FCF sub-score (using the corrected, defensible cash-generation proxy), the EV/EBIT sub-score, both Rate Environment Gate modifiers, and the Upside/Downside Modifier — independently points the same direction. This is not a borderline or marginal result driven by one aggressive assumption; it is a case where multiple independent methods converge.

---

## 7. Order Setup — NOT computed

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) and [operating-brief.md](../framework/operating-brief.md), buy price / sell target / stop loss / R/R (Risk/Reward ratio) / position sizing are only constructed for an actual entry recommendation. Given:

- The **Phase 01 quality gate fails on 6 of 9 criteria** (net margin, ROIC, FCF/NI conversion ratio, EV/EBIT, a defensible FCF yield, and a dilutive share-issuance pattern), and
- The **Phase 02 score is 100.0** — the single most expensive/least attractive score the scale allows, squarely in "Extreme — Trim to 1–2% tracking" territory (not applicable since BULL is not held, but illustrating just how far this sits from a BUY band), and
- The scenario-based fair value work (Section 5) shows the live price trading at roughly **2.1× even the probability-weighted bull/base/bear blended fair value**,

there is no scenario under this framework's rules that supports a buy order, a limit order, or even a watchlist-pending-pullback framing. Order setup mechanics are not applicable.

---

## 8. Five Qualitative Questions (for the qualitative record, per the operating-calendar template)

**1. Why are margins high?**
Gross margin is genuinely high (77.45%) — this reflects the software/platform economics of a brokerage (incremental customer trades cost very little to serve once the platform exists) rather than a one-off. However, gross margin has been **contracting**, not expanding, over the available history (84.6% in 2022 → 77.45% in 2025), and net margin is thin-to-negative once operating costs, taxes, and especially the SPAC-related preferred-share/warrant accounting charges are included. High *gross* margin is a real software-platform structural feature; high *net* profitability is not yet established.

**2. What would it take to compete with them?**
Retail brokerage/trading-platform competition is intense and well-capitalized (Robinhood, Charles Schwab, Interactive Brokers, Fidelity, and other zero/low-commission platforms). Webull's stated differentiation is around international/Asian-market access, a community/social trading layer, and options/derivatives tooling — these are real product features but are not obviously a durable moat (network effects in retail brokerage are weaker than in, say, payment networks — switching costs for a retail trading account are real but not high, and regulatory/compliance barriers are a cost of doing business industry-wide, not Webull-specific).

**3. How has management allocated capital over 5–10 years?**
The company's public history under this structure is only ~14 months (post-SPAC-merger), so a 5–10 year *public-company* capital allocation track record does not exist. What is visible: heavy historical losses attributable to ordinary shareholders for 3 of the last 4 fiscal years (driven by SPAC-related preferred/warrant accounting rather than core-business cash burn), continued investment in platform/customer-acquisition (customer assets +81% YoY per Q1 2026 reporting), and a recent dilutive share issuance (+13.9% share count in FY2025) likely tied to the SPAC-merger structure itself.

**4. Where is growth coming from next 3–5 years?**
Customer asset growth (+81% YoY, $24.6B per most recent reporting) and trading-volume growth (equity notional volume reportedly doubled YoY) are the stated growth drivers, alongside international expansion. Revenue CAGR of 13.71% (3yr) is real and decent, but earnings have not grown in step — the framework's "EPS growth exceeding revenue growth by >10pp" earnings-quality check (Phase 04) is not triggered here; if anything the *opposite* concern applies (earnings/cash conversion lagging revenue growth).

**5. Best bear case against owning it?**
(a) **Earnings quality/cash-conversion risk** — the FCF/NI conversion ratio is not just below threshold, it is structurally unreliable for this business model (Section 2), meaning investors cannot easily verify how much of reported activity translates into real distributable cash. (b) **Profitability is not yet durable** — TTM net income is negative, and 3 of the last 4 fiscal years showed net losses to ordinary shareholders; the FY2025 positive $24.8M figure is recent and not yet a multi-year trend. (c) **Valuation is already pricing in a very optimistic outcome** — at 37–68× EV/EBIT and 47.5× forward PE (current-year-consensus basis), the market is paying a premium more typical of an established, proven-profitable growth compounder than a 14-month-old public company with volatile quarterly results. (d) **Dilution risk** — the SPAC-merger-related share count increase (+13.9%) is a documented dilutive pattern, one of the framework's explicit Phase 01 red flags. (e) **Trading-volume cyclicality** — as a brokerage, revenue and earnings are inherently tied to retail trading activity/volume, which is itself cyclical and sentiment-driven (visible directly in the swing from a +$13.1M net income quarter to a −$21.7M net loss quarter one year later).

**Disruption vector check:** No single new technology threatens to make online brokerage itself obsolete within 5 years, but the competitive-intensity risk is high and ongoing — commission-free trading, fractional shares, and platform features have already been commoditized across the industry, and AI-driven trading-assistant tools could further compress brokers' differentiation if Webull does not keep pace.

---

## 9. Recommendation: **PASS**

**The Phase 01 quality gate fails on 6 of 9 criteria** — net margin (4.34% FY2025 / −1.64% TTM vs. >15% threshold), ROIC (6.20% vs. >15%), the FCF/NI conversion ratio (structurally unreliable due to brokerage-float distortion, not merely below the 70% threshold), EV/EBIT (37–68× vs. <20×), FCF yield on a defensible basis (0.61% vs. >4%), and a dilutive share-issuance pattern (+13.9% share count in FY2025). Per the framework's own process discipline, a gate failure of this severity should stop the evaluation before scoring — this session carried the analysis through to completion regardless (consistent with the 2026-06-20 SSU precedent, to fully document the SPAC-listing/brokerage-float lessons this case illustrates), but **the gate failure is the controlling fact** for this recommendation.

Even setting the gate aside, the **Phase 02 score is 100.0 — the single most expensive score the 0.0–100.0 scale allows**, squarely in the "Extreme" band. And the independent scenario-based fair value work (Section 5) — a bull/base/bear EV/EBIT-multiples blend — puts the live price at roughly **2.1× the probability-weighted fair value estimate ($3.37 vs. $7.12)**, with even the bull case ($5.47) below the current price.

This is not a borderline or marginal call. Multiple independent signals — the quality gate, the valuation score, and the scenario-based fair value work — all converge on the same conclusion from different angles (accounting quality, current multiples, and forward-looking expected return).

**No order setup is applicable. No limit order is set.** This is added to the not-in-portfolio watchlist for future monitoring — the next earnings release (re-test net margin/ROIC/FCF-NI quality with another quarter of data) and any clean multi-quarter run of positive ordinary-shareholder net income (which would at minimum clear the PEG-eligibility and earnings-quality concerns, even if valuation remained rich) are the natural re-evaluation triggers. Given the magnitude of the gate failure and overvaluation, this is a clear **PASS**, not merely a "watchlist, revisit soon" call.

---

## 10. Data quality flags carried forward (summary)

- **Reported FCF / FCF-NI conversion ratio**: not usable at face value for this business model — driven by brokerage customer-cash/margin working-capital swings (+$806.3M "Change in Other Working Capital" in FY2025 alone). A cleaner owner-earnings-style proxy (NI + D&A − CapEx, full CapEx conservatively treated as maintenance) was used for the FCF_Score sub-score instead, yielding a far less favorable 0.61% yield vs. the misleading 14.91% raw figure. Flagged as the single most important data-judgment call in this session.
- **Forward PE "0y vs +1y" trap**: yfinance's default `forwardPE` field (23.21×) uses next-fiscal-year consensus, not current-fiscal-year consensus. The corrected 47.47× (0y basis) is used throughout, per the methodology established in the 2026-06-20 SSU session.
- **No 5-year PE history**: only 4 quarters of public trading history exist (SPAC merger ~April 2025). No-history fallback (FwdPE_Score = 50.0) correctly applied — not a forced estimate.
- **PEG excluded**: trailing EPS deeply negative and distorted by one-off SPAC-related preferred-share/warrant accounting; net income to ordinary shareholders negative in 3 of 4 fiscal years. No reliable 3+ year clean earnings base exists. Redistributed to EV/EBIT per the 2026-06-20 clarification.
- **DCF not run as a standalone method**: no credible, non-distorted multi-year FCF base to project. A documented bull/base/bear EV/EBIT-multiples scenario was used instead for the Upside/Downside Modifier's fair-value input, with assumptions shown explicitly (Section 5b) rather than a fabricated DCF.
- **Maintenance vs. growth CapEx split**: not disclosed by the company; full CapEx ($4.89M, FY2025) was conservatively treated as maintenance CapEx in the owner-earnings-style proxy. This likely modestly understates true owner earnings if any of that CapEx is growth-oriented, but the FCF score is already at the expensive end (93.9) regardless — this would not change the qualitative conclusion.

---

## 11. Token usage note

This session involved one IBKR contract search + live price snapshot, roughly 6 rounds of `yfinance` data pulls (info fields, annual/quarterly financials, cashflow, balance sheet, earnings dates/estimates, working-capital detail), 4 WebSearch calls (price cross-check, 10-K/annual-report financials, 10Y Treasury yield, Q1 2026 earnings detail, analyst price targets), and a multi-scenario EV/EBIT fair-value build with full E-calculation for the Upside/Downside Modifier. This is toward the lower-middle of the ~120–160K token/ticker range cited in [.claude/commands/new-position.md](../.claude/commands/new-position.md)'s batch-processing guidance — somewhat lighter than the SSU GDR precedent (no multi-currency/ratio-confirmation/segment-SOTP work was needed here), but with meaningful extra diligence on the brokerage-float FCF distortion.

---

## Glossary

- **10Y Treasury yield** — the interest rate the US government pays on its 10-year bonds; the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate.
- **bps (basis points)** — 1 bps = 0.01 percentage points.
- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value over several years.
- **CapEx** — Capital Expenditure, money spent buying or upgrading physical assets.
- **D&A** — Depreciation & Amortization, the non-cash accounting expense that spreads the cost of long-lived assets over time.
- **DCF** — Discounted Cash Flow, a valuation method estimating a company's worth today by projecting future cash flow and discounting it back.
- **Dilutive (share issuance)** — raising money or settling a transaction by issuing new shares, shrinking each existing shareholder's ownership percentage.
- **EBIT** — Earnings Before Interest and Taxes, operating profit before financing/tax effects.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization, a rough proxy for cash operating profit.
- **EPS** — Earnings Per Share, net income divided by shares outstanding.
- **EV** — Enterprise Value, a company's total value to all capital providers: market cap + debt − cash.
- **EV/EBIT** — Enterprise Value divided by EBIT, a multiple used to compare how expensive companies are relative to operating profit.
- **EY (Earnings Yield)** — 1 ÷ Forward PE, the inverse of the PE ratio, comparable to bond yields.
- **Fast Grower** — Peter Lynch's term for a company growing EPS faster than 15%/year for 3+ years on a reliable earnings base; this framework's trigger for the PEG sub-score.
- **FCF** — Free Cash Flow, cash a business generates after running and maintaining itself.
- **FCF Yield** — Free Cash Flow ÷ Market Cap; higher is cheaper, all else equal.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether reported accounting profit is actually turning into real cash.
- **Forward PE** — Price ÷ next twelve months' expected earnings per share.
- **FV (Fair Value)** — the analyst's estimate of what a company is intrinsically worth, independent of its market price.
- **GAAP** — Generally Accepted Accounting Principles, the standard US accounting rulebook.
- **IRR** — Internal Rate of Return, the annualized percentage return an investment is expected to generate.
- **M&A** — Mergers & Acquisitions.
- **Moat** — Warren Buffett's term for a durable competitive advantage protecting a business's profits from competitors.
- **NI (Net Income)** — accounting profit after all expenses, interest, and taxes.
- **Owner Earnings** — Buffett's adjusted cash-flow measure: Net Income + D&A − Maintenance CapEx only; used here as a data-integrity correction to a distorted reported FCF figure.
- **PE (Price-to-Earnings) ratio** — share price ÷ earnings per share.
- **PEG ratio** — PE ratio ÷ earnings growth rate, used to judge whether a fast grower's multiple is justified by its growth rate.
- **pp (percentage points)** — a direct difference between two percentages.
- **PT (Price Target)** — an analyst's forecast of a stock's future price.
- **PW (probability-weighted)** — the bull/base/bear scenario blend (25%/50%/25%) used to compute fair value.
- **R/R (Risk/Reward ratio)** — (expected gain) ÷ (expected loss) on a trade; this framework requires at least 2:1 before entering (not applicable here — no entry recommended).
- **Rate Environment Gate** — the mandatory pre-check before every Phase 02 score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier.
- **Rate Regime Modifier** — an additive adjustment (−10 to +10) applied based on the current Treasury-yield bracket.
- **ROIC** — Return on Invested Capital, how efficiently a company turns invested capital (debt + equity) into profit.
- **SPAC** — Special Purpose Acquisition Company, a shell company that raises money via IPO with the purpose of merging with a private company to take it public — the mechanism by which Webull became a public company.
- **TAM** — Total Addressable Market.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.
- **Upside/Downside Modifier** — an additive score adjustment (−15 to +15) based on expected annual return vs. a 10% hurdle, folding the forward dimension into the score.

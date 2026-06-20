# RESCORE — ZS (Zscaler, Inc.) — 2026-06-20

**Task type:** RESCORE (single ticker; first run applying the new Upside/Downside Modifier)
**Date:** 20 Jun 2026
**10Y US Treasury Yield:** 4.451% (^TNX close 18 Jun 2026, via `yfinance`; market closed intraday today gives same last close)
**Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% bracket) — plus a separate +5 from the Step-1 Earnings-Yield-Spread flag (see §3)

This is the first ZS re-score to apply the **Upside/Downside Modifier (Expected-Return Modifier)** added to `valuation-scoring.md` on 2026-06-20 — folding expected forward return (gap to probability-weighted fair value, annualized over the catalyst window, plus intrinsic growth and shareholder yield) into the single score.

---

## 1. Live Data (Rule 0 — fetch prices first, never infer)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$124.85** | `yfinance` `currentPrice`/`regularMarketPrice` (IBKR `get_price_snapshot` permission was denied this session — fell back per the prompt's stated order) |
| Prior close | $124.38 | `yfinance` |
| **52-week range** | **$114.63 – $336.99** | `yfinance` — price sits ~9% off the 52-wk low, ~63% below the high |
| **Analyst consensus PT** | mean **$193.05**, median $190, range $145–$250 (n=45) | `yfinance` `targetMeanPrice` etc. |
| 10Y Treasury | 4.451% | `yfinance` ^TNX, 18 Jun 2026 close |

> **Rule 0 note:** The prior ZS records used $129.60 (05 Jun 2026). Price is refreshed to $124.85 — a −3.7% move, no fundamental trigger, within the "act only on a documented trigger" discipline. The re-score itself is the routine valuation refresh.

> **Jargon, plain-English on first use:** FCF = free cash flow (operating cash flow minus capital expenditure — the cash a business actually generates after maintaining/growing its asset base). NI = net income (accounting bottom-line profit). GAAP = Generally Accepted Accounting Principles (the standardized US accounting rules; "GAAP loss" = a reported accounting loss). Non-GAAP / adjusted EPS = earnings per share with stock-based compensation and one-offs stripped out (what management and analysts headline). SBC = stock-based compensation (paying staff in shares — a real cost that dilutes owners but isn't a cash outflow). EV/EBIT = enterprise value ÷ earnings before interest & tax (a debt-neutral valuation multiple). PEG = price/earnings-to-growth ratio (forward PE divided by the earnings growth rate; <1 cheap-for-growth, >2 expensive). MoS = margin of safety (the discount to fair value demanded before buying). PW = probability-weighted (the bull/base/bear blend). CAGR = compound annual growth rate. R/R = reward-to-risk ratio. pp = percentage points.

---

## 2. Standard Re-Score Inputs (all from `yfinance`, computed where the doc allows)

| Metric | Value | Notes |
|---|---|---|
| Sector | Tech — Cybersecurity (Zero Trust / SaaS) | unchanged |
| **FCF yield** | **4.410%** | TTM (trailing-twelve-month) FCF $890.3M (sum of last 4 quarters) ÷ market cap $20.19B. Cash-based, used because NI is a GAAP loss (see SBC distortion note). |
| EV/EBIT | **undefined** | TTM GAAP EBIT = **−$29.2M** (still negative) → EV/EBIT not computable → neutral placeholder (flagged) |
| Enterprise Value | $18.52B | Mkt cap $20.19B − net cash $1.67B (totalCash $3.54B, totalDebt $1.87B) — **net-cash gap from the prior pass now resolved** |
| Forward PE | **27.16×** | `yfinance` forwardPE; implies forward non-GAAP EPS ≈ $4.60 |
| Current TTM non-GAAP EPS | $3.94 | reconstructed from `get_earnings_dates` (reported/adjusted EPS), positive and growing |
| 5yr avg PE | 161× (20q) — **distorted**; 3yr avg **67×** used | The 5yr window is inflated by the 2021–22 SaaS-bubble peaks (PE 600× → 32× de-rating). The post-bubble 3yr window (67× avg, 32–90× range) is the representative benchmark — using the bubble-distorted 5yr avg would falsely flag ZS as deeply cheap. |
| Revenue CAGR 3yr | **34.8%** | FY2022 $1,090.9M → FY2025 $2,673.1M (`t.financials`) |
| ROIC | negative (~−2 to −4%) | `returnOnEquity` −3.7%; GAAP operating margin −3.3% → **fails Phase 01 quality gate** on a GAAP basis |
| Gross margin | **76.7%** | very high (software scale economics) |
| Net margin | **−2.4%** | GAAP net loss; NI −$77.4M TTM |
| Net debt/EBITDA | **net cash** | net cash $1.67B; TTM EBITDA +$142M → no leverage concern (Debt Gate passes trivially) |
| FCF/NI conversion | **not meaningful** | NI is negative → ratio negative/undefined. This is the SBC distortion: FCF is strongly positive ($890M TTM) while GAAP NI is a small loss, because SBC and other non-cash items sit between them. **Use cash-based FCF, not NI** (per prompt and Rule 2 "never use net income as a proxy for FCF"). |
| Dividend yield | 0% | no dividend |
| Current weight | 0.24% | holdings.md |
| Last score | 61.1 (low-confidence), Jun 2026 | holdings.md / 2026-06-11 |

**Fast Grower (Upgrade 3) eligibility — CONFIRMED.** Revenue CAGR 34.8% (3yr) and a 5-year run of rising non-GAAP EPS ($0.24 → $3.94 TTM) clear the ">15% growth for 3+ years" bar. PEG is therefore an applicable 15%-weight sub-score (not redistributed, unlike the prior two passes which lacked a usable earnings base). PEG = 1.36 (`yfinance`).

**Low-confidence inputs — resolution status:**
- ✅ **Net-debt/cash gap RESOLVED** — totalCash $3.54B / totalDebt $1.87B sourced; EV $18.52B clean.
- ✅ **PE-history gap RESOLVED** — a real positive non-GAAP EPS series exists; 5yr PE reconstructable (3yr post-bubble window used as the non-distorted benchmark). Prior pass wrongly concluded "no meaningful PE history" by reading GAAP losses only.
- ✅ **PEG RESOLVED** — prior PEG of 34.55 was built on a near-zero GAAP earnings base; the correct non-GAAP-based PEG is 1.36.
- 🚩 **EV/EBIT REMAINS a flagged placeholder** — TTM GAAP EBIT is still negative (−$29.2M), so the multiple is genuinely undefined; not invented. This is the one input that keeps a residual flag, but it is now an *isolated* placeholder (1 of 4 inputs) rather than the compounding 2-of-4 gap that drove the prior low-confidence label.

**Net: the low-confidence flag is substantially RESOLVED** — downgraded from "low-confidence (two compounding placeholder inputs + unusable PEG)" to "EV/EBIT placeholder only (GAAP EBIT negative)."

---

## 3. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test:** EY (earnings yield = 1 ÷ forward PE) = 1 ÷ 27.16 = 3.68%. Spread = 3.68% − 4.451% (10Y) = **−0.77%** → below the +1.5% bar → **FAIL → +5 to the score** (yellow flag, not a veto; per strategy.md 2026-06-07).

**Step 2 — Rate Regime Modifier:** 10Y at 4.451% sits in the 3.5–5% bracket → **+5**.

**Total rate-related additive: +10** (+5 Step 1 + +5 Step 2).

---

## 4. Full Score Calculation (every sub-score shown)

```
FCF_Score    = clamp(100 × (1 − 4.410/10), 0, 100)              = 55.90      (40% weight)
EV/EBIT_Score = 50.0  (neutral placeholder — TTM GAAP EBIT negative, flagged)  (25% weight)
FwdPE_Score  = clamp(50 + ((27.16 − 67.0)/67.0 × 100) × 2.5, 0, 100)
             = clamp(50 + (−59.5%) × 2.5, 0, 100) = clamp(50 − 148.8, 0, 100) = 0.0   (20% weight)
PEG_Score    = clamp((1.36 − 0.5)/2.0 × 100, 0, 100)            = 43.00      (15% weight)

Raw weighted = 55.90×0.40 + 50.0×0.25 + 0.0×0.20 + 43.00×0.15
             = 22.360 + 12.500 + 0.000 + 6.450
             = 41.31
```

**Forward-PE note:** the fallback formula (5yr *average* only, no clean range) folds in the Historical-PE Modifier (Upgrade 2) — no separate ±10 applied. The forward PE (27.16×) is ~59% below even the post-bubble 3yr average (67×), so the sub-score floors at 0.0. This is directionally honest (ZS trades cheaper than its own recent history) but is the input most sensitive to the chosen benchmark window — flagged.

---

## 5. Upside/Downside Modifier (Expected-Return Modifier) — REQUIRED, new this session

### Step 1 — Scenario fair values (Rule 7, bull/base/bear) → PW Fair Value

ZS is a Fast Grower SaaS name; fair value is anchored on forward non-GAAP EPS × multiple and forward FCF/share × multiple (Rule 1 Tech/Growth: DCF/PEG/EV-Rev), cross-checked against the analyst consensus PT band ($145–$250, median $190).

- Forward non-GAAP EPS ≈ **$4.60** (124.85 ÷ 27.16 fwd PE); TTM FCF/share = $890.3M ÷ 161.71M sh = **$5.51**.

| Scenario | Weight | Key assumption | EPS-method | FCF-method | Blended (60/40) |
|---|---|---|---|---|---|
| **Bull** | 25% | growth re-accelerates, multiple re-rates toward 3yr norm: $5.00 × 50× / FCF $6.34 × 40× | $250 | $254 | **$251** |
| **Base** | 50% | consensus: $4.60 × 38× (between 32× trough and 67× 3yr-avg) / FCF $5.51 × 30× | $175 | $165 | **$171** |
| **Bear** | 25% | growth decelerates to ~15%, multiple compresses to ~22×, FCF margin pressure: $4.20 × 22× / FCF $4.96 × 20× | $92 | $99 | **$95** |

```
PW Fair Value = 0.25×251 + 0.50×171 + 0.25×95 = $172.1
```

Sanity (Rule 4): base $171 sits just below the analyst median ($190); bear $95 is below the 52-wk low ($114.63) and below the low PT ($145) — an honest downside for a high-multiple, GAAP-loss-making name where a SaaS-growth de-rating is the live risk. Bull $251 ≈ the analyst high ($250). The band is reasonable and not anchored on the rosy point (guardrail #2).

### Step 2 — Expected annual return `E`

```
Gap Upside %    = (172.1 ÷ 124.85) − 1                 = +37.8%
Catalyst window = 2 years (Rule 10 — no narrower window; default 2yr)
Annualized gap  = 37.8% ÷ 2                             = +18.9%/yr
Intrinsic growth = +17%/yr   (forward non-GAAP EPS CAGR, decelerated conservatively from the 30%+ trailing rate)
Shareholder yield = −2%/yr   (no dividend; net share count RISING ~2%/yr from SBC → a negative buyback yield, honestly counted)

E = 18.9 + 17.0 + (−2.0) = +33.9%/yr
```

### Step 3 — Map `E` to modifier `M` (hurdle H = 10%)

```
E (33.9%) ≥ H (10%)  →  M = −15 × clamp((33.9 − 10)/15pp, 0, 1) = −15 × clamp(1.59,0,1) = −15 × 1 = −15.0
```

**M = −15.0** (saturated at the floor). Sensitivity check: even on a markedly more conservative scenario set (base $150, bear $85) E ≈ 23% → M ≈ −13; E would have to fall below ~+25%/yr to come off the floor, and below +10% to lose its negative sign. The strong-upside read is robust to reasonable conservatism.

**Catalyst guardrail (#1):** A documented catalyst within 18–24 months exists — quarterly earnings prints (next ~Sep 2026) plus the Zero-Trust / AI-security adoption cycle driving the 30%+ revenue growth. So the upside (negative) side is **not** capped at −5. (Guardrail satisfied; full E calc shown per guardrail #3.)

---

## 6. Final Score & Action

```
Final = Raw 41.31 + Rate additives (+10) + Upside/Downside Modifier (−15.0)
      = 41.31 + 10 − 15.0
      = 36.31  → round to 36.3
```

**FINAL SCORE = 36.3** → **Action band: 30.0–49.9 → BUY — Standard position 3–5%.**

**Band CHANGED:** prior 61.1 (Hold — watch only) → **36.3 (Buy — Standard position).** Two forces moved it: (a) resolving the placeholder/PEG inputs lowered the raw weighted score from 56.1 → 41.3, and (b) the new Upside/Downside Modifier added −15 for the strong expected return — exactly the "great company with strong forward return gets pulled into a buy band" behaviour the modifier was designed to deliver.

> This is precisely the gap the 2026-06-20 modifier closes: under the old engine ZS sat in "Hold, never buy" despite a large, catalyst-backed expected return.

---

## 6a. Order Setup (BUY action → required)

| Item | Value | Basis |
|---|---|---|
| Blended Fair Value | **$172** | PW fair value (Rule 7 triangulation) |
| Margin of Safety | 30% (band 25–30%; top of range, given GAAP losses / high multiple) | Rule 8 |
| **Buy Price (limit)** | **$120.47** | $172 × (1 − 0.30) |
| Primary Sell Target | $172 | blended FV |
| Bull-case Trim Target | $226 | bull FV $251 × 0.90 |
| Stop Loss | $86.74 | buy $120.47 × (1 − 0.28); band 25–30% |
| **R/R at the $120.47 buy** | **1.53:1** | ($172−$120.47)/($120.47−$86.74) — **BELOW the 2:1 minimum** |

🚩 **Order discipline overrides the buy signal at today's levels.** Two problems:
1. **Live price $124.85 is ABOVE the disciplined buy price $120.47** → at minimum this is a *limit order*, not a market buy (Phase 03 / FV-methodology integration: Score 30–49.9 = "approaching buy price → set limit order").
2. **R/R fails the 2:1 minimum** at the standard 25–30% MoS. To clear 2:1 with a 25% stop, entry must be **≈$114.73 (≈33% MoS)**; with a 28% stop, ≈$110.32 (≈36% MoS). Below 2:1 the framework says **do not enter** — wait for a lower entry.

**Actionable conclusion:** ZS scores into the BUY band, but **do not buy at $124.85.** Set a **limit order at ≈$114.73** (33% MoS, ~25% stop at ~$86), which is the level that simultaneously satisfies the 2:1 R/R gate. That limit sits right at the 52-week low ($114.63) — i.e. the framework wants ZS only on a retest of its low, not here. Position sizing is bounded by the 3–5% band (Upgrade 7 hard cap 15% not in play); current weight 0.24% leaves ample room, but **no add is triggered until the limit fills.** Risk-based share count is left for the order ticket once portfolio value is confirmed at execution.

---

## 7. Flags & Caveats

- **EV/EBIT remains a flagged neutral placeholder** (TTM GAAP EBIT negative) — the only residual low-confidence input. Not invented.
- **Phase 01 quality gate still fails on GAAP** (negative net margin/ROIC) — but FCF is strongly positive and growing, gross margin 76.7%, net cash balance sheet. ZS belongs on the `override-log.md` watch (carried from the 2026-06-07/06-11 passes) precisely because the score now says BUY while the GAAP quality gate says FAIL. **Resolve via override-log review before any actual add**, independent of the limit-order mechanics.
- **Forward-PE sub-score (0.0) is benchmark-sensitive** — driven by the 3yr post-bubble avg (67×). A different window changes it; flagged.
- **IBKR price snapshot was permission-denied** this session; price sourced from `yfinance` instead (per the prompt's stated fallback order). All other inputs are `yfinance`-derived.

## 8. Next Review Trigger

- **Next ZS earnings (≈ Sep 2026)** → standard re-score (Rule 9).
- **`override-log.md` quality-gate review** (GAAP Phase-01 fail vs. BUY score) — do this *before* acting on the limit order.
- **Limit-order watch at ≈$114.73** — if filled, log the trade in `decisions/`.
- **Quarterly Rate Environment Gate refresh (Jul 2026)** — affects the +10 rate additive.
- Any >15% unexplained price move (Rule 9) → immediate re-score.

*Session complete. Score 36.3 (was 61.1). Low-confidence flag substantially resolved (EV/EBIT placeholder remains). BUY band, but R/R discipline gates entry to a ≈$114.73 limit — no action at $124.85.*

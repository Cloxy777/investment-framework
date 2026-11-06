# NEW POSITION — SNDK (Sandisk Corporation, NASDAQ) — 2026-11-06

**Task type:** NEW POSITION (4th evaluation; prior: 07-15 Phase 01 FAIL, 08-05 and 08-13 WATCHLIST ONLY on a failed R/R gate) · **Not held**
**Outcome in one line:** Quality Score **86.9** (passes the 80.0 gate) · Valuation Score **0.0** · Composite Score **6.5** → **BUY — Full-position band (6–8%)**. Base-case **R/R 2.50:1 clears the 2:1 minimum for the first time**. Recommendation: **ENTER NOW (framework signal) — about 3 shares / $2,580 / ≈5.6% of the framework account**. **This session placed no order**; the decision is yours.
**Date / 10Y yield / Rate Regime Modifier:** 2026-11-06 · **4.90%** (FRED `DGS10`, latest posted observation 2026-11-04) · **+5** (3.5–5% bracket)
**Why it ran:** Q1 FY2027 results (8-K 2026-10-29, 10-Q 2026-10-30) are the "next review trigger" named in [the watchlist entry](../watchlist/not-in-portfolio/SNDK/SNDK-2026-08-05.md), and the entry carried a ⚠️ STALE SCORE banner from the 2026-10-12 SBC-as-a-cost methodology change.

---

## 1. Live price (Rule 0)

| Item | Value |
|---|---|
| **Live price used** | **$860.00** — IBKR `get_price_snapshot`, contract **760250490** (NASDAQ "SANDISK CORP", the standalone equity — not one of the leveraged/inverse single-stock ETFs that also match the ticker), tick timestamp 2026-11-06 07:55:01 UTC |
| Bid / Ask | $859.66 / $860.73 |
| Change vs prior regular-session close | +$53.57 / +6.64% → prior close **$806.43** |
| 52-week range | $183.00 – $2,354.39 → price is **−63.5% below the 52-week high** |
| vs 08-13 session | $1,548.46 → $860.00 (−44.5%) |

**Caveat on the price.** The tick is dated 07:55 UTC (≈ 02:55 ET), i.e. an overnight-session print, 6.6% above the regular-session close of $806.43. I used the higher $860.00 because it is the latest IBKR price and it is the *less* favourable one for an entry. At $806.43 every result below would look better (larger gap to fair value, higher R/R). Re-check the live price before acting.

**Why the price fell (context only, not an input).** Search results report that SNDK fell **13.5% to $1,150.89 on 2026-10-30**, the day after results that beat the company's own guidance, with media tying it to a **Kioxia** outlook that the AI-driven flash-price surge is fading and to a broad memory-sector sell-off; a Seeking Alpha headline calls it a third consecutive double-digit slide. I did not open those pages, and I found no source explaining the further slide from $1,151 to $860. The framework never acts on price alone, so none of this is a score input.

---

## 2. Data gaps and how each was handled

| # | Gap | Handling |
|---|---|---|
| 1 | `fetch_fundamentals` priced the market cap at the **prior close ($806.43)** and shares of 142,289,365 | Price-dependent inputs (FCF yield, EV/EBIT, forward PE) were **recomputed by hand at $860.00** (§5). Price-independent inputs (margins, ROIC, CAGR, SBC, FCF/NI) are the script's values. |
| 2 | Gross buyback yield printed `UNKNOWN` | Sourced from the filings: repurchases **$4,524M (FY2026) + $5,000M (Q1 FY2027) − $0 (Q1 FY2026) = $9,524M TTM** (XBRL `PaymentsForRepurchaseOfCommonStock`, 10-K/10-Q) ÷ market cap $122,368.9M = **7.783%**. |
| 3 | `cycle_peak` and `value_trap_candidate` printed `UNKNOWN` (yfinance lacks 8 quarters of EPS) | Re-run by hand with filed quarterly diluted EPS (§4). |
| 4 | Only 4 quarters of PE history (listed 21 Feb 2025) | **No-history fallback**: Forward PE sub-score = 50.0 (neutral, flagged), as in all prior SNDK sessions. |
| 5 | The script's `FCF/NI annual` series `[43.5%, 70.7%, 7.3%, 100.5%]` mixes years where FCF and NI were both negative (ratio meaningless) | Used only the economically meaningful readings: **FY2026 100.53%** and **TTM plain 89.41%**. Both are above 70%. |
| 6 | Consensus forward EPS of **$287.26** (yfinance, single source) looks high next to company guidance (Q1 non-GAAP EPS $49.51 + Q2 guide ≈ $56 = ≈ $105 for H1) | Same data-quality flag as the 2026-08-05 and 08-13 sessions. It feeds only the Rate Gate's earnings-yield test (which passes by a very wide margin on any plausible EPS) and the Forward PE line, which is the neutral 50.0 fallback anyway — **no effect on the score**. It is *not* used in fair value. |
| 7 | TrendForce 2Q26 share figure for SanDisk (11.4%) is from a secondary summary | The primary TrendForce release (2026-08-18) gives revenue growth only: SanDisk **+50.7% QoQ to ≈ $8.97B vs. top-five +77% to $68.87B**, "slowest growth in the group", ranked 5th. That alone proves share fell, so the Moat call does not depend on the 11.4% number. |

---

## 3. Fundamentals (verbatim script output) and primary-source reconciliation

`python -m scripts.fetch_fundamentals SNDK --normalised-ni 18267000000 --normalisation-note "..."`:

```
Market Cap            = 114,746,408,960      (script priced at prior close $806.43 — recomputed at $860.00 below)
Enterprise Value      = 109,741,416,448
Shares Outstanding    = 142,289,365
Forward PE            = 2.807
FCF Yield %           = 15.133
EV/EBIT               = 4.933
Net Margin %          = 67.039   (reported; 63.05% after the normalisation below)
Gross Margin %        = 79.952
ROIC % (NOPAT/InvCap) = 123.618  [tax_rate=0.1256, NOPAT=19,452,603,728, InvestedCapital=15,736,000,000]
Revenue 3yr CAGR %    = 49.285
Net Debt/EBITDA       = -0.216  [EBITDA_ttm=21,212,000,256]
FCF/NI TTM % (plain)  = 89.409
(FCF - SBC)/NI TTM %  = 93.584  [NI NORMALISED: Removed after-tax mark-to-market gains on equity securities: FY2026 pre-tax gain 808M (FY2026 10-K, acc 0001628280-26-057406) + Q1 FY2027 pre-tax gain 513M (10-Q acc 0001628280-26-068601) = 1,321M TTM (Q1 FY2026 gain = 0); tax-effected at TTM effective rate 12.56% (2,790/22,212) = 1,155M removed from reported TTM NI 19,422M]
SBC yield %           = 0.235
Gross buyback yield % = UNKNOWN - supply manually; scorers will stop and ask   → supplied manually: 7.783% (gap 2)
FCF/NI annual (oldest first) = [43.5%, 70.7%, 7.3%, 100.5%]
FCF positive 3yr+     = False
5yr PE history        = NO-HISTORY FALLBACK (n=4 usable quarters) — only 4 quarters of reconstructable TTM-EPS PE history available, need 20 (5yr)

SBC block (TTM, advisory — no score effect)
  SBC 270,000,000.0   FCF 17,365,000,000.0   Market cap 114,746,408,960.0
  SBC/FCF = 1.6%
  FCF yield (reported)  = 15.13%
  FCF yield after SBC   = 14.90%
Advisory flags (no score effect)
  cycle_peak             UNKNOWN   EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN   forward PE or trailing EPS growth unavailable
```

**Reconciliation to primary sources (SEC EDGAR).** The script's TTM figures tie to the filings, so I treat them as verified:

| Item | Build | Result |
|---|---|---|
| TTM revenue | FY2026 $20,248M + Q1 FY27 $11,031M − Q1 FY26 $2,308M | **$28,971M** |
| TTM operating income (EBIT) | $12,389M + $8,780M − $176M | **$20,993M** |
| TTM net income (reported) | $11,433M + $8,101M − $112M | **$19,422M** |
| TTM FCF | OCF: $11,671M + $6,363M − $488M = $17,546M; capex: $177M + $54M − $50M = $181M | **$17,365M** (matches script) |
| TTM SBC | $232M (FY26) + $91M − $53M | **$270M** (matches script) |
| Shares outstanding | 10-Q cover: **142,289,365** as of 2026-10-26 (144M at 2026-10-02 balance sheet; the company repurchased 3.2M shares for $5.0B in the quarter) | 142.289M |
| Balance sheet 2026-10-02 | Cash $5,136M; **no debt**; marketable equity securities $2,289M (not netted, framework convention); equity $18,134M | net cash |

**Q1 FY2027 (quarter ended 2026-10-02), 10-Q and 8-K Ex. 99.1:** revenue **$11,031M** (+378% YoY, +23% QoQ); gross margin 85.0%; operating income $8,780M; net income $8,101M (GAAP diluted EPS $52.60) including a **$513M equity-securities gain**; OCF $6,363M, capex $54M → **FCF ≈ $6,309M**. Datacenter revenue $4,802M (+61% QoQ). Contract liabilities (customer prepayments under long-term agreements) $1.5B. **Q2 FY2027 guidance** (context only, not scored): revenue $12.2–12.6B, gross margin 84.4–85.4%. **8-for-1 forward stock split** announced: record date 2026-11-09, shares issued after the close 2026-11-19, post-split trading from **2026-11-20**.

**Normalisation (one-time item).** Reported TTM net income carries mark-to-market gains on equity securities that are not operating profit: $808M (FY2026) + $513M (Q1 FY2027) = $1,321M pre-tax; tax-effected at the TTM effective rate 12.56% ($2,790M ÷ $22,212M) = $1,155M removed → normalised NI **$18,267M**. The adjustment lowers the NI denominator, so it lifts (FCF − SBC)/NI from 88.0% to 93.6%. Sensitivity: unnormalised, FCF Quality would be 80.0 instead of 89.3 and the Quality Score 86.0 instead of 86.9 — **same gate outcome either way**.

---

## 4. Advisory flags (no score effect)

`python -m scripts.scoring.flags_common --eps-now 124.75 --eps-prior -12.02 --forward-pe 2.99 --eps-growth 130`

```
cycle_peak             LOSS_TO_PROFIT_BASE    prior-year EPS <= 0: growth undefined; PEG-ineligible base (valuation-scoring.md)
multiple_ceiling       NONE                   forward PE 3.0, EPS growth 130.0%
value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
```

Inputs: TTM diluted EPS now = 5.15 + 23.03 + 43.97 + 52.60 = **$124.75** (filed quarters Q2 FY26–Q1 FY27); a year earlier (quarters Q2 FY25 0.72, Q3 FY25 −13.33, Q4 FY25 −0.16, Q1 FY26 0.75) = **−$12.02**.

How each was handled:
- **`cycle_peak` — not formally raised, but I treat it as live.** The script cannot compute growth off a loss-making base, which is itself the signature: TTM EPS went from −$12.02 to +$124.75. Earnings are at a commodity-memory peak by any reading, and the market is pricing exactly that fear (forward PE ≈ 3×). This is why the fair value below uses a below-market multiple (10×) on near-peak cash flow and fades FCF 20% a year in the base case.
- **`multiple_ceiling`:** NONE — a 3× forward PE is nowhere near the 30× trigger.
- **`value_trap_candidate` (UNKNOWN → closed by hand):** the flag looks for a cheap multiple *with falling* trailing earnings. Trailing EPS is rising sharply, so the premise is not met. The residual risk is the forward one (earnings roll over), which the bear case models.

---

## 5. Phase 01 — Quality Score (script output, verbatim)

Hard-disqualifier checks:

| Disqualifier | Test | Result |
|---|---|---|
| FCF not positive for 3+ consecutive years | Rolling window per the settled rule ([quality-scoring.md](../framework/quality-scoring.md), clarified 2026-08-05): FY2024 −$475M, FY2025 −$120M, FY2026 +$11,494M; only 2 consecutive negative years, and TTM FCF is +$17,365M | **Does not fire** (input `true`) |
| FCF/NI conversion <70% for 2+ consecutive meaningful years | FY2026 100.53%, TTM 89.41% | **Pass** |
| Net Debt/EBITDA over threshold | −0.216× (net cash) | **Pass** |
| SBC ≥ 100% of FCF | $270M ÷ $17,365M = 1.6% | **Pass** |

`python -m scripts.scoring.quality_score --input <inputs.json> --set 'fcf_ni_annual_pct=[100.53, 89.41]'`:

```
## Quality Score

Profitability (25%)
  NetMargin_Component = clamp((63.05/30)x100) = 100.00
  ROIC_Component = clamp((123.618/30)x100) = 100.00
  Profitability_Score = (100.00 + 100.00) / 2 = 100.00
Margins (15%)
  GrossMargin_Score = clamp((79.952/80)x100) = 99.94
  +10 structural-trend bonus -> clamp(99.94+10, 0, 100) = 100.00
Growth (20%)
  Growth_Score = clamp((49.285/25)x100) = 100.00
  Growth_Score (final, clamped) = 100.00
Balance Sheet (15%)
  BalanceSheet_Score = clamp(100x(1 - -0.216/4)) = 100.00
Moat Signal (15%)
  | market_share_stable_or_growing | False | TrendForce 2Q26 NAND ranking (2026-08-18): SanDisk revenue +50.7% QoQ to ~$8.97B vs top-five +77% QoQ ($68.87B) - slowest growth in the group, fell to 5th place; share therefore fell vs 1Q26 (secondary summary: 13.9% -> 11.4%) |
  | brand_premium                  | False | No third-party citation of a company-specific sustained price premium without volume loss; ASP surge is industry-wide |
  | network_effect                 | False | Hardware/component manufacturer |
  | switching_costs                | True  | Lengthy product qualification cycles (SanDisk 10-K risk factors); new multi-year NBM long-term agreements (contract liabilities $1.5B at 2026-10-02, 10-Q) |
  | scale_cost_advantage           | False | No $/GB cost-per-unit citation vs peers found |
  Moat_Score = (1/5) x 100 = 20.00
FCF Quality (10%)
  Net income normalised: (see §3)
  FCFQuality_Score = clamp(((0.9358 - 0.40)/0.60)x100) = 89.31  [ratio = (FCF - SBC)/NI]

Quality Score = (100.00x0.25) + (100.00x0.15) + (100.00x0.20) + (100.00x0.15) + (20.00x0.15) + (89.31x0.10)
= 86.931 -> rounds to 86.9

# Quality Score = 86.9 — PASSES the 80.0+ gate
```

**What changed vs 08-13 (89.4 → 86.9):** the Moat market-share signal flipped from TRUE to FALSE (SanDisk's NAND share fell in 2Q26 while peers grew faster), costing 3.0 points (Moat 40.0 → 20.0); FCF Quality moved from 100.0 to 89.3 because SBC is now deducted and the TTM ratio is below 100%. TAM-expansion and decelerating-growth modifiers were left off (not credited without a company-specific source; growth sub-score is capped at 100 either way).

---

## 6. Rate Environment Gate and Phase 02 — Valuation Score

**Price-dependent inputs recomputed at the live $860.00 price:**

```
Market cap = $860.00 × 142,289,365 = $122,368.9M
EV         = $122,368.9M − cash $5,136M − debt $0 = $117,232.9M   (marketable equity securities $2,289M NOT netted — conservative)
FCF yield  = TTM FCF $17,365M ÷ $122,368.9M = 14.1907%
SBC yield  = $270M ÷ $122,368.9M            = 0.2206%
EV/EBIT    = $117,232.9M ÷ TTM EBIT $20,993M = 5.5844×
Forward PE = $860.00 ÷ $287.26 = 2.9938×   (see gap 6)
Gross buyback yield = $9,524M ÷ $122,368.9M = 7.783%
```

**Fair value (Rule 7: bull/base/bear; Rule 3: 40% DCF / 60% multiples; re-derived because new audited data exists).** The 08-05 / 08-13 sessions carried a $1,214.25 fair value built on a *forecast* FY2027. One quarter of FY2027 is now actual and a second is guided, so the old bear case (Year-1 FCF $12.0B) is already below what the first half will deliver. The method is unchanged; only the Year-1 anchors, net cash, share count and the risk-free rate are updated.

- **Year-1 (FY2027) FCF anchor.** H1 ≈ Q1 actual $6,309M × 2 = **$12,618M** (assuming Q2 FCF equals Q1; Q2 revenue is guided +12–14% sequentially, so this is conservative). Base H2 = H1 → **$25,000M**. Bull H2 ≈ 1.6× H1's run-rate → **$33,000M**. Bear H2 = half of H1 → **$19,000M**. *These H2 numbers are scenario judgments, not facts — flagged as the most judgment-heavy inputs in this session.*
- **Years 2–5:** base fades −20%/yr, bull −5%/yr, bear follows the 08-05 path ($6,000M → $1,500M → $0 → −$200M). **Years 6–10:** geometric decay toward a mid-cycle floor (bull $13,733M, base $3,200M, bear $1,800M), floors carried from 08-05. WACC bull 11% / base 15% / bear 16% (risk-free 4.90% + beta 2.0 × 5% = 14.9%, rounded up to 15% — same beta judgment as 08-05); terminal growth 2.5%; end-of-year discounting; net cash $5,136M; 142.289M shares.
- **Multiples:** bull 12× and base 10× Year-1 FCF/share; bear 6× the Year 1–3 average — the low-multiple-on-peak-cash-flow convention for cyclicals, unchanged from 08-05.

```
Scenario  Year-1..10 FCF ($M)                                                  PV(FCF)   PV(TV)   Equity   DCF/sh   Multiple/sh  Blended (40/60)
Bull      33000 31350 29782 28293 26879 21620 18465 16572 15437 14755          150,415   62,664   218,216  $1,533.6  $2,783.1     $2,283.28
Base      25000 20000 16000 12800 10240  7424  5734  4721  4112  3747          68,796    7,596    81,527   $573.0    $1,757.0     $1,283.38
Bear      19000  6000  1500     0  -200   600  1080  1368  1541  1644          23,528    2,830    31,494   $221.3    $372.5       $312.02

PW Fair Value = 0.25×2,283.28 + 0.50×1,283.38 + 0.25×312.02 = $1,290.52
```

The PW fair value is +6.3% vs. 08-13's $1,214.25. Terminal value is 9.3% of base-case DCF equity value, nowhere near the 75% Rule 4 warning level. Sanity check against the Street was not repeated this session (no fresh analyst-target source was pulled); the PW figure is deliberately below the bull case and Rule 7 forbids using a single rosy target.

`python -m scripts.scoring.valuation_score --input <inputs.json>`:

```
FCF Yield (40%)
  FCF yield after SBC = 14.1907% - 0.2206% (SBC yield) = 13.9701%
  FCF_Score = clamp(100x(1 - 13.9701/10)) = 0.000
EV/EBIT (40%: PEG's 15% redistributed)
  EV/EBIT_Score = clamp((5.5844 - 12)/23 x 100) = 0.000
Forward PE (20%)
  No 5yr PE history available (no-history fallback) -> FwdPE_Score = 50.0 (neutral, flagged)
PEG: not applicable (not a Fast Grower: EPS history is loss-to-profit, not clean) -> 15% redistributed to EV/EBIT

Rate Environment Gate
  EY = 1/2.9938 x 100 = 33.4024%
  Spread = EY - 10Y (4.9%) = 28.5024pp -> Step 1 = +0 (pass, >=1.5pp)
  10Y = 4.9% -> Step 2 bracket modifier = +5
  Total Rate Modifier = 0 + 5 = +5

Upside/Downside Modifier
  PW Fair Value = 0.25x2283.28 + 0.50x1283.38 + 0.25x312.02 = 1290.5150
  Gap Upside % = (1290.5150/860.0) - 1 = 50.0599%
  Annualized gap = 50.0599% / 2yr = 25.0299%/yr
  E = 25.0299 (annualized gap) + 5.0 (intrinsic growth) + 7.7830 (shareholder yield: 0.0 div + 7.783 buyback) = 37.8129%/yr
  E (37.8129%) >= H (10.0%) -> M = -15 x clamp((37.8129-10.0)/15, 0, 1) = -15.0000
  Upside/Downside Modifier (bounded [-15, +15]) = -15.0000

Raw Weighted Score = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2 = 10.000
Final Score = Raw (10.000) + Rate Modifier (+5) + Upside/Downside Modifier (-15.000) = 0.000 -> rounds to 0.0

# Valuation Score = 0.0
```

Inputs behind the modifier: catalyst window 2 years (Rule 10 default); intrinsic growth +5.00%/yr (carried from 08-05: a structural estimate net of the cyclical fade that is already in the gap term); no dividend; gross-cash buyback yield 7.783% (basis `gross_cash`, as the 2026-10-12 methodology requires).

**Catalyst guardrail — sensitivity.** I treated the guardrail as satisfied: dated catalysts exist inside 18–24 months (the Q2 FY27 print in roughly late January/February 2027 against guided revenue of $12.2–12.6B, and the following two quarterly prints). If a reader judges that no catalyst is "identifiable", the upside side is capped at −5, and the result becomes **Valuation Score 10.0 → Composite 11.5**. The action band (0.0–29.9) and the recommendation are the same either way; only the R/R-independent score label moves.

**Notes on reading a 0.0.** The two cash-flow metrics bottom out at 0 because SNDK's trailing numbers are at a cyclical high; the framework's formulas cannot say "cheap because peak" versus "cheap because mispriced". That judgment lives in the fair value (below-market multiple, 20%/yr fade, bear case at $312) and in the advisory flags (§4), not in the 0.0.

---

## 7. Composite Score

`python -m scripts.scoring.composite_score --set quality_score=86.9 --set valuation_score=0.0`

```
Composite Score = 0.50x(100 - 86.9) + 0.50x0.0 = 6.550 -> rounds to 6.5

# Composite Score = 6.5
```

Phase 03 table: **0.0–29.9 → BUY — Full position (6–8%)**. Path from 08-13 (Composite 32.7): the price fell 44.5% against a fair value that rose 6.3%, turning an expected-loss modifier (+8.85) into the maximum expected-gain modifier (−15), and the cash-flow multiples collapsed.

---

## 8. Order setup

Band choices (all within the 0.0–29.9 ranges): Margin of Safety 20% (top of 15–20%), Max Loss 20% (bottom of 20–25%), risk 1.5% of portfolio, allocation cap 6% (bottom of 6–8%; chosen because the account already holds NVDA 8.47% and AVGO 4.26%, which are correlated AI-semiconductor exposures — SNDK would take the three to ≈ 18% combined). Portfolio value $46,102.05 (framework account NLV, [holdings.md](../portfolio/holdings.md), 2026-11-01 sync).

`python -m scripts.scoring.order_setup --input <inputs.json>`:

```
Band: 0.0-29.9 (Enter now)
Buy Price = Fair Value (1290.52) x (1 - 20%) = 1032.4160
Live price 860.0 vs buy price ceiling 1032.4160 -> enter now (live price at/below buy price ceiling); entry price used = 860.0000
Primary Sell Target = Fair Value = 1290.5200
Bull-Case Trim Target = Bull FV (2283.28) x 0.90 = 2054.9520
Stop Loss = Entry Price (860.0000) x (1 - 20%) = 688.0000
R/R Ratio = (1290.5200 - 860.0000) / (860.0000 - 688.0000) = 430.5200/172.0000 = 2.5030:1
Max $ Risk = 46102.05 x 1.5% = 691.5308 ; Risk Per Share = 172.0000 ; risk-based = 4.0205 sh
Allocation cap = 46102.05 x 6% = 2766.1230 -> 3.2164 shares   [binding: allocation cap]
Position Size = 3.2164 sh = $2,766.12

[✓] Risk/Reward Ratio: 2.50:1 (must be >= 2:1)
```

Whole-share implementation: **3 shares ≈ $2,580 (≈ 5.6% of NLV)**. Sensitivity of the R/R gate: with a 25% stop (top of the allowed range) R/R = 2.0024:1 — a knife-edge pass; with the 20% stop it is a clear pass.

**Practical points before acting (not scored):**
1. **The 8-for-1 split lands 2026-11-20.** 3 shares today become 24 shares at ≈ $107.50. Order prices in the table are pre-split; if you place a GTC order before the split, check how IBKR adjusts it (limit/stop prices ÷ 8, quantity × 8), or place it after 11-20 using post-split prices: entry ≈ $107.50, stop ≈ $86.00, target ≈ $161.31.
2. **A 20% stop is tight for this stock.** SNDK has moved ±13–15% in single days several times this year (and −13.5% on 2026-10-30), so a stop at $688 may trigger on volatility rather than on a thesis break. The framework's stop band is what it is; this is a risk to size mentally, and it is part of why the position is capped at 6% rather than 8%.
3. **Margin.** The 2026-11-01 sync shows a negative USD cash balance in the framework account (a margin debit). A $2,580 buy adds to it; check `/safe-guard` headroom first.

---

## 9. Recommendation

# **ENTER NOW is the framework's signal — Composite 6.5, BUY Full-position band, R/R 2.50:1 — implemented as ~3 shares (≈5.6% of the account) and gated on a fresh live-price check. Not executed by this session.**

Why the framework says yes:
1. **Quality gate passes with room** (86.9; 6.9 points above the 80.0 line, and still above it under every sensitivity run: unnormalised 86.0).
2. **Valuation is as cheap as the formula can show**: a 14.2% FCF yield, 5.6× EV/EBIT, net cash with $5.0B buyback in one quarter, against a Year-1 FCF anchor that is already half-banked ($6.3B of FCF in Q1 alone).
3. **The 2:1 R/R gate that blocked entry on 08-05 and 08-13 now clears (2.50:1)** because the price fell far below the buy-price ceiling ($1,032.42), not because the target was inflated (fair value moved only +6.3%).

What argues for caution (the framework does not score these, you should weigh them):
- **This is a peak-cycle commodity-memory name.** The advisory `cycle_peak` flag could not even compute (loss-to-profit base). The market's forward PE of ≈ 3× is the market saying the earnings will not last, and the Kioxia outlook (flash prices fading) is the first public sign from a peer. If NAND prices roll over, the base case here (FCF fades 20%/yr) is itself an optimistic path and the bear case is $312/share (−64%).
- **Fair value is a judgment-heavy number** (H2 FY27 FCF scenarios, WACC 11/15/16%, a 10× multiple). A fair value 25% lower ($968) would still show a 12.6% gap, but the R/R would drop below 2:1 at the same entry/stop.
- **Market share is slipping** (Moat signal flipped), and SanDisk depends on Kioxia's fabs (Flash Ventures) for substantially all wafers.
- **Price was not explained** beyond 2026-10-30 (§1).

Net: the framework's mechanics say buy and the cap keeps the loss if the stop is hit to ≈ $516 on the $46k account (3 shares × $172). The decision to place the order is yours; no order was placed or prepared in IBKR by this session.

---

## 10. Next review trigger

- **Q2 FY2027 results (≈ late Jan / early Feb 2027)** against the guide: revenue $12.2–12.6B, gross margin 84.4–85.4%. A miss or a cut is a Rule 9 trigger and would fail the fair-value anchor (H1 FCF assumption).
- **Any Kioxia / NAND contract-price datapoint** that confirms or denies the "fading" narrative; the next TrendForce vendor ranking (3Q26) for the share signal.
- **Split effective 2026-11-20** — re-run order prices post-split.
- If entered: Phase 04 monitoring at each quarterly print; a price move toward the $688 stop is not itself a trigger (Rule 0), but the stop is a pre-set risk limit.
- Standard Rule 9 triggers: guidance revision, management change, M&A, macro shift, >15% unexplained move.

---

## 11. Housekeeping

- Watchlist: new entry [SNDK-2026-11-06.md](../watchlist/not-in-portfolio/SNDK/SNDK-2026-11-06.md) (Rule 9 fundamental event + score change); the previous 08-05 file's STALE banner and the STALE.md row are cleared by this rescore under the 2026-10-12 methodology.
- No position was opened, so nothing is logged in `decisions/`. If you place the order, log it there.
- Framework files changed: only [glossary.md](../framework/glossary.md) (new term: Kioxia).

---

## 12. Glossary

| Term | Meaning |
|---|---|
| **Quality Score** | This framework's 0.0–100.0 continuous score grading profitability, margins, growth, balance sheet, moat and FCF quality; 80.0+ needed to proceed to valuation scoring. SNDK: 86.9. |
| **Valuation Score** | 0.0 (cheapest) to 100.0 (most expensive); combines the valuation sub-scores, the Rate Environment Gate and the Upside/Downside Modifier. SNDK: 0.0. |
| **Composite Score** | `0.50 × (100 − Quality) + 0.50 × Valuation`, 0.0 = most attractive; the number used against the action table. SNDK: 6.5. |
| **FCF / FCF Yield** | Free Cash Flow (cash left after running and maintaining the business) and FCF ÷ market cap. SNDK TTM: $17,365M, 14.2%. |
| **EV/EBIT** | Enterprise value (market cap + debt − cash) ÷ operating profit — how expensive the business is versus its operating profit, independent of capital structure. SNDK: 5.6×. |
| **Forward PE** | Price ÷ expected next-twelve-months earnings per share. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared directly with the 10-Year Treasury yield in the Rate Environment Gate. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing earnings yield with the 10Y Treasury yield, plus an additive score adjustment by yield bracket (+5 for 3.5–5%). |
| **Upside/Downside Modifier** | An additive ±15 valuation-score adjustment from expected annual return (gap to probability-weighted fair value + growth + shareholder yield). SNDK: −15 (maximum favourable). |
| **PW (Probability-Weighted) Fair Value** | 25% bull + 50% base + 25% bear blended fair value. SNDK: $1,290.52. |
| **DCF / WACC / Terminal value** | Discounted-cash-flow valuation; the discount rate (cost of financing); and the lump sum for cash flows past the forecast period. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set (20% here). |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss; this framework needs at least 2:1. SNDK: 2.50:1. |
| **SBC (Stock-Based Compensation)** | Pay in shares/options instead of cash; since 2026-10-12 this framework treats it as a real cost. SNDK TTM: $270M (1.6% of FCF). |
| **TTM (Trailing Twelve Months)** | The last four reported quarters added together. |
| **GAAP / Non-GAAP** | Audited accounting-rule figures versus a company's own adjusted figures (the framework scores GAAP). |
| **ROIC** | Return on invested capital. SNDK: 123.6% (cycle-peak reading). |
| **Net Debt/EBITDA** | Leverage ratio; negative means net cash. SNDK: −0.22×. |
| **Hard disqualifier** | A Quality condition that fails a company regardless of its weighted score. |
| **Cycle peak** | The top of a business cycle, when earnings are temporarily inflated (memory prices at a high), so a stock looks cheapest exactly when it is most at risk. |
| **Gross cash buyback yield** | Cash spent repurchasing shares in the last twelve months ÷ market cap (7.8% for SNDK). |
| **NAND** | Flash-memory chips used in SSDs and phones; a commoditized, boom-bust business. |
| **TrendForce** | Independent research firm whose quarterly NAND supplier rankings are the third-party source for the market-share Moat signal. |
| **Kioxia** | Japanese NAND maker, a top-five supplier and SanDisk's partner in the Flash Ventures fabs; its outlook moves SNDK. *(New term this session.)* |
| **Flash Ventures** | The SanDisk–Kioxia joint ventures that make roughly all of SanDisk's wafers in Japan. |
| **New Business Model (SanDisk)** | SanDisk's long-term supply agreements with customers (customer prepayments sit in "contract liabilities"). |
| **Marketable equity securities** | Investments in other companies' shares — on the balance sheet but not netted as cash in this framework. |
| **stock split** | A corporate action multiplying share count (8-for-1 here, effective 2026-11-20) and dividing the price; value and ownership percentages do not change. |
| **8-K / 10-Q** | SEC filings: the event report that carried the earnings release, and the fuller quarterly report. |

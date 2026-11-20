# RESCORE — NVDA (NVIDIA Corporation)

**Task type:** RESCORE (single ticker, mode `--both`) — user-invoked (`/rescore NVDA`), **post-earnings** (Q3 FY2027 print, 2026-11-17) and **Rule 9 management-change trigger** (CEO resignation, 2026-11-11/12)
**Date:** 2026-11-20
**10Y US Treasury Yield:** 5.07% (FRED DGS10, latest print 2026-11-18; 11-19/11-20 not yet posted. Prior in this series: 5.10 on 11-12, 5.15 on 11-13, 5.12 on 11-16, 5.10 on 11-17)
**Rate Regime Modifier:** +10 (>5% bracket)
**Last review on record:** Composite 18.0 (Quality 89.7 / Valuation 25.8), 2026-11-12 — [2026-11-12-rescore-nvda.md](2026-11-12-rescore-nvda.md)
**Current position (material change since last review):** **50 sh** (was 40 on the 11-12 log; avg cost now $180.64 per live IBKR positions, i.e. **+10 sh bought at ≈$171.65 implied by the average-cost change — no session/decision on file**). 50 × $143.20 = **$7,160.00**; framework NLV **$42,316.86** (IBKR `get_account_summary`, 2026-11-20) → **16.92%**. **Above the 15% hard cap (Upgrade 7)**; ~8.9pp over the 8% allocation cap.

## 1. Live Price (Rule 0)

IBKR `get_price_snapshot` (contract 4815747): last **$143.22**, bid/ask $143.21 / $143.28 (earlier pulls this session: $143.09, $143.71). Today −$2.76 / −1.89%. **New 52-week low** (prior 52-wk low $145.71; high $243.37). YTD −23.18%. vs 11-12 ($160.73): **−10.9%**; vs 11-05 ($186.77): **−23.3%**; vs 09-17 ($218.70): −34.5%. The 11-12 −7.48% day is now explained: that was the CEO-resignation announcement (§2, item 1). No single-day move this session exceeds the 15% Rule 9 line; the Rule 9 triggers fired this session are **quarterly earnings** and **management change**, not price.

## 2. What changed since 2026-11-12 (Rule 9 events — verified against primary sources)

1. **CEO resignation — SEC 8-K Item 5.02, filed 2026-11-12 (accession 0001045810-26-000082; event date 2026-11-11).** The Board accepted the resignation of Jen-Hsun (Jensen) Huang as President, CEO and director, effective immediately. EVP/CFO **Colette Kress is interim CEO** (keeps the CFO role); **Harvey C. Jones, age 73, appointed Chair**; a search for a permanent CEO is under way. The 8-K gives no reason. **Secondary reporting (not primary, unverified in detail):** the Board opened an independent-committee inquiry on 2026-11-08 (outside counsel reportedly Wachtell Lipton; investigator reportedly Joon H. Kim) the same day Huang disclosed an extramarital affair to staff; on 2026-11-17 the Board said it does not intend to reinstate him and formed a committee on export-control / national-security compliance; congressional questioning is reported for Dec 1–2. NVIDIA's own 2026-11-17 press release lists "the ongoing investigation by an independent committee of NVIDIA's board" among its forward-looking-risk topics, which confirms an investigation exists. Reports linking Huang to other individuals are explicitly unconfirmed and are **not** used here.
2. **Q3 FY2027 results — SEC 8-K Item 2.02, filed 2026-11-17 (accession 0001045810-26-000088; Ex. 99.1 `q3fy27pr.htm`, CFO commentary `q3fy27cfocommentary.htm`).** Quarter ended 2026-10-25: revenue **$115.8B** (+103% YoY, +20% QoQ; Q3 guide was $108.0B); Data Center **$107.6B** (+110% YoY); GAAP gross margin 74.8%; GAAP operating income $77.5B; GAAP net income $65.3B; GAAP diluted EPS $2.70 (non-GAAP $2.68). **Q4 FY2027 guide: revenue $130.0B ±3% (includes an extra week; assumes no China Data Center compute revenue); GAAP gross margin 71.0–72.0% (≈3pp below Q3).** Shareholder returns $28.1B in the quarter; buyback authorization raised by $150B in September; $227.3B remaining; dividend $0.25/qtr.
3. **Balance-sheet / commitment changes worth knowing (CFO commentary):** supply commitments **$390B** (from $279B, mostly multi-year memory procurement); cloud-service + data-center lease commitments $102B (from $74B); neocloud "additional commitments" contingent on those customers' financing; **guarantees** (SB Energy / OpenAI-hosting campus credit support, neocloud land/power/shell, power-and-systems support — no payments to date); long-term debt **$32.4B** (from $7.5B at FY-end; $25B issued in H1); non-marketable securities $65.5B and marketable equity securities $44.2B (large strategic-stakes book, mark-to-market gains run through net income).
4. **Not yet filed:** the Q3 FY2027 **10-Q** (SEC feed shows no 10-Q after the 2026-08-26 one). All TTM figures below come from the 8-K press-release statements plus the FY2026 10-K XBRL; the 10-Q could restate or add detail.

## 3. Data gaps / sourcing notes

1. **yfinance (`fetch_fundamentals`) ran, but its output is only partly updated:** EBITDA ($243,280M) and EV/EBIT match my independent TTM derivation, but its net margin (63.663%), FCF ($127,006M-based yield), FCF/NI, SBC and buyback figures are still the *pre-Q3* values. **I did not use those stale fields**; every statement-based input was re-derived from the SEC 8-K and FY2026 10-K XBRL (§4). Its market cap implies a stale ≈$146 price; all price-linked figures were recomputed at the live $143.22. Its fresh **5-yr PE avg 52.061×** (range 17.993–122.129, n=20) is used.
2. **TTM derivation (SEC data, $M):** TTM = FY2026 (10-K, FYE 2026-01-25) + 9M FY2027 (8-K) − 9M FY2026 (8-K). Revenue 215,938 + 293,681 − 147,811 = **361,808**; gross profit 153,463 + 219,976 − 102,370 = **271,069**; operating income 130,387 + 194,791 − 86,088 = **239,090**; net income 120,067 + 183,297 − 77,107 = **226,257**; operating cash flow 102,718 + 122,675 − 66,530 = **158,863**; capex (PP&E + intangibles) 6,042 + 8,856 − 4,758 = **10,140** → **FCF 148,723**; D&A 2,843 + 3,378 − 2,031 = 4,190 → **EBITDA 243,280** (✓ equals yfinance's EBITDA); SBC 6,386 + 6,042 − 4,753 = **7,675**; gross cash buybacks 40,086 + 61,166 − 36,271 = **64,981**; diluted EPS TTM 4.90 + 7.55 − 3.14 = **$9.31** (✓ finviz EPS ttm 9.31); EPS a year earlier 2.94 + 3.14 − 2.04 = **$4.04**.
3. **Net income carries equity-security gains (advisory, not normalised):** TTM gains from equity securities ≈ 8,918 (FY26, XBRL `GainLossOnInvestments`) + 25,474 − 3,426 = **≈$30,966M pre-tax**. Prior NVDA sessions used reported (unnormalised) NI; kept for continuity. Sensitivity in §8.
4. **Net debt:** long-term debt 32,371 − (cash 29,089 + marketable debt securities 24,423) = **−$21,141M** (net cash; marketable equity securities $44,219M excluded, same convention as prior sessions: net cash was $23,220M at the prior reuse). Net debt/EBITDA = −21,141 ÷ 243,280 = **−0.0869×**.
5. **ROIC re-derived (prior 63.21% not reproducible from the log):** NOPAT = EBIT 239,090 × (1 − 16.84% tax, 9M FY27 effective: 37,130 ÷ 220,427) = 198,816; invested capital = equity 266,666 + debt 32,371 − cash and marketable debt securities 53,512 = 245,525 → **80.98%**. Any definition ≥30% gives the same 100.0 sub-score (prior 63.21%, yfinance 116.6%).
6. **Share count:** Q3 FY2027 basic weighted-average **24,106M** (10-Q cover count not yet filed); diluted 24,186M. Prior sessions used 24,100M.
7. **Forward EPS $16.59 = finviz "EPS next Y"** (growth +71.52%; stockanalysis shows "EPS Next Year 16"); finviz "EPS this Y" +102.83%. Not independently re-verified beyond that two-source check.
8. **GAP — MarketBeat consensus price target unobtainable** (HTTP 403 from `marketbeat.com`; a search returned no dated figure). Prior sessions' multiples anchor was the mean of stockanalysis and MarketBeat. **Substituted:** mean of stockanalysis **$246** (stated average target) and finviz **$242.79** = **$244.395**. Reference only: TipRanks $229.33 (44 analysts, 2026-11-18, per a secondary article); a Nasdaq/MarketBeat-attributed article quotes ≈$262 (date unclear). The consensus fell ≈24% from the 11-05 level ($322.995) as the price fell ≈23%.
9. **Facts I could not verify:** a secondary article describes the 11-17 call as Kress's first as interim CEO (consistent with the 8-K); fiscal-2028 revenue-growth "≈75%, up from 70%" comes from secondary reporting of the call, **not** the 8-K — not used in any score.
10. **Portfolio value for sizing is live:** NLV $42,316.86 (IBKR `get_account_summary`, 2026-11-20).

## 4. Inputs

| Item | Value | Source / derivation |
|---|---|---|
| Live price | **$143.22** | IBKR (§1) |
| Market cap | 24,106M × $143.22 = **$3,452,461M** | Q3 basic wtd-avg shares |
| Net debt / EV | −$21,141M / **$3,431,320M** | §3.4 |
| TTM revenue / GP / EBIT / NI | $361,808M / $271,069M / $239,090M / $226,257M | §3.2 |
| TTM OCF / CapEx / **FCF** | $158,863M / $10,140M / **$148,723M** | §3.2 |
| TTM EBITDA | $243,280M | §3.2 |
| TTM SBC / gross buybacks | $7,675M / $64,981M | §3.2 |
| Net margin / gross margin | **62.54%** / **74.92%** | NI ÷ revenue; GP ÷ revenue |
| FCF/NI plain; (FCF−SBC)/NI | 65.73%; **62.34%** | (148,723 ÷ 226,257); (148,723 − 7,675) ÷ 226,257 |
| ROIC | 80.98% | §3.5 |
| Revenue 3-yr CAGR | 100.05% | FY23→FY26 annual (yfinance, unchanged; ≥25 caps the sub-score) |
| Net debt/EBITDA | −0.0869× | §3.4 |
| FCF yield / SBC yield | 4.3077% / 0.2223% | ÷ market cap |
| EV/EBIT | 3,431,320 ÷ 239,090 = **14.352×** | |
| Dividend yield / gross buyback yield | 0.6982% ($1.00 ÷ price) / 1.8822% | |
| Forward EPS / **Forward PE** | $16.59 / $143.22 ÷ $16.59 = **8.633×** | |
| PEG | 8.633 ÷ 71.52 = **0.1207** | EPS next-Y growth 71.52% |
| 5-yr PE avg | 52.061× (`pe_mode: avg`) | yfinance |
| 10Y | 5.07% | FRED |

Fast Grower: yes (EPS growth >15% for 3+ years on a clean base; no `--normalised-ni`).

yfinance output (verbatim, `python -m scripts.fetch_fundamentals NVDA`; statement-based fields stale, see §3.1):

```
Market Cap            = 3,524,978,802,688
Enterprise Value      = 3,459,410,821,120
Shares Outstanding    = 24,147,000,000
Forward PE            = 8.791
FCF Yield %           = 3.603
EV/EBIT               = 15.027
Net Margin %          = 63.663
Gross Margin %        = 74.675
ROIC % (NOPAT/InvCap) = 116.594  [tax_rate=0.1605, NOPAT=193,267,706,460, InvestedCapital=165,761,000,000]
Revenue 3yr CAGR %    = 100.045
Net Debt/EBITDA       = 0.002  [EBITDA_ttm=243,280,003,072]
FCF/NI TTM % (plain)  = 65.848
(FCF - SBC)/NI TTM %  = 62.093  [reported NI]
SBC yield %           = 0.205
Gross buyback yield % = 1.569
FCF/NI annual (oldest first) = [87.2%, 90.8%, 83.5%, 80.5%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 52.061 / 17.993 / 122.129  (n=20 quarters)

SBC block (TTM, advisory - no score effect)
  SBC 7,241,000,000.0   FCF 127,006,000,000.0   Market cap 3,524,978,802,688.0
  SBC/FCF = 5.7%
  FCF yield (reported)  = 3.60%
  FCF yield after SBC   = 3.40%
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
```

## 5. Quality Score (scripted)

Hard disqualifiers: annual FCF/NI FY25 83.5% / FY26 80.5% ✅; net debt/EBITDA −0.087× ✅; FCF-positive ✅; SBC/FCF 5.2% ✅ (7,675 ÷ 148,723). TTM FCF/NI 65.7% plain (62.3% after SBC) remains the standing watch item (disqualifier tests completed fiscal years only; next test at FY2027 year-end ≈ Feb 2027). `gross_margin_structural_trend` = false, `scale_cost_advantage` = false, `growth_decelerating_evidence` = false (same strict readings as prior sessions — Q4 guide implies ≈+91% YoY vs +103% in Q3, and QoQ growth slows 20%→12%, but nothing documents a *structural* deceleration, which is what the −10 requires).

## Quality Score

**Profitability (25%)**
```
NetMargin_Component = clamp((62.54/30)x100) = 100.00
ROIC_Component = clamp((80.98/30)x100) = 100.00
Profitability_Score = (100.00 + 100.00) / 2 = 100.00
```
**Margins (15%)**
```
GrossMargin_Score = clamp((74.92/80)x100) = 93.65
```
**Growth (20%)**
```
Growth_Score = clamp((100.05/25)x100) = 100.00
+10 TAM/pricing-power evidence: NVIDIA 8-K Item 2.02 / Ex.99.1 (SEC acc. 0001045810-26-000088, 2026-11-17): Q3 FY2027 revenue $115.8B +103% YoY, Data Center $107.6B +110% YoY; Q4 FY2027 revenue guide $130.0B +/-3% (excludes any China Data Center compute); supply commitments up to $390B from $279B (CFO commentary).
Growth_Score (final, clamped) = 100.00
```
**Balance Sheet (15%)**
```
BalanceSheet_Score = clamp(100x(1 - -0.0869/4)) = 100.00
```
**Moat Signal (15%)**
```
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Data Center 93% of Q3 FY2027 revenue ($107.6B of $115.8B, +110% YoY); Vera Rubin NVL72 shipped (8-K 2026-11-17) |
| brand_premium | True | Gross margin 74.8% GAAP in Q3 FY2027 (8-K 2026-11-17); premium ASPs vs AMD/ASIC per 2026-07-05 session, unchanged |
| network_effect | True | CUDA ecosystem 4M+ developers, 40,000+ orgs (2026-07-05 session), unchanged |
| switching_costs | True | CUDA-embedded production code (2026-07-05 session), unchanged |
| scale_cost_advantage | False | No cost-per-unit citation vs a named smaller competitor - same strict reading as every prior session |
Moat_Score = (4/5) x 100 = 80.00
```
**FCF Quality (10%)**
```
FCFQuality_Score = clamp(((0.6234 - 0.40)/0.60)x100) = 37.23  [ratio = (FCF - SBC)/NI]
```
**Quality Score — Final**
```
Quality Score = (100.00x0.25) + (93.65x0.15) + (100.00x0.20) + (100.00x0.15) + (80.00x0.15) + (37.23x0.10)
= 89.771 -> rounds to 89.8
```

# Quality Score = 89.8 — PASSES the 80.0+ gate

*Governance is not a scored input in this methodology — the CEO departure and the board investigation are carried as a flagged, unscored risk in §9, not by editing a moat signal or any other input.*

## 6. Valuation Score (scripted)

Fair values: **base** = forward EPS $16.59 × 21× = **$348.39**; **bull** $432.00 ($18 × 24×) and **bear** $176.00 ($11 × 16×) **carried unchanged** from 09-17/11-05/11-12; catalyst = FY2028 Vera Rubin ramp and resolution of the CEO search / board investigation, 2-year window; intrinsic growth 10%; `pe_mode: avg` (52.061×).

**Disclosed limitation:** the live price ($143.22) is now **below the bear value ($176)**, meaning the market is pricing something worse than the framework's earnings-reversion bear case (governance discount, AI-capex-digestion, credit/counterparty exposure from the commitments and guarantees in §2.3). I did not invent a new bear case. The score is insensitive to this: the Upside/Downside Modifier sits at its −15.0 floor for any bear value (even $0 gives E ≈ 65%/yr ≥ the 25%/yr needed to floor it), so only the blended fair value in §8 (and thus the *order setup* prices) moves.

## Valuation Score

**FCF Yield (40%)**
```
FCF yield after SBC = 4.3077% - 0.2223% (SBC yield) = 4.0854%
FCF_Score = clamp(100x(1 - 4.0854/10)) = 59.146
```
**EV/EBIT**
```
EV/EBIT_Score = clamp((14.352 - 12)/23 x 100) = 10.226
```
**Forward PE**
```
Deviation% = (8.6329 - 52.061)/52.061 x 100 = -83.418%
FwdPE_Score = clamp(50 + -83.418x2.5) = 0.000 (fallback formula; Historical PE Modifier already folded in)
```
**PEG**
```
PEG_Score = clamp((0.1207 - 0.5)/2.0 x 100) = 0.000
```
**Rate Environment Gate**
```
EY = 1/8.6329 x 100 = 11.5836%
Spread = EY - 10Y (5.07%) = 6.5136pp -> Step 1 = +0 (pass, >=1.5pp)
10Y = 5.07% -> Step 2 bracket modifier = +10
Total Rate Modifier = 0 + 10 = +10
```
**Upside/Downside Modifier**
```
PW Fair Value = 0.25x432.0 + 0.50x348.39 + 0.25x176.0 = 326.1950
Gap Upside % = (326.1950/143.22) - 1 = 127.7580%
Annualized gap = 127.7580% / 2.0yr = 63.8790%/yr
E = 63.8790 (annualized gap) + 10.0 (intrinsic growth) + 2.5804 (shareholder yield: 0.6982 div + 1.8822 buyback) = 76.4594%/yr
E (76.4594%) >= H (10.0%) -> M = -15 x clamp((76.4594-10.0)/15, 0, 1) = -15.0000
Upside/Downside Modifier (bounded [-15, +15]) = -15.0000
```
**Raw Weighted Score**
```
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.25 + FwdPE_Score x 0.2 + PEG_Score x 0.15
= 26.215
```
**Final Valuation Score**
```
Final Score = Raw (26.215) + Rate Modifier (+10) + Upside/Downside Modifier (-15.000)
= 21.215 -> rounds to 21.2
```

# Valuation Score = 21.2

### 6b. Advisory flags (no score effect)

```
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             CYCLE_PEAK_CANDIDATE   EPS TTM +130% > 100%† — state why the multiple is compared with a normalised base
  multiple_ceiling       NONE                   forward PE 8.6, EPS growth 71.5%
  value_trap_candidate   NONE                   forward PE 8.6, EPS TTM growth +130.4%
```
- **`CYCLE_PEAK_CANDIDATE` (raised again):** TTM GAAP diluted EPS $9.31 vs $4.04 a year earlier (+130.4%). Handling unchanged from 11-05/11-12: the FwdPE and PEG sub-scores floor at 0.0 against any plausible normalised base (5-yr *low* PE is now 18.0×; even a 50% EPS haircut gives ≈17×, still under the 52× average); the weight-carrying sub-scores (FCF yield, EV/EBIT) use realised cash flow and operating profit; the bear case ($11 × 16×) is the earnings-reversion scenario. **New this session:** reported NI includes ≈$31B pre-tax of equity-security gains (§3.3), and Q4 gross margin is guided ≈3pp lower — both argue the earnings base is not purely structural. Stated, not scored.
- `MULTIPLE_CEILING`: NONE. `VALUE_TRAP_CANDIDATE`: NONE. The two `UNKNOWN`s in the yfinance block were resolved by supplying the SEC EPS figures (§3.2).

## 7. Rate Environment Gate

EY 11.58% vs 10Y 5.07% → spread +6.51pp ≥ +1.5 → pass (+0). Step 2: **the 10Y has crossed above 5% (5.07%, +0.07pp)** → bracket modifier **+10** (was +5 at 4.88% on 11-12). This lifts Valuation by +5.0 versus the 11-12 bracket and is the single largest *scoring* difference between this run and the last (offset by cheaper EV/EBIT and FCF yield).

## 8. Composite Score

## Composite Score

```
Composite Score = 0.50x(100 - 89.8) + 0.50x21.2 = 15.700 -> rounds to 15.7
```

# Composite Score = 15.7
(Quality Score 89.8, Valuation Score 21.2)

| | 11-05 | 11-12 | **11-20** | Driver |
|---|---|---|---|---|
| Quality | 89.7 | 89.7 | **89.8** | Q3 TTM refresh: gross margin 74.68→74.92 (93.35→93.65), FCF Quality 36.82→37.23; net debt/EBITDA −0.115→−0.087 (still 100.0) |
| Valuation | 30.9 | 25.8 | **21.2** | Price −10.9% and TTM FCF/EBIT up sharply: EV/EBIT 19.5×→14.4× (32.6→10.2), FCF yield 3.28%→4.31% (FCF_Score 69.1→59.1); Rate modifier +5→+10 (10Y crossed 5%); U/D modifier stays at the −15.0 floor |
| Composite | 20.6 | 18.0 | **15.7** | Price- and earnings-driven; deeper in the 0.0–29.9 band |

**Sensitivities (not adopted):**
- *Normalise NI for ≈$31B pre-tax equity gains* (after-tax ≈$25.8B → NI ≈$200.5B): (FCF−SBC)/NI = 70.3% → FCF Quality ≈50.6 → Quality ≈91.1, Composite ≈15.0. Same band, same action.
- *Bear case stressed to $11 × 12× = $132:* PW FV $315.2, Valuation unchanged at 21.2 (modifier floored), blended FV ≈$271.
- *10Y back below 5%:* Rate modifier +5 → Valuation 16.2, Composite 13.2 — same band, same action.

## 9. Action recommendation & order setup

Fair value: PW FV **$326.195**; multiples anchor **$244.395** (mean of stockanalysis $246 and finviz $242.79 — MarketBeat unavailable, §3.8); blended FV = 0.40 × 326.195 + 0.60 × 244.395 = **$277.12**. MoS 17.5%, stop 22.5%, risk 1.5%, cap 8% (band-midpoint convention for 0.0–29.9).

## Order Setup

```
Band: 0.0-29.9 (Enter now)
Buy Price = Fair Value (277.12) x (1 - 17.5%) = 228.6240
Live price 143.22 vs buy price ceiling 228.6240 -> enter now (live price at/below buy price ceiling); entry price used = 143.2200
Primary Sell Target = Fair Value = 277.1200
Bull-Case Trim Target = Bull FV (432.0) x 0.90 = 388.8000
Stop Loss = Entry Price (143.2200) x (1 - 22.5%) = 110.9955
R/R Ratio = (Sell Target 277.1200 - Entry 143.2200) / (Entry 143.2200 - Stop 110.9955) = 133.9000/32.2245 = 4.1552:1
Max $ Risk = Portfolio Value (42316.86) x 1.5% = 634.7529
Risk Per Share = Entry (143.2200) - Stop (110.9955) = 32.2245
Shares by risk-based sizing = 634.7529 / 32.2245 = 19.6978
Allocation cap = Portfolio Value (42316.86) x 8.0% = 3385.3488 -> 23.6374 shares
Position Size (shares) = min(risk-based, cap) = 19.6978  [binding: risk-based sizing]
Position Size ($) = 19.6978 x 143.2200 = 2821.1240
Current shares held = 50; gap vs. target = -30.3022
```

### Order Setup Checklist
```
[✓] Risk/Reward Ratio:      4.16:1  (must be >= 2:1)
[ ] BUY PRICE (ceiling):     228.62
[ ] Entry Price used:        143.22  (enter now (live price at/below buy price ceiling))
[ ] PRIMARY SELL TARGET:     277.12
[ ] BULL-CASE TRIM TARGET:   388.80
[ ] STOP LOSS:               111.00
[ ] Max $ Risk:               634.75
[ ] POSITION SIZE (shares):  19.6978  (binding: risk-based sizing)
[ ] POSITION SIZE ($):       2821.12
[ ] Current shares held:     50
```

### Interpretation

- **Nominal action by score: BUY — full position (6–8%).** Composite 15.7 is in the 0.0–29.9 band, R/R 4.16:1 passes the 2:1 gate. **Practical valuation action: no add** — 50 sh is ≈2.5× the 19.70-sh risk-based target.
- **The one binding constraint is the 15% hard cap (Upgrade 7), and it is now breached.** 50 × $143.20 ÷ $42,316.86 = **16.92%**. The hard cap says never exceed 15% "under any circumstances", so this is a documented rule trigger (not an action on price alone). Reaching ≤15% needs **at least 6 shares sold (≈$860)**: 44 sh ≈ 14.9%, 45 sh ≈ 15.2% (holding the rest of the account flat; the weight moves with NVDA's price and the account's NLV). The framework's sizing target of ≈19.7 sh would mean selling ≈30 sh, but nothing in the framework *requires* going below the 15% line — that further trim is a judgment call, and it would be selling a 15.7-composite name at its 52-week low.
- **Decision for the human (this session placed/modified no order):** (a) trim ≥6 sh to restore compliance, or (b) keep 50 sh and **record a deliberate override** in [override-log.md](../portfolio/override-log.md) with the reason. Either way the 11-12 → 11-20 add (≈10 sh at ≈$171.65) is still **undocumented** and the 11-05 and 11-12 rescores both said *no add*. The standing SELL 10 @ $200.50 order is no longer in the live order book.
- **A short NVDA put is inconsistent with this log.** Assignment would add 100 sh to a position already over the hard cap; no strike satisfies Upgrade 7 (see the in-conversation margin/pricing analysis of 2026-11-12 and 2026-11-20).
- **Unscored governance risk (flag, not a score input):** (i) CEO of 33 years resigned; interim CEO is the sitting CFO, who also owns the financial reporting; new chair is a 73-year-old long-tenured director; (ii) an independent-committee investigation is ongoing with no published conclusion; (iii) reported Dec 1–2 congressional questioning and a new Board committee on export controls; (iv) $390B supply commitments, $102B cloud/lease commitments, new guarantees and +$25B of debt raise counterparty and capex-digestion exposure. None of these changes a framework input today, but together they are why the live price is below the bear case.
- **Thesis-invalidation triggers (carried and extended):** AI-capex digestion (Q4 print vs the $130.0B guide ±3%); gross margin below the 71–72% guide, or >3pp *structural* fall; FCF/NI conversion (65.7% plain / 62.3% after SBC TTM; re-test at FY2027 year-end ≈ Feb 2027); CUDA moat erosion; a filed guidance cut; **new:** an adverse conclusion from the board investigation, a permanent-CEO appointment that signals strategy change, a Rule-9-grade export-control/China development, and any call on the guarantees.

All final decision authority rests with the human investor.

## 10. Next review trigger

- **NVDA Q3 FY2027 10-Q** (not yet filed as of this log) — re-derive any TTM input that moves; due within days.
- **Permanent CEO named / board-investigation conclusion / Dec 1–2 congressional questioning** — each is a Rule 9 management-change-type event; rescore on the filing or credible report.
- **Hard-cap line:** 15% ≈ 44 sh at the current price and NLV — resolve before the next `/rebalance` (trim or log an override).
- **Q4 FY2027 earnings (≈ late Feb 2027)** — FY2027 year-end FCF/NI disqualifier test; standard post-earnings rescore.
- Rate gate: 10Y 5.07% sits 0.07pp above the 5% bracket line; back below 5% removes 5 points from the Rate modifier.

---

## Glossary

**10-Q (Quarterly Report)**: The quarterly financial-disclosure report a US public company files with the SEC between annual 10-Ks, containing unaudited (reviewed) financial statements for the most recent fiscal quarter — used in this framework to reconstruct trailing-twelve-month (TTM) figures between annual reports, as in the 2026-07-06 AAPL session.
**8-K**: The "current report" a US public company must file with the SEC within days of a material event — most commonly used to furnish (via an attached exhibit, typically "Exhibit 99.1") a quarterly earnings press release ahead of the fuller, audited 10-Q/10-K that follows weeks later. Item 5.02 of an 8-K reports officer/director changes (used here for the CEO resignation). *(New term.)*
**Composite Score**: This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50 — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only for companies that have already cleared the 80.0+ Quality Score gate. Used against the Phase 03/05 action tables instead of the raw valuation score. See [valuation-scoring.md](valuation-scoring.md).
**Quality Score**: This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. See [quality-scoring.md](quality-scoring.md).
**Valuation score**: This framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive) combining the Phase 02 valuation sub-scores, the Rate Environment Gate, and the Upside/Downside Modifier into a single number that maps to an action band (Very Cheap/Cheap/Fair Value/Expensive) — see [valuation-scoring.md](valuation-scoring.md).
**FCF**: Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
**SBC (Stock-Based Compensation)**: Employee pay in the form of company shares or stock options rather than cash. A non-cash expense added back in cash-flow statements (inflating FCF relative to GAAP net income), but a real economic cost to existing shareholders through ongoing dilution — worth tracking alongside FCF/NI conversion and share-count trend, not just the headline FCF figure. Since the 2026-10-12 methodology it is treated as a cost in both the FCF yield (Valuation) and FCF Quality (Quality).
**EV/EBIT, EV/EBITDA**: Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.
**Forward PE**: Price ÷ next twelve months' *expected* earnings per share (vs. Trailing PE, which uses the last twelve months' actual earnings).
**PEG ratio**: PE ratio ÷ earnings growth rate — a PE adjusted for growth, used to judge whether a fast grower's multiple is justified by its growth rate.
**Fast Grower**: Peter Lynch's term for a company growing earnings per share (EPS) faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score.
**Rate Regime Modifier**: An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in.
**Treasury yield (10Y)**: The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate.
**Upside/Downside Modifier (Expected-Return Modifier)**: An additive ±15 adjustment to the valuation score based on expected annual return (the gap to PW Fair Value, annualized over the catalyst window, plus intrinsic growth and shareholder yield) — folds the forward-looking dimension into the score so strong expected upside pulls a name toward "buy" and a thin/negative expected return pushes it toward "trim/sell."
**PW (Probability-Weighted) Fair Value**: This framework's blended fair value estimate — 25% bull case + 50% base case + 25% bear case (Rule 7) — used as the single fair-value input to both the order setup and the Upside/Downside Modifier.
**FV (Fair Value)**: The analyst's estimate of what a company is intrinsically worth, independent of its current market price.
**MoS (Margin of Safety)**: How far below fair value the buy price is set, as a cushion against being wrong — e.g. a 25% MoS means buying at 75% of estimated fair value.
**R/R (Risk/Reward ratio)**: (Expected gain) ÷ (Expected loss) on a trade — this framework requires at least 2:1 before entering.
**Stop loss**: A pre-set price below the entry at which a position is exited to cap the loss on a trade; this framework sets it 20–35% below entry depending on the Composite Score band (fair-value-methodology.md Step 4), and the position size is derived from it so a stop-out costs only 1–2% of the portfolio.
**TTM (Trailing Twelve Months)**: The most recent 12 months of reported financial results (the last four quarters added together), as opposed to a single fiscal year or a forward-looking estimate. *(New term.)*
**ROIC**: Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
**Net Debt/EBITDA**: Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
**Cycle peak**: The top of a business cycle, when earnings are temporarily inflated (e.g. memory-chip prices at a high). A stock then looks cheap on trailing earnings exactly when it is most expensive on normal earnings. This framework flags it when trailing EPS grew more than 100% in a year.
**Advisory flag**: A warning printed during analysis (e.g. `CYCLE_PEAK_CANDIDATE`, `MULTIPLE_CEILING`, `VALUE_TRAP_CANDIDATE`, the SBC block) that changes **no** score or action by itself. The analyst must say in the session log how it was handled; `UNKNOWN` means missing data, not a pass. See valuation-scoring.md, "Advisory Flags".
**NLV (Net Liquidation Value)**: A broker's headline value for an account: all positions at current market price, plus cash, minus any liabilities — the broker's own summary number, distinct from manually summing position values and cash yourself (the two can differ slightly due to settlement timing).
**Rule 9**: This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
**Position cap (15% hard cap / 8% allocation cap)**: Two separate ceilings on how much of the framework account one stock may be. The **15% hard cap** (Hybrid Upgrade 7) is never to be exceeded under any circumstances. The **allocation cap** is the tighter, score-band-specific ceiling in the order-setup cap table (e.g. 8% for a 0.0–29.9 Composite) that sizes a *new* purchase; a position can sit above the allocation cap yet below the hard cap, which is a flag for review, not a forced sale. *(New term.)*
**Interim CEO / key-person risk**: An interim CEO is a temporary chief executive (here the sitting CFO) while the Board searches for a permanent one. Key-person risk is the chance that losing one individual (here the founder-CEO) damages a company's strategy, relationships or reputation — a governance risk this framework flags but does not currently score. *(New term.)*

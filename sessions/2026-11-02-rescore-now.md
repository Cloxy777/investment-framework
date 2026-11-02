# RESCORE — NOW (ServiceNow, Inc.) — 2026-11-02

**Task type:** RESCORE (`--both`). **Why NOW:** user asked for a rescore of "fallen or non-growing" holdings; NOW is −43% from its 52-week high, was last reviewed 2026-08-09, and reported Q3 FY2026 on 2026-10-28 (Rule 9 earnings trigger; stock −26.9% next day). Sister session: [NFLX](2026-11-02-rescore-nflx.md).
**10Y Treasury:** 4.929% (Yahoo `^TNX` close 2026-10-30) → Step 2 = +5. **Last review:** Valuation 75.9 · Quality 73.2 · Composite 51.4 (ref), TRIM 25–30% — [2026-08-09](2026-08-09-rescore-now.md).
**Position:** 9 shares (IBKR, avg cost $87.61), 2.07% of NLV.

## 1. Live price (Rule 0)
$106.35 — IBKR `get_price_snapshot` (contract 109911821), 2026-11-02 (bid 106.13 / ask 106.48). Yahoo `currentPrice` showed $105.12 (prior close $109.67); IBKR used. 52-week range $81.24–$184.43. Analyst mean PT $154.69 (Yahoo; bull-case sanity only, probably pre-print stale).

## 2. Rule 9 trigger — Q3 FY2026 (8-K EX-99.1 filed 2026-10-28; 10-Q period 2026-09-30; read from SEC filings via subagent)
- Revenue $4,106M (+20.5%, +20% cc) — slowest growth in 5 quarters; subscription $3,988M (+21%). cRPO $13.65B (+20.5%); RPO $29.7B (+22%).
- **Q4 cRPO growth guided to 18.5%** (mgmt: strong early renewals pulled deals from Q4). FY26 subscription guide $15,780–15,790M. FY26 FCF margin target raised to 36%.
- GAAP op income $385M (9.5% margin vs 17%); GAAP NI $277M (vs $502M); GAAP EPS $0.27; non-GAAP EPS $1.00 vs ~$1.02 consensus (first adjusted miss in 6 quarters; secondary sources).
- OCF $839M, capex $91M. SBC $630M. Buybacks $0 in Q3.
- AI ACV target raised to $1.7B (from $1B at start of year).
- Severance $87M, deal costs $35M, intangible amortisation $198M (non-GAAP exclusions; not removed from GAAP EBIT here).
- Balance sheet 2026-09-30: cash $2,393M + current securities $2,214M = $4,607M (+$2,354M LT securities, excluded per prior-session convention); debt $2,086M + $5,438M = $7,524M; equity $13,096M.

## 3. Data gaps / flags (how handled)
1. **Net debt basis:** `fetch_fundamentals` printed Net Debt/EBITDA −0.409 (vendor basis incl. LT investments). Used the 10-Q cash+current-securities convention (same as 2026-08-09): net debt $2,917M ÷ EBITDA $3,235M = **0.902×**. Counting LT securities would give ≈0.17× and add ~+3 pts to Balance Sheet score — does not change the gate result.
2. **ROIC:** debt+equity convention: NOPAT $1,557.9M (script) ÷ ($7,524M + $13,096M) = **7.56%** (script's vendor invested capital $14,455M would give 10.8%). Below the ~9% WACC from 2026-08-09 — carried-forward yellow flag.
3. **Moat checklist carried forward from 2026-08-09, NOT re-verified** (still an open item). 3/5 TRUE.
4. **Net income not normalised:** 9M includes +$367M strategic-investment gains and a $51M valuation-allowance release (small vs TTM NI; not adjusted). Gate fails by a wide margin regardless.
5. **Forward EPS $4.80** (Yahoo NTM consensus) may not yet reflect post-print revisions.
6. **Advisory flags:** `cycle_peak` UNKNOWN (script lacks EPS history) — not applicable on inspection (GAAP NI fell ~45% YoY); `value_trap_candidate` UNKNOWN — fwd PE 22.1 > 15 so not raised; `multiple_ceiling` NONE (fwd PE 22.1 < 30). SBC/FCF 48.9% — above the 30% watch line, below the 100% disqualifier.
7. Growth deceleration (−10) not credited: the cRPO guide 20.5% → 18.5% is management-attributed to timing; revenue still +20%. Sensitivity: crediting it → Quality ≈ 69.3, still fails.

## 4. fetch_fundamentals output (verbatim; price at run time $105.12)
```
```
Market Cap            = 109,105,840,128
Enterprise Value      = 112,913,833,984
Shares Outstanding    = 1,037,917,000
Forward PE            = 21.892
FCF Yield %           = 4.354
EV/EBIT               = 51.795
Net Margin %          = 9.364
Gross Margin %        = 73.080
ROIC % (NOPAT/InvCap) = 10.778  [tax_rate=0.2854, NOPAT=1,557,912,957, InvestedCapital=14,455,000,000]
Revenue 3yr CAGR %    = 22.377
Net Debt/EBITDA       = -0.409  [EBITDA_ttm=3,235,000,064]
FCF/NI TTM % (plain)  = 328.720
(FCF - SBC)/NI TTM %  = 167.958  [reported NI]
SBC yield %           = 2.129
Gross buyback yield % = 2.586
FCF/NI annual (oldest first) = [668.6%, 156.0%, 236.8%, 259.3%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 58.724 / 23.101 / 89.608  (n=20 quarters)
```

```
SBC block (TTM, advisory — no score effect)
  SBC 2,323,000,000.0   FCF 4,750,000,000.0   Market cap 109,105,840,128.0
  SBC/FCF = 48.9%  -> at/above the 30% † watch line
  FCF yield (reported)  = 4.35%
  FCF yield after SBC   = 2.22%
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
  (cycle_peak / value_trap need 8 consecutive quarters of Diluted EPS; if yfinance lacks them, run python -m scripts.scoring.flags_common with manually sourced EPS TTM figures.)
```
```

## 5. Quality Score

Inputs: net margin 9.364%, ROIC 7.56% (re-based), gross margin 73.08%, net debt/EBITDA 0.902, (FCF−SBC)/NI 168.0%, SBC $2,323M, FCF $4,750M.

## Quality Score

**Profitability (25%)**
```
NetMargin_Component = clamp((9.364/30)x100) = 31.21
ROIC_Component = clamp((7.56/30)x100) = 25.20
Profitability_Score = (31.21 + 25.20) / 2 = 28.21
```
**Margins (15%)**
```
GrossMargin_Score = clamp((73.08/80)x100) = 91.35
```
**Growth (20%)**
```
Growth_Score = clamp((22.377/25)x100) = 89.51
+10 TAM/pricing-power evidence: ServiceNow Q3 FY2026 release (8-K EX-99.1, 2026-10-28): AI ACV target raised again to $1.7B for 2026 (from $1B at start of year, +70%); RPO $29.7B (+22%), cRPO $13.65B (+20.5%).
Growth_Score (final, clamped) = 99.51
```
**Balance Sheet (15%)**
```
BalanceSheet_Score = clamp(100x(1 - 0.902/4)) = 77.45
```
**Moat Signal (15%)**
```
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Carried forward from 2026-08-09 (Gartner MQ ITSM leadership) - NOT re-verified this session |
| brand_premium | True | Carried forward from 2026-08-09 (annual price escalators, Now Assist add-on pricing) - NOT re-verified |
| network_effect | False | No two-sided marketplace mechanism documented |
| switching_costs | True | Carried forward: CMDB as embedded IT system of record - NOT re-verified |
| scale_cost_advantage | False | No cost-per-unit citation vs smaller ITSM competitors |
Moat_Score = (3/5) x 100 = 60.00
```
**FCF Quality (10%)**
```
FCFQuality_Score = clamp(((1.6796 - 0.40)/0.60)x100) = 100.00  [ratio = (FCF - SBC)/NI]
```
**Quality Score — Final**
```
Quality Score = (28.21x0.25) + (91.35x0.15) + (99.51x0.20) + (77.45x0.15) + (60.00x0.15) + (100.00x0.10)
= 71.273 -> rounds to 71.3
```

# Quality Score = 71.3 — FAILS the 80.0+ gate

## 6. Valuation Score

Inputs: price $106.35; FCF yield 4.303% ($4,750M ÷ $110,382M); SBC yield 2.105%; EV/EBIT 51.97 (EV $113,299M ÷ EBIT $2,180M); fwd PE 22.149; 5yr PE 23.101 / 58.724 / 89.608. Scenarios: Bull EPS 5.20 × 25 = $130; Base 4.80 × 20 = $96; Bear 4.20 × 15 = $63. Intrinsic growth cut 18% → 15% (cRPO guide 18.5%). Gross buyback yield 2.556% (TTM; Q3 = $0).

## Valuation Score

**FCF Yield (40%)**
```
FCF yield after SBC = 4.303% - 2.105% (SBC yield) = 2.1980%
FCF_Score = clamp(100x(1 - 2.1980/10)) = 78.020
```
**EV/EBIT**
```
EV/EBIT_Score = clamp((51.97 - 12)/23 x 100) = 100.000
```
**Forward PE**
```
FwdPE_Score (raw) = clamp((22.149 - 23.101)/(89.608 - 23.101) x 100) = 0.000
Deviation vs 5yr avg (58.724) = (22.149 - 58.724)/58.724 x 100 = -62.283%
Historical PE Modifier: >20% below 5yr avg -> -10
FwdPE_Score = clamp(0.000 + -10) = 0.000
```
**PEG**
```
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT
```
**Rate Environment Gate**
```
EY = 1/22.149 x 100 = 4.5149%
Spread = EY - 10Y (4.929%) = -0.4141pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 4.929% -> Step 2 bracket modifier = +5
Total Rate Modifier = 5 + 5 = +10
```
**Upside/Downside Modifier**
```
PW Fair Value = 0.25x130.0 + 0.50x96.0 + 0.25x63.0 = 96.2500
Gap Upside % = (96.2500/106.35) - 1 = -9.4969%
Annualized gap = -9.4969% / 2yr = -4.7485%/yr
E = -4.7485 (annualized gap) + 15 (intrinsic growth) + 2.5560 (shareholder yield: 0 div + 2.556 buyback) = 12.8075%/yr
E (12.8075%) >= H (10.0%) -> M = -15 x clamp((12.8075-10.0)/15, 0, 1) = -2.8075
Upside/Downside Modifier (bounded [-15, +15]) = -2.8075
```
**Raw Weighted Score**
```
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 71.208
```
**Final Valuation Score**
```
Final Score = Raw (71.208) + Rate Modifier (+10) + Upside/Downside Modifier (-2.808)
= 78.400 -> rounds to 78.4
```

# Valuation Score = 78.4

## 7. Composite Score

```
# Composite Score REFUSED — Quality Score fails the 80.0+ gate
Quality Score 71.3 < 80.0 — fails the gate, Composite Score is not computed for a company that hasn't cleared Phase 01
```
(Script refuses because Quality fails the gate; precedent — raw Valuation Score governs.)

## 8. Action
**TRIM 25–30%** (Valuation 78.4, 70.0–79.9 band). 25–30% of 9 shares = 2.25–2.7 → **sell 2 shares** (22%, nearest whole share). Price $106.35 is above PW fair value $96.25 (+10.5%), so execute at/near market. No order-setup R/R (exit, not entry); `order_setup.py` not run — it needs a rebuilt DCF/blended FV that this session did not redo, so PW multiples FV $96.25 is the trim reference. Est. proceeds ≈ $212.70; realised gain ≈ 2 × (106.35 − 87.61) ≈ $37.5. No MCP tool places orders — for the human to execute.

**Honest read of the signal:** score stays "Expensive" after a −43% drawdown because (a) EV/EBIT on GAAP EBIT is 52× (saturated at 100), (b) SBC is now deducted from FCF yield (4.30% → 2.20%), (c) +10 rate modifier; only forward PE (0) offsets. The framework acts on the score, not price. Position is only ~2%.

**Full Exit triggers:** none met (gross margin 73.1% vs 74.8% = −1.7pp < 3pp; ROIC 7.6% < WACC ~9% but one quarter; leverage 0.9×; Valuation < 90).

**Open order conflict (flag, not acted on):** working order SELL 1 NOW Feb19'27 $85 put @ 5.00 (id 166895475) *opens a short put* (~$8,500 assignment notional) — undocumented, and at odds with a trim thesis. Confirm in TWS.

## 9. Next review trigger
Q4 FY2026 earnings (~late Jan 2027): cRPO growth vs the 18.5% guide; ROIC vs WACC; moat re-verification with fresh citations; mgmt-change check (10-Q Item 5 not read); >15% unexplained price move.

## Glossary

| Term | Meaning |
|---|---|
| **Quality Score** | 0.0–100.0 grade of profitability, margins, growth, balance sheet, moat, FCF quality; 80.0+ needed to pass the gate. |
| **Valuation Score** | 0.0 (cheapest) – 100.0 (most expensive) score; 70.0–79.9 = Trim band. |
| **Composite Score** | 50/50 blend of Quality and (100 − Valuation); not computed when Quality fails the gate. |
| **FCF / FCF yield** | Free cash flow (operating cash flow − capex); yield = FCF ÷ market cap. |
| **SBC** | Stock-based compensation; treated as a real cost in FCF yield and FCF Quality (methodology 2026-10-12). |
| **ROIC** | Return on invested capital — after-tax operating profit per dollar of debt+equity capital. |
| **EV/EBIT** | Enterprise value ÷ operating profit; lower = cheaper. |
| **Rate Environment Gate** | Valuation add-on based on the 10Y Treasury yield and earnings-yield spread. |
| **RPO / cRPO** | (Current) remaining performance obligations — contracted revenue not yet recognised; a SaaS backlog gauge. |
| **Rule 9** | Re-score only on documented triggers (earnings, guidance, M&A, management change, >15% unexplained move). |
| **Rule 6 (normalisation)** | Strip one-time items from earnings before scoring. |
| **Moat** | Durable competitive advantage protecting profits. |
| **TAM** | Total addressable market. |
| **Net Debt/EBITDA** | Debt minus cash, divided by operating earnings before depreciation; leverage gauge. |
| **Phase 04 Quality Watch** | Flag for a held position whose Quality Score is below the 80.0 gate; not a forced exit. |

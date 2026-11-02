# RESCORE — NFLX (Netflix, Inc.) — 2026-11-02

**Task type:** RESCORE (`--both`). **Why NFLX:** user asked for a rescore of "fallen or non-growing" holdings; NFLX is −47% from its 52-week high ($116.73), last reviewed 2026-07-17, and reported Q3 2026 on 2026-10-20 (Rule 9 earnings trigger; ad-revenue guide cut). Sister session: [NOW](2026-11-02-rescore-now.md).
**10Y Treasury:** 4.929% (Yahoo `^TNX` close 2026-10-30) → Step 2 = +5. **Last review:** Valuation 49.3 · Quality 69.8 · Composite 39.8 (false green light), HOLD — [2026-07-17](2026-07-17-rescore-nflx.md).
**Position:** 12 shares (IBKR, avg cost $87.79), 1.62% of NLV; a working BUY 20 @ $46.97 GTC (id 1206895879) is on the book, undocumented.

## 1. Live price (Rule 0)
$62.19 — IBKR `get_price_snapshot` (contract 15124833), 2026-11-02 (bid 62.16 / ask 62.21); Yahoo $62.08. 10-for-1 split already effected 2025-11-14 (all per-share figures post-split). Analyst mean PT $84.76 (Yahoo; sanity only).

## 2. Rule 9 trigger — Q3 2026 (8-K EX-99.1 filed 2026-10-20, read from SEC via subagent)
- Revenue $12,874M (+11.8%, +11% FX-neutral). Operating income $4,459M (+37%, margin 34.6%, "ahead of forecast due primarily to timing of expenses"). NI $3,664M, diluted EPS $0.87 (vs $0.82 consensus per secondary sources).
- OCF $3,162M, capex $279M, FCF $2,884M. SBC $133.7M. **Buybacks $4.8B in Q3** (63.9M sh, "largest quarter ever"); $22.3B authorization left.
- Debt $15,132M (+$1B bond), cash+ST inv. $8,223M → net debt $6,910M.
- **Guidance:** Q4 revenue $13.4B (+11.5%), Q4 margin 26.0% (incl. ~120bp headcount-reduction hit); FY26 revenue **$51.1B (trimmed)**, margin 31.5%; FY26 FCF ~$12.0B (was $12.5B, "real estate transaction"); **FY26 ad revenue ~$2.7B vs ~$3B** ("slower rollout of some ad product capabilities"; ad-tier expansion to 15 countries pushed to 2027).
- Stock reaction: −5–6% after hours (secondary sources); letter itself cites "investor concern about our view hours growth".

## 3. Data gaps / flags (how handled)
1. **One-time WBD termination fee ($2.8B, Q1 2026 "interest and other income")** inflates TTM NI and TTM FCF (Q1 OCF $5.29B vs $1.74B Q2 / $3.16B Q3). Rule 6: NI normalised to **$11,967M** (TTM NI $14,767M − $2.8B; no tax shield assumed, conservative) and TTM FCF to **$8,575M** ($11,375M − $2.8B; the cash tax later paid on the fee is inside TTM FCF, so FCF ex-fee is slightly understated — conservative). Fee size from Q1 2026 coverage; the Q1 letter itself was not re-opened this session.
2. **`fetch_fundamentals` EBIT includes the fee** (EV/EBIT 14.2 uses EBIT of ~$18.6B). Replaced with quarterly GAAP operating income TTM **$15,566M** → EV/EBIT 17.08×; ROIC re-based to NOPAT $12,987M ÷ $41,078M = **31.6%**. The script's `--normalised-ni` flag mis-scales when given $M (it expects raw dollars), so (FCF−SBC)/NI was computed by hand: ($8,575M − $540M) ÷ $11,967M = **67.1%**.
3. **Net margin:** $11,967M ÷ TTM revenue $49,735M = **24.06%** (script's 29.7% includes the fee).
4. Net debt/EBITDA: $6,910M ÷ EBITDA $15,957M = **0.433×** (script 0.340× used older debt data).
5. **Moat:** brand-premium and market-share evidence is thin (no fresh churn or subscriber disclosure; carried from 2026-07-17 + Q3 regional growth). Still 3/5.
6. **Advisory flags:** `cycle_peak` UNKNOWN (EPS history unavailable; TTM EPS inflated by the one-time fee — noted, handled by normalisation); `value_trap_candidate` UNKNOWN — fwd PE 16.5 > 15, not raised; `multiple_ceiling` NONE (fwd PE 16.5, EPS growth ~5%). SBC/FCF 4.7% — no concern.
7. Forward EPS $3.77 = Yahoo NTM consensus (FY27 +5.1% vs FY26); Q4 guide EPS $0.67 vs ~$0.73 consensus, so estimates may still be falling.

## 4. fetch_fundamentals output (verbatim; as printed, includes the fee-inflated figures — see flags 2–3)
```
```
Market Cap            = 258,497,380,352
Enterprise Value      = 264,227,553,280
Shares Outstanding    = 4,163,939,676
Forward PE            = 16.461
FCF Yield %           = 4.400
EV/EBIT               = 14.239
Net Margin %          = 29.691
Gross Margin %        = 50.685
ROIC % (NOPAT/InvCap) = 37.688  [tax_rate=0.1657, NOPAT=15,481,494,663, InvestedCapital=41,078,324,000]
Revenue 3yr CAGR %    = 12.640
Net Debt/EBITDA       = 0.340  [EBITDA_ttm=15,957,057,536]
FCF/NI TTM % (plain)  = 77.032
(FCF - SBC)/NI TTM %  = 73.375  [reported NI]
SBC yield %           = 0.209
Gross buyback yield % = 4.975
FCF/NI annual (oldest first) = [36.0%, 128.1%, 79.5%, 86.2%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 36.023 / 18.798 / 51.457  (n=20 quarters)
```

```
SBC block (TTM, advisory — no score effect)
  SBC 540,064,000.0   FCF 11,375,063,000.0   Market cap 258,497,380,352.0
  SBC/FCF = 4.7%
  FCF yield (reported)  = 4.40%
  FCF yield after SBC   = 4.19%
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
  (cycle_peak / value_trap need 8 consecutive quarters of Diluted EPS; if yfinance lacks them, run python -m scripts.scoring.flags_common with manually sourced EPS TTM figures.)
```
```

## 5. Quality Score

Inputs (normalised for the $2.8B WBD fee, see flags): net margin 24.06%, ROIC 31.6%, gross margin 50.685%, net debt/EBITDA 0.433, (FCF−SBC)/NI 67.1%, SBC $540M, FCF $8,575M.

## Quality Score

**Profitability (25%)**
```
NetMargin_Component = clamp((24.06/30)x100) = 80.20
ROIC_Component = clamp((31.6/30)x100) = 100.00
Profitability_Score = (80.20 + 100.00) / 2 = 90.10
```
**Margins (15%)**
```
GrossMargin_Score = clamp((50.685/80)x100) = 63.36
```
**Growth (20%)**
```
Growth_Score = clamp((12.64/25)x100) = 50.56
+10 TAM/pricing-power evidence: Netflix Q3 2026 shareholder letter (8-K EX-99.1, 2026-10-20): revenue +12% (+11% FX-neutral) with all four regions growing: UCAN +11%, EMEA +11%, LATAM +17%, APAC +12%; operating income +37% to $4.46B, margin 34.6%; letter says subscription revenue growth outperformed.
-10 structural growth deceleration evidence: Netflix YoY revenue growth: Q4'25 17.6% -> Q1'26 16.2% -> Q2'26 13.4% -> Q3'26 11.8%, Q4'26 guided 11.5%; FY26 revenue guide trimmed to $51.1B and FY26 ad revenue cut to ~$2.7B from ~$3B (Q3 2026 letter, 8-K 2026-10-20).
Growth_Score (final, clamped) = 50.56
```
**Balance Sheet (15%)**
```
BalanceSheet_Score = clamp(100x(1 - 0.433/4)) = 89.18
```
**Moat Signal (15%)**
```
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Double-digit revenue growth in every region Q3 2026 (UCAN +11%, EMEA +11%, LATAM +17%, APAC +12%); Q3 2026 letter |
| brand_premium | True | Letter: subscription revenue growth outperformed; price changes carried (carried from 07-17 session, no fresh churn disclosure) |
| network_effect | False | No two-sided marketplace mechanism |
| switching_costs | False | Month-to-month, cancel-anytime |
| scale_cost_advantage | True | Largest content-spend scale; cash content spend/amortization ~1.1x FY26 (Q3 letter) |
Moat_Score = (3/5) x 100 = 60.00
```
**FCF Quality (10%)**
```
Net income normalised: TTM NI $14,767M (derived FCF/plain ratio) less $2.8B Warner Bros. Discovery termination fee recorded in Q1 2026 'interest and other income' (shareholder letter via Q1 2026 coverage) = $11,967M; no tax shield assumed (conservative). TTM FCF also reduced by the $2.8B cash fee: $11,375M -> $8,575M.
FCFQuality_Score = clamp(((0.6710 - 0.40)/0.60)x100) = 45.17  [ratio = (FCF - SBC)/NI]
```
**Quality Score — Final**
```
Quality Score = (90.10x0.25) + (63.36x0.15) + (50.56x0.20) + (89.18x0.15) + (60.00x0.15) + (45.17x0.10)
= 69.033 -> rounds to 69.0
```

# Quality Score = 69.0 — FAILS the 80.0+ gate

## 6. Valuation Score

Inputs: price $62.19; FCF yield 3.311% ($8,575M ÷ $258,953M, fee-normalised); SBC yield 0.2085%; EV/EBIT 17.08 (EV $265,863M ÷ operating income $15,566M); fwd PE 16.49 (62.19 ÷ 3.771); 5yr PE 18.798 / 36.023 / 51.457. Scenarios: Bull EPS 4.00 × 22 = $88.0; Base 3.77 × 16 = $60.3 (≈ current multiple, no re-rate; cross-check 07-17 PW DCF $56.20); Bear 3.40 × 12 = $40.8. Intrinsic growth 10%; gross buyback yield 4.966%.

## Valuation Score

**FCF Yield (40%)**
```
FCF yield after SBC = 3.311% - 0.2085% (SBC yield) = 3.1025%
FCF_Score = clamp(100x(1 - 3.1025/10)) = 68.975
```
**EV/EBIT**
```
EV/EBIT_Score = clamp((17.08 - 12)/23 x 100) = 22.087
```
**Forward PE**
```
FwdPE_Score (raw) = clamp((16.49 - 18.798)/(51.457 - 18.798) x 100) = 0.000
Deviation vs 5yr avg (36.023) = (16.49 - 36.023)/36.023 x 100 = -54.224%
Historical PE Modifier: >20% below 5yr avg -> -10
FwdPE_Score = clamp(0.000 + -10) = 0.000
```
**PEG**
```
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT
```
**Rate Environment Gate**
```
EY = 1/16.49 x 100 = 6.0643%
Spread = EY - 10Y (4.929%) = 1.1353pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 4.929% -> Step 2 bracket modifier = +5
Total Rate Modifier = 5 + 5 = +10
```
**Upside/Downside Modifier**
```
PW Fair Value = 0.25x88.0 + 0.50x60.3 + 0.25x40.8 = 62.3500
Gap Upside % = (62.3500/62.19) - 1 = 0.2573%
Annualized gap = 0.2573% / 2yr = 0.1286%/yr
E = 0.1286 (annualized gap) + 10 (intrinsic growth) + 4.9660 (shareholder yield: 0 div + 4.966 buyback) = 15.0946%/yr
E (15.0946%) >= H (10.0%) -> M = -15 x clamp((15.0946-10.0)/15, 0, 1) = -5.0946
Upside/Downside Modifier (bounded [-15, +15]) = -5.0946
```
**Raw Weighted Score**
```
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 36.425
```
**Final Valuation Score**
```
Final Score = Raw (36.425) + Rate Modifier (+10) + Upside/Downside Modifier (-5.095)
= 41.330 -> rounds to 41.3
```

# Valuation Score = 41.3

## 7. Composite Score

```
# Composite Score REFUSED — Quality Score fails the 80.0+ gate
Quality Score 69.0 < 80.0 — fails the gate, Composite Score is not computed for a company that hasn't cleared Phase 01
```
(Script refuses because Quality fails the gate; precedent — raw Valuation Score governs.)

## 8. Action
**HOLD — watch only; no add, no trim.** Valuation 41.3 sits in the lower Fair-Value/"Cheap" boundary, but Quality 69.0 fails the 80.0 gate, so no new entry is allowed and the nominal Composite is not computed (script refuses; prior sessions' 39.8 / 43.0 were flagged "false green lights"). Price $62.19 ≈ PW fair value $62.35 (+0.3%), so there is no valuation edge either; Upside/Downside Modifier is −5.1 (E = 15.1%/yr vs 10% hurdle driven by 5.0% buyback yield + 10% intrinsic growth).

**Full Exit triggers (checked, none met):** margins not broken (op margin 34.6%, FY guide 31.5%); ROIC 31.6% ≫ cost of capital; leverage 0.43×; *guidance*: FY26 revenue guide trimmed to $51.1B and ad revenue cut ~10% this quarter, but this is the first trim — the "2+ consecutive guidance cuts without a one-off" condition is not met yet. **Watch hard:** a second consecutive guide cut at Q4 would trip "Growth thesis broken".

**Quality trend:** 74.0 → 69.8 → 69.0. Decline now driven by FCF Quality (45.2 after the fee is stripped) and the −10 deceleration modifier (growth 17.6% → 16.2% → 13.4% → 11.8% → guided 11.5%). Phase 04 Quality Watch stays on.

**Open order flag:** working BUY 20 NFLX @ $46.97 GTC (id 1206895879, ~$939) is undocumented and conflicts with HOLD / no-new-entry (price is 24% above it; the framework's 2:1 R/R and quality gate would not authorise a buy). Confirm in TWS or cancel. `order_setup.py` not run (HOLD, no BUY/TRIM).

## 9. Next review trigger
Q4 2026 earnings (~mid-Jan 2027): FY26 revenue/ad guide vs the trimmed $51.1B / ~$2.7B; the Q4 margin including headcount cuts; cash tax paid on the WBD fee (to firm up normalised FCF); buyback pace ($22.3B left); >15% unexplained price move.

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

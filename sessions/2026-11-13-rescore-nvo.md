# RESCORE — NVO (Novo Nordisk A/S, US-listed ADR) — 2026-11-13

**Task type:** RESCORE (mode `--both`)
**Trigger:** Q3 / 9M 2026 results — Novo company announcement No 65/2026, Form 6-K filed 2026-11-04 (accession 0001628280-26-069805) — a genuine Rule 9 earnings trigger, plus a third consecutive guidance raise.
**10Y:** 5.14% (Yahoo ^TNX 13 Nov, intraday; 11 Nov close 4.998%). **Rate Regime +10.**
**Position:** 0.43% of NLV (holdings.md). **Last review:** 09 Aug 2026 (Valuation 51.4, Quality 67.2, Composite 42.1 ref, HOLD).
**ADR note:** 1 NVO ADR = 1 Novo B-share; IFRS DKK reporting; ratios are DKK-to-DKK, USD only for market cap/EV/yields. FX **USD/DKK 6.7786** (x-rates 13 Nov; 6.7379 on 12 Nov — a ~0.6% swing, immaterial).

## 1. Live price (Rule 0)
**$41.63** (bid 41.63 / ask 41.64), +2.41% on day — IBKR `get_price_snapshot` (contract 10611); Yahoo 41.635. Down 11.9% from $47.26 (08-09). 52-wk $34.21–$61.26. Yahoo analyst mean PT $45.22.
Shares 4,417M = Q3 net profit 16,740M ÷ diluted EPS 3.79 (the vendor `sharesOutstanding` 3,333M is a share-class artefact — not used) → market cap $183,880M (vendor $183,542M ✓).

## 2. Data & gaps
Primary source: 6-K 2026-11-04 (main text only — the appendices were unreadable, see gaps). Q4'25 from yfinance (DKK).

| DKKm | Value | Basis |
|---|---|---|
| 9M'26 net sales adj. / reported | 227,746 / 254,506 | 6-K (excl. 340B reversal 26,760) |
| 9M'26 gross profit adj. | 182,872 | 6-K |
| 9M'26 EBIT adj. / reported | 97,967 / 109,690 | 6-K (adj. excludes 340B 26,760 and 15,037 impairments) |
| 9M'26 net profit adj. / reported | 82,502 / 86,286 | 6-K |
| Q3'26 net sales / EBIT adj. / net profit adj. | 79,195 / 31,720 (+27% CER) / 25,602 | 6-K |
| Q4'25 sales / GP / EBIT / NI (reported) | 79,144 / 63,996 / 31,736 / 26,891 | yfinance |
| **TTM adj. (Q4'25 + 9M'26 adj.)** | sales **306,890**; GP **246,868** (80.44%); EBIT **129,703**; NI **109,393** (35.65%) | derived |
| Balance sheet 30 Sep 2026 | debt 134,480; cash 44,151; **net debt 90,329** (down from 95,645); equity 217,802 | yfinance (equity ties to 6-K 217,802) |
| D&A TTM ex-impairment | 18,737 = Q4'25 5,562 (FY25 21,982 − H1'25 8,663 − Q3'25 7,757) + 9M'26 13,175 (EBITDA 137,902 − EBIT 109,690 − impairments 15,037) | derived |
| TTM adj. EBITDA | 148,440 → ND/EBITDA **0.609×** | derived |
| TTM FCF (OCF − PP&E − intangibles) | **44,969** = Q4'25 −37,505 + Q1 12,045 + Q2 42,398 + Q3 28,031 | yfinance quarterly (sums to company 9M 83,780 less 1,306 intangibles ✓) |
| TTM FCF, company definition (OCF − PP&E only) | 71,683 (= Q4'25 −12,097 + 9M 83,780) | sensitivity only |
| 9M buybacks / dividends paid | 10,002 / 51,900 (trailing div DKK 11.70/sh) | 6-K / yfinance |
| 5yr PE low/avg/high | 14.10 / 30.52 / 38.25 | **carried** from 2026-08-09 (wisesheets annual series; `fetch_fundamentals` PE series is wrong for this ADR — DKK EPS vs USD price) |
| PEG | 4.21 | Yahoo (current) |
| Fwd EPS (NTM) | $3.414 → fwd PE **12.19×** | Yahoo |

**Gaps (flagged, none estimated):** (1) **TTM SBC not found** — Novo's 6-K text and the 20-F body do not give it; **user approved using FY2024 DKK 2,289M** (Yahoo annual cash-flow line) as an out-of-period proxy; it is ~5% of TTM FCF so cannot move any outcome. (2) Q4'25 one-off items not found — Q4'25 treated as reported/clean (its adjusted figures could differ). (3) US GLP-1 share vs Lilly **not refreshed** for Q3 (6-K gives only Novo's own metrics: Wegovy >50% of new branded-obesity starts, Wegovy pill ~80% new-to-brand). (4) CagriSema FDA date not confirmed — 6-K says US launch prep for early 2027; the Ozempic 25 mg pill decision is Q4 2026. (5) Interim dividend per share not found. (6) Tax: 21.9% effective rate used (6-K).

## 3. Fundamental changes since 08-09
- **Guidance raised a 3rd time:** FY26 adjusted sales and operating profit growth −2% to +2% CER (was −6% to 0%); FCF guide DKK 60–70B (was 45–55B); capex ~DKK 50B (was 55B).
- Q3 adjusted EBIT 31,720 (+34% DKK / +27% CER), adjusted gross margin 82.1%; Q3 adjusted sales +4% CER.
- Q3 non-cash impairments DKK 8.7B (ziltivekimab 4.6B; manufacturing right-sizing 4.1B) — second consecutive clean-up quarter.
- Net debt 95.6B → 90.3B; Wegovy pill ~3.6M Q3 prescriptions, >8M since launch.
- Price −11.9% since 08-09 despite the beat/raise — no Rule 9 trigger beyond earnings.

## 4. Rate gate
EY = 1/12.193 = 8.20%; spread vs 5.14% = +3.06pp → Step 1 pass (+0); 10Y >5% → Step 2 +10. **Total +10** (was +5).

## 5. Quality Score (script output)
```
NetMargin 35.65% -> 100.00 ; ROIC = NOPAT 101,297 (EBIT 129,703 x (1-21.9%)) / IC 308,131 (134,480 + 217,802 - 44,151) = 32.87% -> 100.00 ; Profitability 100.00
GrossMargin 80.44% -> 100.00 (was 98.68)
Growth: CAGR 20.43% -> 81.72 ; -10 structural deceleration -> 71.72
BalanceSheet: ND/EBITDA 0.609x -> 84.78
Moat: 0/5 -> 0.00
FCF Quality: (44,969 - 2,289)/109,393 = 39.02% -> clamp((0.3902-0.40)/0.60) = 0.00
Quality Score = 25.0 + 15.0 + 14.344 + 12.717 + 0 + 0 = 67.060 -> 67.1
# Quality Score = 67.1 — FAILS the 80.0+ gate
```
Hard disqualifiers: FCF/NI <70% for FY2024 (69.0%) and FY2025 (28.3%) → the growth-capex carve-out (Catalent/Clayton/Kalundborg build-out + Q4'25 intangible purchases DKK 25.4B) is carried from 08-09; N/D-EBITDA 0.61× and SBC 5% of FCF pass.
**Judgement calls:** the −10 deceleration is now cited to Novo's own numbers (9M adj. sales 0%/+2% CER, guide −2%/+2% vs a 20.4% CAGR), not the stale share data. The Moat share signal stays FALSE on the carried Aug Lilly-60/Novo-39 data (not refreshed; Novo's own sub-segment claims don't reverse the aggregate). Sensitivity: company-definition FCF (71,683) → Quality 70.5 — still a clear fail.

## 6. Valuation Score (script output)
Scenarios (Aug structure, EPS scaled by new/old fwd EPS 3.414/3.075 = 1.110; multiples unchanged): bull $63.95 (3.552 × 18), base $47.80 (3.414 × 14), bear $26.98 (2.998 × 9); intrinsic growth −3.0% (9M adj. diluted EPS −3%, 6-K); catalysts inside 2yr (oral Wegovy international ramp, CagriSema launch early 2027).
```
FCF yield after SBC = 3.608% - 0.184% = 3.424% -> FCF_Score 65.760   (FCF 44,969/6.7786 = $6,634M ; SBC $338M)
EV/EBIT = (183,880 + 90,329/6.7786 = 13,325 => EV 197,205) / (129,703/6.7786 = 19,134) = 10.31x -> 0.000
FwdPE 12.193 below 5yr low 14.10 -> raw 0 ; dev vs 30.52 avg -60.05% -> -10 -> 0.000
PEG 4.21 -> clamp((4.21-0.5)/2.0) = 100.000
Raw = 65.76x0.40 + 0x0.25 + 0x0.20 + 100x0.15 = 41.304
Rate Modifier +10
PW FV = 0.25x63.95 + 0.5x47.80 + 0.25x26.98 = 46.6325 ; gap +12.02% ; annualised 6.01%/yr
E = 6.008 - 3.0 + 4.948 (div 4.146 [DKK 11.70/6.7786/41.63] + gross buyback 0.802 [10,002/6.7786/183,880]) = 7.956%/yr -> M = 5 x (10-7.956)/10 = +1.022
Final = 41.304 + 10 + 1.022 = 52.326 -> 52.3
# Valuation Score = 52.3 (was 51.4)
```
**Sensitivities (script re-runs):** 10Y 4.99% → **47.3**; company-definition FCF yield (≈5.75%) → **43.9**; **PEG not scored (Fast Grower eligibility dropped) → 37.3**. The last is the big one: Fast-Grower eligibility is a backward-looking carried ruling (trailing 3yr EPS CAGR 23.5% from 06-20) while forward EPS growth is ≤0 (consensus FY26 +1.6%, FY27 −2.9%; Yahoo earningsGrowth −15.8%); PEG saturates at 100 under it (+15 pts). Flagged for a framework call; no action effect because Quality fails the gate either way.
`flags_common --forward-pe 12.19 --eps-growth -2.9` → `multiple_ceiling NONE`; `cycle_peak`, `value_trap_candidate` UNKNOWN = data gaps (trailing EPS series unavailable). Value-trap is plausible (fwd PE 12.2 with consensus EPS −2.9% FY27 and guided flat growth) — the cheapness is partly the market pricing falling EPS and share loss; treated as unreliable cheapness, consistent with the Quality fail.

## 7. Composite Score
`composite_score --set quality_score=67.1 --set valuation_score=52.3` → **REFUSED** (Quality < 80.0). Hand-calc reference: 0.5×(100−67.1)+0.5×52.3 = 16.45+26.15 = **42.6**, not actionable.

## 8. Action — HOLD (0.43% position)
- Valuation 52.3 → 50.0–69.9 Fair Value band: hold, no new entry, no trim (trim threshold 70.0 far away).
- No add: Quality gate fails (67.1), Moat 0.0, and the cheapness is partly earnings decline. Order setup N/A.
- No exit trigger: guidance raised (not cut), balance sheet improving, margins excellent. The standing override-log/EXIT REVIEW question (flagged since 06-07, no NVO row in override-log.md) is still unactioned — for the user's call.
- Position cap check: 0.43% ≪ 15%.

## 9. Stale-score mechanism
Banner dropped from the new watchlist entry; NVO row removed manually from `watchlist/STALE.md` (`stale_score --apply` does not resolve it and adds a duplicate header row — reverted).

## 10. Next review trigger
Novo FY2026 results (~early Feb 2027); CagriSema US launch/approval (early 2027); Ozempic 25 mg pill FDA (Q4 2026); refresh US share vs Lilly and Q3-era Moat evidence; get actual SBC from the Annual Report 2025 notes; framework decision on PEG eligibility under negative forward growth; 10Y vs 5.00%.

## Glossary
- **340B**: US drug-discount programme; a provision reversal is a one-off non-cash gain.
- **ADR**: US-listed receipt for a foreign share.
- **CER**: constant exchange rate growth.
- **Composite Score**: 0.50×(100−Quality)+0.50×Valuation; valid only if Quality ≥ 80.0.
- **EBIT / EBITDA**: operating profit before interest and tax / plus depreciation and amortisation.
- **EV/EBIT**: enterprise value ÷ operating profit.
- **Fast Grower / PEG**: EPS growing >15%/yr for 3+ years; PE ÷ growth.
- **FCF / FCF Yield**: operating cash flow minus CapEx / ÷ market cap.
- **Forward PE (NTM)**: price ÷ next-12-month expected EPS.
- **Form 6-K / 20-F**: foreign issuer's event report / annual report.
- **Hard disqualifier**: rule failing a company regardless of weighted score.
- **IFRS**: international accounting rules Novo reports under.
- **Moat**: durable competitive advantage.
- **NOPAT / ROIC**: after-tax operating profit / ÷ invested capital.
- **PW Fair Value**: 25% bull / 50% base / 25% bear.
- **Quality Score**: 0–100.0 grade; 80.0+ is the gate.
- **Rate Environment Gate / Rate Regime Modifier**: earnings-yield-vs-10Y test plus bracket add-on.
- **SBC**: stock-based compensation, treated as a real cost.
- **TTM**: trailing twelve months.
- **Upside/Downside Modifier**: ±15 adjustment from expected annual return vs the 10% hurdle.

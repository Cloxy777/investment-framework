# NEW POSITION — MA (Mastercard Incorporated) — 2026-09-11

**Task type:** NEW POSITION (full fresh re-run — not-in-portfolio watchlist refresh)
**Date:** 2026-09-11 (Friday, intraday, US markets open)
**10Y US Treasury Yield:** 4.95% (WebSearch: TradingEconomics/Bloomberg, 2026-09-11 intraday print — bond selloff pushing 10Y toward 5%, highest since 2023)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket, per [strategy.md](../framework/strategy.md))
**Purpose of this session:** a **full fresh re-run**, not a delta check — every input refetched live rather than carried forward, since MA's Q2 2026 earnings (30 Jul 2026) and the BVNK acquisition close (3 Aug 2026) have both occurred since the [2026-07-09 session](2026-07-09-new-position-ma.md) (Quality 84.6, Valuation 38.0 carried-forward, Composite 26.7, nominal BUY-Full but R/R-gated WATCHLIST ONLY).
**Current MA portfolio weight:** 0% — **not held** (absent from [holdings.md](../portfolio/holdings.md), no entry in [override-log.md](../portfolio/override-log.md)). Most recent prior MA session: [2026-07-09](2026-07-09-new-position-ma.md) — no more recent rescore exists, so this run is not a duplicate.
**Sector:** Payment network (duopoly with Visa) — asset-light financial

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$566.15** | IBKR `get_price_snapshot` (contract_id 38685693, NYSE — resolved via `search_contracts`), `last` field, intraday 2026-09-11. |
| Prior close (yfinance, cross-check) | $565.37 (2026-09-10 close) | Consistent — $0.78 (+0.14%) intraday move, no data-quality concern. |
| 52-week range | $464.58 – $601.23 | IBKR `misc_statistics` |
| Bid/Ask | $565.03 / $570.00 | IBKR `bid_ask` |
| Price vs. 2026-07-09 review ($520.05) | **+8.87%** | Under the 15% Rule 9 "unexplained move" threshold, and not unexplained regardless — general market/sector drift plus a beat-and-raise Q2 print. |
| Analyst consensus PT | Mean $668.53 / Median $669.00 (36 analysts, yfinance), high $740 / low $550 | "Strong Buy" consensus. Live price sits ~15.3% below consensus mean. |

---

## 2. Rule 9 Trigger Check (2026-07-09 → 2026-09-11) — multiple triggers fired, full fresh re-run warranted

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | **YES** | Q2 2026 reported 30 Jul 2026 (after close, as scheduled). Net revenue $9,277M (+14% YoY, +12% CC); net income $4,388M (+18.5% YoY); GAAP diluted EPS ~$4.97, adjusted EPS $5.04 (+21%). GAAP operating margin 60.2%. Beat on both revenue and EPS. |
| Guidance revision | **YES (raised, not cut)** | FY2026 net-revenue-growth guidance moved from "high end of low-double-digit to low-teens" to **"high end of low-double-digit range,"** explicitly "higher within the range than prior expectations" on strength of H1 — a positive revision, not a cut. Full-year opex growth still guided low-double-digits. |
| Management change | No | CFO transition (Ling Hai succeeding Sachin Mehra) took effect 3 Aug 2026 as previously announced (2 Jun 2026) — not a new trigger, already reflected in the 07-09 session. CEO Michael Miebach unchanged. |
| M&A | **YES (closed)** | BVNK stablecoin-infrastructure acquisition (~$1.8B) **closed 3 Aug 2026** — ahead of the "late 2026" original timeline, clearing regulatory hurdles roughly five months early. This is a completed M&A event since the 07-09 session (which only had it as pending). |
| Macro shift | **YES** | 10Y Treasury moved 4.58% (07-09) → 4.95% (09-11) — still inside the "3.5–5%" bracket (no Rate Regime Modifier bracket change), but the move is material (bond-market selloff, cited by Bloomberg as pushing yields "to the cusp of 5%," highest since 2023). |
| >15% unexplained price move | No | +8.87% since 07-09 — under the 15% threshold, and explained by the earnings beat/guide-up, not unexplained. |

**Conclusion:** multiple Rule 9 triggers fired (earnings, guidance raise, M&A close) — this session is correctly scoped as a full fresh re-run of every input (TTM financials, valuation multiples, fair-value scenarios), not a delta check. All data below is refetched live; nothing is carried forward from 07-09 except the qualitative moat mechanism descriptions, which are re-verified against current disclosures.

---

## 3. Data Sources & Methodology Notes

- **TTM financial period:** four quarters ended 2026-06-30 (Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026), sourced via `yfinance` `quarterly_financials`/`quarterly_cashflow`/`quarterly_balance_sheet`, cross-checked against Mastercard's own Q2 2026 10-Q (SEC EDGAR) and Q2 2026 8-K earnings release for revenue/net income/interest expense.
- **GAAP EBIT field:** used `"Total Operating Income As Reported"` (not the plain `"Operating Income"`/`"EBIT"` fields, which run ~2-6% higher) — same convention established in the 2026-06-22 MA session after that session's own reconciliation. TTM = $20,465M (sum of Q3'25 $5,061M + Q4'25 $4,910M + Q1'26 $4,907M + Q2'26 $5,587M).
- **TTM EBITDA** = TTM EBIT (GAAP, as above) + TTM D&A ($1,195M, sum of last 4 quarters) = **$21,660M**. (Note: `yfinance`'s own bundled `"EBITDA"` field TTM-sums to $22,116M because it's built on the plain `"EBIT"` field, not the GAAP-reconciled one — flagged for consistency, not used.)
- **Net Debt** = Total Debt ($24,643M, 2026-06-30) − Cash & Equivalents ($11,291M) = **$13,352M**.
- **5-year trailing PE band** reconstructed via the documented `yfinance` `get_earnings_dates` + rolling-TTM-EPS method (46 quarterly EPS prints back to 2021, last 20 quarters used): **avg 34.99×, range 27.65×–44.27×**. This supersedes the 06-22 session's 36.225×/27.695–54.159× band — the oldest (highest-multiple, 2021) quarters have rolled off the 20-quarter window, materially compressing the top of the range.
- **Credit rating** re-confirmed unchanged: Aa3 (Moody's) / A+ (S&P), both stable (WebSearch cross-check 2026-09-11) — investment grade, asset-light Debt Gate override (Upgrade 5) still applies.

---

## 4. MA — Quality Score (full re-computation, 2026-06-29 methodology)

**Hard disqualifier check (all must pass before the weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | FY2022–2025: 101.7% / 97.3% / 105.5% / 109.8%; TTM 98.27% — all comfortably ≥70% every year on record | disqualify if <70% for 2+ yrs *without* explanation | ✅ PASS, comfortably |
| Net Debt/EBITDA over threshold? | **0.616×** (vs. 2.5× standard or 6× asset-light-override floor — both cleared with enormous headroom) | disqualify if over applicable threshold | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FCF-positive and growing every year on record (FY2022–2025 and TTM) | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### 4a. Profitability (25% weight)

```
Net Margin (TTM)     = $16,257M / $35,083M = 46.34%
NetMargin_Component  = clamp((46.34/30)×100, 0, 100) = clamp(154.5, 0, 100) = 100.0
```

**ROIC** (NOPAT / Invested Capital, period-end 2026-06-30, consistent with the 07-09 session's convention):
```
TTM Pretax Income = $20,173M; TTM Tax Provision = $3,916M → TTM effective tax rate = 19.41%
NOPAT             = TTM EBIT × (1 − tax rate) = $20,465M × (1 − 0.1941) = $16,492.3M
Total Debt (2026-06-30) = $24,643M; MA Stockholders' Equity (2026-06-30) = $5,611M
Invested Capital  = $24,643M + $5,611M = $30,254M
ROIC (TTM)        = $16,492.3M / $30,254M = 54.51%
ROIC_Component    = clamp((54.51/30)×100, 0, 100) = clamp(181.7, 0, 100) = 100.0
```

```
Profitability_Score = (100.0 + 100.0) / 2 = 100.0   (no FCF cap — FCF-positive and growing every year on record)
```

### 4b. Margins (15% weight)

Gross-margin proxy = operating margin (payment networks report ~100% "gross margin" per data aggregators — no traditional COGS line):
```
Operating Margin (TTM, GAAP "Total Operating Income As Reported") = $20,465M / $35,083M = 58.33%
GrossMargin_Score = clamp((58.33/80)×100, 0, 100) = clamp(72.92, 0, 100) = 72.92
```
No structural-trend bonus applicable — already well above the 40% threshold the bonus targets.

### 4c. Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $22,237M → FY2025 $32,791M) = (32,791/22,237)^(1/3) − 1 = 13.82%
Growth_Score = clamp((13.82/25)×100, 0, 100) = 55.29
```
**+10 (documented TAM expansion / pricing power, cited, re-verified this session):**
- Q2 2026 payment-network **rebates and incentives** grew 22–23% YoY (20–19% currency-neutral) "reflecting growth in key drivers and new/renewed partner deals" — Mastercard Q2 2026 earnings materials/10-Q, still outpacing the 14% headline revenue growth (same dynamic documented in the 07-09 session, confirmed continuing).
- Value-Added Services and Solutions (VAS) remains the fastest-growing net-revenue segment (per Q2 2026 earnings call commentary), continuing the trend already documented with pricing-power language in the Q1 2026 8-K.
- **BVNK acquisition closed 3 Aug 2026** (ahead of schedule) — a *realized*, not merely pending, TAM-expansion vector: Mastercard now owns stablecoin settlement infrastructure with ~$30B in annualized payment volume, per company/press disclosures. Cited directionally (too new to show up in TTM financials) but a stronger, more concrete signal than the "pending" citation used in the 07-09 session.
- FY2026 revenue-growth guidance was **raised** (not cut) this window — "higher within the range than prior expectations" — the opposite of structural deceleration evidence.

No structural-deceleration evidence found this session. **Growth_Score (with bonus) = clamp(55.29 + 10, 0, 100) = 65.29**

### 4d. Balance Sheet (15% weight)

```
Net Debt/EBITDA (TTM) = $13,352M / $21,660M = 0.616×
```
**Asset-light override (Upgrade 5) applies** — payment network, ~100% financial debt, interest coverage 27.36× (TTM EBIT $20,465M ÷ TTM interest expense $748M — far above the 15× threshold), investment-grade rated (Aa3/A+, both stable, re-confirmed §3). Using the /6 denominator:
```
BalanceSheet_Score = clamp(100×(1 − 0.616/6), 0, 100) = 89.73
```
(Standard /4 denominator would give 84.59 — either way comfortably high; leverage has ticked up modestly from 07-09's 0.531× on debt-funded buybacks/BVNK financing, but the score impact is minor.)

### 4e. Moat Signal (15% weight) — checklist, cited evidence per signal, re-verified this session

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Nilson Report 2025 US data (via Capital One Shopping/WalletHub aggregation, checked 2026-09-11): Mastercard holds ~29.6% of combined Visa+Mastercard US purchase volume, Visa ~70.4% — stable duopoly position. **Growing (share-of-growth, not raw volume):** MA's TTM revenue grew 16.0% (stockanalysis.com TTM figure) / Q2 2026 net revenue grew 14% YoY vs. Visa's Q3 FY2026 net revenue growth of 14% (near-parity this specific quarter) — but MA's own 3yr revenue CAGR (13.82%, FY2022→FY2025) continues to outpace Visa's over the same window (10.921%, per this repo's 2026-07-05 V session), the more decision-relevant multi-year comparison for a moat check. |
| Brand premium (pricing power) | **TRUE** | Rebates/incentives growing 22-23% YoY alongside continued net-revenue growth (not eroding into flat/negative net yield) and VAS's continued outperformance — consistent pricing-power evidence carried through Q1 and Q2 2026 disclosures (§4c). |
| Network effect | **TRUE** | Unchanged mechanism, re-confirmed: Mastercard's four-party network model (issuer, acquirer, merchant, cardholder) per its own 10-K business description — each additional participant increases network value to all others. No structural change to this mechanism since 07-09. |
| Switching costs | **FALSE** | Re-verified this session: rebates and incentives (the cost of retaining/winning customer volume) grew 22-23% YoY in Q2 2026, continuing to **outpace** total net revenue growth (14%) — the same "must keep paying more to retain non-exclusive customers" dynamic documented in the 07-09 session, now confirmed for a second consecutive quarter rather than a one-off. Marked FALSE on this continuing cited evidence. |
| Scale cost advantage | **TRUE** | Mastercard's TTM/Q2 2026 GAAP operating margin (58.3% TTM, 60.2% in Q2 alone) remains dramatically wider than American Express's operating margin (~17-21% range per prior-session sourcing, no contrary evidence found this session) — same asset-light "toll booth" cost-structure gap vs. a named smaller competitor. |

```
Moat_Score = (4/5) × 100 = 80.0
```

### 4f. FCF Quality (10% weight)

```
FCF/NI (TTM) = $15,975M / $16,257M = 98.27%
FCFQuality_Score = clamp(((0.9827 − 0.40)/0.60)×100, 0, 100) = clamp(97.11, 0, 100) = 97.11
```
(TTM FCF sourced from `yfinance` quarterly-cashflow sum: Q3'25 $5,304M + Q4'25 $4,712M + Q1'26 $2,664M + Q2'26 $3,295M = $15,975M. A separately-sourced stockanalysis.com TTM figure read $16,702M — a different quarterly cutoff/rounding convention; both are comfortably in the same range and don't change the disqualifier or score materially. Used the `yfinance` figure as the framework's documented primary source.)

### 4g. Quality Score — Final

```
Quality Score = (100.0×0.25) + (72.92×0.15) + (65.29×0.20) + (89.73×0.15) + (80.0×0.15) + (97.11×0.10)
              = 25.000 + 10.938 + 13.058 + 13.4595 + 12.000 + 9.711
              = 84.1665 → rounds to 84.2
```

# Quality Score = 84.2 — PASSES the 80.0+ gate (comfortably; essentially unchanged from the 07-09 session's 84.6 — the small drop is entirely attributable to modestly higher leverage from debt-funded buybacks/BVNK financing, not a fundamentals deterioration).

---

## 5. MA — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE (yfinance forwardPE) = 24.558×
EY     = 1 ÷ 24.558 = 4.072%
Spread = EY − 10Y Treasury = 4.072% − 4.95% = −0.878%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** → **+5 additive** (yellow flag, not a veto).

**Step 2 — Rate Regime Modifier**
10Y = 4.95% → "3.5–5%" bracket (just under the >5% "+10" threshold, per the Bloomberg-cited approach-to-5% context) → **+5**

**Total Rate Modifier for MA = +10** (same combined result as the 06-22 and 07-09 sessions, though the underlying 10Y print has risen materially — a further ~0.05pp move above 5.00% would push Step 2 to +10 and the total to +15; flagged as a near-term watch item).

---

## 6. MA — Valuation Score (Phase 02, full re-computation)

**Inputs:**

| Item | Value | Basis |
|---|---|---|
| Live price | $566.15 | §1 |
| Shares outstanding | 869,464,115 | yfinance |
| **Market Cap** | $566.15 × 869.464115M = **$492,247.1M** | Computed |
| Net Debt | $13,352M | §3 |
| **Enterprise Value (EV)** | **$505,599.1M** | Computed |
| TTM EBIT (GAAP) | $20,465M | §3 |
| **EV/EBIT** | 505,599.1 ÷ 20,465 = **24.706×** | Computed |
| TTM FCF | $15,975M | §4f |
| **FCF Yield** | 15,975 ÷ 492,247.1 = **3.245%** | Computed |
| Forward PE (yfinance) | **24.558×** | yfinance `forwardPE` |
| 5yr PE band | avg 34.99×, low 27.65×, high 44.27× (n=20 qtrs) | §3, freshly reconstructed |
| PEG | **1.48** | yfinance `pegRatio` |
| EPS FY22/23/24/25 | $10.22 / $11.83 / $13.89 / $16.52 | yfinance financials (unchanged — fiscal years complete since before 07-09) |
| EPS 3yr CAGR | 17.37% (accelerating each year) | Computed |
| Fast Grower test | **Pass** — GAAP EPS growth >15% for 3 consecutive years on a clean base, re-confirmed | Phase 02 / Upgrade 3 |

**FCF Yield (40% weight):**
```
FCF_Score = clamp(100 × (1 − 3.245/10), 0, 100) = 67.55
```
Contribution: 67.55 × 0.40 = **27.02**

**EV/EBIT (25% weight):**
```
EV/EBIT_Score = clamp((24.706 − 12) / 23 × 100, 0, 100) = 55.24
```
Contribution: 55.24 × 0.25 = **13.81**

**Forward PE (20% weight, primary range formula — forward PE sits below the 5yr low):**
```
FwdPE_Score = clamp((24.558 − 27.65) / (44.27 − 27.65) × 100, 0, 100) = clamp(−18.6, 0, 100) = 0.0
```
Contribution: 0.0 × 0.20 = **0.0** (forward PE ~29.8% below the 5yr average — the single biggest "cheap" signal in the score; no Structural Quality Override needed, that only gates the +10 *expensive*-side penalty)

**PEG (15% weight, Fast Grower path):**
```
PEG_Score = clamp((1.48 − 0.5) / 2.0 × 100, 0, 100) = 49.0
```
Contribution: 49.0 × 0.15 = **7.35**

**Raw weighted score (Fast Grower path):**
```
= 27.02 + 13.81 + 0.0 + 7.35 = 48.18
```
**+ Rate Modifier (+10) = 58.18** (before the Upside/Downside Modifier)

**Stalwart cross-check (PEG's 15% redistributed to EV/EBIT at 40%):**
```
= 67.55×0.40 + 55.24×0.40 + 0.0×0.20 = 27.02 + 22.10 = 49.12  →  +10 = 59.12
```
Both paths land within ~1pt of each other.

---

## 7. MA — Upside/Downside Modifier

**Step 0 — Scenario fair value (Rule 7; multiples method).** Anchored on NTM EPS (yfinance `forwardEps` = **$23.02**, cross-check: $566.15 ÷ 24.558 = $23.05 ✓) and MA's fresh trailing 5-year PE band (27.65×–34.99×–44.27×). PE selections cross-checked against analyst PT band ($550 low / $668.53 mean / $740 high):

| Scenario | Weight | PE applied | Rationale | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | 32.0× | Cross-border/VAS growth sustains, BVNK integration (now closed, ahead of schedule) becomes a realized growth contributor rather than a hedge; multiple partially re-rates toward mid-band. FV lands just below the $740 analyst high PT. | $23.02 × 32.0 = **$736.70** |
| **Base** | 50% | 29.0× | Consensus continuation of mid-to-high-teens EPS growth; multiple stays compressed well below the 34.99× 5yr average, reflecting the higher-rate regime (10Y approaching 5%) and persistent interchange-fee/regulatory overhang. FV lands almost exactly at the $668.53/$669.00 analyst mean/median PT. | $23.02 × 29.0 = **$667.64** |
| **Bear** | 25% | 24.0× | Rate regime tightens further (10Y crosses 5%, Step 2 modifier moves to +10) and/or regulatory action on interchange fees compresses the multiple toward the 5yr low. FV lands just above the $550 analyst low PT. | $23.02 × 24.0 = **$552.53** |

```
PW Fair Value = 0.25×736.70 + 0.50×667.64 + 0.25×552.53 = $656.13
```
(Sits ~1.9% below the $668.53 analyst mean PT — conservative, sanity check passes.)

**Step 1 — Expected annual return E.**
```
Gap Upside %      = (656.13 ÷ 566.15) − 1                = +15.89%
Catalyst window   = 2 years (Q3/Q4 2026 earnings, FY2027 cross-border/VAS cycle,
                    BVNK integration milestones now that the deal has closed — within
                    Rule 10's 18–24mo horizon → full upside credit allowed, no −5 cap)
Annualized gap    = 15.89% ÷ 2                            = +7.95%
Intrinsic growth  = +13.0%/yr  (Mastercard's own raised FY2026 guidance — "high end of
                    low-double-digit" currency-neutral net revenue growth — deliberately
                    below the 17.37% 3yr GAAP EPS CAGR to avoid double-counting the
                    buyback contribution already in shareholder yield below)
Shareholder yield = dividend 0.61% + net buyback 2.28%/yr = +2.89%
                    (buyback: 3yr diluted-share decline, 971M FY2022 → 906M FY2025,
                    (906/971)^(1/3) − 1 = −2.28%/yr)

E = 7.95% + 13.0% + 2.89% = +23.84%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 23.84% ≥ H → M = −15 × clamp((23.84 − 10)/15, 0, 1) = −15 × clamp(0.923, 0, 1) = −15 × 0.923 = −13.84
```
**Modifier M = −13.84**

**Guardrail checks:**
1. **Catalyst:** documented (Q3/Q4 2026 earnings, FY2027 cross-border/VAS cycle, now-closed BVNK integration) within 18–24 months → upside credit allowed, no −5 cap. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($656.13) sits just below the analyst mean/median, not the bull case; bear underwritten just above the $550 low PT. ✓
3. **Full calc shown** (above), no black box. ✓
4. **Bounded ±15:** at −13.84, inside the bound, not floored. ✓

---

## 8. MA — Final Valuation Score & Composite Score

```
Final Valuation Score = raw weighted 48.18 + Rate Modifier (+10) + Upside/Downside Modifier (−13.84)
                       = 44.34 → rounds to 44.3   (Fast Grower path — primary)
Stalwart cross-check   = 49.12 + 10 − 13.84 = 45.28 → 45.3   (same action band)
```

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 84.2) + 0.50 × 44.3
                = 0.50 × 15.8 + 22.15
                = 7.90 + 22.15
                = 30.05 → rounds UP (exactly on ".X5") → 30.1
```

| | Value |
|---|---|
| Quality Score (this session) | 84.2 (PASSES 80.0+ gate) |
| Valuation Score (this session, Fast Grower path) | 44.3 |
| **Composite Score** | **30.1** |

**Composite Score = 30.1 → falls in the 30.0–49.9 "Cheap" band** (nominal Standard position, 3–5%) — **one full band less attractive than the 07-09 session's 26.7 ("Very Cheap," nominal Full position 6–8%).** This is a genuine, real change: the ~8.9% price rise since 07-09 outpaced the modest improvement in fair-value inputs (fair value moved from $640.67 to $656.13, +2.4%, while price moved +8.9%), and Quality Score dipped slightly (84.6→84.2) on higher leverage. **Boundary-sensitivity check:** the 30.05 raw composite sits almost exactly on the 29.9/30.0 "Very Cheap"/"Cheap" band edge — recomputed with unrounded Quality (84.1665) and Valuation (44.34) inputs, the raw composite is 30.09, still rounding to 30.1 and still inside the Cheap band on either side of the rounding convention. Not a knife-edge call in practice, but flagged transparently per "no black box."

---

## 9. MA — Action Table Read

**Composite Score 30.1 → nominal action: BUY — Standard position (3–5% of portfolio), per the current Action Table (30.0–49.9 band).**

Per the operating brief, the full order setup is run below using the Composite-Score-implied band's Margin-of-Safety/Stop parameters (30.0–49.9 → MoS 25–30%, Max Loss 25–30% — [fair-value-methodology.md](../framework/fair-value-methodology.md)).

---

## 10. Order Setup & R/R Gate

```
Blended Fair Value (= PW FV, §7): $656.13
PRIMARY SELL TARGET (= Blended FV): $656.13
BULL-CASE TRIM TARGET (bull × 0.90): $736.70 × 0.90 = $663.03
```

**Full applicable range (30.0–49.9 band: MoS 25–30%, Max Loss 25–30%):**
```
R/R = MoS / [(1 − MoS) × MaxLoss%]
Max R/R  (MoS=30%, MaxLoss=25%): 0.30 / (0.70×0.25) = 0.30/0.175 = 1.714:1
Min R/R  (MoS=25%, MaxLoss=30%): 0.25 / (0.75×0.30) = 0.25/0.225 = 1.111:1
```
**R/R ranges 1.11:1 – 1.71:1 across the entire applicable band — fails the 2:1 minimum throughout, at every combination.**

**Concrete check at the combination giving the best (highest) R/R in the band (MoS 30%, Max Loss 25%):**
```
BUY PRICE (limit)      = $656.13 × (1 − 0.30)               = $459.29
STOP LOSS               = $459.29 × (1 − 0.25)               = $344.47
R/R at formal entry     = ($656.13 − $459.29) / ($459.29 − $344.47) = $196.84 / $114.82 = 1.71:1   ❌ below 2:1
R/R at live price ($566.15) = ($656.13 − $566.15) / ($566.15 − $344.47) = $89.98 / $221.68 = 0.41:1   ❌ far below 2:1
```

**Per fair-value-methodology.md Step 6 ("Below 2:1 = do not enter... wait for lower entry, find tighter stop, or pass on the trade entirely"): R/R fails the minimum threshold across the entire applicable Composite-band MoS/Stop range. No order should be placed.**

**Net: WATCHLIST ONLY — do not enter.** MA is not held (0% weight); no position exists to hold or trim, and no order is being placed. The nominal Composite-Score band (30.1, "Cheap") reads as a Standard-position BUY signal, but — consistent with every prior MA session (06-22, 07-09) — the R/R gate independently blocks entry: MA's own MoS/MaxLoss band structure caps achievable R/R below 2:1 at every combination the current band permits, regardless of the absolute fair-value gap.

---

## 11. Recommendation

**PASS on entry now / WATCHLIST ONLY.** Composite Score 30.1 ("Cheap," nominally BUY-Standard 3–5%) is a real, favorable score, and MA continues to clear the Quality gate comfortably (84.2). But per the Phase 03 action table cross-checked against the R/R gate (§10), no order is being placed today: R/R is 1.11:1–1.71:1 across the entire applicable band, below the 2:1 minimum everywhere. This is not a marginal, "wait a few points" case — the structural math (MoS ÷ [(1−MoS) × MaxLoss]) caps R/R below 2:1 for this Composite-Score band regardless of price, so a lower entry price alone would not fix it without also finding a materially tighter stop than the band's own 25–30% Max Loss range permits.

---

## 12. Next Review Trigger

- **Routine:** MA's Q3 2026 earnings release (expected late October/early November 2026, per Mastercard's usual quarterly cadence) — next scheduled full re-score.
- **Watch (highest priority): the 10Y Treasury.** At 4.95% and "cusp of 5%" per Bloomberg, a move above 5.00% would push the Step 2 Rate Regime Modifier from +5 to +10 (total Rate Modifier +10 → +15), pushing the Valuation and Composite Scores further into the "Expensive" direction even before any fundamental change — worth a standalone check before the next scheduled earnings-driven rescore if the move happens.
- **Watch: the R/R gate.** If price pulls back toward the $459–492 buy-price range (MoS 25–30% band) without a fundamental deterioration, or if the fair-value/PW-FV inputs move meaningfully higher at the next earnings print, re-run the order setup — R/R could approach or clear 2:1 well before the next scheduled rescore.
- **Rule 9 triggers (standing):** any further guidance revision, management change, a 10Y Treasury move materially past 5%, a >15% unexplained price move from $566.15, or the Q3 2026 earnings print itself.
- **Governance note:** unlike the 07-09 session, this session found **no** live unauthorized IBKR order flagged against MA in the data reviewed — if one exists, it is outside this session's scope to check further (no holdings/order-snapshot review was part of this NEW POSITION task).

---

## Glossary

*(New terms not already in [glossary.md](../framework/glossary.md) added there as part of this session; existing framework terms cited below per [operating-brief.md](../framework/operating-brief.md) OUTPUT FORMAT step 9.)*

| Term | Meaning |
|---|---|
| **10-Q** | A US company's quarterly SEC financial-disclosure filing — this session's source for MA's Q2 2026 income statement and balance sheet detail (interest expense, debt, equity). |
| **8-K** | A US company's "current report" SEC filing disclosing a material event between regular quarterly/annual filings — source for MA's Q2 2026 earnings release language. |
| **BVNK** | A stablecoin-infrastructure company Mastercard agreed to acquire (~$1.8B, announced March 2026) — **closed 3 Aug 2026**, ahead of the original "late 2026" schedule; now a realized (not merely pending) TAM-expansion vector. |
| **CAGR** | Compound Annual Growth Rate. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate. MA this session: 30.1 ("Cheap" band), down one band from 07-09's 26.7 ("Very Cheap"). |
| **D&A** | Depreciation & Amortization. |
| **Debt Gate** | This framework's balance-sheet check on Net Debt/EBITDA (Hybrid Upgrade 5) — standard threshold <2.5×, relaxed to <4× (and the score's denominator to /6) for asset-light payment networks/exchanges with strong interest coverage and investment-grade ratings. Applied to MA again this session. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — used in the Rate Environment Gate's Step 1 spread test against the 10Y Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — MA re-confirmed as a Fast Grower this session (17.37% 3yr EPS CAGR, accelerating). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Interest coverage (ratio)** | EBIT ÷ interest expense — part of the asset-light Debt Gate override test (MA: 27.36× this session). |
| **Invested Capital** | Total capital (debt + equity) put to work in a business — the ROIC denominator. |
| **Investment grade** | A credit rating (Aa3/A+ for MA, re-confirmed unchanged) indicating a low-risk borrower, required for the asset-light Debt Gate override. |
| **Moat** | A durable competitive advantage protecting a business's profits — graded here as a 5-signal checklist. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **NTM (Next Twelve Months)** | Forward-looking 12-month window — used here for the Forward EPS anchoring the fair-value scenarios. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value — 25% bull + 50% base + 25% bear — recomputed fresh this session at $656.13 (vs. 07-09's $640.67). |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. MA this session: 84.2 (vs. 84.6 on 07-09 — essentially unchanged; small dip from higher leverage). |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss on a trade; this framework requires ≥2:1 to enter — MA fails this at every point in the applicable band this session, as in every prior MA session. |
| **Rate Regime Modifier** | The additive −10/0/+5/+10 score adjustment based on the current 10-Year Treasury yield bracket — still +5 this session (3.5–5% bracket), but the 10Y print (4.95%) is now very close to the >5% "+10" threshold. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 9** | This framework's standing instructions to always fetch a live price first, and to force re-valuation on specific documented fundamental triggers (earnings, guidance, M&A, management change, macro shift, >15% unexplained move) — three such triggers fired this session (earnings, guidance raise, M&A close). |
| **Shareholder yield** | Cash returned to owners as a % of price (dividends plus net share buybacks) — feeds the Upside/Downside Modifier's expected-return calculation. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — this session's window is Q3 2025 through Q2 2026 (ended 2026-06-30), refreshed from the 07-09 session's Q2 2025–Q1 2026 window. |
| **VAS (Value-Added Services and Solutions)** | Mastercard's non-core-network product line (fraud/risk tools, tokenization, advisory, issuing/acceptance support) — its fastest-growing revenue segment, cited for this session's Growth and Brand-premium sub-score findings. |

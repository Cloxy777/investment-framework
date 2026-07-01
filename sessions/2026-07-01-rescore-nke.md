# RESCORE — NKE (NIKE, Inc.)

## 1. Session header
- **Task type:** RESCORE (single ticker) — Telegram-triggered (Routine 6)
- **Trigger:** [myroslavkorol/2499](https://t.me/myroslavkorol/2499) (~20:36:55 UTC, 2026-06-30): "В цілому несмертельно. Норм по прибутку але трохи міс по виручці. На пост маркеті -3%" ("Overall not fatal. Fine on profit but a slight miss on revenue. -3% in post-market.") — a follow-up to the same channel's [myroslavkorol/2498](https://t.me/myroslavkorol/2498) post (2026-06-30, ~14:02 UTC) that had already flagged NKE's FY2026 Q4 earnings as imminent and was logged as "no action — earnings not yet released; flagged for next-run revisit" in [portfolio/snapshots/telegram-watch.md](../portfolio/snapshots/telegram-watch.md). This post's text is a trigger only, never a financial input (Rule 0) — NIKE's own SEC Form 8-K (filed 2026-06-30) is the actual data source used below.
- **Date:** 2026-07-01
- **10Y US Treasury yield:** 4.38% (FRED `DGS10`, most recent non-blank value, 2026-06-29 — 2026-06-30/07-01 not yet posted)
- **Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% band)
- **Prior score:** 43.1 (2026-06-20 rescore) — Cheap band, HOLD existing / do NOT add, under a documented value-trap override
- **First-use jargon decode:** see closing Glossary section (step 9).

## 2. Data gaps flagged (before proceeding)

- **yfinance unreachable** — identical `curl_cffi` TLS-impersonation `SSLError` already documented for AAPL/CHTR/WSE/AMD/CDR/CRCL in this repo's session history. Fallback per Rule 0's documented contingency: NIKE's own SEC filings.
- **FY2026 cash-flow statement not yet filed.** NIKE's fiscal year ended 31 May 2026; the Q4/full-year earnings release ([Form 8-K](https://www.sec.gov/Archives/edgar/data/320187/000032018726000076/q4fy26exhibit991er.htm), filed 2026-06-30) contains the income statement and balance sheet but **not** a cash-flow statement — that comes with the Form 10-K, not yet filed (Nike's 10-K for a fiscal year ended 31 May has historically been filed in mid-to-late July). Confirmed via SEC XBRL `companyconcept` API: the latest `NetCashProvidedByUsedInOperatingActivities` tag on file is the **9-month YTD figure through 28 Feb 2026 ($1,231M)** from the Q3 FY2026 10-Q — no full-year FY2026 figure exists anywhere yet.
  - **Handling (not a guess):** FCF Yield and FCF/NI Conversion sub-inputs continue to use **FY2025's audited full-year FCF ($3.268B = OCF $3,698M − CapEx $430M, both SEC-filed)** — the same normalization base already used in the 2026-06-20 session, carried forward unchanged rather than invented. D&A for the EBITDA calc is similarly carried forward from FY2025 ($775M, audited) since FY2026 D&A isn't filed yet either. Flagged explicitly per CLAUDE.md Rule 0; **next revisit trigger set on the FY2026 10-K filing** (see step 10).
  - 9-month FY2026 YTD OCF ($1,231M) − CapEx ($546M) = **+$685M**, confirming FY2026 cash flow remains positive through Q3 (used only as a sign check, not a scored input).
- **No analyst-consensus forward-EPS source reachable via yfinance or the IBKR connector.** Forward PE sourced instead from a third-party consensus aggregator (stockanalysis.com, 36 analysts covering, FY2027 EPS consensus $2.37) — a real, cited external figure, not invented, consistent with how this framework already uses third-party analyst consensus price targets as a sanity check (fair-value-methodology.md Rule 0, Step 4).
- **5yr historical PE range (18.2× low / 40.3× high / 29.5× avg) carried forward unchanged from the 2026-06-20 session** — the `yfinance`-based reconstruction method (`get_earnings_dates` + price history) that built this range is unavailable this session for the same TLS reason above. A slow-moving 5-year trailing statistic; not expected to have shifted materially in 11 days. Flagged for a full recompute once yfinance access is restored.
- **Nike's own Q4 FY2026 EBIT-by-segment table discloses the exact one-time IEEPA tariff-recovery benefit** ($986M gross-margin / EBIT benefit for the full year, largely offsetting the IEEPA tariffs paid earlier in FY2026 per Nike's own footnote) — used qualitatively below to judge whether FY2026's reported EBIT needs further normalization; it does not, per Nike's own disclosure that the year's tariff cost and its recovery roughly net out (see step 4).

## 3. Live data (Rule 0 — fetched first)

| Item | Value | Source |
|---|---|---|
| Live price | **$39.80** | IBKR `get_price_snapshot` (contract_id 10291, NYSE) — after-hours reaction to the just-released Q4 earnings, session change **−3.05% (−$1.25)** vs. prior close $41.05 — matches the post's "-3% post-market" framing (corroboration only, not a financial input) |
| 52-week range | **$39.80 (new intraday low, not yet reflected in IBKR's `misc_statistics` field, which still shows $40.00) – $78.72** | IBKR `get_price_snapshot` |
| Diluted weighted-avg shares (FY2026) | 1,481.0M | SEC Form 8-K income statement — used as the market-cap share count (same reconciled 1.481B-share basis flagged in the 2026-06-20 session vs. yfinance's unreliable `sharesOutstanding` field) |
| Market cap (computed) | $58.94B (1,481.0M × $39.80) | Computed |
| Total debt | $7,942M (current LT debt $2,000M + LT debt $5,942M) | SEC Form 8-K balance sheet (31 May 2026) |
| Cash + short-term investments | $9,027M ($7,563M + $1,464M) | SEC Form 8-K balance sheet |
| Enterprise value (computed) | $57.86B | Computed (Market cap + Debt − Cash&STI) |
| Analyst consensus FY2027 EPS | $2.37 (36 analysts) | stockanalysis.com/stocks/nke/forecast — cited third-party consensus, not scored trailing data |
| 10Y Treasury | 4.38% | FRED `DGS10`, 2026-06-29 |

## 4. Fundamental changes since last review (FY2026 Q4, reported 30 Jun 2026)

Source: [NIKE Form 8-K, Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/320187/000032018726000076/q4fy26exhibit991er.htm) (filed 2026-06-30, fiscal year ended 31 May 2026).

- **Full FY2026:** Revenue $46,398M (flat vs. FY2025's $46,309M, reported basis; **−2% currency-neutral**). Net income $3,108M (**−3%** YoY). Diluted EPS **$2.10** (vs. $2.16 FY2025, −3%). Gross margin 42.9% (+20bps). EBIT $3,850M (+2%). Effective tax rate 20.3% (vs. 17.1% FY2025).
- **Q4 FY2026 alone:** Revenue $10,972M (−1% reported / −4% currency-neutral). Diluted EPS **$0.72** (vs. $0.14 Q4 FY2025, +414% — beat the post's own "fine on profit" framing). Gross margin jumped to 49.2% (+890bps), **but ~900bps of that is a one-time, non-recurring benefit from the expected recovery of $986M in previously-paid IEEPA tariffs** (the IEEPA tariff regime was ruled unauthorized by the US Supreme Court on 20 Feb 2026) — Nike's own disclosure states this recovery "largely offsets" the IEEPA tariff cost recognized earlier in FY2026, so the **full-year** EBIT/margin figures are reasonably clean on a net basis (the one-off is a within-year timing effect, not a full-year overstatement) — no further ad hoc normalization applied beyond noting this.
- **Greater China:** Q4 revenue −12% reported / −17% currency-neutral; full-year −11% reported / −13% currency-neutral — a continuation, not a reversal, of the decline already flagged in the 2026-06-20 session (which cited "~−20%" guided).
- **Wholesale vs. Direct:** Q4 Wholesale +4% reported; NIKE Direct −7% reported (Digital −12%, stores −5%) — the mix shift toward lower-margin wholesale (already noted 2026-06-20) continues.
- **Capital returns:** FY2026 dividends $2.4B (+5%), buybacks **$123M** (1.8M shares) for the full year — a small amount did resume at some point in FY2026 (weighted diluted share count fell from 1,487.6M FY2025 → 1,481.0M FY2026, a −0.44% reduction), a partial update to the 2026-06-20 session's "buybacks effectively paused ($0 in Q3)" note; still far below the ~$3.0B/yr pace of FY2025 and earlier.
- **Q3 FY2026 (already known, unchanged):** the −3% currency-neutral revenue / $0.35 EPS beat covered in the 2026-06-20 session.

## 5. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** EY = 1 ÷ Forward PE = 1 ÷ 16.79 = **5.96%**. Spread = 5.96% − 4.38% = **+1.58%**, which is **≥ +1.5% → PASS → +0** (no yellow-flag addition — this is a change from the 2026-06-20 session, which failed this step at +5, because Forward PE has fallen sharply — see step 6).
- **Step 2 — Rate Regime Modifier:** 10Y 4.38% sits in the 3.5–5% band → **+5**.
- Combined Rate-Gate additions: **+5**.

## 6. Quality Score (first computation for NKE — 2026-06-29 methodology, see [quality-scoring.md](../framework/quality-scoring.md))

NKE has never been scored under the Quality Score / Composite Score methodology added 2026-06-29 (its `holdings.md` row shows `?` for both columns) — this is its first pass.

```
Profitability (25%): Net Margin FY2026 = 3,108/46,398 = 6.70%; ROIC FY2026 = NOPAT/(Debt+Equity)
  NOPAT = EBIT × (1 − eff. tax rate) = 3,850 × (1 − 0.203) = $3,068.5M
  Invested Capital = Total Debt ($7,942M) + Shareholders' Equity ($14,865M) = $22,807M
    (this IC definition — no cash netting — reconciles with the 2026-06-20 session's own
    stated ROIC figures: recomputing FY2025 the same way gives 14.80%, matching that
    session's "FY2025: 14.5%" to within rounding; used for consistency, not invented fresh)
  ROIC FY2026 = 3,068.5 / 22,807 = 13.45%
  NetMargin_Component = clamp((6.70/30)×100) = 22.33
  ROIC_Component       = clamp((13.45/30)×100) = 44.83
  Profitability_Score  = (22.33 + 44.83) / 2 = 33.58   (no FCF-positive cap — 3yr positive, confirmed §2)

Margins (15%): Gross margin FY2026 42.92% (19,911/46,398)
  GrossMargin_Score = clamp((42.92/80)×100) = 53.65
  3yr trend: FY2024 44.56% → FY2025 42.74% → FY2026 42.92% — net DOWN over 3 years despite the
    small FY25→FY26 uptick (itself partly IEEPA-recovery-assisted) → NOT structurally expanding,
    no +10 bonus.

Growth (20%): Revenue 3yr CAGR (FY2023 $51,217M → FY2026 $46,398M) = (46,398/51,217)^(1/3) − 1 = −3.24%
  Growth_Score = clamp((−3.24/25)×100, 0, 100) = 0.0
  No TAM-expansion/pricing-power bonus (revenue is declining, not expanding).
  No −10 structural-deceleration penalty applied: the decline is attributed to company-specific
    execution/mix issues (DTC pullback, wholesale-channel shift, China share loss, tariffs) within
    a global athletic-footwear category that is itself still growing (Euromonitor/WWD, see Moat
    below) — judged cyclical/competitive, not a structurally shrinking TAM. Judgment call, disclosed.

Balance Sheet (15%): Net Debt = Total Debt ($7,942M) − Cash&STI ($9,027M) = −$1,085M (net cash)
  EBITDA = EBIT ($3,850M) + D&A (FY2025 audited, carried forward per §2: $775M) = $4,625M
  Net Debt/EBITDA = −1,085/4,625 = −0.235×
  BalanceSheet_Score = clamp(100×(1−(−0.235)/4)) = 105.9 → clamp to 100.0

Moat Signal (15%) — checklist, cited evidence only:
  ✗ Market share stable/growing — FALSE. Euromonitor International (via WWD, 2026) and YipitData's
     2026 footwear-market-trends report both document Nike LOSING footwear-market share in 2025–2026
     to Hoka, On, New Balance, and Adidas across both wholesale and direct channels, even though Nike
     remains the #1 player by revenue (~18% global footwear share per Euromonitor; ~27% of the
     broader sportswear category per Kantar). "Still largest" ≠ "stable or growing" — marked false.
  ✗ Brand premium — FALSE. Kantar BrandZ's "Most Valuable Global Brands" ranking shows Nike's brand
     value falling from 27th (2024) → 51st (2025) → 69th (2026); Zara has overtaken Nike as the
     world's most valuable apparel brand per Kantar's 2026 report. Documented erosion of the
     pricing-power proxy, not evidence of a sustained premium.
  ✗ Network effect — FALSE. No documented two-sided-marketplace or user-growth-driven mechanism
     cited for Nike's core footwear/apparel business.
  ✗ Switching costs — FALSE. No documented lock-in mechanism (integration depth, contractual,
     data/workflow migration cost) for a consumer footwear/apparel purchase — same treatment as
     every prior consumer-discretionary name scored in this repo.
  ✓ Scale cost advantage — TRUE. Nike's ~$46.4B annual revenue is, per Kantar/WWD's own framing,
     "nearly double its closest rival" in the category — real evidence of sourcing, manufacturing,
     and marketing-spend scale that smaller competitors (Hoka $2.2B, On ~low single-digit billions)
     cannot match, even while those smaller players grow faster off a lower base.
  Moat_Score = (1/5) × 100 = 20.0

FCF Quality (10%): FY2025 FCF/NI (carried forward per §2) = 3,268/3,219 = 101.5%
  FCFQuality_Score = clamp(((1.015 − 0.40)/0.60)×100) = 100.0

Quality Score = 33.58×0.25 + 53.65×0.15 + 0.0×0.20 + 100.0×0.15 + 20.0×0.15 + 100.0×0.10
              = 8.395 + 8.0475 + 0 + 15.0 + 3.0 + 10.0
              = 44.4425 → 44.4
```

**⚠️ Quality Score 44.4 — FAILS the 80.0+ gate decisively.** No individual hard disqualifier fires (FCF/NI conversion clears 70% comfortably; net cash position clears the Debt Gate; FCF positive at least 3 consecutive years including the FY2026 9-month sign-check) — the failure is purely the weighted average, driven by weak Growth (0.0, declining revenue), weak Moat (20.0, only scale-advantage cited-true, both share and brand-value signals now documented as actively eroding rather than merely absent), and modest Profitability (33.58).

**Per the RESCORE process (unlike a NEW POSITION session), an existing holding failing the Quality Gate is not retroactively force-exited** — but this is NKE's **first-ever computed Quality Score, and it fails decisively**, which is itself new information worth surfacing prominently as a **Phase 04 Quality Watch escalation**, not just a routine data point. This hardens, rather than resolves, the "possible value trap" language already carried in NKE's watchlist entry since 2026-06-07/06-20.

## 7. Phase 02 Valuation Score

```
FCF Yield (40% weight): FCF (FY2025, carried forward — §2) $3,268M ÷ Market cap $58,944M = 5.544%
  FCF_Score = clamp(100×(1 − 5.544/10), 0, 100) = 44.56
  contribution = 44.56 × 0.40 = 17.824

EV/EBIT (25% + 15% PEG-redistributed = 40% weight): EV $57,859M ÷ EBIT (FY2026) $3,850M = 15.03×
  EV/EBIT_Score = clamp((15.03 − 12)/23 × 100, 0, 100) = 13.17
  contribution = 13.17 × 0.40 = 5.268

Forward PE (20% weight): $39.80 ÷ FY2027 consensus EPS $2.37 = 16.79×
  5yr range (carried forward, §2): low 18.2×, high 40.3×, avg 29.5×
  FwdPE_Score = clamp((16.79 − 18.2)/(40.3 − 18.2) × 100, 0, 100) = clamp(−6.38, 0, 100) = 0.0
  Historical PE Modifier (Upgrade 2): dev vs 5yr avg = (16.79 − 29.5)/29.5 = −43.1% → >20% below
    → −10 modifier — but FwdPE_Score is already at its 0.0 floor, so the modifier has no further
    effect (can't push the clamped 0–100 sub-score below 0). Both signals point the same direction:
    NKE's forward multiple is now below its own 5-year trading range.
  contribution = 0.0 × 0.20 = 0.0

PEG (15% weight): n/a — NKE is not a Fast Grower (EPS declining, not >15%/yr) → redistributed to EV/EBIT above.

Raw weighted = 17.824 + 5.268 + 0.0 = 23.092
+ Rate Gate Step 1 (EY spread PASS)   +0
+ Rate Gate Step 2 (Rate Regime)      +5
= 28.092  (before Upside/Downside Modifier)
```

## 8. Upside/Downside Modifier — full calc

**Scenario fair values** (Rule 7 — carried forward from the 2026-06-20 session; today's Q4 print was, per Nike's own CFO, "in line with our expectations," so nothing in this release changes the underlying bull/base/bear narrative enough to warrant new scenario numbers — cross-checked against the fresh FY2027 consensus EPS of $2.37, which is consistent with the Base case below):

| Scenario | FV | Assumption |
|---|---|---|
| Bull (25%) | $72 | Turnaround executes, margin inflection sustains into FY2027-28, multiple re-rates toward the historical average on ~$2.60-2.70 normalized EPS 2yr out |
| Base (50%) | $52 | FY2027 consensus EPS $2.37 × a below-average ~22× exit multiple (reflecting ongoing China/competitive headwinds) ≈ $52 |
| Bear (25%) | $33 | China share loss and wholesale-mix margin dilution continue per the moat evidence in §6; margin inflection slips |

```
PW Fair Value = 0.25×72 + 0.50×52 + 0.25×33 = $52.25   (unchanged from 2026-06-20)
Gap Upside %  = (52.25 ÷ 39.80) − 1 = +31.28%   (wider than 2026-06-20's +15.60% — driven by
   today's price drop to $39.80, not by any change in the FV estimate itself)
Catalyst window = 2.0 yr  (unchanged — mgmt's named Q2 FY2027 margin inflection is now only
   ~6-8 months out, but nothing in today's release firms up that timing beyond what was already
   known 2026-06-20, so the same Rule 10 conservative 2yr window is kept rather than shortened
   on optimism)
Annualized gap = 31.28% ÷ 2.0 = +15.64%

Intrinsic growth = +4.0%/yr  (unchanged, conservative — kept below the raw FY2026→FY2027 consensus
   EPS growth implied by $2.10→$2.37 (+12.9%) since that comparison is distorted by FY2026's
   one-time IEEPA tariff-recovery benefit in the base year; not a clean growth-rate input)
Shareholder yield = dividend $1.63/$39.80 = 4.10% + net buyback 0.44% (FY2026 share count −0.44%,
   §4 — updated from the 2026-06-20 session's 0.0% "fully paused" assumption now that the full-year
   figure shows $123M/1.8M shares were repurchased) = 4.54%

E = 15.64 + 4.0 + 4.54 = +24.18%   (expected annual return)
```

**Map E → M** (hurdle H = 10%, E ≥ H branch):
```
M = −15 × clamp((24.18 − 10)/15, 0, 1) = −15 × clamp(0.945, 0, 1) = −14.18
```
**Catalyst guardrail:** a specific catalyst (margin inflection) is named within 18–24 months (in fact within ~6–8 months per management's own words) → the −5 upside cap does **not** bind; M = −14.18 stands, within the [−15, +15] bound.

## 9. Final valuation score + Composite Score

```
FINAL VALUATION SCORE = 28.092 (raw + rate gate) + (−14.18) (Upside/Downside) = 13.912 → 13.9
```

| | Value |
|---|---|
| Raw weighted | 23.092 |
| Rate Gate (Step 1 + Step 2) | +5 |
| Upside/Downside Modifier | **−14.18** (E = +24.18%) |
| **FINAL VALUATION SCORE** | **13.9** |
| Prior valuation score | 43.1 |
| **Quality Score** | **44.4 (FAILS 80.0+ gate)** |

```
Composite Score = 0.50 × (100 − 44.4) + 0.50 × 13.9 = 0.50×55.6 + 0.50×13.9 = 27.8 + 6.95 = 34.75
  → exactly on a ".X5" boundary → round UP (conservative) → 34.8
```

**Composite Score = 34.8** — numerically lands in the "BUY — Standard position 3–5%" band (30.0–49.9) per the Phase 03 action table. **This numeric result is a false green light and must not be acted on at face value** — see §10.

## 10. Action recommendation — HOLD existing, DO NOT ADD (qualitative override strengthened, not resolved)

Two independent reasons both point the same direction, before any qualitative judgment is applied:

**(a) Order-setup gate fails on its own terms.** Treated as Turnaround (Rule 8/Upgrade 4 — ROIC still below the >15% Phase 01 threshold, guided declines persisting):

| Field | Value |
|---|---|
| Blended Fair Value (PW) | $52.25 |
| Margin of Safety (turnaround) | 35% |
| **Buy price (limit)** | **$33.96** (unchanged — PW FV unchanged) |
| Primary sell target | $52.25 |
| Bull-case trim target | $64.80 |
| Stop loss (buy × 0.70) | $23.77 |
| **R/R at buy price** | (52.25−33.96)/(33.96−23.77) = **1.79:1 — still below the 2:1 minimum** |
| R/R at live $39.80 | (52.25−39.80)/(39.80−23.77) = **0.78:1** |

Live price ($39.80) remains well above the disciplined buy price ($33.96), and R/R at the buy price itself (1.79:1) still fails the 2:1 floor — same conclusion as 2026-06-20, independent of anything below. **No order placed.**

**(b) Quality Watch escalation (new this session).** NKE's first-ever computed Quality Score (44.4) fails the 80.0+ gate decisively, and the two moat signals most central to a consumer-brand thesis — market share and brand premium — are now both **documented as actively eroding** (Euromonitor/WWD/YipitData share-loss data; Kantar BrandZ brand-value collapse 27th→51st→69th over 2 years), not merely "not yet evidenced." This is materially different from — and firmer than — the pre-existing "possible value trap" language: it is the first citable, third-party evidence that the *moat itself*, not just trailing ROIC, is deteriorating. This does **not** meet the Full Exit bar (Phase 06 requires *sustained* deterioration, e.g. 2+ quarters, and the global athletic-footwear category itself is still growing — this looks like company-specific competitive/execution weakness within a healthy category, not a shrinking TAM or a broken business model) — but it meaningfully strengthens the case, already on record since 2026-06-07, for converting NKE into a **formal Upgrade 4 Turnaround Sub-Gate review + `override-log.md` entry**, which remains open and unresolved after three consecutive rescores (2026-06-07, 2026-06-20, 2026-07-01).

**Net: HOLD the existing ~1.49%-weight position. Do NOT add — independently blocked by both the R/R gate and the newly-quantified quality deterioration.** The very cheap-looking Composite Score (34.8) reflects a real price/expected-return gap (E = +24.18%) but does not override either the order-setup discipline or the qualitative moat-erosion evidence — consistent with this framework's operating-brief instruction that the score "informs but never overrides" a Turnaround/value-trap qualitative override.

## 11. Next review trigger

- **The FY2026 Form 10-K filing** (expected mid-to-late July 2026) — will supply the actual FY2026 cash-flow statement, closing the FCF/FCF-NI/D&A data gaps flagged in §2 and allowing a full recompute of the FCF-dependent Quality and Valuation sub-scores on a current-year basis rather than the carried-forward FY2025 figures used here.
- **Q2 FY2027 (expected to report ~March 2027):** the named margin-inflection catalyst quarter — if margins do not visibly move by then, both the turnaround thesis and the Upside/Downside Modifier's E=+24.18% (heavily dependent on this catalyst materializing within the 2yr window) should be treated as failed/expired.
- **A formal Upgrade 4 Turnaround Sub-Gate review + `override-log.md` entry** — recommended explicitly, now overdue across three consecutive rescores.
- **Rule 9 triggers (standing):** guidance revision, the margin-inflection catalyst landing or confirmed slipping, a >15% unexplained price move, or a management change.

## 12. Glossary

- **8-K (Form 8-K):** a US company's "current report" disclosing a material event (like an earnings release) between its regular quarterly/annual filings.
- **CAGR:** Compound Annual Growth Rate — the smoothed yearly growth rate between a start and end value.
- **CapEx:** Capital Expenditure — money spent on physical assets.
- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50.
- **D&A:** Depreciation & Amortization.
- **EBIT / EBITDA:** operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **EPS:** Earnings Per Share.
- **EV / EV/EBIT:** Enterprise Value (market cap + debt − cash) / EV divided by EBIT, a valuation multiple.
- **EY (Earnings Yield):** 1 ÷ Forward PE, compared against the 10-Year Treasury yield.
- **Fast Grower:** a company growing EPS >15%/yr for 3+ years — triggers the PEG sub-score.
- **FCF / FCF Yield / FCF/NI conversion ratio:** Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality).
- **Forward PE:** price ÷ next year's expected EPS.
- **FV / PW Fair Value:** Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear).
- **Hard disqualifier:** one of three Quality Score conditions that fails a company regardless of weighted score.
- **Hurdle rate:** the minimum acceptable annual return (10% in this framework).
- **IEEPA:** International Emergency Economic Powers Act — see the new glossary entry added this session; Nike's Q4 FY2026 results include a one-time tariff-recovery benefit tied to a Supreme Court ruling against IEEPA tariffs.
- **IRR:** Internal Rate of Return.
- **Moat:** a durable competitive advantage protecting a business's profits.
- **MoS (Margin of Safety):** the discount below fair value demanded before buying.
- **Net Debt/EBITDA:** a leverage ratio; this framework's primary balance-sheet-risk gate.
- **NOPAT:** Net Operating Profit After Tax — EBIT × (1 − effective tax rate).
- **PE (Price-to-Earnings) ratio / PEG ratio:** price ÷ earnings; PE ÷ growth rate.
- **pp (percentage points):** a direct difference between two percentages.
- **Quality Score:** this framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02.
- **Rate Environment Gate / Rate Regime Modifier:** the pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss); this framework requires ≥2:1.
- **ROIC:** Return on Invested Capital — NOPAT ÷ Invested Capital.
- **Shareholder yield:** dividend yield plus net buyback yield.
- **TAM:** Total Addressable Market.
- **Treasury yield (10Y):** the US government's 10-year borrowing rate, this framework's risk-free-rate benchmark.
- **TTM:** Trailing Twelve Months.
- **Turnaround Sub-Gate:** the conditional path letting a company failing some quality criteria still enter as a small position if it passes 5 specific tests.
- **Upside/Downside Modifier:** an additive ±15 valuation-score adjustment based on expected annual return.

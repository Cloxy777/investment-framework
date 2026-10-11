# RESCORE — CSGP (CoStar Group, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`) — **off-cycle**: no new filing since the last review. Q3 FY2026 earnings are 2026-10-27 (Yahoo calendar, 10-27). Run triggered manually to pick up (a) the **Zonda close** (Rule 9 M&A trigger), (b) the **10Y yield moving into the >5% band** (+5 → +10 regime modifier), (c) a fresh live price.
**Date:** 2026-10-11
**Last review:** Valuation 84.8 / Quality 69.2 / Composite 57.8 — 2026-08-09, [sessions/2026-08-09-rescore-csgp.md](2026-08-09-rescore-csgp.md). HOLD, Phase 04 Quality Watch.
**Portfolio weight:** 1.09% per [holdings.md](../portfolio/holdings.md) (well under the 15% cap).
**10Y US Treasury:** **5.244%** (Yahoo `^TNX`, 2026-10-11 pull; ties to the 5.26% in [2026-Q4 rate review](../sessions/quarterly/2026-Q4-rate-environment-review.md)).
**Data route:** `yfinance` worked this session (no `curl_cffi` failure); price cross-checked IBKR vs Yahoo.

> *Jargon decoded in the closing Glossary.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Price used** | **$29.72** | IBKR `get_price_snapshot` (contract 6726677) `last`, not halted; equals IBKR mark price |
| Cross-check | $29.67 | Yahoo `regularMarketPrice` / `fast_info` — within 0.2% |
| Prior close / change | $29.81 / −$0.09 (−0.3%) | IBKR |
| 52-week range | $25.89 – $79.08 | IBKR `misc_statistics` (13w high $33.82) |
| Analyst mean PT | $37.25 | Yahoo `targetMeanPrice` — sanity anchor only (was $37.10) |

Price vs 08-09 ($30.75): −3.3%. No Rule 9 price trigger (<15%).

## 2. Flags

1. **Zonda closed 2026-08-21** — $800M cash, from MidOcean; Zonda 2025 revenue ≈$170M at ~23% adj. EBITDA margin ([HousingWire](https://housingwire.com/articles/costar-zonda-acquisition-closes), [RISMedia 2026-08-21](https://www.rismedia.com/2026/08/21/costar-closes-on-800-million-zonda-acquisition/), [Commercial Observer](https://commercialobserver.com/?p=577414)). **Rule 9 trigger fired.** The 08-09 session flagged this as pending. The balance sheet is **not yet filed post-close** (latest filed = 2026-06-30), so the scored Balance Sheet / EV inputs stay on the filed Q2 figures — no estimate scored. A clearly-labelled **pro-forma sensitivity** is shown in §7 using only disclosed facts ($800M cash price; Zonda revenue × margin).
2. **10Y >5%** → Rate Regime Modifier steps up +5 → **+10**. Mechanical, not fundamental.
3. **No filing / guidance change since 07-28.** FY2026 adj. EBITDA guide $780–820M and buyback target unchanged; no news found for Sep–Oct 2026 (web search). Nasdaq-100 removal (2026-05-18) noted as already-known context.
4. **Forward EPS** now $1.77241 (Yahoo `forwardEps`; was $1.72529) → forward PE 16.77×.
5. **Same inputs as 08-09 for everything TTM-based** (Q2 FY26 is still the latest filed quarter; verified via quarterly statements: revenue $925.0M, EBIT $76.0M, NI $55.0M, FCF $57.0M, total debt $1,202M, cash $1,266M). 5yr PE history still unreconstructable → FwdPE 50.0 neutral fallback; PEG N/A (EPS not growing >15% on clean base) → weight to EV/EBIT.
6. Q3 buybacks, post-Zonda cash and financing (if any) are **unknown until the Q3 10-Q** — not estimated.

## 3. Inputs

| Item | Value |
|---|---|
| Shares | 405,197,588 |
| Market cap | 405.198M × $29.72 = **$12,042.47M** |
| Net cash (Q2 FY26, filed) | $1,266.0M − $1,202.0M = **+$64.0M** |
| EV | $12,042.47M − $64.0M = **$11,978.47M** |
| TTM revenue | $3,555.5M (Q3'25–Q2'26: 833.6 + 899.9 + 897.0 + 925.0) |
| TTM gross profit / margin | $2,797.6M / **78.68%** |
| TTM EBIT | **$77.0M** (−51.1 + 49.1 + 3.0 + 76.0) |
| TTM EBITDA | $394.0M |
| TTM net income / margin | $73.6M / **2.07%** |
| TTM pretax / tax | $101.1M / $27.5M → 27.20% |
| TTM FCF | **$227.0M** (−23.6 + 95.6 + 98.0 + 57.0). Yahoo's `info.freeCashflow` ($412.7M) is a different vendor calc; quarterly cash-flow statements used for consistency with prior sessions |
| Invested capital | $8,926.0M |
| Revenue FY2022→FY2025 | $2,182.4M → $3,247.0M; 3yr CAGR **14.16%** |

## 4. Quality Score (2026-06-29 methodology)

**Hard disqualifiers (rolling FY window FY2023–FY2025):**
- FCF/NI <70% for 2+ consecutive yrs: FY23 92.5% / FY24 −176.3% / FY25 585.7% → one dip only → ✅ pass
- Net debt/EBITDA: −0.162× (filed) → ✅ pass
- FCF-positive 3+ consecutive yrs: FY23 +$347M, **FY24 −$245M**, FY25 +$41M → ⚠️ **fires** (unchanged; clears only when FY2024 rolls out, i.e. after FY2027 completes FCF-positive)

**Sub-scores (inputs identical to 08-09 → results identical):**
```
Net margin component  = 2.07/30×100 = 6.90
NOPAT = 77.0×(1−0.2720) = 56.06; ROIC = 56.06/8,926 = 0.628% → component 2.09
Profitability = (6.90+2.09)/2 = 4.50
Margins   = 78.68/80×100 = 98.35 (trend mildly down, no bonus)
Growth    = 14.16/25×100 = 56.64 + 10 (TAM/pricing evidence, carried; Zonda close adds new-home TAM) = 66.64
BalSheet  = 100×(1−(−0.162)/4) → clamp 100.0   (filed Q2; see §7 sensitivity)
Moat      = 5/5 = 100.0   (all five signals carried from 08-09 citations — no new evidence either way; Rule 6 carry)
FCF qual  = FCF/NI 227.0/73.6 = 308% → clamp 100.0 (inflated by thin NI base, flagged)

Quality = 4.50×0.25 + 98.35×0.15 + 66.64×0.20 + 100×0.15 + 100×0.15 + 100×0.10
        = 1.125 + 14.753 + 13.328 + 15.0 + 15.0 + 10.0 = 69.206 → 69.2
```
**Quality 69.2 — FAILS 80.0+ gate** (weighted score + hard disqualifier). Phase 04 Quality Watch continues; not force-exited on quality alone.

## 5. Rate Environment Gate

- Step 1: forward PE = 29.72 ÷ 1.77241 = **16.77×**; EY = 5.964%; spread = 5.964 − 5.244 = **+0.72pp** < +1.5 → **+5**
- Step 2: 10Y 5.244% → ">5%" band → **+10**
- **Total rate modifier = +15** (was +10)

## 6. Valuation Score

```
FCF yield = 227.0 / 12,042.47 = 1.885%   → FCF_Score = 100×(1−0.1885) = 81.15   → ×0.40 = 32.46
EV/EBIT   = 11,978.47 / 77.0 = 155.6×     → clamp 100.0 (weight 25%+15% PEG = 40%) → 40.00
Fwd PE    = no 5yr history → 50.0 (flagged)                                      → ×0.20 = 10.00
PEG       = N/A (redistributed)
Raw weighted = 82.46
```
Upgrade 1 (Owner Earnings) does not trigger on TTM basis (CapEx $270M < D&A $317M), same as 08-09.

**Upside/Downside Modifier** — scenarios unchanged (guided targets unchanged; filed net cash $64M, 405.2M shares):

| Scenario | Wt | Norm. EBIT | EV/EBIT | FV/sh |
|---|---|---|---|---|
| Bull | 25% | $800M | 22× | $43.59 |
| Base | 50% | $650M | 20× | $32.24 |
| Bear | 25% | $450M | 16× | $17.93 |

```
PW FV = 0.25×43.59 + 0.50×32.24 + 0.25×17.93 = $31.50
Gap upside = 31.50/29.72 − 1 = +5.99%;  catalyst: Homes.com spend cut + EBITDA path to $1.25B FY28, 2yr window → +2.99%/yr
Intrinsic growth +12%/yr (unchanged, conservative vs 14.16% CAGR)
Shareholder yield +4.69%/yr (Q2'25→Q2'26 diluted share decline; carried, no newer share data until Q3)
E = 2.99 + 12.0 + 4.69 = 19.68%
M = −15 × clamp((19.68−10)/15, 0, 1) = −9.68
```
Guardrails: catalyst within 24 months ✓; PW (not rosy) ✓; bounded ±15 ✓.

```
FINAL VALUATION = 82.46 + 15 (rate) − 9.68 = 87.78 → 87.8
```

## 7. Zonda pro-forma sensitivity (NOT scored — shown for transparency)

Using only disclosed facts: −$800M cash; +Zonda EBITDA ≈ $170M × 23% ≈ $39M; scenario EBIT unchanged (conservative — ignores Zonda earnings); Q3 buybacks ignored (unknown).
- Net debt ≈ $736M; ND/EBITDA ≈ 736 / (394 + 39) = 1.70× → BalSheet ≈ 57.5 → Quality ≈ **62.8**
- PW FV falls by $800M/405.2M = $1.97 → ≈ $29.53; E ≈ 16.4% → M ≈ −6.4 → Valuation ≈ **91.1**
- Composite ≈ 0.5×(100−62.8) + 0.5×91.1 ≈ **64.1** → still HOLD band.

Read: the as-filed score understates the real Zonda cost; true post-close picture is probably somewhat less attractive, but still Hold. **Re-score properly on the Q3 10-Q (10-27).** Note the pro-forma valuation (~91) is at the edge of the 90–100 zone that, held 2+ consecutive quarters, is an exit trigger — watch it.

## 8. Composite and Action

```
Composite = 0.50×(100 − 69.2) + 0.50×87.8 = 15.4 + 43.9 = 59.3
```

| | Now | 08-09 |
|---|---|---|
| Valuation | **87.8** | 84.8 |
| Quality | **69.2** | 69.2 |
| Composite | **59.3** | 57.8 |

**Composite 59.3 → 50.0–69.9 band → HOLD** (no add, no trim). Raw Valuation alone (87.8) reads "Trim to 50%", but Composite governs. The +3.0 valuation move is almost entirely the rate modifier (+5): fundamentals inputs were unchanged and price fell 3.3%, which helped FCF yield and the upside modifier. No Phase 06 exit trigger: gross margin intact, revenue growth unbroken, Valuation has not held 90–100 for 2+ quarters. No order setup (HOLD).

## 9. Next Review Trigger

- **Q3 FY2026 earnings 2026-10-27** — full re-score. Specifically: post-Zonda balance sheet, cash and financing; buyback pace; bookings trend; FY26 FCF positive; Zonda contribution to revenue/EBITDA.
- Earlier on Rule 9: guidance revision, further management change, >15% unexplained move.
- Hard-disqualifier / Profitability re-check each quarter.

## Housekeeping
- Watchlist: [CSGP-2026-10-11.md](../watchlist/in-portfolio/CSGP/CSGP-2026-10-11.md) added (score changed; Rule 9 Zonda-close trigger). No STALE row existed for CSGP.
- [holdings.md](../portfolio/holdings.md) CSGP row updated: 87.8 / 69.2 / 59.3 / 11 Oct 2026.

## Glossary
Terms (see [glossary.md](../framework/glossary.md)): **Composite Score** (0.5×(100−Quality)+0.5×Valuation; lower = more attractive), **EBIT/EBITDA** (operating profit before interest & tax / also before depreciation & amortization), **EV** (market cap + net debt), **EY (Earnings Yield)** (1 ÷ forward PE), **FCF / FCF Yield** (free cash flow; FCF ÷ market cap), **Forward PE**, **Hard disqualifier** (quality condition failing a company regardless of weighted score), **Hurdle rate** (10%/yr), **NOPAT / ROIC** (after-tax operating profit; return on invested capital), **PEG**, **PW Fair Value** (25/50/25 bull/base/bear blend), **Quality Gate (80.0+)**, **Rate Regime Modifier / Rate Environment Gate** (adjustment for the 10-year Treasury yield level), **Rule 0 / Rule 9** (live-price rule / re-valuation triggers), **TAM** (total addressable market), **TTM** (trailing twelve months), **Upside/Downside Modifier** (±15 expected-return adjustment), **Zonda** (new-home construction data company CoStar bought for $800M cash).

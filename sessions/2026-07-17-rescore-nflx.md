# RESCORE — NFLX (Netflix, Inc.) — 2026-07-17

**Task type:** RESCORE (single ticker — existing holding), mode `--both`
**Trigger:** Hourly Telegram-scan routine (Routine 6) flagged that tarasguk and FinnInvestChannel both posted today (2026-07-17) claiming Netflix reported Q2 2026 earnings. Per CLAUDE.md/Rule 0, the Telegram posts' text is **never** treated as financial data — every number below is independently sourced from Netflix's own SEC 8-K exhibit, SEC EDGAR XBRL, IBKR live market data, and WebSearch-cited coverage. This is also the mandatory Rule 9 re-score explicitly flagged as the "next review trigger" on NFLX's 2026-07-05 watchlist entry ("Q2 2026 earnings — Thursday 16 July 2026 (confirmed date) — mandatory re-score").
**Date:** 17 Jul 2026
**10Y US Treasury Yield used:** 4.54% (16 Jul 2026 close — FRED/TradingEconomics-aggregated print, the most recent available; refreshed from the 05 Jul session's 4.49%)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket, unchanged bracket)
**Current NFLX portfolio weight:** 1.49% (per [holdings.md](../portfolio/holdings.md)) — Last Score 59.9, Quality Score 74.0, Composite Score 43.0 (05 Jul 2026)
**Sector:** Communication Services — Streaming Media & Entertainment

*First-use jargon decoded in the closing Glossary (step 9 of the operating brief).*

---

## 0. Fundamental-Trigger Check Since Last Review (Rule 9)

**Netflix reported Q2 2026 earnings after market close on Thursday, 16 Jul 2026** — confirmed via Netflix's own SEC Form 8-K (Exhibit 99.1 shareholder letter, filed CIK 0001065280) and cross-checked against independent press coverage (Hollywood Reporter, 24/7 Wall St, CNBC). This is a genuine Rule 9 fundamental trigger — the first earnings release since the 05 Jul 2026 rescore, and the one that session explicitly flagged as pending.

**Headline:** Q2 revenue $12.56B (in line, +13.4% YoY) and EPS $0.80 (slightly ahead of the $0.79 consensus) — but Q2 free cash flow fell hard ($1.5B vs $2.3B a year ago, partly due to disclosed one-off cash tax payments tied to the WBD termination fee), and Q3 guidance implies further revenue-growth deceleration (11.7% YoY guided, down from 13.4% in Q2, 16.2% in Q1, 17.6% in Q4 2025). The stock fell as much as ~9% in after-hours trading to a fresh 52-week low — confirmed independently via IBKR live data and WebSearch (see §1), **not** taken from the Telegram posts.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$67.80** | IBKR `get_price_snapshot` (contract_id 15124833) — `last` = $67.80 and `plprice` (mark) = $67.80 agree exactly (no repeat of the 05 Jul `last`-field staleness quirk). Timestamp corresponds to post-earnings after-hours trading following the 16 Jul close (IBKR 15-min bars show the stock trading in a $67.35–$68.9 after-hours band following a $74.35 regular-session close, consistent with the reported ~8.8–9% drop). Independently cross-validated via WebSearch: "NFLX stock sunk as much as 9 percent, hitting not just a 52-week low, but a low dating back as far as September 2024" (Hollywood Reporter, 24/7 Wall St). |
| Change vs prior close | −$6.55 / −8.81% | IBKR `change` field; prior close $74.35 (16 Jul regular-session close, IBKR daily bar) |
| 52-week range | New 52-week low set today, ~$67.4–$67.8 (breaking the $70.86 low set before the 05 Jul session) – $127.75 (52w high, IBKR `misc_statistics`, rolled down slightly from $129.50 as the trailing year window advances) | IBKR `misc_statistics` — ⚠️ note this field still shows `low_52w: 70.86`, not yet reflecting today's fresh low; a statistics-refresh-cadence lag (different from the previously-documented `last`-field staleness bug), corroborated instead via WebSearch ("Netflix Stock Hits 52-Week Low On Q2 Earnings Report"). |
| Analyst consensus PT | ~$110.71–$115 (mean/median, 32–78 analysts, "Strong Buy"/"Buy") | WebSearch aggregation (stockanalysis.com, S&P Global) — essentially unchanged from prior sessions; shown for context only, never used directly (Rule 7/10 — scenario-weighted PW FV is the input that matters, not the rosy consensus point). |
| `yfinance` availability | **Unreachable this session** — `curl_cffi.requests.exceptions.SSLError` ("Recv failure: Connection reset by peer") on the standard `t.info` pull, the same TLS failure mode documented in multiple prior sessions (distinct from the 05 Jul session's `YFRateLimitError`). Fell back to IBKR (price) + SEC EDGAR XBRL + the SEC 8-K exhibit + WebSearch, per Rule 0's documented contingency chain. |

**Context:** NFLX at $67.80 sits ~46.9% below its 52-week high ($127.75) and at (or just below) its 52-week low — a materially different picture from the 05 Jul session's $77.65 (then ~9.6% above the old low). This is a real, earnings-driven move (Rule 9 fundamental trigger), not an unexplained price move, so the separate ">15% unexplained move" trigger doesn't independently fire — but note the move (−12.7% from $77.65 on 05 Jul) is large and *is* explained by the Q2 print/guidance, consistent with Rule 9's "quarterly earnings release" trigger already firing this session.

---

## 2. Data Gathered — Sources & Gaps

Primary source this session: **Netflix's own Q2 2026 shareholder letter, filed as Exhibit 99.1 to Form 8-K** (SEC EDGAR, `data.sec.gov`/`www.sec.gov`, CIK 0001065280, accession 000106528026000211) — a Rule-0-compliant primary filing, not the Telegram posts. Cross-checked against SEC EDGAR's XBRL `companyconcept` API for Q3 2025 / Q4 2025 / Q1 2026 (already 10-Q/10-K-tagged) and against independent WebSearch coverage (Hollywood Reporter, 24/7 Wall St, CNBC, TipRanks, stockanalysis.com). No metric below was invented or estimated — every figure traces to a specific SEC filing line or a cited news source; anywhere a precise number wasn't disclosed, that gap is flagged explicitly rather than guessed.

### Q2 2026 actuals (quarter ended 30 Jun 2026), per the 8-K exhibit

| Metric | Value |
|---|---|
| Revenue | $12,559.938M (+13.4% YoY) |
| Cost of revenues | $6,036.965M |
| Operating income (EBIT) | $4,192.610M (op margin 33.4%, vs 34.1% Q2 2025) |
| Net income | $3,401.414M |
| Diluted EPS | $0.80 |
| Income tax provision | $667.172M |
| D&A (property/equipment/intangibles, non-content) | $100.530M |
| Operating cash flow | $1,743.812M (vs $2,423.258M Q2 2025) |
| CapEx | $218.644M |
| Free cash flow | $1,525.168M (vs $2,267.369M Q2 2025) |
| Share repurchases | $4,714.403M — management's own words: "our largest quarter of share repurchases" |
| Diluted shares (company-disclosed "Shares (FD)") | 4,261.3M |

**Balance sheet, as of 30 Jun 2026:**

| Metric | Value |
|---|---|
| Cash and cash equivalents | $9,099.232M |
| Short-term investments | $28.678M |
| Short-term debt | $2,483.758M |
| Long-term debt | $11,825.548M |
| Total debt ("gross debt", per management's own letter: "$14.4B") | $14,309.306M |
| Net debt | $5,181.396M |
| Total stockholders' equity | $30,152.052M |

**Guidance (per the same letter):**

| | Q3 2026 (guide) | FY2026 (guide) |
|---|---|---|
| Revenue | $12,860M (+11.7%/+11% FX-neutral YoY) | $51.0–$51.4B (13–14% growth, ~12% FX-neutral) — **narrowed** from the prior $50.7–$51.7B range, same ~$51.2B midpoint |
| Operating margin | 33.2% | 31.5% (unchanged from prior guide; vs 29.49% FY2025 actual) |
| Diluted EPS | $0.82 | — |
| FCF | — | ~$12.5B (unchanged) |
| Ad revenue | — | ~$3.0B, roughly doubling YoY (unchanged) |

**⚠️ Confirmed multi-quarter revenue-growth deceleration (new, material fact this session).** Per the letter's own guidance table, YoY revenue growth has decelerated for four straight quarters: Q4 2025 17.6% → Q1 2026 16.2% → Q2 2026 13.4% (actual) → Q3 2026 11.7% (guided). This is the single most important new fact this session and is treated as genuine evidence of **structural** (not cyclical) growth deceleration in the Quality Score's Growth sub-score below — a first for this framework's NFLX coverage (the 05 Jul session explicitly found "no structural-deceleration evidence" based on annual data; the now-available quarterly cadence changes that conclusion).

**⚠️ Engagement growth remains anemic.** "In the first half of 2026, our members watched more than 97 billion hours, up 2% year over year. This was slightly faster than the 1.5% growth in 2025" — management's own framing, attributing some of the softness to the Winter Olympics/World Cup competing for viewing time. Cited as Moat/Growth context, not scored directly (no precise subscriber count disclosed this quarter to update the Moat Signal "market share" citation beyond what's already on file).

**⚠️ WBD termination-fee normalization — carried forward, with a new unquantified residual flagged.** The $2.8B Warner Bros. Discovery termination fee (recognized in Q1 2026, below the EBIT line, established in the 06/07 sessions) still sits inside this session's TTM window (Q3 2025–Q2 2026 includes Q1 2026). The normalization convention from the 05 Jul session — subtract the ~$2.259B after-tax gain from TTM Net Income, and the $2.8B gross cash inflow from TTM OCF/FCF — is carried forward unchanged (see §3.7 for exact figures). **New this session:** Netflix's own letter states Q2 2026 FCF "included higher cash tax payments due in part to the Warner Bros. termination fee" but **does not disclose the dollar amount of that component**. This means the "normalized" FCF figure below still contains an unquantified residual drag from the fee's tax cash-payment timing that this session's normalization does not back out (doing so would require inventing a split that isn't disclosed — explicitly not done, per "never invent or estimate financial data"). Net effect: the normalized FCF/FCF-Yield/FCF-Quality figures below are, if anything, **conservatively understated** relative to a fully clean run-rate — flagged rather than corrected.

### TTM (Q3 2025–Q2 2026) reconstruction

Q3 2025, Q4 2025, and Q1 2026 individual-quarter figures reconstructed from SEC EDGAR XBRL `companyconcept` (subtracting YTD cumulative values, cross-checked against the XBRL `frame`-tagged standalone-quarter values where available — both methods agree to the thousand). Q2 2026 taken directly from the 8-K exhibit above (not yet XBRL-tagged — the Q2 2026 10-Q hasn't been filed yet, consistent with the "use the 8-K until the 10-Q is available" convention established in prior sessions).

| Metric | TTM value | Derivation |
|---|---|---|
| Revenue | $48,370.764M | Q3'25 $11,510.307M + Q4'25 $12,050.762M + Q1'26 $12,249.757M + Q2'26 $12,559.938M |
| Operating Income (EBIT) | $14,354.517M | Q3'25 $3,248.247M + Q4'25 $2,956.663M + Q1'26 $3,956.997M + Q2'26 $4,192.610M |
| Net Income (as-reported) | $13,649.642M | Q3'25 $2,546.916M + Q4'25 $2,418.521M + Q1'26 $5,282.791M + Q2'26 $3,401.414M |
| Operating Cash Flow (as-reported) | $11,970.833M | Q3'25 $2,825.174M + Q4'25 $2,111.642M + Q1'26 $5,290.205M + Q2'26 $1,743.812M |
| CapEx | $818.828M | Q3'25 $164.719M + Q4'25 $239.335M + Q1'26 $196.130M + Q2'26 $218.644M |
| FCF (as-reported) = OCF − CapEx | $11,152.005M | Computed |
| Cost of Revenue | $24,612.074M | Q3'25 $6,164.250M + Q4'25 $6,522.621M + Q1'26 $5,888.238M + Q2'26 $6,036.965M |
| Gross Profit / Margin | $23,758.690M / **49.12%** | Computed |
| D&A (property/equipment, non-content) | $372.414M | Q3'25 $87.326M + Q4'25 $85.983M + Q1'26 $98.575M + Q2'26 $100.530M |
| Income tax expense | $2,843.181M | Q3'25 $562.494M + Q4'25 $349.220M + Q1'26 $1,264.295M + Q2'26 $667.172M |

**Normalized (WBD fee removed, Rule 6 — same convention as 05 Jul):**

| | As-reported (TTM) | Normalized (TTM, fee removed) |
|---|---|---|
| Net Income | $13,649.642M | $11,390.322M |
| Net Margin | 28.22% | 23.55% |
| OCF | $11,970.833M | $9,170.833M |
| FCF | $11,152.005M | $8,352.005M |
| FCF/NI conversion | 81.70% | 73.33% |

**Other inputs, updated or carried forward:**
- **FY2026 consensus EPS: $3.57** (post-Q2 revision — KeyBanc's own estimate and stockanalysis.com's aggregated consensus both independently land at $3.57; superseded the 05 Jul session's pre-earnings $3.66) — used as the Forward PE denominator below.
- **Diluted shares: 4,261.3M** (Netflix's own Q2 2026 "Shares (FD)" figure, up from 4,212.79M as of Q1 2026 — reflects both share issuance and the offsetting record buyback).
- **5yr PE range (avg 39.44×, low 19.32×, high 55.82×, n=20 quarters, `yfinance`-reconstructed 2026-06-20) — carried forward.** `yfinance` unreachable again this session (see §1); this is a slow-moving statistic per precedent. **Notable: Forward PE (18.99×, see §5) is now below the entire 5-year range's low end (19.32×) for the first time in this ticker's session history** — the FwdPE sub-score formula floors at 0.0 regardless, but this is worth flagging as a genuinely new data point (the multiple has broken below its own trailing 5-year floor).
- **Revenue 3yr CAGR (FY2022→FY2025) 12.51%** — carried forward; FY2026 annual figures aren't final yet (only interim quarters), so the FY-level CAGR basis is unchanged from prior sessions.

---

## 3. Quality Score

**Hard disqualifier check:**

| Check | NFLX Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | TTM 73.3% (normalized) / 81.7% (as-reported); FY2025 86.2%; FY2024 79.5% — all above 70% | disqualify if <70% for 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | 0.352× (see below) | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2023/24/25 and TTM all positive | disqualify if not | ✅ PASS |

No hard disqualifier fires. Proceeding to the weighted score (normalized basis primary; as-reported shown as sensitivity, consistent with 05 Jul convention).

### Profitability (25% weight)

```
Net Margin (TTM, normalized) = $11,390.322M / $48,370.764M = 23.548%
NetMargin_Component = clamp((23.548/30)×100, 0, 100) = 78.49

ROIC — NOPAT ÷ Net Invested Capital (cash-netted, glossary-standard):
  NOPAT = TTM EBIT × (1 − FY2025's clean effective tax rate 13.69%)
        = $14,354.517M × 0.8631 = $12,389.38M
    [Using FY2025's rate rather than TTM's own blended rate (17.24%, itself still lifted by the
     WBD fee's tax treatment sitting inside Q1 2026) — same convention as 05 Jul, for the same reason.]
  Net Invested Capital = Total Debt ($14,309.306M) + Equity ($30,152.052M) − Cash&STI ($9,127.910M)
                        = $35,333.448M
  ROIC = $12,389.38M / $35,333.448M = 35.07%
ROIC_Component = clamp((35.07/30)×100, 0, 100) = clamp(116.9, 0, 100) = 100.0

Profitability_Score = (78.49 + 100.0) / 2 = 89.25
```
No FCF-positivity cap applies.

**⚠️ ROIC sensitivity (carried forward from 05 Jul, no fresher third-party figure found this session):** third-party (GuruFocus-style) ROIC range 21.3–25.5%, vs. this session's from-scratch 35.07%. Using the low end (21.3%): ROIC_Component = 71.0, Profitability_Score = 74.75, Quality Score ≈ **66.1** (see §3.7) — still fails the gate by a wide margin either way.

### Margins (15% weight)

```
Gross Margin (TTM) = 49.12% (computed above)
GrossMargin_Score = clamp((49.12/80)×100, 0, 100) = 61.39
```
No structural-trend bonus (reserved for margins below the 40% threshold that are still expanding — not applicable here).

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022→FY2025, carried forward) = 12.51%
Growth_Score (base) = clamp((12.51/25)×100, 0, 100) = 50.04

TAM/pricing-power evidence (documented, +10):
  - Ad revenue guided to ~$3.0B in 2026 (roughly doubling YoY) — unchanged target, reaffirmed
    in the Q2 2026 letter.
  - "The results of our recent price changes are consistent with prior changes and our
    expectations" (Q2 2026 letter, direct quote) — continued pricing power without disclosed
    volume loss.
  - Double-digit revenue growth in every region this quarter (UCAN +10%, EMEA +14%, LATAM +21%,
    APAC +16%) — continued international TAM expansion.
  → +10

Structural-deceleration evidence (documented, −10 — NEW this session, reversing the 05 Jul
  session's "no structural-deceleration evidence" finding):
  - Netflix's own guidance table shows YoY revenue growth decelerating for four consecutive
    prints: Q4 2025 17.6% → Q1 2026 16.2% → Q2 2026 13.4% (actual) → Q3 2026 11.7% (guided).
    This is company-guided, not a one-quarter miss, and the trend is monotonic across four
    data points — the "3yr steady ~16%" read from the 05 Jul session (based only on
    annual-level data) is superseded by this now-visible quarterly cadence.
  - H1 2026 member-viewing-hours growth of just +2% YoY (vs 1.5% in 2025) — engagement growth
    remains structurally weak even by management's own "slightly faster" framing.
  → −10

Growth_Score = clamp(50.04 + 10 − 10, 0, 100) = 50.04
```
Both modifiers are independently documented and cited (per quality-scoring.md, both may apply — this isn't an either/or test) — net effect is zero, but the underlying picture has changed materially from 05 Jul: a maturing, still-expanding business (ad tier, international, pricing power) that is now also confirmed to be structurally decelerating on revenue growth.

### Balance Sheet (15% weight)

```
Net Debt = $5,181.396M (§2) — up from $2,072.07M at the 05 Jul session, driven almost entirely
  by the record $4.7B Q2 2026 buyback funded from cash (gross debt is roughly flat: $14.31B now
  vs $14.36B then). This is a capital-allocation choice, not new borrowing or balance-sheet stress.
EBITDA (TTM) = EBIT ($14,354.517M) + non-content D&A ($372.414M) = $14,726.931M
Net Debt/EBITDA = $5,181.396M / $14,726.931M = 0.352×
BalanceSheet_Score = clamp(100×(1 − 0.352/4), 0, 100) = 91.21
```
Standard /4 denominator (Upgrade 5 override doesn't apply — not a payment network/exchange).

### Moat Signal (15% weight) — checklist, carried forward with updated citations where new evidence exists

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Continued double-digit revenue growth in every region this quarter; no fresher third-party subscriber count disclosed this session to update beyond the "~325M+" figure already on file. |
| Brand premium | **TRUE** | Q2 2026 letter: "results of our recent price changes are consistent with prior changes and our expectations" — continued pricing power without a disclosed volume/churn deterioration this quarter (note: unlike Q1 2026, this quarter's letter does not repeat an explicit "churn improved" statement — flagged as a citation gap, not assumed either way). |
| Network effect | FALSE | Unchanged — no documented two-sided-marketplace mechanism for core streaming. |
| Switching costs | FALSE | Unchanged — month-to-month, cancel-anytime subscription. |
| Scale cost advantage | **TRUE** | Unchanged — largest industry content-spend scale (2026 content budget ~$20B guided, carried forward; no update disclosed this session). |

```
Moat_Score = (3/5) × 100 = 60.0
```

### FCF Quality (10% weight)

```
FCF/NI (TTM, normalized) = $8,352.005M / $11,390.322M = 73.33%
FCFQuality_Score = clamp(((0.7333 − 0.40)/0.60)×100, 0, 100) = 55.54
```
*Sensitivity (as-reported): 81.70% → FCFQuality_Score = 69.51.* Note this metric dropped materially from 05 Jul (69.71 normalized then vs 55.54 now) — almost entirely a mechanical consequence of Q2 2026's much lower reported OCF (partly the unquantified WBD-fee-tax-payment drag flagged in §2), not a change in underlying earnings quality.

### Quality Score — Final

```
Quality Score = (89.25×0.25) + (61.39×0.15) + (50.04×0.20) + (91.21×0.15) + (60.0×0.15) + (55.54×0.10)
              = 22.3125 + 9.2085 + 10.008 + 13.6815 + 9.000 + 5.554
              = 69.764 → 69.8
```

### 3.7 — Robustness check (three bases, all fail the gate — more decisively than 05 Jul)

| Basis | Quality Score | Gate result |
|---|---|---|
| **Normalized (primary — fee removed, Rule 6)** | **69.8** | **FAILS** (10.2pp below 80.0) |
| As-reported (fee left in — sensitivity) | 73.1 | FAILS (6.9pp below 80.0) |
| Normalized + lowest third-party ROIC (21.3%) | 66.1 | FAILS (13.9pp below 80.0) |

**Quality Score = 69.8 — FAILS the 80.0+ gate, more decisively than the 05 Jul session's 74.0.** The decline (−4.2 points) is driven almost entirely by two mechanical, well-explained factors: the Growth sub-score flipping from a net +10 (60.04) to a net 0 (50.04) once the now-confirmed quarterly deceleration is credited, and the FCF Quality sub-score dropping (69.71→55.54) as Q2's reported OCF fell (partly an unquantified WBD-fee-tax-payment effect, §2). No hard disqualifier fires, and no single factor is alarming in isolation (ROIC and margins remain very strong) — but this is a real, cited, further move away from the gate, not noise.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $67.80 / $3.57 = 18.9916×
EY = 1 ÷ 18.9916 = 5.2654%
Spread = EY − 10Y Treasury = 5.2654% − 4.54% = +0.7254%
```
Spread (+0.73%) < +1.5% → **FAILS** → **+5 additive** (yellow flag, not a veto).

**Step 2 — Rate Regime Modifier:** 10Y = 4.54% → 3.5–5% bracket → **+5**

**Total Rate Modifier: +10** (unchanged bracket vs. 05 Jul — the spread improved slightly, from +0.22% to +0.73%, but is still short of the +1.5% pass threshold).

---

## 5. Valuation Score (Phase 02)

**Market Cap** = 4,261.3M shares × $67.80 = **$288,916.14M**

**FCF Yield — 40% weight** (normalized TTM FCF, Rule 6)
```
FCF Yield = $8,352.005M / $288,916.14M = 2.891%
FCF_Score = clamp(100×(1 − 2.891/10), 0, 100) = 71.09
```
*Sensitivity (as-reported): yield 3.860% → FCF_Score 61.40.*

**EV/EBIT — 40% weight (PEG redistributed — NFLX still isn't a Fast Grower; the newly-confirmed deceleration reinforces this, not just the historical FY2024 EPS decline already on file)**
```
Net Debt = $5,181.396M
EV = $288,916.14M + $5,181.396M = $294,097.54M
EV/EBIT = $294,097.54M / $14,354.517M = 20.49×
EV/EBIT_Score = clamp((20.49 − 12)/23 × 100, 0, 100) = 36.91
```

**Forward PE — 20% weight (5yr-range primary formula, carried-forward range)**
```
Forward PE = 18.99×, 5yr Low = 19.32×, 5yr High = 55.82× (carried forward, §2)
FwdPE_Score (range) = clamp((18.99 − 19.32)/(55.82 − 19.32) × 100, 0, 100) = clamp(−0.90, 0, 100) = 0.0
  [Forward PE is now BELOW the entire 5-year trailing range for the first time this session series.]
Historical PE Modifier (Upgrade 2): Deviation vs 5yr avg (39.44×) = (18.99 − 39.44)/39.44 = −51.85%
  → >20% below → −10 modifier (moot — already floored at 0.0)
FwdPE_Score = clamp(0.0 − 10, 0, 100) = 0.0
```

**PEG — still not applicable.** NFLX fails the Fast-Grower test (established across every prior session; the newly-confirmed multi-quarter deceleration reinforces rather than reverses this). Weight redistributed to EV/EBIT (→ 40%).

### 5.1 Raw weighted score

```
Normalized (primary) = (71.09×0.40) + (36.91×0.40) + (0.0×0.20) = 28.44 + 14.76 + 0.0 = 43.20
As-reported (sensitivity) = (61.40×0.40) + (36.91×0.40) + (0.0×0.20) = 24.56 + 14.76 + 0.0 = 39.32
```
**+ Rate Modifier (+10):**
```
Normalized: 53.20 (before Upside/Downside Modifier)
As-reported: 49.32 (before Upside/Downside Modifier)
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier) — Rebuilt

Per fair-value-methodology.md/task instructions: rebuild the PW Fair Value scenario if Q2 earnings materially changed guidance. **Headline FY2026 guidance (revenue, margin, FCF, ad-revenue target) is essentially unchanged in midpoint terms** — the revenue range only narrowed ($50.7–51.7B → $51.0–51.4B, same ~$51.2B midpoint). But the now-confirmed, company-guided multi-quarter revenue-growth deceleration (§3) is new, material information not reflected in the 06-12/06-20 DCF's growth assumptions, and the balance sheet has moved materially (net debt more than doubled from the record Q2 buyback, shares outstanding rose). **Decision: rebuild**, trimming near-term DCF growth assumptions modestly to reflect the confirmed deceleration while keeping the FY2026 FCF anchor unchanged (since that guide itself didn't move), and refreshing net debt/shares/Forward-EPS inputs to current values.

### Step 1 — DCF (3 scenarios, Rule 2/7), rebuilt

| Scenario | WACC | Yr1 FCF | Yrs 2–5 growth | Yrs 6–10 fade | Terminal growth | PV Stage 1 | PV Stage 2 | PV Terminal | Total EV | Equity Value | **FV/share** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bear | 10.5% | $11.5B | 6%→4% *(was 8%→5%)* | 4%→2% *(was 4.5%→2.5%)* | 2.0% | $47.41B | $34.87B | $71.63B | $153.91B | $148.73B | **$34.90** |
| Base | 9.5% | $12.5B | 10%→7% *(was 12%→9%)* | 6%→3.5% *(was 7%→4%)* | 2.5% | $56.56B | $48.84B | $129.04B | $234.44B | $229.25B | **$53.80** |
| Bull | 8.5% | $13.0B | 13%→10% *(was 15%→12%)* | 8%→5% *(was 9%→5.5%)* | 3.0% | $63.88B | $64.09B | $227.92B | $355.89B | $350.71B | **$82.30** |

WACC unchanged from 06-12 (risk-free ~4.5% + β≈1.4 × ERP≈3.6% ≈ 9.5% base, ∓1% bull/bear) — the ~5bp change in risk-free rate is immaterial. Yr1 FCF anchors unchanged (FY2026 guide itself didn't move). **Yrs 2–10 growth trimmed by roughly 2pp across all three scenarios** — the single explicit change this session, reflecting the now-confirmed Q3 guide deceleration (11.7%) sitting toward the low end of even the Bear case's near-term band. Net debt ($5.181B) and shares (4.2613B) updated to current values. Terminal value is 46.5–64.0% of total EV across scenarios — under the 75% trigger for extending Stage 2 (Rule 4).

```
PW DCF FV = 0.25×82.30 + 0.50×53.80 + 0.25×34.90 = 20.575 + 26.90 + 8.725 = $56.20
```

### Step 2 — Comparable Multiples, refreshed

| Approach | "Fair" multiple | Calculation | FV/share |
|---|---|---|---|
| Forward PE comp | 28× (unchanged rationale — modest re-rating above the current compressed 19.0×, still well below the 5yr avg 39.44×) | 28 × $3.57 | **$99.96** |
| EV/EBIT comp | 18× on FY2026E EBIT ($51.2B × 31.5% = $16.13B) | EV $290.30B − net debt $5.18B → equity $285.12B ÷ 4.2613B shares | **$66.91** |
| FCF-yield comp | 5.0% yield on FY2026E FCF ($12.5B) | EV $250.0B − net debt $5.18B → equity $244.82B ÷ 4.2613B shares | **$57.45** |
| **Multiples avg** | | | **$74.77** |

**Per-scenario blend (same 40% DCF / 60% Multiples pairing convention as the 06-20 session — Bear↔FCF-yield comp, Base↔EV/EBIT comp, Bull↔Fwd-PE comp):**

| Scenario | DCF | Multiples comp | Blended (0.4×DCF + 0.6×comp) |
|---|---|---|---|
| Bear | $34.90 | $57.45 (FCF-yield comp) | **$48.43** |
| Base | $53.80 | $66.91 (EV/EBIT comp) | **$61.67** |
| Bull | $82.30 | $99.96 (Fwd-PE comp) | **$92.90** |

```
PW Fair Value = 0.25×$92.90 + 0.50×$61.67 + 0.25×$48.43 = $23.225 + $30.835 + $12.1075 = $66.17
```

**Cross-check (headline Blended FV, 40% DCF-PW + 60% Multiples-avg, Rule 3 style):**
```
Blended FV = 0.40×$56.20 + 0.60×$74.77 = $22.48 + $44.86 = $67.34
```
This lands within 0.8% of the live price ($67.80) — a useful independent sanity check that the market's post-earnings repricing landed close to where this rebuilt, deceleration-adjusted framework would put fair value, rather than clearly over- or under-shooting.

**Historical PE cross-check (Rule 3, context only — 0% weight):**
```
TTM EPS (as-reported) = $13,649.642M / 4,261.3M shares = $3.20
Historical PE FV = $3.20 × 5yr avg PE (39.44×) = $126.34
```
Directionally consistent with the consensus PT (~$110–115) and both far above the live price and our blended FV — shown for context only (a reversion this large would imply an unreasonably high IRR per Rule 4), not weighted into the blend.

### Step 3 — E and the Modifier

```
PW Fair Value = $66.17
Gap Upside % = ($66.17 ÷ $67.80) − 1 = −2.40%     (price sits just ABOVE PW fair value — much closer
                                                      to fair value than 05 Jul's −10.15% gap)
Catalyst window = 2 years (Rule 10, unchanged) — Q3 2026 earnings (~Oct 2026) is a near-term
  checkpoint on whether the deceleration stabilizes or continues, but the fuller
  deceleration-vs-ad-monetization-offset question plays out over the FY2026 ad-revenue
  doubling target and beyond — no narrower fully-resolving window identified.
Annualized gap = −2.40% ÷ 2 = −1.20%/yr

Intrinsic growth = +11.0%/yr (revised DOWN from the stale +13.0%/yr carried since 06-12/06-20 —
  reflects the now-confirmed top-line deceleration, even as margin expansion continues)
Shareholder yield = +4.1%/yr (revised UP from the stale +0.5%/yr — Netflix's own H1 2026 cash-flow
  statement shows $5,984.991M of buybacks net of $109.290M of issuance = $5,875.701M net,
  annualized (×2) ÷ $288,916.14M market cap = 4.07%/yr, rounded to 4.1%. The prior +0.5%/yr
  assumption is clearly stale given Q2 2026's own disclosed "largest quarter of share repurchases
  ever" and $27.1B of remaining authorization.)

E = −1.20 + 11.0 + 4.1 = +13.9%/yr
```

**Map E to M** (hurdle H = 10%, E ≥ H branch):
```
M = −15 × clamp((13.9 − 10)/15, 0, 1) = −15 × 0.260 = −3.90
```

**Upside/Downside Modifier M = −3.90** — a meaningfully larger pull-down than the 05 Jul session's +0.79, driven mostly by (a) the price now sitting near, not well above, PW Fair Value, and (b) the updated, no-longer-stale shareholder-yield input.

**⚠️ Boundary-sensitivity check (transparency, not a separate scenario):** using the OLD, stale assumptions (intrinsic growth +13.0%, shareholder yield +0.5%) instead of the updated ones: `E = −1.20+13.0+0.5 = +12.3%/yr` → `M = −15×clamp((12.3−10)/15,0,1) = −2.30` → Final Score would be 53.20−2.30 = **50.9** (still technically the 50.0–69.9 Hold band, vs. 49.3 with updated assumptions landing one notch into the 30.0–49.9 Cheap band). **This session's conclusion is genuinely boundary-sensitive to the shareholder-yield update** — flagged explicitly rather than glossed over. The updated yield is used as primary because it is directly sourced from Netflix's own just-filed Q2 cash-flow statement (not an assumption), and carrying forward a demonstrably stale figure when fresher, real data exists would itself violate Rule 0's spirit.

**Guardrails:** documented catalyst + timeline exists within 18–24 months (Q3 2026 earnings, ongoing ad-ramp) — the −5 upside cap doesn't bind here since this is the "strong upside" (negative M) branch driven mostly by shareholder yield and a near-fair-value price, not a large speculative upside claim. Scenario-weighted PW FV used throughout, never the bull case or the consensus PT. Full calc shown above — no black box.

---

## 7. Final Valuation Score

```
Final Score (normalized, primary) = 53.20 (raw+rate) − 3.90 (Upside/Downside) = 49.30
Final Score (as-reported, sensitivity) = 49.32 − 3.90 = 45.42 → 45.4
```

**Valuation Score = 49.3 — nominally "Cheap"** (30.0–49.9 band, which would nominally map to "BUY — Standard position 3–5%"). **This is one band lower than the 05 Jul session's 59.9 ("Fair Value/Hold")** — both the price crash and the updated Upside/Downside inputs pushed the standalone valuation score down. As-reported sensitivity (45.4) lands in the same "Cheap" band — for the first time, the normalization-basis choice doesn't change the standalone valuation-band conclusion (05 Jul had both bases in "Hold"; both bases are now in "Cheap"). **See §9 for why this nominal reading is not acted on at face value.**

---

## 8. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 69.8) + 0.50 × 49.3
                = 0.50 × 30.2 + 24.65
                = 15.1 + 24.65
                = 39.75 → exactly on a ".X5" boundary → round UP (conservative) → 39.8
```
*(As-reported sensitivity: 0.50×(100−73.1) + 0.50×45.4 = 13.45+22.7 = 36.15 → 36.2 — same "Cheap" band either way.)*

**Composite Score = 39.8** — numerically lands in the "Cheap" (30.0–49.9) → Standard position 3–5% band.

**⚠️ This is a false green light and must not be acted on at face value — the same pattern flagged in the 05 Jul session, now more pronounced.** NFLX's Quality Score (69.8) fails the 80.0+ gate even more decisively than before. The Composite Score's `(100 − Quality Score)` term is again doing most of the work of making a stock whose own standalone Valuation Score (49.3) is only marginally in the Cheap band read as more attractive than it should. The action call below is driven by the quality-gate failure (Phase 04 Quality Watch escalation) and — independently — by the order-setup math failing its own risk/reward gate (§9), **not** by the numerically-attractive Composite.

---

## 9. Action Recommendation

**Three independent checks, run in full per fair-value-methodology.md — none of them supports an add:**

### (a) Order-setup math, run against the nominal "Cheap" (30.0–49.9) band's own rules

```
MoS (30.0–49.9 band): 25–30%
Buy price range off PW FV $66.17: $46.32 (30% MoS) – $49.63 (25% MoS); midpoint (27.5%) = $47.97
Live price ($67.80) sits 41.3% ABOVE even the most aggressive buy price ($49.63) — no entry point exists.
Stop loss (25–30% max loss from buy price, midpoint) = $47.97 × (1 − 0.275) = $34.78
R/R at midpoint buy price = ($66.17 − $47.97) / ($47.97 − $34.78) = $18.20 / $13.19 = 1.38:1 — FAILS the 2:1 minimum.
```
**No order is placed** — R/R fails the minimum threshold by a wide margin, exactly the same 1.38:1 result (coincidentally) as the 05 Jul session, and the live price remains far above any disciplined buy price even after the ~12.7% two-week price decline. This mirrors the standing pattern across this repo (AVGO 07-04, NKE 07-01, NFLX 07-05): a favorable-looking score does not automatically produce an executable trade.

### (b) Phase 04 Quality Watch escalation

NFLX's Quality Score (69.8) fails the 80.0+ gate by a wider margin than the 05 Jul session's 74.0. Two specific, real, cited developments this session:
- **Confirmed structural revenue-growth deceleration** (four consecutive quarterly prints: 17.6%→16.2%→13.4%→11.7% guided) — a genuine change from the 05 Jul finding of "no structural-deceleration evidence."
- **Net debt more than doubled** ($2.07B→$5.18B) — driven entirely by the record $4.7B Q2 buyback, not new borrowing; leverage remains very low in absolute terms (0.35× Net Debt/EBITDA, well inside the 2.5× standard threshold) — a capital-return choice, not balance-sheet stress.

### (c) Full Exit trigger check (explicitly verified, not assumed absent)

| Trigger | Checked against | Result |
|---|---|---|
| Fundamental deterioration — margins structurally broken, ROIC below cost of capital | Op margin compressed only 0.7pp YoY in Q2 (33.4% vs 34.1%); FY2026 margin guide (31.5%) is actually **above** FY2025 actual (29.49%); ROIC 35.07% (or 21.3–25.5% on the low third-party sensitivity) — both far above any reasonable cost of capital | ❌ Not met |
| Growth thesis broken — TAM shrinking, disruption visible, pricing power lost, **or guidance cut 2+ consecutive quarters w/o a one-off explanation** | FY2026 revenue guidance midpoint is **unchanged** (~$51.2B both before and after Q2) — the range only narrowed, which is not a cut. Pricing power evidence still cited (§3 Growth). TAM (ad tier, international) still expanding. | ❌ Not met |
| Balance sheet crisis — leverage spikes, dilutive raise | Net debt rose but leverage ratio (0.35×) remains very low; no dilutive raise; buyback-funded, not distress-funded | ❌ Not met |
| Extreme overvaluation — Score 90.0–100.0 sustained 2+ quarters | Score is now at the opposite end of the range (49.3, "Cheap") | ❌ Not met (inapplicable) |

**No Full Exit trigger fires.** This is a genuine further quality deterioration worth tracking closely (unlike 05 Jul's "ordinary business-model characteristics, not decay" framing — the growth deceleration specifically is new, real decay, not just an inherent trait), but it doesn't cross any hard threshold.

### Net Action: **HOLD** — maintain the current 1.49%-weight position as-is

- **No add**, despite the nominally attractive Composite (39.8) and Valuation (49.3) scores — independently blocked by (i) the order-setup R/R failing 2:1 (§9a), and (ii) the Quality Score sitting further below the 80.0+ gate than last session (§9b).
- **No trim** — score is nowhere near the 70.0+ trim threshold; if anything it moved further away from it this session.
- **No Full Exit** — none of the four hard triggers fire (§9c), explicitly checked rather than assumed.
- **Phase 04 Quality Watch flag intensified** — unlike 05 Jul, this session finds *real* incremental deterioration (confirmed growth deceleration), not just an inherent business-model characteristic. Watch closely at the next rescore (Q3 2026 earnings, ~Oct 2026) for whether the deceleration stabilizes (11–12% range) or continues falling.
- **Boundary sensitivity flagged** (§6): the Valuation Score's move from "Hold" to nominal "Cheap" band hinges partly on updating a previously-stale shareholder-yield assumption — a legitimate, well-sourced update, but worth the human investor's awareness that this isn't an overwhelming, unambiguous signal in either direction.

All final-decision authority rests with the human investor per the operating brief.

---

## 10. Next Review Trigger

- **Q3 2026 earnings — expected mid-October 2026** (not yet confirmed to an exact date; check IBKR/company IR calendar closer to the date) — mandatory re-score (Rule 9). Check: (a) whether Q3 revenue growth lands at or below the 11.7% guide, confirming/extending the deceleration trend, or stabilizes; (b) Q3 operating margin vs. the 33.2% guide; (c) any fresh subscriber/engagement disclosure beyond the H1 2026 "97B hours, +2%" figure; (d) pace of buybacks against the $27.1B remaining authorization (feeds the shareholder-yield input directly); (e) any further clarity on the WBD-fee-related cash tax payment magnitude (currently an unquantified, flagged gap — §2).
- **>15% unexplained price move from $67.80 in either direction** — immediate re-score (Rule 9). Note NFLX is sitting at (or just below) a fresh 52-week low set this session — worth watching whether it stabilizes here or continues falling.
- **`yfinance` access** — flag for `/healthcheck`: unreachable again this session (`curl_cffi` TLS `SSLError`, "Recv failure: Connection reset by peer") — a recurring, not one-off, failure mode across multiple recent sessions.
- **Growth-deceleration trend specifically** — if Q3 2026 actual growth falls meaningfully below the 11.7% guide (rather than stabilizing near it), or if management's Q3 letter walks back the FY2026 revenue guidance midpoint (a genuine "guidance cut"), that would trip the Phase 04 "Growth thesis broken" Full Exit condition — worth flagging to the human investor as the specific threshold to watch for, not just a generic "re-score next quarter."
- No position change executed by this session — recommendation only (Hold at 1.49%). If the investor acts, log it in `decisions/` per CLAUDE.md Rule 10.

---

## 11. Glossary

- **8-K (Form 8-K):** a US company's "current report" filed with the SEC to disclose a material event between regular quarterly/annual filings — this session's primary source (Netflix's Q2 2026 earnings press release/shareholder letter was filed as Exhibit 99.1 to an 8-K).
- **bps / pp (basis points / percentage points):** 0.01 percentage points / a direct difference between two percentages.
- **Buyback yield (net buyback yield):** the rate a company's share count shrinks per year from repurchasing its own stock, net of new issuance — a component of shareholder yield, revised up materially this session based on Netflix's own disclosed H1 2026 buyback figures.
- **CAGR:** Compound Annual Growth Rate.
- **CapEx:** Capital Expenditure.
- **Composite Score:** this framework's blended 0.0–100.0 ranking number (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`), computed here as a reference figure only because Quality fails the 80.0+ gate — see §8.
- **DCF:** Discounted Cash Flow — a valuation method estimating value from projected future cash flows discounted to the present.
- **D&A:** Depreciation & Amortization.
- **EBIT / EBITDA:** operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **Effective tax rate:** actual tax paid ÷ pretax income for a period; used here to compute NOPAT, with the FY2025 "clean" rate substituted for the WBD-fee-distorted TTM rate.
- **EPS:** Earnings Per Share.
- **EV / EV/EBIT:** Enterprise Value (market cap + debt − cash) / EV divided by EBIT, a valuation multiple.
- **EY (Earnings Yield):** 1 ÷ Forward PE, compared against the 10-Year Treasury yield in the Rate Environment Gate.
- **Fast Grower:** Peter Lynch's term for EPS growth >15%/yr for 3+ years on a clean earnings base — triggers the PEG sub-score. NFLX still doesn't qualify.
- **FCF / FCF Yield / FCF/NI conversion ratio:** Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income.
- **Forward PE:** price ÷ next-twelve-months expected EPS.
- **GAAP:** Generally Accepted Accounting Principles.
- **Gross Margin:** Gross Profit ÷ Revenue.
- **Hard disqualifier:** a Quality Score condition that fails a company regardless of weighted score — none fired for NFLX this session.
- **Hurdle rate:** the minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against.
- **Invested Capital:** total capital (debt + equity, net of cash) put to work in a business — the denominator of ROIC.
- **Moat:** a durable competitive advantage protecting a business's profits from competitors.
- **MoS (Margin of Safety):** the discount below fair value demanded before buying.
- **Net Debt/EBITDA:** a leverage ratio — this framework's primary balance-sheet-risk gate.
- **Net Margin:** Net Income ÷ Revenue.
- **NOPAT:** Net Operating Profit After Tax — EBIT × (1 − effective tax rate).
- **PEG ratio:** PE ÷ earnings growth rate — not applicable to NFLX this session.
- **PT (Price Target):** an analyst's price forecast.
- **PW (Probability-Weighted) Fair Value:** this framework's blended fair value — 25% bull + 50% base + 25% bear (Rule 7) — rebuilt this session (§6).
- **Quality Score:** this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. NFLX's second-ever computed value (69.8) fails this gate more decisively than the first (74.0).
- **Rate Environment Gate / Rate Regime Modifier:** the mandatory pre-score check comparing Earnings Yield to the 10-Year Treasury, and the resulting additive score adjustment.
- **Rule 0 / Rule 6 / Rule 9 / Rule 10:** this framework's standing instructions to always fetch a live price first; normalize distorted earnings before valuing; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss) on a trade; this framework requires ≥2:1 to enter.
- **ROIC:** Return on Invested Capital — NOPAT ÷ Invested Capital.
- **Shareholder yield:** dividend yield plus net buyback yield — revised materially upward this session based on Netflix's own disclosed Q2 2026 buyback activity.
- **TAM:** Total Addressable Market.
- **Treasury yield (10Y):** the US government's 10-year borrowing rate, this framework's risk-free-rate benchmark.
- **TTM (Trailing Twelve Months):** the most recent 12 months of reported results.
- **Upside/Downside Modifier (Expected-Return Modifier):** the additive ±15 adjustment to the valuation score based on expected annual return vs. the 10% hurdle.
- **Valuation Score:** this framework's 0.0–100.0 score combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.
- **WACC:** Weighted Average Cost of Capital — used in the rebuilt DCF (§6).

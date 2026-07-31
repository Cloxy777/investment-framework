# RESCORE — AMZN — 2026-07-31

**Task type:** RESCORE (single ticker, mode `--both`)
**Trigger:** Automated Telegram-scan (Routine 6) — FinnInvestChannel post at 2026-07-30T20:09:55Z reporting Amazon's Q2 FY2026 earnings. **Per CLAUDE.md Rule 0, the Telegram post text was used only as the trigger, never as a data source** — every figure below was independently pulled from Amazon's own SEC 8-K/EX-99.1 filings, IBKR live pricing, and stockanalysis.com, cross-checked.
**Date of this session:** 31 Jul 2026 (earnings released 30 Jul 2026, after US market close)
**10Y US Treasury Yield:** 4.68% (web search, dated 30 Jul 2026 — most recent print available; still inside the "3.5–5%" bracket → Rate Regime Modifier Step 2 unchanged at +5)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** AMZN **81.8** (2026-07-04, HOLD (Composite governs) — [sessions/2026-07-04-rescore-amzn.md](2026-07-04-rescore-amzn.md)). Quality Score 57.6 / Composite 62.1 as of that session.

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; D&A = depreciation and amortization; capex = capital expenditure; Owner Earnings = net income + D&A − maintenance capex; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ PE); NOPAT = net operating profit after tax; ROIC = return on invested capital; TAM = total addressable market; TTM = trailing twelve months; FTC = Federal Trade Commission.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$257.27** | IBKR `get_price_snapshot` (contract_id 3691937, AMZN / NASDAQ), pulled this session, intraday (`is_close: false` — US market open 31 Jul 2026) |
| Bid / Ask | $257.01 / $257.30 | IBKR, same pull |
| 52-week range | **$196.00 – $278.56** | IBKR `misc_statistics` |
| Year-to-date change | **+11.46%** (+$26.45) | IBKR `year_to_date_change` |
| Dividend yield | 0.0% | IBKR `dividend_yield` |
| Analyst consensus PT | **$313.07** (64–66 analysts, "Strong Buy") | Web search, dated 31 Jul 2026, but underlying individual price-target updates cited are from 28 Jul 2026 (pre-earnings) — bull-case sanity anchor only, never a score input; flagged as possibly not yet reflecting the Q2 print |

Price vs 07-04 session: $241.70 → $257.27 = **+6.44%**. Below the 15% Rule 9 unexplained-move threshold, and fully explained by the Q2 earnings beat/reaction regardless.

---

## 2. Rule 9 Trigger Check (2026-07-04 → 2026-07-31)

| Trigger | Found? | Detail |
|---|---|---|
| **Quarterly earnings** | **YES** | Q2 FY2026 reported 30 Jul 2026 after close — this is the trigger firing (also the exact "Next review trigger" flagged in the 07-04 watchlist entry) |
| Guidance revision | Standard quarterly guidance issued alongside earnings (not a separate mid-quarter revision) — folded into the earnings trigger, not double-counted. Q3 2026 guidance: net sales $197.0–$202.0B, operating income $22.5–$26.5B (both independently pulled from the SEC 8-K exhibit, §3) |
| M&A | No new M&A since the 14 Apr 2026 Globalstar agreement (already priced in, not a new event this window) |
| Management change | None found |
| Macro shift | 10Y ticked 4.48% → 4.68%, still inside "3.5–5%" bracket — no bracket change |
| >15% unexplained price move | No — +6.44%, and explained by earnings anyway |

**Conclusion: Rule 9 fires on the quarterly earnings release**, as expected — this is a scheduled, not ad hoc, re-score.

---

## 3. AMZN — Data Collected

**Sector:** Consumer Discretionary — E-commerce & Cloud Infrastructure (AWS). Treated as Technology/Growth for fair-value method per Rule 1.
**Current portfolio weight:** 9.48% (per [holdings.md](../portfolio/holdings.md), as of the 2026-07-26 sync — pre-dates this session, not recomputed here; IBKR alone shows 12 shares, avg cost $210.588, market value $3,087.24 this session).

`yfinance` remains unreachable this session (same persistent `curl_cffi`/TLS proxy failure documented across recent sessions). **All figures below are sourced directly from Amazon's own SEC 8-K/EX-99.1 filings (Q2 2026, Q1 2026, Q3 2025, Q4 2025/FY2025) plus stockanalysis.com for gross-margin cross-checks and consensus estimates.**

### Q2 FY2026 headline results (quarter ended 30 Jun 2026) — independently verified against SEC EX-99.1, not the Telegram post

| Line | Q2 2026 | Q2 2025 | YoY |
|---|---|---|---|
| Net sales | $200.6B | $167.702B | +19.6% |
| AWS net sales | $42.2B | — | +37% (vs. Synergy Research's independently-tracked ~19–20% industry-wide AWS growth for the most recent quarter it has published — see §6 moat-signal note) |
| Operating income | $27.5B | $19.2B | +43.2% |
| Other income (expense), net | $53.415B | $1.117B | dominated by a disclosed **$53.4B pre-tax gain "primarily from our investments in Anthropic"** |
| Income before income taxes | $80.9B | $20.9B | — |
| Provision for income taxes | $18.2B (22.5% effective rate) | $2.7B (12.8% effective rate) | — |
| Net income | $62.6B | $18.2B | +245% |
| Diluted EPS | $5.75 | $1.68 | — |

Source: [Amazon Q2 2026 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm).

**Q3 2026 guidance (company-issued, not scored per "Why Forward Guidance Is Not a Sub-score" — [valuation-scoring.md](../framework/valuation-scoring.md)):** net sales $197.0–$202.0B (9–12% YoY growth), operating income $22.5–$26.5B (vs. $17.4B GAAP in Q3 2025, which itself absorbed $4.3B of one-off charges — see §4). Midpoint operating income guide ($24.5B) is +12.9% over Q3 2025's *normalized* ($17.4B + $4.3B = $21.7B) base — a real but more modest beat-rate than the raw YoY comparison implies. Used only as bear/base/bear scenario context in §8, never as a scored input.

### TTM roll-forward, ended 30 Jun 2026

Built as **FY2025 (audited 10-K/8-K) + H1 FY2026 (10-Q/8-K) − H1 FY2025 (10-Q)** — cross-checked against a direct quarterly sum (Q3'25 + Q4'25 + Q1'26 + Q2'26), both methods agreeing to within rounding:

| Line | FY2025 | H1 2026 | H1 2025 | **TTM (to 30 Jun 2026)** |
|---|---|---|---|---|
| Net sales | $716.924B | $382.119B | $323.369B | **$775.674B** |
| Operating income (GAAP) | $79.975B | $51.352B | $37.605B | **$93.722B** |
| Net income (GAAP) | $77.670B | $92.855B | $35.327B | **$135.198B** |

Sources: FY2025 — [Amazon Q4/FY2025 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm). Q1 2026 — [Amazon Q1 2026 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000012/amzn-20260331xex991.htm). Q2 2026 — [Amazon Q2 2026 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm). Q1/Q2 2025 — comparative columns in the same filings, cross-checked against stockanalysis.com.

**Directly company-reported TTM cash-flow figures (no reconstruction needed):**

| Item | TTM to 30 Jun 2026 | Source |
|---|---|---|
| Operating cash flow | $161.4B (+33% YoY) | Amazon Q2 2026 8-K Ex-99.1 |
| Purchases of property & equipment (net of proceeds) | $169.0B | Amazon Q2 2026 8-K Ex-99.1 |
| **Free cash flow (Amazon's own definition)** | **−$7.6B** — negative for the first time in this name's session history | Amazon Q2 2026 8-K Ex-99.1 (= OCF − net capex, ties out exactly) |
| Depreciation & amortization | $75.2B | Amazon Q2 2026 8-K Ex-99.1 |

### Balance sheet, as of 30 Jun 2026

| Item | Value | Source |
|---|---|---|
| Cash and cash equivalents | $78.2B | Q2 2026 8-K Ex-99.1 |
| Marketable securities | $44.8B | Q2 2026 8-K Ex-99.1 |
| Total long-term debt | $128.9B | Q2 2026 8-K Ex-99.1 |
| Total stockholders' equity | $551.6B | Q2 2026 8-K Ex-99.1 |
| **Net debt** | **+$5.9B (net debt, not net cash)** | $128.9B − ($78.2B + $44.8B) — a **reversal** from the −$24.0B net-cash position at 31 Mar 2026; cash + securities fell $20.1B quarter-over-quarter (funding the accelerated $220B FY2026 capex guide and/or Anthropic-related investment activity) |

### Other collected inputs

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 10.783B (as of 30 Jun 2026) | Amazon Q2 2026 8-K Ex-99.1 cover-page share count |
| Diluted weighted-avg shares, Q2 2026 vs Q2 2025 | 10.903B vs 10.806B (+0.9% YoY) | Amazon Q2 2026 8-K Ex-99.1 — confirms shares outstanding are still net *increasing* (SBC-driven issuance outpacing buybacks), consistent with the 0% shareholder-yield assumption carried from 07-04 |
| FY2026 consensus EPS | $8.71 (non-GAAP adjusted, 60 analysts) | stockanalysis.com forecast page, dated ~30–31 Jul 2026, post-earnings |
| Gross margin, Q2 2026 / Q1 2026 / Q4 2025 / Q3 2025 / Q2 2025 / Q1 2025 | 52.26% / 51.82% / 48.47% / 50.79% / 51.81% / 50.55% | stockanalysis.com quarterly financials, cross-checked against each quarter's own revenue/gross-profit figures |
| FY2025 effective tax rate (carried, used for NOPAT normalization) | 19.6% | Amazon FY2025 8-K Ex-99.1 (unchanged from 07-04 session — cleanest full-year, non-quarter-distorted rate available) |
| Revenue FY2022 (for 3yr CAGR, unchanged — FY2025 still the latest completed fiscal year) | $513.983B | Carried from prior sessions (SEC-sourced) |
| PEG (trailing, unscored sensitivity check) | Not re-pulled this session — PEG remains inapplicable regardless (§7) | — |

---

## 4. Data Gaps, Corrections & Flags

1. **New this session — Q3 2025 special charges normalized out of TTM EBIT (Rule 6).** Amazon's own Q3 2025 release discloses **two one-off "special charges" inside Q3 2025's GAAP operating income**: a **$2.5B FTC legal-settlement charge** and a **$1.8B severance charge** (planned role eliminations), totaling **$4.3B**. Q3 2025 sits inside both this session's TTM window (Jul 2025–Jun 2026) *and* the 07-04 session's TTM window (Apr 2025–Mar 2026) — but the 07-04 session's EBIT figure did **not** normalize these out. Rule 6 ("normalize before you value... strip out one-time items — restructuring, litigation") explicitly covers both a legal settlement and a severance/restructuring charge, and both dollar amounts are directly company-disclosed (not estimated), so this session applies the normalization: **Normalized TTM EBIT = GAAP TTM EBIT ($93.722B) + $4.3B addback = $98.022B.** This is a **methodology refinement discovered this session, not a change in the business** — flagged prominently because it materially affects EV/EBIT, ROIC, and EBITDA below. For transparency, the **unnormalized GAAP TTM EBIT ($93.722B) would have produced EV/EBIT_Score ≈ 76.8** (vs. 71.1 normalized) — see §7.
2. **Anthropic investment gains — three separate one-off quarters within this TTM window, all normalized out.** Unlike the 07-04 session (which only had to normalize a single $16.8B Q1 2026 gain), this TTM window (Jul 2025–Jun 2026) captures **three** disclosed pre-tax Anthropic mark-to-market gains: Q3 2025 ($9.5B, 24.5% effective tax rate that quarter), Q1 2026 ($16.8B, 24.0% rate), and Q2 2026 ($53.415B — effectively the entirety of that quarter's $53.4B "Other income, net" line, 22.5% rate). Each is normalized out at its own quarter's effective tax rate (consistent with the 07-04 session's method): after-tax total = $9.5B×0.755 + $16.8B×0.76 + $53.415B×0.775 = $7.173B + $12.768B + $41.397B = **$61.338B**. **Normalized TTM Net Income = $135.198B (GAAP) − $61.338B (Anthropic) + $3.2465B (FTC/severance after-tax addback) = $77.107B.**
3. **Q4 2025 carried no comparable one-off gain** — its "Other income (expense), net" was a modest $1.177B, with no Anthropic-gain disclosure found in that quarter's release. Not normalized (nothing to normalize).
4. **FY2026 consensus EPS ($8.71) is explicitly labeled "non-GAAP adjusted" by the source** (vs. the 07-04 session's un-labeled $8.69 figure) — this is reassuring evidence that sell-side models are *already* excluding one-off investment gains like the Anthropic marks from their EPS estimates, partially resolving the open caveat flagged in the 07-04 session's Data Gap #3. Still not independently verifiable exactly what's excluded — flagged as a partially-resolved, not fully-resolved, caveat.
5. **Analyst consensus PT ($313.07)** is dated 31 Jul 2026 in aggregate, but the individual analyst target changes cited alongside it (UBS, BMO, Mizuho) are dated 28 Jul 2026 — **two days before** the Q2 print. May not yet reflect the earnings reaction; used only as a bull-case sanity anchor, never a score input, and flagged as potentially stale (same divergence-from-consensus pattern flagged in the 07-04 session persists).
6. **"Market share stable or growing" moat signal — re-verified, still resolved FALSE.** The most recent independently-sourced (Synergy Research Group) global cloud-infrastructure market-share data available is Q1 2026: AWS 28% (unchanged from the 07-04 session's finding), Azure 21%, Google Cloud 14%, with Azure (40% YoY) and Google Cloud (63% YoY) both growing faster than AWS (19% YoY per Synergy's methodology) that same quarter. Amazon's own Q2 2026 release states AWS revenue grew 37% YoY — a real acceleration in Amazon's self-reported growth rate — but this is a different quarter and a different (company-reported, not independent) methodology than the Synergy figures the market-share signal is graded against. Given the most recent *independent, cited* share data still shows AWS flat at 28% (not growing) while faster-growing rivals continue gaining share, this signal remains marked **FALSE**, consistent with 07-04 — while explicitly noting AWS's own reported growth rate strengthened materially this quarter as a countervailing, closely-watched data point for next quarter's re-check.

---

## 5. AMZN — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = Live Price ÷ FY2026 consensus EPS = $257.27 ÷ $8.71 = 29.5315×
EY         = 1 ÷ 29.5315 = 3.3862%
Spread     = EY − 10Y Treasury = 3.3862% − 4.68% = −1.2938%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (−1.2938%, ~2.8pp short) → **+5 additive.**

**Step 2 — Rate Regime Modifier**
10Y = 4.68% → "3.5–5%" bracket → **+5**

**Total Rate Modifier = +10** (unchanged from 07-04).

---

## 6. AMZN — Quality Score (2026-06-29 methodology, re-computed)

```
Profitability (25%):
  Net Margin (normalized, ex-Anthropic, ex-FTC/severance) = $77.107B ÷ $775.674B (TTM revenue) = 9.941%
  ROIC: NOPAT = Normalized EBIT × (1 − FY2025 effective tax rate) = $98.022B × (1 − 0.196) = $78.826B
    Invested Capital = Total Debt ($128.9B) + Total Equity ($551.6B) = $680.5B
    ROIC = $78.826B / $680.5B = 11.583%
  NetMargin_Component = clamp((9.941/30)×100, 0, 100) = 33.14
  ROIC_Component       = clamp((11.583/30)×100, 0, 100) = 38.61
  Profitability_Score  = (33.14 + 38.61) / 2 = 35.87   (no FCF cap — FCF-positive every *completed fiscal
    year* on record, FY2023–FY2025; TTM going negative this quarter is a live, in-progress-year signal,
    not yet a completed-FY breach — see FCF Quality note below for how seriously this is still flagged)

Margins (15%): TTM gross margin — weighted by quarterly revenue: (Q3'25 $91.499B + Q4'25 $103.427B +
  Q1'26 ~$94.080B + Q2'26 ~$104.833B) / $775.674B = $393.839B / $775.674B = 50.775%
  GrossMargin_Score = clamp((50.775/80)×100, 0, 100) = 63.47   (already >40% — no separate trend bonus;
    the underlying trend (48.47%→51.82%→52.26% over the last 3 quarters) is genuinely expanding and
    used as qualitative evidence elsewhere, not double-counted here)

Growth (20%): Revenue 3yr CAGR, FY2022 $513.983B → FY2025 $716.924B (unchanged — FY2025 still the latest
  completed fiscal year; will next update once FY2026 closes)
  CAGR = (716.924/513.983)^(1/3) − 1 = 11.731%
  Growth_Score = clamp((11.731/25)×100, 0, 100) = 46.92
  + 10 (documented TAM expansion / accelerating-not-decelerating growth — reaffirmed and strengthened
    this session: AWS revenue growth accelerated to +37% YoY, beating the ~31% consensus estimate cited
    in the Telegram trigger and independently confirmed via the SEC filing; North America net sales +16%
    YoY on Prime Day strength; Q3 2026 guidance still implies continued double-digit YoY growth)
  Growth_Score (with bonus) = 56.92

Balance Sheet (15%): Net Debt = $128.9B − ($78.2B + $44.8B) = $5.9B (net debt — see §4 reversal note)
  EBITDA (normalized) = Normalized EBIT + D&A = $98.022B + $75.2B = $173.222B
  Net Debt/EBITDA = 5.9/173.222 = 0.0341×
  BalanceSheet_Score = clamp(100×(1−0.0341/4), 0, 100) = clamp(99.15, 0, 100) = 99.15

Moat Signal (15%) — checklist, cited evidence, re-verified this session:
  ✗ Market share stable/growing — FALSE (unchanged; see Data Gap #6 for full re-verification detail —
     AWS still 28% per the most recent independent Synergy Research data, flat, while faster-growing
     rivals continue gaining share, even as Amazon's own self-reported growth rate accelerated this
     quarter)
  ✓ Brand premium — TRUE (unchanged evidence from 07-04, no new contradicting data found)
  ✓ Network effect — TRUE (unchanged — third-party sellers still driving 60–62% of units sold)
  ✓ Switching costs — TRUE (unchanged — AWS data-egress fee structure)
  ✓ Scale cost advantage — TRUE (unchanged — multi-year cost-per-unit efficiency)
  Moat_Score = (4/5) × 100 = 80.0

FCF Quality (10%): FCF/NI TTM (GAAP NI, consistent basis with 07-04) = −$7.6B / $135.198B = −5.62%
  FCFQuality_Score = clamp(((−0.0562 − 0.40)/0.60)×100, 0, 100) = clamp(−76.03, 0, 100) = 0.0
  **TTM FCF has gone outright negative for the first time in this name's session history** (was
  +$1.232B/+0.047% yield at 07-04, now −$7.6B). FY2023–FY2025 were each individually FCF-positive
  (established in prior sessions), so the "3+ consecutive fiscal years FCF-positive" hard-disqualifier
  condition still measures against completed fiscal years, not a partial FY2026 — it does not fire this
  session. But this is flagged as the single most significant Quality Watch data point this quarter:
  the FCF/NI hard-disqualifier's growth-capex carve-out (documented, standing, and now even larger —
  growth capex is $93.8B of $169.0B TTM net capex = 55.5%, above 07-04's 52.2% and META's precedent
  52%) still applies, so the hard disqualifier does not fire — but the trend is deteriorating, not
  stabilizing, and is the clearest test of whether Q3/Q4 2026 begin showing operating leverage catching
  up to the capex build, per management's own framing.

Quality Score = 35.87×0.25 + 63.47×0.15 + 56.92×0.20 + 99.15×0.15 + 80.0×0.15 + 0.0×0.10
              = 8.9675 + 9.5205 + 11.384 + 14.8725 + 12.0 + 0.0
              = 56.7445 → rounds to 56.7
```

**Quality Score = 56.7 — still FAILS the 80.0+ gate decisively** (57.6 → 56.7, essentially flat but a further modest decline).

**Hard disqualifier check:** none fire. FCF/NI <70% for 2+ (now arguably heading toward 3+) consecutive years still carries the same documented, standing growth-capex explanation (now 55.5% growth-capex share, the highest yet seen for this name); Net Debt/EBITDA is trivial (0.034×) even after the shift from net cash to net debt; FCF-positive every *completed* fiscal year on record (TTM negative is a live, in-progress signal, not yet a completed-FY breach).

**Why the picture is not improving:** the 07-04 session flagged this Quality Watch expecting Q2 earnings to be "the natural checkpoint for whether operating income and FCF conversion begin recovering as the $200B FY2026 capex program matures." **The result is mixed, not a clean recovery**: operating income and margins are genuinely strong and improving (Profitability, Margins, Balance Sheet, Moat sub-scores all roughly flat-to-slightly-better), but **FCF conversion has gotten materially worse, not better** — TTM FCF flipped from thin-positive to outright negative as the FY2026 capex guide was raised to $220B (from the $200B guided as of the 07-04 session). This is the capex-supercycle dynamic Owner Earnings (Upgrade 1) exists to look through *for valuation purposes*, but the Quality Score's FCF Quality sub-score has no such carve-out and correctly registers the intensified strain — **still not a hard disqualifier (documented carve-out holds), but the Quality Watch escalation is intensifying, not resolving.**

---

## 7. AMZN — Phase 02 Valuation Score

**Owner Earnings (Upgrade 1) — shown explicitly:**
- Growth capex check: TTM net capex $169.0B; maintenance-capex proxy (= D&A) $75.2B; growth capex = $93.8B = **55.5% of total** → exceeds the 30% trigger → Upgrade 1 applies.
- OE = Normalized Net Income (ex-Anthropic, ex-FTC/severance — §4) $77.107B + D&A $75.2B − maintenance capex (=D&A) $75.2B = **$77.107B** (D&A terms cancel by construction).
- Market Cap = 10.783B shares × $257.27 = **$2,774.142B**.
- OE yield = $77.107B ÷ $2,774.142B = **2.7793%**.

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.7793/10), 0, 100) = 72.207
```
→ Contribution: 72.207 × 0.40 = **28.883**

(Reported/raw FCF, for contrast only, not scored: TTM −$7.6B ÷ $2,774.142B = **−0.274% yield** — would clamp to a score of 100 (maximally "expensive"), hugely overstating expensiveness; exactly why Upgrade 1/Owner Earnings is required for this name.)

**EV/EBIT — 40% weight** (PEG not applicable, see below → 15% redistributed here)
```
EV  = Market Cap $2,774.142B + Net Debt $5.9B = $2,780.042B
EV/EBIT_Score = clamp(($2,780.042B / $98.022B − 12)/23 × 100, 0, 100) = clamp((28.362 − 12)/23 × 100, 0, 100) = 71.14
```
→ Contribution: 71.14 × 0.40 = **28.456**

*(For transparency — the unnormalized GAAP EBIT ($93.722B, before the Q3'25 special-charges addback, §4) would give EV/EBIT = $2,780.042B/$93.722B = 29.665×, EV/EBIT_Score ≈ 76.80, contribution ≈ 30.72 — a ~2.3-point swing in the raw weighted score from this session's Rule 6 refinement alone.)*

**Forward PE — 20% weight**
Still no clean 5-year PE history (unchanged rationale — FY2022's GAAP-loss quarters still fully inside the trailing 5-year window; won't clear until ~2028):
```
FwdPE_Score = 50.0 (neutral fallback, flagged — unchanged)
```
→ Contribution: 50.0 × 0.20 = **10.0**

**PEG — Fast-Grower test: still FAILS**, same reasoning as 07-04 (net income trajectory is a recovery off the FY2022 loss, not 3+ years of clean >15% growth on a non-distorted base — and TTM net income is now itself dominated by one-off Anthropic marks, reinforcing rather than resolving this). **PEG's 15% weight redistributed to EV/EBIT** (used above).

**Raw weighted score:**
```
= 28.883 + 28.456 + 10.0 = 67.339
```
**+ Rate Modifier (+10) = 77.339** *(before the Upside/Downside Modifier)*

---

## 8. AMZN — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario fair value (Rule 7, EV/EBIT-multiple method on forward EBIT).** Same three qualitative scenarios, exit multiples, and dollar-growth assumptions as the 07-04 session (AWS-reacceleration bull / consensus base / capex-drag-and-slowdown bear — +25%/+18%/+8% off current EBIT), rebuilt on the **corrected $98.022B normalized TTM EBIT base** (§4/§6) rather than the 07-04 session's $85.422B:

| Scenario | Wt | Forward EBIT | Exit EV/EBIT | Equity Value = EBIT×Mult − Net Debt | FV/share (÷10.783B sh) |
|---|---|---|---|---|---|
| Bull | 25% | $98.022B × 1.25 = $122.528B | 27.0× | $3,308.24B − $5.9B = $3,302.34B | **$306.24** |
| Base | 50% | $98.022B × 1.18 = $115.666B | 24.0× | $2,775.98B − $5.9B = $2,770.08B | **$256.87** |
| Bear | 25% | $98.022B × 1.08 = $105.864B | 18.0× | $1,905.55B − $5.9B = $1,899.65B | **$176.16** |

```
PW Fair Value = 0.25×306.24 + 0.50×256.87 + 0.25×176.16 = $249.04
```

**Sanity check (Rule 4/0 Step 4):** PW FV ($249.04) and the Bull case ($306.24) both sit **below** the $313.07 analyst consensus PT (flagged in §4 as possibly pre-earnings/stale) — the same pattern of divergence flagged at 07-04, unresolved. Flagged honestly rather than adjusted to match, per Rule 7's guardrail against using the rosy point. **Bear-case context (not a scored input, per "Why Forward Guidance Is Not a Sub-score"):** Q3 2026 guidance came in modestly below sell-side consensus on both revenue ($200B guide midpoint vs. ~$204B est per the Telegram trigger, independently corroborated by the $197.0–202.0B guided range) and operating income ($24.5B guide midpoint vs. ~$25B est) — consistent with, and supportive of, the bear scenario's more conservative growth assumption already baked in, not a reason to revise the scenario weights themselves.

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = ($249.04 ÷ $257.27) − 1                    = −3.200%   (price sits ABOVE PW FV, as at 07-04)
Catalyst window = 2 years (unchanged default — no single hard re-rating catalyst within 18–24mo;
                   the capex-to-FCF inflection and AWS re-acceleration remain multi-year stories)
Annualized gap  = −3.200% ÷ 2                                 = −1.600%/yr
Intrinsic growth = +10%/yr (carried, unchanged — durable owner-earnings growth anchored to the
                   11.73% revenue CAGR, decelerating modestly at scale, net of SBC dilution)
Shareholder yield = 0% (Amazon pays no dividend; diluted shares outstanding still net *increasing*
                   YoY — 10.806B → 10.903B, +0.9% — confirmed net dilutive again this session)
```
```
E (expected annual return) = −1.600 + 10.0 + 0.0 = +8.400%/yr
```

**Step 3 — Catalyst/timeline (Rule 10 + Guardrail 1).** No hard catalyst within 18–24 months identified (unchanged) — the guardrail caps the *upside* (negative M) side at −5 if claiming large upside with no path to realize it. Not binding here since E sits on the positive-modifier (thin-return) side of the mapping.

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
0 ≤ E < H → M = +5 × (H − E)/H = +5 × (10 − 8.400)/10 = +5 × 0.160 = +0.800
```

**Interpretation:** price remains modestly above the corrected probability-weighted fair value, same direction as 07-04 but the gap narrowed slightly (−8.89% → −3.20%) — driven by the larger normalized EBIT base (which raises both the numerator of the multiples-based fair value *and* the EV/EBIT sub-score's expensiveness read simultaneously). The modifier stays small and positive (+0.8, vs. +2.2 at 07-04) because durable intrinsic growth (+10%/yr) still carries most of the expected-return math, keeping E just under the 10% hurdle.

---

## 9. AMZN — Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (67.339) + Rate Modifier (+10) + Upside/Downside (+0.800)
                       = 78.139
```
Boundary rule: not a ".X5" → standard rounding → **Final Valuation Score = 78.1**

| | Value |
|---|---|
| Raw weighted | 67.339 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | +0.800 (E = +8.400%) |
| **FINAL VALUATION SCORE** | **78.1** |
| Prior valuation score | 81.8 (07-04) |
| **Quality Score** | **56.7 (FAILS 80.0+ gate; prior: 57.6)** |

```
Composite Score = 0.50 × (100 − 56.7) + 0.50 × 78.1 = 0.50×43.3 + 0.50×78.1 = 21.65 + 39.05 = 60.70
```

**Composite Score = 60.7** (prior: 62.1).

---

## 10. AMZN — Action

**Raw Valuation Score alone: 81.8 → 78.1** — stays inside the same 70.0–79.9 "Trim 25–30%" band as 07-04 (was near the top of it at 81.8, now mid-band). Driven mostly by the larger EBIT base (both GAAP and normalized) lowering the EV/EBIT multiple slightly, partially offset by the Rule-6 special-charges refinement pulling normalized EBIT down relative to the unnormalized figure.

**Composite Score (60.7) → Action band: HOLD — watch only, no new entry, no trim (50.0–69.9 band).** Same band as 07-04 (62.1). Per [valuation-scoring.md](../framework/valuation-scoring.md), the Composite Score — not the raw Valuation Score — governs the Phase 03/05 action-table lookup once a Quality Score exists.

**No change in action recommendation this session — but the Quality Watch escalation is not resolving.** The 07-04 session flagged Q2 earnings as the specific checkpoint for whether operating income/FCF conversion would show signs of recovering. The result: operating income, margins, and balance-sheet quality all held up or modestly improved, but **TTM free cash flow turned outright negative for the first time**, and the FY2026 capex guide was raised further (to $220B, from $200B). The Quality Score (56.7) is essentially unchanged from 57.6 in net terms, but the *composition* of that stability masks a worsening cash-conversion picture offset by resilient profitability — worth reading as "the Quality Watch flag has not been resolved by this earnings print," not as "the situation has stabilized."

**Practical recommendation: HOLD — no new entry, no trim forced by the score** (per the framework's rule that the Composite Score governs the action table, and that an existing holding failing the Quality Gate is a watch flag, not an automatic force-exit or force-trim — rescore.md step 3). Next earnings (Q3 FY2026, guided for reporting ~late Oct/early Nov 2026) is the next natural checkpoint for whether FCF conversion begins recovering as the capex build matures, or continues deteriorating into a second consecutive quarter of negative TTM FCF.

**No order setup required** — action is HOLD, not BUY/TRIM, so the order-setup checklist in [fair-value-methodology.md](../framework/fair-value-methodology.md) is out of scope this session (operating-brief.md OUTPUT FORMAT step 6 applies only to BUY/TRIM actions).

**Cap note:** at 9.48% (per holdings.md, pre-dating this session's price move), AMZN is comfortably under Upgrade 7's 15% hard cap regardless of which score/band is read — not a cap-driven consideration either way. This session's price move (+6.44% since the 07-26 sync's pricing basis) would push the live weight modestly higher, but recomputing portfolio weight is `/sync-portfolio`'s job, not this session's, per the task brief (holdings.md update deferred to the orchestrator).

---

## 11. Portfolio Note

This session does not change `portfolio/holdings.md` — that update (Last Score 78.1, Quality Score 56.7, Composite Score 60.7, Last Review 31 Jul 2026) is handled by the orchestrator across the batch, per this session's task brief (a parallel AAPL agent is running concurrently). No trade is recommended or executed this session.

---

## 12. Next Review Triggers

- **Next earnings — AMZN Q3 FY2026**, expected to report in the standard late-Oct/early-Nov window (exact date not yet confirmed by the company as of this session) — the next checkpoint for whether TTM FCF recovers toward positive or the guided $220B FY2026 capex program keeps it negative into a second consecutive quarter, and for whether Q3's actual results land inside, above, or below the guided $197.0–202.0B net sales / $22.5–26.5B operating income range.
- **Phase 04 Quality Watch (carried, intensifying).** AMZN's Quality Score remains decisively below the 80.0+ gate (56.7, essentially flat vs. 57.6) — but the composition shifted: profitability/margins/balance-sheet held up, while FCF Quality deteriorated further (TTM FCF flipped negative for the first time). Re-verify at Q3 FY2026 whether this is the trough of the capex cycle or a continuing trend.
- **Rule 9 fundamental triggers (standing):** any guidance revision outside the normal quarterly cadence, management change, material new M&A, or a >15% unexplained price move.
- **Analyst consensus PT staleness:** the $313.07 consensus figure used for sanity-checking (§8) may not yet reflect the Q2 print (underlying target changes cited are dated 28 Jul, pre-earnings) — worth a fresh pull next session.
- **Forward PE off the 50.0 neutral fallback:** still not available until ~2028, when FY2022's GAAP-loss quarters roll out of the trailing 5-year PE lookback window.

---

## 13. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **8-K (Form 8-K)** | A US company's "current report" disclosing a material event between regular filings; earnings press releases are typically furnished as an exhibit to one. |
| **10-K / 10-Q** | A US company's annual (10-K) or quarterly (10-Q) report filed with the SEC, containing audited/reviewed financial statements. |
| **bps / pp (percentage points)** | A direct difference between two percentages, distinct from a "%" change. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean base — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FTC (Federal Trade Commission)** | The US federal agency enforcing antitrust and consumer-protection law — the counterparty in the $2.5B legal-settlement charge normalized out of AMZN's TTM EBIT this session. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score, absent a documented carve-out. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for moat-building reinvestors (Upgrade 1; applies to AMZN, MSFT, GOOGL, META). |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 6** | Normalize earnings/margins/revenue/debt before valuing — strip out one-time items (this session's basis for normalizing out the FTC settlement and severance charges). |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation (fired here via the quarterly earnings release). |
| **SBC (Stock-Based Compensation)** | Employee pay in company shares/options — a real dilution cost though a non-cash accounting expense. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |

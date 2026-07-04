# RESCORE — AMZN — 2026-07-04

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 4 Jul 2026
**10Y US Treasury Yield:** 4.48% (web search, dated 1–2 Jul 2026 — US bond market closed 3–4 Jul 2026 for the Independence Day holiday, so this is the most recent trading print available; still inside the "3.5–5%" bracket → Rate Regime Modifier Step 2 unchanged at +5)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** AMZN **73.4** (2026-06-20, TRIM 25–30% — [sessions/2026-06-20-rescore-amzn.md](2026-06-20-rescore-amzn.md)). Quality Score / Composite Score had never been computed for AMZN — flagged stale per [watchlist/STALE.md](../watchlist/STALE.md) 2026-06-29 methodology table.
**First-ever Quality Score / Composite Score computation for AMZN this session.**

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; D&A = depreciation and amortization; capex = capital expenditure; Owner Earnings = net income + D&A − maintenance capex; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ PE); NOPAT = net operating profit after tax; ROIC = return on invested capital; TAM = total addressable market; TTM = trailing twelve months.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$241.70** | IBKR `get_price_snapshot` (contract_id 3691937, AMZN / NASDAQ), pulled this session. Flagged `is_close: true` — the US equity market is closed 3 Jul 2026 (Independence Day, observed) and 4 Jul 2026 (Saturday), so this is the last-close print from Thursday 2 Jul 2026, the most recent price available. Rule 0 compliant: this is a fresh pull this session, not a reused figure from the 2026-06-28 portfolio snapshot. |
| 52-week range | **$196.00 – $278.56** | IBKR `misc_statistics` |
| Year-to-date change | **+4.71%** (+$10.88) | IBKR `year_to_date_change` |
| Analyst consensus PT | **$312.91** (66 analysts, "Strong Buy") | stockanalysis.com, dated 2026-07-02 — bull-case sanity anchor only, never a score input |

Price vs 06-20 session: $244.39 → $241.70 = **−1.1%**. Nowhere near the 15% Rule 9 threshold.

---

## 2. Rule 9 Trigger Check (2026-06-20 → 2026-07-04)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Next report: **Q2 FY2026, expected 30 Jul 2026** (after close) — unchanged, still ahead |
| Guidance revision | No | No new guidance since the $200B FY2026 capex figure (already known before 06-20) |
| M&A | No — pre-existing, not new | Amazon–Globalstar merger agreement (satellite/direct-to-device connectivity) was announced **14 Apr 2026** — well before the 06-20 review, already priced in; not a new event this window |
| Management change | No | None found |
| Macro shift | No | 10Y ticked 4.45% → 4.48%, still inside "3.5–5%" bracket |
| >15% unexplained price move | No | −1.1% over 2 weeks |

**Conclusion: no Rule 9 trigger fired.** This is a routine, schedule-free re-score whose real substance is (a) the first-ever Quality Score computation and (b) a data-quality correction discovered this session (§4).

---

## 3. AMZN — Data Collected

**Sector:** Consumer Discretionary — E-commerce & Cloud Infrastructure (AWS). Treated as Technology/Growth for fair-value method per Rule 1.
**Current portfolio weight:** 9.99% combined (IBKR + Freedom24) — per [holdings.md](../portfolio/holdings.md), not recomputed this session. Freedom24 leg priced off the same live IBKR quote per the task brief (single global market price, split custody, no separate Freedom24 API).

`yfinance` is unreachable this session (`curl_cffi`/TLS proxy error — the same persistent failure documented across recent sessions, e.g. META 2026-07-01 Data Gap #3). **All figures below are sourced directly from Amazon's own SEC filings (10-K, 10-Q, 8-K earnings-release exhibits) via web search/fetch, not yfinance.**

### Trailing-twelve-months (TTM) roll-forward, ended 31 Mar 2026 (most recent quarter reported)

Built as **FY2025 (audited 10-K/8-K) + Q1 FY2026 (10-Q/8-K) − Q1 FY2025 (10-Q)** — the standard TTM construction, shown in full for auditability:

| Line | FY2025 (12mo to 31 Dec 2025) | Q1 FY2026 (3mo to 31 Mar 2026) | Q1 FY2025 (3mo to 31 Mar 2025) | **TTM (to 31 Mar 2026)** |
|---|---|---|---|---|
| Net sales | $716.924B | $181.519B | $155.667B | **$742.776B** |
| Operating income (EBIT) | $79.975B | $23.852B | $18.405B | **$85.422B** |
| Net income (GAAP) | $77.670B | $30.255B | $17.127B | **$90.798B** |

Sources: FY2025 — [Amazon Q4/FY2025 earnings release, 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm). Q1 2026 — [Amazon Q1 2026 earnings release, 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000012/amzn-20260331xex991.htm). Q1 2025 — [Amazon Q1 2025 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872425000036/amzn-20250331.htm).

**Directly company-reported TTM figures (no reconstruction needed):**

| Item | TTM to 31 Mar 2026 | Source |
|---|---|---|
| Operating cash flow | $148.531B | Amazon Q1 2026 earnings release |
| Purchases of property & equipment (capex) | $147.299B | Amazon Q1 2026 earnings release |
| Free cash flow (Amazon's own definition) | **$1.232B** | Amazon Q1 2026 earnings release (= OCF − capex, ties out exactly) |
| Depreciation & amortization | $70.439B | Amazon Q1 2026 earnings release |

### Balance sheet, as of 31 Mar 2026 (most recent quarter-end)

| Item | Value | Source |
|---|---|---|
| Cash and cash equivalents | $101.816B | Q1 2026 10-Q/8-K |
| Marketable securities | $41.273B | Q1 2026 10-Q/8-K |
| Total long-term debt | $119.074B | Q1 2026 10-Q/8-K |
| Total stockholders' equity | $441.914B | Q1 2026 10-Q/8-K |
| **Net debt** | **−$24.015B (net cash)** | $119.074B − ($101.816B + $41.273B) |

### FY2025 effective tax rate (used for NOPAT normalization, §5)

Provision for income taxes $19.087B ÷ Income before taxes $97.311B = **19.6%** ([Amazon FY2025 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm)). Used as the cleanest available full-year, non-quarter-distorted rate (see Data Gap #2 below on why the Q1 2026 quarterly rate isn't used instead).

### Other collected inputs

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 10.76B | stockanalysis.com, dated 2026-07-04 (consistent with $2,600.7B market cap ÷ $241.70) |
| FY2026 consensus EPS | $8.69 | stockanalysis.com analyst-estimates page, dated 2026-07-02, n=66 analysts |
| Gross margin (TTM to 31 Mar 2026) | **51.82%** | macrotrends.net, cross-checked against FY2025 50.3% and a 2021→2025 uptrend (42.0%→50.3%) — structurally expanding, multi-year, not a one-quarter blip |
| Revenue FY2022 (for 3yr CAGR) | $513.983B | Carried from 06-20 session (SEC-sourced; independently corroborated this session at "$514.0B") |
| FY2024 FCF / Net Income | $38.22B / $59.25B | Amazon Q4/FY2024 earnings release |
| PEG (trailing, unscored sensitivity check) | 1.35 | stockanalysis.com, 2026-07-04 |

---

## 4. Data Gaps, Corrections & Flags

1. **EBIT correction (material — supersedes the 06-20 session's carried figure).** The 06-20 session used **EBIT $99.585B**, sourced from `yfinance`'s generic `ebit` field. This session independently reconstructs TTM Operating Income at **$85.422B** directly from Amazon's own reported quarterly/annual GAAP operating-income line items (§3), a $14.16B (14.2%) gap. **Best-evidence explanation:** `yfinance`'s `ebit` field is typically computed as *pretax income + interest expense*, not the company's own "Operating Income" line — and Q1 2026 pretax income ($39.834B) includes a **$16.8B pre-tax non-operating gain from Amazon's investment in Anthropic** (disclosed in Amazon's own Q1 2026 earnings release; see #2 below). If a TTM "ebit" proxy incorporated this quarter's inflated pretax income, it would overstate true operating profit by roughly this magnitude — consistent with the size of the gap found. **This session uses the GAAP Operating Income figure ($85.422B), independently reconstructed from primary SEC filings, as the correct basis** — cross-validated against the resulting EBITDA (EBIT $85.422B + D&A $70.439B = $155.861B) matching the 06-20 session's separately-carried EBITDA figure ($155.86B) almost exactly, which the flawed $99.585B "EBIT" figure would not do. **This is a data-quality correction discovered this session, not a fundamental deterioration in the business** — flagged prominently because it materially changes EV/EBIT and the Upside/Downside Modifier's fair-value scenarios (§6, §8).
2. **Anthropic investment gain — one-off, normalized out.** Amazon's Q1 2026 net income ($30.255B) includes a disclosed **$16.8B pre-tax gain** from its Anthropic investment (mark-to-market on a non-operating equity stake), per Amazon's own earnings release. This is exactly the kind of one-time, non-operating item Rule 6 ("normalize before you value") and this framework's precedent (deferred-tax-release, uncertain-tax-position entries in [glossary.md](../framework/glossary.md)) require stripping out before using net income as a quality/profitability input. **Normalization:** after-tax impact estimated at $16.8B × (1 − 24.0% Q1'26 effective tax rate) ≈ **$12.77B**, giving **normalized TTM Net Income ≈ $78.03B** (vs. $90.80B GAAP). Used for the Quality Score's Profitability sub-score and for Owner Earnings (§5, §6). The company did not itemize the exact after-tax component — this is an effective-rate-based estimate, flagged as such, not an invented number (analogous to META's tax-rate-normalization treatment, 2026-07-01 session).
3. **FY2026 consensus EPS ($8.69) may not be fully "clean."** If sell-side models haven't fully backed out the Anthropic gain from their FY2026 estimate (updated after the 29 Apr 2026 Q1 print), the Forward PE computed below could be modestly understated (i.e., the true "clean" forward PE could be a touch higher). Flagged as an open caveat; not independently resolvable from public aggregator data this session.
4. **"Market share stable or growing" moat signal — resolved against Amazon this session (see §6).** AWS's own cloud-infrastructure market share has *declined* from ~32% (2021) to 28% (Q1 2026, Synergy Research Group, cited) as Azure and Google Cloud grow faster. US e-commerce share estimates are mixed across sources (35.7%–38%) with no clear multi-year growth trend found. Given AWS is the company's primary profit engine and its erosion is the most consistently documented data point, this signal is marked **FALSE** rather than assumed true — consistent with "never mark a signal true without cited evidence."
5. **Total debt figure ($119.074B) is "total long-term debt" per the 10-Q/8-K** — may exclude a small current-portion-of-long-term-debt line if reported separately; not independently broken out in the sources found this session. Immaterial to the Net Debt/EBITDA conclusion given the large net-cash cushion.

---

## 5. AMZN — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = Live Price ÷ FY2026 consensus EPS = $241.70 ÷ $8.69 = 27.8136×
EY         = 1 ÷ 27.8136 = 3.5954%
Spread     = EY − 10Y Treasury = 3.5954% − 4.48% = −0.8846%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (−0.8846%, ~2.4pp short) → **+5 additive.**

**Step 2 — Rate Regime Modifier**
10Y = 4.48% → "3.5–5%" bracket → **+5**

**Total Rate Modifier = +10** (unchanged from 06-20).

---

## 6. AMZN — Quality Score (first-ever computation, 2026-06-29 methodology)

```
Profitability (25%):
  Net Margin (normalized, ex-Anthropic) = $78.030B ÷ $742.776B (TTM revenue) = 10.505%
  ROIC: NOPAT = EBIT × (1 − FY2025 effective tax rate) = $85.422B × (1 − 0.196) = $68.679B
    Invested Capital = Total Debt ($119.074B) + Total Equity ($441.914B) = $560.988B
    ROIC = $68.679B / $560.988B = 12.243%
  NetMargin_Component = clamp((10.505/30)×100, 0, 100) = 35.02
  ROIC_Component       = clamp((12.243/30)×100, 0, 100) = 40.81
  Profitability_Score  = (35.02 + 40.81) / 2 = 37.91   (no FCF cap — FCF-positive every year on record,
    including the capex-crushed TTM $1.232B, which is still positive)

Margins (15%): Gross margin 51.82% (TTM to 31 Mar 2026, macrotrends — structurally expanding 2021→2026)
  GrossMargin_Score = clamp((51.82/80)×100, 0, 100) = 64.78   (already >40% — no separate trend bonus
    needed; the expansion is directionally supportive evidence used elsewhere, not double-counted here)

Growth (20%): Revenue 3yr CAGR, FY2022 $513.983B → FY2025 $716.924B (both SEC-filed annual figures)
  CAGR = (716.924/513.983)^(1/3) − 1 = 11.731%
  Growth_Score = clamp((11.731/25)×100, 0, 100) = 46.93
  + 10 (documented TAM expansion, no decel evidence — growth is *accelerating*, not decelerating:
    quarterly YoY net-sales growth 9%→12%→17% into Q1 2026; global cloud-infrastructure spend +35% YoY
    market-wide (Synergy Research); Amazon's 14 Apr 2026 Globalstar acquisition opens a new
    direct-to-device satellite-connectivity market; grocery delivery scaled 30x to 2,300 cities)
  Growth_Score (with bonus) = 56.93

Balance Sheet (15%): Net Debt = $119.074B − ($101.816B + $41.273B) = −$24.015B (net cash)
  EBITDA = EBIT + D&A = $85.422B + $70.439B = $155.861B
  Net Debt/EBITDA = −24.015/155.861 = −0.154× (net cash)
  BalanceSheet_Score = clamp(100×(1−(−0.154)/4), 0, 100) = clamp(103.85, 0, 100) = 100.0

Moat Signal (15%) — checklist, cited evidence:
  ✗ Market share stable/growing — FALSE. AWS cloud-infrastructure market share has declined from
     ~32% (2021) to 30% (Q4 2024) to 28% (Q1 2026) as Azure (21%) and Google Cloud (14%) grow faster
     (Synergy Research Group, via Statista/CRN). US e-commerce share estimates are mixed (35.7%–38%,
     no clear multi-year uptrend documented). Given AWS drives the majority of operating profit and its
     erosion is the most consistently documented trend, this signal does not clear the bar.
  ✓ Brand premium — TRUE. Amazon ranks #4 among the world's most valuable brands in 2026 at $370B
     brand value (Kantar BrandZ / Visual Capitalist / Statista), built on Prime subscription premium
     and multi-category trust (retail, cloud, advertising).
  ✓ Network effect — TRUE. Amazon's marketplace is a textbook two-sided network: third-party sellers
     accounted for 60–62% of units sold in 2026 (Marketplace Pulse/Statista), drawn from ~1.65M active
     sellers, with buyer traffic and seller supply reinforcing each other.
  ✓ Switching costs — TRUE. AWS data-egress fees ($0.09/GB) create real, documented enterprise
     migration friction — moving 100TB off AWS costs roughly $8,000 in egress charges alone before
     migration engineering costs, a structural lock-in mechanism (even with a 2026 EU-pressure-driven
     waiver for "legitimate" planned migrations, the underlying cost structure remains a switching
     deterrent for routine competitive shopping).
  ✓ Scale cost advantage — TRUE. Amazon has reduced cost-per-unit for the third straight year despite
     rising delivery volumes and speed (1,000+ fulfillment centers; 8B+ same/next-day Prime items in
     2025, +30% YoY) — documented, multi-year scale-driven cost efficiency.
  Moat_Score = (4/5) × 100 = 80.0

FCF Quality (10%): FCF/NI TTM (GAAP) = $1.232B / $90.798B = 1.357%
  FCFQuality_Score = clamp(((0.01357 − 0.40)/0.60)×100, 0, 100) = clamp(−64.4, 0, 100) = 0.0
  FY2024 FCF/NI = $38.22B/$59.25B = 64.51% (<70%); FY2025 = $11.194B/$77.670B = 14.41% (<70%) —
  **2 consecutive fiscal years below 70%, which is the hard-disqualifier condition on its face.**
  Does NOT fire: both years carry the same documented growth-capex explanation that underlies
  Upgrade 1 (Owner Earnings) for this name — TTM growth capex is 52.2% of total capex
  (($147.299B − $70.439B)/$147.299B), well above the 30% trigger, and Amazon has publicly guided
  $200B of FY2026 capex explicitly for AI/data-center/robotics buildout, not maintenance. A cited,
  standing explanation, not an unexplained shortfall — same treatment as META's 2026-07-01 session.

Quality Score = 37.91×0.25 + 64.78×0.15 + 56.93×0.20 + 100.0×0.15 + 80.0×0.15 + 0.0×0.10
              = 9.4775 + 9.717 + 11.386 + 15.0 + 12.0 + 0.0
              = 57.5805 → rounds to 57.6
```

**Quality Score = 57.6 — FAILS the 80.0+ gate decisively.**

**Hard disqualifier check:** none fire outright. FCF/NI <70% for 2 consecutive years has a documented, standing growth-capex explanation (Upgrade 1 basis, 52.2% growth-capex share — the highest ratio yet seen in this framework, well above META's 52% at its own last rescore); Net Debt/EBITDA is a net-cash position, nowhere near either threshold; FCF-positive every year on record (TTM $1.232B is thin but still positive).

**Why the failure is real, not a data artifact:** unlike the EBIT correction (§4, a data-quality fix), this Quality Score failure reflects genuine current-state weakness — normalized net margin (10.5%) and ROIC (12.2%) are thin relative to a rapidly-growing invested-capital base (the $200B FY2026 capex program), and FCF/NI conversion has collapsed to ~1.4% TTM. This is the same capex-supercycle dynamic Upgrade 1 (Owner Earnings) exists to look through *for valuation purposes* — but the Quality Score's Profitability and FCF Quality sub-scores have no equivalent capex-normalization carve-out, so they correctly register the current cash-conversion and capital-efficiency strain. **Flagged as a Phase 04 Quality Watch escalation** (per rescore.md step 3) — AMZN is an existing holding, so it is **not retroactively force-exited on quality alone**, but this is the first hard evidence that quality has drifted, worth tracking closely into Q2 earnings (30 Jul 2026), which should show whether operating income is beginning to scale with the capex build per management's own framing.

---

## 7. AMZN — Phase 02 Valuation Score

**Owner Earnings (Upgrade 1) — shown explicitly:**
- Growth capex check: TTM total capex $147.299B; maintenance-capex proxy (= D&A) $70.439B; growth capex = $76.860B = **52.2% of total** → exceeds the 30% trigger → Upgrade 1 applies.
- OE = Net Income (normalized, ex-Anthropic — §4 Data Gap #2) $78.030B + D&A $70.439B − maintenance capex (=D&A) $70.439B = **$78.030B** (D&A terms cancel by construction of the maintenance-capex proxy).
- OE yield = $78.030B ÷ Market Cap $2,600.692B (10.76B shares × $241.70) = **3.0004%**.

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 3.0004/10), 0, 100) = 69.996
```
→ Contribution: 69.996 × 0.40 = **27.998**

(Reported/raw FCF, for contrast only, not scored: TTM $1.232B ÷ $2,600.692B = 0.047% yield — would have scored ~100, hugely overstating expensiveness; exactly why Upgrade 1 is required.)

**EV/EBIT — 40% weight** (PEG not applicable, see below → 15% redistributed here)
```
EV  = Market Cap $2,600.692B + Net Debt (−$24.015B) = $2,576.677B
EV/EBIT_Score = clamp(($2,576.677B / $85.422B − 12)/23 × 100, 0, 100) = clamp((30.164 − 12)/23 × 100, 0, 100) = 78.97
```
→ Contribution: 78.97 × 0.40 = **31.588**

**Forward PE — 20% weight**
No clean 5-year PE history: the trailing 5-year window (mid-2021 → mid-2026) still fully contains FY2022's GAAP net-loss quarters, which distort any reconstructed average/range upward (individual quarterly PE readings of 120×–251× in that window, per the 06-20 session's finding). **FY2023–FY2025 are now three clean profitable years, but the framework's fallback requires a full 5-year average/range**, not 3 — the earliest a clean 5yr window becomes available is ~2028, once FY2022 rolls out of the lookback.
```
FwdPE_Score = 50.0 (neutral fallback, flagged — unchanged rationale from 06-20)
```
→ Contribution: 50.0 × 0.20 = **10.0**

**PEG — Fast-Grower test: still FAILS.** Net income trajectory FY2022 loss → FY2023 $30.43B → FY2024 $59.25B (+94.7%) → FY2025 $77.67B (+31.1%) is a recovery off the 2022 loss, not 3+ years of clean >15% growth on a non-distorted base. **PEG's 15% weight redistributed to EV/EBIT** (used above; trailing PEG of 1.35 per stockanalysis.com recorded as a sensitivity check only, not scored).

**Raw weighted score:**
```
= 27.998 + 31.588 + 10.0 = 69.586
```
**+ Rate Modifier (+10) = 79.586** *(before the Upside/Downside Modifier)*

---

## 8. AMZN — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario fair value (Rule 7, EV/EBIT-multiple method on forward EBIT).** Same three qualitative scenarios and exit multiples as the 06-20 session (AWS-reacceleration bull / consensus base / capex-drag-and-slowdown bear), but **rebuilt on the corrected $85.422B TTM EBIT base** (§4 Data Gap #1) rather than the erroneous $99.585B carried forward — the dollar growth assumptions (+25%/+18%/+8%) are unchanged judgments, only the base they're applied to is corrected:

| Scenario | Wt | Forward EBIT | Exit EV/EBIT | Equity Value = EBIT×Mult − Net Debt | FV/share (÷10.76B sh) |
|---|---|---|---|---|---|
| Bull | 25% | $85.422B × 1.25 = $106.78B | 27.0× | $2,882.9B − (−$24.0B) = $2,906.9B | **$270.17** |
| Base | 50% | $85.422B × 1.18 = $100.80B | 24.0× | $2,419.2B + $24.0B = $2,443.2B | **$227.06** |
| Bear | 25% | $85.422B × 1.08 = $92.26B | 18.0× | $1,660.6B + $24.0B = $1,684.6B | **$156.56** |

```
PW Fair Value = 0.25×270.17 + 0.50×227.06 + 0.25×156.56 = $220.21
```

**Sanity check (Rule 4/0 Step 4):** PW FV ($220.21) and even the Bull case ($270.17) now sit **below** the $312.91 analyst consensus PT — a reversal from 06-20, where the bull case ($310) sat just under consensus. Flagged honestly rather than adjusted to match: sell-side models likely use segment sum-of-the-parts or DCF methods with different long-run margin assumptions than this framework's single EV/EBIT-multiple scenario approach; this divergence is an open item to watch as the capex cycle matures, not resolved by inflating the bull case to meet consensus (Rule 7 guardrail — never use the rosy point).

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = ($220.21 ÷ $241.70) − 1                    = −8.890%   (price is now ABOVE PW FV)
Catalyst window = 2 years (unchanged default — no single hard re-rating catalyst within 18–24mo;
                   the capex-to-FCF inflection and AWS re-acceleration are multi-year stories)
Annualized gap  = −8.890% ÷ 2                                 = −4.445%/yr
Intrinsic growth = +10%/yr (carried, unchanged — durable owner-earnings growth anchored to the
                   11.73% revenue CAGR, decelerating modestly at scale, net of SBC dilution)
Shareholder yield = 0% (Amazon pays no dividend; the sole $10B buyback program authorized since 2022
                   has not offset SBC-driven share issuance — shares outstanding have net *increased*
                   since 2022 despite the repurchases, confirmed this session — net dilutive, treated
                   conservatively as 0% rather than negative)
```
```
E (expected annual return) = −4.445 + 10.0 + 0.0 = +5.555%/yr
```

**Step 3 — Catalyst/timeline (Rule 10 + Guardrail 1).** No hard catalyst within 18–24 months identified — the guardrail caps the *upside* (negative M) side at −5 if claiming large upside with no path to realize it. Not binding here since E is on the *positive-modifier* (thin/negative-return) side of the mapping, not the upside side — no cap needed.

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
0 ≤ E < H → M = +5 × (H − E)/H = +5 × (10 − 5.555)/10 = +5 × 0.4445 = +2.2225
```

**Interpretation:** for the first time in this name's session history, the gap term is *negative* — price ($241.70) now sits **above**, not below, the corrected probability-weighted fair value ($220.21). The modifier is only mildly positive (+2.2) because durable intrinsic growth (+10%/yr) still carries most of the expected-return math, keeping E just above the 10% hurdle rather than pushing it negative. This is a materially different picture from 06-20 (+2.9% gap, M = −1.40) — driven almost entirely by the EBIT correction (§4), not by any 2-week change in the business.

---

## 9. AMZN — Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (69.586) + Rate Modifier (+10) + Upside/Downside (+2.2225)
                       = 81.809
```
Boundary rule: not a ".X5" → standard rounding → **Final Valuation Score = 81.8**

| | Value |
|---|---|
| Raw weighted | 69.586 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | +2.2225 (E = +5.555%) |
| **FINAL VALUATION SCORE** | **81.8** |
| Prior valuation score | 73.4 (06-20) |
| **Quality Score** | **57.6 (FAILS 80.0+ gate)** |

```
Composite Score = 0.50 × (100 − 57.6) + 0.50 × 81.8 = 0.50×42.4 + 0.50×81.8 = 21.2 + 40.9 = 62.1
```

**Composite Score = 62.1.**

---

## 10. AMZN — Action & the divergence between the two scores (read carefully — see NKE 2026-07-01 precedent)

**Raw Valuation Score alone: 73.4 → 81.8** (moves from the 70.0–79.9 "Trim 25–30%" band into the **80.0–89.9 "Trim to 50%"** band) — driven almost entirely by the EBIT correction (§4: true EBIT is ~14% lower than the figure carried forward from 06-20, so EV/EBIT is meaningfully higher/more expensive than previously believed) and the resulting swing in the Upside/Downside Modifier from mildly negative to mildly positive. **This is a data-quality correction, not two weeks of fundamental deterioration.**

**Composite Score (62.1) → Action band: HOLD — watch only, no new entry, no trim (50.0–69.9 band).** Per [valuation-scoring.md](../framework/valuation-scoring.md), the Composite Score — not the raw Valuation Score — governs the Phase 03/05 action-table lookup once a Quality Score exists. AMZN's newly-computed Quality Score (57.6) pulls the blended number down a full band from what the raw valuation score alone implies.

**This divergence must not be read as "the Quality Score rescues AMZN into a comfortable Hold."** Unlike the 2026-07-01 NKE case (where a low Quality Score combined with a very cheap raw Valuation Score to produce a misleadingly bullish Composite that had to be overridden *down*), here the Quality Score failure and the raw Valuation Score's trim signal **point the same direction** — both say "be more cautious about AMZN right now," for related but distinct reasons:
- The raw Valuation Score's "Trim to 50%" read says the stock is priced above this framework's own probability-weighted fair value for the first time in this name's session history.
- The Quality Score's 57.6 (FAILS 80.0+) says current profitability, capital efficiency, and cash-conversion are genuinely strained by the heaviest capex cycle in the company's history, and AWS's core market-share moat signal is documented as eroding, not merely stable.

**Practical recommendation: HOLD — no new entry, no trim forced by the score** (per the framework's explicit rule that the Composite Score governs the action table, and that an existing holding failing the Quality Gate is a **watch flag, not an automatic force-exit or force-trim** — rescore.md step 3). But this is flagged as a **Phase 04 Quality Watch escalation**, not a routine, comfortable Hold: the position's underlying quality has genuinely drifted since it was last implicitly assumed "high quality enough" (pre-Quality-Score era), and the next earnings print (Q2 FY2026, 30 Jul 2026 — just 3.5 weeks away) is the natural checkpoint to see whether operating income and FCF conversion begin scaling with the capex build as management has guided, or whether the strain persists into a second consecutive quarter.

**No order setup required** — action is HOLD, not BUY/TRIM, so [fair-value-methodology.md](../framework/fair-value-methodology.md)'s order-setup checklist is out of scope this session (operating-brief.md OUTPUT FORMAT step 6 applies only to BUY/TRIM actions).

**Cap note:** at 9.99% combined (IBKR + Freedom24), AMZN is comfortably under Upgrade 7's 15% hard cap regardless of which score/band is read — not a cap-driven consideration either way.

---

## 11. Portfolio Note

This session does not change `portfolio/holdings.md` — that update (Last Score 81.8, Quality Score 57.6, Composite Score 62.1, Last Review 4 Jul 2026) is handled by the orchestrator across the batch. No trade is recommended or executed this session. AMZN's row in [watchlist/STALE.md](../watchlist/STALE.md) (2026-06-29 methodology table) should be removed by the orchestrator now that both scores are computed.

---

## 12. Next Review Triggers

- **Next earnings — AMZN Q2 FY2026, expected 30 Jul 2026 (after close)** — the natural, near-term checkpoint for whether operating income and FCF/NI conversion begin recovering as the $200B FY2026 capex program (guided) matures, per management's own framing. This is also the point at which analyst FY2026 EPS consensus should be re-checked for whether it has normalized the Anthropic one-off (Data Gap #3).
- **Phase 04 Quality Watch (new this session).** AMZN's first-ever Quality Score decisively fails the 80.0+ gate (57.6) — re-verify at the next rescore whether Profitability/FCF Quality sub-scores are recovering (capex-cycle-driven) or structurally worsening, and whether the AWS market-share erosion (32%→28%, 2021→2026) continues or stabilizes.
- **Rule 9 fundamental triggers (standing):** any guidance revision, management change, material new M&A, or a >15% unexplained price move.
- **EBIT/data-quality correction (§4):** if `yfinance` access is restored, cross-check the independently-reconstructed TTM EBIT ($85.422B) against a fresh `yfinance` pull to confirm the correction and rule out any remaining discrepancy.
- **Forward PE off the 50.0 neutral fallback:** not available until ~2028, when FY2022's GAAP-loss quarters roll out of the trailing 5-year PE lookback window.

---

## 13. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **8-K (Form 8-K)** | A US company's "current report" disclosing a material event between regular filings; earnings press releases are typically furnished as an exhibit to one. |
| **10-K / 10-Q** | A US company's annual (10-K) or quarterly (10-Q) report filed with the SEC, containing audited/reviewed financial statements. |
| **bps / pp (percentage points)** | A direct difference between two percentages, distinct from a "%" change. |
| **Buyback yield** | The rate at which a company's share count shrinks per year from repurchases, net of new issuance. |
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
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 6** | Normalize earnings/margins/revenue/debt before valuing — strip out one-time items. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **SBC (Stock-Based Compensation)** | Employee pay in company shares/options — a real dilution cost though a non-cash accounting expense. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |

# RESCORE — META — 2026-08-05

**Task type:** RESCORE (single ticker) — **Telegram-triggered** (Routine 6 / `/telegram-scan`), **P1 priority** (≥5% weight holding, per automation-schedule.md)
**Trigger:** New post [t.me/tarasguk/11606](https://t.me/tarasguk/11606) (~15:23 UTC, 2026-08-05): "$META is still not more expensive than $SPCX even after its 7% drop after the report" (translated from Ukrainian). Per CLAUDE.md Rule 0, the post's text is used only as a *trigger* — every figure below is independently re-pulled from `yfinance`, SEC EDGAR, Meta's own investor-relations site, and wire coverage, not from the post. The post implies Meta reported Q2 2026 earnings and dropped ~7% — **independently confirmed true** (§2). The SPCX (SpaceX) comparison in the post is not evaluated here — out of scope, no SPCX position or evaluation exists in this repo.
**Date:** 05 Aug 2026
**10Y US Treasury Yield:** 4.70% (FRED `DGS10`, last posted non-blank value, dated 2026-08-03 — no 08-04/08-05 print yet; up marginally from 4.69% used 07-28, still inside the "3.5–5%" bracket → Rate Regime Modifier Step 2 unchanged at +5)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** META **31.3** (2026-07-28, Composite 20.7, BUY — Full position 6–8% — [sessions/2026-07-28-rescore-meta.md](2026-07-28-rescore-meta.md))
**Gap since last review:** 8 days.

⚠️ **IBKR snapshot denied; price = yfinance/web close.** The IBKR MCP connector was not reachable in this session (tool not found). Per this repo's precedent ([sessions/2026-06-20-rescore-nvo.md](2026-06-20-rescore-nvo.md)), falling back to a live `yfinance` pull, cross-checked against a web quote, rather than skipping the rescore.

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; NOPAT = net operating profit after tax; ROIC = return on invested capital; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; pp = percentage points; EY = earnings yield (1 ÷ PE); TTM = trailing twelve months; NTM = next twelve months; JV = joint venture; 10-Q = quarterly SEC filing; 8-K = SEC "current report" filing.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$584.48** | `yfinance` `fast_info["last_price"]`, pulled this session (ts 2026-08-05 ~16:20 UTC / ~12:20pm ET) |
| Cross-check | $582.20 (12:15pm ET) / previous close $587.94–$589.60 (small variance across sources/minutes) | stockanalysis.com WebFetch + a second `yfinance` pull minutes apart — same ballpark, confirms no stale/cached quote |
| 52-week range | **$520.26 – $796.25** | `yfinance` `fast_info` |
| Year-to-date / vs 07-28 | $593.41 (07-28 close, per `yfinance` history) → $584.48 today = **−1.51%** over 8 days | Computed |
| Analyst consensus PT | **$756.95** (62 analysts, S&P Global via stockanalysis.com, "Strong Buy") | WebFetch — bull-case sanity check only (Rule 0 Step 4) |

⚠️ **IBKR fallback flagged as required by task scope.** No live IBKR snapshot this session; `yfinance` used instead (verified working this session — see §4 for the larger implication).

---

## 2. Rule 9 Trigger Check (2026-07-28 → 2026-08-05) — Independent Verification of the Trigger Post

| Trigger | Found? | Detail |
|---|---|---|
| **Quarterly earnings** | **YES** | Meta reported **Q2 2026 results after close on 29 Jul 2026** — independently confirmed via `investor.atmeta.com` press release, the SEC 8-K/10-Q ([meta-20260630.htm](https://www.sec.gov/Archives/edgar/data/0001326801/000162828026050705/meta-20260630.htm)), PRNewswire, and wire/analysis pickups (StockTitan, Investing.com, CNBC, Variety, TradingKey, KuCoin, TechTimes, DigitalApplied). |
| **Guidance revision** | **YES** | FY26 capex guidance narrowed to **$130–145B** (effectively raising the low end from the $125B floor used in the 07-28 log); FY26 total-expense guidance raised to **$165–169B** (from ~$162–169B), explicitly to absorb a $2.4B Q2 legal charge. Both are official, company-issued revisions — an independent second Rule 9 trigger, on top of the earnings release itself. |
| Material M&A / JV | No *new* one | El Paso/BlackRock JV (07-28 trigger) was reaffirmed qualitatively on the earnings call, no new JV disclosed this window. |
| Management change | No | None found. |
| Macro shift | No | 10Y ticked 4.69%→4.70%, essentially flat, still inside the "3.5–5%" bracket. |
| >15% unexplained price move | No (and explained regardless) | See below — the move is well below 15% net, and it's explained by the earnings print, not "unexplained." |

**The triggering post's claim, independently verified — confirmed true, and clears the Rule 9 bar decisively (quarterly earnings is the single most direct Rule 9 trigger category).**

**Verified Q2 2026 results (not from the post):**
- **Revenue:** $60.801B, +28% YoY, beat consensus (~$60.2–60.3B).
- **Diluted EPS:** $6.18, **missed** consensus (~$7.17–7.22) by ~14%, down from $7.14 a year ago.
- **Net income:** $15.848B (down from $18.337B a year ago).
- **Operating income (EBIT):** $18.775B; **operating margin compressed to 31%, from 43%** a year ago.
- **Total costs & expenses:** $42.026B, +55% YoY — includes a **$2.4B legal-proceedings charge** and **$1.18B severance** (May 2026 layoffs).
- **Capital expenditures:** $31.08B in the quarter alone (record) — almost entirely AI/data-center infrastructure.
- **Free cash flow:** company-reported **$784M** for the quarter (down from $8.549B a year ago) — `yfinance`'s own OCF-minus-capex reconciliation gives **$1.746B** for the same quarter; the ~$960M gap is finance-lease-principal-payment treatment (Meta's own FCF definition nets these out, `yfinance`'s does not). Both figures independently confirm the same qualitative story: FCF collapsed this quarter under record capex.
- **Share repurchases: $0 this quarter — buybacks have now been suspended for 3 consecutive quarters** (Q4 2025, Q1 2026, Q2 2026 all show $0 in `yfinance`'s quarterly cash-flow statement), a major, verified change from the ~$26B TTM pace used in every session through 07-28. Dividends continue ($1.353B this quarter, a small per-share raise).
- **Balance sheet (30 Jun 2026):** Cash + marketable securities $90.26B; long-term debt (senior notes, excl. lease obligations) $83.664B — Meta issued ~$25B of new long-term debt in Q2 alone. Net cash position **fell from $22.432B (Q1 2026) to $6.596B (Q2 2026)** — see §6.
- **Effective/forward tax rate guidance raised:** management now guides **15–17%** (midpoint 16%) for the rest of 2026, up from the 13–16% guided as of Q1 2026 — used in the ROIC recompute (§6).

**Independently verified price move (not the post's framing):** close 07-29 (pre-earnings-reaction) $585.61 → after-hours −9.64% to ~$529.15 → first full reaction day (07-30) closed **$539.03, a −7.96% move from the 07-29 close** (or **−9.16%** from the 07-28 pre-earnings close of $593.41) — this closely matches, and if anything slightly *understates*, the triggering post's "~7% drop" framing. The stock then **recovered most of the loss** over the following week (07-31 $556.71 → 08-03 $590.24 → 08-04 $587.94 → 08-05 $584.48), landing only **−1.51%** below its pre-earnings level by today. Net: the post's core claim (an earnings-driven ~7% drop) is verified true; what it omits is the subsequent near-full recovery.

**AI-infrastructure JV commentary on the call (qualitative context only, per 07-28 session's treatment):** Zuckerberg reaffirmed the El Paso/BlackRock JV and the Louisiana ("Hyperion") facility (now disclosed at "over $50B" cost), and added a new data point: *"We're getting a lot of offers for compute at a significant premium over what we paid for it"* — the first concrete, on-the-record evidence for the "Meta Compute" leasing story tracked qualitatively since 07-01/07-09. Susan Li (CFO) explicitly **declined to give 2027 capex guidance**, calling infrastructure planning "highly dynamic." None of this changes any scored input this session (same treatment as 07-28 §2/§4) — noted as qualitative color only.

**Conclusion: Rule 9 trigger CONFIRMED, decisively** (quarterly earnings + guidance revision, the two least-ambiguous trigger categories in the framework) — full re-score proceeds as a triggered event.

---

## 3. META — Inputs Collected (fresh this session — first full live re-pull since persistent `yfinance` rate-limiting began)

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** **6.43%⚠️** (per [holdings.md](../portfolio/holdings.md), live-synced 2026-08-02 — the unexplained 6→5→6 share-count anomaly from override-log.md remains open and unresolved, out of `/rescore`'s scope; using the current 6.43% as the authoritative live weight per Rule 0).

### 🚩 Major data correction this session — shares outstanding

`yfinance`'s full quarterly balance sheet (working for the first time in ~11 consecutive META sessions — see §4) shows **"Ordinary Shares Number" = 2,548,378,209** as of 30 Jun 2026 (Class A 2,206M + Class B 342M, confirmed independently via the Q2 2026 10-Q), not the **≈2.196B carried across every prior META session** since at least 06-11. Checking the historical quarterly series: total shares were already **2.516B a year ago (Q2 2025)** — i.e. the "2.196B" figure wasn't a stale-but-once-true number, it was **already wrong when first carried**, and closely matches *Class A alone* (2.206B today) rather than total combined Class A+B shares. This is the same failure pattern as the **Dual-class shares** glossary entry (FUBO precedent: vendor `sharesOutstanding` captured only the traded class) — Meta's Class B converts 1:1 into Class A, so total economic shares outstanding is the sum, not the Class A count alone. **Every prior META Market Cap / EV / EV-EBIT figure in this repo's history was therefore understated by ~14–16%** (2.196/2.548 ≈ 0.862). Not retroactively restated (git history preserves the prior logs as historical record, consistent with how the framework treats past sessions) — flagged here, going forward, as the corrected basis. **This session uses 2,548,378,209 shares.**

### Fresh TTM inputs (Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026, via `yfinance` quarterly statements — first live recomputation, not carried)

| Item | Prior (07-28, carried) | Fresh this session | Computation |
|---|---|---|---|
| TTM Revenue | $214.963B | **$228.247B** | 51.242+59.893+56.311+60.801 |
| TTM EBIT | $88.621B | **$86.927B** | 20.535+24.745+22.872+18.775 |
| TTM Net Income | $70.629B | **$68.098B** | 2.709+22.768+26.773+15.848 |
| TTM FCF (raw) | $45.65B | **$40.976B** | 11.170+14.831+13.229+1.746 (`yfinance` quarterly "Free Cash Flow") |
| Gross margin (TTM) | 81.9% (carried) | **81.75%** | $186.587B gross profit ÷ $228.247B revenue |
| Cash + marketable securities | $81.180B | **$90.26B** | 10-Q, 30 Jun 2026 |
| Senior-note debt (excl. leases) | $58.748B | **$83.664B** | 10-Q "Long Term Debt", 30 Jun 2026 |
| Net cash | $22.432B | **$6.596B** | $90.26B − $83.664B |
| Shares outstanding | ≈2.196B (see correction above) | **2.548378B** | 10-Q, 30 Jun 2026 |
| TTM EBITDA | (not shown 07-28) | **$112.282B** | 26.853+31.221+28.313+25.895 |
| Buyback ($, TTM) | $26.25B | **$3.327B** | Q3'25 only ($3.327B); **Q4'25/Q1'26/Q2'26 all $0 — buybacks suspended 3 consecutive quarters** |
| Dividend ($, TTM) | $5.32B | **$5.367B** | 1.330+1.338+1.346+1.353 |
| 5yr avg PE (auto-reconstructed) | 23.589× (range 9.255×–36.014×, n=20q, carried, data gap) | **23.152× (range 9.255×–36.014×, n=20q)** | **Resolved this session** — see §4 |

### Refreshed this session (price/consensus-dependent)

| Item | 07-28 value | 08-05 value (fresh) | Computation |
|---|---|---|---|
| Live price | $594.00 | **$584.48** | `yfinance` fast_info (§1) |
| Market Cap | $1,304.4240B | **$1,489.4761B** | 2,548,378,209 × $584.48 (shares correction, see above — **not** a simple price-driven change) |
| EV | $1,281.9920B | **$1,482.8801B** | $1,489.4761B − $6.596B net cash |
| **EV/EBIT** | 14.4660× | **17.0589×** | $1,482.8801B ÷ $86.927B |
| **FCF Yield** | 3.4996% | **2.7510%** | $40.976B ÷ $1,489.4761B |
| Forward EPS (NTM/CY2026 consensus) | $31.72 | **$30.93** | S&P Global consensus via stockanalysis.com, fetched 2026-08-05 (62 analysts, updated 08-03 — down from $31.72, consistent with the EPS miss/lowered outlook) |
| Forward PE | 18.7264× | **18.8969×** | $584.48 ÷ $30.93 |

### Fast-Grower (PEG eligibility) test — re-verified, still fails

Annual diluted EPS: FY2022 $8.59 → FY2023 $14.87 (+73.1%) → FY2024 $23.86 (+60.5%) → **FY2025 $23.49 (−1.55%)**. Most recent fiscal year is negative — **still FAILS** ">15% EPS growth for 3+ consecutive years on a clean base." **PEG not applicable; its 15% weight redistributed to EV/EBIT** — unchanged from every prior META session.

---

## 4. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved; raw FCF used (at least 11th consecutive session).** Meta's Q2 2026 10-Q still does not disclose a maintenance-vs-growth capex split (confirmed again this session via direct 10-Q read). No new information to resolve this.
2. **5yr PE reconstruction — RESOLVED this session, after 2 consecutive sessions of `yfinance` rate-limiting failures.** `yfinance`'s `get_earnings_dates(limit=40)` + `t.history()` pipeline worked cleanly this session (46 quarters of reported EPS reconstructed back to 2021-10-25, no rate-limit errors). Fresh result: **23.152× avg, 9.255×–36.014× range, n=20 quarters (2021-10-25 to 2026-07-29)** — close to, but a genuine fresh recomputation of, the long-carried 23.589× figure (the oldest quarter in the rolling 20-quarter window rolled off, the fresh Q2 2026 earnings-date point rolled on).
3. **Convention note — a 5yr PE *range* is technically available this session, but the fallback (average-based) formula is used, consistent with every prior META session's explicit "Forward PE (fallback formula)" labeling (07-01, 07-09, 07-13, 07-28), even though a range has apparently always technically existed. Not changed here to preserve auditability/continuity — flagged as worth a `decisions/` clarification on why META specifically uses the fallback despite range availability, but not resolved unilaterally in this session.**
4. **This session marks the first full fresh quantitative TTM recomputation via a working `yfinance` pull since the persistent rate-limiting began** — every quantitative figure in §3 (other than the two carried-forward scenario tables in §8) is now independently fresh-pulled, not carried, for the first time in many sessions. This is a second, independent (non-earnings) reason several figures moved beyond what the earnings print alone would explain (notably the shares-outstanding correction above).
5. **Shares-outstanding correction (§3) — the single largest driver of this session's Market Cap/EV/EV-EBIT changes**, larger in magnitude than the earnings-driven fundamental changes themselves. Flagged prominently; not an invented number — sourced directly from the fresh 10-Q balance sheet, cross-checked against `yfinance`'s own quarterly balance sheet field and its live `fast_info` market-cap/shares calculation (both agree to within 0.04%).
6. **FCF quarterly-figure discrepancy ($784M company-reported vs. $1.746B `yfinance`-reconciled for Q2 2026) — noted in §2/§3, not resolved as a gap** (both are real, sourced figures; the difference is a documented definitional one — finance-lease-principal-payment treatment — not a data-quality problem). This session's TTM FCF ($40.976B) uses the `yfinance`-consistent basis throughout, per the framework's own documented automation methodology (valuation-scoring.md "Screening Tools" section).
7. **Bull/Bear scenario EPS assumptions ($40.0 / $28.0) and both exit multiples (24×/13×) — carried unchanged for the 7th+ consecutive session, not revisited despite two real earnings prints since they were set.** Per "never invent or estimate financial data," no new sourced Bull/Bear-specific consensus exists to replace them — only the Base-case EPS is updated to the fresh consensus, same practice as every prior session. Flagged as increasingly overdue for a dedicated review: the Bull case ($40.0 EPS) is now ~29% above the fresh CY2026 consensus ($30.93) and TTM EPS is $26.73 (NI $68.098B ÷ 2.548378B shares) — the gap between "current run-rate" and "bull case" has widened materially given this quarter's margin compression, worth a specific follow-up rather than continuing to carry a 2+-month-old placeholder indefinitely.
8. **META weight (holdings.md, §3):** 6.43%⚠️ — the ongoing unresolved 6→5→6 share-count anomaly (override-log.md) is unrelated to this session's data-source share-count correction (that's Meta's *own total shares outstanding*, this is *this portfolio's position size in shares*) — both flagged, neither resolved here, out of `/rescore`'s scope (would need `get_account_trades`).

---

## 5. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 18.8969 = 5.2919%
Spread = EY − 10Y Treasury = 5.2919% − 4.70% = +0.5919%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.5919%, ~0.91pp short) → **+5 additive.**

> Slightly wider miss than 07-28 (+0.65% cushion → +0.59% cushion) — forward PE ticked up marginally (18.7264×→18.8969×) as the fresh consensus EPS fell faster than the price, while the 10Y was essentially flat (4.69%→4.70%).

**Step 2 — Rate Regime Modifier**
10Y = 4.70% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +10** (unchanged from 07-28).

---

## 6. META — Quality Score (recomputed — first genuine, non-rounding change in this ticker's history)

```
Profitability (25%):
  Net Margin = TTM NI ÷ TTM Revenue = $68.098B ÷ $228.247B = 29.8352%
  ROIC: NOPAT = TTM EBIT × (1 − normalized tax rate)
    Normalized tax rate: TTM effective rate is distorted (Q3 2025 carries a large one-off
    tax charge, still inside this TTM window). Using management's own guided forward rate
    instead: 15–17% (midpoint 16%), per Meta's Q2 2026 earnings call (§2) — a company-
    disclosed figure, consistent with the 07-01 session's precedent of using guided rate
    over a distorted TTM rate.
    NOPAT = $86.927B × (1 − 0.16) = $73.019B
    Invested Capital = Senior debt ($83.664B) + Total Equity ($261.221B, 10-Q) = $344.885B
    ROIC = $73.019B ÷ $344.885B = 21.1719%
  NetMargin_Component = clamp(29.8352/30×100, 0, 100) = 99.4507
  ROIC_Component       = clamp(21.1719/30×100, 0, 100) = 70.5730
  Profitability_Score  = (99.4507 + 70.5730) / 2 = 85.0119

Margins (15%): Gross margin 81.7478% (fresh) → clamp(81.7478/80×100,0,100) = 100.0

Growth (20%): Revenue 3yr CAGR 19.89% (unchanged — FY2022–FY2025 annual figures, the only
  fiscal years complete; FY2026 isn't done yet, so this input doesn't move until year-end)
  Growth_Score = clamp(19.89/25×100, 0, 100) = 79.56
  + 10 (TAM-expansion bonus — ad-market-share data + 28% YoY revenue growth this quarter
    independently supports it; still excludes the JV/compute-leasing news per §2/§4 of the
    07-28 session's established treatment) → 89.56

Balance Sheet (15%): Net Debt/EBITDA = −$6.596B ÷ $112.282B = −0.05874× (net cash)
  BalanceSheet_Score = clamp(100×(1−(−0.05874)/4), 0, 100) = 100.0
  🚩 Still clamped at the 100.0 ceiling, but net cash collapsed from $22.432B (Q1 2026) to
  $6.596B (Q2 2026) — a ~70% one-quarter decline, driven by ~$25B of new debt issuance to
  fund record capex. Doesn't move the score yet (still deep in net-cash territory), but this
  is the fastest one-quarter deterioration in this line in the ticker's history — worth
  close monitoring; another 1–2 quarters at this pace could flip Meta into net debt.

Moat Signal (15%): 5/5 signals unchanged (market share, brand premium, network effect,
  switching costs, scale cost advantage) — Q2 ad revenue +27% YoY, no erosion evidence → 100.0

FCF Quality (10%): FCF/NI = $40.976B ÷ $68.098B = 60.1721%
  FCFQuality_Score = clamp(((0.601721−0.40)/0.60)×100, 0, 100) = 33.6202
  (Down from 64.6%/41.0 on 07-28 — FCF collapsed on record capex; growth-capex explanation
  still stands per §2's capex-guidance detail, so no hard disqualifier fires — see below.)

Quality Score = 85.0119×0.25 + 100.0×0.15 + 89.56×0.20 + 100.0×0.15 + 100.0×0.15 + 33.6202×0.10
              = 21.2530 + 15.0 + 17.912 + 15.0 + 15.0 + 3.3620
              = 87.5270 → rounds to 87.5
```

**Quality Score = 87.5 — PASSES the 80.0+ gate, but down 2.4 points from 07-28's 89.9 — this ticker's first genuine (non-rounding-precision) quality decline.** Driven by three real, earnings-confirmed inputs: (1) ROIC compression (25.05%→21.17%) as invested capital grew faster than NOPAT amid the AI-capex surge, compounded by a higher guided tax rate (14.5%→16%); (2) net margin compression (32.86%→29.83%) from the Q3 2025 one-off tax charge still sitting in the TTM window plus this quarter's own legal/severance charges; (3) FCF quality decline (64.6%→60.17%) as capex hit a record $31.08B in the quarter. **Still comfortably above the 80.0+ gate — no Phase 04 Quality Watch escalation required** (operating-brief.md's escalation trigger is a drop *below* 80.0, not any decline).

**Hard disqualifier check:**
- FCF/NI <70% for 2+ consecutive years without a documented growth-capex explanation: **does not fire** — the growth-capex explanation (record, guided-up AI infrastructure capex, explicitly not maintenance capex per §2/§4) still applies, arguably more strongly than ever.
- Net Debt/EBITDA over threshold: **does not fire** — still net cash.
- Not FCF-positive 3+ consecutive years: **does not fire** — still FCF-positive (thin, but positive).

---

## 7. META — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.7510/10), 0, 100) = 72.4897
```
→ Contribution: 72.4897 × 0.40 = **28.9959**

**EV/EBIT — 40% weight** (PEG not applicable → 15% redistributed here)
```
EV/EBIT_Score = clamp((17.0589 − 12)/23 × 100, 0, 100) = 21.9953
```
→ Contribution: 21.9953 × 0.40 = **8.7981**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (18.8969 − 23.152)/23.152 × 100 = −18.3791%
FwdPE_Score = clamp(50 + (−18.3791) × 2.5, 0, 100) = clamp(4.0522, 0, 100) = 4.0522
```
→ Contribution: 4.0522 × 0.20 = **0.8104**

**PEG — Fast-Grower test: FAIL** (re-verified §3). Weight redistributed to EV/EBIT (used above).

**Raw weighted score:**
```
= 28.9959 + 8.7981 + 0.8104 = 38.6044
```
**+ Rate Modifier (+10) = 48.6044** *(before the Upside/Downside Modifier)*

---

## 8. META — Upside/Downside Modifier (Expected-Return Modifier)

**Decision: update Base-case EPS to the fresh $30.93 consensus; Bull/Bear EPS and both exit multiples carried unchanged** — same practice as every prior session (see §4 flag 7 re: this growing stale).

**Step 1 — Scenario fair values**

| Scenario | Weight | EPS assumption | Exit PE | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | $40.0 (carried) | 24× | **$960.00** |
| **Base** | 50% | $30.93 (fresh consensus) | 20× | **$618.60** |
| **Bear** | 25% | $28.0 (carried) | 13× | **$364.00** |

```
PW Fair Value = 0.25×960.00 + 0.50×618.60 + 0.25×364.00 = $640.30
```
(Down from 07-28's $648.20 — the Base-case consensus EPS ticked down $31.72→$30.93, consistent with the EPS miss.)

Sanity check (Rule 0 Step 4 / Rule 4): PW FV $640.30 remains well below the $756.95 analyst consensus PT.

Live price ($584.48) remains **below** the PW Fair Value ($640.30, **+9.55% gap**) — continuing the pattern first seen 07-28 (price fell back below FV), though the gap narrowed slightly (was +9.12% on 07-28) as the price partially recovered post-earnings while FV also declined a bit.

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = ($640.30 ÷ $584.48) − 1                    = +9.5504%
Catalyst window = 2 years (unchanged — AI ad-monetization proof points, capex-ROI
                   demonstration; no new specific dated milestone disclosed this call —
                   management explicitly declined to give 2027 capex guidance, so the
                   window basis is unchanged, not extended or shortened)
Annualized gap  = +9.5504% ÷ 2                                = +4.7752%/yr
Intrinsic growth = +12.0%/yr   (carried, unchanged basis)
Shareholder yield = buyback yield + dividend yield (recomputed at fresh market cap $1,489.4761B)
                  = $3.327B/$1,489.4761B + $5.367B/$1,489.4761B = 0.2234% + 0.3603% = +0.5837%/yr
```
```
E (expected annual return) = +4.7752 + 12.0 + 0.5837 = +17.3589%/yr
```

🚩 **Shareholder yield collapsed from +2.4202%/yr (07-28) to +0.5837%/yr** — the single largest input change in this modifier, driven almost entirely by the buyback suspension (§2/§3: $0 repurchases for 3 consecutive quarters). This alone would have pulled `E` down by ~1.84pp had nothing else changed.

**Step 3 — Catalyst/timeline (Rule 10 + Guardrail 1).** Same two standing catalysts as prior sessions (AI ad-monetization proof, capex-ROI demonstration), both still inside the 18–24-month window. **Upside credit fully allowed; the −5 catalyst cap does NOT apply** (E ≥ H, catalyst-guardrail only constrains the case with no catalyst).

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
E = 17.3589% ≥ H → M = −15 × clamp((17.3589 − 10)/15, 0, 1)
                      = −15 × clamp(0.49059, 0, 1)
                      = −7.3589
```
**Upside/Downside Modifier M = −7.3589** — less negative (less attractive) than 07-28's −8.9825, driven almost entirely by the shareholder-yield collapse (the Gap Upside % term actually widened slightly in absolute annualized terms).

---

## 9. META — Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (38.6044) + Rate Modifier (+10) + Upside/Downside (−7.3589)
                       = 41.2455
```
Boundary rule: not a ".X5" (hundredths digit is 4) → standard rounding → **Final Valuation Score = 41.2**

| | Value |
|---|---|
| Raw weighted | 38.6044 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −7.3589 (E = +17.36%) |
| **FINAL VALUATION SCORE** | **41.2** |
| Prior valuation score | 31.3 (07-28) |
| **Quality Score** | **87.5 (down 2.4 from 89.9 — first genuine decline, §6; still PASSES 80.0+ gate)** |

```
Composite Score = 0.50 × (100 − 87.5) + 0.50 × 41.2 = 0.50×12.5 + 0.50×41.2 = 6.25 + 20.6 = 26.85
```
Boundary rule: 26.85 falls exactly on a ".X5" → round **UP** (conservative) → **Composite Score = 26.9**

**Composite Score = 26.9** (up from 20.7 on 07-28 — a real, earnings-driven deterioration in attractiveness, though still comfortably inside the same BUY-Full band). Both the Quality decline (§6) and the Valuation increase (mainly the shareholder-yield collapse, §8, plus the modest richening of EV/EBIT and FCF Yield at a shares-corrected, larger Market Cap) push in the same direction this session — the first time in this ticker's history both scores have moved *against* it in the same window.

---

## 10. META — Action & Category Change

**Valuation Score alone: 31.3 → 41.2** — stays inside the BUY-Standard band (30.0–49.9), but now moves *further from* the BUY-Full boundary (was 1.4pp above it on 07-28; now 11.2pp above it) — a reversal of the multi-session trend of the raw valuation score creeping toward BUY-Full.

**Composite Score: 20.7 → 26.9 → Action band: BUY — Full position 6–8% (Score 0.0–29.9), unchanged band, but a meaningfully less attractive number within it** (now only 3.0pp from the top of the band, vs. 9.2pp of room on 07-28). No action-category change.

**Practical recommendation: HOLD — no automatic fresh capital.** META is an existing holding at **6.43%⚠️** (per holdings.md; see §3 flag on the share-count anomaly), inside the 6–8% full-position band, well under the 15% hard cap.

---

## 11. META — Order Setup (Composite Score in BUY-Full band → required)

Confidence: wide-moat proven compounder (Quality Score 87.5, still high despite this session's real decline) with heavy in-flight AI capex, now funded increasingly via new debt issuance and a suspended buyback program rather than JV structures alone — same conservative 20% MoS used every prior session.

```
[x] Composite Score (drives action band):        26.9   (≤29.9 ✓ — Full-position entry permitted)
[x] Raw Valuation Score (incl. Upside/Downside):  41.2
[x] Expected annual return E / catalyst window:   +17.36% / 2yr
[x] Upside/Downside Modifier applied:             −7.3589
[x] Blended Fair Value (PW, Rule 7):              $640.30  (down from $648.20 — consensus EPS drift)
[x] Margin of Safety %:                           20%
[x] BUY PRICE (limit):     $640.30 × (1 − 0.20)        = $512.24
[x] PRIMARY SELL TARGET:   = Blended FV                = $640.30
[x] BULL-CASE TRIM TARGET: $960.00 × 0.90               = $864.00
[x] STOP LOSS:             $512.24 × (1 − 0.25)        = $384.18   (25% max loss, high-conviction bracket)
[x] Risk/Reward Ratio (base-case target):  ($640.30 − $512.24) ÷ ($512.24 − $384.18) = $128.06 ÷ $128.06 = 1.00:1
[x] Risk/Reward Ratio (bull-case trim target): ($864.00 − $512.24) ÷ $128.06 = $351.76 ÷ $128.06 = 2.75:1
```

Live price ($584.48) is **$72.24 (14.10%) above** the $512.24 buy-price limit — a marginal narrowing from 07-28's 14.55%, continuing the multi-session convergence trend, but still well short of a qualifying entry. **Base-case R/R still exactly 1.00:1 (fails the 2:1 minimum)**, the same recurring shape as literally every META session on record. **Net: no automatic qualifying entry fires this session either** — both the price-limit condition and the R/R condition still fail, unchanged in *kind* from every prior session even though the underlying inputs moved meaningfully this time.

**Position sizing:** META is at **6.43%⚠️** (holdings.md), inside the 6–8% band. Room to the 8% ceiling: **1.57pp**. No forced trim or top-up.

---

## 12. Portfolio Note

META at 6.43% is comfortably under the 15% hard cap (Upgrade 7) and sits within the 6–8% full-position band its Composite Score points to. No portfolio-level action is forced by this score (no trim signal — nowhere near the 70+ trim bands; no forced top-up — R/R and price-limit both still fail). This session does not change the `holdings.md` weight itself, only Last Score/Quality Score/Composite Score/Last Review. **The unresolved 6→5→6 share-count anomaly (override-log.md) remains a separate, open governance issue for this position — not resolved or investigated further by this rescore.** Separately, this session's shares-outstanding *data-source* correction (§3) is about Meta's own total shares outstanding (used to compute Market Cap/EV), not this portfolio's position size — the two are unrelated.

**Consistent with this repo's recurring META pattern: a "BUY — Full position" *score label* has never once, across 9 sessions since 06-12, actually produced a qualifying automatic entry** — the independent price-limit and 2:1 R/R gates have failed every single time, including this session. No BUY, TRIM, or EXIT action actually fires this session; the action-band label is unchanged and continues to be blocked by the same two gates as always.

---

## 13. Next Review Triggers

- **Q3 2026 earnings** — Meta's next scheduled print (typically late October/early November 2026) — will refresh every TTM fundamental in this log and is the natural next checkpoint. Management explicitly declined to give 2027 capex guidance this call, so that revision (if/when it comes) would itself be an independent Rule 9 trigger.
- **Balance sheet watch — the sharpest-deteriorating item this session.** Net cash fell ~70% in one quarter ($22.432B→$6.596B) on ~$25B of new debt issuance. The Balance Sheet sub-score is still clamped at the 100.0 ceiling, but 1–2 more quarters at this pace could flip Meta into a net-debt position and start actually moving the score — worth checking explicitly at the next earnings print even absent a separate trigger.
- **Buy-price / fair-value watch:** live price is 14.10% above the $512.24 buy limit (essentially unchanged from 07-28's 14.55%) — still the closest sustained proximity in this ticker's history, but no closer this session. Base-case R/R remains stuck at exactly 1.00:1.
- **Rate Gate watch:** Step 1 FAILED again, cushion widened slightly (+0.59% vs +0.65% on 07-28) — worth rechecking if the 10Y or the price/EPS mix shifts further.
- **Rule 9 fundamental triggers (standing):** any further guidance revision, management change, material M&A, or a >15% unexplained price move.
- **Shares-outstanding correction (§3) — flagged for a possible `decisions/` entry** to formally record why the total-shares basis changed and to check whether any other framework outputs (e.g. `holdings.md` weight-sum footnotes) reference the old 2.196B figure. Not created this session (out of `/rescore`'s explicit scope), but flagged prominently here and in the watchlist entry.
- **Bull/Bear scenario assumptions ($40.0/$28.0 EPS, 24×/13× exit multiples) — flagged as increasingly stale** (§4 flag 7); worth a dedicated review given two real earnings prints have landed since they were last set.
- **holdings.md's unresolved 6→5→6 META share-count anomaly** — still needs a manual `get_account_trades` follow-up, out of `/rescore`'s scope, tracked in override-log.md.
- **Owner Earnings (Upgrade 1) methodology decision** — still open, at least 11th consecutive session; Meta still discloses no maintenance-vs-growth capex split.

---

## 14. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output; no new terms required this session — the relevant concepts (NOPAT, ROIC, Effective tax rate, Invested Capital, Shareholder yield, Owner Earnings, Dual-class shares, 10-Q, 8-K) were all already on file from prior sessions)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **8-K** | The "current report" a US public company files with the SEC within days of a material event, most often to furnish an earnings press release ahead of the fuller 10-Q/10-K. |
| **10-Q** | The quarterly financial-disclosure report a US public company files with the SEC, containing unaudited financial statements — used here to source Meta's Q2 2026 balance sheet and income statement. |
| **bps / pp (percentage points)** | A direct difference between two percentages, distinct from a "%" change. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists. |
| **Dual-class shares** | A capital structure with two+ classes of common stock (here, Meta's Class A/Class B) — a data-integrity trap when a vendor field captures only the traded class's share count, understating total shares and Market Cap (see §3's correction this session). |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **Effective tax rate** | The actual % of pretax income paid as tax in a period — distinct from the statutory rate; used here (via management's own guided forward rate) to normalize NOPAT/ROIC against a TTM window distorted by a one-off tax charge. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | Debt + Equity used as the ROIC denominator. |
| **Joint Venture (JV)** | A separate legal entity jointly owned/funded by two or more companies for a specific project, often used to push funding (including debt) onto the JV's own balance sheet. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the numerator this framework uses to compute ROIC. |
| **NTM** | Next Twelve Months. |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for moat-building reinvestors (Upgrade 1; unresolved for META, Data Gap #1). |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

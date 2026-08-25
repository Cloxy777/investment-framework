# New Position Evaluation — LLY (Eli Lilly and Company)

**Task type:** NEW POSITION
**Date:** 2026-08-25
**10Y US Treasury Yield:** 4.66% (TradingEconomics, 2026-08-25 — "eased to 4.66% on August 25, 2026, marking a 0.04pp decrease from the previous session")
**Trigger:** Telegram post, `FinnInvestChannel` — reported Eli Lilly launched its weight-loss/diabetes drug "Foundayo" in Britain, its first European launch. Per Rule 0, **the post text is not used as data anywhere below** — it is only the signal to run this evaluation. LLY is **not currently held** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md) — no LLY row) and has **no prior watchlist entry anywhere in the repo** (first-ever `/new-position` pass for this ticker).

Independently verified via WebSearch (not the Telegram post): Eli Lilly launched **Foundayo** (orforglipron, an oral small-molecule GLP-1 agonist) in the UK on **2026-08-24** for weight management and type 2 diabetes, available by private prescription after the UK's medicines regulator (MHRA) authorised it on 2026-08-10 — Britain is the first European market where the pill is available. Priced £100–£120/month self-pay (vs. Mounjaro's £330/month injection); England's NICE (National Institute for Health and Care Excellence) reimbursement assessment for NHS availability is still pending. This is a genuine, dated fundamental/commercial event (first ex-US launch of a major new pipeline asset), so evaluating LLY now — rather than treating the post as noise — is the correct call per this framework's Rule 9 spirit, even though LLY isn't yet a holding.

*Jargon decoded on first use (non-finance reader): TTM = trailing twelve months; NI = net income; ROIC = return on invested capital; NOPAT = net operating profit after tax; EBIT/EBITDA = operating profit (before/also before depreciation & amortization); CAGR = compound annual growth rate; FCF = free cash flow; MHRA = UK's drug regulator; NICE = UK's cost-effectiveness/reimbursement watchdog for the NHS; IPR&D = a one-off acquisition accounting charge (defined in full below).*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price (used)** | **$1,257.42** | IBKR `get_price_snapshot` (contract_id 9160, NYSE), `last.price`, `is_close: false`, timestamp epoch 1787674131 = **2026-08-25T16:08:51Z** |
| Change vs. prior close | **+$10.49 (+0.84%)** | IBKR `change` field |
| Bid/Ask | $1,256.93 / $1,257.54 | IBKR `bid_ask` |
| 52-week range | $708.66 – $1,292.60 | IBKR `misc_statistics` |
| Dividend yield (trailing) | 0.54% | IBKR `dividend_yield` |
| Analyst PT context (bull-case sanity check, Rule 0 Step 4) | Citi $895 (raised from $675, Buy); a separate outlet's 12-month PT $1,480.01 (+17.9% from a lower reference price) | WebSearch, TipRanks / 24/7 Wall St, 2026-08-24 |

---

## 2. Quality Score — Phase 01 (methodology version 2026-06-29, unchanged)

**Sources:** `yfinance` (via a plain-`requests` session — the library's default `curl_cffi` backend failed TLS through this session's egress proxy; a standard-`requests`-backed session was substituted and cross-checked, noted for the record) for TTM financials/cashflow/balance sheet (quarterly data Q3 2025–Q2 2026) and annual FY2022–FY2025 data; WebSearch cross-checks against company press releases (investor.lilly.com, BioPharma Dive, BioSpace) and third-party market-share reporting for the qualitative Moat and Growth-modifier evidence. All figures cross-checked internally (e.g. TTM revenue $79,665.8M sums to `yfinance`'s own `totalRevenue` field of $79,666.0M; TTM net income $26,711.2M matches `netIncomeToCommon` $26,711.0M).

### TTM inputs (Q3 2025 → Q2 2026, USD millions)

| Line | Q3'25 | Q4'25 | Q1'26 | Q2'26 | **TTM** |
|---|---|---|---|---|---|
| Revenue | 17,600.8 | 19,292.0 | 19,799.0 | 22,974.0 | **79,665.8** |
| Gross Profit | 14,592.5 | 15,920.3 | 16,222.0 | 19,706.0 | **66,440.8** |
| EBIT | 7,412.0 | 11,558.8 | 9,778.0 | 12,457.0 | **41,205.8** |
| EBITDA | 7,882.3 | 12,144.5 | 10,287.0 | 12,991.0 | **43,304.8** |
| Net Income | 5,582.5 | 6,637.7 | 7,396.0 | 7,095.0 | **26,711.2** |
| Pretax Income | 7,232.4 | 8,266.2 | 8,850.0 | 9,247.0 | **33,595.6** |
| Tax Provision | 1,649.9 | 1,628.5 | 1,454.0 | 2,152.0 | **6,884.4** |
| Operating Cash Flow | 8,835.4 | 3,224.6 | 5,333.0 | 10,690.0 | **28,083.0** |
| CapEx | 2,807.6 | 2,970.4 | 2,530.0 | 6,215.0 | **14,523.0** |
| FCF (OCF − CapEx) | 6,027.8 | 254.2 | 2,803.0 | 4,475.0 | **13,560.0** |

Latest balance sheet (2026-06-30): Total Debt $54,908M, Cash $8,950M, Net Debt $45,958M, Stockholders' Equity $33,879M.

### Sub-scores

```
Profitability (25%):
  TTM Net Margin = 26,711.2 / 79,665.8 = 33.529%
  Effective tax rate (TTM) = 6,884.4 / 33,595.6 = 20.492%
  NOPAT = EBIT_TTM 41,205.8 × (1 − 0.20492) = 32,761.9
  Invested Capital = Total Debt 54,908 + Stockholders' Equity 33,879 = 88,787
    (this framework's standard NOPAT/Invested-Capital convention — matches
    yfinance's own "Invested Capital" field exactly, 88,787, a strong cross-check)
  ROIC = 32,761.9 / 88,787 = 36.899%
  NetMargin_Component = clamp((33.529/30)×100, 0, 100) = 100.0 (capped)
  ROIC_Component       = clamp((36.899/30)×100, 0, 100) = 100.0 (capped)
  Profitability_Score (uncapped) = (100.0 + 100.0) / 2 = 100.0

  FCF-positivity cap check — annual FCF: FY2022 +$4,600.4M, FY2023 −$3,152.0M
    (see §2a below), FY2024 +$414.0M, FY2025 +$5,964.0M. Two readings of "not
    FCF-positive for 3+ consecutive years" (see §2a — both computed, both fail
    the 80.0 gate regardless):
      Literal cap reading (cap applies unless all 3 of the most recent years
        are individually positive — FY2023 breaks that): Profitability_Score
        CAPPED AT 40.0.
      Rolling-window reading (extending the 2026-08-05 hard-disqualifier
        clarification's logic to this identically-worded cap — cap fires only
        if the 3-year window is uniformly negative; FY2024/FY2025 are positive,
        so it is not): Profitability_Score = 100.0 (uncapped).
  → Primary (literal) reading used below: Profitability_Score = 40.0

Margins (15%): TTM Gross Margin = 66,440.8 / 79,665.8 = 83.399%
  GrossMargin_Score = clamp((83.399/80)×100, 0, 100) = 100.0 (capped)
  Already far above the 40% bonus-eligibility ceiling — no trend bonus applicable.

Growth (20%): Revenue 3yr CAGR, FY2022 $28,541.4M → FY2025 $65,179.0M
  CAGR = (65,179.0/28,541.4)^(1/3) − 1 = 31.687%
  Growth_Score = clamp((31.687/25)×100, 0, 100) = 100.0 (capped)
  TAM/pricing-power modifier moot (already capped) — but strongly documented
    regardless: 60% US GLP-1 market share (up from a Novo-led market a year
    ago), Zepbound ~70% share of new obesity-drug prescriptions, FY2026
    revenue guidance raised to $85.0–87.0B (+30–33% YoY), and the 2026-08-24
    Foundayo UK launch (this session's own trigger) opening a new ex-US
    market. [Yahoo Finance/24-7 Wall St, 2026-05; investor.lilly.com Q2 2026
    release]

Balance Sheet (15%): Net Debt/EBITDA = 45,958 / 43,304.8 = 1.061×
  BalanceSheet_Score = clamp(100×(1 − 1.061/4), 0, 100) = 73.468
  Comfortably clear of the 2.5× hard-disqualifier threshold (no asset-light
    override applicable — LLY is a capital-intensive manufacturer, not
    asset-light).

Moat Signal (15%) — 1 of 5 signals cited TRUE:
  ✓ Market share stable/growing — Eli Lilly holds ~60% of the total US GLP-1
     market (Mounjaro + Zepbound combined), a share that has grown from a
     Novo-Nordisk-led market a year prior; Zepbound alone holds ~70% of new
     obesity-drug prescriptions; Mounjaro is "the market leader in new
     prescriptions among incretin analogs for type II diabetes in both the
     United States and ex-U.S. markets" [Yahoo Finance/24-7 Wall St, TIKR.com,
     2026-05].
  ✗ Brand premium — FALSE. Evidence found runs the opposite direction: Lilly
     has repeatedly CUT LillyDirect self-pay prices — Zepbound vials $349→$299/
     mo (Dec 2025, CNBC), with further per-dose cuts since; Mounjaro flat
     $499/mo, described as "~54% discount off list price." This is
     competitive discounting in a two-player price war with Novo Nordisk, not
     "price increases without volume loss" — the clean signal this checklist
     requires.
  ✗ Network effect — FALSE. No documented two-sided or platform-style
     mechanism found; a branded-pharma manufacturing/distribution model does
     not exhibit this dynamic.
  ✗ Switching costs — FALSE. Evidence found cuts against this signal: PBM
     (pharmacy benefit manager) formulary exclusions — e.g. CVS Caremark
     dropping Zepbound coverage — can force an already-stable patient off
     therapy regardless of clinical response or prior approval, per a 2026
     patient-advocacy source. No countervailing cited mechanism of genuine
     patient/prescriber lock-in was found.
  ✗ Scale cost advantage — FALSE. Lilly's $50B+ committed US manufacturing
     buildout and its lower-complexity "vial strategy" (vs. Novo's
     autoinjector-pen bottlenecks) are real and documented, but no
     cost-per-unit figure versus a smaller competitor was found — industry
     sources explicitly frame both majors as "competing on price and
     formulation advantages rather than emphasizing cost-per-dose
     advantages" [IntuitionLabs, BioPharma Dive, 2026]. Considered but not
     credited, consistent with this framework's evidentiary bar (cf. the
     2026-07-05 NVDA session's CoWoS scale-signal precedent — capacity/
     investment data alone, without a cost-per-unit citation, does not
     qualify).
  Moat_Score = (1/5) × 100 = 20.0

FCF Quality (10%): TTM FCF/NI = 13,560.0 / 26,711.2 = 50.765%
  FCFQuality_Score = clamp(((0.50765 − 0.40)/0.60)×100, 0, 100) = 17.942
```

```
Quality Score (literal cap reading, primary) =
  40.0×0.25 + 100.0×0.15 + 100.0×0.20 + 73.468×0.15 + 20.0×0.15 + 17.942×0.10
  = 10.00 + 15.00 + 20.00 + 11.020 + 3.00 + 1.794
  = 60.8

Quality Score (rolling-window reading, alternate — shown for transparency,
  does not change the outcome) =
  100.0×0.25 + 100.0×0.15 + 100.0×0.20 + 73.468×0.15 + 20.0×0.15 + 17.942×0.10
  = 25.00 + 15.00 + 20.00 + 11.020 + 3.00 + 1.794
  = 75.8
```

**Quality Score = 60.8 / 100.0 (or 75.8 under the alternate reading) — FAILS the 80.0+ gate either way.**

### 2a. Hard disqualifier check (all three)

| Check | Value | Threshold | Result |
|---|---|---|---|
| Not FCF-positive for 3+ consecutive years | FY2023 **−$3,152.0M** (negative), FY2024 +$414.0M, FY2025 +$5,964.0M — window is NOT uniformly negative (2 of 3 years positive) | disqualify only if the current 3-year window is uniformly negative, per the 2026-08-05 rolling-window ruling ([decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md](../decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md)) | ✅ PASS (does not fire) |
| FCF/NI conversion <70% for 2+ consecutive years, no documented growth-capex explanation | FY2023 −60.2%, FY2024 **3.9%**, FY2025 **28.9%** — most recent 2 consecutive years both <70% | disqualify unless growth-capex explanation documented | **Waived** — see below |
| Net Debt/EBITDA over threshold | 1.061× (TTM) | disqualify if >2.5× (standard; no asset-light override applies) | ✅ PASS, comfortably |

**FCF/NI conversion carve-out — documented growth-capex explanation:** LLY's CapEx has escalated sharply and explicitly for new manufacturing *capacity*, not maintenance: FY2022 $2,985.3M → FY2023 $7,392.0M → FY2024 $8,404.0M → FY2025 $10,849.0M → TTM $14,523.0M. This is tied to named, dated, dollar-quantified announcements, not a vague "reinvestment" claim:
- **2025-02-26** — Lilly announced $27B of *new* investment (bringing cumulative US manufacturing commitments since 2020 to **>$50B**) for four new drug-production facilities (three API, one injectables), explicitly stating "the commercial success of Zepbound has played a major role motivating Lilly's manufacturing spending" [BioPharma Dive].
- Named facilities since: $6B Huntsville, AL (announced 2025, construction starting 2026); >$1.2B Puerto Rico oral-medicine capacity expansion; $6.5B Texas API facility; $3.5B Lehigh Valley, PA facility explicitly for "next-gen weight-loss therapies" including retatrutide [investor.lilly.com, BioPharma Dive, StocksToTrade, 2025–2026].

This is the same style of carve-out this framework has applied before (e.g. the 2026-07-10 MU session's escalating, management-guided HBM/DRAM capacity buildout) — an explicit, escalating, named-facility capacity-expansion program, not maintenance capex. **Disqualifier does not fire.**

**Net effect: no hard disqualifier independently fires — this is a pure weighted-score shortfall**, the same pattern as the MELI and MU sessions. The gate fails almost entirely on two sub-scores: **Moat (20.0)** — only "market share" clears this framework's strict 5-signal evidentiary bar, with brand-premium and switching-cost evidence actually cutting the *other* way (price cuts, not increases; payer-side formulary exclusions, not lock-in) — and **FCF Quality (17.9)** — the FCF/NI ratio is genuinely low even though the disqualifier is waived, because the capex is real and immediate cash-flow-suppressing even though it's legitimate and growth-directed.

---

## 3. PEG / Fast-Grower eligibility (for the record — moot given the gate fails)

LLY does **not** qualify as a Fast Grower under this framework's "reliable, non-distorted earnings base" test (2026-06-20 clarification). FY2023 GAAP EPS fell to $5.80 from FY2022's $6.57 — and within that year, **Q3 2023 GAAP EPS was an outright loss of $0.06/share**, driven by a **$2.98B ($3.29/share) acquired IPR&D (in-process R&D) charge** from the DICE Therapeutics, Versanis Bio, and Emergence Therapeutics acquisitions — a documented, dated, one-off distortion [Yahoo Finance/BioSpace/investor.lilly.com Q3 2023 release]. This is exactly the "one-off-distorted EPS does NOT qualify" case the 2026-06-20 clarification describes. Had the gate been cleared, PEG's 15% weight would redistribute to EV/EBIT (40% weight) — noted for a future rescore, not scored here.

---

## 4. Recommendation

**PASS — Quality Score (60.8, or 75.8 under the alternate cap reading) fails the 80.0+ gate. No new position opened. Watchlist only.**

Per [quality-scoring.md](../framework/quality-scoring.md)'s Strict 80.0+ Gate: *"stop — don't proceed to valuation, regardless of how cheap the stock looks."* No Rate Environment Gate, Phase 02 valuation score, or Composite Score is computed as part of this recommendation, consistent with the MELI (2026-08-05) and MU (2026-07-10) precedents for a gate-failing candidate. (A fully-worked, clearly-labeled reference appendix is included below for audit-trail completeness only — see §6 — but it plays no role in the recommendation.)

**What's genuinely notable here, worth surfacing:**
- This is not a "weak business" failure. Profitability, Margins, Growth, and Balance Sheet sub-scores are all at or near their ceiling (100.0, 100.0, 100.0, 73.5) — LLY is, on the numbers that measure current business quality, an exceptional company.
- The gate fails almost entirely on **Moat (20.0)** — this framework's 5-signal checklist is strict by design, and four of the five signals either have no documented mechanism (network effect) or the *evidence actually found points the wrong way* (repeated list-price cuts against "brand premium"; PBM formulary exclusions against "switching costs"). Patent/regulatory exclusivity — arguably LLY's real moat — isn't one of the five checklist categories, a known limitation of this generic checklist worth flagging for a future framework discussion, not silently worked around here.
- **FCF Quality (17.9)** is genuinely low, not just disqualifier-adjacent: even with the hard disqualifier legitimately waived (real, documented growth capex), the TTM FCF/NI ratio (50.8%) means roughly half of accounting profit isn't (yet) showing up as free cash — a real, current fact about the business, not an accounting artifact.
- The Trulicity biosimilar patent cliff (~$7B+ annual revenue, US patent exposure starting 2027) is a documented, dated risk worth tracking on any future re-score, independent of today's gate outcome.

**Next review trigger:** LLY's next quarterly earnings release (Q3 2026, historically early November), or any Rule 9 event (guidance revision, management change, M&A, macro shift, >15% unexplained price move) in the interim. Specifically worth re-testing at that point: (1) whether the FCF/NI ratio is recovering as the manufacturing buildout matures, (2) any new cited pricing-power or switching-cost evidence (e.g. a genuine list-price increase sustained without volume loss, or a payer-lock-in mechanism), and (3) NICE's pending NHS reimbursement decision on Foundayo.

---

## 5. Watchlist & Portfolio Note

New entry created: [watchlist/not-in-portfolio/LLY/LLY-2026-08-25.md](../watchlist/not-in-portfolio/LLY/LLY-2026-08-25.md) — LLY's first-ever watchlist entry. This session does not touch [portfolio/holdings.md](../portfolio/holdings.md) (LLY is not held, and no position is opened). No trade recommended or executed; nothing logged to `decisions/`.

---

## 6. Appendix — Phase 02 reference figures (NOT used for the recommendation; Quality Gate fails)

*Computed for audit-trail completeness and to give a future re-score a documented starting point, exactly as several existing holdings in [holdings.md](../portfolio/holdings.md) carry a "(ref only, gate fail)" Composite Score. No Composite Score is computed — per [valuation-scoring.md](../framework/valuation-scoring.md), "Composite Score isn't computed for, and doesn't rescue, a company failing the quality gate."*

**Rate Environment Gate:** Forward PE 26.62× (live price $1,257.42 ÷ forward EPS $47.234) → Earnings Yield 3.756%. Spread vs. 10Y Treasury (4.66%) = **−0.90%**, below +1.5% → **Step 1 fails, +5 flag**. 10Y yield sits in the 3.5–5% bracket → **Step 2 Rate Regime Modifier +5**. Combined: **+10**.

**Valuation sub-scores** (PEG inapplicable per §3 — its 15% weight redistributed to EV/EBIT, making EV/EBIT 40%):

| Sub-score (weight) | Value | Sub-score |
|---|---|---|
| FCF Yield (40%) | FCF $13,560.0M ÷ Market Cap $1,121.29B = 1.209% | 87.9 |
| EV/EBIT (40%) | EV $1,167.25B ÷ EBIT $41,205.8M = 28.33× | 71.0 |
| Forward PE (20%) | 26.62× vs. reconstructed 5yr range 28.36×–112.64× (20 quarters, `yfinance` `get_earnings_dates`) — **below even the 5yr low**, clamps to floor. *Flag: the high end of this range is distorted by the Q3 2023 IPR&D-charge-driven EPS collapse (§3), which mechanically inflated trailing PE in late 2023/2024; doesn't change this result since Forward PE already sits below the low end regardless of the high.* | 0.0 |

Raw weighted score = 87.9×0.40 + 71.0×0.40 + 0.0×0.20 = **63.6**. Plus Rate Gate (+10) = **73.6** before the Upside/Downside Modifier.

**Upside/Downside Modifier:** DCF (3-stage, WACC 8% central ±1% per Rule 2, terminal growth 2.5%) scenario per-share values: Bull $1,329.14, Base $829.15, Bear $356.38 (Stage-1 growth/FCF-margin assumptions explicitly modeled, not sourced consensus — flagged; FY2026 revenue base $86.0B is company guidance, sourced). Multiples-Based Value (peer set: JNJ, MRK, PFE, ABBV, BMY, NVS, AZN — NVO excluded, its `yfinance` EBIT figure is implausible/data-quality-flagged): Peer EV/EBIT (median 26.19×) → $1,158.66/sh; Peer Forward PE (median 15.535×) → $733.78/sh; averaged → $946.22/sh. Blended FV (40% DCF + 60% Multiples, per scenario) → PW Fair Value (25/50/25) = **$902.11/sh**. Gap vs. live price = **−28.26%**; annualized over a 2yr catalyst window (Trulicity US patent exposure begins 2027) = **−14.13%/yr**; + intrinsic growth (Base-case Y1–Y5 revenue CAGR) 18.97%/yr + shareholder yield 1.14%/yr → **E = +5.98%**. E<H(10%) and E≥0 → **M = +5×(10−5.98)/10 = +2.0**.

**Reference Valuation Score = 63.6 + 10 + 2.0 = 75.6** (would map to "TRIM 25–30%" / "do not buy" per the Phase 03 action table if it were being used — it is not, per the gate policy above).

---

## 7. Glossary

*(Pulled from [glossary.md](../framework/glossary.md); 7 new terms added this session — Foundayo (orforglipron), MHRA, NICE, Incretin, Performance margin (Lilly), Most-Favored-Nation (MFN) pricing, Loss of Exclusivity (LOE))*

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate. |
| **EBIT / EBITDA** | Operating profit, before/also-before depreciation & amortization. |
| **Effective tax rate** | Tax provision ÷ pretax income for the period. |
| **FCF / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Net Income, a cash-quality check on accounting profit. |
| **Fast Grower** | Peter Lynch's term for EPS growth >15%/yr for 3+ years — this framework's PEG-eligibility trigger. |
| **Foundayo (orforglipron)** | Eli Lilly's oral, small-molecule GLP-1 receptor agonist for obesity and type 2 diabetes — a pill (unlike injectable Mounjaro/Zepbound), branded Foundayo. Launched in the UK on 2026-08-24 following MHRA approval on 2026-08-10, Britain being the first European market where it's available — the trigger event for this session. *(New term.)* |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of its weighted score, independent of the score itself. |
| **Incretin** | A class of gut hormones (including GLP-1 and GIP) that stimulate insulin release after eating; "incretin portfolio" is how Eli Lilly refers to its combined Mounjaro/Zepbound/Foundayo franchise, since tirzepatide (Mounjaro/Zepbound) activates both the GLP-1 and GIP receptors while orforglipron (Foundayo) targets GLP-1 alone. *(New term.)* |
| **Invested Capital** | Debt + equity put to work in a business — this session's convention (Total Debt + Stockholders' Equity, no cash netting) matches `yfinance`'s own "Invested Capital" field exactly. |
| **IPR&D (Acquired In-Process Research & Development) charge** | A GAAP-mandated, non-cash, immediate expense for the fair value of in-process R&D programs acquired via M&A — a real, dollar-quantified, one-off item tied to deal-closing timing. LLY recognized a $2.98B ($3.29/share) IPR&D charge in Q3 2023 (DICE Therapeutics, Versanis Bio, Emergence Therapeutics acquisitions), turning that quarter's GAAP EPS negative and disqualifying FY2023 as a "clean" earnings-base year for this framework's Fast-Grower/PEG test. |
| **Loss of Exclusivity (LOE)** | The point at which a drug's patent and/or regulatory market-exclusivity protection expires, opening the door to generic or biosimilar competition and typically causing a sharp, fast revenue decline for the originator. Eli Lilly's Trulicity (dulaglutide, ~$7B+ annual revenue) faces US patent/LOE exposure starting 2027 — a documented, dated risk for this ticker's future re-scores. *(New term.)* |
| **MHRA (Medicines and Healthcare products Regulatory Agency)** | The United Kingdom's national medicines regulator — the UK's equivalent of the US FDA. Authorised Foundayo (orforglipron) on 2026-08-10, ahead of its 2026-08-24 UK commercial launch. *(New term.)* |
| **Most-Favored-Nation (MFN) pricing** | A drug-pricing policy requiring a manufacturer to charge a government payer (here, US Medicare/Medicaid) no more than the lowest price it charges in any other comparable country. Under a 2026 agreement with the Trump administration, Medicare/Medicaid prices for Zepbound and Mounjaro were set at $245/month (Medicare beneficiary co-pay $50/month) — a real, negotiated pricing constraint relevant to this ticker's future margin and moat assessment, separate from LillyDirect's self-pay discounting. *(New term.)* |
| **NICE (National Institute for Health and Care Excellence)** | England's health cost-effectiveness watchdog, which must assess a drug before it can be reimbursed on the NHS (the UK's public health system) — distinct from MHRA's separate safety/efficacy approval. Foundayo cleared MHRA approval but still awaits a NICE reimbursement decision as of this session. *(New term.)* |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the ROIC numerator. |
| **PBM (Pharmacy Benefit Manager)** | A company administering prescription-drug benefits for health plans/employers, negotiating rebates and reimbursement — able to exclude a drug from a plan's formulary. |
| **Performance margin (Lilly)** | Eli Lilly's own non-GAAP operating-margin presentation basis (comparable in spirit to "Adjusted EBITDA," "AOI," or "Core" elsewhere in this glossary) — guided to 49.0%–50.5% for full-year 2026, raised from a prior 47.0%–48.5% range. This framework scores off GAAP EBIT/EBITDA, not this company-reported non-GAAP figure; shown here only as guidance context, not a scored input. *(New term.)* |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02 valuation scoring. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples or stale data. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **TTM (Trailing Twelve Months)** | The most recent four reported quarters combined. |

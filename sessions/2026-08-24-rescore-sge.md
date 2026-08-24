# RESCORE — SGE.L (The Sage Group plc)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-08-24
**10Y US Treasury Yield:** 4.71% (TradingEconomics.com) — for reference only; see scope note below, the Rate Environment Gate is not reached this session.

> ⚠️ **Scope note — SGE is not a current holding**, same situation as this session's earlier ABNB rescore. Last touched via `/new-position` on [2026-06-19](2026-06-19-new-position-sge.md) (old 1–10 scale, Score 21.1 "Very Cheap" → **ENTER NOW**, but no order was ever placed — nothing in `holdings.md` or `decisions/`). SGE has carried an existing `watchlist/not-in-portfolio/SGE/` entry since, flagged stale against **two** methodology versions (2026-06-20 Upside/Downside Modifier, 2026-06-29 Quality Score + 80.0+ gate) per [STALE.md](../watchlist/STALE.md). This run computes SGE's **first-ever Quality Score** — and, as shown below, that score changes the outcome materially: **SGE now fails the 80.0+ Quality Gate**, which stops this session before the Rate Environment Gate or a Phase 02 valuation score is computed at all, per [quality-scoring.md](../framework/quality-scoring.md)'s explicit "don't proceed to valuation... regardless of how cheap the stock looks" rule. This is the same convention already applied to other not-in-portfolio gate-fail tickers (e.g. LULU, CHTR, 2026-06-29) — no Composite Score, no order setup.

**Last review on record:** SGE **Score 21.1 ("Very Cheap")** on the old 1–10 scale — 2026-06-19, [sessions/2026-06-19-new-position-sge.md](2026-06-19-new-position-sge.md). No Quality Score existed at that time (added 2026-06-29). Recommendation then: **ENTER NOW** (never executed).

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **1,096.75p** (£10.9675) | IBKR `get_price_snapshot` (contract_id 129028068, LSE), `last`, intraday live tick (`is_close: false`) during regular trading hours. Cross-checked against Yahoo Finance `regularMarketPrice`: 1,096.00p — within 0.07%, consistent. |
| 52-week range | 771.66p – 1,181.00p | IBKR `misc_statistics` |
| Price vs. 2026-06-19 review (812.60p) | **+35.0%** | Not an unexplained Rule 9 move — H1 FY26 results (beat-and-raise, 21 May 2026) and an active buyback are the documented drivers, see §3. |
| Analyst consensus PT (Rule 0 Step 4, sanity check) | Mean **1,119.94p** / Median 1,150p (18 analysts, high 1,349p / low 850p) | Yahoo Finance `financialData` — current price sits just below the mean target, roughly in line with consensus (unlike ABNB earlier this session, no material divergence flagged here). |

---

## 2. Data Gaps / Flags

1. **Same `yfinance`/`curl_cffi` transport issue as earlier sessions this run** — worked around with the `requests.Session()` + cookie/crumb fix, pulling `quoteSummary` and `fundamentals-timeseries` endpoints directly.
2. **Yahoo's `defaultKeyStatistics.forwardPE` field is a units-mismatch bug for this ticker**, returning a nonsensical 1,902.9× — it divides a pence-denominated price (1,096p) by a GBP-denominated EPS estimate (£0.576, i.e. 57.6p) without normalizing units. **Not used.** `summaryDetail.forwardPE` (19.03×) uses consistent units and is corroborated independently below. Same general class of "vendor field silently mixes bases" issue flagged for this same ticker in the June session (there it was the `+1y` vs `0y` EPS-estimate-period issue).
3. **TTM "underlying" (non-GAAP) figures are rolled forward, not directly disclosed as a single TTM line.** Sage discloses "underlying" results only at FY (Sep year-end) and H1 (Mar) — no quarterly cadence. This session's TTM figures = FY2025 (year to Sep 2025) − H1 FY2025 (est. by backing out the disclosed YoY growth rate from H1 FY2026's reported figure) + H1 FY2026 (Mar 2026, directly disclosed). This is the same rolling-window approach used elsewhere in this framework when only annual/half-year cadences are available; the H1 FY2025 comparatives are back-solved from disclosed YoY growth rates (revenue +11%, operating profit +15%, PAT +10%, EPS +16%) rather than an independently-sourced H1 FY2025 print — flagged as a modeling approximation, not a primary-source figure.
4. **Invested Capital denominator (£2,196M) is FY2025 year-end (Sep 2025), not rolled forward to the Mar 2026 balance sheet** — no quarterly invested-capital figure available from the vendor. A modest timing mismatch against the TTM-basis EBIT numerator, flagged rather than papered over (consistent with how this same class of mismatch was handled in the June session's EV/EBIT calc, and doesn't change the gate outcome below by any plausible margin — see §5 robustness table).
5. **Net debt basis:** Yahoo's H1 FY26 balance-sheet-derived net debt (Total Debt £2,022M − Total Cash £518M = **£1,504M**) is used, cross-checked against Sage's own directly-disclosed leverage ratio (net debt/LTM underlying EBITDA = **2.0×**, off a disclosed £742M LTM underlying EBITDA figure — implying ≈£1,484M net debt). The two are within 1.3% of each other — good corroboration, not a real discrepancy.

---

## 3. Fundamental Changes Since Last Review (2026-06-19)

- **H1 FY2026 results (six months to 31 March 2026, reported 21 May 2026):** underlying revenue +11% YoY to £1,363M, underlying operating profit +15% to £326M (23.9% margin), underlying PAT +10% to £224M, underlying basic EPS +16% to 23.7p. ARR +11% to £2,727M. Renewal rate by value 102% (up from 101% H1 FY25).
- **FY2026 guidance raised**: organic total revenue growth for FY26 now expected "above 9%"; margins expected to keep trending up.
- **Capital returns stepped up materially**: £600M in share buybacks announced across H1 FY26 (a further £300M tranche approved March 2026); interim dividend +8% to 8.05p.
- **Leverage has risen, now at the framework's monitoring threshold on the company's own disclosed basis**: net debt/LTM underlying EBITDA = **2.0×**, up from 1.5× a year earlier — the company's own words, not this session's derivation — driven by the buyback pace. Sage's own stated medium-term target range is 1–2×, so this sits at the top of, not above, management's own guardrail — but it is a real, continuing increase from the already-elevated 2.0× flagged as a "tightening trend to monitor" in the June session (net debt itself has grown further since; the ratio holding at 2.0× reflects LTM EBITDA growing roughly in step).
- **Sage is leaning into agentic AI as a strategic response, not passively exposed to it** — active rollout of "Sage Copilot" and AI agents across Intacct/HCM/payroll workflows (April/May 2026 announcements), which meaningfully updates the June session's "AI-native bookkeeping disruptors" bear-case framing from a passive threat to a two-sided contest. The competitive threat from agile, lower-priced rivals (Xero, Intuit QuickBooks) remains real and unresolved either way.
- **First-ever Quality Score computed for SGE** (methodology added 2026-06-29, postdates the June session) — and it fails the 80.0+ gate. See §4.

---

## 4. Quality Score (Phase 01 — full recompute, first time for SGE)

**Hard disqualifier checks:**

| Check | SGE Value (underlying/TTM basis) | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years | FY2024 141.2%, FY2025 122.2%, TTM 115.5% — every year comfortably ≥70% | Fail if <70% for 2+ yrs | ✅ CLEAR |
| Net Debt/EBITDA over threshold | 2.0× (company-disclosed, LTM underlying EBITDA basis) | <2.5× standard | ✅ CLEAR — though at strategy.md's separate, stricter <2× Phase 01 pre-screen ceiling (a different, non-hard-disqualifier threshold — see the quality-scoring.md/strategy.md inconsistency flagged in prior sessions, not resolved here) |
| Not FCF-positive for 3+ consecutive years | Positive every year, FY2022–FY2025 and TTM | Fail if not | ✅ CLEAR |

No hard disqualifier fires. Proceeding to the weighted score.

**Sub-scores** (all figures GBP; TTM = FY2025 rolled forward with H1 FY2026, see §2 flag 3):

**Profitability (25% weight)**
```
Net Margin (TTM, underlying PAT £443.4M ÷ underlying revenue £2,648.1M) = 16.7%
ROIC = NOPAT ÷ Invested Capital
  EBIT (TTM, underlying) = £642.5M
  Effective tax rate on underlying PBT (H1 FY26, company-disclosed) = 24% (unchanged YoY)
  NOPAT = 642.5 × (1 − 0.24) = £488.3M
  Invested Capital (FY2025 year-end, latest available) = £2,196M
  ROIC = 488.3 / 2,196 = 22.2%

NetMargin_Component = clamp((16.7/30)×100) = 55.8
ROIC_Component       = clamp((22.2/30)×100) = 74.1
Profitability_Score  = (55.8 + 74.1) / 2 = 65.0
```
(Cross-check: June session's independently-derived ROIC was 22.29% — near-identical, confirms quality here hasn't materially drifted on this axis.)

**Margins (15% weight)**
```
Gross Margin (TTM) = 92.56%   (FY2025 annual: 92.72% — flat, stable, not a new trend either way)
GrossMargin_Score = clamp((92.56/80)×100) = 100.0  (clamped)
```

**Growth (20% weight)**
```
Revenue 3yr CAGR = (£2,513M FY2025 / £1,947M FY2022)^(1/3) − 1 = 8.9%
Growth_Score (base) = clamp((8.9/25)×100) = 35.5
```
TAM/pricing-power modifier — **+10 applied**, cited: H1 FY26 revenue growth (+11% YoY) accelerated *above* the trailing 3yr CAGR base, FY26 guidance was raised (not cut) to "above 9%," and the 102% renewal-rate-by-value (up from 101%) is direct evidence of net-positive pricing/cross-sell power within the existing customer base, not just new-logo growth. No structural-deceleration evidence found this session to weigh against it.
```
Growth_Score = clamp(35.5 + 10) = 45.5
```

**Balance Sheet (15% weight)**
```
Net Debt/EBITDA = 2.0× (company-disclosed, LTM underlying EBITDA basis)
BalanceSheet_Score = clamp(100 × (1 − 2.0/4)) = 50.0
```

**Moat Signal (15% weight)**

| Signal | Result | Evidence (cited) |
|---|---|---|
| Market share stable or growing | ✅ TRUE | ~40% of the UK SME accounting-software market (TechFinitive/Kalkine coverage, 2026) — clear market-leader position in Sage's core/home market; UK & Ireland revenue +10% YoY (latest FY) corroborates a stable-to-growing position there. |
| Brand premium | ✅ TRUE | Renewal rate by value 102% (H1 FY26, up from 101% H1 FY25) — net-positive revenue retention within the existing base, evidence of pricing power/cross-sell without customer loss. |
| Network effect | ❌ FALSE | No cited two-sided-marketplace-style mechanism found — Sage's partner/app ecosystem is a platform extension, not established this session as a true network effect. |
| Switching costs | ✅ TRUE | Deeply embedded accounting/payroll/tax-compliance workflows (data migration, staff retraining, regulatory-continuity risk on switching) — a well-documented SaaS-ERP mechanism, further evidenced by the sustained >100% renewal rate (low realized attrition). |
| Scale cost advantage | ❌ FALSE | No cited cost-per-unit data vs. smaller competitors (Xero, Intuit QuickBooks) this session — not invented. |

```
Moat_Score = (3/5) × 100 = 60.0
```

**FCF Quality (10% weight)**
```
FCF/NI (TTM, underlying) = £512.0M / £443.4M = 115.5%
FCFQuality_Score = clamp(((1.155 − 0.40)/0.60)×100) = 100.0  (clamped)
```

### Quality Score — Final

```
Quality Score = 65.0×0.25 + 100.0×0.15 + 45.5×0.20 + 50.0×0.15 + 60.0×0.15 + 100.0×0.10
              = 16.25 + 15.00 + 9.10 + 7.50 + 9.00 + 10.00
              = 66.85 → rounds to 66.8
```

# **Quality Score: 66.8 — FAILS the 80.0+ gate** (a clear fail, not a knife-edge one — see robustness check below)

### Robustness check — unlike this session's earlier ABNB result, this is not a close call

| If instead... | Quality Score | Gate result |
|---|---|---|
| **As computed above** | **66.8** | **FAIL** |
| No TAM/pricing-power modifier applied to Growth (0 instead of +10) | 64.8 | FAIL |
| Moat_Score = 40.0 (2/5 signals) | 63.8 | FAIL |
| Both of the above, most conservative reading | 61.8 | FAIL |
| Most generous plausible reading (both judgment calls resolved favorably, as computed) | 66.8 | **Still FAIL, by 13.2 points** |

No combination of this session's genuinely-contestable judgment calls gets SGE within reach of 80.0. The gap is driven structurally, not by any single flagged assumption: Profitability (65.0), Growth (45.5), and Balance Sheet (50.0) all sit well below their respective ceilings — a solid, profitable business, but not the exceptional-quality tier this framework's deliberately strict gate is calibrated to admit.

---

## 5. Why this session stops here

Per [quality-scoring.md](../framework/quality-scoring.md): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all. Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* SGE fails at 66.8. Consistent with how this framework has already handled other not-in-portfolio gate-fail tickers (e.g. LULU, CHTR, 2026-06-29): **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, no order setup this session.**

This is a meaningful reversal of the June 2026-06-19 "ENTER NOW — Very Cheap" call — not because the June valuation math was wrong (it wasn't re-litigated here), but because the framework itself has since added a quality bar that the June session had no way to check SGE against. The June session's own qualitative notes (§9 there) already flagged the demanding growth/leverage backdrop; the Quality Score engine now makes that judgment explicit and numeric, and the answer is a clean fail — a genuinely good business (92.6% gross margin, 22.2% ROIC, market-leading position in its core market) that falls short of this framework's deliberately high bar mainly on growth (8.9% 3yr CAGR, well under the 25% ceiling the sub-score is calibrated against) and leverage (2.0×, at the midpoint of the balance-sheet sub-score's 0–4× range).

**Action: PASS** — does not qualify for entry consideration under the current methodology, independent of price.

---

## 6. Next Review Trigger

- **FY2026 full-year results** (expected ~mid-November 2026) — mandatory Rule 9 re-score; the next point where a full-year revenue-CAGR/growth recompute could plausibly move the Growth sub-score, and where net debt/EBITDA post-buyback-program will be visible on an audited basis.
- **Any >15% unexplained move** from 1,096.75p (Rule 9).
- **A second, larger step-up in growth** — if organic revenue growth sustainably clears the mid-teens% (vs. today's high-single-digit trailing CAGR / low-double-digit current run-rate), the Growth sub-score would move meaningfully; worth an explicit re-check at the next result.
- **Net debt/EBITDA rising past 2.0×** without a matching EBITDA increase — would pull the Balance Sheet sub-score down further, moving in the wrong direction for the gate.
- **A credible, evidenced AI-native bookkeeping disruption signal specific to Sage's SMB base** — the qualitative bear case flagged in June, not yet resolved either way.

---

## 7. Glossary

| Term | Meaning |
|---|---|
| **ARR (Annual Recurring Revenue)** | The annualized run-rate value of a company's recurring subscription revenue at a point in time. |
| **CAGR (Compound Annual Growth Rate)** | The smoothed annual growth rate that would take a value from its starting point to its ending point over a period, accounting for compounding. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / Earnings Before Interest, Taxes, Depreciation and Amortization — operating-profit measures. |
| **Gross Margin** | Revenue minus cost of revenue, as a percentage of revenue. |
| **Hard disqualifier** | One of three Quality Score conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company regardless of its weighted Quality Score. None fired for SGE this session. |
| **Invested Capital** | The total capital (debt + equity, net of cash) invested in a business — the denominator in a ROIC calculation. |
| **Moat / Moat Signal** | A durable competitive advantage; this framework's 5-point scored checklist (market share, brand premium, network effect, switching costs, scale cost advantage). |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; this framework's primary balance-sheet-risk gate. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT adjusted for taxes — the numerator in a ROIC calculation. |
| **Quality Score / Quality Gate** | This framework's 0.0–100.0 continuous score grading profitability, margins, growth, balance sheet, moat, and FCF quality; a company must score 80.0+ to proceed to valuation scoring at all. |
| **Renewal rate (by value)** | The percentage of a subscription customer base's revenue value retained (and, above 100%, expanded via cross-sell/price increases) at renewal — a standard SaaS pricing-power/retention metric. |
| **ROIC (Return on Invested Capital)** | NOPAT ÷ Invested Capital — how efficiently a company turns invested capital into after-tax operating profit. |
| **Rule 0 / Rule 9** | This framework's standing instructions to always fetch a live price first (0), and to force re-valuation on specific fundamental triggers — quarterly earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained move (9). |
| **TTM (Trailing Twelve Months)** | The most recent 12-month period, reconstructed here from FY2025 annual results rolled forward with the H1 FY2026 half-year print (see §2 flag 3). |
| **Underlying (non-GAAP) results** | A company's own adjusted results excluding items it deems non-recurring or non-operational — used here as the primary basis (per this framework's Rule 6) consistent with the June 2026-06-19 session's precedent, with statutory/GAAP figures shown as cross-checks where relevant. |

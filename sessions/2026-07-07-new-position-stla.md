# New Position Evaluation — STLA (Stellantis N.V.)

**Task type:** NEW POSITION
**Date:** 2026-07-07
**10Y US Treasury yield:** 4.48% (FRED `DGS10`, 2026-07-06 close — most recent published value as of this session) — cited for header consistency with the standard session template only; **not actually invoked**, since Phase 01 fails before the Rate Environment Gate is reached (see Section 3).
**Trigger:** Telegram post (`t.me/tarasguk`, post #11308, ~19:36 UTC, 2026-07-07): "🇮🇹 $STLA Fiat запускає продажі у 🇺🇸 електрокара за $14 тис" (Fiat launches US sales of an electric car for $14K — model "Topolino," 74km range) — names $STLA via cashtag, resolving unambiguously to **Stellantis N.V.** (NYSE: STLA), Fiat's parent company. STLA had **no prior watchlist entry anywhere** (checked both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)) — actioned per `/telegram-scan`'s "no watchlist entry exists at all → `/new-position`" rule, same precedent as OUST/AMD/CRCL/HNHPF/AAPL. Per Rule 0, **the triggering post's own text is never used as a financial input** anywhere below — every figure is independently sourced and cited; the post is only the reason this ticker was looked at. (The Fiat Topolino EV-launch claim itself is not independently re-verified here since it doesn't affect the Phase 01 outcome — see Section 3.)

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers, before any valuation work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 463647466, NYSE — "STELLANTIS NV") | **$5.67** | Last trade, not halted. |
| IBKR `change` field | −$0.13 / **−2.24%** intraday (prior close $5.80) | Below Rule 9's >15% unexplained-move threshold — N/A here regardless, since this is a new-position evaluation, not a re-score of an existing holding. |
| IBKR `misc_statistics` (52-week) | Low **$5.56** (13-week and 26-week low too) / High **$12.21** / Open-52w **$9.90** | Price is sitting just $0.11 above its 52-week low, and **down ~53.6% from its 52-week high** — directionally consistent with (not proof of, but not contradicted by) the fundamental distress picture in Section 3. |
| Cross-check: stockanalysis.com (via research agent, fetched same day) | $5.65, −2.59%, mkt cap $16.50B, 2.90B shares out, fwd PE 5.47×, analyst consensus "Hold" (avg PT $9.19) | Within 0.4% of the IBKR figure — consistent, no discrepancy flagged. |

**Live price used throughout this session: $5.67 (IBKR).**

---

## 2. Data Source Note — IFRS 20-F filer, no SEC 10-K; yfinance unavailable (documented environment failure) — SEC XBRL + primary press used instead

`yfinance` failed in this environment with the documented `curl_cffi` TLS-impersonation error — confirmed on both STLA and a control ticker (AAPL), consistent with the AAPL/CHTR/WSE/AMD/CDR/CRCL/OUST/NKE/HNHPF precedent already on record in this repo. Per Rule 0's documented fallback, fundamentals were sourced directly from:

- **SEC EDGAR XBRL company facts** (`data.sec.gov/api/xbrl/companyfacts/CIK0001605484.json`, CIK confirmed via SEC EDGAR company search) — Stellantis files a **[Form 20-F](../framework/glossary.md)** as a foreign private issuer, most recently for **FY2025** (filed 2026-02-26, accession 0001605484-26-000021). All figures are **as-filed under [IFRS](../framework/glossary.md), reported in EUR** (`ifrs-full` taxonomy) — Stellantis does not file a US-GAAP 10-K or a 10-Q equivalent (semi-annual 6-K + annual 20-F cadence only). No EUR→USD conversion was applied (flagged as a cross-holding comparability gap, not invented).
- **Stellantis's own FY2025 and H1 2025 results press releases** (stellantis.com/media.stellantis.com) and secondary business press (Detroit News, CBS News, Politico/E&E News, CarEdge, CNBC, Axios, Fox Business) for qualitative Growth/Moat evidence — cited individually below.

Every figure below is cited to one of these sources; nothing was estimated or invented. Where a figure could not be cleanly retrieved (an industrial-only, ex-captive-financing net-debt breakout), it's flagged explicitly rather than guessed — see 3.2 Balance Sheet note.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

Most recent audited annual period = **FY2025** (the closest available TTM equivalent for a 20-F filer). **Flag: FY2025 is a one-off "kitchen-sink" restructuring year** — €25.4B of charges (EV product-plan write-downs, warranty provisions, workforce restructuring) were booked, mostly through cost of sales and operating expense, materially distorting Profitability/Margins/FCF-Quality inputs vs. the pre-crisis run rate. FY2023/FY2024 figures are shown alongside FY2025 throughout so the underlying trend isn't lost, but the framework's formulas are computed on the strict FY2025 TTM figure as instructed.

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | STLA data | Verdict |
|---|---|---|
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FCF (CFO − CapEx, SEC XBRL): FY2023 €7,761M / **FY2024 −€9,525M** / **FY2025 −€12,637M**. Net Income: FY2023 €18,625M / FY2024 €5,520M / FY2025 −€22,332M. FY2024 ratio: −9,525/5,520 = **−172.6%**. FY2025: both FCF and NI negative — the resulting ratio (+56.6%) is a **spurious artifact of dividing two negatives**, not a meaningful conversion figure. **Both of the two most recent consecutive years are effectively far below the 70% reference point**, and no growth-capex explanation applies — the negative FCF is driven by restructuring charges and an EV-strategy write-down/reversal, not capacity expansion for growth (contrast with the HNHPF session's genuine, documented AI-server-capex carve-out). | **FIRES.** |
| **Not FCF-positive for 3+ consecutive years** | FCF: FY2021 (not directly needed, but FY2023 shown for trend) €7,761M positive / **FY2024 −€9,525M** / **FY2025 −€12,637M**. The two most recent fiscal years are both negative — STLA is **not** FCF-positive on any trailing 3-consecutive-year window ending in FY2025. (Stellantis's own narrower non-GAAP "Industrial Free Cash Flow" KPI was also negative, −€4.5B, for FY2025 — directionally consistent.) | **FIRES.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | Net Debt (Borrowings − Cash, SEC XBRL): FY2025 €45,947M − €30,146M = **€15,801M** (positive net debt). EBITDA (EBIT + D&A add-back): FY2025 −€26,254M + €6,981M = **−€19,273M** (negative). The ratio is mathematically undefined/degenerate with a negative denominator — **not** the favorable "net cash, ratio doesn't apply" edge case seen in the OUST session (which had zero debt); here the company carries real net debt (€15.8B) against negative operating cash profit, the worst combination the ratio is meant to flag. Treated conservatively (Section 3.2, BalanceSheet_Score = 0.0) rather than let the formula's literal arithmetic (a negative-over-negative producing a large positive number) score this favorably. **Conglomerate rule** ([strategy.md](../framework/strategy.md) line 18): the €45,947M `Borrowings` figure is the fully consolidated IFRS balance-sheet total, which already includes Stellantis Financial Services' captive-financing debt — already consolidated per the rule, no add-back needed. An industrial-only (ex-SFS) breakout could not be cleanly extracted from search results this session — flagged as a data gap, not invented. | **Directionally fails** (not cleanly computable as a clean ratio, but the underlying position — net debt against negative EBITDA — is unambiguously poor; not relied on alone since the two disqualifiers above already fire independently). |

**Two independent hard disqualifiers fire outright** (FCF/NI conversion, FCF-positivity), with the Net Debt/EBITDA condition directionally consistent with (not contradicting) that conclusion. Per [quality-scoring.md](../framework/quality-scoring.md): *"Hard disqualifiers — fail regardless of weighted score."* The weighted score is still computed below in full per this framework's "show every calculation, no black-box outputs" standard.

### 3.2 Sub-scores (all six, per the weighted formula)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (FY2025) = −22,368/153,508 = **−14.57%** (net income attributable to parent; consolidated basis −14.55% is materially identical) → NetMargin_Component = clamp((−14.57/30)×100, 0, 100) = **0.0**. ROIC (FY2025) — NOPAT/Invested Capital, shown in full: EBIT −€26,254M, pretax loss −€26,605M, tax benefit −€4,273M → effective tax rate 16.06% → NOPAT = −26,254×(1−0.1606) = **−€22,037M**. Invested Capital = Borrowings €45,947M + Equity (incl. NCI) €54,001M − Cash €30,146M = **€69,802M**. ROIC = −22,037/69,802 = **−31.6%** → ROIC_Component = clamp((−31.6/30)×100, 0, 100) = **0.0**. Profitability_Score = (0.0+0.0)/2 = 0.0; the FCF-positivity cap (≤40.0) doesn't bind since the raw score is already at the floor. *(Context only, not scored: FY2023 ROIC 27.4%, FY2024 ROIC 5.9% — the FY2025 figure is a severe one-off collapse, not the multi-year baseline, but it is the strict TTM figure the formula calls for.)* | **0.0** |
| **Margins (15%)** | Gross Margin (FY2025) = (153,508−155,627)/153,508 = **−1.38%** (cost of sales exceeded revenue) → GrossMargin_Score = clamp((−1.38/80)×100, 0, 100) = **0.0**. 3yr trend: FY2021 19.73% → FY2022 19.64% → FY2023 20.12% → FY2024 13.08% → **FY2025 −1.38%** — **structurally contracting, the documented opposite of expansion** (driven by €25.4B in charges booked largely through cost of sales). No +10 trend bonus (that requires expansion). | **0.0** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 €179,592M → FY2025 €153,508M) = (153,508/179,592)^(1/3) − 1 = **−5.10%** → base = clamp((−5.10/25)×100, 0, 100) = **0.0**. TAM-expansion/pricing-power evidence check: **none found supporting expansion** — instead, documented evidence of structural deceleration/distress: FY2025 net loss €22.3B with €25.4B in charges (Stellantis FY2025 Results press release, stellantis.com); 2026 dividend suspended, up to €5B in hybrid bonds authorized to preserve the balance sheet (same source); Adjusted Operating Income (**[AOI](../framework/glossary.md)**) swung from +€8.6B (FY2024) to −€842M (FY2025); US tariff cost ~€1.0B FY2025 (Politico/E&E News, CBS News); Europe (EU30) market share down ~2pp in H1 2025 (Stellantis H1 2025 press release, media.stellantis.com); US Q1 2025 sales −12% YoY with discount-led "Employee Pricing for Everyone" and "Freedom of Choice Pricing" programs to clear above-average dealer inventory (CarEdge, Detroit News) — the documented opposite of pricing power; new CEO Antonio Filosa's $70B turnaround plan (May 2026 Capital Markets Day) itself targets **positive industrial cash flow only by 2027** and explicitly reverses the prior all-EV-first strategy (CNBC, Axios, Fox Business) — i.e. management's own framing is "not yet turned around." **−10 modifier applies** (documented structural deceleration), though it doesn't move the already-floored score: Growth_Score = clamp(0.0 − 10, 0, 100) = **0.0**. | **0.0** |
| **Balance Sheet (15%)** | Net Debt/EBITDA (FY2025): Net Debt **+€15,801M**, EBITDA **−€19,273M** — degenerate ratio (negative EBITDA with positive net debt), see 3.1. The formula's literal arithmetic (clamp(100×(1−ND/EBITDA/4))) would compute a positive net debt divided by a negative EBITDA as a negative ratio, producing a **spuriously high** score (~100+, clamped to 100) — the opposite of what the underlying financial position (real debt, no operating cash profit to service it) warrants. Scored conservatively at the floor instead, consistent with how this framework treats degenerate-ratio edge cases on their economic substance rather than literal formula output (contrast with OUST's *net-cash* edge case, which was legitimately favorable). | **0.0 (flagged override — see note above)** |
| **Moat Signal (15%)** | 0 of 5 signals cleared the cited-evidence bar — see evidence table below. | **0.0** |
| **FCF Quality (10%)** | FCF/NI (FY2025) = −12,637/−22,332 = +56.6% **on paper**, but this is a spurious artifact of dividing two negative numbers (see 3.1) — not a real "56.6% of profit converts to cash" reading when there is neither profit nor cash generation. Scored conservatively at **0.0** rather than let the sign cancellation produce a favorable-looking mid-range score; FY2024's genuinely computable ratio (−172.6%) would also clamp to 0.0 regardless. | **0.0 (flagged override — see note above)** |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | Europe (EU30) share down ~2pp in H1 2025 vs. H1 2024, with only a partial +127bps recovery in H2 2025 after new launches; US Q1 2025 sales −12% YoY (Stellantis H1 2025 press release, media.stellantis.com) | **FALSE** |
| Brand premium | Discount-led strategy documented in 2025 ("Employee Pricing for Everyone," "Freedom of Choice Pricing Program") to clear above-average dealer inventory — the opposite of pricing power (CarEdge, Detroit News) | **FALSE** |
| Network effect | No two-sided-marketplace or user-growth-driven mechanism found or applicable — a mass-market auto OEM | **FALSE** |
| Switching costs | No documented mechanism found — a vehicle purchase is a discrete transaction with no material lock-in/integration cost cited | **FALSE** |
| Scale cost advantage | Company cites a self-reported ~€5B/yr synergy target from platform/powertrain consolidation and joint purchasing, but this is a **company-claimed target, not realized cost-per-unit data** vs. smaller competitors — doesn't meet the framework's "cited cost-per-unit data" evidentiary bar | **FALSE** |

### 3.3 Final weighted Quality Score

```
Quality Score = (0.0 × 0.25) + (0.0 × 0.15) + (0.0 × 0.20) + (0.0 × 0.15) + (0.0 × 0.15) + (0.0 × 0.10)
              = 0.0
```

**0.0 < 80.0 — fails the gate**, at the absolute floor. This is the most decisive Phase 01 failure on record in this repo to date — every one of the six sub-scores independently lands at 0.0, and two of the three hard disqualifiers fire outright on top of that. The result is not sensitive to any judgment call made in this session (the Balance Sheet/FCF Quality conservative overrides, the moat "scale cost advantage" evidentiary bar, or the growth-CAGR window choice) — reversing any single one of them would not move the total off the floor, since every other sub-score independently already sits at 0.0.

### Result: **Phase 01 FAIL**

Stellantis is currently in the middle of a severe, company-acknowledged financial reset: a €22.4B FY2025 net loss driven by €25.4B in restructuring/write-down charges, a suspended dividend, negative free cash flow for two straight years, contracting (now negative) gross margins, shrinking revenue, losing market share on both sides of the Atlantic, and a brand-new CEO whose own turnaround plan targets *return* to positive industrial cash flow only by 2027 — i.e. management's own guidance describes a company not yet at the bottom of its cycle, let alone recovering. Nothing here contradicts the Fiat Topolino EV-launch headline that triggered this look — a genuinely cheap, low-cost EV launch is plausibly part of the very turnaround plan being described — but a single new-model launch doesn't offset a company-wide quality picture this weak on this framework's specific quantitative bar.

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**PASS. Do not open a position.** No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this decisively.

The stock's own price action (down ~54% off its 52-week high, sitting at a fresh 52-week low) is directionally consistent with, not contradicted by, this session's fundamental findings — this isn't a case of "quality company, market being irrationally pessimistic"; the market's re-pricing and this framework's Quality Score point the same direction.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) H1 2026 interim results (first reported period fully inside new CEO Antonio Filosa's turnaround plan) — expected as a 6-K, no confirmed date found this session; (b) a full fiscal year returning to positive free cash flow and/or positive net income; (c) a sustained, multi-quarter gross-margin re-rating back toward the ~20% pre-2024 baseline (not just the absence of further one-off charges); (d) a management change or material M&A; (e) resolution of the reported US tariff exposure (a trade-policy change, not a company-specific event, but material to STLA's US-built-vehicle economics); (f) a >15% unexplained price move.
- Absent any of the above, future Telegram mentions of Stellantis/Fiat/Jeep/Chrysler/Ram/STLA should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **AOI (Adjusted Operating Income)** — Stellantis's own non-GAAP operating-profit measure, excluding one-off items like restructuring and EV write-downs; this framework scores off the filed IFRS operating result, not this self-reported figure.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation & Amortization — a rough proxy for cash operating profit, used in the Net Debt/EBITDA leverage ratio.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; a ratio below 70% for 2+ consecutive years is this framework's FCF Quality hard disqualifier unless a documented growth-capex explanation exists (none applied here — see Section 3.1).
- **Form 20-F** — The annual report US-listed foreign private issuers (non-US companies like Stellantis) file with the SEC — the international equivalent of a US 10-K.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. One of this framework's Quality Score Margins sub-score inputs.
- **Hard disqualifier** — One of three Quality Score conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company regardless of its weighted Quality Score — see [quality-scoring.md](../framework/quality-scoring.md). Two of the three fire independently for STLA (Section 3.1).
- **IFRS (International Financial Reporting Standards)** — The accounting standard Stellantis (and most non-US companies) use for audited financial statements, as opposed to US GAAP — figures used as-filed here, not converted.
- **Invested Capital** — The total capital (debt + equity, netted for cash) put to work in a business — the denominator in a ROIC calculation.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. STLA's is degenerate/undefined this period (negative EBITDA against positive net debt), treated conservatively as a fail rather than let the formula's arithmetic score it favorably.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NCI (Noncontrolling Interest)** — The portion of a consolidated subsidiary's equity that belongs to outside shareholders rather than the parent company — included in the Equity figure used in this session's Invested Capital calculation.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — operating profit after a tax adjustment but before financing costs; the numerator this framework uses to compute ROIC.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. STLA scores **0.0** — the floor.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (STLA does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price (and primary financial data) before any valuation work — never infer or invent it.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).

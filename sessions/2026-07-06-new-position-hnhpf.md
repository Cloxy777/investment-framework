# New Position Evaluation — HNHPF (Hon Hai Precision Industry Co., Ltd. / "Foxconn Technology Group")

**Task type:** NEW POSITION
**Date:** 2026-07-06
**10Y US Treasury yield:** 4.38% (most recent value on record in this repo, per the 2026-06-30 CRCL session — cited for header consistency with the standard session template only; **not actually invoked**, since Phase 01 fails before the Rate Environment Gate is reached — see Section 3)
**Trigger:** Telegram post reporting Foxconn's revenue +40%, driven by pivoting from Apple-product assembly to Nvidia AI-server manufacturing (said to now be over half its revenue). The reporting entity is **Hon Hai Precision Industry Co., Ltd.** ("Foxconn Technology Group" / commonly "Foxconn" in media), Taiwan-domiciled, primary listing **TWSE:2317**. HNHPF (the IBKR-tradeable OTC PINK Reg S GDR, contract_id 339808287, country_code US) is used as the canonical ticker throughout this session per instruction. **Not** to be confused with two separate, smaller, legally distinct IBKR-listed entities: Foxconn Industrial Internet (601138, Shanghai A-share) or Foxconn Technology Co Ltd (TWSE:2354) — neither is the flagship parent the trigger post describes. HNHPF has **no prior watchlist entry anywhere** under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). Per Rule 0, **no claim from the triggering post is used as a financial input anywhere below** — every figure in this session is independently sourced and cited; the post is only the reason this ticker was looked at. (The post's own "AI servers now over half of revenue" framing is separately, independently corroborated in Section 3's Growth sub-score — from company/press sources, not the post itself.)

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any valuation work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 339808287, PINK — "HON HAI PRECISION-GDR REG S") | **$14.6175** | Last trade, flagged `is_close: true`. Session run pre-market (11:22 UTC / ~07:22 ET, before the 13:30 UTC US market open) — no trade had yet printed today, so this is the last available trade, corroborated below. |
| IBKR daily price history (`ONE_MONTH`, `ONE_DAY` bars) | Close **$14.62** on 2026-07-02 (most recent bar in the series — no bar exists yet for the 2026-07-06 session, consistent with pre-market timing) | This directly corroborates the snapshot's $14.6175 last-trade figure — not stale/prior-session-note data, but the actual most recent trade on this thinly-traded OTC GDR. |
| Bid/ask | Empty at fetch time (`{}`) | No live two-sided quote available pre-market for this thin OTC line — expected for a low-volume Reg S GDR before the primary Taipei/NY session overlap. |
| 52-week range (IBKR `misc_statistics`) | low **$10.68** / high **$20.26** | Current price sits well off the 52-week high, roughly mid-range. |
| Native listing cross-reference | TWSE:2317 (contract_id 37928714) — **not independently re-quoted this session**; HNHPF used as the sole canonical price per instruction | Noted per task instructions as a valid cross-reference path, not used as a second price source here since it isn't necessary for this session's outcome (see Section 3 result). |

**Live price used throughout this session: $14.6175 (HNHPF).**

---

## 2. Data Source Note — Taiwan filer, no SEC filings; yfinance not attempted (documented environment failure) — secondary aggregator + primary press used instead

Hon Hai is a **Taiwan-domiciled company that files with Taiwan's MOPS (Market Observation Post System) / TWSE**, not SEC EDGAR — it is not a US-domestic filer, and the HNHPF GDR is unsponsored, so there is no 10-K/20-F to pull. Per this documented data gap and the repeated `yfinance` `curl_cffi` TLS-impersonation failure precedent already established across AAPL/CHTR/WSE/AMD/CDR/CRCL/OUST/NKE sessions in this repo, `yfinance` was not separately re-attempted this session (would be expected to fail identically and add no new information) — fundamentals were sourced directly from:

- **stockanalysis.com** (TPE:2317 financials, balance sheet, cash flow statement, and ratios pages) — a reputable secondary aggregator, explicitly named as a Rule-0-valid source in this task's instructions, for GAAP-comparable annual income statement, balance sheet, and cash flow figures, FY2021–FY2025.
- **Hon Hai / Foxconn Technology Group's own press releases** (honhai.com/foxconn.com press center — Q1 2026 and FY2025/4Q25 results releases) and **Chairman Young Liu's public statements**, relayed via reputable secondary business press (DigiTimes, BigGo Finance, tech-insider.org, DD News/ANI News wire, ad-hoc-news.de), for the Growth sub-score's TAM-expansion evidence (AI server / cloud-networking revenue mix shift, capex guidance, AI server market share).
- **valueinvesting.io** — cited for Pegatron's (TWSE:4938) gross margin, used as a Moat Signal cross-reference (scale cost advantage).

Every figure below is cited to one of these sources. No required Phase 01 input was invented or estimated; where a figure could not be found (e.g. a directly-disclosed maintenance-vs-growth CapEx split for Upgrade 1 Owner Earnings purposes), it is flagged explicitly rather than guessed (see Section 3.2 Profitability/FCF Quality notes).

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | HNHPF data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF (Operating Cash Flow − CapEx, stockanalysis.com cash flow statement): FY2021 **−190,508M TWD** (negative) / FY2022 **+11,773M** / FY2023 **+333,808M** / FY2024 **+29,690M** / FY2025 **+53,089M**. **FCF-positive for 4 consecutive years (FY2022–FY2025).** | **PASS — does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard / 4× asset-light)** | Net Debt/EBITDA is **negative (net cash)** every year shown: FY2025 **−0.88×**, FY2024 −1.26×, FY2023 −1.70×, FY2022 −0.47×, FY2021 −0.94× (stockanalysis.com ratios page). Cross-checked via balance sheet: Cash $1,016,440M + Short-Term Investments $569,899M − Total Debt $1,286,837M ≈ **+$299,502M net cash** (FY2025), consistent with stockanalysis's own "Net Cash (Debt)" line of $302,134M (small variance = other minor liquid-asset lines). | **PASS — does not fire (best-case: net cash position, not net debt).** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FCF/NI: FY2021 n/m (FCF negative) / FY2022 **8.32%** (11,773/141,483) / FY2023 **234.9%** (333,808/142,098 — a one-year working-capital-driven spike) / FY2024 **19.44%** (29,690/152,705) / FY2025 **28.03%** (53,089/189,354). **FY2024 and FY2025 — the two most recent consecutive years — are both well below 70%.** **Documented growth-capex explanation found and used to waive this disqualifier**: CapEx has risen every year (FY2021 $92,296M → FY2025 $173,763M) and management has explicitly, publicly tied this to **AI-server production capacity expansion** — Chairman Young Liu: current AI data-center rack output "over 1,000 racks/week," targeting **2,000 racks/week by end-2026**; company guiding **capex up >30% in 2026** specifically for AI/cloud infrastructure capacity (sources: DD News/ANI wire, 2026-05-15; Foxconn Q1 2026 results press release). This is a genuine, independently-sourced (not from the trigger post), documented growth-capex narrative, not a one-off accounting item — **carve-out applied, disqualifier waived.** | **Waived per documented growth-capex carve-out** — does not independently stop the session (the continuous FCF Quality sub-score below still reflects the poor conversion ratio directly). |

**No hard disqualifier independently fires** (one condition technically matched but the text's own carve-out applies, and is used here with the citation shown). This is a judgment call, flagged explicitly per operating-brief.md's "show your reasoning" requirement — the underlying weak FCF/NI conversion is still fully reflected in the FCF Quality sub-score (3.2) rather than silently discounted.

### 3.2 Sub-scores (all six, per the weighted formula)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (FY2025) = 189,354M / 8,103,105M = **2.337%** (stockanalysis.com income statement) → NetMargin_Component = clamp((2.337/30)×100) = **7.79**. ROIC (FY2025, stockanalysis.com ratios page) = **11.98%** → ROIC_Component = clamp((11.98/30)×100) = **39.93**. *(Note: stockanalysis's separate "statistics" page shows a slightly different TTM ROIC of 11.07% — the 11.98% FY2025-annual figure from the ratios page is used here for consistency with the other FY2025-annual-basis figures throughout; both are the vendor's own computed ROIC, not independently re-derived via NOPAT/Invested-Capital by this session, since an effective-tax-rate figure needed for that re-derivation wasn't separately sourced — flagged for transparency.)* Profitability_Score = (7.79 + 39.93)/2 = **23.86** (no FCF-positivity cap — 4yr positive streak shown in 3.1). | **23.86** |
| **Margins (15%)** | Gross Margin (FY2025) = 498,161M/8,103,105M = **6.15%** (stockanalysis.com). GrossMargin_Score = clamp((6.15/80)×100) = **7.69**. 3yr/5yr trend: FY2021 6.04% → FY2022 6.04% → FY2023 6.30% → FY2024 6.25% → FY2025 6.15% — **flat/noisy within a ~0.3pp band, not a structural expansion** (in fact the most recent year, FY2025, is *down* from FY2024). **No +10 trend bonus applies.** | **7.69** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $6,626,997M → FY2025 $8,103,105M) = (8,103,105/6,626,997)^(1/3) − 1 = **+6.93%** → base = clamp((6.93/25)×100) = **27.72**. **Documented TAM-expansion evidence** (independently sourced, not from the trigger post): Hon Hai's own Q1 2026 and FY2025/4Q25 results press releases and Chairman Young Liu's public statements report AI-server rack shipments +300% QoQ in a recent quarter, cumulative AI-server revenue reaching "NT trillion-dollar scale," and the Cloud & Networking segment (now >40% AI-server-driven) projected to grow from ~40% to ~50%+ of total company revenue by Q4 2026 (up from Smart Consumer Electronics' declining ~46%→38% share) — against a backdrop of ~$725B in combined 2026 AI capex from the four major North American hyperscalers, with Foxconn's AI-server assembly market share climbing toward 55–60% (sources: DigiTimes 2025-12-08; BigGo Finance; tech-insider.org; ad-hoc-news.de). This independently corroborates (without relying on) the trigger post's own framing. **+10 applied.** Growth_Score = 27.72 + 10 = **37.72**. | **37.72** |
| **Balance Sheet (15%)** | Net Debt/EBITDA (FY2025) = **−0.88×** (net cash — see 3.1). BalanceSheet_Score = clamp(100×(1−(−0.88)/4)) = clamp(122.0) = **100.0**. | **100.0** |
| **Moat Signal (15%)** | See evidence table below — **2 of 5 signals** cleared the cited-evidence bar. (2/5)×100 | **40.0** |
| **FCF Quality (10%)** | FCF/NI (FY2025) = 53,089/189,354 = **28.03%** → clamp(((0.2803−0.40)/0.60)×100) = clamp(−19.9) = **0.0**. (FY2024's 19.44% would score identically at 0.0 — the ratio has been below the 70% reference point in both of the two most recent years, per 3.1's disqualifier discussion; the growth-capex carve-out waives the *hard-fail* trigger but does not — and should not — inflate this continuous sub-score.) | **0.0** |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | EMS industry share **>40%**, more than 2.5× #2 Pegatron's ~15% (multiple secondary sources, Dec 2025–2026); AI-server assembly share specifically cited climbing toward **55–60% in 2026** | **TRUE** |
| Brand premium | Explicitly contradicted by secondary sourcing: "pricing power is limited in commodity-like assembly"; contract/EMS work is described as thin-margin and price-competitive, not brand-premium-driven | **FALSE** |
| Network effect | No two-sided-marketplace or user-growth-driven mechanism — a contract electronics manufacturer, not a platform | **FALSE** |
| Switching costs | Evidence found cuts **against**, not for, this signal: reporting explicitly states Apple ("Foxconn's main customer") is **"diversifying its manufacturing supply chain away from sole suppliers"** — the opposite of durable lock-in. General "deep tooling expertise" commentary about China's manufacturing ecosystem broadly is not a company-specific, cited switching-cost mechanism. | **FALSE** |
| Scale cost advantage | Gross margin comparison as a cost-efficiency proxy: Hon Hai **6.15%** (FY2025) vs. #2-scale peer Pegatron's **4.09%** (valueinvesting.io) — a modest but real, cited per-unit-cost-efficiency gap consistent with Hon Hai's >2.5× larger scale. Flagged as an indirect proxy (gross-margin differential) rather than literal disclosed unit-cost data, since no direct cost-per-unit breakdown was found this session. | **TRUE** (flagged as proxy evidence) |

### 3.3 Final weighted Quality Score

```
Quality Score = (23.86 × 0.25) + (7.69 × 0.15) + (37.72 × 0.20) + (100.0 × 0.15) + (40.0 × 0.15) + (0.0 × 0.10)
              = 5.965 + 1.1535 + 7.544 + 15.0 + 6.0 + 0.0
              = 35.66 → 35.7 (rounded to nearest 0.1)
```

**35.7 < 80.0 — fails the gate**, and fails it by a wide margin (44.3 points short) — decisively, not a borderline call. The result is not sensitive to any of this session's judgment calls (the ROIC-source ambiguity, the moat "scale cost advantage" proxy-evidence flag, or the FCF/NI hard-disqualifier carve-out) — none of those, resolved the other way, would move the weighted score anywhere close to 80.0.

### Result: **Phase 01 FAIL**

Hon Hai/Foxconn is a genuinely fast-improving, well-capitalized business riding a real and independently-documented AI-server manufacturing boom (Growth sub-score 37.7, driven by a legitimate +10 TAM modifier; Balance Sheet a clean 100.0 net-cash position; a real, if modest, scale-driven Moat edge). But it is, at its core, a **contract electronics manufacturer (EMS)** — a business model with structurally thin margins (gross margin ~6%, net margin ~2.3%) regardless of how fast its revenue mix shifts toward higher-value AI-server work. Those two sub-scores alone (Profitability 23.86, Margins 7.69) — reflecting a business model, not a temporary dip — are what the strict 80.0+ Quality Score gate is specifically designed to catch: a company can be growing quickly, well-financed, and even gaining moat-relevant scale, and still not clear this framework's bar for "high quality" if its underlying unit economics are this thin.

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring.

This is not a verdict that the "Foxconn pivoting to Nvidia AI-server manufacturing" story reported in the trigger post is false or unimportant — it's real, independently corroborated, and shows up cleanly in the Growth sub-score. It is a verdict that a structurally thin-margin contract manufacturer does not become a "high quality" business (per this framework's specific definition) just because its growth is faster and its balance sheet is clean — the Profitability and Margins sub-scores are the framework doing exactly the job it's designed to do.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) a sustained, multi-year structural gross-margin re-rating (not just mix shift) that would meaningfully move the Margins/Profitability sub-scores toward the 40%/15% Phase 01 reference points; (b) a quarterly earnings release or guidance revision; (c) a management change or material M&A; (d) further developments from the 2026 Foxconn cyberattack (reported theft of Apple/Nvidia-related data) noted in passing during this session's research — a potential data-security/customer-relationship risk not otherwise scored here and worth independent monitoring if it escalates; (e) a >15% stock-price move with no identified cause.
- Absent any of the above, future Telegram mentions of Foxconn/HNHPF/2317 should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation & Amortization — a rough proxy for cash operating profit, used in the Net Debt/EBITDA leverage ratio.
- **EMS (Electronics Manufacturing Services)** — The contract-manufacturing industry Hon Hai/Foxconn operates in: companies that assemble electronics on behalf of brand owners (e.g. Apple, Nvidia) rather than selling products under their own brand. Structurally thin-margin and capital-intensive.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; a ratio below 70% for 2+ consecutive years is this framework's FCF Quality hard disqualifier unless a documented growth-capex explanation exists (as applied here — see Section 3.1).
- **GDR (Global Depositary Receipt)** — A certificate representing shares of a non-US company, traded outside that company's home market (here, HNHPF trades over-the-counter in the US representing Hon Hai's Taipei-listed shares) — the non-US-specific analog of an ADR. "Reg S" (Regulation S) denotes a GDR issued/traded under the SEC's exemption for offerings outside the US, typically thinner/less liquid than a sponsored US-listed ADR.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. One of this framework's Quality Score Margins sub-score inputs.
- **Hard disqualifier** — One of three Quality Score conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company regardless of its weighted Quality Score — see [quality-scoring.md](../framework/quality-scoring.md). The FCF/NI conversion disqualifier carries an explicit carve-out for a documented growth-capex explanation, applied in this session (Section 3.1); the other two do not fire independently.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **MOPS (Market Observation Post System)** — Taiwan's official corporate-disclosure/regulatory-filing system (run by the Taiwan Stock Exchange), the Taiwanese equivalent of the US SEC's EDGAR — where Hon Hai (TWSE:2317) files as a domestic Taiwan issuer, rather than with the SEC.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. A negative figure means net cash, not net debt (Hon Hai's case here).
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. HNHPF scores 35.7.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (HNHPF does not make this list.)
- **QoQ** — Quarter-over-Quarter — a growth-rate comparison against the immediately preceding quarter, rather than the same quarter a year earlier (YoY).
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price (and primary financial data) before any valuation work — never infer or invent it.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).

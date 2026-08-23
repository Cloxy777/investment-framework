# New Position Evaluation: AFRM (Affirm Holdings, Inc.) — 2026-08-23

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Ticker:** AFRM — NASDAQ, IBKR contract_id 465119069
**Company:** Affirm Holdings, Inc. — buy-now-pay-later (BNPL) point-of-sale consumer credit / specialty finance fintech (originates, holds, sells, and securitizes installment loans; also issues the Affirm Card)
**Fiscal year end:** June 30 (fiscal Q4/FY2026 spans April–June 2026)
**10Y US Treasury yield:** 4.74% (FRED `DGS10`, 2026-08-21 close) — recorded for completeness only; this session stops before the Rate Environment Gate would apply (see §3)
**First-use jargon decode:** see closing Glossary (§6)

---

## 0. Why this session exists — trigger source, and watchlist check

A Telegram post (channel author's own earnings-week watchlist commentary) named AFRM among BNPL names being monitored "for credit risk indicators / rising delinquencies as a potential credit-shock signal." **This text is not financial data — it is only the reason this session was triggered.** Per this repo's standing convention, a first-ever mention of a ticker with no existing watchlist entry triggers a full `/new-position` evaluation regardless of the mention's substance, and regardless of whether the post describes a Rule 9 event.

**Watchlist check performed before assuming no entry exists** (per this session's explicit instructions, after a sibling BRK.B evaluation earlier today found the "no entry exists" premise wrong due to a folder-naming mismatch): `ls` and `find -iname "*afrm*"` against both `watchlist/in-portfolio/AFRM/` and `watchlist/not-in-portfolio/AFRM/` returned **no matches anywhere in the watchlist tree**. AFRM is also absent from [holdings.md](../portfolio/holdings.md). This is confirmed to be a genuine first-ever evaluation — proceeding with the full flow.

Independently confirmed via SEC EDGAR and Affirm's own investor-relations page: Affirm's Q4/full-year FY2026 results are scheduled for **2026-08-27** (4 days after this session) — not yet reported. The most recent complete reporting period available is **Q3 FY2026 (quarter and nine months ended 2026-03-31)**, filed via 10-Q on 2026-05-07. **The triggering post's framing (credit risk / delinquencies) is not used as a financial input anywhere below** — see §4 for what Affirm's own disclosed delinquency data actually shows.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

Contract confirmed via `search_contracts("AFRM")`: contract_id **465119069**, NASDAQ, "AFFIRM HOLDINGS INC" — the correct primary US listing (other results returned were the MEXI cross-listing and an unrelated leveraged single-stock ETF "AFRU" — neither used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$77.43** | IBKR `get_price_snapshot`, `last` field, contract_id 465119069. `is_close: false`, `halted: false` — timestamp resolves to 2026-08-21 23:37 UTC (Friday evening print); today (Sunday 2026-08-23) markets are closed, so this is the most recent price obtainable via a live fetch attempt, consistent with the AXP/SCHW 2026-07-19 Sunday-trigger precedent. |
| Change vs. prior close | +$2.38 (+3.17%) | IBKR `change` |
| Prior close | $75.05 | IBKR `prior_close` |
| 52-week high / low | $100.00 / $42.10 | IBKR `misc_statistics` |
| 13-week / 26-week high | $86.80 / $86.80 | IBKR `misc_statistics` |
| Open 52 weeks ago | $74.29 | IBKR `misc_statistics` |
| Dividend yield | 0.0% (no dividend) | IBKR `dividend_yield` |
| US 10Y Treasury yield | 4.74% | FRED `DGS10`, 2026-08-21 |

$77.43 sits roughly in the middle of the 52-week range ($42.10–$100.00) — context only, not scored. No order-setup arithmetic is performed this session (see §3 for why).

**Shares outstanding:** 294,357,801 Class A + 40,540,764 Class B = **334,898,565** (as of 2026-05-01, per 10-Q cover page; both classes carry identical economic rights, differing only in votes-per-share). **Market cap** = $77.43 × 334,898,565 ≈ **$25.93B**.

---

## 2. Data Sourcing

`yfinance` was not attempted given its documented SSL breakage since 2026-07-07 (repo precedent). **Primary sources used throughout:**
- **SEC XBRL `companyconcept` API** (`data.sec.gov`, CIK 0001820953) for `NetCashProvidedByUsedInOperatingActivities`, `PaymentsToAcquirePropertyPlantAndEquipment`, and `NetIncomeLoss` — audited, tagged, company-filed figures, fiscal-year-labeled by the SEC's own structured data (not a vendor's re-derivation).
- **Affirm's own Q3 FY2026 10-Q** (filed 2026-05-07, accession 0001628280-26-032294, fetched directly from `sec.gov`) for the Condensed Consolidated Statements of Operations, Balance Sheet, Cash Flow Statement, and debt-note disclosures.
- **stockanalysis.com** (WebFetch) for supplementary/derived figures (forward PE, PEG, EV/EBITDA multiple) — every figure that mattered to a hard-disqualifier conclusion was independently cross-verified against the primary sources above before being relied upon (see §4).
- **Affirm's own Q3 FY2026 shareholder letter / 8-K** (2026-05-07) for GMV, active consumers, and delinquency-rate disclosures (qualitative context, §4.4).

**Data-quality note:** a WebSearch query for FY2022–FY2024 operating cash flow returned an AI-synthesized answer with fiscal-year labels that did **not** match the SEC XBRL structured data (values were shifted by one year relative to the correct labels). This was caught by cross-checking against the XBRL API directly and is **not** used anywhere below — flagged here as a caution about trusting search-engine-synthesized financial summaries over structured primary sources, consistent with "never invent or estimate financial data."

---

## 3. Phase 01 — Quality Score: Hard Disqualifier Check

Per [quality-scoring.md](../framework/quality-scoring.md), three hard disqualifiers fail a company **regardless of weighted score**. Given this session's explicit instruction to check these "carefully" for a lending/fintech balance sheet rather than forcing a mechanical fit, each is shown in full below.

### 3.1 — FCF/Net Income conversion ratio <70% for 2+ consecutive years (without a documented growth-capex explanation)

| Fiscal Year | Operating Cash Flow | CapEx | FCF | Net Income | FCF/NI |
|---|---|---|---|---|---|
| FY2024 | $450.138M | $159.296M | $290.842M | **−$517.757M** | not meaningful — NI negative |
| FY2025 | $793.909M | $192.189M | $601.720M | **+$52.186M** | **1,152.9%** |

(All figures: SEC XBRL `companyconcept`, primary-sourced — see §2.)

Only one of the two most recently completed fiscal years has a Net Income base positive enough for this ratio to be meaningful in the sense the check intends (catching cash-flow-quality problems, not the absence of GAAP profit itself). That one computable year (FY2025) clears 70% by more than 16x over. **This disqualifier does NOT fire** — there is no 2-consecutive-year run below 70% (there's zero years below 70% among the computable ones).

### 3.2 — Net Debt/EBITDA over threshold (2.5× standard, or 4× under the Upgrade 5 asset-light override)

**This is the genuine judgment call flagged up front, per this session's task instructions.** Affirm's income statement, unlike a bank/broker (AXP, SCHW, JPM, Citigroup, SoFi precedent), **does** carry a real GAAP "Operating income (loss)" line — so EBIT/EBITDA are computable in principle. The open question is what counts as "debt" for a company that originates and holds loans on its own balance sheet.

**TTM (Apr 2025–Mar 2026) EBITDA build** (all primary-sourced from the Q3 FY2026 10-Q and the FY2025 10-K, cross-verified against stockanalysis.com's TTM figures):
```
TTM Operating Income = Q4 FY2025 ($57.877M) + 9mo ended Mar 2026 ($269.716M) = $327.593M
TTM D&A              = Q4 FY2025 ($64.019M)  + 9mo ended Mar 2026 ($215.985M) = $280.004M
TTM EBITDA           = $327.593M + $280.004M = $607.597M
```
(Cross-check: stockanalysis.com's own EV/EBITDA multiple of 52.44× against its stated EV of $33.12B implies EBITDA ≈ $631.6M — within ~4% of this session's independently-built figure, likely reflecting a slightly different EBITDA/adjustment convention. This session uses its own primary-sourced $607.6M build.)

**Debt breakdown as of 2026-03-31** (Q3 FY2026 10-Q, primary):
| Component | Balance | Recourse to Affirm's general credit? |
|---|---|---|
| Convertible senior notes, net | $1,128.617M | Yes — genuine corporate debt |
| Notes issued by securitization trusts | $5,327.589M | **No** — VIE structure, creditors "have no recourse to the general credit of Affirm" (10-Q/10-K disclosure) |
| Funding debt (warehouse facilities) | $2,417.705M | **No** — same non-recourse VIE structure |
| **Total debt** | **$8,873.911M** | |
| Cash and cash equivalents | $1,723.413M | — |

This non-recourse structure is independently confirmed by the company's own disclosures (§2), and further supported by the cash-flow statement: purchases/originations of **loans held for investment** ($33.4B, 9mo FY2026) sit in **investing** activities, not operating — meaning Affirm's reported operating cash flow is not itself distorted by loan-book growth the way it was for JPM/Citigroup (where loan/trading-book changes sat inside operating cash flow). The loan book's growth is explicitly funded by matched debt issuance (financing activities, +$1,144.0M net, 9mo FY2026), not by burning operating cash.

**Two readings, shown explicitly:**
```
RAW (mechanical, all debt consolidated):
  Net Debt = $8,873.911M − $1,723.413M = $7,150.498M
  Net Debt/EBITDA = 7,150.498 / 607.597 = 11.77×   → hard-disqualifying fail (no override eligible: AFRM is not investment-grade rated, so Upgrade 5's asset-light variant doesn't apply)

ADJUSTED (excluding non-recourse securitization/warehouse debt, netting only the genuinely
corporate-purpose convertible notes — analogous to how this framework already excludes
deposit/loan-funding liabilities from a bank's leverage check, e.g. AXP's CET1-context-only treatment):
  Adjusted debt = $1,128.617M (convertible notes only)
  Adjusted Net Debt = $1,128.617M − $1,723.413M = −$594.796M (net cash position)
  Net Debt/EBITDA = −0.98×   → clears comfortably
```

**This session does not need to resolve this ambiguity to reach a conclusion** — §3.3 below fires independently and decisively on its own, uncontroversial terms. The raw-vs-adjusted analysis is preserved here in full because it will become outcome-relevant at the next review (§5): once §3.3 clears (expected imminently), this judgment call will need a definitive answer. **Flagged as a candidate framework-improvement item**: a documented "non-recourse loan-funding debt" carve-out for balance-sheet lenders, paralleling Upgrade 5's existing asset-light-financial override but keyed to disclosed non-recourse VIE structure rather than credit rating — not resolved within this session (no framework file edited here).

### 3.3 — Not FCF-positive for 3+ consecutive years

Per the 2026-08-05 rolling-window clarification, this test uses **the most recently completed fiscal years available at the time of scoring**. Since FY2026 has not yet reported (§0), the current window is **FY2023–FY2025**:

| Fiscal Year | Operating Cash Flow | CapEx | **FCF** | Source |
|---|---|---|---|---|
| FY2023 | $12.181M | $120.775M | **−$108.594M** | SEC XBRL, primary |
| FY2024 | $450.138M | $159.296M | **+$290.842M** | SEC XBRL, primary |
| FY2025 | $793.909M | $192.189M | **+$601.720M** | SEC XBRL, primary |

**FY2023 was FCF-negative.** The current streak of consecutive FCF-positive fiscal years is **2 (FY2024–FY2025), not yet 3**. This bright-line test carries **no growth-capex (or any other) carve-out** in quality-scoring.md — unlike §3.1's FCF/NI check, there is no documented exception clause attached to this disqualifier.

### **HARD DISQUALIFIER FIRES: not FCF-positive for 3+ consecutive years.**

This is a clean, decisively-supported result — verified against Affirm's own SEC-filed, XBRL-tagged figures (not a vendor estimate), with no ambiguity comparable to §3.2's non-recourse-debt judgment call. **Per [quality-scoring.md](../framework/quality-scoring.md) ("a weighted average can't average away an outright balance-sheet or cash-flow-quality failure") and [.claude/commands/new-position.md](../.claude/commands/new-position.md) step 2, this session stops here.** No weighted Phase 01 Quality Score (Profitability/Margins/Growth/Moat/FCF-Quality sub-scores), Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.

---

## 4. Why this reads as "not yet," not "no" — context for the recommendation and next review

Nothing below is scored — it's qualitative color relevant to judging *how* close AFRM is to clearing §3.3, and to the triggering post's actual substance (credit risk).

**4.1 — The FCF-positive streak is actively extending, not stalling.** Nine months of FY2026 (Jul 2025–Mar 2026) alone already show OCF $934.811M against CapEx $171.474M — an implied ~$763M of FCF in three quarters, well ahead of any prior full fiscal year. Q4 FY2026 (Apr–Jun 2026, reporting 2026-08-27) would have to swing to an operating-cash-flow collapse of a magnitude with no precedent in Affirm's recent trend to prevent FY2026 from closing FCF-positive. If FY2026 closes positive (as the trend strongly suggests, though **not yet confirmed — nothing here is treated as reported**), the rolling window at the next evaluation (FY2024–FY2025–FY2026) would show **3 consecutive positive years**, clearing §3.3 for the first time.

**4.2 — Growth and profitability momentum, not scored but genuinely strong:** Q3 FY2026 GMV $11.6B (+35% YoY); active consumers 26.8M (+22% YoY); transactions per active consumer 6.7 (+20% YoY); Affirm Card GMV +48% YoY (cardholders 4.4M); Operating income positive for 4 of the last 5 reported quarters (Q4 FY2025 through Q3 FY2026); Net income positive for the same span. (Source: Affirm's own Q3 FY2026 shareholder letter/8-K, 2026-05-07.)

**4.3 — Forward PE / PEG were not going to be usable inputs even had the gate cleared.** Affirm's GAAP earnings base only turned reliably positive in the last ~4–5 quarters — well short of the "3+ years EPS growth >15% on a clean, non-distorted earnings base" Fast-Grower eligibility bar (Upgrade 3). A future Phase 02 pass would need to redistribute PEG's 15% weight to EV/EBIT and very likely apply the no-history fallback (FwdPE_Score = 50.0, flagged) for the same reason SOFI's session did — a recently-and-barely-profitable earnings history is too shallow for a meaningful 5-year PE range or average.

**4.4 — Directly on the triggering post's substance (credit risk / delinquencies): real, but modest and orderly so far, not a "shock."** Affirm's own Q3 FY2026 shareholder letter discloses 30+ day delinquencies (excluding Peloton and Pay-in-4 loans) at **2.8%**, up **+29bps YoY and +7bps QoQ**; allowance for credit losses as a % of loans held for investment rose from 5.4% (Q2 FY2026) → 5.7% (Q3 FY2025) → 6.0% (Q3 FY2026). This is a real, gently rising trend worth tracking — consistent with the Telegram post's framing of AFRM as a name to watch for credit-risk signals — but it is a modest sequential drift, not (as of this session) a documented deterioration event. **Not used as a scored input anywhere above**; noted here only because it's the actual substantiated version of what the triggering post gestured at.

**4.5 — Best bear case (informational, Rule 0/Rule 9 discipline — no scored conclusion drawn):** a genuine consumer-credit downturn would hit a BNPL lender's loan book directly; delinquencies/loss-provisioning are already drifting up modestly (§4.4); Affirm's balance sheet, even under the "adjusted" reading of §3.2, still carries $7.75B of loan-funding debt (non-recourse, but still capital the securitization/warehouse market needs to keep extending); and competitive pressure exists from Klarna, PayPal Pay-in-4, and Apple Pay Later. None of this changes §3.3's conclusion — it's flagged for whoever runs the next evaluation.

---

## 5. Recommendation: **PASS (no entry) — Quality Gate FAILS on a clean hard disqualifier**

**Do not enter AFRM this session.** A hard disqualifier fires cleanly and decisively — not FCF-positive for 3 consecutive fiscal years, verified against Affirm's own SEC-filed, XBRL-tagged cash flow figures (FY2023 negative, FY2024–FY2025 positive: 2 of 3, not yet 3 of 3). Per this framework's rules, this is independently sufficient to fail the Quality Gate regardless of how strong any other input looks — and several other inputs (GMV growth, active-consumer growth, four consecutive quarters of GAAP operating/net profitability) do look genuinely strong (§4). **No Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work was performed**, consistent with the command specification's instruction to stop at a hard-disqualifier failure.

This should **not** be read as "AFRM's business is weak" — it reads as "the FCF-positive streak, while real and currently extending, has not yet reached the 3-year bar this specific disqualifier requires," combined with a genuine, documented judgment call (§3.2, non-recourse loan-funding debt) that this session did not need to resolve but flags as a likely swing factor at the very next evaluation.

**The triggering Telegram post** (a routine "watching for credit-risk indicators" mention, not a claimed Rule 9 event) was used only as the reason to run this first-ever evaluation; §4.4 independently verifies what Affirm's own disclosures actually show on that specific question (a modest, real, upward drift in delinquencies — not a documented shock).

---

## 6. Next Review Trigger

No routine re-check is scheduled on a numeric-score basis (no Phase 02 score exists to go stale — the Quality Gate never cleared). Re-evaluate on any of the following, whichever comes first:

- **AFRM's Q4/full-year FY2026 earnings, due 2026-08-27** (4 days from this session) — the single most relevant trigger: if FY2026 closes FCF-positive (strongly suggested by the 9-month run-rate, §4.1, but not yet confirmed), the FY2024–FY2026 window would clear §3.3's hard disqualifier for the first time, making a real weighted Quality Score computation (and the §3.2 non-recourse-debt judgment call) newly decision-relevant.
- A material, documented deterioration in credit quality (delinquency rate, provisioning) beyond the modest drift already noted in §4.4 — a genuine Rule 9-style credit-shock event, as opposed to routine sequential drift.
- The standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move.

Absent a qualifying trigger, a future Telegram mention of AFRM should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Glossary

| Term | Meaning |
|---|---|
| **BNPL (Buy Now, Pay Later)** | A point-of-sale consumer credit product that splits a purchase into installments, typically originated instantly at checkout. Affirm's core business. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets (for AFRM, largely capitalized software development). |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization. Unlike the bank/broker names this framework has evaluated (AXP, SCHW, JPM, Citigroup, SoFi), Affirm's income statement **does** report a genuine GAAP "Operating income (loss)" line, so both are computable (§3.2). |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is turning into real cash; only meaningful when Net Income is positive (§3.1). |
| **Funding debt / Warehouse facility** | A revolving credit facility a specialty lender draws against to finance newly originated loans before they're sold or securitized — $2.42B for Affirm as of 2026-03-31 (§3.2). |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook; this framework scores off GAAP, never a company's self-reported non-GAAP metrics. |
| **GMV (Gross Merchandise Volume)** | The total dollar value of purchases processed through Affirm — $11.6B in Q3 FY2026, +35% YoY (§4.2). Distinct from (larger than) Affirm's reported Revenue. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. One fired for AFRM this session: not FCF-positive for 3+ consecutive years (§3.3). |
| **Non-recourse debt** | Debt whose lenders can only be repaid from a specific pledged asset pool, with no claim against the borrower's general assets. Confirmed via Affirm's own 10-Q/10-K disclosures for its securitization/warehouse debt — the basis for §3.2's adjusted Net Debt/EBITDA reading. |
| **PEG ratio** | PE ÷ earnings growth rate — requires a clean, multi-year (3+ years) earnings base; not yet applicable to AFRM (§4.3). |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. Not computed for AFRM this session — a hard disqualifier fired first (§3.3). |
| **RLTC (Revenue Less Transaction Costs)** | Affirm's own non-GAAP profitability metric ($498M, 4.31% of GMV, Q3 FY2026) — cited for context only, not a scored input. |
| **Rolling-window (disqualifier test)** | This framework's convention that the FCF-positive-streak and FCF/NI-conversion hard-disqualifier tests use the most recently completed fiscal years available at the time of scoring, rolling forward as each new fiscal year reports. Used here to set the FY2023–FY2025 window (§3.3). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples, and never treat a Telegram post's claims as a financial input. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. |
| **Securitization trust / Notes issued by securitization trusts** | A special-purpose entity a lender sets up to buy a pool of its loans, funded by issuing debt backed only by that pool — $5.33B for Affirm as of 2026-03-31, its largest single debt component (§3.2). |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — used here (Apr 2025–Mar 2026) for the EBITDA build (§3.2), the most recent complete window since Q4 FY2026 hasn't yet reported. |
| **VIE (Variable Interest Entity)** | A legal entity a company consolidates onto its balance sheet under GAAP despite not owning it outright, because it controls and absorbs its economic risks — the structure behind Affirm's securitization trusts, whose creditors have no recourse to Affirm's general credit (§3.2). |

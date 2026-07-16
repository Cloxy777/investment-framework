# New Position Evaluation — OKLO (Oklo Inc.)

**Task type:** NEW POSITION
**Date:** 2026-07-16
**10Y US Treasury yield:** 4.57% (^TNX, live quote fetched this session — not ultimately used, see below)
**Trigger:** Telegram Stock-Mention Scan (Routine 6), FinnInvestChannel post #2945 (2026-07-16, ~15:01 UTC): *"52-week lows: Oklo, NuScale, Oracle"* / *"52-week highs: UnitedHealth Group (UNH) and Tinder."* Per Rule 0, **the post's text is not used as financial data anywhere below** — it is only the reason this ticker was looked at, and every figure in this session was pulled independently from IBKR, yfinance, and SEC EDGAR. OKLO has **no prior watchlist entry anywhere** under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). This is OKLO's first-ever evaluation in this repo, run per `.claude/commands/telegram-scan.md` step 4's "no watchlist entry exists at all → `/new-position`" rule.

---

## 1. Contract Disambiguation & Live Price (Rule 0)

"OKLO" resolves to several IBKR-tradeable instruments; the correct one had to be picked deliberately, not assumed:

| Symbol | Exchange | Description | Used? |
|---|---|---|---|
| **OKLO** | **NYSE** | **OKLO INC** (contract_id **500073396**) | ✅ **Yes — the actual company** |
| OKLL | NASDAQ | Defiance 2x Daily Long OKLO ETF | ❌ Leveraged derivative product, not the company |
| OKLS | ARCA | Defiance 2x Daily Short OKLO ETF | ❌ Leveraged inverse derivative product |
| OKLC | BATS | Corgi OKLO 2x Daily ETF | ❌ Leveraged derivative product |
| 3OKL / OKL3 | LSEETF (GB/NL) | Leverage Shares 3x OKLO ETP | ❌ Leveraged derivative product, foreign-listed |
| OKU | VALUE (ASX) | Oklo Resources Ltd | ❌ Unrelated Australian gold-exploration company, name collision only |
| JYA | FWB2 (Frankfurt) | Oklo Resources Ltd | ❌ Same unrelated Australian miner, German listing |

**Live price fetched via IBKR `get_price_snapshot` on contract_id 500073396 (NYSE):**

| Field | Value |
|---|---|
| **Last trade price** | **$41.46** |
| Bid / Ask | $41.40 / $41.49 |
| Change (on the day) | **−$4.23 (−9.26%)** |
| Volume (session) | ~4.97M shares |
| 52-week high (IBKR `misc_statistics`) | $193.84 |
| 52-week low (IBKR `misc_statistics`) | $44.18 |

Cross-checked independently against Yahoo Finance's chart endpoint (queried moments later): `regularMarketPrice` $41.51, `regularMarketDayLow` $41.32, `fiftyTwoWeekLow` $41.32 — i.e. today's intraday low **is** a fresh 52-week low by Yahoo's real-time calculation (IBKR's `misc_statistics` 52w-low field appears to lag by a session and hadn't rolled the $44.18 figure forward yet). This independently confirms — via live market data, never via the trigger post's text — that OKLO is trading at/through a fresh 52-week low today, down **~78.6%** from its 52-week high of $193.84.

**Live price used throughout this session: $41.46** (IBKR, the framework's designated primary broker source).

---

## 2. Data Sources

- **yfinance** — reachable this session via a custom `requests.Session` (default `curl_cffi` backend hit a TLS reset in this environment; routing through `requests` with the proxy CA bundle worked normally). Used for `Ticker.info`, `.financials`, `.cashflow`, `.balance_sheet`.
- **SEC EDGAR** (CIK **0001849056**, "Oklo Inc.," formerly AltC Acquisition Corp. — the SPAC that merged with Oklo in May 2024) — `companyconcept` and `companyfacts` XBRL APIs, used to independently cross-verify every fundamental figure below against Oklo's own filed 10-K (accession 0001628280-26-018698, filed 2026-03-17).
- **World Nuclear News, Oklo's own newsroom, Utility Dive** — qualitative-only sources for NRC licensing status and customer-agreement context (Moat Signal discussion, §3). Not used as financial inputs.

---

## 3. Phase 01 — Quality Score (Gate)

### Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | Applies to OKLO? | Basis |
|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years, no growth-capex carve-out | Not meaningfully applicable — see FCF Quality sub-score note below; moot given the disqualifier below fires outright | Both FCF and Net Income are negative every year 2022–2025 — this isn't "profit not converting to cash," it's a company burning cash while also posting an accounting loss. The ratio's premise (checking whether *positive* accounting profit is real cash) doesn't hold when there is no profit. |
| Net Debt/EBITDA over threshold (2.5× standard / 4× asset-light) | **No**, in the ordinary "too much leverage" sense — but see Balance Sheet sub-score note below, where the *formula* still mechanically reads as a failure because EBITDA is negative | Total debt is **$1.45M** (SEC 10-K balance sheet) against **$788.4M** cash-and-equivalents ($2,208.6M total cash & short-term investments per yfinance) — OKLO is virtually debt-free, funded almost entirely by SPAC-merger and follow-on equity raises (FY2025 cash flow statement shows $1,263.6M of stock issuance proceeds). Not a leverage problem in the conventional sense. |
| **Not FCF-positive for 3+ consecutive years** | **✅ YES — FIRES** | Free Cash Flow (Operating Cash Flow − CapEx) has been negative in **every fiscal year the company has reported: FY2022 (−$10.14M), FY2023 (−$16.08M), FY2024 (−$38.74M), FY2025 (−$115.38M)** — the entirety of OKLO's public reporting history, and the burn is accelerating, not narrowing. |

**Cross-verification (yfinance vs. SEC EDGAR XBRL, both primary-source-adjacent):**

| Fiscal year | Operating Cash Flow (yfinance) | CapEx (yfinance) | FCF (yfinance) | OCF (SEC XBRL) | CapEx (SEC XBRL) | FCF (derived from SEC) |
|---|---|---|---|---|---|---|
| FY2022 | −$9.99M | −$0.15M (implied) | −$10.14M | −$0.95M* | n/a | n/a |
| FY2023 | −$16.00M | −$0.08M | −$16.08M | −$10.84M* | −$0.08M | −$10.93M* |
| FY2024 | −$38.39M | −$0.35M | −$38.74M | −$38.39M | −$0.35M | −$38.74M ✅ |
| FY2025 | −$82.17M | −$33.21M | −$115.38M | −$82.17M | −$33.21M | −$115.38M ✅ |

*FY2022/FY2023 SEC figures reflect the pre-/mid-de-SPAC-merger reporting entity (AltC Acquisition Corp. shell → Oklo Inc.) and don't reconcile cleanly to yfinance's post-merger-restated annuals for those two years — a known artifact of SPAC-merger accounting (see **SPAC** glossary entry) rather than a data error. **FY2024 and FY2025 — the two most recent, most decision-relevant years — reconcile exactly between yfinance and SEC EDGAR to the dollar.** Regardless of which pair of years is used, FCF is negative in **all four** reported fiscal years; the disqualifier fires under either data source.

**Independent confirmation OKLO is genuinely pre-revenue (not a data gap — a structural fact):** SEC EDGAR's XBRL `companyfacts` API for CIK 0001849056 contains **no "Revenues" tag, no "RevenueFromContractWithCustomerExcludingAssessedTax" tag, and no revenue-recognition tag of any kind** — Oklo has never tagged a dollar of revenue in any filed 10-K. yfinance's `Total Revenue` line independently confirms **$0** in every reported fiscal year (2022, 2023, 2024, 2025). This is why the Aurora powerhouse (Oklo's first planned reactor) is still under NRC licensing review, with commercial operation targeted for **2027–2028**, not yet reached ([World Nuclear News](https://www.world-nuclear-news.org/articles/licensing-of-oklo-pilot-reactor-facilities-advances); [Oklo newsroom, NRC PDC topical report approval](https://oklo.com/newsroom/news-details/2026/Oklos-NRC-Principal-Design-Criteria-Topical-Report-Approved-for-Aurora-Powerhouse-in-Idaho/default.aspx)).

### Result: **Hard disqualifier fires — "Not FCF-positive for 3+ consecutive years."**

Per [quality-scoring.md](../framework/quality-scoring.md): *"These mirror the existing Phase 01 non-negotiables — a weighted average can't average away an outright balance-sheet or cash-flow-quality failure."* This alone is dispositive. **Stop here — do not proceed to Phase 02 valuation scoring, regardless of any weighted Quality Score.**

### Weighted Quality Score — shown for full transparency (per "no black-box outputs"), not because it changes the verdict

Two of six sub-scores (Growth; the Net Margin half of Profitability) are **mathematically undefined** from a $0-revenue base rather than merely low — computing a specific number for them would mean inventing data the company genuinely doesn't have, which Rule 0 forbids. Where the sub-score formula's `clamp(x, 0, 100)` behavior lets the correct floor value be reasoned out **without inventing a magnitude** (any negative or zero input clamps to 0.0 regardless of exactly how negative), that reasoning is shown explicitly below. Two other sub-score formulas (Balance Sheet's Net Debt/EBITDA; FCF Quality's FCF/NI ratio) are designed around a *positive*-EBITDA / *positive*-NI company and **mechanically break down** for OKLO — both are shown with the literal formula output and a clear caveat that the number is not a trustworthy read of the real underlying situation.

| Sub-score (weight) | Inputs (source) | Calculation | Result | Caveat |
|---|---|---|---|---|
| **Profitability** (25%) | Net Margin: undefined (Revenue = $0, all years, SEC EDGAR + yfinance). ROIC (TTM/FY2025, normalized): EBIT −$139.294M × (1 − 4.1% tax rate) = NOPAT −$133.583M ÷ Invested Capital $689.215M (Debt $1.45M + Equity $1,476.21M − Cash $788.445M, all SEC 10-K balance sheet) = **−19.38%** | NetMargin_Component: negative-infinite-limit margin (loss on zero revenue) clamps to floor → **0.0**. ROIC_Component = clamp((−19.38/30)×100) = clamp(−64.6) → **0.0**. Profitability_Score = (0.0+0.0)/2 | **0.0** | FCF-positivity cap (≤40.0) is moot — already at the absolute floor. |
| **Margins** (15%) | Gross Margin (TTM) 0.0% (yfinance `grossMargins`; consistent with $0 revenue → $0 gross profit) | clamp((0/80)×100) | **0.0** | No structural-trend bonus applies — margin isn't "below 40% and expanding," there is no revenue base for a margin to exist on at all. |
| **Growth** (20%) | Revenue 3yr CAGR: **not computable** — $0 → $0 → $0 → $0, FY2022–FY2025 (confirmed via SEC EDGAR: no revenue XBRL tag exists in any filing) | No revenue has ever been generated in OKLO's public history, so there is no revenue growth to credit under this sub-score's formula | **0.0** | **Not applying the +10 TAM-expansion modifier.** Oklo has real, cited non-binding commercial interest — a Dec-2024 **12 GWe Master Power Agreement** with Switch data centers, non-binding LOIs with Equinix/Diamondback Energy/Prometheus Hyperscale, and a tentative selection for Eielson Air Force Base ([Utility Dive](https://www.utilitydive.com/news/oklo-advanced-nuclear-microreactor-project-pipeline-nrc/724343/), citing a ~14,100 MWe order book) — but none of it has converted into a single dollar of recognized revenue or a binding delivery obligation. Crediting a growth-rate modifier with no underlying growth rate to modify would be inventing the very number Rule 0 forbids. |
| **Balance Sheet** (15%) | Net Debt = $1.45M debt − $788.445M cash = **−$786.995M** (net cash). EBITDA (FY2025) = **−$138.772M** (negative). Net Debt/EBITDA = −786.995 ÷ −138.772 = **+5.671×** | clamp(100×(1 − 5.671/4)) = clamp(100×(1 − 1.418)) = clamp(−41.8) | **0.0 (mechanical)** | **Formula breakdown, not a real signal of distress.** OKLO is almost entirely debt-free with a ~$2.2B total cash/investment cushion against just $25.5M of current liabilities — objectively a strong balance sheet on any conventional leverage reading. The ratio only reads as "maximally over-levered" because dividing a negative net-debt figure by a negative EBITDA figure flips the sign into a large positive number the formula was never designed to handle (it assumes positive EBITDA). |
| **Moat Signal** (15%) | 5-signal checklist, evidence required per signal (see table below) | 0 of 5 signals cleared the cited-evidence bar | **0.0** | Not a data gap — OKLO has not yet reached commercial operation of a single reactor, so several signals are structurally not-yet-evidenceable (see below), not merely under-researched. |
| **FCF Quality** (10%) | FCF (FY2025) −$115.379M ÷ Net Income (FY2025) −$105.663M = **+109.2%** (two negatives divide to a positive ratio) | clamp(((1.092−0.40)/0.60)×100) = clamp(115.3) | **100.0 (mechanical)** | **Inverted-signal formula breakdown — do not read as "excellent cash conversion."** The ratio is designed to catch *positive* accounting profit that isn't turning into cash; with both figures negative, a mechanically "high" ratio actually means OKLO burned **more** cash (−$115.4M) than its own accounting loss (−$105.7M) — heavier CapEx stacked on top of an operating loss, which if anything is a *worse* signal than the ratio's 100.0 output implies. |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | No operating market exists yet to hold share in — OKLO is pre-commercial-operation (Aurora powerhouse targeted 2027–2028). The ~14,100 MWe order book (Utility Dive) is uncontracted capacity interest, not measured share of a functioning market. | **FALSE** |
| Brand premium | No priced product exists to evidence pricing power. | **FALSE** |
| Network effect | Not applicable to this business model (single-asset power generation, not a multi-sided platform). | **FALSE** |
| Switching costs | The Switch 12 GWe Master Power Agreement and various LOIs are pre-commercial framework agreements, not evidence of a live customer locked into an operating relationship. | **FALSE** |
| Scale cost advantage | No production/operating cost-per-unit data exists — nothing has been built and operated commercially yet. | **FALSE** |

```
Quality Score = 0.0×0.25 + 0.0×0.15 + 0.0×0.20 + 0.0×0.15 + 0.0×0.15 + 100.0×0.10
              = 0.00 + 0.00 + 0.00 + 0.00 + 0.00 + 10.00
              = 10.0
```

**Even under this literal mechanical computation — which includes one formula-breakdown artifact (FCF Quality) inflated all the way to its 100.0 ceiling in OKLO's favor — the weighted Quality Score is 10.0, catastrophically below the 80.0+ gate.** The hard disqualifier above is the dispositive, headline reason to stop; this weighted number simply confirms the same conclusion from a different angle and is shown only for the "no black-box outputs" discipline, not as an independent basis for the verdict.

---

## 4. Recommendation

**PASS — do not open a position; not eligible for the watchlist's "scored" bucket.** Per [new-position.md](../.claude/commands/new-position.md) step 2 and [quality-scoring.md](../framework/quality-scoring.md): a hard disqualifier firing stops the evaluation before Phase 02 regardless of how the weighted score comes out. Accordingly:

- **No Rate Environment Gate was run.**
- **No Phase 02 valuation score was computed.**
- **No Composite Score exists** for OKLO.
- **No DCF, comparables, Upside/Downside Modifier, or order setup was produced** — none of that work is meaningful for a name that fails the quality gate this decisively, and none of it should be inferred from the live price alone (Oklo's very high market cap — ~$7.2B — against $0 revenue is itself a reflection of speculative/thematic (advanced-nuclear, AI-power-demand) sentiment, not something this framework's bottom-up valuation machinery is built to price without invented inputs).

This is not a verdict that Oklo's underlying technology or commercial pipeline lacks promise — the NRC's accelerated review of its Principal Design Criteria topical report, the scale of its non-binding order book, and its essentially debt-free balance sheet (funded by ~$1.26B of FY2025 equity issuance, not debt) are all real, positive facts about the company's *prospects*. But this framework scores *demonstrated* quality — profitability, margins, growth, balance-sheet strength, moat, and cash-flow quality *as filed* — and a company that has never generated a dollar of revenue or a dollar of positive free cash flow in its public history cannot pass that bar under any reading of the rules, regardless of how promising the story is. Re-evaluate once Oklo begins generating actual revenue (expected around first commercial reactor operation, 2027–2028) or discloses a Rule-9-style fundamental event that changes this picture materially sooner.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries carry no numeric Phase 02 score and so don't go stale on a future methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) Oklo begins generating actual recognized revenue (e.g. Aurora powerhouse reaches commercial operation, currently targeted 2027–2028); (b) any of the currently non-binding agreements (Switch MPA, Equinix/Diamondback/Prometheus Hyperscale LOIs, Eielson AFB selection) converts into a binding, revenue-generating contract; (c) NRC grants a construction permit or operating license (a major de-risking milestone, though not itself a revenue event); (d) a quarterly earnings report showing a materially different cash-burn trajectory; (e) a management change or material M&A; (f) a dilutive capital raise or balance-sheet-structure change; (g) a >15% unexplained price move from $41.46 with no identified cause (today's −9.26% move is explained by the fresh 52-week-low context already discussed, not "unexplained").
- Absent any of the above, future Telegram mentions of OKLO should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **CapEx** — Capital Expenditure — money spent buying or upgrading physical assets (factories, equipment, data centers).
- **Composite Score** — `0.50×(100−Quality Score) + 0.50×Valuation Score` — combines quality and cheapness into one number, computed only for companies that clear the 80.0+ Quality Score gate. Not computed for OKLO (gate fails).
- **de-SPAC merger** — The transaction in which a SPAC completes its combination with a private operating company, converting the private company into a publicly-traded one under the SPAC's listing. Oklo went public this way in May 2024 (AltC Acquisition Corp. → Oklo Inc.).
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. Breaks down as a signal when both figures are negative (see §3).
- **Hard disqualifier** — One of three Quality Score conditions (FCF/NI conversion <70% for 2+ consecutive years without a documented growth-capex explanation; Net Debt/EBITDA over the Debt Gate threshold; not FCF-positive for 3+ consecutive years) that fails a company regardless of its weighted Quality Score — see [quality-scoring.md](../framework/quality-scoring.md). The FCF-positivity check fires for OKLO.
- **Invested Capital** — The total capital (debt + equity, minus cash) deployed in a business — the denominator of ROIC.
- **Letter of Intent (LOI)** — A non-binding document expressing an intention to enter into a future agreement, signed before parties finalize binding contractual terms — signals commercial interest but creates no enforceable obligation. Several of Oklo's disclosed customer commitments (Equinix, Diamondback Energy, Prometheus Hyperscale) are LOIs, not binding revenue contracts.
- **Master Power Agreement (MPA)** — A framework-level power-supply agreement establishing terms under which individual project-level Power Purchase Agreements can later be signed, without itself obligating either party to a specific delivered volume or firm revenue. Oklo's December 2024 12 GWe MPA with Switch data centers is this kind of framework agreement, not yet converted into binding revenue.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; negative net debt means net cash. The ratio's usual interpretation breaks down when EBITDA is also negative, as for OKLO.
- **NOPAT** — Net Operating Profit After Tax — EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **NRC (Nuclear Regulatory Commission)** — The US federal agency responsible for licensing and regulating nuclear reactor construction and operation, including advanced/small modular reactor designs. Oklo's Aurora powerhouse has cleared an early NRC design-review milestone but has not yet received a construction or operating license.
- **Pre-revenue (company)** — A company that has not yet generated any revenue from commercial sales, typically because its core product is still in development, testing, or regulatory approval. Standard revenue-based ratios are mathematically undefined (not merely low) for such a company — a structural fact, not a missing data point. Oklo Inc. is pre-revenue: $0 total revenue in every fiscal year 2022–2025.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. OKLO's mechanically-computed score is 10.0, and separately fails an outright hard disqualifier.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **SMR (Small Modular Reactor)** — A class of nuclear fission reactor designs that are smaller, factory-fabricated, and intended to be simpler/faster to build than a traditional large nuclear power plant; a "microreactor" is an even smaller SMR sub-class (typically under ~20 MWe). Oklo's Aurora powerhouse is a microreactor-class SMR design, still pre-commercial as of this session.
- **SPAC** — Special Purpose Acquisition Company — a shell company that raises money via its own IPO to merge with a private company and take it public, as an alternative to a traditional IPO. Oklo went public via a SPAC merger with AltC Acquisition Corp. (May 2024), which can leave a short, distorted trailing public earnings history — one contributor to the FY2022/FY2023 data reconciliation note in §3.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.

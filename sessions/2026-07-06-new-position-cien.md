# NEW POSITION (Quality Score Engine addendum) — CIEN (Ciena Corporation) — 2026-07-06

**Task type:** NEW POSITION — Quality Score Engine addendum (lightweight, per the CCL precedent), not a full re-evaluation
**Date:** 6 Jul 2026
**Ticker:** CIEN (Ciena Corporation, NYSE)
**Prior session:** [2026-06-11-new-position-cien.md](2026-06-11-new-position-cien.md) — Phase 01 FAIL (net margin, ROIC, revenue CAGR all short of threshold), predates the 2026-06-29 Quality Score engine addition — CIEN has never had a Quality Score computed until this session
**Current CIEN portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

CIEN's 06-11 session failed Phase 01 on TTM Net Margin (7.9% vs >15%), TTM ROIC (~7% vs >15%), and Revenue 3yr CAGR (~9.55% vs >10%, borderline), and was never scored under the new 0-100.0 Quality Score engine. Per this task's explicit scope, this session does three things:

1. A Rule 9 check — verify whether CIEN reported Q3 FY2026 earnings yet (flagged as due ~Sept 2026), whether TTM net margin/ROIC moved since the Q2 FY2026 inflection quarter, and what happened with the $2.5B convertible-note deployment flagged in the prior session.
2. Compute CIEN's first-ever Quality Score under the current engine, with every sub-score shown.
3. Only redo the full Phase 01 gate / Phase 02 valuation if a Rule 9 trigger fired that flips the previously-failing criteria.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$428.97** | IBKR `get_price_snapshot`, contract_id 41045553, intraday, `is_close: false`, ts 1783319641 |
| Change vs. 06-11 baseline ($441.36) | **-2.8%** | Computed — well short of the >15% Rule 9 threshold, and not "unexplained" regardless (see Rule 9 checklist) |
| 52-week range | $76.90 - $637.09 (open 52w ago $79.76) | IBKR `misc_statistics` |

---

## 2. Rule 9 checklist (all 6 categories)

| Category | Result |
|---|---|
| Earnings | **NO new report.** Q2 FY2026 (quarter ended 2 May 2026) was reported 4 Jun 2026 — already reflected in the 06-11 session. Q3 FY2026 not yet reported; consensus ~3 Sept 2026 (MarketBeat), not company-confirmed. |
| Guidance revision | FY2026 revenue guidance raised to $6.3B ±$100M (32% YoY at midpoint) on 4 Jun 2026 — already reflected pre-06-11, nothing new since. |
| Management change | None found. |
| M&A / capital raise | **YES.** The $2.5B convertible-note offering flagged as "very recent, pricing" in the 06-11 session has since been upsized and closed: **$2.875B of 0.00%-coupon convertible senior notes due 2031**, priced 9 Jun 2026, closed ~11 Jun 2026 (full exercise of the initial purchasers' over-allotment option). Disclosed use of proceeds: ~$100M note-hedge cost, ~$140M share buyback (~0.3M shares), **~$1.14B to repay the existing term loan**, remainder for general corporate purposes including supply-chain capacity investment. |
| Macro shift | None new beyond the already-known AI-datacenter/optical-networking demand tailwind. |
| >15% unexplained price move | No (-2.8%). |

**Net effect:** Rule 9 fired in the capital-raise category, but it's a financing event — it doesn't move margins, ROIC, or growth, and the term-loan repayment plus 0% coupon is balance-sheet-strengthening, not concerning. It closed **after** the Q2 FY2026 quarter-end (2 May 2026) used for this session's financials, so the Balance Sheet sub-score below reflects the pre-convert capital structure — flagged explicitly in the watchlist addendum.

---

## 3. Refreshed TTM financials (through Q2 FY2026, same 4 quarters as 06-11 — no new quarter reported)

**Data sourcing:** Primary sources — Ciena's 10-Q for the quarter ended 2 May 2026 ([SEC EDGAR](https://www.sec.gov/Archives/edgar/data/0000936395/000162828026040767/cien-20260502.htm)) and the Q2 FY2026 / Q1 FY2026 / Q4 FY2025 / Q3 FY2025 8-K earnings-release exhibits (EX-99.1, SEC EDGAR). Cross-checked against Yahoo Finance's `fundamentals-timeseries` endpoint, queried directly via plain `requests` (not `yfinance`'s own `curl_cffi` client, which failed the same TLS-handshake issue documented in the 2026-07-06 CCL session).

### Quarterly figures used to build TTM (Q3 FY2025 - Q2 FY2026)

| Quarter end | Revenue | Gross Profit | Op. Income (EBIT) | Pretax Income | Tax | Net Income |
|---|---|---|---|---|---|---|
| 2025-08-02 (Q3 FY25) | $1,219.39M | $503.08M | $73.54M | $65.80M | $15.50M | $50.31M |
| 2025-11-01 (Q4 FY25) | $1,351.98M | $577.18M | $10.49M | $2.86M | -$16.63M | $19.49M |
| 2026-01-31 (Q1 FY26) | $1,427.0M | $625.5M | $189.4M | $181.1M | $30.8M | $150.3M |
| 2026-05-02 (Q2 FY26) | $1,570.7M | $691.6M | $237.9M | $231.1M | $12.8M | $218.2M |
| **TTM (sum)** | **$5,569.07M** | **$2,397.36M** | **$511.29M** | **$480.86M** | **$42.47M** | **$438.29M** |

Yahoo's own `trailing*` fields (as-of 2026-04-30, TTM) confirm: Revenue $5,569.15M, Gross Profit $2,397.33M, Net Income $438.30M (**identical** to the 06-11 session's $438.3M — confirms same 4 quarters, no drift), EBIT $567.82M (Yahoo's EBIT definition differs from the summed GAAP operating-income figure above), effective tax rate 8.85%.

### Balance sheet (2 May 2026, per 10-Q)

| Metric | Value |
|---|---|
| Cash and cash equivalents | $1,045.13M |
| Short-term + long-term investments | $357.81M |
| Total Debt (current + long-term, net) | $1,531.12M |
| Total Stockholders' Equity | $2,892.23M |
| Company-disclosed Net Debt (nets cash + investments) | $138M (per earnings materials; 10-Q-derived figure $128.18M, immaterial gap) |
| Yahoo `quarterlyNetDebt` (nets cash only) | $485.99M |
| `quarterlyInvestedCapital` (Yahoo, = Debt + Equity, no cash netting) | $4,423.34M |

### Recomputed ratios

```
TTM Net Margin   = $438.30M / $5,569.15M = 7.87%   (06-11: 7.9% — essentially unchanged, still fails >15%)
TTM Gross Margin = $2,397.33M / $5,569.15M = 43.05% (still clears >40%)
Revenue 3yr CAGR (FY2022 $3,632.66M → FY2025 $4,769.51M) = 9.51% (06-11: ≈9.55% — essentially unchanged, still fails >10%)

ROIC (raw Debt+Equity IC, matches the 2026-07-06 CCL session's convention):
  NOPAT $517.57M [EBIT $567.82M × (1 − 8.85%)] / IC $4,423.34M = 11.70%  — still fails >15%

ROIC (glossary.md's literal "debt + equity − cash" convention, netting Cash & Equivalents only):
  NOPAT $517.57M / IC $3,378.22M [$1,531.12M + $2,892.23M − $1,045.13M] = 15.32%  — CROSSES >15%
```

**A flagged framework-consistency issue, not a fundamental change:** the 06-11 session's ROIC figure (~6.98%, GuruFocus, methodology undisclosed) can't be directly reconciled against either of the above. More importantly, this framework's own glossary.md defines Invested Capital as cash-netted ("debt + equity − cash"), but the CCL precedent (2026-07-06) used Yahoo's raw, non-cash-netted `InvestedCapital` field directly — for CCL this didn't matter (leverage was high, cash was small relative to IC, both conventions gave a similar answer), but for CIEN (large cash/investments balance relative to a small debt load) the choice changes whether ROIC lands above or below the 15% Phase 01 threshold. Flagged in the watchlist addendum as worth reconciling in the framework docs; **does not change this session's conclusion** either way, since Net Margin (7.87%) and Revenue CAGR (9.51%) both still fail decisively regardless of which ROIC convention is used — Phase 01's overall verdict requires all criteria to pass, so it remains **FAIL**. Per the task's branching instruction, this stays an addendum — no fuller Phase 01 re-check or new dated file.

---

## 4. Quality Score Engine — CIEN's first-ever computation

Per [framework/quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). Full detail and citations are in the [watchlist addendum](../watchlist/not-in-portfolio/CIEN/CIEN-2026-06-11.md); summarized here:

**Hard disqualifiers — none fire:** FCF positive 3+ consecutive years (FY2023-FY2025, TTM); FCF/NI conversion ≥70% for both of the last 2 complete fiscal years (FY2024 450.1%, FY2025 539.4% — FY2022-23's weak conversion falls outside the operative 2-year window); Net Debt/EBITDA 0.16-0.58x, far under the 2.5x threshold.

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 38.65 (primary, glossary-literal cash-netted ROIC) / 32.62 (cross-check, raw Debt+Equity IC) |
| Margins (15%) | 53.81 |
| Growth (20%) | 48.03 |
| Balance Sheet (15%) | 95.90 (primary, company-disclosed Net Debt) / 85.57 (cross-check, Yahoo cash-only Net Debt) |
| Moat (15%) | 40.0 |
| FCF Quality (10%) | 100.0 |

```
Quality Score (primary) = 38.65×0.25 + 53.81×0.15 + 48.03×0.20 + 95.90×0.15 + 40.0×0.15 + 100.0×0.10
                         = 9.6625 + 8.0715 + 9.606 + 14.385 + 6.00 + 10.00 = 57.7

Cross-check             = 32.62×0.25 + 53.81×0.15 + 48.03×0.20 + 85.57×0.15 + 40.0×0.15 + 100.0×0.10 = 54.7
```

**Quality Score = 57.7 / 100.0 — fails the 80.0+ gate, and fails it under every methodology variant tested (54.7-57.7).** No hard disqualifier fires. The gate fails mainly on Profitability (Net Margin is the binding constraint at 7.87%, regardless of the ROIC methodology question) and a middling Moat score (2 of 5 signals). No Composite Score computed. No Phase 02 valuation performed (out of scope, and moot given the gate result).

### Moat Signal detail

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Dell'Oro Group: Ciena holds ~50% share of the US optical-transport market, the largest single 2025 market-share gain (+3pp) among major vendors, and top-3 revenue share (with Nokia, Cisco) in Data Center Interconnect (DCI) |
| Brand premium (pricing power) | **TRUE** | Q2 FY2026 8-K: GAAP gross margin +380bps YoY to 44.0% (adjusted 44.9%), achieved simultaneously with 40% YoY revenue growth and continued share gains — margin expansion without discounting for volume |
| Network effect | FALSE | Hardware/optical-equipment vendor; no two-sided marketplace dynamics |
| Switching costs | FALSE | Ciena's own OFC 2026 messaging explicitly promotes open, interoperable standards to *reduce* vendor lock-in and switching costs — works against, not for, a lock-in-based moat |
| Scale cost advantage | FALSE | No cost-per-unit data vs. smaller competitors found in available sources |

Moat_Score = (2/5) × 100 = **40.0**

---

## 5. Recommendation

# **PASS — Quality Score 57.7/100.0 (54.7-57.7 across methodology cross-checks), fails the 80.0+ gate. Do not enter. Watchlist addendum appended, no new file created.**

The Q2 FY2026 inflection quarter is real and the newly-closed $2.875B 0% convertible-note financing is a genuinely shareholder-friendly capital-structure event (cheap financing, largely retiring an existing term loan) — but neither changes the substance of the 06-11 Phase 01 FAIL. Net Margin (7.87%) and Revenue CAGR (9.51%) both remain clearly below threshold on a TTM basis. ROIC is a genuine open question — one defensible reading (this framework's own written Invested-Capital convention) now crosses 15%, but that alone isn't sufficient to pass Phase 01 (which requires all criteria to clear), and it barely moves the Quality Score, which fails its much stricter 80.0 bar by more than 20 points either way.

**No position opened — nothing to log in `decisions/`.**

---

## 6. Files touched this session

- `watchlist/not-in-portfolio/CIEN/CIEN-2026-06-11.md` — appended the Rule 9 check + Quality Score addendum as a dated note (no new file, per the task's branching instruction — no Phase 01 verdict change); updated the summary table's top row
- `framework/glossary.md` — added **Backlog**, **Convertible senior notes**, **Dell'Oro Group**, and **DCI (Data Center Interconnect)**
- `sessions/2026-07-06-new-position-cien.md` — this file

`watchlist/STALE.md` was not touched (CIEN was not listed there — it predates the Quality Score engine but was never a "stale re-score" case, it was a Phase 01 FAIL that had never been scored at all).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **8-K** — a US company's "current report" filed with the SEC disclosing a material event between regular filings; used here as the primary source for Ciena's Q1 FY2026, Q4 FY2025, and Q3 FY2025 earnings releases.
- **10-Q** — a US public company's quarterly report filed with the SEC, containing unaudited financial statements; used here as the primary source for Ciena's Q2 FY2026 balance sheet.
- **Backlog** — the dollar value of signed customer orders not yet recognized as revenue; Ciena's record $7.7B backlog is cited as Growth sub-score TAM-expansion evidence.
- **BalanceSheet_Score** — this framework's 0-100 Quality Score sub-score derived from Net Debt/EBITDA.
- **CAGR** — Compound Annual Growth Rate.
- **Convertible senior notes** — a bond convertible into the issuer's shares at a preset strike price; Ciena closed $2.875B of 0.00%-coupon convertible senior notes due 2031 in June 2026.
- **DCI (Data Center Interconnect)** — the optical-networking sub-segment linking separate data centers over fiber, where Ciena is a top-3 vendor by revenue share.
- **Dell'Oro Group** — an independent telecom/networking market-research firm, the third-party source for Ciena's market-share figures in this session.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization.
- **Effective tax rate** — the actual share of pretax income paid as tax.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check.
- **GAAP** — Generally Accepted Accounting Principles.
- **Gross Margin** — Gross Profit ÷ Revenue.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; none fire for CIEN this session.
- **Invested Capital** — the capital (debt + equity, this framework's glossary says netted for cash) deployed in a business; the ROIC denominator. This session flags an inconsistency between the glossary's written definition and how it was actually applied in the CCL precedent.
- **Moat** — a durable competitive advantage.
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate.
- **Quality Score** — this framework's 0-100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. CIEN scores 57.7 on its first-ever computation.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.
- **TAM (Total Addressable Market)** — the total revenue opportunity available if a company captured its entire target market.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.

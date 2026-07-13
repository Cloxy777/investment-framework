# NEW POSITION (Quality Score Engine addendum) — GTLB (GitLab Inc.) — 2026-07-09

**Task type:** NEW POSITION — Quality Score Engine addendum (lightweight, per the CCL/CDR precedent), not a full re-evaluation
**Date:** 9 Jul 2026
**Ticker:** GTLB (GitLab Inc., NASDAQ)
**Prior session:** [2026-06-12-new-position-gtlb.md](2026-06-12-new-position-gtlb.md) — Phase 01 FAIL (TTM Net Margin ≈ −5.86%, ROIC ≈ −4.57%, both structural; GAAP OCF negative FY2025; SBC ~22.5% of revenue), predates the 2026-06-29 Quality Score engine addition — GTLB has never had a Quality Score computed until this session
**Current GTLB portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

GTLB's 06-12 session failed Phase 01 (the binary quality screen that predates the 2026-06-29 Quality Score engine) and was never scored under the new 0-100.0 engine. Per this task's explicit scope, this session does three things:

1. A live price check (Rule 0).
2. A Rule 9 check — has GitLab reported Q2 FY2027 earnings yet (flagged as due ~early Sept 2026)? Has GAAP net income turned positive in any quarter, has there been a material SBC policy change, or has CEO/CFO insider buying been reported (any of which would reopen the Turnaround Sub-Gate check per the 06-12 session's note)? Any other Rule 9 trigger?
3. Compute GTLB's first-ever Quality Score under the current engine, with every sub-score shown.

Per the task's branching instruction, a fuller Phase 01 re-check (or a new dated watchlist file) is only warranted if a Rule 9 trigger changes the verdict on the previously-failing criteria (net margin, ROIC). As shown below, both remain decisively negative on the freshest TTM data, so this stays an addendum appended to the existing watchlist file, not a new one.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$34.16** | IBKR `get_price_snapshot`, contract_id 520512263 (NASDAQ, resolved via `search_contracts`), snapshot ts 1783620244 → 2026-07-09 18:04:04 UTC, `is_close: false` |
| Bid / Ask | $34.14 / $34.16 | Same snapshot |
| Prior close | $31.74 | Same snapshot |
| Day change | +7.62% ($2.42) | Same snapshot |
| 52-week range | $18.73 – $52.38 | `misc_statistics` field, same snapshot |
| 13-week / 26-week high | $34.06 / $38.64 | Same snapshot |
| Baseline (06-12) | ~$28.00 | Prior session |
| Change since 06-12 | **+22.0%** | Computed |

A clean, non-ambiguous live quote this time (contrast with 06-12, where IBKR tool access was denied and WebSearch had to be used as a fallback with conflicting figures).

---

## 2. Rule 9 check — all 6 categories

| Category | Result |
|---|---|
| Earnings | **NO.** Q1 FY2027 (reported 2026-06-02) was already reflected in the 06-12 baseline. Q2 FY2027 (quarter ending ~2026-07-31) has not even closed yet — not yet reported, expected ~early September 2026 (exact date not confirmed via IR calendar this session). |
| Guidance revision | None. A 2026-07-08 investor update highlighted consumption-based business progress (refined Consumption Run Rate >$20M by 2026-06-30) and new AI-driven "agentic DevOps" product architecture — a business/product update, not a formal guidance revision. |
| Management change | None found. |
| M&A | None found. |
| Macro shift | None identified specific to GTLB. |
| >15% unexplained price move | Nominally yes (+22.0% since 06-12), but explained by two documented events (see §3) — not "unexplained." |

### The +22% move, explained

Two dated, sourced events account for the move:
1. **FTSE Russell's semi-annual US Indexes reconstitution** (effective late June 2026) reclassified GTLB from Russell Growth to Russell Value indices — cited as driving an ~11.5% single-day jump around 2026-07-02 via systematic passive-fund rebalancing (sahmcapital.com / Simply Wall St, cross-checked against LSEG's own reconstitution summary documentation).
2. The 2026-07-08 investor update noted above. Today's own +7.62% day move sits inside this same window, with the stock also reclaiming its 13-week high intraday.

**Net effect: no Rule 9 trigger fires that changes the Phase 01 verdict.**

---

## 3. Refreshed TTM financials (through Q1 FY2027, quarter ended 2026-04-30)

**Data-sourcing note:** IBKR MCP tools were available this session (unlike 06-12) and used for the live price. Fundamentals were sourced via WebSearch aggregation cross-checked against primary SEC 8-K exhibits fetched directly (GitLab's Q1 FY2027, Q4 FY2026, Q3 FY2026, and Q2 FY2026 earnings-release exhibits), consistent with "never invent or estimate financial data" — every quarterly figure below traces to a company-issued earnings release or a directly-fetched SEC filing, not a third-party estimate.

### Quarterly figures (4 most recent, the TTM window)

| Quarter end | Revenue | Gross Profit | GAAP Net Loss | OCF | CapEx | SBC |
|---|---|---|---|---|---|---|
| 2025-07-31 (Q2 FY26) | $236.0M | $207.5M | −$9.2M | $49.37M | $2.90M | $54.284M |
| 2025-10-31 (Q3 FY26) | $244.4M | $212.1M | −$8.3M | $31.43M | $3.04M | $51.682M |
| 2026-01-31 (Q4 FY26) | $260.4M | $225.42M | −$2.6M | $45.76M | $3.97M | $53.158M |
| 2026-04-30 (Q1 FY27) | $264.158M | $226.670M | −$4.972M | $149.2M | $2.39M | $50.061M |
| **TTM** | **$1,004.958M** | **$871.69M** | **−$25.072M** | **$275.76M** | **$12.30M** | **$209.185M** |

Sources: Q2/Q3/Q4 FY2026 and Q1 FY2027 8-K earnings-release exhibits (SEC EDGAR, fetched directly); OCF/CapEx cross-checked against stockanalysis.com's quarterly cash-flow summary.

### Balance sheet (2026-04-30, per the Q1 FY2027 10-Q)

| Metric | Value |
|---|---|
| Total assets | $1,705.533M |
| Total liabilities | $674.147M |
| Total stockholders' equity | $1,031.386M |
| Total debt | $0 (no long-term debt, finance leases, or borrowings) |
| Cash and cash equivalents | $335.395M |
| Short-term investments | $1,022.117M |
| Combined liquid assets | $1,357.512M |

### Recomputed ratios (TTM through Q1 FY2027)

```
Net Margin (TTM)  = −$25.072M / $1,004.958M = −2.50%   (06-12: −5.86% on an FY2026-annual basis — a sharp narrowing, but still deeply negative, still fails >15%/>12%)
Gross Margin (TTM) = $871.69M / $1,004.958M = 86.7%     (06-12: 87% FY2026-annual — essentially unchanged, still a clear pass)
TTM Operating Loss = −$18.4M − $12.4M − $5.208M(*) − $15.749M = −$51.757M
  (*Q4 FY26 operating loss derived from its disclosed −2% GAAP operating margin × $260.4M revenue)
Invested Capital (2026-04-30) = Total Equity $1,031.386M − Cash & Equivalents $335.395M − $0 Debt = $695.991M
ROIC (TTM, computed) = −$51.757M / $695.991M = −7.44%
ROIC (third-party cross-check, same quarter-end) = −4.57% (stockanalysis.com)
```

**Neither previously-failing Phase 01 criterion (net margin, ROIC) crossed its threshold.** Net margin improved dramatically in absolute terms (−5.86% annual → −2.50% TTM) but remains far below >15%/>12%; ROIC remains meaningfully negative on both a freshly-computed and a third-party basis (−7.4% to −4.6%). **Per this task's explicit branching instruction, this confirms the addendum-only path — no fuller Phase 01 re-check or new dated file is warranted.**

### GAAP net income / SBC / insider-buying re-check

- **GAAP net income positive in any quarter? NO.** All 4 TTM quarters remain net-loss (−$9.2M, −$8.3M, −$2.6M, −$4.972M) — Q4 FY2026 came closest to breakeven, but Q1 FY2027 ticked back up slightly, not a clean monotonic path to positive.
- **Material SBC policy change? NO.** TTM SBC $209.185M / TTM Revenue $1,004.958M = 20.8%, down modestly from the FY2026-annual 22.5% cited on 06-12 (continued gradual dilution of the ratio as revenue outgrows SBC dollar growth — not a structural shift). Compensation structure (RSU-based, new-hire/annual-refresh/promotion grants, 4-year vesting) unchanged per the FY2026 10-K/DEF 14A.
- **CEO/CFO insider buying reported? Technically YES.** CEO Bill Staples: 4,188 shares at $29.36 (~$122,961) on 2026-06-30, and 6,010 shares at ~$21-22 (~$129,215) on 2026-03-31 — both Form 4-disclosed, both executed under a pre-arranged **Rule 10b5-1 trading plan** adopted 2025-09-25 (scheduled, not discretionary). Combined ~$252,176 over 6 months.

Per the 06-12 session's note, insider buying being reported reopens the **Turnaround Sub-Gate (Upgrade 4)** check:

1. Historical ROIC >15% for ≥5 of past 10 years — ❌ still fails outright (GitLab IPO'd Oct 2021, never posted a GAAP-profitable/high-ROIC year as a public company).
2. CEO/CFO insider buying >$500K in past 6 months (Form 4-verified, discretionary) — ❌ fails: $252,176 is roughly half the $500K bar, and it's 10b5-1 plan-driven, not discretionary open-market conviction buying.
3. Independent FV estimate ≥40% MOS — not built (moot).
4. Net Debt/EBITDA <3× — ✅ passes trivially (net cash, $0 debt).
5. Core moat still identifiable — ✅ yes.

Conditions 1 and 2 both still fail — **the Turnaround Sub-Gate remains closed.**

---

## 4. Quality Score Engine — GTLB's first-ever computation

Per [framework/quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29).

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 0.0 |
| Margins (15%) | 100.0 |
| Growth (20%) | 100.0 |
| Balance Sheet (15%) | 100.0 |
| Moat (15%) | 40.0 |
| FCF Quality (10%) | 0.0 |

```
Quality Score = 0.0×0.25 + 100.0×0.15 + 100.0×0.20 + 100.0×0.15 + 40.0×0.15 + 0.0×0.10
              = 0.00 + 15.00 + 20.00 + 15.00 + 6.00 + 0.00
              = 56.0
```

**Quality Score = 56.0 / 100.0 — fails the 80.0+ gate.** GTLB fails two independent ways at once, mirroring the CCL/CDR pattern:

1. **The weighted score itself** (56.0 < 80.0) — driven by Profitability clamped to 0.0 (net margin and ROIC both negative) and FCF Quality clamped to 0.0 (see caveat below).
2. **A hard disqualifier, independent of the weighted score: "not FCF-positive for 3+ consecutive years."** Using the same literal interpretation this framework's own CD Projekt (CDR) precedent (2026-06-29) established — the 3 most recently completed fiscal years must *all* be FCF-positive on a GAAP OCF−CapEx basis, with no carve-out available for this disqualifier — GitLab's FY2024 was FCF-positive (+$35.0M OCF), **FY2025 was FCF-negative (−$64.0M GAAP OCF**, independently sourced from GitLab's own FY2025 earnings release, unchanged from 06-12), and FY2026 was FCF-positive again (+$232.9M OCF). One negative year breaks the "3 consecutive positive years" requirement — the same two-positive-bracketing-one-negative pattern that fired this exact disqualifier for CDR.

Disqualifier #1 (FCF/NI conversion <70% for 2+ consecutive years) is arguably also triggered on a literal fiscal-year basis, since NI was negative in FY2024/FY2025/FY2026 alike — but that reading is flagged as an interpretive tension rather than resolved (the disqualifier's evident intent — catching cash flow *lagging* accounting profit — is the opposite of GitLab's actual situation, where SBC-driven non-cash losses make cash flow *exceed* accounting profit), since disqualifier #3 already independently and unambiguously fails the gate regardless.

**No Composite Score computed** (requires clearing the gate first). **No Phase 02 valuation work performed** (moot, gate fails).

### FCF Quality sub-score detail (the negative-NI/positive-FCF edge case)

```
TTM FCF = TTM OCF $275.76M − TTM CapEx $12.30M = $263.46M (positive, ~26% FCF margin)
TTM NI  = −$25.072M (negative)
Literal FCF/NI ratio = 263.46 / −25.072 = −1050.8%
FCFQuality_Score = clamp(((−10.508 − 0.40) / 0.60) × 100, 0, 100) = clamp(−1818, 0, 100) = 0.0
```

Applied mechanically per the stated formula (all inputs are known, GAAP-sourced figures — not a data gap), consistent with this framework's FUBO/CDR precedent of letting `clamp()` resolve negative-input edge cases rather than declaring the sub-score uncomputable. Flagged explicitly: a negative-NI/positive-FCF pairing driven by ~$209M TTM non-cash SBC is the *opposite* of the earnings-quality problem this sub-score exists to catch — GitLab's actual cash generation is robust and growing, not weak. The 0.0 score should be read with that caveat, not as evidence of poor cash conversion.

### Moat Signal detail (cited evidence required per signal)

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | FALSE | Only a share snapshot found (GitLab ~16.20% vs. GitHub ~37.98% of the source-code-management market), no cited YoY trend — falls short of the "stable or growing" evidentiary bar. GitLab's 4-consecutive-year Gartner Magic Quadrant Leader placement is directionally supportive but is a standing/recognition signal, not share data. |
| Brand premium (pricing power) | **TRUE** | 117-118% Net Retention Rate (FY2026/Q1 FY2027 earnings releases) + documented Duo/Duo Enterprise pricing escalation at renewal — customers moving from flat seat pricing to materially higher negotiated pricing for AI capabilities "increasingly integral to developer workflows." |
| Network effect | FALSE | No two-sided marketplace dynamic; single-application platform, not user-growth-driven network value. |
| Switching costs | **TRUE** | Integrated single-application DevSecOps platform (source code mgmt + CI/CD + security scanning + AI agents); $1.1B Total RPO (+18-20% YoY) / $724.1M cRPO (+24% YoY) evidencing multi-year contractual lock-in and deep workflow integration. |
| Scale cost advantage | FALSE | No cost-per-unit data found showing a documented gap vs. smaller competitors. |

Moat_Score = (2/5) × 100 = **40.0**

---

## 5. Recommendation

# **PASS — Quality Score 56.0/100.0, fails the 80.0+ gate (also independently failed by the FCF-positivity hard disqualifier). Do not enter. Watchlist addendum appended, no new file created.**

GitLab's TTM financials have genuinely improved since 06-12 — net margin narrowed from −5.86% (FY2026-annual basis) to −2.50% (TTM) — but the substance of the 06-12 Phase 01 FAIL is unchanged: net margin and ROIC remain decisively negative, and GitLab's first-ever Quality Score computation confirms the same conclusion from the new engine's angle. The FCF-positivity hard disqualifier (FY2025's negative GAAP OCF breaking an otherwise-positive 3-year streak) fails the gate independently of the 56.0 weighted score, mirroring the CDR precedent exactly. Insider buying was technically reported this cycle but falls well short of the Turnaround Sub-Gate's $500K/discretionary-buying bar, and the historical-ROIC condition still fails outright regardless.

**No position opened — nothing to log in `decisions/`.**

---

## 6. Files touched this session

- `watchlist/not-in-portfolio/GTLB/GTLB-2026-06-12.md` — appended the Rule 9 check, Turnaround Sub-Gate re-check, and Quality Score addendum as a dated note (no new file, per the task's branching instruction — no Phase 01 verdict change); added a Glossary section (the original 06-12 session predated the CLAUDE.md closing-Glossary requirement)
- `framework/glossary.md` — added **Gartner Magic Quadrant**, **Net Retention Rate (NRR / Dollar-Based Net Retention)**, **RPO (Remaining Performance Obligations) / cRPO**, and **Russell Reconstitution / Reclassification**
- `sessions/2026-07-09-new-position-gtlb.md` — this file

`watchlist/STALE.md` was not touched (GTLB was not listed there — it predates the Quality Score engine but was never a "stale re-score" case, it was a Phase 01 FAIL that had never been scored at all). No `git` commands were run.

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **10b5-1 Trading Plan** — a pre-arranged, scheduled insider stock-trading plan; not treated by this framework as satisfying the Turnaround Sub-Gate's discretionary insider-buying condition.
- **8-K** — a US company's "current report" filed with the SEC disclosing a material event between regular filings; used here as the primary source for GitLab's quarterly earnings-release exhibits.
- **CAGR** — Compound Annual Growth Rate.
- **CapEx** — Capital Expenditure.
- **cRPO** — the portion of RPO expected to be recognized as revenue within the next 12 months.
- **EBIT** — Earnings Before Interest and Taxes.
- **FCF** — Free Cash Flow.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check; not meaningful in the conventional sense when Net Income is negative and FCF is positive, as here.
- **Form 4** — the SEC filing disclosing an insider's change in beneficial ownership.
- **GAAP** — Generally Accepted Accounting Principles.
- **Gartner Magic Quadrant** — an analyst-firm vendor ranking; GitLab has been named a Leader for four consecutive years.
- **Gross Margin** — Gross Profit ÷ Revenue.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; GTLB's FCF-positivity check (FY2025 GAAP OCF negative) fires this one independently of the 56.0 weighted score.
- **Invested Capital** — the capital (debt + equity, net of cash) put to work in a business; the ROIC denominator.
- **Moat** — a durable competitive advantage.
- **Net Retention Rate (NRR)** — the percentage of recurring revenue retained/expanded from an existing customer cohort over 12 months; GitLab's 117-118% is cited as pricing-power/switching-cost Moat Signal evidence.
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Quality Score** — this framework's 0-100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. GTLB scores 56.0 on its first-ever computation.
- **ROIC** — Return on Invested Capital.
- **RPO (Remaining Performance Obligations)** — contracted-but-unrecognized subscription revenue; a forward demand/backlog metric.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.
- **Russell Reconstitution / Reclassification** — FTSE Russell's periodic rebalancing of its index family; GitLab's move from Growth to Value indices in June 2026 drove a documented, explainable price move via systematic fund flows.
- **SBC (Stock-Based Compensation)** — non-cash employee pay in company shares/options; a real dilutive cost to shareholders even though it inflates FCF relative to GAAP net income.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.
- **Turnaround Sub-Gate** — the conditional path (Hybrid Upgrade 4) letting a company failing some quality criteria still enter as a small position if it passes 5 specific tests; not reachable here (fails condition 1 outright, and condition 2 on both dollar-amount and discretionary-buying grounds).

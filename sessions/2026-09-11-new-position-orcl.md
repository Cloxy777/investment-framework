# NEW POSITION — ORCL (Oracle Corporation)

## 1. Session Header

| | |
|---|---|
| **Task type** | NEW POSITION |
| **Date** | 2026-09-11 |
| **10Y US Treasury yield** | 4.83% (FRED DGS10, last published close 2026-09-09 — no 2026-09-10/11 print yet available) |
| **Rate Regime Modifier bracket** | 3.5–5% → +5 (would apply if Phase 02 were reached; **moot**, see verdict below) |
| **Trigger** | Telegram posts (tarasguk, FinnInvestChannel) flagging Oracle's Q1 FY2027 earnings (reported after the close 2026-09-10). Per Rule 0, the Telegram text is used only as the prompt to re-run this evaluation — every number below is independently re-sourced from SEC EDGAR (the 8-K filed 2026-09-10, Exhibit 99.1) and IBKR, never from the post itself. |
| **Prior state on file** | [ORCL-2026-06-12.md](../watchlist/not-in-portfolio/ORCL/ORCL-2026-06-12.md) — Quality Score 38.7/100.0 (2026-07-10 addendum, reaffirmed unchanged 2026-07-16), fails the 80.0+ gate on two independent hard disqualifiers. Documented next-review-trigger: "ORCL's FY2027 Q1 earnings (~mid-September 2026)" — exactly this event. |

---

## 2. Data Gaps Flagged

- **FY2027 is still in progress** (fiscal year ends 2027-05-31; only Q1 FY2027, quarter ended 2026-08-31, has reported). Wherever a "trailing twelve months" (TTM) figure is used below, it is explicitly reconstructed as **FY2026 total − Q1 FY2026 + Q1 FY2027** from primary-source quarterly data (SEC 8-K Exhibit 99.1) — flagged as TTM, not treated as a completed fiscal year.
- **The Quality Score's two "N consecutive fiscal years" hard-disqualifier tests use only completed fiscal years** (FY2024–FY2026), per the framework's rolling-window convention ([quality-scoring.md](../framework/quality-scoring.md#the-strict-800-gate)) — Q1 FY2027 data is *not* used to evaluate those two tests, only the continuous sub-scores that call for TTM inputs (Profitability, Margins, Balance Sheet, FCF Quality).
- **FY2025 standalone Net Income** (used only for the FCF/NI carve-out discussion) is carried forward from the 2026-07-10 addendum's SEC-XBRL-sourced figure rather than re-derived here — nothing in this quarter's release changes that already-completed, audited fiscal year.
- No other gaps — every quantitative input below is sourced to a primary filing (SEC 8-K Ex-99.1 filed 2026-09-10, or the FY2026 10-K already verified 2026-07-10) or a live IBKR/FRED quote.

---

## 3. Live Price (Rule 0)

**IBKR** (contract_id 272800, NYSE, "ORACLE CORP" — confirmed via `search_contracts`):

| Field | Value |
|---|---|
| Last trade | **$159.62**, ts 2026-09-11 00:07:26 UTC (= 2026-09-10 8:07:26 PM EDT) |
| `is_close` | `false` — genuine live print, not a stale close |
| Bid / Ask | $159.59 / $159.80 |
| Change | +$6.68 / **+4.37%** |
| Dividend yield (trailing) | 1.24% |
| 52-week low / high | $114.51 / $328.36 |
| 13-week high | $195.28 |
| 26-week high | $250.24 |

**This is an after-hours quote, not a regular-session price** — Oracle reported Q1 FY2027 results after the 2026-09-10 4:00pm ET close. Cross-check ([stockanalysis.com](https://stockanalysis.com/stocks/orcl/)): regular-session close **$152.94** (−5.38%, 4:00pm ET) → after-hours **$159.30** (+4.16%, 7:59pm ET) — i.e. the stock actually *fell* into the print during the regular session, then jumped on the beat-and-raise release. IBKR's $159.62 (8:07pm ET) and stockanalysis.com's $159.30 (7:59pm ET) are 0.2% apart, 8 minutes apart, on a fast-moving post-earnings tape — both genuine live prints, consistent with each other. **Using $159.62 (IBKR) as the Rule-0 price of record.**

Note: stockanalysis.com's displayed 52-week high ($345.72) is stale relative to IBKR's rolling $328.36 — the $345.72 print has aged out of the trailing-52-week window between the two snapshots. Not decision-relevant here (see verdict).

Change vs. the last watchlist reference price ($125.99, 2026-07-16): **+26.69%** — fires the >15% Rule 9 threshold, but explained (earnings beat), not unexplained.

---

## 4. Quality Score Recomputation (Phase 01) — full re-derivation, 2026-06-29 engine (unchanged version)

Primary source for this session's new data: **SEC EDGAR, CIK 0001341439, 8-K filed 2026-09-10, accession [0001193125-26-387905](https://www.sec.gov/Archives/edgar/data/1341439/000119312526387905/0001193125-26-387905-index.htm), Exhibit 99.1** — Q1 FY2027 (quarter ended 2026-08-31) condensed financial statements. Cross-referenced against the FY2026 10-K (filed 2026-06-22) already verified in the 2026-07-10 session for prior-fiscal-year figures.

### Q1 FY2027 vs. Q1 FY2026 — as reported

| ($M except EPS) | Q1 FY2027 | Q1 FY2026 | Change |
|---|---|---|---|
| Total revenue | 19,345 | 14,926 | +30% |
| Cloud revenue | 11,607 | 7,186 | +62% |
| — Cloud Infrastructure (IaaS) | 7,388 | 3,347 | +121% |
| — Cloud Applications (SaaS) | 4,219 | 3,839 | +10% |
| GAAP operating income | 6,728 | 4,277 | +57% |
| Non-GAAP operating income | 8,151 | 6,236 | +31% |
| GAAP net income | 4,760 | 2,927 | +63% |
| Net income available to common (after $81M preferred dividends) | 4,679 | 2,927 | +60% |
| GAAP diluted EPS | $1.56 | $1.01 | +55% |
| Non-GAAP diluted EPS | $1.92 | $1.47 | +30% |
| GAAP operating cash flow | 23,103 | 8,140 | +184% |
| Capital expenditures | (28,499) | (8,502) | +235% |
| **Free cash flow (OCF − CapEx)** | **(5,396)** | (362) | more negative |
| RPO | $664B (+$209B YoY) | — | — |

RPO grew from $638B (end of FY2026, 2026-06-10) to **$664B** — Oracle booked >$30B of *additional* AI cloud contracts this quarter alone. Independent press confirms ~$300B of total RPO is attributable to a single counterparty (OpenAI) — the same customer-concentration risk already flagged by S&P in its 2026-07-09 downgrade, now reinforced, not resolved. [Sources: Oracle 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1341439/000119312526387905/orcl-ex99_1.htm); [Gokhshtein, "Oracle's $300B OpenAI Bet," 2026-09-09](https://gokhshtein.com/news/2026-09-09-oracles-300b-openai-bet-rpo-surge-masks-execution-risk); [Yahoo Finance, "Oracle stock wins reprieve... despite ongoing OpenAI concerns"](https://finance.yahoo.com/news/oracle-stock-wins-reprieve-on-strong-results-despite-ongoing-openai-concerns-162927985.html).

### TTM reconstruction (Q2 FY2026 + Q3 FY2026 + Q4 FY2026 + Q1 FY2027 = FY2026 total − Q1 FY2026 + Q1 FY2027)

| Metric | FY2026 total | − Q1 FY2026 | + Q1 FY2027 | = TTM (through 2026-08-31) |
|---|---|---|---|---|
| Revenue | 67,357 | 14,926 | 19,345 | **71,776** |
| Net income (pre-preferred-div) | 17,087 | 2,927 | 4,760 | **18,920** |
| GAAP operating income | 20,606 | 4,277 | 6,728 | **23,057** |
| Capital expenditures | 55,663 | 8,502 | 28,499 | **75,660** |
| Operating cash flow | 31,977 | 8,140 | 23,103 | **46,940** |
| **Free cash flow** | (23,686) | (362) | (5,396) | **(28,720)** |
| Tax provision | 2,467 | 500 | 847 | **2,814** |
| Pretax income | 19,554 | 3,427 | 5,607 | **21,734** |
| Depreciation | 7,623 | 1,351 | 3,156 | **9,428** |
| Amortization of intangibles | 1,671 | 420 | 202 | **1,453** |
| Gross profit (Revenue − Cloud/Hardware/Services cost lines) | 44,336 | 10,042 | 11,612 | **45,906** |

**TTM free cash flow is now −$28.72B — the most negative trailing-twelve-month reading yet** (vs. FY2026's already-negative −$23.69B), because Q1 FY2027 capex ($28.5B) alone exceeds the whole of Q1 FY2026's capex more than 3×. The capex ramp is *accelerating*, not stabilizing.

### Sub-score computation

**Profitability (25% weight)**
```
TTM Net Margin  = 18,920 / 71,776 = 26.36%  →  NetMargin_Component = clamp(26.36/30×100) = 87.9
TTM effective tax rate = 2,814 / 21,734 = 12.95%
TTM NOPAT = GAAP Op. Income TTM × (1 − tax rate) = 23,057 × (1 − 0.1295) = $20,073M
Invested Capital (8/31/26 balance sheet) = Total Debt + Equity − Cash
  Total Debt (Notes payable current $7,625M + non-current $117,712M) = $125,337M
  Equity $67,196M (jumped from $43,056M at 5/31/26 — the $20B ATM raise)
  Cash $36,369M
  Invested Capital = 125,337 + 67,196 − 36,369 = $156,164M
TTM ROIC = 20,073 / 156,164 = 12.85%  →  ROIC_Component = clamp(12.85/30×100) = 42.8

Uncapped Profitability_Score = (87.9 + 42.8) / 2 = 65.4
FCF-positivity cap applies (not FCF-positive 3 consecutive fiscal years, see disqualifier below)
```
**Profitability_Score = 40.0 (capped; would be 65.4 uncapped)** — a real improvement over the 2026-07-10 addendum's 60.3 uncapped figure (ROIC up from 10.78% to 12.85% TTM, on the earnings beat), but the cap still binds because the underlying cash-flow-quality problem hasn't cleared.

**Margins (15% weight)**
```
Q1 FY2027 Gross Profit = 19,345 − (Cloud/software cost $6,400 + Hardware cost $281 + Services cost $1,052) = $11,612M  (60.0% margin)
Q1 FY2026 Gross Profit = 14,926 − (3,607+178+1,099) = $10,042M  (67.3% margin)
TTM Gross Profit = 44,336 − 10,042 + 11,612 = $45,906M
TTM Gross Margin = 45,906 / 71,776 = 63.96%  →  GrossMargin_Score = clamp(63.96/80×100) = 79.9
```
No structural-trend bonus — margin is still **contracting**, and the contraction has *widened*: FY2023 72.85% → FY2024 71.41% → FY2025 70.51% → FY2026 65.82% → **TTM (through Q1 FY2027) 63.96%**. Consistent with the AI-datacenter cost ramp management has repeatedly flagged.
**Margins_Score = 79.9**

**Growth (20% weight)**
```
Revenue 3yr CAGR (FY2023 $49.954B → FY2026 $67.357B, most recent completed fiscal years) = 10.48%  (unchanged — no new FY has completed)
Growth_Score raw = clamp(10.48/25×100) = 41.9
+10 documented TAM-expansion modifier: RPO $664B (+$209B YoY, +$30B+ booked this quarter alone); Cloud Infrastructure revenue +121% YoY
No deceleration penalty — growth is accelerating, and has accelerated further: FY2024 +6.0% → FY2025 +8.4% → FY2026 +17.3% → Q1 FY2027 +30% YoY total revenue growth
```
**Growth_Score = 51.9**

**Balance Sheet (15% weight)**
```
EBITDA (TTM, GAAP-derived) = Op. Income TTM $23,057M + D&A TTM ($9,428M Depreciation + $1,453M Amortization = $10,881M) = $33,938M

PRIMARY (broad — Notes payable/borrowings + non-current Operating lease liabilities, consistent with the 2026-07-10 addendum's methodology):
  Total Debt = $125,337M (notes payable) + $30,594M (non-current op. lease liabilities) = $155,931M
  Net Debt = 155,931 − 36,369 (cash) = $119,562M
  Net Debt/EBITDA = 119,562 / 33,938 = 3.52×
  BalanceSheet_Score = clamp(100×(1 − 3.52/4)) = 11.9

CROSS-CHECK (narrow — notes payable/borrowings only, no lease liabilities):
  Net Debt = 125,337 − 36,369 = $88,968M
  Net Debt/EBITDA = 88,968 / 33,938 = 2.62×
  BalanceSheet_Score = clamp(100×(1 − 2.62/4)) = 34.5
```
**Both methods exceed the 2.5× standard threshold** (asset-light override — Upgrade 5's <4× — does not apply; Oracle remains a capital-intensive infrastructure operator, reaffirming every prior session's finding). **This is a genuine, material improvement** from the 2026-07-10 read (3.73×–4.18×) — driven by the $20B ATM equity raise (retained partly as cash, cutting net debt) and the EBITDA surge from this quarter's earnings beat — but it does not clear the bar under either interpretation. Using the *most* favorable plausible reading (narrow debt, cash + $708M marketable securities netted) still yields ≈2.60× — still over 2.5×.
**BalanceSheet_Score = 11.9 (primary); 34.5 (cross-check) — same conclusion (disqualifier fires) either way.**

**Moat Signal (15% weight)** — reassessed against the same 5-point checklist; no new evidence found this session that changes any signal's verdict:

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable/growing | **FALSE** | Gartner's DBMS market-share analysis (cited 2026-04-21, no fresher data found this session) still describes Oracle's share as "slowly eroding" — wrong direction for a "stable or growing" claim. |
| Brand premium / pricing power | **TRUE** | Automatic 8% annual price escalation on standard support/subscription renewals; January 2026 Java SE relicensing raised list pricing up to 17× for some enterprise customers, largely absorbed rather than migrated away from (carried forward, unchanged; no new pricing action found this session). |
| Network effect | **FALSE** | No citable two-sided-marketplace mechanism. |
| Switching costs | **TRUE** | Same Java relicensing lock-in evidence, reinforced by #1 DB-Engines database-popularity ranking (Jan 2026) reflecting a very large, high-migration-cost installed base. |
| Scale cost advantage | **FALSE** | No cost-per-unit data found vs. AWS/Azure/GCP. |

**Moat_Score = (2/5) × 100 = 40.0.** Qualitative context (not a scored signal): the ~$300B of RPO tied to a single counterparty (OpenAI) is a *concentration* risk, not moat evidence either way — flagged here for completeness since it dominated this quarter's analyst commentary, but it doesn't move any of the 5 checklist items.

**FCF Quality (10% weight)**
```
TTM FCF/NI = −28,720 / 18,920 = −151.8%  →  clamp(((−1.518 − 0.40)/0.60)×100) = 0.0
```
**FCFQuality_Score = 0.0**

Hard-disqualifier check (2+ consecutive years, FY basis, unchanged since no new FY has completed): FY2025 FCF/NI ≈ **−3.2%**, FY2026 FCF/NI = −23,686/17,087 = **−138.6%** — both under 70% for 2 consecutive years. This **does not independently fire** because of the same documented growth-capex explanation already established 2026-07-10 (the entire capex ramp is transparently tied to contracted RPO, not maintenance spend) — same carve-out treatment as this framework's MU precedent.

### Hard disqualifiers — re-tested on the current rolling window (FY2024–FY2026, the most recently completed fiscal years)

| Disqualifier | FY2024 | FY2025 | FY2026 | Fires? |
|---|---|---|---|---|
| Not FCF-positive 3+ consecutive years | +$11.807B | **−$0.394B** | **−$23.686B** | **YES — unconditional, no carve-out applies to this one.** Two of the last three completed fiscal years are negative; there is no 3-year positive streak in the current window. Q1 FY2027 (−$5.396B) continues the negative trend rather than reversing it — TTM FCF is now −$28.72B, the most negative TTM reading on file. |
| Net Debt/EBITDA over threshold | — | — | 3.73×–4.18× (07-10) | **YES**, still — now 2.62×–3.52× TTM (see Balance Sheet above). Materially improved, but every methodology tested still exceeds the 2.5× standard threshold; asset-light override does not apply. |
| FCF/NI conversion <70% for 2+ years, no carve-out | — | −3.2% | −138.6% | Carve-out applies (documented growth-capex explanation) — does not independently fire. |

### Final Quality Score

```
Quality Score = Profitability×0.25 + Margins×0.15 + Growth×0.20 + BalanceSheet×0.15 + Moat×0.15 + FCFQuality×0.10
              = 40.0×0.25 + 79.9×0.15 + 51.9×0.20 + 11.9×0.15 + 40.0×0.15 + 0.0×0.10
              = 10.00 + 11.985 + 10.38 + 1.785 + 6.00 + 0.00
              = 40.15  →  round (exactly on ".X5" → round up) →  40.2
```

**Quality Score = 40.2 / 100.0** (cross-check using the narrow Balance Sheet reading instead: 43.5 — same conclusion either way).

### Gate Verdict: **FAILS the 80.0+ gate**

Two independent conditions both fail it at once, same dual-failure pattern as the 2026-07-10/07-16 sessions:
1. **The weighted score itself** (40.2, or 43.5 under the alternate Balance Sheet reading) is far short of 80.0.
2. **The "not FCF-positive for 3+ consecutive years" hard disqualifier fires unconditionally** — no carve-out exists for it, and it is not a knife-edge reading: two of the last three completed fiscal years are negative, and the trailing-twelve-month trend has gotten *more* negative, not less, since the last check.
3. The **Net Debt/EBITDA hard disqualifier also independently fires** under every methodology tested (2.62×–3.52× TTM vs. the 2.5× standard threshold) — narrower than in July, but still over the line.

**Net effect vs. the 2026-07-10/07-16 addenda: real, measurable improvement (38.7 → 40.2; ROIC 10.78% → 12.85% TTM; leverage 3.73–4.18× → 2.62–3.52× TTM) driven by this quarter's earnings beat and the completed $20B equity raise — but not remotely close to closing the gap to 80.0, and the specific facts that disqualify Oracle (cash-burn depth, leverage) both remain on the wrong side of their thresholds.** Per [quality-scoring.md](../framework/quality-scoring.md) and this task's branching instruction: **stop here. No Rate Environment Gate, no Phase 02 valuation score, and no Composite Score are computed** — a Quality Score below 80.0 is not eligible for either, regardless of how cheap the stock looks post-move.

---

## 5. Recommendation

**PASS — watchlist only, do not buy.** Same action category as every prior ORCL entry (2026-06-12, 2026-07-10, 2026-07-16) — this session **does not change the action**, but it does refresh every underlying number against a genuine Rule 9 fundamental trigger (earnings release) with a materially different (improved, but still failing) picture underneath, which is why a new dated watchlist row is warranted rather than a "no change" line.

Why: the framework's Quality Score gate is a strict, non-negotiable 80.0+ bar before any valuation work is even attempted, and Oracle's Q1 FY2027 beat — real and substantial as it is (revenue +30%, GAAP EPS +55%, RPO +$209B YoY) — does not change the trailing cash-flow and balance-sheet facts the gate is built to catch: TTM free cash flow is more negative than it has ever been on file here (−$28.72B), and leverage, while improved, is still over the 2.5× standard threshold. A market rewarding forward guidance and RPO growth with a >4% after-hours pop is not itself a signal this framework's Phase 01 gate is built to act on (trailing financials, not narrative or price action) — consistent with every prior ORCL session's core finding: "trailing financials fail despite strong forward narrative."

**Next review trigger:** ORCL's FY2027 Q2 earnings (guided for 30–34% revenue growth; call typically ~early December 2026); FY2027 fiscal year-end 10-K (~July 2027) — the first point at which a full completed fiscal year could show FCF stabilizing or the leverage ratio crossing back under 2.5×; any further credit-rating action (Moody's/Fitch both carry negative outlooks as of the 2026-07-09 S&P downgrade); resolution of the ~$300B OpenAI RPO concentration risk (a completed, funded delivery track record vs. a funding shortfall becoming apparent); Net Debt/EBITDA crossing under 2.5× on a full-FY basis; a full fiscal year of positive FCF; ROIC clearing 15%; >15% unexplained price move from the new reference price of **$159.62** (superseding $125.99).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session (all pre-existing entries — none needed adding): 8-K, 10-K, After-hours trading, ATM Program (At-the-Market Offering Program), Basis points (bps), CAGR, CapEx, Composite Score, EBIT, EBITDA, EDGAR, EPS, Effective tax rate, FCF, FCF/NI conversion ratio, FCF Yield, GAAP, Gross Margin, Hard disqualifier, IaaS, Investment grade, Invested Capital, Moat, Moat Signal, Net Debt/EBITDA, Net Margin, Non-GAAP, NOPAT, Quality Score, Rate Environment Gate, Rate Regime Modifier, ROIC, RPO (Remaining Performance Obligations), SaaS, TTM (Trailing Twelve Months), XBRL.

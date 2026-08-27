# RESCORE — NVDA (NVIDIA Corporation)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-08-27
**10Y US Treasury Yield:** 4.65% (TradingEconomics, US 10Y Note yield, close 2026-08-26, queried 2026-08-27 — [tradingeconomics.com/united-states/government-bond-yield](https://tradingeconomics.com/united-states/government-bond-yield))
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** NVDA **21.3** Composite (Quality 91.7 / Valuation 34.3), 2026-07-05 — [sessions/2026-07-05-rescore-nvda.md](2026-07-05-rescore-nvda.md)
**Current NVDA portfolio weight:** ≈6.80% live (19 sh × $218.81 = $4,157.39 ÷ $61,101.28, the last portfolio-wide combined total on file in [holdings.md](../portfolio/holdings.md), dated 2026-08-23 — this session refreshes NVDA's own numbers only, not a full portfolio resync) — essentially unchanged from the 6.78% stated in holdings.md; comfortably under the 15% hard cap (Upgrade 7) and already at/near the top of the Composite Score's target position band (see §10).
**Not on the stale-score registry** ([watchlist/STALE.md](../watchlist/STALE.md)) — checked, no pending mark to clear.

## Why this session ran

**Unattended Routine 6 (Telegram Stock-Mention Scan) trigger.** Two monitored channels posted about NVIDIA's Q2 FY2027 results within minutes of each other on 2026-08-26:

| Channel | Post ID | Timestamp (UTC) |
|---|---|---|
| tarasguk | 11782 | ~20:26 |
| FinnInvestChannel | 3149 | ~20:40 |

**Provenance only — not a data source.** Per this task's explicit instruction, none of the figures those posts claimed (revenue ~$96.2B, adj EPS ~$2.22, Data Center ~$89B, Q3 guide ~$108B, gross margin ~75%/~74% guide) were used as inputs below. Every financial figure in this session was independently pulled from NVIDIA's own SEC 8-K press release, SEC EDGAR XBRL `companyfacts` data, IBKR live pricing, and third-party consensus/price-target aggregators (cited inline, §1 and §4). **The independently-sourced figures turned out to match the posts' claims almost exactly** (see §2) — which just means the posts were accurate, not that they were relied upon.

This also happens to be a **legitimate, independent Rule 9 trigger in its own right**: NVDA reported Q2 FY2027 earnings after close 2026-08-26 (quarterly-earnings trigger) and issued fresh Q3 FY2027 guidance (guidance-revision trigger) — this would have been due for a scheduled re-score regardless of the Telegram scan, per the "Next review trigger" on file in [watchlist/in-portfolio/NVDA/NVDA-2026-07-05.md](../watchlist/in-portfolio/NVDA/NVDA-2026-07-05.md).

> *Jargon decoded on first use throughout — see closing Glossary.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$218.81** | IBKR `get_price_snapshot` (contract_id 4815747, NASDAQ), intraday last trade, 2026-08-27. Bid/ask $218.80/$218.95. |
| Prior close | $209.66 | IBKR `change`/`prior_close`; independently cross-checked against Yahoo Finance's `/v8/finance/chart/NVDA` `chartPreviousClose` (also $209.66). |
| Today's move | **+$9.15 / +4.36%** | IBKR `change` — the market's reaction to the Q2 FY2027 beat + raised Q3 guide reported after close 2026-08-26. Explained by a clear fundamental trigger (not a Rule 9 "unexplained move" candidate; also well under the 15% threshold either way). |
| 52-week range | $164.04 – $236.54 | IBKR `misc_statistics` |
| YTD change | +17.33% | IBKR `year_to_date_change` |
| Analyst consensus PT | mean **$305.79**, median $300.00, high $500, low $180, 61 analysts, "Strong Buy" | stockanalysis.com/stocks/nvda/forecast/, pulled 2026-08-27 (post-earnings). Cross-checked against a second aggregator (marketbeat.com): mean $308.46, high $500, low $218, 54 analysts, "Moderate Buy" — a real cross-provider spread (different analyst panels/timing), flagged not reconciled; stockanalysis.com's figures used throughout for internal consistency with the EPS-estimate figures pulled from the same source (§4). Bull-case sanity check only (Rule 0 Step 4), not a scored input. |

---

## 2. Independent Verification of NVIDIA's Q2 FY2027 Results (primary source, not the Telegram posts)

Pulled directly from NVIDIA's SEC 8-K (Exhibit 99.1 press release), filed 2026-08-26: [sec.gov/.../q2fy27pr.htm](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm)

| Metric | Actual (SEC 8-K, primary source) | Telegram posts' unverified claim | Match? |
|---|---|---|---|
| Total revenue | $96,221M | ~$96.2B | ✅ matches |
| Data Center revenue | $89.0B (+117% YoY) | ~$89B | ✅ matches |
| Non-GAAP diluted EPS | $2.22 | ~$2.22 | ✅ matches |
| GAAP diluted EPS | $2.46 | not claimed | — |
| GAAP / non-GAAP gross margin | 75.0% / 75.0% | ~75% actual | ✅ matches |
| Q3 FY2027 revenue guide | $108.0B ± 2% | ~$108B | ✅ matches |
| Q3 FY2027 gross margin guide | 74.0% ± 50bps | ~74% guide | ✅ matches |
| Cash + equivalents (2026-07-26) | $22,443M | not claimed | — |
| Total debt (2026-07-26) | $33,366M | not claimed | — |
| Capital returned to shareholders (Q2) | ≈$26.0B (buybacks + dividends) | not claimed | — |

**Conclusion: the Telegram posts were accurate**, but every figure above is cited to the SEC 8-K, independently retrieved — the posts are logged for provenance only, per the task's instruction.

---

## 3. Data Gaps / Sourcing Notes (flagged, not silently worked around)

1. **`yfinance` unavailable this entire session — persistent rate-limiting, not transient.** Every attempt (5 retries across the session, including after multi-minute gaps doing other work) returned `YFRateLimitError` / HTTP 429 on the crumb fetch, through both the direct client and the documented `requests.Session()`-with-CA-bundle workaround. This is the first NVDA session where the framework's usual `yfinance` pipeline was fully unavailable. **Substitute sourcing used instead** (all real, cited, primary or reputable-secondary sources — nothing invented):
   - **SEC EDGAR XBRL `companyfacts` API** (`data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json`) for all TTM financial-statement rollups (revenue, EBIT, net income, cash flow, balance sheet, historical quarterly diluted EPS) — arguably a *stronger* primary source than `yfinance` for these, since it's the SEC's own structured data pulled directly from filed 10-Qs/10-Ks.
   - **stockanalysis.com** (forecast, overview, and quarterly-ratios pages) for analyst consensus EPS estimates, price targets, and a pre-built quarterly trailing-PE history table (used for the 5yr PE reconstruction, §4).
   - **IBKR** for live price (as always, Rule 0) and 52-week range.
   - **WebSearch** for the current 10Y Treasury yield and NVIDIA's confirmed/estimated next earnings date.
2. **5-year PE reconstruction — sourced differently than the 07-05/06-20 sessions, flagged.** Those sessions manually reconstructed a trailing-PE series from `yfinance`'s `get_earnings_dates` + price history. With `yfinance` unavailable, a from-scratch SEC-XBRL reconstruction was attempted first and **rejected**: NVIDIA's two stock splits (4-for-1 Jul 2021, 10-for-1 Jun 2024) mean a 10-Q's prior-year comparative EPS figure is only ever refiled on the split-adjusted basis if that specific historical quarter happens to still be shown as a comparative in a filing made *after* the relevant split — many older quarters aren't, so a naive SEC-only pull mixes split bases. Caught this via a sanity check: a naive pull implied a −$1.00 Q4 FY2023 EPS, inconsistent with NVIDIA's actual ~$1.4B Q4 FY2023 net income — **rejected, not used**. Instead, used **stockanalysis.com's pre-built quarterly trailing-PE table** (already split-consistent), trailing 20 quarters (Jan '22 – Aug '26): **5yr avg PE 57.77×, range 25.97×–142.78×** (vs. the 07-05 session's yfinance-derived 56.54× avg / 36.32×–122.27× range — reasonably close, continued downward drift in the low/high band consistent with the ongoing PE-compression trend already noted in prior sessions).
3. **Forward EPS — same open methodology item flagged in the 07-05/06-20 sessions, unresolved.** stockanalysis.com's forecast page labels a $9.02 "FY2026 (Current)" and $13.04 "FY2027 (Next Year)" EPS estimate — but $9.02 doesn't match NVIDIA's own actual FY2026 diluted EPS ($4.90, already reported), confirming (consistent with the prior sessions' finding on `yfinance`'s equivalent field) that this vendor's fiscal-year labels are offset from NVIDIA's own convention by roughly one year, and the figure actually being read is closer to a "+1y-out" consensus than a strict next-twelve-months figure. Used **$13.04** as Forward EPS (continuing the same, imperfect-but-consistent convention as the prior two sessions, for score comparability) → **Forward PE = $218.81 ÷ $13.04 = 16.78×**. Flagged, not corrected — still an open item for a future `decisions/` entry.
4. **PEG — self-computed this session, not sourced from `yfinance`'s `trailingPegRatio` field (unavailable).** Computed directly per Lynch's original definition (PE ÷ expected EPS growth rate): Forward PE (16.78×) ÷ forward EPS growth rate (44.6%, stockanalysis.com's own stated "FY2026→FY2027" EPS growth, on the same offset labeling as above) = **PEG 0.376**. Different computation basis than the `trailingPegRatio` field the 07-05 session used (0.608) — but both land near the PEG_Score's 0.0 floor (≤0.5 → 0), so the different methodology is immaterial to the final sub-score this session; flagged for transparency regardless.
5. **Balance sheet composition changed materially this quarter — real, not a data artifact.** Total debt jumped from $12,348M (07-05 session, 2026-04-30 balance sheet) to **$33,366M** (2026-07-26) — NVIDIA raised ~$24.9B of new debt in H1 FY2027 (`ProceedsFromDebtNetOfIssuanceCosts`, SEC XBRL). Cash + short-term marketable securities also fell from $80,572M to **$56,586M** ($22,443M cash + $34,143M current marketable securities). Net effect: the net-cash cushion shrank from −$68.2B to **−$23.2B** — still comfortably net-cash (Balance Sheet sub-score still caps at 100.0 either way, §5), but a real, worth-watching shift, not a rounding difference. Separately, the balance sheet now also carries **~$90.7B combined** in strategic equity stakes in other companies (`EquitySecuritiesFvNi` $42.78B + `EquitySecuritiesWithoutReadilyDeterminableFairValueAmount` $47.9B, SEC XBRL) — consistent with NVIDIA's widely-reported 2025–2026 wave of strategic AI-ecosystem investments (e.g. the disclosed OpenAI commitment cited in this framework's own AMZN glossary entry for the Series C Preferred Stock term). **Deliberately excluded from the Net Debt calc** (illiquid/less-liquid, not cash-equivalent) — conservative treatment, consistent with the framework's existing "Cash + ST Investments" convention.
6. **FCF/NI conversion — TTM reading has dropped meaningfully below the 07-05 session's figure; annual data still clears the hard-disqualifier bar. See §5 for the full number and why it doesn't trigger a disqualifier, and §5 for why this is the swing factor in this session's Quality Score decline.**
7. **Next earnings date — third-party estimate, not yet NVIDIA-confirmed.** Q3 FY2027 earnings estimated **25 Nov 2026, after close** (tipranks.com/marketbeat.com earnings calendars) — NVIDIA's own investor-relations site had not yet posted an official date as of this session (typical this far out; the 07-05 session's Q2 date was similarly sourced from calendar aggregators before IR confirmation, and that estimate proved correct).

---

## 4. NVDA — Inputs Collected (TTM rollup, SEC EDGAR XBRL `companyfacts`, CIK 0001045810)

**Sector:** Technology — Semiconductors (AI Compute & Data-Center GPUs)
**TTM window: Q3 FY2026 (Oct 2025) + Q4 FY2026 (Jan 2026, derived) + Q1 FY2027 (Apr 2026) + Q2 FY2027 (Jul 2026)**

| Item | Value | Source / derivation |
|---|---|---|
| Shares outstanding | 24,100,000,000 | SEC 10-Q cover page (`dei:EntityCommonStockSharesOutstanding`), filed 2026-08-21 — freshest figure on file |
| **Market Cap** | 24.1B × $218.81 = **$5,273,321M** | Computed |
| TTM Revenue | $57,006M+$68,127M+$81,615M+$96,221M = **$302,969M** | SEC XBRL quarterly rollforward (Q4 FY26 derived: FY26 annual $215,938M − 9mo FY26 $147,811M = $68,127M) |
| TTM EBIT (Operating Income) | $36,010M+$44,299M+$53,536M+$63,734M = **$197,579M** | Same derivation method |
| TTM Net Income | $31,910M+$42,960M+$58,321M+$59,688M = **$192,879M** | Same |
| TTM Pretax Income / Tax | $229,744M / $36,865M | Same |
| **Effective tax rate (TTM)** | 36,865/229,744 = **16.05%** | Computed |
| TTM Operating Cash Flow | $23,751M+$36,188M+$50,344M+$24,077M = **$134,360M** | SEC XBRL — Q2 FY27 alone ($24,077M) matches the 8-K's disclosed "Operating cash flow: $24,077M (Q2 only)" exactly |
| TTM CapEx (`PaymentsToAcquireProductiveAssets`) | $1,636M+$1,284M+$1,757M+$2,677M = **$7,354M** | SEC XBRL — Q2 FY27 alone ($2,677M) implies Q2 FCF of $21,400M, vs. the 8-K's disclosed $21,341M — a $59M (0.3%) gap, likely NVIDIA's own FCF definition netting a small additional investing-activity item; immaterial, flagged not reconciled further |
| **TTM FCF** | $134,360M − $7,354M = **$127,006M** | Computed |
| TTM D&A | $751M+$812M+$997M+$1,127M = **$3,687M** | SEC XBRL |
| **TTM EBITDA** | $197,579M + $3,687M = **$201,266M** | Computed |
| TTM Gross Profit | $41,849M+$51,093M+$61,157M+$72,142M = **$226,241M** | SEC XBRL |
| **Gross Margin (TTM)** | 226,241/302,969 = **74.68%** | Computed |
| **Net Margin (TTM)** | 192,879/302,969 = **63.66%** | Computed |
| Total Debt (2026-07-26) | $1,000M (current) + $32,366M (noncurrent) = **$33,366M** | SEC XBRL — matches 8-K exactly |
| Cash + ST marketable securities (2026-07-26) | $22,443M + $34,143M = **$56,586M** | SEC XBRL (`CashAndCashEquivalentsAtCarryingValue` + `DebtSecuritiesCurrent`) |
| **Net Debt** | $33,366M − $56,586M = **−$23,220M (net cash)** | Computed — see Data Gap #5 for the material shrinkage vs. 07-05 |
| **Enterprise Value** | $5,273,321M + (−$23,220M) = **$5,250,101M** | Computed |
| **EV/EBIT** | $5,250,101M ÷ $197,579M = **26.57×** | Computed. Cross-check: stockanalysis.com's own live EV/EBIT read 25.39× (computed off a slightly earlier/lower price) — consistent once re-based to the same price, validates methodology |
| Stockholders' Equity (2026-07-26) | $228,984M | SEC XBRL |
| **Invested Capital** (Debt+Equity convention) | $33,366M + $228,984M = **$262,350M** | Computed |
| **NOPAT** | $197,579M × (1−0.1605) = **$165,873M** | Computed |
| **ROIC (TTM)** | $165,873M ÷ $262,350M = **63.21%** | Computed — far above the 30% component ceiling either way |
| Revenue 3yr CAGR (FY2023 $26,974M → FY2026 $215,938M) | (215,938/26,974)^(1/3) − 1 = **100.05%** | SEC XBRL annual — matches prior sessions exactly (both figures independently re-verified this session) |
| Forward EPS (vendor "+1y"-offset figure, see Data Gap #3) | $13.04 | stockanalysis.com/stocks/nvda/forecast/ |
| **Forward PE** | $218.81 ÷ $13.04 = **16.78×** | Computed |
| PEG (self-computed, see Data Gap #4) | **0.376** | Computed: 16.78 ÷ 44.6% forward EPS growth |
| 5yr avg/range PE | avg **57.77×**, range **25.97×–142.78×** (n=20 quarters) | stockanalysis.com quarterly ratios table, see Data Gap #2 |
| FCF/NI conversion (TTM) | 127,006/192,879 = **65.85%** | Computed — see §5 for the hard-disqualifier check and trend |
| FCF/NI conversion (annual, FY23–FY26) | 87.18% / 90.80% / 83.50% / 80.51% | SEC XBRL annual OCF/CapEx/NI — all comfortably above 70% |
| Diluted weighted-avg shares (Q2 FY27 vs Q2 FY26) | 24,285M vs 24,532M | SEC XBRL — net buyback yield ≈ **+1.007%/yr** |
| Dividend rate (forward run-rate) | $1.00/yr (0.457% of $218.81) | 8-K: "$0.25 per share on October 1, 2026" |
| Next earnings | ~25 Nov 2026, after close (Q3 FY2027), unconfirmed by NVIDIA IR as of this session | tipranks.com / marketbeat.com — see Data Gap #7 |

---

## 5. NVDA — Quality Score (2026-06-29 methodology)

**Hard disqualifier check:**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ *fiscal years* unexplained? | Most recently completed FYs: **FY2025 83.50%, FY2026 80.51%** — both comfortably ≥70% (per the rolling-window clarification, only completed fiscal years count, not TTM) | disqualify if <70% for 2+ *years* | ✅ PASS — but see the TTM flag below |
| Net Debt/EBITDA over threshold? | **−0.115× (net cash)**, though the cushion shrank materially this quarter (Data Gap #5) | disqualify if >2.5× | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FCF-positive every year on record (FY2023–2026) and TTM ($127.0B) | disqualify if not | ✅ PASS |

**No hard disqualifier triggers.** But flag clearly: **the TTM (rolling 4-quarter) FCF/NI ratio has fallen to 65.85%** — below 70% for the first time in this framework's NVDA coverage, and a real, accelerating decline (87.18% → 90.80% → 83.50% → 80.51% → 65.85% TTM). This does **not** trip the disqualifier (which is evaluated on completed fiscal years, both of which still clear 70%), but it is the single largest driver of this session's Quality Score decline (see FCF Quality sub-score below) and worth close monitoring at FY2027 year-end (Jan 2027) — cash conversion is lagging net-income growth as capex ramps for the AI-infrastructure buildout (TTM capex $7,354M vs. $6,572M last session) and working capital scales with the business.

### Profitability (25% weight)

```
Net Margin (TTM)    = 192,879/302,969 = 63.66%
NetMargin_Component = clamp((63.66/30)×100, 0, 100) = 100.0   (cap)

ROIC (TTM)           = 165,873/262,350 = 63.21%
ROIC_Component       = clamp((63.21/30)×100, 0, 100) = 100.0   (cap)

Profitability_Score  = (100.0 + 100.0) / 2 = 100.0   (no FCF cap — FCF-positive every year on record)
```

### Margins (15% weight)

```
Gross Margin (TTM) = 74.68%
GrossMargin_Score = clamp((74.68/80)×100, 0, 100) = 93.35
```
No structural-trend bonus needed — already well above the 40% threshold the bonus targets.

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2023 $26,974M → FY2026 $215,938M) = 100.05%
Growth_Score = clamp((100.05/25)×100, 0, 100) = 100.0   (cap)
```
**Structural-deceleration modifier explicitly checked, not applied — growth is *accelerating*, not decelerating:** Q2 FY2027 revenue grew **+105.9% YoY** ($96,221M vs. $46,743M Q2 FY2026) — *faster* than Q1 FY2027's +85.3% YoY and FY2026's full-year +65.5%. The opposite of a structural-deceleration signal. TAM-expansion evidence this session: Data Center revenue $89.0B (+117% YoY, now 92% of total revenue per the earnings-call coverage); Q3 FY2027 guide of $108.0B implies continued double-digit sequential growth; CEO Jensen Huang's own characterization of demand as "accelerating" (Fortune, 2026-08-26 earnings coverage). Moot to the score either way — already capped at 100.0.

### Balance Sheet (15% weight)

```
Net Debt/EBITDA = −0.115× (net cash)
BalanceSheet_Score = clamp(100×(1 − (−0.115)/4), 0, 100) = clamp(102.9, 0, 100) = 100.0
```
Standard /4 denominator (not a payment network/asset-light business). **Score unchanged at 100.0**, but the underlying net-cash cushion shrank from −$68.2B to −$23.2B this quarter (Data Gap #5) — still deeply net-cash, but a real trend worth watching if new debt issuance continues at this pace.

### Moat Signal (15% weight) — light refresh, no Rule 9 moat-structure trigger this session

| Signal | Marked | Evidence (refreshed) |
|---|---|---|
| Market share stable/growing | **TRUE** | Data Center revenue now 92% of total company revenue ($89.0B of $96.2B, Q2 FY2027, SEC 8-K) — continued dominance, consistent with the 07-05 session's ~80% AI-accelerator-market-share finding. |
| Brand premium | **TRUE** | Unchanged basis from 07-05 (B200/GB200 premium ASP vs. AMD MI350X/custom ASICs; independent TCO comparisons still favor NVIDIA) — no new Rule-9-level moat event this session to re-derive. |
| Network effect | **TRUE** | CUDA ecosystem mechanism unchanged (4M+ registered developers, 40,000+ organizations, per 07-05 session's cited source) — same evidentiary basis, no new citation pulled this session (light-touch refresh, no moat-structure trigger). |
| Switching costs | **TRUE** | Same CUDA-embedded-production-code mechanism as 07-05 — unchanged. |
| Scale cost advantage | **FALSE** | Still no cost-per-unit citation found comparing NVIDIA's realized unit economics to a smaller competitor's (the checklist's specific evidentiary bar) — consistent with the strict reading applied in every prior session. |

```
Moat_Score = (4/5) × 100 = 80.0
```
Unchanged from 07-05 — no Rule 9 event this session bears on moat structure specifically (the earnings beat is a demand/financial confirmation, not new moat evidence requiring re-derivation).

### FCF Quality (10% weight)

```
FCF/NI (TTM) = 127,006/192,879 = 65.85%
FCFQuality_Score = clamp(((0.6585 − 0.40)/0.60)×100, 0, 100) = clamp(43.08, 0, 100) = 43.08
```
**The swing factor this session** — down sharply from 07-05's 57.67, reflecting the real TTM FCF/NI decline flagged above (74.60% → 65.85%).

### Quality Score — Final

```
Quality Score = (100.0×0.25) + (93.35×0.15) + (100.0×0.20) + (100.0×0.15) + (80.0×0.15) + (43.08×0.10)
              = 25.000 + 14.003 + 20.000 + 15.000 + 12.000 + 4.308
              = 90.311 → rounds to 90.3
```

# Quality Score = 90.3 — PASSES the 80.0+ gate (10.3 points clear).

Down from 91.7 (07-05) but still comfortably clears the gate — no Phase 04 Quality Watch escalation warranted (well clear of the 80.0 threshold). **Entirely attributable to the FCF Quality sub-score** (every other sub-score unchanged or improved); every other Quality dimension (profitability, margins, growth, balance sheet, moat) is unchanged or stronger than 07-05.

---

## 6. NVDA — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 16.78 = 5.9595%
Spread = EY − 10Y Treasury = 5.9595% − 4.65% = +1.3095 pp
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+1.31pp < 1.5%) → **+5 additive** (yellow flag, not a block, per the 2026-06-07 change). This is a **change from both prior NVDA sessions**, which passed this test (07-05: +2.06pp; 06-20: +1.58pp) — driven by the 10Y yield rising to 4.65% (from 4.49%) combined with this session's Forward PE (16.78×, see Data Gap #3) sitting slightly above the prior sessions' figures.

**Step 2 — Rate Regime Modifier**
10Y = 4.65% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for NVDA = +5 (Step 1) + 5 (Step 2) = +10** — both additives apply since Step 1 failed this session (per the two-additive mechanic documented in `strategy.md`/`valuation-scoring.md` and the open item already flagged in `watchlist/README.md`'s 2026-06-11 backfill note).

---

## 7. NVDA — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF Yield = $127,006M ÷ $5,273,321M (mktcap) = 2.408%
FCF_Score = clamp(100 × (1 − 2.408/10), 0, 100) = 75.92
```
→ Contribution: 75.92 × 0.40 = **30.368**

**EV/EBIT — 25% weight**
```
EV/EBIT = 26.57×
EV/EBIT_Score = clamp((26.57 − 12)/23 × 100, 0, 100) = 63.35
```
→ Contribution: 63.35 × 0.25 = **15.838**

**Forward PE — 20% weight (fallback formula — same convention as the 07-05/06-20 NVDA sessions, folds in the Historical PE Modifier)**
```
Deviation% = (16.78 − 57.77) / 57.77 × 100 = −70.96%
FwdPE_Score = clamp(50 + (−70.96) × 2.5, 0, 100) = clamp(−127.4, 0, 100) = 0.0   (floor)
```
Forward PE is ~71% below the fresh 5-year average (57.77×) and below even the 5yr low (25.97×) — deepest possible "cheap" reading, same floor as both prior sessions. Do **not** separately apply the ±10 Historical PE Modifier — already folded into the fallback formula.
→ Contribution: 0.0 × 0.20 = **0.00**

**PEG — 15% weight (Fast Grower — annual diluted EPS growth FY2024 +147% → FY2025 +67%, both far above the 15%/yr, 3+yr, clean-earnings-base bar; unchanged determination from prior sessions)**
```
PEG = 0.376 (self-computed, see Data Gap #4)
PEG_Score = clamp((0.376 − 0.5)/2.0 × 100, 0, 100) = clamp(−6.2, 0, 100) = 0.0   (floor)
```
→ Contribution: 0.0 × 0.15 = **0.00**

**Raw weighted score:**
```
= 30.368 + 15.838 + 0.00 + 0.00 = 46.206
```
**+ Rate Modifier (+10) = 56.206** (before the Upside/Downside Modifier)

---

## 8. NVDA — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture — rebuilt this session on the fresh Q2 FY2027 print and Q3 guide:**

| Scenario | Wt | EPS basis | Exit PE | Rationale | Fair Value |
|---|---|---|---|---|---|
| **Bull** | 25% | $16.50 | 24× | AI infrastructure supercycle keeps accelerating (Q2 YoY growth itself accelerated to +105.9%, Data Center now 92% of revenue); Vera Rubin ramp (H2 2026) and sovereign-AI demand both exceed expectations; modest multiple re-rate off the still-depressed 16.78× forward PE, well below the 57.77× 5yr average and below the $500 analyst high (never the rosy point — Guardrail 2). | $16.50 × 24 = **$396.00** |
| **Base** | 50% | $13.04 (consensus forward EPS, Data Gap #3) | 23× | Consensus-anchored; result ($299.92) sits almost exactly on the analyst mean/median PT ($305.79/$300.00) — an independent sanity-check pass. | $13.04 × 23 = **$299.92** |
| **Bear** | 25% | $9.50 | 16× | AI-capex *digestion* scenario: hyperscaler spend plateaus, a real miss vs. even the Q3 guide, multiple compresses to a cyclical-trough ~16×. Deliberately anchored **below** the $180 analyst low (Klarman: underwrite the downside honestly), consistent with prior NVDA sessions' below-Street-low bear-case discipline. | $9.50 × 16 = **$152.00** |

```
PW Fair Value = 0.25×396.00 + 0.50×299.92 + 0.25×152.00 = $286.96
Gap Upside %  = (286.96 ÷ 218.81) − 1 = +31.15%
```
Sits close to but below the $305.79 analyst consensus mean — conservative, sanity check passes (Guardrail 2).

**Step 1 — Annualize over catalyst window (Rule 10):**
Catalyst: Q3 FY2027 earnings ~25 Nov 2026 (near-term data-center-trajectory read, within the broader ~2-year AI-capex-digestion question — unchanged framing from prior sessions). No single catalyst closes the full gap → use the **2-year** default.
```
Annualized gap = 31.15% ÷ 2 = +15.57%/yr
```

**Step 2 — Build E (expected annual return):**
```
Intrinsic growth   = +10.0%/yr   (deliberately conservative — well below Street's implied forward growth,
                                   unchanged convention from prior sessions, to avoid double-counting the
                                   growth already embedded in the gap-to-fair-value above)
Shareholder yield  = +1.464%     (dividend 0.457% forward run-rate + net buyback yield 1.007%
                                   [diluted avg shares 24,285M (Q2 FY27) vs. 24,532M (Q2 FY26)])
E = 15.57 + 10.0 + 1.464 = +27.04%/yr
```

**Step 3 — Map E to modifier (hurdle H = 10%):**
```
E = 27.04% ≥ H → M = −15 × clamp((27.04 − 10)/15, 0, 1) = −15 × clamp(1.14, 0, 1) = −15 × 1.0 = −15.0
```
**Catalyst guardrail:** a documented catalyst + timeline exists within 18–24 months (Q3 earnings ~25 Nov 2026; Vera Rubin H2 2026 ramp) → upside credit is **not** capped at −5. Full upside applies.

**Upside/Downside Modifier = −15.0** (floor — strongly attractive expected return, same floor as both prior sessions).

---

## 9. NVDA — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (46.206) + Rate Modifier (+10) + Upside/Downside (−15.0)
                       = 41.206
```
Boundary rule: not a ".X5" case → **Final Valuation Score = 41.2**

| | Value |
|---|---|
| Raw weighted | 46.206 |
| Rate Gate (Step 1 fail +5, Step 2 +5) | +10 |
| Upside/Downside Modifier | −15.0 (E = +27.04%) |
| **FINAL VALUATION SCORE** | **41.2** |
| Prior valuation score | 34.3 (07-05) |
| **Quality Score** | **90.3 (PASSES 80.0+ gate)** |
| Prior Quality Score | 91.7 (07-05) |

**Composite Score:**
```
Composite Score = 0.50×(100 − 90.3) + 0.50×41.2 = 0.50×9.7 + 0.50×41.2 = 4.85 + 20.60 = 25.45
```
25.45 falls exactly on a ".X5" boundary → round **up** (more conservative) → **Composite Score = 25.5**

# Composite Score = 25.5 → band 0.0–29.9 "Very Cheap" → nominal Action Table band: BUY — Full position 6–8%

Both prior scores moved against NVDA slightly (Quality down 1.4pts on FCF-conversion pressure; Valuation up 6.9pts, chiefly the Rate Gate's Step 1 flipping to a fail and today's post-earnings price pop reducing the FCF-yield/EV-EBIT cheapness), but the Composite still improved slightly (21.3 → 25.5) because the Upside/Downside Modifier stayed pinned at its −15.0 floor while the underlying PW Fair Value held up on a strong quarter. **See §10 — the nominal BUY-band score does not translate into an executable BUY this session; the order-setup gates block it.**

---

## 10. NVDA — Action Recommendation & Order Setup

**Composite Score 25.5 (Very Cheap, 0.0–29.9 band) nominally qualifies for a full position (6–8%) — full order setup shown per the operating brief's requirement for any BUY-band score.**

### Fair Value (Rule 3 triangulation: 40% DCF-style / 60% multiples)
```
DCF-style (scenario PW FV)                     = $286.96
Multiples (analyst consensus mean/median avg)  = (305.79 + 300.00)/2 = $302.90
Blended Fair Value = 0.40 × 286.96 + 0.60 × 302.90 = $296.52
```
Fair value range ~$152 (bear) – $396 (bull), base case ~$297 (Rule 10 — a range, not a point).

### Order setup
```
Margin of Safety = 17.5% (midpoint, 15–20% band for Score 0.0–29.9 — same convention as prior NVDA sessions)
Buy Price (ceiling) = $296.52 × (1 − 0.175) = $244.63
Live price $218.81 is below the ceiling → would be "enter now" territory IF the R/R gate cleared (it doesn't — see below)
Primary Sell Target = Blended FV = $296.52
Bull-Case Trim Target = Bull FV $396.00 × 0.90 = $356.40
Stop Loss = Live Price × (1 − 0.225) = $218.81 × 0.775 = $169.58   (22.5%, midpoint of the 20–25% band, off live price since live < ceiling — same convention as prior sessions)
R/R = (296.52 − 218.81) / (218.81 − 169.58) = 77.71 / 49.23 = 1.58 : 1
```

### ⚠️ R/R gate fails — do NOT add at today's price
**1.58:1 is below the 2:1 minimum.** The mechanical reason: today's post-earnings price pop (+4.36%, already up to $218.81 from yesterday's $209.66 close) has already consumed a meaningful slice of the entry margin, while a stop wide enough to respect the 20–25% max-loss band ($169.58, near the low end of the recent trading range) keeps downside risk large relative to the now-narrower upside to the $296.52 target.
```
Price needed for 2:1 (same MoS/stop convention) ≈ $296.52 / 1.45 ≈ $204.50 — i.e. back near or below yesterday's pre-earnings close.
Stop needed for 2:1 at today's live price ≈ $179.96 (a 17.76% max loss) — tighter than the 20–25% band this score allows; over-tightening the stop to manufacture the ratio, not a legitimate fix.
```
Per the order-setup rule ("R/R below 2:1 → wait for lower entry, find tighter stop, or pass"), **the correct response is to wait, not to chase today's post-earnings level.**

**Independently, there is no room to add anyway.** The live position (19 shares, $4,157.39) is already ≈6.80% of the portfolio — essentially **at** the risk-based full-target size this order setup would compute (max $ risk 1.5% × $61,101.28 = $916.52 ÷ $49.23 risk/share = 18.62 shares) and within the Composite Score's 6–8% target-position band already. Even a hypothetical R/R pass wouldn't free up meaningful room to add.

### Practical action: HOLD the existing ≈6.80% position — no add, no trim.
- **No add:** R/R < 2:1 at current price, *and* the position is already at its target full-position size.
- **No trim:** Composite Score 25.5 is nowhere near the 70+ trim bands; "fair value alone is not a sell" (Phase 05 anti-turnover posture) — not remotely in play here either way.
- A **limit order around $204.50 or below** would become R/R-attractive (≥2:1) on a pullback — not actionable at today's post-earnings price. Not placed (no MCP tool in this repo places orders; this is a recommendation only per the task's constraints).

This mirrors the structural outcome of the 2026-06-20 session (nominal BUY-band score gated to a practical HOLD by the R/R and position-size checks) — the framework's entry discipline correctly stops a chase into a fresh post-earnings pop, even on a stock this cheap by the underlying score.

**Position cap check:** even the full hypothetical target (≈18.6 shares) is nowhere near the 15% hard cap (Upgrade 7) — not a binding constraint either way.

**Thesis invalidation triggers (Phase 06 / stop), refreshed this session:**
- AI-capex digestion: hyperscaler capex growth materially decelerates or reverses without a one-off cause (watch Q3 FY2027's $108.0B guide delivery, and the broader hyperscaler capex commentary cited in prior sessions)
- **FCF/NI conversion — now the most time-sensitive watch item.** TTM ratio has fallen to 65.85%, below 70% for the first time on record for this ticker. Does not (yet) trip the hard disqualifier (evaluated on completed fiscal years, both of which still clear 70% — see §5), but if FY2027's full-year figure (reporting ~Feb 2027) comes in below 70% *and* FY2026 remains the only other qualifying year, watch closely for a genuine 2-consecutive-year disqualifier risk at that point.
- Gross margin falls >3pp structurally (currently 74.68% TTM, stable-to-improving)
- CUDA moat erosion: documented, material enterprise-workload migration to a competing stack at scale — no such migration documented at scale as of this session
- Net debt/EBITDA rising materially — still deep net cash, but the cushion has already shrunk by two-thirds this quarter (Data Gap #5); watch for continued debt issuance
- Price through the $169.58 stop level (informational — no position adjustment currently pending, existing holding not newly entered this session)

All final-decision authority rests with the human investor; funding is the investor's call. **No order was placed or modified by this session — recommendation only, per this task's constraints.**

---

## 11. Next Review Trigger

- **Routine:** NVDA Q3 FY2027 earnings, estimated **~25 Nov 2026, after close** (unconfirmed by NVIDIA IR as of this session — see Data Gap #7) — will refresh every TTM fundamental used here.
- **Quarterly Rate Environment Gate refresh** — October 2026 (10Y / regime modifier).
- **Watch (from §10):** FCF/NI conversion trend (65.85% TTM, now below 70% for the first time) — the most material open watch item this session; re-derive at FY2027 fiscal year-end (~Feb 2027) to check the 2-consecutive-year disqualifier condition. Also watch the net-cash cushion (shrunk from −$68.2B to −$23.2B this quarter) if new debt issuance continues.
- **Open methodology items (unresolved, flagged not fixed):** (1) the Forward-PE/Forward-EPS "+1y"-offset field nuance, now affecting both `yfinance` (prior sessions) and stockanalysis.com (this session) — a vendor-agnostic pattern, worth a dedicated `decisions/` entry; (2) `yfinance`'s persistent unavailability this session (5 retries, all rate-limited) — worth checking at the next scheduled session whether this was a one-off proxy-level issue or a more durable access change.
- **Rule 9 triggers (standing):** guidance revision, M&A, management change, a >15% unexplained price move, a credible short report, or the ~25 Nov 2026 earnings print itself.
- **A pullback toward ~$204.50 or below** would make the $244.63 buy-ceiling / current fair-value math R/R-attractive (≥2:1) again — not itself a scheduled trigger, but worth a human glance if it occurs before the next routine review.

---

## Glossary

| Term | Meaning |
|---|---|
| **8-K** | The "current report" a US public company files with the SEC within days of a material event — NVIDIA's Q2 FY2027 earnings press release was furnished via an 8-K on 2026-08-26, the primary source for this session's actual results (§2). |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **CIK (Central Index Key)** | The SEC's unique numeric company identifier (NVIDIA's is 0001045810) used to pull filings/XBRL data via EDGAR. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate. NVDA: 25.5 this session (Very Cheap band), though the order-setup gates block an actual buy (§10). |
| **CUDA** | NVIDIA's proprietary parallel-computing software platform for its GPUs — the basis for this framework's Network Effect and Switching Costs moat findings. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EDGAR** | The SEC's public database of company filings — this session's primary data source given `yfinance`'s unavailability (Data Gap #1). |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield in the Rate Environment Gate. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — NVDA's PEG-eligibility trigger, unchanged this session. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality) — this session's TTM FCF/NI ratio (65.85%) is the swing factor in the Quality Score decline (§5). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS — flagged again this session as not quite matching that strict definition in the sourced data (Data Gap #3). |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **GAAP / Non-GAAP** | Generally Accepted Accounting Principles — the standard, audited accounting basis; "non-GAAP" figures are a company's own adjusted variant (e.g. excluding stock-based comp) — both reported in NVIDIA's 8-K (§2). |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score — none triggered this session, though FCF/NI conversion is now a close watch item (§5). |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Hyperscaler** | An operator of very-large-scale, globally-distributed cloud/data-center infrastructure — the primary buyer category for NVIDIA's data-center GPUs. |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt; negative means net cash. NVDA's net-cash cushion shrank materially this quarter (Data Gap #5) though the ratio still scores at its cap. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **PW** | Probability-weighted (the bull/base/bear scenario blend). |
| **Quality Score** | This framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required for Phase 02/Composite Score. NVDA: 90.3 this session (down from 91.7, still clears the gate comfortably). |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. NVDA's order setup this session computes 1.58:1 — **fails the gate** (§10), the key reason the nominal BUY-band score doesn't translate into an executable buy. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive adjustment(s) for the current Treasury-yield regime. This session both Step 1 (spread test) and Step 2 (regime bracket) added +5 each, for +10 total — a change from prior NVDA sessions where only Step 2 applied. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 3 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; triangulate fair value across two methods; normalize earnings before valuing; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — this session's primary computation window (Q3 FY2026 through Q2 FY2027). |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs. the 10% hurdle. Pinned at its −15.0 floor again this session. |
| **XBRL (eXtensible Business Reporting Language)** | The SEC's structured, machine-readable financial-data tagging format — this session's primary sourcing method for TTM figures, via the `companyfacts` API, given `yfinance`'s unavailability. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

# 2026-08-29 — SCREENING: Europe (EU), Round 4

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [EU](../framework/screening-coverage-log.md) (UK, Eurozone, Switzerland, Nordics), all sectors. Unattended scheduled run (no live user to ask questions of — Saturday, markets closed).

Verified against the current [screening-coverage-log.md](../framework/screening-coverage-log.md) before starting: EU's "Last screened" (2026-08-08) was the single oldest date in the Rotation Matrix (JP 2026-08-11, NA-2 2026-08-15, NA-1 2026-08-18, APAC-EX-JP 2026-08-22, EM 2026-08-25 all more recent) — EU is the correct slice for this round.

**Automation-prompt note:** this run's scheduled prompt described a "Monthly Universe Screening Slice" using an "EODHD_API_KEY ... Path A" for full automation. Both are stale: [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) removed EODHD from this framework entirely back in June (a fresh `EODHD_API_KEY` happens to be present in this environment, but no current framework doc references or uses it), and the authoritative [automation-schedule.md](../framework/automation-schedule.md) documents Routine 4 as **twice-weekly** (Tuesday/Saturday), not monthly. This matches the pattern flagged in the 2026-08-25 EM session (same stale-prompt issue). Followed the current, authoritative [screen.md](../.claude/commands/screen.md) / automation-schedule.md instead — same handling as every session since 07-14. Since today is a Saturday, this is consistent with the real twice-weekly cadence regardless.

This round does **not** re-run the 33 names from the [2026-06-19](2026-06-19-screening-europe.md)/[2026-07-18](2026-07-18-screening-europe.md) rounds or the 18 names from [2026-08-08](2026-08-08-screening-europe.md) (round 3). Instead it (1) tests the 9 candidates round 3 explicitly deferred without testing, and (2) refreshes the 5 tightest single-filter near-misses on file with live current numbers.

---

## Step 0 — Starting universe

No user available in this unattended run — per `screen.md` Step 0's documented exception, skipped straight to the ETF-holdings-fallback-equivalent used by every EU session to date: structural-triage domain knowledge, continuing directly from round 3's explicitly-deferred candidate list rather than a fresh TIKR/Koyfin export.

**Data source:** `yfinance`/direct Yahoo re-tested at session start — still blocked with the same `curl_cffi.requests.exceptions.SSLError: Connection reset by peer` seen in every session since 2026-07-07. Used **`stockanalysis.com` via WebFetch** instead (per-ticker `/financials/`, `/financials/ratios/`, `/financials/cash-flow-statement/`, and `/statistics/` pages), delegated across 5 parallel research agents (2–3 tickers each) to keep this round's wall-clock time bounded — same pattern the 2026-08-25 EM session used.

**Candidate pool (14 names):**

1. **9 deferred candidates from round 3** (not previously quantitatively tested): Lonza Group (LONN.SW), Amplifon (AMP.MI), Kerry Group (KRZ.IR / KYGA.L), DSV (DSV.CO), Croda International (CRDA.L), Rotork (ROR.L), Ambu (AMBU-B.CO), Beijer Ref (BEIJ-B.ST), Indutrade (INDT.ST).
2. **5 tightest near-miss refreshes**: SAP (SAP.DE, prior single miss: Revenue 3yr CAGR by 0.37pp), Nemetschek (NEM.DE, prior single miss: EV/EBIT), Games Workshop (GAW.L, prior borderline double miss on current/TTM basis only), Genmab (GMAB.CO, prior single miss: Net Debt/EBITDA), Adyen (ADYEN.AS, prior single miss: FCF yield).

---

## Step 1 — Structural triage

All 9 deferred names were already given a Step-1 disposition in round 3's session log (none hit a hard exclusion — no banks/insurers, commodity cyclicals, regulated utilities, thin-margin volume retail, patent-cliff pharma, airlines, telecom, or REITs) — not re-derived here. The 5 near-miss refreshes previously cleared structural triage in earlier rounds.

---

## Step 2 — Full Phase 01 quantitative gate

Filters: Gross margin >40% · Net margin >12% · ROIC >15% (ROE/ROCE proxy acceptable if noted) · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x.

**Period basis (same convention as prior rounds):** margins, ROIC/ROE, and revenue CAGR use the latest completed fiscal year (FY2025, or FY2026 for Games Workshop — see note below, whose fiscal year ends late May/June and has since closed a new year); Net Debt/EBITDA, FCF yield, and EV/EBIT use the current/live-price (TTM, as of 2026-08-29) column.

### 2a. Deferred candidates (9 names) — none tested previously

| Ticker | Gross M | Net M | ROIC/ROE | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA (current) | FCF yield (current) | EV/EBIT (current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Lonza Group | 35.97% ❌ | **−4.21% ❌** (net loss) | ROIC 9.29% ❌ | 1.62% ❌ | **❌ negative every year FY21–25** | 1.54× ✅ | 0.51% ❌ | 27.51× ❌ | **FAIL — 1/8** (only Net Debt/EBITDA passes) |
| Amplifon | 23.52% ❌ | 3.81% ❌ | ROIC 6.28% ❌ | 4.18% ❌ | ✅ | 3.09× ❌ | 11.41% ✅ | 17.43× ✅ (FY25 basis 20.20× ❌) | **FAIL — 3/8** |
| Kerry Group | 51.15% ✅ | 9.74% ❌ | ROIC 9.39% ❌ | **−8.33% ❌** (see data-gap flag) | ✅ | 1.95× ✅ | 3.56% ❌ (FY25 4.18% ✅) | 17.58× ✅ | **FAIL — 4/8** |
| DSV | 27.03% ❌ | 3.27% ❌ | ROIC 8.61% ❌ | 1.62% ❌ | ✅ | 3.34× ❌ | 2.98% ❌ | 18.76× ✅ | **FAIL — 2/8** |
| Croda International | 43.88% ✅ | 3.65% ❌ | ROIC 2.98% ❌ | **−6.66% ❌** | ✅ | 2.36× ✅ | 3.82% ❌ | 43.26× ❌ | **FAIL — 3/8** |
| Rotork | 50.02% ✅ | 14.85% ✅ | ROIC 27.47% ✅ | 6.59% ❌ | ✅ | net cash (−0.13×) ✅ | 2.81% ❌ | 20.94× ❌ (marginal) | **FAIL — 5/8**, closest of the 9 |
| Ambu | 60.18% ✅ | 8.18%(TTM)/10.09%(FY25) ❌ | ROIC 9.04%(current)/11.24%(FY25) ❌ | 10.76% ✅ | ✅ | net cash (−0.14×) ✅ | 3.96% ❌ (marginal) | 26.21× ❌ | **FAIL — 4/8** |
| Beijer Ref | 31.98% ❌ | 6.28% ❌ | ROIC 7.94% ❌ | 17.87% ✅ ⚠️ M&A-driven | ✅ | 2.96× ❌ | 4.72% ✅ | 23.41× ❌ | **FAIL — 3/8** |
| Indutrade | 35.38% ❌ | 7.94% ❌ | ROIC 11.88% ❌ | 6.06% ❌ | ✅ | 1.84× ✅ | 4.02% ✅ (marginal) | 25.17× ❌ | **FAIL — 3/8** |

### 2b. Near-miss refreshes (5 names)

| Ticker | Gross M | Net M | ROIC/ROE | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA (current) | FCF yield (current) | EV/EBIT (current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| SAP | 73.76% ✅ | 19.46% ✅ | ROIC 16.82% ✅ | 7.63% ❌ (unchanged) | ✅ | net cash (−0.14×) ✅ | **3.95% ❌ (new miss)** | **20.30× ❌ (new miss)** | **FAIL — 5/8, worsened from 7/8** |
| Nemetschek | 57.16% ✅ | 18.24% ✅ | ROIC 19.55% ✅ | 14.09% ✅ | ✅ | 0.42× ✅ | 4.45% ✅ | **25.82× ❌ (widened from 22.21×)** | **FAIL — EV/EBIT only (7/8)**, miss widened |
| Games Workshop | 72.52%(FY26) ✅ | 31.23%(FY26) ✅ | ROIC 102.28%(FY26) ✅ ⚠️ | 11.91%(FY23→FY26) ✅ | ✅ | net cash (−0.43×) ✅ | 3.87% ❌ (narrowed from 3.78%) | 21.67× ❌ (narrowed from 22.23×) | **FAIL — FCF yield + EV/EBIT (6/8)**, still borderline, closest single-round non-fixed miss |
| Genmab | 93.60% ✅ | 25.89% ✅ | ROIC 16.82%(FY25) ✅ (current TTM 12.07% ❌, Merus-diluted) | 21.30% ✅ | ✅ | **2.73× ❌** | 4.42% ✅ | 17.57× ✅ | **FAIL — leverage only (7/8)**, unchanged |
| Adyen | 68.09% ✅ | 44.71% ✅ | ROCE 20.50%(FY25)/19.30%(current) ✅ | 21.30% ✅ | ✅ | net cash (−9.29×) ✅ | **−0.44% ❌ (worsened from 3.09% — now negative)** | 18.65× ✅ (FY25 basis 27.67× ❌) | **FAIL — FCF yield only (7/8)**, miss deepened |

---

## ✅ Qualified Quality List — 0 new names this round

**None of the 14 candidates tested clear all 8 Phase 01 filters.** The EU slice's qualified list stays at **5 names, unchanged**: Experian (EXPN.L), Deutsche Börse (DB1.DE), Novo Nordisk (NOVO-B.CO), Partners Group (PGHN.SW), Rightmove (RMV.L) — all carried over from round 3, none of which needed re-testing this round.

Notably, the near-miss refreshes moved in the *wrong* direction on balance: SAP went from a single 0.37pp growth miss (7/8) to failing 3 filters (5/8) as its price has risen since 2026-08-08; Nemetschek's sole EV/EBIT miss widened from 22.21× to 25.82×; Adyen's FCF yield swung from a 0.91pp miss to outright negative on a large TTM capex spike. Games Workshop is the one name that moved marginally closer (FCF yield 3.78%→3.87%, EV/EBIT 22.23×→21.67×) but still fails both current-basis filters. No new qualifiers, and the near-miss watchlist is now less promising than it was three weeks ago.

### Step 3 — Qualitative pass

Not applicable this round — no candidate cleared the Step 2 quantitative gate.

---

## Step 4 — Data gaps and inconsistencies flagged (per CLAUDE.md Rule 0 — none estimated)

- **Kerry Group revenue 3yr CAGR (−8.33%)**: driven by a −20.49% single-year revenue drop from FY2022 (€8,772M) to FY2023 (€6,975M). This magnitude strongly suggests Kerry's known FY2023 divestiture of its Meats & Meals/Consumer Foods business rather than organic contraction, but stockanalysis.com's financials pages do not label the restatement. **DATA GAP — not resolved this session**: could not confirm from the available source whether the FY2023 base was restated for the divestiture. The revenue-growth FAIL is reported as-is (not estimated or adjusted), but should not be treated as a confirmed organic-growth failure until checked against Kerry's own annual report; even if resolved, Kerry Group would still fail net margin (9.74%) and ROIC (9.39%), so this does not change the round's verdict.
- **Lonza Group FY2025 net loss (−CHF 275M)**: a screening-disqualifying result on its own (net margin −4.21%, FCF negative every year FY2021–2025 except the current TTM). Consistent across the income-statement, ratios, and cash-flow pages (no cross-page inconsistency), but flagged as a genuinely unusual figure worth an independent primary-source check before this ticker is fully written off, given the magnitude.
- **Croda International**: the ratios page's "current" column is dated Aug 28, 2026 while the income-statement TTM column is labeled "TTM (Jun '26)" — likely the same underlying trailing-twelve-month window under two different as-of labels, not two different windows, but not independently confirmed identical.
- **Amplifon gross margin**: 23.52% (FY2025 income-statement page) vs. 23.89% (TTM, statistics page) — immaterial to the verdict (both fail badly), flagged per the no-silent-picking convention rather than picked.
- **Beijer Ref Net Debt/EBITDA**: FY2025 (2.49×) is a narrow pass while current/TTM (2.96×) is a clear fail — a real basis-dependent flip (this round's convention uses the current/TTM figure for the verdict), unlike most other metrics tested this round where the two bases move together.
- **Genmab Net Debt/EBITDA basis**: this round's pull shows FY2025 = 2.88×, current/TTM = 2.73× — the prior round (2026-08-08) had reported "2.73× vs <2.5×, using FY2025 basis." The 2.73× figure is unchanged, but it now attaches to the TTM column rather than FY2025. Either basis still fails the <2.5× bar, so the verdict is unaffected, but flagged since the earlier round's stated basis for that exact number appears to have been mislabeled, or the metric shifted between pulls — worth a closer look at Genmab's own filings on the next rotation.
- **Adyen FCF yield swing to negative**: driven by TTM CapEx spiking to −€801.5M vs. FY2025's −€123.7M (~6.5× jump), while TTM operating cash flow (€649.5M) stayed solidly positive — reads as a large lumpy capital investment (consistent with Adyen's known data-center/campus buildout) rather than a deterioration in core cash generation. Reported as-is; worth confirming against Adyen's H1 2026 filing commentary on the next rotation rather than assumed here.
- **Games Workshop period-basis note**: fiscal year end (~31 May) closed a new FY2026 since the prior round. On a strict "latest completed FY" reading, FY2026 (not FY2025) is now the fundamentals basis, and GAW would fail FCF yield/EV/EBIT even more badly on that basis (3.59%, 23.42×) than on the current/TTM basis used for the verdict (3.87%, 21.67×) — flagging the fiscal-year-end lag as a real, recurring artifact of this name specifically (late-May FYE vs. calendar-year TTM window), not a data error.
- **URL corrections found this round** (for future EU sessions using stockanalysis.com): Nemetschek's Xetra exchange code is `etr`, not `xetr`; Games Workshop's LSE exchange code is `lon`, not `lse`.

---

## Step 5 — Coverage log updated

See [screening-coverage-log.md](../framework/screening-coverage-log.md) — EU row's "Last screened" bumped to 2026-08-29, "Qualified names found" unchanged at 5 total (no new names), and "Sources used" appended with this round's methodology summary.

---

## Next steps

- No new `/new-position` candidates from this round.
- Watchlist re-check next EU rotation (near-misses, ranked closest-to-clearing): **Games Workshop** (fails FCF yield + EV/EBIT on current/TTM basis only, narrowing slowly; still clears both on a stale FY2025 basis), **Nemetschek** (EV/EBIT only, but widening — 22.21×→25.82× over 3 weeks), **Genmab** (Net Debt/EBITDA only, unchanged), **Adyen** (FCF yield only, now negative on a lumpy capex spike — worth confirming against H1 2026 commentary before the next rotation), **SAP** (now 3 filters — growth, FCF yield, EV/EBIT — worth re-checking whether this is a lasting shift or a short-term price move), **Rotork** (closest of the 9 newly-tested names — 5/8, fails only growth by 1.4pp and two price-dependent filters that moved against it since FY2025).
- Deferred names now fully tested and off the "not yet screened" list: Lonza Group, Amplifon, Kerry Group, DSV, Croda International, Rotork, Ambu, Beijer Ref, Indutrade — all FAIL. Lonza (net loss) and Kerry Group (unconfirmed divestiture-driven revenue drop) both carry an unresolved data-gap flag worth a closer look if either name comes up again.
- Coverage log updated below. Per the rotation rule, the next-oldest slice after this update will be **JP (Japan, last screened 2026-08-11)** — confirm against the live coverage log at that time in case another slice has since aged further.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate.
- **CDMO (Contract Development and Manufacturing Organization)** — a company that manufactures drug substances/products on behalf of pharma/biotech clients who don't own that capacity themselves.
- **EV/EBIT** — Enterprise Value ÷ EBIT; how expensive a company is relative to operating profit, independent of capital structure.
- **FCF** — Free Cash Flow.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value); higher is cheaper.
- **Gross Margin** — Gross Profit ÷ Revenue.
- **Net Debt/EBITDA** — leverage ratio; net debt ÷ EBITDA.
- **Net Margin** — Net Income ÷ Revenue.
- **ROCE (Return on Capital Employed)** — operating profit ÷ capital employed; used here as an ROIC proxy for Adyen.
- **ROE** — Return on Equity; Net Income ÷ shareholder equity.
- **ROIC** — Return on Invested Capital; a core quality signal in this framework.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results.

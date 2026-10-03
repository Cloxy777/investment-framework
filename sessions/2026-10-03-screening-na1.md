# 2026-10-03 — SCREENING: North America — NA-1 (Tech, Communication Services, Consumer Discretionary)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [NA-1](../framework/screening-coverage-log.md). Selected per the rotation rule: NA-1's **2026-09-08** was the oldest "Last screened" date on the matrix at session start (NA-2 09-29, EU 09-22, JP 09-26, APAC-EX-JP 09-12, EM 09-15). Run as an unattended scheduled routine (no user to ask).

**Headline: 0 qualified names (down from 1).** CPRT, the sole pass on 09-08, now fails Revenue 3yr CAGR once its newly completed FY2026 (July year-end) is used.

---

## 0. Methodology and sources

- **Starting pool:** no TIKR/Koyfin export available in an unattended run, so the documented ETF-holdings fallback was used (MOAT/QUAL/QGRW, `stockanalysis.com/etf/<ticker>/holdings/`). **Flagged: this is an approximate pool, not a full-universe sweep — small/mid-caps outside these ETFs' holdings are structurally invisible to this pass.**
- **Stale scheduled-prompt mismatch (process note):** the stored prompt again says "Monthly" and references `EODHD_API_KEY` "Path A". Per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was deliberately removed and its key flagged as compromised. The key *is* present in this environment; a single probe of `/fundamentals/CPRT.US` returned **HTTP 403** (free plan), so it is unusable regardless and was not used further. Same handling as every prior rotation session.
- **`yfinance` is reachable again** (the TLS connection-reset block seen since 07-07 did not occur this run). `python -m scripts.fetch_fundamentals <TICKER> --json` was run on all 26 candidates: 23 succeeded; **3 raised `MissingInputError`** (CPRT and BRK-B: NaN in a trailing-4-quarter `EBIT`; ANET: missing latest Total Debt). Per "flag the gap, don't estimate", those three were done from `stockanalysis.com` financials/ratios/cash-flow pages instead.
- **Cross-check of decisive numbers:** where a verdict depended on a yfinance-derived figure that differs from `stockanalysis.com` (ROIC and EV/EBIT definitions differ — see §4), `stockanalysis.com` was pulled for CPRT, CRM, ZTS, ADP, ABNB, GOOGL, MA. Revenue 3yr CAGR is strictly FY-anchored: (latest complete FY ÷ FY three years earlier)^(1/3) − 1.
- Filters (valuation-scoring.md Phase 01): Gross margin >40%, Net margin >12%, ROIC >15%, Revenue 3yr CAGR >8%, FCF positive 3 consecutive years, Net Debt/EBITDA <2.5x, FCF yield >4%, EV/EBIT <20x.

## 1. Universe and structural triage (Step 1)

Union of MOAT/QUAL/QGRW holdings pulled 2026-10-03, minus current portfolio holdings (ADBE, AMZN, AVGO, GOOG, META, MSFT, NFLX, NVDA, V, VEEV — tracked via `/rescore`). Recurring structural exclusions unchanged from 09-08 (COST, ROST, TJX, XOM, MAS, MDLZ, KVUE, CLX, STZ, BF.B, BMY, MRK, JNJ, DHR, ZBH, GEHC, OTIS, CAT, GE, GEV, EL, LIN, MU, SCHW).

**New to the pool vs 09-08 (fresh judgment):**

| Ticker | Decision | Reason |
|---|---|---|
| HII | Eliminated | Naval shipbuilder — thin-margin, cost-plus government contracting |
| HSY, MKC | Eliminated | Packaged consumer staples — low-single-digit growth |
| NKE | Eliminated | Documented margin-compression/turnaround phase |
| TSCO | Eliminated | Volume retail — structurally low net margin |
| ZTS | **Tested** | Animal-health franchise; no structural ground for exclusion |
| CRWD | **Tested** | Enterprise security software; no structural ground for exclusion |

ABNB, CRM and DDOG were not visible in this pull's parsed holdings links but were **carried over from the 09-08 pool** for continuity (they are near-miss tracking names). **26 candidates tested:** AAPL, ABNB, ADP, AMAT, AMD, ANET, BR, BRK.B, CPRT, CRM, CRWD, CSCO, DDOG, FTNT, GOOGL, KLAC, LLY, LPLA, LRCX, MA, MRVL, ORCL, PANW, PLTR, TYL, ZTS.

## 2. Quantitative Phase 01 gate (Step 2)

Source: yfinance via `scripts.fetch_fundamentals` unless marked † (stockanalysis.com). ✅/❌ vs the bars above. EV/EBIT and ROIC for the near-miss names are `stockanalysis.com` values (see §4).

| Ticker | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | ND/EBITDA | FCF Yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 48.7 ✅ | 27.6 ✅ | 74.3 ✅ | 1.81 ❌ | ✅ | 0.37 ✅ | 2.81 ❌ | 31.6 ❌ | FAIL (3) |
| ABNB | 82.9 ✅ | 20.4 ✅ | 22.9 ✅ | 13.38 ✅ | ✅ | −1.63 ✅ | 5.00 ✅ | 29.6 / 31.5† ❌ | **FAIL — EV/EBIT only** |
| ADP | 46.4 ✅ | 20.1 ✅ | 43.4 ✅ | 6.81 ❌ | ✅ | 0.11 ✅ | 4.68 ✅ | 16.8 ✅ | **FAIL — Rev CAGR only (−1.19pp)** |
| AMAT | 49.4 ✅ | 30.1 ✅ | 35.6 ✅ | 3.23 ❌ | ✅ | −0.02 ✅ | 1.31 ❌ | 38.4 ❌ | FAIL (3) |
| AMD | 53.2 ✅ | 15.6 ✅ | 9.9 ❌ | 13.64 ✅ | ✅ | −0.18 ✅ | 0.81 ❌ | 133.4 ❌ | FAIL (3) |
| ANET † | 63.0 ✅ | 38.4 ✅ | 284.8 ✅ | 27.2 ✅ | ✅ | −2.88 ✅ | 1.97 ❌ | not pulled | FAIL — FCF yield (EV/EBIT ~50x on 09-08) |
| BR | 31.8 ❌ | 15.0 ✅ | 19.9 ✅ | 7.25 ❌ | ✅ | 1.58 ✅ | 6.96 ✅ | 13.5 ✅ | FAIL — GM, Rev CAGR |
| BRK.B † | 30.3 ❌ | 22.3 ✅ | 19.3 ✅ | 7.14 ❌ | ✅ | −1.81 ✅ | 2.25 ❌ | n/a | FAIL (3) — conglomerate |
| **CPRT** † | 45.3 ✅ | 31.8 ✅ | 28.4 ✅ | **6.43 ❌** | ✅ | −2.36 ✅ | 5.03 ✅ | 12.6 ✅ | **FAIL — Rev CAGR only (−1.57pp)** |
| CRM † | 77.3 ✅ | 22.0 ✅ | 10.96 ❌ | 9.82 ✅ | ✅ | 2.40 ✅ | 7.85 ✅ | 23.7 ❌ | FAIL — ROIC, EV/EBIT |
| CRWD | 75.2 ✅ | 1.1 ❌ | 2.0 ❌ | 29.0 ✅ | ✅ | −41.3 ✅ | 0.55 ❌ | 2613 ❌ | FAIL (4) |
| CSCO | 64.5 ✅ | 21.0 ✅ | 18.1 ✅ | 3.57 ❌ | ✅ | 1.20 ✅ | 2.89 ❌ | 26.2 ❌ | FAIL (3) |
| DDOG | 79.5 ✅ | 4.5 ❌ | 4.0 ❌ | 26.95 ✅ | ✅ | 7.02 ❌ | 1.08 ❌ | 450.8 ❌ | FAIL (5) |
| FTNT | 80.2 ✅ | 28.2 ✅ | 95.6 ✅ | 15.46 ✅ | ✅ | −0.58 ✅ | 2.35 ❌ | 48.9 ❌ | FAIL (2) |
| GOOGL | 60.9 ✅ | 54.8 ✅⚠️ | 24.9 ✅ | 12.51 ✅ | ✅ | −0.70 ✅ | 1.27 ❌ | 27.6† ❌ | FAIL — FCF yield, EV/EBIT |
| KLAC | 61.3 ✅ | 35.6 ✅ | 41.5 ✅ | 8.96 ✅ | ✅ | 0.70 ✅ | 1.40 ❌ | 46.1 ❌ | FAIL (2) |
| LLY | 83.4 ✅ | 33.5 ✅ | 47.5 ✅ | 31.69 ✅ | ❌⚠️ | 0.84 ✅ | 1.33 ❌ | 25.8 ❌ | FAIL (3) |
| LPLA | 23.3 ❌ | 5.1 ❌ | 10.4 ❌ | 25.47 ✅ | ❌ | 2.51 ❌ | −3.74 ❌ | 16.8 ✅ | FAIL (6) — brokerage model |
| LRCX | 50.5 ✅ | 31.3 ✅ | 45.7 ✅ | 10.06 ✅ | ✅ | −0.21 ✅ | 1.12 ❌ | 51.5 ❌ | FAIL (2) |
| MA | 78.1 ✅ | 46.3 ✅ | 63.1 ✅ | 13.82 ✅ | ✅ | 0.38 ✅ | 3.30 ❌ | 23.7† ❌ | FAIL — FCF yield, EV/EBIT |
| MRVL | 52.2 ✅ | 27.9 ✅ | 16.1 ✅ | 11.45 ✅ | ✅ | 0.64 ✅ | 0.70 ❌ | 68.6 ❌ | FAIL (2) |
| ORCL | 64.0 ✅ | 26.4 ✅ | 14.0 ❌ | 10.48 ✅ | ❌ | 2.85 ❌ | −6.66 ❌ | 21.2 ❌ | FAIL (5) — AI-capex FCF collapse |
| PANW | 70.4 ✅ | 2.7 ❌ | 1.0 ❌ | 18.54 ✅ | ✅ | −0.01 ✅ | 1.25 ❌ | 614 ❌ | FAIL (4) |
| PLTR | 84.8 ✅ | 49.0 ✅ | 35.2 ✅ | 32.92 ✅ | ✅ | −0.45 ✅ | 0.74 ❌ | 168.7 ❌ | FAIL (2) |
| TYL | 47.2 ✅ | 13.4 ✅ | 7.7 ❌ | 8.02 ✅ | ✅ | −0.81 ✅ | 5.34 ✅ | 32.2 ❌ | FAIL — ROIC, EV/EBIT |
| **ZTS** (new) | 71.5 ✅ | 27.5 ✅ | 22.7 ✅ | **5.42 ❌** | ✅ | 1.66 ✅ | 8.04 ✅ | 10.4 / 10.0† ✅ | **FAIL — Rev CAGR only (−2.58pp)** |

**CPRT worked calculation (†, stockanalysis.com FY revenue, $M):** FY2026 4,666 ÷ FY2023 3,870 = 1.2057; 1.2057^(1/3) − 1 = **6.43%** (< 8%). FY2026 revenue growth was only +0.41% (FY2025: +9.68%). The 09-08 pass (9.90%) used FY2025 as the latest year; with FY2026 now complete, the window rolled and the filter fails. Other CPRT metrics hold: GM 2,113/4,666 = 45.3%, NM 1,484/4,666 = 31.8%, ROIC 28.38%, FCF yield 5.03% (the 09-08 "fragile" flag resolved upward), EV/EBIT 12.59x, ND/EBITDA −2.36x.

**ANET (†):** Revenue CAGR (9,006 ÷ 4,381)^(1/3) − 1 = 27.2% using FY2025/FY2022.

## ✅ Qualified Quality List — **0 names**

No candidate clears all 8 filters. **Qualified count vs. prior round: 1 → 0.**

**Single-filter near-misses (priority watch):**
- **ZTS (Zoetis, new)** — only Rev CAGR (5.42%); otherwise the most valuation-attractive name in the pool (FCF yield 8.04%, EV/EBIT ~10x), with ROIC 22.7% and net margin 27.5%. Growth has decelerated; worth a dedicated look at whether FCF yield is depressed-price-driven (EV/EBITDA fell 14.9x → 9.0x vs FY2025).
- **CPRT** — only Rev CAGR (6.43%); FY2026 growth stalled at +0.41%. A rebound would be needed for the window to recover.
- **ADP** — only Rev CAGR (6.81%); sixth consecutive round with this exact single-filter story.
- **ABNB** — only EV/EBIT (~30–31x).
- 2-filter: **BR** (GM + CAGR), **CRM** (ROIC + EV/EBIT; FCF yield 7.85%), **TYL** (ROIC + EV/EBIT), **MA** (FCF yield + EV/EBIT), **GOOGL** (FCF yield + EV/EBIT).

## 3. Qualitative pass (Step 3)

Not run — no name cleared the quantitative gate. (Batching rule N/A.)

## 4. Data gaps and caveats (Step 4)

- **Three `MissingInputError`s** (CPRT, BRK-B: NaN `EBIT` in trailing quarters; ANET: missing latest Total Debt) — covered via `stockanalysis.com`; no estimation. ANET's EV/EBIT and BRK.B's gross margin/EV/EBIT were not independently pulled this round (ANET and BRK.B fail on other filters regardless).
- **yfinance vs stockanalysis.com definitional differences:** ROIC and EV/EBIT differ materially for several names (CRM ROIC 13.4% vs 10.96%; CRM EV/EBIT 17.7x vs 23.7x; GOOGL EV/EBIT 13.6x vs 27.6x; AAPL ROIC 74% vs 102%). Verdicts for near-miss names use `stockanalysis.com` (consistent with all prior NA-1 rounds). GOOGL's yfinance EV/EBIT looks inflated-EBIT (likely includes non-operating gains) — not independently confirmed. Figures are not strictly comparable to the 09-08 round's stockanalysis-only values.
- **LLY** — yfinance returns FCF-positive-3yr = False, contradicting prior rounds; not reconciled this session. Fails FCF yield (1.33%) and EV/EBIT independently, so the verdict is unaffected.
- **GOOGL TTM net margin 54.8%** — same unexplained outlier flagged since 08-18; unchanged.
- **BRK.B** Revenue CAGR 7.14% reproduced exactly (371,444 ÷ 302,020), matching 09-08.
- **ETF-pool visibility:** ABNB/CRM/DDOG carried over without being visible in the parsed holdings; the ETF pull is a top-holdings view, not guaranteed exhaustive.
- **EODHD:** 403 on a single probe (see §0); unused.

## 5. Coverage log update (Step 5)

[screening-coverage-log.md](../framework/screening-coverage-log.md) NA-1 row: Last screened → 2026-10-03; Qualified names → **0 (CPRT dropped)**; near-misses refreshed; Sources → MOAT/QUAL/QGRW holdings + yfinance (`scripts.fetch_fundamentals`) with stockanalysis.com fallback/cross-check.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate; the smoothed yearly growth rate between two values.
- **EV/EBIT** — Enterprise value ÷ operating profit; lower means cheaper.
- **FCF / FCF Yield** — free cash flow, and free cash flow ÷ market value; higher means cheaper.
- **FY (fiscal year)** — a company's own 12-month reporting year, which may not match the calendar year.
- **Gross / Net Margin** — share of revenue left after direct costs / after all expenses.
- **Net Debt/EBITDA** — leverage gauge; negative means more cash than debt.
- **Phase 01** — this framework's universe-screening/quality-gate stage.
- **Qualified Quality List** — names that cleared Phase 01.
- **ROIC** — Return on Invested Capital; profit earned per dollar of capital employed.
- **Rotation Matrix** — the coverage-log table that tracks which slice was screened when.
- **TTM** — trailing twelve months.

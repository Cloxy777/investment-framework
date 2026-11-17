# 2026-11-17 — SCREENING: North America — NA-2, Round 7 (unattended, fresh 12-name pool)

**Task type:** SCREENING (Phase 01), slice [NA-2](../framework/screening-coverage-log.md). Picked by the rotation rule: oldest "Last screened" date (NA-2, 2026-10-27; next oldest NA-1 11-03). Scheduled run.

## 0. Methodology / source notes

- **EODHD (Path A) not usable:** `EODHD_API_KEY` is set but `/fundamentals` still returns HTTP 403 (free plan; see [decision](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). No bulk screener, so Step 0 used a hand-built pool of names never tested in any prior NA-2 session (checked by grep of all `*-screening-na2.md` logs).
- **yfinance reachable** (after `pip install yfinance pandas`): `python3 -m scripts.fetch_fundamentals <TICKER>` run per name.
- Gate: Gross margin >40%, Net margin >12%, ROIC >15%, Rev 3yr CAGR >8%, FCF positive 3 yrs, ND/EBITDA <2.5x, EV/EBIT <20x, FCF yield >4%.

## 1. Step 1 — structural triage
Pool (12): VRTX, ZTS, EW, ERIE, BR, MA, V, NDSN, LECO, HALO, LNTH, ROK — none structurally excluded (MA/V kept despite known rich valuation to test it live).

## 2. Step 2 — quantitative gate (script output, yfinance)

| Ticker | Gross | Net | ROIC | Rev CAGR | FCF 3y+ | ND/EBITDA | EV/EBIT | FCF Yld | Result |
|---|---|---|---|---|---|---|---|---|---|
| **HALO** | 82.27% | 26.93% | 22.90% | 28.38% | Yes | 1.76x | 19.51x | 5.44% | **PASS 8/8** (EV/EBIT buffer 0.49pp-x) |
| **LNTH** | 61.26% | 17.28% | 17.21% | 18.14% | Yes | 0.59x | 18.21x | 5.82% | **PASS 8/8** (see qualitative) |
| ZTS | 71.35% | 26.15% | 21.65% | **5.42%** | Yes | 1.67x | 12.52x | 6.64% | FAIL (1: Rev CAGR) near-miss |
| BR | **31.52%** | 13.95% | 18.75% | **7.25%** | Yes | 1.59x | 17.46x | 5.87% | FAIL (2: gross margin, CAGR) |
| VRTX | 85.53% | 30.70% | 20.42% | 10.35% | **No** | net cash | **29.93x** | **2.35%** | FAIL (3) |
| MA | 78.42% | 46.73% | 65.89% | 13.82% | Yes | 0.37x | **27.15x** | **2.68%** | FAIL (2: valuation) |
| V | 80.39% | 51.20% | 41.85% | 12.02% | Yes | 0.29x | **27.40x** | **2.77%** | FAIL (2: valuation) |
| NDSN | 55.29% | 18.63% | **12.50%** | **2.53%** | Yes | 1.97x | **25.71x** | 4.03% | FAIL (3) |
| LECO | **35.49%** | 12.40% | 22.23% | **4.02%** | Yes | 1.06x | 19.74x | **3.42%** | FAIL (3) |
| ROK | 50.01% | 15.69% | 22.23% | **-0.26%** | Yes | 1.43x | **24.99x** | 4.03% | FAIL (2) |
| EW | — | — | — | — | — | — | — | — | **Data gap** — script error: TTM Pretax Income NaN. Not estimated, unscored. |
| ERIE | — | — | — | — | — | — | — | — | **Data gap** — script error: no 'EBIT' row. Not estimated, unscored (insurance-services structure also an awkward fit). |

Full per-ticker script output was captured in the session scratch directory; key lines are reproduced above. Advisory flags (cycle_peak, value_trap) are UNKNOWN for HALO/LNTH (EPS series unavailable). FCF/NI (oldest→newest): HALO 116/133/106/113%; LNTH 939/79/149/149% (first-year figure distorted by a tiny NI base). SBC/FCF: HALO 11.3%, LNTH 19.5%.

## 3. Step 3 — qualitative pass (2 survivors, one batch)

**HALO — PASS with FLAGS.** ENHANZE drug-delivery royalty model (asset-light, 82% gross margin). Q3 2026 results (Nov 5) raised guidance: royalties $1.235–1.255B, total revenue $1.86–1.925B; Q3 royalties $341M (+44% YoY), driven mainly by DARZALEX Faspro. Flags: (1) **royalty concentration on DARZALEX Faspro**; (2) **ENHANZE patent expiry from 2027** (US; EU step-down Mar 2029 per one summary — unverified vs. 10-K), partly offset by acquisitions (Elektrofi, Surf Bio) and MDASE patent litigation (Dutch court found Merck infringing, Oct 2026); (3) EV/EBIT 19.51x leaves almost no valuation buffer; (4) 28% CAGR includes acquisition/royalty-step effects. Sources are aggregators/press releases, not filings.

**LNTH — INELIGIBLE (pending takeover).** Search results indicate Lantheus is being acquired by Curium for $102.50 cash/share (+ up to $12 milestone), FTC HSR waiting period extended 2026-10-21, guidance suspended. A pinned deal-price stock has no framework-style valuation opportunity; do **not** carry as a `/new-position` candidate unless the deal breaks. Underlying PSMA-imaging franchise faces price compression (340B) and competition. Deal facts come from low-quality secondary sources — verify before relying.

## 4. Step 4 — data gaps
EW and ERIE unscored (script errors above). Not estimated.

## 5. Outcome
NA-2 "Last screened" → 2026-11-17. Qualified total **6 → 7** (+HALO; LNTH passed quant but excluded as takeover target). Near-miss: ZTS (Rev CAGR 5.42% only). Next step: `/new-position HALO` (verify patent-expiry facts from filings first).

## Glossary
- **CAGR** — Compound Annual Growth Rate.
- **EV/EBIT** — Enterprise value ÷ operating profit; lower = cheaper.
- **FCF / FCF Yield** — cash left after running the business; yield = FCF ÷ market cap.
- **Gross / Net Margin** — share of revenue left after direct costs / all costs.
- **Net Debt/EBITDA** — leverage measure.
- **ROIC** — Return on Invested Capital.
- **Royalty** — fee a company receives for licensing its technology/IP to others.
- **ENHANZE** — Halozyme's technology enabling subcutaneous (under-skin) versions of injected drugs.
- **SBC** — Stock-based compensation.
- **HSR / FTC** — US antitrust review of mergers.
- **340B** — US drug-discount program that compresses drug prices.
- **Phase 01** — this framework's quality-gate screening stage.

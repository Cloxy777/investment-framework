# Global Screening Coverage Log

Tracks which slice of the global investable universe each `/screen` session has covered, so Phase 01 screening **rotates systematically through every region and sector** instead of repeatedly re-covering the same familiar large-cap names. The point: a great business — any sector, any country — should never be missed simply because it was never in the starting pool.

## How to use this log

1. **Picking the next slice:** when `/screen` runs with no argument, take the row below with the oldest "Last screened" date (ties → "Never" first, then alphabetical), and screen that. State which slice was picked and why.
2. **Sourcing non-US slices:** TIKR and Koyfin both cover 100k+ global tickers (see [valuation-scoring.md](valuation-scoring.md) — Screening Tools). Filter them by region/country, and start from regional quality-factor pre-screens the same way the first US pass started from MOAT/QUAL/QGRW — e.g. MSCI International Quality Factor (IQLT), MSCI Europe/Japan/EM Quality indices, or country-level quality/Magic-Formula screens on Gurufocus/Validea.
3. **After screening:** update that row's *Last screened* date, *Qualified names found*, and *Sources used* — commit it alongside the session log so the rotation state persists in git history.
4. **Data-gap caveat (CLAUDE.md Rule 0):** non-US small/mid-caps often carry thinner third-party coverage — currency translation, local filing standards (IFRS vs. GAAP vs. local GAAP), ADR-vs-ordinary-share quirks. Flag missing metrics; never estimate them.

## Rotation Matrix

| Slice | Geography | Sector emphasis this pass | Last screened | Qualified names found | Sources used |
|---|---|---|---|---|---|
| NA-1 | North America (US + Canada) | Tech, Communication Services, Consumer Discretionary | 2026-07-07 | 0 — near-misses flagged: ABNB, ADP, QCOM (each miss only 1 filter), MA, FTNT, KLAC (each miss only 2, both close) | MOAT/QUAL/QGRW ETF holdings + stockanalysis.com quantitative gate (yfinance/direct Yahoo blocked by a TLS connection-reset error this session) — see [sessions/2026-07-07-screening-na1.md](../sessions/2026-07-07-screening-na1.md) |
| NA-2 | North America (US + Canada) | Financials, Healthcare, Industrials, Energy, Materials, Real Estate/Utilities | 2026-07-04 | 1 — Doximity (DOCS); near-misses flagged: DexCom (DXCM), CME Group (CME) | Structural triage (domain knowledge) + sourced fundamentals from stockanalysis.com (yfinance/Yahoo Finance returned persistent HTTP 429 rate-limit responses all session) — see [sessions/2026-07-04-screening-na2.md](../sessions/2026-07-04-screening-na2.md) |
| EU | Europe (UK, Eurozone, Switzerland, Nordics) | All sectors | 2026-06-19 | 2 — Experian (EXPN.L), Deutsche Börse (DB1.DE); near-misses flagged: LVMH, SAP, RELX, Assa Abloy; data-gap cases: Novo Nordisk, Adyen | Structural triage (domain knowledge) + sourced fundamentals from `yfinance` — see [sessions/2026-06-19-screening-europe.md](../sessions/2026-06-19-screening-europe.md) |
| JP | Japan | All sectors | 2026-06-30 | 0 — no clean Phase 01 PASSes this rotation; near-misses flagged: M3 Inc (2413.T), Obic (4684.T) | Structural triage (domain knowledge) + sourced fundamentals from `yfinance` — see [sessions/2026-06-30-screening-japan.md](../sessions/2026-06-30-screening-japan.md) |
| APAC-EX-JP | Developed Asia-Pacific ex-Japan (Australia, Hong Kong, Singapore, South Korea, Taiwan) | All sectors | 2026-07-11 | 1 clean — iFAST Corporation (AIY.SG); flagged pending `/new-position` confirmation: KRAFTON (259960.KS, gross-margin data gap), ResMed (RMD) and CSL (CSL.AX) — both reversed from near-miss/data-gap to all-8-clear on live/current pricing; near-misses: Prada (1913.HK, narrow ROIC miss), Computershare (CPU.AX, narrow growth miss) | Structural triage (domain knowledge) + sourced fundamentals from stockanalysis.com (yfinance blocked all session — `curl_cffi` SSL "Connection reset by peer", same failure mode as the 2026-07-07 NA-1 session); `twse` exchange-code path on stockanalysis.com also down all session (404, confirmed via TSMC/2330 retest) — see [sessions/2026-07-11-screening-apac-ex-japan.md](../sessions/2026-07-11-screening-apac-ex-japan.md) |
| EM | Emerging Markets (China, India, Brazil, Mexico, and other major EM) | All sectors | 2026-07-14 | 3 — Tencent (0700.HK), PDD Holdings (PDD), Kweichow Moutai (600519.SH); near-miss watchlist: Infosys (INFY, 0.02pp CAGR miss), NetEase (NTES), WEG (WEGE3.SA) | Structural triage (domain knowledge, refreshed pool) + sourced fundamentals from stockanalysis.com (reachable this session, unlike 06-14; yfinance/Yahoo still blocked — `curl_cffi` SSL connection reset) — see [sessions/2026-07-14-screening-emerging-markets.md](../sessions/2026-07-14-screening-emerging-markets.md) |

*Add or split rows as coverage matures — e.g., once a region's "all sectors" pass turns up too many qualified names to triage in one session, split it into sector-focused slices the way NA was split into NA-1/NA-2.*

## Full-cycle cadence

One full pass through every row = the **annual full universe re-screen** already on the [operating calendar](operating-calendar.md) (January). Target: clear the entire matrix at least once a year. Re-run a slice sooner if a major index reconstitution, sector-wide re-rating, or a Rate Environment Gate regime shift makes it likely the qualified set there has moved.

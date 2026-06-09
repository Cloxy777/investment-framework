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
| NA-1 | North America (US + Canada) | Tech, Communication Services, Consumer Discretionary | 2026-06-07 | 11 — ABNB, AMAT, ANET, APP, AVGO, FTNT, KLAC, LLY, LRCX, MA, PLTR | MOAT/QUAL/QGRW ETF holdings + Finviz quantitative gate — see [sessions/2026-06-07-screening-broad-quality-universe.md](../sessions/2026-06-07-screening-broad-quality-universe.md) |
| NA-2 | North America (US + Canada) | Financials, Healthcare, Industrials, Energy, Materials, Real Estate/Utilities | 2026-06-09 | 5 — ISRG, VEEV, IDXX, MCO, CTAS (conditional) | ETF fallback (QUAL/MOAT/sector ETFs) — see [sessions/2026-06-09-screening-na2-healthcare-financials-industrials.md](../sessions/2026-06-09-screening-na2-healthcare-financials-industrials.md). ⚠️ Re-run with EODHD for small/mid-cap coverage. |
| EU | Europe (UK, Eurozone, Switzerland, Nordics) | All sectors | Never | — | — |
| JP | Japan | All sectors | Never | — | — |
| APAC-EX-JP | Developed Asia-Pacific ex-Japan (Australia, Hong Kong, Singapore, South Korea, Taiwan) | All sectors | Never | — | — |
| EM | Emerging Markets (China, India, Brazil, Mexico, and other major EM) | All sectors | Never | — | — |

*Add or split rows as coverage matures — e.g., once a region's "all sectors" pass turns up too many qualified names to triage in one session, split it into sector-focused slices the way NA was split into NA-1/NA-2.*

## Full-cycle cadence

One full pass through every row = the **annual full universe re-screen** already on the [operating calendar](operating-calendar.md) (January). Target: clear the entire matrix at least once a year. Re-run a slice sooner if a major index reconstitution, sector-wide re-rating, or a Rate Environment Gate regime shift makes it likely the qualified set there has moved.

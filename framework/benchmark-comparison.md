# Benchmark Comparison — MSCI Quality Index

## Purpose

40-year stress test compares this framework against S&P 500 — low bar; any quality-tilted strategy should beat a cap-weighted index over long periods. Meaningful question: does framework beat a *properly constructed quality benchmark* that's also bias-free?

This page tracks ongoing performance against two survivor-blind quality benchmarks. **Update annually in Q1.**

## Why Not Just Use the S&P 500?

S&P 500 has no quality filter — beating it with a quality-value strategy is expected, simply confirms the quality premium exists (already well-documented). Meaningful test: does *this specific implementation* of quality-value outperform a *systematic, bias-free* implementation of the same idea? MSCI QUAL and QMJ are that test. Beating S&P 500 by 3%/yr might mean genuine skill — or just that any quality ETF would've done the same.

## The Two Benchmarks

### Benchmark 1 — MSCI World Quality Index (MSCI QUAL)

Selects stocks from MSCI World universe on three factors: high ROE, low leverage (debt-to-equity), low earnings variability. Reconstituted twice yearly using point-in-time data — no survivorship bias.

- **Tracking ticker:** iShares MSCI World Quality Factor ETF (IWQU) or Xtrackers MSCI World Quality ETF
- **Reference:** MSCI World Quality vs MSCI World (2000–2023): ~+3.5%/yr outperformance, strongest in crises (2000–02, 2008–09), weakest in speculative bull runs (2017, 2020–21)

### Benchmark 2 — Fama-French Quality Minus Junk (QMJ) Factor

Academic factor (AQR / Asness et al., 2019): long high-quality, short low-quality across major markets, based on profitability, growth, safety, payout signals. Data from 1957.

- **Source:** AQR Data Library (aqr.com) — free, updated quarterly
- **Reference:** ~+4.1%/yr annualised alpha (1963–2023), Sharpe ~0.5. Negative years: 2020, 1999–2000.

## Annual Comparison Table

Update each Q1 — compare framework's trailing 12-month total return (incl. dividends, currency-adjusted) against both benchmarks.

| Year | Framework Return | MSCI QUAL Return | QMJ Factor Return | S&P 500 | Framework vs QUAL | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 (YTD) | — | — | — | — | — | First year of tracking |

## Interpretation Rules

- **Beats QUAL by >2%/yr over 3-year rolling window:** Active selection adding real value. Continue.
- **Roughly matches QUAL (<2% gap) over 3 years:** Consider shifting 30–40% of portfolio to a QUAL ETF — reduces selection risk and time cost while preserving quality exposure.
- **Underperforms QUAL over 3 years:** Stock selection destroying value relative to passive quality tilt. Full review of Phase 01–02 criteria required (log in `decisions/`); consider larger passive allocation.

*Added: May 2026 · Addresses survivorship bias in the 40-year stress test · Update annually in Q1*

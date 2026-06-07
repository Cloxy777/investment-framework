# 📊 Benchmark Comparison — MSCI Quality Index

# Purpose

The 40-year stress test compares this framework against the S&P 500. That is a low bar — any quality-tilted strategy should beat a cap-weighted index over long periods. The meaningful question is whether the framework beats a *properly constructed quality benchmark* that is also bias-free.

This page tracks ongoing performance against two survivor-blind quality benchmarks. Updated annually in Q1.

---

# The Two Benchmarks

## Benchmark 1 — MSCI World Quality Index (MSCI QUAL)

**What it is:** Selects stocks from the MSCI World universe based on three quality factors: high ROE, low leverage (debt-to-equity), and low earnings variability. Reconstituted twice per year using point-in-time data. No survivorship bias.

**Why it matters:** If the framework cannot beat MSCI QUAL net of the time cost of active management, a portion of the portfolio should be allocated to QUAL or a similar ETF instead.

**Ticker for tracking:** MSCI World Quality ETF — iShares MSCI World Quality Factor ETF (IWQU) or Xtrackers MSCI World Quality ETF.

**Historical performance reference:**

- MSCI World Quality Index vs MSCI World (2000–2023): ~+3.5% annualised outperformance
- Strongest outperformance: crisis periods (2000–2002, 2008–2009) — quality factor is defensive
- Weakest: momentum-driven bull markets (2017, 2020–2021) — quality trails during speculative runs

## Benchmark 2 — Fama-French Quality Minus Junk (QMJ) Factor

**What it is:** Academic factor constructed by AQR (Asness et al., 2019). Goes long high-quality stocks and short low-quality stocks across all major markets. Based on profitability, growth, safety, and payout signals. Data available from 1957.

**Why it matters:** QMJ represents the pure return to quality as a factor — isolated from market beta. If the framework is genuinely capturing quality at value, it should show positive correlation with QMJ returns.

**Where to access:** AQR Data Library ([aqr.com](http://aqr.com)) — free download, updated quarterly.

**Historical performance reference:**

- QMJ annualised alpha vs market: ~+4.1% (1963–2023)
- Sharpe ratio: ~0.5 — meaningful but not extraordinary
- Negative years: 2020 (growth/momentum dominated), 1999–2000 (bubble peak)

---

# Annual Comparison Table

Update each Q1. Compare framework's trailing 12-month return vs both benchmarks.

| Year | Framework Return | MSCI QUAL Return | QMJ Factor Return | S&P 500 | Framework vs QUAL | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 (YTD) | — | — | — | — | — | First year of tracking |

---

# Interpretation Rules

**If framework beats QUAL by >2%/yr over a 3-year rolling window:** The active stock selection is adding real value. Continue.

**If framework roughly matches QUAL (<2% gap) over 3 years:** Consider shifting 30–40% of the portfolio to a QUAL ETF to reduce selection risk and time cost while preserving quality exposure.

**If framework underperforms QUAL over 3 years:** The framework's stock selection is destroying value relative to a passive quality tilt. Full review of Phase 01–02 criteria required. Consider a larger passive allocation.

**Note on measurement:** Compare on a total-return basis, including dividends. Adjust for any currency effects if the portfolio is denominated in a different currency than the benchmark.

---

# Why Not Just Use S&P 500 as the Benchmark?

The S&P 500 is a cap-weighted index with no quality filter. Beating it with a quality-value strategy in most environments is expected — it simply confirms the quality premium exists, which is already well-documented. The meaningful test is whether *your specific implementation* of quality-value outperforms a *systematic, bias-free* implementation of the same idea. MSCI QUAL and QMJ are that test.

Beating the S&P 500 by 3% per year may mean you are capturing the quality premium (which any ETF can do) — or it may mean genuine skill. Only comparison against QUAL separates the two.

---

*Added: May 2026 · Addresses survivorship bias in 40-year stress test · Update annually in Q1*
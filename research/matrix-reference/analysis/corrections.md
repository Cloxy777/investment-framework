# Corrections to the 29.09 baseline notes (baseline files are untouched)

Date of corrections: 2026-10-03, source: 20 free-tier cards + live methodology page. Baseline claim -> correction.

1. **rules-supplement B1.7** "pessimistic growth = consensus steps 1-2 x 0.50, years 3-5 still decay path" -> the 0.50 coefficient multiplies **all five** steps (ABNB pessimistic 9.5, 9.9, 9.4, 8.9, 8.5 = half of the base path 18.9, 19.8, 18.8, 17.9, 17.0). See formulas/x2.md.
2. **B1.4** "base multiple = min(current, 3-year average)" -> average is the 3-year **trailing** P/E mean **rescaled to the NTM basis**: `mean3 x NTM_PE / trailing_PE` (ABNB 29.3 x 26.3/36.0 = 21.4). Optimistic multiple is not "return to mean / ceiling 26.2" but `1.2 x base` (or the S&P forward P/E 20.1 when base <= 20.1).
3. **B1.8 / E7** "х2 досягається у році N = ln2/ln(1+CAGR)" -> does not fit (e.g. AMD base CAGR 29.4 % shows 2.4 vs 2.67); formula unknown.
4. **B2 vs-own-history lens** "above average -> -1, below -> +1" -> band is +-10 % (within the band 0); `<= 5y-min x 1.05 -> +2` / `>= 3y-max x 0.95 -> -2`; history shorter than 36 months clamps to +-1.
5. **E1 ABNB S&P lens -1 at ratio 1.29** -> explained by **hysteresis** (card now prints "гістерезис: бал лінз «проти S&P 500» лишився з попередньої картки, вхід у смузі 5 % біля порога"): the lens keeps the previous score while the ratio is within 5 % of the threshold (1.3 x 0.95 = 1.235 .. 1.365). Same mechanism explains GOOG PEG, NVDA history lens, V FCF-yield lens.
6. **E2 ABNB growth 13.8** -> revenue 4.8 + EPS 7.0 (EPS growth 29.1 % >= 25 %) + FCF-unknown 2.0 = 13.8; the "FCF forecast" is always unknown (FMP lacks it) and contributes 40 % of its 5 points. EPS band 15-25 % is 5.95 (not 6.0) which explains 15.9 displayed totals.
7. **rules-and-metrics "Unknown values = 40 % of weight"** -> true for growth sub-scores (3.2, 2.8, 2.0) but profitability unknown = 7.5 (50 %), margin 5 (50 %), balance 5 (50 %), SBC 5.5 (offset form), ROIC 0. Sub-score tables on the methodology page are measured steps; real configuration is weight x fraction (9.75/5.25 instead of 9.8/5.2).
8. **Quality maximum** -> Capital & SBC can display 12 of 10; no clamp above.
9. **Ten signs thresholds** now bracketed (formulas/ten-signs.md).
10. **Index sources** changed (SPY/QQQ holdings via FMP; S&P 501, Nasdaq 100 = 100) and the index comparison on charts uses SPY/QQQ prices.
11. **Data completeness** now has recovered gap weights (formulas/data-completeness.md); baseline "ABNB 97 %, ORCL 90 %" explained: guidance 3 pp, SBC share 7 pp.
12. **Access model** (README/open-questions item 1, `screens/access.md`): the invite-code test access seen on 29.09 is gone; `/access/` now offers "Почати безкоштовно" (free showcase) and "Оформити повний доступ" (paid); `/welcome/` "Закрите тестування" copy may be outdated.
13. **Card layout** changed since 29.09: price chart now has 6 periods and SPY comparison, header shows day change and market cap, tile list unchanged (16 tiles incl. 'AI аналітика · платно'), FCF yield and thresholds now shown with config keys (`quality.*`, `red_flags.*`).
14. Matrix counts (start page) on the free tier now count only the 20 registry cards (e.g. A-cheap 2); old 164-card counts in rules-supplement section D are historical.

---
# Corrections added after the paid-tier capture (487 cards)
15. **"Methodology page = rule book" is incomplete**: the page says broken thesis -> BUY WAIT for A/B/C; data show AVOID when the thesis flag coincides with NTM revenue growth < 10 % and when two or more critical flags fire (verdict-rules.md).
16. **Unknown values are not always 40 %**: unclassified companies get the component excluded and the score renormalised over the known weights (quality.md).
17. **Level E** is not only "score < 55": fires on loss-making, SBC/FCF >= 100 % and the registry tag; scores up to 76 (CBOE) can be E.
18. **Rule of 40** applies by registry basket `software` with LTM growth (not NTM), not by business type (quality.md); the 29.09 notes had no such rule.
19. **Baseline `rules-supplement.md` E8 (scatter axis +8)**: with regime bonus the lens sum reaches 6 in the free set; the paid S&P page axis runs -8..+8.
20. **Baseline counts**: universe is 547 (546 on 29.09), 487 cards, screener "показано 487 з 547" (60 tickers without card); NEED_DATA exists (3 cards). The 29.09 note "БРАКУЄ ДАНИХ has 0 companies" is outdated.
21. **Access page**: invite-code flow replaced by free showcase + paid subscription (474 UAH/month early-bird, annual 4 551 UAH); see screens/paid-tier.md.

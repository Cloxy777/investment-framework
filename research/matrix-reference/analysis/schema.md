# Parsed card schema (`data/cards/<T>.json`, built by `analysis/parse_cards.py`)

Raw text stays beside it (`<T>.simple.txt`, `<T>.detailed.txt`) so the parse can be redone (`python analysis/parse_cards.py [T ...]`). NBSP/narrow-NBSP are normalised to spaces; Ukrainian decimal comma -> float; `млрд/млн/трлн` multiplied out in `num()`.

```
ticker_file, captured (ISO time)
header: name, ticker, exchange, day_change_pct, market_cap_short, verdict_block[], verdict_line, shadow_verdict, price_word_chip, level, gate0_note,
        cycle_peak_note, taras_holds, taras_review_line, year_change_pct, off_52w_high_pct, market_cap, ntm_pe, dividend_yield_pct, high_52w, low_52w,
        tile_summaries{tile: collapsed value}, text_analysis, subsector_line, completeness_line, completeness_pct, data_as_of
gate0: headline, text
quality: headline, level, score, components{ name: {points, max, explain, inputs{label: {raw, value, source}}, thresholds_line, threshold_keys[], fields[], sec_tags} },
         sum_components, flag_penalty, score_final, level_final, level_cut_tail, explanation, tag_numbers{moat, predictability}, level_by_year[{year, score, level, flags}], level_history_days
ten_signs: headline, items[{mark: pass|fail|unknown, text}], positive_signals
flags: headline, counts{critical, serious, minor, below_threshold}, sentences[], table[{flag, severity, points_removed, note}], known_risks[]
valuation: headline, eps_growth_peg_pct, eps_growth_peg_analysts, lenses{PEG, FCF yield після SBC, Проти S&P 500, Проти власної історії, Ріст проти EPS індексу: {value, compare, score}},
           lens_sum, lens_sum_word, hysteresis[], eps_5y_table[], eps_path_rule, implied_growth{need_15, need_10, consensus, engine, exit_multiple}, trailing_pe_history{}
valuation_change: headline, text
x2: headline, optimistic_cagr, pessimistic_cagr, engine_growth_per_year, eps_today[3], eps_5y[3], multiple_today[3], multiple_scenario[3], price_5y[3], cagr[3], x2_year[3],
    price_today, growth_paths[[5 strings] x3 (pess, base, opt)], bars{buy_pct, hold_pct}, what_decided, buy_price_table[{row, price, base_cagr, to_current_pct}], price_for_15,
    analyst_table[{fiscal_year_end, eps, growth, analysts}], method_text
ttm: headline, ttm_pe, ttm_pfcf, ttm_pocf, fcf_ttm, ocf_ttm (+_raw), history{P/E|P/FCF|P/OCF: {points, since, mean, max, min, last}}, history_table_tail
other_tiles{next_report, fin_revenue, fin_segments, fin_revenue_forecast, fin_eps, fin_eps_forecast, fin_cashflow, ai}  (raw text, first 6000 chars)
detailed: gate0, gate1, gate2, matrix, x2, verdict_why, needed, headline, position_line, kill-lines text, '-30 %' rule text, structure line
periods{1m,6m,ytd,1y,5y,all}: price chart panel text (textContent)
```
Raw file sections: `simple.txt`: `### BASE`, `### PRICE CHARTS STRIP`, `### PRICE PERIOD PANEL pp-<T>-<period>`, `=== TILE <id> ===` (ids: gate0, level, checklist, flags, valuation, change, returns, ttm, next_report, ai, fin_revenue, fin_segments, fin_revenue_forecast, fin_eps, fin_eps_forecast, fin_cashflow), `### FULL ARTICLE AFTER EXPANDING EVERYTHING`. `detailed.txt`: `### BASE` and `### EXPANDED`.
Test vectors: `../test-vectors.json` (`analysis/make_test_vectors.py`): per ticker `inputs` and `expected`.

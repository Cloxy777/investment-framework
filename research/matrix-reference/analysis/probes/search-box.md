# Probe: header search box
Inputs/outputs: `data/lists/search-probes.txt` (60 queries). Typeahead list under `<input type=search placeholder="Введіть тікер або назву компанії, наприклад: NVDA, Apple">`.
- Hits: ticker (any case), English name, Ukrainian alias, partial strings ("Taiwan", "TSMC", "ab" -> ABNB + GOOG because the name Alphabet contains "ab"); one char "a" lists all names containing it.
- Row format: `TICKER / Name (Ukrainian alias) / · basket · level`.
- Misses (all non-free companies and tickers): Toyota, Nestle, SAP, Tencent, HSBC, 7203.T, 0700.HK, Berkshire, Samsung, 005930.KS, ASML, JPM, JPMorgan, Exxon, Walmart, Coca, Pepsi, Boeing, Lilly, Intel, Disney, Nike, Alibaba, zzzz -> text `нічого не знайшли: у нас 20 компаній` (N = accessible card count).
- Alias gaps: "Ейрбнб" misses (alias is "Ербіенбі").

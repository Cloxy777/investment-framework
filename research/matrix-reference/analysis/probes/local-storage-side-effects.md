# Probe: browser-storage writes made by viewing
- `chartview:<chartid>_table` (48 keys) are written whenever a "таблиця/графік" toggle is clicked on a card. All 48 created by this harvest were removed afterwards.
- `cardmode` is written by the "просто/детально" switch; removed after each card (absent = simple).
- Other origin keys at start and end: `matrix:watchlist_moved`, `watchlist` (`[]`), extension keys (`__bnc_*`, `__bw3w_*`).

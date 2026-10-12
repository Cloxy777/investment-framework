# PROGRESS — matrix.tarasguk.com documentation

Last updated: 2026-09-29 (site banner: this tester's access ends **06.10.2026** -> prioritise breadth, then depth)
Last URL visited: https://matrix.tarasguk.com/start/ (theme test)
Status: browser connected (Claude in Chrome, "Browser 1"). Session = invite-code test access (NOT an email account). Screenshots save to disk OK (JPEG, viewport-sized; `save_to_disk:true`, then `cp` the printed source path into screenshots/). Tip: JS extraction of page text works but output containing `=`,`?`,`&`,`%` gets BLOCKED by the tool — sanitise those chars in the script before returning.
Site language: Ukrainian. Docs are English with UA labels.

## Setup
- [x] Folder scaffold, README, PROGRESS
- [x] Browser connected + logged in (invite-code test access)
- [x] Screenshot-to-disk verified (jpg, not png)
- [x] Nav mapped -> sitemap.md

## Screens
| # | Screen | URL | Status | File |
|---|---|---|---|---|
| 1 | Global chrome (header, banner, search, footer) | all | DONE (in sitemap.md + start.md); todo: header search results page | sitemap.md |
| 2 | Start page | /start/ , / | DONE (todo: empty-cell click, "таблиця" toggle on trades chart) | screens/start.md |
| 3 | How to read a card | /how-to-read/ | DONE | screens/how-to-read.md |
| 4 | Screener | /screener/ | DONE (todo: "Ще 16 фільтрів" panel screenshot, numeric-filter validation, column toggles effect, pagination click) | screens/screener.md |
| 5 | Compare | /compare/ | DONE (2 companies) | screens/compare.md |
| 6-7 | Nasdaq 100 / S&P 500 | /nasdaq100/ /sp500/ | DONE (todo: constituent-table details, "Добірки" clicks) | screens/indices.md |
| 8-9 | What changed / Week | /changes/ /week/ | DONE | screens/changes-week.md |
| 10 | Ideas | /ideas/ | DONE | screens/ideas.md |
| 11 | Report calendar | /reports/ | DONE | screens/reports.md |
| 12 | Taras's portfolio | /portfolio/ | DONE (todo: other 4 KPI tiles' expansions) | screens/portfolio.md |
| 13-16 | My portfolio / watchlist / alerts / access | /my/ /watchlist/ /alerts/ /account/ | DONE incl. filled watchlist + portfolio (test data added and removed 2026-09-29); alerts save not exercised | screens/user-area.md |
| 17 | Company card | /t/<TICKER>/ | DONE for ABNB (simple mode) | screens/company-card.md |
| 18 | Methodology | /methodology/ | DONE | screens/methodology.md + rules-and-metrics.md |
| 19 | Data & access banner | banner | DONE | screens/start.md |
| 20 | Sign-in / access | /access/ | DONE (nothing submitted) | screens/access.md |
| 21 | how-to-enter, welcome, no-access | /how-to-enter/ /welcome/ /no-access/ | DONE (text only; /welcome/ partly) | screens/auth-and-marketing-pages.md |
| 22 | Privacy policy + report-error form | /privacy/ | DONE (summary) | screens/report-error-and-privacy.md |
| 23 | Header search typeahead / no-result | (search) | DONE | screens/search.md |
| 24 | Card variants | /t/... | DONE: STRONG BUY (NVDA), AVOID (ORCL), stop-list (SOFI), spec-only (MU), non-US (005930.KS); БРАКУЄ ДАНИХ has 0 companies today (not observable) | |
| 25 | Card detailed mode + Детальні фінанси + extra bottom sections | /t/... | DONE (addendum in company-card.md); price chart periods + financial tiles DONE (Addendum 2) | |
| 26 | "Повідомити про помилку" form | footer/all | DONE (not submitted) | screens/report-error-and-privacy.md |
| 27 | Start page "таблиця" toggle + empty matrix cell | /start/ | todo | |
| 28 | Dark theme look | all | DONE (start__dark-theme.jpg) | screens/start.md |
| 29 | Mobile layout | all | DONE via 390px iframe (screens/mobile-layout.md) | |

## Flows (flows/*.md; watchlist/alerts flow pending user OK)
- [x] search company -> card
- [x] matrix cell click -> company list -> screener with filters
- [x] screener filter -> results -> card
- [x] compare companies
- [x] watchlist add / remove and portfolio add / remove (done with user OK; alerts save still todo)
- [x] sign-in (documented, not executed)

## Cross-cutting docs
- [x] rules-and-metrics.md (very detailed from /methodology/)
- [x] glossary.md
- [x] open-questions.md
- [x] sitemap.md additions
- [x] README.md summary (update when more is done)

## Do-not-touch
Never click "Вийти". No adds to watchlist/portfolio/alerts, no PDF/CSV/ICS downloads, no email/code entry, no "Повідомити про помилку" submissions without asking the user.

## Resume instructions
Read README.md + PROGRESS.md, then continue from first `todo` above. Copy screenshots with `cp <printed tool-results path> screenshots/<slug>__<state>.jpg`.

---
## 2026-10-03 — replication harvest (Phase 0): BLOCKED, waiting for user
- Baseline files read. Folders created: `data/{cards,lists,history,raw}`, `analysis/probes`, `formulas`. Collector written: `analysis/collector.py` (127.0.0.1, random port + path token, writes only under `data/`); **not yet tested end-to-end** (first page-side `fetch` hung with no request reaching the server — likely Chrome local-network-access prompt or page navigation; re-test once access is back).
- **Blocker:** the Claude in Chrome profile is NOT on the invite-code test access. `/start/` redirects to `/free/start/`; footer says 547 companies; `/screener/` shows "показано 19 з 20" (Taras's registry only, 20 cards, verdict bars STRONG BUY 2 / BUY 5 / BUY WAIT 8 / AVOID 3 / НЕ МІЙ СЕКТОР 1); `/account/` shows "Підписки ще немає" (no subscription, early-bird plan upsell); no test-access banner. Baseline had 164 cards + banner "access ends 06.10.2026".
- Rule respected: no code/email/credentials entered. Nothing downloaded, nothing written to the site.
- Resume: user restores test access in the Chrome profile (or says to proceed on the free tier = 20 cards), then continue at Phase 0 step 3 (collector test).

## 2026-10-03 (later) — user confirmed: proceed on free tier (beta-test free access, 20 registry cards)
- DONE: `/free/methodology/` fully captured: `data/raw/methodology.free.2026-10-03.txt` (verbatim), `formulas/methodology-rules.json` (structured, script-validated), `formulas/methodology-diff-2026-10-03.md` (diff vs 29.09 + what the page cannot tell us).
- Free-tier facts: screener "показано 19 з 20", 19 cards visible: NVDA MA MSFT V NFLX ADBE GOOG TSM PLTR AVGO META AAPL AMD AMZN COST UBER CRM ORCL TSLA; "Оцінка Тараса" column and portfolio hidden; card UI changed (price chart with SPY comparison, 1м/6м/YTD/1р/5р/Макс, market cap, dividend). Baseline-only companies (ABNB, SOFI, MU, 005930.KS, ASML, ADSK, GOOG compare, ...) cannot be re-captured.
- BLOCKER for bulk harvest: Chrome permission `loopback-network` = denied for matrix.tarasguk.com (page fetch to 127.0.0.1 fails). Collector itself works (curl ping OK). Needs user to set Site settings -> Local network / Loopback access = Allow for matrix.tarasguk.com, then reload. Fallback = get_page_text + Write (slower, more tokens).
- Next: cards x19/20 (simple + detailed, all tiles), screener 15 columns, /free/start, indices, reports, changes/week, locked-card look.

## 2026-10-03 (final state of this session) — free-tier harvest + engine replica
Done: Phase 0 (collector `analysis/collector.py`, harvest JS pattern documented in data/INVENTORY.md), Phase 1 on the free tier (20/20 cards simple+detailed, parsed JSON, screener controls/rows, compare tables for all 20, reports with "що дивитись", 18 other pages, 17 locked/missing probes, search probes, methodology), Phase 2 probes (A taxonomy/coverage, B search, C screener numeric/sort/hash, D compare limits, E partial: price period panels + tables via textContent, H none that write) and Phase 3 (engine replica: quality 20/20 exact, lenses/price word/verdict 20/20 with hysteresis exceptions, x2 CAGR within 0.2 pp, next-verdict score/CAGR routes exact).
Deliverables: `formulas/*.md|json`, `analysis/{engine_replica,parse_cards,make_test_vectors,make_coverage,extract_explanations,collector}.py`, `analysis/{REPORT,schema,corrections}.md`, `analysis/probes/`, `test-vectors.json`, `taxonomy.md`, `coverage-matrix.csv`, `data/`.
Left: second/third daily snapshots (hysteresis, quadrant, history), non-US/REIT/loss-making/E-level examples (paid), CSV export (not requested), doubling-year formula, next-verdict price/growth routes, flag firing logic.
Collector stopped; Chrome tab created by this session closed; storage side effects reverted. Last URL: https://matrix.tarasguk.com/free/screener/. No commit made.

## 2026-10-03 (evening) — PAID TIER harvest and final fit
User activated the subscription (monthly plan). Done: all 487 company cards + ABNB harvested (simple mode, every tile; Taras's paid tiles), screener 487 rows x 16 columns, filter membership (baskets, sub-sectors, indices), change feed day/week, portfolio, start page trades, reports (161), index pages, methodology (identical), account/alerts/my/watchlist pages. Parsed 488 JSONs; engine replica run on all (see analysis/REPORT.md): components/penalty/score exact on 488, lenses exact except printed hysteresis, verdict layer 464/467.
Not done: second/third daily snapshots, detailed-mode text for the 467 new cards, CSV export (not requested), AI analytics (teaser only).
Stopped: collector; tabs created by this session closed at the end; browser storage keys written by clicks (`chartview:*`) removed. Last URL: https://matrix.tarasguk.com/how-to-read/ (helper tab).
Operational notes: Chrome freezes/discards hidden tabs (CDP "renderer frozen", tab ids change) — use `analysis/js/harvest_cards.js` (serves from collector `/js/`, holds a Web Lock). Restart recipe in README.

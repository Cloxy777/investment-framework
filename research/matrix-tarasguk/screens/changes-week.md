# Screens: What changed — `/changes/` (today) and `/week/` (week summary)

- Nav: Що нового -> Що змінилось сьогодні (`/changes/`), Підсумок тижня (`/week/`). Same page component: two tabs "За день (N)" / "За тиждень (N)"; `/week/` opens with the week tab preselected (page title "Підсумок тижня: що змінилось"; `/changes/` title "Що змінилось"). Captured 2026-09-29. Screenshots: `changes__day.jpg`, `week__week-tab.jpg`.

## Purpose
Change feed of the engine: what changed in company cards since the previous nightly recalculation (day) or over the last 7 days (week).

## Inputs
Tab buttons `За день (12)` · `За тиждень (64)` (counts of changed cards). Ticker links -> `/t/<TICKER>/`. No other controls.

## Outputs
- Header line: day: "Recalculation 29.09.2026, compared with 26.09.2026: 12 cards changed." Week: "Week from 22.09.2026 to 29.09.2026: 64 cards changed."
- Grouped sections with counts (bullet lists, one line per change `TICKER Company: <what changed> [: reason]`):
  - Увійшли в зону BUY (entered BUY zone) — e.g. "ABNB … verdict BUY WAIT → BUY: entered BUY zone"; week version adds "причина:" (reason) text explaining which methodology change caused it (e.g. 5-year growth now computed from annual analyst forecasts in 12-month segments; PEG second-year growth taken from forecast with more analysts; 3–9 analysts = average with our model, <3 = our model).
  - Вийшли із зони BUY (left BUY zone) — week only in sample (3).
  - Стали дешевими (became cheap) — "price became cheap: fair → cheap".
  - Перестали бути дешевими (stopped being cheap).
  - Нові критичні прапорці (new critical flags) — week (18).
  - Знято критичний прапорець (critical flag removed) — week (2).
  - Звіти і що після них (reports and what follows) — week (3).
  - Інші зміни вердикту і рівня (other verdict/level changes) — e.g. "CDNS level C → B (score 68,8 → 71,2)", "V Visa level B → A (85,0 → 85,0)", "KER level C → D", "STX verdict BUY WAIT → speculation only" (day: 9; week: 50).
  - Нові картки (new cards) — week (1).
  - Звіти найближчих днів (upcoming reports) and Зараз у зоні BUY (16) — week page footer sections.
- Insight for replication: the change feed is derived from nightly snapshot diffs of (verdict, level+score, price word, critical flags, membership in BUY zone), with the *cause* attributed to methodology changes when the change stems from a rules update.

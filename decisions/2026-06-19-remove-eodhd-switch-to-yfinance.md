# 2026-06-19 — Framework change: drop EODHD, standardize on `yfinance`

**What changed:**

Removed all EODHD API references from the framework's operating docs and automation. `yfinance` (already used as the working fallback since the 2026-06-14 screening sessions — EODHD's free plan kept returning 403 on `/screener` and `/fundamentals`) is now the sole automated data source for per-candidate Phase 01 verification and earnings-date checks. Bulk universe screening, which EODHD's screener endpoint used to provide, has no automated replacement — `/screen` Step 0 goes back to a manual TIKR/Koyfin export/paste (or a quality-factor ETF holdings fallback when screener access isn't available, used automatically in unattended routine runs).

**Why:**

EODHD's free-plan limits made it unreliable in practice (see screening-coverage-log.md and the 2026-06-14 session logs), and `yfinance` was already covering the same ground at no cost. Carrying two documented data paths added complexity without adding capability. The `EODHD_API_KEY` committed to `.claude/settings.json` on 2026-06-13 (see that day's decision entry) is also removed — it was a live credential checked into git history; treat it as compromised if it's ever needed again and rotate at eodhd.com before reuse.

**Files touched:**
- `.claude/settings.json` — removed `EODHD_API_KEY`
- `.claude/commands/screen.md` — removed the EODHD-automatic Path A; the former manual Path B (TIKR/Koyfin paste, ETF-holdings fallback) is now the only Step 0
- `framework/valuation-scoring.md` — removed the EODHD screener/fundamentals endpoint docs; `yfinance` is now documented as the standard per-candidate verification method, not a fallback
- `framework/automation-schedule.md` — Routines 1/2 now use `yfinance` for earnings-date checks instead of EODHD's calendar endpoint; Routine 4 now builds its unattended starting universe from quality-factor ETF holdings instead of an EODHD-automated screener pass; removed EODHD from the one-time network allowlist, the January health-check item, and the review-cadence note
- `portfolio/calendar/investment-routine-schedule.ics` — updated Routine 1/2/4 and the Q1-review event descriptions to match

**Not touched (historical record, left as-is):** `sessions/2026-06-14-screening-apac-ex-japan.md`, `sessions/2026-06-14-screening-emerging-markets.md`, `sessions/2026-06-14-new-position-dash.md`, `sessions/weekly-briefs/2026-06-15-weekly-brief.md`, `framework/screening-coverage-log.md`'s Rotation Matrix "Sources used" entries, and `decisions/2026-06-13-automation-routine-schedule.md` — these describe what was actually used in past sessions and stay accurate as a record even though EODHD is no longer part of the current process.

**Follow-up:** Routine 4 (Monthly Universe Screening Slice) previously got full unattended automation from EODHD's bulk screener. Without it, its starting universe is now always the ETF-holdings approximation (MOAT/QUAL/QGRW/IQLT) rather than a true 70k-ticker sweep — a real coverage trade-off versus the 2026-06-13 design, accepted in exchange for not depending on a paid/rate-limited API. Revisit if a reliable free bulk-screener API turns up.

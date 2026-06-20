# 2026-06-20 — Framework change: historical PE lookback shortened to 5yr; FCF/NI conversion now auto-computed

**What changed:**

Two Standard Re-Score inputs that previously required a manual pull from Macrotrends/TIKR/Koyfin are now computed automatically via `yfinance`, closing the data-availability gap that kept Routine 1's `rescore-due` issues from being fully pre-filled:

1. **Historical PE lookback shortened from 10yr to 5yr**, everywhere it's used: Upgrade 2 (Historical PE Relative Modifier, [strategy.md](../framework/strategy.md)), the Forward PE primary/fallback sub-score formulas ([valuation-scoring.md](../framework/valuation-scoring.md)), the Historical PE Fair Value cross-check ([fair-value-methodology.md](../framework/fair-value-methodology.md)), and the operating brief/calendar templates.
2. **FCF/NI conversion ratio is now a computed formula**, not a separate manual lookup.

**Why:**

This started from the question of whether `/rescore` could be more fully automated. Testing live against `yfinance`:

- `t.financials` (annual EPS) only goes back **4 years** on the free tier — too shallow to support a genuine 10-year historical PE average or range. This confirmed the existing manual-Macrotrends step was justified *for a 10-year window specifically*.
- However, `t.get_earnings_dates(limit=40)` (quarterly **Reported EPS**, not the annual statement) returned **49 quarters of history for MSFT — back to 2014**, far deeper than the annual financials. Reconstructing trailing-twelve-month EPS by summing 4 consecutive quarters, then pairing each quarter with its contemporaneous price from `t.history()`, produces a usable PE series. Verified live: MSFT 5yr avg PE 32.0×, range 24.2–38.8× (n=20 quarters) — in line with MSFT's known historical multiple band.
- The user accepted **5 years** as the practical lookback this method reliably supports (20 quarters), rather than holding out for a full 10-year reconstruction of uncertain depth across smaller/less-covered tickers.
- Separately, the FCF/NI conversion ratio was never actually a data-availability problem: `t.cashflow["Free Cash Flow"]` and `t.financials["Net Income"]` are already pulled by the existing `yfinance` Phase 01 verification script ([valuation-scoring.md](../framework/valuation-scoring.md)) — the ratio just hadn't been wired into the automation prompt. Verified against MSFT (2022–2025): 89.6%, 82.2%, 84.0%, 70.3%.

**What this does and does not close:**

- **Closes:** the data-gathering blocker on finishing a `/rescore` — Routine 1 can now pre-fill every Standard Re-Score field, including 5yr avg/low/high PE and FCF/NI conversion, with no Macrotrends/TIKR/Koyfin step required for the common case.
- **Does not close:** the separate, judgment-based reasons `/rescore` stays a human-run command rather than something Routine 1 finishes and pushes to `main` unattended — the qualitative questions (moat, margin durability, disruption vector), the Structural Quality Override call, Short Thesis Engagement, and Rule 0's "stop and ask" requirement when something still doesn't fit. Those are unchanged by this entry.
- **Known consequence:** Step 3 (Rate-Normalised Historical PE, annual January task) draws on the same historical PE series, which is now 5 years deep instead of 10 — fewer rate-matched quarters may be available for that recalc. Flagged in `strategy.md`; revisit if it starts returning too few matching periods to be useful.
- **Known limitation:** `get_earnings_dates` history depth varies by ticker. If a candidate has fewer than 20 quarters of reported EPS, the existing no-history fallback (`FwdPE_Score = 50.0`, flagged) applies rather than computing an average over a shorter, less meaningful window.

**Files touched:**
- `framework/valuation-scoring.md` — Forward PE formulas relabeled 10yr → 5yr; new "automated 5yr avg PE & FCF/NI conversion ratio" subsection documenting the verified method
- `framework/strategy.md` — Upgrade 2 table/header relabeled; Step 3 caveat note added
- `framework/operating-brief.md` — Upgrade 2 and Forward PE formula text relabeled; input-format line relabeled
- `framework/operating-calendar.md` — data-source row, data-input template relabeled
- `framework/fair-value-methodology.md` — Historical PE Fair Value formula relabeled
- `framework/automation-schedule.md` — Routine 1 prompt now computes both fields instead of flagging them as gaps; coverage map and "what stays manual" section updated accordingly
- `decisions/2026-06-20-framework-change-5yr-historical-pe-automation.md` — this entry

**Not touched (historical record, left as-is):** any `sessions/` log that cites a "10yr avg PE" sourced from Macrotrends prior to this date — those describe what was actually used at the time and stay accurate as a record.

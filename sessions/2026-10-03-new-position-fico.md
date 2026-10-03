# NEW POSITION — FICO (Fair Isaac Corporation) — 2026-10-03

**Task type:** NEW POSITION (re-check of a previously failed candidate).
**Prior record:** [2026-09-06 session](2026-09-06-new-position-fico.md) — Quality Score 61.4, FAIL (also hard disqualifier: Net Debt/EBITDA 4.26x). That session is the prior state; earlier near-miss sessions (06-14, 07-07) are superseded by it.

## 1. Live price (Rule 0)

IBKR `get_price_snapshot`, contract_id 269280: **last $661.35** (ts 1790985576, `is_close: false`, intraday), prior close $661.75, change -0.06%. 52-week range $586.41-$1,882.53 (IBKR `misc_statistics`; the 52w low of $586.41 was set inside the last 13 weeks). Versus $934.52 on 2026-09-04 (09-06 session): **-29.2%**. This move is explained (see section 2), not unexplained.

## 2. Rule 9 trigger check since 2026-09-06

| Category | Fired? | Detail |
|---|---|---|
| Earnings | No | Q4 FY2026 (FY ends 30 Sep 2026) not yet reported; expected ~early Nov 2026. No new fundamentals since Q3 FY2026 (quarter ended 30 Jun 2026). |
| Guidance revision | No | None since the Q3 raise already noted on 09-06. |
| Management change | None found | |
| M&A | None found | |
| **Macro/regulatory shift** | **Yes, escalation of the 09-06 event** | Search results (web search, 2026-10-03) report FHFA went further than the 09-03 VantageScore 4.0 approval: it "eliminated VantageScore's pricing disadvantage, creating a level playing field with Classic FICO", and TransUnion locked in **$0.99 VantageScore pricing through 2028** (versus FICO's $10.00 mortgage royalty). Mortgage originations are reported as >60% of the Scores segment revenue. Sources: [Finimize](https://finimize.com/content/fair-isaacs-credit-score-moat-just-got-a-new-rival), [Yahoo Finance](https://finance.yahoo.com/real-estate/articles/us-moves-end-fico-mortgage-131040861.html), [BigGo Finance](https://finance.biggo.com/news/a4689fa8-2f8f-44f6-9ca0-ee34ed8eaf76), [StocksToTrade](https://stockstotrade.com/news/fair-isaac-corporation-fico-news-2026_10_01/). Secondary-source reporting; I did not locate the primary FHFA text this session. |
| >15% price move | Yes, explained | -29.2% since 09-04 close, driven by the regulatory news above and a BofA downgrade (Buy to Neutral, target $1,400 to $700; context only, not an action trigger). Not "unexplained". |

## 3. Quality Score gate

No new financial statements exist since the 09-06 computation (no new 10-Q/8-K; Q4 FY2026 unreported), so the 09-06 inputs are the latest primary-source data and the **Quality Score is carried forward, not recomputed from scratch** (never invent or estimate data; no new primary balance-sheet figures to substitute). I did not run `scripts.scoring.quality_score` since its inputs are identical to 09-06; the 09-06 session log holds the full calculation.

Carried-forward sub-scores (from [2026-09-06](2026-09-06-new-position-fico.md) section 4):

| Sub-score (weight) | Value |
|---|---|
| Profitability (25%) | 100.0 |
| Margins (15%) | 100.0 |
| Growth (20%) | 41.76 (51.76 base - 10 structural-deceleration modifier) |
| Balance Sheet (15%) | 0.0 (Net Debt/EBITDA 4.26x, sub-investment-grade Ba2, no asset-light override) |
| Moat (15%) | 20.0 (1 of 5 signals) |
| FCF Quality (10%) | 100.0 |

```
Quality Score = 25.00 + 15.00 + 8.352 + 0.00 + 3.00 + 10.00 = 61.352 -> 61.4
```

**Direction of new evidence: only negative.** The pricing parity and $0.99 competing price attack the one remaining true moat signal (Brand premium/pricing power) prospectively, and could only lower Moat (20.0) and the Growth modifier further. The Balance Sheet hard disqualifier (4.26x > 2.5x) is unchanged. A lower price does not help: the gate tests business quality, and the lower share price does not change net debt in the formula (market cap falls, but Net Debt/EBITDA uses EBITDA, not market value). No input moved favorably.

**Result: 61.4 / 100.0 - FAILS the 80.0+ gate by 18.6 points, and independently fails the Net Debt/EBITDA hard disqualifier. STOP per `/new-position` step 2.** No Rate Environment Gate, no Phase 02 valuation score, no Composite Score, no fair value or order setup (all moot).

## 4. Recommendation

# **PASS - do not enter. Quality Score 61.4 (unchanged, carried forward), hard disqualifier still fires.**

The -29% price drop is not a buy signal under this framework (act on score changes and fundamentals, never price alone). The thesis-relevant developments since 09-06 are all adverse. No position opened; nothing to log in `decisions/`.

**Flag, not a scoring input:** consider whether the market's repricing could in time bring FICO back to a good-value situation; this only matters if quality is first restored, which requires (a) net debt materially declining and (b) evidence GSE mortgage volumes/pricing hold.

## 5. Next review trigger

- Q4 FY2026 earnings (~early Nov 2026): net debt/EBITDA trend, any disclosed lender/volume or pricing impact.
- Any Moody's rating action (debt roughly doubled in FY2026).
- Primary-source FHFA/GSE operational guidance on VantageScore adoption.

## 6. Watchlist

Per `scripts.watchlist_diff` (old 61.4 PASS -> new 61.4 PASS, no fundamental event flag since no new filing data): decision `append`. A "Last checked (no significant change)" line was appended to `watchlist/not-in-portfolio/FICO/FICO-2026-06-14.md`. `scripts.stale_score --apply`: nothing resolved, nothing newly stale (FICO never carried a stale mark).

## Files touched
- `sessions/2026-10-03-new-position-fico.md` (this file)
- `watchlist/not-in-portfolio/FICO/FICO-2026-06-14.md` (appended check line)
- `framework/glossary.md` (added "Analyst downgrade / price target")

---

## Glossary

Standing definitions in [framework/glossary.md](../framework/glossary.md):

- **Analyst downgrade / price target** - a Wall Street analyst lowering a recommendation or 12-month price forecast; context only, never an action trigger here.
- **FHFA (Federal Housing Finance Agency)** - regulator of Fannie Mae and Freddie Mac; ended FICO's sole-model status in GSE mortgages.
- **GSE (Government-Sponsored Enterprise)** - Fannie Mae and Freddie Mac.
- **Hard disqualifier** - a Quality Score condition (here Net Debt/EBITDA above 2.5x) that fails a company regardless of weighted score.
- **Moat** - a durable competitive advantage; FICO scores 1 of 5 signals.
- **Net Debt/EBITDA** - debt minus cash, divided by operating earnings before depreciation; a leverage measure. FICO: 4.26x.
- **Quality Score** - 0-100.0 grade; 80.0+ needed to proceed to valuation. FICO: 61.4.
- **Rule 0** - always fetch a live price first.
- **Rule 9** - list of events (earnings, guidance, management, M&A, macro/regulatory shift, >15% unexplained move) that force re-valuation.
- **VantageScore** - rival credit score owned by the three credit bureaus; now accepted for GSE mortgages.

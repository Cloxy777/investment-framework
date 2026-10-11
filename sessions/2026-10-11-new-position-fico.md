# NEW POSITION — FICO (Fair Isaac Corporation) — 2026-10-11

**Task type:** NEW POSITION (re-check of a previously-passed candidate; FICO has no [holdings.md](../portfolio/holdings.md) row).
**Prior record:** [2026-06-14](2026-06-14-new-position-fico.md) (Phase 01 FAIL), [2026-07-07](2026-07-07-new-position-fico.md) (Quality 79.4–79.6), [2026-09-06](2026-09-06-new-position-fico.md) (Quality **61.4**, Net Debt/EBITDA 4.26× hard-disqualifier). This session confirms the 09-06 verdict.
**10Y Treasury yield:** not fetched — Rate Environment Gate not run; gate fails before Phase 02 (see §4).

---

## 1. Live price (Rule 0)

IBKR `get_price_snapshot`, contract_id 269280: **last $676.30**, ts 1791590363 → 2026-10-09 23:59:23 UTC (Friday close area, `is_close: false`; markets shut over the weekend, so latest live tick — not inferred). Vs. $934.52 at the 09-06 session = **−27.6%**. Vs. $1,179.19 at first check (06-14) = −42.6%. Press cites YTD −~60% (12/31/2025 close $1,690.62; close $681.77 on 10-07 per press — secondary source, not used as an input).

## 2. Data gaps flagged

- **No new FICO filing since the 09-06 session.** Q4 FY2026 (FYE 30 Sep 2026) not yet reported (~early Nov 2026). All balance-sheet/TTM inputs therefore remain the 30 Jun 2026 figures from the 09-06 session. Nothing newer exists to fetch.
- **Debt after the late-Sep/Oct events is unknown.** Press says FICO "borrowed to accelerate buybacks"; no primary-source figure found for any post-30-Jun debt change. Not estimated (never invent data). Direction of risk is *higher* leverage, not lower.
- No Moody's rating action found (search returned nothing on it) — Ba2 assumed unchanged; Upgrade 5 asset-light override stays inapplicable.
- Phase 02 inputs (forward PE, 5yr PE range, EV/EBIT) **not fetched** — moot, gate fails.

## 3. Rule 9 trigger check — fires (macro/regulatory), new since 09-06

| Category | Fired? | Detail |
|---|---|---|
| Earnings | No | Q4 FY2026 not yet reported. |
| Guidance revision | No new | Last: FY2026 raised at Q3 (30 Jul). Company disclosed ~$27.0M pre-tax severance in fiscal Q4 (below). |
| Management change | No | No CEO/CFO change found. |
| M&A | No | None found. |
| **Macro/regulatory shift** | **YES — fires** | (a) **2026-09-28:** FHFA announced a single Fannie Mae/Freddie Mac pricing grid that includes VantageScore 4.0 with equal upfront mortgage fees — removes a practical advantage for classic FICO. Stock −8% after hours that day, then roughly −20% to −27% on 09-29 (sources disagree on exact %). (b) **2026-10-01:** Bloomberg report that FHFA plans to direct the GSEs to require lenders to pull credit data from **two** bureaus instead of three (reported, not confirmed policy). (c) Same day: Bank of America halved its target to $700 from $1,400 and cut to Neutral. Builds on the 09-03 VantageScore 4.0 approval already scored on 09-06. |
| Restructuring (company event) | Informational | **2026-10-06:** FICO announced ~15% workforce reduction, ~$27.0M pre-tax severance in fiscal Q4. |
| >15% price move | Yes, explained | −27.6% since 09-06 session, explained by the FHFA items above — not unexplained. |

Sources: [Motley Fool 2026-09-29](https://www.fool.com/investing/2026/09/29/why-fair-isaac-corporation-plunged-today/), [Motley Fool 2026-10-02](https://www.fool.com/investing/2026/10/02/massive-news-for-fico-stock-investors-sending-shar/), [StocksToTrade 2026-10-01](https://stockstotrade.com/news/fair-isaac-corporation-fico-news-2026_10_01/), [Yahoo Finance — FICO cutting 15% of workforce](https://finance.yahoo.com/markets/stocks/articles/fico-cutting-15-workforce-losing-125426649.html), [Defense World 2026-10-10](https://defenseworld.net/2026/10/10/why-is-fair-isaac-corporation-nyse-fico-stock-down-60-this-year.html), [MPA — implementation will take time](https://www.mpamag.com/us/specialty/wholesale/fhfas-vantagescore-adoption-is-a-win-but-implementation-will-take-time-executive/572914). All secondary (press); none used as a numeric scoring input. Press also notes adoption is lender-by-lender, not mandated, and tri-merge data still required for now.

## 4. Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology v2026-06-29)

No new financial statements exist since 09-06, so every fundamental input is unchanged. Re-applied each sub-score against the new events:

| Sub-score (weight) | Change vs. 09-06? | Value |
|---|---|---|
| Profitability (25%) | None — TTM net margin 34.06%, ROIC judgment call unchanged → 100.0 | **100.0** |
| Margins (15%) | None — gross margin 85.9% → 100.0 | **100.0** |
| Growth (20%) | Base 51.76 unchanged (FY2025 still latest full FY). Modifier stays **−10** (structural regulatory threat to pricing power — now reinforced by the 09-28 pricing grid and 10-01 two-bureau report). Cannot move up. | **41.76** |
| Balance Sheet (15%) | Net Debt/EBITDA 4.26× (30 Jun 2026) → clamp(100×(1−4.26/4)) = **0.0**; hard disqualifier fires (>2.5×; Ba2, asset-light override N/A). Later debt unknown — risk is upward. | **0.0** |
| Moat (15%) | Already 1/5 signals true (pricing power only). New events pressure even that signal, but it is a prospective read, not yet shown in realized pricing; held at 1/5 conservatively **in FICO's favor**. Cannot rise. | **20.0** |
| FCF Quality (10%) | TTM FCF/NI 117.9% → 100.0 | **100.0** |

```
Quality Score = 100.0×0.25 + 100.0×0.15 + 41.76×0.20 + 0.0×0.15 + 20.0×0.15 + 100.0×0.10
              = 25.00 + 15.00 + 8.352 + 0.00 + 3.00 + 10.00
              = 61.352 → 61.4
```

**Quality Score = 61.4 / 100.0 — fails 80.0+ gate by 18.6 pts, and the Net Debt/EBITDA hard disqualifier (4.26× vs 2.5×) independently fails it.** Even with the most generous reading of the new events (Moat and Growth modifier unchanged from 09-06), score cannot reach 80. The result is a *ceiling* under current data, not an estimate that needs refining.

Per procedure: **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, no fair value/order setup.** All moot.

## 5. Recommendation

# **PASS — do not enter. Quality Score 61.4/100.0 (fails 80.0+ gate by 18.6); hard disqualifier Net Debt/EBITDA 4.26× also fires.**

Price is −27.6% since the last check and −~60% YTD, so the stock looks "cheap" — but the framework does not buy price drops (Rule 9: act on documented triggers, never price alone, and the gate sits *before* valuation). The drop is the market repricing a real, dated, structural erosion of the GSE-mortgage moat plus a debt-funded buyback balance sheet. Earnings are still strong (Q3 revenue +26–27%, Scores revenue +41% per press), which is why this is a "valuation reset" story — but the framework's Quality gate, not the multiple, is the binding constraint.

**No position opened — nothing to log in `decisions/`.**

## 6. Next review trigger

- **Q4 FY2026 earnings (~early Nov 2026):** first primary-source look at post-quarter debt, buyback funding, restructuring charge, and FY2027 guidance. A full re-check is warranted *only* if net debt/EBITDA falls to ≤2.5× **and** Moat evidence recovers — a very large gap (needs Quality +18.6).
- Formal FHFA/GSE guidance on two-bureau pulls, FICO 10T pricing deal (Pulte said a deal with FICO is under review), or lender adoption data.
- Any Moody's action (Ba2) given debt growth.

---

## Files touched this session

- `sessions/2026-10-11-new-position-fico.md` — this log
- `watchlist/not-in-portfolio/FICO/FICO-2026-06-14.md` — new dated row (Rule 9 fired, price −27.6%; score/action unchanged)
- `framework/glossary.md` — added Bi-merge / tri-merge, GSE pricing grid (LLPA)

`watchlist/STALE.md` not touched — FICO is Phase 01 FAIL / not scored, never listed.

---

## Glossary

Standing definitions: [framework/glossary.md](../framework/glossary.md).

- **Bi-merge / tri-merge** — a mortgage credit file merging reports from three bureaus (tri) vs. two (bi); the Oct 1 report says FHFA wants two.
- **FHFA / GSE / VantageScore** — see glossary: regulator of Fannie/Freddie; the two mortgage giants; rival credit score owned by the three bureaus.
- **Hard disqualifier** — a Quality Score condition (Net Debt/EBITDA >2.5×, etc.) that fails a company regardless of weighted score.
- **Net Debt/EBITDA** — debt minus cash, divided by operating earnings before depreciation; leverage measure. FICO 4.26×.
- **Pricing grid (LLPA)** — the fee table Fannie/Freddie charge lenders by loan risk; making it score-neutral removes FICO's fee edge.
- **Quality Score** — framework's 0–100.0 quality grade; 80.0+ needed. FICO 61.4.
- **Rule 0 / Rule 9** — always fetch live price first / events that force a re-look (earnings, guidance, management, M&A, macro, >15% unexplained move).
- **TTM** — trailing twelve months.

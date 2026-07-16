# NEW POSITION Session — ORCL (Oracle Corporation)

**Date:** 2026-07-16
**Trigger:** Automated Telegram Stock-Mention Scan (Routine 6) — FinnInvestChannel post #2945 (2026-07-16, ~15:01 UTC): "52-week lows: Oklo, NuScale, Oracle." Per Rule 0, the Telegram post's text is never used as financial data — it is only the trigger. ORCL is not held and has a prior not-in-portfolio entry ([watchlist/not-in-portfolio/ORCL/ORCL-2026-06-12.md](../watchlist/not-in-portfolio/ORCL/ORCL-2026-06-12.md), most recently addended 2026-07-10 with Quality Score 38.7/100, FAIL). Per `.claude/commands/telegram-scan.md` step 4, a claimed new 52-week low is potentially material new information beyond what the 07-10 entry reflects (which explicitly stated the 52-week low was *unchanged* at $134.57 as of that date) — this independently triggers a fresh `/new-position ORCL` run to verify.

## Step 1 — Live price fetch (Rule 0) and 52-week range check

**IBKR (contract_id 272800, account U19421206):**
- Last trade: **$125.99**, snapshot ts 2026-07-16 16:20:52 UTC, `is_close: false` (live, regular session)
- Bid/ask: $125.92 / $126.04
- Change: -$6.50 / -4.91% (vs. prior close)
- Today's intraday range: low **$125.57**, high $131.78, open $130.00
- `misc_statistics`: 52w high $343.05, 52w low $127.84 (this appears to be an EOD-basis statistic that has not yet rolled forward to reflect today's intraday print — see below), 13w/26w low also $127.84, open 52 weeks ago $233.66

**Cross-check — Yahoo Finance:** $126.90 (-4.22%), ts 11:35:52 AM EDT = 15:35:52 UTC, `Market State: Open`. 52-week range shown: **$125.93 – $345.72**. 0.7% apart from IBKR's last trade, both genuine live quotes ~45 minutes apart — consistent.

**Verdict: new 52-week low confirmed, independently on both sources.**
- Prior 52-week low on file (06-12 session, reaffirmed unchanged 07-10): **$134.57**
- Today's intraday low (IBKR): **$125.57** → **6.69% below** the prior low
- Today's last trade (IBKR): **$125.99** → 6.38% below the prior low
- Yahoo's own 52-week-low field has already rolled to **$125.93**, corroborating that today's session set the new low
- 52-week high has also drifted down to $343.05 (IBKR) / stayed at $345.72 (Yahoo) — the rolling 52-week window is dropping older, higher prints from ~a year ago as time advances; not itself a new event.

**Rule 9 >15% price-move check, from the 07-10 reference price ($141.15):**
```
(125.99 - 141.15) / 141.15 = -10.74%
```
**Does NOT independently cross the 15% Rule 9 threshold** this time (07-10's move from 06-12 was -22.77%; this incremental move since 07-10 is smaller). However, the *new 52-week low* itself is new information the 07-10 entry did not have (it explicitly stated the low was unchanged), which is why `telegram-scan.md` step 4 correctly routed this to a fresh `/new-position` run regardless of the 15%-threshold math. For completeness, cumulative move since the 06-12 baseline ($182.77): **-31.07%**.

**Catalyst investigation (WebSearch, since this is a large continued decline):** The additional ~10.7% slide since 07-10 is attributable to a **continuation of the same narrative already on file**, not a new discrete shock:
- **2026-07-13:** ORCL fell ~6.5% intraday (close $131.54), reported by multiple outlets as continued fallout from the **2026-07-09 S&P downgrade** (BBB→BBB-) — [Motley Fool](https://www.fool.com/investing/2026/07/13/heres-why-oracle-stock-slumped-today/), [MarketBeat](https://www.marketbeat.com/instant-alerts/oracle-nyseorcl-reaches-new-12-month-low-heres-what-happened-2026-07-13/), [TradingKey](https://www.tradingkey.com/news/market-movers/262026758-market-movers-orcl-20260713). Cited drivers: OpenAI revenue-concentration risk (OpenAI ≈ half of Oracle's RPO per S&P), the ~$42B FY2027 FCF-deficit projection (already on file 07-10), and **management raising the FY2027 capex forecast to $90–95B** — up from the ~$70B figure already cited in the 07-10 entry. This is an escalation of an already-known trend, not a new direction.
- **2026-07-14 to 07-16:** Continued weakness/volatility (close $127.94 → $132.49 → today's $125.99), described by [Forbes](https://www.forbes.com/sites/greatspeculations/2026/07/15/how-low-can-oracle-stock-really-go/), [Trefis](https://www.trefis.com/stock/orcl/articles-v3/607048/how-deep-can-oracle-stock-fall/2026-07-14), and [Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60419798/oracle-stock-flashes-oversold-signal-as-it-nears-52-week-lows) as a broader tech risk-off rotation layered on the existing capex/leverage/OpenAI-concentration story, plus an oversold technical setup. No new company-specific catalyst identified.
- **Credit ratings:** Confirmed via WebSearch that Moody's negative-outlook/Baa2 action (citing OpenAI counterparty concentration) **predates** 07-10 and was already reflected in that entry's "all three agencies at the low end of investment grade" language — not a new event. No further rating action (S&P, Moody's, or Fitch) found since 07-09.
- **SEC filings:** No 8-K filed by Oracle (CIK 0001341439) since the 07-10 entry's last-checked filings; no new 10-Q/earnings (next: Q1 FY2027, expected ~mid-September 2026).

**Conclusion: explained, not unexplained** — the price action is a continued repricing of the same capex/FCF-deficit/leverage/OpenAI-concentration thesis already the basis of the 07-10 FAIL, compounded by a raised (worse) FY2027 capex guide and a risk-off tech rotation. No new, discrete, unexplained catalyst.

## Step 2 — Quality Score recheck

**Nothing material has changed in the trailing fundamentals since 07-10.** The Quality Score is computed from the audited FY2026 10-K (fiscal year ended 31 May 2026), filed 2026-06-22 — that filing, and the sub-scores derived from it, are unchanged: no new 10-Q, no new 10-K, no earnings event, and no restatement since 07-10. The FY2027 capex guidance raise ($70B → $90–95B) is *forward* guidance, not a trailing-financials input to the Quality Score engine, and does not itself change any sub-score. No new credit-rating action since 07-09 (already reflected 07-10).

Per this task's branching instruction: since nothing material changed beyond the price itself, the full sub-score table is **not** re-derived from scratch — it is carried forward from the 07-10 addendum (see [watchlist/not-in-portfolio/ORCL/ORCL-2026-06-12.md](../watchlist/not-in-portfolio/ORCL/ORCL-2026-06-12.md) lines 26-43 for full computation detail, sources, and formulas), with the current gate verdict restated below.

| Sub-score (weight) | Value (unchanged from 07-10) |
|---|---|
| Profitability (25%) | 40.0 (FCF-positivity cap applied; would be 60.3 uncapped) |
| Margins (15%) | 82.3 |
| Growth (20%) | 51.9 |
| Balance Sheet (15%) | 0.0 (Net Debt/EBITDA 4.18x primary / 3.73x cross-check, both over threshold) |
| Moat (15%) | 40.0 |
| FCF Quality (10%) | 0.0 |

```
Quality Score = 40.0×0.25 + 82.3×0.15 + 51.9×0.20 + 0.0×0.15 + 40.0×0.15 + 0.0×0.10
              = 10.00 + 12.345 + 10.38 + 0.00 + 6.00 + 0.00
              = 38.7
```

**Quality Score = 38.7 / 100.0 — still fails the 80.0+ gate, with both hard disqualifiers still firing:**
1. **Not FCF-positive for 3+ consecutive years** (FY2025 -$0.394B, FY2026 -$23.686B; no carve-out exists for this disqualifier)
2. **Net Debt/EBITDA over threshold** (4.18x primary / 3.73x cross-check, both exceed the 2.5x standard threshold; the asset-light 4x override does not apply to Oracle)

## Step 3 — Rate Environment Gate / Phase 02 valuation

**Not reached.** Per `new-position.md`, the Quality Score gate (80.0+) must clear before Phase 02 valuation proceeds. ORCL fails at 38.7/100.0 — same verdict as 06-12 and 07-10, now reconfirmed against fresh live pricing and a fresh 52-week-low check. No Composite Score computed.

## Step 4 — Fair value / order setup

**Not applicable.** Gate not cleared.

## Step 5 — Recommendation

**PASS / watchlist only — do not enter.** The Quality Score gate fails decisively (38.7 vs. 80.0 required) on two independent hard disqualifiers that are unchanged from 07-10: persistent negative FCF and excessive leverage (Net Debt/EBITDA). The new 52-week low ($125.57 intraday, 6.7% below the prior $134.57 low) is real and independently confirmed on two data sources, but it is a continuation of an already-documented, already-explained repricing (S&P downgrade, FY2027 FCF-deficit/capex escalation, OpenAI concentration risk) — not new information that would flip the trailing-financials-based Quality Score gate. No entry, no limit order. Continue to hold on watchlist only.

## Data gaps flagged

None new this session. All required trailing inputs (FY2026 10-K figures, live price, 52-week range) were available from primary/live sources; no metric was invented or estimated. Forward-looking figures (FY2027 capex guidance) were cited as context only, not used as Quality Score inputs, consistent with Rule 0.

## Next review trigger

Unchanged from 07-10: ORCL's FY2027 Q1 earnings (~mid-September 2026); any further credit-rating action; resolution/expansion of the equity/debt financing plan; Net Debt/EBITDA crossing back under 2.5x; ROIC clearing 15%; FCF returning to positive for a full fiscal year; a >15% unexplained price move from the new reference price of $125.99 (superseding the prior $141.15 reference).

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session: 52-week range, 8-K, 10-K, 10-Q, Credit rating / Investment grade, FCF (Free Cash Flow), Hard disqualifier, Net Debt/EBITDA, Quality Score, Rule 0, Rule 9, RPO (Remaining Performance Obligation).

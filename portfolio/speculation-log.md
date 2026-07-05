# Speculation Sleeve Log

## Purpose

Every trade entered under the [Speculation Module](../framework/speculation-module.md) is logged here — the sleeve's equivalent of [override-log.md](override-log.md), but for a bounded, sanctioned activity rather than a rule violation. The point is the same: untracked, unreviewed trades are how speculation quietly turns destructive. Logged and reviewed, it stays a small, contained experiment that either earns a larger allocation or gets shut down on the evidence.

**Reviewed monthly** (not annually — the sleeve's horizon is weeks, not years).

## Sleeve status

| | |
|---|---|
| Bucket cap (Rule 2) | 5% of total portfolio (proposed default — confirm) |
| Current sleeve value | $0.00 |
| Current sleeve utilization | 0% of cap |
| Open positions | 0 |

*Update this table at every `/sync-portfolio` once the sleeve holds anything.*

## Trade Log

| Date Opened | Ticker | Instrument | Catalyst (Rule 6) | Time-Stop | Stop-Loss / Max Loss | Size ($ / % of sleeve) | Entry Price | Exit Date | Exit Price | P&L | Outcome vs. Thesis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *(none yet)* | | | | | | | | | | | |

## Evaluated but not entered

Trades that went through Rules 1/6/7/8 but didn't clear one or more gates — logged so "why we passed" isn't lost, same spirit as the trade log itself.

| Date | Ticker | Gate(s) that failed | Notes |
| --- | --- | --- | --- |
| 2026-07-01 | META | Rule 1 (Quality Score not yet confirmed ≥80 under current methodology), Rule 6 (catalyst unconfirmed — Bloomberg report on AI compute sales, not company-confirmed), Rule 3 (cheapest reasonable single options contract exceeded the proposed per-trade cap at current portfolio size) | Full evaluation in [sessions/2026-07-01-speculation-module-worked-example-meta.md](../sessions/2026-07-01-speculation-module-worked-example-meta.md) — the module's first live test. Existing 6-share core position left untouched. |

## Monthly Review Checklist

1. **Win rate and expectancy** — (avg win × win rate) − (avg loss × loss rate), net of costs, across all closed trades.
2. **Sleeve return vs. benchmark** — vs. S&P 500 and vs. simply holding the same tickers long-term, over a rolling 6–12 month / 20+ trade sample.
3. **Rule violations** — any averaging-down, any skipped time-stop, any trade without a documented catalyst at entry? Each one is a discipline failure to fix, not a one-off.
4. **Kill-switch check (Rule 11)** — if the sleeve is underperforming the benchmark over the rolling sample, this is the trigger to shrink the cap or pause new entries. Don't wait for the annual review to act on this one.

*Added: 2026-07-01, alongside [framework/speculation-module.md](../framework/speculation-module.md) — see [decisions/2026-07-01-framework-change-speculation-module.md](../decisions/2026-07-01-framework-change-speculation-module.md).*

---
description: Run Phase 01 universe screening to build a Qualified Quality List
---

Run a `SCREENING` session — Phase 01 of the [strategy](../../framework/strategy.md), using the quantitative pre-screen filters in [valuation-scoring.md](../../framework/valuation-scoring.md).

Universe / sector to screen: $ARGUMENTS

---

## Step 0 — Fetch the starting universe automatically

Check whether `EODHD_API_KEY` is set in the environment.

### Path A — EODHD key is present (fully automatic)

Run a two-phase automated screen against the global universe.

**Phase A-1: Screener pre-filter (reduces ~70k tickers → ~300–600 candidates)**

Call the EODHD screener endpoint, paginating with `limit=100` until all results are collected. Apply the best available quality filters — try these fields in the `filters` array and drop any that return an API error (they are not supported as filter fields on this plan):

```
https://eodhd.com/api/screener?api_token={EODHD_API_KEY}
  &filters=[
    ["market_capitalization",">=","300000000"],
    ["ProfitMargin",">=","0.12"],
    ["ReturnOnEquityTTM",">=","0.15"],
    ["OperatingMarginTTM",">=","0.10"],
    ["QuarterlyRevenueGrowthYOY",">=","0.06"]
  ]
  &limit=100&offset=0
```

If quality-metric filters are unsupported, fall back to basic filters only:
```
[["market_capitalization",">=","300000000"]]
```
...and apply the quality checks manually on the response data after collecting all results.

Paginate: increment `offset` by 100 until a page returns fewer than 100 results. Collect all tickers with their returned metrics.

**Phase A-2: Discovery mode (optional)**

If the user wants undiscovered, pre-institutional candidates — or if $ARGUMENTS contains "discovery" — run a second screener call layering the discovery filters from [valuation-scoring.md](../../framework/valuation-scoring.md):

```
["market_capitalization",">=","300000000"], ["market_capitalization","<=","10000000000"]
```

Combine and deduplicate both result sets.

**Phase A-3: Triage and Phase 01 gate**

On the combined candidate list (~300–600 names), apply the full Phase 01 quality gate — sourcing exact numbers for each candidate from the EODHD fundamentals endpoint for any metric not already in the screener response:

```
https://eodhd.com/api/fundamentals/{TICKER}.{EXCHANGE}?api_token={EODHD_API_KEY}&filter=Highlights
```

Phase 01 metrics to verify for each candidate (see [valuation-scoring.md](../../framework/valuation-scoring.md) for thresholds):
- Gross margin > 40% → `GrossProfitTTM / RevenueTTM`
- Net margin > 12% → `ProfitMargin`
- ROIC > 15% → use `ReturnOnEquityTTM` as proxy; flag where equity-heavy structure makes ROE unreliable as a ROIC stand-in
- Revenue growth > 8% (3yr CAGR) → `QuarterlyRevenueGrowthYOY` is a quarterly proxy; flag names where this diverges materially from a 3yr trend
- FCF positive 3 consecutive years → `FreeCashFlow` from annual cash flow statements (call fundamentals endpoint with `filter=Financials` if not in Highlights)
- Net debt/EBITDA < 2.5x → derive from balance sheet if not returned directly
- FCF/Net Income conversion > 70% for 2+ years

**Plan-limit fallback — `yfinance`:** If EODHD's `/fundamentals` endpoint returns `403 — "Only EOD data allowed for free users"` (a plan limitation, not a network block), do not drop to Path B for this step. Instead, pull the same Phase 01 metrics per-candidate via the free `yfinance` Python package as documented in [valuation-scoring.md](../../framework/valuation-scoring.md#free-fallback-yfinance-no-api-key-verified-working-2026-06-14) (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet` — works with exchange-suffixed tickers like `.AX`/`.HK`/`.SI`/`.TW`). Note `yf.screen()` is unreliable for bulk filtering, so it is not a substitute for Phase A-1/A-2 — only for this per-candidate verification step.

**Network caveat:** If EODHD returns `Host not in allowlist`, the current session's network policy does not allow connections to `eodhd.com`. Try the `yfinance` fallback above (it hits `query1.finance.yahoo.com`, which may be allowed even when `eodhd.com` is not); if that host is also blocked, either update the network policy for this session (see [claude.ai/code/docs](https://code.claude.com/docs)) or fall back to Path B below.

---

### Path B — No EODHD key (manual paste)

Ask the user to run the saved Phase 01 screen in TIKR or Koyfin (setup in [valuation-scoring.md](../../framework/valuation-scoring.md)) and paste the ticker list. Do not silently fall back to ETF holdings — that defeats the goal of finding undiscovered names.

The one exception: if the user explicitly says screener access isn't available right now, use regional quality-factor ETF holdings (MOAT/QUAL/QGRW for US; IQLT for international) as an approximate starting pool, but flag prominently that this approach misses small/mid-cap names not yet in those ETFs.

---

## Step 1 — Structural triage

Before spending analysis budget on every candidate, eliminate names that plainly fail Phase 01 on well-documented business-model grounds: thin-margin volume retail, commodity cyclicals, patent-cliff pharma, regulated utilities, etc. Flag every elimination with one-line reason so any name can be pulled back on request.

## Step 2 — Full Phase 01 quantitative gate

Run the complete set of Phase 01 filters with real, sourced numbers on the survivors. Produce the Qualified Quality List.

## Step 3 — Qualitative pass

For each name that clears the quantitative gate, walk through the 5 qualitative questions in [valuation-scoring.md](../../framework/valuation-scoring.md).

**Batch processing:** if this produces more than a couple of names needing a deep qualitative pass, do not launch a parallel subagent per name — run them in small batches (default 2 concurrent) per the batch-processing policy in [new-position.md](new-position.md), committing/pushing progress after each batch and adapting batch size based on observed token cost and whether the session usage limit is hit.

## Step 4 — Data gaps

Do NOT score valuations yet (that's `/new-position` or `/rescore`). Flag any missing metric rather than estimating it (CLAUDE.md Rule 0) — expect this most often for non-US small/mid-caps: currency translation, local filing standards, ADR-vs-ordinary quirks.

## Step 5 — Update the coverage log

Record the "Last screened" date, qualified-name count, and data source used for the relevant slice in [screening-coverage-log.md](../../framework/screening-coverage-log.md). Commit it alongside the session log.

Save the session as `sessions/YYYY-MM-DD-screening-<universe>.md`.

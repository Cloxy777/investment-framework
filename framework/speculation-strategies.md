# Speculation Strategies Playbook

> **Status: v1, added 2026-07-04.** This is the "which technique, and why" layer `/speculate` walks through for any ticker that has already cleared [speculation-module.md](speculation-module.md)'s Rule 1 eligibility gate. This file never overrides that module's numbers (bucket cap, per-trade cap, stop bands, time-stop, minimum R/R) — it only supplies the method for picking a direction, an instrument, and price levels. See [decisions/2026-07-04-framework-change-speculation-strategies-and-speculate-command.md](../decisions/2026-07-04-framework-change-speculation-strategies-and-speculate-command.md) for why this was added.

## Evidence grading

Every technique below is tagged so its actual evidentiary weight is visible, not implied:

- **Academic** — a published, peer-reviewed factor/anomaly with documented out-of-sample persistence, cited by name.
- **Practitioner-established** — decades of documented professional use for timing/risk-framing; evidence for a standalone edge is weaker or mixed, so it is used here only as a regime filter or a risk/level-setting tool, never as the sole reason to enter a trade.

**Deliberately excluded:** chart-pattern reading (head-and-shoulders, triangles, flags/pennants), Fibonacci retracement/extension levels, Elliott Wave, and candlestick-pattern naming (doji, hammer, engulfing, etc.). None has robust out-of-sample evidence of predictive power net of data-mining bias — including them would break the "proven ones only" bar this file is held to. A future addition needs the same evidence citation the entries below carry, recorded in `decisions/`.

## Section A — Regime classification (run first, always)

Classify the ticker's current regime from **live data** (Rule 0 — fetched via `get_price_history`/`get_price_snapshot`, never guessed) before picking a strategy. Three axes:

### A1. Trend regime — SMA(50)/SMA(200) + ADX(14)

```
SMA(n)  = arithmetic mean of the last n daily closes
EMA(n)  = Close × k + EMA_prev × (1 − k), where k = 2 ÷ (n + 1), seeded by SMA(n)

True Range (TR)     = max(High − Low, |High − PrevClose|, |Low − PrevClose|)
+DM                 = (High − PrevHigh) if positive and > (PrevLow − Low), else 0
−DM                 = (PrevLow − Low) if positive and > (High − PrevHigh), else 0
Smoothed TR14/+DM14/−DM14 — Wilder's smoothing: Value_today = Value_prev − (Value_prev ÷ 14) + New_today
+DI14 = 100 × (Smoothed +DM14 ÷ Smoothed TR14)
−DI14 = 100 × (Smoothed −DM14 ÷ Smoothed TR14)
DX    = 100 × |+DI14 − −DI14| ÷ (+DI14 + −DI14)
ADX   = Wilder 14-period smoothed average of DX
```

**Read:**
- **Trending** — ADX(14) ≥ 25. Direction from Price vs. SMA50 vs. SMA200 (price and SMA50 above SMA200 → uptrend; both below → downtrend).
- **Transitional** — ADX(14) 20–25. Treat as a weak signal either way; require stronger confirmation from A3 before acting on it.
- **Range-bound** — ADX(14) < 20. Momentum/breakout strategies (B1, B2) are not eligible here — use the mean-reversion family (B4) instead.

### A2. Volatility regime — IV percentile vs. historical vol

Pull `implied_volatility_percentile` (52-week window) and `historical_vol` directly from `get_price_snapshot` — both are live fields, don't recompute them from scratch.

- **Rich** — IV percentile ≥ 50th AND current IV > historical vol → the market is already pricing a real event. Expect the premium to be expensive and an IV crush (speculation-module.md Rule 8) once the catalyst resolves.
- **Cheap/normal** — IV percentile < 50th AND IV ≈ or below historical vol → no special event priced in. Options are relatively inexpensive, but a "big move coming" thesis is not shared by the market — state that gap explicitly per Rule 7.

### A3. Participation — Relative Volume (RVOL)

```
RVOL = Today's volume-to-date ÷ 20-trading-day average full-day volume
```

Compute the 20-day average from `get_price_history` daily bars; take today's running total from `get_price_snapshot`'s `volume` field. **Caveat:** comparing a partial trading day's volume-to-date against a full-day historical average understates RVOL before the close — note the time of day the reading was taken, and prefer the completed prior session's RVOL when the catalyst isn't intraday-urgent.

- RVOL ≥ 1.5 → confirmed, high-conviction participation (classic volume-confirmation rule from O'Neil/Livermore-style breakout trading) — supports acting on a breakout.
- RVOL < 1.0 → weak participation — a breakout on thin volume is more likely to fail; lean toward passing or waiting for confirmation.

## Section B — Strategy menu

All instruments are constrained by speculation-module.md Rule 8/9: **long shares, or a single long call/put — never a short share position, never a multi-leg spread, never anything requiring margin beyond the sleeve's own cash.** A bearish thesis is always expressed as a long put, never a short share position.

### B1. Momentum / Donchian Breakout
**Evidence:** Academic — Jegadeesh & Titman (1993) documented 3–12 month price momentum persisting across decades and markets (with crash-risk caveats per Daniel & Moskowitz 2016). The specific entry trigger is **Practitioner-established** — the 20-day Donchian channel breakout is the entry rule from the "Turtle Trading" system (Richard Dennis, 1980s), with a long, publicly documented track record.
**Use when:** A1 = trending in the catalyst's direction, A3 RVOL ≥ 1.5 confirming the move, and price clears the 20-day Donchian high (or breaks the 20-day low, for the bearish/put version).
**Instrument:** shares by default; long calls (or puts) instead if A2 = cheap/normal and the time window is short.

### B2. Post-Earnings Announcement Drift (PEAD)
**Evidence:** Academic — Bernard & Thomas (1989), one of the most replicated anomalies in finance. Effect concentrates in roughly the 60 trading days following the print and scales with the size of the earnings surprise.
**Use when:** A confirmed beat-and-raise (or miss-and-cut for the bearish/put version) was reported within the last ~1–10 trading days, ahead of the pre-existing Quality Score gate.
**Instrument:** shares, or long calls/puts matched to the surprise direction. Time-stop set to roughly the 60-trading-day drift window (inside the module's 90-day default).

### B3. Catalyst Binary Event (defined-risk long option)
**Evidence:** Practitioner-established — using a long option (not shares) around a known, dated, binary event (regulatory decision, confirm/deny of a reported deal, litigation ruling) to cap risk at the premium paid is standard, decades-old derivatives-desk practice. The sizing method is speculation-module.md's own Rule 7 (IV-based expected move) and Rule 8 (premium = max loss).
**Use when:** the catalyst has a specific, confirmed date; the expected move is large but direction is genuinely uncertain; A2 is typically "rich" (event already priced in) — accept the IV-crush risk explicitly, since the defined-risk structure bounds the downside regardless of which way it resolves.
**Instrument:** a single long call **or** a single long put, chosen by whatever directional lean the news/technical read supports — not both legs. A long straddle (buying both) is a recognized professional technique for genuinely two-sided binary events, but is **not currently an authorized instrument under Rule 8's "long calls/puts" wording** — flag this to the user as a possible future addition rather than using it unconfirmed.
**Instrument:** long call or long put only (see above) — never both legs.

### B4. Oversold Mean-Reversion Bounce
**Evidence:** Practitioner-established, with mixed academic support — short-horizon reversal exists in some academic literature (Jegadeesh 1990) but is noisy and heavily arbitraged/cost-sensitive at short horizons. Use narrowly, never as a standalone reason to trade.
**Use when:** A1 = range-bound (ADX < 20); RSI(14) ≤ 30 (oversold, long-side) or ≥ 70 (overbought, put-side); price at/through a 20-period Bollinger Band (SMA(20) ± 2×stdev(20)) or a Donchian support/resistance level; **and** a specific, confirmed, already-resolved catalyst exists establishing *why* the move was an overreaction. "Oversold" alone is never the catalyst — Rule 6 still applies in full.
**Instrument:** shares only — avoid paying rich short-dated option premium on top of an already-weaker-evidence bet.

```
RSI(14): AvgGain / AvgLoss over 14 periods, Wilder-smoothed like ATR above.
RS  = AvgGain ÷ AvgLoss
RSI = 100 − 100 ÷ (1 + RS)
```

## Section C — Selection matrix

Run top to bottom; the first matching row wins.

| Condition | → Strategy |
|---|---|
| No confirmed catalyst at all (Rule 6) | **Pass** — stop here regardless of what the regime looks like |
| Trend direction conflicts with the catalyst's implied direction | **Pass** — the thesis fights the tape; this module doesn't override that with conviction sizing |
| A1 trending in the catalyst's direction, A3 RVOL ≥ 1.5 | **B1 — Momentum/Donchian Breakout** |
| Confirmed earnings beat/miss within ~10 trading days | **B2 — PEAD** |
| Scheduled, unresolved, genuinely binary catalyst, A2 rich | **B3 — Catalyst Binary Event** |
| A1 range-bound, catalyst already resolved, thesis = overreaction | **B4 — Mean-Reversion Bounce** |

## Section D — Level-setting techniques (apply regardless of which strategy above is chosen)

**D1 — Expected move.** Already defined in speculation-module.md Rule 7 (implied-vol-based, ATM-straddle cross-checked). This file only decides direction/instrument; Rule 7 always sizes the move — don't recompute it differently here.

**D2 — ATR-based stop distance.** Stop distance = 1.5× ATR(14) for momentum trades (B1/B2 — a tighter invalidation is meaningful in a trending name), or 2× ATR(14) for mean-reversion trades (B4 — needs more room given the counter-trend bet). Cross-check against Rule 8's stated 15–20% default band: if the ATR-based distance falls inside that band, use it (more precise, name-specific); if it falls outside, default back to the nearest edge of the band and flag the mismatch (the name's realized volatility is unusually low or high relative to what the band assumes) rather than silently overriding Rule 8's stated ceiling.

**D3 — Support/resistance for targets.** Set the Sell Target at a technically meaningful level — the prior Donchian channel bound for breakout trades (B1), or the mid-Bollinger-band / opposite band for mean-reversion bounces (B4) — using the 52-week high/low from `get_price_snapshot`'s `misc_statistics` field as a sanity check, rather than an arbitrary percentage gain. Then check the resulting Target/Stop pair against Rule 9's 2:1 minimum R/R before proceeding.

## Open items

- This is a v1 curated list, not exhaustive — expand only with a cited evidence basis, recorded in `decisions/`, same bar as the entries above.
- The long-straddle exception noted under B3 is flagged, not resolved — confirm in [speculation-module.md](speculation-module.md) Rule 8 if the user wants to authorize it.
- ADX/RSI/ATR thresholds above (25/20, 30/70, 1.5–2×) are standard textbook (Wilder) defaults, not back-tested against this specific universe — treat as a reasonable starting point, adjust here (with reasoning recorded) if live use shows they're miscalibrated for the names this sleeve actually trades.

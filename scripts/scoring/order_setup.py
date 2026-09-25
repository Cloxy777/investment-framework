#!/usr/bin/env python3
"""Order setup calculator — implements Steps 2-6 of framework/fair-value-methodology.md.

Buy price, sell target, stop loss, position size, and R/R ratio, cross-checked
against the allocation-cap table. Flags (never silently passes) an R/R below 2:1.

Only runs for a governing score in the 0.0-49.9 range (the bands with a defined
Margin of Safety) — the 50.0-100.0 bands ("Watchlist only" / "Trim or exit") have
no buy-side order setup by design and this script refuses to invent one.

Usage:
    python -m scripts.scoring.order_setup --input path/to/inputs.json

JSON input schema:

{
  "score": float,                    # Composite Score (or Valuation Score if no Quality Score on file)
  "special_category": null | "turnaround" | "speculative",  # overrides the score-band MoS/stop/position ranges
  "fair_value": float,               # blended fair value -> primary sell target
  "bull_fair_value": float,          # -> bull-case trim target (x0.90)
  "live_price": float,               # Rule 0 — fetch live, never infer
  "margin_of_safety_pct": float,     # must fall within the applicable Step 2 MoS range for the band
  "max_loss_pct": float,             # must fall within the applicable Step 4 stop-loss range for the band
  "portfolio_value": float,
  "risk_pct": float,                 # must fall within the applicable Step 5 risk range for the band
  "max_position_pct": float,         # must fall within the applicable Step 5 position-size cap range for the band
  "current_shares": float            # optional, default 0 — for gap-vs-current reporting
}
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from scripts.scoring.common import MissingInputError, require

# (mos_range, stop_range, position_range, risk_range, label)
BANDS = {
    "0.0-29.9": {"mos": (15, 20), "stop": (20, 25), "position": (6, 8), "risk": (1, 2), "label": "Enter now"},
    "30.0-49.9": {"mos": (25, 30), "stop": (25, 30), "position": (3, 5), "risk": (1.5, 1.5), "label": "Set limit order"},
    "turnaround": {"mos": (35, 40), "stop": (30, 35), "position": (2, 3), "risk": (1, 1), "label": "Turnaround / Fallen Angel sub-gate"},
    "speculative": {"mos": (40, 50), "stop": (30, 35), "position": (2, 3), "risk": (1, 1), "label": "Speculative / pre-profit"},
}


class NoOrderSetup(Exception):
    pass


def _select_band(d: dict) -> tuple[str, dict]:
    special = d.get("special_category")
    if special:
        if special not in ("turnaround", "speculative"):
            raise MissingInputError(f"Unknown special_category: {special!r} (expected 'turnaround' or 'speculative')")
        return special, BANDS[special]

    score = require(d, "score")
    if score < 30.0:
        return "0.0-29.9", BANDS["0.0-29.9"]
    if score < 50.0:
        return "30.0-49.9", BANDS["30.0-49.9"]
    if score < 70.0:
        raise NoOrderSetup(f"Score {score} is in the 50.0-69.9 'Watchlist only' band — no Margin of Safety, no order setup")
    raise NoOrderSetup(f"Score {score} is in the 70.0-100.0 'Trim or exit' band — no order setup, see trim/exit protocol")


def _validate_range(name: str, value: float, lo: float, hi: float) -> None:
    if not (lo - 1e-9 <= value <= hi + 1e-9):
        raise MissingInputError(f"'{name}' = {value} is outside the applicable band range [{lo}, {hi}]")


def compute(d: dict) -> dict:
    band_name, band = _select_band(d)

    fair_value = require(d, "fair_value")
    bull_fv = require(d, "bull_fair_value")
    live_price = require(d, "live_price")
    mos_pct = require(d, "margin_of_safety_pct")
    max_loss_pct = require(d, "max_loss_pct")
    portfolio_value = require(d, "portfolio_value")
    risk_pct = require(d, "risk_pct")
    max_position_pct = require(d, "max_position_pct")
    current_shares = d.get("current_shares", 0)

    _validate_range("margin_of_safety_pct", mos_pct, *band["mos"])
    _validate_range("max_loss_pct", max_loss_pct, *band["stop"])
    _validate_range("risk_pct", risk_pct, *band["risk"])
    _validate_range("max_position_pct", max_position_pct, *band["position"])

    steps = [f"Band: {band_name} ({band['label']})"]

    # Step 2 — Buy Price
    buy_price = fair_value * (1 - mos_pct / 100)
    steps.append(f"Buy Price = Fair Value ({fair_value}) x (1 - {mos_pct}%) = {buy_price:.4f}")

    if live_price <= buy_price:
        entry_price = live_price
        order_type = "enter now (live price at/below buy price ceiling)"
    else:
        entry_price = buy_price
        order_type = "limit order at buy price (live price above ceiling)"
    steps.append(f"Live price {live_price} vs buy price ceiling {buy_price:.4f} -> {order_type}; entry price used = {entry_price:.4f}")

    # Step 3 — Sell Target
    sell_target = fair_value
    bull_trim_target = bull_fv * 0.90
    steps.append(f"Primary Sell Target = Fair Value = {sell_target:.4f}")
    steps.append(f"Bull-Case Trim Target = Bull FV ({bull_fv}) x 0.90 = {bull_trim_target:.4f}")

    # Step 4 — Stop Loss
    stop_loss = entry_price * (1 - max_loss_pct / 100)
    steps.append(f"Stop Loss = Entry Price ({entry_price:.4f}) x (1 - {max_loss_pct}%) = {stop_loss:.4f}")

    # Step 6 — R/R (computed before sizing, per the checklist order)
    risk_per_share = entry_price - stop_loss
    reward_per_share = sell_target - entry_price
    rr = reward_per_share / risk_per_share if risk_per_share else float("inf")
    rr_fails = rr < 2.0
    steps.append(
        f"R/R Ratio = (Sell Target {sell_target:.4f} - Entry {entry_price:.4f}) / "
        f"(Entry {entry_price:.4f} - Stop {stop_loss:.4f}) = {reward_per_share:.4f}/{risk_per_share:.4f} = {rr:.4f}:1"
    )
    if rr_fails:
        steps.append(f"*** FLAG: R/R {rr:.4f}:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***")

    # Step 5 — Position Size
    max_dollar_risk = portfolio_value * risk_pct / 100
    shares_by_risk = max_dollar_risk / risk_per_share if risk_per_share else float("inf")
    max_position_value = portfolio_value * max_position_pct / 100
    shares_by_cap = max_position_value / entry_price
    final_shares = min(shares_by_risk, shares_by_cap)
    binding_constraint = "risk-based sizing" if shares_by_risk <= shares_by_cap else "allocation cap"
    position_size_dollars = final_shares * entry_price

    steps.append(f"Max $ Risk = Portfolio Value ({portfolio_value}) x {risk_pct}% = {max_dollar_risk:.4f}")
    steps.append(f"Risk Per Share = Entry ({entry_price:.4f}) - Stop ({stop_loss:.4f}) = {risk_per_share:.4f}")
    steps.append(f"Shares by risk-based sizing = {max_dollar_risk:.4f} / {risk_per_share:.4f} = {shares_by_risk:.4f}")
    steps.append(f"Allocation cap = Portfolio Value ({portfolio_value}) x {max_position_pct}% = {max_position_value:.4f} -> {shares_by_cap:.4f} shares")
    steps.append(f"Position Size (shares) = min(risk-based, cap) = {final_shares:.4f}  [binding: {binding_constraint}]")
    steps.append(f"Position Size ($) = {final_shares:.4f} x {entry_price:.4f} = {position_size_dollars:.4f}")
    steps.append(f"Current shares held = {current_shares}; gap vs. target = {final_shares - current_shares:.4f}")

    return {
        "band": band_name,
        "order_type": order_type,
        "buy_price": buy_price,
        "entry_price": entry_price,
        "sell_target": sell_target,
        "bull_trim_target": bull_trim_target,
        "stop_loss": stop_loss,
        "rr_ratio": rr,
        "rr_fails": rr_fails,
        "max_dollar_risk": max_dollar_risk,
        "shares_by_risk": shares_by_risk,
        "shares_by_cap": shares_by_cap,
        "final_shares": final_shares,
        "position_size_dollars": position_size_dollars,
        "binding_constraint": binding_constraint,
        "current_shares": current_shares,
        "steps": steps,
    }


def render_markdown(result: dict) -> str:
    lines = ["## Order Setup\n", "```"]
    lines.extend(result["steps"])
    lines.append("```")
    lines.append("\n### Order Setup Checklist")
    lines.append(
        f"""
```
[{'✓' if not result['rr_fails'] else '✗'}] Risk/Reward Ratio:      {result['rr_ratio']:.2f}:1  (must be >= 2:1)
[ ] BUY PRICE (ceiling):     {result['buy_price']:.2f}
[ ] Entry Price used:        {result['entry_price']:.2f}  ({result['order_type']})
[ ] PRIMARY SELL TARGET:     {result['sell_target']:.2f}
[ ] BULL-CASE TRIM TARGET:   {result['bull_trim_target']:.2f}
[ ] STOP LOSS:               {result['stop_loss']:.2f}
[ ] Max $ Risk:               {result['max_dollar_risk']:.2f}
[ ] POSITION SIZE (shares):  {result['final_shares']:.4f}  (binding: {result['binding_constraint']})
[ ] POSITION SIZE ($):       {result['position_size_dollars']:.2f}
[ ] Current shares held:     {result['current_shares']}
```
""".strip()
    )
    return "\n".join(lines)


def _parse_set_flags(pairs: list[str]) -> dict:
    out = {}
    for pair in pairs:
        if "=" not in pair:
            raise SystemExit(f"--set expects key=value, got: {pair}")
        key, raw = pair.split("=", 1)
        try:
            value = json.loads(raw)
        except json.JSONDecodeError:
            value = raw
        out[key] = value
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", type=Path, help="Path to a JSON input file")
    parser.add_argument("--set", action="append", default=[], metavar="key=value")
    args = parser.parse_args(argv)

    data = {}
    if args.input:
        data = json.loads(args.input.read_text())
    data.update(_parse_set_flags(args.set))

    if not data:
        parser.error("no input provided — pass --input <file.json> and/or --set key=value")

    try:
        result = compute(data)
    except NoOrderSetup as exc:
        print(f"# No order setup: {exc}")
        return 1
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(render_markdown(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

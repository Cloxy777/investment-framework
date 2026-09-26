#!/usr/bin/env python3
"""IBKR snapshot sync — Stage 3 of scripts/TOKEN-OPTIMIZATION-PLAN.md.

`get_account_positions` / `get_account_balances` / `get_account_orders` are MCP-only (no
standalone script can call them — see scripts/TOKEN-OPTIMIZATION-PLAN.md finding #1), so
this script takes JSON dumps of all three as input: Claude fetches live via MCP, dumps the
JSON, this script does the math/formatting/table-generation documented in
portfolio/sync-sop.md.

**Scope note (flagged per the Stage 3 instructions rather than silently adapted):**
portfolio/snapshots/ibkr.md, ibkr-orders.md, and holdings.md as committed today carry a
large amount of hand-written narrative — week-over-week diff commentary, Rule 9 ±15%-move
flags, cross-references to open GitHub issues and undocumented-order investigations, and
(in holdings.md) a blended IBKR+Freedom24 total requiring judgment about which broker leg
is current. None of that is reconstructable from a single JSON dump without either git
history (to diff against the prior sync) or qualitative judgment — both explicitly Claude's
job, not a script's, per the plan's core principle ("Claude still shows every ... Claude
just stops deriving it token-by-token"). This script therefore generates exactly the
mechanical pieces portfolio/sync-sop.md assigns to each sync step:
  - ibkr.md: the positions table + the position-derived header fields (Gross Position
    Value, Unrealized P&L) via `render_positions_section`; the Cash Balances table + the
    cash-derived header fields (Net Liquidation, Total Cash) via `render_cash_section`.
  - ibkr-orders.md: the active-orders table + header counts via `render_orders_section`.
  - holdings.md: per-ticker Weight % recomputation via `compute_weights` /
    `patch_holdings_weights` (Broker-column and score/review-date columns are left
    untouched, matching sync-sop.md's explicit "leave ... untouched" instructions).
Claude assembles these generated fragments into the full file alongside its own narrative
sections, exactly as Stage 1's scoring calculators produce the shown sub-scores while
Claude still writes the surrounding session-log prose.

Input JSON shapes:

positions.json — list of:
    {"contract_id": 49462172, "ticker": "V", "shares": 1, "market_price": 365.86,
     "avg_cost": 319.51, "currency": "USD"}

balances.json:
    {"base": {"cash_balance": 4097.84, "net_liquidation_value": 50330.70},
     "currencies": {"USD": {"cash_balance": 3836.84, "settled_cash": 3836.84,
                             "exchange_rate": 1.0}, ...}}

orders.json — list of:
    {"order_id": 862563681, "side": "BUY", "ticker": "V", "qty": 9, "order_type": "LIMIT",
     "price": 285.00, "time_in_force": "GTC", "status": "NEW",
     "order_placed_utc": "2026-07-05T19:17:13Z"}

Hard requirement: every field consumed is required, never defaulted. A currency present on
a position or in `currencies` but missing `exchange_rate` when a USD conversion is needed
hard-fails naming the currency (never assume/estimate an FX rate, per Rule 0).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from scripts.scoring.common import MissingInputError, require

ACTIVE_ORDER_STATUSES = {"NEW", "SUBMITTED", "PRESUBMITTED", "PARTIALLY_FILLED"}
EXCLUDED_ORDER_STATUSES = {"REPLACED", "CANCELLED", "FILLED", "EXPIRED", "INACTIVE"}


def _usd_value(amount: float, currency: str, currencies: dict) -> float:
    if currency == "USD":
        return amount
    fx = currencies.get(currency)
    if fx is None or fx.get("exchange_rate") is None:
        raise MissingInputError(f"No exchange_rate for currency '{currency}' — never assumed (Rule 0)")
    return amount * fx["exchange_rate"]


def compute_positions(positions: list[dict], currencies: dict) -> list[dict]:
    rows = []
    for pos in positions:
        ticker = require(pos, "ticker", "position")
        shares = require(pos, "shares", f"position {ticker}")
        market_price = require(pos, "market_price", f"position {ticker}")
        avg_cost = require(pos, "avg_cost", f"position {ticker}")
        currency = require(pos, "currency", f"position {ticker}")

        market_value = shares * market_price
        unrealized_pnl = (market_price - avg_cost) * shares
        pnl_pct = (market_price - avg_cost) / avg_cost * 100 if avg_cost else None
        if pnl_pct is None:
            raise MissingInputError(f"Position {ticker} has avg_cost of 0 — P&L % undefined")
        market_value_usd = _usd_value(market_value, currency, currencies)
        unrealized_pnl_usd = _usd_value(unrealized_pnl, currency, currencies)

        rows.append(
            {
                "ticker": ticker,
                "shares": shares,
                "market_price": market_price,
                "market_value": market_value,
                "avg_cost": avg_cost,
                "unrealized_pnl": unrealized_pnl,
                "pnl_pct": pnl_pct,
                "currency": currency,
                "contract_id": pos.get("contract_id"),
                "market_value_usd": market_value_usd,
                "unrealized_pnl_usd": unrealized_pnl_usd,
            }
        )
    rows.sort(key=lambda r: r["ticker"])
    return rows


def render_positions_section(rows: list[dict]) -> dict:
    gross_position_value_usd = sum(r["market_value_usd"] for r in rows)
    unrealized_pnl_usd = sum(r["unrealized_pnl_usd"] for r in rows)

    lines = [
        "| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |",
        "|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|",
    ]
    for r in rows:
        lines.append(
            f"| {r['ticker']} | {r['shares']} | {r['market_price']:.4f} | {r['market_value']:,.2f} | "
            f"{r['avg_cost']:.4f} | {r['unrealized_pnl']:+,.2f} | {r['pnl_pct']:+.2f}% | {r['currency']} | "
            f"{r['contract_id']} |"
        )
    return {
        "table_markdown": "\n".join(lines),
        "gross_position_value_usd": gross_position_value_usd,
        "unrealized_pnl_usd": unrealized_pnl_usd,
    }


def render_cash_section(balances: dict) -> dict:
    base = require(balances, "base", "balances")
    total_cash_usd = require(base, "cash_balance", "balances.base")
    net_liquidation = require(base, "net_liquidation_value", "balances.base")
    currencies = require(balances, "currencies", "balances")

    lines = [
        "| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |",
        "|----------|--------------|--------------|----------------|-----------------|",
    ]
    row_sum_usd = 0.0
    for currency in sorted(currencies):
        c = currencies[currency]
        cash_balance = require(c, "cash_balance", f"balances.currencies[{currency}]")
        settled_cash = require(c, "settled_cash", f"balances.currencies[{currency}]")
        exchange_rate = require(c, "exchange_rate", f"balances.currencies[{currency}]")
        usd_equiv = cash_balance * exchange_rate
        row_sum_usd += usd_equiv
        lines.append(f"| {currency} | {cash_balance:,.2f} | {settled_cash:,.2f} | {exchange_rate:.7f} | {usd_equiv:,.2f} |")
    lines.append(f"| **Total (USD-equiv)** | | | | **{total_cash_usd:,.2f}** |")

    return {
        "table_markdown": "\n".join(lines),
        "total_cash_usd": total_cash_usd,
        "net_liquidation": net_liquidation,
        "row_sum_usd": row_sum_usd,
        "row_sum_vs_base_diff": row_sum_usd - total_cash_usd,
    }


def filter_active_orders(orders: list[dict]) -> tuple[list[dict], list[dict]]:
    active, excluded = [], []
    for order in orders:
        status = require(order, "status", f"order {order.get('order_id', '?')}")
        if status in ACTIVE_ORDER_STATUSES:
            active.append(order)
        elif status in EXCLUDED_ORDER_STATUSES:
            excluded.append(order)
        else:
            raise MissingInputError(
                f"Unfamiliar order status '{status}' on order {order.get('order_id', '?')} "
                f"({order.get('ticker', '?')}) — ask before classifying as active/non-active"
            )
    return active, excluded


def render_orders_section(orders: list[dict]) -> dict:
    active, excluded = filter_active_orders(orders)
    active_sorted = sorted(active, key=lambda o: o["ticker"])

    lines = [
        "| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |",
        "|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|",
    ]
    for o in active_sorted:
        price = o.get("price")
        price_str = f"{price:.4f}".rstrip("0").rstrip(".") if price is not None else "MARKET"
        lines.append(
            f"| {o['order_id']} | {o['side']} | {o['ticker']} | {o['qty']} | {o['order_type']} | "
            f"{price_str} | {o['time_in_force']} | {o['status']} | {o['order_placed_utc']} |"
        )
    return {
        "table_markdown": "\n".join(lines),
        "active_count": len(active_sorted),
        "excluded_count": len(excluded),
        "excluded_orders": excluded,
    }


def compute_weights(position_rows: list[dict], total_value_usd: float) -> dict:
    if total_value_usd <= 0:
        raise MissingInputError("total_value_usd must be > 0 to compute weight %")
    return {r["ticker"]: r["market_value_usd"] / total_value_usd * 100 for r in position_rows}


_HOLDINGS_ROW_RE_TEMPLATE = r"^(\|\s*\**{ticker}\**\s*\|)([^|]*)(\|.*)$"


def patch_holdings_weights(holdings_markdown: str, weights: dict) -> tuple[str, list[str]]:
    """Replace the Weight % cell (column 2) for each ticker row found; leave everything else.

    Returns (patched_markdown, tickers_not_found). Never invents a row for a ticker not
    already present in holdings.md — a new position belongs to /new-position, not a sync.
    """
    lines = holdings_markdown.splitlines()
    not_found = set(weights.keys())
    for i, line in enumerate(lines):
        for ticker, weight_pct in weights.items():
            pattern = _HOLDINGS_ROW_RE_TEMPLATE.format(ticker=re.escape(ticker))
            match = re.match(pattern, line)
            if match:
                suffix = match.group(2)
                warn_marker = "".join(ch for ch in suffix if ch in "⚠️🚨")
                new_cell = f" {weight_pct:.2f}%{warn_marker} "
                lines[i] = f"{match.group(1)}{new_cell}{match.group(3)}"
                not_found.discard(ticker)
                break
    return "\n".join(lines), sorted(not_found)


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # table headers use "→"; avoid cp1252 crashes on Windows consoles
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--positions", help="Path to positions JSON")
    parser.add_argument("--balances", help="Path to balances JSON")
    parser.add_argument("--orders", help="Path to orders JSON")
    parser.add_argument("--holdings", help="Path to existing holdings.md, to patch Weight % in place")
    parser.add_argument(
        "--total-value",
        type=float,
        help="Denominator for Weight %% (e.g. combined IBKR+Freedom24 total per sync-sop.md) — required with --holdings",
    )
    parser.add_argument("--json", action="store_true", help="Print raw JSON instead of markdown fragments")
    args = parser.parse_args(argv)

    output = {}
    try:
        if args.positions:
            positions = json.loads(Path(args.positions).read_text(encoding="utf-8"))
            balances_currencies = {}
            if args.balances:
                balances_data = json.loads(Path(args.balances).read_text(encoding="utf-8"))
                balances_currencies = require(balances_data, "currencies", "balances")
            rows = compute_positions(positions, balances_currencies)
            output["positions"] = render_positions_section(rows)

            if args.holdings and args.total_value:
                weights = compute_weights(rows, args.total_value)
                holdings_text = Path(args.holdings).read_text(encoding="utf-8")
                patched, not_found = patch_holdings_weights(holdings_text, weights)
                output["holdings_patched"] = patched
                output["holdings_tickers_not_found"] = not_found

        if args.balances:
            balances_data = json.loads(Path(args.balances).read_text(encoding="utf-8"))
            output["cash"] = render_cash_section(balances_data)

        if args.orders:
            orders = json.loads(Path(args.orders).read_text(encoding="utf-8"))
            output["orders"] = render_orders_section(orders)
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(output, indent=2, default=str))
    else:
        if "positions" in output:
            print(output["positions"]["table_markdown"])
            print(f"\nGross Position Value (USD) = {output['positions']['gross_position_value_usd']:,.2f}")
            print(f"Unrealized P&L (USD) = {output['positions']['unrealized_pnl_usd']:+,.2f}\n")
        if "cash" in output:
            print(output["cash"]["table_markdown"])
            print(f"\nNet Liquidation = {output['cash']['net_liquidation']:,.2f}")
            print(f"Total Cash (USD-equiv) = {output['cash']['total_cash_usd']:,.2f}\n")
        if "orders" in output:
            print(output["orders"]["table_markdown"])
            print(f"\nActive orders: {output['orders']['active_count']} · Excluded: {output['orders']['excluded_count']}\n")
        if "holdings_patched" in output:
            print("--- patched holdings.md ---")
            print(output["holdings_patched"])
            if output["holdings_tickers_not_found"]:
                print(f"\nWARNING: tickers not found in holdings.md: {output['holdings_tickers_not_found']}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

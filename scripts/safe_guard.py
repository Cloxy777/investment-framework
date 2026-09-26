#!/usr/bin/env python3
"""Margin safe-guard calculator — Stage 3 of scripts/TOKEN-OPTIMIZATION-PLAN.md.

Implements the worst-case simultaneous-fill margin math and the OCA greedy-grouping
algorithm documented in .claude/commands/safe-guard.md. IBKR active orders and cash
balances are MCP-only (no standalone script can call `get_account_orders` /
`get_account_balances` — see scripts/TOKEN-OPTIMIZATION-PLAN.md finding #1), so this
script takes a JSON dump of both as input: Claude fetches live, dumps the JSON, this
script does the math/formatting.

Input JSON shape:
{
  "orders": [
    {"order_id": 652254170, "side": "BUY", "ticker": "V", "qty": 9, "price": 285.20,
     "currency": "USD", "status": "NEW"},
    ...
  ],
  "balances": {
    "USD": {"cash_balance": 103.69, "exchange_rate": 1.0},
    "AUD": {"cash_balance": -31.07, "exchange_rate": 0.6938792},
    ...
  }
}

Active statuses (kept): NEW, SUBMITTED, PRESUBMITTED, PARTIALLY_FILLED.
Excluded (dropped silently, per safe-guard.md Step 1): REPLACED, CANCELLED, FILLED,
EXPIRED, INACTIVE.
Any other status is unfamiliar — hard-fails naming the order and status rather than
guessing which bucket it belongs in (safe-guard.md: "if an unfamiliar status appears,
ask rather than guessing").

A BUY order with no `price` (e.g. a MARKET order) is never assigned an invented price —
it's excluded from the notional sum and reported separately as an unbounded contributor,
per safe-guard.md Step 1.

A currency with orders but no exchange_rate/cash_balance in `balances` hard-fails (never
assume or look up an FX rate elsewhere — safe-guard.md Step 2 / Rule 0).

Usage:
    python -m scripts.safe_guard --input orders_and_balances.json
    python -m scripts.safe_guard --input - --json   # read JSON from stdin
"""

from __future__ import annotations

import argparse
import json
import sys
from decimal import ROUND_HALF_UP, Decimal

from scripts.scoring.common import MissingInputError, require, round_boundary

ACTIVE_STATUSES = {"NEW", "SUBMITTED", "PRESUBMITTED", "PARTIALLY_FILLED"}
EXCLUDED_STATUSES = {"REPLACED", "CANCELLED", "FILLED", "EXPIRED", "INACTIVE"}
THRESHOLD_USD = Decimal("5000.00")


def _money(value: float) -> float:
    return round_boundary(value, 2)


def _cents(value: float) -> Decimal:
    return Decimal(str(round_boundary(value, 2)))


def filter_active_orders(orders: list[dict]) -> list[dict]:
    active = []
    for order in orders:
        status = require(order, "status", f"order {order.get('order_id', '?')}")
        if status in EXCLUDED_STATUSES:
            continue
        if status not in ACTIVE_STATUSES:
            raise MissingInputError(
                f"Unfamiliar order status '{status}' on order {order.get('order_id', '?')} "
                f"({order.get('ticker', '?')}) — not in the known active or excluded sets; "
                "ask the user how to treat it rather than guessing"
            )
        active.append(order)
    return active


def compute_per_currency(orders: list[dict], balances: dict) -> dict:
    """Returns {currency: {...}} with BUY notional, cash, shortfall, margin usage, contributing orders."""
    currencies = set(balances.keys())
    buy_orders_by_currency: dict[str, list[dict]] = {}
    unbounded_by_currency: dict[str, list[dict]] = {}

    for order in orders:
        if order.get("side") != "BUY":
            continue
        currency = require(order, "currency", f"order {order.get('order_id')}")
        currencies.add(currency)
        price = order.get("price")
        if price is None:
            unbounded_by_currency.setdefault(currency, []).append(order)
            continue
        qty = require(order, "qty", f"order {order.get('order_id')}")
        buy_orders_by_currency.setdefault(currency, []).append(
            {
                "order_id": order.get("order_id"),
                "ticker": require(order, "ticker", f"order {order.get('order_id')}"),
                "qty": qty,
                "price": price,
                "notional": qty * price,
            }
        )

    result = {}
    for currency in sorted(currencies):
        bal = balances.get(currency)
        contributing = sorted(buy_orders_by_currency.get(currency, []), key=lambda o: o["notional"], reverse=True)
        unbounded = unbounded_by_currency.get(currency, [])
        buy_notional = sum(o["notional"] for o in contributing)

        if bal is None:
            if buy_notional or unbounded:
                raise MissingInputError(
                    f"Currency '{currency}' has active BUY orders but no entry in `balances` "
                    "— cash balance and FX rate are required, never assumed"
                )
            continue

        available_cash = require(bal, "cash_balance", f"balances[{currency}]")
        exchange_rate = require(bal, "exchange_rate", f"balances[{currency}]")

        shortfall = buy_notional - available_cash
        margin_usage = max(0.0, shortfall)
        margin_usage_usd = margin_usage * exchange_rate

        result[currency] = {
            "buy_notional": buy_notional,
            "available_cash": available_cash,
            "shortfall": shortfall,
            "margin_usage": margin_usage,
            "exchange_rate": exchange_rate,
            "margin_usage_usd": margin_usage_usd,
            "contributing_orders": contributing,
            "unbounded_orders": unbounded,
        }
    return result


def total_margin_usage_usd(per_currency: dict) -> float:
    return sum(c["margin_usage_usd"] for c in per_currency.values())


def propose_grouping(per_currency: dict, threshold_usd: float = 5000.0) -> dict:
    """Greedy OCA grouping per safe-guard.md's "Grouping algorithm" section.

    For each breaching currency (largest margin usage first), repeatedly merge the
    next-largest remaining contributing order into the currency's single growing group
    until the grand total (across all currencies) drops to/under the threshold, or every
    contributing order in that currency has been merged into the one group.
    """
    breaching = sorted(
        (c for c, v in per_currency.items() if v["margin_usage_usd"] > 0),
        key=lambda c: per_currency[c]["margin_usage_usd"],
        reverse=True,
    )

    other_total = {c: v["margin_usage_usd"] for c, v in per_currency.items()}
    groups_by_currency: dict[str, list[list[dict]]] = {}
    group_letters = iter("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    unresolved_currencies = []

    def grand_total() -> float:
        return sum(other_total.values())

    for currency in breaching:
        info = per_currency[currency]
        contributing = list(info["contributing_orders"])
        cash = info["available_cash"]
        fx = info["exchange_rate"]

        if len(contributing) < 2:
            # No pair of orders to merge (e.g. a lone or zero contributing order, or a
            # currency whose margin usage comes only from a pre-existing negative cash
            # balance with no order to group) — grouping cannot touch this currency.
            if grand_total() > threshold_usd:
                unresolved_currencies.append(currency)
            continue

        group = [contributing[0], contributing[1]]
        ungrouped = contributing[2:]

        def recompute_usage():
            notional = max(o["notional"] for o in group) + sum(o["notional"] for o in ungrouped)
            return max(0.0, notional - cash) * fx

        other_total[currency] = recompute_usage()

        while grand_total() > threshold_usd and ungrouped:
            group.append(ungrouped.pop(0))
            other_total[currency] = recompute_usage()

        groups_by_currency[currency] = [group]

        if grand_total() > threshold_usd and not ungrouped:
            unresolved_currencies.append(currency)

    letters = {}
    rendered_groups = []
    for currency, groups in groups_by_currency.items():
        for group in groups:
            letter = next(group_letters)
            letters[(currency, id(group))] = letter
            rendered_groups.append(
                {
                    "letter": letter,
                    "currency": currency,
                    "orders": group,
                    "invocation": "+".join(f"{o['ticker']}({o['order_id']})" for o in group),
                }
            )

    return {
        "groups": rendered_groups,
        "recomputed_total_usd": grand_total(),
        "clears_threshold": grand_total() <= threshold_usd,
        "unresolved_currencies": unresolved_currencies,
    }


def render_markdown(per_currency: dict, total_usd: float, threshold_usd: float, grouping: dict | None) -> str:
    lines = ["## Margin Safe-Guard\n"]
    lines.append("| Currency | BUY Notional | Available Cash | Shortfall | Margin Usage (USD) |")
    lines.append("|----------|--------------|-----------------|-----------|---------------------|")
    for currency, v in sorted(per_currency.items()):
        lines.append(
            f"| {currency} | {v['buy_notional']:,.2f} | {v['available_cash']:,.2f} | "
            f"{v['shortfall']:,.2f} | {v['margin_usage_usd']:,.2f} |"
        )
        for order in v["unbounded_orders"]:
            lines.append(
                f"| | *unbounded: {order.get('ticker')} order {order.get('order_id')} — no fixed price* | | | |"
            )
    lines.append("")
    lines.append(f"**Total Potential Margin Usage (USD) = {total_usd:,.2f}**")
    lines.append(f"**Threshold = {threshold_usd:,.2f}**")

    if total_usd <= threshold_usd:
        lines.append(f"\nWithin threshold — {total_usd:,.2f} <= {threshold_usd:,.2f}.")
        return "\n".join(lines)

    lines.append(f"\n**BREACH** — {total_usd:,.2f} > {threshold_usd:,.2f}.")
    if grouping is not None:
        lines.append("\n### Suggested OCA grouping\n")
        invocation_parts = [f"GROUP-{g['letter']}: {g['invocation']}" for g in grouping["groups"]]
        if invocation_parts:
            lines.append("```")
            lines.append("/update-orders " + "; ".join(invocation_parts))
            lines.append("```")
        lines.append(f"\nRecomputed total after grouping: {grouping['recomputed_total_usd']:,.2f}")
        if grouping["clears_threshold"]:
            lines.append("Clears the threshold.")
        else:
            lines.append(
                "Still exceeds the threshold even with every contributing order in one group per "
                f"currency ({', '.join(grouping['unresolved_currencies'])}); grouping alone cannot fix "
                "it — cancelling or reducing the largest order in that currency is the only remaining lever."
            )
    return "\n".join(lines)


def run(data: dict, threshold_usd: float = 5000.0) -> dict:
    orders = require(data, "orders", "input")
    balances = require(data, "balances", "input")
    active_orders = filter_active_orders(orders)
    per_currency = compute_per_currency(active_orders, balances)
    total_usd = total_margin_usage_usd(per_currency)
    breach = total_usd > threshold_usd
    grouping = propose_grouping(per_currency, threshold_usd) if breach else None
    return {
        "per_currency": per_currency,
        "total_margin_usage_usd": total_usd,
        "threshold_usd": threshold_usd,
        "breach": breach,
        "grouping": grouping,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", required=True, help="Path to JSON input file, or '-' for stdin")
    parser.add_argument("--threshold", type=float, default=5000.0)
    parser.add_argument("--json", action="store_true", help="Print raw JSON instead of the markdown block")
    args = parser.parse_args(argv)

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    data = json.loads(raw)

    try:
        result = run(data, threshold_usd=args.threshold)
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print(
            render_markdown(
                result["per_currency"], result["total_margin_usage_usd"], result["threshold_usd"], result["grouping"]
            )
        )
    return 1 if result["breach"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

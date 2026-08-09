#!/usr/bin/env python3
"""
Standalone OCA-regrouping executor for account U19421206.

This is NOT run by Claude and is not wired into any repo routine. It connects
to a TWS / IB Gateway instance YOU are running, under YOUR own logged-in
session, and modifies live orders in place to set an OCA (One-Cancels-All)
group -- the same change /update-orders' manual checklist describes for TWS's
"Attach/Modify Order" dialog, done here via the API instead of by hand.

Requires: pip install ib_insync

Usage:
    python update_orders_execute.py "GROUP-A: V(652254170)+MA(652254171)+NOW(1423738919)"
    python update_orders_execute.py "GROUP-A: ..." --execute --yes

Defaults to a dry run (prints the plan, modifies nothing). Pass --execute to
actually send order modifications, and --yes to skip the interactive
confirmation prompt. Refuses to run --execute while NYSE is in its regular
trading session unless --skip-market-check is also passed.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone

from ib_insync import IB, Stock, Order

GRAMMAR_GROUP = re.compile(r"GROUP-(?P<name>[A-Za-z0-9]+)\s*:\s*(?P<members>[^;]+)")
GRAMMAR_MEMBER = re.compile(r"(?P<ticker>[A-Za-z.]+)\((?P<order_id>\d+)\)")

ACTIVE_STATUSES = {"PendingSubmit", "PreSubmitted", "Submitted", "ApiPending"}


@dataclass
class GroupMember:
    ticker: str
    order_id: int


@dataclass
class Group:
    name: str
    members: list


def parse_grouping(spec: str) -> list:
    groups = []
    for m in GRAMMAR_GROUP.finditer(spec):
        members = [
            GroupMember(ticker=mm.group("ticker").upper(), order_id=int(mm.group("order_id")))
            for mm in GRAMMAR_MEMBER.finditer(m.group("members"))
        ]
        if len(members) < 2:
            raise ValueError(f"GROUP-{m.group('name')} has fewer than 2 members -- not a valid OCA group")
        groups.append(Group(name=m.group("name"), members=members))
    if not groups:
        raise ValueError(f"Could not parse any GROUP-<name>: ... clauses from: {spec!r}")
    return groups


def nyse_is_closed(ib: IB) -> bool:
    """Query IBKR for NYSE's live trading schedule via contract details on a
    NYSE-primary-listed instrument, rather than hardcoding a holiday calendar."""
    contract = Stock("SPY", "SMART", "USD")
    details = ib.reqContractDetails(contract)
    if not details:
        raise RuntimeError("Could not fetch contract details for SPY to determine NYSE trading hours")

    liquid_hours = details[0].liquidHours  # e.g. "20260706:0930-20260706:1600;20260707:0930-..."
    now_et = datetime.now(timezone.utc).astimezone().astimezone(tz=None)
    now_et_str = now_et.strftime("%Y%m%d")

    for session in liquid_hours.split(";"):
        session = session.strip()
        if not session or session.endswith("CLOSED"):
            continue
        day, _, hours = session.partition(":")
        if day != now_et_str:
            continue
        if "-" not in hours:
            continue
        start_str, end_str = hours.split("-")
        start = datetime.strptime(f"{day}{start_str}", "%Y%m%d%H%M").replace(tzinfo=now_et.tzinfo)
        end = datetime.strptime(f"{day}{end_str}", "%Y%m%d%H%M").replace(tzinfo=now_et.tzinfo)
        if start <= now_et <= end:
            return False  # inside a live NYSE session -> NOT closed
    return True


def fetch_active_orders(ib: IB) -> dict:
    ib.reqAllOpenOrders()  # requires clientId=0 (master client) in TWS/Gateway API settings
    # to see orders placed by other client sessions/manually in TWS.
    trades = ib.openTrades()
    by_id = {}
    for t in trades:
        if t.orderStatus.status in ACTIVE_STATUSES:
            by_id[t.order.orderId] = t
    return by_id


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("grouping", help='e.g. "GROUP-A: V(652254170)+MA(652254171)+NOW(1423738919)"')
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=7496, help="7496=TWS live, 7497=TWS paper, 4001=Gateway live, 4002=Gateway paper")
    parser.add_argument("--client-id", type=int, default=0, help="0 = master client, required to manage orders placed by other sessions")
    parser.add_argument("--account", default="U19421206")
    parser.add_argument("--execute", action="store_true", help="Actually send order modifications. Default is dry-run.")
    parser.add_argument("--yes", action="store_true", help="Skip the interactive confirmation prompt.")
    parser.add_argument("--skip-market-check", action="store_true", help="Bypass the NYSE-closed guard (e.g. for paper-account testing).")
    args = parser.parse_args()

    groups = parse_grouping(args.grouping)

    ib = IB()
    ib.connect(args.host, args.port, clientId=args.client_id)

    try:
        if args.execute and not args.skip_market_check:
            if not nyse_is_closed(ib):
                print("REFUSING: NYSE is currently in its regular trading session. "
                      "Re-run after close, or pass --skip-market-check if you accept the risk "
                      "of a live order changing state mid-modification.", file=sys.stderr)
                sys.exit(1)

        active = fetch_active_orders(ib)

        plan = []
        for group in groups:
            resolved = []
            for member in group.members:
                trade = active.get(member.order_id)
                if trade is None:
                    print(f"STOP: order {member.order_id} ({member.ticker}) in GROUP-{group.name} "
                          f"is not an active order (filled/cancelled/replaced, or not visible to this "
                          f"API session -- check clientId=0 / master client is enabled). Aborting.",
                          file=sys.stderr)
                    sys.exit(1)
                live_ticker = trade.contract.symbol.upper()
                if live_ticker != member.ticker:
                    print(f"STOP: order {member.order_id} is live but for {live_ticker}, "
                          f"not {member.ticker} as specified. Aborting -- ticker/order-ID mismatch.",
                          file=sys.stderr)
                    sys.exit(1)
                if trade.order.action != "BUY":
                    print(f"STOP: order {member.order_id} ({member.ticker}) is a {trade.order.action} order, "
                          f"not BUY. This tool only groups BUY orders per the safe-guard worst-case model. "
                          f"Aborting.", file=sys.stderr)
                    sys.exit(1)
                resolved.append(trade)

            oca_group_name = f"SAFEGUARD-{datetime.now().strftime('%Y-%m-%d')}-{group.name}"
            plan.append((oca_group_name, resolved))

        print("Plan:")
        for oca_group_name, trades in plan:
            for t in trades:
                print(f"  order {t.order.orderId} ({t.contract.symbol}, "
                      f"{t.order.totalQuantity}@{t.order.lmtPrice}) "
                      f"-> ocaGroup={oca_group_name!r}, ocaType=1")

        if not args.execute:
            print("\nDry run only -- no order was modified. Pass --execute to apply.")
            return

        if not args.yes:
            confirm = input(f"\nModify {sum(len(t) for _, t in plan)} live orders on account "
                             f"{args.account} as shown above? Type YES to proceed: ")
            if confirm.strip() != "YES":
                print("Aborted by user.")
                return

        for oca_group_name, trades in plan:
            for t in trades:
                t.order.ocaGroup = oca_group_name
                t.order.ocaType = 1  # Cancel Block: partial fill reduces siblings' qty rather than cancelling them
                ib.placeOrder(t.contract, t.order)  # same orderId => modify in place, not a new order
                print(f"Modified order {t.order.orderId}: ocaGroup={oca_group_name}")

        ib.sleep(1)
        print("\nDone. Verify the new OCA group in TWS/Client Portal's Orders pane, "
              "then re-run /safe-guard to confirm worst-case exposure actually dropped.")

    finally:
        ib.disconnect()


if __name__ == "__main__":
    main()

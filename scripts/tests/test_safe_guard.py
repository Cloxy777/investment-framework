import pytest

from scripts.safe_guard import compute_per_currency, filter_active_orders, propose_grouping, run
from scripts.scoring.common import MissingInputError

# Worked example: sessions/2026-07-05-safe-guard.md
WORKED_ORDERS = [
    {"order_id": 652254170, "side": "BUY", "ticker": "V", "qty": 9, "price": 285.20, "currency": "USD", "status": "NEW"},
    {"order_id": 652254171, "side": "BUY", "ticker": "MA", "qty": 4, "price": 464.00, "currency": "USD", "status": "NEW"},
    {"order_id": 1423738919, "side": "BUY", "ticker": "NOW", "qty": 20, "price": 80.00, "currency": "USD", "status": "NEW"},
    {"order_id": 1150965513, "side": "BUY", "ticker": "PDD", "qty": 10, "price": 72.55, "currency": "USD", "status": "NEW"},
    {"order_id": 21429034, "side": "BUY", "ticker": "META", "qty": 1, "price": 579.85, "currency": "USD", "status": "NEW"},
    {"order_id": 21429036, "side": "BUY", "ticker": "META", "qty": 1, "price": 550.84, "currency": "USD", "status": "NEW"},
    # excluded: non-active statuses
    {"order_id": 1, "side": "SELL", "ticker": "CSGP", "qty": 25, "price": 30.0, "currency": "USD", "status": "REPLACED"},
    {"order_id": 2, "side": "BUY", "ticker": "TLT", "qty": 100, "price": 87.0, "currency": "USD", "status": "REPLACED"},
    {"order_id": 3, "side": "SELL", "ticker": "NKE", "qty": 20, "price": 54.2, "currency": "USD", "status": "NEW"},
    # Note: the real 2026-07-05 session also saw an RGL order in status PENDING_CANCEL_REPLACE
    # and an HDSN order in PENDING_NEW — both unfamiliar statuses the session resolved by
    # asking the user (excluded manually). This script hard-fails on an unfamiliar status
    # instead (see test_unfamiliar_status_raises) rather than silently excluding it, so
    # they're left out of this fixture, which reproduces only the already-resolved orders.
]

WORKED_BALANCES = {
    "USD": {"cash_balance": 103.69, "exchange_rate": 1.0},
    "AUD": {"cash_balance": -31.07, "exchange_rate": 0.6938792},
    "EUR": {"cash_balance": 227.49, "exchange_rate": 1.1485799},
    "GBP": {"cash_balance": 0.28, "exchange_rate": 1.3395958},
}


def test_worked_example_excludes_non_active_statuses():
    active = filter_active_orders(WORKED_ORDERS)
    tickers = {o["ticker"] for o in active}
    # NKE stays in the active-orders set (status NEW) but is a SELL, so compute_per_currency
    # excludes it from the BUY-only worst-case notional per Step 3.
    assert tickers == {"V", "MA", "NOW", "PDD", "META", "NKE"}
    assert "TLT" not in tickers  # REPLACED, excluded per Step 1
    assert "CSGP" not in tickers  # REPLACED, excluded per Step 1


def test_unfamiliar_status_raises():
    orders = [{"order_id": 1, "side": "BUY", "ticker": "X", "qty": 1, "price": 1.0, "currency": "USD", "status": "WEIRD"}]
    with pytest.raises(MissingInputError, match="Unfamiliar order status"):
        filter_active_orders(orders)


def test_worked_example_per_currency_usd_shortfall():
    active = filter_active_orders(WORKED_ORDERS)
    per_currency = compute_per_currency(active, WORKED_BALANCES)
    usd = per_currency["USD"]
    assert usd["buy_notional"] == pytest.approx(7878.99)
    assert usd["margin_usage_usd"] == pytest.approx(7775.30, abs=0.01)


def test_worked_example_aud_pre_existing_negative_cash_counts():
    active = filter_active_orders(WORKED_ORDERS)
    per_currency = compute_per_currency(active, WORKED_BALANCES)
    aud = per_currency["AUD"]
    # No AUD BUY orders in this fixture — margin usage comes entirely from the pre-existing
    # negative cash balance, exactly like the session log's AUD line.
    assert aud["buy_notional"] == 0
    assert aud["margin_usage_usd"] == pytest.approx(21.56, abs=0.01)


def test_worked_example_total_matches_session_log():
    result = run({"orders": WORKED_ORDERS, "balances": WORKED_BALANCES})
    assert result["total_margin_usage_usd"] == pytest.approx(7796.86, abs=0.01)
    assert result["breach"] is True


def test_worked_example_grouping_matches_session_log():
    result = run({"orders": WORKED_ORDERS, "balances": WORKED_BALANCES})
    grouping = result["grouping"]
    assert len(grouping["groups"]) == 1
    group = grouping["groups"][0]
    assert group["invocation"] == "V(652254170)+MA(652254171)+NOW(1423738919)"
    assert grouping["recomputed_total_usd"] == pytest.approx(4340.86, abs=0.01)
    assert grouping["clears_threshold"] is True


def test_threshold_boundary_pass_at_exactly_5000():
    orders = [{"order_id": 1, "side": "BUY", "ticker": "X", "qty": 1, "price": 5000.00, "currency": "USD", "status": "NEW"}]
    balances = {"USD": {"cash_balance": 0.0, "exchange_rate": 1.0}}
    result = run({"orders": orders, "balances": balances})
    assert result["total_margin_usage_usd"] == pytest.approx(5000.00)
    assert result["breach"] is False


def test_threshold_boundary_breach_at_5000_01():
    orders = [{"order_id": 1, "side": "BUY", "ticker": "X", "qty": 1, "price": 5000.01, "currency": "USD", "status": "NEW"}]
    balances = {"USD": {"cash_balance": 0.0, "exchange_rate": 1.0}}
    result = run({"orders": orders, "balances": balances})
    assert result["total_margin_usage_usd"] == pytest.approx(5000.01)
    assert result["breach"] is True


def test_unbounded_market_order_excluded_not_invented():
    orders = [
        {"order_id": 1, "side": "BUY", "ticker": "X", "qty": 1, "price": None, "currency": "USD", "status": "NEW"},
    ]
    balances = {"USD": {"cash_balance": 0.0, "exchange_rate": 1.0}}
    active = filter_active_orders(orders)
    per_currency = compute_per_currency(active, balances)
    assert per_currency["USD"]["buy_notional"] == 0
    assert len(per_currency["USD"]["unbounded_orders"]) == 1


def test_missing_fx_rate_hard_fails():
    orders = [{"order_id": 1, "side": "BUY", "ticker": "X", "qty": 1, "price": 100.0, "currency": "JPY", "status": "NEW"}]
    with pytest.raises(MissingInputError, match="JPY"):
        compute_per_currency(orders, {})


def test_grouping_alone_insufficient_flags_it():
    orders = [
        {"order_id": 1, "side": "BUY", "ticker": "A", "qty": 1, "price": 8000.0, "currency": "USD", "status": "NEW"},
        {"order_id": 2, "side": "BUY", "ticker": "B", "qty": 1, "price": 7000.0, "currency": "USD", "status": "NEW"},
    ]
    balances = {"USD": {"cash_balance": 0.0, "exchange_rate": 1.0}}
    result = run({"orders": orders, "balances": balances})
    assert result["breach"] is True
    assert result["grouping"]["clears_threshold"] is False
    assert "USD" in result["grouping"]["unresolved_currencies"]

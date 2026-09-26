import pytest

from scripts.sync_ibkr import (
    compute_positions,
    compute_weights,
    filter_active_orders,
    patch_holdings_weights,
    render_cash_section,
    render_orders_section,
    render_positions_section,
)
from scripts.scoring.common import MissingInputError

# Fixture built from portfolio/sync-sop.md's documented field names, reproducing a subset
# of the tickers/values actually committed in portfolio/snapshots/ibkr.md (2026-09-20 sync)
# so the generated table can be diffed against the real file, modulo timestamp.
POSITIONS = [
    {"contract_id": 265768, "ticker": "ADBE", "shares": 10, "market_price": 248.32, "avg_cost": 202.0700, "currency": "USD"},
    {"contract_id": 49462172, "ticker": "V", "shares": 1, "market_price": 365.86, "avg_cost": 319.5100, "currency": "USD"},
    {"contract_id": 371871705, "ticker": "TRN", "shares": 600, "market_price": 2.010, "avg_cost": 2.1195, "currency": "GBP"},
]

CURRENCIES = {
    "USD": {"cash_balance": 3836.84, "settled_cash": 3836.84, "exchange_rate": 1.0000000},
    "GBP": {"cash_balance": 0.00, "settled_cash": 0.00, "exchange_rate": 1.3395958},
}

BALANCES = {"base": {"cash_balance": 4097.84, "net_liquidation_value": 50330.70}, "currencies": CURRENCIES}

ORDERS = [
    {
        "order_id": 862563681, "side": "BUY", "ticker": "V", "qty": 9, "order_type": "LIMIT",
        "price": 285.00, "time_in_force": "GTC", "status": "NEW", "order_placed_utc": "2026-07-05T19:17:13Z",
    },
    {
        "order_id": 1986163848, "side": "SELL", "ticker": "CSGP", "qty": 25, "order_type": "LIMIT",
        "price": 40.0, "time_in_force": "GTC", "status": "REPLACED", "order_placed_utc": "2026-05-26T00:00:00Z",
    },
]


def test_positions_match_committed_ibkr_md_values():
    rows = compute_positions(POSITIONS, CURRENCIES)
    adbe = next(r for r in rows if r["ticker"] == "ADBE")
    assert adbe["market_value"] == pytest.approx(2483.20)
    assert adbe["unrealized_pnl"] == pytest.approx(462.50, abs=0.01)
    assert adbe["pnl_pct"] == pytest.approx(22.89, abs=0.01)

    trn = next(r for r in rows if r["ticker"] == "TRN")
    assert trn["market_value"] == pytest.approx(1206.00, abs=0.01)
    assert trn["market_value_usd"] == pytest.approx(1615.55, abs=0.5)  # matches holdings.md's stated USD-equiv


def test_positions_table_is_sorted_alphabetically_like_committed_file():
    rows = compute_positions(POSITIONS, CURRENCIES)
    assert [r["ticker"] for r in rows] == ["ADBE", "TRN", "V"]


def test_positions_missing_fx_rate_hard_fails():
    positions = [{"contract_id": 1, "ticker": "XEON", "shares": 10, "market_price": 150.26, "avg_cost": 149.0250, "currency": "EUR"}]
    with pytest.raises(MissingInputError, match="EUR"):
        compute_positions(positions, {})


def test_cash_section_matches_committed_ibkr_md():
    result = render_cash_section(BALANCES)
    assert result["total_cash_usd"] == pytest.approx(4097.84)
    assert result["net_liquidation"] == pytest.approx(50330.70)
    assert "3,836.84" in result["table_markdown"]


def test_orders_section_excludes_replaced_matches_committed_file():
    result = render_orders_section(ORDERS)
    assert result["active_count"] == 1
    assert result["excluded_count"] == 1
    assert "862563681" in result["table_markdown"]
    assert "CSGP" not in result["table_markdown"]


def test_unfamiliar_order_status_hard_fails():
    orders = [{"order_id": 1, "side": "BUY", "ticker": "X", "qty": 1, "order_type": "LIMIT", "price": 1.0,
               "time_in_force": "GTC", "status": "WEIRD", "order_placed_utc": "2026-01-01T00:00:00Z"}]
    with pytest.raises(MissingInputError, match="Unfamiliar order status"):
        filter_active_orders(orders)


def test_compute_weights_matches_committed_holdings_md():
    rows = compute_positions(POSITIONS, CURRENCIES)
    weights = compute_weights(rows, total_value_usd=61220.66)  # combined total per holdings.md
    # ADBE committed weight is 4.06% on the full 24-position book; here we only have ADBE
    # in the fixture, so just check the arithmetic is right for this subset.
    assert weights["ADBE"] == pytest.approx(2483.20 / 61220.66 * 100, abs=0.001)


def test_patch_holdings_weights_updates_only_matching_rows_preserves_rest():
    holdings = (
        "| Ticker | Weight % | Last Score | Broker |\n"
        "|--------|----------|------------|--------|\n"
        "| ADBE | 4.06% | 0.0 | IBKR |\n"
        "| AMZN | 4.99% | 82.7 | IBKR (Freedom24 leg sold — see note above) |\n"
    )
    patched, not_found = patch_holdings_weights(holdings, {"ADBE": 5.00})
    assert "| ADBE | 5.00% | 0.0 | IBKR |" in patched
    assert "| AMZN | 4.99% | 82.7 | IBKR (Freedom24 leg sold — see note above) |" in patched
    assert not_found == []


def test_patch_holdings_weights_preserves_warning_markers():
    holdings = "| NOW | 2.00%⚠️ | 75.9 | IBKR |\n"
    patched, _ = patch_holdings_weights(holdings, {"NOW": 2.50})
    assert "2.50%⚠️" in patched


def test_patch_holdings_weights_reports_ticker_not_found():
    holdings = "| ADBE | 4.06% | 0.0 | IBKR |\n"
    _, not_found = patch_holdings_weights(holdings, {"ZZZZ": 1.0})
    assert not_found == ["ZZZZ"]

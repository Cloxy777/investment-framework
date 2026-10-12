import datetime as dt

import pytest

from scripts.performance import (
    LEDGER_FILE, NAV_FILE, PERF_DIR, PRICES_FILE, _sub_months, chain, excluded_series, framework_daily,
    ingest_pa, load_ledger, load_nav, load_prices, window_stats,
)

D = dt.date
PX = {D(2026, 1, d): {"TLT": 100.0, "RGL": 0.01, "LM8": 0.3, "AUD": 0.5} for d in range(1, 8)}


def navrow(d, nav, ret=0.0, flow=0.0):
    return {"date": D(2026, 1, d), "nav": nav, "ret": ret, "flow": flow}


def test_excluded_sleeve_does_not_move_framework_return():
    # framework sleeve 1000 -> 1010 (+1%); TLT 10 sh @100 constant = 1000. NAV = 2000 -> 2010.
    nav = [navrow(1, 2000), navrow(2, 2010, 0.005)]
    ledger = [{"date": D(2026, 1, 1), "ticker": "TLT", "action": "open", "qty": 10, "price": None, "ccy": "USD", "commission": 0}]
    rows = framework_daily(nav, ledger, PX)
    assert rows[1]["ret"] == pytest.approx(0.01)
    assert rows[1]["pa_ret"] == pytest.approx(0.005)


def test_buy_of_excluded_position_is_not_a_framework_loss():
    # day 2: framework cash 500 buys 5 TLT @100 -> NAV unchanged, framework sleeve shrinks by 500 with zero return
    nav = [navrow(1, 1500), navrow(2, 1500)]
    ledger = [
        {"date": D(2026, 1, 1), "ticker": "TLT", "action": "open", "qty": 5, "price": None, "ccy": "USD", "commission": 0},
        {"date": D(2026, 1, 2), "ticker": "TLT", "action": "buy", "qty": 5, "price": 100.0, "ccy": "USD", "commission": 0},
    ]
    rows = framework_daily(nav, ledger, PX)
    assert rows[1]["ret"] == pytest.approx(0.0)
    assert rows[1]["framework"] == pytest.approx(500.0)


def test_transfer_out_has_no_framework_effect():
    # day 2: TLT (1000) leaves the account; PA records a -1000 flow
    nav = [navrow(1, 2000), navrow(2, 1000, 0.0, -1000.0)]
    ledger = [
        {"date": D(2026, 1, 1), "ticker": "TLT", "action": "open", "qty": 10, "price": None, "ccy": "USD", "commission": 0},
        {"date": D(2026, 1, 2), "ticker": "TLT", "action": "transfer_out", "qty": 10, "price": None, "ccy": "USD", "commission": 0},
    ]
    rows = framework_daily(nav, ledger, PX)
    assert rows[1]["ret"] == pytest.approx(0.0)
    assert rows[1]["excluded"] == 0


def test_inconsistent_transfer_quantity_raises():
    nav = [navrow(1, 2000), navrow(2, 1000)]
    ledger = [
        {"date": D(2026, 1, 1), "ticker": "TLT", "action": "open", "qty": 10, "price": None, "ccy": "USD", "commission": 0},
        {"date": D(2026, 1, 2), "ticker": "TLT", "action": "transfer_out", "qty": 9, "price": None, "ccy": "USD", "commission": 0},
    ]
    with pytest.raises(ValueError, match="ledger inconsistent"):
        excluded_series(nav, ledger, PX)


def test_excluded_income_is_removed_from_framework_value():
    nav = [navrow(1, 2000), navrow(2, 2050, 0.025)]  # +50 dividend cash arrives
    ledger = [{"date": D(2026, 1, 1), "ticker": "TLT", "action": "open", "qty": 10, "price": None, "ccy": "USD", "commission": 0}]
    rows = framework_daily(nav, ledger, PX, income=[{"date": D(2026, 1, 2), "usd": 50.0}])
    assert rows[1]["ret"] == pytest.approx(0.0)


def test_window_stats_chain_and_clamp():
    rows = [{"date": D(2026, 1, d), "ret": None if d == 1 else 0.01, "pa_ret": None if d == 1 else 0.02} for d in range(1, 6)]
    s = window_stats(rows, D(2026, 1, 1), D(2026, 1, 5))
    assert s["framework"] == pytest.approx(chain([0.01] * 4))
    assert s["reported"] == pytest.approx(chain([0.02] * 4))
    assert window_stats(rows, D(2025, 6, 1), D(2026, 1, 5)) is None  # way before history
    assert window_stats(rows, D(2025, 12, 28), D(2026, 1, 5))["clamped"]


def test_sub_months_clamps_day():
    assert _sub_months(D(2026, 3, 31), 1) == D(2026, 2, 28)
    assert _sub_months(D(2026, 1, 15), 12) == D(2025, 1, 15)


def test_ingest_adds_new_days_and_rejects_gap():
    rows = [navrow(1, 1000), navrow(2, 1010, 0.01)]
    rows[0]["date"], rows[1]["date"] = D(2026, 1, 1), D(2026, 1, 2)
    period = {"start_date": "20260102", "start_nav": 1010.0, "dates": ["20260105"], "nav": [1020.1], "cps": [0.01]}
    added, updated = ingest_pa(period, rows)
    assert (added, updated) == (1, 0)
    assert rows[-1]["ret"] == pytest.approx(0.01)
    gap = {"start_date": "20260120", "start_nav": 1.0, "dates": ["20260121"], "nav": [1.0], "cps": [0.0]}
    with pytest.raises(ValueError, match="gap"):
        ingest_pa(gap, rows)


def test_real_data_transfer_day_reconciles():
    nav = load_nav(PERF_DIR / NAV_FILE)
    rows = framework_daily(nav, load_ledger(PERF_DIR / LEDGER_FILE), load_prices(PERF_DIR / PRICES_FILE))
    day = next(r for r in rows if r["date"] == D(2026, 10, 12))
    # PA's withdrawal must match the ledger's market value of the three transferred positions (within ~$10)
    assert abs(day["pa_flow"] - day["x"]) < 10
    assert day["excluded"] == 0


def test_status_fresh_and_stale_period_choice():
    from scripts.performance import latest_weekday, parse_inline, status
    nav = [navrow(5, 1000)]
    nav[0]["date"] = D(2026, 10, 12)  # Monday
    assert not status(nav, D(2026, 10, 12))["stale"]
    assert not status(nav, D(2026, 10, 11))["stale"]  # Sunday -> latest weekday is Friday 10-09, already covered
    st = status(nav, D(2026, 10, 14))
    assert st["stale"] and st["period"] == "7D"
    assert status(nav, D(2026, 10, 30))["period"] == "MTD"
    assert status(nav, D(2027, 3, 1))["period"] == "1Y"
    assert latest_weekday(D(2026, 10, 10)) == D(2026, 10, 9)
    p = parse_inline("20261009@57230.18 20261012:48694.41:0.00025465")
    assert p["dates"] == ["20261012"] and p["nav"] == [48694.41] and p["start_nav"] == 57230.18


def test_run_inline_roundtrip(tmp_path):
    import shutil
    from scripts.performance import main
    shutil.copytree(PERF_DIR, tmp_path / "p")
    rc = main(["run", "--dir", str(tmp_path / "p"), "--inline", "20261012@48694.41 20261013:48800.00:0.0021"])
    assert rc == 0
    latest = (tmp_path / "p" / "latest.md").read_text(encoding="utf-8")
    assert "2026-10-13" in latest and "## Glossary" in latest and "NOT FOUND" not in latest

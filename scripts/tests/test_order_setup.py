import pytest

from scripts.scoring.order_setup import NoOrderSetup, compute


def test_nvda_2026_09_17_rescore_session_order_setup():
    """Cross-check against sessions/2026-09-17-rescore-nvda.md section 10."""
    d = {
        "score": 23.0,
        "fair_value": 322.64,
        "bull_fair_value": 432.00,
        "live_price": 218.70,
        "margin_of_safety_pct": 17.5,
        "max_loss_pct": 22.5,
        "portfolio_value": 61192.89,
        "risk_pct": 1.5,
        "max_position_pct": 8,
        "current_shares": 19,
    }
    result = compute(d)
    assert result["buy_price"] == pytest.approx(266.18, abs=0.05)
    assert result["stop_loss"] == pytest.approx(169.49, abs=0.05)
    assert result["rr_ratio"] == pytest.approx(2.112, abs=0.01)
    assert result["rr_fails"] is False
    assert result["shares_by_risk"] == pytest.approx(18.66, abs=0.05)
    assert result["shares_by_cap"] == pytest.approx(22.38, abs=0.05)
    assert result["binding_constraint"] == "risk-based sizing"
    assert result["final_shares"] == pytest.approx(result["shares_by_risk"], abs=0.001)


def test_rr_below_2_to_1_is_flagged_not_silently_passed():
    d = {
        "score": 20.0,
        "fair_value": 110.0,
        "bull_fair_value": 130.0,
        "live_price": 100.0,
        "margin_of_safety_pct": 17.5,
        "max_loss_pct": 22.5,
        "portfolio_value": 10000.0,
        "risk_pct": 1.5,
        "max_position_pct": 7,
        "current_shares": 0,
    }
    result = compute(d)
    assert result["rr_ratio"] < 2.0
    assert result["rr_fails"] is True


def test_score_in_watchlist_band_refuses_order_setup():
    d = {"score": 55.0, "fair_value": 100, "bull_fair_value": 120, "live_price": 90, "margin_of_safety_pct": 17.5,
         "max_loss_pct": 22.5, "portfolio_value": 10000, "risk_pct": 1.5, "max_position_pct": 7}
    with pytest.raises(NoOrderSetup):
        compute(d)


def test_score_in_trim_band_refuses_order_setup():
    d = {"score": 80.0, "fair_value": 100, "bull_fair_value": 120, "live_price": 90, "margin_of_safety_pct": 17.5,
         "max_loss_pct": 22.5, "portfolio_value": 10000, "risk_pct": 1.5, "max_position_pct": 7}
    with pytest.raises(NoOrderSetup):
        compute(d)


def test_out_of_band_margin_of_safety_raises():
    from scripts.scoring.common import MissingInputError

    d = {
        "score": 20.0,
        "fair_value": 100,
        "bull_fair_value": 120,
        "live_price": 90,
        "margin_of_safety_pct": 30,  # out of the 15-20 range for the 0.0-29.9 band
        "max_loss_pct": 22.5,
        "portfolio_value": 10000,
        "risk_pct": 1.5,
        "max_position_pct": 7,
    }
    with pytest.raises(MissingInputError):
        compute(d)

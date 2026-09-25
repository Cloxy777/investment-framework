import pytest

from scripts.scoring.common import MissingInputError
from scripts.scoring.valuation_score import _upside_downside, compute


def test_upside_downside_worked_example_valuation_scoring_md():
    """framework/valuation-scoring.md Upside/Downside worked example:
    raw score 54, E = +24%, Modifier = -14.0, final score 40.0.
    """
    d = {
        "bull_fair_value": 118,
        "base_fair_value": 118,
        "bear_fair_value": 118,  # PW FV given directly as $118 in the worked example
        "live_price": 100,
        "catalyst_within_18_24_months": True,
        "catalyst_window_years": 2,
        "intrinsic_growth_pct": 14,
        "dividend_yield_pct": 1,
        "net_buyback_yield_pct": 0,
    }
    modifier, _steps = _upside_downside(d)
    assert modifier == pytest.approx(-14.0, abs=0.01)

    raw_score = 54
    assert raw_score + modifier == pytest.approx(40.0, abs=0.01)


def test_nvda_2026_09_17_rescore_session():
    """Cross-check against sessions/2026-09-17-rescore-nvda.md section 7/8/9: Valuation Score 36.2."""
    d = {
        "fcf_yield_pct": 2.4096,
        "ev_ebit": 26.560,
        "fast_grower": True,
        "peg": 0.2001,
        "forward_pe": 13.930,
        "pe_mode": "avg",
        "pe_5yr_avg": 57.84,
        "treasury_10y_pct": 4.95,
        "live_price": 218.70,
        "bull_fair_value": 432.00,
        "base_fair_value": 329.70,
        "bear_fair_value": 176.00,
        "catalyst_within_18_24_months": True,
        "catalyst_window_years": 2,
        "intrinsic_growth_pct": 10.0,
        "dividend_yield_pct": 0.4572,
        "net_buyback_yield_pct": 1.007,
    }
    result = compute(d)
    assert result["valuation_score"] == pytest.approx(36.2, abs=0.1)


def test_avgo_2026_09_15_rescore_session():
    """Cross-check against sessions/2026-09-15-rescore-avgo.md section 5/6/7: Valuation Score 70.9."""
    d = {
        "fcf_yield_pct": 2.333,
        "ev_ebit": 40.27,
        "fast_grower": False,
        "forward_pe": 17.8266,
        "pe_mode": "range",
        "pe_5yr_low": 13.3897,
        "pe_5yr_high": 52.8544,
        "pe_5yr_avg": 29.9465,
        "treasury_10y_pct": 5.018,
        "live_price": 345.55,
        "bull_fair_value": 724.96,
        "base_fair_value": 484.60,
        "bear_fair_value": 247.15,
        "catalyst_within_18_24_months": True,
        "catalyst_window_years": 1.24,
        "intrinsic_growth_pct": 12.0,
        "dividend_yield_pct": 0.75,
        "net_buyback_yield_pct": 0,
    }
    result = compute(d)
    assert result["valuation_score"] == pytest.approx(70.9, abs=0.1)


def test_pe_deviation_undocumented_band_raises():
    """framework/strategy.md's Upgrade 2 table leaves the 10-20% deviation band undefined —
    the script must flag this rather than guess a modifier.
    """
    d = {
        "fcf_yield_pct": 5,
        "ev_ebit": 15,
        "fast_grower": False,
        "forward_pe": 22,
        "pe_mode": "range",
        "pe_5yr_low": 10,
        "pe_5yr_high": 30,
        "pe_5yr_avg": 20,  # deviation = +10.0%... use a value strictly inside (10, 20)
        "treasury_10y_pct": 3.0,
        "live_price": 100,
        "bull_fair_value": 120,
        "base_fair_value": 110,
        "bear_fair_value": 90,
        "catalyst_within_18_24_months": True,
        "catalyst_window_years": 2,
        "intrinsic_growth_pct": 5,
        "dividend_yield_pct": 0,
        "net_buyback_yield_pct": 0,
    }
    d["pe_5yr_avg"] = 18.5  # (22 - 18.5)/18.5 = ~18.9% -> inside the undocumented (10, 20) band
    with pytest.raises(MissingInputError):
        compute(d)


def test_peg_not_applicable_redistributes_weight_to_ev_ebit():
    d = {
        "fcf_yield_pct": 5,
        "ev_ebit": 20,
        "fast_grower": False,
        "forward_pe": 15,
        "pe_mode": "none",
        "treasury_10y_pct": 3.0,
        "live_price": 100,
        "bull_fair_value": 100,
        "base_fair_value": 100,
        "bear_fair_value": 100,
        "catalyst_within_18_24_months": True,
        "catalyst_window_years": 2,
        "intrinsic_growth_pct": 0,
        "dividend_yield_pct": 0,
        "net_buyback_yield_pct": 0,
    }
    result = compute(d)
    assert result["weights"]["ev_ebit"] == 0.40
    assert result["weights"]["peg"] == 0.0

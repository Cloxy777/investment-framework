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
        "buyback_yield_pct": 0, "buyback_yield_basis": "gross_cash",
    }
    modifier, _steps = _upside_downside(d)
    assert modifier == pytest.approx(-14.0, abs=0.01)

    raw_score = 54
    assert raw_score + modifier == pytest.approx(40.0, abs=0.01)


def test_nvda_2026_09_17_rescore_session():
    """Cross-check against sessions/2026-09-17-rescore-nvda.md section 7/8/9: Valuation Score 36.2."""
    d = {
        "fcf_yield_pct": 2.4096, "sbc_yield_pct": 0,
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
        "buyback_yield_pct": 1.007, "buyback_yield_basis": "gross_cash",
    }
    result = compute(d)
    assert result["valuation_score"] == pytest.approx(36.2, abs=0.1)


def test_avgo_2026_09_15_rescore_session():
    """Cross-check against sessions/2026-09-15-rescore-avgo.md section 5/6/7: Valuation Score 70.9."""
    d = {
        "fcf_yield_pct": 2.333, "sbc_yield_pct": 0,
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
        "buyback_yield_pct": 0, "buyback_yield_basis": "gross_cash",
    }
    result = compute(d)
    assert result["valuation_score"] == pytest.approx(70.9, abs=0.1)


def test_pe_deviation_undocumented_band_raises():
    """framework/strategy.md's Upgrade 2 table leaves the 10-20% deviation band undefined —
    the script must flag this rather than guess a modifier.
    """
    d = {
        "fcf_yield_pct": 5, "sbc_yield_pct": 0,
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
        "buyback_yield_pct": 0, "buyback_yield_basis": "gross_cash",
    }
    d["pe_5yr_avg"] = 18.5  # (22 - 18.5)/18.5 = ~18.9% -> inside the undocumented (10, 20) band
    with pytest.raises(MissingInputError):
        compute(d)


def test_peg_not_applicable_redistributes_weight_to_ev_ebit():
    d = {
        "fcf_yield_pct": 5, "sbc_yield_pct": 0,
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
        "buyback_yield_pct": 0, "buyback_yield_basis": "gross_cash",
    }
    result = compute(d)
    assert result["weights"]["ev_ebit"] == 0.40
    assert result["weights"]["peg"] == 0.0


# --- SBC treatment (methodology 2026-10-12) ---


def test_fcf_score_deducts_sbc_yield():
    from scripts.scoring.valuation_score import _fcf_yield

    # DUOL-like: reported 5.75%, SBC 2.09% -> 3.66% -> 100x(1 - 0.366) = 63.4
    score, steps = _fcf_yield({"fcf_yield_pct": 5.75, "sbc_yield_pct": 2.09})
    assert score == pytest.approx(63.4, abs=0.01)
    assert any("after SBC" in s for s in steps)
    # sbc exceeds fcf yield -> negative adjusted yield -> clamped at 100
    assert _fcf_yield({"fcf_yield_pct": 1.0, "sbc_yield_pct": 3.0})[0] == 100.0


def test_owner_earnings_names_are_not_double_penalised():
    from scripts.scoring.valuation_score import _fcf_yield

    plain, _ = _fcf_yield({"fcf_yield_pct": 2.4, "sbc_yield_pct": 0})
    oe, steps = _fcf_yield({"fcf_yield_pct": 2.4, "owner_earnings_used": True})
    assert oe == pytest.approx(plain)
    assert any("Owner Earnings" in s for s in steps)


def test_missing_or_negative_sbc_yield_stops():
    from scripts.scoring.valuation_score import _fcf_yield

    with pytest.raises(MissingInputError):
        _fcf_yield({"fcf_yield_pct": 5})
    with pytest.raises(MissingInputError):
        _fcf_yield({"fcf_yield_pct": 5, "sbc_yield_pct": -1})


def _ud(**over):
    d = {
        "bull_fair_value": 118, "base_fair_value": 118, "bear_fair_value": 118, "live_price": 100,
        "catalyst_within_18_24_months": True, "catalyst_window_years": 2, "intrinsic_growth_pct": 14,
        "dividend_yield_pct": 1, "buyback_yield_pct": 0, "buyback_yield_basis": "gross_cash",
    }
    d.update(over)
    return d


def test_legacy_net_buyback_key_is_refused():
    d = _ud()
    del d["buyback_yield_pct"]
    d["net_buyback_yield_pct"] = 1.0
    with pytest.raises(MissingInputError, match="replaced by"):
        _upside_downside(d)


def test_buyback_basis_must_be_gross_cash():
    with pytest.raises(MissingInputError, match="gross_cash"):
        _upside_downside(_ud(buyback_yield_basis="net_of_issuance"))
    d = _ud()
    del d["buyback_yield_basis"]
    with pytest.raises(MissingInputError):
        _upside_downside(d)

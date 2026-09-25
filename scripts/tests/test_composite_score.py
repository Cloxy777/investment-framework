import pytest

from scripts.scoring.composite_score import GateFailure, compute


def test_worked_example_valuation_scoring_md_company_a():
    result = compute({"quality_score": 88.0, "valuation_score": 35.0})
    assert result["composite_score"] == pytest.approx(23.5, abs=0.01)


def test_worked_example_valuation_scoring_md_company_c():
    result = compute({"quality_score": 84.0, "valuation_score": 28.0})
    assert result["composite_score"] == pytest.approx(22.0, abs=0.01)


def test_company_b_fails_gate_never_reaches_composite():
    with pytest.raises(GateFailure):
        compute({"quality_score": 72.0, "valuation_score": 10.0})


def test_nvda_2026_09_17_rescore_session():
    """Cross-check against sessions/2026-09-17-rescore-nvda.md section 9: Composite Score 23.0."""
    result = compute({"quality_score": 90.3, "valuation_score": 36.2})
    assert result["composite_score"] == pytest.approx(23.0, abs=0.05)


def test_avgo_2026_09_15_rescore_session():
    """Cross-check against sessions/2026-09-15-rescore-avgo.md section 8: Composite Score 42.3."""
    result = compute({"quality_score": 86.3, "valuation_score": 70.9})
    assert result["composite_score"] == pytest.approx(42.3, abs=0.05)


def test_compute_from_raw_input_blocks_end_to_end():
    """The 'quality'/'valuation' raw-input passthrough mode chains both calculators."""
    quality_inputs = {
        "net_margin_pct": 63.66,
        "roic_pct": 63.21,
        "fcf_positive_3yr_or_more": True,
        "gross_margin_pct": 74.68,
        "gross_margin_structural_trend": False,
        "revenue_cagr_3yr_pct": 100.05,
        "tam_expansion_evidence": False,
        "growth_decelerating_evidence": False,
        "net_debt_to_ebitda": -0.115,
        "moat_signals": {
            "market_share_stable_or_growing": {"true": True, "evidence": "x"},
            "brand_premium": {"true": True, "evidence": "x"},
            "network_effect": {"true": True, "evidence": "x"},
            "switching_costs": {"true": True, "evidence": "x"},
            "scale_cost_advantage": {"true": False, "evidence": ""},
        },
        "fcf_ni_ttm_pct": 65.85,
        "fcf_ni_annual_pct": [83.50, 80.51],
    }
    valuation_inputs = {
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
    result = compute({"quality": quality_inputs, "valuation": valuation_inputs})
    assert result["composite_score"] == pytest.approx(23.0, abs=0.1)

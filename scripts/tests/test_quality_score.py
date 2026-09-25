import pytest

from scripts.scoring.quality_score import FailsGate, compute


def _base_moat(true_keys):
    signals = {}
    for key in [
        "market_share_stable_or_growing",
        "brand_premium",
        "network_effect",
        "switching_costs",
        "scale_cost_advantage",
    ]:
        is_true = key in true_keys
        signals[key] = {"true": is_true, "evidence": "cited evidence" if is_true else ""}
    return signals


def test_worked_example_quality_scoring_md():
    """framework/quality-scoring.md worked example -> 71.2, fails the 80.0+ gate."""
    d = {
        "net_margin_pct": 18,
        "roic_pct": 22,
        "fcf_positive_3yr_or_more": True,
        "gross_margin_pct": 55,
        "gross_margin_structural_trend": False,
        "revenue_cagr_3yr_pct": 14,
        "tam_expansion_evidence": True,
        "tam_expansion_evidence_text": "documented TAM expansion",
        "growth_decelerating_evidence": False,
        "growth_decelerating_evidence_text": None,
        "net_debt_to_ebitda": 0.8,
        "asset_light_override": False,
        "moat_signals": _base_moat(
            ["market_share_stable_or_growing", "brand_premium", "network_effect", "switching_costs"]
        ),
        "fcf_ni_ttm_pct": 82,
        "fcf_ni_annual_pct": [82, 82],
    }
    result = compute(d)
    assert result["quality_score"] == pytest.approx(71.2, abs=0.05)
    assert result["passes_gate"] is False


def test_nvda_2026_09_17_rescore_session():
    """Cross-check against sessions/2026-09-17-rescore-nvda.md section 5: Quality Score 90.3."""
    d = {
        "net_margin_pct": 63.66,
        "roic_pct": 63.21,
        "fcf_positive_3yr_or_more": True,
        "gross_margin_pct": 74.68,
        "gross_margin_structural_trend": False,
        "revenue_cagr_3yr_pct": 100.05,
        "tam_expansion_evidence": False,
        "growth_decelerating_evidence": False,
        "net_debt_to_ebitda": -0.115,
        "asset_light_override": False,
        "moat_signals": _base_moat(
            ["market_share_stable_or_growing", "brand_premium", "network_effect", "switching_costs"]
        ),
        "fcf_ni_ttm_pct": 65.85,
        "fcf_ni_annual_pct": [83.50, 80.51],
    }
    result = compute(d)
    assert result["quality_score"] == pytest.approx(90.3, abs=0.1)
    assert result["passes_gate"] is True


def test_avgo_2026_09_15_rescore_session():
    """Cross-check against sessions/2026-09-15-rescore-avgo.md section 3: Quality Score 86.3."""
    d = {
        "net_margin_pct": 42.944,
        "roic_pct": 30.47,
        "fcf_positive_3yr_or_more": True,
        "gross_margin_pct": 68.77,
        "gross_margin_structural_trend": False,
        "revenue_cagr_3yr_pct": 24.38,
        "tam_expansion_evidence": True,
        "tam_expansion_evidence_text": "carried-forward TAM evidence",
        "growth_decelerating_evidence": False,
        "net_debt_to_ebitda": 0.687,
        "asset_light_override": False,
        "moat_signals": _base_moat(["market_share_stable_or_growing", "brand_premium"]),
        "fcf_ni_ttm_pct": 102.97,
        "fcf_ni_annual_pct": [102.97, 102.97],
    }
    result = compute(d)
    assert result["quality_score"] == pytest.approx(86.3, abs=0.1)
    assert result["passes_gate"] is True


def test_hard_disqualifier_not_fcf_positive():
    d = {
        "net_margin_pct": 18,
        "roic_pct": 22,
        "fcf_positive_3yr_or_more": False,
        "gross_margin_pct": 55,
        "gross_margin_structural_trend": False,
        "revenue_cagr_3yr_pct": 14,
        "tam_expansion_evidence": False,
        "growth_decelerating_evidence": False,
        "net_debt_to_ebitda": 0.8,
        "moat_signals": _base_moat([]),
        "fcf_ni_ttm_pct": 82,
        "fcf_ni_annual_pct": [82, 82],
    }
    with pytest.raises(FailsGate):
        compute(d)


def test_hard_disqualifier_net_debt_over_threshold():
    d = {
        "net_margin_pct": 18,
        "roic_pct": 22,
        "fcf_positive_3yr_or_more": True,
        "gross_margin_pct": 55,
        "gross_margin_structural_trend": False,
        "revenue_cagr_3yr_pct": 14,
        "tam_expansion_evidence": False,
        "growth_decelerating_evidence": False,
        "net_debt_to_ebitda": 3.0,
        "moat_signals": _base_moat([]),
        "fcf_ni_ttm_pct": 82,
        "fcf_ni_annual_pct": [82, 82],
    }
    with pytest.raises(FailsGate):
        compute(d)


def test_hard_disqualifier_fcf_ni_two_consecutive_years_unexplained():
    d = {
        "net_margin_pct": 18,
        "roic_pct": 22,
        "fcf_positive_3yr_or_more": True,
        "gross_margin_pct": 55,
        "gross_margin_structural_trend": False,
        "revenue_cagr_3yr_pct": 14,
        "tam_expansion_evidence": False,
        "growth_decelerating_evidence": False,
        "net_debt_to_ebitda": 0.8,
        "moat_signals": _base_moat([]),
        "fcf_ni_ttm_pct": 82,
        "fcf_ni_annual_pct": [65, 68],
    }
    with pytest.raises(FailsGate):
        compute(d)


def test_fcf_ni_two_consecutive_low_years_with_explanation_does_not_disqualify():
    d = {
        "net_margin_pct": 18,
        "roic_pct": 22,
        "fcf_positive_3yr_or_more": True,
        "gross_margin_pct": 55,
        "gross_margin_structural_trend": False,
        "revenue_cagr_3yr_pct": 14,
        "tam_expansion_evidence": False,
        "growth_decelerating_evidence": False,
        "net_debt_to_ebitda": 0.8,
        "moat_signals": _base_moat([]),
        "fcf_ni_ttm_pct": 82,
        "fcf_ni_annual_pct": [65, 68],
        "fcf_ni_low_conversion_explanation": "growth capex, documented",
    }
    result = compute(d)  # should not raise
    assert result["quality_score"] > 0


def test_asset_light_override_ineligible_raises():
    from scripts.scoring.common import MissingInputError

    d = {
        "net_margin_pct": 18,
        "roic_pct": 22,
        "fcf_positive_3yr_or_more": True,
        "gross_margin_pct": 55,
        "gross_margin_structural_trend": False,
        "revenue_cagr_3yr_pct": 14,
        "tam_expansion_evidence": False,
        "growth_decelerating_evidence": False,
        "net_debt_to_ebitda": 3.5,
        "asset_light_override": True,
        "asset_light_interest_coverage": 10,  # <= 15, ineligible
        "asset_light_investment_grade": True,
        "moat_signals": _base_moat([]),
        "fcf_ni_ttm_pct": 82,
        "fcf_ni_annual_pct": [82, 82],
    }
    with pytest.raises(MissingInputError):
        compute(d)


def test_missing_input_raises_named_error():
    from scripts.scoring.common import MissingInputError

    with pytest.raises(MissingInputError):
        compute({})

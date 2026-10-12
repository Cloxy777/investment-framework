import pytest

from scripts.scoring.common import MissingInputError
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
        "fcf_after_sbc_ni_ttm_pct": 82, "sbc_ttm": 0, "fcf_ttm": 100,
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
        "fcf_after_sbc_ni_ttm_pct": 65.85, "sbc_ttm": 0, "fcf_ttm": 100,
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
        "fcf_after_sbc_ni_ttm_pct": 102.97, "sbc_ttm": 0, "fcf_ttm": 100,
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
        "fcf_after_sbc_ni_ttm_pct": 82, "sbc_ttm": 0, "fcf_ttm": 100,
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
        "fcf_after_sbc_ni_ttm_pct": 82, "sbc_ttm": 0, "fcf_ttm": 100,
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
        "fcf_after_sbc_ni_ttm_pct": 82, "sbc_ttm": 0, "fcf_ttm": 100,
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
        "fcf_after_sbc_ni_ttm_pct": 82, "sbc_ttm": 0, "fcf_ttm": 100,
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
        "fcf_after_sbc_ni_ttm_pct": 82, "sbc_ttm": 0, "fcf_ttm": 100,
        "fcf_ni_annual_pct": [82, 82],
    }
    with pytest.raises(MissingInputError):
        compute(d)


def test_missing_input_raises_named_error():
    from scripts.scoring.common import MissingInputError

    with pytest.raises(MissingInputError):
        compute({})


# --- SBC treatment (methodology 2026-10-12) ---


def _q_inputs(**over):
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
        "fcf_after_sbc_ni_ttm_pct": 82,
        "sbc_ttm": 10,
        "fcf_ttm": 100,
        "fcf_ni_annual_pct": [120, 110],
    }
    d.update(over)
    return d


def test_fcf_quality_uses_after_sbc_ratio():
    # (0.82 - 0.40)/0.60 = 70.0
    assert compute(_q_inputs(fcf_after_sbc_ni_ttm_pct=82))["sub_scores"]["FCFQuality"] == pytest.approx(70.0, abs=0.01)
    assert compute(_q_inputs(fcf_after_sbc_ni_ttm_pct=40))["sub_scores"]["FCFQuality"] == 0.0
    assert compute(_q_inputs(fcf_after_sbc_ni_ttm_pct=126))["sub_scores"]["FCFQuality"] == 100.0


def test_legacy_fcf_ni_ttm_key_alone_is_refused():
    d = _q_inputs()
    del d["fcf_after_sbc_ni_ttm_pct"]
    d["fcf_ni_ttm_pct"] = 82
    with pytest.raises(MissingInputError, match="replaced by"):
        compute(d)


def test_duol_reported_vs_normalised_net_income():
    """sessions: DUOL TTM to 2026-06-30 (research/framework-review/10-duol-filings-check.md).
    FCF ~398M, SBC ~144.7M. Reported NI 410.8M -> 62% -> FCFQuality 35.9 (artifact of a one-time
    245.7M tax benefit); normalised NI (pretax 201.9M) -> 126% -> 100.0."""
    reported = compute(_q_inputs(fcf_after_sbc_ni_ttm_pct=100 * (398 - 144.7) / 410.8, sbc_ttm=144.7, fcf_ttm=398))
    assert reported["sub_scores"]["FCFQuality"] == pytest.approx(35.9, abs=0.3)
    norm = compute(
        _q_inputs(
            fcf_after_sbc_ni_ttm_pct=100 * (398 - 144.7) / 201.9,
            sbc_ttm=144.7,
            fcf_ttm=398,
            ni_normalised=True,
            ni_normalisation_text="excludes $245.7M Q3-2025 tax benefit (valuation allowance release), 10-Q 0001628280-25-049743",
        )
    )
    assert norm["sub_scores"]["FCFQuality"] == 100.0
    assert any("normalised" in s for s in norm["steps"]["FCF Quality (10%)"])


def test_ni_normalised_requires_text():
    with pytest.raises(MissingInputError):
        compute(_q_inputs(ni_normalised=True))


def test_sbc_equal_or_above_fcf_is_hard_disqualifier():
    with pytest.raises(FailsGate, match="SBC"):
        compute(_q_inputs(sbc_ttm=100, fcf_ttm=100))
    with pytest.raises(FailsGate, match="SBC"):
        compute(_q_inputs(sbc_ttm=150, fcf_ttm=100))


def test_sbc_just_below_fcf_passes_the_disqualifier():
    compute(_q_inputs(sbc_ttm=99.9, fcf_ttm=100))


def test_sbc_with_nonpositive_fcf_is_disqualifier_but_zero_sbc_is_not():
    with pytest.raises(FailsGate):
        compute(_q_inputs(sbc_ttm=5, fcf_ttm=-10))
    compute(_q_inputs(sbc_ttm=0, fcf_ttm=-10, fcf_positive_3yr_or_more=True))


def test_sbc_disqualifier_waiver_needs_documentation():
    compute(_q_inputs(sbc_ttm=120, fcf_ttm=100, sbc_one_off_documented=True, sbc_one_off_text="IPO-year RSU grants $90M, S-1 p.52"))
    with pytest.raises(MissingInputError):
        compute(_q_inputs(sbc_ttm=120, fcf_ttm=100, sbc_one_off_documented=True))


def test_missing_sbc_inputs_stop_and_ask():
    d = _q_inputs()
    del d["sbc_ttm"]
    with pytest.raises(MissingInputError):
        compute(d)


def test_annual_fcf_ni_disqualifier_stays_on_plain_ratio():
    """After-SBC must not feed the <70% test: plain annual ratios >=70% still pass even if after-SBC would be low."""
    compute(_q_inputs(fcf_after_sbc_ni_ttm_pct=23, fcf_ni_annual_pct=[76, 87]))

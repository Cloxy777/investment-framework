import pytest

from scripts.scoring import flags_common as fc


def test_cycle_peak_exactly_100_pct_is_none():
    assert fc.cycle_peak(2.0, 1.0)["flag"] == "NONE"


def test_cycle_peak_just_above_threshold_flags():
    r = fc.cycle_peak(2.0001, 1.0)
    assert r["flag"] == "CYCLE_PEAK_CANDIDATE"
    assert r["growth_pct"] == pytest.approx(100.01, abs=1e-6)


def test_cycle_peak_loss_to_profit_base():
    assert fc.cycle_peak(1.0, -0.5)["flag"] == "LOSS_TO_PROFIT_BASE"
    assert fc.cycle_peak(1.0, 0.0)["flag"] == "LOSS_TO_PROFIT_BASE"


def test_cycle_peak_prior_positive_now_negative_is_none():
    r = fc.cycle_peak(-1.0, 1.0)
    assert r["flag"] == "NONE"
    assert r["growth_pct"] == pytest.approx(-200.0)


def test_cycle_peak_both_negative_is_none():
    assert fc.cycle_peak(-1.0, -2.0)["flag"] == "NONE"


@pytest.mark.parametrize("a", [(None, 1.0), (1.0, None), (None, None)])
def test_cycle_peak_missing_is_unknown(a):
    assert fc.cycle_peak(*a)["flag"] == "UNKNOWN"


def test_multiple_ceiling_boundaries():
    assert fc.multiple_ceiling(30.0, 29.9)["flag"] == "MULTIPLE_CEILING"
    assert fc.multiple_ceiling(29.9, 10.0)["flag"] == "NONE"
    assert fc.multiple_ceiling(35.0, 30.0)["flag"] == "NONE"
    assert fc.multiple_ceiling(-5.0, 0.0)["flag"] == "NONE"
    assert fc.multiple_ceiling(None, 10.0)["flag"] == "UNKNOWN"
    assert fc.multiple_ceiling(35.0, None)["flag"] == "UNKNOWN"


def test_value_trap_candidate():
    assert fc.value_trap_candidate(12.0, -10.0)["flag"] == "VALUE_TRAP_CANDIDATE"
    assert fc.value_trap_candidate(15.0, -0.1)["flag"] == "VALUE_TRAP_CANDIDATE"
    assert fc.value_trap_candidate(15.1, -10.0)["flag"] == "NONE"
    assert fc.value_trap_candidate(12.0, 0.0)["flag"] == "NONE"
    assert fc.value_trap_candidate(-3.0, -10.0)["flag"] == "NONE"
    assert fc.value_trap_candidate(None, -10.0)["flag"] == "UNKNOWN"
    assert fc.value_trap_candidate(12.0, None)["flag"] == "UNKNOWN"


def test_eps_growth_undefined_for_nonpositive_prior():
    assert fc.eps_growth_ttm_pct(1.0, 0.0) is None
    assert fc.eps_growth_ttm_pct(1.0, -1.0) is None
    assert fc.eps_growth_ttm_pct(None, 1.0) is None
    assert fc.eps_growth_ttm_pct(1.5, 1.0) == pytest.approx(50.0)


def test_cli_runs_with_partial_inputs(capsys):
    assert fc.main(["--forward-pe", "34", "--eps-growth", "18"]) == 0
    out = capsys.readouterr().out
    assert "MULTIPLE_CEILING" in out
    assert "UNKNOWN" in out  # cycle_peak has no EPS inputs
    assert "no score effect" in out

import json

import pytest

from scripts.scoring import sbc
from scripts.scoring.common import MissingInputError


def test_reference_example_matches_design():
    m = sbc.sbc_metrics(640.0, 1980.0, 45000.0)
    assert m["sbc_pct_fcf"] == pytest.approx(32.323, abs=1e-3)
    assert m["fcf_yield_reported_pct"] == pytest.approx(4.4, abs=1e-6)
    assert m["fcf_yield_after_sbc_pct"] == pytest.approx(2.9778, abs=1e-3)
    assert m["severity"] == "elevated"


def test_below_watch_line_is_none():
    assert sbc.sbc_metrics(100.0, 1000.0, 20000.0)["severity"] == "none"


def test_boundaries_are_inclusive():
    assert sbc.sbc_metrics(300.0, 1000.0, 20000.0)["severity"] == "elevated"
    assert sbc.sbc_metrics(1000.0, 1000.0, 20000.0)["severity"] == "severe"


def test_negative_fcf_ratio_undefined_and_severe():
    m = sbc.sbc_metrics(50.0, -10.0, 1000.0)
    assert m["sbc_pct_fcf"] is None
    assert m["severity"] == "severe"
    assert m["fcf_yield_after_sbc_pct"] == pytest.approx(-6.0)


def test_zero_fcf_zero_sbc_is_none():
    assert sbc.sbc_metrics(0.0, 0.0, 1000.0)["severity"] == "none"


def test_sbc_above_fcf_gives_negative_after_sbc_yield():
    m = sbc.sbc_metrics(150.0, 100.0, 1000.0)
    assert m["severity"] == "severe"
    assert m["fcf_yield_after_sbc_pct"] < 0


@pytest.mark.parametrize("args", [(None, 1.0, 1.0), (1.0, None, 1.0), (1.0, 1.0, None), (1.0, 1.0, 0.0), (-1.0, 1.0, 1.0)])
def test_missing_or_invalid_inputs_raise(args):
    with pytest.raises(MissingInputError):
        sbc.sbc_metrics(*args)


def test_render_mentions_no_score_effect_and_unavailable_ratio():
    text = sbc.render(sbc.sbc_metrics(50.0, -10.0, 1000.0))
    assert "no score effect" in text
    assert "n/a" in text


def test_cli_prints_block(capsys):
    assert sbc.main(["--sbc", "640", "--fcf", "1980", "--market-cap", "45000"]) == 0
    assert "FCF yield after SBC" in capsys.readouterr().out


def test_cli_missing_input_exits_2(capsys):
    assert sbc.main(["--sbc", "640", "--fcf", "1980"]) == 2
    assert "ERROR" in capsys.readouterr().err


def test_cli_json_input(tmp_path, capsys):
    f = tmp_path / "x.json"
    f.write_text(json.dumps({"sbc_ttm": 100, "fcf_ttm": 1000, "market_cap": 20000}))
    assert sbc.main(["--input", str(f)]) == 0
    assert "SBC/FCF = 10.0%" in capsys.readouterr().out

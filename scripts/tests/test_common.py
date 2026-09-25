from scripts.scoring.common import round_boundary


def test_round_boundary_half_rounds_up():
    assert round_boundary(47.45) == 47.5
    assert round_boundary(22.95) == 23.0
    assert round_boundary(0.05) == 0.1
    assert round_boundary(99.95) == 100.0


def test_round_boundary_normal_cases():
    assert round_boundary(47.44) == 47.4
    assert round_boundary(47.46) == 47.5
    assert round_boundary(71.2) == 71.2

from random import randint
from round_robin_generator import generate_matchups
import pytest


@pytest.mark.parametrize(
    "p,expected", [(2, 7), (3, 8), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)]
)
def test_apply_offset(p, expected):
    assert generate_matchups.apply_offset(p, 8, 2) == expected


@pytest.mark.parametrize("p", range(1, 10))
def test_apply_offset__offset_0(p):
    assert (
        generate_matchups.apply_offset(p, 10, 0) == p
    ), "Should be idempotent on offset 0"


@pytest.mark.parametrize("n", range(1, 10))
def test_applyoffset__p_equals_1(n):
    assert generate_matchups.apply_offset(1, n, randint(1, n)) == 1, "1 should be fixed"

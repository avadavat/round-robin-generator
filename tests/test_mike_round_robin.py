import pytest
from round_robin_generator import mike_round_robin
import numpy as np

test_players = ['Mike', 'Joe', 'Dan', 'Bill']


@pytest.mark.parametrize("num_rounds", range(1, 4))
def test_default_scramble(num_rounds):
    """
    Checking to ensure the output shape is valid. Also checks to make sure there are no
    duplicate matches.
    :param num_rounds: Number of rounds to run the round robin algorithm.
    :return:
    """
    output = mike_round_robin.default_scramble(num_rounds, test_players)
    assert output.shape[0] >= 1
    assert output.shape[1] == 2
    # Verify all matches are unique
    assert len(np.unique(output.values)) == output.shape[0] * output.shape[1]


def test_invalid_round_numbers():
    # Where the number of rounds equals the number of players
    with pytest.raises(Exception):
        mike_round_robin.default_scramble(4, test_players)

    with pytest.raises(Exception):
        mike_round_robin.default_scramble(0, test_players)

    with pytest.raises(Exception):
        mike_round_robin.default_scramble(2, ['Mike', 'Joe', 'Dan'])

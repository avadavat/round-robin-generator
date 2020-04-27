import pytest
from round_robin_generator.matchup_generation_default_scramble import default_scramble
import numpy as np

test_players = ["Mike", "Joe", "Dan", "Bill"]


@pytest.mark.parametrize("num_rounds", range(1, 4))
def test_default_scramble(num_rounds):
    """
    Checking to ensure the output shape is valid. Also checks to make sure there are no
    duplicate matches.
    :param num_rounds: Number of rounds to run the round robin algorithm.
    """
    output = default_scramble(num_rounds, test_players)
    assert output.shape[0] >= 1
    assert output.shape[1] == 2
    # Verify all matches are unique
    assert len(np.unique(output.values)) == output.shape[0] * output.shape[1]


def test_excess_rounds():
    """
    Test when the number of rounds is greater than the number of teams -1.
    """
    output = default_scramble(6, test_players, reshuffle_excess=False)
    assert sorted(np.unique(output.loc[:'Round 3', :].values)) == sorted(np.unique(output.loc['Round 4':, :].values))

    # The the case with two teams
    o2 = default_scramble(2, ['Mike', 'Tim'], reshuffle_excess=False)
    assert o2.loc['Round 1', 'Game 1'] == o2.loc['Round 2', 'Game 1']

def test_invalid_round_numbers():
    with pytest.raises(Exception):
        default_scramble(0, test_players)

    with pytest.raises(Exception):
        default_scramble(2, ["Mike", "Joe", "Dan"])



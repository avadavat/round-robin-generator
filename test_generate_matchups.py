from random import randint
from generate_matchups import apply_offset, generate_matchups

def test_apply_offset():
    for i in range(1, 10):
        assert apply_offset(i, 10, 0) == i, "Should be idempotent on offset 0"

    for i in range(1, 10):
        assert apply_offset(1, i, randint(1,i)) == 1, "1 should be fixed"

    assert apply_offset(8, 8, 2) == 6, "Should be 6"
    assert apply_offset(7, 8, 2) == 5, "Should be 5"
    assert apply_offset(6, 8, 2) == 4, "Should be 4"
    assert apply_offset(5, 8, 2) == 3, "Should be 3"
    assert apply_offset(4, 8, 2) == 2, "Should be 2"
    assert apply_offset(3, 8, 2) == 8, "Should be 8"
    assert apply_offset(2, 8, 2) == 7, "Should be 7"

if __name__ == "__main__":
    test_apply_offset()
    print("Everything passed")
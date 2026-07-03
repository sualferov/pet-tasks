import pytest

from pet_tasks.leetcode.monotonic_stack.daily_temperature import daily_temperature


@pytest.mark.parametrize(
    ('temperatures', 'exp_res'),
    [
        ([], []),
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
    ],
)
def test_daily_temperature(temperatures: list[int], exp_res: list[list[int]]) -> None:
    assert daily_temperature(temperatures=temperatures) == exp_res

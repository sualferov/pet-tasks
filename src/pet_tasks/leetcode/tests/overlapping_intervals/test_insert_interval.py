import pytest

from pet_tasks.leetcode.overlapping_intervals.insert_interval import insert_interval


@pytest.mark.parametrize(
    ('intervals', 'new_interval', 'exp_res'),
    [
        ([], [], [[]]),
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ],
)
def test_insert_interval(intervals: list[list[int]], new_interval: list[int], exp_res: list[list[int]]) -> None:
    assert insert_interval(intervals=intervals, new_interval=new_interval) == exp_res

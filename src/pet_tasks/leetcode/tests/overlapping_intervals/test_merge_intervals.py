import pytest

from pet_tasks.leetcode.overlapping_intervals.merge_intervals import merge_intervals


@pytest.mark.parametrize(
    ('intervals', 'exp_res'),
    [
        ([], []),
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[4, 7], [1, 4]], [[1, 7]]),
    ],
)
def test_merge_intervals(intervals: list[list[int]], exp_res: list[list[int]]) -> None:
    assert merge_intervals(intervals=intervals) == exp_res

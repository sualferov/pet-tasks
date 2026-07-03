import pytest

from pet_tasks.leetcode.overlapping_intervals.remove_overlap_intervals import remove_overlap_intervals


@pytest.mark.parametrize(
    ('intervals', 'exp_res'),
    [
        ([], 0),
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ],
)
def test_remove_overlap_intervals(intervals: list[list[int]], exp_res: int) -> None:
    assert remove_overlap_intervals(intervals=intervals) == exp_res

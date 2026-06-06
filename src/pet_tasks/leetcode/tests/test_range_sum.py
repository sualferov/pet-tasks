import pytest

from pet_tasks.leetcode.range_sum import RangeSum


@pytest.mark.parametrize(
    ('nums', 'idx_left', 'idx_right', 'exp_res'),
    [
        ([-2, 0, 3, -5, 2, -1], 0, 2, 1),
        ([-2, 0, 3, -5, 2, -1], 2, 5, -1),
        ([-2, 0, 3, -5, 2, -1], 0, 5, -3),
    ],
)
def test_range_sum(nums: list[int], idx_left: int, idx_right: int, exp_res: list[int]) -> None:
    assert RangeSum(nums=nums).sum_range(left=idx_left, right=idx_right) == exp_res

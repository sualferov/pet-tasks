import pytest

from pet_tasks.leetcode.prefix_sum.contiguous_array import ContiguousArray


@pytest.mark.parametrize(
    ('nums', 'exp_res'),
    [
        ([0], 0),
        ([0, 1], 2),
        ([1, 0], 2),
        ([0, 1, 0], 2),
        ([0, 1, 0, 1], 4),
        ([0, 1, 1, 1, 1, 1, 0, 0, 0], 6),
        ([0, 1, 0, 1, 0, 1, 0, 1, 0], 2),
    ],
)
def test_contiguous_array(nums: list[int], exp_res: int) -> None:
    assert ContiguousArray.find_max_length(nums=nums) == exp_res

import pytest

from pet_tasks.leetcode.two_sum import two_sum


@pytest.mark.parametrize(
    ('nums', 'target', 'exp_res'),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([3, 3], 7, []),
    ],
)
def test_two_sum__success(nums: list[int], target: int, exp_res: list[int]) -> None:
    # act
    res = two_sum(nums=nums, target=target)

    # assert
    assert res == exp_res

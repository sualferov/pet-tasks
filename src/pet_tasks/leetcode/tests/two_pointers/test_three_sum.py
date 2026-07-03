import pytest

from pet_tasks.leetcode.two_pointers.three_sum import three_sum


@pytest.mark.parametrize(
    ('numbers', 'exp_res'),
    [
        ([], []),
        ([1, 2], []),
        ([-1, 1, 0], [[-1, 0, 1]]),
        ([-4, -1, -1, 2], [[-1, -1, 2]]),
        ([-4, -1, -1, 0, 1, 2], [[-1, -1, 2], [-1, 0, 1]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ],
)
def test_range_sum(numbers: list[int], exp_res: list[list[int]]) -> None:
    assert sorted(three_sum(nums=numbers)) == sorted(exp_res)

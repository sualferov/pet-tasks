import pytest

from pet_tasks.leetcode.two_pointers.two_sum import two_sum


@pytest.mark.parametrize(
    ('numbers', 'target', 'exp_res'),
    [
        ([], 2, []),
        ([2, 4], 2, []),
        ([4, 6], 10, [1, 2]),
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
    ],
)
def test_range_sum(numbers: list[int], target: int, exp_res: list[int]) -> None:
    assert two_sum(numbers=numbers, target=target) == exp_res

import pytest

from pet_tasks.leetcode.top_k_elements.k_largest_element import find_k_largest_element


@pytest.mark.parametrize(
    ('nums', 'k', 'exp_res'),
    [
        ([], 2, 0),
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ],
)
def test_top_k_frequent(nums: list[int], k: int, exp_res: int) -> None:
    assert find_k_largest_element(nums=nums, k=k) == exp_res

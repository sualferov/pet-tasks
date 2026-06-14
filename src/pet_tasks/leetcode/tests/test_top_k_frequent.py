import pytest

from pet_tasks.leetcode.top_k_frequent import top_k_frequent_elements


@pytest.mark.parametrize(
    ('nums', 'k', 'exp_res'),
    [
        ([], 2, []),
        ([1], 1, [1]),
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2]),
        ([1, 2, 2, 1, 2, 3, 1, 3, 2, 4, 4], 2, [1, 2]),
    ],
)
def test_top_k_frequent(nums: list[int], k: int, exp_res: list[int]) -> None:
    assert set(top_k_frequent_elements(nums=nums, k=k)) == set(exp_res)

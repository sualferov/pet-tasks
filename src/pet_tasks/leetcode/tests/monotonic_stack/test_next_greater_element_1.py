import pytest

from pet_tasks.leetcode.monotonic_stack.next_greater_element import next_greater_element_1


@pytest.mark.parametrize(
    ('nums1', 'nums2', 'exp_res'),
    [
        ([], [], []),
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
    ],
)
def test_next_greater_element_1(nums1: list[int], nums2: list[int], exp_res: list[list[int]]) -> None:
    assert next_greater_element_1(nums1=nums1, nums2=nums2) == exp_res

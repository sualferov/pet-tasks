import pytest

from pet_tasks.leetcode.linked_list.list_node import ListNode
from pet_tasks.leetcode.linked_list.swap_pairs import swap_pairs


@pytest.mark.parametrize(
    ('nums', 'exp_res'),
    [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
    ],
)
def test_swap_pairs(nums: list[int], exp_res: list[int]) -> None:
    assert swap_pairs(head=ListNode.create(nums=nums)).to_list() == exp_res

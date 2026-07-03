import pytest

from pet_tasks.leetcode.linked_list.list_node import ListNode
from pet_tasks.leetcode.linked_list.reverse_list import reverse_list


@pytest.mark.parametrize(
    ('nums', 'exp_res'),
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ],
)
def test_reverse_list(nums: list[int], exp_res: list[int]) -> None:
    assert reverse_list(head=ListNode.create(nums=nums)).to_list() == exp_res

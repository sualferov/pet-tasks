import pytest

from pet_tasks.leetcode.linked_list.list_node import ListNode
from pet_tasks.leetcode.linked_list.reverse_list_between import reverse_list_between


@pytest.mark.parametrize(
    ('nums', 'left', 'right', 'exp_res'),
    [
        ([3], 1, 1, [3]),
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
    ],
)
def test_reverse_list_between(nums: list[int], left: int, right: int, exp_res: list[int]) -> None:
    assert reverse_list_between(left=left, right=right, head=ListNode.create(nums=nums)).to_list() == exp_res

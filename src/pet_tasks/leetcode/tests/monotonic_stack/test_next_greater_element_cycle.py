import pytest

from pet_tasks.leetcode.monotonic_stack.next_greater_element_cycle import next_greater_element_cycle


@pytest.mark.parametrize(
    ('nums', 'exp_res'),
    [
        ([], []),
        ([1, 2, 1], [2, -1, 2]),
        ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),
    ],
)
def test_next_greater_element_cycle(nums: list[int], exp_res: list[list[int]]) -> None:
    assert next_greater_element_cycle(nums=nums) == exp_res

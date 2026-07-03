import pytest

from pet_tasks.leetcode.binary_tree_traversal.smallest_element_bst import kth_smallest
from pet_tasks.leetcode.entities.tree_node import TreeNode


@pytest.mark.parametrize(
    ('root', 'k', 'exp_res'),
    [
        (None, 2, 0),
        (TreeNode(3, TreeNode(1, right=TreeNode(2)), TreeNode(4)), 1, 1),
        (TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 3, 3),
    ],
)
def test_kth_smallest(root: TreeNode | None, k: int, exp_res: list[str] | None) -> None:
    assert kth_smallest(root=root, k=k) == exp_res

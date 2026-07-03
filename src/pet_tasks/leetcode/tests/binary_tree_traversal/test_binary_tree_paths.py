import pytest

from pet_tasks.leetcode.binary_tree_traversal.binary_tree_paths import binary_tree_paths
from pet_tasks.leetcode.entities.tree_node import TreeNode


@pytest.mark.parametrize(
    ('root', 'exp_res'),
    [
        (None, []),
        (TreeNode(1), ['1']),
        (TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3)), ['1->2->5', '1->3']),
    ],
)
def test_binary_tree_paths(root: TreeNode | None, exp_res: list[str] | None) -> None:
    assert binary_tree_paths(root=root) == (exp_res or [])

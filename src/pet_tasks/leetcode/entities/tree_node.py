from dataclasses import dataclass


@dataclass
class TreeNode:
    """Definition for a binary tree node."""

    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None

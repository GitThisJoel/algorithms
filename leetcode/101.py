# 101. Symmetric Tree
from typing import Optional


def isSymmetric(root: Optional[TreeNode]) -> bool:
    def recr(left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val != right.val:
            return False

        return recr(left.left, right.right) and recr(left.right, right.left)

    return recr(root.left, root.right)

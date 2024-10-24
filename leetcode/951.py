# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def rec(a, b):
            if not a and not b:
                return True
            if (not a and b) or (not b and a):
                return False
            if a.val != b.val:
                return False
            normal = rec(a.left, b.left) and rec(a.right, b.right)
            flip = rec(a.left, b.right) and rec(a.right, b.left)

            return normal or flip

        return rec(root1, root2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 222. Count Complete Tree Node
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        count = 0
        def count(cur):
            if not cur:
                return 0
            return 1 + count(cur.left) + count(cur.right)
        
        return count(root)

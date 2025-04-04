# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(cur):
            if not cur:
                return 0, None
            l, r = rec(cur.left), rec(cur.right)
            if l[0] > r[0]:
                return l[0] + 1, l[1]
            if r[0] > l[0]:
                return r[0] + 1, r[1]
            return l[0] + 1, cur
        
        return rec(root)[1]

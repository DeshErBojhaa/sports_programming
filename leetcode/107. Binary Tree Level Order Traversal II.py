# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 107. Binary Tree Level Order Traversal II
from collections import defaultdict
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        l = defaultdict(list)
        
        def rec(cur, lev):
            if not cur:
                return
            l[lev].append(cur.val)
            rec(cur.left, lev+1)
            rec(cur.right, lev+1)
        
        rec(root, 0)
        
        ans = []
        for k in sorted(l, reverse=True):
            ans.append(l[k])
        return ans

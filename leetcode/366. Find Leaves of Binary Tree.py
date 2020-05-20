# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 366. Find Leaves of Binary Tree
from collections import defaultdict
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)
        
        def rec(cur):
            if not cur:
                return 0
            
            leaf_lev = rec(cur.left)
            leaf_lev = max(leaf_lev, rec(cur.right))
            
            d[leaf_lev].append(cur.val)
            
            return leaf_lev + 1
        
        rec(root)
        return d.values()

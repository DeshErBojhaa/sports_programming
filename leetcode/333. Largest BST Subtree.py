# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 333. Largest BST Subtree
from functools import lru_cache
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        ans = 0
        
        @lru_cache(maxsize=None)
        def trav(cur, mn, mx):
            if not cur:
                return 0
            
            nonlocal ans
            ans = max(1, ans)
            
            # Start A new Tree From Here
            l = trav(cur.left, float('-inf'), cur.val)
            r = trav(cur.right, cur.val, float('inf'))
            
            if l > -1 and r > -1:
                ans = max(ans, l+r+1)
            
            if cur.val <= mn or cur.val >= mx:
                return -1
                        
            l = trav(cur.left, mn, cur.val)
            r = trav(cur.right, cur.val, mx)

            
            if l == -1 or r == -1:
                return -1
            
            cur_max = l + r + 1
            ans = max(ans, cur_max, 1)
            
            return cur_max
        
        trav(root, float('-inf'), float('inf'))
        return ans
#      3
#  2       4
#        1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        @lru_cache(maxsize=None)
        def trav(cur, lo, hi):
            if not cur:
                return 0, 0 # Max from subtree, Can contribute upper
            if not cur.left and not cur.right:
                if cur.val > lo and cur.val < hi:
                    return cur.val, cur.val
                return cur.val, -float('inf')
            
            if cur.val <= lo or cur.val >= hi: # This is an invalid root make this one root
                left = trav(cur.left, -float('inf'), cur.val)
                right = trav(cur.right, cur.val, float('inf'))
                if cur.val == 9:
                    print('9 >', left, right)
                # Get max from subtrees
                subtree = max(left[0], right[0], left[1], right[1])
                
                # Cur Node as root
                root_val = left[1] + right[1] + cur.val
                
                return max(subtree, root_val), -float('inf')
            
            # I am part of a bigger tree
            left = trav(cur.left, lo, cur.val)
            right = trav(cur.right, cur.val, hi)
            if cur.val == 9:
                print('OK 9 >', left, right)
            max_subtrees = left[1] + right[1] + cur.val
            
            # I am the root
            left = trav(cur.left, -float('inf'), cur.val)
            right = trav(cur.right, cur.val, float('inf'))
            subtree = max(left[0], right[0], left[1], right[1])
            root_val = left[1] + right[1] + cur.val
            
            return max(subtree, root_val), max_subtrees
        return max(*trav(root, -float('inf'), float('inf')), 0)

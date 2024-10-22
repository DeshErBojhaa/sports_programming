# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        d = Counter()
        def rec(cur, lev=0):
            if not cur:
                return
            d[lev] += cur.val
            rec(cur.left, lev+1)
            rec(cur.right, lev+1)
        
        rec(root)
        if len(d) < k:
            return -1
        vals = sorted(d.values(), reverse=True)
        return vals[k-1]

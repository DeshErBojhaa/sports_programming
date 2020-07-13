# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1302. Deepest Leaves Sum
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans = [-1, -1]
        
        def trav(cur, depth):
            if not cur:
                return
            nonlocal ans
            if depth > ans[0]:
                ans = [depth, cur.val]
            elif depth == ans[0]:
                ans[1] += cur.val
            
            trav(cur.left, depth+1)
            trav(cur.right, depth+1)
        
        trav(root, 0)
        
        return ans[1]

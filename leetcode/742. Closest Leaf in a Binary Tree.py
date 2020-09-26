# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 742. Closest Leaf in a Binary Tree
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        path = []
        
        def trav(cur, p):
            if not cur:
                return
            if cur.val == k:
                nonlocal path
                path = list([cur] + p)
                return
            
            trav(cur.left, [cur] + p)
            trav(cur.right, [cur] + p)
        
        trav(root, [])
        ln, ans = 10001, None
        dp = [[-1, -1]] * 1001
        
        def rec(cur):
            if not cur:
                return [11111110, 0]
            if not cur.left and not cur.right:
                dp[cur.val] = [0, cur.val]
                return dp[cur.val]
            
            if dp[cur.val][0] != -1:
                return dp[cur.val]
            dep, val = rec(cur.left)
            dp[cur.val] = [dep+1, val]
            
            dep, val = rec(cur.right)
            if dep+1 < dp[cur.val][0]:
                dp[cur.val] = [dep+1, val]
                
            return dp[cur.val]
        
        rec(root)
        
        for i, v in enumerate(path):
            if ln > dp[v.val][0] + i:
                ln = dp[v.val][0] + i
                ans = dp[v.val][1]
        
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 979. Distribute Coins in Binary Tree
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ans = 0
        def post_order(cur):
            if not cur:
                return 0
            l = post_order(cur.left)
            r = post_order(cur.right)
            nonlocal ans
            ans += abs(l) + abs(r)
            return cur.val + l + r - 1
        
        post_order(root)
        return ans
            

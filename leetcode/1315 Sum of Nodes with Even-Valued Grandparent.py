# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1315. Sum of Nodes with Even-Valued Grandparent
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def trav(cur, par, gp):
            if not cur:
                return 0
            
            ans = 0
            if gp and gp.val % 2 == 0:
                ans += cur.val
            
            ans += trav(cur.left, cur, par) + trav(cur.right, cur, par)
            
            return ans
        
        return trav(root, None, None)
            

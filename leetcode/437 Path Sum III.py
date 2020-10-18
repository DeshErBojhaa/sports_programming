# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 437. Path Sum III
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        ans = 0
        
        def rec(cur, prev_sum, value_propagated):
            nonlocal ans
            if not cur:
                return
            
            if value_propagated:
                if cur.val + prev_sum == sum:
                    ans += 1
                    
                if cur.left:
                    rec(cur.left, cur.val + prev_sum, True)
                if cur.right:
                    rec(cur.right, cur.val + prev_sum, True)
            else:
                ans += cur.val == sum
                if cur.left:
                    rec(cur.left, cur.val, True)
                    rec(cur.left, 0, False)
                if cur.right:
                    rec(cur.right, 0, False)
                    rec(cur.right, cur.val, True)
                
            
        rec(root, 0, False)
        
        return ans

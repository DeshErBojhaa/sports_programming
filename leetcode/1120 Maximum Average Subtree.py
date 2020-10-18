# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# 1120. Maximum Average Subtree
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if not root:
            return 0
        
        ans = float('-inf')
        
        def trav(cur):
            nonlocal ans
            if not cur.left and not cur.right:
                ans = max(ans, cur.val / 1.)
                return cur.val, 1
            
            l_sum, l_cnt = 0, 0
            r_sum, r_cnt = 0, 0
            
            if cur.left:
                l_sum, l_cnt = trav(cur.left)
            if cur.right:
                r_sum, r_cnt = trav(cur.right)
            
            cur_avg = (l_sum + r_sum + cur.val) / (l_cnt + r_cnt + 1)
            ans = max(ans, cur_avg)
            return (l_sum + r_sum + cur.val) , (l_cnt + r_cnt + 1)
        
        trav(root)
        return ans

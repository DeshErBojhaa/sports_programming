# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 129. Sum Root to Leaf Numbers
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0
        def trav(cur, tot):
            if not cur:
                return
            nonlocal ans

            now = tot * 10 + cur.val
            # print(cur.val, tot, now, depth)
            if cur.left is None and cur.right is None:
                # print(cur.val, now)
                ans += now
            if cur.left:    
                trav(cur.left, now)
            if cur.right:
                trav(cur.right, now)
        
        trav(root, 0)
        return ans

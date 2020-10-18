# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        def trav(cur):
            if not cur:
                return 0
            ans = 0
            if cur.val > R:
                    ans += trav(cur.left)
            elif cur.val < L:
                ans += trav(cur.right)
            else:
                ans += trav(cur.left) + trav(cur.right) + cur.val
                
            return ans
        
        return trav(root)
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        def trav(cur):
            if not cur:
                return 0
            l = trav(cur.left)
            r = trav(cur.right)
            nonlocal ans
            ans = max(ans, l+r)
            
            return max(l, r) + 1
        
        trav(root)
        
        return ans

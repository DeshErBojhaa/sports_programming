# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def trav(cur, minval, maxval):
            if not cur:
                return True
            if cur.val <= minval or cur.val >= maxval:
                return False
            
            return trav(cur.left, minval, cur.val) and trav(cur.right, cur.val, maxval)
        
        return trav(root, float('-inf'), float('inf'))

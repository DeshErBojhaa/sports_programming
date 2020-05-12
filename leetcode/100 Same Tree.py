# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def trav(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False
            
            return trav(a.left, b.left) and trav(a.right, b.right)
        
        return trav(p, q)

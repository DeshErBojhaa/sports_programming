# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def get(par, cur, dep, target):
            if not cur:
                return -1, None
            
            if cur.val == target:
                return dep, par
            d, p = get(cur, cur.left, dep+1, target)
            if d > -1:
                return d, p
            return get(cur, cur.right, dep+1, target)
        
        depth1, par1 = get(root, root, 0, x)
        depth2, par2 = get(root, root, 0, y)
        
        if depth1 < 0 or depth2 < 0 or not par1 or not par2 or par1 == par2:
            return False
        return depth1 == depth2

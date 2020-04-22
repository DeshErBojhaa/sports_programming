# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        q_val, p_val = q.val, p.val
        p_depth, q_depth = 0, 0
        par = {}
        
        def trav(cur, depth):
            nonlocal p_depth, q_depth
            if not cur:
                return
            if cur.val == p_val:
                p_depth = depth
            if cur.val == q_val:
                q_depth = depth
                
            if cur.left:
                par[cur.left] = cur
                trav(cur.left, depth+1)
            if cur.right:
                par[cur.right] = cur
                trav(cur.right, depth+1)
        
        trav(root, 0)
        
        while p != q:
            # print(p.val, p_depth, q.val, q_depth)
            if p_depth > q_depth:
                p = par[p]
                p_depth -= 1
            else:
                q = par[q]
                q_depth -= 1
        
        return p
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def rec(cur_s, cur_t):
            if not cur_s and not cur_t:
                return True
            if not cur_s or not cur_t:
                return False
            if cur_s.val != cur_t.val:
                return False
            return rec(cur_s.left, cur_t.left) and rec(cur_s.right, cur_t.right)
        
        def travers_s(cur):
            if not cur:
                return False
            if cur.val == t.val:
                if rec(cur, t):
                    return True
            return travers_s(cur.left) or travers_s(cur.right)
        
        return travers_s(s)

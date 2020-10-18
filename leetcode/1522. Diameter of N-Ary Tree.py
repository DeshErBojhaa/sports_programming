"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
# 1522. Diameter of N-Ary Tree
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        ans = 0
        def trav(cur):
            if not cur or not cur.children:
                return 0
            
            mx1, mx2 = 0, 0
            for nxt in cur.children:
                mx2 = max(mx2, trav(nxt) + 1)
                mx1, mx2 = max(mx1, mx2), min(mx1, mx2)
            
            nonlocal ans
            ans = max(ans, mx1 + mx2)
            
            return mx1
        
        trav(root)
        return ans
                

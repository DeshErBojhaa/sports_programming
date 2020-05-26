"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 117. Populating Next Right Pointers in Each Node II
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        d = {}
        
        def rec(cur, lev):
            if not cur:
                return
            
            rec(cur.left, lev + 1)
            
            nonlocal d
            if lev in d:
                d[lev].next = cur
            d[lev] = cur
            
            rec(cur.right, lev + 1)
        
        rec(root, 0)
        
        return root

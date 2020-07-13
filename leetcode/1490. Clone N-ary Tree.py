# 1490. Clone N-ary Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        
        def clone(cur):
            if not cur:
                return None
            tmp_cur = Node(cur.val, [])
            
            for nxt in cur.children:
                tmp_cur.children.append(clone(nxt))
            
            return tmp_cur
        
        return clone(root)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
# 1506. Find Root of N-Ary Tree
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        xor = 0
        
        for n in tree:
            xor ^= n.val
            for c in n.children:
                xor ^= c.val
        
        return [x for x in tree if x.val == xor][0]

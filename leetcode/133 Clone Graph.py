"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        d = defaultdict(Node)
        seen = set()
        
        def trav(cur):
            if cur in seen:
                return
            seen.add(cur)
            _copy = d[cur]
            _copy.val = cur.val
            
            neighbours = []
            for n in cur.neighbors:
                neighbours.append(d[n])
            _copy.neighbors = neighbours
            
            for n in cur.neighbors:
                trav(n)
            
        trav(node)
        return d[node]

# 427. Construct Quad Tree
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid or not grid[0]:
            return None
        R, C = len(grid), len(grid[0])
        
        def build(r1, c1, r2, c2):
            # print(r1, c1, r2, c2)
            if r1 > r2 or c1 > c2:
                return None
            if r1 == r2 and c1 == c2:
                return Node(grid[r1][c1], 1, None, None, None, None)
            half = (r2 - r1) // 2
            
            topl = build(r1, c1, r1 + half, c1 + half)
            topr = build(r1, c1 + half + 1, r1 + half, c2)
            
            botl = build(r1+half+1, c1, r2, c1 + half)
            botr = build(r1+half+1, c1+half+1, r2, c2)
            
            cur = Node(-1, 0, topl, topr, botl, botr)
            
            childs = [topl, topr, botl, botr]
            if all(x.isLeaf for x in childs) and len(set(x.val for x in childs)) == 1:
                cur.isLeaf = 1
                cur.val = topl.val
                cur.topLeft = None
                cur.topRight = None
                cur.bottomLeft = None
                cur.bottomRight = None
            
            return cur
        
        return build(0,0, R-1, C-1)

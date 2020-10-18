# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random
# 1485. Clone Binary Tree With Random Pointer
class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        d = defaultdict(NodeCopy)
        d[None] = None
        
        def rec(cur):
            if not cur:
                return None
            
            c = d[cur]
            c.val = cur.val
        
            c.left = rec(cur.left)
            c.right = rec(cur.right)
            c.random = d[cur.random]
            
            return c
        
        return rec(root)

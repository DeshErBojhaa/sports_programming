# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
from queue import SimpleQueue
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        d = defaultdict(list)
        q = SimpleQueue()
        
        far_left = 0
        q.put((root,0))
        
        while q.qsize():
            top, ind = q.get()
            d[ind].append(top.val)
            
            if top.left:
                q.put((top.left, ind-1))
            if top.right:
                q.put((top.right, ind+1))
        
        return [d[k] for k in sorted(d)]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 103. Binary Tree Zigzag Level Order Traversal
from collections import deque, defaultdict
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append((root, 0))
        node_level = defaultdict(list)
        
        
        while q:
            top, depth = q.popleft()
            node_level[depth].append(top.val)
            
            if top.left:
                q.append((top.left, depth+1))
            if top.right:
                q.append((top.right, depth+1))
        
        ans = []
        for k, v in node_level.items():
            if k%2:
                v = v[::-1]
            ans.append(v)
        
        return ans

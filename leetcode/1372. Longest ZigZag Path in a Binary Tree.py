# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1372. Longest ZigZag Path in a Binary Tree
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        def dfs(cur):
            if not cur:
                return [-1, -1, -1]
            l = dfs(cur.left)
            r = dfs(cur.right)
            
            return [l[1] + 1, r[0] + 1, max(l[1] + 1, r[0] + 1, l[2], r[2])]
        
        return dfs(root)[-1]

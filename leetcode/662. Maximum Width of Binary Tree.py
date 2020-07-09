# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 662. Maximum Width of Binary Tree
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        d = {}
        def trav(cur, col, depth):
            if not cur:
                return
            nonlocal ans, d
            
            if depth not in d:
                d[depth] = col
            
            ans = max(ans, col - d[depth] + 1)
            trav(cur.left, col*2, depth+1)
            trav(cur.right, col*2+1, depth+1)
            
        trav(root, 0, 0)
        return ans

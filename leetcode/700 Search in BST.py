# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def search(cur, val):
            if not cur:
                return None
            if cur.val == val:
                return cur
            
            if cur.val > val:
                return search(cur.left, val)
            return search(cur.right, val)
        return search(root, val)

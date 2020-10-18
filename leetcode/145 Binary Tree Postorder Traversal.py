# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 145. Binary Tree Postorder Traversal
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def trav(cur):
            if not cur:
                return
            trav(cur.left)
            trav(cur.right)
            
            ans.append(cur.val)
        trav(root)
        return ans

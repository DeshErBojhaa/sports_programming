# 538. Convert BST to Greater Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def trav(cur, right_top):
            if not cur:
                return 0
            
            right_bottom = trav(cur.right, right_top)
            updated_cur_val = right_top + right_bottom + cur.val
            
            left_bottom = trav(cur.left, updated_cur_val)
            ret_val = cur.val + left_bottom + right_bottom
            
            cur.val = updated_cur_val
            
            return ret_val
        
        trav(root, 0)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 105. Construct Binary Tree from Preorder and Inorder Traversal
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        preorder = deque(preorder)
        
        def build(preorder, inorder):
            if not inorder:
                return None
            root_val = preorder.popleft()
            cur_node = TreeNode(root_val)
            
            split_ind = inorder.index(root_val)
            
            cur_node.left = build(preorder, inorder[:split_ind])
            cur_node.right = build(preorder, inorder[split_ind+1:])
            
            return cur_node
        
        return build(preorder, inorder)
            

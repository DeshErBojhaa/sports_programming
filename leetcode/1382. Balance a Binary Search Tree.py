# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1382. Balance a Binary Search Tree
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        
        def inorder(cur):
            if not cur:
                return
            inorder(cur.left)
            arr.append(cur.val)
            inorder(cur.right)
        
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            cur = TreeNode(arr[mid])
            
            cur.left = build(l, mid-1)
            cur.right = build(mid+1, r)
            
            return cur
        
        inorder(root)
        return build(0, len(arr)-1)

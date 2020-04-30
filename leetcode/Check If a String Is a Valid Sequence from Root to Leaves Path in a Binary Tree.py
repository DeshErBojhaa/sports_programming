# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        ans = False
        
        def trav(cur, ind):
            nonlocal ans
            
            if ans:
                return
            if not cur:
                return
            if not cur.left and not cur.right and ind == len(arr) - 1 and cur.val == arr[-1]:
                ans = True
                return
            if ind >= len(arr):
                return
            
            if cur.val != arr[ind]:
                return
            trav(cur.left, ind+1)
            trav(cur.right, ind+1)
        
        trav(root, 0)
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 108. Convert Sorted Array to Binary Search Tree
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            cur = TreeNode(nums[mid])
            cur.left = build(l, mid-1)
            cur.right = build(mid+1, r)
            return cur
        
        return build(0, len(nums)-1)

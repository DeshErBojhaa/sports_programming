# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def iterate(cur):
            if not cur:
                return
            yield cur
            yield from iterate(cur.left)
            yield from iterate(cur.right)
        
        for n1, n2 in zip(iterate(original), iterate(cloned)):
            if n1 == target:
                return n2
        

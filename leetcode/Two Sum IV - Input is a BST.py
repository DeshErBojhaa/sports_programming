# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        already = set()
        
        def find(cur):
            if not cur:
                return False
            val = cur.val
            rem = k - val
            
            if rem in already:
                return True
            already.add(val)
            
            if find(cur.left):
                return True
            return find(cur.right)
        
        return find(root)

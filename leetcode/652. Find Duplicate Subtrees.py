# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 652. Find Duplicate Subtrees
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        ans, seen = {}, {}
        
        def trav(cur):
            if not cur:
                return '#'
            l = trav(cur.left)
            r = trav(cur.right)
            
            s = str(cur.val) + 'l' + l + 'r' + r
            
            if s in seen:
                ans[s] = cur
            
            seen[s] = cur
            return s
        
        trav(root)
        return ans.values()

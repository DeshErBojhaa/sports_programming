# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sm = Counter()
        
        def trav(cur, lev=0):
            if not cur:
                return None
            sm[lev] += cur.val
            
            cpy = TreeNode(cur.val)
            cpy.left = trav(cur.left, lev+1)
            cpy.right = trav(cur.right, lev+1)

            return cpy

        copy_tree = trav(root)

        def replace(cur, cpy, lev=0):
            if not cur:
                return
            if not cur.left and not cur.right:
                return
            ss = sm[lev + 1]
            now = (cpy.left.val if cpy.left else 0 ) + (cpy.right.val if cpy.right else 0)
            if cur.left:
                cur.left.val = ss - now
            if cur.right:
                cur.right.val = ss - now
            replace(cur.left, cpy.left, lev+1)
            replace(cur.right, cpy.right, lev+1)
        replace(root, copy_tree)
        root.val = 0

        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        max_depth_sofar = -1
        def trav(cur, depth):
            if not cur:
                return
            nonlocal max_depth_sofar
            
            if depth > max_depth_sofar:
                ans.append(cur.val)
                max_depth_sofar = depth
            
            
            trav(cur.right, depth + 1)
            trav(cur.left, depth + 1)
            
        trav(root, 0)
        
        return ans

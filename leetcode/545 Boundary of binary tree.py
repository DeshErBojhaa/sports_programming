# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        
        def left_path(cur):
            if not cur:
                return
            if not cur.left and not cur.right:  # If last node in the left path
                return
            ans.append(cur.val)
            if not cur.left:
                return left_path(cur.right)
            return left_path(cur.left)
        
        def leaf(cur):
            if not cur:
                return
            if not cur.left and not cur.right:
                if cur != root:
                    ans.append(cur.val)
                return
            leaf(cur.left)
            leaf(cur.right)
            return
        
        def right_path(cur):
            if not cur:
                return
            if not cur.left and not cur.right:  # If last node in the left path
                return
            
            if not cur.right:
                right_path(cur.left)
            else:
                right_path(cur.right)
            ans.append(cur.val)
            return
        
        ans.append(root.val)
        
        left_path(root.left)
        leaf(root)
        right_path(root.right)
        
        return ans

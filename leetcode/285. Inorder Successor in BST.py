# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 285. Inorder Successor in BST
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def right_successor(cur):
            cur = cur.right
            while cur.left:
                cur = cur.left
            return cur
        
        def trav(cur, stk):
            if not cur:
                return None
            
            if cur.val == p.val:
                if cur.right:
                    return right_successor(cur)
                while stk:
                    top = stk.pop()
                    if top.val > p.val:
                        return top
                return None
            
            stk.append(cur)
            l = trav(cur.left, stk)
            if l:
                return l
            r = trav(cur.right, stk)
            if r:
                return r
            if stk:
                stk.pop()
            return None
        
        return trav(root, [])
    
# [2,1,3]
# 1
# [5,3,6,2,4,null,null,1]
# 6

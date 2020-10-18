# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def predessor(cur):
            cur = cur.left
            while cur.right:
                cur = cur.right
            return cur.val
        def successor(cur):
            cur = cur.right
            while cur.left:
                cur = cur.left
            return cur.val
        
        def delete(cur, val):
            if not cur:
                return None
            
            if cur.val > val:
                cur.left = delete(cur.left, val)
            elif cur.val < val:
                cur.right = delete(cur.right, val)
            else:
                if cur.right:
                    cur.val = successor(cur)
                    cur.right = delete(cur.right, cur.val)
                elif cur.left:
                    cur.val = predessor(cur)
                    cur.left = delete(cur.left, cur.val)
                else:
                    cur = None
            return cur
        return delete(root, key)

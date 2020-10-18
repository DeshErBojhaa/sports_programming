# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        arr = [root]
        l = 10
        while arr:
            nxt = []
            for cur in arr:
                if not cur:
                    continue
                if cur.left:
                    nxt.append(cur.left)
                else:
                    nxt.append(None)
                if cur.right:
                    nxt.append(cur.right)
                else:
                    nxt.append(None)
            
            if len(nxt) % 2:
                return False
            left = nxt[:len(nxt)//2][::-1]
            right = nxt[len(nxt)//2:]
            for a, b in zip(left, right):
                if (a and not b) or (not a and b):
                    return False
                if a and b and a.val != b.val:
                    return False
            arr = nxt[::]
        return True

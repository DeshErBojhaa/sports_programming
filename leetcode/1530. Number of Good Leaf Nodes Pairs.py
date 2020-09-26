# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1530. Number of Good Leaf Nodes Pairs
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        
        def rec(cur):
            if not cur:
                return [0] * (distance+1)
            
            if not cur.left and not cur.right:
                ret = [0] * (distance + 1)
                ret[1] = 1
                return ret
            
            l = rec(cur.left)
            r = rec(cur.right)
            nonlocal ans
            for i in range(1, distance+1):
                for j in range(1, distance+1-i):
                    ans += (l[i] * r[j])
            
            ret = [0] * (distance+1)
            for i, (a,b) in enumerate(zip(l, r)):
                if i+1 > distance:
                    break
                ret[i+1] = a + b
            return ret
        
        rec(root)
        return ans
    
# [1,2,3,4,5,6,7]
# 4

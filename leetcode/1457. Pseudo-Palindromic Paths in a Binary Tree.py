# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1457. Pseudo-Palindromic Paths in a Binary Tree
from collections import Counter
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def rec(cur, cnt):
            if not cur:
                return 0
            if not cur.left and not cur.right:
                cnt[cur.val] += 1
                ans = int(sum(v%2 for v in cnt.values()) < 2)
                cnt[cur.val] -= 1
                return ans
            
            ans = 0
            cnt[cur.val] += 1
            ans += rec(cur.left, cnt) + rec(cur.right, cnt)
            cnt[cur.val] -= 1
            
            return ans
        
        return rec(root, Counter())
            

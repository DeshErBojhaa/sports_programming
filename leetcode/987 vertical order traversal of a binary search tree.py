# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)
        def trav(cur, x, y):
            if not cur:
                return
            d[x].append((cur.val, y))
            trav(cur.left, x-1, y+1)
            trav(cur.right, x+1, y+1)
            
        
        trav(root, 0, 0)
        l = [sorted(d[c], key=lambda x: x[1]) for c in sorted(d)]
        # print(l)
        ans = []
        for r in l:
            tmp = []
            for a,b in sorted(r, key=lambda x: (x[1],x[0])):
                tmp.append(a)
            ans.append(tmp[::])
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ch = defaultdict(list)
        def rec(cur, depth):
            if not cur:
                return
            ch[depth].append(cur)
            rec(cur.left, depth+1)
            rec(cur.right, depth+1)
            return
        
        rec(root, 0)
        
        for d, l in ch.items():
            if d&1==0:
                continue
            
            for i in range(len(l)//2):
                l[i].val, l[~i].val = l[~i].val, l[i].val
        
        return root

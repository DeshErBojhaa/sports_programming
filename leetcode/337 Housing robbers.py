from functools import lru_cache
class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(maxsize=None)
        def trav(cur=root, take=False):
            if not cur:
                return 0
            if not take:
                return trav(cur.left, True)+ trav(cur.right, True)
            
            no = trav(cur.left, True) + trav(cur.right, True)
            yes = trav(cur.left, False) + trav(cur.right, False) + cur.val
            
            return max(no, yes)
        
        return max(trav(), trav(root, True))

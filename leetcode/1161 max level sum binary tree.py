    def maxLevelSum(self, root: TreeNode) -> int:
        lev_sum = [0] * 10002
        
        def trav(cur, lev = 1):
            if not cur:
                return
            lev_sum[lev] += cur.val
            trav(cur.left, lev+1)
            trav(cur.right, lev+1)
        
        trav(root)
        
        return lev_sum.index(max(lev_sum))

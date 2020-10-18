def findBottomLeftValue(self, root: TreeNode) -> int:
        ans = (0,root.val)
        
        def trav(cur, ok=False, lev=0):
            nonlocal ans
            if not cur:
                return
            if not cur.left and not cur.right:
                if lev > ans[0]:
                    ans = (lev, cur.val)
            
            trav(cur.left, True, lev+1)
            trav(cur.right, False, lev+1)
        
        trav(root)
        return ans[1]

def largestValues(self, root: TreeNode) -> List[int]:
        ans = []
        
        def trav(cur, lev=0):
            if not cur:
                return
            
            nonlocal ans
            if lev >= len(ans):
                ans.append(cur.val)

            ans[lev] = max(ans[lev], cur.val)
            
            trav(cur.left, lev+1)
            trav(cur.right, lev+1)
        
        trav(root)
        return ans

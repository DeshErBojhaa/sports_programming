def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def trav(cur, mn, mx):
            if not cur:
                return -1
            
            ans = abs(mx - cur.val)
            ans = max(ans, abs(cur.val - mn))
            
            ans = max(ans, trav(cur.left, min(mn, cur.val), max(mx, cur.val)))
            ans = max(ans, trav(cur.right, min(mn, cur.val), max(mx, cur.val)))
            
            return ans
        
        return trav(root, root.val, root.val)

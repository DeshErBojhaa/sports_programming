def maxPathSum(self, root: TreeNode) -> int:
        ans = -999999999990
        
        def trav(cur):
            if not cur:
                return 0
            
            left = trav(cur.left)
            right = trav(cur.right)
            
            nonlocal ans
            # Path goes through this node
            ans = max(ans, max(0, left+right)+cur.val)
            
            # Path includes this node
            return max(0, max(0, max(left, right)) + cur.val)
        
        trav(root)
        return ans

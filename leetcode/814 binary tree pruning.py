def pruneTree(self, root: TreeNode) -> TreeNode:
        def trav(cur):
            if not cur:
                return None
            cur.left = trav(cur.left)
            cur.right = trav(cur.right)
            
            if not cur.left and not cur.right and cur.val == 0:
                cur = None
            return cur
        
        return trav(root)

def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        n = TreeNode(val)
        if not root or val > root.val:
            n.left = root
            return n
        
        par = None
        cur = root
        while cur and cur.val > val:
            par = cur
            cur = cur.right
        
        child = par.right
        par.right = n
        n.left = child
        
        return root

def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def trav(cur1, cur2):
            # print(cur1, cur2)
            if not cur1 and not cur2:
                return True
            if not cur1 or not cur2:
                return False
            
            if cur1.val != cur2.val:
                return False
            
            ok = trav(cur1.left, cur2.left)
            ok |= trav(cur1.left, cur2.right)
            ok2 = trav(cur1.right, cur2.left)
            ok2 |= trav(cur1.right, cur2.right)
            
            return ok & ok2
        
        # print(root1, root2)
        return trav(root1, root2)

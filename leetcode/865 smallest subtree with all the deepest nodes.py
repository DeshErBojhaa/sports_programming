def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        ans = [root, 0]

        def trav(cur, depth, ans):
            # print(ans)
            if not cur:
                return depth
            
            l = trav(cur.left, depth + 1, ans)
            r = trav(cur.right, depth + 1, ans)
            
            if l == r and l >= ans[1]:
                ans[0], ans[1] = cur, l
            
            return max(l, r)
        
        trav(root, 0, ans)
        
        return ans[0]

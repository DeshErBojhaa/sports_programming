def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        pi, poi, n = 0, 0, len(pre)
        
        def make():
            nonlocal pi, poi
            if pi >= n or poi >= n:
                return None
            
            cur = TreeNode(pre[pi])
            
            if cur.val == post[poi]:
                poi += 1
                return cur
            
            pi += 1
            cur.left = make()
            
            if cur.val == post[poi]:
                poi += 1
                return cur
            
            pi += 1
            cur.right = make()
            
            if cur.val == post[poi]:
                poi += 1
            
            return cur
        return make()

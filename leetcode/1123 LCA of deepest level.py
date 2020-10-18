def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        leafs = deque()
        def find_leafs(cur, d=0):
            if not cur:
                return
            if not cur.left and not cur.right:
                while leafs and leafs[-1][1] < d:
                    leafs.pop()
                if not leafs or leafs[-1][1] == d:
                    leafs.append((cur,d))
                
            find_leafs(cur.left, d+1)
            find_leafs(cur.right, d+1)
            
        def find_path(cur, target, path, ans):
            
            if len(ans) or not cur:
                return
            
            if cur == target: # match by id if error
            
                if cur not in path:
                    path.append(cur)
                ans.extend(path[:])
                return
                
            path.append(cur)
            find_path(cur.left, target, path, ans)
            find_path(cur.right, target, path, ans)
            path.pop()
        
        def find_lca(a, b):
            root_to_a, root_to_b = [], []
            find_path(root, a, [], root_to_a)
            find_path(root, b, [], root_to_b)
            
            i = 0
            while i < len(root_to_a) and i < len(root_to_b):
                if root_to_a[i] != root_to_b[i]:
                    return root_to_a[i-1]
                i += 1
            if len(root_to_a) < len(root_to_b):
                return root_to_a[-1]
            return root_to_b[-1]
        
        find_leafs(root)
        lca = leafs[0][0]
        print(leafs)
        
        for i in range(1, len(leafs)):
            lca = find_lca(lca, leafs[i][0])
        return lca

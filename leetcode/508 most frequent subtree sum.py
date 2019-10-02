def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        c = Counter()
        mc = 0
        def trav(cur):
            if not cur:
                return 0
            
            x = cur.val + trav(cur.left) + trav(cur.right)
            c[x] += 1
            nonlocal mc
            mc = max(mc, c[x])
            return x
        
        trav(root)
        return list(x for x, i in c.items() if i == mc)
        

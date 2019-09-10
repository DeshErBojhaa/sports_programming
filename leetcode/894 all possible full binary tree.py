def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N%2==0:
            return []
        
        def make(n):
            if n == 1:
                return [TreeNode(0)]
            if n%2==0:
                return []
            
            all_cur = []
            for i in range(1, n-1):
                all_left , all_right = [], []
                all_left.extend(make(i))
                all_right.extend(make(n-1-i))
                for l in all_left:
                    for r in all_right:
                        cur = TreeNode(0)
                        cur.left = l
                        cur.right = r
                        all_cur.append(cur)
            return all_cur
        
        return make(N)

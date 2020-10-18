def findCircleNum(self, M: List[List[int]]) -> int:
        ans, f = 0, [False] * len(M)
        
        def trav(cur):
            nonlocal f
            for i, v in enumerate(M[cur]):
                if v and not f[i]:
                    f[i] = True
                    trav(i)

        for i in range(len(M)):
            if not f[i]:
                f[i] = True
                trav(i)
                ans += 1
        
        return ans

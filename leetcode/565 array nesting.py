def arrayNesting(self, n: List[int]) -> int:
        l = len(n)
        f = [False] * l
        
        def go(cur, cnt):
            if f[cur]:
                return cnt
            f[cur] = True
            return go(n[cur], cnt+1)
        
        ans = 1
        for i in n:
            if f[i]:
                continue
            ans = max(ans, go(i, 0))
        
        return ans

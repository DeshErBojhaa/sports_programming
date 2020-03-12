    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[-float('Inf') for _ in range(102)] for _ in range(102)]
        def rec(s, e, M):
            if s > e:
                return -float('Inf')
            if s == e:
                return 0
            
            if dp[s][M] != -float('Inf'):
                return dp[s][M]
            
            cur = -float('Inf')
            
            for i in range(1, (M*2)+1):
                if s+i > n:
                    break
                x = rec(s+i, e, max(M,i))
                cur = max(cur, -x+ sum(piles[s:s+i]))
                
            dp[s][M] = cur
            return cur
        
        more =  rec(0, n, 1)
        return ((sum(piles) - more)//2) + more

def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[(2000000000, -1)]*n for _ in range(n)]
        # dp[i][j] => min val, biggest num in this interval
        
        def rec(i, j):
            if i == j:
                return (0, arr[i])

            nonlocal dp
            if dp[i][j][0] < 2000000000:
                return dp[i][j]
            
            for x in range(0, j-i):
                lft = rec(i, i+x)
                rt = rec(i+x+1, j)
                
                val = lft[1] * rt[1]
                val += lft[0] + rt[0]
                    
                if val < dp[i][j][0]:
                    dp[i][j] = (val, max(lft[1], rt[1]))
            return dp[i][j]
        
        return rec(0, n-1)[0]

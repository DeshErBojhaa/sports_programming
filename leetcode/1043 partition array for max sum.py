def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [-1] * len(A)
        max_element = {}
        for i in range(len(A)):
            me = A[i]
            for j in range(K+1):
                if i+j >= len(A):
                    break
                me = max(me, A[i+j])
                max_element[(i, i+j)] = me
                
        def rec(cur):
            if cur == len(A):
                return 0  
            if dp[cur] > -1:
                return dp[cur]
            dp[cur] = 0
            
            for i in range(K):
                if cur + i >= len(A):
                    break
                max_num = max_element[(cur,cur+i)]
                dp[cur] = max(dp[cur], rec(cur+i+1) + (max_num * (i+1)))
            
            return dp[cur]
        return rec(0)

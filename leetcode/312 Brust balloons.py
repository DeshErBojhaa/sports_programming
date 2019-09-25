# This problem has a tricky idea. If we try to think we first brust the i-th
    # element and then split the call in [L, i-1] ans [i+1, R], then it will not work.
    # Because, there can be overlap in those 2 new sub sections.
    # Instead think at sime point i, We will burst it last, once all the left and right 
    # balloons are already brusted.
    # For more detail, look at erichto's youtube video called `leetcode dynamic programming`
    def maxCoins(self, A: List[int]) -> int:
        if not A:
            return 0
        
        n = len(A)
        dp = [[-1]*n for _ in range(n)]
        
        def rec(l, r):
            if l > r :
                return 0
            if dp[l][r] > -1:
                #pass
                return dp[l][r]
            dp[l][r] = 0
            
            for i in range(l, r+1):
                le = A[l-1] if l else 1
                re = A[r+1] if r+1 < n else 1
                # print(i, le, re, A[i])
                dp[l][r] = max(dp[l][r], A[i]*le*re + rec(l, i-1) + rec(i+1, r))
            
            return dp[l][r]
        
        return rec(0, n-1)

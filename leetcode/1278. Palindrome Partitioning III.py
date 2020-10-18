# 1278. Palindrome Partitioning III
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        N = len(s)
        
        @lru_cache(None)
        def cost(l, r):
            if l >= r:
                return 0
    
            if s[l] == s[r]:
                return cost(l+1, r-1)
            return cost(l+1, r-1) + 1
            
        
        
        @lru_cache(None)
        def rec(cur, K):
            if K == 1:
                return cost(cur, N-1)
            if cur == N or K <= 0:
                return inf
            
            ans = inf
            
            for i in range(cur, N):
                ans = min(ans, rec(i+1, K-1) + cost(cur, i))
            
            return ans
        
        return rec(0, k)

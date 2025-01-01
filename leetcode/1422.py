class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        N = len(s)
        
        for i in range(N-1):
            z, o = 0, 0
            for j in range(i, -1, -1):
                z += (s[j] == '0')
            for j in range(i+1, N):
                o += (s[j] == '1')
            
            ans = max(ans, z+o)
        
        return ans

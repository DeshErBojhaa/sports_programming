# 275. H-Index II 
class Solution:
    def hIndex(self, c: List[int]) -> int:
        if not c:
            return 0
        
        c.sort()
        ans, N = 0, len(c)
        
        for i, v in enumerate(c):
            if v >= N - i:
                ans = max(ans, N - i)
        
        return ans

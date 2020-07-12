# 1513. Number of Substrings With Only 1s
class Solution:
    def numSub(self, s: str) -> int:
        ans, mod = 0, 10 ** 9 + 7
        l = -1
        
        for i, v in enumerate(s):
            if v == '0':
                l = i
                continue
            ans += (i - l)
            if ans >= mod:
                ans -= mod
                
        return ans

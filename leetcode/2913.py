class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s), 2):
            ans = ans + (s[i:i+2] == '01' or s[i:i+2] == '10')
        
        return ans

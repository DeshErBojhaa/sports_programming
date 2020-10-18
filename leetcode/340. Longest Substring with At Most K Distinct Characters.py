# 340. Longest Substring with At Most K Distinct Characters
from collections import Counter
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        distinct = Counter()
        ans, l, r = 0, 0, 0
        
        while r < len(s):
            distinct[s[r]] += 1
            r += 1
            
            while len(distinct) > k:
                distinct[s[l]] -= 1
                if distinct[s[l]] == 0:
                    del distinct[s[l]]
                l += 1
            
            ans = max(ans, r - l)
        
        return ans

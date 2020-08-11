# 1371. Find the Longest Substring Containing Vowels in Even Counts
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        pos, mask = {0:-1}, 0
        ans = 0
        
        for i, ch in enumerate(s):
            dig = ord(ch) - 97
            if ch in 'aeiou':
                mask ^= (1 << dig)
            
            ans = max(ans, i - pos.get(mask, i))
            if mask not in pos:
                pos[mask] = i
        
        return ans

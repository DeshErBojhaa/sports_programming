# 1542. Find Longest Awesome Substring
class Solution:
    def longestAwesome(self, s: str) -> int:
        pos, mask = {0:-1}, 0
        ans = 1
        
        for i, ch in enumerate(s):
            ch = ord(ch) - 48
            mask ^= (1<<ch)
            
            ans = max(ans, i - pos.get(mask, i))
            
            for v in range(10):
                mask_with_one_odd = mask ^ (1<<v)
                ans = max(ans, i - pos.get(mask_with_one_odd, i))
                
            if mask not in pos:
                pos[mask] = i
        
        return ans
                
        

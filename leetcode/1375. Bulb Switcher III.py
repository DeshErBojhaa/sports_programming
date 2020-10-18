# 1375. Bulb Switcher III
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        store, ans = 0, 0
        mx = -1
        for l in light:
            mx = max(l, mx)
            store += 1
            
            ans += int(mx == store)
        
        return ans

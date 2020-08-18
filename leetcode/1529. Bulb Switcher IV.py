# 1529. Bulb Switcher IV
class Solution:
    def minFlips(self, target: str) -> int:
        want, ans = 0, 0
        
        for c in target:
            if int(c) == want:
                continue
            ans += 1
            want = 1 - want
        
        return ans

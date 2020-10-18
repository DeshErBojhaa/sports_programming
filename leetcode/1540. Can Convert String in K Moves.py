# 1540. Can Convert String in K Moves
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        
        for a, b in zip(s, t):
            d = (ord(b) - ord(a)) % 26
            if d and cnt[d] * 26 + d > k:
                return False
            cnt[d] += 1
        
        return True

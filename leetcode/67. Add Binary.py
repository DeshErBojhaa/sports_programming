# 67. Add Binary
from itertools import zip_longest
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        hand, ans = 0, []
        
        for x, y in zip_longest(a[::-1], b[::-1]):
            x = int(x) if x is not None else 0
            y = int(y) if y is not None else 0
            val = x + y + hand
            ans.append(val%2)
            hand = int(val > 1)
        
        if hand:
            ans.append(1)
        
        
        return ''.join(map(str, ans[::-1]))

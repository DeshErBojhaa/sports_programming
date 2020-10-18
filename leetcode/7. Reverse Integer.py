# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        y = int(str(abs(x))[::-1])
        y *= -1 if x < 0 else 1
        
        if y > (2**31)-1 or y < -(2**31):
            return 0
        return y

# 50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(a, b):
            if not b:
                return 1
            ret = 1.
            if b%2:
                ret *= a
            tmp = power(a, b//2)
            tmp *= tmp
            
            return ret * tmp
        
        xx = power(x, abs(n))
        if n < 0:
            xx = 1/xx
        return xx

class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 1
        
        f0, f1 = 1, 1
        
        for i in range(n-1):
            f0, f1 = f1, f0+f1
        return f1

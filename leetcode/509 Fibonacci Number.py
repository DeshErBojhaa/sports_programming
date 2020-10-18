class Solution:
    def fib(self, N: int) -> int:
        if not N:
            return 0
        f0 = 0
        f1 = 1
        
        for i in range(N-1):
            f0, f1 = f1, f0 + f1
        
        return f1

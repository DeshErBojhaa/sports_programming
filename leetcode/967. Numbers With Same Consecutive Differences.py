# 967. Numbers With Same Consecutive Differences
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ans = []
        if N < 2:
            return range(10)
        
        def build(num, rem):
            if not rem:
                ans.append(num)
                return
            prev = num%10
            for nn in (prev+K, prev-K):
                if -1 < nn < 10:
                    build(num*10 + nn, rem -1)
        
        for i in range(1, 10):
            build(i, N - 1)
        
        return set(ans)

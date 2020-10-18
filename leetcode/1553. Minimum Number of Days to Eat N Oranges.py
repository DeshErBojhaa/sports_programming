# 1553. Minimum Number of Days to Eat N Oranges
class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def rec(rem):
            if rem < 3:
                return rem
            return min(rem%2 + rec(rem//2), rem%3 + rec(rem//3))+1
        return rec(n)

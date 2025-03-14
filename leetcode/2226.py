class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo, hi = 0, max(candies)

        def ok(x):
            if x == 0:
                return True
            cnt = 0
            for c in candies:
                cnt += (c // x)
                if cnt >= k:
                    return True

            return False
        
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                lo = mid + 1
            else:
                hi = mid
        
        if ok(lo):
            return lo
        return max(0, lo - 1)

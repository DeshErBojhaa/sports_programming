class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def ok(nn):
            cnt = 0
            for q in quantities:
                cnt += ceil(q/nn)
            return cnt <= n
        
        lo, hi = 1, sum(quantities)
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

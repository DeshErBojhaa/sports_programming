class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        lo, hi = 1, 10**15

        def ok(lim):
            cnt = 0
            for r in ranks:
                xx = lim // r
                x = int(sqrt(xx))
                cnt += x
                if cnt >= cars:
                    return True
            return False

        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

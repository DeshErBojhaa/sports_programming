class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        lo, hi = 0, 3*(10**9)
        def ok(gap):
            now = start[0] - gap
            for l in start:
                r = l + d
                if now + gap > r:
                    return False
                now = max(now + gap, l)
            return True

        while lo < hi:
            mid = (lo + hi) // 2
            if not ok(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo - 1

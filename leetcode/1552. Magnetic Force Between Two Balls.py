# 1552. Magnetic Force Between Two Balls
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        N = len(position)
        position.sort()
        
        lo, hi = 0, position[-1] + 1
        ans = 1
        
        def place(must_dist):
            rem, prev_pos = m-1, position[0]
            for i in range(1, N):
                if position[i] - prev_pos >= must_dist:
                    prev_pos = position[i]
                    rem -= 1
                if rem <= 0:
                    return True
            return bool(rem <= 0)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if place(mid):
                lo = mid + 1
            else:
                hi = mid
        
        return lo - 1

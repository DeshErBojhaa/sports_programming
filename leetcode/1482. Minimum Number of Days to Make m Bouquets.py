# 1482. Minimum Number of Days to Make m Bouquets
class Solution:
    def minDays(self, bday: List[int], m: int, k: int) -> int:
        lo, hi = min(bday), max(bday) + 100
        
        def ok(day):
            num_bucket, taken = 0, 0
            for v in bday:
                if v > day:
                    taken = 0
                    continue
                taken += 1
                if taken == k:
                    num_bucket += 1
                    taken = 0
            # print(f'day {day}  bucket {num_bucket}')
            return num_bucket >= m
        
        ans = float('inf')
        while lo < hi:
            # print(lo, hi)
            mid = (lo + hi) // 2
            if not ok(mid):
                # ans = min(ans, mid)
                lo = mid + 1
            else:
                hi = mid
        
        return lo if lo <= max(bday) else -1

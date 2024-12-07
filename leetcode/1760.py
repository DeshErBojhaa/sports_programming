class Solution:
    def minimumSize(self, nums: List[int], mop: int) -> int:
        lo, hi = 1, max(nums)
        def can(mv):
            op = 0
            for x in nums:
                if x <= mv:
                    continue
                op += x//mv - (x%mv == 0)
                if op > mop:
                    return False
            return True
        
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

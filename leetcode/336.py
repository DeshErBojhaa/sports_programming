class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        lo, hi = 0, len(queries)
        if all(x==0 for x in nums):
            return 0

        def ok(idx):
            cum = [0] * len(nums)
            for l, h, x in queries[:idx + 1]:
                cum[l] += x
                if h + 1 < len(cum):
                    cum[h+1] -= x
            cum = list(accumulate(cum))
            for i, v in enumerate(cum):
                if v < nums[i]:
                    return False
            return True

        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo + 1 if lo < len(queries) else -1

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        limit = 0
        @cache
        def rec(idx, rem):
            if rem == 1:
                return sum(nums[idx:])
            if idx == N and rem == 0:
                return 0
            if idx >= N or rem <= 0:
                return inf

            cum, ret = 0, inf
            nonlocal limit
            for i, x in enumerate(nums[idx:], idx):
                if cum > limit:
                    break
                cum += x
                ret = min(ret, max(cum, rec(i+1, rem - 1)))
            return ret
        
        lo, hi = 0, sum(nums)
        while lo < hi:
            limit = (lo + hi) // 2
            val = rec(0, k)
            if val > limit:
                lo = limit + 1
            else:
                hi = limit
        return lo

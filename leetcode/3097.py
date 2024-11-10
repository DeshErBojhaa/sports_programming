class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        N = ceil(log2(max(nums))) + 1
        c, ans, l = [0] * N, 999999999999, 0
        
        def update_bits(n, d):
            for i in range(N):
                if n & (1<<i):
                    c[i] += d
            return c

        def ok():
            x = 0
            for i in range(N):
                if c[i] <= 0:
                    continue
                x |= (1 << i)
            return x >= k
        
        for i, x in enumerate(nums):
            update_bits(x, 1)
            while l <= i and ok():
                ans = min(ans, i - l + 1)
                update_bits(nums[l], -1)
                l += 1
        
        return ans if ans < 9999999999 else -1

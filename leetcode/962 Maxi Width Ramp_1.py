class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [[nums[-1], n-1]] * n
        for i in range(n-2, -1, -1):
            x, idx = nums[i], i
            if x > arr[i+1][0]:
                arr[i] = [x, i]
                continue
            arr[i] = arr[i+1]
        
        def bi(lo, hi = n):
            target = nums[lo]
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid][0] >= target:
                    lo = mid + 1
                else:
                    hi = mid
            
            return lo - 1

        ans = 0
        for i, n in enumerate(nums):
            ii = bi(i)
            ans = max(ans, ii - i)
        return ans

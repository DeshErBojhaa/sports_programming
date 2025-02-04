class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        N = len(nums)
        
        pref = list(accumulate(nums))
        
        ans = -inf
        
        for i in range(N):
            for j in range(i, N):
                sm, last = 0, -inf
                for k in range(i, j+1):
                    if nums[k] <= last:
                        break
                    sm += nums[k]
                    last = nums[k]
                else:
                    ans = max(ans, sm)
        return ans

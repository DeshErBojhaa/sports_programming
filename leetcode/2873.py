class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N, ans = len(nums), 0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])
        return ans

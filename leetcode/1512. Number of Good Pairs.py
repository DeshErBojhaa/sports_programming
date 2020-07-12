# 1512. Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ans += int(nums[i] == nums[j])
        
        return ans

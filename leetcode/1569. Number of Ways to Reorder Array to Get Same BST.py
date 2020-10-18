# 1569. Number of Ways to Reorder Array to Get Same BST
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = (10**9) + 7
        def rec(nums):
            if len(nums) < 3:
                return 1
            small = [x for x in nums if x < nums[0]]
            big = [x for x in nums if x > nums[0]]
            
            return (rec(small) * rec(big) * math.comb(len(small) + len(big),len(small)))%mod
        
        return (rec(nums) - 1)%mod

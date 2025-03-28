class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)-2):
            if nums[i]:
                continue
            nums[i] = 1
            nums[i+1] ^= 1
            nums[i+2] ^= 1
            cnt += 1
        
        if not all(a==1 for a in nums):
            return -1
        return cnt

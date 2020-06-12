# 665. Non-decreasing Array
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        N = len(nums)
        if N < 3:
            return True
        x = nums[::]
        for i in range(N-2, -1, -1):
            if nums[i] > nums[i+1]:    
                cnt += 1
                nums[i] = nums[i+1]
            
        if cnt < 2:
            return True
        cnt = 0
        nums = x[::]
        for i in range(N-1):
            if nums[i] > nums[i+1]:
                nums[i+1] = nums[i]
                cnt += 1
        
        return cnt < 2

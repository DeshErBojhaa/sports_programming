class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
    
        a, b = [], []
        for i in range(len(nums)):
            if nums[i] == 0:
                b.append(0)
                continue
            a.append(nums[i])
                
        
        return a + b    

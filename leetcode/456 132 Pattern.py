# 456. 132 Pattern
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        min_arr = [nums[0]] * n
        
        for i in range(1, n):
            min_arr[i] = min(min_arr[i-1], nums[i])
        
        # a -> from the min_arr
        # c -> from the loop
        # b -> from the stack
        
        stack = []
        
        for i in range(n-1, -1, -1):
            while stack and min_arr[i] >= stack[-1]:
                stack.pop()
            if stack and min_arr[i] < stack[-1] and nums[i] > stack[-1]:
                return True
            while stack and nums[i] > stack[-1]:
                stack.pop()
            
            stack.append(nums[i])
        
        return False

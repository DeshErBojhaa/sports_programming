class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = nums[::]
        for i in range(1, len(ans)-1):
            ans[i] *= ans[i-1]
        
        right = 1
        for i in range(len(ans)-1, -1, -1):
            ans[i] = (ans[i-1] if i else 1) * right
            right *= nums[i]
        return ans

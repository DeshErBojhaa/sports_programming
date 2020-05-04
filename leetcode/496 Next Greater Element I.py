# 496. Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        for v in nums2:
            while stack and stack[-1] < v:
                next_greater[stack.pop()] = v
            stack.append(v)
        
        while stack:
            next_greater[stack.pop()] = -1
        
        ans = [-1] * len(nums1)
        for i, x in enumerate(nums1):
            ans[i] = next_greater[x]
        return ans

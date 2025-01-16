class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        ans = 0
        if len(nums2) % 2:
            for x in nums1:
                ans = ans ^ x
        if len(nums1) % 2:
            for x in nums2:
                ans = ans ^ x
        return ans

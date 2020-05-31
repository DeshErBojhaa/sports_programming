# 81. Search in Rotated Sorted Array II
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        lo, hi = 0, len(nums) - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            if nums[lo] >= nums[hi]:
                if nums[hi] == target:
                    return True
                hi -= 1
                continue
            
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        
        return nums[lo] == target

# 154. Find Minimum in Rotated Sorted Array II
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def find_min(lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] == nums[hi]:
                    return min(find_min(lo, mid-1), find_min(mid+1, hi), nums[mid])
                elif nums[mid] > nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid
            return nums[lo]
        
        return find_min(0, len(nums) - 1)
        

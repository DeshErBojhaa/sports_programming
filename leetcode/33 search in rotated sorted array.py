class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        N = len(nums)
        lo, hi = 0, N-1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            
            if nums[lo] <= nums[mid]:  # Left side sequential
                if target >= nums[lo] and target <= nums[mid]:
                    hi = mid - 1
                    continue
                lo = mid + 1
            else:   # Right side sequential
                if nums[mid] <= target and target <= nums[hi]:
                    lo = mid + 1
                    continue
                hi = mid - 1
        if nums[hi] == target:
            return hi
        if nums[lo] == target:
            return lo
        return -1
                

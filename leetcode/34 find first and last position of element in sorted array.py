class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_x(l, x):
            lo, hi = 0, len(l)-1
            ans = len(l)
            while lo <= hi:
                mid = (lo + hi)//2
                if l[mid] >= x:
                    ans = mid
                    hi = mid -1
                else:
                    lo = mid + 1
            return ans
        
        left = first_x(nums, target)
        right = first_x(nums, target+1)
        
        if left < right:
            return [left, right-1]
        return [-1, -1]

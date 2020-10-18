from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Running Quick Select (N-k) times
        n = len(nums)
        
        def partition(left, right, pivot):
            pivot_val = nums[pivot]
            nums[pivot], nums[right] = nums[right], nums[pivot]
            active_ind = left
            for i in range(left, right):
                if nums[i] < pivot_val:
                    nums[active_ind], nums[i] = nums[i], nums[active_ind]
                    active_ind += 1
            nums[active_ind], nums[right] = nums[right], nums[active_ind]
            return active_ind
                
        
        def quick_select(left, right, ksmallest):
            if left == right:
                return nums[left]
            random_pivot = randint(left, right)
            pivot_index = partition(left, right, random_pivot)
            if pivot_index == ksmallest:
                return nums[ksmallest]
            elif pivot_index > ksmallest:
                return quick_select(left, pivot_index - 1, ksmallest)
            else:
                return quick_select(pivot_index+1, right, ksmallest)
        
        return quick_select(0, n-1, n - k)

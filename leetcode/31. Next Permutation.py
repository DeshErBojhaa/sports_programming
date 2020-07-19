# 31. Next Permutation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                break

        if i == 0 and nums[0] > nums[1]:
            nums.reverse()
            return
        swapped = False
        if i >= 0:
            for j in range(i+1, n):
                if nums[j] <= nums[i]:
                    nums[i], nums[j-1] = nums[j-1], nums[i]
                    swapped = True
                    break
            if not swapped:
                swapped = True
                nums[i], nums[-1] = nums[-1], nums[i]
        
        for x, y in zip(range(i+int(swapped), n), range(n-1,i+int(swapped)-1, -1)):
            if x >= y:
                break
            nums[x], nums[y] = nums[y], nums[x]
        

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def set_bit(n):
            ans = 0
            while n:
                ans += int(n & 1)
                n //= 2
            return ans
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    continue
                if set_bit(nums[i]) != set_bit(nums[j]):
                    return False
                nums[i], nums[j] = nums[j], nums[i]
        return True

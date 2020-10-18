class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        if len(nums) == 1:
            if nums[0] != 1:
                return 1
            return 2
        
        for i, v in enumerate(nums):
            if i == v-1 or v > len(nums) or v < 0:
                continue
            while v <= len(nums) and v > 0 and nums[v-1] != v:
                nxt = nums[v-1]
                nums[v-1] = v
                v = nxt
            # nums[v] = v
        
        found = 0
        for i, v in enumerate(nums):
            if i != (v-1):
                return i + 1
            found = max(found, v)
        return found + 1

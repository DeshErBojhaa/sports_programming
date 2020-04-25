class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_can_reach = 0
        for i, v in enumerate(nums):
            if i > max_can_reach:
                return False
            max_can_reach = max(max_can_reach, v + i)
        return True
            

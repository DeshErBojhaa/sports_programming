class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:  # [0] case
            return 0
        ans = 1
        max_can_go_this_jump, max_can_go_sofar = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if max_can_go_this_jump < i:
                ans += 1
                max_can_go_this_jump = max_can_go_sofar
            max_can_go_sofar = max(max_can_go_sofar, i + nums[i])
        return ans

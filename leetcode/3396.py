class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums, ans = deque(nums), 0
        while nums:
            dup = False
            for x in nums:
                if nums.count(x) > 1:
                    dup = True
                    break
            if not dup:
                break
            for i in range(3):
                if nums:
                    nums.popleft()
            ans += 1
        
        return ans

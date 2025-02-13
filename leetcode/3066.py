class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0
        heapify(nums)
        cnt = 0
        while nums[0] < k and len(nums) > 1:
            a, b = heappop(nums), heappop(nums)
            x = (min(a, b) * 2) + max(a, b)
            heappush(nums, x)
            cnt += 1
        return cnt

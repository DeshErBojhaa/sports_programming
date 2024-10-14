class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-c for c in nums]
        heapify(nums)
        ans = 0
        for i in range(k):
            x = -heappop(nums)
            ans += x
            heappush(nums, -ceil(x/3))
        return ans

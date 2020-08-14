# 1508. Range Sum of Sorted Subarray Sums
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        h = [(v,i) for i, v in enumerate(nums)]
        heapify(h)
        ans = 0
        
        for i in range(1, right+1):
            v, ind = heappop(h)
            if i >= left:
                ans += v
            if ind + 1 < n:
                heappush(h, (v + nums[ind+1], ind+1))
        
        return ans%1000000007

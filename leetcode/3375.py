class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        for x in set(nums):
            if x < k:
                return -1
            cnt += x > k
        return cnt

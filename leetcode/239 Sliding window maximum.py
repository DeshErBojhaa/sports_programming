from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        
        for i in range(k):
            while dq and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])
        
        ans = []
        for i, v in enumerate(nums[:-k]):
            ans.append(dq[0])
            if v == dq[0]:
                dq.popleft()
            while dq and nums[i + k] > dq[-1]:
                dq.pop()
            dq.append(nums[i+k])
        if dq:
            ans.append(dq[0])
        return ans

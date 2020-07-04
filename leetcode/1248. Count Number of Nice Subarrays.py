# 1248. Count Number of Nice Subarrays
from collections import deque
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = [i for i, v in enumerate(nums) if v&1]
        arr = arr + [len(nums)]
        N = len(arr)
        ans, dq = 0, deque()
        left_ind = -1
        
        for i in range(N-1):
            dq.append(arr[i])
            if len(dq) > k:
                left_ind = dq.popleft()
            
            if len(dq) == k:
                left = dq[0] - left_ind
                right = arr[i+1] - dq[-1]
                
                ans += left * right
        
        return ans

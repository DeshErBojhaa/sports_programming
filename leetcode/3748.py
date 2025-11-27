class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        acc, ans, s = [1] * N, [], 1
        for i, x in enumerate(nums[1:], 1):
            s = s + 1 if x >= nums[i-1] else 1
            acc[i] = acc[i-1] + s

        inv = [N] * N
        for i in range(N-2, -1, -1):
            inv[i] = i + 1 if nums[i] > nums[i+1] else inv[i+1]
        
        cnt = lambda x: (x * (x+1))//2

        for a, b in queries:
            ii = inv[a]
            if ii > b:
                ans.append(cnt(b - a + 1))
                continue
            ans.append(cnt(ii - a) + acc[b] - (acc[ii-1] if ii else 0))
        
        return ans

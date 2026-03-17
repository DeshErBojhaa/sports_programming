class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = nums[0]
        p = []
        for x in nums:
            mx = max(mx, x)
            p.append(gcd(mx, x))
        
        p.sort()
        ans = 0
        N = len(nums)
        for i, j in zip(range(N), range(N-1, -1, -1)):
            if i >= j:
                break
            ans += gcd(p[i], p[j])
        
        return ans

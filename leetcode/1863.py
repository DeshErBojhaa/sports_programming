class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N, ans = len(nums), 0

        for msk in range(2**N):
            x = 0
            for i in range(N):
                if msk & (1<<i) == 0:
                    continue
                x ^= nums[i]
            ans += x

        return ans 

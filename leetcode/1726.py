class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        c = Counter()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x = nums[i] * nums[j]
                c[x] += 1
        
        ans = 0
        for k, v in c.items():
            tmp = v * (v-1)
            tmp *= 4
            ans += tmp
        
        return ans

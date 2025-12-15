class Solution:
    pal = []
    for i in range(1, 5050):
        s = bin(i)[2:]
        if s == s[::-1]:
            pal.append(i)
    def minOperations(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            idx = bisect_left(self.pal, x)
            l, r = abs(self.pal[idx-1] - x), abs(self.pal[idx] - x)
            if l <= r:
                ans.append(l)
            else:
                ans.append(r)
        return ans

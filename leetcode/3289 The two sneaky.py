class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        for a, v in c.items():
            if v > 1:
                ans.append(a)
        return ans

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        a,b,ans = -inf, -inf, -inf

        for i, n in enumerate(values):
            ans = max(ans, a + n - i)
            a = max(a, n + i)
        
        return ans

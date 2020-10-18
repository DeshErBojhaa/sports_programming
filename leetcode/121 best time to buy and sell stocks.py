class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, mn = 0, float('inf')
        
        for x in prices:
            ans = max(ans, x- mn)
            mn = min(mn, x)
        return ans

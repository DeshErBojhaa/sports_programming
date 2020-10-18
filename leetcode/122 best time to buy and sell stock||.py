class Solution:
    def maxProfit(self, p: List[int]) -> int:
        return sum(max(p[i+1] - p[i], 0) for i in range(len(p)-1))

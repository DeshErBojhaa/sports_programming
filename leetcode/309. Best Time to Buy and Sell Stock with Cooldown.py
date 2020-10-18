# 309. Best Time to Buy and Sell Stock with Cooldown
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, cooldown = float('-inf'), float('-inf'), 0
        for p in prices:
            tmp_sell = sell
            sell = buy + p
            buy = max(buy, cooldown - p)
            cooldown = max(cooldown, tmp_sell)
        
        return max(cooldown, sell)

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices[::]
        
        for i in range(len(prices)):
            mx = 0
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    continue
                mx = max(mx, prices[j])
                break
            ans[i] = min(ans[i], prices[i] - mx)
        
        return ans

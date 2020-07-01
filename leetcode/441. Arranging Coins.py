# 441. Arranging Coins
class Solution:
    def arrangeCoins(self, n: int) -> int:
        x, cnt = 0, 0
        for i in range(1, n+1):
            x += i
            if x > n:
                break
            cnt += 1
        
        return cnt

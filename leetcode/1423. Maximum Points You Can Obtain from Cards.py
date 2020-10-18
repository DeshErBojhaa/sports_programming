# 1423. Maximum Points You Can Obtain from Cards
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        dont_take = len(cardPoints) - k
        global_min = float('inf')
        j, min_sum, tot = 0, 0, 0
        
        for i, v in enumerate(cardPoints):
            tot += v
            min_sum += v
            
            if i - j + 1 > dont_take:
                min_sum -= cardPoints[j]
                j += 1
                
            if i - j + 1 == dont_take:
                global_min = min(min_sum, global_min)
        
        return tot - global_min

# 1395. Count Number of Teams
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans, n = 0, len(rating)
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    ans += int(rating[i] < rating[j] < rating[k])
                    ans += int(rating[i] > rating[j] > rating[k])
        
        return ans

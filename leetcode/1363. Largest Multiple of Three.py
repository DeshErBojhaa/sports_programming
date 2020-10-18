# 1363. Largest Multiple of Three
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        dp = [-1, -1, -1]
        
        for v in sorted(digits, reverse=True):
            for x in dp + [0]:
                a = x * 10 + v
                dp[a%3] = max(dp[a%3], a)
        
        return str(dp[0]) if dp[0] > -1 else ''

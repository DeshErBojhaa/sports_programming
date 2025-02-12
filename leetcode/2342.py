class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d, ans = {}, -1
        for n in nums:
            sm = 0
            N = n
            while n:
                sm += int(n%10)
                n //= 10
            
            ans = max(ans, d.get(sm, -inf) + N)
            d[sm] = max(d.get(sm, -inf), N)
        
        return ans

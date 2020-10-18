# 1359. Count All Valid Pickup and Delivery Options
class Solution:
    def countOrders(self, n: int) -> int:
        
        @lru_cache(None)
        def rec(d, p):
            if p < d:
                return 0
            if d == 0:
                return factorial(p)
            
            ans = rec(d-1, p) * d  # Pick any remaing delivery
            
            
            done_delivery = n - d
            done_pickup = n - p
            
            avail_pickup = done_delivery - done_pickup
            ans += rec(d, p-1) * avail_pickup
            
            return ans % (10**9+7)
        
        return rec(n, n) % (10**9+7)

# 1524. Number of Sub-arrays With Odd Sum
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        positions_where_sum_is_odd = 0
        positions_where_sum_is_even = 1 # initially sum is 0
        
        tot_sum, ans = 0, 0
        
        for v in arr:
            tot_sum += v
            
            if tot_sum%2:
                positions_where_sum_is_odd += 1
                ans += positions_where_sum_is_even
            else:
                positions_where_sum_is_even += 1
                ans += positions_where_sum_is_odd
                
        return ans % (10**9+7)
        
        

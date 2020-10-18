class Solution:
    def maxProfit(self, K: int, p: List[int]) -> int:
        if not p or not K:
            return 0
        n = len(p)
        if K > n//2:
            return sum(max(0, p[i] - p[i-1]) for i in range(1, n))
        
        
        odd_transaction, even_transaction = [0] * n, [0]* n
        for k in range(1, K+1):
            cur_tran = even_transaction
            prev_tran = odd_transaction
            if k%2:
                cur_tran = odd_transaction
                prev_tran = even_transaction
                        
            max_pref_sum = float('-inf')
            # 3 2 6 5 0 3
            for i in range(1, n):
                # The inner loop can be replaced with max prefix sum.
                max_pref_sum = max(max_pref_sum, prev_tran[i-1] - p[i-1])
                cur_tran[i] = max(cur_tran[i-1], max_pref_sum + p[i])
            
        return odd_transaction[-1] if k%2 else even_transaction[-1]

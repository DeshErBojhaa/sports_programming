# 60. Permutation Sequence
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1,1,2,6,24,120,720,5040,40320,362880]
        
        def build(mask, N, K):
            # print(bin(mask), N, K)
            if bin(mask).count('1') == n:
                return ""
            if K < 1:
                K = 1
            
            remain_comb = fact[N - 1]
            for x in range(1, 10):
                cur_comb = x * remain_comb
                if cur_comb >= K:
                    cnt = 0
                    for i in range(1, 10):
                        if mask & (1<<i) == 0:
                            cnt += 1
                        if cnt == x:
                            return str(i) + build(mask | (1<<i), N-1, K - ((x-1) * remain_comb))
        
        return build(0, n, k)

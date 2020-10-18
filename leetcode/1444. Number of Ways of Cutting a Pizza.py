# 1444. Number of Ways of Cutting a Pizza
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        N, M = len(pizza), len(pizza[0])        
        row_apple, col_apple = [0] * N, [0] * M

        for i in range(N):
            for j in range(M):
                row_apple[i] += int(pizza[i][j] == 'A')
                col_apple[j] += int(pizza[i][j] == 'A')
        
        row_apple = list(accumulate(row_apple))
        col_apple = list(accumulate(col_apple))
        
        mod = (10**9) + 7
        
        @lru_cache(None)
        def rec(r, c, cut):
            if r >= (N) or c >= (M):
                return 0
            # print(' '*space, r,c,cut)
            if cut == 0:
                # return 1
                ret = 0
                for i in range(r, N):
                    for j in range(c, M):
                        ret += (pizza[i][j] == 'A')

                # print(f'{" "*space} Found {ret}  from {r,c}')
                return int(ret > 0)
            
            ans = 0
            first_valid_row, first_valid_col = 100, 100
            for i in range(r, N):
                for j in range(c, M):
                    if pizza[i][j] == 'A':
                        first_valid_row = min(first_valid_row, i)
                        first_valid_col = min(first_valid_col, j)

            
            if first_valid_row > 51:
                return ans
            
            for i in range(first_valid_row, N):
                ans += rec(i+1, c, cut-1)
            
            for i in range(first_valid_col, M):
                ans += rec(r, i+1, cut-1)

            return ans%mod
        
        return rec(0,0,k-1)%mod

# [".A","AA","A."]
# 3
# [".A","AA","A."]
# 3
# [".A..A","A.A..","A.AA.","AAAA.","A.AA."]
# 5           

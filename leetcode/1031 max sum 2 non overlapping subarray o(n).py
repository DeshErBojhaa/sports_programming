def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n, a = len(A), list(accumulate(A))
        
        def solution(l, m):
            max_pref_end, max_suff_start = [-1] * n, [-1]*n
            mx = -1
            for i in range(l-1,n):
                max_pref_end[i] = max(mx, a[i] - (a[i-l] if i-l>=0 else 0))
                mx = max(mx, max_pref_end[i])
            
            mx = -1
            for i in range(n-m, -1, -1):
                max_suff_start[i] = max(mx, a[i+m-1]-(a[i-1] if i else 0))
                mx = max(mx, max_suff_start[i])
            
            # print(max_pref_end)
            # print(max_suff_start)
            mx = -1
            for i in range(n-1):
                mx = max(mx, max_pref_end[i] + max_suff_start[i+1])
            
            return mx
        return max(solution(L, M), solution(M, L))

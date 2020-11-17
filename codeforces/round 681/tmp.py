from math import inf
from functools import lru_cache


def minSwap( A, B):
    A = [-inf] + A
    B = [-inf] + B
    N = len(A)
    
    @lru_cache(None)
    def rec(cur, sw, ls, sp=0):
        if cur == N:
            return sw
        
        a, b = (A, B) if ls == 0 else (B, A)
        ans = inf
        print(f'{"  " * sp}Cur {cur} Swap Cnt {sw}   Last {bool(ls)}')
        print(f'{"  " * sp}{"-" if not cur else a[cur-1]}   {A[cur]}')
        print(f'{"  " * sp}{"-" if not cur else b[cur-1]}   {B[cur]}')
        # Need swaping
        if cur and (a[cur-1] >= A[cur] or b[cur-1] >= B[cur]):
            print(f'{"  " * sp}Need Swap')
            return rec(cur+1, 1+sw, 1, sp+1)
        
        print(f'{"  "*sp}Normal Call Without Swap')
        ans = rec(cur+1, sw, 0, sp+1)
        if (cur < N-1 and A[cur] < B[cur+1] and B[cur] < A[cur+1] and
                a[cur-1] < A[cur] and b[cur-1] < B[cur]):

            print(f'{"  "*sp}Optional Swap')
            ans = min(ans, rec(cur+1, 1+sw, 1, sp+1))
        print(f'{"  " * sp}Cur{cur}  Ans {ans}')
        return ans
    
    return rec(1, 0, 0)


print(minSwap([0,7,8,10,10,11,12,13,19,18], [4,4,5,7,11,14,15,16,17,20]))

# [0,7,8,10,10,11,12,13,19,18], 
# [4,4,5,7,11,14,15,16,17,20]


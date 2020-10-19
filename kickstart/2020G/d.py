from itertools import accumulate
from collections import Counter
from functools import lru_cache
from math import factorial


def do():
    N = int(input())
    arr = list(map(int, input().split()))

    # dp = [[0] * (N+1) for _ in range(N+1)]
    acc = list(accumulate(arr))

    @lru_cache(None)
    def rec(l, r):
        if l >= r:
            return 0
        if l + 1 == r:
            return arr[l] + arr[r]
        
        ans = 0
        cum = acc[r] - (acc[l-1] if l else 0)
        
        for mid in range(l, r):
            ans += rec(l, mid) + rec(mid+1, r) + cum
        return ans
    
    total = rec(0, N-1)
    ways = factorial(N-1)
    print(total, ways)
    
    return total/ways

    # for i in range(N-1):
    #     dp[i][i+2] = acc[i+2] - acc[i]

    # for gap in range(2, N+1):
    #     for l in range(N - gap + 1):
    #         r = l + gap
    #         dp[l][r] = acc[r] - acc[l] + sum(dp[l][k] + dp[k][r] for k in range(l+1, r))
    
    # for r in dp:
    #     print(r)
    # print()
    # total = dp[0][N]
    # print(total)
    # return total


T = int(input())

for tt in range(1, T+1):
    ans = do()
    print('Case #{}: {}'.format(tt, ans))

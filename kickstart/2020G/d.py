from itertools import accumulate
from functools import lru_cache


def handle_case():
    N = int(input())
    arr = list(map(int, input().split()))

    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(N):
            if i:
                dp[i][j] = (1 + dp[i-1][j]) / (i + j)
            if i > 1:
                dp[i][j] += (dp[i-1][j]) * ((i - 1)/ (i + j))
            if j:
                dp[i][j] += (1 + dp[i][j-1]) / (i + j)
            if j > 1:
                dp[i][j] += dp[i][j-1] * ((j-1)/(i+j))

    ans = 0
    for i, v in enumerate(arr):
        l, r = i, N - i - 1
        ans += v * dp[l][r]

    return ans



T = int(input())

for tt in range(1, T+1):
    res = handle_case()
    print('Case #{}: {}'.format(tt, res))

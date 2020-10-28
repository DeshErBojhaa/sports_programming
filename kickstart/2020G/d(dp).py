from itertools import accumulate
from functools import lru_cache


def handle_recursive(l, r, arr):
    if l >= r:
        return 0
    if l + 1 == r:
        return arr[l] + arr[r]
    ans = 0
    for i in range(l, r):
        ans += handle_recursive(l, i, arr) + handle_recursive(i+1, r, arr) + sum(arr[l:r+1])
    return ans


def handle_case():
    N = int(input())
    arr = list(map(int, input().split()))

    acc = list(accumulate(arr))
    dp = [[0] * N for _ in range(N)]

    for i in range(N-1):
        dp[i][i+1] = arr[i] + arr[i+1]

    for l in range(N-3, -1, -1):
        for r in range(l+2, N):
            ac_val = acc[r] - (acc[l-1] if l else 0)
            print(l, r)
            for mid in range(l, r):
                print('    ', l, mid, '      ', mid+1, r)
                dp[l][r] += dp[l][mid] + dp[mid+1][r] + ac_val
            dp[l][r] /= (r - l)


    #  recursive = handle_recursive(0, N-1, arr)
    #  print(recursive, dp[0][N-1])
    return dp[0][N-1]


T = int(input())

for tt in range(1, T+1):
    res = handle_case()
    print('Case #{}: {}'.format(tt, res))


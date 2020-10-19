from collections import Counter
from math import inf


def find_distance(arr, comp, N):
    ans = 0
    for v in arr:
        ans += min((v - comp + N)%N, (comp - v + N)%N)
    return ans
    


def do():
    L = list(map(int, input().split()))
    
    W, N = L[0], L[1]
    arr = list(map(int, input().split()))
    for i in range(W):
        arr[i] -= 1

    arr.sort()
    mid1 = W // 2

    # ans, mid_val = 0, arr[mid1]
    # ans = find_distance(arr, arr[0], N)
    # ans = min(ans, find_distance(arr, arr[-1], N))
    # ans = min(ans, find_distance(arr, mid_val, N))

    # if mid1:
    #     mid2 = mid1 - 1
    #     mid_val = arr[mid2]
    #     ans = min(ans, find_distance(arr, mid_val, N))
    
    ans = inf
    for v in arr:
        ans = min(ans, find_distance(arr, v, N))

    return ans


T = int(input())

for tt in range(1, T+1):
    ans = do()
    print('Case #{}: {}'.format(tt, ans))

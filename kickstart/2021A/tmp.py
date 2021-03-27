from math import factorial


def rec(arr):
    if len(arr) == 2:
        return arr[0] + arr[1]
    
    ans = 0
    for i in range(len(arr)-1):
        left = arr[:i]
        mid = [arr[i], arr[i+1]]
        right = arr[i+2:]

        ans += rec(left + [sum(mid)] + right) + sum(mid)
    
    return ans / (len(arr)-1)

T = int(input())

for tt in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = rec(arr)
    print('Case #{}: {}'.format(tt, ans))
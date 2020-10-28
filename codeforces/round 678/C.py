from math import factorial


n, x, pos = map(int, input().split())
MOD = (10**9) + 7

small, big, ans = x-1, n-x, 1

l, r = 0, n

while l < r:
    mid = (l + r) //2
    if mid < pos:
        ans *= small
        small -= 1
        l = mid + 1
    elif mid > pos:
        ans *= big
        big -= 1
        r = mid
    else:
        l = mid+1

ans *= factorial(small + big)

print(ans%MOD)

T = int(input())

def calc(arr, r, c):
    left = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not arr[i][j]:
                continue
            left[i][j] = (left[i][j-1] if j else 0) + 1
    right = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c-1, -1, -1):
            if not arr[i][j]:
                continue
            right[i][j] = (right[i][j+1] if j+1 < c else 0) + 1
    up = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not arr[i][j]:
                continue
            up[i][j] = (up[i-1][j] if i else 0) + 1
    down = [[0] * c for _ in range(r)]
    for i in range(r-1,-1,-1):
        for j in range(c):
            if not arr[i][j]:
                continue
            down[i][j] = (down[i+1][j] if i+1 < r else 0) + 1

    def get_res(a, b):
        b = min(a, b)
        if b < 2:
            return 0
        lo, hi = 2, a
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid <= b and (mid * 2) <= a:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
#        print(f'a, b, ans  {a, b, ans - 1}')
        return ans - 1 if ans else 0

    ans = 0
    for i in range(r):
        for j in range(c):
            # long side from up
            ans += get_res(up[i][j], left[i][j])
            ans += get_res(up[i][j], right[i][j])
            # Long side from down
            ans += get_res(down[i][j], left[i][j])
            ans += get_res(down[i][j], right[i][j])
            # Long side left
            ans += get_res(left[i][j], up[i][j])
            ans += get_res(left[i][j], down[i][j])
            # Long side right
            ans += get_res(right[i][j], up[i][j])
            ans += get_res(right[i][j], down[i][j])
    return ans


for tt in range(1, T+1):
    r, c = map(int, input().split())
    arr = []
    for _ in range(r):
        arr.append(list(map(int, input().split())))

    print(f'Case #{tt}: {calc(arr, r, c)}')

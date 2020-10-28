# from collections import defaultdict, deque
# from math import ceil
# from sys import setrecursionlimit
import io, os


# setrecursionlimit(300000)
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

T = int(input())

for tt in range(T):
    n, m = map(int, input().split())
    
    rows = []
    row_begin = {}

    for i in range(n):
        rows.append(list(map(int, input().split())))
        row_begin[rows[-1][0]] = i

    ans = [[] * m for _ in range(n)]
    built = False

    for i in range(m):
        arr = list(map(int, input().split()))
        if built:
            continue
        if arr[0] in row_begin:
            for ii, cv in enumerate(arr):
                ans[ii] = rows[row_begin[cv]]
                built = True

    for r in ans:
        print(*r)


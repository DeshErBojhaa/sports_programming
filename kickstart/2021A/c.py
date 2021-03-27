from heapq import heappop, heappush
T = int(input())

def do(arr, r, c):
    ans = 0
    max_heap = []
    for i, row in enumerate(arr):
        for j, v in enumerate(row):
            heappush(max_heap, [-v, i, j])

    while max_heap:
        h, i, j = heappop(max_heap)
        h = -1 * h
        for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if not 0 <= ni < r or not 0 <= nj < c:
                continue
            if h - arr[ni][nj] <= 1:
                continue
            ans += (h - arr[ni][nj] - 1)
            arr[ni][nj] = h - 1
            heappush(max_heap, [-(h-1), ni, nj])
    return ans


for tt in range(1, T+1):
    r, c = map(int, input().split())
    arr = []
    for _ in range(r):
        arr.append(list(map(int, input().split())))
    ans = do(arr, r, c)
    print('Case #{}: {}'.format(tt, ans))

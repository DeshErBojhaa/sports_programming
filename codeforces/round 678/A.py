T = int(input())

for tt in range(1, T+1):
    N, S = map(int, input().split())
    arr = map(int, input().split())

    if sum(arr) == S:
        print('YES')
        continue
    print('NO')

T = int(input())

for tt in range(1, T+1):
    N = int(input())
    ans = [[0] * N for _ in range(N)]

    # ans[0][0] = ans[0][1] = ans[1][0] = ans[1][1] = 1
    for i in range(0, N-1, 2):
        ans[i][i] = ans[i][i+1] = ans[i+1][i] = ans[i+1][i+1] = 1

    if N % 2:
        ans[-1][0] = ans[-1][-1] = ans[0][-1] = 1

    for r in ans:
        print(*r)


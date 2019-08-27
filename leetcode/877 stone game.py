def call(arr):
    n = len(arr)
    dp = [[0] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = arr[i]

    for j in range(1, n):
        for i in range(n - j):
            dp[i][i+j] = max(arr[i] - dp[i+1][i+j], arr[i+j] - dp[i][i + j -1])

    return dp[0][n-1]

if __name__ == "__main__":
    x = call([5, 3, 4, 5])
    print(x)

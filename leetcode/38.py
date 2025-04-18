class Solution:

    def rle(s):
        cnt = 0
        last = None
        ans = ''
        for ch in s:
            if ch != last and last is not None:
                ans += f'{cnt}{last}'
                cnt = 0
            cnt += 1
            last = ch
        ans += f'{cnt}{last}'
        return ans

    s = "1"
    dp = [None] * 32
    dp[0] = s
    for i in range(1, 31):
        last = dp[i-1]
        ans = rle(last)
        dp[i] = ans
    # print(dp)
    def countAndSay(self, n: int) -> str:
        return Solution.dp[n-1]

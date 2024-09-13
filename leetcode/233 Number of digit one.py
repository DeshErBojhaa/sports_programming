class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        n = len(s)

        @cache
        def rec(cur, cnt, go_wild):
            if cur == n:
                return cnt
            digit = int(s[cur])
            limit = 9 if go_wild else digit
            ans = 0
            for i in range(limit+1):
                ans += rec(cur+1, cnt + + (i == 1), go_wild or i < digit)
            return ans

        return rec(0, 0, False)

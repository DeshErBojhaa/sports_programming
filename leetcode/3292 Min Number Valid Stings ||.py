class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        def kmp(w):
            s = w + '#' + target
            par = [0] * len(s)
            k = 0
            for i in range(1, len(s)):
                while k and s[k] != s[i]:
                    k = par[k-1]
                k += (s[k] == s[i])
                par[i] = k
            par = par[len(w)+ 1:]
            return par

        dp = [0] * n
        for w in words:
            par_ = kmp(w)
            for i, v in enumerate(par_):
                dp[i] = max(dp[i], v)

        idx = n - 1
        ans = 0
        while idx >= 0:
            if dp[idx] <= 0:
                return -1
            ans += 1
            idx -= dp[idx]
        return ans

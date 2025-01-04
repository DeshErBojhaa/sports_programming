class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        c, nc, ans = Counter(s), Counter(), 0
        seen = set()
        for ch in s[:-1]:
            for k in nc:
                l = nc[k]
                r = c[k] - l - (ch == k)
                if k + ch + k in seen:
                    continue
                ans += min(l, r, 1)
                seen.add(k + ch + k)
            nc[ch] += 1
        return ans

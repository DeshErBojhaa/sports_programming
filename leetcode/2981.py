class Solution:
    def maximumLength(self, s: str) -> int:
        def kmp(a, b):
            n = len(a)
            s = a + '#' + b
            k, par = 0, [0] * len(s)
            for i, ch in enumerate(s[1:], 1):
                while k and ch != s[k]:
                    k = par[k-1]
                k += ch == s[k]
                par[i] = k
            cnt = sum([1 for x in par if x >= n])
            if cnt > 2:
                return n
            return -1
        
        ans = -1
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                if len(set(s[i:j])) > 1:
                    continue
                ans = max(ans, kmp(s[i:j], s))
        return ans

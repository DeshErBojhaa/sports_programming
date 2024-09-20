class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        def kmp(s):
            n = len(s)
            s = s + '#' + s[::-1]
            N = len(s)
            k, par = 0, [0] * N
            for i, ch in enumerate(s[1:], 1):
                while k and s[k] != s[i]:
                    k = par[k-1]
                k += int(s[k] == s[i])
                par[i] = k
            return par[-1]
        
        x = kmp(s)
        
        return s[x:][::-1] + s

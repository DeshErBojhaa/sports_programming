class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        nxt = {a:b for a, b in zip('abcdefghijklmnopqrstuvwxyz', 'bcdefghijklmnopqrstuvwxyza')}

        l, n = 0, len(str2)
        for i, ch in enumerate(str1):
            if ch == str2[l] or nxt[ch] == str2[l]:
                l += 1
            if l == n:
                return True
        return False

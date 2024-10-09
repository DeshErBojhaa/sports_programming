class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l, r = 0, 0
        for ch in s:
            if ch == '(':
                l += 1
                continue
            if l:
                l -= 1
            else:
                r += 1
        return l + r

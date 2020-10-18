def minAddToMakeValid(self, S: str) -> int:
        l, r, ans = 0, 0, 0
        for s in S:
            if s == '(':
                l += 1
            else:
                if l:
                    l -= 1
                else:
                    ans += 1
        return ans + l

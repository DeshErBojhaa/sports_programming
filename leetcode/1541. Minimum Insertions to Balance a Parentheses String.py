# 1541. Minimum Insertions to Balance a Parentheses String
class Solution:
    def minInsertions(self, s: str) -> int:
        ans, lp, rp = 0,0,0
        for p in s:
            if p == '(':
                if rp == 1:
                    ans += 1  # Insert one )
                    rp = 0    # Now we have 2 )), match them with prev ( or insert one (
                    ans += int(lp == 0)
                    lp = max(0, lp -1)
                lp += 1
                continue
            if p == ')':
                rp += 1
                if rp == 2:
                    ans += int(lp == 0)  # No ( virtually add one
                    lp = max(0, lp -1)
                    rp = 0
        
        if lp > 0:
            ans += (2 * lp) - rp
        elif rp > 0:
            ans += 2
        return ans

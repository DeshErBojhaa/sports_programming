from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        left_brace_min, left_brace_max = 0, 0
        
        for c in s:
            if c == '(':
                left_brace_min += 1
                left_brace_max += 1
            elif c == ')':
                left_brace_min -= 1
                left_brace_max -= 1
            else:
                left_brace_min -= 1
                left_brace_max += 1
            if left_brace_max < 0:
                return False
            left_brace_min = max(0, left_brace_min)
        
        return left_brace_min == 0

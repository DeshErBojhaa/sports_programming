# 1544. Make The String Great
from collections import deque
class Solution:
    def makeGood(self, s: str) -> str:
        if len(s)  < 2:
            return s
        changed = True
        
        while changed:
            new_s, changed = '', False
            
            for i in range(len(s)-1):
                if s[i].islower() and s[i+1].isupper() and s[i].lower() == s[i+1].lower():
                    new_s = s[:i] + s[i+2:]
                    changed = True
                if s[i].isupper() and s[i+1].islower() and s[i].lower() == s[i+1].lower():
                    new_s = s[:i] + s[i+2:]
                    changed = True
                
                if changed:
                    s = new_s
                    break
        return s

from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stot, ttos = {}, {}
        s = list(s)
        
        for i in range(len(s)):
            if s[i] in stot or t[i] in ttos:
                if stot.get(s[i], None) != t[i] or ttos.get(t[i], None) != s[i]:
                    return False
            else:
                stot[s[i]] = t[i]
                ttos[t[i]] = s[i]
            
            s[i] = t[i]
        return ''.join(s) == t

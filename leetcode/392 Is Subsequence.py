class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        inds, indt = 0, 0
        Ns, Nt = len(s), len(t)
        
        while inds < Ns and indt < Nt:
            if s[inds] == t[indt]:
                inds += 1
            indt += 1
            if inds == Ns:
                return True
        
        return inds == Ns

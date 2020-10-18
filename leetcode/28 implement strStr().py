class Solution:
    def strStr(self, h: str, n: str) -> int:
        if not n:
            return 0
        nl = len(n)
        hl = len(h)
        
        for i in range(hl-nl+1):
            if h[i] != n[0]:
                continue
            
            if h[i: i+nl] == n:
                return i
        return -1

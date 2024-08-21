class Solution:
    def minimumMoney(self, T: List[List[int]]) -> int:
        a, mx = 0, 0
        for c, b in T:
            a += max(0, c - b)
            mx = max(mx, min(b, c))
            
        return a + mx
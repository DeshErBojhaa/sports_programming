class Solution:
    def minCost(self, A: list[int], B: list[int]) -> int:
        if len(A) != len(B):
            return -1
        
        ans = 0
        c, C = Counter(A), Counter(A + B)
        for k, v in C.items():
            if v % 2:
                return -1
            target = v // 2
            ans += abs(c[k] - target)
        
        return ans//2

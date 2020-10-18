# 1536. Minimum Swaps to Arrange a Binary Grid
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        z = [0] * N
        for i, v in enumerate(grid):
            idx = N-1
            while idx > -1 and v[idx] == 0:
                z[i] += 1
                idx -= 1
        
        ans = 0
        for i in range(N-1):
            req = N - 1- i
            for j in range(i, N, 1):
                if z[j] >= req:
                    ans += j - i
                    x = z.pop(j)
                    z.insert(i, x)
                    break
            else:
                return -1
        
        return ans

# 1504. Count Submatrices With All Ones
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        ans, dp = 0, [[0] * C for _ in range(R)]
        
        for i in range(R):
            for j in range(C-1,-1,-1):
                if not mat[i][j]:
                    continue
                if j == C-1:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i][j+1] + 1

        for i in range(R):
            for j in range(C):
                if not mat[i][j]:
                    continue
                width = float('inf')
                for k in range(i, R):
                    width = min(width, dp[k][j])
                    ans += width
        return ans
                
                
# [[1,0,1],[1,1,0],[1,1,0]]
# [[1,1,1,1,1,1]]
# [[1,0,1],[0,1,0],[1,0,1]]
# [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
# [[1,0,1,1,1,1,0],[1,1,1,1,0,1,1],[0,0,0,0,1,1,1],[0,1,0,1,1,1,1],[0,0,1,0,1,1,1]]
# [[1,0,1,1,1,1,0],[1,1,1,1,0,1,1]]
# [[0,0,0,0,1,1,1],[0,1,0,1,1,1,1],[0,0,1,0,1,1,1]]
# [[0,1,1,1],[1,1,0,1],[1,0,1,1]]

# 110
# 011
# 111
# 111

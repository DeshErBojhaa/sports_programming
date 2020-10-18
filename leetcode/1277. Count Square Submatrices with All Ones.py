# 1277. Count Square Submatrices with All Ones
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                if i and j:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                ans += matrix[i][j]
        return ans
